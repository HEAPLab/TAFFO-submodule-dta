#include <string>
#include <vector>
#include <set>
#include <fstream>


#ifndef __TAFFO_DTA_MODEL_H__
#define __TAFFO_DTA_MODEL_H__

using namespace std;

namespace tuner {
    class Model {
    public:
        enum ProblemType{
            MIN, MAX
        };

    private:
        set<string> variablesPool;
        ofstream modelFile;

        vector<pair<string, double>> objectiveFunction;
        ProblemType  problemType;
        Model();
    public:




        Model(ProblemType type);

        enum ConstraintType {
            EQ, LE, GE
        }; //Equal, less or equal, greater or equal; strict inequalities are not handled by the tools usually
        void createVariable(const string &varName);

        void insertLinearConstraint(const vector<pair<string, double>> &variables, ConstraintType constraintType);



        bool isVariableDeclared(const string &variable);


        void finalizeAndSolve();

        void createVariable(const string &varName, double min, double max);


        void insertObjectiveElement(const pair<string, double> &variables);

        void writeOutObjectiveFunction();
    };
}


#endif