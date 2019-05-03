#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/InstIterator.h"
#include "llvm/IR/Metadata.h"
#include "llvm/Support/Debug.h"

#include "TaffoDTA.h"
#include "TypeUtils.h"
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
  std::vector<llvm::Value*> vals;
  llvm::SmallPtrSet<llvm::Value*, 8U> valset;
  retrieveAllMetadata(m, vals, valset);

  mergeFixFormat(vals, valset);

  std::vector<Function*> toDel;
  toDel = collapseFunction(m);

  attachFPMetaData(vals);
  attachFunctionMetaData(m);

  for (Function *f : toDel)
    f->eraseFromParent();

  return true;
}


void TaffoTuner::retrieveAllMetadata(Module &m, std::vector<llvm::Value*> &vals,
				     llvm::SmallPtrSetImpl<llvm::Value *> &valset)
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

  sortQueue(vals, valset);
}


bool TaffoTuner::processMetadataOfValue(Value *v, MDInfo *MDI)
{
  if (!MDI)
    return false;
  std::shared_ptr<MDInfo> newmdi(MDI->clone());

  if (v->getType()->isVoidTy()) {
    valueInfo(v)->metadata = newmdi;
    return true;
  }

  bool skippedAll = true;
  Type *fuwt = fullyUnwrapPointerOrArrayType(v->getType());
  llvm::SmallVector<std::pair<MDInfo *, Type *>, 8> queue({std::make_pair(newmdi.get(), fuwt)});

  while (queue.size() > 0) {
    std::pair<MDInfo *, Type *> elem = queue.pop_back_val();

    if (InputInfo *II = dyn_cast<InputInfo>(elem.first)) {
      if (!isFloatType(elem.second)) {
        DEBUG(dbgs() << "[Info] Skipping a member of " << *v << " because not a float\n");
        continue;
      }
      if (associateFixFormat(*II))
        skippedAll = false;

    } else if (StructInfo *SI = dyn_cast<StructInfo>(elem.first)) {
      if (!elem.second->isStructTy()) {
        DEBUG(dbgs() << "[ERROR] found non conforming structinfo " << SI->toString() << " on value " << *v << "\n");
        DEBUG(dbgs() << "contained type " << *elem.second << " is not a struct type\n");
        DEBUG(dbgs() << "The top-level MDInfo was " << MDI->toString() << "\n");
        llvm_unreachable("Non-conforming StructInfo.");
      }
      int i=0;
      for (std::shared_ptr<MDInfo> se: *SI) {
        if (se.get() != nullptr) {
          Type *thisT = fullyUnwrapPointerOrArrayType(elem.second->getContainedType(i));
          queue.push_back(std::make_pair(se.get(), thisT));
        }
        i++;
      }

    } else {
      llvm_unreachable("unknown mdinfo subclass");
    }
  }

  if (!skippedAll)
    valueInfo(v)->metadata = newmdi;
  return !skippedAll;
}


bool TaffoTuner::associateFixFormat(InputInfo& II)
{
  if (II.IEnableConversion == false)
    return false;

  if (II.IType.get() != nullptr)
    return true;

  Range* rng = II.IRange.get();
  if (rng == nullptr)
    return false;

  if (std::isnan(rng->Min) || std::isnan(rng->Max)) {
    DEBUG(dbgs() << "[WARNING] NaN range bound!\n");
    return false;
  }

  bool isSigned = rng->Min < 0;

  if (std::isinf(rng->Min) || std::isinf(rng->Max)) {
    DEBUG(dbgs() << "[WARNING] Infinite range bound. Overflow may occur!\n");
    II.IType.reset(new FPType(TotalBits, 0, isSigned));
    return true;
  }

  double max = std::max(std::abs(rng->Min), std::abs(rng->Max));
  int intBit = std::lround(std::ceil(std::log2(max+1.0))) + (isSigned ? 1 : 0);
  int bitsAmt = TotalBits;
  int fracBitsAmt = bitsAmt - intBit;

  // Check dimension
  if (fracBitsAmt < FracThreshold) {
    DEBUG(dbgs() << "[WARNING] Fractional part is too small!\n");
    fracBitsAmt = 0;
    if (intBit > bitsAmt) {
      DEBUG(dbgs() << "[WARNING] Overflow may occur!\n");
    }
  }

  II.IType.reset(new FPType(bitsAmt, fracBitsAmt, isSigned));
  return true;
}

void TaffoTuner::sortQueue(std::vector<llvm::Value *> &vals,
			   llvm::SmallPtrSetImpl<llvm::Value *> &valset)
{
  mdutils::MetadataManager &MDManager = mdutils::MetadataManager::getMetadataManager();

  // Topological sort by means of a reversed DFS.
  enum VState { Visited, Visiting };
  DenseMap<Value *, VState> vstates;
  std::vector<Value *> revQueue;
  std::vector<Value *> stack;
  revQueue.reserve(vals.size());
  stack.reserve(vals.size());

  for (Value *v : vals) {
    if (vstates.count(v))
      continue;

    stack.push_back(v);
    while (!stack.empty()) {
      Value *c = stack.back();
      auto cstate = vstates.find(c);
      if (cstate == vstates.end()) {
	vstates[c] = Visiting;
	for (Value *u : c->users()) {
	  if (!isa<Instruction>(u) && !isa<GlobalObject>(u))
	    continue;

	  if (!MDManager.retrieveMDInfo(u)) {
	    DEBUG(dbgs() << "[WARNING] Found Value " << *u << " without TAFFO info!\n");
	    continue;
	  }

	  stack.push_back(u);
	  if (!hasInfo(u)) {
	    DEBUG(dbgs() << "[WARNING] Found Value " << *u << " without range!\n");
	    Type *utype = fullyUnwrapPointerOrArrayType(u->getType());
	    if (!utype->isStructTy() && !fullyUnwrapPointerOrArrayType(c->getType())->isStructTy()) {
	      InputInfo *ii = cast<InputInfo>(valueInfo(c)->metadata->clone());
	      ii->IRange.reset();
	      valueInfo(u)->metadata.reset(ii);
	    } else {
	      if (utype->isStructTy())
		valueInfo(u)->metadata = StructInfo::constructFromLLVMType(utype);
	      else
		valueInfo(u)->metadata.reset(new InputInfo());
	      DEBUG(dbgs() << "not copying metadata of " << *c << " to " << *u << " because at least one value has struct typing\n");
	    }
	  }
	}
      } else if (cstate->second == Visiting) {
	revQueue.push_back(c);
	stack.pop_back();
	vstates[c] = Visited;
      } else {
	assert(cstate->second == Visited);
	stack.pop_back();
      }
    }
  }

  vals.clear();
  valset.clear();
  for (auto i = revQueue.rbegin(); i != revQueue.rend(); ++i) {
    vals.push_back(*i);
    valset.insert(*i);
  }
}

void TaffoTuner::mergeFixFormat(const std::vector<llvm::Value *> &vals,
				const llvm::SmallPtrSetImpl<llvm::Value *> &valset)
{
  if (DisableTypeMerging)
    return;

  assert(vals.size() == valset.size() && "They must contain the same elements.");
  bool merged = false;
  for (Value *v : vals) {
    for (Value *u: v->users()) {
      if (valset.count(u)) {
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
        if (v->getType()->isPointerTy() || u->getType()->isPointerTy()) {
          DEBUG(dbgs() << "not attempting merge of " << *v << ", " << *u << " because at least one is a pointer\n");
          continue;
        }
        FPType *fpv = cast<FPType>(iiv->IType.get());
        FPType *fpu = cast<FPType>(iiu->IType.get());
        if (!(*fpv == *fpu)) {
          if (fpv->getWidth() == fpu->getWidth() &&
              std::abs((int)fpv->getPointPos() - (int)fpu->getPointPos())
              + (fpv->isSigned() == fpu->isSigned() ? 0 : 1) <= SimilarBits) {

            int sign_v = fpv->isSigned() ? 1 : 0;
            int int_v = fpv->getWidth() - fpv->getPointPos() - sign_v;
            int sign_u = fpu->isSigned() ? 1 : 0;
            int int_u = fpu->getWidth() - fpu->getPointPos() - sign_v;
            
            int sign_res = std::max(sign_u, sign_v);
            int int_res = std::max(int_u, int_v);
            int size_res = std::max(fpv->getWidth(), fpu->getWidth());
            int frac_res = size_res - int_res - sign_res;
            std::shared_ptr<FPType> fp(new FPType(size_res, frac_res, sign_res));
            if (sign_res + int_res + frac_res != size_res || frac_res < 0) {
              DEBUG(dbgs() << "not attempting merge of " << *v << ", " << *u << " because resulting type " << fp->toString() << " is invalid\n");
              continue;
            }
            DEBUG(dbgs() << "Merged fixp : \n"
                         << "\t" << *v << " fix type " << fpv->toString() << "\n"
                         << "\t" << *u << " fix type " << fpu->toString() << "\n"
                         << "Final format " << fp->toString() << "\n";);

            iiv->IType.reset(fp->clone());
            iiu->IType.reset(fp->clone());

            restoreTypesAcrossFunctionCall(v);
            restoreTypesAcrossFunctionCall(u);

            merged = true;
          } else {
            FixCast++;
          }
        }
      }
    }
  }
  if (merged)
    mergeFixFormat(vals, valset);
}


void TaffoTuner::restoreTypesAcrossFunctionCall(Value *v)
{
  DEBUG(dbgs() << "restoreTypesAcrossFunctionCall(" << *v << ")\n");
  if (!hasInfo(v)) {
    DEBUG(dbgs() << " --> skipping restoring types because value is not converted\n");
    return;
  }
  
  std::shared_ptr<MDInfo> finalMd = valueInfo(v)->metadata;
  
  if (Argument *arg = dyn_cast<Argument>(v)) {
    setTypesOnCallArgumentFromFunctionArgument(arg, finalMd);
    return;
  }
  
  for (Use& use: v->uses()) {
    User *user = use.getUser();
    CallSite call(user);
    if (call.getInstruction() == nullptr)
      continue;
    
    Function *fun = dyn_cast<Function>(call.getCalledFunction());
    if (fun == nullptr) {
      DEBUG(dbgs() << " --> skipping restoring types from call site " << *user << " because function reference cannot be resolved\n");
      continue;
    }
    if (fun->isVarArg()) {
      DEBUG(dbgs() << " --> skipping restoring types from call site " << *user << " because function is vararg\n");
      continue;
    }
    
    assert(fun->arg_size() > use.getOperandNo() && "invalid call to function; operandNo > numOperands");
    Argument *arg = fun->arg_begin() + use.getOperandNo();
    if (hasInfo(arg)) {
      valueInfo(arg)->metadata.reset(finalMd->clone());
      setTypesOnCallArgumentFromFunctionArgument(arg, finalMd);
    }
  }
}


void TaffoTuner::setTypesOnCallArgumentFromFunctionArgument(Argument *arg, std::shared_ptr<MDInfo> finalMd)
{
  Function *fun =  arg->getParent();
  int n = arg->getArgNo();
  DEBUG(dbgs() << " --> setting types to " << finalMd->toString() << " on call arguments from function " << fun->getName() << " argument " << n << "\n");
  for (auto it = fun->user_begin(); it != fun->user_end(); it++) {
    if (isa<CallInst>(*it) || isa<InvokeInst>(*it)) {
      Value *callarg = it->getOperand(n);
      DEBUG(dbgs() << " --> target " << *callarg << ", callsite " << **it << "\n");
      if (!hasInfo(callarg)) {
        DEBUG(dbgs() << " --> argument doesn't get converted; skipping\n");
      } else {
        valueInfo(callarg)->metadata.reset(finalMd->clone());
      }
    }
  }
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
        if (fClone->user_begin() == fClone->user_end()) {
          DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t Ignoring " << fClone->getName()
            << " because it's not used anywhere\n");
        } else if (Function *eqFun = findEqFunction(fClone, &f)) {
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


Function* TaffoTuner::findEqFunction(Function *fun, Function *origin)
{
  std::vector<std::pair<int, std::shared_ptr<MDInfo>>> fixSign;

  DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Search eq function for " << fun->getName()
    << " in " << origin->getName() << " pool\n";);

  if (isFloatType(fun->getReturnType()) && hasInfo(*fun->user_begin())) {
    std::shared_ptr<MDInfo> retval = valueInfo(*fun->user_begin())->metadata;
    if (retval) {
      fixSign.push_back(std::pair<int, std::shared_ptr<MDInfo>>(-1, retval)); //ret value in signature
      DEBUG_WITH_TYPE(DEBUG_FUN, dbgs() << "\t\t Return type : "
          << valueInfo(*fun->user_begin())->metadata->toString() << "\n";);
    }
  }

  int i=0;
  for (Argument &arg: fun->args()) {
    if (hasInfo(&arg) && valueInfo(&arg)->metadata) {
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
        if (fcheck->second != fthis->second)
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
      DEBUG(dbgs() << "[WARNING] Cannot attach MetaData to " << *v << " (normal for function args)\n");
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
