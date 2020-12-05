#Time Arit Math
These benchmarks compute the correct model parameters that are used by the model solver as reference for the precision-speed tradeoff.

##Compilation and run
The current configuration of the benchmark is suitable to benchmark "powerful" architectures, such as personal computer.

Just run the `make` command and wait for the compilation and run of the benchmark.

A the end, a file called `dummyModel.csv`, containing the correct values for the model, will be produced.

##Configuration
It is possible to configure the benchmark in two ways:

###Makefile
At the beginning of the `Makefile` there are two configuration line:

```
C99 	= clang
CFLAGS	= -g -O0 -DNOFLT80 -DNOFLT128 -DNBRUN=128 -DMEMSIZE=10000000 #-DNOMEMALIGN
```
The first line configures the compiler used to build the benchmarks. The current selected compiler is set to `clang` as 
it is the one used by the framework.

The second line configures the flags of the C compiler:
* `-O0` the optimization, should always be set to 0 to reduce the optimization of the compiler and enhance the fidelity of the results.
* `-DNOFLT80` removes the support to 80 bits floating point, that are not used by the model, currently
* `-DNOFLT128` same as above
* `-DNBRUN=128` controls the number of run of the same test
* `-DMEMSIZE=10000000` controls the memory used by each single test. 
  Should be greater than the cache size to minimize the effects of them on the benchmark score.

##C source code
The same constants are also defined inside the `time_arit.c` if the compiler does not provide them through the command line.
The constants have the same effects.

#Non posix / embedded systems
The benchmark make use of standard libraries calls both for the time keeping and for writing the benchmarks intermediate 
and final results respectively to stdout.
Usually the printf functions is present in most embedded systems OS. Hence for the output part no action is needed.

For the time keeping part, both the posix timing and the libc clock are supported.
Please see lines 139 of timing.c to implement the correct calls for your operating system, in case neither of these libraries are not available.
