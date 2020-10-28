#include <llvm/Analysis/ScalarEvolution.h>
#include "Optimizer.h"
#include "LoopAnalyzerUtil.h"
#include "llvm/IR/IntrinsicInst.h"
#include "llvm/ADT/APFloat.h"


using namespace tuner;
using namespace mdutils;

void Optimizer::initialize() {

     for (llvm::Function &f : module.functions()) {
        dbgs() << "\nGetting info of " << f.getName() << ":\n";
        if (f.empty()) {
            continue;
        }
        const std::string name = f.getName().str();
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


    string varNameBase(string(functionName).append((std::string)value->getName()).append(nameAppendix));
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

    if(hasHalf)
    model.createVariable(optimizerInfo->getHalfSelectedVariable(), 0, 1);
    if(hasQuad)
    model.createVariable(optimizerInfo->getQuadSelectedVariable(), 0, 1);
    if(hasFP80)
    model.createVariable(optimizerInfo->getFP80SelectedVariable(), 0, 1);
    if(hasPPC128)
    model.createVariable(optimizerInfo->getPPC128SelectedVariable(), 0, 1);
    if(hasBF16)
    model.createVariable(optimizerInfo->getBF16SelectedVariable(), 0, 1);

    //ENOB propagation, free variable
    model.createVariable(optimizerInfo->getRealEnobVariable(), -BIG_NUMBER, BIG_NUMBER);

    auto constraint = vector<pair<string, double>>();
    int ENOBfloat = getENOBFromRange(rangeInfo, FloatType::Float_float);
    int ENOBdouble = getENOBFromRange(rangeInfo, FloatType::Float_double);
    int ENOBhalf = 0;
    int ENOBquad = 0;
    int ENOBppc128 = 0;
    int ENOBfp80 = 0;
    int ENOBbf16 = 0;       


    //Enob constraints fix
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getRealEnobVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), -1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER, "Enob constraint for fix");

    auto enobconstraint = [&]( int ENOB, const std::string (tuner::OptimizerScalarInfo::* getVariable)(), const char * desc) mutable {
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getRealEnobVariable(), 1.0));
    constraint.push_back(make_pair( ((*optimizerInfo).*getVariable)(), BIG_NUMBER));
    model.insertLinearConstraint(constraint, Model::LE, BIG_NUMBER + ENOB, desc);
    };
    //Enob constraints float     
    enobconstraint(ENOBfloat, &tuner::OptimizerScalarInfo::getFloatSelectedVariable, "Enob constraint for float");

    //Enob constraints Double     
    enobconstraint(ENOBdouble, &tuner::OptimizerScalarInfo::getDoubleSelectedVariable, "Enob constraint for double");

    //Enob constraints Half
    if(hasHalf){
    ENOBhalf = getENOBFromRange(rangeInfo, FloatType::Float_half);
    enobconstraint(ENOBhalf, &tuner::OptimizerScalarInfo::getHalfSelectedVariable, "Enob constraint for half");    
    }

    // Enob constraints Quad
    if (hasQuad) {
      ENOBquad = getENOBFromRange(rangeInfo, FloatType::Float_fp128);
      enobconstraint(ENOBquad,
                     &tuner::OptimizerScalarInfo::getQuadSelectedVariable,
                     "Enob constraint for quad");
    }
    // Enob constraints FP80
    
      if (hasFP80){
        ENOBfp80 = getENOBFromRange(rangeInfo, FloatType::Float_x86_fp80);
      enobconstraint(ENOBfp80,
                     &tuner::OptimizerScalarInfo::getFP80SelectedVariable,
                     "Enob constraint for fp80");
    }
    // Enob constraints PPC128
    
      if (hasPPC128){
        ENOBppc128 = getENOBFromRange(rangeInfo, FloatType::Float_ppc_fp128);
      enobconstraint(ENOBppc128,
                     &tuner::OptimizerScalarInfo::getPPC128SelectedVariable,
                     "Enob constraint for ppc128");
    }
    // Enob constraints FP80
    
      if (hasBF16){
        ENOBbf16 = getENOBFromRange(rangeInfo, FloatType::Float_bfloat);
      enobconstraint(ENOBbf16,
                     &tuner::OptimizerScalarInfo::getBF16SelectedVariable,
                     "Enob constraint for bf16");
    }

    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFractBitsVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), -BIG_NUMBER));
    //DO NOT REMOVE THE CAST OR SOMEONE WILL DEBUG THIS FOR AN WHOLE DAY AGAIN
    model.insertLinearConstraint(constraint, Model::GE, (-BIG_NUMBER-FIX_DELTA_MAX)+((int)fpInfo->getPointPos()), "Limit the lower number of frac bits"+to_string(fpInfo->getPointPos()));

    int enobMaxCost = max({ENOBfloat, ENOBdouble, (int)fpInfo->getPointPos()});
    
    enobMaxCost = hasHalf ? max(enobMaxCost, ENOBhalf) : enobMaxCost;
    enobMaxCost = hasFP80 ? max(enobMaxCost, ENOBfp80) : enobMaxCost;
    enobMaxCost = hasQuad ? max(enobMaxCost, ENOBquad) : enobMaxCost;
    enobMaxCost = hasPPC128 ? max(enobMaxCost, ENOBppc128) : enobMaxCost;
    enobMaxCost = hasBF16 ? max(enobMaxCost, ENOBbf16) : enobMaxCost;




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
    if(hasHalf)
    constraint.push_back(make_pair(optimizerInfo->getHalfSelectedVariable(), 1.0));
    if(hasQuad)
    constraint.push_back(make_pair(optimizerInfo->getQuadSelectedVariable(), 1.0));    
    if(hasPPC128)
    constraint.push_back(make_pair(optimizerInfo->getPPC128SelectedVariable(), 1.0));  
    if(hasFP80)
    constraint.push_back(make_pair(optimizerInfo->getFP80SelectedVariable(), 1.0)); 
    if(hasBF16)
    constraint.push_back(make_pair(optimizerInfo->getBF16SelectedVariable(), 1.0)); 

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
    if(hasHalf)
    model.createVariable(optimizerInfo->getHalfSelectedVariable(), 0, 1);
    if(hasQuad)
    model.createVariable(optimizerInfo->getQuadSelectedVariable(), 0, 1);
    if(hasPPC128)
    model.createVariable(optimizerInfo->getPPC128SelectedVariable(), 0, 1);
    if(hasFP80)
    model.createVariable(optimizerInfo->getFP80SelectedVariable(), 0, 1);
    if(hasBF16)
    model.createVariable(optimizerInfo->getBF16SelectedVariable(), 0, 1);
    //model.createVariable(optimizerInfo->getRealEnobVariable(), -BIG_NUMBER, BIG_NUMBER);

    auto constraint = vector<pair<string, double>>();
    //Constraint for mixed precision: only one constraint active at one time:
    //_float + _double + _fixed = 1
    constraint.clear();
    constraint.push_back(make_pair(optimizerInfo->getFixedSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getFloatSelectedVariable(), 1.0));
    constraint.push_back(make_pair(optimizerInfo->getDoubleSelectedVariable(), 1.0));
    if(hasHalf)
    constraint.push_back(make_pair(optimizerInfo->getHalfSelectedVariable(), 1.0));
     if(hasQuad)
    constraint.push_back(make_pair(optimizerInfo->getQuadSelectedVariable(), 1.0));
    if(hasPPC128)
    constraint.push_back(make_pair(optimizerInfo->getPPC128SelectedVariable(), 1.0));
    if(hasFP80)
    constraint.push_back(make_pair(optimizerInfo->getFP80SelectedVariable(), 1.0));
    if(hasBF16)
    constraint.push_back(make_pair(optimizerInfo->getBF16SelectedVariable(), 1.0));


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
                              cpuCosts.getCost(CPUCosts::CAST_FIX_HALF),  
                              cpuCosts.getCost(CPUCosts::CAST_FIX_DOUBLE),                                                          
                              cpuCosts.getCost(CPUCosts::CAST_FLOAT_FIX),
                              cpuCosts.getCost(CPUCosts::CAST_FLOAT_DOUBLE), 
                              cpuCosts.getCost(CPUCosts::CAST_FLOAT_HALF),
                              cpuCosts.getCost(CPUCosts::CAST_HALF_FIX),
                              cpuCosts.getCost(CPUCosts::CAST_HALF_DOUBLE), 
                              cpuCosts.getCost(CPUCosts::CAST_HALF_FLOAT),                                                                                        
                              cpuCosts.getCost(CPUCosts::CAST_DOUBLE_FIX),
                              cpuCosts.getCost(CPUCosts::CAST_DOUBLE_HALF),
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
    auto costcrosslambda = [&](std::string& variable , tuner::CPUCosts::CostsId cost, const string (tuner::OptimizerScalarInfo::*getFirstVariable)(), const string (tuner::OptimizerScalarInfo::*getSecondVariable)(), const std::string desc) mutable {
    
    constraint.clear();
    constraint.push_back(make_pair(((*info).*getFirstVariable)(), 1.0));
    constraint.push_back(make_pair(((*optimizerInfo).*getSecondVariable)(), 1.0));
    constraint.push_back(make_pair(variable, -1));
    model.insertLinearConstraint(constraint, Model::LE, 1, desc);
    model.insertObjectiveElement(make_pair(variable, I_COST * cpuCosts.getCost(cost)), MODEL_OBJ_CASTCOST, 0);
    };

    int counter2 = 3;
    for (auto& CostsString : cpuCosts.CostsIdValues){


        if(CostsString.find("CAST") == 0 && CostsString.find("CAST_FIX_FIX") == std::string::npos){
            const string (tuner::OptimizerScalarInfo::*first_f )() = nullptr;
            std::size_t first_i = 0;
            std::size_t second_i = 0;
            char * first_c;
            char * second_c;            
            const string (tuner::OptimizerScalarInfo::*second_f)() = nullptr;
            std::size_t fixed_i  = CostsString.find("FIX");
            std::size_t float_i  = CostsString.find("FLOAT");
            std::size_t double_i  = CostsString.find("DOUBLE");
            std::size_t quad_i  = CostsString.find("QUAD");
            std::size_t fp80_i  = CostsString.find("FP80");
            std::size_t ppc128_i  = CostsString.find("PPC128");
            std::size_t half_i  = CostsString.find("HALF");
            std::size_t bf16_i  = CostsString.find("BF16");
            LLVM_DEBUG(dbgs()<< "C"<<std::to_string(counter2)<<"\n");
            if(!hasHalf && half_i != std::string::npos) continue;
            if(!hasQuad && quad_i != std::string::npos) continue;
            if(!hasFP80 && fp80_i != std::string::npos) continue;
            if(!hasPPC128 && ppc128_i != std::string::npos) continue;
            if(!hasBF16 && bf16_i != std::string::npos) continue;

            if (fixed_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getFixedSelectedVariable; first_i = fixed_i; first_c = "Fixed";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getFixedSelectedVariable; second_i = fixed_i; second_c = "Fixed";}
            }
            if (float_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getFloatSelectedVariable; first_i = float_i; first_c = "Float";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getFloatSelectedVariable; second_i = float_i; second_c = "Float";}
            }
            if (double_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getDoubleSelectedVariable; first_i = double_i; first_c = "Double";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getDoubleSelectedVariable; second_i = double_i; second_c = "Double";}
            }
            if (quad_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getQuadSelectedVariable; first_i = quad_i; first_c = "Quad";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getQuadSelectedVariable; second_i = quad_i; second_c = "Quad";}
            }
            if (fp80_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getFP80SelectedVariable; first_i = fp80_i; first_c = "FP80";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getFP80SelectedVariable; second_i = fp80_i; second_c = "FP80";}
            }
            if (ppc128_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getPPC128SelectedVariable; first_i = ppc128_i; first_c = "PPC128";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getPPC128SelectedVariable; second_i = ppc128_i; second_c = "PPC128";}
            }
            if (half_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getHalfSelectedVariable; first_i = half_i; first_c = "Half";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getHalfSelectedVariable; second_i = half_i; second_c = "Half";}
            }
            if (bf16_i != std::string::npos){
                if (first_f == nullptr) {first_f = &tuner::OptimizerScalarInfo::getBF16SelectedVariable; first_i = half_i; first_c = "bf16";}
                else                    {second_f = &tuner::OptimizerScalarInfo::getBF16SelectedVariable; second_i = half_i; second_c = "bf16";}
            }            


            if(first_i > second_i){
                std::swap(first_f,second_f);
                std::swap(first_c,second_c);
            }

            auto CX = std::string("C") + std::to_string(counter2) + "_" + varName;
            counter2++;

            model.createVariable(CX, 0, 1);

            LLVM_DEBUG(llvm::dbgs() << "Inserting constraint " << CostsString << " first " << first_c << " second " << second_c << " wtih desc " << std::string(first_c) + " to " + std::string(second_c) << "\n" );

            costcrosslambda(CX, cpuCosts.decodeId(CostsString), first_f, 
                        second_f, std::string(first_c) + " to " + std::string(second_c));

                
            
        }
    }
    auto CX = std::string("C") + std::to_string(counter2) + "_" + varName;
    model.createVariable(CX, 0, 1);
    costcrosslambda(CX, cpuCosts.CAST_FIX_FIX, &tuner::OptimizerScalarInfo::getFixedSelectedVariable, &tuner::OptimizerScalarInfo::getFixedSelectedVariable
            ,"Fix to Fix");
    
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


    auto eqconstraintlambda = [&](const string (tuner::OptimizerScalarInfo::*getFirstVariable)(), const std::string desc) mutable {
    constraint.clear();
    constraint.push_back(make_pair(((*op1).*getFirstVariable)(), 1.0));
    constraint.push_back(make_pair(((*op2).*getFirstVariable)(), -1.0));
    model.insertLinearConstraint(constraint, Model::EQ, 0, desc);
    };

    eqconstraintlambda(&tuner::OptimizerScalarInfo::getFixedSelectedVariable,"fix equality");

    eqconstraintlambda(&tuner::OptimizerScalarInfo::getFloatSelectedVariable,"float equality");

    eqconstraintlambda(&tuner::OptimizerScalarInfo::getDoubleSelectedVariable,"double equality");
   
    if(hasHalf)
    eqconstraintlambda(&tuner::OptimizerScalarInfo::getHalfSelectedVariable,"Half equality");

    if(hasQuad)
    eqconstraintlambda(&tuner::OptimizerScalarInfo::getQuadSelectedVariable,"Quad equality");

    if(hasPPC128)
    eqconstraintlambda(&tuner::OptimizerScalarInfo::getPPC128SelectedVariable,"PPC128 equality");

    if(hasFP80)
    eqconstraintlambda(&tuner::OptimizerScalarInfo::getFP80SelectedVariable,"FP80 equality");

    if(hasBF16)
    eqconstraintlambda(&tuner::OptimizerScalarInfo::getBF16SelectedVariable,"FP80 equality");

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
        case mdutils::FloatType::Float_half:
            fractionalDigits = llvm::APFloat::semanticsPrecision(llvm::APFloat::IEEEhalf()) - 1;
            minExponentPower = llvm::APFloat::semanticsMinExponent(llvm::APFloat::IEEEhalf());
            break;        
        case mdutils::FloatType::Float_float:
            fractionalDigits = llvm::APFloat::semanticsPrecision(llvm::APFloat::IEEEsingle()) - 1;
            minExponentPower = llvm::APFloat::semanticsMinExponent(llvm::APFloat::IEEEsingle());
            break;
        case mdutils::FloatType::Float_double:
            fractionalDigits = llvm::APFloat::semanticsPrecision(llvm::APFloat::IEEEdouble()) - 1;
            minExponentPower = llvm::APFloat::semanticsMinExponent(llvm::APFloat::IEEEdouble());
            break;
        case mdutils::FloatType::Float_bfloat:
            fractionalDigits = llvm::APFloat::semanticsPrecision(llvm::APFloat::BFloat()) - 1;
            minExponentPower = llvm::APFloat::semanticsMinExponent(llvm::APFloat::BFloat());
            break;
        case mdutils::FloatType::Float_fp128:
            fractionalDigits = llvm::APFloat::semanticsPrecision(llvm::APFloat::IEEEquad()) - 1;
            minExponentPower = llvm::APFloat::semanticsMinExponent(llvm::APFloat::IEEEquad());
            break;
        case mdutils::FloatType::Float_ppc_fp128:
            fractionalDigits = llvm::APFloat::semanticsPrecision(llvm::APFloat::PPCDoubleDouble()) - 1;
            minExponentPower = llvm::APFloat::semanticsMinExponent(llvm::APFloat::PPCDoubleDouble());
            break;
        case mdutils::FloatType::Float_x86_fp80:
            fractionalDigits = llvm::APFloat::semanticsPrecision(llvm::APFloat::x87DoubleExtended()) - 1;
            minExponentPower = llvm::APFloat::semanticsMinExponent(llvm::APFloat::x87DoubleExtended());
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
        function = instr->getFunction()->getName().str();
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
    }else if(info->getKind() == OptimizerInfo::K_Pointer){
        auto apr = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(info);
        dbgs() << "Unwrapping pointer...\n";
        return buildDataHierarchy(apr->getOptInfo());
    }

    if(!info){
        dbgs() << "OptimizerInfo null!\n";
    }else{
        dbgs() << "Unknown OptimizerInfo: " << info->toString() << "\n";
    }
    llvm_unreachable("Unnknown data type");
}

shared_ptr<mdutils::TType> Optimizer::modelvarToTType(shared_ptr<OptimizerScalarInfo> scalarInfo) {
    if (!scalarInfo) {
        dbgs() << "Nullptr scalar info!";
        return nullptr;
    }
    LLVM_DEBUG(dbgs() << "\nmodel var values\n" );
    double selectedFixed = model.getVariableValue(scalarInfo->getFixedSelectedVariable());
    LLVM_DEBUG(dbgs() << scalarInfo->getFixedSelectedVariable() << " " << selectedFixed << "\n" );
    double selectedFloat = model.getVariableValue(scalarInfo->getFloatSelectedVariable());
    LLVM_DEBUG(dbgs() << scalarInfo->getFloatSelectedVariable() << " " << selectedFloat << "\n" );
    double selectedDouble = model.getVariableValue(scalarInfo->getDoubleSelectedVariable());
    LLVM_DEBUG(dbgs() << scalarInfo->getDoubleSelectedVariable() << " " << selectedDouble << "\n" );
    double selectedHalf = 0;
    double selectedFP80 = 0;
    double selectedPPC128 = 0;
    double selectedQuad = 0;
    double selectedBF16 = 0;


    if(hasHalf){
     selectedHalf = model.getVariableValue(scalarInfo->getHalfSelectedVariable());
    LLVM_DEBUG(dbgs() << scalarInfo->getHalfSelectedVariable() << " " << selectedHalf << "\n" );
    }
    if(hasQuad){
     selectedQuad = model.getVariableValue(scalarInfo->getQuadSelectedVariable());
    LLVM_DEBUG(dbgs() << scalarInfo->getQuadSelectedVariable() << " " << selectedQuad << "\n" );
    }
    if(hasPPC128){
     selectedPPC128 = model.getVariableValue(scalarInfo->getPPC128SelectedVariable());
    LLVM_DEBUG(dbgs() << scalarInfo->getPPC128SelectedVariable() << " " << selectedPPC128 << "\n" );
    }
    if(hasFP80){
     selectedFP80 = model.getVariableValue(scalarInfo->getFP80SelectedVariable());
    LLVM_DEBUG(dbgs() << scalarInfo->getFP80SelectedVariable() << " " << selectedFP80 << "\n" );
    }   
    if(hasBF16){
    selectedBF16 = model.getVariableValue(scalarInfo->getBF16SelectedVariable());   
    LLVM_DEBUG(dbgs() << scalarInfo->getBF16SelectedVariable() << " " << selectedBF16 << "\n" );
    }


    double fracbits = model.getVariableValue(scalarInfo->getFractBitsVariable());
    
    assert(selectedDouble + selectedFixed + selectedFloat + selectedHalf + selectedFP80 + selectedPPC128 + selectedQuad + selectedBF16 == 1 &&
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


    if (selectedHalf == 1) {
        StatSelectedHalf++;
        return make_shared<mdutils::FloatType>(FloatType::Float_half, 0);
    }

    if (selectedQuad == 1) {
        StatSelectedQuad++;
        return make_shared<mdutils::FloatType>(FloatType::Float_fp128, 0);
    }

    if (selectedPPC128 == 1) {
        StatSelectedPPC128++;
        return make_shared<mdutils::FloatType>(FloatType::Float_ppc_fp128, 0);
    }

    if (selectedFP80 == 1) {
        StatSelectedFP80++;
        return make_shared<mdutils::FloatType>(FloatType::Float_x86_fp80, 0);
    }

    if (selectedBF16 == 1) {
        StatSelectedBF16++;
        return make_shared<mdutils::FloatType>(FloatType::Float_bfloat, 0);
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
    dbgs() << "Converted to half: " << StatSelectedHalf << "\n";

    int total = StatSelectedFixed + StatSelectedFloat + StatSelectedDouble + StatSelectedHalf;

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
    statFile << "TOHALF, " << StatSelectedHalf << "\n";
    statFile << "COSTENOB, " << model.costEnob << "\n";
    statFile << "COSTCAST, " << model.costCast << "\n";
    statFile << "COSTTIME, " << model.costTime << "\n";
    statFile.flush();
    statFile.close();

}







