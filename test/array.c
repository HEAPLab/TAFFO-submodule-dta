#include <stdio.h>
#define ELEMENTS 10
double array[ELEMENTS] __attribute((annotate("scalar(range(7, 2000))")));
double sum;
int main(){

    for(int i=0; i<ELEMENTS; i++){
        //load, process, store
        array[i] = array[i] + 1.0;
    }
    //double x = array[1] + array[2];


}