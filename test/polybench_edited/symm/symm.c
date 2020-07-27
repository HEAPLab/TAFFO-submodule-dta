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

#   define M 200
#   define N 240

#   define _PB_M M
#   define _PB_N N

int main(){
    TIMING_CPUCLOCK_START();
    /* Retrieve problem size. */
    int m = M;
    int n = N;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) alpha;
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) beta;
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) C[M][N];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) A[M][M];
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) B[M][N];

    int i __attribute__((annotate("scalar(range(0, 200) final)")));
    int j __attribute__((annotate("scalar(range(0, 240) final)")));

    alpha = 1.5;
    beta = 1.2;
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++) {
            C[i][j] = (DATA_TYPE) ((i+j) % 100) / m;
            B[i][j] = (DATA_TYPE) ((n+i-j) % 100) / m;
        }
    for (i = 0; i < m; i++) {
        for (j = 0; j <=i; j++)
            A[i][j] = (DATA_TYPE) ((i+j) % 100) / m;
        for (j = i+1; j < m; j++)
            A[i][j] = -999; //regions of arrays that should not be used
    }

    int k;
    DATA_TYPE temp2;

    for (i = 0; i < _PB_M; i++)
        for (j = 0; j < _PB_N; j++ )
        {
            temp2 = 0;
            for (k = 0; k < i; k++) {
                C[k][j] += alpha*B[i][j] * A[i][k];
                temp2 += B[k][j] * A[i][k];
            }
            C[i][j] = beta * C[i][j] + alpha*B[i][j] * A[i][i] + alpha * temp2;
        }

    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++) {
            if ((i * m + j) % 20 == 0) fprintf (POLYBENCH_DUMP_TARGET, "\n");
            fprintf (POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, C[i][j]);
        }
    TIMING_CPUCLOCK_TOGGLE();
    TIMING_CPUCLOCK_PRINT();
    return 0;
}