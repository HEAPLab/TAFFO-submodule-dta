#include "llvm/ADT/Statistic.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Pass.h"
#define DEBUG_TYPE "taffo-dta"

#ifndef DTACONFIG
#define DTACONFIG
llvm::cl::opt<int> FracThreshold("minfractbits", llvm::cl::value_desc("bits"),
                                 llvm::cl::desc("Threshold of fractional bits in fixed point numbers"),
                                 llvm::cl::init(3));
llvm::cl::opt<int> TotalBits("totalbits", llvm::cl::value_desc("bits"),
                             llvm::cl::desc("Total amount of bits in fixed point numbers"), llvm::cl::init(32));
llvm::cl::opt<int> SimilarBits("similarbits", llvm::cl::value_desc("bits"),
                               llvm::cl::desc("Maximum number of difference bits that leads two fixp formats to merge"),
                               llvm::cl::init(2));
llvm::cl::opt<bool> DisableTypeMerging("notypemerge",
                                       llvm::cl::desc("Disables adjacent type optimization"), llvm::cl::init(false));
llvm::cl::opt<bool> IterativeMerging("iterative",
                                     llvm::cl::desc("Enables old iterative merging"), llvm::cl::init(false));

llvm::cl::opt<bool> MixedMode("mixedmode",
                                     llvm::cl::desc("Enable or disable the experimental mixed-precision mode"), llvm::cl::init(false));

llvm::cl::opt<double> MixedTuningENOB("mixedtuningenob", llvm::cl::value_desc("Enob importance"),
                               llvm::cl::desc("Set the importance given to the best ENOB preservation in mixed precision mode"),
                               llvm::cl::init(1));

llvm::cl::opt<double> MixedTuningTime("mixedtuningtime", llvm::cl::value_desc("Time importance"),
                                      llvm::cl::desc("Set the importance to keep down the computation time in mixed precision mode"),
                                      llvm::cl::init(1));
llvm::cl::opt<double> MixedTuningCastingTime("mixedtuningcastingtime", llvm::cl::value_desc("Casting time importance"),
                                      llvm::cl::desc("Set the importance to keep down the computation  casting time in mixed precision mode"),
                                      llvm::cl::init(1));

llvm::cl::opt<bool> MixedDoubleEnabled("mixeddoubleenabled", llvm::cl::value_desc("Double enabled"),
                                             llvm::cl::desc("Set if the double dataype can be used in the resulting mix"),
                                             llvm::cl::init(true));


llvm::cl::opt<string> CostModelFilename("costmodelfilename", llvm::cl::value_desc("Cost model filename"),
                                       llvm::cl::desc("Set the filename to load optimization constant parameter i.e. operation costs"),
                                       llvm::cl::init("DOES-NOT-EXIST"));

STATISTIC(FixCast, "Number of fixed point format cast");
#endif