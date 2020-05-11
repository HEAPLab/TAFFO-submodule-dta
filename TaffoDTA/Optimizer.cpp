#include "Optimizer.h"

using namespace tuner;
using namespace mdutils;

//FIXME: I_COST should absolutely not be constant
//FIXME: K_COST should be tunable in some way
#define I_COST 1
#define K_SHIFT 1
#define K_FIX_TO_FLOAT 1
#define K_FLOAT_TO_FIX 1
#define K_FIX_TO_DOUBLE 1
#define K_DOUBLE_TO_FIX 1
#define K_FLOAT_TO_DOUBLE 1
#define K_DOUBLE_TO_FLOAT 1
#define P_COST 1
#define M 10000


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


        allocateNewVariableForValue(glob, fptype, fieldInfo->IRange, "");

    } else {
        dbgs() << " ^ this is a pointer, skipping as it is unsupported at the moment.\n";
        return;
    }

}

shared_ptr<OptimizerScalarInfo>
Optimizer::allocateNewVariableForValue(Value *value, shared_ptr<FPType> fpInfo, shared_ptr<Range> rangeInfo,
                                       string functionName) {
    if (valueToVariableName.find(value) != valueToVariableName.end()) {
        llvm_unreachable("Trying to associate a new variable to the same value!\n");
    }

    assert(fpInfo && "fpInfo should not be nullptr here!");
    assert(rangeInfo && "rangeInfo should not be nullptr here!");

    if (!functionName.empty()) {
        functionName = functionName.append("_");
    }


    string varNameBase(string(functionName).append(value->getName()));
    string varName(varNameBase);

    int counter = 0;
    while (model.isVariableDeclared(varName + "_fixp")) {
        varName = string(varNameBase.append("_").append(to_string(counter)));
        counter++;
    }

    dbgs() << "Allocating new variable, will have the following name: " << varName << "\n";

    auto optimizerInfo = make_shared<OptimizerScalarInfo>(varName, 0, fpInfo->getPointPos());
    valueToVariableName.insert(make_pair(value, optimizerInfo));

    dbgs() << "Allocating variable " << varName << " with limits [" << optimizerInfo->minBits << ", "
           << optimizerInfo->maxBits << "];\n";
    model.createVariable(optimizerInfo->getFractBitsVariable(), optimizerInfo->minBits, optimizerInfo->maxBits);

    //binary variables for mixed precision
    model.createVariable(optimizerInfo->getFixedSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getFloatSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getDoubleSelectedVariable(), 0, 1);


    //introducing precision cost: the more a variable is precise, the better it is
    model.insertObjectiveElement(make_pair(optimizerInfo->getFractBitsVariable(), (-1) * P_COST));

    //La variabile indica solo se il costo è attivo o meno, senza indicare nulla riguardo ENOB
    //Enob is computed from Range
    int ENOBfloat = getENOBFromRange(rangeInfo, FloatType::Float_float);
    int ENOBdouble = getENOBFromRange(rangeInfo, FloatType::Float_double);
    model.insertObjectiveElement(make_pair(optimizerInfo->getFloatSelectedVariable(), (-1) * P_COST * ENOBfloat));
    model.insertObjectiveElement(make_pair(optimizerInfo->getDoubleSelectedVariable(), (-1) * P_COST * ENOBdouble));

    auto constraint = vector<pair<string, double>>();
    //Constraint for mixed precision: only one constraint active at one time:
    //_float + _double + _fixed = 1
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 1);

    //Constraint for mixed precision: if fixed is not the selected data type, force bits to 0
    //x_bits - M * x_fixp <= 0
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), -M));
    model.insertLinearConstraint(constraint, Model::LE, 0);

    return optimizerInfo;

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


        shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableForValue(instruction, fptype, fieldInfo->IRange,
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


    shared_ptr<OptimizerScalarInfo> varCast1 = allocateNewVariableWithCastCost(op1, instr);
    shared_ptr<OptimizerScalarInfo> varCast2 = allocateNewVariableWithCastCost(op2, instr);



    //Obviously the type should be sufficient to contain the result
    shared_ptr<OptimizerScalarInfo> result = allocateNewVariableForValue(instr, fptype, inputInfo->IRange,
                                                                         instr->getFunction()->getName());

    insertTypeEqualityConstraint(varCast1, varCast2);
    insertTypeEqualityConstraint(varCast1, result);

    //Precision cost
    //Handloed in allocating variable

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

        valueToVariableName.insert(make_pair(instruction, make_shared<OptimizerScalarInfo>(sinfos->getBaseName(),
                                                                                           sinfos->getMinBits(),
                                                                                           sinfos->getMaxBits())));

        dbgs() << "For this load, reusing variable" << sinfos->getBaseName() << "\n";

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

    auto info_pointer = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info1);

    shared_ptr<OptimizerScalarInfo> variable = allocateNewVariableWithCastCost(opRegister, instruction);

    insertTypeEqualityConstraint(info_pointer, variable);


}

shared_ptr<OptimizerScalarInfo> Optimizer::allocateNewVariableWithCastCost(Value *toUse, Value *whereToUse) {
    auto info_t = getInfoOfValue(toUse);
    if (!info_t) {
        llvm_unreachable("Every value should have an info here!");
    }

    auto info = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info_t);
    if (!info) {
        llvm_unreachable("Here we should only have floating variable, not aggregate.");
    }

    auto originalVar = info->getBaseName();

    string varNameBase((originalVar + ("_") + whereToUse->getName().str()));

    string varName(varNameBase);

    int counter = 0;
    while (model.isVariableDeclared(varName + "_fixp")) {
        varName = string(varNameBase.append("_").append(to_string(counter)));
        counter++;
    }

    dbgs() << "Allocating new variable, will have the following name: " << varName << "\n";


    unsigned minBits = info->minBits;
    unsigned maxBits = info->maxBits;

    auto optimizerInfo = make_shared<OptimizerScalarInfo>(varName, minBits, maxBits);


    dbgs() << "Allocating variable " << varName << " with limits [" << minBits << ", " << maxBits
           << "] with casting cost from " << info->getBaseName() << "\n";

    model.createVariable(optimizerInfo->getFractBitsVariable(), minBits, maxBits);

    //binary variables for mixed precision
    model.createVariable(optimizerInfo->getFixedSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getFloatSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getDoubleSelectedVariable(), 0, 1);

    auto constraint = vector<pair<string, double>>();
    //Constraint for mixed precision: only one constraint active at one time:
    //_float + _double + _fixed = 1
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 1);

    //Constraint for mixed precision: if fixed is not the selected data type, force bits to 0
    //x_bits - M * x_fixp <= 0
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), -M));
    model.insertLinearConstraint(constraint, Model::LE, 0);


    //Variables for costs:

    //Shift cost
    auto C1 = "C1_" + varName;
    auto C2 = "C2_" + varName;
    model.createVariable(C1, 0, 1);
    model.createVariable(C2, 0, 1);

    //Constraint for binary value to activate
    constraint.clear();
    constraint.push_back(make_pair(info->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), -1.0));
    constraint.push_back(make_pair(C1, -M));
    model.insertLinearConstraint(constraint, Model::LE, 0);

    constraint.clear();
    //Constraint for binary value to activate
    constraint.push_back(make_pair(info->getFractBitsVariable(), -1.0));
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(C2, -M));
    model.insertLinearConstraint(constraint, Model::LE, 0);

    //Casting costs
    model.insertObjectiveElement(make_pair(C1, I_COST * K_SHIFT));
    model.insertObjectiveElement(make_pair(C2, I_COST * K_SHIFT));





    //TYPE CAST
    auto C3 = "C3_" + varName;
    auto C4 = "C4_" + varName;
    auto C5 = "C5_" + varName;
    auto C6 = "C6_" + varName;
    auto C7 = "C7_" + varName;
    auto C8 = "C8_" + varName;


    model.createVariable(C3, 0, 1);
    model.createVariable(C4, 0, 1);
    model.createVariable(C5, 0, 1);
    model.createVariable(C6, 0, 1);
    model.createVariable(C7, 0, 1);
    model.createVariable(C8, 0, 1);


    //FIX to FLOAT
    constraint.clear();
    constraint.push_back(make_pair(info->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C3, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1);
    model.insertObjectiveElement(make_pair(C3, I_COST * K_FIX_TO_FLOAT));


    //FLOAT to FIX
    constraint.clear();
    constraint.push_back(make_pair(info->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C4, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1);
    model.insertObjectiveElement(make_pair(C4, I_COST * K_FLOAT_TO_FIX));

    //FIX to DOUBLE
    constraint.clear();
    constraint.push_back(make_pair(info->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C5, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1);
    model.insertObjectiveElement(make_pair(C5, I_COST * K_FIX_TO_DOUBLE));


    //DOUBLE to FIX
    constraint.clear();
    constraint.push_back(make_pair(info->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C6, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1);
    model.insertObjectiveElement(make_pair(C6, I_COST * K_DOUBLE_TO_FIX));



    //FLOAT to DOUBLE
    constraint.clear();
    constraint.push_back(make_pair(info->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C7, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1);
    model.insertObjectiveElement(make_pair(C7, I_COST * K_FLOAT_TO_DOUBLE));


    //DOUBLE to FLOAT
    constraint.clear();
    constraint.push_back(make_pair(info->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C8, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1);
    model.insertObjectiveElement(make_pair(C8, I_COST * K_DOUBLE_TO_FLOAT));



    return optimizerInfo;
}

void Optimizer::handleFPPrecisionShift(Instruction *instruction, shared_ptr<ValueInfo> valueInfo) {

    auto operand = instruction->getOperand(0); //The argument to be casted

    auto info = getInfoOfValue(operand);
    auto sinfos = dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info);
    if (!sinfos) {
        dbgs() << "No info for the operand, ignoring...\n";
        return;
    }


    valueToVariableName.insert(make_pair(instruction, make_shared<OptimizerScalarInfo>(sinfos->getBaseName(),
                                                                                       sinfos->getMinBits(),
                                                                                       sinfos->getMaxBits())));

    dbgs() << "For this fpext/fptrunc, reusing variable" << sinfos->getBaseName() << "\n";


}

void Optimizer::finish() {
    model.finalizeAndSolve();
}

void Optimizer::insertTypeEqualityConstraint(shared_ptr<OptimizerScalarInfo> op1, shared_ptr<OptimizerScalarInfo> op2) {
    assert(op1 && op2 && "One of the info is nullptr!");


    auto constraint = vector<pair<string, double>>();
    //Inserting constraint about of the very same type
    constraint.clear();
    constraint.push_back(make_pair(op1->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(op2->getFixedSelectedVariable(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0);

    constraint.clear();
    constraint.push_back(make_pair(op1->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(op2->getFloatSelectedVariable(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0);

    constraint.clear();
    constraint.push_back(make_pair(op1->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(op2->getDoubleSelectedVariable(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0);

    constraint.clear();
    constraint.push_back(make_pair(op1->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(op2->getFractBitsVariable(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0);


}


int Optimizer::getENOBFromRange(shared_ptr<mdutils::Range> range, mdutils::FloatType::FloatStandard standard) {
    assert(range && "We must have a valid range here!");

    int fractionalDigits;
    int minExponentPower; //eheheh look at this
    switch (standard) {
        case mdutils::FloatType::Float_float:
            fractionalDigits = 23;
            minExponentPower = -126;
            break;
        case mdutils::FloatType::Float_double:
            fractionalDigits = 52;
            minExponentPower = -1022;
            break;
        default:
            llvm_unreachable("Unsupported type here!");
    }

    //We explore the range in order to understand where to compute the number of bits
    //TODO: implement other less pessimistics algorithm, like medium value, or wathever
    double smallestRepresentableNumber;
    if (range->Min <= 0 && range->Max >= 0) {
        //range overlapping 0
        smallestRepresentableNumber = 0;
    } else if (range->Min >= 0) {
        //both are greater than 0
        smallestRepresentableNumber = range->Min;
    } else {
        //Both are less than 0
        smallestRepresentableNumber = abs(range->Max);
    }

    double exponentOfExponent = log2(smallestRepresentableNumber);
    int exponentInt = floor(exponentOfExponent);

    if (exponentInt < minExponentPower) exponentInt = minExponentPower;


    return (-exponentInt) + fractionalDigits;
}















