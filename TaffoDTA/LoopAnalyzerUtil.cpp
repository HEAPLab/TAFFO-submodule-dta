//
// Created by nicola on 07/08/20.
//

#include <llvm/IR/Instruction.h>
#include <llvm/Support/Debug.h>
#include <llvm/Analysis/LoopInfo.h>
#include <llvm/Analysis/ScalarEvolution.h>
#include "LoopAnalyzerUtil.h"


using namespace llvm;

unsigned LoopAnalyzerUtil::computeFullTripCount(ModulePass *tuner, Instruction *instruction) {
    auto bb = instruction->getParent();
    auto f = instruction->getParent()->getParent();
    auto loop = tuner->getAnalysis<LoopInfoWrapperPass>(*f).getLoopInfo().getLoopFor(bb);

    unsigned info;
    info = computeFullTripCount(tuner, loop);

    dbgs() << "Total trip count: " << info << "\n";
    return info;
}

unsigned LoopAnalyzerUtil::computeFullTripCount(ModulePass *tuner, Loop *loop) {
    if (loop) {
        auto scev = tuner->getAnalysis<ScalarEvolutionWrapperPass>(
                *loop->getHeader()->getParent()).getSE().getSmallConstantTripCount(loop);
        dbgs() << "Got SCEV " << scev << "; looking for nested loops...\n";
        return scev * computeFullTripCount(tuner, loop->getParentLoop());
    } else {
        dbgs() << "Loop Info: loop is null! Not part of a loop, finishing search!\n";
        return 1;
    }

}