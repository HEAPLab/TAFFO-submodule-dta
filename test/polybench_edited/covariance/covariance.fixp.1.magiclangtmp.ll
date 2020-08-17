; ModuleID = 'polybench_edited/covariance/covariance.c'
source_filename = "polybench_edited/covariance/covariance.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque
%struct.timespec = type { i64, i64 }

@time_that_takes = common dso_local global i64 0, align 8
@stderr = external dso_local global %struct._IO_FILE*, align 8
@.str = private unnamed_addr constant [4 x i8] c"%ld\00", align 1
@.str.1 = private unnamed_addr constant [49 x i8] c"scalar(range(-10000, 10000) final error(1e-100))\00", section "llvm.metadata"
@.str.2 = private unnamed_addr constant [41 x i8] c"polybench_edited/covariance/covariance.c\00", section "llvm.metadata"
@.str.3 = private unnamed_addr constant [28 x i8] c"scalar(range(1, 260) final)\00", section "llvm.metadata"
@data = common dso_local global [260 x [240 x double]] zeroinitializer, align 16
@mean = common dso_local global [240 x double] zeroinitializer, align 16
@cov = common dso_local global [260 x [240 x double]] zeroinitializer, align 16
@stdout = external dso_local global %struct._IO_FILE*, align 8
@.str.4 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1
@.str.5 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1
@.str.6 = private unnamed_addr constant [53 x i8] c"scalar(range(-2097152, 2097151) final error(1e-100))\00", section "llvm.metadata"
@.str.7 = private unnamed_addr constant [22 x i8] c"scalar(error(1e-100))\00", section "llvm.metadata"
@llvm.global.annotations = appending global [3 x { i8*, i8*, i8*, i32 }] [{ i8*, i8*, i8*, i32 } { i8* bitcast ([260 x [240 x double]]* @data to i8*), i8* getelementptr inbounds ([53 x i8], [53 x i8]* @.str.6, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 33 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([260 x [240 x double]]* @cov to i8*), i8* getelementptr inbounds ([53 x i8], [53 x i8]* @.str.6, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 34 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([240 x double]* @mean to i8*), i8* getelementptr inbounds ([22 x i8], [22 x i8]* @.str.7, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 35 }], section "llvm.metadata"

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i64 @gettime() #0 {
entry:
  %tmp = alloca %struct.timespec, align 8
  %call = call i32 @clock_gettime(i32 2, %struct.timespec* %tmp) #3
  %tv_sec = getelementptr inbounds %struct.timespec, %struct.timespec* %tmp, i32 0, i32 0
  %0 = load i64, i64* %tv_sec, align 8
  %mul = mul nsw i64 %0, 1000000
  %tv_nsec = getelementptr inbounds %struct.timespec, %struct.timespec* %tmp, i32 0, i32 1
  %1 = load i64, i64* %tv_nsec, align 8
  %div = sdiv i64 %1, 1000
  %add = add nsw i64 %mul, %div
  ret i64 %add
}

; Function Attrs: nounwind
declare dso_local i32 @clock_gettime(i32, %struct.timespec*) #1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @TIMING_CPUCLOCK_START() #0 {
entry:
  %call = call i64 @gettime()
  store i64 %call, i64* @time_that_takes, align 8
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @TIMING_CPUCLOCK_TOGGLE() #0 {
entry:
  %call = call i64 @gettime()
  %0 = load i64, i64* @time_that_takes, align 8
  %sub = sub i64 %call, %0
  store i64 %sub, i64* @time_that_takes, align 8
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i64 @TIMING_CPUCLOCK_S() #0 {
entry:
  %0 = load i64, i64* @time_that_takes, align 8
  ret i64 %0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @TIMING_CPUCLOCK_PRINT() #0 {
entry:
  %0 = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %1 = load i64, i64* @time_that_takes, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %0, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i64 %1)
  ret void
}

declare dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #2

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @TAFFO_DUMPCONFIG() #0 {
entry:
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main(i32 %argc, i8** %argv) #0 {
entry:
  %retval = alloca i32, align 4
  %argc.addr = alloca i32, align 4
  %argv.addr = alloca i8**, align 8
  %n = alloca i32, align 4
  %m = alloca i32, align 4
  %float_n = alloca double, align 8
  %i = alloca i32, align 4
  %j = alloca i32, align 4
  %k = alloca i32, align 4
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  call void @TAFFO_DUMPCONFIG()
  call void @TIMING_CPUCLOCK_START()
  store i32 260, i32* %n, align 4
  store i32 240, i32* %m, align 4
  %float_n1 = bitcast double* %float_n to i8*
  call void @llvm.var.annotation(i8* %float_n1, i8* getelementptr inbounds ([49 x i8], [49 x i8]* @.str.1, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 46)
  %i2 = bitcast i32* %i to i8*
  call void @llvm.var.annotation(i8* %i2, i8* getelementptr inbounds ([28 x i8], [28 x i8]* @.str.3, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 50)
  %j3 = bitcast i32* %j to i8*
  call void @llvm.var.annotation(i8* %j3, i8* getelementptr inbounds ([28 x i8], [28 x i8]* @.str.3, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 51)
  %k4 = bitcast i32* %k to i8*
  call void @llvm.var.annotation(i8* %k4, i8* getelementptr inbounds ([28 x i8], [28 x i8]* @.str.3, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 52)
  %0 = load i32, i32* %n, align 4
  %conv = sitofp i32 %0 to double
  store double %conv, double* %float_n, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc14, %entry
  %1 = load i32, i32* %i, align 4
  %cmp = icmp slt i32 %1, 260
  br i1 %cmp, label %for.body, label %for.end16

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %j, align 4
  br label %for.cond6

for.cond6:                                        ; preds = %for.inc, %for.body
  %2 = load i32, i32* %j, align 4
  %cmp7 = icmp slt i32 %2, 240
  br i1 %cmp7, label %for.body9, label %for.end

for.body9:                                        ; preds = %for.cond6
  %3 = load i32, i32* %i, align 4
  %conv10 = sitofp i32 %3 to double
  %4 = load i32, i32* %j, align 4
  %conv11 = sitofp i32 %4 to double
  %mul = fmul double %conv10, %conv11
  %div = fdiv double %mul, 2.400000e+02
  %5 = load i32, i32* %i, align 4
  %idxprom = sext i32 %5 to i64
  %arrayidx = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom
  %6 = load i32, i32* %j, align 4
  %idxprom12 = sext i32 %6 to i64
  %arrayidx13 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx, i64 0, i64 %idxprom12
  store double %div, double* %arrayidx13, align 8
  br label %for.inc

for.inc:                                          ; preds = %for.body9
  %7 = load i32, i32* %j, align 4
  %inc = add nsw i32 %7, 1
  store i32 %inc, i32* %j, align 4
  br label %for.cond6

for.end:                                          ; preds = %for.cond6
  br label %for.inc14

for.inc14:                                        ; preds = %for.end
  %8 = load i32, i32* %i, align 4
  %inc15 = add nsw i32 %8, 1
  store i32 %inc15, i32* %i, align 4
  br label %for.cond

for.end16:                                        ; preds = %for.cond
  store i32 0, i32* %j, align 4
  br label %for.cond17

for.cond17:                                       ; preds = %for.inc39, %for.end16
  %9 = load i32, i32* %j, align 4
  %cmp18 = icmp slt i32 %9, 240
  br i1 %cmp18, label %for.body20, label %for.end41

for.body20:                                       ; preds = %for.cond17
  %10 = load i32, i32* %j, align 4
  %idxprom21 = sext i32 %10 to i64
  %arrayidx22 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom21
  store double 0.000000e+00, double* %arrayidx22, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond23

for.cond23:                                       ; preds = %for.inc33, %for.body20
  %11 = load i32, i32* %i, align 4
  %cmp24 = icmp slt i32 %11, 260
  br i1 %cmp24, label %for.body26, label %for.end35

for.body26:                                       ; preds = %for.cond23
  %12 = load i32, i32* %i, align 4
  %idxprom27 = sext i32 %12 to i64
  %arrayidx28 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom27
  %13 = load i32, i32* %j, align 4
  %idxprom29 = sext i32 %13 to i64
  %arrayidx30 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx28, i64 0, i64 %idxprom29
  %14 = load double, double* %arrayidx30, align 8
  %15 = load i32, i32* %j, align 4
  %idxprom31 = sext i32 %15 to i64
  %arrayidx32 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom31
  %16 = load double, double* %arrayidx32, align 8
  %add = fadd double %16, %14
  store double %add, double* %arrayidx32, align 8
  br label %for.inc33

for.inc33:                                        ; preds = %for.body26
  %17 = load i32, i32* %i, align 4
  %inc34 = add nsw i32 %17, 1
  store i32 %inc34, i32* %i, align 4
  br label %for.cond23

for.end35:                                        ; preds = %for.cond23
  %18 = load double, double* %float_n, align 8
  %19 = load i32, i32* %j, align 4
  %idxprom36 = sext i32 %19 to i64
  %arrayidx37 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom36
  %20 = load double, double* %arrayidx37, align 8
  %div38 = fdiv double %20, %18
  store double %div38, double* %arrayidx37, align 8
  br label %for.inc39

for.inc39:                                        ; preds = %for.end35
  %21 = load i32, i32* %j, align 4
  %inc40 = add nsw i32 %21, 1
  store i32 %inc40, i32* %j, align 4
  br label %for.cond17

for.end41:                                        ; preds = %for.cond17
  store i32 0, i32* %i, align 4
  br label %for.cond42

for.cond42:                                       ; preds = %for.inc59, %for.end41
  %22 = load i32, i32* %i, align 4
  %cmp43 = icmp slt i32 %22, 260
  br i1 %cmp43, label %for.body45, label %for.end61

for.body45:                                       ; preds = %for.cond42
  store i32 0, i32* %j, align 4
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc56, %for.body45
  %23 = load i32, i32* %j, align 4
  %cmp47 = icmp slt i32 %23, 240
  br i1 %cmp47, label %for.body49, label %for.end58

for.body49:                                       ; preds = %for.cond46
  %24 = load i32, i32* %j, align 4
  %idxprom50 = sext i32 %24 to i64
  %arrayidx51 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom50
  %25 = load double, double* %arrayidx51, align 8
  %26 = load i32, i32* %i, align 4
  %idxprom52 = sext i32 %26 to i64
  %arrayidx53 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom52
  %27 = load i32, i32* %j, align 4
  %idxprom54 = sext i32 %27 to i64
  %arrayidx55 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx53, i64 0, i64 %idxprom54
  %28 = load double, double* %arrayidx55, align 8
  %sub = fsub double %28, %25
  store double %sub, double* %arrayidx55, align 8
  br label %for.inc56

for.inc56:                                        ; preds = %for.body49
  %29 = load i32, i32* %j, align 4
  %inc57 = add nsw i32 %29, 1
  store i32 %inc57, i32* %j, align 4
  br label %for.cond46

for.end58:                                        ; preds = %for.cond46
  br label %for.inc59

for.inc59:                                        ; preds = %for.end58
  %30 = load i32, i32* %i, align 4
  %inc60 = add nsw i32 %30, 1
  store i32 %inc60, i32* %i, align 4
  br label %for.cond42

for.end61:                                        ; preds = %for.cond42
  store i32 0, i32* %i, align 4
  br label %for.cond62

for.cond62:                                       ; preds = %for.inc111, %for.end61
  %31 = load i32, i32* %i, align 4
  %cmp63 = icmp slt i32 %31, 240
  br i1 %cmp63, label %for.body65, label %for.end113

for.body65:                                       ; preds = %for.cond62
  %32 = load i32, i32* %i, align 4
  store i32 %32, i32* %j, align 4
  br label %for.cond66

for.cond66:                                       ; preds = %for.inc108, %for.body65
  %33 = load i32, i32* %j, align 4
  %cmp67 = icmp slt i32 %33, 240
  br i1 %cmp67, label %for.body69, label %for.end110

for.body69:                                       ; preds = %for.cond66
  %34 = load i32, i32* %i, align 4
  %idxprom70 = sext i32 %34 to i64
  %arrayidx71 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom70
  %35 = load i32, i32* %j, align 4
  %idxprom72 = sext i32 %35 to i64
  %arrayidx73 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx71, i64 0, i64 %idxprom72
  store double 0.000000e+00, double* %arrayidx73, align 8
  store i32 0, i32* %k, align 4
  br label %for.cond74

for.cond74:                                       ; preds = %for.inc92, %for.body69
  %36 = load i32, i32* %k, align 4
  %cmp75 = icmp slt i32 %36, 260
  br i1 %cmp75, label %for.body77, label %for.end94

for.body77:                                       ; preds = %for.cond74
  %37 = load i32, i32* %k, align 4
  %idxprom78 = sext i32 %37 to i64
  %arrayidx79 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom78
  %38 = load i32, i32* %i, align 4
  %idxprom80 = sext i32 %38 to i64
  %arrayidx81 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx79, i64 0, i64 %idxprom80
  %39 = load double, double* %arrayidx81, align 8
  %40 = load i32, i32* %k, align 4
  %idxprom82 = sext i32 %40 to i64
  %arrayidx83 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom82
  %41 = load i32, i32* %j, align 4
  %idxprom84 = sext i32 %41 to i64
  %arrayidx85 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx83, i64 0, i64 %idxprom84
  %42 = load double, double* %arrayidx85, align 8
  %mul86 = fmul double %39, %42
  %43 = load i32, i32* %i, align 4
  %idxprom87 = sext i32 %43 to i64
  %arrayidx88 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom87
  %44 = load i32, i32* %j, align 4
  %idxprom89 = sext i32 %44 to i64
  %arrayidx90 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx88, i64 0, i64 %idxprom89
  %45 = load double, double* %arrayidx90, align 8
  %add91 = fadd double %45, %mul86
  store double %add91, double* %arrayidx90, align 8
  br label %for.inc92

for.inc92:                                        ; preds = %for.body77
  %46 = load i32, i32* %k, align 4
  %inc93 = add nsw i32 %46, 1
  store i32 %inc93, i32* %k, align 4
  br label %for.cond74

for.end94:                                        ; preds = %for.cond74
  %47 = load i32, i32* %i, align 4
  %idxprom95 = sext i32 %47 to i64
  %arrayidx96 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom95
  %48 = load i32, i32* %j, align 4
  %idxprom97 = sext i32 %48 to i64
  %arrayidx98 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx96, i64 0, i64 %idxprom97
  %49 = load double, double* %arrayidx98, align 8
  %div99 = fdiv double %49, 2.590000e+02
  store double %div99, double* %arrayidx98, align 8
  %50 = load i32, i32* %i, align 4
  %idxprom100 = sext i32 %50 to i64
  %arrayidx101 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom100
  %51 = load i32, i32* %j, align 4
  %idxprom102 = sext i32 %51 to i64
  %arrayidx103 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx101, i64 0, i64 %idxprom102
  %52 = load double, double* %arrayidx103, align 8
  %53 = load i32, i32* %j, align 4
  %idxprom104 = sext i32 %53 to i64
  %arrayidx105 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom104
  %54 = load i32, i32* %i, align 4
  %idxprom106 = sext i32 %54 to i64
  %arrayidx107 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx105, i64 0, i64 %idxprom106
  store double %52, double* %arrayidx107, align 8
  br label %for.inc108

for.inc108:                                       ; preds = %for.end94
  %55 = load i32, i32* %j, align 4
  %inc109 = add nsw i32 %55, 1
  store i32 %inc109, i32* %j, align 4
  br label %for.cond66

for.end110:                                       ; preds = %for.cond66
  br label %for.inc111

for.inc111:                                       ; preds = %for.end110
  %56 = load i32, i32* %i, align 4
  %inc112 = add nsw i32 %56, 1
  store i32 %inc112, i32* %i, align 4
  br label %for.cond62

for.end113:                                       ; preds = %for.cond62
  call void @TIMING_CPUCLOCK_TOGGLE()
  call void @TIMING_CPUCLOCK_PRINT()
  store i32 0, i32* %i, align 4
  br label %for.cond114

for.cond114:                                      ; preds = %for.inc134, %for.end113
  %57 = load i32, i32* %i, align 4
  %58 = load i32, i32* %m, align 4
  %cmp115 = icmp slt i32 %57, %58
  br i1 %cmp115, label %for.body117, label %for.end136

for.body117:                                      ; preds = %for.cond114
  store i32 0, i32* %j, align 4
  br label %for.cond118

for.cond118:                                      ; preds = %for.inc131, %for.body117
  %59 = load i32, i32* %j, align 4
  %60 = load i32, i32* %m, align 4
  %cmp119 = icmp slt i32 %59, %60
  br i1 %cmp119, label %for.body121, label %for.end133

for.body121:                                      ; preds = %for.cond118
  %61 = load i32, i32* %i, align 4
  %62 = load i32, i32* %m, align 4
  %mul122 = mul nsw i32 %61, %62
  %63 = load i32, i32* %j, align 4
  %add123 = add nsw i32 %mul122, %63
  %rem = srem i32 %add123, 20
  %cmp124 = icmp eq i32 %rem, 0
  br i1 %cmp124, label %if.then, label %if.end

if.then:                                          ; preds = %for.body121
  %64 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %64, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.4, i32 0, i32 0))
  br label %if.end

if.end:                                           ; preds = %if.then, %for.body121
  %65 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %66 = load i32, i32* %i, align 4
  %idxprom126 = sext i32 %66 to i64
  %arrayidx127 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom126
  %67 = load i32, i32* %j, align 4
  %idxprom128 = sext i32 %67 to i64
  %arrayidx129 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx127, i64 0, i64 %idxprom128
  %68 = load double, double* %arrayidx129, align 8
  %call130 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %65, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.5, i32 0, i32 0), double %68)
  br label %for.inc131

for.inc131:                                       ; preds = %if.end
  %69 = load i32, i32* %j, align 4
  %inc132 = add nsw i32 %69, 1
  store i32 %inc132, i32* %j, align 4
  br label %for.cond118

for.end133:                                       ; preds = %for.cond118
  br label %for.inc134

for.inc134:                                       ; preds = %for.end133
  %70 = load i32, i32* %i, align 4
  %inc135 = add nsw i32 %70, 1
  store i32 %inc135, i32* %i, align 4
  br label %for.cond114

for.end136:                                       ; preds = %for.cond114
  ret i32 0
}

; Function Attrs: nounwind
declare void @llvm.var.annotation(i8*, i8*, i8*, i32) #3

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
