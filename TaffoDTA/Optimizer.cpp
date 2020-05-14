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
            allocateNewVariableForValue(glob, fptype, fieldInfo->IRange, "");
        } else if (valueInfo->metadata->getKind() == MDInfo::K_Struct) {
            dbgs() << " ^ This is a real structure\n";

            auto fieldInfo = dynamic_ptr_cast_or_null<StructInfo>(valueInfo->metadata);
            if (!fieldInfo) {
                dbgs() << "No struct info. Bailing out.\n";
                return;
            }

            auto optInfo = loadStructInfo(glob, fieldInfo, "");
            valueToVariableName.insert(make_pair(glob, optInfo));

        } else {
            llvm_unreachable("Unknown metadata!");
        }


    } else {
        dbgs() << " ^ this is a pointer, skipping as it is unsupported at the moment.\n";
        return;
    }

}

shared_ptr<OptimizerScalarInfo>
Optimizer::allocateNewVariableForValue(Value *value, shared_ptr<FPType> fpInfo, shared_ptr<Range> rangeInfo,
                                       string functionName, bool insertInList, string nameAppendix) {
    if (valueToVariableName.find(value) != valueToVariableName.end()) {
        llvm_unreachable("Trying to associate a new variable to the same value!\n");
    }

    assert(fpInfo && "fpInfo should not be nullptr here!");
    assert(rangeInfo && "rangeInfo should not be nullptr here!");

    if (!functionName.empty()) {
        functionName = functionName.append("_");
    }


    string varNameBase(string(functionName).append(value->getName()).append(nameAppendix));
    string varName(varNameBase);

    int counter = 0;
    while (model.isVariableDeclared(varName + "_fixp")) {
        varName = string(varNameBase.append("_").append(to_string(counter)));
        counter++;
    }

    dbgs() << "Allocating new variable, will have the following name: " << varName << "\n";

    auto optimizerInfo = make_shared<OptimizerScalarInfo>(varName, 0, fpInfo->getPointPos());
    if (insertInList) {
        valueToVariableName.insert(make_pair(value, optimizerInfo));
    }

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
    assert(value && "Value must not be nullptr!");

    //Global object are constant too but we have already seen them :)
    auto findIt = valueToVariableName.find(value);
    if (findIt != valueToVariableName.end()) {
        return findIt->second;
    }

    if (auto constant = dyn_cast_or_null<Constant>(value)) {
        return processConstant(constant);
    }

    dbgs() << "Could not find any info for ";
    value->print(dbgs());
    dbgs() << "     :( \n";

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
        handleCastInstruction(instruction, valueInfo);

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
                handleGEPInstr(instruction, valueInfo);
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
            case llvm::Instruction::ICmp: {
                dbgs() << "Comparing two integers, skipping...\n";
                break;
            }
            case llvm::Instruction::FCmp: {
                handleFCmp(instruction, valueInfo);
            }
                break;
            case llvm::Instruction::PHI: {
                handlePhi(instruction, valueInfo);
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


void Optimizer::finish() {
    model.finalizeAndSolve();
}

void Optimizer::insertTypeEqualityConstraint(shared_ptr<OptimizerScalarInfo> op1, shared_ptr<OptimizerScalarInfo> op2, bool forceFixBitsConstraint) {
    assert(op1 && op2 && "One of the info is nullptr!");


    auto constraint = vector<pair<string, double>>();
    //Inserting constraint about of the very same type

    if(forceFixBitsConstraint) {
        constraint.clear();
        constraint.push_back(make_pair(op1->getFixedSelectedVariable(), 1.0));
        constraint.push_back(make_pair(op2->getFixedSelectedVariable(), -1.0));
        model.insertLinearConstraint(constraint, Model::EQ, 0);
    }

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

shared_ptr<OptimizerStructInfo> Optimizer::loadStructInfo(Value *glob, shared_ptr<StructInfo> pInfo, string name) {
    shared_ptr<OptimizerStructInfo> optInfo = make_shared<OptimizerStructInfo>(pInfo->size());

    string function = "";
    if(auto instr = dyn_cast_or_null<Instruction>(glob)){
        function=instr->getFunction()->getName();
    }


    int i = 0;
    for (auto it = pInfo->begin(); it != pInfo->end(); it++) {
        if (auto structInfo = dynamic_ptr_cast_or_null<StructInfo>(*it)) {
            optInfo->setField(i, loadStructInfo(glob, structInfo, (name + "_" + to_string(i))));
        } else if (auto ii = dyn_cast<InputInfo>(it->get())) {
            auto fptype = dynamic_ptr_cast_or_null<FPType>(ii->IType);
            if (!fptype) {
                dbgs() << "No fixed point info associated. Bailing out.\n";

            }else {
                auto info = allocateNewVariableForValue(glob, fptype, ii->IRange, function, false, name + "_" + to_string(i));
                optInfo->setField(i, info);
            }
        } else {

        }
        i++;
    }

    return optInfo;
}
















