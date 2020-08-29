; ModuleID = 'polybench_edited/corr/corr.fixp.3.magiclangtmp.ll'
source_filename = "polybench_edited/corr/corr.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque
%struct.timespec = type { i64, i64 }

@time_that_takes = common dso_local global i64 0, align 8, !taffo.info !0
@stderr = external dso_local global %struct._IO_FILE*, align 8
@.str = private unnamed_addr constant [4 x i8] c"%ld\00", align 1, !taffo.info !2
@.str.2 = private unnamed_addr constant [29 x i8] c"polybench_edited/corr/corr.c\00", section "llvm.metadata", !taffo.info !4
@data = common dso_local global [32 x [28 x double]] zeroinitializer, align 16, !taffo.info !6, !taffo.initweight !10
@mean = common dso_local global [28 x double] zeroinitializer, align 16, !taffo.info !11, !taffo.initweight !10
@stddev = common dso_local global [28 x double] zeroinitializer, align 16, !taffo.info !14, !taffo.initweight !10
@corr = common dso_local global [28 x [28 x double]] zeroinitializer, align 16, !taffo.info !18, !taffo.initweight !10
@.str.6 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !2
@.str.7 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !21
@.str.8 = private unnamed_addr constant [49 x i8] c"scalar(range(-50000, 50000) final error(1e-100))\00", section "llvm.metadata", !taffo.info !23
@.str.9 = private unnamed_addr constant [43 x i8] c"scalar(range(-10, 10) error(1e-100) final)\00", section "llvm.metadata", !taffo.info !23
@.str.10 = private unnamed_addr constant [40 x i8] c"scalar(range(0, 5) error(1e-100) final)\00", section "llvm.metadata", !taffo.info !23
@.str.11 = private unnamed_addr constant [44 x i8] c"scalar(range(-4096,4096) error(1e-1) final)\00", section "llvm.metadata", !taffo.info !23
@llvm.global.annotations = appending global [4 x { i8*, i8*, i8*, i32 }] [{ i8*, i8*, i8*, i32 } { i8* bitcast ([28 x double]* @mean to i8*), i8* getelementptr inbounds ([49 x i8], [49 x i8]* @.str.8, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 33 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([32 x [28 x double]]* @data to i8*), i8* getelementptr inbounds ([43 x i8], [43 x i8]* @.str.9, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 34 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([28 x [28 x double]]* @corr to i8*), i8* getelementptr inbounds ([40 x i8], [40 x i8]* @.str.10, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 35 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([28 x double]* @stddev to i8*), i8* getelementptr inbounds ([44 x i8], [44 x i8]* @.str.11, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 36 }], section "llvm.metadata"

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @gettime() #0 !taffo.initweight !27 !taffo.funinfo !27 {
entry:
  %tmp = alloca %struct.timespec, align 8, !taffo.structinfo !27
  %call = call i32 @clock_gettime(i32 2, %struct.timespec* %tmp) #3, !taffo.constinfo !28
  %tv_sec = getelementptr inbounds %struct.timespec, %struct.timespec* %tmp, i32 0, i32 0
  %tmp1 = load i64, i64* %tv_sec, align 8
  %mul = mul nsw i64 %tmp1, 1000000, !taffo.constinfo !29
  %tv_nsec = getelementptr inbounds %struct.timespec, %struct.timespec* %tmp, i32 0, i32 1
  %tmp2 = load i64, i64* %tv_nsec, align 8
  %div = sdiv i64 %tmp2, 1000, !taffo.constinfo !29
  %add = add nsw i64 %mul, %div
  ret i64 %add
}

; Function Attrs: nounwind
declare !taffo.initweight !30 !taffo.funinfo !31 dso_local i32 @clock_gettime(i32, %struct.timespec*) #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_START() #0 !taffo.initweight !27 !taffo.funinfo !27 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !32
  store i64 %call, i64* @time_that_takes, align 8, !taffo.constinfo !29
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_TOGGLE() #0 !taffo.initweight !27 !taffo.funinfo !27 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !32
  %tmp = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %sub = sub i64 %call, %tmp
  store i64 %sub, i64* @time_that_takes, align 8, !taffo.constinfo !29
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @TIMING_CPUCLOCK_S() #0 !taffo.initweight !27 !taffo.funinfo !27 {
entry:
  %tmp = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  ret i64 %tmp
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_PRINT() #0 !taffo.initweight !27 !taffo.funinfo !27 {
entry:
  %tmp = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %tmp1 = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i64 %tmp1), !taffo.constinfo !33
  ret void
}

declare !taffo.initweight !30 !taffo.funinfo !31 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #2

; Function Attrs: noinline nounwind uwtable
define dso_local void @TAFFO_DUMPCONFIG() #0 !taffo.initweight !27 !taffo.funinfo !27 {
entry:
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !27 !taffo.funinfo !27 {
entry:
  call void @TAFFO_DUMPCONFIG(), !taffo.constinfo !32
  call void @TIMING_CPUCLOCK_START(), !taffo.constinfo !32
  br label %for.cond

for.cond:                                         ; preds = %for.inc12, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc13, %for.inc12 ], !taffo.info !34
  %cmp = icmp slt i32 %i.0, 32, !taffo.info !36, !taffo.initweight !37
  br i1 %cmp, label %for.body, label %for.end14, !taffo.info !36, !taffo.initweight !38

for.body:                                         ; preds = %for.cond
  br label %for.cond5

for.cond5:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !39
  %cmp6 = icmp slt i32 %j.0, 28, !taffo.info !41, !taffo.initweight !37
  br i1 %cmp6, label %for.body7, label %for.end, !taffo.info !41, !taffo.initweight !38

for.body7:                                        ; preds = %for.cond5
  %mul = mul nsw i32 %i.0, %j.0, !taffo.info !36, !taffo.initweight !37
  %conv = sitofp i32 %mul to double, !taffo.info !42, !taffo.initweight !38
  %div = fdiv double %conv, 2.800000e+01, !taffo.info !44, !taffo.initweight !47, !taffo.constinfo !48
  %conv8 = sitofp i32 %i.0 to double, !taffo.info !42, !taffo.initweight !37
  %add = fadd double %div, %conv8, !taffo.info !51, !taffo.initweight !38
  %div9 = fdiv double %add, 3.200000e+01, !taffo.info !53, !taffo.initweight !47, !taffo.constinfo !55
  %idxprom = sext i32 %i.0 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom, !taffo.info !6, !taffo.initweight !58
  %idxprom10 = sext i32 %j.0 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx11 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx, i64 0, i64 %idxprom10, !taffo.info !6, !taffo.initweight !37
  store double %div9, double* %arrayidx11, align 8, !taffo.info !59, !taffo.initweight !38
  br label %for.inc

for.inc:                                          ; preds = %for.body7
  %inc = add nsw i32 %j.0, 1, !taffo.info !41, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond5

for.end:                                          ; preds = %for.cond5
  br label %for.inc12

for.inc12:                                        ; preds = %for.end
  %inc13 = add nsw i32 %i.0, 1, !taffo.info !36, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond

for.end14:                                        ; preds = %for.cond
  br label %for.cond16

for.cond16:                                       ; preds = %for.inc39, %for.end14
  %j.1 = phi i32 [ 0, %for.end14 ], [ %inc40, %for.inc39 ], !taffo.info !39
  %cmp17 = icmp slt i32 %j.1, 28, !taffo.info !41, !taffo.initweight !37
  br i1 %cmp17, label %for.body19, label %for.end41, !taffo.info !41, !taffo.initweight !38

for.body19:                                       ; preds = %for.cond16
  %idxprom20 = sext i32 %j.1 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx21 = getelementptr inbounds [28 x double], [28 x double]* @mean, i64 0, i64 %idxprom20, !taffo.info !11, !taffo.initweight !58
  store double 0.000000e+00, double* %arrayidx21, align 8, !taffo.info !60, !taffo.initweight !37, !taffo.constinfo !61
  br label %for.cond22

for.cond22:                                       ; preds = %for.inc33, %for.body19
  %i.1 = phi i32 [ 0, %for.body19 ], [ %inc34, %for.inc33 ], !taffo.info !34
  %cmp23 = icmp slt i32 %i.1, 32, !taffo.info !36, !taffo.initweight !37
  br i1 %cmp23, label %for.body25, label %for.end35, !taffo.info !36, !taffo.initweight !38

for.body25:                                       ; preds = %for.cond22
  %idxprom26 = sext i32 %i.1 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx27 = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom26, !taffo.info !6, !taffo.initweight !58
  %idxprom28 = sext i32 %j.1 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx29 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx27, i64 0, i64 %idxprom28, !taffo.info !6, !taffo.initweight !37
  %tmp = load double, double* %arrayidx29, align 8, !taffo.info !6, !taffo.initweight !38
  %idxprom30 = sext i32 %j.1 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx31 = getelementptr inbounds [28 x double], [28 x double]* @mean, i64 0, i64 %idxprom30, !taffo.info !11, !taffo.initweight !58
  %tmp1 = load double, double* %arrayidx31, align 8, !taffo.info !11, !taffo.initweight !37
  %add32 = fadd double %tmp1, %tmp, !taffo.info !62, !taffo.initweight !38
  store double %add32, double* %arrayidx31, align 8, !taffo.info !60, !taffo.initweight !37
  br label %for.inc33

for.inc33:                                        ; preds = %for.body25
  %inc34 = add nsw i32 %i.1, 1, !taffo.info !36, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond22

for.end35:                                        ; preds = %for.cond22
  %idxprom36 = sext i32 %j.1 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx37 = getelementptr inbounds [28 x double], [28 x double]* @mean, i64 0, i64 %idxprom36, !taffo.info !11, !taffo.initweight !58
  %tmp2 = load double, double* %arrayidx37, align 8, !taffo.info !11, !taffo.initweight !37
  %div38 = fdiv double %tmp2, 3.200000e+01, !taffo.info !64, !taffo.initweight !37, !taffo.constinfo !55
  store double %div38, double* %arrayidx37, align 8, !taffo.info !60, !taffo.initweight !37
  br label %for.inc39

for.inc39:                                        ; preds = %for.end35
  %inc40 = add nsw i32 %j.1, 1, !taffo.info !41, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond16

for.end41:                                        ; preds = %for.cond16
  br label %for.cond42

for.cond42:                                       ; preds = %for.inc87, %for.end41
  %j.2 = phi i32 [ 0, %for.end41 ], [ %inc88, %for.inc87 ], !taffo.info !39
  %cmp43 = icmp slt i32 %j.2, 28, !taffo.info !41, !taffo.initweight !37
  br i1 %cmp43, label %for.body45, label %for.end89, !taffo.info !41, !taffo.initweight !38

for.body45:                                       ; preds = %for.cond42
  %idxprom46 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx47 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom46, !taffo.info !14, !taffo.initweight !58
  store double 0.000000e+00, double* %arrayidx47, align 8, !taffo.info !67, !taffo.initweight !37, !taffo.constinfo !61
  br label %for.cond48

for.cond48:                                       ; preds = %for.inc69, %for.body45
  %i.2 = phi i32 [ 0, %for.body45 ], [ %inc70, %for.inc69 ], !taffo.info !34
  %cmp49 = icmp slt i32 %i.2, 32, !taffo.info !36, !taffo.initweight !37
  br i1 %cmp49, label %for.body51, label %for.end71, !taffo.info !36, !taffo.initweight !38

for.body51:                                       ; preds = %for.cond48
  %idxprom52 = sext i32 %i.2 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx53 = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom52, !taffo.info !6, !taffo.initweight !58
  %idxprom54 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx55 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx53, i64 0, i64 %idxprom54, !taffo.info !6, !taffo.initweight !37
  %tmp3 = load double, double* %arrayidx55, align 8, !taffo.info !6, !taffo.initweight !38
  %idxprom56 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx57 = getelementptr inbounds [28 x double], [28 x double]* @mean, i64 0, i64 %idxprom56, !taffo.info !11, !taffo.initweight !58
  %tmp4 = load double, double* %arrayidx57, align 8, !taffo.info !11, !taffo.initweight !37
  %sub = fsub double %tmp3, %tmp4, !taffo.info !62, !taffo.initweight !38
  %idxprom58 = sext i32 %i.2 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx59 = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom58, !taffo.info !6, !taffo.initweight !58
  %idxprom60 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx61 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx59, i64 0, i64 %idxprom60, !taffo.info !6, !taffo.initweight !37
  %tmp5 = load double, double* %arrayidx61, align 8, !taffo.info !6, !taffo.initweight !38
  %idxprom62 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx63 = getelementptr inbounds [28 x double], [28 x double]* @mean, i64 0, i64 %idxprom62, !taffo.info !11, !taffo.initweight !58
  %tmp6 = load double, double* %arrayidx63, align 8, !taffo.info !11, !taffo.initweight !37
  %sub64 = fsub double %tmp5, %tmp6, !taffo.info !62, !taffo.initweight !38
  %mul65 = fmul double %sub, %sub64, !taffo.info !68, !taffo.initweight !47
  %idxprom66 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx67 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom66, !taffo.info !14, !taffo.initweight !58
  %tmp7 = load double, double* %arrayidx67, align 8, !taffo.info !14, !taffo.initweight !37
  %add68 = fadd double %tmp7, %mul65, !taffo.info !71, !taffo.initweight !38
  store double %add68, double* %arrayidx67, align 8, !taffo.info !67, !taffo.initweight !37
  br label %for.inc69

for.inc69:                                        ; preds = %for.body51
  %inc70 = add nsw i32 %i.2, 1, !taffo.info !36, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond48

for.end71:                                        ; preds = %for.cond48
  %idxprom72 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx73 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom72, !taffo.info !14, !taffo.initweight !58
  %tmp8 = load double, double* %arrayidx73, align 8, !taffo.info !14, !taffo.initweight !37
  %div74 = fdiv double %tmp8, 3.200000e+01, !taffo.info !73, !taffo.initweight !37, !taffo.constinfo !55
  store double %div74, double* %arrayidx73, align 8, !taffo.info !67, !taffo.initweight !37
  %idxprom75 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx76 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom75, !taffo.info !14, !taffo.initweight !58
  %tmp9 = load double, double* %arrayidx76, align 8, !taffo.info !14, !taffo.initweight !37
  %call = call double @sqrt(double %tmp9) #3, !taffo.info !76, !taffo.initweight !38, !taffo.constinfo !29
  %idxprom77 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx78 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom77, !taffo.info !14, !taffo.initweight !58
  store double %call, double* %arrayidx78, align 8, !taffo.info !67, !taffo.initweight !37
  %idxprom79 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx80 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom79, !taffo.info !14, !taffo.initweight !58
  %tmp10 = load double, double* %arrayidx80, align 8, !taffo.info !14, !taffo.initweight !37
  %cmp81 = fcmp ole double %tmp10, 1.000000e-01, !taffo.info !79, !taffo.initweight !37
  br i1 %cmp81, label %cond.true, label %cond.false, !taffo.info !80, !taffo.initweight !38

cond.true:                                        ; preds = %for.end71
  br label %cond.end

cond.false:                                       ; preds = %for.end71
  %idxprom83 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx84 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom83, !taffo.info !14, !taffo.initweight !58
  %tmp11 = load double, double* %arrayidx84, align 8, !taffo.info !14, !taffo.initweight !37
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !14, !taffo.initweight !38
  %idxprom85 = sext i32 %j.2 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx86 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom85, !taffo.info !14, !taffo.initweight !58
  store double %cond, double* %arrayidx86, align 8, !taffo.info !67, !taffo.initweight !37
  br label %for.inc87

for.inc87:                                        ; preds = %cond.end
  %inc88 = add nsw i32 %j.2, 1, !taffo.info !41, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond42

for.end89:                                        ; preds = %for.cond42
  br label %for.cond90

for.cond90:                                       ; preds = %for.inc117, %for.end89
  %i.3 = phi i32 [ 0, %for.end89 ], [ %inc118, %for.inc117 ], !taffo.info !34
  %cmp91 = icmp slt i32 %i.3, 32, !taffo.info !36, !taffo.initweight !37
  br i1 %cmp91, label %for.body93, label %for.end119, !taffo.info !36, !taffo.initweight !38

for.body93:                                       ; preds = %for.cond90
  br label %for.cond94

for.cond94:                                       ; preds = %for.inc114, %for.body93
  %j.3 = phi i32 [ 0, %for.body93 ], [ %inc115, %for.inc114 ], !taffo.info !39
  %cmp95 = icmp slt i32 %j.3, 28, !taffo.info !41, !taffo.initweight !37
  br i1 %cmp95, label %for.body97, label %for.end116, !taffo.info !41, !taffo.initweight !38

for.body97:                                       ; preds = %for.cond94
  %idxprom98 = sext i32 %j.3 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx99 = getelementptr inbounds [28 x double], [28 x double]* @mean, i64 0, i64 %idxprom98, !taffo.info !11, !taffo.initweight !58
  %tmp12 = load double, double* %arrayidx99, align 8, !taffo.info !11, !taffo.initweight !37
  %idxprom100 = sext i32 %i.3 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx101 = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom100, !taffo.info !6, !taffo.initweight !58
  %idxprom102 = sext i32 %j.3 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx103 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx101, i64 0, i64 %idxprom102, !taffo.info !6, !taffo.initweight !37
  %tmp13 = load double, double* %arrayidx103, align 8, !taffo.info !6, !taffo.initweight !38
  %sub104 = fsub double %tmp13, %tmp12, !taffo.info !62, !taffo.initweight !38
  store double %sub104, double* %arrayidx103, align 8, !taffo.info !59, !taffo.initweight !38
  %call105 = call double @sqrt(double 3.200000e+01) #3, !taffo.info !81, !taffo.initweight !37, !taffo.constinfo !83
  %idxprom106 = sext i32 %j.3 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx107 = getelementptr inbounds [28 x double], [28 x double]* @stddev, i64 0, i64 %idxprom106, !taffo.info !14, !taffo.initweight !58
  %tmp14 = load double, double* %arrayidx107, align 8, !taffo.info !84, !taffo.initweight !37
  %mul108 = fmul double %call105, %tmp14, !taffo.info !86, !taffo.initweight !38
  %idxprom109 = sext i32 %i.3 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx110 = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom109, !taffo.info !6, !taffo.initweight !58
  %idxprom111 = sext i32 %j.3 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx112 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx110, i64 0, i64 %idxprom111, !taffo.info !6, !taffo.initweight !37
  %tmp15 = load double, double* %arrayidx112, align 8, !taffo.info !6, !taffo.initweight !38
  %div113 = fdiv double %tmp15, %mul108, !taffo.info !88, !taffo.initweight !47
  store double %div113, double* %arrayidx112, align 8, !taffo.info !59, !taffo.initweight !38
  br label %for.inc114

for.inc114:                                       ; preds = %for.body97
  %inc115 = add nsw i32 %j.3, 1, !taffo.info !41, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond94

for.end116:                                       ; preds = %for.cond94
  br label %for.inc117

for.inc117:                                       ; preds = %for.end116
  %inc118 = add nsw i32 %i.3, 1, !taffo.info !36, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond90

for.end119:                                       ; preds = %for.cond90
  br label %for.cond120

for.cond120:                                      ; preds = %for.inc169, %for.end119
  %i.4 = phi i32 [ 0, %for.end119 ], [ %inc170, %for.inc169 ], !taffo.info !34
  %cmp121 = icmp slt i32 %i.4, 27, !taffo.info !36, !taffo.initweight !37
  br i1 %cmp121, label %for.body123, label %for.end171, !taffo.info !36, !taffo.initweight !38

for.body123:                                      ; preds = %for.cond120
  %idxprom124 = sext i32 %i.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx125 = getelementptr inbounds [28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 %idxprom124, !taffo.info !18, !taffo.initweight !58
  %idxprom126 = sext i32 %i.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx127 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx125, i64 0, i64 %idxprom126, !taffo.info !18, !taffo.initweight !37
  store double 1.000000e+00, double* %arrayidx127, align 8, !taffo.info !91, !taffo.initweight !38, !taffo.constinfo !92
  %add128 = add nsw i32 %i.4, 1, !taffo.info !36, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond129

for.cond129:                                      ; preds = %for.inc166, %for.body123
  %j.4 = phi i32 [ %add128, %for.body123 ], [ %inc167, %for.inc166 ], !taffo.info !34
  %cmp130 = icmp slt i32 %j.4, 28, !taffo.info !41, !taffo.initweight !37
  br i1 %cmp130, label %for.body132, label %for.end168, !taffo.info !41, !taffo.initweight !38

for.body132:                                      ; preds = %for.cond129
  %idxprom133 = sext i32 %i.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx134 = getelementptr inbounds [28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 %idxprom133, !taffo.info !18, !taffo.initweight !58
  %idxprom135 = sext i32 %j.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx136 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx134, i64 0, i64 %idxprom135, !taffo.info !18, !taffo.initweight !37
  store double 0.000000e+00, double* %arrayidx136, align 8, !taffo.info !91, !taffo.initweight !38, !taffo.constinfo !61
  br label %for.cond137

for.cond137:                                      ; preds = %for.inc155, %for.body132
  %k.0 = phi i32 [ 0, %for.body132 ], [ %inc156, %for.inc155 ], !taffo.info !39
  %cmp138 = icmp slt i32 %k.0, 32, !taffo.info !41, !taffo.initweight !37
  br i1 %cmp138, label %for.body140, label %for.end157, !taffo.info !41, !taffo.initweight !38

for.body140:                                      ; preds = %for.cond137
  %idxprom141 = sext i32 %k.0 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx142 = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom141, !taffo.info !6, !taffo.initweight !58
  %idxprom143 = sext i32 %i.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx144 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx142, i64 0, i64 %idxprom143, !taffo.info !6, !taffo.initweight !37
  %tmp16 = load double, double* %arrayidx144, align 8, !taffo.info !6, !taffo.initweight !38
  %idxprom145 = sext i32 %k.0 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx146 = getelementptr inbounds [32 x [28 x double]], [32 x [28 x double]]* @data, i64 0, i64 %idxprom145, !taffo.info !6, !taffo.initweight !58
  %idxprom147 = sext i32 %j.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx148 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx146, i64 0, i64 %idxprom147, !taffo.info !6, !taffo.initweight !37
  %tmp17 = load double, double* %arrayidx148, align 8, !taffo.info !6, !taffo.initweight !38
  %mul149 = fmul double %tmp16, %tmp17, !taffo.info !95, !taffo.initweight !47
  %idxprom150 = sext i32 %i.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx151 = getelementptr inbounds [28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 %idxprom150, !taffo.info !18, !taffo.initweight !58
  %idxprom152 = sext i32 %j.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx153 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx151, i64 0, i64 %idxprom152, !taffo.info !18, !taffo.initweight !37
  %tmp18 = load double, double* %arrayidx153, align 8, !taffo.info !18, !taffo.initweight !38
  %add154 = fadd double %tmp18, %mul149, !taffo.info !98, !taffo.initweight !47
  store double %add154, double* %arrayidx153, align 8, !taffo.info !91, !taffo.initweight !38
  br label %for.inc155

for.inc155:                                       ; preds = %for.body140
  %inc156 = add nsw i32 %k.0, 1, !taffo.info !41, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond137

for.end157:                                       ; preds = %for.cond137
  %idxprom158 = sext i32 %i.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx159 = getelementptr inbounds [28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 %idxprom158, !taffo.info !18, !taffo.initweight !58
  %idxprom160 = sext i32 %j.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx161 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx159, i64 0, i64 %idxprom160, !taffo.info !18, !taffo.initweight !37
  %tmp19 = load double, double* %arrayidx161, align 8, !taffo.info !18, !taffo.initweight !38
  %idxprom162 = sext i32 %j.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx163 = getelementptr inbounds [28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 %idxprom162, !taffo.info !18, !taffo.initweight !58
  %idxprom164 = sext i32 %i.4 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx165 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx163, i64 0, i64 %idxprom164, !taffo.info !18, !taffo.initweight !37
  store double %tmp19, double* %arrayidx165, align 8, !taffo.info !91, !taffo.initweight !38
  br label %for.inc166

for.inc166:                                       ; preds = %for.end157
  %inc167 = add nsw i32 %j.4, 1, !taffo.info !41, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond129

for.end168:                                       ; preds = %for.cond129
  br label %for.inc169

for.inc169:                                       ; preds = %for.end168
  %inc170 = add nsw i32 %i.4, 1, !taffo.info !36, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond120

for.end171:                                       ; preds = %for.cond120
  store double 1.000000e+00, double* getelementptr inbounds ([28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 27, i64 27), align 8, !taffo.info !91, !taffo.initweight !37, !taffo.constinfo !92
  call void @TIMING_CPUCLOCK_TOGGLE(), !taffo.constinfo !32
  call void @TIMING_CPUCLOCK_PRINT(), !taffo.constinfo !32
  br label %for.cond172

for.cond172:                                      ; preds = %for.inc189, %for.end171
  %i.5 = phi i32 [ 0, %for.end171 ], [ %inc190, %for.inc189 ], !taffo.info !34
  %cmp173 = icmp slt i32 %i.5, 28, !taffo.info !36, !taffo.initweight !37
  br i1 %cmp173, label %for.body175, label %for.end191, !taffo.info !36, !taffo.initweight !38

for.body175:                                      ; preds = %for.cond172
  br label %for.cond176

for.cond176:                                      ; preds = %for.inc185, %for.body175
  %j.5 = phi i32 [ 0, %for.body175 ], [ %inc186, %for.inc185 ], !taffo.info !39
  %cmp177 = icmp slt i32 %j.5, 28, !taffo.info !41, !taffo.initweight !37
  br i1 %cmp177, label %for.body179, label %for.end187, !taffo.info !41, !taffo.initweight !38

for.body179:                                      ; preds = %for.cond176
  %idxprom180 = sext i32 %i.5 to i64, !taffo.info !36, !taffo.initweight !37
  %arrayidx181 = getelementptr inbounds [28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 %idxprom180, !taffo.info !18, !taffo.initweight !58
  %idxprom182 = sext i32 %j.5 to i64, !taffo.info !41, !taffo.initweight !37
  %arrayidx183 = getelementptr inbounds [28 x double], [28 x double]* %arrayidx181, i64 0, i64 %idxprom182, !taffo.info !18, !taffo.initweight !37
  %tmp20 = load double, double* %arrayidx183, align 8, !taffo.info !18, !taffo.initweight !38
  %call184 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.6, i32 0, i32 0), double %tmp20), !taffo.info !100, !taffo.initweight !47, !taffo.constinfo !28
  br label %for.inc185

for.inc185:                                       ; preds = %for.body179
  %inc186 = add nsw i32 %j.5, 1, !taffo.info !41, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond176

for.end187:                                       ; preds = %for.cond176
  %call188 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.7, i32 0, i32 0)), !taffo.constinfo !29
  br label %for.inc189

for.inc189:                                       ; preds = %for.end187
  %inc190 = add nsw i32 %i.5, 1, !taffo.info !36, !taffo.initweight !37, !taffo.constinfo !29
  br label %for.cond172

for.end191:                                       ; preds = %for.cond172
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !101 !taffo.funinfo !102 dso_local double @sqrt(double) #1

declare !taffo.initweight !101 !taffo.funinfo !102 dso_local i32 @printf(i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!25}
!llvm.ident = !{!26}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 0.000000e+00}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.080000e+02}
!4 = !{i1 false, !5, i1 false, i2 0}
!5 = !{double 0.000000e+00, double 1.210000e+02}
!6 = !{!7, !8, !9, i2 -1}
!7 = !{!"fixp", i32 -32, i32 27}
!8 = !{double -1.000000e+01, double 1.000000e+01}
!9 = !{double 1.000000e-100}
!10 = !{i32 0}
!11 = !{!12, !13, !9, i2 -1}
!12 = !{!"fixp", i32 -32, i32 15}
!13 = !{double -5.000000e+04, double 5.000000e+04}
!14 = !{!15, !16, !17, i2 -1}
!15 = !{!"fixp", i32 -32, i32 18}
!16 = !{double -4.096000e+03, double 4.096000e+03}
!17 = !{double 1.000000e-01}
!18 = !{!19, !20, !9, i2 -1}
!19 = !{!"fixp", i32 32, i32 29}
!20 = !{double 0.000000e+00, double 5.000000e+00}
!21 = !{i1 false, !22, i1 false, i2 0}
!22 = !{double 0.000000e+00, double 1.000000e+01}
!23 = !{i1 false, !24, i1 false, i2 0}
!24 = !{double 0.000000e+00, double 1.150000e+02}
!25 = !{i32 1, !"wchar_size", i32 4}
!26 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!27 = !{}
!28 = !{i1 false, i1 false, i1 false}
!29 = !{i1 false, i1 false}
!30 = !{i32 -1, i32 -1}
!31 = !{i32 0, i1 false, i32 0, i1 false}
!32 = !{i1 false}
!33 = !{i1 false, i1 false, i1 false, i1 false}
!34 = !{i1 false, !35, i1 false, i2 0}
!35 = !{double 0.000000e+00, double 2.400000e+02}
!36 = !{i1 false, !35, i1 false, i2 -1}
!37 = !{i32 2}
!38 = !{i32 3}
!39 = !{i1 false, !40, i1 false, i2 0}
!40 = !{double 0.000000e+00, double 2.600000e+02}
!41 = !{i1 false, !40, i1 false, i2 -1}
!42 = !{!43, !35, i1 false, i2 -1}
!43 = !{!"fixp", i32 32, i32 24}
!44 = !{!45, !46, i1 false, i2 -1}
!45 = !{!"fixp", i32 32, i32 28}
!46 = !{double 0.000000e+00, double 0x4021249249249249}
!47 = !{i32 4}
!48 = !{i1 false, !49}
!49 = !{i1 false, !50, i1 false, i2 0}
!50 = !{double 2.800000e+01, double 2.800000e+01}
!51 = !{!43, !52, i1 false, i2 -1}
!52 = !{double 0.000000e+00, double 0x406F124924924925}
!53 = !{!45, !54, i1 false, i2 -1}
!54 = !{double 0.000000e+00, double 0x401F124924924925}
!55 = !{i1 false, !56}
!56 = !{i1 false, !57, i1 false, i2 0}
!57 = !{double 3.200000e+01, double 3.200000e+01}
!58 = !{i32 1}
!59 = !{i1 false, !8, !9, i2 -1}
!60 = !{i1 false, !13, !9, i2 -1}
!61 = !{!0, i1 false}
!62 = !{!12, !63, !9, i2 -1}
!63 = !{double -5.001000e+04, double 5.001000e+04}
!64 = !{!65, !66, !9, i2 1}
!65 = !{!"fixp", i32 -32, i32 20}
!66 = !{double -1.562500e+03, double 1.562500e+03}
!67 = !{i1 false, !16, !17, i2 -1}
!68 = !{!69, !70, !9, i2 -1}
!69 = !{!"fixp", i32 -64, i32 31}
!70 = !{double 0xC1E2A24774800000, double 0x41E2A24774800000}
!71 = !{!69, !72, !17, i2 -1}
!72 = !{double 0xC1E2A24974800000, double 0x41E2A24974800000}
!73 = !{!74, !75, !9, i2 1}
!74 = !{!"fixp", i32 -32, i32 23}
!75 = !{double -1.280000e+02, double 1.280000e+02}
!76 = !{!77, !78, !17, i2 -1}
!77 = !{!"fixp", i32 32, i32 25}
!78 = !{double 0.000000e+00, double 6.400000e+01}
!79 = !{!15, i1 false, !17, i2 -1}
!80 = !{i1 false, i1 false, i1 false, i2 1}
!81 = !{!19, !82, !9, i2 1}
!82 = !{double 0x4016A09E667F3BCD, double 0x4016A09E667F3BCD}
!83 = !{!56, i1 false}
!84 = !{!85, !16, !17, i2 -1}
!85 = !{!"fixp", i32 -32, i32 16}
!86 = !{!85, !87, !17, i2 -1}
!87 = !{double 0xC0D6A09E667F3BCD, double 0x40D6A09E667F3BCD}
!88 = !{!89, !90, !9, i2 -1}
!89 = !{!"fixp", i32 -32, i32 30}
!90 = !{double 0xBF3C48C6001F0ABF, double 0x3F3C48C6001F0ABF}
!91 = !{i1 false, !20, !9, i2 -1}
!92 = !{!93, i1 false}
!93 = !{i1 false, !94, i1 false, i2 0}
!94 = !{double 1.000000e+00, double 1.000000e+00}
!95 = !{!96, !97, !9, i2 -1}
!96 = !{!"fixp", i32 -32, i32 24}
!97 = !{double -1.000000e+02, double 1.000000e+02}
!98 = !{!96, !99, !9, i2 -1}
!99 = !{double -1.000000e+02, double 1.050000e+02}
!100 = !{!19, i1 false, !9, i2 -1}
!101 = !{i32 -1}
!102 = !{i32 0, i1 false}
