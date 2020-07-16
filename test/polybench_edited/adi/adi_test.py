from subprocess import Popen, PIPE
from decimal import *
import os.path

if not os.path.isfile('./magiclang2.sh'):
    print("Script run from the wrong fodler.")
    exit(-1)






def compileAndCheck(MIX_MODE, TUNING_ENOB, TUNING_TIME, TUNING_CAST_TIME, DOUBLE_ENABLED):
    global dataset
    # Compilation
    compilationParams = []
    compilationParams.append("./magiclang2.sh")
    compilationParams.append("-debug-taffo")
    compilationParams.append("-lm")
    compilationParams.append("-Xvra")
    compilationParams.append("-propagate-all")
    compilationParams.append("-Xvra")
    compilationParams.append("-unroll=0")
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedmode="+MIX_MODE)
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningenob=" + str(TUNING_ENOB))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningtime=" + str(TUNING_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixedtuningcastingtime=" + str(TUNING_CAST_TIME))
    compilationParams.append("-Xdta")
    compilationParams.append("-mixeddoubleenabled=" + DOUBLE_ENABLED)
    compilationParams.append("-debug-taffo")
    compilationParams.append("polybench_edited/adi/adi.c")
    compilationParams.append("-o")
    compilationParams.append("polybench_edited/adi/adi.fixp")

    process = Popen(compilationParams, stderr=PIPE, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    text_file = open("result.txt", "w")
    text_file.write(err.decode('ascii'))
    text_file.close()

    if (exit_code != 0):
        print(err.decode('ascii'))
        print("Error compiling the program!")
        exit(-1)

    process = Popen(["polybench_edited/adi/adi.fixp"], stdout=PIPE)
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
    skipped = 0
    for i in range(0, len(output)):
        if dataset[i] != 0:
            accumulator += abs((output[i] - dataset[i])/dataset[i])
            #print(output[i], dataset[i])
        else:
            skipped += 1

    print("Skipped", skipped)
    return accumulator/len(output)

def loadReferenceRun():
    process = Popen(["polybench_edited/adi/adi.flt"], stdout=PIPE)
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

print("Very precise", compileAndCheck("true", 100000, 1, 1, "true"))

print("No double but precise", compileAndCheck("true", 1000, 1, 1, "false"))

print("Medium precision", compileAndCheck("true", 50, 50, 50, "false"))

print("Quick mode", compileAndCheck("true", 1, 10000, 10000, "false"))

print("Fix only", compileAndCheck("false", 0, 0, 0, "true"))
