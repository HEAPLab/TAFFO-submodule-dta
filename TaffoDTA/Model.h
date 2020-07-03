#include <string>
#include <vector>
#include <set>
#include <fstream>
#include <map>
#include <llvm/Support/CommandLine.h>


#ifndef __TAFFO_DTA_MODEL_H__
#define __TAFFO_DTA_MODEL_H__

#define MODEL_OBJ_CASTCOST "castCostObj"
#define MODEL_OBJ_ENOB "enobCostObj"
#define MODEL_OBJ_MATHCOST "mathCostObj"

extern llvm::cl::opt<double> MixedTuningTime;
extern llvm::cl::opt<double> MixedTuningENOB;
extern llvm::cl::opt<double> MixedTuningCastingTime;
extern llvm::cl::opt<bool> MixedDoubleEnabled;


using namespace std;

namespace tuner {
    class Model {
    public:
        enum ProblemType{
            MIN, MAX
        };

    private:
        set<string> variablesPool;
        map<string, double> variableValues;

        map<string, bool> objDeclarationOccoured;

        ofstream modelFile;

        vector<pair<string, double>> objectiveFunction;
        ProblemType  problemType;
        Model() = delete;
    public:




        Model(ProblemType type);

        enum ConstraintType {
            EQ, LE, GE
        }; //Equal, less or equal, greater or equal; strict inequalities are not handled by the tools usually
        void createVariable(const string &varName);

        void insertLinearConstraint(const vector<pair<string, double>> &variables, ConstraintType constraintType,  double rightSide, string comment);



        bool isVariableDeclared(const string &variable);


        bool finalizeAndSolve();

        void createVariable(const string &varName, double min, double max);


        void insertObjectiveElement(const pair<string, double> &variables, string costName);

        void writeOutObjectiveFunction();

        bool VARIABLE_NOT_DECLARED(string var);

        bool loadResultsFromFile(string modelFile);

        double getVariableValue(string variable);

        double getMultiplier(string var);

        void insertComment(string comment, int spaceBefore=0, int spaceAfter=0);
    };
}


#endif