#include "Optimizer.h"
#include "llvm/Support/Debug.h"


using namespace tuner;
using namespace mdutils;
using namespace std;
using namespace taffo;

extern llvm::cl::opt<int> TotalBits;
extern llvm::cl::opt<int> FracThreshold;

shared_ptr<OptimizerInfo> Optimizer::processConstant(Constant *constant) {
    //Constant variable should, in general, not be saved anywhere.
    //In fact, the same constant may be used in different ways, but by the fact that
    //it is a constant, it may be modified in the final code
    //For example, a double 1.00 can become a float 1.00 in one place and a fixp 1 in another!
    dbgs() << "Processing constant...\n";

    if(auto global = dyn_cast_or_null<GlobalObject>(constant)){
        if(tuner->hasInfo(constant)){
            llvm_unreachable("This should already have been handled!");
        }else{
            dbgs() << "Trying to process a non float global...\n";
            return nullptr;
        }

    }

    if (auto constantData = dyn_cast_or_null<ConstantData>(constant)) {
        //ATM: only handling FP types, should be enough
        if (auto constantFP = dyn_cast_or_null<ConstantFP>(constant)) {
            dbgs() << "Processing FPconstant...\n";

            APFloat tmp = constantFP->getValueAPF();
            bool losesInfo;
            tmp.convert(APFloatBase::IEEEdouble(), APFloat::roundingMode::rmNearestTiesToEven, &losesInfo);
            double a = tmp.convertToDouble();

            double min, max;
            min = a;
            max = a;

            Range rangeInfo(min, max);


            FixedPointTypeGenError fpgerr;
            FPType fpInfo = fixedPointTypeFromRange(rangeInfo, &fpgerr, TotalBits, FracThreshold, 64, TotalBits);
            if (fpgerr != FixedPointTypeGenError::NoError) {
                emitError("Error generating infos for constant propagation!");
                return nullptr;
            }

            string fname = "ConstantValue";
            //ENOB should not be considered for constant.... It is a constant and will be converted as best as possible
            auto info = allocateNewVariableForValue(constantFP, make_shared<FPType>(fpInfo), make_shared<Range>(rangeInfo), nullptr, fname, true, "", false);
            info->setReferToConstant(true);
            return info;
        }

        dbgs() << "[ERROR] handling unknown ConstantData, I don't know what to do: ";
        constant->print(dbgs());
        dbgs() << "\n";
        return nullptr;
    }

    if (auto constantExpr = dyn_cast_or_null<ConstantExpr>(constant)) {
        if (constantExpr->isGEPWithNoNotionalOverIndexing()) {
            return handleGEPConstant(constantExpr);
        }

    }

    llvm_unreachable("Constant not handled!");
}


shared_ptr<OptimizerInfo> Optimizer::handleGEPConstant(const ConstantExpr *cexp_i) {
    //The first operand is the beautiful object
    Value *operand = cexp_i->getOperand(0U);


    Type *source_element_type =
            cast<PointerType>(operand->getType()->getScalarType())->getElementType();
    std::vector<unsigned> offset;

    //We compute all the offsets that will be used in our "data structure" to navigate it, to reach the correct range
    if (extractGEPOffset(source_element_type,
                         iterator_range<User::const_op_iterator>(cexp_i->op_begin() + 1,
                                                                 cexp_i->op_end()),
                         offset)) {


        dbgs() << "Exctracted offset: [";
        for (int i = 0; i < offset.size(); i++) {
            dbgs() << offset[i] << ", ";
        }
        dbgs() << "]\n";
        //When we load an address from a "thing" we need to store a reference to it in order to successfully update the error
        auto optInfo_t = dynamic_ptr_cast_or_null<OptimizerPointerInfo>(getInfoOfValue(operand));
        if (!optInfo_t) {
            dbgs() << "Probably trying to access a non float element, bailing out.\n";
            return nullptr;
        }


        auto optInfo = optInfo_t->getOptInfo();
        if (!optInfo) {
            dbgs() << "Probably trying to access a non float element, bailing out.\n";
            return nullptr;
        }
        //This will only contain displacements for struct fields...
        for (int i = 0; i < offset.size(); i++) {
            auto structInfo = dynamic_ptr_cast_or_null<OptimizerStructInfo>(optInfo);
            if (!structInfo) {
                dbgs() << "Probably trying to access a non float element, bailing out.\n";
                return nullptr;
            }

            optInfo = structInfo->getField(offset[i]);
        }


        return make_shared<OptimizerPointerInfo>(optInfo);
    }
    return nullptr;
}