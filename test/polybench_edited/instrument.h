#include <stdio.h>
#include <stdlib.h>
#ifdef _MIOSIX
#include "interfaces/arch_registers.h"
#endif

#ifndef __INSTRUMENT_H__
#define __INSTRUMENT_H__

#ifndef _MIOSIX
#include <time.h>
#endif

long unsigned time_that_takes;

long unsigned gettime(){
#ifdef _MIOSIX
    #warning Using STM32 specific instructions
    return DWT->CYCCNT;
#else
#warning On general linux architecture
    return clock();
#endif
}

void TIMING_CPUCLOCK_START(){
#ifdef _MIOSIX
    #warning Using STM32 specific instructions
    CoreDebug->DEMCR |= CoreDebug_DEMCR_TRCENA_Msk;
    DWT->CYCCNT = 0;
    DWT->CTRL |= DWT_CTRL_CYCCNTENA_Msk;
#endif
    time_that_takes = gettime();
}

void TIMING_CPUCLOCK_TOGGLE(){
    time_that_takes = gettime() - time_that_takes;
}


long unsigned TIMING_CPUCLOCK_S(){
    return time_that_takes;
}

void TIMING_CPUCLOCK_PRINT(){
#ifdef _MIOSIX
    printf("\n___TAFFOTIME___ %ld ___TAFFOTIME___\n", time_that_takes);
#else
    fprintf(stderr, "%ld", time_that_takes);
#endif
}


void TAFFO_DUMPCONFIG(){
#ifdef _MIOSIX
    printf("{");
    printf("__TAFFO_mixedtuningenob_" __TAFFO_MIXEDTUNINGENOB_ "__TAFFO_mixedtuningenob_\n");
    printf("__TAFFO_mixedtuningtime_" __TAFFO_MIXEDTUNINGTIME_ "__TAFFO_mixedtuningtime_\n");
    printf("__TAFFO_mixedtuningcastingtime_" __TAFFO_MIXEDTUNINGCASTTIME_ "__TAFFO_mixedtuningcastingtime_\n");
    printf("__TAFFO_mixeddoubleenabled_" __TAFFO_MIXEDDOUBLEENABLED_ "__TAFFO_mixeddoubleenabled_\n");
    printf("__TAFFO_presetname_" __TAFFO_PRESETNAME_ "__TAFFO_presetname_\n");
    printf("}\n");
#endif
}




#endif
