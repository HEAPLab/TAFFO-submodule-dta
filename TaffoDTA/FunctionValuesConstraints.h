#include "llvm/IR/Module.h"
#include "llvm/IR/Value.h"
#include "llvm/ADT/APFloat.h"


#ifndef FUNCTION_VALUES_CONSTRAINTS_H
#define FUNCTION_VALUES_CONSTRAINTS_H


namespace tuner {


class Constraint {
public:
  enum ConstraintKind {
    CK_OneValueType,
    CK_MultipleValueEquality
  };
  using ValueListStorage = llvm::SmallVector<llvm::Value *, 1>;
private:
  const ConstraintKind Kind;
  const ValueListStorage Values;
protected:
  Constraint(ConstraintKind K, llvm::ArrayRef<llvm::Value *> V) : Kind(K), Values(V.begin(), V.end()) {}
public:
  ConstraintKind getKind() const { return Kind; }
  
  llvm::ArrayRef<llvm::Value *> getConstrainedValues() const { return llvm::ArrayRef<llvm::Value *>(Values); }
  
  using const_iterator = ValueListStorage::const_iterator;
  const_iterator begin() const { return Values.begin(); }
  const_iterator end() const { return Values.end(); }
};


/// A constraint relative to the type of a single value
///
class OneValueConstraint : public Constraint {
public:
  OneValueConstraint(llvm::Value *V) : Constraint(CK_OneValueType, {V}) {}
  
  static bool classof(const Constraint *C) { return C->getKind() == CK_OneValueType; }
  /// TODO: fill here
};


/// A constraint which specifies that a given list of values must be assigned the
/// same type.
class MultipleValueEqualityConstraint : public Constraint {
public:
  MultipleValueEqualityConstraint(llvm::ArrayRef<llvm::Value *> V) : Constraint(CK_MultipleValueEquality, V) {}
  
  static bool classof(const Constraint *C) { return C->getKind() == CK_MultipleValueEquality; }
};


/// FunctionValuesConstraints is a class which encapsulates the constraints
/// for the data type allocation of the values in a given function.
///
class FunctionValuesConstraints {
public:

};


}


#endif

