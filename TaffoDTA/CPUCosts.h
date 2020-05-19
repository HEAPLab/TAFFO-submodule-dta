#include <map>
#include <string>


#ifndef __TAFFO_DTA_CPUCOSTS_H__
#define __TAFFO_DTA_CPUCOSTS_H__


using namespace std;

namespace tuner {
    ///This class will manage data about the costs in a cpu model
    ///These data are loaded from a file!
    class CPUCosts {

    public:
        enum CostsId {
            ADD_FIX=0, ADD_FLOAT, ADD_DOUBLE,
            SUB_FIX, SUB_FLOAT, SUB_DOUBLE,
            MUL_FIX, MUL_FLOAT, MUL_DOUBLE,
            DIV_FIX, DIV_FLOAT, DIV_DOUBLE,
            REM_FIX, REM_FLOAT, REM_DOUBLE,
            CAST_FIX_FLOAT, CAST_FIX_DOUBLE,
            CAST_FLOAT_FIX, CAST_FLOAT_DOUBLE,
            CAST_DOUBLE_FIX, CAST_DOUBLE_FLOAT,
            CAST_FIX_FIX
        };

        const vector<string> CostsIdValues ={"ADD_FIX", "ADD_FLOAT", "ADD_DOUBLE",
                                             "SUB_FIX", "SUB_FLOAT", "SUB_DOUBLE",
                                             "MUL_FIX", "MUL_FLOAT", "MUL_DOUBLE",
                                             "DIV_FIX", "DIV_FLOAT", "DIV_DOUBLE",
                                             "REM_FIX", "REM_FLOAT", "REM_DOUBLE",
                                             "CAST_FIX_FLOAT", "CAST_FIX_DOUBLE",
                                             "CAST_FLOAT_FIX", "CAST_FLOAT_DOUBLE",
                                             "CAST_DOUBLE_FIX", "CAST_DOUBLE_FLOAT",
                                             "CAST_FIX_FIX"};
    private:
        map<CostsId, double> costsMap;
    public:
        CPUCosts() = delete;

        CPUCosts(string modelFile);


        void loadModelFile(string basicString);

        CostsId decodeId(string &basicString);

        string CostsIdToString(CostsId id);

        void dump();

        double getCost(CostsId id);
    };


}

#endif