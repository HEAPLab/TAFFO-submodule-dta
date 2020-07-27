#include <stdio.h>
#include <stdlib.h>

#ifndef __INSTRUMENT_H__
#define __INSTRUMENT_H__




long unsigned time_that_takes;

long unsigned gettime(){
#ifdef MIOSIX
    #warning Using STM32 specific instructions
    return DWT->CYCCNT;
#else
#warning On general linux architecture
    return clock();
#endif
}

void TIMING_CPUCLOCK_START(){
    time_that_takes = gettime();
}

void TIMING_CPUCLOCK_TOGGLE(){
    time_that_takes = gettime() - time_that_takes;
}


long unsigned TIMING_CPUCLOCK_S(){
    return time_that_takes;
}

void TIMING_CPUCLOCK_PRINT(){
    fprintf(stderr, "%ld", time_that_takes);
}







#endif
