#include "Optimizer.h"

using namespace tuner;
using namespace mdutils;

//FIXME: replace with a dynamic version!
#define I_COST 1

void
Optimizer::handleBinaryInstruction(Instruction *instr, const unsigned OpCode, const shared_ptr<ValueInfo> &valueInfos) {
    //We are only handling operations between floating point, as we do not care about other values when building the model
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
            handleFSub(binop, OpCode, valueInfos);
            break;
            //case llvm::Instruction::Mul:
        case llvm::Instruction::FMul:
            //return handleMul(op1, op2, destRange);
            handleFMul(binop, OpCode, valueInfos);
            break;
            //case llvm::Instruction::UDiv:
            //case llvm::Instruction::SDiv:
        case llvm::Instruction::FDiv:
            //return handleDiv(op1, op2, destRange);
            handleFDiv(binop, OpCode, valueInfos);
            break;
            //case llvm::Instruction::URem:
            //case llvm::Instruction::SRem:
        case llvm::Instruction::FRem:
            //return handleRem(op1, op2, destRange);
            handleFRem(binop, OpCode, valueInfos);
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

    auto res = handleBinOpCommon(instr, op1, op2, true, valueInfos);
    if(!res) return;

    model.insertObjectiveElement(make_pair(res->getFixedSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::ADD_FIX)));
    model.insertObjectiveElement(make_pair(res->getFloatSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::ADD_FLOAT)));
    model.insertObjectiveElement(make_pair(res->getDoubleSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::ADD_DOUBLE)));

    //Precision cost
    //Handloed in allocating variable

}


void Optimizer::handleFSub(BinaryOperator *instr, const unsigned OpCode, const shared_ptr<ValueInfo> &valueInfos) {
    assert(instr->getOpcode() == llvm::Instruction::FSub && "Operand mismatch!");

    auto op1 = instr->getOperand(0);
    auto op2 = instr->getOperand(1);

    auto res = handleBinOpCommon(instr, op1, op2, true, valueInfos);
    if(!res) return;

    model.insertObjectiveElement(make_pair(res->getFixedSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::SUB_FIX)));
    model.insertObjectiveElement(make_pair(res->getFloatSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::SUB_FLOAT)));
    model.insertObjectiveElement(make_pair(res->getDoubleSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::SUB_DOUBLE)));

    //Precision cost
    //Handloed in allocating variable

}

void Optimizer::handleFMul(BinaryOperator *instr, const unsigned OpCode, const shared_ptr<ValueInfo> &valueInfos) {
    assert(instr->getOpcode() == llvm::Instruction::FMul && "Operand mismatch!");

    auto op1 = instr->getOperand(0);
    auto op2 = instr->getOperand(1);


    auto res = handleBinOpCommon(instr, op1, op2, false, valueInfos);
    if(!res) return;

    model.insertObjectiveElement(make_pair(res->getFixedSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::MUL_FIX)));
    model.insertObjectiveElement(make_pair(res->getFloatSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::MUL_FLOAT)));
    model.insertObjectiveElement(make_pair(res->getDoubleSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::MUL_DOUBLE)));

    //Precision cost
    //Handloed in allocating variable

}

void Optimizer::handleFDiv(BinaryOperator *instr, const unsigned OpCode, const shared_ptr<ValueInfo> &valueInfos) {
    assert(instr->getOpcode() == llvm::Instruction::FDiv && "Operand mismatch!");

    auto op1 = instr->getOperand(0);
    auto op2 = instr->getOperand(1);


    auto res = handleBinOpCommon(instr, op1, op2, false, valueInfos);
    if(!res) return;

    model.insertObjectiveElement(make_pair(res->getFixedSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::DIV_FIX)));
    model.insertObjectiveElement(make_pair(res->getFloatSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::DIV_FLOAT)));
    model.insertObjectiveElement(make_pair(res->getDoubleSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::DIV_DOUBLE)));
    //Precision cost
    //Handloed in allocating variable

}

void Optimizer::handleFRem(BinaryOperator *instr, const unsigned OpCode, const shared_ptr<ValueInfo> &valueInfos) {
    assert(instr->getOpcode() == llvm::Instruction::FRem && "Operand mismatch!");

    auto op1 = instr->getOperand(0);
    auto op2 = instr->getOperand(1);


    auto res = handleBinOpCommon(instr, op1, op2, false, valueInfos);

    if(!res) return;

    model.insertObjectiveElement(make_pair(res->getFixedSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::REM_FIX)));
    model.insertObjectiveElement(make_pair(res->getFloatSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::REM_FLOAT)));
    model.insertObjectiveElement(make_pair(res->getDoubleSelectedVariable(), I_COST * cpuCosts.getCost(CPUCosts::REM_DOUBLE)));
    //Precision cost
    //Handloed in allocating variable

}

shared_ptr<OptimizerScalarInfo> Optimizer::handleBinOpCommon(Instruction* instr, Value * op1, Value * op2, bool forceFixEquality, shared_ptr<ValueInfo> valueInfos){
    auto info1 = getInfoOfValue(op1);
    auto info2 = getInfoOfValue(op2);

    if (!info1 || !info2) {
        dbgs() << "One of the two values does not have info, ignoring...\n";
        return nullptr;
    }

    auto inputInfo = dynamic_ptr_cast_or_null<InputInfo>(valueInfos->metadata);
    if (!inputInfo) {
        dbgs() << "No info on destination, bailing out, bug in VRA?\n";
        return nullptr;
    }

    auto fptype = dynamic_ptr_cast_or_null<FPType>(inputInfo->IType);
    if (!fptype) {
        dbgs() << "No fixed point info associated. Bailing out.\n";
        return nullptr;
    }


    shared_ptr<OptimizerScalarInfo> varCast1 = allocateNewVariableWithCastCost(op1, instr);
    shared_ptr<OptimizerScalarInfo> varCast2 = allocateNewVariableWithCastCost(op2, instr);



    //Obviously the type should be sufficient to contain the result
    shared_ptr<OptimizerScalarInfo> result = allocateNewVariableForValue(instr, fptype, inputInfo->IRange,
                                                                         instr->getFunction()->getName());

    insertTypeEqualityConstraint(varCast1, varCast2, forceFixEquality);
    insertTypeEqualityConstraint(varCast1, result, forceFixEquality);

    return result;
}