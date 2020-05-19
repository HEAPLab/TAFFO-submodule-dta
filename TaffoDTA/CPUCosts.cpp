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

CPUCosts::CostsId CPUCosts::decodeId(string &basicString) {
    auto it = std::find(CostsIdValues.begin(), CostsIdValues.end(), basicString);
    if(it != CostsIdValues.end()){
        int index = it - CostsIdValues.begin();
        return CostsId(index);
    }

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
    auto it = costsMap.find(id);
    if(it!=costsMap.end()){
        return it->second;
    }

    llvm_unreachable("This cost was not loaded from model file!");
}
