#include <stdio.h>
#include <stdlib.h>
#include <math.h>



#define N 28
#define M 32
#define DATA_TYPE double
int main(){
    DATA_TYPE __attribute((annotate("scalar(range(-50000, 50000) final error(1e-100))"))) mean[M];
    DATA_TYPE __attribute((annotate("scalar(range(-10, 10) error(1e-100) final)"))) data[N][M];
    DATA_TYPE __attribute((annotate("scalar(range(0, 5) error(1e-100) final)"))) corr[M][M];
    DATA_TYPE __attribute((annotate("scalar(range(-4096,4096) error(1e-100) final)"))) stddev[M];



    int __attribute((annotate("scalar(range(0, 28) final disabled)"))) i;
    int __attribute((annotate("scalar(range(0, 32) final disabled)"))) j;
    int __attribute((annotate("scalar(range(0, 32) final disabled)"))) k;


    DATA_TYPE __attribute((annotate("scalar(range(1, 3000) error(1e-100))"))) float_n;
    float_n = (DATA_TYPE)N;

    for (i = 0; i < N; i++)
        for (j = 0; j < M; j++)
            data[i][j] = ((DATA_TYPE)(i*j)/M + i)/N;

    //Print
    /*double min = data[0][0];
    double max = data[0][0];
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            if(data[i][j] > max) max = data[i][j];
            if(data[i][j] < min) min = data[i][j];
        }
    }
    printf("min: %f, max: %f\n", min, max);*/



    ///KERNEL
    DATA_TYPE __attribute((annotate("scalar()"))) eps = (0.1);
    for (j = 0; j < M; j++)
    {
        mean[j] = (0.0);
        for (i = 0; i < N; i++)
            mean[j] += data[i][j];
        mean[j] /= float_n;
    }


    for (j = 0; j < M; j++)
    {
        stddev[j] = (0.0);
        for (i = 0; i < N; i++)
            stddev[j] += (data[i][j] - mean[j]) * (data[i][j] - mean[j]);
        stddev[j] /= float_n;
        stddev[j] = sqrt(stddev[j]);
        /* The following in an inelegant but usual way to handle
           near-zero std. dev. values, which below would cause a zero-
           divide. */
        stddev[j] = stddev[j] <= eps ? (1.0) : stddev[j];
    }

    /* Center and reduce the column vectors. */
    for (i = 0; i < N; i++)
        for (j = 0; j < M; j++)
        {
            data[i][j] -= mean[j];
            data[i][j] /= sqrt(float_n) * stddev[j];
        }

    /*//Print
    min = data[0][0];
    max = data[0][0];
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            if(data[i][j] > max) max = data[i][j];
            if(data[i][j] < min) min = data[i][j];
        }
    }
    printf("min: %f, max: %f\n", min, max);*/

    /* Calculate the m * m correlation matrix. */
    for (i = 0; i < M-1; i++)
    {
        corr[i][i] = (1.0);
        for (j = i+1; j < M; j++)
        {
            corr[i][j] = (0.0);
            for (k = 0; k < N; k++)
                corr[i][j] += (data[k][i] * data[k][j]);
            corr[j][i] = corr[i][j];
        }
    }
    corr[M-1][M-1] = (1.0);

    /*//Print
    min = corr[0][0];
    max = corr[0][0];
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            if(corr[i][j] > max) max = corr[i][j];
            if(corr[i][j] < min) min = corr[i][j];
        }
    }
    printf("CORR min: %f, max: %f\n", min, max);*/



    //Print
    //printf("\n\nCORR:\n");
    for (i = 0; i < M; i++) {
        for (j = 0; j < M; j++) {
            printf("%.16lf ", corr[i][j]);
        }
        printf("\n");
    }

}
