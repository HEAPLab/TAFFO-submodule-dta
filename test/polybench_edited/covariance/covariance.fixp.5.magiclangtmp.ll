; ModuleID = 'polybench_edited/covariance/covariance.fixp.4.magiclangtmp.ll'
source_filename = "polybench_edited/covariance/covariance.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

@time_that_takes = common dso_local global i64 0, align 8, !taffo.info !0
@stderr = external dso_local global %struct._IO_FILE*, align 8
@.str = private unnamed_addr constant [4 x i8] c"%ld\00", align 1, !taffo.info !2
@.str.2 = private unnamed_addr constant [41 x i8] c"polybench_edited/covariance/covariance.c\00", section "llvm.metadata", !taffo.info !4
@data = common dso_local global [32 x [28 x double]] zeroinitializer, align 16, !taffo.info !6, !taffo.initweight !10
@mean = common dso_local global [28 x double] zeroinitializer, align 16, !taffo.info !11, !taffo.initweight !10
@cov = common dso_local global [32 x [28 x double]] zeroinitializer, align 16, !taffo.info !6, !taffo.initweight !10
@stdout = external dso_local global %struct._IO_FILE*, align 8
@.str.4 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !14
@.str.5 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !2
@.str.6 = private unnamed_addr constant [53 x i8] c"scalar(range(-2097152, 2097151) final error(1e-100))\00", section "llvm.metadata", !taffo.info !16
@.str.7 = private unnamed_addr constant [22 x i8] c"scalar(error(1e-100))\00", section "llvm.metadata", !taffo.info !16
@llvm.global.annotations = appending global [3 x { i8*, i8*, i8*, i32 }] [{ i8*, i8*, i8*, i32 } { i8* bitcast ([32 x [28 x double]]* @data to i8*), i8* getelementptr inbounds ([53 x i8], [53 x i8]* @.str.6, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 11 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([32 x [28 x double]]* @cov to i8*), i8* getelementptr inbounds ([53 x i8], [53 x i8]* @.str.6, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 12 }, { i8*, i8*, i8*, i32 } { i8* bitcast ([28 x double]* @mean to i8*), i8* getelementptr inbounds ([22 x i8], [22 x i8]* @.str.7, i32 0, i32 0), i8* getelementptr inbounds ([41 x i8], [41 x i8]* @.str.2, i32 0, i32 0), i32 13 }], section "llvm.metadata"
@data.fixp = common global [32 x [28 x i32]] zeroinitializer, align 16, !taffo.info !6
@mean.fixp = common global [28 x i32] zeroinitializer, align 16, !taffo.info !11
@cov.fixp = common global [32 x [28 x i32]] zeroinitializer, align 16, !taffo.info !6

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @gettime() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %call = call i64 @clock() #3, !taffo.constinfo !21
  ret i64 %call
}

; Function Attrs: nounwind
declare !taffo.initweight !20 !taffo.funinfo !20 dso_local i64 @clock() #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_START() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !21
  store i64 %call, i64* @time_that_takes, align 8, !taffo.constinfo !22
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_TOGGLE() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !21
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
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i64 %tmp1), !taffo.constinfo !23
  ret void
}

declare !taffo.initweight !24 !taffo.funinfo !25 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #2

; Function Attrs: noinline nounwind uwtable
define dso_local void @TAFFO_DUMPCONFIG() #0 !taffo.initweight !20 !taffo.funinfo !20 {
entry:
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main(i32 %argc, i8** %argv) #0 !taffo.initweight !24 !taffo.funinfo !25 {
entry:
  call void @TAFFO_DUMPCONFIG(), !taffo.constinfo !21
  call void @TIMING_CPUCLOCK_START(), !taffo.constinfo !21
  br label %for.cond

for.cond:                                         ; preds = %for.inc14, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc15, %for.inc14 ], !taffo.info !26
  %cmp = icmp slt i32 %i.0, 32, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp, label %for.body, label %for.end16, !taffo.info !28, !taffo.initweight !31

for.body:                                         ; preds = %for.cond
  br label %for.cond6

for.cond6:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !26
  %cmp7 = icmp slt i32 %j.0, 28, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp7, label %for.body9, label %for.end, !taffo.info !28, !taffo.initweight !31

for.body9:                                        ; preds = %for.cond6
  %conv10.u7_25fixp = shl i32 %i.0, 25, !taffo.info !32
  %conv11.u7_25fixp = shl i32 %j.0, 25, !taffo.info !32
  %0 = zext i32 %conv10.u7_25fixp to i64, !taffo.info !32
  %1 = zext i32 %conv11.u7_25fixp to i64, !taffo.info !32
  %2 = mul i64 %0, %1, !taffo.info !34
  %3 = lshr i64 %2, 32, !taffo.info !34
  %mul.u14_18fixp = trunc i64 %3 to i32, !taffo.info !37
  %4 = zext i32 %mul.u14_18fixp to i64, !taffo.info !37
  %5 = udiv i64 %4, 28, !taffo.info !39, !taffo.constinfo !42
  %6 = shl i64 %5, 5, !taffo.info !39, !taffo.constinfo !42
  %div.u9_23fixp = trunc i64 %6 to i32, !taffo.info !46
  %idxprom = sext i32 %i.0 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @data.fixp, i64 0, i64 %idxprom, !taffo.info !6
  %idxprom12 = sext i32 %j.0 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx13.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx.s23_9fixp, i64 0, i64 %idxprom12, !taffo.info !6
  %7 = lshr i32 %div.u9_23fixp, 14, !taffo.info !46
  store i32 %7, i32* %arrayidx13.s23_9fixp, align 8, !taffo.info !49
  br label %for.inc

for.inc:                                          ; preds = %for.body9
  %inc = add nsw i32 %j.0, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond6

for.end:                                          ; preds = %for.cond6
  br label %for.inc14

for.inc14:                                        ; preds = %for.end
  %inc15 = add nsw i32 %i.0, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond

for.end16:                                        ; preds = %for.cond
  br label %for.cond17

for.cond17:                                       ; preds = %for.inc39, %for.end16
  %j.1 = phi i32 [ 0, %for.end16 ], [ %inc40, %for.inc39 ], !taffo.info !26
  %cmp18 = icmp slt i32 %j.1, 28, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp18, label %for.body20, label %for.end41, !taffo.info !28, !taffo.initweight !31

for.body20:                                       ; preds = %for.cond17
  %idxprom21 = sext i32 %j.1 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx22.s26_6fixp = getelementptr inbounds [28 x i32], [28 x i32]* @mean.fixp, i64 0, i64 %idxprom21, !taffo.info !11
  store i32 0, i32* %arrayidx22.s26_6fixp, align 8, !taffo.info !50, !taffo.constinfo !51
  br label %for.cond23

for.cond23:                                       ; preds = %for.inc33, %for.body20
  %i.1 = phi i32 [ 0, %for.body20 ], [ %inc34, %for.inc33 ], !taffo.info !26
  %cmp24 = icmp slt i32 %i.1, 32, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp24, label %for.body26, label %for.end35, !taffo.info !28, !taffo.initweight !31

for.body26:                                       ; preds = %for.cond23
  %idxprom27 = sext i32 %i.1 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx28.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @data.fixp, i64 0, i64 %idxprom27, !taffo.info !6
  %idxprom29 = sext i32 %j.1 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx30.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx28.s23_9fixp, i64 0, i64 %idxprom29, !taffo.info !6
  %tmp.s23_9fixp = load i32, i32* %arrayidx30.s23_9fixp, align 8, !taffo.info !6
  %idxprom31 = sext i32 %j.1 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx32.s26_6fixp = getelementptr inbounds [28 x i32], [28 x i32]* @mean.fixp, i64 0, i64 %idxprom31, !taffo.info !11
  %tmp1.s26_6fixp = load i32, i32* %arrayidx32.s26_6fixp, align 8, !taffo.info !52
  %8 = ashr i32 %tmp.s23_9fixp, 3, !taffo.info !6
  %add.s26_6fixp = add i32 %tmp1.s26_6fixp, %8, !taffo.info !11
  store i32 %add.s26_6fixp, i32* %arrayidx32.s26_6fixp, align 8, !taffo.info !50
  br label %for.inc33

for.inc33:                                        ; preds = %for.body26
  %inc34 = add nsw i32 %i.1, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond23

for.end35:                                        ; preds = %for.cond23
  %idxprom36 = sext i32 %j.1 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx37.s26_6fixp = getelementptr inbounds [28 x i32], [28 x i32]* @mean.fixp, i64 0, i64 %idxprom36, !taffo.info !11
  %tmp2.s26_6fixp = load i32, i32* %arrayidx37.s26_6fixp, align 8, !taffo.info !11
  %9 = sext i32 %tmp2.s26_6fixp to i64, !taffo.info !11
  %10 = shl i64 %9, 26, !taffo.info !11
  %11 = sdiv i64 %10, 2147483648, !taffo.info !54
  %12 = shl i64 %11, 7, !taffo.info !54
  %div38.s19_13fixp = trunc i64 %12 to i32, !taffo.info !57
  %13 = ashr i32 %div38.s19_13fixp, 7, !taffo.info !57
  store i32 %13, i32* %arrayidx37.s26_6fixp, align 8, !taffo.info !50
  br label %for.inc39

for.inc39:                                        ; preds = %for.end35
  %inc40 = add nsw i32 %j.1, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond17

for.end41:                                        ; preds = %for.cond17
  br label %for.cond42

for.cond42:                                       ; preds = %for.inc59, %for.end41
  %i.2 = phi i32 [ 0, %for.end41 ], [ %inc60, %for.inc59 ], !taffo.info !26
  %cmp43 = icmp slt i32 %i.2, 32, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp43, label %for.body45, label %for.end61, !taffo.info !28, !taffo.initweight !31

for.body45:                                       ; preds = %for.cond42
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc56, %for.body45
  %j.2 = phi i32 [ 0, %for.body45 ], [ %inc57, %for.inc56 ], !taffo.info !26
  %cmp47 = icmp slt i32 %j.2, 28, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp47, label %for.body49, label %for.end58, !taffo.info !28, !taffo.initweight !31

for.body49:                                       ; preds = %for.cond46
  %idxprom50 = sext i32 %j.2 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx51.s26_6fixp = getelementptr inbounds [28 x i32], [28 x i32]* @mean.fixp, i64 0, i64 %idxprom50, !taffo.info !11
  %tmp3.s26_6fixp = load i32, i32* %arrayidx51.s26_6fixp, align 8, !taffo.info !11
  %idxprom52 = sext i32 %i.2 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx53.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @data.fixp, i64 0, i64 %idxprom52, !taffo.info !6
  %idxprom54 = sext i32 %j.2 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx55.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx53.s23_9fixp, i64 0, i64 %idxprom54, !taffo.info !6
  %tmp4.s23_9fixp = load i32, i32* %arrayidx55.s23_9fixp, align 8, !taffo.info !6
  %14 = ashr i32 %tmp4.s23_9fixp, 3, !taffo.info !6
  %sub.s26_6fixp = sub i32 %14, %tmp3.s26_6fixp, !taffo.info !59
  %15 = shl i32 %sub.s26_6fixp, 3, !taffo.info !59
  store i32 %15, i32* %arrayidx55.s23_9fixp, align 8, !taffo.info !49
  br label %for.inc56

for.inc56:                                        ; preds = %for.body49
  %inc57 = add nsw i32 %j.2, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond46

for.end58:                                        ; preds = %for.cond46
  br label %for.inc59

for.inc59:                                        ; preds = %for.end58
  %inc60 = add nsw i32 %i.2, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond42

for.end61:                                        ; preds = %for.cond42
  br label %for.cond62

for.cond62:                                       ; preds = %for.inc111, %for.end61
  %i.3 = phi i32 [ 0, %for.end61 ], [ %inc112, %for.inc111 ], !taffo.info !26
  %cmp63 = icmp slt i32 %i.3, 28, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp63, label %for.body65, label %for.end113, !taffo.info !28, !taffo.initweight !31

for.body65:                                       ; preds = %for.cond62
  br label %for.cond66

for.cond66:                                       ; preds = %for.inc108, %for.body65
  %j.3 = phi i32 [ %i.3, %for.body65 ], [ %inc109, %for.inc108 ], !taffo.info !26
  %cmp67 = icmp slt i32 %j.3, 28, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp67, label %for.body69, label %for.end110, !taffo.info !28, !taffo.initweight !31

for.body69:                                       ; preds = %for.cond66
  %idxprom70 = sext i32 %i.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx71.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @cov.fixp, i64 0, i64 %idxprom70, !taffo.info !6
  %idxprom72 = sext i32 %j.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx73.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx71.s23_9fixp, i64 0, i64 %idxprom72, !taffo.info !6
  store i32 0, i32* %arrayidx73.s23_9fixp, align 8, !taffo.info !49, !taffo.constinfo !51
  br label %for.cond74

for.cond74:                                       ; preds = %for.inc92, %for.body69
  %k.0 = phi i32 [ 0, %for.body69 ], [ %inc93, %for.inc92 ], !taffo.info !26
  %cmp75 = icmp slt i32 %k.0, 32, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp75, label %for.body77, label %for.end94, !taffo.info !28, !taffo.initweight !31

for.body77:                                       ; preds = %for.cond74
  %idxprom78 = sext i32 %k.0 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx79.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @data.fixp, i64 0, i64 %idxprom78, !taffo.info !6
  %idxprom80 = sext i32 %i.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx81.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx79.s23_9fixp, i64 0, i64 %idxprom80, !taffo.info !6
  %tmp5.s23_9fixp = load i32, i32* %arrayidx81.s23_9fixp, align 8, !taffo.info !6
  %idxprom82 = sext i32 %k.0 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx83.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @data.fixp, i64 0, i64 %idxprom82, !taffo.info !6
  %idxprom84 = sext i32 %j.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx85.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx83.s23_9fixp, i64 0, i64 %idxprom84, !taffo.info !6
  %tmp6.s23_9fixp = load i32, i32* %arrayidx85.s23_9fixp, align 8, !taffo.info !6
  %16 = sext i32 %tmp5.s23_9fixp to i64, !taffo.info !6
  %17 = sext i32 %tmp6.s23_9fixp to i64, !taffo.info !6
  %18 = mul i64 %16, %17, !taffo.info !61
  %mul86.s44_20fixp = shl i64 %18, 2, !taffo.info !64
  %idxprom87 = sext i32 %i.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx88.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @cov.fixp, i64 0, i64 %idxprom87, !taffo.info !6
  %idxprom89 = sext i32 %j.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx90.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx88.s23_9fixp, i64 0, i64 %idxprom89, !taffo.info !6
  %tmp7.s23_9fixp = load i32, i32* %arrayidx90.s23_9fixp, align 8, !taffo.info !6
  %19 = sext i32 %tmp7.s23_9fixp to i64, !taffo.info !6
  %20 = shl i64 %19, 11, !taffo.info !6
  %add91.s44_20fixp = add i64 %20, %mul86.s44_20fixp, !taffo.info !66
  %21 = ashr i64 %add91.s44_20fixp, 11, !taffo.info !66
  %22 = trunc i64 %21 to i32, !taffo.info !66
  store i32 %22, i32* %arrayidx90.s23_9fixp, align 8, !taffo.info !49
  br label %for.inc92

for.inc92:                                        ; preds = %for.body77
  %inc93 = add nsw i32 %k.0, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond74

for.end94:                                        ; preds = %for.cond74
  %idxprom95 = sext i32 %i.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx96.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @cov.fixp, i64 0, i64 %idxprom95, !taffo.info !6
  %idxprom97 = sext i32 %j.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx98.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx96.s23_9fixp, i64 0, i64 %idxprom97, !taffo.info !6
  %tmp8.s23_9fixp = load i32, i32* %arrayidx98.s23_9fixp, align 8, !taffo.info !6
  %23 = sext i32 %tmp8.s23_9fixp to i64, !taffo.info !6
  %24 = sdiv i64 %23, 31, !taffo.info !68, !taffo.constinfo !71
  %25 = shl i64 %24, 5, !taffo.info !68, !taffo.constinfo !71
  %div99.s18_14fixp = trunc i64 %25 to i32, !taffo.info !74
  %26 = ashr i32 %div99.s18_14fixp, 5, !taffo.info !74
  store i32 %26, i32* %arrayidx98.s23_9fixp, align 8, !taffo.info !49
  %idxprom100 = sext i32 %i.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx101.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @cov.fixp, i64 0, i64 %idxprom100, !taffo.info !6
  %idxprom102 = sext i32 %j.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx103.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx101.s23_9fixp, i64 0, i64 %idxprom102, !taffo.info !6
  %tmp9.s23_9fixp = load i32, i32* %arrayidx103.s23_9fixp, align 8, !taffo.info !6
  %idxprom104 = sext i32 %j.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx105.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @cov.fixp, i64 0, i64 %idxprom104, !taffo.info !6
  %idxprom106 = sext i32 %i.3 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx107.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx105.s23_9fixp, i64 0, i64 %idxprom106, !taffo.info !6
  store i32 %tmp9.s23_9fixp, i32* %arrayidx107.s23_9fixp, align 8, !taffo.info !49
  br label %for.inc108

for.inc108:                                       ; preds = %for.end94
  %inc109 = add nsw i32 %j.3, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond66

for.end110:                                       ; preds = %for.cond66
  br label %for.inc111

for.inc111:                                       ; preds = %for.end110
  %inc112 = add nsw i32 %i.3, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond62

for.end113:                                       ; preds = %for.cond62
  call void @TIMING_CPUCLOCK_TOGGLE(), !taffo.constinfo !21
  call void @TIMING_CPUCLOCK_PRINT(), !taffo.constinfo !21
  br label %for.cond114

for.cond114:                                      ; preds = %for.inc134, %for.end113
  %i.4 = phi i32 [ 0, %for.end113 ], [ %inc135, %for.inc134 ], !taffo.info !26
  %cmp115 = icmp slt i32 %i.4, 28, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp115, label %for.body117, label %for.end136, !taffo.info !28, !taffo.initweight !31

for.body117:                                      ; preds = %for.cond114
  br label %for.cond118

for.cond118:                                      ; preds = %for.inc131, %for.body117
  %j.4 = phi i32 [ 0, %for.body117 ], [ %inc132, %for.inc131 ], !taffo.info !26
  %cmp119 = icmp slt i32 %j.4, 28, !taffo.info !28, !taffo.initweight !30
  br i1 %cmp119, label %for.body121, label %for.end133, !taffo.info !28, !taffo.initweight !31

for.body121:                                      ; preds = %for.cond118
  %mul122 = mul nsw i32 %i.4, 28, !taffo.info !48, !taffo.initweight !30, !taffo.constinfo !22
  %add123 = add nsw i32 %mul122, %j.4, !taffo.info !28, !taffo.initweight !30
  %rem = srem i32 %add123, 20, !taffo.info !76, !taffo.initweight !31, !taffo.constinfo !22
  %cmp124 = icmp eq i32 %rem, 0, !taffo.info !78, !taffo.initweight !80
  br i1 %cmp124, label %if.then, label %if.end, !taffo.info !28, !taffo.initweight !81

if.then:                                          ; preds = %for.body121
  %tmp10 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp10, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.4, i32 0, i32 0)), !taffo.constinfo !82
  br label %if.end

if.end:                                           ; preds = %for.body121, %if.then
  %tmp11 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %idxprom126 = sext i32 %i.4 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx127.s23_9fixp = getelementptr inbounds [32 x [28 x i32]], [32 x [28 x i32]]* @cov.fixp, i64 0, i64 %idxprom126, !taffo.info !6
  %idxprom128 = sext i32 %j.4 to i64, !taffo.info !48, !taffo.initweight !30
  %arrayidx129.s23_9fixp = getelementptr inbounds [28 x i32], [28 x i32]* %arrayidx127.s23_9fixp, i64 0, i64 %idxprom128, !taffo.info !6
  %tmp12.s23_9fixp = load i32, i32* %arrayidx129.s23_9fixp, align 8, !taffo.info !6
  %27 = sitofp i32 %tmp12.s23_9fixp to double, !taffo.info !6
  %28 = fdiv double %27, 5.120000e+02, !taffo.info !6
  %call130.flt = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp11, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.5, i32 0, i32 0), double %28), !taffo.info !83, !taffo.initweight !80, !taffo.constinfo !23
  br label %for.inc131

for.inc131:                                       ; preds = %if.end
  %inc132 = add nsw i32 %j.4, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
  br label %for.cond118

for.end133:                                       ; preds = %for.cond118
  br label %for.inc134

for.inc134:                                       ; preds = %for.end133
  %inc135 = add nsw i32 %i.4, 1, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !22
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
!21 = !{i1 false}
!22 = !{i1 false, i1 false}
!23 = !{i1 false, i1 false, i1 false, i1 false}
!24 = !{i32 -1, i32 -1}
!25 = !{i32 0, i1 false, i32 0, i1 false}
!26 = !{i1 false, !27, i1 false, i2 0}
!27 = !{double 0.000000e+00, double 1.000000e+02}
!28 = !{i1 false, !29, i1 false, i2 -1}
!29 = !{double 1.000000e+00, double 1.000000e+02}
!30 = !{i32 2}
!31 = !{i32 3}
!32 = !{!33, !27, i1 false, i2 -1}
!33 = !{!"fixp", i32 32, i32 25}
!34 = !{!35, !36, i1 false, i2 -1}
!35 = !{!"fixp", i32 64, i32 50}
!36 = !{double 1.000000e+00, double 1.000000e+04}
!37 = !{!38, !36, i1 false, i2 -1}
!38 = !{!"fixp", i32 32, i32 18}
!39 = !{!40, !41, i1 false, i2 -1}
!40 = !{!"fixp", i32 64, i32 18}
!41 = !{double 0x3FA2492492492492, double 0x4076524924924925}
!42 = !{i1 false, !43}
!43 = !{!44, !45, i1 false, i2 0}
!44 = !{!"fixp", i32 32, i32 0}
!45 = !{double 2.800000e+01, double 2.800000e+01}
!46 = !{!47, !41, i1 false, i2 -1}
!47 = !{!"fixp", i32 32, i32 23}
!48 = !{i1 false, !27, i1 false, i2 -1}
!49 = !{i1 false, !8, !9, i2 -1}
!50 = !{i1 false, i1 false, !9, i2 1}
!51 = !{!0, i1 false}
!52 = !{!12, !53, !9, i2 1}
!53 = !{double 0xC170000000000000, double 0x416FFFFF00000000}
!54 = !{!55, !56, !9, i2 -1}
!55 = !{!"fixp", i32 -64, i32 6}
!56 = !{double -1.966080e+05, double 0x4107FFFF40000000}
!57 = !{!58, !56, !9, i2 -1}
!58 = !{!"fixp", i32 -32, i32 13}
!59 = !{!12, !60, !9, i2 1}
!60 = !{double 0xC173FFFF70000000, double 0x4173FFFFF0000000}
!61 = !{!62, !63, !9, i2 -1}
!62 = !{!"fixp", i32 -64, i32 18}
!63 = !{double 0xC28FFFFF00000000, double 0x4290000000000000}
!64 = !{!65, !63, !9, i2 -1}
!65 = !{!"fixp", i32 -64, i32 20}
!66 = !{!65, !67, !9, i2 -1}
!67 = !{double 0xC290000000000000, double 0x429000007FFFFC00}
!68 = !{!69, !70, !9, i2 -1}
!69 = !{!"fixp", i32 -64, i32 9}
!70 = !{double 0xC0F0842108421084, double 0x40F0842084210842}
!71 = !{i1 false, !72}
!72 = !{!44, !73, i1 false, i2 0}
!73 = !{double 3.100000e+01, double 3.100000e+01}
!74 = !{!75, !70, !9, i2 -1}
!75 = !{!"fixp", i32 -32, i32 14}
!76 = !{i1 false, !77, i1 false, i2 -1}
!77 = !{double 0.000000e+00, double 2.000000e+01}
!78 = !{i1 false, !79, i1 false, i2 -1}
!79 = !{double 0.000000e+00, double 1.000000e+00}
!80 = !{i32 4}
!81 = !{i32 5}
!82 = !{i1 false, i1 false, i1 false}
!83 = !{!7, i1 false, !9, i2 -1}
