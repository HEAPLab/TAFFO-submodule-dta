#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/InstIterator.h"
#include "llvm/IR/Metadata.h"
#include "llvm/Support/Debug.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Support/raw_ostream.h"
#include "TaffoTunerPass.h"

#include "Metadata.h"


using namespace llvm;
using namespace tuner;

char TaffoTuner::ID = 0;

static RegisterPass<TaffoTuner> X(
  "taffotuner",
  "TAFFO Framework Data Type Allocation",
  false /* does not affect the CFG */,
  true /* Optimization Pass */);

bool TaffoTuner::runOnModule(Module &m)
{
  std::vector<Value*> vals;
  retrieveValue(m, vals);

  mergeFixFormat(vals);

  std::vector<Function*> toDel;
  toDel = collapseFunction(m);

  attachFPMetaData(vals);
  attachFunctionMetaData(m);

  for (Function *f : toDel)
    f->eraseFromParent();

  return true;
}


void TaffoTuner::retrieveValue(Module &m, std::vector<Value *> &vals) {

  mdutils::MetadataManager &MDManager = mdutils::MetadataManager::getMetadataManager();

  for (GlobalObject &globObj : m.globals()) {
    if (mdutils::InputInfo *II = MDManager.retrieveInputInfo(globObj)) {
      if (parseMDRange(&globObj, II)) {
        valueInfo(&globObj)->fixpType = associateFixFormat(valueInfo(&globObj)->rangeError);
        vals.push_back(&globObj);
      }
    }
  }

  for (Function &f : m.functions()) {
    SmallVector<mdutils::InputInfo*, 5> argsII;
    MDManager.retrieveArgumentInputInfo(f, argsII);
    auto arg = f.arg_begin();
    for (mdutils::InputInfo* II : argsII) {
      if (parseMDRange(arg, II)) {
        valueInfo(arg)->fixpType = associateFixFormat(valueInfo(arg)->rangeError);
        vals.push_back(arg);
      }
      arg++;
    }

    for (inst_iterator iIt = inst_begin(&f), iItEnd = inst_end(&f); iIt != iItEnd; iIt++) {
      if (mdutils::InputInfo *II = MDManager.retrieveInputInfo(*iIt)) {
        if (parseMDRange(&*iIt, II)) {
          valueInfo(&*iIt)->fixpType = associateFixFormat(valueInfo(&*iIt)->rangeError);
          vals.push_back(&*iIt);
        }
      }
    }
  }

  sortQueue(vals);
}


bool TaffoTuner::parseMDRange(Value *v, mdutils::InputInfo *II) {
  mdutils::Range* rng = II->IRange;
  if (rng!=nullptr && !std::isnan(rng->Max) && !std::isnan(rng->Min)) {
    valueInfo(v)->rangeError.Max = rng->Max;
    valueInfo(v)->rangeError.Min = rng->Min;
    return true;
  } else {
    return false;
  }
}


FixedPointType TaffoTuner::associateFixFormat(RangeError rng) {
  FixedPointType fp;
  fp.isSigned = rng.Min < 0;

  int max = std::max(std::abs(rng.Min), std::abs(rng.Max));
  int intBit = std::ceil(std::log2(max+1)) + (fp.isSigned ? 1 : 0);

  fp.bitsAmt = TotalBits;
  fp.fracBitsAmt = fp.bitsAmt - intBit;

  //Check dimension
  if (fp.fracBitsAmt < FracThreshold) {
    dbgs() << "[WARNING] Fractional part is too small !\n";
    fp.fracBitsAmt = 0;
    if (intBit > fp.bitsAmt) {
      dbgs() << "[WARNING] Overflow may occurs !\n";
    }
  }
  return fp;
}


void TaffoTuner::sortQueue(std::vector<llvm::Value *> &vals) {
  size_t next = 0;
  while (next < vals.size()) {
    Value *v = vals.at(next);

    for (auto *u: v->users()) {

      /* Insert u at the end of the queue.
       * If u exists already in the queue, *move* it to the end instead. */
      for (int i=0; i<vals.size();) {
        if (vals[i] == u) {
          vals.erase(vals.begin() + i);
          if (i < next)
            next--;
        } else {
          i++;
        }
      }

      if (Instruction *inst = dyn_cast<Instruction>(u)) {
        if (inst->getMetadata(INPUT_INFO_METADATA)) {
          vals.push_back(u);
          if (!hasInfo(u)) {
            dbgs() << "[WARNING] Find Value without range!\n";
            valueInfo(u)->rangeError = valueInfo(v)->rangeError;
            valueInfo(u)->fixpType = associateFixFormat(valueInfo(v)->rangeError);
          }
        } else {
          dbgs() << "[WARNING] Find Value without TAFFO info!\n";
        }

      } else if (GlobalObject *go = dyn_cast<GlobalObject>(u)) {
        if (go->getMetadata(INPUT_INFO_METADATA)) {
          vals.push_back(u);
          if (!hasInfo(u)) {
            dbgs() << "[WARNING] Find Value without range!\n";
            valueInfo(u)->rangeError = valueInfo(v)->rangeError;
            valueInfo(u)->fixpType = associateFixFormat(valueInfo(v)->rangeError);
          }
        } else {
          dbgs() << "[WARNING] Find Value without TAFFO info!\n";
        }
      }

    }
    next++;
  }
}


void TaffoTuner::mergeFixFormat(std::vector<llvm::Value *> &vals) {
  bool merged = false;
  for (Value *v : vals) {
    for (Value *u: v->users()) {
      if (std::find(vals.begin(),vals.end(),u) != vals.end()) {
        FixedPointType *fpv = &valueInfo(v)->fixpType;
        FixedPointType *fpu = &valueInfo(u)->fixpType;
        if (!(*fpv == *fpu)) {
          if (fpv->bitsAmt == fpu->bitsAmt &&
              std::abs(fpv->fracBitsAmt - fpu->fracBitsAmt)
              + (fpv->isSigned == fpu->isSigned ? 0 : 1) <= SimilarBits) {

            FixedPointType fp(fpv->isSigned || fpu->isSigned,
                              std::min(fpv->fracBitsAmt, fpu->fracBitsAmt),
                              fpv->bitsAmt);
            DEBUG(dbgs() << "Merged fixp : \n"
                         << "\t" << *v << " fix type " << *fpv << "\n"
                         << "\t" << *u << " fix type " << *fpu << "\n"
                         << "Final format " << fp << "\n";);

            valueInfo(v)->fixpType = fp;
            valueInfo(u)->fixpType = fp;

            if (Argument *arg =  dyn_cast<Argument>(v)) {
              Function *fun =  arg->getParent();
              int n = arg->getArgNo();
              for (auto it = fun->user_begin(); it != fun->user_end(); it++) {
                if (isa<CallInst>(*it) || isa<InvokeInst>(*it)) {
                  DEBUG(dbgs() << "Argument " << *arg << " nr. " << n
                               << " propagate fix type merge on callsite " << **it << "\n";);
                  valueInfo(it->getOperand(n))->fixpType = fp;
                }
              }
            }

            merged = true;
          } else {
            FixCast++;
          }
        }
      }
    }
  }
  if (merged)
    mergeFixFormat(vals);
}


std::vector<Function*> TaffoTuner::collapseFunction(Module &m) {
  std::vector<Function*> toDel;
  for (Function &f : m.functions()) {
    if (MDNode *mdNode = f.getMetadata(CLONED_FUN_METADATA)) {
      if (std::find(toDel.begin(), toDel.end(), &f) != toDel.end())
        continue;
      DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "Analyzing original function " << f.getName() << "\n";);

      for (auto mdIt = mdNode->op_begin(); mdIt != mdNode->op_end(); mdIt++) {
        DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t Clone : " << **mdIt << "\n";);

        ValueAsMetadata *md = dyn_cast<ValueAsMetadata>(*mdIt);
        Function *fClone = dyn_cast<Function>(md->getValue());
        if (Function *eqFun = findEqFunction(fClone, &f)) {
          DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t Replace function " << fClone->getName()
            << " with " << eqFun->getName() << "\n";);
          fClone->replaceAllUsesWith(eqFun);
          toDel.push_back(fClone);
        }

      }
    }
  }
  return toDel;
}


Function* TaffoTuner::findEqFunction(Function *fun, Function *origin) {
  std::vector<std::pair<int,FixedPointType>> fixSign;

  DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Search eq function for " << fun->getName()
    << " in " << origin->getName() << " pool\n";);

  if(isFloatType(fun->getReturnType())) {
    fixSign.push_back(std::pair<int, FixedPointType>
        (-1, valueInfo(*fun->user_begin())->fixpType) ); //ret value in signature
    DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Return type : "
        << valueInfo(*fun->user_begin())->fixpType << "\n";);
  }

  int i=0;
  for (Argument &arg : fun->args()) {
    if (hasInfo(&arg)) {
      fixSign.push_back(std::pair<int, FixedPointType>(i,valueInfo(&arg)->fixpType));
      DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Arg "<< i << " type : "
          << valueInfo(&arg)->fixpType << "\n";);
    }
    i++;
  }

  for (FunInfo fi : functionPool[origin]) {
    if (fi.fixArgs == fixSign) {
      return fi.newFun;
    }
  }

  FunInfo funInfo;
  funInfo.newFun = fun;
  funInfo.fixArgs = fixSign;
  functionPool[origin].push_back(funInfo);
  DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t Function " << fun->getName() << " used\n";);
  return nullptr;
}


void TaffoTuner::attachFPMetaData(std::vector<llvm::Value *> &vals) {
  mdutils::MetadataManager &MDManager = mdutils::MetadataManager::getMetadataManager();

  for (Value *v : vals) {
    assert(info[v] && "Every value should have info");
    FixedPointType fpty = valueInfo(v)->fixpType;
    mdutils::FPType *fpMD = new mdutils::FPType(fpty.bitsAmt, fpty.fracBitsAmt, fpty.isSigned);

    if (Instruction *inst = dyn_cast<Instruction>(v)) {
      mdutils::InputInfo *II = MDManager.retrieveInputInfo(*inst);
      II = II ? II : new mdutils::InputInfo();
      II->IType = fpMD;
      mdutils::MetadataManager::setInputInfoMetadata(*inst, *II);

    } else if (GlobalObject *go = dyn_cast<GlobalObject>(v)) {
      mdutils::InputInfo *II = MDManager.retrieveInputInfo(*go);
      II = II ? II : new mdutils::InputInfo();
      II->IType = fpMD;
      mdutils::MetadataManager::setInputInfoMetadata(*go, *II);

    } else if (!isa<Argument>(v)) {
      dbgs() << "[WARNING] Cannot attach MetaData to " << *v << "\n";
    }
  }
}


void TaffoTuner::attachFunctionMetaData(llvm::Module &m) {
  mdutils::MetadataManager &MDManager = mdutils::MetadataManager::getMetadataManager();

  for (Function &f : m.functions()) {
    SmallVector<mdutils::InputInfo*, 5> argsII;
    MDManager.retrieveArgumentInputInfo(f, argsII);
    auto argsIt = argsII.begin();
    for (Argument &arg : f.args()) {
      if (hasInfo(&arg)) {
        FixedPointType fpty = valueInfo(&arg)->fixpType;
        mdutils::FPType* fpMD = new mdutils::FPType(fpty.bitsAmt, fpty.fracBitsAmt, fpty.isSigned);
        (*argsIt)->IType = fpMD;
      }
      argsIt++;
    }
    MDManager.setArgumentInputInfoMetadata(f, argsII);
  }
}