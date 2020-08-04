import datetime
from subprocess import Popen, PIPE
from decimal import *
import os.path
import sys
import json
import csv

if not os.path.isfile('./magiclang2.sh'):
    print("Script run from the wrong fodler.")
    exit(-1)

PROGRAM_NAME = sys.argv[1]
COST_MODEL = "i7-4.csv"
OPT_FLAG="-O0"
COMPILER_NAME="clang"
TEST_DIM="MEDIUM"
HONEST_MODE_ENABLED=True
TAFFO_DEBUG=False
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
    compilationParams.append("polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".fixp")


    start = datetime.datetime.now()
    print("Compilation params:", " ".join(compilationParams), file=sys.stderr)
    process = Popen(compilationParams, stderr=PIPE, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    end = datetime.datetime.now()
    delta = end-start

    text_file = open("result.txt", "w")
    text_file.write(err.decode('ascii'))
    text_file.close()

    if (exit_code != 0):
        print(err.decode('ascii'), file=sys.stderr)
        print("Error compiling the program!", file=sys.stderr)
        return {"ERROR": "COMPILATION"}

    if NAME == "NONE":
        print(".ll files generated, not performing tests...", file=sys.stderr)
        return {"ERROR": "NO DATA"}

    cumulated_time = 0
    for i in range(0, 20):
        process = Popen(["polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".fixp"], stdout=PIPE, stderr=PIPE)
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

    accumulator = (0.0)
    skipped = 0

    if len(output) != len(dataset):
        print("FUUUUUUUUUUUU")
        exit(-1)


    for i in range(0, len(output)):
        if abs(dataset[i]) >= 10**-3: #To keep out values near to zero: will have a huuuge impact on error
            tmp = abs((output[i] - dataset[i]) / dataset[i])
            accumulator += tmp
            if tmp>1:
                print(output[i], dataset[i], file=sys.stderr)
            #print(output[i], dataset[i], file=sys.stderr)
        else:
            skipped += 1


    err = accumulator / (len(output)-skipped)

    var = {}
    var["SKIPPED_TEST"] = skipped
    var["COMPILE_TIME"] = delta.total_seconds()
    var["RUNNING_TIME"] = run_time
    var["SPEEDUP"] = orig_run_time/run_time

    if MIX_MODE == "true":
        with open('stats.txt', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                var[row[0]] = row[1]
        var["TUNING_ENOB"] = TUNING_ENOB
        var["TUNING_TIME"] = TUNING_TIME
        var["TUNING_CAST_TIME"] = TUNING_CAST_TIME
        var["DOUBLE_ENABLED"] = DOUBLE_ENABLED

    var["MIX_MODE"] = MIX_MODE
    var["ERR"] = float(err)
    var["NAME"] = NAME
    return var


def loadReferenceRun():
    compilationParams = []
    compilationParams.append(COMPILER_NAME)
    compilationParams.append("-lm")
    compilationParams.append(OPT_FLAG)
    compilationParams.append("polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".fixp.1.magiclangtmp.ll")
    compilationParams.append("-o")
    compilationParams.append("polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".flt")

    process = Popen(compilationParams, stderr=PIPE, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    cumulated_time = 0
    for i in range(0, 20):
        process = Popen(["polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".flt"], stdout=PIPE, stderr=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()

        if (exit_code != 0):
            print("Error executing reference the program!", file=sys.stderr)
            exit(-1)

        output = output.decode('ascii').strip()
        output = output.replace('\n', '')
        output = output.split(' ')

        run_time = float(err.decode('ascii').strip())
        cumulated_time+=run_time

    for i in range(0, len(output)):
        output[i] = float(output[i])

    return (output, cumulated_time/20)


# Parameters:

# Loading reference dataset

#pre compilation in order to prepare the correct ll file
compileAndCheck("NONE", "false", 0, 0, 0, "false")
dataset, orig_run_time = loadReferenceRun()


testSet = {}

testSet["PRECISE"] = compileAndCheck("PRECISE", "true", 100000, 1, 1, "true")

testSet["NODOUBLE"] = compileAndCheck("NODOUBLE", "true", 1000, 1, 1, "false")

testSet["MEDIUM"] = compileAndCheck("MEDIUM", "true", 50, 50, 50, "true")

testSet["IMPRECISE"] = compileAndCheck("IMPRECISE", "true", 20, 80, 80, "true")

testSet["QUICK"] = compileAndCheck("QUICK", "true", 1, 1000, 1000, "true")

testSet["FIX"] = compileAndCheck("FIX", "false", 0, 0, 0, "true")

print(json.dumps(testSet, indent=4))
