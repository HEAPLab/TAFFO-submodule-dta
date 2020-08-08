; ModuleID = 'polybench_edited/corr/corr.c'
source_filename = "polybench_edited/corr/corr.c"
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
@.str.1 = private unnamed_addr constant [29 x i8] c"scalar(range(0, 240) final )\00", section "llvm.metadata"
@.str.2 = private unnamed_addr constant [29 x i8] c"polybench_edited/corr/corr.c\00", section "llvm.metadata"
@.str.3 = private unnamed_addr constant [29 x i8] c"scalar(range(0, 260) final )\00", section "llvm.metadata"
@.str.4 = private unnamed_addr constant [37 x i8] c"scalar(range(1, 3000) error(1e-100))\00", section "llvm.metadata"
@data = common dso_local global [260 x [240 x double]] zeroinitializer, align 16
@.str.5 = private unnamed_addr constant [9 x i8] c"scalar()\00", section "llvm.metadata"
@mean = common dso_local global [240 x double] zeroinitializer, align 16
@stddev = common dso_local global [240 x double] zeroinitializer, align 16
@corr = common dso_local global [240 x [240 x double]] zeroinitializer, align 16
@.str.6 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1
@.str.7 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1
@.str.8 = private unnamed_addr constant [49 x i8] c"scalar(range(-50000, 50000) final error(1e-100))\00", section "llvm.metadata"
@.str.9 = private unnamed_addr constant [43 x i8] c"scalar(range(-10, 10) error(1e-100) final)\00", section "llvm.metadata"
@.str.10 = private unnamed_addr constant [40 x i8] c"scalar(range(0, 5) error(1e-100) final)\00", section "llvm.metadata"
@.str.11 = private unnamed_addr constant [44 x i8] c"scalar(range(-4096,4096) error(1e-1) final)\00", section "llvm.metadata"
@llvm.global.annotations = appending global [4 x { i8*, i8*, i8*, i32 }] [{ i8*, i8*, i8*, i32 } { i8* bitcast ([240 x double]* @mean to i8*), i8* getelementptr inbounds ([49 x i8], [49 x i8]* @.str.8, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 33 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([260 x [240 x double]]* @data to i8*), i8* getelementptr inbounds ([43 x i8], [43 x i8]* @.str.9, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 34 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([240 x [240 x double]]* @corr to i8*), i8* getelementptr inbounds ([40 x i8], [40 x i8]* @.str.10, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 35 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([240 x double]* @stddev to i8*), i8* getelementptr inbounds ([44 x i8], [44 x i8]* @.str.11, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 36 }], section "llvm.metadata"

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
define dso_local i32 @main() #0 {
entry:
  %retval = alloca i32, align 4
  %i = alloca i32, align 4
  %j = alloca i32, align 4
  %k = alloca i32, align 4
  %float_n = alloca double, align 8
  %eps = alloca double, align 8
  store i32 0, i32* %retval, align 4
  call void @TAFFO_DUMPCONFIG()
  call void @TIMING_CPUCLOCK_START()
  %i1 = bitcast i32* %i to i8*
  call void @llvm.var.annotation(i8* %i1, i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.1, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 48)
  %j2 = bitcast i32* %j to i8*
  call void @llvm.var.annotation(i8* %j2, i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.3, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 49)
  %k3 = bitcast i32* %k to i8*
  call void @llvm.var.annotation(i8* %k3, i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.3, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 50)
  %float_n4 = bitcast double* %float_n to i8*
  call void @llvm.var.annotation(i8* %float_n4, i8* getelementptr inbounds ([37 x i8], [37 x i8]* @.str.4, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 53)
  store double 2.600000e+02, double* %float_n, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc12, %entry
  %0 = load i32, i32* %i, align 4
  %cmp = icmp slt i32 %0, 260
  br i1 %cmp, label %for.body, label %for.end14

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %j, align 4
  br label %for.cond5

for.cond5:                                        ; preds = %for.inc, %for.body
  %1 = load i32, i32* %j, align 4
  %cmp6 = icmp slt i32 %1, 240
  br i1 %cmp6, label %for.body7, label %for.end

for.body7:                                        ; preds = %for.cond5
  %2 = load i32, i32* %i, align 4
  %3 = load i32, i32* %j, align 4
  %mul = mul nsw i32 %2, %3
  %conv = sitofp i32 %mul to double
  %div = fdiv double %conv, 2.400000e+02
  %4 = load i32, i32* %i, align 4
  %conv8 = sitofp i32 %4 to double
  %add = fadd double %div, %conv8
  %div9 = fdiv double %add, 2.600000e+02
  %5 = load i32, i32* %i, align 4
  %idxprom = sext i32 %5 to i64
  %arrayidx = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom
  %6 = load i32, i32* %j, align 4
  %idxprom10 = sext i32 %6 to i64
  %arrayidx11 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx, i64 0, i64 %idxprom10
  store double %div9, double* %arrayidx11, align 8
  br label %for.inc

for.inc:                                          ; preds = %for.body7
  %7 = load i32, i32* %j, align 4
  %inc = add nsw i32 %7, 1
  store i32 %inc, i32* %j, align 4
  br label %for.cond5

for.end:                                          ; preds = %for.cond5
  br label %for.inc12

for.inc12:                                        ; preds = %for.end
  %8 = load i32, i32* %i, align 4
  %inc13 = add nsw i32 %8, 1
  store i32 %inc13, i32* %i, align 4
  br label %for.cond

for.end14:                                        ; preds = %for.cond
  %eps15 = bitcast double* %eps to i8*
  call void @llvm.var.annotation(i8* %eps15, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.5, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 75)
  store double 1.000000e-01, double* %eps, align 8
  store i32 0, i32* %j, align 4
  br label %for.cond16

for.cond16:                                       ; preds = %for.inc39, %for.end14
  %9 = load i32, i32* %j, align 4
  %cmp17 = icmp slt i32 %9, 240
  br i1 %cmp17, label %for.body19, label %for.end41

for.body19:                                       ; preds = %for.cond16
  %10 = load i32, i32* %j, align 4
  %idxprom20 = sext i32 %10 to i64
  %arrayidx21 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom20
  store double 0.000000e+00, double* %arrayidx21, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond22

for.cond22:                                       ; preds = %for.inc33, %for.body19
  %11 = load i32, i32* %i, align 4
  %cmp23 = icmp slt i32 %11, 260
  br i1 %cmp23, label %for.body25, label %for.end35

for.body25:                                       ; preds = %for.cond22
  %12 = load i32, i32* %i, align 4
  %idxprom26 = sext i32 %12 to i64
  %arrayidx27 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom26
  %13 = load i32, i32* %j, align 4
  %idxprom28 = sext i32 %13 to i64
  %arrayidx29 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx27, i64 0, i64 %idxprom28
  %14 = load double, double* %arrayidx29, align 8
  %15 = load i32, i32* %j, align 4
  %idxprom30 = sext i32 %15 to i64
  %arrayidx31 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom30
  %16 = load double, double* %arrayidx31, align 8
  %add32 = fadd double %16, %14
  store double %add32, double* %arrayidx31, align 8
  br label %for.inc33

for.inc33:                                        ; preds = %for.body25
  %17 = load i32, i32* %i, align 4
  %inc34 = add nsw i32 %17, 1
  store i32 %inc34, i32* %i, align 4
  br label %for.cond22

for.end35:                                        ; preds = %for.cond22
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
  br label %for.cond16

for.end41:                                        ; preds = %for.cond16
  store i32 0, i32* %j, align 4
  br label %for.cond42

for.cond42:                                       ; preds = %for.inc87, %for.end41
  %22 = load i32, i32* %j, align 4
  %cmp43 = icmp slt i32 %22, 240
  br i1 %cmp43, label %for.body45, label %for.end89

for.body45:                                       ; preds = %for.cond42
  %23 = load i32, i32* %j, align 4
  %idxprom46 = sext i32 %23 to i64
  %arrayidx47 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom46
  store double 0.000000e+00, double* %arrayidx47, align 8
  store i32 0, i32* %i, align 4
  br label %for.cond48

for.cond48:                                       ; preds = %for.inc69, %for.body45
  %24 = load i32, i32* %i, align 4
  %cmp49 = icmp slt i32 %24, 260
  br i1 %cmp49, label %for.body51, label %for.end71

for.body51:                                       ; preds = %for.cond48
  %25 = load i32, i32* %i, align 4
  %idxprom52 = sext i32 %25 to i64
  %arrayidx53 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom52
  %26 = load i32, i32* %j, align 4
  %idxprom54 = sext i32 %26 to i64
  %arrayidx55 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx53, i64 0, i64 %idxprom54
  %27 = load double, double* %arrayidx55, align 8
  %28 = load i32, i32* %j, align 4
  %idxprom56 = sext i32 %28 to i64
  %arrayidx57 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom56
  %29 = load double, double* %arrayidx57, align 8
  %sub = fsub double %27, %29
  %30 = load i32, i32* %i, align 4
  %idxprom58 = sext i32 %30 to i64
  %arrayidx59 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom58
  %31 = load i32, i32* %j, align 4
  %idxprom60 = sext i32 %31 to i64
  %arrayidx61 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx59, i64 0, i64 %idxprom60
  %32 = load double, double* %arrayidx61, align 8
  %33 = load i32, i32* %j, align 4
  %idxprom62 = sext i32 %33 to i64
  %arrayidx63 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom62
  %34 = load double, double* %arrayidx63, align 8
  %sub64 = fsub double %32, %34
  %mul65 = fmul double %sub, %sub64
  %35 = load i32, i32* %j, align 4
  %idxprom66 = sext i32 %35 to i64
  %arrayidx67 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom66
  %36 = load double, double* %arrayidx67, align 8
  %add68 = fadd double %36, %mul65
  store double %add68, double* %arrayidx67, align 8
  br label %for.inc69

for.inc69:                                        ; preds = %for.body51
  %37 = load i32, i32* %i, align 4
  %inc70 = add nsw i32 %37, 1
  store i32 %inc70, i32* %i, align 4
  br label %for.cond48

for.end71:                                        ; preds = %for.cond48
  %38 = load double, double* %float_n, align 8
  %39 = load i32, i32* %j, align 4
  %idxprom72 = sext i32 %39 to i64
  %arrayidx73 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom72
  %40 = load double, double* %arrayidx73, align 8
  %div74 = fdiv double %40, %38
  store double %div74, double* %arrayidx73, align 8
  %41 = load i32, i32* %j, align 4
  %idxprom75 = sext i32 %41 to i64
  %arrayidx76 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom75
  %42 = load double, double* %arrayidx76, align 8
  %call = call double @sqrt(double %42) #3
  %43 = load i32, i32* %j, align 4
  %idxprom77 = sext i32 %43 to i64
  %arrayidx78 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom77
  store double %call, double* %arrayidx78, align 8
  %44 = load i32, i32* %j, align 4
  %idxprom79 = sext i32 %44 to i64
  %arrayidx80 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom79
  %45 = load double, double* %arrayidx80, align 8
  %46 = load double, double* %eps, align 8
  %cmp81 = fcmp ole double %45, %46
  br i1 %cmp81, label %cond.true, label %cond.false

cond.true:                                        ; preds = %for.end71
  br label %cond.end

cond.false:                                       ; preds = %for.end71
  %47 = load i32, i32* %j, align 4
  %idxprom83 = sext i32 %47 to i64
  %arrayidx84 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom83
  %48 = load double, double* %arrayidx84, align 8
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond = phi double [ 1.000000e+00, %cond.true ], [ %48, %cond.false ]
  %49 = load i32, i32* %j, align 4
  %idxprom85 = sext i32 %49 to i64
  %arrayidx86 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom85
  store double %cond, double* %arrayidx86, align 8
  br label %for.inc87

for.inc87:                                        ; preds = %cond.end
  %50 = load i32, i32* %j, align 4
  %inc88 = add nsw i32 %50, 1
  store i32 %inc88, i32* %j, align 4
  br label %for.cond42

for.end89:                                        ; preds = %for.cond42
  store i32 0, i32* %i, align 4
  br label %for.cond90

for.cond90:                                       ; preds = %for.inc117, %for.end89
  %51 = load i32, i32* %i, align 4
  %cmp91 = icmp slt i32 %51, 260
  br i1 %cmp91, label %for.body93, label %for.end119

for.body93:                                       ; preds = %for.cond90
  store i32 0, i32* %j, align 4
  br label %for.cond94

for.cond94:                                       ; preds = %for.inc114, %for.body93
  %52 = load i32, i32* %j, align 4
  %cmp95 = icmp slt i32 %52, 240
  br i1 %cmp95, label %for.body97, label %for.end116

for.body97:                                       ; preds = %for.cond94
  %53 = load i32, i32* %j, align 4
  %idxprom98 = sext i32 %53 to i64
  %arrayidx99 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom98
  %54 = load double, double* %arrayidx99, align 8
  %55 = load i32, i32* %i, align 4
  %idxprom100 = sext i32 %55 to i64
  %arrayidx101 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom100
  %56 = load i32, i32* %j, align 4
  %idxprom102 = sext i32 %56 to i64
  %arrayidx103 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx101, i64 0, i64 %idxprom102
  %57 = load double, double* %arrayidx103, align 8
  %sub104 = fsub double %57, %54
  store double %sub104, double* %arrayidx103, align 8
  %58 = load double, double* %float_n, align 8
  %call105 = call double @sqrt(double %58) #3
  %59 = load i32, i32* %j, align 4
  %idxprom106 = sext i32 %59 to i64
  %arrayidx107 = getelementptr inbounds [240 x double], [240 x double]* @stddev, i64 0, i64 %idxprom106
  %60 = load double, double* %arrayidx107, align 8
  %mul108 = fmul double %call105, %60
  %61 = load i32, i32* %i, align 4
  %idxprom109 = sext i32 %61 to i64
  %arrayidx110 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom109
  %62 = load i32, i32* %j, align 4
  %idxprom111 = sext i32 %62 to i64
  %arrayidx112 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx110, i64 0, i64 %idxprom111
  %63 = load double, double* %arrayidx112, align 8
  %div113 = fdiv double %63, %mul108
  store double %div113, double* %arrayidx112, align 8
  br label %for.inc114

for.inc114:                                       ; preds = %for.body97
  %64 = load i32, i32* %j, align 4
  %inc115 = add nsw i32 %64, 1
  store i32 %inc115, i32* %j, align 4
  br label %for.cond94

for.end116:                                       ; preds = %for.cond94
  br label %for.inc117

for.inc117:                                       ; preds = %for.end116
  %65 = load i32, i32* %i, align 4
  %inc118 = add nsw i32 %65, 1
  store i32 %inc118, i32* %i, align 4
  br label %for.cond90

for.end119:                                       ; preds = %for.cond90
  store i32 0, i32* %i, align 4
  br label %for.cond120

for.cond120:                                      ; preds = %for.inc169, %for.end119
  %66 = load i32, i32* %i, align 4
  %cmp121 = icmp slt i32 %66, 239
  br i1 %cmp121, label %for.body123, label %for.end171

for.body123:                                      ; preds = %for.cond120
  %67 = load i32, i32* %i, align 4
  %idxprom124 = sext i32 %67 to i64
  %arrayidx125 = getelementptr inbounds [240 x [240 x double]], [240 x [240 x double]]* @corr, i64 0, i64 %idxprom124
  %68 = load i32, i32* %i, align 4
  %idxprom126 = sext i32 %68 to i64
  %arrayidx127 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx125, i64 0, i64 %idxprom126
  store double 1.000000e+00, double* %arrayidx127, align 8
  %69 = load i32, i32* %i, align 4
  %add128 = add nsw i32 %69, 1
  store i32 %add128, i32* %j, align 4
  br label %for.cond129

for.cond129:                                      ; preds = %for.inc166, %for.body123
  %70 = load i32, i32* %j, align 4
  %cmp130 = icmp slt i32 %70, 240
  br i1 %cmp130, label %for.body132, label %for.end168

for.body132:                                      ; preds = %for.cond129
  %71 = load i32, i32* %i, align 4
  %idxprom133 = sext i32 %71 to i64
  %arrayidx134 = getelementptr inbounds [240 x [240 x double]], [240 x [240 x double]]* @corr, i64 0, i64 %idxprom133
  %72 = load i32, i32* %j, align 4
  %idxprom135 = sext i32 %72 to i64
  %arrayidx136 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx134, i64 0, i64 %idxprom135
  store double 0.000000e+00, double* %arrayidx136, align 8
  store i32 0, i32* %k, align 4
  br label %for.cond137

for.cond137:                                      ; preds = %for.inc155, %for.body132
  %73 = load i32, i32* %k, align 4
  %cmp138 = icmp slt i32 %73, 260
  br i1 %cmp138, label %for.body140, label %for.end157

for.body140:                                      ; preds = %for.cond137
  %74 = load i32, i32* %k, align 4
  %idxprom141 = sext i32 %74 to i64
  %arrayidx142 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom141
  %75 = load i32, i32* %i, align 4
  %idxprom143 = sext i32 %75 to i64
  %arrayidx144 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx142, i64 0, i64 %idxprom143
  %76 = load double, double* %arrayidx144, align 8
  %77 = load i32, i32* %k, align 4
  %idxprom145 = sext i32 %77 to i64
  %arrayidx146 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom145
  %78 = load i32, i32* %j, align 4
  %idxprom147 = sext i32 %78 to i64
  %arrayidx148 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx146, i64 0, i64 %idxprom147
  %79 = load double, double* %arrayidx148, align 8
  %mul149 = fmul double %76, %79
  %80 = load i32, i32* %i, align 4
  %idxprom150 = sext i32 %80 to i64
  %arrayidx151 = getelementptr inbounds [240 x [240 x double]], [240 x [240 x double]]* @corr, i64 0, i64 %idxprom150
  %81 = load i32, i32* %j, align 4
  %idxprom152 = sext i32 %81 to i64
  %arrayidx153 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx151, i64 0, i64 %idxprom152
  %82 = load double, double* %arrayidx153, align 8
  %add154 = fadd double %82, %mul149
  store double %add154, double* %arrayidx153, align 8
  br label %for.inc155

for.inc155:                                       ; preds = %for.body140
  %83 = load i32, i32* %k, align 4
  %inc156 = add nsw i32 %83, 1
  store i32 %inc156, i32* %k, align 4
  br label %for.cond137

for.end157:                                       ; preds = %for.cond137
  %84 = load i32, i32* %i, align 4
  %idxprom158 = sext i32 %84 to i64
  %arrayidx159 = getelementptr inbounds [240 x [240 x double]], [240 x [240 x double]]* @corr, i64 0, i64 %idxprom158
  %85 = load i32, i32* %j, align 4
  %idxprom160 = sext i32 %85 to i64
  %arrayidx161 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx159, i64 0, i64 %idxprom160
  %86 = load double, double* %arrayidx161, align 8
  %87 = load i32, i32* %j, align 4
  %idxprom162 = sext i32 %87 to i64
  %arrayidx163 = getelementptr inbounds [240 x [240 x double]], [240 x [240 x double]]* @corr, i64 0, i64 %idxprom162
  %88 = load i32, i32* %i, align 4
  %idxprom164 = sext i32 %88 to i64
  %arrayidx165 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx163, i64 0, i64 %idxprom164
  store double %86, double* %arrayidx165, align 8
  br label %for.inc166

for.inc166:                                       ; preds = %for.end157
  %89 = load i32, i32* %j, align 4
  %inc167 = add nsw i32 %89, 1
  store i32 %inc167, i32* %j, align 4
  br label %for.cond129

for.end168:                                       ; preds = %for.cond129
  br label %for.inc169

for.inc169:                                       ; preds = %for.end168
  %90 = load i32, i32* %i, align 4
  %inc170 = add nsw i32 %90, 1
  store i32 %inc170, i32* %i, align 4
  br label %for.cond120

for.end171:                                       ; preds = %for.cond120
  store double 1.000000e+00, double* getelementptr inbounds ([240 x [240 x double]], [240 x [240 x double]]* @corr, i64 0, i64 239, i64 239), align 8
  call void @TIMING_CPUCLOCK_TOGGLE()
  call void @TIMING_CPUCLOCK_PRINT()
  store i32 0, i32* %i, align 4
  br label %for.cond172

for.cond172:                                      ; preds = %for.inc189, %for.end171
  %91 = load i32, i32* %i, align 4
  %cmp173 = icmp slt i32 %91, 240
  br i1 %cmp173, label %for.body175, label %for.end191

for.body175:                                      ; preds = %for.cond172
  store i32 0, i32* %j, align 4
  br label %for.cond176

for.cond176:                                      ; preds = %for.inc185, %for.body175
  %92 = load i32, i32* %j, align 4
  %cmp177 = icmp slt i32 %92, 240
  br i1 %cmp177, label %for.body179, label %for.end187

for.body179:                                      ; preds = %for.cond176
  %93 = load i32, i32* %i, align 4
  %idxprom180 = sext i32 %93 to i64
  %arrayidx181 = getelementptr inbounds [240 x [240 x double]], [240 x [240 x double]]* @corr, i64 0, i64 %idxprom180
  %94 = load i32, i32* %j, align 4
  %idxprom182 = sext i32 %94 to i64
  %arrayidx183 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx181, i64 0, i64 %idxprom182
  %95 = load double, double* %arrayidx183, align 8
  %call184 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.6, i32 0, i32 0), double %95)
  br label %for.inc185

for.inc185:                                       ; preds = %for.body179
  %96 = load i32, i32* %j, align 4
  %inc186 = add nsw i32 %96, 1
  store i32 %inc186, i32* %j, align 4
  br label %for.cond176

for.end187:                                       ; preds = %for.cond176
  %call188 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.7, i32 0, i32 0))
  br label %for.inc189

for.inc189:                                       ; preds = %for.end187
  %97 = load i32, i32* %i, align 4
  %inc190 = add nsw i32 %97, 1
  store i32 %inc190, i32* %i, align 4
  br label %for.cond172

for.end191:                                       ; preds = %for.cond172
  ret i32 0
}

; Function Attrs: nounwind
declare void @llvm.var.annotation(i8*, i8*, i8*, i32) #3

; Function Attrs: nounwind
declare dso_local double @sqrt(double) #1

declare dso_local i32 @printf(i8*, ...) #2

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
