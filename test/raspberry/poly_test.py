import datetime
from subprocess import Popen, PIPE
from decimal import *
import os.path
import sys
import json
import csv

#if not os.path.isfile('./magiclang2.sh'):
#    print("Script run from the wrong fodler.")
#    exit(-1)

PROGRAM_NAME = sys.argv[1]
COST_MODEL = "raspberry-clang.csv"
OPT_FLAG="-O0"
COMPILER_NAME="clang"
TEST_DIM="MEDIUM"
HONEST_MODE_ENABLED=True
TAFFO_DEBUG=False
print("Running test for", PROGRAM_NAME, file=sys.stderr)


def compileAndCheck(NAME, MIX_MODE, TUNING_ENOB, TUNING_TIME, TUNING_CAST_TIME, DOUBLE_ENABLED):
    print("mixed", NAME, file=sys.stderr)
    cumulated_time = 0
    for i in range(0, 20):
        print("Run", i, file=sys.stderr)
        process = Popen(["compiled/" + PROGRAM_NAME + "/" + PROGRAM_NAME + "_" + NAME + ".fixp"], stdout=PIPE, stderr=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()

        if (exit_code != 0):
            print("Error executing the program!", file=sys.stderr)
            return {"ERROR": "EXECUTION"}

        output = output.decode('ascii').strip()
        output = output.replace('\n', '')
        output = output.split(' ')


        run_time = float(err.decode('ascii').strip())
        cumulated_time+=run_time

    run_time = cumulated_time/20
    for i in range(0, len(output)):
        output[i] = float(output[i])



    var = {}
    var["RUNNING_TIME"] = run_time
    var["SPEEDUP"] = orig_run_time/run_time


    var["MIX_MODE"] = MIX_MODE
    var["NAME"] = NAME
    return var


def loadReferenceRun():
    print("Floating point", file=sys.stderr)
    cumulated_time = 0
    for i in range(0, 20):
        print("Run", i, file=sys.stderr)
        process = Popen(["compiled/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".flt"], stdout=PIPE, stderr=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()

        if (exit_code != 0):
            print("Error executing reference the program!", file=sys.stderr)
            exit(-1)

        run_time = float(err.decode('ascii').strip())
        cumulated_time+=run_time


    return (output, cumulated_time/20)


# Parameters:

# Loading reference dataset

#pre compilation in order to prepare the correct ll file
#compileAndCheck("NONE", "false", 0, 0, 0, "false")
dataset, orig_run_time = loadReferenceRun()


testSet = {}

testSet["ORIG"] = {}
testSet["ORIG"]["RUNNING_TIME"] = orig_run_time

testSet["PRECISE"] = compileAndCheck("PRECISE", "true", 100000, 1, 1, "true")

testSet["NODOUBLE"] = compileAndCheck("NODOUBLE", "true", 1000, 1, 1, "false")

testSet["MEDIUM"] = compileAndCheck("MEDIUM", "true", 50, 50, 50, "true")

testSet["IMPRECISE"] = compileAndCheck("IMPRECISE", "true", 20, 80, 80, "true")

testSet["QUICK"] = compileAndCheck("QUICK", "true", 1, 1000, 1000, "true")

testSet["FIX"] = compileAndCheck("FIX", "false", 0, 0, 0, "true")

print(json.dumps(testSet, indent=4))
