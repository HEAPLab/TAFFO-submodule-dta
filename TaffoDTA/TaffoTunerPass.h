#include <limits>
#include <llvm/IR/CallSite.h>
#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Constants.h"
#include "llvm/ADT/SmallPtrSet.h"
#include "llvm/Support/Debug.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"
#include "InputInfo.h"

#ifndef __TAFFO_TUNER_PASS_H__
#define __TAFFO_TUNER_PASS_H__

#define DEBUG_TYPE "taffo-tuner"
#define DEBUG_FUN  "tunerfunction"


llvm::cl::opt<int> FracThreshold("minfractbits", llvm::cl::value_desc("bits"),
    llvm::cl::desc("Threshold of fractional bits in fixed point numbers"), llvm::cl::init(3));
llvm::cl::opt<int> TotalBits("totalbits", llvm::cl::value_desc("bits"),
    llvm::cl::desc("Total amount of bits in fixed point numbers"), llvm::cl::init(32));
llvm::cl::opt<int> SimilarBits("similarbits", llvm::cl::value_desc("bits"),
    llvm::cl::desc("Maximum number of difference bits that leads two fixp formats to merge"), llvm::cl::init(2));

STATISTIC(FixCast, "Number of fixed point format cast");


namespace tuner {

  struct ValueInfo {
    std::shared_ptr<mdutils::MDInfo> metadata;
  };

  struct FunInfo {
    llvm::Function* newFun;
    /* {function argument index, type of argument}
     * argument idx is -1 for return value */
    std::vector<std::pair<int, std::shared_ptr<mdutils::MDInfo>>> fixArgs;
  };


  struct TaffoTuner : public llvm::ModulePass {
    static char ID;

    /* to not be accessed directly, use valueInfo() */
    llvm::DenseMap<llvm::Value *, std::shared_ptr<ValueInfo>> info;
    
    /* original function -> cloned function map */
    llvm::DenseMap<llvm::Function*, std::vector<FunInfo>> functionPool;

    TaffoTuner(): ModulePass(ID) { }
    bool runOnModule(llvm::Module &M) override;

    void retrieveAllMetadata(llvm::Module &m, std::vector<llvm::Value *> &vals);
    bool processMetadataOfValue(llvm::Value *v, mdutils::MDInfo *MDI);
    bool associateFixFormat(mdutils::InputInfo& rng);
    void sortQueue(std::vector<llvm::Value*> &vals);
    void mergeFixFormat(std::vector<llvm::Value*> &vals);
    std::vector<llvm::Function*> collapseFunction(llvm::Module &m);
    llvm::Function *findEqFunction(llvm::Function *fun, llvm::Function *origin);
    void attachFPMetaData(std::vector<llvm::Value*> &vals);
    void attachFunctionMetaData(llvm::Module &m);


    std::shared_ptr<ValueInfo> valueInfo(llvm::Value *val) {
      auto vi = info.find(val);
      if (vi == info.end()) {
        info[val] = std::make_shared<ValueInfo>(ValueInfo());
        return info[val];
      } else {
        return vi->getSecond();
      }
    };

    bool hasInfo(llvm::Value *val) {
      return info.find(val) != info.end();
    };
  };


}


#endif

