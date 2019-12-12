#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/ADT/DenseMap.h"
#include "llvm/ADT/SmallPtrSet.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"
#include "InputInfo.h"
#include "Metadata.h"
#include "TypeUtils.h"

#ifndef __TAFFO_TUNER_PASS_H__
#define __TAFFO_TUNER_PASS_H__

#define DEBUG_TYPE "taffo-dta"
#define DEBUG_FUN  "tunerfunction"


llvm::cl::opt<int> FracThreshold("minfractbits", llvm::cl::value_desc("bits"),
    llvm::cl::desc("Threshold of fractional bits in fixed point numbers"), llvm::cl::init(3));
llvm::cl::opt<int> TotalBits("totalbits", llvm::cl::value_desc("bits"),
    llvm::cl::desc("Total amount of bits in fixed point numbers"), llvm::cl::init(32));
llvm::cl::opt<int> SimilarBits("similarbits", llvm::cl::value_desc("bits"),
    llvm::cl::desc("Maximum number of difference bits that leads two fixp formats to merge"), llvm::cl::init(2));
llvm::cl::opt<bool> DisableTypeMerging("notypemerge",
    llvm::cl::desc("Disables adjacent type optimization"), llvm::cl::init(false));


STATISTIC(FixCast, "Number of fixed point format cast");


namespace tuner {

struct TaffoTuner : public llvm::ModulePass {
  static char ID;

  TaffoTuner(): ModulePass(ID) { }
  bool runOnModule(llvm::Module &M) override;
};

}


#endif

