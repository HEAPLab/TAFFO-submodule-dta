#include <limits>
#include <llvm/IR/CallSite.h>
#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Constants.h"
#include "llvm/ADT/SmallPtrSet.h"
#include "llvm/Support/Debug.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"


#ifndef __TAFFO_TUNER_PASS_H__
#define __TAFFO_TUNER_PASS_H__


namespace tuner {

struct TaffoTuner : public llvm::ModulePass {
  static char ID;

  TaffoTuner(): ModulePass(ID) { }
  bool runOnModule(llvm::Module &M) override;

};


}


#endif

