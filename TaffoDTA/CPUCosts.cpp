#include <iostream>
#include <fstream>
#include <cassert>
#include <sstream>
#include <vector>
#include <llvm/Support/Debug.h>
#include "llvm/IR/Module.h"
#include "llvm/ADT/DenseMap.h"
#include "llvm/ADT/SmallPtrSet.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"
#include "CPUCosts.h"
#define DEBUG_TYPE "taffo-dta"
using namespace tuner;
using namespace std;

CPUCosts::CPUCosts(string modelFile) {
    // File pointer
    loadModelFile(modelFile);
}

void CPUCosts::loadModelFile(string modelFile) {
    fstream fin;

    fin.open(modelFile, ios::in);

    assert(fin.is_open() && "Cannot open model file!");

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

        CostsId id = decodeId(row[0]);
        value = stod(row[1]);

        if(costsMap.find(id) != costsMap.end()){
            llvm::dbgs() << "Found duplicated info: [" << line << "], skipping...\n";
            continue;
        }

        costsMap.insert(make_pair(id, value));


    }
}

CPUCosts::CostsId CPUCosts::decodeId(const string& basicString) const{
    auto it = std::find(CostsIdValues.begin(), CostsIdValues.end(), basicString);

    LLVM_DEBUG(llvm::dbgs() <<  "searching cost [" << basicString << "]");
    if(it != CostsIdValues.end()){
        int index = it - CostsIdValues.begin();
        LLVM_DEBUG(llvm::dbgs() <<  " found [" << *it <<"]\n" );
        return CostsId(index);
    }

    LLVM_DEBUG( 
        {
            for ( auto& i : CostsIdValues ){
                llvm::dbgs() << i << " = " << basicString << " : " << std::to_string(basicString == i) << "\n";
            }
        }
    );
    llvm::dbgs() << "Unknown value: "<<basicString<<"\n";

    llvm_unreachable("Unknown cost value!");
}

string CPUCosts::CostsIdToString(CostsId id){
    return CostsIdValues[id];
}

void CPUCosts::dump(){
    llvm::dbgs() << "Available model costs:\n";
    for(auto pair : costsMap){
        llvm::dbgs() << "[" << CostsIdToString(pair.first) << ", " << pair.second << "]\n";
    }
}

double CPUCosts::getCost(CPUCosts::CostsId id) {
    //FIXME: the workaround is done due to the model not being able to distiguish between a delta in fixp due to change of datatype or change of bit number
    // in this way should fix the 90% of the cases

    bool fixDoubleCast = false;
    switch (id) {
        case CAST_HALF_FIX:
        case CAST_FIX_HALF:
        case CAST_FIX_DOUBLE:
        case CAST_FIX_FLOAT:
        case CAST_FLOAT_FIX:
        case CAST_DOUBLE_FIX:
            fixDoubleCast=true;
            break;
        default:
            break;
    }



    auto it = costsMap.find(id);
    if(it!=costsMap.end()){
        if(fixDoubleCast){
            return it->second - getCost(CAST_FIX_FIX);
        }
        return it->second;
    }

    llvm_unreachable("This cost was not loaded from model file!");
}
