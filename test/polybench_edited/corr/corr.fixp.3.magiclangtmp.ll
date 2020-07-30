; ModuleID = 'polybench_edited/corr/corr.fixp.2.magiclangtmp.ll'
source_filename = "polybench_edited/corr/corr.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

@time_that_takes = common dso_local global i64 0, align 8, !taffo.info !0
@stderr = external dso_local global %struct._IO_FILE*, align 8
@.str = private unnamed_addr constant [4 x i8] c"%ld\00", align 1, !taffo.info !2
@.str.1 = private unnamed_addr constant [28 x i8] c"scalar(range(0, 28) final )\00", section "llvm.metadata", !taffo.info !4
@.str.2 = private unnamed_addr constant [29 x i8] c"polybench_edited/corr/corr.c\00", section "llvm.metadata", !taffo.info !6
@.str.3 = private unnamed_addr constant [28 x i8] c"scalar(range(0, 32) final )\00", section "llvm.metadata", !taffo.info !4
@.str.4 = private unnamed_addr constant [37 x i8] c"scalar(range(1, 3000) error(1e-100))\00", section "llvm.metadata", !taffo.info !4
@data = common dso_local global [28 x [32 x double]] zeroinitializer, align 16, !taffo.initweight !8, !taffo.info !9
@.str.5 = private unnamed_addr constant [9 x i8] c"scalar()\00", section "llvm.metadata", !taffo.info !4
@mean = common dso_local global [32 x double] zeroinitializer, align 16, !taffo.initweight !8, !taffo.info !12
@stddev = common dso_local global [32 x double] zeroinitializer, align 16, !taffo.initweight !8, !taffo.info !14
@corr = common dso_local global [32 x [32 x double]] zeroinitializer, align 16, !taffo.initweight !8, !taffo.info !17
@.str.6 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !2
@.str.7 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !19
@.str.8 = private unnamed_addr constant [49 x i8] c"scalar(range(-50000, 50000) final error(1e-100))\00", section "llvm.metadata", !taffo.info !4
@.str.9 = private unnamed_addr constant [43 x i8] c"scalar(range(-10, 10) error(1e-100) final)\00", section "llvm.metadata", !taffo.info !4
@.str.10 = private unnamed_addr constant [40 x i8] c"scalar(range(0, 5) error(1e-100) final)\00", section "llvm.metadata", !taffo.info !4
@.str.11 = private unnamed_addr constant [44 x i8] c"scalar(range(-4096,4096) error(1e-1) final)\00", section "llvm.metadata", !taffo.info !4
@llvm.global.annotations = appending global [4 x { i8*, i8*, i8*, i32 }] [{ i8*, i8*, i8*, i32 } { i8* bitcast ([32 x double]* @mean to i8*), i8* getelementptr inbounds ([49 x i8], [49 x i8]* @.str.8, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 11 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([28 x [32 x double]]* @data to i8*), i8* getelementptr inbounds ([43 x i8], [43 x i8]* @.str.9, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 12 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([32 x [32 x double]]* @corr to i8*), i8* getelementptr inbounds ([40 x i8], [40 x i8]* @.str.10, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 13 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([32 x double]* @stddev to i8*), i8* getelementptr inbounds ([44 x i8], [44 x i8]* @.str.11, i32 0, i32 0), i8* getelementptr inbounds ([29 x i8], [29 x i8]* @.str.2, i32 0, i32 0), i32 14 }], section "llvm.metadata"

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @gettime() #0 !taffo.initweight !23 !taffo.funinfo !23 {
entry:
  %call = call i64 @clock() #3, !taffo.constinfo !24
  ret i64 %call
}

; Function Attrs: nounwind
declare !taffo.initweight !23 !taffo.funinfo !23 dso_local i64 @clock() #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_START() #0 !taffo.initweight !23 !taffo.funinfo !23 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !24
  store i64 %call, i64* @time_that_takes, align 8, !taffo.constinfo !25
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_TOGGLE() #0 !taffo.initweight !23 !taffo.funinfo !23 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !24
  %0 = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %sub = sub i64 %call, %0
  store i64 %sub, i64* @time_that_takes, align 8, !taffo.constinfo !25
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @TIMING_CPUCLOCK_S() #0 !taffo.initweight !23 !taffo.funinfo !23 {
entry:
  %0 = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  ret i64 %0
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_PRINT() #0 !taffo.initweight !23 !taffo.funinfo !23 {
entry:
  %0 = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %1 = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %0, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i64 %1), !taffo.constinfo !26
  ret void
}

declare !taffo.initweight !27 !taffo.funinfo !28 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #2

; Function Attrs: noinline nounwind uwtable
define dso_local void @TAFFO_DUMPCONFIG() #0 !taffo.initweight !23 !taffo.funinfo !23 {
entry:
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !23 !taffo.funinfo !23 {
entry:
  call void @TAFFO_DUMPCONFIG(), !taffo.constinfo !24
  call void @TIMING_CPUCLOCK_START(), !taffo.constinfo !24
  br label %for.cond

for.cond:                                         ; preds = %for.inc12, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc13, %for.inc12 ], !taffo.info !29
  %cmp = icmp slt i32 %i.0, 28, !taffo.initweight !31, !taffo.info !32
  br i1 %cmp, label %for.body, label %for.end14, !taffo.initweight !33, !taffo.info !32

for.body:                                         ; preds = %for.cond
  br label %for.cond5

for.cond5:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !34
  %cmp6 = icmp slt i32 %j.0, 32, !taffo.initweight !31, !taffo.info !36
  br i1 %cmp6, label %for.body7, label %for.end, !taffo.initweight !33, !taffo.info !36

for.body7:                                        ; preds = %for.cond5
  %mul = mul nsw i32 %i.0, %j.0, !taffo.initweight !31, !taffo.info !32
  %conv = sitofp i32 %mul to double, !taffo.initweight !33, !taffo.info !32
  %div = fdiv double %conv, 3.200000e+01, !taffo.initweight !37, !taffo.info !38, !taffo.constinfo !40
  %conv8 = sitofp i32 %i.0 to double, !taffo.initweight !31, !taffo.info !32
  %add = fadd double %div, %conv8, !taffo.initweight !33, !taffo.info !43
  %div9 = fdiv double %add, 2.800000e+01, !taffo.initweight !37, !taffo.info !45, !taffo.constinfo !47
  %idxprom = sext i32 %i.0 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom, !taffo.initweight !50, !taffo.info !9
  %idxprom10 = sext i32 %j.0 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx11 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx, i64 0, i64 %idxprom10, !taffo.initweight !31, !taffo.info !9
  store double %div9, double* %arrayidx11, align 8, !taffo.initweight !33, !taffo.info !9
  br label %for.inc

for.inc:                                          ; preds = %for.body7
  %inc = add nsw i32 %j.0, 1, !taffo.initweight !31, !taffo.info !36, !taffo.constinfo !25
  br label %for.cond5

for.end:                                          ; preds = %for.cond5
  br label %for.inc12

for.inc12:                                        ; preds = %for.end
  %inc13 = add nsw i32 %i.0, 1, !taffo.initweight !31, !taffo.info !32, !taffo.constinfo !25
  br label %for.cond

for.end14:                                        ; preds = %for.cond
  br label %for.cond16

for.cond16:                                       ; preds = %for.inc39, %for.end14
  %j.1 = phi i32 [ 0, %for.end14 ], [ %inc40, %for.inc39 ], !taffo.info !34
  %cmp17 = icmp slt i32 %j.1, 32, !taffo.initweight !31, !taffo.info !36
  br i1 %cmp17, label %for.body19, label %for.end41, !taffo.initweight !33, !taffo.info !36

for.body19:                                       ; preds = %for.cond16
  %idxprom20 = sext i32 %j.1 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx21 = getelementptr inbounds [32 x double], [32 x double]* @mean, i64 0, i64 %idxprom20, !taffo.initweight !50, !taffo.info !12
  store double 0.000000e+00, double* %arrayidx21, align 8, !taffo.initweight !31, !taffo.info !12, !taffo.constinfo !51
  br label %for.cond22

for.cond22:                                       ; preds = %for.inc33, %for.body19
  %i.1 = phi i32 [ 0, %for.body19 ], [ %inc34, %for.inc33 ], !taffo.info !29
  %cmp23 = icmp slt i32 %i.1, 28, !taffo.initweight !31, !taffo.info !32
  br i1 %cmp23, label %for.body25, label %for.end35, !taffo.initweight !33, !taffo.info !32

for.body25:                                       ; preds = %for.cond22
  %idxprom26 = sext i32 %i.1 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx27 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom26, !taffo.initweight !50, !taffo.info !9
  %idxprom28 = sext i32 %j.1 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx29 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx27, i64 0, i64 %idxprom28, !taffo.initweight !31, !taffo.info !9
  %0 = load double, double* %arrayidx29, align 8, !taffo.initweight !33, !taffo.info !9
  %idxprom30 = sext i32 %j.1 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx31 = getelementptr inbounds [32 x double], [32 x double]* @mean, i64 0, i64 %idxprom30, !taffo.initweight !50, !taffo.info !12
  %1 = load double, double* %arrayidx31, align 8, !taffo.initweight !31, !taffo.info !12
  %add32 = fadd double %1, %0, !taffo.initweight !33, !taffo.info !52
  store double %add32, double* %arrayidx31, align 8, !taffo.initweight !31, !taffo.info !12
  br label %for.inc33

for.inc33:                                        ; preds = %for.body25
  %inc34 = add nsw i32 %i.1, 1, !taffo.initweight !31, !taffo.info !32, !taffo.constinfo !25
  br label %for.cond22

for.end35:                                        ; preds = %for.cond22
  %idxprom36 = sext i32 %j.1 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx37 = getelementptr inbounds [32 x double], [32 x double]* @mean, i64 0, i64 %idxprom36, !taffo.initweight !50, !taffo.info !12
  %2 = load double, double* %arrayidx37, align 8, !taffo.initweight !31, !taffo.info !12
  %div38 = fdiv double %2, 2.800000e+01, !taffo.initweight !31, !taffo.info !54, !taffo.constinfo !47
  store double %div38, double* %arrayidx37, align 8, !taffo.initweight !31, !taffo.info !12
  br label %for.inc39

for.inc39:                                        ; preds = %for.end35
  %inc40 = add nsw i32 %j.1, 1, !taffo.initweight !31, !taffo.info !36, !taffo.constinfo !25
  br label %for.cond16

for.end41:                                        ; preds = %for.cond16
  br label %for.cond42

for.cond42:                                       ; preds = %for.inc87, %for.end41
  %j.2 = phi i32 [ 0, %for.end41 ], [ %inc88, %for.inc87 ], !taffo.info !34
  %cmp43 = icmp slt i32 %j.2, 32, !taffo.initweight !31, !taffo.info !36
  br i1 %cmp43, label %for.body45, label %for.end89, !taffo.initweight !33, !taffo.info !36

for.body45:                                       ; preds = %for.cond42
  %idxprom46 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx47 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom46, !taffo.initweight !50, !taffo.info !14
  store double 0.000000e+00, double* %arrayidx47, align 8, !taffo.initweight !31, !taffo.info !14, !taffo.constinfo !51
  br label %for.cond48

for.cond48:                                       ; preds = %for.inc69, %for.body45
  %i.2 = phi i32 [ 0, %for.body45 ], [ %inc70, %for.inc69 ], !taffo.info !29
  %cmp49 = icmp slt i32 %i.2, 28, !taffo.initweight !31, !taffo.info !32
  br i1 %cmp49, label %for.body51, label %for.end71, !taffo.initweight !33, !taffo.info !32

for.body51:                                       ; preds = %for.cond48
  %idxprom52 = sext i32 %i.2 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx53 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom52, !taffo.initweight !50, !taffo.info !9
  %idxprom54 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx55 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx53, i64 0, i64 %idxprom54, !taffo.initweight !31, !taffo.info !9
  %3 = load double, double* %arrayidx55, align 8, !taffo.initweight !33, !taffo.info !9
  %idxprom56 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx57 = getelementptr inbounds [32 x double], [32 x double]* @mean, i64 0, i64 %idxprom56, !taffo.initweight !50, !taffo.info !12
  %4 = load double, double* %arrayidx57, align 8, !taffo.initweight !31, !taffo.info !12
  %sub = fsub double %3, %4, !taffo.initweight !33, !taffo.info !52
  %idxprom58 = sext i32 %i.2 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx59 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom58, !taffo.initweight !50, !taffo.info !9
  %idxprom60 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx61 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx59, i64 0, i64 %idxprom60, !taffo.initweight !31, !taffo.info !9
  %5 = load double, double* %arrayidx61, align 8, !taffo.initweight !33, !taffo.info !9
  %idxprom62 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx63 = getelementptr inbounds [32 x double], [32 x double]* @mean, i64 0, i64 %idxprom62, !taffo.initweight !50, !taffo.info !12
  %6 = load double, double* %arrayidx63, align 8, !taffo.initweight !31, !taffo.info !12
  %sub64 = fsub double %5, %6, !taffo.initweight !33, !taffo.info !52
  %mul65 = fmul double %sub, %sub64, !taffo.initweight !37, !taffo.info !56
  %idxprom66 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx67 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom66, !taffo.initweight !50, !taffo.info !14
  %7 = load double, double* %arrayidx67, align 8, !taffo.initweight !31, !taffo.info !14
  %add68 = fadd double %7, %mul65, !taffo.initweight !33, !taffo.info !58
  store double %add68, double* %arrayidx67, align 8, !taffo.initweight !31, !taffo.info !14
  br label %for.inc69

for.inc69:                                        ; preds = %for.body51
  %inc70 = add nsw i32 %i.2, 1, !taffo.initweight !31, !taffo.info !32, !taffo.constinfo !25
  br label %for.cond48

for.end71:                                        ; preds = %for.cond48
  %idxprom72 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx73 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom72, !taffo.initweight !50, !taffo.info !14
  %8 = load double, double* %arrayidx73, align 8, !taffo.initweight !31, !taffo.info !14
  %div74 = fdiv double %8, 2.800000e+01, !taffo.initweight !31, !taffo.info !60, !taffo.constinfo !47
  store double %div74, double* %arrayidx73, align 8, !taffo.initweight !31, !taffo.info !14
  %idxprom75 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx76 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom75, !taffo.initweight !50, !taffo.info !14
  %9 = load double, double* %arrayidx76, align 8, !taffo.initweight !31, !taffo.info !14
  %call = call double @sqrt(double %9) #3, !taffo.initweight !33, !taffo.info !62, !taffo.constinfo !25
  %idxprom77 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx78 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom77, !taffo.initweight !50, !taffo.info !14
  store double %call, double* %arrayidx78, align 8, !taffo.initweight !31, !taffo.info !14
  %idxprom79 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx80 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom79, !taffo.initweight !50, !taffo.info !14
  %10 = load double, double* %arrayidx80, align 8, !taffo.initweight !31, !taffo.info !14
  %cmp81 = fcmp ole double %10, 1.000000e-01, !taffo.initweight !31, !taffo.info !64
  br i1 %cmp81, label %cond.true, label %cond.false, !taffo.initweight !33, !taffo.info !66

cond.true:                                        ; preds = %for.end71
  br label %cond.end

cond.false:                                       ; preds = %for.end71
  %idxprom83 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx84 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom83, !taffo.initweight !50, !taffo.info !14
  %11 = load double, double* %arrayidx84, align 8, !taffo.initweight !31, !taffo.info !14
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond = phi double [ 1.000000e+00, %cond.true ], [ %11, %cond.false ], !taffo.initweight !33, !taffo.info !14
  %idxprom85 = sext i32 %j.2 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx86 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom85, !taffo.initweight !50, !taffo.info !14
  store double %cond, double* %arrayidx86, align 8, !taffo.initweight !31, !taffo.info !14
  br label %for.inc87

for.inc87:                                        ; preds = %cond.end
  %inc88 = add nsw i32 %j.2, 1, !taffo.initweight !31, !taffo.info !36, !taffo.constinfo !25
  br label %for.cond42

for.end89:                                        ; preds = %for.cond42
  br label %for.cond90

for.cond90:                                       ; preds = %for.inc117, %for.end89
  %i.3 = phi i32 [ 0, %for.end89 ], [ %inc118, %for.inc117 ], !taffo.info !29
  %cmp91 = icmp slt i32 %i.3, 28, !taffo.initweight !31, !taffo.info !32
  br i1 %cmp91, label %for.body93, label %for.end119, !taffo.initweight !33, !taffo.info !32

for.body93:                                       ; preds = %for.cond90
  br label %for.cond94

for.cond94:                                       ; preds = %for.inc114, %for.body93
  %j.3 = phi i32 [ 0, %for.body93 ], [ %inc115, %for.inc114 ], !taffo.info !34
  %cmp95 = icmp slt i32 %j.3, 32, !taffo.initweight !31, !taffo.info !36
  br i1 %cmp95, label %for.body97, label %for.end116, !taffo.initweight !33, !taffo.info !36

for.body97:                                       ; preds = %for.cond94
  %idxprom98 = sext i32 %j.3 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx99 = getelementptr inbounds [32 x double], [32 x double]* @mean, i64 0, i64 %idxprom98, !taffo.initweight !50, !taffo.info !12
  %12 = load double, double* %arrayidx99, align 8, !taffo.initweight !31, !taffo.info !12
  %idxprom100 = sext i32 %i.3 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx101 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom100, !taffo.initweight !50, !taffo.info !9
  %idxprom102 = sext i32 %j.3 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx103 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx101, i64 0, i64 %idxprom102, !taffo.initweight !31, !taffo.info !9
  %13 = load double, double* %arrayidx103, align 8, !taffo.initweight !33, !taffo.info !9
  %sub104 = fsub double %13, %12, !taffo.initweight !33, !taffo.info !52
  store double %sub104, double* %arrayidx103, align 8, !taffo.initweight !33, !taffo.info !9
  %call105 = call double @sqrt(double 2.800000e+01) #3, !taffo.initweight !31, !taffo.info !67, !taffo.constinfo !69
  %idxprom106 = sext i32 %j.3 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx107 = getelementptr inbounds [32 x double], [32 x double]* @stddev, i64 0, i64 %idxprom106, !taffo.initweight !50, !taffo.info !14
  %14 = load double, double* %arrayidx107, align 8, !taffo.initweight !31, !taffo.info !14
  %mul108 = fmul double %call105, %14, !taffo.initweight !33, !taffo.info !70
  %idxprom109 = sext i32 %i.3 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx110 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom109, !taffo.initweight !50, !taffo.info !9
  %idxprom111 = sext i32 %j.3 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx112 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx110, i64 0, i64 %idxprom111, !taffo.initweight !31, !taffo.info !9
  %15 = load double, double* %arrayidx112, align 8, !taffo.initweight !33, !taffo.info !9
  %div113 = fdiv double %15, %mul108, !taffo.initweight !37, !taffo.info !72
  store double %div113, double* %arrayidx112, align 8, !taffo.initweight !33, !taffo.info !9
  br label %for.inc114

for.inc114:                                       ; preds = %for.body97
  %inc115 = add nsw i32 %j.3, 1, !taffo.initweight !31, !taffo.info !36, !taffo.constinfo !25
  br label %for.cond94

for.end116:                                       ; preds = %for.cond94
  br label %for.inc117

for.inc117:                                       ; preds = %for.end116
  %inc118 = add nsw i32 %i.3, 1, !taffo.initweight !31, !taffo.info !32, !taffo.constinfo !25
  br label %for.cond90

for.end119:                                       ; preds = %for.cond90
  br label %for.cond120

for.cond120:                                      ; preds = %for.inc169, %for.end119
  %i.4 = phi i32 [ 0, %for.end119 ], [ %inc170, %for.inc169 ], !taffo.info !29
  %cmp121 = icmp slt i32 %i.4, 31, !taffo.initweight !31, !taffo.info !32
  br i1 %cmp121, label %for.body123, label %for.end171, !taffo.initweight !33, !taffo.info !32

for.body123:                                      ; preds = %for.cond120
  %idxprom124 = sext i32 %i.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx125 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* @corr, i64 0, i64 %idxprom124, !taffo.initweight !50, !taffo.info !17
  %idxprom126 = sext i32 %i.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx127 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx125, i64 0, i64 %idxprom126, !taffo.initweight !31, !taffo.info !17
  store double 1.000000e+00, double* %arrayidx127, align 8, !taffo.initweight !33, !taffo.info !17, !taffo.constinfo !74
  %add128 = add nsw i32 %i.4, 1, !taffo.initweight !31, !taffo.info !32, !taffo.constinfo !25
  br label %for.cond129

for.cond129:                                      ; preds = %for.inc166, %for.body123
  %j.4 = phi i32 [ %add128, %for.body123 ], [ %inc167, %for.inc166 ], !taffo.info !29
  %cmp130 = icmp slt i32 %j.4, 32, !taffo.initweight !31, !taffo.info !36
  br i1 %cmp130, label %for.body132, label %for.end168, !taffo.initweight !33, !taffo.info !36

for.body132:                                      ; preds = %for.cond129
  %idxprom133 = sext i32 %i.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx134 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* @corr, i64 0, i64 %idxprom133, !taffo.initweight !50, !taffo.info !17
  %idxprom135 = sext i32 %j.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx136 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx134, i64 0, i64 %idxprom135, !taffo.initweight !31, !taffo.info !17
  store double 0.000000e+00, double* %arrayidx136, align 8, !taffo.initweight !33, !taffo.info !17, !taffo.constinfo !51
  br label %for.cond137

for.cond137:                                      ; preds = %for.inc155, %for.body132
  %k.0 = phi i32 [ 0, %for.body132 ], [ %inc156, %for.inc155 ], !taffo.info !34
  %cmp138 = icmp slt i32 %k.0, 28, !taffo.initweight !31, !taffo.info !36
  br i1 %cmp138, label %for.body140, label %for.end157, !taffo.initweight !33, !taffo.info !36

for.body140:                                      ; preds = %for.cond137
  %idxprom141 = sext i32 %k.0 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx142 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom141, !taffo.initweight !50, !taffo.info !9
  %idxprom143 = sext i32 %i.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx144 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx142, i64 0, i64 %idxprom143, !taffo.initweight !31, !taffo.info !9
  %16 = load double, double* %arrayidx144, align 8, !taffo.initweight !33, !taffo.info !9
  %idxprom145 = sext i32 %k.0 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx146 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* @data, i64 0, i64 %idxprom145, !taffo.initweight !50, !taffo.info !9
  %idxprom147 = sext i32 %j.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx148 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx146, i64 0, i64 %idxprom147, !taffo.initweight !31, !taffo.info !9
  %17 = load double, double* %arrayidx148, align 8, !taffo.initweight !33, !taffo.info !9
  %mul149 = fmul double %16, %17, !taffo.initweight !37, !taffo.info !77
  %idxprom150 = sext i32 %i.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx151 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* @corr, i64 0, i64 %idxprom150, !taffo.initweight !50, !taffo.info !17
  %idxprom152 = sext i32 %j.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx153 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx151, i64 0, i64 %idxprom152, !taffo.initweight !31, !taffo.info !17
  %18 = load double, double* %arrayidx153, align 8, !taffo.initweight !33, !taffo.info !17
  %add154 = fadd double %18, %mul149, !taffo.initweight !37, !taffo.info !79
  store double %add154, double* %arrayidx153, align 8, !taffo.initweight !33, !taffo.info !17
  br label %for.inc155

for.inc155:                                       ; preds = %for.body140
  %inc156 = add nsw i32 %k.0, 1, !taffo.initweight !31, !taffo.info !36, !taffo.constinfo !25
  br label %for.cond137

for.end157:                                       ; preds = %for.cond137
  %idxprom158 = sext i32 %i.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx159 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* @corr, i64 0, i64 %idxprom158, !taffo.initweight !50, !taffo.info !17
  %idxprom160 = sext i32 %j.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx161 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx159, i64 0, i64 %idxprom160, !taffo.initweight !31, !taffo.info !17
  %19 = load double, double* %arrayidx161, align 8, !taffo.initweight !33, !taffo.info !17
  %idxprom162 = sext i32 %j.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx163 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* @corr, i64 0, i64 %idxprom162, !taffo.initweight !50, !taffo.info !17
  %idxprom164 = sext i32 %i.4 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx165 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx163, i64 0, i64 %idxprom164, !taffo.initweight !31, !taffo.info !17
  store double %19, double* %arrayidx165, align 8, !taffo.initweight !33, !taffo.info !17
  br label %for.inc166

for.inc166:                                       ; preds = %for.end157
  %inc167 = add nsw i32 %j.4, 1, !taffo.initweight !31, !taffo.info !36, !taffo.constinfo !25
  br label %for.cond129

for.end168:                                       ; preds = %for.cond129
  br label %for.inc169

for.inc169:                                       ; preds = %for.end168
  %inc170 = add nsw i32 %i.4, 1, !taffo.initweight !31, !taffo.info !32, !taffo.constinfo !25
  br label %for.cond120

for.end171:                                       ; preds = %for.cond120
  store double 1.000000e+00, double* getelementptr inbounds ([32 x [32 x double]], [32 x [32 x double]]* @corr, i64 0, i64 31, i64 31), align 8, !taffo.initweight !31, !taffo.info !17, !taffo.constinfo !74
  call void @TIMING_CPUCLOCK_TOGGLE(), !taffo.constinfo !24
  call void @TIMING_CPUCLOCK_PRINT(), !taffo.constinfo !24
  br label %for.cond172

for.cond172:                                      ; preds = %for.inc189, %for.end171
  %i.5 = phi i32 [ 0, %for.end171 ], [ %inc190, %for.inc189 ], !taffo.info !29
  %cmp173 = icmp slt i32 %i.5, 32, !taffo.initweight !31, !taffo.info !32
  br i1 %cmp173, label %for.body175, label %for.end191, !taffo.initweight !33, !taffo.info !32

for.body175:                                      ; preds = %for.cond172
  br label %for.cond176

for.cond176:                                      ; preds = %for.inc185, %for.body175
  %j.5 = phi i32 [ 0, %for.body175 ], [ %inc186, %for.inc185 ], !taffo.info !34
  %cmp177 = icmp slt i32 %j.5, 32, !taffo.initweight !31, !taffo.info !36
  br i1 %cmp177, label %for.body179, label %for.end187, !taffo.initweight !33, !taffo.info !36

for.body179:                                      ; preds = %for.cond176
  %idxprom180 = sext i32 %i.5 to i64, !taffo.initweight !31, !taffo.info !32
  %arrayidx181 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* @corr, i64 0, i64 %idxprom180, !taffo.initweight !50, !taffo.info !17
  %idxprom182 = sext i32 %j.5 to i64, !taffo.initweight !31, !taffo.info !36
  %arrayidx183 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx181, i64 0, i64 %idxprom182, !taffo.initweight !31, !taffo.info !17
  %20 = load double, double* %arrayidx183, align 8, !taffo.initweight !33, !taffo.info !17
  %call184 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.6, i32 0, i32 0), double %20), !taffo.initweight !37, !taffo.info !17, !taffo.constinfo !81
  br label %for.inc185

for.inc185:                                       ; preds = %for.body179
  %inc186 = add nsw i32 %j.5, 1, !taffo.initweight !31, !taffo.info !36, !taffo.constinfo !25
  br label %for.cond176

for.end187:                                       ; preds = %for.cond176
  %call188 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.7, i32 0, i32 0)), !taffo.constinfo !25
  br label %for.inc189

for.inc189:                                       ; preds = %for.end187
  %inc190 = add nsw i32 %i.5, 1, !taffo.initweight !31, !taffo.info !32, !taffo.constinfo !25
  br label %for.cond172

for.end191:                                       ; preds = %for.cond172
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !82 !taffo.funinfo !83 void @llvm.var.annotation(i8*, i8*, i8*, i32) #3

; Function Attrs: nounwind
declare !taffo.initweight !84 !taffo.funinfo !85 dso_local double @sqrt(double) #1

declare !taffo.initweight !84 !taffo.funinfo !85 dso_local i32 @printf(i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!21}
!llvm.ident = !{!22}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 0.000000e+00}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.080000e+02}
!4 = !{i1 false, !5, i1 false, i2 0}
!5 = !{double 0.000000e+00, double 1.150000e+02}
!6 = !{i1 false, !7, i1 false, i2 0}
!7 = !{double 0.000000e+00, double 1.210000e+02}
!8 = !{i32 0}
!9 = !{i1 false, !10, !11, i2 -1}
!10 = !{double -1.000000e+01, double 1.000000e+01}
!11 = !{double 1.000000e-100}
!12 = !{i1 false, !13, !11, i2 -1}
!13 = !{double -5.000000e+04, double 5.000000e+04}
!14 = !{i1 false, !15, !16, i2 -1}
!15 = !{double -4.096000e+03, double 4.096000e+03}
!16 = !{double 1.000000e-01}
!17 = !{i1 false, !18, !11, i2 -1}
!18 = !{double 0.000000e+00, double 5.000000e+00}
!19 = !{i1 false, !20, i1 false, i2 0}
!20 = !{double 0.000000e+00, double 1.000000e+01}
!21 = !{i32 1, !"wchar_size", i32 4}
!22 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!23 = !{}
!24 = !{i1 false}
!25 = !{i1 false, i1 false}
!26 = !{i1 false, i1 false, i1 false, i1 false}
!27 = !{i32 -1, i32 -1}
!28 = !{i32 0, i1 false, i32 0, i1 false}
!29 = !{i1 false, !30, i1 false, i2 0}
!30 = !{double 0.000000e+00, double 2.800000e+01}
!31 = !{i32 2}
!32 = !{i1 false, !30, i1 false, i2 -1}
!33 = !{i32 3}
!34 = !{i1 false, !35, i1 false, i2 0}
!35 = !{double 0.000000e+00, double 3.200000e+01}
!36 = !{i1 false, !35, i1 false, i2 -1}
!37 = !{i32 4}
!38 = !{i1 false, !39, i1 false, i2 -1}
!39 = !{double 0.000000e+00, double 8.750000e-01}
!40 = !{i1 false, !41}
!41 = !{i1 false, !42, i1 false, i2 0}
!42 = !{double 3.200000e+01, double 3.200000e+01}
!43 = !{i1 false, !44, i1 false, i2 -1}
!44 = !{double 0.000000e+00, double 2.887500e+01}
!45 = !{i1 false, !46, i1 false, i2 -1}
!46 = !{double 0.000000e+00, double 1.031250e+00}
!47 = !{i1 false, !48}
!48 = !{i1 false, !49, i1 false, i2 0}
!49 = !{double 2.800000e+01, double 2.800000e+01}
!50 = !{i32 1}
!51 = !{!0, i1 false}
!52 = !{i1 false, !53, !11, i2 -1}
!53 = !{double -5.001000e+04, double 5.001000e+04}
!54 = !{i1 false, !55, !11, i2 1}
!55 = !{double 0xC09BE6DB6DB6DB6E, double 0x409BE6DB6DB6DB6E}
!56 = !{i1 false, !57, !11, i2 -1}
!57 = !{double 0xC1E2A24774800000, double 0x41E2A24774800000}
!58 = !{i1 false, !59, !16, i2 -1}
!59 = !{double 0xC1E2A24974800000, double 0x41E2A24974800000}
!60 = !{i1 false, !61, !11, i2 1}
!61 = !{double 0xC062492492492492, double 0x4062492492492492}
!62 = !{i1 false, !63, !16, i2 -1}
!63 = !{double 0.000000e+00, double 6.400000e+01}
!64 = !{i1 false, !65, i1 false, i2 1}
!65 = !{double 0.000000e+00, double 1.000000e+00}
!66 = !{i1 false, i1 false, i1 false, i2 1}
!67 = !{i1 false, !68, !11, i2 1}
!68 = !{double 0x40152A7FA9D2F8EA, double 0x40152A7FA9D2F8EA}
!69 = !{!48, i1 false}
!70 = !{i1 false, !71, !16, i2 -1}
!71 = !{double 0xC0D52A7FA9D2F8EA, double 0x40D52A7FA9D2F8EA}
!72 = !{i1 false, !73, !11, i2 -1}
!73 = !{double 0xBF3E3CB66051F5E0, double 0x3F3E3CB66051F5E0}
!74 = !{!75, i1 false}
!75 = !{i1 false, !76, i1 false, i2 0}
!76 = !{double 1.000000e+00, double 1.000000e+00}
!77 = !{i1 false, !78, !11, i2 -1}
!78 = !{double -1.000000e+02, double 1.000000e+02}
!79 = !{i1 false, !80, !11, i2 -1}
!80 = !{double -1.000000e+02, double 1.050000e+02}
!81 = !{i1 false, i1 false, i1 false}
!82 = !{i32 -1, i32 -1, i32 -1, i32 -1}
!83 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
!84 = !{i32 -1}
!85 = !{i32 0, i1 false}
