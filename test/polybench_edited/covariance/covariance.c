#include <stdio.h>
#include <stdlib.h>
#include "../instrument.h"
#define DATA_TYPE double
#   define M 80
#   define N 100

#define _PB_M M
#define _PB_N N


int main(int argc, char** argv)
{
    TIMING_CPUCLOCK_START();
    /* Retrieve problem size. */
    int n = N;
    int m = M;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute((annotate("scalar(range(-10000, 10000) final error(1e-100))"))) float_n;
    DATA_TYPE __attribute((annotate("scalar(range(-10000, 10000) final error(1e-100))"))) data[N][M];
    DATA_TYPE __attribute((annotate("scalar(range(-10000, 100000) error(1e-100))"))) cov[N][M];
    DATA_TYPE __attribute((annotate("scalar(range(-5000, 5000) final error(1e-100))"))) mean[M];


    int __attribute((annotate("scalar(range(1, 100) final)"))) i;
    int __attribute((annotate("scalar(range(1, 100) final)"))) j;
    int __attribute((annotate("scalar(range(1, 100) final)"))) k;

    float_n = (DATA_TYPE)n;

    for (i = 0; i < N; i++)
        for (j = 0; j < M; j++)
            data[i][j] = ((DATA_TYPE) i*j) / M;






    for (j = 0; j < _PB_M; j++)
    {
        mean[j] = 0.0;
        for (i = 0; i < _PB_N; i++)
            mean[j] += data[i][j];
        mean[j] /= float_n;
    }



    for (i = 0; i < _PB_N; i++)
        for (j = 0; j < _PB_M; j++)
            data[i][j] -= mean[j];





    for (i = 0; i < _PB_M; i++)
        for (j = i; j < _PB_M; j++)
        {
            cov[i][j] = 0.0;
            for (k = 0; k < _PB_N; k++) {
                cov[i][j] += data[k][i] * data[k][j];
            }
            //cov[i][j] /= (float_n - 1.0);
            cov[i][j] /= (N - 1.0);
            cov[j][i] = cov[i][j];
        }





    for (i = 0; i < m; i++)
        for (j = 0; j < m; j++) {
            if ((i * m + j) % 20 == 0) fprintf (stdout, "\n");
            fprintf (stdout, "%.16lf ", cov[i][j]);
        }

    TIMING_CPUCLOCK_TOGGLE();
    TIMING_CPUCLOCK_PRINT();
    return 0;
}