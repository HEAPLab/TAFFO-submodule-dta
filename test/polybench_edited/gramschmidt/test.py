import datetime
from subprocess import Popen, PIPE
from decimal import *
import os.path
import sys
import json
import csv


process = Popen(["./gramschmidt.flt"], stdout=PIPE, stderr=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()

if (exit_code != 0):
    print("Error executing the program!", file=sys.stderr)
    exit(-1)

output = output.decode('ascii').strip()
output = output.replace('\n', '')
output = output.split(' ')

for i in range(0, len(output)):
    output[i] = float(output[i])


process = Popen(["./gramschmidt.fixp"], stdout=PIPE, stderr=PIPE)
(output1, err) = process.communicate()
exit_code = process.wait()

if (exit_code != 0):
    print("Error executing the program!", file=sys.stderr)
    exit(-1)

output1 = output1.decode('ascii').strip()
output1 = output1.replace('\n', '')
output1 = output1.split(' ')

for i in range(0, len(output1)):
    output1[i] = float(output1[i])

accumulator = (0.0)
skipped = 0

if len(output) != len(output1):
    print("FUUUUUUUUUUUU")
    exit(-1)

problematic = 0
for i in range(0, len(output)):
    if abs(output1[i]) >= 10**-3: #To keep out values near to zero: will have a huuuge impact on error
        tmp = abs((output[i] - output1[i]) / output1[i])
        accumulator += tmp
        if tmp>1:
            problematic += 1
            print(output[i], output1[i], file=sys.stderr)
    else:
        skipped += 1


err = accumulator / (len(output)-skipped)

print("Problematic: ", problematic, "on", len(output)-skipped, problematic/(len(output)-skipped) *100)