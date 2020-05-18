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

llvm::cl::opt<int> ForceFloat("forcefloat",
                              llvm::cl::desc("Force a specific floating point type as output [0=half, 1=float, 2=double, 3=fp128]"), llvm::cl::init(-1));

STATISTIC(FixCast, "Number of fixed point format cast");
#endif