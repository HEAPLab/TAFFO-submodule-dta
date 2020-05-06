#include <set>
#include <fstream>
#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/ADT/DenseMap.h"
#include "llvm/ADT/SmallPtrSet.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"
#include "InputInfo.h"
#include "Metadata.h"
#include "TypeUtils.h"
#include "Infos.h"
#include "OptimizerInfo.h"
#include "Model.h"

#ifndef __TAFFO_DTA_OPTIMIZER_H__
#define __TAFFO_DTA_OPTIMIZER_H__

using namespace llvm;

namespace tuner {
    template<class T, class U>
    std::shared_ptr<T> dynamic_ptr_cast_or_null(const std::shared_ptr<U> &r) noexcept {
        if (auto p = llvm::dyn_cast_or_null<typename std::shared_ptr<T>::element_type>(r.get())) {
            return std::shared_ptr<T>(r, p);
        } else {
            return std::shared_ptr<T>();
        }
    }

    class Optimizer {

        DenseMap<llvm::Value *, std::shared_ptr<OptimizerInfo>> valueToVariableName;
        Model model;

    public:
        void handleInstruction(Instruction * instruction, shared_ptr <ValueInfo> valueInfo);
        void handleGlobal(GlobalObject * glob, shared_ptr<ValueInfo> valueInfo);
        void finish();

        Optimizer() : model(Model::MIN){

        }


    protected:
        string allocateNewVariableForValue(Value* value, unsigned minBits, unsigned maxBits,  string functionName);


        void emitError(const string stringhina);

        void handleAlloca(Instruction *instruction, shared_ptr<ValueInfo> valueInfo);

        void handleLoad(Instruction *instruction, const shared_ptr<ValueInfo>& valueInfo);

        shared_ptr<OptimizerInfo> getInfoOfValue(Value *value);

        void
        handleBinaryInstruction(Instruction *instr, const unsigned int OpCode, const shared_ptr<ValueInfo> &valueInfos);

        void handleFAdd(BinaryOperator *instr, const unsigned int OpCode, const shared_ptr<ValueInfo> &valueInfos);

        string allocateNewVariableWithCastCost(Value *toUse, Value *whereToUse);


        void handleStore(Instruction *instruction, const shared_ptr<ValueInfo> &valueInfo);

        void handleFPPrecisionShift(Instruction *instruction, shared_ptr<ValueInfo> valueInfo);


    };








}

#endif