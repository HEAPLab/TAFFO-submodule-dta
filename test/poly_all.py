from subprocess import Popen, PIPE
from decimal import *
import os.path
import sys
import json
import csv

if not os.path.isfile('./magiclang2.sh'):
    print("Script run from the wrong fodler.")
    exit(-1)


def runSet(name):
    process = Popen(["python", "poly_test.py", name], stdout=PIPE, stderr=sys.stderr)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if (exit_code != 0):
        print("Error executing reference the program!")
        exit(-1)

    results = json.loads(output.decode('ascii'))

    return results


def evaluateResults(res):
    for (k) in res:
        v = res[k]
        if v['ERR'] > 0.1:
            success = False
        else:
            success = True
        print("Error for", k, ":", v['ERR'], success)


TEST_SET = ["2mm", "3mm", "adi", "atax", "bicg", "cholesky", "corr", "covariance", "deriche", "doitgen", "durbin",
            "fdtd-2d", "gemm", "gemmver", "gesummv", "gramschmidt", "heat-3d", "jacobi-1d", "jacobi-2d", "lu", "ludcmp",
            "mvt", "seidel-2d", "symm", "syr2k", "syrk", "trisolv", "trmm"]

for test in TEST_SET:
    res = runSet(test)
    evaluateResults(res)
