; ModuleID = 'polybench_edited/covariance/covariance.fixp.4.magiclangtmp.ll'
source_filename = "polybench_edited/covariance/covariance.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

@stdout = external dso_local global %struct._IO_FILE*, align 8
@.str.5 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !0
@.str.6 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !2

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main(i32 %argc, i8** %argv) #0 !taffo.initweight !6 !taffo.funinfo !7 {
entry:
  %data.s15_17fixp = alloca [100 x [80 x i32]], align 16, !taffo.info !8
  %cov.s30_34fixp = alloca [100 x [80 x i64]], align 16, !taffo.info !12
  %mean.s14_18fixp = alloca [80 x i32], align 16, !taffo.info !15
  br label %for.cond

for.cond:                                         ; preds = %for.inc17, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc18, %for.inc17 ], !taffo.info !18
  %cmp = icmp slt i32 %i.0, 100, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp, label %for.body, label %for.end19, !taffo.info !23, !taffo.initweight !25

for.body:                                         ; preds = %for.cond
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !26
  %cmp10 = icmp slt i32 %j.0, 80, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp10, label %for.body12, label %for.end, !taffo.info !23, !taffo.initweight !25

for.body12:                                       ; preds = %for.cond9
  %conv13 = sitofp i32 %i.0 to double, !taffo.info !28, !taffo.initweight !22
  %conv14 = sitofp i32 %j.0 to double, !taffo.info !18, !taffo.initweight !22
  %mul = fmul double %conv13, %conv14, !taffo.info !18, !taffo.initweight !25
  %div = fdiv double %mul, 8.000000e+01, !taffo.info !30, !taffo.initweight !32, !taffo.constinfo !33
  %0 = fmul double 1.310720e+05, %div, !taffo.info !30, !taffo.constinfo !33
  %1 = fptosi double %0 to i32, !taffo.info !30
  %idxprom = sext i32 %i.0 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom, !taffo.info !8
  %idxprom15 = sext i32 %j.0 to i64, !taffo.info !18, !taffo.initweight !22
  %arrayidx16.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx.s15_17fixp, i64 0, i64 %idxprom15, !taffo.info !8
  store i32 %1, i32* %arrayidx16.s15_17fixp, align 8, !taffo.info !36
  br label %for.inc

for.inc:                                          ; preds = %for.body12
  %inc = add nsw i32 %j.0, 1, !taffo.info !37, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc17

for.inc17:                                        ; preds = %for.end
  %inc18 = add nsw i32 %i.0, 1, !taffo.info !40, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond

for.end19:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc42, %for.end19
  %j.1 = phi i32 [ 0, %for.end19 ], [ %inc43, %for.inc42 ], !taffo.info !18
  %cmp21 = icmp slt i32 %j.1, 80, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp21, label %for.body23, label %for.end44, !taffo.info !23, !taffo.initweight !25

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx25.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom24, !taffo.info !15
  store i32 0, i32* %arrayidx25.s14_18fixp, align 8, !taffo.info !42, !taffo.constinfo !43
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc36, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc37, %for.inc36 ], !taffo.info !26
  %cmp27 = icmp slt i32 %i.1, 100, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp27, label %for.body29, label %for.end38, !taffo.info !23, !taffo.initweight !25

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.info !18, !taffo.initweight !22
  %arrayidx31.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom30, !taffo.info !8
  %idxprom32 = sext i32 %j.1 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx33.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx31.s15_17fixp, i64 0, i64 %idxprom32, !taffo.info !8
  %tmp.s15_17fixp = load i32, i32* %arrayidx33.s15_17fixp, align 8, !taffo.info !8
  %idxprom34 = sext i32 %j.1 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx35.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom34, !taffo.info !15
  %tmp1.s14_18fixp = load i32, i32* %arrayidx35.s14_18fixp, align 8, !taffo.info !46
  %2 = ashr i32 %tmp1.s14_18fixp, 1, !taffo.info !46
  %add.s15_17fixp = add i32 %2, %tmp.s15_17fixp, !taffo.info !47
  %3 = shl i32 %add.s15_17fixp, 1, !taffo.info !47
  store i32 %3, i32* %arrayidx35.s14_18fixp, align 8, !taffo.info !42
  br label %for.inc36

for.inc36:                                        ; preds = %for.body29
  %inc37 = add nsw i32 %i.1, 1, !taffo.info !37, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond26

for.end38:                                        ; preds = %for.cond26
  %idxprom39 = sext i32 %j.1 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx40.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom39, !taffo.info !15
  %tmp2.s14_18fixp = load i32, i32* %arrayidx40.s14_18fixp, align 8, !taffo.info !46
  %4 = sext i32 %tmp2.s14_18fixp to i64, !taffo.info !46
  %5 = sdiv i64 %4, 100, !taffo.info !49
  %6 = ashr i64 %5, 1, !taffo.info !49
  %div41.s15_17fixp = trunc i64 %6 to i32, !taffo.info !8
  %7 = shl i32 %div41.s15_17fixp, 1, !taffo.info !8
  store i32 %7, i32* %arrayidx40.s14_18fixp, align 8, !taffo.info !42
  br label %for.inc42

for.inc42:                                        ; preds = %for.end38
  %inc43 = add nsw i32 %j.1, 1, !taffo.info !40, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond20

for.end44:                                        ; preds = %for.cond20
  br label %for.cond45

for.cond45:                                       ; preds = %for.inc62, %for.end44
  %i.2 = phi i32 [ 0, %for.end44 ], [ %inc63, %for.inc62 ], !taffo.info !18
  %cmp46 = icmp slt i32 %i.2, 100, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp46, label %for.body48, label %for.end64, !taffo.info !23, !taffo.initweight !25

for.body48:                                       ; preds = %for.cond45
  br label %for.cond49

for.cond49:                                       ; preds = %for.inc59, %for.body48
  %j.2 = phi i32 [ 0, %for.body48 ], [ %inc60, %for.inc59 ], !taffo.info !26
  %cmp50 = icmp slt i32 %j.2, 80, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp50, label %for.body52, label %for.end61, !taffo.info !23, !taffo.initweight !25

for.body52:                                       ; preds = %for.cond49
  %idxprom53 = sext i32 %j.2 to i64, !taffo.info !18, !taffo.initweight !22
  %arrayidx54.s14_18fixp = getelementptr inbounds [80 x i32], [80 x i32]* %mean.s14_18fixp, i64 0, i64 %idxprom53, !taffo.info !15
  %tmp3.s14_18fixp = load i32, i32* %arrayidx54.s14_18fixp, align 8, !taffo.info !46
  %idxprom55 = sext i32 %i.2 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx56.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom55, !taffo.info !8
  %idxprom57 = sext i32 %j.2 to i64, !taffo.info !18, !taffo.initweight !22
  %arrayidx58.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx56.s15_17fixp, i64 0, i64 %idxprom57, !taffo.info !8
  %tmp4.s15_17fixp = load i32, i32* %arrayidx58.s15_17fixp, align 8, !taffo.info !8
  %8 = ashr i32 %tmp3.s14_18fixp, 1, !taffo.info !46
  %sub.s15_17fixp = sub i32 %tmp4.s15_17fixp, %8, !taffo.info !47
  store i32 %sub.s15_17fixp, i32* %arrayidx58.s15_17fixp, align 8, !taffo.info !36
  br label %for.inc59

for.inc59:                                        ; preds = %for.body52
  %inc60 = add nsw i32 %j.2, 1, !taffo.info !37, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond49

for.end61:                                        ; preds = %for.cond49
  br label %for.inc62

for.inc62:                                        ; preds = %for.end61
  %inc63 = add nsw i32 %i.2, 1, !taffo.info !40, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond45

for.end64:                                        ; preds = %for.cond45
  br label %for.cond65

for.cond65:                                       ; preds = %for.inc114, %for.end64
  %i.3 = phi i32 [ 0, %for.end64 ], [ %inc115, %for.inc114 ], !taffo.info !18
  %cmp66 = icmp slt i32 %i.3, 80, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp66, label %for.body68, label %for.end116, !taffo.info !23, !taffo.initweight !25

for.body68:                                       ; preds = %for.cond65
  br label %for.cond69

for.cond69:                                       ; preds = %for.inc111, %for.body68
  %j.3 = phi i32 [ %i.3, %for.body68 ], [ %inc112, %for.inc111 ], !taffo.info !18
  %cmp70 = icmp slt i32 %j.3, 80, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp70, label %for.body72, label %for.end113, !taffo.info !23, !taffo.initweight !25

for.body72:                                       ; preds = %for.cond69
  %idxprom73 = sext i32 %i.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx74.s30_34fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s30_34fixp, i64 0, i64 %idxprom73, !taffo.info !12
  %idxprom75 = sext i32 %j.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx76.s30_34fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx74.s30_34fixp, i64 0, i64 %idxprom75, !taffo.info !12
  store i64 0, i64* %arrayidx76.s30_34fixp, align 8, !taffo.info !51, !taffo.constinfo !43
  br label %for.cond77

for.cond77:                                       ; preds = %for.inc95, %for.body72
  %k.0 = phi i32 [ 0, %for.body72 ], [ %inc96, %for.inc95 ], !taffo.info !26
  %cmp78 = icmp slt i32 %k.0, 100, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp78, label %for.body80, label %for.end97, !taffo.info !23, !taffo.initweight !25

for.body80:                                       ; preds = %for.cond77
  %idxprom81 = sext i32 %k.0 to i64, !taffo.info !18, !taffo.initweight !22
  %arrayidx82.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom81, !taffo.info !8
  %idxprom83 = sext i32 %i.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx84.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx82.s15_17fixp, i64 0, i64 %idxprom83, !taffo.info !8
  %tmp5.s15_17fixp = load i32, i32* %arrayidx84.s15_17fixp, align 8, !taffo.info !8
  %idxprom85 = sext i32 %k.0 to i64, !taffo.info !18, !taffo.initweight !22
  %arrayidx86.s15_17fixp = getelementptr inbounds [100 x [80 x i32]], [100 x [80 x i32]]* %data.s15_17fixp, i64 0, i64 %idxprom85, !taffo.info !8
  %idxprom87 = sext i32 %j.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx88.s15_17fixp = getelementptr inbounds [80 x i32], [80 x i32]* %arrayidx86.s15_17fixp, i64 0, i64 %idxprom87, !taffo.info !8
  %tmp6.s15_17fixp = load i32, i32* %arrayidx88.s15_17fixp, align 8, !taffo.info !8
  %9 = sext i32 %tmp5.s15_17fixp to i64, !taffo.info !8
  %10 = sext i32 %tmp6.s15_17fixp to i64, !taffo.info !8
  %11 = mul i64 %9, %10, !taffo.info !53
  %12 = ashr i64 %11, 30, !taffo.info !53
  %mul89.s28_4fixp = trunc i64 %12 to i32, !taffo.info !55
  %idxprom90 = sext i32 %i.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx91.s30_34fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s30_34fixp, i64 0, i64 %idxprom90, !taffo.info !12
  %idxprom92 = sext i32 %j.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx93.s30_34fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx91.s30_34fixp, i64 0, i64 %idxprom92, !taffo.info !12
  %tmp7.s30_34fixp = load i64, i64* %arrayidx93.s30_34fixp, align 8, !taffo.info !57
  %13 = sext i32 %mul89.s28_4fixp to i64, !taffo.info !55
  %14 = shl i64 %13, 30, !taffo.info !55
  %add94.s30_34fixp = add i64 %tmp7.s30_34fixp, %14, !taffo.info !12
  store i64 %add94.s30_34fixp, i64* %arrayidx93.s30_34fixp, align 8, !taffo.info !51
  br label %for.inc95

for.inc95:                                        ; preds = %for.body80
  %inc96 = add nsw i32 %k.0, 1, !taffo.info !37, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond77

for.end97:                                        ; preds = %for.cond77
  %idxprom98 = sext i32 %i.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx99.s30_34fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s30_34fixp, i64 0, i64 %idxprom98, !taffo.info !12
  %idxprom100 = sext i32 %j.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx101.s30_34fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx99.s30_34fixp, i64 0, i64 %idxprom100, !taffo.info !12
  %tmp8.s30_34fixp = load i64, i64* %arrayidx101.s30_34fixp, align 8, !taffo.info !12
  %15 = sext i64 %tmp8.s30_34fixp to i96, !taffo.info !12
  %16 = sdiv i96 %15, 99, !taffo.info !59, !taffo.constinfo !62
  %17 = ashr i96 %16, 25, !taffo.info !59, !taffo.constinfo !62
  %div102.s23_9fixp = trunc i96 %17 to i32, !taffo.info !66
  %18 = sext i32 %div102.s23_9fixp to i64, !taffo.info !66
  %19 = shl i64 %18, 25, !taffo.info !66
  store i64 %19, i64* %arrayidx101.s30_34fixp, align 8, !taffo.info !51
  %idxprom103 = sext i32 %i.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx104.s30_34fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s30_34fixp, i64 0, i64 %idxprom103, !taffo.info !12
  %idxprom105 = sext i32 %j.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx106.s30_34fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx104.s30_34fixp, i64 0, i64 %idxprom105, !taffo.info !12
  %tmp9.s30_34fixp = load i64, i64* %arrayidx106.s30_34fixp, align 8, !taffo.info !12
  %idxprom107 = sext i32 %j.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx108.s30_34fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s30_34fixp, i64 0, i64 %idxprom107, !taffo.info !12
  %idxprom109 = sext i32 %i.3 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx110.s30_34fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx108.s30_34fixp, i64 0, i64 %idxprom109, !taffo.info !12
  store i64 %tmp9.s30_34fixp, i64* %arrayidx110.s30_34fixp, align 8, !taffo.info !51
  br label %for.inc111

for.inc111:                                       ; preds = %for.end97
  %inc112 = add nsw i32 %j.3, 1, !taffo.info !40, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond69

for.end113:                                       ; preds = %for.cond69
  br label %for.inc114

for.inc114:                                       ; preds = %for.end113
  %inc115 = add nsw i32 %i.3, 1, !taffo.info !40, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond65

for.end116:                                       ; preds = %for.cond65
  br label %for.cond117

for.cond117:                                      ; preds = %for.inc137, %for.end116
  %i.4 = phi i32 [ 0, %for.end116 ], [ %inc138, %for.inc137 ], !taffo.info !18
  %cmp118 = icmp slt i32 %i.4, 80, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp118, label %for.body120, label %for.end139, !taffo.info !23, !taffo.initweight !25

for.body120:                                      ; preds = %for.cond117
  br label %for.cond121

for.cond121:                                      ; preds = %for.inc134, %for.body120
  %j.4 = phi i32 [ 0, %for.body120 ], [ %inc135, %for.inc134 ], !taffo.info !26
  %cmp122 = icmp slt i32 %j.4, 80, !taffo.info !20, !taffo.initweight !22
  br i1 %cmp122, label %for.body124, label %for.end136, !taffo.info !23, !taffo.initweight !25

for.body124:                                      ; preds = %for.cond121
  %mul125 = mul nsw i32 %i.4, 80, !taffo.info !68, !taffo.initweight !22, !taffo.constinfo !39
  %add126 = add nsw i32 %mul125, %j.4, !taffo.info !70, !taffo.initweight !22
  %rem = srem i32 %add126, 20, !taffo.info !72, !taffo.initweight !25, !taffo.constinfo !39
  %cmp127 = icmp eq i32 %rem, 0, !taffo.info !28, !taffo.initweight !32
  br i1 %cmp127, label %if.then, label %if.end, !taffo.info !23, !taffo.initweight !74

if.then:                                          ; preds = %for.body124
  %tmp10 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp10, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.5, i32 0, i32 0)), !taffo.constinfo !75
  br label %if.end

if.end:                                           ; preds = %if.then, %for.body124
  %tmp11 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %idxprom129 = sext i32 %i.4 to i64, !taffo.info !28, !taffo.initweight !22
  %arrayidx130.s30_34fixp = getelementptr inbounds [100 x [80 x i64]], [100 x [80 x i64]]* %cov.s30_34fixp, i64 0, i64 %idxprom129, !taffo.info !12
  %idxprom131 = sext i32 %j.4 to i64, !taffo.info !18, !taffo.initweight !22
  %arrayidx132.s30_34fixp = getelementptr inbounds [80 x i64], [80 x i64]* %arrayidx130.s30_34fixp, i64 0, i64 %idxprom131, !taffo.info !12
  %tmp12.s30_34fixp = load i64, i64* %arrayidx132.s30_34fixp, align 8, !taffo.info !12
  %20 = sitofp i64 %tmp12.s30_34fixp to double, !taffo.info !12
  %21 = fdiv double %20, 0x4210000000000000, !taffo.info !12
  %call133.flt = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp11, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.6, i32 0, i32 0), double %21), !taffo.info !76, !taffo.initweight !32, !taffo.constinfo !77
  br label %for.inc134

for.inc134:                                       ; preds = %if.end
  %inc135 = add nsw i32 %j.4, 1, !taffo.info !37, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond121

for.end136:                                       ; preds = %for.cond121
  br label %for.inc137

for.inc137:                                       ; preds = %for.end136
  %inc138 = add nsw i32 %i.4, 1, !taffo.info !40, !taffo.initweight !22, !taffo.constinfo !39
  br label %for.cond117

for.end139:                                       ; preds = %for.cond117
  ret i32 0
}

declare !taffo.initweight !6 !taffo.funinfo !7 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #1

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!4}
!llvm.ident = !{!5}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 1.000000e+01}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.080000e+02}
!4 = !{i32 1, !"wchar_size", i32 4}
!5 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!6 = !{i32 -1, i32 -1}
!7 = !{i32 0, i1 false, i32 0, i1 false}
!8 = !{!9, !10, !11, i2 -1}
!9 = !{!"fixp", i32 -32, i32 17}
!10 = !{double -1.000000e+04, double 1.000000e+04}
!11 = !{double 1.000000e-100}
!12 = !{!13, !14, !11, i2 1}
!13 = !{!"fixp", i32 -64, i32 34}
!14 = !{double -4.000100e+08, double 4.001000e+08}
!15 = !{!16, !17, !11, i2 -1}
!16 = !{!"fixp", i32 -32, i32 18}
!17 = !{double -5.000000e+03, double 5.000000e+03}
!18 = !{i1 false, !19, i1 false, i2 0}
!19 = !{double 0.000000e+00, double 2.000000e+00}
!20 = !{i1 false, !21, i1 false, i2 0}
!21 = !{double 1.000000e+00, double 1.000000e+00}
!22 = !{i32 2}
!23 = !{i1 false, !24, i1 false, i2 0}
!24 = !{double 1.000000e+00, double 1.000000e+02}
!25 = !{i32 3}
!26 = !{i1 false, !27, i1 false, i2 0}
!27 = !{double 0.000000e+00, double 3.000000e+00}
!28 = !{i1 false, !29, i1 false, i2 0}
!29 = !{double 0.000000e+00, double 1.000000e+00}
!30 = !{i1 false, !31, i1 false, i2 0}
!31 = !{double 0.000000e+00, double 2.500000e-02}
!32 = !{i32 4}
!33 = !{i1 false, !34}
!34 = !{i1 false, !35, i1 false, i2 0}
!35 = !{double 8.000000e+01, double 8.000000e+01}
!36 = !{i1 false, !10, !11, i2 -1}
!37 = !{i1 false, !38, i1 false, i2 0}
!38 = !{double 1.000000e+00, double 3.000000e+00}
!39 = !{i1 false, i1 false}
!40 = !{i1 false, !41, i1 false, i2 0}
!41 = !{double 1.000000e+00, double 2.000000e+00}
!42 = !{i1 false, !17, !11, i2 -1}
!43 = !{!44, i1 false}
!44 = !{i1 false, !45, i1 false, i2 0}
!45 = !{double 0.000000e+00, double 0.000000e+00}
!46 = !{!9, !17, !11, i2 -1}
!47 = !{!9, !48, !11, i2 -1}
!48 = !{double -1.500000e+04, double 1.500000e+04}
!49 = !{!50, !10, !11, i2 -1}
!50 = !{!"fixp", i32 -64, i32 18}
!51 = !{i1 false, !52, !11, i2 1}
!52 = !{double -1.000000e+04, double 1.000000e+05}
!53 = !{!13, !54, !11, i2 -1}
!54 = !{double -1.000000e+08, double 1.000000e+08}
!55 = !{!56, !54, !11, i2 -1}
!56 = !{!"fixp", i32 -32, i32 4}
!57 = !{!13, !58, !11, i2 1}
!58 = !{double -3.000100e+08, double 3.001000e+08}
!59 = !{!60, !61, !11, i2 1}
!60 = !{!"fixp", i32 -96, i32 34}
!61 = !{double 0xC14ED39C8676F312, double 0x414ED5631219DBCC}
!62 = !{i1 false, !63}
!63 = !{!64, !65, i1 false, i2 0}
!64 = !{!"fixp", i32 32, i32 0}
!65 = !{double 9.900000e+01, double 9.900000e+01}
!66 = !{!67, !61, !11, i2 1}
!67 = !{!"fixp", i32 -32, i32 9}
!68 = !{i1 false, !69, i1 false, i2 0}
!69 = !{double 0.000000e+00, double 8.000000e+01}
!70 = !{i1 false, !71, i1 false, i2 0}
!71 = !{double 0.000000e+00, double 8.200000e+01}
!72 = !{i1 false, !73, i1 false, i2 0}
!73 = !{double -2.000000e+01, double 2.000000e+01}
!74 = !{i32 5}
!75 = !{i1 false, i1 false, i1 false}
!76 = !{!13, i1 false, !11, i2 1}
!77 = !{i1 false, i1 false, i1 false, i1 false}
