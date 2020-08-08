from subprocess import Popen, PIPE
from decimal import *
import os.path
import sys
import json
import csv
import argparse



parser = argparse.ArgumentParser(description='Run all the polybench tests and instrument errors.')
parser.add_argument('--dest', type=str,
                    help='name of the file where to place the results', required=True)


args = parser.parse_args()

dest_file = args.dest

print("Results will be saved in file", dest_file)




if not os.path.isfile('./magiclang2.sh'):
    print("Script run from the wrong fodler.")
    exit(-1)


def runSet(name):
    print("Processing", name)
    process = Popen(["python", "raspberry/generate_single_test.py", name], stdout=PIPE, stderr=sys.stderr)
    (output, err) = process.communicate()
    exit_code = process.wait()
    print(output)

    if (exit_code != 0):
        print("Error executing the test!")
        return {}

    #results = json.loads(output.decode('ascii'))

    return ""



TEST_SET = ["2mm", "3mm", "adi", "atax", "bicg", "cholesky", "corr", "covariance", "deriche", "doitgen", "durbin",
            "fdtd-2d", "gemm", "gemmver", "gesummv", "gramschmidt", "heat-3d", "jacobi-1d", "jacobi-2d", "lu", "ludcmp",
            "mvt", "seidel-2d", "symm", "syr2k", "syrk", "trisolv", "trmm", "floyd-warshall", "nussinov"]

OK_SET=[]
NOTOK_SET=[]

resAll={}

for test in TEST_SET:
    res = runSet(test)
