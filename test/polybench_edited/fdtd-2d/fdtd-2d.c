#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define DATA_TYPE double

#  define DATA_PRINTF_MODIFIER "%0.16lf "
#  define SCALAR_VAL(x) x
#  define SQRT_FUN(x) sqrt(x)
#  define EXP_FUN(x) exp(x)
#  define POW_FUN(x,y) pow(x,y)

#   define TMAX 20
#   define NX 20
#   define NY 30

#   define _PB_TMAX TMAX
#   define _PB_NX NX
#   define _PB_NY NY

#define POLYBENCH_DUMP_TARGET stdout

int main(){
    /* Retrieve problem size. */
    int tmax = TMAX;
    int nx = NX;
    int ny = NY;

    /* Variable declaration/allocation. */
    DATA_TYPE __attribute__((annotate("scalar()"))) ex[NX][NY];
    DATA_TYPE __attribute__((annotate("scalar()"))) ey[NX][NY];
    DATA_TYPE __attribute__((annotate("scalar()"))) hz[NX][NY];
    DATA_TYPE __attribute__((annotate("scalar()"))) _fict_[TMAX];

    int i __attribute__((annotate("scalar(range(0, 20))")));
    int j __attribute__((annotate("scalar(range(0, 30))")));
    int t;

    for (i = 0; i < tmax; i++)
        _fict_[i] = (DATA_TYPE) i;
    for (i = 0; i < nx; i++)
        for (j = 0; j < ny; j++)
        {
            ex[i][j] = ((DATA_TYPE) i*(j+1)) / nx;
            ey[i][j] = ((DATA_TYPE) i*(j+2)) / ny;
            hz[i][j] = ((DATA_TYPE) i*(j+3)) / nx;
        }

    for(t = 0; t < _PB_TMAX; t++)
    {
        for (j = 0; j < _PB_NY; j++)
            ey[0][j] = _fict_[t];
        for (i = 1; i < _PB_NX; i++)
            for (j = 0; j < _PB_NY; j++)
                ey[i][j] = ey[i][j] - SCALAR_VAL(0.5)*(hz[i][j]-hz[i-1][j]);
        for (i = 0; i < _PB_NX; i++)
            for (j = 1; j < _PB_NY; j++)
                ex[i][j] = ex[i][j] - SCALAR_VAL(0.5)*(hz[i][j]-hz[i][j-1]);
        for (i = 0; i < _PB_NX - 1; i++)
            for (j = 0; j < _PB_NY - 1; j++)
                hz[i][j] = hz[i][j] - SCALAR_VAL(0.7)*  (ex[i][j+1] - ex[i][j] +
                                                         ey[i+1][j] - ey[i][j]);
    }


    for (i = 0; i < nx; i++)
        for (j = 0; j < ny; j++) {
            if ((i * nx + j) % 20 == 0) fprintf(POLYBENCH_DUMP_TARGET, "\n");
            fprintf(POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, ex[i][j]);
        }

    for (i = 0; i < nx; i++)
        for (j = 0; j < ny; j++) {
            if ((i * nx + j) % 20 == 0) fprintf(POLYBENCH_DUMP_TARGET, "\n");
            fprintf(POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, ey[i][j]);
        }

    for (i = 0; i < nx; i++)
        for (j = 0; j < ny; j++) {
            if ((i * nx + j) % 20 == 0) fprintf(POLYBENCH_DUMP_TARGET, "\n");
            fprintf(POLYBENCH_DUMP_TARGET, DATA_PRINTF_MODIFIER, hz[i][j]);
        }
}