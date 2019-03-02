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
using namespace mdutils;


Type *fullyUnwrapPointerOrArrayType(Type *srct)
{
  if (srct->isPointerTy()) {
    return fullyUnwrapPointerOrArrayType(srct->getPointerElementType());
  } else if (srct->isArrayTy()) {
    return fullyUnwrapPointerOrArrayType(srct->getArrayElementType());
  }
  return srct;
}


bool isFloatType(Type *srct)
{
  return fullyUnwrapPointerOrArrayType(srct)->isFloatingPointTy();
}


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
      mdutils::InputInfo *newII = cast<mdutils::InputInfo>(II->clone());
      if (parseMDRange(&globObj, newII)) {
        associateFixFormat(*newII);
        valueInfo(&globObj)->metadata.reset(newII);
        vals.push_back(&globObj);
      }
    }
  }

  for (Function &f : m.functions()) {
    SmallVector<mdutils::MDInfo*, 5> argsII;
    MDManager.retrieveArgumentInputInfo(f, argsII);
    auto arg = f.arg_begin();
    for (auto itII = argsII.begin(); itII != argsII.end(); itII++) {
      if (*itII) {
        // TODO: struct support
        mdutils::InputInfo *ii = dyn_cast<mdutils::InputInfo>(*itII);
        if (ii && parseMDRange(arg, ii)) {
          mdutils::InputInfo *newII = cast<mdutils::InputInfo>(ii->clone());
          associateFixFormat(*newII);
          valueInfo(arg)->metadata.reset(newII);
          vals.push_back(arg);
        }
      }
      arg++;
    }

    for (inst_iterator iIt = inst_begin(&f), iItEnd = inst_end(&f); iIt != iItEnd; iIt++) {
      if (mdutils::InputInfo *II = MDManager.retrieveInputInfo(*iIt)) {
        if (parseMDRange(&*iIt, II)) {
          mdutils::InputInfo *newII = cast<mdutils::InputInfo>(II->clone());
          associateFixFormat(*newII);
          valueInfo(&*iIt)->metadata.reset(newII);
          vals.push_back(&*iIt);
        }
      }
    }
  }

  sortQueue(vals);
}


bool TaffoTuner::parseMDRange(Value *v, InputInfo *II) {
  mdutils::Range* rng = II->IRange.get();
  if (!isFloatType(v->getType())) {
    dbgs() << "[Info] Skipping value " << *v << " because not a float\n";
    return false;
  }

  return rng!=nullptr;
}


void TaffoTuner::associateFixFormat(InputInfo& II)
{
  Range& rng = *(II.IRange);
  bool isSigned = rng.Min < 0;

  int max = std::max(std::abs(rng.Min), std::abs(rng.Max));
  int intBit = std::ceil(std::log2(max+1)) + (isSigned ? 1 : 0);
  int bitsAmt = TotalBits;
  int fracBitsAmt = bitsAmt - intBit;

  //Check dimension
  if (fracBitsAmt < FracThreshold) {
    dbgs() << "[WARNING] Fractional part is too small!\n";
    fracBitsAmt = 0;
    if (intBit > bitsAmt) {
      dbgs() << "[WARNING] Overflow may occur!\n";
    }
  }
  
  II.IType.reset(new FPType(bitsAmt, fracBitsAmt, isSigned));
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
            dbgs() << "[WARNING] Find Value " << *inst << " without range!\n";
            valueInfo(u)->metadata.reset(valueInfo(v)->metadata->clone());
          }
        } else {
          dbgs() << "[WARNING] Find Value " << *inst << " without TAFFO info!\n";
          assert(false);
        }

      } else if (GlobalObject *go = dyn_cast<GlobalObject>(u)) {
        if (go->getMetadata(INPUT_INFO_METADATA)) {
          vals.push_back(u);
          if (!hasInfo(u)) {
            dbgs() << "[WARNING] Find Value " << *go << " without range!\n";
            valueInfo(u)->metadata.reset(valueInfo(v)->metadata->clone());
          }
        } else {
          dbgs() << "[WARNING] Find Value " << *go << " without TAFFO info!\n";
          assert(false);
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
        // todo: bail out for structs
        InputInfo *iiv = cast<InputInfo>(valueInfo(v)->metadata.get());
        InputInfo *iiu = cast<InputInfo>(valueInfo(u)->metadata.get());
        FPType *fpv = cast<FPType>(iiv->IType.get());
        FPType *fpu = cast<FPType>(iiu->IType.get());
        if (!(*fpv == *fpu)) {
          if (fpv->getWidth() == fpu->getWidth() &&
              std::abs((int)fpv->getPointPos() - (int)fpu->getPointPos())
              + (fpv->isSigned() == fpu->isSigned() ? 0 : 1) <= SimilarBits) {

            std::shared_ptr<FPType> fp(new FPType(
              std::min(fpv->getPointPos(), fpu->getPointPos()),
              fpv->getWidth(),
              fpv->isSigned() || fpu->isSigned()));
            DEBUG(dbgs() << "Merged fixp : \n"
                         << "\t" << *v << " fix type " << fpv->toString() << "\n"
                         << "\t" << *u << " fix type " << fpu->toString() << "\n"
                         << "Final format " << fp->toString() << "\n";);

            iiv->IType = fp;
            iiu->IType = fp;

            if (Argument *arg =  dyn_cast<Argument>(v)) {
              Function *fun =  arg->getParent();
              int n = arg->getArgNo();
              for (auto it = fun->user_begin(); it != fun->user_end(); it++) {
                if (isa<CallInst>(*it) || isa<InvokeInst>(*it)) {
                  DEBUG(dbgs() << "Argument " << *arg << " nr. " << n
                               << " propagate fix type merge on callsite " << **it << "\n";);
                  InputInfo *iiop = cast<InputInfo>(valueInfo(it->getOperand(n))->metadata.get());
                  iiop->IType = fp;
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
  std::vector<std::pair<int, std::shared_ptr<MDInfo>>> fixSign;

  DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Search eq function for " << fun->getName()
    << " in " << origin->getName() << " pool\n";);

  if(isFloatType(fun->getReturnType())) {
    fixSign.push_back(std::pair<int, std::shared_ptr<MDInfo>>
        (-1, valueInfo(*fun->user_begin())->metadata) ); //ret value in signature
    DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Return type : "
        << valueInfo(*fun->user_begin())->metadata->toString() << "\n";);
  }

  int i=0;
  for (Argument &arg : fun->args()) {
    if (hasInfo(&arg)) {
      fixSign.push_back(std::pair<int, std::shared_ptr<MDInfo>>(i,valueInfo(&arg)->metadata));
      DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Arg "<< i << " type : "
          << valueInfo(&arg)->metadata->toString() << "\n";);
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


void TaffoTuner::attachFPMetaData(std::vector<llvm::Value *> &vals)
{
  for (Value *v : vals) {
    assert(info[v] && "Every value should have info");
    assert(valueInfo(v)->metadata.get() && "every value should have metadata");
    
    if (isa<Instruction>(v) || isa<GlobalObject>(v)) {
      mdutils::MetadataManager::setMDInfoMetadata(v, valueInfo(v)->metadata.get());
    } else {
      dbgs() << "[WARNING] Cannot attach MetaData to " << *v << " (normal for function args)\n";
    }
  }
}


void TaffoTuner::attachFunctionMetaData(llvm::Module &m) {
  mdutils::MetadataManager &MDManager = mdutils::MetadataManager::getMetadataManager();

  for (Function &f : m.functions()) {
    SmallVector<mdutils::MDInfo*, 5> argsII;
    MDManager.retrieveArgumentInputInfo(f, argsII);
    auto argsIt = argsII.begin();
    for (Argument &arg : f.args()) {
      if (*argsIt) {
        if (hasInfo(&arg)) {
          MDInfo *mdi = valueInfo(&arg)->metadata.get();
          *argsIt = mdi;
        }
      }
      argsIt++;
    }
    MDManager.setArgumentInputInfoMetadata(f, argsII);
  }
}
