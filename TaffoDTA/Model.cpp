#include <cassert>
#include <cmath>
#include "Model.h"
#include "llvm/Support/Debug.h"
#include "llvm/Pass.h"
#include "llvm/IR/Module.h"
#include "llvm/ADT/DenseMap.h"
#include "llvm/ADT/SmallPtrSet.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"
#include "InputInfo.h"
#include "Metadata.h"
#include "TypeUtils.h"
#include "Infos.h"
#include "OptimizerInfo.h"
#include "Model.h"

using namespace tuner;
using namespace llvm;
void Model::insertLinearConstraint(const vector<pair<string, double>> &variables, ConstraintType constraintType, double rightSide) {
    //modelFile << "inserting constraint: ";
    //solver.Add(x + 7 * y <= 17.5)
    //Example of
    modelFile<<"solver.Add(";
    for (auto p : variables) {
        assert(isVariableDeclared(p.first) || VARIABLE_NOT_DECLARED(p.first));
        if(p.second==HUGE_VAL || p.second == -HUGE_VAL){
            modelFile << " + (" << (p.second>0?"":"-") << "M" << ")*" << p.first;
            continue;
        }
        modelFile << " + (" << p.second << ")*" << p.first;
    }

    switch (constraintType) {
        case EQ:
            modelFile << "==";
            break;
        case LE:
            modelFile << "<=";
            break;
        case GE:
            modelFile << ">=";
            break;
    }

    modelFile << rightSide << ")\n";
}

void Model::createVariable(const string& varName) {
    assert(false && "Not tested");
    assert(!isVariableDeclared(varName) && "Variable already declared!");
    variablesPool.insert(varName);

    modelFile<<"allocate "<<varName<<";\n";
}

void Model::createVariable(const string& varName, double min, double max) {
    assert(!isVariableDeclared(varName) && "Variable already declared!");
    variablesPool.insert(varName);

    //Prototype line:
    //#x = solver.IntVar(0.0, infinity, 'x')
    modelFile<<varName<<" = solver.IntVar("<<min<<", "<<max<<", "<<"'"<<varName<<"')\n";
}

Model::Model(ProblemType type) {
    modelFile.open("./model_test.txt", ios::out|ios::trunc);
    assert(modelFile.is_open() && "File open failed!");
    this->problemType=type;
}

void Model::finalizeAndSolve() {
    assert(modelFile.is_open() && "Model not opened!");
    writeOutObjectiveFunction();
    modelFile<<"# Model declaration end.";
    modelFile.close();
}

bool Model::isVariableDeclared(const string& variable) {
    return variablesPool.count(variable)!=0;
}

void Model::insertObjectiveElement(const pair<string, double> &p) {
    assert(isVariableDeclared(p.first) && "Variable not declared!");
    objectiveFunction.push_back(p);

}

void Model::writeOutObjectiveFunction() {
    //solver.Minimize(x + 10 * y)
    switch (problemType) {
        case MIN:
            modelFile << "solver.Minimize";
            break;
        case MAX:
            modelFile << "solver.Maximize";
            break;
    }

    modelFile<<"(";

    for (auto p : objectiveFunction) {
        if(p.second==HUGE_VAL || p.second == -HUGE_VAL){
            modelFile << " + (" << (p.second>0?"":"-") << "M" << ")*" << p.first;
            continue;
        }
        modelFile << " + (" << p.second << ")*" << p.first;
    }



    modelFile<<")\n\n";

}

bool Model::VARIABLE_NOT_DECLARED(string var){
    dbgs() << "THIS VARIABLE WAS NOT DECLARED >>" << var <<"<<\n";
    dbgs() << "Here is a list of declared vars:\n";

    for(string a : variablesPool){
        dbgs() << ">>"<<a<<"<<\n";
    }

    assert(false);
}
