#include "Optimizer.h"

using namespace tuner;
using namespace mdutils;


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