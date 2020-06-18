#include <stdio.h>
#include <stdlib.h>

double __attribute((annotate("scalar(range(0, 50000) final error(0.1))"))) mean[10];
double __attribute((annotate("scalar(range(0, 5) final)"))) data[10][10];
double __attribute((annotate("scalar(range(0, 3000))"))) float_n;


int main(){
    int i, j;
    for (j = 0; j < 10; j++)
    {
        mean[j] = 0.0;
        for (i = 0; i < 10; i++)
            mean[j] += data[i][j];
        mean[j] /= float_n;
    }
}