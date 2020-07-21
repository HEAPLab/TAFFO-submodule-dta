#include <stdio.h>
#include <stdlib.h>

#  define DATA_TYPE double
#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x,y) pow(x,y)

#define POLYBENCH_DUMP_TARGET stdout

#   define TSTEPS 100
#   define N 250

#   define _PB_TSTEPS TSTEPS
#   define _PB_N N
int main(){

/* Retrieve problem size. */
    int n = N;
    int tsteps = TSTEPS;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) A[N][N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) B[N][N];


    int i __attribute__((annotate("scalar(range(-250, 250) final disabled)")));
    int j __attribute__((annotate("scalar(range(-250, 250) final disabled)")));
    int t;

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
        {
            A[i][j] = ((DATA_TYPE) i*(j+2) + 2) / n;
            B[i][j] = ((DATA_TYPE) i*(j+3) + 3) / n;
        }

    for (t = 0; t < _PB_TSTEPS; t++)
    {
        for (i = 1; i < _PB_N - 1; i++)
            for (j = 1; j < _PB_N - 1; j++)
                B[i][j] = SCALAR_VAL(0.2) * (A[i][j] + A[i][j-1] + A[i][1+j] + A[1+i][j] + A[i-1][j]);
        for (i = 1; i < _PB_N - 1; i++)
            for (j = 1; j < _PB_N - 1; j++)
                A[i][j] = SCALAR_VAL(0.2) * (B[i][j] + B[i][j-1] + B[i][1+j] + B[1+i][j] + B[i-1][j]);
    }

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++) {
            if ((i * n + j) % 20 == 0) fprintf(POLYBENCH_DUMP_TARGET, "\n");
            fprintf(POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, A[i][j]);
        }

    return 0;
}