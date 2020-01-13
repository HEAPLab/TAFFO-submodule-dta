#include <utility>
#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/InstIterator.h"
#include "llvm/IR/Metadata.h"
#include "llvm/Analysis/CallGraph.h"
#include "llvm/Support/Debug.h"
#include "llvm/Support/Format.h"
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


void TaffoTuner::getAnalysisUsage(AnalysisUsage &AU) const
{
  AU.addRequiredTransitive<CallGraphWrapperPass>();
  AU.setPreservesAll();
}


bool TaffoTuner::runOnModule(Module &M)
{
  CallGraphWrapperPass &CGWP = this->getAnalysis<CallGraphWrapperPass>();
  CallGraph &CG = CGWP.getCallGraph();
  
  const CallGraphNode *Root = GraphTraits<const CallGraph *>::getEntryNode(&CG);
  SmallVector<std::pair<const CallGraphNode *, int>, 16> BFSQueue = {{Root, 0}};
  while (!BFSQueue.empty()) {
    std::pair<const CallGraphNode *, int> CurNode = BFSQueue.pop_back_val();
    FormattedString indentation = FormattedString("", CurNode.second, FormattedString::JustifyLeft);
    if (CurNode.first->getFunction() != nullptr)
      LLVM_DEBUG(dbgs() << indentation << CurNode.first->getFunction()->getName() << "\n");
    else
      LLVM_DEBUG(dbgs() << indentation << "(null)" << "\n");
    SmallDenseSet<std::pair<const CallGraphNode *, int>, 16> Children;
    for (auto Call: *CurNode.first) {
      if (Call.first)
        LLVM_DEBUG(dbgs() << indentation << "[CALL] " << *Call.first << "\n");
      Children.insert({Call.second, CurNode.second + 1});
    }
    BFSQueue.insert(BFSQueue.end(), Children.begin(), Children.end());
  }
  
  return true;
}


