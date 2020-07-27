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
@stdout = external dso_local global %struct._IO_FILE*, align 8
@.str.6 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !4
@.str.7 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !2

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @gettime() #0 !taffo.initweight !8 !taffo.funinfo !8 {
entry:
  %call = call i32 (...) @clock(), !taffo.constinfo !9
  %conv = sext i32 %call to i64
  ret i64 %conv
}

declare !taffo.initweight !8 !taffo.funinfo !8 dso_local i32 @clock(...) #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_START() #0 !taffo.initweight !8 !taffo.funinfo !8 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !9
  store i64 %call, i64* @time_that_takes, align 8, !taffo.constinfo !10
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_TOGGLE() #0 !taffo.initweight !8 !taffo.funinfo !8 {
entry:
  %call = call i64 @gettime(), !taffo.constinfo !9
  %tmp = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %sub = sub i64 %call, %tmp
  store i64 %sub, i64* @time_that_takes, align 8, !taffo.constinfo !10
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i64 @TIMING_CPUCLOCK_S() #0 !taffo.initweight !8 !taffo.funinfo !8 {
entry:
  %tmp = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  ret i64 %tmp
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @TIMING_CPUCLOCK_PRINT() #0 !taffo.initweight !8 !taffo.funinfo !8 {
entry:
  %tmp = load %struct._IO_FILE*, %struct._IO_FILE** @stderr, align 8
  %tmp1 = load i64, i64* @time_that_takes, align 8, !taffo.info !0
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i64 %tmp1), !taffo.constinfo !11
  ret void
}

declare !taffo.initweight !12 !taffo.funinfo !13 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #1

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main(i32 %argc, i8** %argv) #0 !taffo.initweight !12 !taffo.funinfo !13 {
entry:
  %data.s15_17fixp = alloca [100 x [80 x i32]], align 16, !taffo.info !14
  %cov.s31_33fixp = alloca [100 x [80 x i64]], align 16, !taffo.info !18
  %mean.s14_18fixp = alloca [80 x i32], align 16, !taffo.info !21
  call void @TIMING_CPUCLOCK_START(), !taffo.constinfo !9
  br label %for.cond

for.cond:                                         ; preds = %for.inc17, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc18, %for.inc17 ], !taffo.info !24
  %cmp = icmp slt i32 %i.0, 100, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp, label %for.body, label %for.end19, !taffo.info !26, !taffo.initweight !29

for.body:                                         ; preds = %for.cond
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !24
  %cmp10 = icmp slt i32 %j.0, 80, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp10, label %for.body12, label %for.end, !taffo.info !26, !taffo.initweight !29

for.body12:                                       ; preds = %for.cond9
  %conv13.u7_25fixp = shl i32 %i.0, 25, !taffo.info !30
  %conv14.u7_25fixp = shl i32 %j.0, 25, !taffo.info !30
  %0 = zext i32 %conv13.u7_25fixp to i64, !taffo.info !30
  %1 = zext i32 %conv14.u7_25fixp to i64, !taffo.info !30
  %2 = mul i64 %0, %1, !taffo.info !32
  %3 = lshr i64 %2, 32, !taffo.info !32
  %mul.u14_18fixp = trunc i64 %3 to i32, !taffo.info !35
  %4 = zext i32 %mul.u14_18fixp to i64, !taffo.info !35
  %5 = udiv i64 %4, 80, !taffo.info !37, !taffo.constinfo !40
  %6 = shl i64 %5, 7, !taffo.info !37, !taffo.constinfo !40
  %div.u7_25fixp = trunc i64 %6 to i32, !taffo.info !44
  %idxprom = sext i32 %i.0 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom, !taffo.info !14
  %idxprom15 = sext i32 %j.0 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx16.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx.s15_17fixp, i64 0, i64 %idxprom15, !taffo.info !14
  %7 = lshr i32 %div.u7_25fixp, 8, !taffo.info !44
  store i32 %7, i32* %arrayidx16.s15_17fixp, align 8, !taffo.info !46
  br label %for.inc

for.inc:                                          ; preds = %for.body12
  %inc = add nsw i32 %j.0, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc17

for.inc17:                                        ; preds = %for.end
  %inc18 = add nsw i32 %i.0, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond

for.end19:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc42, %for.end19
  %j.1 = phi i32 [ 0, %for.end19 ], [ %inc43, %for.inc42 ], !taffo.info !24
  %cmp21 = icmp slt i32 %j.1, 80, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp21, label %for.body23, label %for.end44, !taffo.info !26, !taffo.initweight !29

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx25.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom24, !taffo.info !21
  store i32 0, i32* %arrayidx25.s14_18fixp, align 8, !taffo.info !47, !taffo.constinfo !48
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc36, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc37, %for.inc36 ], !taffo.info !24
  %cmp27 = icmp slt i32 %i.1, 100, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp27, label %for.body29, label %for.end38, !taffo.info !26, !taffo.initweight !29

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx31.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom30, !taffo.info !14
  %idxprom32 = sext i32 %j.1 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx33.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx31.s15_17fixp, i64 0, i64 %idxprom32, !taffo.info !14
  %tmp.s15_17fixp = load i32, i32* %arrayidx33.s15_17fixp, align 8, !taffo.info !14
  %idxprom34 = sext i32 %j.1 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx35.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom34, !taffo.info !21
  %tmp1.s14_18fixp = load i32, i32* %arrayidx35.s14_18fixp, align 8, !taffo.info !49
  %8 = ashr i32 %tmp1.s14_18fixp, 1, !taffo.info !49
  %add.s15_17fixp = add i32 %8, %tmp.s15_17fixp, !taffo.info !50
  %9 = shl i32 %add.s15_17fixp, 1, !taffo.info !50
  store i32 %9, i32* %arrayidx35.s14_18fixp, align 8, !taffo.info !47
  br label %for.inc36

for.inc36:                                        ; preds = %for.body29
  %inc37 = add nsw i32 %i.1, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond26

for.end38:                                        ; preds = %for.cond26
  %idxprom39 = sext i32 %j.1 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx40.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom39, !taffo.info !21
  %tmp2.s14_18fixp = load i32, i32* %arrayidx40.s14_18fixp, align 8, !taffo.info !49
  %10 = sext i32 %tmp2.s14_18fixp to i64, !taffo.info !49
  %11 = sdiv i64 %10, 100, !taffo.info !52
  %12 = ashr i64 %11, 1, !taffo.info !52
  %div41.s15_17fixp = trunc i64 %12 to i32, !taffo.info !14
  %13 = shl i32 %div41.s15_17fixp, 1, !taffo.info !14
  store i32 %13, i32* %arrayidx40.s14_18fixp, align 8, !taffo.info !47
  br label %for.inc42

for.inc42:                                        ; preds = %for.end38
  %inc43 = add nsw i32 %j.1, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond20

for.end44:                                        ; preds = %for.cond20
  br label %for.cond45

for.cond45:                                       ; preds = %for.inc62, %for.end44
  %i.2 = phi i32 [ 0, %for.end44 ], [ %inc63, %for.inc62 ], !taffo.info !24
  %cmp46 = icmp slt i32 %i.2, 100, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp46, label %for.body48, label %for.end64, !taffo.info !26, !taffo.initweight !29

for.body48:                                       ; preds = %for.cond45
  br label %for.cond49

for.cond49:                                       ; preds = %for.inc59, %for.body48
  %j.2 = phi i32 [ 0, %for.body48 ], [ %inc60, %for.inc59 ], !taffo.info !24
  %cmp50 = icmp slt i32 %j.2, 80, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp50, label %for.body52, label %for.end61, !taffo.info !26, !taffo.initweight !29

for.body52:                                       ; preds = %for.cond49
  %idxprom53 = sext i32 %j.2 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx54.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom53, !taffo.info !21
  %tmp3.s14_18fixp = load i32, i32* %arrayidx54.s14_18fixp, align 8, !taffo.info !49
  %idxprom55 = sext i32 %i.2 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx56.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom55, !taffo.info !14
  %idxprom57 = sext i32 %j.2 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx58.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx56.s15_17fixp, i64 0, i64 %idxprom57, !taffo.info !14
  %tmp4.s15_17fixp = load i32, i32* %arrayidx58.s15_17fixp, align 8, !taffo.info !14
  %14 = ashr i32 %tmp3.s14_18fixp, 1, !taffo.info !49
  %sub.s15_17fixp = sub i32 %tmp4.s15_17fixp, %14, !taffo.info !50
  store i32 %sub.s15_17fixp, i32* %arrayidx58.s15_17fixp, align 8, !taffo.info !46
  br label %for.inc59

for.inc59:                                        ; preds = %for.body52
  %inc60 = add nsw i32 %j.2, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond49

for.end61:                                        ; preds = %for.cond49
  br label %for.inc62

for.inc62:                                        ; preds = %for.end61
  %inc63 = add nsw i32 %i.2, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond45

for.end64:                                        ; preds = %for.cond45
  br label %for.cond65

for.cond65:                                       ; preds = %for.inc114, %for.end64
  %i.3 = phi i32 [ 0, %for.end64 ], [ %inc115, %for.inc114 ], !taffo.info !24
  %cmp66 = icmp slt i32 %i.3, 80, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp66, label %for.body68, label %for.end116, !taffo.info !26, !taffo.initweight !29

for.body68:                                       ; preds = %for.cond65
  br label %for.cond69

for.cond69:                                       ; preds = %for.inc111, %for.body68
  %j.3 = phi i32 [ %i.3, %for.body68 ], [ %inc112, %for.inc111 ], !taffo.info !24
  %cmp70 = icmp slt i32 %j.3, 80, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp70, label %for.body72, label %for.end113, !taffo.info !26, !taffo.initweight !29

for.body72:                                       ; preds = %for.cond69
  %idxprom73 = sext i32 %i.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx74.s31_33fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s31_33fixp, i64 0, i64 %idxprom73, !taffo.info !18
  %idxprom75 = sext i32 %j.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx76.s31_33fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx74.s31_33fixp, i64 0, i64 %idxprom75, !taffo.info !18
  store i64 0, i64* %arrayidx76.s31_33fixp, align 8, !taffo.info !54, !taffo.constinfo !48
  br label %for.cond77

for.cond77:                                       ; preds = %for.inc95, %for.body72
  %k.0 = phi i32 [ 0, %for.body72 ], [ %inc96, %for.inc95 ], !taffo.info !24
  %cmp78 = icmp slt i32 %k.0, 100, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp78, label %for.body80, label %for.end97, !taffo.info !26, !taffo.initweight !29

for.body80:                                       ; preds = %for.cond77
  %idxprom81 = sext i32 %k.0 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx82.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom81, !taffo.info !14
  %idxprom83 = sext i32 %i.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx84.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx82.s15_17fixp, i64 0, i64 %idxprom83, !taffo.info !14
  %tmp5.s15_17fixp = load i32, i32* %arrayidx84.s15_17fixp, align 8, !taffo.info !14
  %idxprom85 = sext i32 %k.0 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx86.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom85, !taffo.info !14
  %idxprom87 = sext i32 %j.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx88.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx86.s15_17fixp, i64 0, i64 %idxprom87, !taffo.info !14
  %tmp6.s15_17fixp = load i32, i32* %arrayidx88.s15_17fixp, align 8, !taffo.info !14
  %15 = sext i32 %tmp5.s15_17fixp to i64, !taffo.info !14
  %16 = sext i32 %tmp6.s15_17fixp to i64, !taffo.info !14
  %17 = mul i64 %15, %16, !taffo.info !56
  %18 = ashr i64 %17, 30, !taffo.info !56
  %mul89.s28_4fixp = trunc i64 %18 to i32, !taffo.info !59
  %idxprom90 = sext i32 %i.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx91.s31_33fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s31_33fixp, i64 0, i64 %idxprom90, !taffo.info !18
  %idxprom92 = sext i32 %j.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx93.s31_33fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx91.s31_33fixp, i64 0, i64 %idxprom92, !taffo.info !18
  %tmp7.s31_33fixp = load i64, i64* %arrayidx93.s31_33fixp, align 8, !taffo.info !61
  %19 = sext i32 %mul89.s28_4fixp to i64, !taffo.info !59
  %20 = shl i64 %19, 29, !taffo.info !59
  %add94.s31_33fixp = add i64 %tmp7.s31_33fixp, %20, !taffo.info !18
  store i64 %add94.s31_33fixp, i64* %arrayidx93.s31_33fixp, align 8, !taffo.info !54
  br label %for.inc95

for.inc95:                                        ; preds = %for.body80
  %inc96 = add nsw i32 %k.0, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond77

for.end97:                                        ; preds = %for.cond77
  %idxprom98 = sext i32 %i.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx99.s31_33fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s31_33fixp, i64 0, i64 %idxprom98, !taffo.info !18
  %idxprom100 = sext i32 %j.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx101.s31_33fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx99.s31_33fixp, i64 0, i64 %idxprom100, !taffo.info !18
  %tmp8.s31_33fixp = load i64, i64* %arrayidx101.s31_33fixp, align 8, !taffo.info !18
  %21 = sext i64 %tmp8.s31_33fixp to i96, !taffo.info !18
  %22 = sdiv i96 %21, 99, !taffo.info !63, !taffo.constinfo !66
  %23 = ashr i96 %22, 26, !taffo.info !63, !taffo.constinfo !66
  %div102.s25_7fixp = trunc i96 %23 to i32, !taffo.info !69
  %24 = sext i32 %div102.s25_7fixp to i64, !taffo.info !69
  %25 = shl i64 %24, 26, !taffo.info !69
  store i64 %25, i64* %arrayidx101.s31_33fixp, align 8, !taffo.info !54
  %idxprom103 = sext i32 %i.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx104.s31_33fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s31_33fixp, i64 0, i64 %idxprom103, !taffo.info !18
  %idxprom105 = sext i32 %j.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx106.s31_33fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx104.s31_33fixp, i64 0, i64 %idxprom105, !taffo.info !18
  %tmp9.s31_33fixp = load i64, i64* %arrayidx106.s31_33fixp, align 8, !taffo.info !18
  %idxprom107 = sext i32 %j.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx108.s31_33fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s31_33fixp, i64 0, i64 %idxprom107, !taffo.info !18
  %idxprom109 = sext i32 %i.3 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx110.s31_33fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx108.s31_33fixp, i64 0, i64 %idxprom109, !taffo.info !18
  store i64 %tmp9.s31_33fixp, i64* %arrayidx110.s31_33fixp, align 8, !taffo.info !54
  br label %for.inc111

for.inc111:                                       ; preds = %for.end97
  %inc112 = add nsw i32 %j.3, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond69

for.end113:                                       ; preds = %for.cond69
  br label %for.inc114

for.inc114:                                       ; preds = %for.end113
  %inc115 = add nsw i32 %i.3, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond65

for.end116:                                       ; preds = %for.cond65
  br label %for.cond117

for.cond117:                                      ; preds = %for.inc137, %for.end116
  %i.4 = phi i32 [ 0, %for.end116 ], [ %inc138, %for.inc137 ], !taffo.info !24
  %cmp118 = icmp slt i32 %i.4, 80, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp118, label %for.body120, label %for.end139, !taffo.info !26, !taffo.initweight !29

for.body120:                                      ; preds = %for.cond117
  br label %for.cond121

for.cond121:                                      ; preds = %for.inc134, %for.body120
  %j.4 = phi i32 [ 0, %for.body120 ], [ %inc135, %for.inc134 ], !taffo.info !24
  %cmp122 = icmp slt i32 %j.4, 80, !taffo.info !26, !taffo.initweight !28
  br i1 %cmp122, label %for.body124, label %for.end136, !taffo.info !26, !taffo.initweight !29

for.body124:                                      ; preds = %for.cond121
  %mul125 = mul nsw i32 %i.4, 80, !taffo.info !45, !taffo.initweight !28, !taffo.constinfo !10
  %add126 = add nsw i32 %mul125, %j.4, !taffo.info !26, !taffo.initweight !28
  %rem = srem i32 %add126, 20, !taffo.info !71, !taffo.initweight !29, !taffo.constinfo !10
  %cmp127 = icmp eq i32 %rem, 0, !taffo.info !73, !taffo.initweight !75
  br i1 %cmp127, label %if.then, label %if.end, !taffo.info !26, !taffo.initweight !76

if.then:                                          ; preds = %for.body124
  %tmp10 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp10, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.6, i32 0, i32 0)), !taffo.constinfo !77
  br label %if.end

if.end:                                           ; preds = %for.body124, %if.then
  %tmp11 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %idxprom129 = sext i32 %i.4 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx130.s31_33fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s31_33fixp, i64 0, i64 %idxprom129, !taffo.info !18
  %idxprom131 = sext i32 %j.4 to i64, !taffo.info !45, !taffo.initweight !28
  %arrayidx132.s31_33fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx130.s31_33fixp, i64 0, i64 %idxprom131, !taffo.info !18
  %tmp12.s31_33fixp = load i64, i64* %arrayidx132.s31_33fixp, align 8, !taffo.info !18
  %26 = sitofp i64 %tmp12.s31_33fixp to double, !taffo.info !18
  %27 = fdiv double %26, 0x4200000000000000, !taffo.info !18
  %call133.flt = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp11, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.7, i32 0, i32 0), double %27), !taffo.info !78, !taffo.initweight !75, !taffo.constinfo !11
  br label %for.inc134

for.inc134:                                       ; preds = %if.end
  %inc135 = add nsw i32 %j.4, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond121

for.end136:                                       ; preds = %for.cond121
  br label %for.inc137

for.inc137:                                       ; preds = %for.end136
  %inc138 = add nsw i32 %i.4, 1, !taffo.info !26, !taffo.initweight !28, !taffo.constinfo !10
  br label %for.cond117

for.end139:                                       ; preds = %for.cond117
  call void @TIMING_CPUCLOCK_TOGGLE(), !taffo.constinfo !9
  call void @TIMING_CPUCLOCK_PRINT(), !taffo.constinfo !9
  ret i32 0
}

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!6}
!llvm.ident = !{!7}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 0.000000e+00}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.080000e+02}
!4 = !{i1 false, !5, i1 false, i2 0}
!5 = !{double 0.000000e+00, double 1.000000e+01}
!6 = !{i32 1, !"wchar_size", i32 4}
!7 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!8 = !{}
!9 = !{i1 false}
!10 = !{i1 false, i1 false}
!11 = !{i1 false, i1 false, i1 false, i1 false}
!12 = !{i32 -1, i32 -1}
!13 = !{i32 0, i1 false, i32 0, i1 false}
!14 = !{!15, !16, !17, i2 -1}
!15 = !{!"fixp", i32 -32, i32 17}
!16 = !{double -1.000000e+04, double 1.000000e+04}
!17 = !{double 1.000000e-100}
!18 = !{!19, !20, !17, i2 1}
!19 = !{!"fixp", i32 -64, i32 33}
!20 = !{double -9.000100e+08, double 9.001000e+08}
!21 = !{!22, !23, !17, i2 -1}
!22 = !{!"fixp", i32 -32, i32 18}
!23 = !{double -5.000000e+03, double 5.000000e+03}
!24 = !{i1 false, !25, i1 false, i2 0}
!25 = !{double 0.000000e+00, double 1.000000e+02}
!26 = !{i1 false, !27, i1 false, i2 -1}
!27 = !{double 1.000000e+00, double 1.000000e+02}
!28 = !{i32 2}
!29 = !{i32 3}
!30 = !{!31, !25, i1 false, i2 -1}
!31 = !{!"fixp", i32 32, i32 25}
!32 = !{!33, !34, i1 false, i2 -1}
!33 = !{!"fixp", i32 64, i32 50}
!34 = !{double 1.000000e+00, double 1.000000e+04}
!35 = !{!36, !34, i1 false, i2 -1}
!36 = !{!"fixp", i32 32, i32 18}
!37 = !{!38, !39, i1 false, i2 -1}
!38 = !{!"fixp", i32 64, i32 18}
!39 = !{double 1.250000e-02, double 1.250000e+02}
!40 = !{i1 false, !41}
!41 = !{!42, !43, i1 false, i2 0}
!42 = !{!"fixp", i32 32, i32 0}
!43 = !{double 8.000000e+01, double 8.000000e+01}
!44 = !{!31, !39, i1 false, i2 -1}
!45 = !{i1 false, !25, i1 false, i2 -1}
!46 = !{i1 false, !16, !17, i2 -1}
!47 = !{i1 false, !23, !17, i2 -1}
!48 = !{!0, i1 false}
!49 = !{!15, !23, !17, i2 -1}
!50 = !{!15, !51, !17, i2 -1}
!51 = !{double -1.500000e+04, double 1.500000e+04}
!52 = !{!53, !16, !17, i2 -1}
!53 = !{!"fixp", i32 -64, i32 18}
!54 = !{i1 false, !55, !17, i2 1}
!55 = !{double -1.000000e+04, double 1.000000e+05}
!56 = !{!57, !58, !17, i2 -1}
!57 = !{!"fixp", i32 -64, i32 34}
!58 = !{double -1.000000e+08, double 1.000000e+08}
!59 = !{!60, !58, !17, i2 -1}
!60 = !{!"fixp", i32 -32, i32 4}
!61 = !{!19, !62, !17, i2 1}
!62 = !{double -8.000100e+08, double 8.001000e+08}
!63 = !{!64, !65, !17, i2 1}
!64 = !{!"fixp", i32 -96, i32 33}
!65 = !{double 0xC16156F8433B7989, double 0x41615769E62433B8}
!66 = !{i1 false, !67}
!67 = !{!42, !68, i1 false, i2 0}
!68 = !{double 9.900000e+01, double 9.900000e+01}
!69 = !{!70, !65, !17, i2 1}
!70 = !{!"fixp", i32 -32, i32 7}
!71 = !{i1 false, !72, i1 false, i2 -1}
!72 = !{double 0.000000e+00, double 2.000000e+01}
!73 = !{i1 false, !74, i1 false, i2 -1}
!74 = !{double 0.000000e+00, double 1.000000e+00}
!75 = !{i32 4}
!76 = !{i32 5}
!77 = !{i1 false, i1 false, i1 false}
!78 = !{!19, i1 false, !17, i2 1}
