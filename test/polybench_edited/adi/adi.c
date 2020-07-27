#include <stdio.h>
#include <stdlib.h>
#include "../instrument.h"
#define DATA_TYPE double
#  define DATA_TYPE double
#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x,y) pow(x,y)
#   define TSTEPS 100
#   define N 200

#   define _PB_TSTEPS TSTEPS
#   define _PB_N N

DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) DX, DY, DT;
DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) B1, B2;
DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) mul1, mul2;
DATA_TYPE __attribute__((annotate("scalar(error(1e-100))"))) a, b, c, d, e, f;


int main(int argc, char** argv)
{
    TIMING_CPUCLOCK_START();
    /* Retrieve problem size. */
    int n = N;
    int tsteps = TSTEPS;

    DATA_TYPE __attribute__((annotate("scalar(range(-4,4) final error(1e-100))")))u[N][N];
    DATA_TYPE __attribute__((annotate("scalar(range(-2,2) final error(1e-100))")))v[N][N];
    DATA_TYPE __attribute__((annotate("scalar(range(-1,1) final error(1e-100))")))p[N][N];
    DATA_TYPE __attribute__((annotate("scalar(range(-500,500) final error(1e-100))")))q[N][N];




    int i __attribute__((annotate("scalar(range(0, 400) final)")));
    int j __attribute__((annotate("scalar(range(0, 400) final)")));

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
        {
            u[i][j] =  (DATA_TYPE)(i + n-j) / n;
        }



    int t;



    DX = (1.0)/_PB_N;
    DY = (1.0)/_PB_N;
    DT = (1.0)/_PB_TSTEPS;
    B1 = (2.0);
    B2 = (1.0);
    mul1 = B1 * DT / (DX * DX);
    mul2 = B2 * DT / (DY * DY);

    a = -mul1 /  SCALAR_VAL(2.0);
    b = SCALAR_VAL(1.0)+mul1;
    c = a;
    d = -mul2 / SCALAR_VAL(2.0);
    e = SCALAR_VAL(1.0)+mul2;
    f = d;


    for (t=1; t<=_PB_TSTEPS; t++) {
        //Column Sweep
        for (i=1; i<_PB_N-1; i++) {

            v[0][i] = SCALAR_VAL(1.0);
            p[i][0] = SCALAR_VAL(0.0);
            q[i][0] = v[0][i];

            for (j=1; j<_PB_N-1; j++) {

                p[i][j] = -c / (a*p[i][j-1]+b); //FIXME: here is the error

                q[i][j] = (-d*u[j][i-1]+(SCALAR_VAL(1.0)+SCALAR_VAL(2.0)*d)*u[j][i] - f*u[j][i+1]-a*q[i][j-1]);

                q[i][j] /= (a*p[i][j-1]+b);

            }


            v[_PB_N-1][i] = SCALAR_VAL(1.0);

            for (j=_PB_N-2; j>=1; j--) {
                v[j][i] = p[i][j] * v[j+1][i] + q[i][j];
            }

        }

        //Row Sweep
        for (i=1; i<_PB_N-1; i++) {
            u[i][0] = SCALAR_VAL(1.0);
            p[i][0] = SCALAR_VAL(0.0);
            q[i][0] = u[i][0];
            for (j=1; j<_PB_N-1; j++) {
                p[i][j] = -f / (d*p[i][j-1]+e); //FIXME: here is the error
                q[i][j] = (-a*v[i-1][j]+(SCALAR_VAL(1.0)+SCALAR_VAL(2.0)*a)*v[i][j] - c*v[i+1][j]-d*q[i][j-1]);
                q[i][j] /= (d*p[i][j-1]+e);
            }
            u[i][_PB_N-1] = SCALAR_VAL(1.0);
            for (j=_PB_N-2; j>=1; j--) {
                u[i][j] = p[i][j] * u[i][j+1] + q[i][j];
            }
        }

    }

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++) {
            if ((i * n + j) % 20 == 0) fprintf(stdout, "\n");
            fprintf (stdout, DATA_PRINTF_MODIFIER, u[i][j]);
        }


    TIMING_CPUCLOCK_TOGGLE();
    TIMING_CPUCLOCK_PRINT();
    return 0;
}