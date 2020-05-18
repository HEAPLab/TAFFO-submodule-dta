#include "Optimizer.h"
#include "llvm/Support/Debug.h"

#define DEBUG_TYPE ""

using namespace tuner;
using namespace mdutils;


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
            allocateNewVariableForValue(alloca, fptype, fieldInfo->IRange, alloca->getFunction()->getName());
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


    if (load->getType()->isFloatingPointTy()) {
        //We are loading a floating point, which means we have it's value in a register.
        //As we cannot cast anything during a load, the register will use the very same variable
        auto loaded = load->getPointerOperand();
        shared_ptr<OptimizerInfo> infos = getInfoOfValue(loaded);

        shared_ptr<OptimizerScalarInfo> sinfos = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(infos);

        if (!sinfos) {
            emitError("Loaded a variable with no information attached...");
            return;
        }

        saveInfoForValue(instruction, make_shared<OptimizerScalarInfo>(sinfos->getBaseName(),
                                                                       sinfos->getMinBits(),
                                                                       sinfos->getMaxBits()));

        dbgs() << "For this load, reusing variable [" << sinfos->getBaseName() << "]\n";

    } else {
        dbgs() << "Loading a non floating point, ingoring.\n";
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

    if (!opRegister->getType()->isFloatingPointTy()) {
        dbgs() << "Storing a non-floating point, skipping...\n";
        return;
    }


    auto info1 = getInfoOfValue(opWhereToStore);
    auto info2 = getInfoOfValue(opRegister);

    if (!info1 || !info2) {
        dbgs() << "One of the two values does not have info, ignoring...\n";
        return;
    }

    auto info_pointer = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info1);

    shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableWithCastCost(opRegister, instruction);

    insertTypeEqualityConstraint(info_pointer, variable, true);


}


void Optimizer::handleFPPrecisionShift(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {

    auto operand = instruction->getOperand(0); //The argument to be casted

    auto info = getInfoOfValue(operand);
    auto sinfos = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
    if (!sinfos) {
        dbgs() << "No info for the operand, ignoring...\n";
        return;
    }


    saveInfoForValue(instruction, make_shared<OptimizerScalarInfo>(sinfos->getBaseName(),
                                                                   sinfos->getMinBits(),
                                                                   sinfos->getMaxBits()));

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

    auto fptype = dynamic_ptr_cast_or_null<FPType>(fieldInfo->IType);
    if (!fptype) {
        dbgs() << "No fixed point info associated. Bailing out.\n";
        return;
    }

    //Allocating variable for result
    shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableForValue(instruction, fptype, fieldInfo->IRange,
                                                                           instruction->getFunction()->getName());


    int missing=0;

    for (unsigned index = 0; index < phi_n->getNumIncomingValues(); index++) {
        dbgs() << "[Phi] Handlign operator " << index << "...\n";
        Value *op = phi_n->getIncomingValue(index);

        if(getInfoOfValue(op)) {
            dbgs() << "[Phi] We have infos, treating as usual.\n";
            //because yes, integrity checks....
            openPhiLoop(phi_n, op);
            closePhiLoop(phi_n, op);
        }else{
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
        emitError("BitCast not handled.");
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
            return;
        }

        auto fptype = dynamic_ptr_cast_or_null<FPType>(fieldInfo->IType);
        if (!fptype) {
            dbgs() << "No fixed point info associated. Bailing out.\n";
            return;
        }


        shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableForValue(instruction, fptype, fieldInfo->IRange,
                                                                               instruction->getFunction()->getName());
        return;
    }

    if (isa<FPToSIInst>(instruction) ||
        isa<FPToUIInst>(instruction)) {
        dbgs() << "Casting Floating point to integer, no costs introduced.\n";
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
        auto optInfo = getInfoOfValue(operand);
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
        saveInfoForValue(gep, optInfo);
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

    insertTypeEqualityConstraint(phiInfo, destInfo, true);
    phiWatcher.closePhiLoop(phiNode, requestedValue);

}

void Optimizer::openPhiLoop(PHINode *phiNode, Value *value) {
    phiWatcher.openPhiLoop(phiNode, value);
}


















