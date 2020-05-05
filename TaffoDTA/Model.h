#include <string>
#include <vector>
#include <set>
#include <fstream>


#ifndef __TAFFO_DTA_MODEL_H__
#define __TAFFO_DTA_MODEL_H__

using namespace std;

namespace tuner {
    class Model {
    private:
        set<string> variablesPool;
        ofstream modelFile;

    public:

        Model();

        enum ConstraintType {
            EQ, LE, GE
        }; //Equal, less or equal, greater or equal; strict inequalities are not handled by the tools usually
        void createVariable(const string &varName);

        void insertLinearConstraint(const vector<pair<string, double>> &variables, ConstraintType constraintType);

        bool isVariableDeclared(const string &variable);


        void finalizeAndSolve();

        void createVariable(const string &varName, double min, double max);
    };
}


#endif