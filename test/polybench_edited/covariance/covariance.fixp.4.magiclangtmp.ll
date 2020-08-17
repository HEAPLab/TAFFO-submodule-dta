; ModuleID = 'polybench_edited/covariance/covariance.fixp.3.magiclangtmp.ll'
source_filename = "polybench_edited/covariance/covariance.c"
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
@.str.2 = private unnamed_addr constant [41 x i8] c"polybench_edited/covariance/covariance.c\00", section "llvm.metadata", !taffo.info !4
@data = common dso_local global [260 x [240 x double]] zeroinitializer, align 16, !taffo.info !6, !taffo.initweight !10
@mean = common dso_local global [240 x double] zeroinitializer, align 16, !taffo.info !11, !taffo.initweight !10
@cov = common dso_local global [260 x [240 x double]] zeroinitializer, align 16, !taffo.info !6, !taffo.initweight !10
@stdout = external dso_local global %struct._IO_FILE*, align 8
@.str.4 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !14
@.str.5 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !2
@.str.6 = private unnamed_addr constant [53 x i8] c"scalar(range(-2097152, 2097151) final error(1e-100))\00", section "llvm.metadata", !taffo.info !16
@.str.7 = private unnamed_addr constant [22 x i8] c"scalar(error(1e-100))\00", section "llvm.metadata", !taffo.info !16
@llvm.global.annotations = appending global [3 x { i8*, i8*, i8*, i32 }] [{ i8*, i8*, i8*, i32 } { i8* bitcast ([260 x [240 x double]]* @data to i8*), i8* getelementptr inbounds ([53 x i8], [53 x i8]* @.str.6, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 33 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([260 x [240 x double]]* @cov to i8*), i8* getelementptr inbounds ([53 x i8], [53 x i8]* @.str.6, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 34 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([240 x double]* @mean to i8*), i8* getelementptr inbounds ([22 x i8], [22 x i8]* @.str.7, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 35 }], section "llvm.metadata"

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @gettime() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %tmp = alloca %struct.timespec, align 8, !taffo.structinfo !20
  %call = call i32 @clock_gettime(i32 2, %struct.timespec* %tmp) #3, !taffo.constinfo !21
  %tv_sec = getelementptr inbounds %struct.timespec, %struct.timespec* %tmp, i32 0, i32 0
  %tmp1 = load i64, i64* %tv_sec, align 8
  %mul = mul nsw i64 %tmp1, 1000000, !taffo.constinfo !22
  %tv_nsec = getelementptr inbounds %struct.timespec, %struct.timespec* %tmp, i32 0, i32 1
  %tmp2 = load i64, i64* %tv_nsec, align 8
  %div = sdiv i64 %tmp2, 1000, !taffo.constinfo !22
  %add = add nsw i64 %mul, %div
  ret i64 %add
}

; Function Attrs: nounwind
declare !taffo.initweight !23 !taffo.funinfo !24 dso_local i32 @clock_gettime(i32, %struct.timespec*) #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_START() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !25
  store i64 %call, i64* @time_that_takes, align 8, !taffo.constinfo !22
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_TOGGLE() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !25
  %tmp = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %sub = sub i64 %call, %tmp
  store i64 %sub, i64* @time_that_takes, align 8, !taffo.constinfo !22
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @TIMING_CPUCLOCK_S() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %tmp = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  ret i64 %tmp
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_PRINT() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %tmp = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %tmp1 = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i64 %tmp1), !taffo.constinfo !26
  ret void
}

declare !taffo.initweight !23 !taffo.funinfo !24 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #2

; Function Attrs: noinline nounwind uwtable
define dso_local void @TAFFO_DUMPCONFIG() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main(i32 %argc, i8** %argv) #0 !taffo.initweight !23 !taffo.funinfo !24 {
entry:
  call void @TAFFO_DUMPCONFIG(), !taffo.constinfo !25
  call void @TIMING_CPUCLOCK_START(), !taffo.constinfo !25
  %conv = sitofp i32 260 to double, !taffo.info !27
  br label %for.cond

for.cond:                                         ; preds = %for.inc14, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc15, %for.inc14 ], !taffo.info !30
  %cmp = icmp slt i32 %i.0, 260, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp, label %for.body, label %for.end16, !taffo.info !32, !taffo.initweight !35

for.body:                                         ; preds = %for.cond
  br label %for.cond6

for.cond6:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !30
  %cmp7 = icmp slt i32 %j.0, 240, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp7, label %for.body9, label %for.end, !taffo.info !32, !taffo.initweight !35

for.body9:                                        ; preds = %for.cond6
  %conv10 = sitofp i32 %i.0 to double, !taffo.info !36, !taffo.initweight !34
  %conv11 = sitofp i32 %j.0 to double, !taffo.info !36, !taffo.initweight !34
  %mul = fmul double %conv10, %conv11, !taffo.info !37, !taffo.initweight !35
  %div = fdiv double %mul, 2.400000e+02, !taffo.info !40, !taffo.initweight !42, !taffo.constinfo !43
  %idxprom = sext i32 %i.0 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom, !taffo.info !6, !taffo.initweight !47
  %idxprom12 = sext i32 %j.0 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx13 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx, i64 0, i64 %idxprom12, !taffo.info !6, !taffo.initweight !34
  store double %div, double* %arrayidx13, align 8, !taffo.info !48, !taffo.initweight !35
  br label %for.inc

for.inc:                                          ; preds = %for.body9
  %inc = add nsw i32 %j.0, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond6

for.end:                                          ; preds = %for.cond6
  br label %for.inc14

for.inc14:                                        ; preds = %for.end
  %inc15 = add nsw i32 %i.0, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond

for.end16:                                        ; preds = %for.cond
  br label %for.cond17

for.cond17:                                       ; preds = %for.inc39, %for.end16
  %j.1 = phi i32 [ 0, %for.end16 ], [ %inc40, %for.inc39 ], !taffo.info !30
  %cmp18 = icmp slt i32 %j.1, 240, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp18, label %for.body20, label %for.end41, !taffo.info !32, !taffo.initweight !35

for.body20:                                       ; preds = %for.cond17
  %idxprom21 = sext i32 %j.1 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx22 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom21, !taffo.info !11, !taffo.initweight !47
  store double 0.000000e+00, double* %arrayidx22, align 8, !taffo.info !49, !taffo.initweight !34, !taffo.constinfo !50
  br label %for.cond23

for.cond23:                                       ; preds = %for.inc33, %for.body20
  %i.1 = phi i32 [ 0, %for.body20 ], [ %inc34, %for.inc33 ], !taffo.info !30
  %cmp24 = icmp slt i32 %i.1, 260, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp24, label %for.body26, label %for.end35, !taffo.info !32, !taffo.initweight !35

for.body26:                                       ; preds = %for.cond23
  %idxprom27 = sext i32 %i.1 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx28 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom27, !taffo.info !6, !taffo.initweight !47
  %idxprom29 = sext i32 %j.1 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx30 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx28, i64 0, i64 %idxprom29, !taffo.info !6, !taffo.initweight !34
  %tmp = load double, double* %arrayidx30, align 8, !taffo.info !6, !taffo.initweight !35
  %idxprom31 = sext i32 %j.1 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx32 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom31, !taffo.info !11, !taffo.initweight !47
  %tmp1 = load double, double* %arrayidx32, align 8, !taffo.info !51, !taffo.initweight !34
  %add = fadd double %tmp1, %tmp, !taffo.info !11, !taffo.initweight !35
  store double %add, double* %arrayidx32, align 8, !taffo.info !49, !taffo.initweight !34
  br label %for.inc33

for.inc33:                                        ; preds = %for.body26
  %inc34 = add nsw i32 %i.1, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond23

for.end35:                                        ; preds = %for.cond23
  %idxprom36 = sext i32 %j.1 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx37 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom36, !taffo.info !11, !taffo.initweight !47
  %tmp2 = load double, double* %arrayidx37, align 8, !taffo.info !11, !taffo.initweight !34
  %div38 = fdiv double %tmp2, %conv, !taffo.info !53, !taffo.initweight !34
  store double %div38, double* %arrayidx37, align 8, !taffo.info !49, !taffo.initweight !34
  br label %for.inc39

for.inc39:                                        ; preds = %for.end35
  %inc40 = add nsw i32 %j.1, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond17

for.end41:                                        ; preds = %for.cond17
  br label %for.cond42

for.cond42:                                       ; preds = %for.inc59, %for.end41
  %i.2 = phi i32 [ 0, %for.end41 ], [ %inc60, %for.inc59 ], !taffo.info !30
  %cmp43 = icmp slt i32 %i.2, 260, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp43, label %for.body45, label %for.end61, !taffo.info !32, !taffo.initweight !35

for.body45:                                       ; preds = %for.cond42
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc56, %for.body45
  %j.2 = phi i32 [ 0, %for.body45 ], [ %inc57, %for.inc56 ], !taffo.info !30
  %cmp47 = icmp slt i32 %j.2, 240, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp47, label %for.body49, label %for.end58, !taffo.info !32, !taffo.initweight !35

for.body49:                                       ; preds = %for.cond46
  %idxprom50 = sext i32 %j.2 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx51 = getelementptr inbounds [240 x double], [240 x double]* @mean, i64 0, i64 %idxprom50, !taffo.info !11, !taffo.initweight !47
  %tmp3 = load double, double* %arrayidx51, align 8, !taffo.info !11, !taffo.initweight !34
  %idxprom52 = sext i32 %i.2 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx53 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom52, !taffo.info !6, !taffo.initweight !47
  %idxprom54 = sext i32 %j.2 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx55 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx53, i64 0, i64 %idxprom54, !taffo.info !6, !taffo.initweight !34
  %tmp4 = load double, double* %arrayidx55, align 8, !taffo.info !6, !taffo.initweight !35
  %sub = fsub double %tmp4, %tmp3, !taffo.info !56, !taffo.initweight !35
  store double %sub, double* %arrayidx55, align 8, !taffo.info !48, !taffo.initweight !35
  br label %for.inc56

for.inc56:                                        ; preds = %for.body49
  %inc57 = add nsw i32 %j.2, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond46

for.end58:                                        ; preds = %for.cond46
  br label %for.inc59

for.inc59:                                        ; preds = %for.end58
  %inc60 = add nsw i32 %i.2, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond42

for.end61:                                        ; preds = %for.cond42
  br label %for.cond62

for.cond62:                                       ; preds = %for.inc111, %for.end61
  %i.3 = phi i32 [ 0, %for.end61 ], [ %inc112, %for.inc111 ], !taffo.info !30
  %cmp63 = icmp slt i32 %i.3, 240, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp63, label %for.body65, label %for.end113, !taffo.info !32, !taffo.initweight !35

for.body65:                                       ; preds = %for.cond62
  br label %for.cond66

for.cond66:                                       ; preds = %for.inc108, %for.body65
  %j.3 = phi i32 [ %i.3, %for.body65 ], [ %inc109, %for.inc108 ], !taffo.info !30
  %cmp67 = icmp slt i32 %j.3, 240, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp67, label %for.body69, label %for.end110, !taffo.info !32, !taffo.initweight !35

for.body69:                                       ; preds = %for.cond66
  %idxprom70 = sext i32 %i.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx71 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom70, !taffo.info !6, !taffo.initweight !47
  %idxprom72 = sext i32 %j.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx73 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx71, i64 0, i64 %idxprom72, !taffo.info !6, !taffo.initweight !34
  store double 0.000000e+00, double* %arrayidx73, align 8, !taffo.info !48, !taffo.initweight !35, !taffo.constinfo !50
  br label %for.cond74

for.cond74:                                       ; preds = %for.inc92, %for.body69
  %k.0 = phi i32 [ 0, %for.body69 ], [ %inc93, %for.inc92 ], !taffo.info !30
  %cmp75 = icmp slt i32 %k.0, 260, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp75, label %for.body77, label %for.end94, !taffo.info !32, !taffo.initweight !35

for.body77:                                       ; preds = %for.cond74
  %idxprom78 = sext i32 %k.0 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx79 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom78, !taffo.info !6, !taffo.initweight !47
  %idxprom80 = sext i32 %i.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx81 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx79, i64 0, i64 %idxprom80, !taffo.info !6, !taffo.initweight !34
  %tmp5 = load double, double* %arrayidx81, align 8, !taffo.info !6, !taffo.initweight !35
  %idxprom82 = sext i32 %k.0 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx83 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @data, i64 0, i64 %idxprom82, !taffo.info !6, !taffo.initweight !47
  %idxprom84 = sext i32 %j.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx85 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx83, i64 0, i64 %idxprom84, !taffo.info !6, !taffo.initweight !34
  %tmp6 = load double, double* %arrayidx85, align 8, !taffo.info !6, !taffo.initweight !35
  %mul86 = fmul double %tmp5, %tmp6, !taffo.info !58, !taffo.initweight !42
  %idxprom87 = sext i32 %i.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx88 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom87, !taffo.info !6, !taffo.initweight !47
  %idxprom89 = sext i32 %j.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx90 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx88, i64 0, i64 %idxprom89, !taffo.info !6, !taffo.initweight !34
  %tmp7 = load double, double* %arrayidx90, align 8, !taffo.info !6, !taffo.initweight !35
  %add91 = fadd double %tmp7, %mul86, !taffo.info !61, !taffo.initweight !42
  store double %add91, double* %arrayidx90, align 8, !taffo.info !48, !taffo.initweight !35
  br label %for.inc92

for.inc92:                                        ; preds = %for.body77
  %inc93 = add nsw i32 %k.0, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond74

for.end94:                                        ; preds = %for.cond74
  %idxprom95 = sext i32 %i.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx96 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom95, !taffo.info !6, !taffo.initweight !47
  %idxprom97 = sext i32 %j.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx98 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx96, i64 0, i64 %idxprom97, !taffo.info !6, !taffo.initweight !34
  %tmp8 = load double, double* %arrayidx98, align 8, !taffo.info !6, !taffo.initweight !35
  %div99 = fdiv double %tmp8, 2.590000e+02, !taffo.info !63, !taffo.initweight !42, !taffo.constinfo !66
  store double %div99, double* %arrayidx98, align 8, !taffo.info !48, !taffo.initweight !35
  %idxprom100 = sext i32 %i.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx101 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom100, !taffo.info !6, !taffo.initweight !47
  %idxprom102 = sext i32 %j.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx103 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx101, i64 0, i64 %idxprom102, !taffo.info !6, !taffo.initweight !34
  %tmp9 = load double, double* %arrayidx103, align 8, !taffo.info !6, !taffo.initweight !35
  %idxprom104 = sext i32 %j.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx105 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom104, !taffo.info !6, !taffo.initweight !47
  %idxprom106 = sext i32 %i.3 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx107 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx105, i64 0, i64 %idxprom106, !taffo.info !6, !taffo.initweight !34
  store double %tmp9, double* %arrayidx107, align 8, !taffo.info !48, !taffo.initweight !35
  br label %for.inc108

for.inc108:                                       ; preds = %for.end94
  %inc109 = add nsw i32 %j.3, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond66

for.end110:                                       ; preds = %for.cond66
  br label %for.inc111

for.inc111:                                       ; preds = %for.end110
  %inc112 = add nsw i32 %i.3, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond62

for.end113:                                       ; preds = %for.cond62
  call void @TIMING_CPUCLOCK_TOGGLE(), !taffo.constinfo !25
  call void @TIMING_CPUCLOCK_PRINT(), !taffo.constinfo !25
  br label %for.cond114

for.cond114:                                      ; preds = %for.inc134, %for.end113
  %i.4 = phi i32 [ 0, %for.end113 ], [ %inc135, %for.inc134 ], !taffo.info !30
  %cmp115 = icmp slt i32 %i.4, 240, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp115, label %for.body117, label %for.end136, !taffo.info !32, !taffo.initweight !35

for.body117:                                      ; preds = %for.cond114
  br label %for.cond118

for.cond118:                                      ; preds = %for.inc131, %for.body117
  %j.4 = phi i32 [ 0, %for.body117 ], [ %inc132, %for.inc131 ], !taffo.info !30
  %cmp119 = icmp slt i32 %j.4, 240, !taffo.info !32, !taffo.initweight !34
  br i1 %cmp119, label %for.body121, label %for.end133, !taffo.info !32, !taffo.initweight !35

for.body121:                                      ; preds = %for.cond118
  %mul122 = mul nsw i32 %i.4, 240, !taffo.info !46, !taffo.initweight !34, !taffo.constinfo !22
  %add123 = add nsw i32 %mul122, %j.4, !taffo.info !32, !taffo.initweight !34
  %rem = srem i32 %add123, 20, !taffo.info !69, !taffo.initweight !35, !taffo.constinfo !22
  %cmp124 = icmp eq i32 %rem, 0, !taffo.info !71, !taffo.initweight !42
  br i1 %cmp124, label %if.then, label %if.end, !taffo.info !32, !taffo.initweight !73

if.then:                                          ; preds = %for.body121
  %tmp10 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp10, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.4, i32 0, i32 0)), !taffo.constinfo !21
  br label %if.end

if.end:                                           ; preds = %if.then, %for.body121
  %tmp11 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %idxprom126 = sext i32 %i.4 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx127 = getelementptr inbounds [260 x [240 x double]], [260 x [240 x double]]* @cov, i64 0, i64 %idxprom126, !taffo.info !6, !taffo.initweight !47
  %idxprom128 = sext i32 %j.4 to i64, !taffo.info !46, !taffo.initweight !34
  %arrayidx129 = getelementptr inbounds [240 x double], [240 x double]* %arrayidx127, i64 0, i64 %idxprom128, !taffo.info !6, !taffo.initweight !34
  %tmp12 = load double, double* %arrayidx129, align 8, !taffo.info !6, !taffo.initweight !35
  %call130 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp11, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.5, i32 0, i32 0), double %tmp12), !taffo.info !74, !taffo.initweight !42, !taffo.constinfo !26
  br label %for.inc131

for.inc131:                                       ; preds = %if.end
  %inc132 = add nsw i32 %j.4, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond118

for.end133:                                       ; preds = %for.cond118
  br label %for.inc134

for.inc134:                                       ; preds = %for.end133
  %inc135 = add nsw i32 %i.4, 1, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !22
  br label %for.cond114

for.end136:                                       ; preds = %for.cond114
  ret i32 0
}

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!18}
!llvm.ident = !{!19}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 0.000000e+00}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.080000e+02}
!4 = !{i1 false, !5, i1 false, i2 0}
!5 = !{double 0.000000e+00, double 1.210000e+02}
!6 = !{!7, !8, !9, i2 -1}
!7 = !{!"fixp", i32 -32, i32 9}
!8 = !{double 0xC140000000000000, double 0x413FFFFF00000000}
!9 = !{double 1.000000e-100}
!10 = !{i32 0}
!11 = !{!12, !13, !9, i2 1}
!12 = !{!"fixp", i32 -32, i32 6}
!13 = !{double 0xC172000000000000, double 0x4171FFFF70000000}
!14 = !{i1 false, !15, i1 false, i2 0}
!15 = !{double 0.000000e+00, double 1.000000e+01}
!16 = !{i1 false, !17, i1 false, i2 0}
!17 = !{double 0.000000e+00, double 1.150000e+02}
!18 = !{i32 1, !"wchar_size", i32 4}
!19 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!20 = !{}
!21 = !{i1 false, i1 false, i1 false}
!22 = !{i1 false, i1 false}
!23 = !{i32 -1, i32 -1}
!24 = !{i32 0, i1 false, i32 0, i1 false}
!25 = !{i1 false}
!26 = !{i1 false, i1 false, i1 false, i1 false}
!27 = !{!28, !29, i1 false, i2 1}
!28 = !{!"fixp", i32 32, i32 23}
!29 = !{double 2.600000e+02, double 2.600000e+02}
!30 = !{i1 false, !31, i1 false, i2 0}
!31 = !{double 0.000000e+00, double 2.600000e+02}
!32 = !{i1 false, !33, i1 false, i2 -1}
!33 = !{double 1.000000e+00, double 2.600000e+02}
!34 = !{i32 2}
!35 = !{i32 3}
!36 = !{!28, !31, i1 false, i2 -1}
!37 = !{!38, !39, i1 false, i2 -1}
!38 = !{!"fixp", i32 32, i32 15}
!39 = !{double 1.000000e+00, double 6.760000e+04}
!40 = !{!28, !41, i1 false, i2 -1}
!41 = !{double 0x3F71111111111111, double 0x40719AAAAAAAAAAB}
!42 = !{i32 4}
!43 = !{i1 false, !44}
!44 = !{i1 false, !45, i1 false, i2 0}
!45 = !{double 2.400000e+02, double 2.400000e+02}
!46 = !{i1 false, !31, i1 false, i2 -1}
!47 = !{i32 1}
!48 = !{i1 false, !8, !9, i2 -1}
!49 = !{i1 false, i1 false, !9, i2 1}
!50 = !{!0, i1 false}
!51 = !{!12, !52, !9, i2 1}
!52 = !{double 0xC170000000000000, double 0x416FFFFF00000000}
!53 = !{!54, !55, !9, i2 -1}
!54 = !{!"fixp", i32 -32, i32 16}
!55 = !{double 0xC0D7A17A17A17A18, double 0x40D7A1795A95A95B}
!56 = !{!12, !57, !9, i2 1}
!57 = !{double 0xC173FFFF70000000, double 0x4173FFFFF0000000}
!58 = !{!59, !60, !9, i2 -1}
!59 = !{!"fixp", i32 -64, i32 20}
!60 = !{double 0xC28FFFFF00000000, double 0x4290000000000000}
!61 = !{!59, !62, !9, i2 -1}
!62 = !{double 0xC290000000000000, double 0x429000007FFFFC00}
!63 = !{!64, !65, !9, i2 -1}
!64 = !{!"fixp", i32 -32, i32 18}
!65 = !{double 0xC0BFA11CAA01FA12, double 0x40BFA11BACF914C2}
!66 = !{i1 false, !67}
!67 = !{i1 false, !68, i1 false, i2 0}
!68 = !{double 2.590000e+02, double 2.590000e+02}
!69 = !{i1 false, !70, i1 false, i2 -1}
!70 = !{double 0.000000e+00, double 2.000000e+01}
!71 = !{i1 false, !72, i1 false, i2 -1}
!72 = !{double 0.000000e+00, double 1.000000e+00}
!73 = !{i32 5}
!74 = !{!7, i1 false, !9, i2 -1}
