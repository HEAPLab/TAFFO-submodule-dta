#include "Optimizer.h"

using namespace tuner;

void MemWatcher::openPhiLoop(LoadInst *load, Value *requestedValue) {
    if (pairsToClose.find(requestedValue) == pairsToClose.end()) {
        pairsToClose.insert(make_pair(requestedValue, vector<LoadInst *>()));
    }

    pairsToClose[requestedValue].push_back(load);
}


LoadInst *MemWatcher::getPhiNodeToClose(Value *value) {
    auto workingEntry = pairsToClose.find(value);
    if ( workingEntry == pairsToClose.end()) {
        return nullptr;
    }

    return workingEntry->getSecond().begin().operator*();
}

void MemWatcher::closePhiLoop(LoadInst *phiNode, Value *requestedValue) {
    auto workingEntry = pairsToClose.find(requestedValue);
    if ( workingEntry == pairsToClose.end()) {
        llvm_unreachable("Tried to close an already closed memLoop!");
    }

    auto toDelete = std::find(workingEntry->getSecond().begin(),
                              workingEntry->getSecond().end(),
                              phiNode);
    workingEntry->getSecond().erase(toDelete);

    if(workingEntry->getSecond().empty()){
        pairsToClose.erase(workingEntry);
    }


}

void MemWatcher::dumpState() {
    if(pairsToClose.empty()){
        dbgs() << "All Mem loops closed!\n";
    }
    for(auto pair :pairsToClose){
        pair.first->print(dbgs());
        dbgs() << " STILL MISSING; will close:\n";
        for(auto a : pair.second){
            a->print(dbgs());
            dbgs() << "\n";
        }
    }

}
