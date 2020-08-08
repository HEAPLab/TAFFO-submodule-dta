import datetime
from subprocess import Popen, PIPE
from decimal import *
import os.path
import sys
import json
import csv
from pathlib import Path

if not os.path.isfile('./magiclang2.sh'):
    print("Script run from the wrong fodler.")
    exit(-1)



PROGRAM_NAME = sys.argv[1]
COST_MODEL = "raspberry-clang.csv"
OPT_FLAG="-O0"
COMPILER_NAME="clang-8"
TEST_DIM="MEDIUM"
HONEST_MODE_ENABLED=True
TAFFO_DEBUG=False
COMPILATION_TARGET_PARAMS="-target armv6l-unknown-linux-gnueabihf -mfloat-abi=hard " \
                          "--sysroot=/home/nicola/dev/cloned/raspberryTools/tools/arm-bcm2708/arm-linux-gnueabihf/arm-linux-gnueabihf/sysroot " \
                          "-B/home/nicola/dev/cloned/raspberryTools/tools/arm-bcm2708/arm-linux-gnueabihf/ " \
                          "-L/home/nicola/dev/cloned/raspberryTools/tools/arm-bcm2708/arm-bcm2708-linux-gnueabi/lib/gcc/arm-bcm2708-linux-gnueabi"

Path("raspberry/compiled/" + PROGRAM_NAME + "/").mkdir(parents=True, exist_ok=True)
print("Running test for", PROGRAM_NAME, file=sys.stderr)


def compileAndCheck(NAME, MIX_MODE, TUNING_ENOB, TUNING_TIME, TUNING_CAST_TIME, DOUBLE_ENABLED):
    print("Running compilation", NAME, file=sys.stderr)

    global dataset
    global COST_MODEL
    global orig_run_time
    global TEST_DIM
    global HONEST_MODE_ENABLED
    # Compilation
    compilationParams = []
    compilationParams.append("./magiclang2.sh")
    compilationParams.append("-lm")
    compilationParams.append(OPT_FLAG)
    compilationParams.append(COMPILATION_TARGET_PARAMS)
    compilationParams.append("-Xvra")
    compilationParams.append("-propagate-all")
    compilationParams.append("-Xvra")
    compilationParams.append("-unroll=1")
    compilationParams.append("-Xvra")
    compilationParams.append("-max-unroll=3")
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedmode=" + MIX_MODE)
    compilationParams.append("-Xdta")
    compilationParams.append("-costmodelfilename=" + COST_MODEL)
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningenob=" + str(TUNING_ENOB))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningtime=" + str(TUNING_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningcastingtime=" + str(TUNING_CAST_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixeddoubleenabled=" + DOUBLE_ENABLED)
    if TAFFO_DEBUG:
        compilationParams.append("-debug-taffo")
    if HONEST_MODE_ENABLED:
        compilationParams.append("-honest-mode")
    compilationParams.append("-D"+TEST_DIM+"_DATASET")
    compilationParams.append("polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".c")
    compilationParams.append("-o")
    compilationParams.append("raspberry/compiled/" + PROGRAM_NAME + "/" + PROGRAM_NAME + "_" + NAME+ ".fixp")


    start = datetime.datetime.now()
    print("Compilation params:", " ".join(compilationParams), file=sys.stderr)
    process = Popen(compilationParams, stderr=PIPE, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    end = datetime.datetime.now()
    delta = end-start


    return ""


def loadReferenceRun():
    compilationParams = []
    compilationParams.append(COMPILER_NAME)
    compilationParams.append("-lm")
    compilationParams.append("-S") #generate assembly as output
    compilationParams.append(OPT_FLAG)
    compilationParams.extend(COMPILATION_TARGET_PARAMS.split(" "))
    compilationParams.append("raspberry/compiled/" + PROGRAM_NAME + "/" + PROGRAM_NAME + "_NONE.fixp.4.magiclangtmp.ll")
    compilationParams.append("-o")
    compilationParams.append("raspberry/compiled/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".4.flt.s")


    print("Compilation params:", " ".join(compilationParams), file=sys.stderr)
    process = Popen(compilationParams, stderr=PIPE, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    print(err)

    return ""


# Parameters:

# Loading reference dataset

#pre compilation in order to prepare the correct ll file
compileAndCheck("NONE", "false", 0, 0, 0, "false")
orig_run_time = loadReferenceRun()


testSet = {}

#testSet["PRECISE"] = compileAndCheck("PRECISE", "true", 100000, 1, 1, "true")

#testSet["NODOUBLE"] = compileAndCheck("NODOUBLE", "true", 1000, 1, 1, "false")

#testSet["MEDIUM"] = compileAndCheck("MEDIUM", "true", 50, 50, 50, "true")

#testSet["IMPRECISE"] = compileAndCheck("IMPRECISE", "true", 20, 80, 80, "true")

#testSet["QUICK"] = compileAndCheck("QUICK", "true", 1, 1000, 1000, "true")

#testSet["FIX"] = compileAndCheck("FIX", "false", 0, 0, 0, "true")

#print(json.dumps(testSet, indent=4))
