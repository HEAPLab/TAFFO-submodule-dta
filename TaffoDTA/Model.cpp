#include <cassert>
#include "Model.h"

using namespace tuner;
void Model::insertLinearConstraint(const vector<pair<string, double>> &variables, ConstraintType constraintType) {
    modelFile << "inserting constraint: ";
    for (auto p : variables) {
        assert(isVariableDeclared(p.first) && "Variable not declared!");
        modelFile << " + (" << p.second << ")*" << p.first;
    }

    switch (constraintType) {
        case EQ:
            modelFile << "=";
            break;
        case LE:
            modelFile << "<=";
            break;
        case GE:
            modelFile << ">=";
            break;
    }

    modelFile << "0\n";
}

void Model::createVariable(const string& varName) {
    assert(!isVariableDeclared(varName) && "Variable already declared!");
    variablesPool.insert(varName);

    modelFile<<"allocate "<<varName<<";\n";
}

void Model::createVariable(const string& varName, double min, double max) {
    assert(!isVariableDeclared(varName) && "Variable already declared!");
    variablesPool.insert(varName);

    modelFile<<"allocate "<<varName<<" in ["<<min<<", "<<max<<"]\n";
}

Model::Model() {
    modelFile.open("./model_test.txt", ios::out|ios::trunc);
    assert(modelFile.is_open() && "File open failed!");
}

void Model::finalizeAndSolve() {
    assert(modelFile.is_open() && "Model not opened!");
    modelFile<<"# Model declaration end.";
    modelFile.close();
}

bool Model::isVariableDeclared(const string& variable) {
    return variablesPool.count(variable)!=0;
}
