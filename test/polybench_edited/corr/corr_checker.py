from subprocess import Popen, PIPE
from decimal import *
import os.path

if not os.path.isfile('./magiclang2.sh'):
    print("Script run from the wrong fodler.")
    exit(-1)






def compileAndCheck(TUNING_ENOB, TUNING_TIME, TUNING_CAST_TIME):
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
    compilationParams.append("-mixeddoubleenabled=true")
    compilationParams.append("polybench_edited/corr/corr.c")
    compilationParams.append("-o")
    compilationParams.append("polybench_edited/corr/corr.fixp")

    process = Popen(compilationParams, stderr=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if (exit_code != 0):
        print("Error compiling the program!")
        exit(-1)

    process = Popen(["polybench_edited/corr/corr.fixp"], stdout=PIPE)
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
        accumulator += abs(output[i] - 1)


    print(accumulator)

#Parameters:
TUNING_ENOB = 100000
TUNING_TIME = 1000
TUNING_CAST_TIME = 500

for param in range(1, 5000, 100):
    TUNING_ENOB = param
    TUNING_TIME = 100000 - TUNING_ENOB
    TUNING_CAST_TIME = TUNING_TIME / 2
    print(param, end=' ')
    compileAndCheck(TUNING_ENOB, TUNING_TIME,TUNING_CAST_TIME)



