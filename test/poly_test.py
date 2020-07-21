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
print("Running test for", PROGRAM_NAME, file=sys.stderr)


def compileAndCheck(NAME, MIX_MODE, TUNING_ENOB, TUNING_TIME, TUNING_CAST_TIME, DOUBLE_ENABLED):
    print("Running compilation", NAME)

    global dataset
    # Compilation
    compilationParams = []
    compilationParams.append("./magiclang2.sh")
    compilationParams.append("-lm")
    compilationParams.append("-Xvra")
    compilationParams.append("-propagate-all")
    compilationParams.append("-Xvra")
    compilationParams.append("-unroll=0")
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedmode=" + MIX_MODE)
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningenob=" + str(TUNING_ENOB))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningtime=" + str(TUNING_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningcastingtime=" + str(TUNING_CAST_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixeddoubleenabled=" + DOUBLE_ENABLED)
    # compilationParams.append("-debug-taffo")
    compilationParams.append("polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".c")
    compilationParams.append("-o")
    compilationParams.append("polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".fixp")

    process = Popen(compilationParams, stderr=PIPE, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    text_file = open("result.txt", "w")
    text_file.write(err.decode('ascii'))
    text_file.close()

    if (exit_code != 0):
        print(err.decode('ascii'))
        print("Error compiling the program!")
        return {"ERROR": "COMPILATION"}

    process = Popen(["polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".fixp"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if (exit_code != 0):
        print("Error executing the program!")
        return {"ERROR": "EXECUTION"}

    output = output.decode('ascii').strip()
    output = output.replace('\n', '')
    output = output.split(' ')

    for i in range(0, len(output)):
        output[i] = Decimal(output[i])

    accumulator = Decimal(0.0)
    skipped = 0
    for i in range(0, len(output)):
        if dataset[i] != 0:
            accumulator += abs((output[i] - dataset[i]) / dataset[i])
            # print(output[i], dataset[i])
        else:
            skipped += 1


    err = accumulator / len(output)

    var = {}
    var["SKIPPED_TEST"] = skipped

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
    process = Popen(["polybench_edited/" + PROGRAM_NAME + "/" + PROGRAM_NAME + ".flt"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if (exit_code != 0):
        print("Error executing reference the program!")
        exit(-1)

    output = output.decode('ascii').strip()
    output = output.replace('\n', '')
    output = output.split(' ')

    for i in range(0, len(output)):
        output[i] = Decimal(output[i])

    return output


# Parameters:

# Loading reference dataset
dataset = loadReferenceRun()

TUNING_ENOB = 100000
TUNING_TIME = 1000
TUNING_CAST_TIME = 500
DOUBLE_ENABLED = "false"

testSet = {}

testSet["PRECISE"] = compileAndCheck("PRECISE", "true", 100000, 1, 1, "true")

testSet["NOFLOAT"] = compileAndCheck("NOFLOAT", "true", 1000, 1, 1, "false")

testSet["MEDIUM"] = compileAndCheck("MEDIUM", "true", 50, 50, 50, "false")

testSet["QUICK"] = compileAndCheck("QUICK", "true", 1, 10000, 10000, "false")

testSet["FIX"] = compileAndCheck("FIX", "false", 0, 0, 0, "true")

print(json.dumps(testSet, indent=4))
