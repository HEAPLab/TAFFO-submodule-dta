#include <llvm/Analysis/ScalarEvolution.h>
#include "Optimizer.h"
#include "LoopAnalyzerUtil.h"

using namespace tuner;
using namespace mdutils;

void Optimizer::initialize() {
    for (llvm::Function &f : module.functions()) {
        dbgs() << "\nGetting info of " << f.getName() << ":\n";
        if (f.empty()) {
            continue;
        }
        const std::string name = f.getName();
        known_functions[name] = &f;
        functions_still_to_visit[name] = &f;
    }

}

void Optimizer::handleGlobal(GlobalObject *glob, shared_ptr<ValueInfo> valueInfo) {
    dbgs() << "handleGlobal called.\n";

    auto * globalVar = dyn_cast_or_null<GlobalVariable>(glob);
    assert(globalVar && "glob is not a global variable!");

    if (!glob->getValueType()->isPointerTy()) {
        if(!valueInfo->metadata->getEnableConversion()){
            dbgs() << "Skipping as conversion is disabled!";
            return;
        }
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
            auto optInfo = allocateNewVariableForValue(glob, fptype, fieldInfo->IRange, fieldInfo->IError, "", false);
            saveInfoForValue(glob, make_shared<OptimizerPointerInfo>(optInfo));
        } else if (valueInfo->metadata->getKind() == MDInfo::K_Struct) {
            dbgs() << " ^ This is a real structure\n";

            auto fieldInfo = dynamic_ptr_cast_or_null<StructInfo>(valueInfo->metadata);
            if (!fieldInfo) {
                dbgs() << "No struct info. Bailing out.\n";
                return;
            }

            auto optInfo = loadStructInfo(glob, fieldInfo, "");
            saveInfoForValue(glob, optInfo);

        } else {
            llvm_unreachable("Unknown metadata!");
        }


    } else {
        if(!valueInfo->metadata->getEnableConversion()){
            dbgs() << "Skipping as conversion is disabled!";
            return;
        }
        dbgs() << " ^ this is a pointer.\n";

        if (valueInfo->metadata->getKind() == MDInfo::K_Field) {
            dbgs() << " ^ This is a real field ptr\n";
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
            //FIXME: hack, this is done to respect the fact that a pointer (yes, even a simple pointer) may be used by hugly people
            //as array, that are allocated through a malloc. In this way we must use this as a form of bypass. We allocate a new
            //value even if it may be overwritten at some time...

            if(globalVar->hasInitializer() && !globalVar->getInitializer()->isNullValue()){
                dbgs() << "Has initializer and it is not a null value! Need more processing!\n";
            }else{
                dbgs() << "No initializer, or null value!\n";
                auto optInfo = allocateNewVariableForValue(glob, fptype, fieldInfo->IRange, fieldInfo->IError, "", false);
                //This is a pointer, so the reference to it is a pointer to a pointer yay
                saveInfoForValue(glob, make_shared<OptimizerPointerInfo>(make_shared<OptimizerPointerInfo>(optInfo)));
            }

        } else if (valueInfo->metadata->getKind() == MDInfo::K_Struct) {
            dbgs() << " ^ This is a real structure ptr\n";

            auto fieldInfo = dynamic_ptr_cast_or_null<StructInfo>(valueInfo->metadata);
            if (!fieldInfo) {
                dbgs() << "No struct info. Bailing out.\n";
                return;
            }

            auto optInfo = loadStructInfo(glob, fieldInfo, "");
            saveInfoForValue(glob, make_shared<OptimizerPointerInfo>(optInfo));

        } else {
            llvm_unreachable("Unknown metadata!");
        }


        return;
    }

}

shared_ptr<OptimizerScalarInfo>
Optimizer::allocateNewVariableForValue(Value *value, shared_ptr<FPType> fpInfo, shared_ptr<Range> rangeInfo, shared_ptr<double> suggestedMinError,
                                       string functionName, bool insertInList, string nameAppendix, bool insertENOBinMin, bool respectFloatingPointConstraint) {
    assert(!valueHasInfo(value) && "The value considered already have an info!");

    assert(fpInfo && "fpInfo should not be nullptr here!");
    assert(rangeInfo && "rangeInfo should not be nullptr here!");

    if (!functionName.empty()) {
        functionName = functionName.append("_");
    }


    string varNameBase(string(functionName).append(value->getName()).append(nameAppendix));
    std::replace(varNameBase.begin(), varNameBase.end(), '.', '_');
    string varName(varNameBase);

    int counter = 0;
    while (model.isVariableDeclared(varName + "_fixp")) {
        varName = string(varNameBase).append("_").append(to_string(counter));
        counter++;
    }


    dbgs() << "Allocating new variable, will have the following name: " << varName << "\n";

    auto optimizerInfo = make_shared<OptimizerScalarInfo>(varName, 0, fpInfo->getPointPos(), fpInfo->getWidth(),
                                                          fpInfo->isSigned(), *rangeInfo, "");


    dbgs() << "Allocating variable " << varName << " with limits [" << optimizerInfo->minBits << ", "
           << optimizerInfo->maxBits << "];\n";

    string out;
    raw_string_ostream stream(out);
    value->print(stream);

    model.insertComment("Stuff for " + stream.str(), 3);

    model.createVariable(optimizerInfo->getFractBitsVariable(), optimizerInfo->minBits, optimizerInfo->maxBits);

    //binary variables for mixed precision
    model.createVariable(optimizerInfo->getFixedSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getFloatSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getDoubleSelectedVariable(), 0, 1);

    //ENOB propagation, free variable
    model.createVariable(optimizerInfo->getRealEnobVariable(), -BIG_NUMBER, BIG_NUMBER);

    auto constraint = vector<pair<string, double>>();
    int ENOBfloat = getENOBFromRange(rangeInfo, FloatType::Float_float);
    int ENOBdouble = getENOBFromRange(rangeInfo, FloatType::Float_double);
    //Enob constraints fix
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getRealEnobVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), -1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER, "Enob constraint for fix");

    //Enob constraints float
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getRealEnobVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER + ENOBfloat, "Enob constraint for float");

    //Enob constraints float
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getRealEnobVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER + ENOBdouble, "Enob constraint for double");


    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), -BIG_NUMBER));
    //DO NOT REMOVE THE CAST OR SOMEONE WILL DEBUG THIS FOR AN WHOLE DAY AGAIN
    model.insertLinearConstraint(constraint, Model::GE, (-BIG_NUMBER-FIX_DELTA_MAX)+((int)fpInfo->getPointPos()), "Limit the lower number of frac bits"+to_string(fpInfo->getPointPos()));

    int enobMaxCost = max({ENOBfloat, ENOBdouble, (int)fpInfo->getPointPos()});

    if(suggestedMinError){
        /*If we have a suggested min initial error, that is used for error propagation, we should cap the enob to that erro.
         * In facts, it is not really necessary to "unbound" the minimum error while the input variables are not error free
         * Think about a reading from a sensor (ADC) or something similar, the error there will be even if we use a double to
         * store its result. Therefore we limit the enob to a useful value even for floating points.*/


        double errorEnob = getENOBFromError(*suggestedMinError);

        dbgs() << "We have a suggested min error, limiting the enob in the model to " << errorEnob << "\n";

        constraint.clear();
        constraint.push_back(make_pair(optimizerInfo->getRealEnobVariable(), 1.0));
        model.insertLinearConstraint(constraint, Model::LE, errorEnob, "Enob constraint for error maximal");

        //Capped at max
        enobMaxCost = min(enobMaxCost, (int) errorEnob);
    }

    if(!MixedDoubleEnabled && respectFloatingPointConstraint){
        constraint.clear();
        constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
        model.insertLinearConstraint(constraint, Model::LE, 0, "Disable double data type");
    }


    /*//introducing precision cost: the more a variable is precise, the better it is
    model.insertObjectiveElement(make_pair(optimizerInfo->getFractBitsVariable(), (-1) * TUNING_ENOB));

    //La variabile indica solo se il costo è attivo o meno, senza indicare nulla riguardo ENOB
    //Enob is computed from Range

    model.insertObjectiveElement(make_pair(optimizerInfo->getFloatSelectedVariable(), (-1) * TUNING_ENOB * ENOBfloat));
    model.insertObjectiveElement(
            make_pair(optimizerInfo->getDoubleSelectedVariable(), (-1) * TUNING_ENOB * ENOBdouble));*/
    if(insertENOBinMin) {
        model.insertObjectiveElement(
                make_pair(optimizerInfo->getRealEnobVariable(), (-1)), MODEL_OBJ_ENOB, enobMaxCost);
    }

    //Constraint for mixed precision: only one constraint active at one time:
    //_float + _double + _fixed = 1
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 1, "Exactly one selected type");

    //Constraint for mixed precision: if fixed is not the selected data type, force bits to 0
    //x_bits - M * x_fixp <= 0
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), -BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, 0, "If not fix, frac part to zero");


    if (insertInList) {
        saveInfoForValue(value, optimizerInfo);
    }

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

    auto info = LoopAnalyzerUtil::computeFullTripCount(tuner, instruction);
    dbgs() << "Optimizer: got trip count " << info << "\n";

    const unsigned opCode = instruction->getOpcode();
    if (opCode == Instruction::Call) {
        handleCall(instruction, valueInfo);
    } else if (Instruction::isTerminator(opCode)) {
        handleTerminators(instruction, valueInfo);
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
                handleSelect(instruction, valueInfo);;
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

void Optimizer::handleTerminators(llvm::Instruction *term, shared_ptr<ValueInfo> valueInfo) {
    const unsigned opCode = term->getOpcode();
    switch (opCode) {
        case llvm::Instruction::Ret:
            handleReturn(term, valueInfo);
            break;
        case llvm::Instruction::Br:
            // TODO improve by checking condition and relatevely update BB weigths
            // do nothing
            break;
        case llvm::Instruction::Switch:
            emitError("Handling of Switch not implemented yet");
            break; // TODO implement
        case llvm::Instruction::IndirectBr:
            emitError("Handling of IndirectBr not implemented yet");
            break; // TODO implement
        case llvm::Instruction::Invoke:
            handleCall(term, valueInfo);
            break;
        case llvm::Instruction::Resume:
            emitError("Handling of Resume not implemented yet");
            break; // TODO implement
        case llvm::Instruction::Unreachable:
            emitError("Handling of Unreachable not implemented yet");
            break; // TODO implement
        case llvm::Instruction::CleanupRet:
            emitError("Handling of CleanupRet not implemented yet");
            break; // TODO implement
        case llvm::Instruction::CatchRet:
            emitError("Handling of CatchRet not implemented yet");
            break; // TODO implement
        case llvm::Instruction::CatchSwitch:
            emitError("Handling of CatchSwitch not implemented yet");
            break; // TODO implement
        default:
            break;
    }

    return;
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

    string endName = whereToUse->getName().str();
    if(endName.empty()){
        if(auto istr = dyn_cast_or_null<Instruction>(whereToUse)){
            endName = string(istr->getOpcodeName());
        }

    }
    std::replace(endName.begin(), endName.end(), '.', '_');



    string varNameBase((originalVar + ("_CAST_") + endName));

    string varName(varNameBase);

    int counter = 0;
    while (model.isVariableDeclared(varName + "_fixp")) {
        varName = string(varNameBase).append("_").append(to_string(counter));
        counter++;
    }

    dbgs() << "Allocating new variable, will have the following name: " << varName << "\n";


    unsigned minBits = info->minBits;
    unsigned maxBits = info->maxBits;

    auto optimizerInfo = make_shared<OptimizerScalarInfo>(varName, minBits, maxBits, info->totalBits, info->isSigned, *info->getRange(), info->getOverridedEnob());




    dbgs() << "Allocating variable " << varName << " with limits [" << minBits << ", " << maxBits
           << "] with casting cost from " << info->getBaseName() << "\n";

    string out;
    raw_string_ostream stream(out);
    whereToUse->print(stream);

    model.insertComment("Constraint for cast for " + stream.str(), 3);

    model.createVariable(optimizerInfo->getFractBitsVariable(), minBits, maxBits);

    //binary variables for mixed precision
    model.createVariable(optimizerInfo->getFixedSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getFloatSelectedVariable(), 0, 1);
    model.createVariable(optimizerInfo->getDoubleSelectedVariable(), 0, 1);
    //model.createVariable(optimizerInfo->getRealEnobVariable(), -BIG_NUMBER, BIG_NUMBER);

    auto constraint = vector<pair<string, double>>();
    //Constraint for mixed precision: only one constraint active at one time:
    //_float + _double + _fixed = 1
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 1, "exactly 1 type");


    //Real enob is still the same!
    //constraint.clear();
    //constraint.push_back(make_pair(info->getRealEnobVariable(), -1.0));
    //constraint.push_back(make_pair(optimizerInfo->getRealEnobVariable(), 1.0));
    //model.insertLinearConstraint(constraint, Model::LE, 0, "The ENOB is less or equal!");

    //Constraint for mixed precision: if fixed is not the selected data type, force bits to 0
    //x_bits - M * x_fixp <= 0
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), -BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, 0, "If no fix, fix frac part = 0");


    double maxCastCost = max({cpuCosts.getCost(CPUCosts::CAST_FIX_FIX),
                              cpuCosts.getCost(CPUCosts::CAST_FIX_FLOAT),
                              cpuCosts.getCost(CPUCosts::CAST_FLOAT_FIX),
                              cpuCosts.getCost(CPUCosts::CAST_FIX_DOUBLE),
                              cpuCosts.getCost(CPUCosts::CAST_DOUBLE_FIX),
                              cpuCosts.getCost(CPUCosts::CAST_FLOAT_DOUBLE),
                              cpuCosts.getCost(CPUCosts::CAST_DOUBLE_FLOAT)});


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
    constraint.push_back(make_pair(C1, -BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, 0, "Shift cost 1");

    constraint.clear();
    //Constraint for binary value to activate
    constraint.push_back(make_pair(info->getFractBitsVariable(), -1.0));
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(C2, -BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, 0, "Shift cost 2");

    //Casting costs
    //Is correct to only place here the maxCastCost, as only one cast will be active at a time
    model.insertObjectiveElement(make_pair(C1, I_COST * cpuCosts.getCost(CPUCosts::CAST_FIX_FIX)), MODEL_OBJ_CASTCOST, maxCastCost);
    model.insertObjectiveElement(make_pair(C2, I_COST * cpuCosts.getCost(CPUCosts::CAST_FIX_FIX)), MODEL_OBJ_CASTCOST, 0);





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
    model.insertLinearConstraint(constraint, Model::LE, 1, "Fix to float");
    model.insertObjectiveElement(make_pair(C3, I_COST * cpuCosts.getCost(CPUCosts::CAST_FIX_FLOAT)), MODEL_OBJ_CASTCOST, 0);


    //FLOAT to FIX
    constraint.clear();
    constraint.push_back(make_pair(info->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C4, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1, "Float to fix");
    model.insertObjectiveElement(make_pair(C4, I_COST * cpuCosts.getCost(CPUCosts::CAST_FLOAT_FIX)), MODEL_OBJ_CASTCOST, 0);

    //FIX to DOUBLE
    constraint.clear();
    constraint.push_back(make_pair(info->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C5, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1, "Fix to double");
    model.insertObjectiveElement(make_pair(C5, I_COST * cpuCosts.getCost(CPUCosts::CAST_FIX_DOUBLE)), MODEL_OBJ_CASTCOST, 0);


    //DOUBLE to FIX
    constraint.clear();
    constraint.push_back(make_pair(info->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C6, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1, "Double to fix");
    model.insertObjectiveElement(make_pair(C6, I_COST * cpuCosts.getCost(CPUCosts::CAST_DOUBLE_FIX)), MODEL_OBJ_CASTCOST, 0);



    //FLOAT to DOUBLE
    constraint.clear();
    constraint.push_back(make_pair(info->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C7, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1, "Float to double");
    model.insertObjectiveElement(
            make_pair(C7, I_COST * cpuCosts.getCost(CPUCosts::CAST_FLOAT_DOUBLE)), MODEL_OBJ_CASTCOST, 0);


    //DOUBLE to FLOAT
    constraint.clear();
    constraint.push_back(make_pair(info->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(C8, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1, "Double to float");
    model.insertObjectiveElement(
            make_pair(C8, I_COST * cpuCosts.getCost(CPUCosts::CAST_DOUBLE_FLOAT)), MODEL_OBJ_CASTCOST, 0);


    return optimizerInfo;
}


bool Optimizer::finish() {
    dbgs() << "[Phi] Phi node state:\n";
    phiWatcher.dumpState();

    dbgs() << "[Mem] MemPhi node state:\n";
    memWatcher.dumpState();

    bool result = model.finalizeAndSolve();

    dbgs() << "Skipped conversions due to disabled flag: " << DisabledSkipped << "\n";

    return result;
}

void Optimizer::insertTypeEqualityConstraint(shared_ptr<OptimizerScalarInfo> op1, shared_ptr<OptimizerScalarInfo> op2,
                                             bool forceFixBitsConstraint) {
    assert(op1 && op2 && "One of the info is nullptr!");


    auto constraint = vector<pair<string, double>>();
    //Inserting constraint about of the very same type


    constraint.clear();
    constraint.push_back(make_pair(op1->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(op2->getFixedSelectedVariable(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0, "fix equality");


    constraint.clear();
    constraint.push_back(make_pair(op1->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(op2->getFloatSelectedVariable(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0, "float equality");

    constraint.clear();
    constraint.push_back(make_pair(op1->getDoubleSelectedVariable(), 1.0));
    constraint.push_back(make_pair(op2->getDoubleSelectedVariable(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0, "double equality");

    if (forceFixBitsConstraint) {
        constraint.clear();
        constraint.push_back(make_pair(op1->getFractBitsVariable(), 1.0));
        constraint.push_back(make_pair(op2->getFractBitsVariable(), -1.0));
        model.insertLinearConstraint(constraint, Model::EQ, 0, "same fractional bit");
    }

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

    /*dbgs() << "smallestNumber: " << smallestRepresentableNumber << "\n";
    dbgs() << "exponentInt: " << exponentInt << "\n";*/

    if (exponentInt < minExponentPower) exponentInt = minExponentPower;


    return (-exponentInt) + fractionalDigits;
}

shared_ptr<OptimizerStructInfo> Optimizer::loadStructInfo(Value *glob, shared_ptr<StructInfo> pInfo, string name) {
    shared_ptr<OptimizerStructInfo> optInfo = make_shared<OptimizerStructInfo>(pInfo->size());

    string function = "";
    if (auto instr = dyn_cast_or_null<Instruction>(glob)) {
        function = instr->getFunction()->getName();
    }


    int i = 0;
    for (auto it = pInfo->begin(); it != pInfo->end(); it++) {
        if (auto structInfo = dynamic_ptr_cast_or_null<StructInfo>(*it)) {
            optInfo->setField(i, loadStructInfo(glob, structInfo, (name + "_" + to_string(i))));
        } else if (auto ii = dyn_cast<InputInfo>(it->get())) {
            auto fptype = dynamic_ptr_cast_or_null<FPType>(ii->IType);
            if (!fptype) {
                dbgs() << "No fixed point info associated. Bailing out.\n";

            } else {
                auto info = allocateNewVariableForValue(glob, fptype, ii->IRange, ii->IError, function, false,
                                                        name + "_" + to_string(i));
                optInfo->setField(i, info);
            }
        } else {

        }
        i++;
    }

    return optInfo;
}

void Optimizer::saveInfoForValue(Value *value, shared_ptr<OptimizerInfo> optInfo) {
    assert(value && "Value must not be nullptr!");
    assert(optInfo && "optInfo must be a valid info!");
    assert(!valueHasInfo(value) && "Double insertion of value info!");

    dbgs() << "Saved info " << optInfo->toString() << " for ";
    value->print(dbgs());
    dbgs()<<"\n";

    valueToVariableName.insert(make_pair(value, optInfo));

    int closed_phi = 0;
    while (PHINode *phiNode = phiWatcher.getPhiNodeToClose(value)) {
        closePhiLoop(phiNode, value);
        closed_phi++;
    }
    if (closed_phi) {
        dbgs() << "Closed " << closed_phi << " PHI loops\n";
    }


    int closed_mem=0;
    while (auto *phiNode = memWatcher.getPhiNodeToClose(value)) {
        closeMemLoop(phiNode, value);
        closed_mem++;
    }
    if (closed_mem) {
        dbgs() << "Closed " << closed_mem << " MEM loops\n";
    }

}

bool Optimizer::valueHasInfo(Value *value) {
    return valueToVariableName.find(value) != valueToVariableName.end();
}


/*This is ugly as hell, but we use this data type to prevent creating other custom classes for nothing*/
shared_ptr<mdutils::MDInfo> Optimizer::getAssociatedMetadata(Value *pValue) {
    auto res = getInfoOfValue(pValue);
    if (!res) {
        return nullptr;
    }

    if (res->getKind() == OptimizerInfo::K_Pointer) {
        //FIXME: do we support double pointers?
        auto res1 = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(res);
        //Unwrap pointer
        res = res1->getOptInfo();
    }

    return buildDataHierarchy(res);
}

shared_ptr<mdutils::MDInfo> Optimizer::buildDataHierarchy(shared_ptr<OptimizerInfo> info) {
    if (info->getKind() == OptimizerInfo::K_Field) {
        auto i = modelvarToTType(dynamic_ptr_cast_or_null<OptimizerScalarInfo>(info));
        auto result = make_shared<InputInfo>();
        result->IType = i;
        return result;
    } else if (info->getKind() == OptimizerInfo::K_Struct) {
        auto sti = dynamic_ptr_cast_or_null<OptimizerStructInfo>(info);
        auto result = make_shared<StructInfo>(sti->size());
        for (int i = 0; i < sti->size(); i++) {
            result->setField(i, buildDataHierarchy(sti->getField(i)));
        }

        return result;
    }


    llvm_unreachable("Unnknown data type");
}

shared_ptr<mdutils::TType> Optimizer::modelvarToTType(shared_ptr<OptimizerScalarInfo> scalarInfo) {
    if (!scalarInfo) {
        dbgs() << "Nullptr scalar info!";
        return nullptr;
    }
    double selectedFixed = model.getVariableValue(scalarInfo->getFixedSelectedVariable());
    double selectedFloat = model.getVariableValue(scalarInfo->getFloatSelectedVariable());
    double selectedDouble = model.getVariableValue(scalarInfo->getDoubleSelectedVariable());
    double fracbits = model.getVariableValue(scalarInfo->getFractBitsVariable());

    assert(selectedDouble + selectedFixed + selectedFloat == 1 &&
           "OMG! Catastrophic failure! Exactly one variable should be selected here!!!");

    if (selectedFixed == 1) {
        StatSelectedFixed++;
        return make_shared<mdutils::FPType>(scalarInfo->getTotalBits(), (int) fracbits, scalarInfo->isSigned);
    }


    if (selectedFloat == 1) {
        StatSelectedFloat++;
        return make_shared<mdutils::FloatType>(FloatType::Float_float, 0);
    }

    if (selectedDouble == 1) {
        StatSelectedDouble++;
        return make_shared<mdutils::FloatType>(FloatType::Float_double, 0);
    }

    llvm_unreachable("Trying to implement a new datatype? look here :D");
}



int Optimizer::getENOBFromError(double error) {
    int enob=floor(log2(error));




    //Fix enob to be at least 0.
    return max(-enob, 0);
}

void Optimizer::printStatInfos() {
    dbgs() << "Converted to fix: " << StatSelectedFixed << "\n";
    dbgs() << "Converted to float: " << StatSelectedFloat << "\n";
    dbgs() << "Converted to double: " << StatSelectedDouble << "\n";

    int total = StatSelectedFixed + StatSelectedFloat + StatSelectedDouble;

    dbgs() << "Conversion entropy as equally distributed variables: " << -(
            ((double)StatSelectedDouble / total) * log2(((double)StatSelectedDouble) / total) +
                    ((double)StatSelectedFloat / total) * log2(((double)StatSelectedFloat) / total) +
                    ((double)StatSelectedDouble / total) * log2(((double)StatSelectedDouble) / total)
            ) << "\n";


    ofstream statFile;
    statFile.open("./stats.txt", ios::out|ios::trunc);
    assert(statFile.is_open() && "File open failed!");
    statFile << "TOFIX, " << StatSelectedFixed << "\n";
    statFile << "TOFLOAT, " << StatSelectedFloat << "\n";
    statFile << "TODOUBLE, " << StatSelectedDouble << "\n";
    statFile << "COSTENOB, " << model.costEnob << "\n";
    statFile << "COSTCAST, " << model.costCast << "\n";
    statFile << "COSTTIME, " << model.costTime << "\n";
    statFile.flush();
    statFile.close();

}







