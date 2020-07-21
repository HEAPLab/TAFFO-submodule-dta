#include <stdio.h>
#include <stdlib.h>
#include <math.h>
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
    /* Retrieve problem size. */
    int n = N;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) r[N];
    DATA_TYPE __attribute__((annotate("scalar(range(-2, 2) final error(1e-100))"))) y[N];


    int i __attribute__((annotate("scalar(range(-400, 400) final disabled)")));
    int k;

    for (i = 0; i < n; i++)
    {
        r[i] = (DATA_TYPE)(n+1-i) / (n*200.0) + 1.5;
    }



    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) z[N];
    DATA_TYPE __attribute__((annotate("scalar(range(-2, 2) final error(1e-100))"))) alpha;
    DATA_TYPE __attribute__((annotate("scalar(range(-2, 2) final error(1e-100))"))) beta;
    DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) sum;

    y[0] = -r[0];
    beta = SCALAR_VAL(1.0);
    alpha = -r[0];

    for (k = 1; k < _PB_N; k++) {
        beta = (1-alpha*alpha)*beta;
        sum = SCALAR_VAL(0.0);
        for (i=0; i<k; i++) {
            sum += r[k-i-1]*y[i];
        }
        alpha = - (r[k] + sum)/beta;

        for (i=0; i<k; i++) {
            z[i] = y[i] + alpha*y[k-i-1];
        }
        for (i=0; i<k; i++) {
            y[i] = z[i];
        }
        y[k] = alpha;
    }

    for (i = 0; i < n; i++) {
        if (i % 20 == 0) fprintf (POLYBENCH_DUMP_TARGET, "\n");
        fprintf (POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, y[i]);
    }

    return 0;
}