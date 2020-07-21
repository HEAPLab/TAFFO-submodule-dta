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
void Model::insertLinearConstraint(const vector<pair<string, double>> &variables, ConstraintType constraintType, double rightSide, string comment) {
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

    modelFile << rightSide << ")    #" << comment <<"\n";
}

void Model::createVariable(const string& varName) {
    assert(false && "Not working");
    assert(!isVariableDeclared(varName) && "Variable already declared!");
    variablesPool.insert(varName);

    modelFile<<varName<<" = solver.IntVar('"<<varName<<"')\n";
}

void Model::createVariable(const string& varName, double min, double max) {
    assert(!isVariableDeclared(varName) && "Variable already declared!");
    variablesPool.insert(varName);

    //Prototype line:
    //#x = solver.IntVar(0.0, infinity, 'x')
    modelFile<<varName<<" = solver.IntVar("<<min<<", "<<max<<", "<<"'"<<varName<<"')\n";
}

Model::Model(ProblemType type) {
    modelFile.open("./model_test.py", ios::out|ios::trunc);
    assert(modelFile.is_open() && "File open failed!");
    this->problemType=type;

}

bool Model::finalizeAndSolve() {
    assert(modelFile.is_open() && "Model not opened!");
    writeOutObjectiveFunction();
    modelFile<<"# Model declaration end.";
    modelFile.close();


    //We should run solver.py that automatically imports the predeclared file
    //FIXME: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH
    int result = system("python3 solver.py");
    if(result){

        dbgs() << "[ERROR] There was an error while solving the model!\n\n";
        return false;
    }

    loadResultsFromFile("model_results.txt");

    dbgs() << "Dumping results:\n\n";
    for(auto var : variablesPool){
        dbgs() << var << " = " << getVariableValue(var) << "\n";
    }

    return true;

}

bool Model::loadResultsFromFile(string modelFile) {
    fstream fin;

    fin.open(modelFile, ios::in);

    assert(fin.is_open() && "Cannot open results file!");

    string line, field, temp;
    vector<string> row;

    //for each line in the file
    int nline=0;
    while (getline(fin, line)) {

        //read the file until a newline is found (discarded from final string)
        row.clear();
        double value = 0;
        nline++;


        //Generate a stream in order to be used by getLine
        stringstream lineStream(line);
        //llvm::dbgs() << "Line: " << line << "\n";

        while (getline(lineStream, field, ',')) {
            row.push_back(field);
        }

        if (row.size() != 2) {
            llvm::dbgs() << "Malformed line found: [" << line << "] on line"<< nline << ", skipping...\n";
            continue;
        }

        string varName = row[0];
        value = stod(row[1]);

        if(varName == "__ERROR__"){
            if(value==0){
                dbgs() << "The model was solved correctly!\n";
            }else{
                dbgs() << "[ERROR] The Python solver signalled an error!\n\n";
                return false;
            }
            //Skips any other computation as this is a state message
            continue;
        }

        if(varName == "__COST_ENOB__"){
            costEnob = value;
            continue;
        }

        if(varName == "__COST_TIME__"){
            costTime = value;
            continue;
        }

        if(varName == "__COST_CONV__"){
            costCast=value;
            continue;
        }

        if(!isVariableDeclared(varName)){
            dbgs() << "Trying to load results for an unknown variable!\nThis may be signal of a more problematic error!\n\n";
            VARIABLE_NOT_DECLARED(varName);
        }

        if(variableValues.find(varName) != variableValues.end()){
            llvm::dbgs() << "Found duplicated result: [" << line << "], skipping...\n";
            continue;
        }

        variableValues.insert(make_pair(varName, value));


    }

    if(variableValues.size() != variablesPool.size()){
        dbgs() << "[ERROR] The number of variables in the file and in the model does not match!\n";
        return false;
    }
    return true;
}

bool Model::isVariableDeclared(const string& variable) {
    return variablesPool.count(variable)!=0;
}


void Model::insertObjectiveElement(const pair<string, double> &p, string costName, double maxVal) {
    assert(isVariableDeclared(p.first) && "Variable not declared!");

    string operand = " += ";
    if(objDeclarationOccoured.find(costName) == objDeclarationOccoured.end() || !objDeclarationOccoured[costName]){
        operand = " = ";
        objDeclarationOccoured.insert(make_pair(costName, true));
    }

    //We use this to normalize the objective value against program complexity changes
    objMaxCosts[costName] = objMaxCosts[costName] + maxVal;

    modelFile <<  costName << operand;

    if(p.second==HUGE_VAL || p.second == -HUGE_VAL){
        modelFile << " + (" << (p.second>0?"":"-") << "M" << ")*" << p.first;

    }else {
        modelFile << " + (" << p.second << ")*" << p.first;
    }

    modelFile << "\n";
    //objectiveFunction.push_back(p);

}

void Model::writeOutObjectiveFunction() {
    //solver.Minimize(x + 10 * y)

    this->insertComment("All the model has been generated, lets solve it!", 5);



    switch (problemType) {
        case MIN:
            modelFile << "solver.Minimize";
            break;
        case MAX:
            modelFile << "solver.Maximize";
            break;
    }

    modelFile<<"(";

    int i =0;
    for(auto a : objDeclarationOccoured){
        if(i>0){
            modelFile<< "+ ";
        }

        modelFile << getMultiplier(a.first) << " * " << a.first << " / " << objMaxCosts[a.first];
        i++;
    }

    //modelFile << "objectiveFunction";


    modelFile<<")\n\n";

}

double Model::getMultiplier(string var){
    if(var == MODEL_OBJ_CASTCOST){
        return MixedTuningCastingTime;
    }

    if(var == MODEL_OBJ_ENOB){
        return MixedTuningENOB;
    }

    if(var == MODEL_OBJ_MATHCOST){
        return MixedTuningTime;
    }

    llvm_unreachable("Cost variable not declared.");
}

bool Model::VARIABLE_NOT_DECLARED(string var){
    dbgs() << "THIS VARIABLE WAS NOT DECLARED >>" << var <<"<<\n";
    dbgs() << "Here is a list of declared vars:\n";

    for(string a : variablesPool){
        dbgs() << ">>"<<a<<"<<\n";
    }

    assert(false);
}

double Model::getVariableValue(string variable){
    if(!isVariableDeclared(variable)){
        VARIABLE_NOT_DECLARED(variable);
    }

    auto res = variableValues.find(variable);
    assert(res!=variableValues.end() && "The value of this variable was not found in the model!");

    return res->second;
}

void Model::insertComment(string comment, int spaceBefore, int spaceAfter) {
    int i;

    for(i=0; i<spaceBefore; i++){
        modelFile << "\n";
    }


    //delete newline
    std::replace(comment.begin(), comment.end(), '\n', '_');
    std::replace(comment.begin(), comment.end(), '\r', '_');
    modelFile << "#" << comment << "\n";

    for(i=0; i<spaceAfter; i++){
        modelFile << "\n";
    }

}
