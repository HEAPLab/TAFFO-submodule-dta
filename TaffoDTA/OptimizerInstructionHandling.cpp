#include <llvm/IR/Intrinsics.h>
#include <llvm/Analysis/MemorySSA.h>
#include "Optimizer.h"
#include "llvm/Support/Debug.h"
#include "MemSSAUtils.hpp"

#include "llvm/IR/InstIterator.h"


using namespace tuner;
using namespace mdutils;
using namespace llvm;


void Optimizer::handleAlloca(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {
    if (!valueInfo) {
        dbgs() << "No value info, skipping...\n";
        return;
    }

    if (!valueInfo->metadata) {
        dbgs() << "No value metadata, skipping...\n";
        return;
    }

    auto *alloca = dyn_cast<AllocaInst>(instruction);


    if (!alloca->getAllocatedType()->isPointerTy()) {
        if (valueInfo->metadata->getKind() == MDInfo::K_Field) {
            dbgs() << " ^ This is a real field\n";
            auto fieldInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfo->metadata);
            if (!fieldInfo) {
                dbgs() << "Not enough information. Bailing out.\n\n";
                return;
            }

            auto fptype = dynamic_ptr_cast_or_null<FPType>(fieldInfo->IType);
            if (!fptype) {
                dbgs() << "No fixed point info associated. Bailing out.\n";
                return;
            }
            auto info = allocateNewVariableForValue(alloca, fptype, fieldInfo->IRange, fieldInfo->IError,
                                                    alloca->getFunction()->getName(),
                                                    false);
            saveInfoForValue(alloca, make_shared<OptimizerPointerInfo>(info));
        } else if (valueInfo->metadata->getKind() == MDInfo::K_Struct) {
            dbgs() << " ^ This is a real structure\n";

            auto fieldInfo = dynamic_ptr_cast_or_null<StructInfo>(valueInfo->metadata);
            if (!fieldInfo) {
                dbgs() << "No struct info. Bailing out.\n";
                return;
            }

            auto optInfo = loadStructInfo(alloca, fieldInfo, "");
            saveInfoForValue(alloca, optInfo);

        } else {
            llvm_unreachable("Unknown metadata!");
        }


    } else {
        dbgs() << " ^ this is a pointer, skipping as it is unsupported at the moment.\n";
        return;
    }


}


void Optimizer::handleLoad(Instruction *instruction, const shared_ptr<ValueInfo> &valueInfo) {
    if (!valueInfo) {
        dbgs() << "No value info, skipping...\n";
        return;
    }

    auto *load = dyn_cast<LoadInst>(instruction);
    auto loaded = load->getPointerOperand();
    shared_ptr<OptimizerInfo> infos = getInfoOfValue(loaded);

    auto pinfos = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(infos);
    if (!pinfos) {
        emitError("Loaded a variable with no information attached, or attached info not a Pointer type!");
        return;
    }


    if (load->getType()->isFloatingPointTy()) {
        auto sinfos = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(pinfos->getOptInfo());
        if (!sinfos) {
            emitError("Loaded a variable with no information attached...");
            return;
        }
        //We are copying the infos, still using variable types and all, the only problem is the enob

        model.insertComment("Restriction for new enob [LOAD]", 1);
        string newEnobVariable = sinfos->getBaseEnobVariable();
        newEnobVariable.append("_memphi_");
        newEnobVariable.append(load->getFunction()->getName());
        newEnobVariable.append("_");
        newEnobVariable.append(load->getName());
        std::replace(newEnobVariable.begin(), newEnobVariable.end(), '.', '_');
        dbgs() << "New enob for load: " << newEnobVariable << "\n";
        model.createVariable(newEnobVariable, -BIG_NUMBER, BIG_NUMBER);

        auto constraint = vector<pair<string, double>>();
        constraint.clear();
        constraint.push_back(make_pair(newEnobVariable, 1.0));
        constraint.push_back(make_pair(sinfos->getBaseEnobVariable(), -1.0));
        model.insertLinearConstraint(constraint, Model::LE, 0,
                                     "Enob constraint, new enob at most original variable enob");

        auto a = make_shared<OptimizerScalarInfo>(sinfos->getBaseName(),
                                                  sinfos->getMinBits(),
                                                  sinfos->getMaxBits(), sinfos->getTotalBits(),
                                                  sinfos->isSigned,
                                                  *sinfos->getRange(), newEnobVariable);



        //We are loading a floating point, which means we have it's value in a register.
        //As we cannot cast anything during a load, the register will use the very same variable

        //Running MemorySSA to find Values from which the load can actually load
        MemorySSA &memssa = tuner->getAnalysis<MemorySSAWrapperPass>(*load->getFunction()).getMSSA();
        taffo::MemSSAUtils memssa_utils(memssa);
        SmallVectorImpl<Value *> &def_vals = memssa_utils.getDefiningValues(load);
        def_vals.push_back(load->getPointerOperand());

        assert(def_vals.size() > 0 && "Loading a not defined value?");

        /*This is the same as for phi nodes. In particular, when using the MemSSA usually the most important
         * instructions that defines a values are store. In particular, when looking at a store, we can use the enob
         * given to that store to understand the enob propagation. This enob will not change during the computation as
         * usually every store is only touched once, differently from the */

        saveInfoForValue(instruction, a);

        constraint.clear();

        vector<bool> toSkip(def_vals.size());

        for (unsigned index = 0; index < def_vals.size(); index++) {
            toSkip[index] = true;
            Value *op = def_vals[index];
            if (!op) {
                dbgs() << "Skipping null value!\n";
                continue;
            }

            auto store = dyn_cast_or_null<StoreInst>(op);
            if (!store) {
                //We skip the variable if it is not a store
                dbgs() << "[INFO] Skipping ";
                op->print(dbgs());
                dbgs() << " as it is NOT a store!\n";
                continue;
            }
            if (auto info = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(getInfoOfValue(op))) {
                if (info->doesReferToConstant()) {
                    //We skip the variable if it is a constant
                    dbgs() << "[INFO] Skipping ";
                    op->print(dbgs());
                    dbgs() << " as it is a constant!\n";
                    continue;
                }
            }

            string enob_selection = getEnobActivationVariable(instruction, index);
            dbgs() << "Declaring " << enob_selection << "for enob...\n";
            model.createVariable(enob_selection, 0, 1);
            constraint.push_back(make_pair(enob_selection, 1.0));
            toSkip[index] = false;
        }

        if (constraint.size() > 0) {
            model.insertLinearConstraint(constraint, Model::EQ, 1, "Enob: one selected constraint");
        } else {
            dbgs() << "[INFO] All constants memPhi node, nothing to do!!!\n";
            //return;
        }


        int missing = 0;

        for (unsigned index = 0; index < def_vals.size(); index++) {
            dbgs() << "[memPhi] Handlign operator " << index << "...\n";
            Value *op = def_vals[index];

            if (toSkip[index]) {
                dbgs() << "Need to skip this...\n";
                continue;
            }

            if (auto info = getInfoOfValue(op)) {
                dbgs() << "[memPhi] We have infos, treating as usual.\n";
                //because yes, integrity checks....
                openMemLoop(load, op);
                closeMemLoop(load, op);
            } else {
                dbgs() << "[memPhi] No value available, inserting in delayed set.\n";
                openMemLoop(load, op);
                missing++;
            }
        }


        dbgs() << "For this load, reusing variable [" << sinfos->getBaseName() << "]\n";

    } else if (load->getType()->isPointerTy()) {
        dbgs() << "Handling load of a pointer...\n";
        //Unvrap the pointer, hoping that it is pointing to something
        auto info = pinfos->getOptInfo();
        if (info->getKind() != OptimizerInfo::K_Pointer) {
            emitError("Expecting a pointer info when unwrapping a pointer...");
            return;
        }
        dbgs() << "The final register will have as info: " << info->toString() << "\n";
        saveInfoForValue(instruction, info);

    } else {
        dbgs() << "Loading a non floating point value, ingoring.\n";
        return;
    }


}


void Optimizer::handleStore(Instruction *instruction, const shared_ptr<ValueInfo> &valueInfo) {
    auto *store = dyn_cast<StoreInst>(instruction);

    if (!store) {
        llvm_unreachable("Instruction mismatch!");
    }

    auto opWhereToStore = store->getPointerOperand();
    auto opRegister = store->getValueOperand();
    auto info2 = getInfoOfValue(opRegister);

    if (opRegister->getType()->isFloatingPointTy()) {
        auto info1 = getInfoOfValue(opWhereToStore);
        if (!info1 || !info2) {
            dbgs() << "One of the two values does not have info, ignoring...\n";
            return;
        }

        auto info_pointer_t = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(info1);
        if (!info_pointer_t) {
            emitError("No info on pointer value!");
            return;
        }

        auto info_variable_oeig_t = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info2);
        if (!info_variable_oeig_t) {
            emitError("No info on register value!");
            return;
        }

        dbgs() << "Storing " << info2->toString() << " into " << info1->toString() << "\n";


        auto info_pointer = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info_pointer_t->getOptInfo());

        shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableWithCastCost(opRegister, instruction);

        insertTypeEqualityConstraint(info_pointer, variable, true);


        bool isConstant;

        if (!info_variable_oeig_t->doesReferToConstant()) {
            isConstant = false;
            //We do this only if storing a real result from a computation, if it comes from a constant we do not override the enob.
            model.insertComment("Restriction for new enob [STORE]", 2);
            string newEnobVariable = info_pointer->getRealEnobVariable();
            newEnobVariable.append("_storeENOB");
            model.createVariable(newEnobVariable, -BIG_NUMBER, BIG_NUMBER);
            info_pointer->overrideEnob(newEnobVariable);

            //We force the enob back to the variable type, just in case!
            auto constraint = vector<pair<string, double>>();
            int ENOBfloat = getENOBFromRange(info_pointer->getRange(), FloatType::Float_float);
            int ENOBdouble = getENOBFromRange(info_pointer->getRange(), FloatType::Float_double);

            constraint.clear();
            constraint.push_back(make_pair(info_pointer->getRealEnobVariable(), 1.0));
            constraint.push_back(make_pair(info_pointer->getFractBitsVariable(), -1.0));
            constraint.push_back(make_pair(info_pointer->getFixedSelectedVariable(), BIG_NUMBER));
            model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER, "Enob constraint for fix");

            //Enob constraints float
            constraint.clear();
            constraint.push_back(make_pair(info_pointer->getRealEnobVariable(), 1.0));
            constraint.push_back(make_pair(info_pointer->getFloatSelectedVariable(), BIG_NUMBER));
            model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER + ENOBfloat, "Enob constraint for float");

            //Enob constraints float
            constraint.clear();
            constraint.push_back(make_pair(info_pointer->getRealEnobVariable(), 1.0));
            constraint.push_back(make_pair(info_pointer->getDoubleSelectedVariable(), BIG_NUMBER));
            model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER + ENOBdouble, "Enob constraint for double");


            constraint.clear();
            constraint.push_back(make_pair(info_pointer->getRealEnobVariable(), 1.0));
            constraint.push_back(make_pair(info_variable_oeig_t->getRealEnobVariable(), -1.0));
            model.insertLinearConstraint(constraint, Model::LE, 0, "Enob constraint ENOB propagation in load/store");
        } else {
            dbgs() << "[INFO] The value to store is a constant, not inserting it as may cause problems...\n";
            model.insertComment("Storing constant, no new enob.", 1);
            isConstant = true;
        }


        //We save the infos so we should retrieve them more quickly when using MemSSA
        //We save the ENOB of the stored variable that is the correct one to use
        auto a = make_shared<OptimizerScalarInfo>(info_variable_oeig_t->getBaseName(),
                                                  info_variable_oeig_t->getMinBits(),
                                                  info_pointer->getMaxBits(), info_pointer->getTotalBits(),
                                                  info_pointer->isSigned,
                                                  *info_pointer->getRange(), info_pointer->getOverridedEnob());
        a->setReferToConstant(isConstant);

        saveInfoForValue(instruction, a);


    } else if (opRegister->getType()->isPointerTy()) {
        //Storing a pointer. In the value there should be a pointer already, and the value where to store is, in fact,
        //a pointer to a pointer
        dbgs() << "The register is: ";
        opRegister->print(dbgs());
        dbgs() << "\n";
        dbgs() << "Storing a pointer...\n";
        if (!info2) {
            dbgs() << "Skipping, as the value to save does not have any info...\n";
            return;
        }

        if (info2->getKind() != OptimizerInfo::K_Pointer) {
            emitError("Storing to a pointer a value that is not a pointer, ouch!");
            return;
        }

        //We wrap the info with a dereference information
        //When a double load occours, for example, this will be handled succesfully, hopefully!
        saveInfoForPointer(opWhereToStore, make_shared<OptimizerPointerInfo>(info2));

    } else {
        dbgs() << "Storing a non-floating point, skipping...\n";
        return;
    }


}


void Optimizer::handleFPPrecisionShift(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {

    auto operand = instruction->getOperand(0); //The argument to be casted

    auto info = getInfoOfValue(operand);
    auto sinfos = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
    if (!sinfos) {
        dbgs() << "No info for the operand, ignoring...\n";
        return;
    }

    //Copy information as for us is like a NOP
    saveInfoForValue(instruction, make_shared<OptimizerScalarInfo>(sinfos->getBaseName(),
                                                                   sinfos->getMinBits(),
                                                                   sinfos->getMaxBits(), sinfos->getTotalBits(),
                                                                   sinfos->isSigned, *sinfos->getRange(),
                                                                   sinfos->getOverridedEnob()));

    dbgs() << "For this fpext/fptrunc, reusing variable" << sinfos->getBaseName() << "\n";


}

void
Optimizer::handlePhi(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {
    auto *phi = dyn_cast<PHINode>(instruction);

    if (!phi->getType()->isFloatingPointTy()) {
        dbgs() << "Phi node with non float value, skipping...\n";
        return;
    }

    //We can have two scenarios here: we can have value that came from a precedent basic block, and therefore we have
    //already infos on it, or from a successor basic block, in this case we cannot have info about the value (ex. loops)

    //In the former case we proceed as usual, in the latter case, we need to insert the value in a special set that will
    //be monitored in case of insertions. In that case, the phi loop can be closed.

    //We treat phi as normal assignment, without looking at the real "backend" implementation. This may be quite different
    //from the real execution, but the overall meaning is the same.



    auto *phi_n = dyn_cast<llvm::PHINode>(phi);
    if (!phi_n) {
        llvm_unreachable("Could not convert Phi instruction to PHINode");
    }
    if (phi_n->getNumIncomingValues() < 1) {
        //This phi node has no value, really?
        llvm_unreachable("Why on earth there is a Phi instruction with no incoming values?");
    }

    auto fieldInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfo->metadata);
    if (!fieldInfo) {
        dbgs() << "Not enough information. Bailing out.\n\n";
        return;
    }

    if (!fieldInfo->IRange) {
        dbgs() << "Not Range information. Bailing out.\n\n";
        return;
    }

    auto fptype = dynamic_ptr_cast_or_null<FPType>(fieldInfo->IType);
    if (!fptype) {
        dbgs() << "No fixed point info associated. Bailing out.\n";
        return;
    }

    //Allocating variable for result
    shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableForValue(instruction, fptype, fieldInfo->IRange,
                                                                           fieldInfo->IError,
                                                                           instruction->getFunction()->getName());
    auto constraint = vector<pair<string, double>>();
    constraint.clear();


    for (unsigned index = 0; index < phi_n->getNumIncomingValues(); index++) {
        Value *op = phi_n->getIncomingValue(index);
        if (auto info = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(getInfoOfValue(op))) {
            if (info->doesReferToConstant()) {
                //We skip the variable if it is a constant
                dbgs() << "[INFO] Skipping ";
                op->print(dbgs());
                dbgs() << " as it is a constant!\n";
                continue;
            }
        }

        string enob_selection = getEnobActivationVariable(instruction, index);
        model.createVariable(enob_selection, 0, 1);
        constraint.push_back(make_pair(enob_selection, 1.0));
    }

    if (constraint.size() > 0) {
        model.insertLinearConstraint(constraint, Model::EQ, 1, "Enob: one selected constraint");
    } else {
        dbgs() << "[INFO] All constants phi node, nothing to do!!!\n";
        return;
    }


    int missing = 0;

    for (unsigned index = 0; index < phi_n->getNumIncomingValues(); index++) {
        dbgs() << "[Phi] Handlign operator " << index << "...\n";
        Value *op = phi_n->getIncomingValue(index);

        if (auto info = getInfoOfValue(op)) {
            if (auto info2 = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info)) {
                if (info2->doesReferToConstant()) {
                    //We skip the variable if it is a constant
                    dbgs() << "[INFO] Skipping ";
                    op->print(dbgs());
                    dbgs() << " as it is a constant!\n";
                    continue;
                }
            }


            dbgs() << "[Phi] We have infos, treating as usual.\n";
            //because yes, integrity checks....
            openPhiLoop(phi_n, op);
            closePhiLoop(phi_n, op);
        } else {
            dbgs() << "[Phi] No value available, inserting in delayed set.\n";
            openPhiLoop(phi_n, op);
            missing++;
        }
    }

    dbgs() << "[Phi] Elaboration concluded. Missing " << missing << " values.\n";

    phiWatcher.dumpState();


}


void Optimizer::handleCastInstruction(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {
    dbgs() << "Handling casting instruction...\n";


    if (isa<BitCastInst>(instruction)) {
        dbgs() << "[Warning] Bitcasting not supported for model generation.";
        return;
    }

    if (isa<FPExtInst>(instruction) ||
        isa<FPTruncInst>(instruction)) {
        handleFPPrecisionShift(instruction, valueInfo);
        return;
    }

    if (isa<TruncInst>(instruction) ||
        isa<ZExtInst>(instruction) ||
        isa<SExtInst>(instruction)) {
        dbgs() << "Cast between integers, skipping...\n";
        return;
    }

    if (isa<UIToFPInst>(instruction) ||
        isa<SIToFPInst>(instruction)) {

        auto fieldInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfo->metadata);
        if (!fieldInfo) {
            dbgs() << "Not enough information. Bailing out.\n\n";

            if (valueInfo->metadata) {
                dbgs() << "WTF metadata has a value but it is not an input info...\n\n";
            } else {
                dbgs() << "Metadata is really null.\n";
            }
            return;
        }

        auto fptype = dynamic_ptr_cast_or_null<FPType>(fieldInfo->IType);
        if (!fptype) {
            dbgs() << "No fixed point info associated. Bailing out.\n";
            return;
        }


        shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableForValue(instruction, fptype, fieldInfo->IRange,
                                                                               fieldInfo->IError,
                                                                               instruction->getFunction()->getName());

        //Limiting the ENOB as coming from an integer we can have an error at min of 1
        //Look that here we have the original program, so these instruction are not related to fixed point implementation!
        auto constraint = vector<pair<string, double>>();
        constraint.clear();
        constraint.push_back(make_pair(variable->getRealEnobVariable(), 1.0));
        model.insertLinearConstraint(constraint, Model::LE, 1, "Limiting Enob for integer to float conversion");
        return;
    }

    if (isa<FPToSIInst>(instruction) ||
        isa<FPToUIInst>(instruction)) {
        dbgs() << "Casting Floating point to integer, no costs introduced.\n";
        return;
    }

    if (isa<IntToPtrInst>(instruction) ||
        isa<PtrToIntInst>(instruction)) {
        dbgs() << "Black magic with pointers is happening. We do not want to awake the dragon, rigth?\n";
        return;
    }


    llvm_unreachable("Did I really forgot something?");
}


void Optimizer::handleGEPInstr(llvm::Instruction *gep, shared_ptr<ValueInfo> valueInfo) {
    const llvm::GetElementPtrInst *gep_i = dyn_cast<llvm::GetElementPtrInst>(gep);
    dbgs() << "Handling GEP. \n";

    Value *operand = gep_i->getOperand(0);
    dbgs() << "Operand: ";
    operand->print(dbgs());
    dbgs() << "\n";

    std::vector<unsigned> offset;

    if (extractGEPOffset(gep_i->getSourceElementType(),
                         iterator_range<User::const_op_iterator>(gep_i->idx_begin(),
                                                                 gep_i->idx_end()),
                         offset)) {
        dbgs() << "Exctracted offset: [";
        for (int i = 0; i < offset.size(); i++) {
            dbgs() << offset[i] << ", ";
        }
        dbgs() << "]\n";
        //When we load an address from a "thing" we need to store a reference to it in order to successfully update the error
        auto optInfo_t = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(getInfoOfValue(operand));
        if (!optInfo_t) {
            dbgs() << "Probably trying to access a non float element, bailing out.\n";
            return;
        }


        auto optInfo = optInfo_t->getOptInfo();
        if (!optInfo) {
            dbgs() << "Probably trying to access a non float element, bailing out.\n";
            return;
        }


        //This will only contain displacements for struct fields...
        for (int i = 0; i < offset.size(); i++) {
            auto structInfo = dynamic_ptr_cast_or_null<OptimizerStructInfo>(optInfo);
            if (!structInfo) {
                dbgs() << "Probably trying to access a non float element, bailing out.\n";
                return;
            }

            optInfo = structInfo->getField(offset[i]);
        }


        dbgs() << "Infos associated: " << optInfo->toString() << "\n";
        saveInfoForValue(gep, make_shared<OptimizerPointerInfo>(optInfo));
        return;
    }
    emitError("Cannot extract GEPOffset!");
}

bool Optimizer::extractGEPOffset(const llvm::Type *source_element_type,
                                 const llvm::iterator_range<llvm::User::const_op_iterator> indices,
                                 std::vector<unsigned> &offset) {
    assert(source_element_type != nullptr);
    (dbgs() << "indices: ");
    for (auto idx_it = indices.begin() + 1; // skip first index
         idx_it != indices.end(); ++idx_it) {

        const llvm::ConstantInt *int_i = dyn_cast<llvm::ConstantInt>(*idx_it);
        if (int_i) {
            int n = static_cast<int>(int_i->getSExtValue());
            if (isa<SequentialType>(source_element_type)) {
                //This is needed to skip the array element in array of structures
                //In facts, we treats arrays as "scalar" things, so we just do not want to deal with them
                source_element_type = cast<SequentialType>(source_element_type)->getTypeAtIndex(n);
                dbgs() << "continuing...   ";
                continue;
            }


            offset.push_back(n);
            /*source_element_type =
                    cast<StructType>(source_element_type)->getTypeAtIndex(n);*/
            (dbgs() << n << " ");
        } else {
            //We can skip only if is a sequential i.e. we are accessing an index of an array
            if (!isa<SequentialType>(source_element_type)) {
                emitError("Index of GEP not constant");
                return false;
            }
        }
    }
    (dbgs() << "--end indices\n");
    return true;
}

void Optimizer::handleFCmp(Instruction *instr, shared_ptr<ValueInfo> valueInfo) {
    assert(instr->getOpcode() == llvm::Instruction::FCmp && "Operand mismatch!");

    auto op1 = instr->getOperand(0);
    auto op2 = instr->getOperand(1);


    auto info1 = getInfoOfValue(op1);
    auto info2 = getInfoOfValue(op2);

    if (!info1 || !info2) {
        dbgs() << "One of the two values does not have info, ignoring...\n";
        return;
    }

    if(auto scalar = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info1)){
        if(scalar->doesReferToConstant()){
            dbgs() << "Info1 is a constant, skipping as no further cast cost will be introduced.\n";
            return;
        }
    }

    if(auto scalar = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info2)){
        if(scalar->doesReferToConstant()){
            dbgs() << "Info2 is a constant, skipping as no further cast cost will be introduced.\n";
            return;;
        }
    }


    shared_ptr<OptimizerScalarInfo> varCast1 = allocateNewVariableWithCastCost(op1, instr);
    shared_ptr<OptimizerScalarInfo> varCast2 = allocateNewVariableWithCastCost(op2, instr);



    //The two variables must only contain the same data type, no floating point value returned.
    insertTypeEqualityConstraint(varCast1, varCast2, true);


}

void Optimizer::closePhiLoop(PHINode *phiNode, Value *requestedValue) {
    dbgs() << "Closing PhiNode reference!\n";
    auto phiInfo = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(getInfoOfValue(phiNode));
    auto destInfo = allocateNewVariableWithCastCost(requestedValue, phiNode);

    assert(phiInfo && "phiInfo not available!");
    assert(destInfo && "destInfo not available!");

    string enob_var;

    for (int index = 0; index < phiNode->getNumIncomingValues(); index++) {
        if (phiNode->getIncomingValue(index) == requestedValue) {
            enob_var = getEnobActivationVariable(phiNode, index);
            break;
        }
    }

    assert(!enob_var.empty() && "Enob var not found!");

    insertTypeEqualityConstraint(phiInfo, destInfo, true);

    auto info1 = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(getInfoOfValue(requestedValue));


    auto constraint = vector<pair<string, double>>();
    constraint.clear();
    constraint.push_back(make_pair(phiInfo->getRealEnobVariable(), 1.0));
    constraint.push_back(make_pair(info1->getRealEnobVariable(), -1.0));
    constraint.push_back(make_pair(enob_var, BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER, "Enob: forcing phi enob");


    phiWatcher.closePhiLoop(phiNode, requestedValue);

}

void Optimizer::closeMemLoop(LoadInst *load, Value *requestedValue) {
    dbgs() << "Closing MemPhi reference!\n";
    auto phiInfo = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(getInfoOfValue(load));
    //auto destInfo = allocateNewVariableWithCastCost(requestedValue, load);

    assert(phiInfo && "phiInfo not available!");
    //assert(destInfo && "destInfo not available!");

    string enob_var;

    MemorySSA &memssa = tuner->getAnalysis<MemorySSAWrapperPass>(*load->getFunction()).getMSSA();
    taffo::MemSSAUtils memssa_utils(memssa);
    SmallVectorImpl<Value *> &def_vals = memssa_utils.getDefiningValues(load);
    def_vals.push_back(load->getPointerOperand());

    for (int index = 0; index < def_vals.size(); index++) {
        if (def_vals[index] == requestedValue) {
            enob_var = getEnobActivationVariable(load, index);
            break;
        }
    }

    assert(!enob_var.empty() && "Enob var not found!");

    //as this is a load, it is implicit that the type is equal!
    //insertTypeEqualityConstraint(phiInfo, destInfo, true);

    auto info1 = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(getInfoOfValue(requestedValue));
    assert(info1 && "No info for the just saved value!");

    model.insertComment("Closing MEM phi loop...", 3);
    auto constraint = vector<pair<string, double>>();
    constraint.clear();
    constraint.push_back(make_pair(phiInfo->getRealEnobVariable(), 1.0));
    constraint.push_back(make_pair(info1->getRealEnobVariable(), -1.0));
    constraint.push_back(make_pair(enob_var, BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER, "Enob: forcing MEM phi enob");


    memWatcher.closePhiLoop(load, requestedValue);

}

void Optimizer::openPhiLoop(PHINode *phiNode, Value *value) {
    phiWatcher.openPhiLoop(phiNode, value);
}

void Optimizer::openMemLoop(LoadInst *load, Value *value) {
    memWatcher.openPhiLoop(load, value);
}

void Optimizer::handleCall(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {
    const auto *call_i = dyn_cast<CallBase>(instruction);
    if (!call_i) {
        llvm_unreachable("Cannot cast a call instruction to llvm::CallBase");
        return;
    }

    //FIXME: each time a call is not handled, a forced casting to the older type is needed.
    //Therefore this should be added as a cost, not simply ignored

    // fetch function name
    llvm::Function *callee = call_i->getCalledFunction();
    if (callee == nullptr) {
        emitError("Indirect calls not supported!");
        return;
    }


    const std::string calledFunctionName = callee->getName();
    dbgs() << ("We are calling " + calledFunctionName + "\n");


    auto function = known_functions.find(calledFunctionName);
    if (function == known_functions.end()) {
        const auto intrinsicsID = callee->getIntrinsicID();
        if (intrinsicsID != llvm::Intrinsic::not_intrinsic) {
            switch (intrinsicsID) {
                //TODO: implement the rest of the libc...
                /*case llvm::Intrinsic::log2:
                case llvm::Intrinsic::sqrt:
                case llvm::Intrinsic::powi:
                case llvm::Intrinsic::sin:
                case llvm::Intrinsic::cos:
                case llvm::Intrinsic::pow:
                case llvm::Intrinsic::exp:
                case llvm::Intrinsic::exp2:
                case llvm::Intrinsic::log:
                case llvm::Intrinsic::log10:
                case llvm::Intrinsic::fma:
                case llvm::Intrinsic::fabs:
                case llvm::Intrinsic::floor:
                case llvm::Intrinsic::ceil:
                case llvm::Intrinsic::trunc:
                case llvm::Intrinsic::rint:
                case llvm::Intrinsic::nearbyint:
                case llvm::Intrinsic::round:*/
                //FIXME: we, for now, emulate the support for these intrinsic; in the real case, these calls have
                // their counterpart in all the versions, so they can be treated in some other ways

                break;
                default:
                    emitError("skipping intrinsic " + calledFunctionName);
                    return;
            }
        }
        dbgs() << "Handling external function call, we will convert all to original parameters.\n";
        handleUnknownFunction(instruction, valueInfo);
        return;
    }

    // fetch ranges of arguments
    std::list<shared_ptr<OptimizerInfo>> arg_errors;
    std::list<shared_ptr<OptimizerScalarInfo>> arg_scalar_errors;
    dbgs() << ("Arguments:\n");
    for (auto arg_it = call_i->arg_begin(); arg_it != call_i->arg_end(); ++arg_it) {
        dbgs() << "info for ";
        (*arg_it)->print(dbgs());
        dbgs() << " --> ";

        //if a variable was declared for type
        auto info = getInfoOfValue(*arg_it);
        if (!info) {
            //This is needed to resolve eventual constants in function call (I'm looking at you, LLVM)
            dbgs() << "No error for the argument!\n";
        } else {
            dbgs() << "Got this error: " << info->toString() << "\n";
        }

        //Even if is a null value, we push it!
        arg_errors.push_back(info);

        /*if (const generic_range_ptr_t arg_info = fetchInfo(*arg_it)) {*/
        //If the error is a scalar, collect it also as a scalar
        auto arg_info_scalar = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
        if (arg_info_scalar) {
            arg_scalar_errors.push_back(arg_info_scalar);
        }
        //}
        dbgs() << "\n\n";
    }
    dbgs() << ("Arguments end.\n");


    auto it = functions_still_to_visit.find(calledFunctionName);
    if (it != functions_still_to_visit.end()) {
        //We mark the called function as visited from the global queue, so we will not visit it starting from root.
        functions_still_to_visit.erase(calledFunctionName);
        dbgs() << "Function " << calledFunctionName << " marked as visited in global queue.\n";
    } else {
        emitError("Cannot find function " + calledFunctionName + " in global queue!\n");
    }

    //Allocating variable for result: all returns will have the same type, and therefore a cast, if needed
    shared_ptr<OptimizerInfo> retInfo;
    if (auto inputInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfo->metadata)) {
        auto fptype = dynamic_ptr_cast_or_null<FPType>(inputInfo->IType);
        if (fptype) {
            dbgs() << fptype->toString();
            shared_ptr<OptimizerScalarInfo> result = allocateNewVariableForValue(instruction, fptype, inputInfo->IRange,
                                                                                 inputInfo->IError,
                                                                                 instruction->getFunction()->getName());
            retInfo = result;
            dbgs() << "Allocated variable for returns.\n";
        } else {
            dbgs() << "There was an input info but no fix point associated.\n";
        }
    } else if (auto pInfo = dynamic_ptr_cast_or_null<StructInfo>(valueInfo->metadata)) {
        auto info = loadStructInfo(instruction, pInfo, "");
        saveInfoForValue(instruction, info);
        retInfo = info;
        dbgs() << "Allocated variable for struct returns (?).\n";
    } else {
        dbgs() << "No info available on return value, maybe it is not a floating point returning function.\n";
    }



    //in retInfo we now have a variable for the return value of the function. Every return should be casted against it!




    //Obviously the type should be sufficient to contain the result
    /* THIS IS A WHITELIST! USE FOR DEBUG
     * auto nm = callee->getName();
    if (!nm.equals("main") &&
        !nm.equals("_Z9bs_threadPv") &&
        !nm.equals("_Z19BlkSchlsEqEuroNoDivdddddifPdS_.3") &&
            !nm.equals("_Z19BlkSchlsEqEuroNoDivfffffifPfS_.5")&&
            !nm.equals("_Z4CNDFf.2.13")&&
            !nm.equals("CNDF.1")) {
        dbgs() << "HALTING CALLING DUE TO DEBUG REQUEST!";
        return;
    }*/



    //In this case we have no known math function.
    //We will have, when enabled, math functions. In this case these will be handled here!

    // if not a whitelisted then try to fetch it from Module
    // fetch llvm::Function
    if (function != known_functions.end()) {
        dbgs() << ("The function belongs to the current module.\n");
        // got the llvm::Function
        llvm::Function *f = function->second;

        // check for recursion
        size_t call_count = 0;
        for (size_t i = 0; i < call_stack.size(); i++) {
            if (call_stack[i] == f) {
                call_count++;
            }
        }

        //WE DO NOT SUPPORT RECURSION!
        if (call_count <= 1) {
            // Can process
            // update parameter metadata
            dbgs() << ("Processing function...\n");
            processFunction(*f, arg_errors, retInfo);
            dbgs() << "Finished processing call " << calledFunctionName << " : ";
        } else {
            emitError("Recursion NOT supported!");
            return;
        }

    } else {
        //FIXME: this branch is totally avoided as it is handled before, make the correct corrections
        //the function was not found in current module: it is undeclared
        const auto intrinsicsID = callee->getIntrinsicID();
        if (intrinsicsID == llvm::Intrinsic::not_intrinsic) {
            // TODO: handle case of external function call: element must be in original type form and result is forced to be a double
        } else {
            switch (intrinsicsID) {
                case llvm::Intrinsic::memcpy:
                    //handleMemCpyIntrinsics(call_i);
                    llvm_unreachable("Memcpy not handled atm!");
                    break;
                default:
                    emitError("skipping intrinsic " + calledFunctionName);
            }
            // TODO handle case of llvm intrinsics function call
        }
    }


    return;

}


void Optimizer::processFunction(Function &f, list<shared_ptr<OptimizerInfo>> argInfo,
                                shared_ptr<OptimizerInfo> retInfo) {
    dbgs() << "\n============ FUNCTION " << f.getName() << " ============\n";

    if (f.arg_size() != argInfo.size()) {
        llvm_unreachable("Sizes should be equal!");
    }

    auto argInfoIt = argInfo.begin();
    for (auto arg = f.arg_begin(); arg != f.arg_end(); arg++, argInfoIt++) {
        if (*argInfoIt) {
            dbgs() << "Copying info of this value.\n";
            saveInfoForValue(&(*arg), *argInfoIt);
        } else {
            dbgs() << "No info for this value.\n";
        }

    }

    //Even if null, we push this on the stack. The return will handle it hopefully
    retStack.push(retInfo);


    //As we have copy of the same function for
    for (inst_iterator iIt = inst_begin(&f), iItEnd = inst_end(&f); iIt != iItEnd; iIt++) {
        //C++ is horrible
        (*iIt).print(dbgs());
        dbgs() << "     -having-     ";
        if (!tuner->hasInfo(&(*iIt)) || !tuner->valueInfo(&(*iIt))->metadata) {
            dbgs() << "No info available.\n";
        } else {
            dbgs() << tuner->valueInfo(&(*iIt))->metadata->toString() << "\n";

            if (!tuner->valueInfo(&(*iIt))->metadata->getEnableConversion()) {
                dbgs() << "Skipping as conversion is disabled!\n";
                DisabledSkipped++;
                continue;
            }
        }


        handleInstruction(&(*iIt), tuner->valueInfo(&(*iIt)));
        dbgs() << "\n\n";
    }

    //When the analysis is completed, we remove the info from the stack, as it is no more necessary.
    retStack.pop();

}

void Optimizer::handleReturn(Instruction *instr, shared_ptr<ValueInfo> valueInfo) {
    const auto *ret_i = dyn_cast<llvm::ReturnInst>(instr);
    if (!ret_i) {
        llvm_unreachable("Could not convert Return Instruction to ReturnInstr");
        return;
    }

    llvm::Value *ret_val = ret_i->getReturnValue();

    if (!ret_val) {
        dbgs() << "Handling return void, doing nothing.\n";
        return;
    }


    //When returning, we must return the same data type used.
    //Therefore we should eventually take into account the conversion cost.
    auto regInfo = getInfoOfValue(ret_val);
    if (!regInfo) {
        dbgs() << "No info on returned value, maybe a non float return, forgetting about it.\n";
        return;
    }


    auto info = retStack.top();
    if (!info) {
        emitError("We wanted to save a result, but on the stack there is not an info available. This maybe an error!");
        return;
    }

    auto infoLinear = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
    if (!infoLinear) {
        llvm_unreachable("Structure return still not handled!");
    }

    auto allocated = allocateNewVariableWithCastCost(ret_val, instr);
    insertTypeEqualityConstraint(infoLinear, allocated, true);


}

void Optimizer::saveInfoForPointer(Value *value, shared_ptr<OptimizerPointerInfo> pointerInfo) {
    assert(value && "Value cannot be null!");
    assert(pointerInfo && "Pointer info cannot be nullptr!");

    auto info = getInfoOfValue(value);
    if (!info) {
        dbgs() << "Storing new info for the value!\n";
        saveInfoForValue(value, pointerInfo);
        return;
    }

    dbgs() << "Updating info of pointer...\n";

    //PointerInfo() -> PointerInfo() -> Value[s]
    auto info_old = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(info);
    assert(info_old && info_old->getOptInfo()->getKind() == OptimizerInfo::K_Pointer);
    info_old = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(info_old->getOptInfo());
    assert(info_old);
    //We here should have info about the pointed element
    auto info_old_pointee = info_old->getOptInfo();
    if (info_old_pointee->getKind() == OptimizerInfo::K_Pointer) {
        dbgs() << "[WARNING] not handling pointer to pointer update!\n";
        return;
    }

    //Same code but for new data
    auto info_new = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(pointerInfo);
    assert(info_new && info_new->getOptInfo()->getKind() == OptimizerInfo::K_Pointer);
    info_new = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(info_new->getOptInfo());
    assert(info_new);
    //We here should have info about the pointed element
    auto info_new_pointee = info_new->getOptInfo();
    if (info_new_pointee->getKind() == OptimizerInfo::K_Pointer) {
        dbgs() << "[WARNING] not handling pointer to pointer update (and also unpredicted state!)!\n";
        return;
    }

    if (info_old_pointee->getKind() != info_new_pointee->getKind()) {
        dbgs()
                << "[WARNING] This pointer will in a point refer to two different variable that may have different data types.\n"
                   "The results may be unpredictable, you have been warned!\n";
    }

    if (!info_old_pointee->operator==(*info_new_pointee)) {
        dbgs()
                << "[WARNING] This pointer will in a point refer to two different variable that may have different data types.\n"
                   "The results may be unpredictable, you have been warned!\n";
    }


    valueToVariableName[value] = pointerInfo;


}


void Optimizer::handleCallFromRoot(Function *f) {
    //Therefore this should be added as a cost, not simply ignored



    dbgs() << "\n============ FUNCTION FROM ROOT: " << f->getName() << " ============\n";
    const std::string calledFunctionName = f->getName();
    dbgs() << ("We are calling " + calledFunctionName + " from root\n");


    auto function = known_functions.find(calledFunctionName);
    if (function == known_functions.end()) {
        dbgs() << "Calling an external function, UNSUPPORTED at the moment.\n";
        return;
    }


    //In teoria non dobbiamo mai pushare variabili per quanto riguarda una chiamata da root
    //Infatti, la chiamata da root implica la compatibilità con codice esterno che si aspetta che non vengano modificate
    //le call ad altri tipi. Per lo stesso motivo non serve nulla per il valore di ritorno.
    /*
    // fetch ranges of arguments
    std::list<shared_ptr<OptimizerInfo>> arg_errors;
    std::list<shared_ptr<OptimizerScalarInfo>> arg_scalar_errors;
    dbgs() << ("Arguments:\n");
    for (auto arg = f->arg_begin(); arg != f->arg_end(); arg++) {
        dbgs() << "info for ";
        (arg)->print(dbgs());
        dbgs() << " --> ";

        //if a variable was declared for type
        auto info = getInfoOfValue(arg);
        if (!info) {
            //This is needed to resolve eventual constants in function call (I'm looking at you, LLVM)
            dbgs() << "No error for the argument!\n";
        } else {
            dbgs() << "Got this error: " << info->toString() << "\n";
        }

        //Even if is a null value, we push it!
        arg_errors.push_back(info);

        //If the error is a scalar, collect it also as a scalar
        auto arg_info_scalar = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
        if (arg_info_scalar) {
            arg_scalar_errors.push_back(arg_info_scalar);
        }
        //}
        dbgs() << "\n\n";
    }
    dbgs() << ("Arguments end.");*/


    auto it = functions_still_to_visit.find(calledFunctionName);
    if (it != functions_still_to_visit.end()) {
        //We mark the called function as visited from the global queue, so we will not visit it starting from root.
        functions_still_to_visit.erase(calledFunctionName);
        dbgs() << "Function " << calledFunctionName << " marked as visited in global queue.\n";
    } else {
        dbgs()
                << "[WARNING] We already visited this function, for example when called from another function. Ignoring.\n";

        return;
    }

    //Allocating variable for result: all returns will have the same type, and therefore a cast, if needed
    //SEE COMMENT BEFORE!
    /*shared_ptr<OptimizerInfo> retInfo;
    if (auto inputInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfo->metadata)) {
        auto fptype = dynamic_ptr_cast_or_null<FPType>(inputInfo->IType);
        if (fptype) {
            dbgs() << fptype->toString();
            shared_ptr<OptimizerScalarInfo> result = allocateNewVariableForValue(instruction, fptype, inputInfo->IRange,
                                                                                 instruction->getFunction()->getName());
            retInfo = result;
        } else {
            dbgs() << "There was an input info but no fix point associated.\n";
        }
    } else if (auto pInfo = dynamic_ptr_cast_or_null<StructInfo>(valueInfo->metadata)) {
        auto info = loadStructInfo(instruction, pInfo, "");
        saveInfoForValue(instruction, info);
        retInfo = info;
    } else {
        dbgs() << "No info available on return value, maybe it is not a floating point call.\n";
    }*/

    //in retInfo we now have a variable for the return value of the function. Every return should be casted against it!




    //Obviously the type should be sufficient to contain the result




    //In this case we have no known math function.
    //We will have, when enabled, math functions. In this case these will be handled here!


    dbgs() << ("The function belongs to the current module.\n");
    // got the llvm::Function


    // check for recursion
    //no stack check for recursion from root, I hope
    /*size_t call_count = 0;
    for (size_t i = 0; i < call_stack.size(); i++) {
        if (call_stack[i] == f) {
            call_count++;
        }
    }*/

    std::list<shared_ptr<OptimizerInfo>> arg_errors;
    dbgs() << ("Arguments:\n");
    for (auto arg_i = f->arg_begin(); arg_i != f->arg_end(); arg_i++) {
        //Even if is a null value, we push it!
        arg_errors.push_back(nullptr);
    }


    dbgs() << ("Processing function...\n");

    //See comment before to understand why these variable are set to nulls here
    processFunction(*f, arg_errors, nullptr);


    return;

}

string Optimizer::getEnobActivationVariable(Value *value, int cardinal) {
    assert(value && "Value must not be null!");
    assert(cardinal >= 0 && "Cardinal should be a positive number!");
    string valueName;

    if (auto instr = dyn_cast_or_null<Instruction>(value)) {
        valueName.append(instr->getFunction()->getName());
        valueName.append("_");
    }

    if (!value->getName().empty()) {
        valueName.append(value->getName());
    } else {
        valueName.append(to_string(value->getValueID()));
        valueName.append("_");
    }

    std::replace(valueName.begin(), valueName.end(), '.', '_');
    Instruction *i;

    assert(!valueName.empty() && "The value should have a name!!!");

    string fname;
    if (auto instr = dyn_cast_or_null<Instruction>(value)) {
        fname = instr->getFunction()->getName();
        std::replace(fname.begin(), fname.end(), '.', '_');
    }

    if (!fname.empty()) {
        valueName = fname + "_" + valueName;
    }

    string toreturn = valueName + "_enob_" + to_string(cardinal);

    return toreturn;
}

int Optimizer::getMinIntBitOfValue(Value *pValue) {
    int bits = -1024;
    double smallestRepresentableNumber;

    auto *fp_i = dyn_cast<llvm::ConstantFP>(pValue);
    if (fp_i) {
        APFloat tmp = fp_i->getValueAPF();
        bool losesInfo;
        tmp.convert(APFloatBase::IEEEdouble(), APFloat::roundingMode::rmNearestTiesToEven, &losesInfo);
        auto a = tmp.convertToDouble();
        dbgs() << "Getting max bits of constant " << a << "!\n";
        smallestRepresentableNumber = abs(a);
    } else {
        if (!tuner->hasInfo(pValue)) {
            dbgs() << "No info available for IntBit computation. Using default value\n";
            return bits;
        }

        auto metadata = tuner->valueInfo(pValue)->metadata;

        if (!metadata) {
            dbgs() << "No metadata available for IntBit computation. Using default value\n";
            return bits;
        }


        auto metadata_InputInfo = dynamic_ptr_cast_or_null<InputInfo>(metadata);
        assert(metadata_InputInfo && "Not an InputInfo!");

        auto range = metadata_InputInfo->IRange;


        if (range->Min <= 0 && range->Max >= 0) {
            dbgs() << "The lowest possible number is a 0, infinite ENOB wooooo.\n";
            return bits;
        } else if (range->Min >= 0) {
            //both are greater than 0
            smallestRepresentableNumber = range->Min;
        } else {
            //Both are less than 0
            smallestRepresentableNumber = abs(range->Max);
        }
    }

    double exponentOfExponent = log2(smallestRepresentableNumber);
    bits = round(exponentOfExponent);

    return bits;

}

int Optimizer::getMaxIntBitOfValue(Value *pValue) {
    int bits = 1024;

    double biggestRepresentableNumber;
    auto *fp_i = dyn_cast<llvm::ConstantFP>(pValue);
    if (fp_i) {
        APFloat tmp = fp_i->getValueAPF();
        bool losesInfo;
        tmp.convert(APFloatBase::IEEEdouble(), APFloat::roundingMode::rmNearestTiesToEven, &losesInfo);
        dbgs() << "Getting max bits of constant!\n";
        biggestRepresentableNumber = abs(tmp.convertToDouble());
    } else {
        if (!tuner->hasInfo(pValue)) {
            dbgs() << "No info available for IntBit computation. Using default value\n";
            return bits;
        }

        auto metadata = tuner->valueInfo(pValue)->metadata;

        if (!metadata) {
            dbgs() << "No metadata available for IntBit computation. Using default value\n";
            return bits;
        }


        auto metadata_InputInfo = dynamic_ptr_cast_or_null<InputInfo>(metadata);
        assert(metadata_InputInfo && "Not an InputInfo!");

        auto range = metadata_InputInfo->IRange;

        biggestRepresentableNumber = max(abs(range->Min), abs(range->Max));
    }

    double exponentOfExponent = log2(biggestRepresentableNumber);
    bits = round(exponentOfExponent);

    return bits;

}

void Optimizer::handleUnknownFunction(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {

    assert(instruction && "Instruction is nullptr");
    const auto *call_i = dyn_cast<CallBase>(instruction);
    dbgs() << "=====> Unknown function handling: " << call_i->getCalledFunction()->getName() << "\n";


    assert(call_i && "Cannot cast instruction to call!");
    shared_ptr<OptimizerScalarInfo> retInfo;
    //handling return value. We will force it to be in the original type.
    if (auto inputInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfo->metadata)) {
        if (inputInfo->IRange && instruction->getType()->isFloatingPointTy()) {
            auto fptype = dynamic_ptr_cast_or_null<FPType>(inputInfo->IType);
            if (fptype) {
                dbgs() << fptype->toString();
                shared_ptr<OptimizerScalarInfo> result = allocateNewVariableForValue(instruction, fptype,
                                                                                     inputInfo->IRange,
                                                                                     inputInfo->IError,
                                                                                     call_i->getFunction()->getName(),
                                                                                     true,
                                                                                     "",
                                                                                     true,
                                                                                     false);
                retInfo = result;
                dbgs() << "Correctly handled. New info: " << retInfo->toString() << "\n";
            } else {
                dbgs() << "There was an input info but no fix point associated.\n";
            }
        } else {
            dbgs() << "The call does not return a floating point value.\n";
        }
    } else if (auto pInfo = dynamic_ptr_cast_or_null<StructInfo>(valueInfo->metadata)) {
        emitError("The function considered returns a struct [?]\n");
        return;
    } else {
        dbgs() << "No info available on return value, maybe it is not a floating point returning function.\n";
    }

    //If we have info on return value, forcing the return value in the model to be of the returned type of function
    if (retInfo) {
        if (instruction->getType()->isDoubleTy()) {
            auto constraint = vector<pair<string, double>>();
            constraint.clear();
            constraint.push_back(make_pair(retInfo->getDoubleSelectedVariable(), 1.0));
            model.insertLinearConstraint(constraint, Model::EQ, 1, "Type constraint for return value");
            dbgs() << "Forced return cast to double.\n";
        } else if (instruction->getType()->isFloatTy()) {
            auto constraint = vector<pair<string, double>>();
            constraint.clear();
            constraint.push_back(make_pair(retInfo->getFloatSelectedVariable(), 1.0));
            model.insertLinearConstraint(constraint, Model::EQ, 1, "Type constraint for return value");
            dbgs() << "Forced return cast to float.\n";
        } else if (instruction->getType()->isFloatingPointTy()) {
            dbgs() << "The function returns a floating point type not implemented in the model. Bailing out.\n";
        } else {
            dbgs() << "Probably the functions returns a pointer but i do not known what to do!\n";
        }
    }



    //Return value handled, now it's time for parameters
    dbgs() << ("Arguments:\n");
    int arg = 0;
    for (auto arg_it = call_i->arg_begin(); arg_it != call_i->arg_end(); ++arg_it, arg++) {
        dbgs() << "[" << arg << "] info for ";
        (*arg_it)->print(dbgs());
        dbgs() << " --> ";

        //if a variable was declared for type
        auto info = getInfoOfValue(*arg_it);
        if (!info) {
            //This is needed to resolve eventual constants in function call (I'm looking at you, LLVM)
            dbgs() << "No info for the argument!\n";
            continue;
        } else {
            dbgs() << "Got this info: " << info->toString() << "\n";
        }

        /*if (const generic_range_ptr_t arg_info = fetchInfo(*arg_it)) {*/
        //If the error is a scalar, collect it also as a scalar
        auto arg_info_scalar = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
        if (arg_info_scalar) {
            //Ok, we have info and it is a scalar, let's hope that it's not a pointer
            if ((*arg_it)->getType()->isFloatTy()) {
                auto info2 = allocateNewVariableWithCastCost(arg_it->get(), instruction);
                auto constraint = vector<pair<string, double>>();
                constraint.clear();
                constraint.push_back(make_pair(info2->getFloatSelectedVariable(), 1.0));
                model.insertLinearConstraint(constraint, Model::EQ, 1, "Type constraint for argument value");
                dbgs() << "Forcing argument to float type.\n";
            } else if ((*arg_it)->getType()->isDoubleTy()) {
                auto info2 = allocateNewVariableWithCastCost(arg_it->get(), instruction);
                auto constraint = vector<pair<string, double>>();
                constraint.clear();
                constraint.push_back(make_pair(info2->getDoubleSelectedVariable(), 1.0));
                model.insertLinearConstraint(constraint, Model::EQ, 1, "Type constraint for argument value");
                dbgs() << "Forcing argument to double type.\n";
            } else if ((*arg_it)->getType()->isFloatingPointTy()) {
                dbgs() << "The function uses a floating point type not implemented in the model. Bailing out.\n";
            } else {
                dbgs() << "Probably the functions uses a pointer but I do not known what to do!\n";
            }

        } else {
            dbgs()
                    << "This is a struct passed to an external function but has been optimized by TAFFO. Is this even possible???\n";
        }

        dbgs() << "\n\n";
    }
    dbgs() << ("Arguments end.\n");

    dbgs() << "Function should be correctly handled now.\n";


}


void
Optimizer::handleSelect(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {
    auto *select = dyn_cast<SelectInst>(instruction);

    if (!select->getType()->isFloatingPointTy()) {
        dbgs() << "select node with non float value, skipping...\n";
        return;
    }

    //The select is different from phi because we have all the value in the current basic block, therefore we will have
    // them while computing top down



    if (!select) {
        llvm_unreachable("Could not convert Select instruction to Selectinstruction");
    }


    auto fieldInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfo->metadata);
    if (!fieldInfo) {
        dbgs() << "Not enough information. Bailing out.\n\n";
        return;
    }

    auto fptype = dynamic_ptr_cast_or_null<FPType>(fieldInfo->IType);
    if (!fptype) {
        dbgs() << "No fixed point info associated. Bailing out.\n";
        return;
    }

    //Allocating variable for result
    shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableForValue(instruction, fptype, fieldInfo->IRange,
                                                                           fieldInfo->IError,
                                                                           instruction->getFunction()->getName());
    auto constraint = vector<pair<string, double>>();
    constraint.clear();

    vector<Value *> incomingValues;
    incomingValues.push_back(select->getFalseValue());
    incomingValues.push_back(select->getTrueValue());

    //Yes yes there is not the need to do a loop, but it has the same structure of the phi instruction!
    for (unsigned index = 0; index < incomingValues.size(); index++) {
        Value *op = incomingValues[index];
        if (auto info = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(getInfoOfValue(op))) {
            if (info->doesReferToConstant()) {
                //We skip the variable if it is a constant
                dbgs() << "[INFO] Skipping ";
                op->print(dbgs());
                dbgs() << " as it is a constant!\n";
                continue;
            }
        }
        if (!valueHasInfo(op)) {
            dbgs() << "[INFO] Skipping ";
            op->print(dbgs());
            dbgs() << " as it is does not have an info!\n";
            continue;
        }


        string enob_selection = getEnobActivationVariable(instruction, index);
        model.createVariable(enob_selection, 0, 1);
        constraint.push_back(make_pair(enob_selection, 1.0));
    }

    if (constraint.size() > 0) {
        model.insertLinearConstraint(constraint, Model::EQ, 1, "Enob: one selected constraint");
    } else {
        dbgs() << "[INFO] All constants or unknown nodes, nothing to do!!!\n";
        return;
    }


    int missing = 0;

    for (unsigned index = 0; index < incomingValues.size(); index++) {
        dbgs() << "[Select] Handlign operator " << index << "...\n";
        Value *op = incomingValues[index];

        if (auto info = getInfoOfValue(op)) {
            if (auto info2 = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info)) {
                if (info2->doesReferToConstant()) {
                    //We skip the variable if it is a constant
                    dbgs() << "[INFO] Skipping ";
                    op->print(dbgs());
                    dbgs() << " as it is a constant!\n";
                    continue;
                }
            } else {
                dbgs() << "Strange select value as it is not a number...\n";
            }


            dbgs() << "[Select] We have infos, treating as usual.\n";

            auto destInfo = allocateNewVariableWithCastCost(op, select);

            string enob_var = getEnobActivationVariable(select, index);


            assert(!enob_var.empty() && "Enob var not found!");

            insertTypeEqualityConstraint(variable, destInfo, true);


            auto constraint = vector<pair<string, double>>();
            constraint.clear();
            constraint.push_back(make_pair(variable->getRealEnobVariable(), 1.0));
            constraint.push_back(make_pair(destInfo->getRealEnobVariable(), -1.0));
            constraint.push_back(make_pair(enob_var, -BIG_NUMBER));
            model.insertLinearConstraint(constraint, Model::LE, 0, "Enob: forcing select enob");
        }
        //if no info is to skip
    }


}


















