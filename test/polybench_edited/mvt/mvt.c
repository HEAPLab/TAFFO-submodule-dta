#include <stdio.h>
#include <stdlib.h>
#include "../instrument.h"
#  define DATA_TYPE double
#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x,y) pow(x,y)

#   define N 400
#   define _PB_N N

#define POLYBENCH_DUMP_TARGET stdout

int main(){
    TIMING_CPUCLOCK_START();
    /* Retrieve problem size. */
    int n = N;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) A[N][N];
    DATA_TYPE __attribute__((annotate("scalar(range(-256, 255) final error(1e-100))"))) x1[N];
    DATA_TYPE __attribute__((annotate("scalar(range(-256, 255) final error(1e-100))"))) x2[N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) y_1[N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) y_2[N];


    int i __attribute__((annotate("scalar(range(0, 400) final)")));
    int j __attribute__((annotate("scalar(range(0, 400) final)")));

    for (i = 0; i < n; i++)
    {
        x1[i] = (DATA_TYPE) (i % n) / n;
        x2[i] = (DATA_TYPE) ((i + 1) % n) / n;
        y_1[i] = (DATA_TYPE) ((i + 3) % n) / n;
        y_2[i] = (DATA_TYPE) ((i + 4) % n) / n;
        for (j = 0; j < n; j++)
            A[i][j] = (DATA_TYPE) (i*j % n) / n;
    }

    for (i = 0; i < _PB_N; i++)
        for (j = 0; j < _PB_N; j++)
            x1[i] = x1[i] + A[i][j] * y_1[j];
    for (i = 0; i < _PB_N; i++)
        for (j = 0; j < _PB_N; j++)
            x2[i] = x2[i] + A[j][i] * y_2[j];

    for (i = 0; i < n; i++) {
        if (i % 20 == 0) fprintf (POLYBENCH_DUMP_TARGET, "\n");
        fprintf (POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, x1[i]);
    }


    for (i = 0; i < n; i++) {
        if (i % 20 == 0) fprintf (POLYBENCH_DUMP_TARGET, "\n");
        fprintf (POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, x2[i]);
    }
    TIMING_CPUCLOCK_TOGGLE();
    TIMING_CPUCLOCK_PRINT();
    return 0;
}