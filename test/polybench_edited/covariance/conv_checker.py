from subprocess import Popen, PIPE
from decimal import *
import os.path

if not os.path.isfile('./magiclang2.sh'):
    print("Script run from the wrong fodler.")
    exit(-1)






def compileAndCheck(TUNING_ENOB, TUNING_TIME, TUNING_CAST_TIME, DOUBLE_ENABLED):
    global dataset
    # Compilation
    compilationParams = []
    compilationParams.append("./magiclang2.sh")
    compilationParams.append("-lm")
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedmode=true")
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningenob=" + str(TUNING_ENOB))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningtime=" + str(TUNING_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningcastingtime=" + str(TUNING_CAST_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixeddoubleenabled=" + DOUBLE_ENABLED)
    compilationParams.append("polybench_edited/covariance/covariance.c")
    compilationParams.append("-o")
    compilationParams.append("polybench_edited/covariance/covariance.fixp")

    process = Popen(compilationParams, stderr=PIPE, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if (exit_code != 0):
        print("Error compiling the program!")
        exit(-1)

    process = Popen(["polybench_edited/covariance/covariance.fixp"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if (exit_code != 0):
        print("Error executing the program!")
        exit(-1)

    output = output.decode('ascii').strip()
    output = output.replace('\n', '')
    output = output.split(' ')

    for i in range(0, len(output)):
        output[i] = Decimal(output[i])

    accumulator = Decimal(0.0)
    for i in range(0, len(output)):
        accumulator += abs(output[i] - dataset[i])


    return accumulator

def loadReferenceRun():
    process = Popen(["polybench_edited/covariance/covariance.flt"], stdout=PIPE)
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

#Parameters:

#Loading reference dataset
dataset = loadReferenceRun()




TUNING_ENOB = 100000
TUNING_TIME = 1000
TUNING_CAST_TIME = 500
DOUBLE_ENABLED = "false"

print("Very precise", compileAndCheck(100, 1, 0.5, "true"))

print("No double but precise", compileAndCheck(100, 1, 0.5, "false"))

print("Medium precision", compileAndCheck(50, 50, 25, "true"))

print("Quick mode", compileAndCheck(1, 100, 50, "true"))