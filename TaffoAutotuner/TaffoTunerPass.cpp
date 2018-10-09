#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/InstIterator.h"
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
