#include "Optimizer.h"

using namespace tuner;
using namespace mdutils;


void Optimizer::handleGlobal(GlobalObject *glob, shared_ptr<ValueInfo> valueInfo) {
    dbgs() << "handleGlobal called.\n";

    if (!glob->getValueType()->isPointerTy()) {
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

        //Get fractional bits. As we have just got infos about this variable, we should have the maximum number of bits.
        unsigned maxFractionalBits = fptype->getPointPos();
        unsigned minFractionalBits = 0;

        allocateNewVariableForValue(glob, minFractionalBits, maxFractionalBits, "");

    } else {
        dbgs() << " ^ this is a pointer, skipping as it is unsupported at the moment.\n";
        return;
    }

}

string
Optimizer::allocateNewVariableForValue(Value *value, unsigned int minBits, unsigned int maxBits, string functionName) {
    if (valueToVariableName.find(value) != valueToVariableName.end()) {
        llvm_unreachable("Trying to associate a new variable to the same value!\n");
    }

    if (!functionName.empty()) {
        functionName = functionName.append("_");
    }

    string varNameBase(string("x_" + functionName).append(value->getName()));

    string varName(varNameBase);

    int counter = 0;
    while (model.isVariableDeclared(varName)) {
        varName = string(varNameBase.append("_").append(to_string(counter)));
        counter++;
    }

    dbgs() << "Allocating new variable, will have the following name: " << varName << "\n";

    auto optimizerInfo = make_shared<OptimizerScalarInfo>(varName, minBits, maxBits);
    valueToVariableName.insert(make_pair(value, optimizerInfo));

    dbgs() << "Allocating variable " << varName << " with limits [" << minBits << ", " << maxBits << "];\n";
    model.createVariable(varName, minBits, maxBits);

    return varName;

}

shared_ptr<OptimizerInfo> Optimizer::getInfoOfValue(Value *value) {
    auto findIt = valueToVariableName.find(value);
    if (findIt != valueToVariableName.end()) {
        return findIt->second;
    }

    if (auto constant = dyn_cast_or_null<ConstantExpr>(value)) {
        llvm_unreachable("Constant exp still not handled");
    }

    return nullptr;
}


void Optimizer::handleInstruction(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {
    //This will be a mess. God bless you.


    const unsigned opCode = instruction->getOpcode();
    if (opCode == Instruction::Call) {
        emitError("Call not handled atm.");
    } else if (Instruction::isTerminator(opCode)) {
        //Returns :D
        emitError("Returns not handlet atm.");
    } else if (Instruction::isCast(opCode)) {
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
        llvm_unreachable("Not handled.");

    } else if (Instruction::isBinaryOp(opCode)) {
        handleBinaryInstruction(instruction, opCode, valueInfo);

    } else if (Instruction::isUnaryOp(opCode)) {
        llvm_unreachable("Not handled.");

    } else {
        switch (opCode) {
            // memory operations
            case llvm::Instruction::Alloca:
                handleAlloca(instruction, valueInfo);
                break;
            case llvm::Instruction::Load:
                handleLoad(instruction, valueInfo);
                break;
            case llvm::Instruction::Store:
                handleStore(instruction, valueInfo);
                break;
            case llvm::Instruction::GetElementPtr:
                llvm_unreachable("Not handled.");
                break;
            case llvm::Instruction::Fence:
                emitError("Handling of Fence not supported yet");
                break; // TODO implement
            case llvm::Instruction::AtomicCmpXchg:
                emitError("Handling of AtomicCmpXchg not supported yet");
                break; // TODO implement
            case llvm::Instruction::AtomicRMW:
                emitError("Handling of AtomicRMW not supported yet");
                break; // TODO implement

                // other operations
            case llvm::Instruction::ICmp:
            case llvm::Instruction::FCmp: {
                llvm_unreachable("Not handled.");
            }
                break;
            case llvm::Instruction::PHI: {
                llvm_unreachable("Not handled.");
            }
                break;
            case llvm::Instruction::Select:
                llvm_unreachable("Not handled.");
                break;
            case llvm::Instruction::UserOp1: // TODO implement
            case llvm::Instruction::UserOp2: // TODO implement
                emitError("Handling of UserOp not supported yet");
                break;
            case llvm::Instruction::VAArg: // TODO implement
                emitError("Handling of VAArg not supported yet");
                break;
            case llvm::Instruction::ExtractElement: // TODO implement
                emitError("Handling of ExtractElement not supported yet");
                break;
            case llvm::Instruction::InsertElement: // TODO implement
                emitError("Handling of InsertElement not supported yet");
                break;
            case llvm::Instruction::ShuffleVector: // TODO implement
                emitError("Handling of ShuffleVector not supported yet");
                break;
            case llvm::Instruction::ExtractValue: // TODO implement
                emitError("Handling of ExtractValue not supported yet");
                break;
            case llvm::Instruction::InsertValue: // TODO implement
                emitError("Handling of InsertValue not supported yet");
                break;
            case llvm::Instruction::LandingPad: // TODO implement
                emitError("Handling of LandingPad not supported yet");
                break;
            default:
                emitError("unknown instruction " + std::to_string(opCode));
                break;
        }
        // TODO here be dragons
    } // end else

}

void Optimizer::emitError(string stringhina) {
    dbgs() << "[ERROR] " << stringhina << "\n";

}

void Optimizer::handleAlloca(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {
    if (!valueInfo) {
        dbgs() << "No value info, skipping...\n";
        return;
    }

    auto *alloca = dyn_cast<AllocaInst>(instruction);


    if (!alloca->getAllocatedType()->isPointerTy()) {
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

        //Get fractional bits. As we have just got infos about this variable, we should have the maximum number of bits.
        unsigned maxFractionalBits = fptype->getPointPos();
        unsigned minFractionalBits = 0;

        allocateNewVariableForValue(instruction, minFractionalBits, maxFractionalBits,
                                    instruction->getFunction()->getName());

    } else {
        dbgs() << " ^ this is a pointer, skipping as it is unsupported at the moment.\n";
        return;
    }


}

void
Optimizer::handleBinaryInstruction(Instruction *instr, const unsigned OpCode, const shared_ptr<ValueInfo> &valueInfos) {
    //We are only handling operations between float, as we do not care about other values when building the model
    //This is ok as floating point instruction can only be used inside floating point operations in LLVM! :D
    auto binop = dyn_cast_or_null<BinaryOperator>(instr);


    switch (OpCode) {
        //case llvm::Instruction::Add:
        case llvm::Instruction::FAdd:
            handleFAdd(binop, OpCode, valueInfos);
            break;
            //case llvm::Instruction::Sub:
        case llvm::Instruction::FSub:
            //return handleSub(op1, op2, destRange);
            llvm_unreachable("Not implemented!");
            break;
            //case llvm::Instruction::Mul:
        case llvm::Instruction::FMul:
            //return handleMul(op1, op2, destRange);
            llvm_unreachable("Not implemented!");
            break;
            //case llvm::Instruction::UDiv:
            //case llvm::Instruction::SDiv:
        case llvm::Instruction::FDiv:
            //return handleDiv(op1, op2, destRange);
            llvm_unreachable("Not implemented!");
            break;
            //case llvm::Instruction::URem:
            //case llvm::Instruction::SRem:
        case llvm::Instruction::FRem:
            //return handleRem(op1, op2, destRange);
            llvm_unreachable("Not implemented!");

            break;
            /*case llvm::Instruction::Shl:
                return handleShl(op1, op2, destRange);
            case llvm::Instruction::LShr:
            case llvm::Instruction::AShr:
                return handleAShr(op1, op2, destRange);
                llvm_unreachable("No implemented");
            case llvm::Instruction::And:
            case llvm::Instruction::Or:
            case llvm::Instruction::Xor:
                //This is even ok to implement? :/
                break;*/
        default:
            emitError("Unhandled binary operator " + to_string(OpCode)); // unsupported operation
            break;
    }
}

void Optimizer::handleFAdd(BinaryOperator *instr, const unsigned OpCode, const shared_ptr<ValueInfo> &valueInfos) {
    assert(instr->getOpcode() == llvm::Instruction::FAdd && "Operand mismatch!");

    auto op1 = instr->getOperand(0);
    auto op2 = instr->getOperand(1);


    auto info1 = getInfoOfValue(op1);
    auto info2 = getInfoOfValue(op2);

    if (!info1 || !info2) {
        dbgs() << "One of the two values does not have info, ignoring...\n";
        return;
    }

    auto inputInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfos->metadata);
    if (!inputInfo) {
        dbgs() << "No info on destination, bailing out, bug in VRA?\n";
    }

    auto fptype = dynamic_ptr_cast_or_null<FPType>(inputInfo->IType);
    if (!fptype) {
        dbgs() << "No fixed point info associated. Bailing out.\n";
        return;
    }


    string varCast1 = allocateNewVariableWithCastCost(op1, instr);
    string varCast2 = allocateNewVariableWithCastCost(op2, instr);



    //Obviously the type should be sufficient to contain the result
    string result = allocateNewVariableForValue(instr, 0, fptype->getPointPos(), instr->getFunction()->getName());

    //Forcing restriction on I/O
    auto constraint = vector<pair<string, double>>();

    //Argument must be equals
    constraint.push_back(make_pair(varCast1, 1.0));
    constraint.push_back(make_pair(varCast2, -1.0));
    model.insertLinearConstraint(constraint, Model::EQ);


    constraint.clear();
    //Result will be equal to one of the argument
    constraint.push_back(make_pair(varCast1, 1.0));
    constraint.push_back(make_pair(result, -1.0));
    model.insertLinearConstraint(constraint, Model::EQ);


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
        }

        valueToVariableName.insert(make_pair(instruction, make_shared<OptimizerScalarInfo>(sinfos->getVariableName(),
                                                                                           sinfos->getMinBits(),
                                                                                           sinfos->getMaxBits())));

        dbgs() << "For this load, reusing variable" << sinfos->getVariableName() << "\n";

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
        dbgs() << "Store not on a floating point, skipping...\n";
        return;
    }


    auto info1 = getInfoOfValue(opWhereToStore);
    auto info2 = getInfoOfValue(opRegister);

    if (!info1 || !info2) {
        dbgs() << "One of the two values does not have info, ignoring...\n";
        return;
    }

    auto info1_t = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info1);

    string variable = allocateNewVariableWithCastCost(opRegister, instruction);

    //Forcing restriction on I/O
    auto constraint = vector<pair<string, double>>();

    //Argument must be equals
    constraint.push_back(make_pair(variable, 1.0));
    constraint.push_back(make_pair(info1_t->getVariableName(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ);


}

string Optimizer::allocateNewVariableWithCastCost(Value *toUse, Value *whereToUse) {
    auto info_t = getInfoOfValue(toUse);
    if (!info_t) {
        llvm_unreachable("Every value should have an info here!");
    }

    auto info = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info_t);
    if (!info) {
        llvm_unreachable("Here we should only have floating variable, not aggregate.");
    }

    auto originalVar = info->getVariableName();

    string varNameBase((originalVar + ("_") + whereToUse->getName().str()));

    string varName(varNameBase);

    int counter = 0;
    while (model.isVariableDeclared(varName)) {
        varName = string(varNameBase.append("_").append(to_string(counter)));
        counter++;
    }

    dbgs() << "Allocating new variable, will have the following name: " << varName << "\n";


    unsigned minBits = info->minBits;
    unsigned maxBits = info->maxBits;

    auto optimizerInfo = make_shared<OptimizerScalarInfo>(varName, minBits, maxBits);


    dbgs() << "Allocating variable " << varName << " with limits [" << minBits << ", " << maxBits
           << "] with casting cost from " << info->getVariableName() << "\n";

    model.createVariable(varName, minBits, maxBits);


    //Variables for cost:
    auto C1 = "C1_" + varName;
    auto C2 = "C2_" + varName;
    model.createVariable(C1, 0, 1);
    model.createVariable(C2, 0, 1);

    auto constraint = vector<pair<string, double>>();
    //Constraint for binary value to activate
    constraint.push_back(make_pair(originalVar, 1.0));
    constraint.push_back(make_pair(varName, -1.0));
    constraint.push_back(make_pair(C1, -HUGE_VAL));
    model.insertLinearConstraint(constraint, Model::LE);

    constraint.clear();
    //Constraint for binary value to activate
    constraint.push_back(make_pair(originalVar, -1.0));
    constraint.push_back(make_pair(varName, 1.0));
    constraint.push_back(make_pair(C2, -HUGE_VAL));
    model.insertLinearConstraint(constraint, Model::LE);

    return varName;
}

void Optimizer::handleFPPrecisionShift(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {

    auto operand = instruction->getOperand(0); //The argument to be casted

    auto info = getInfoOfValue(operand);
    auto sinfos = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
    if (!sinfos) {
        dbgs() << "No info for the operand, ignoring...\n";
        return;
    }


    valueToVariableName.insert(make_pair(instruction, make_shared<OptimizerScalarInfo>(sinfos->getVariableName(),
                                                                                       sinfos->getMinBits(),
                                                                                       sinfos->getMaxBits())));

    dbgs() << "For this fpext/fptrunc, reusing variable" << sinfos->getVariableName() << "\n";


}

void Optimizer::finish() {
    model.finalizeAndSolve();
}
