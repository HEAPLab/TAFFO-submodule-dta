#include <stdio.h>
#include <stdlib.h>

#define POLYBENCH_DUMP_TARGET stdout
#  define DATA_TYPE double
#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x,y) pow(x,y)

#   define N 250
#define _PB_N N

int main(){

    /* Retrieve problem size. */
    int n = N;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) alpha;
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) beta;
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) A[N][N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) B[N][N];
    DATA_TYPE __attribute__((annotate("scalar(range(-256, 255) final error(1e-100))"))) tmp[N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) x[N];
    DATA_TYPE __attribute__((annotate("scalar(range(-256, 255) final error(1e-100))"))) y[N];


    int i __attribute__((annotate("scalar(range(0,250) final disabled)")));
    int j __attribute__((annotate("scalar(range(0,250) final disabled)")));

    alpha = 1.5;
    beta = 1.2;
    for (i = 0; i < n; i++)
    {
        x[i] = (DATA_TYPE)( i % n) / n;
        for (j = 0; j < n; j++) {
            A[i][j] = (DATA_TYPE) ((i*j+1) % n) / n;
            B[i][j] = (DATA_TYPE) ((i*j+2) % n) / n;
        }
    }

    for (i = 0; i < _PB_N; i++)
    {
        tmp[i] = SCALAR_VAL(0.0);
        y[i] = SCALAR_VAL(0.0);
        for (j = 0; j < _PB_N; j++)
        {
            tmp[i] = A[i][j] * x[j] + tmp[i];
            y[i] = B[i][j] * x[j] + y[i];
        }
        y[i] = alpha * tmp[i] + beta * y[i];
    }

    for (i = 0; i < n; i++) {
        if (i % 20 == 0) fprintf (POLYBENCH_DUMP_TARGET, "\n");
        fprintf (POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, y[i]);
    }

    return 0;
}