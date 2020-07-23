#include <stdio.h>
#include <stdlib.h>

#  define DATA_TYPE double
#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x,y) pow(x,y)

#   define M 390
#   define N 410

#   define _PB_M M
#   define _PB_N N

#define POLYBENCH_DUMP_TARGET stdout

int main(){
    /* Retrieve problem size. */
    int m = M;
    int n = N;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) A[M][N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) x[N];
    DATA_TYPE __attribute__((annotate("scalar(range(-4096, 4096) final error(1e-100))"))) y[N];
    DATA_TYPE __attribute__((annotate("scalar(range(-4096, 4096) final error(1e-100))"))) tmp[M];

    int i __attribute__((annotate("scalar(range(0, 410) final)")));
    int j __attribute__((annotate("scalar(range(0, 410) final)")));
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) fn;
    fn = (DATA_TYPE)n;

    for (i = 0; i < n; i++)
        x[i] = 1 + (i / fn);
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            A[i][j] = (DATA_TYPE) ((i+j) % n) / (5*m);

    for (i = 0; i < _PB_N; i++)
        y[i] = 0;
    for (i = 0; i < _PB_M; i++)
    {
        tmp[i] = SCALAR_VAL(0.0);
        for (j = 0; j < _PB_N; j++)
            tmp[i] = tmp[i] + A[i][j] * x[j];
        for (j = 0; j < _PB_N; j++)
            y[j] = y[j] + A[i][j] * tmp[i];
    }

    for (i = 0; i < n; i++) {
        if (i % 20 == 0) fprintf (POLYBENCH_DUMP_TARGET, "\n");
        fprintf (POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, y[i]);
    }

    return 0;
}