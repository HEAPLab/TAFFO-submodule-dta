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
  retrieveAllMetadata(m, vals);

  mergeFixFormat(vals);

  std::vector<Function*> toDel;
  toDel = collapseFunction(m);

  attachFPMetaData(vals);
  attachFunctionMetaData(m);

  for (Function *f : toDel)
    f->eraseFromParent();

  return true;
}


void TaffoTuner::retrieveAllMetadata(Module &m, std::vector<Value *> &vals)
{
  mdutils::MetadataManager &MDManager = mdutils::MetadataManager::getMetadataManager();

  for (GlobalObject &globObj : m.globals()) {
    MDInfo *MDI = MDManager.retrieveMDInfo(&globObj);
    if (processMetadataOfValue(&globObj, MDI))
      vals.push_back(&globObj);
  }

  for (Function &f : m.functions()) {
    SmallVector<mdutils::MDInfo*, 5> argsII;
    MDManager.retrieveArgumentInputInfo(f, argsII);
    auto arg = f.arg_begin();
    for (auto itII = argsII.begin(); itII != argsII.end(); itII++) {
      if (processMetadataOfValue(arg, *itII))
        vals.push_back(arg);
      arg++;
    }

    for (inst_iterator iIt = inst_begin(&f), iItEnd = inst_end(&f); iIt != iItEnd; iIt++) {
      MDInfo *MDI = MDManager.retrieveMDInfo(&(*iIt));
      if (processMetadataOfValue(&(*iIt), MDI))
        vals.push_back(&*iIt);
    }
  }

  sortQueue(vals);
}


bool TaffoTuner::processMetadataOfValue(Value *v, MDInfo *MDI)
{
  if (!MDI)
    return false;
  std::shared_ptr<MDInfo> newmdi(MDI->clone());
  
  bool skippedAll = true;
  Type *fuwt = fullyUnwrapPointerOrArrayType(v->getType());
  llvm::SmallVector<std::pair<MDInfo *, Type *>, 8> queue({std::make_pair(newmdi.get(), fuwt)});

  while (queue.size() > 0) {
    std::pair<MDInfo *, Type *> elem = queue.pop_back_val();
    
    if (InputInfo *II = dyn_cast<InputInfo>(elem.first)) {
      if (!isFloatType(elem.second)) {
        dbgs() << "[Info] Skipping a member of " << *v << " because not a float\n";
        continue;
      }
      if (associateFixFormat(*II))
        skippedAll = false;
      
    } else if (StructInfo *SI = dyn_cast<StructInfo>(elem.first)) {
      if (!elem.second->isStructTy()) {
        dbgs() << "[ERROR] found non conforming structinfo " << SI->toString() << " on value " << *v << "\n";
        dbgs() << "contained type " << *elem.second << " is not a struct type\n";
        dbgs() << "The top-level MDInfo was " << MDI->toString() << "\n";
        assert(false);
      }
      int i=0;
      for (std::shared_ptr<MDInfo> se: *SI) {
        if (se.get() == nullptr)
          continue;
        Type *thisT = fullyUnwrapPointerOrArrayType(elem.second->getContainedType(i));
        queue.push_back(std::make_pair(se.get(), thisT));
        i++;
      }
      
    } else {
      assert(false && "unknown mdinfo subclass");
    }
  }
  
  if (!skippedAll)
    valueInfo(v)->metadata = newmdi;
  return !skippedAll;
}


bool TaffoTuner::associateFixFormat(InputInfo& II)
{
  if (II.IType.get() != nullptr)
    return true;
  
  Range* rng = II.IRange.get();
  if (rng == nullptr)
    return false;

  bool isSigned = rng->Min < 0;

  int max = std::max(std::abs(rng->Min), std::abs(rng->Max));
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
  return true;
}


void TaffoTuner::sortQueue(std::vector<llvm::Value *> &vals)
{
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
      
      if (!isa<Instruction>(u) && !isa<GlobalObject>(u))
        continue;

      if (!MetadataManager::getMetadataManager().retrieveMDInfo(u)) {
        dbgs() << "[WARNING] Find Value " << *u << " without TAFFO info!\n";
        assert(false);
      }
      vals.push_back(u);
      if (!hasInfo(u)) {
        dbgs() << "[WARNING] Find Value " << *u << " without range!\n";
        Type *utype = fullyUnwrapPointerOrArrayType(u->getType());
        if (!utype->isStructTy() && !fullyUnwrapPointerOrArrayType(v->getType())->isStructTy()) {
          InputInfo *ii = cast<InputInfo>(valueInfo(v)->metadata->clone());
          ii->IRange.reset();
          valueInfo(u)->metadata.reset(ii);
        } else {
          if (utype->isStructTy())
            valueInfo(u)->metadata = StructInfo::constructFromLLVMType(utype);
          else
            valueInfo(u)->metadata.reset(new InputInfo());
          dbgs() << "not copying metadata of " << *v << " to " << *u << " because at least one value has struct typing\n";
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
        InputInfo *iiv = dyn_cast<InputInfo>(valueInfo(v)->metadata.get());
        InputInfo *iiu = dyn_cast<InputInfo>(valueInfo(u)->metadata.get());
        if (!iiv || !iiu) {
          DEBUG(dbgs() << "not attempting merge of " << *v << ", " << *u << " because at least one is a struct\n");
          continue;
        }
        if (!iiv->IType.get() || !iiu->IType.get()) {
          DEBUG(dbgs() << "not attempting merge of " << *v << ", " << *u << " because at least one does not change to a fixed point type\n");
          continue;
        }
        FPType *fpv = cast<FPType>(iiv->IType.get());
        FPType *fpu = cast<FPType>(iiu->IType.get());
        if (!(*fpv == *fpu)) {
          if (fpv->getWidth() == fpu->getWidth() &&
              std::abs((int)fpv->getPointPos() - (int)fpu->getPointPos())
              + (fpv->isSigned() == fpu->isSigned() ? 0 : 1) <= SimilarBits) {

            std::shared_ptr<FPType> fp(new FPType(
              fpv->getWidth(),
              std::min(fpv->getPointPos(), fpu->getPointPos()),
              fpv->isSigned() || fpu->isSigned()));
            DEBUG(dbgs() << "Merged fixp : \n"
                         << "\t" << *v << " fix type " << fpv->toString() << "\n"
                         << "\t" << *u << " fix type " << fpu->toString() << "\n"
                         << "Final format " << fp->toString() << "\n";);

            iiv->IType.reset(fp->clone());
            iiu->IType.reset(fp->clone());

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


bool compareTypesOfMDInfo(MDInfo& mdi1, MDInfo& mdi2)
{
  if (mdi1.getKind() != mdi2.getKind())
    return false;
  
  if (isa<InputInfo>(&mdi1)) {
    InputInfo& ii1 = cast<InputInfo>(mdi1);
    InputInfo& ii2 = cast<InputInfo>(mdi2);
    if (ii1.IType.get() && ii2.IType.get()) {
      return *ii1.IType == *ii2.IType;
    } else
      return false;
    
  } else if (isa<StructInfo>(&mdi1)) {
    StructInfo& si1 = cast<StructInfo>(mdi1);
    StructInfo& si2 = cast<StructInfo>(mdi2);
    if (si1.size() == si2.size()) {
      int c = si1.size();
      for (int i=0; i<c; i++) {
        std::shared_ptr<MDInfo> p1 = si1.getField(i);
        std::shared_ptr<MDInfo> p2 = si1.getField(i);
        if ((p1.get() == nullptr) != (p2.get() == nullptr))
          return false;
        if (p1.get() != nullptr) {
          if (!compareTypesOfMDInfo(*p1, *p2))
            return false;
        }
      }
      return true;
      
    } else
      return false;
  
  } else {
    return false;
  }
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
    if (fi.fixArgs.size() == fixSign.size()) {
      auto fcheck = fi.fixArgs.begin();
      auto fthis = fixSign.begin();
      for (; fthis != fixSign.end(); fcheck++, fthis++) {
        if (fcheck->first != fthis->first)
          break;
        if (!compareTypesOfMDInfo(*fcheck->second, *fthis->second))
          break;
      }
      if (fthis == fixSign.end())
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
