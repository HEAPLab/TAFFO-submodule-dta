#include <stdio.h>
#include <stdlib.h>
#include "../instrument.h"
#  define DATA_TYPE double
#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x, y) pow(x,y)

#define POLYBENCH_DUMP_TARGET stdout


#   define M 20
#   define N 30

#   define _PB_M M
#   define _PB_N N

DATA_TYPE __attribute__((annotate("scalar(range(-256, 255) final error(1e-100))"))) C[N][N];
DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) A[N][M];
DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) B[N][M];

int main() {
    TAFFO_DUMPCONFIG();
    TIMING_CPUCLOCK_START();
    /* Retrieve problem size. */
    int n = N;
    int m = M;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) alpha;
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) beta;


    int i __attribute__((annotate("scalar(range(0, 240))")));
    int j __attribute__((annotate("scalar(range(0, 200))")));
    int k;

    alpha = 1.5;
    beta = 1.2;
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++) {
            A[i][j] = (DATA_TYPE) ((i * j + 1) % n) / n;
            B[i][j] = (DATA_TYPE) ((i * j + 2) % m) / m;
        }


    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++) {
            C[i][j] = (DATA_TYPE) ((i * j + 3) % n) / m;
        }


    for (i = 0; i < _PB_N; i++) {
        for (j = 0; j <= i; j++)
            C[i][j] *= beta;
        for (k = 0; k < _PB_M; k++)
            for (j = 0; j <= i; j++) {
                C[i][j] += A[j][k] * alpha * B[i][k] + B[j][k] * alpha * A[i][k];
            }
    }
    TIMING_CPUCLOCK_TOGGLE();
    TIMING_CPUCLOCK_PRINT();
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if ((i * n + j) % 20 == 0) fprintf(POLYBENCH_DUMP_TARGET, "\n");
            fprintf(POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, C[i][j]);
        }
    }

    return 0;

}