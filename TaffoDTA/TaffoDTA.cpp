#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/InstIterator.h"
#include "llvm/IR/Metadata.h"
#include "llvm/Support/Debug.h"

#include "TaffoDTA.h"
#include "Metadata.h"


using namespace llvm;
using namespace tuner;
using namespace mdutils;
using namespace taffo;


char TaffoTuner::ID = 0;

static RegisterPass<TaffoTuner> X(
  "taffodta",
  "TAFFO Framework Data Type Allocation",
  false /* does not affect the CFG */,
  true /* Optimization Pass */);


bool TaffoTuner::runOnModule(Module &m)
{
  return true;
}


