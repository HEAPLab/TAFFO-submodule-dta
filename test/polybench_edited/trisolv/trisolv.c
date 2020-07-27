#include <stdio.h>
#include <stdlib.h>
#include "../instrument.h"
#  define DATA_TYPE double
#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x,y) pow(x,y)

#define POLYBENCH_DUMP_TARGET stdout
#   define N 400
#   define _PB_N N

int main(){
    TIMING_CPUCLOCK_START();
    /* Retrieve problem size. */
    int n = N;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) L[N][N];
    DATA_TYPE __attribute__((annotate("scalar(range(-1, 1) error(1e-100))"))) x[N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) b[N];


    int i __attribute__((annotate("scalar(range(-8000, 8000) final)")));
    int j __attribute__((annotate("scalar(range(-8000, 8000) final)")));

    for (i = 0; i < n; i++)
    {
        x[i] = - 999;
        b[i] =  i ;
        for (j = 0; j <= i; j++)
            L[i][j] = (DATA_TYPE) (i+n-j+1)*2/n;
    }

    for (i = 0; i < _PB_N; i++)
    {
        x[i] = b[i];
        for (j = 0; j <i; j++)
            x[i] -= L[i][j] * x[j];
        x[i] = x[i] / L[i][i];
    }

    for (i = 0; i < n; i++) {
        fprintf (POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, x[i]);
        if (i % 20 == 0) fprintf (POLYBENCH_DUMP_TARGET, "\n");
    }
    TIMING_CPUCLOCK_TOGGLE();
    TIMING_CPUCLOCK_PRINT();
    return 0;
}