; ModuleID = 'polybench_edited/corr/corr.fixp.2.magiclangtmp.ll'
source_filename = "polybench_edited/corr/corr.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [49 x i8] c"scalar(range(-50000, 50000) final error(1e-100))\00", section "llvm.metadata", !taffo.info !0
@.str.1 = private unnamed_addr constant [29 x i8] c"polybench_edited/corr/corr.c\00", section "llvm.metadata", !taffo.info !2
@.str.2 = private unnamed_addr constant [43 x i8] c"scalar(range(-10, 10) error(1e-100) final)\00", section "llvm.metadata", !taffo.info !0
@.str.3 = private unnamed_addr constant [40 x i8] c"scalar(range(0, 5) error(1e-100) final)\00", section "llvm.metadata", !taffo.info !0
@.str.4 = private unnamed_addr constant [46 x i8] c"scalar(range(-4096,4096) error(1e-100) final)\00", section "llvm.metadata", !taffo.info !0
@.str.5 = private unnamed_addr constant [36 x i8] c"scalar(range(0, 28) final disabled)\00", section "llvm.metadata", !taffo.info !0
@.str.6 = private unnamed_addr constant [36 x i8] c"scalar(range(0, 32) final disabled)\00", section "llvm.metadata", !taffo.info !0
@.str.7 = private unnamed_addr constant [37 x i8] c"scalar(range(1, 3000) error(1e-100))\00", section "llvm.metadata", !taffo.info !0
@.str.8 = private unnamed_addr constant [9 x i8] c"scalar()\00", section "llvm.metadata", !taffo.info !0
@.str.9 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !4
@.str.10 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !6

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !10 !taffo.funinfo !10 {
entry:
  %mean = alloca [32 x double], align 16, !taffo.initweight !11, !taffo.info !12
  %data = alloca [28 x [32 x double]], align 16, !taffo.initweight !11, !taffo.info !15
  %corr = alloca [32 x [32 x double]], align 16, !taffo.initweight !11, !taffo.info !17
  %stddev = alloca [32 x double], align 16, !taffo.initweight !11, !taffo.info !19
  %mean1 = bitcast [32 x double]* %mean to i8*, !taffo.initweight !21, !taffo.info !12
  %data2 = bitcast [28 x [32 x double]]* %data to i8*, !taffo.initweight !21, !taffo.info !15
  %corr3 = bitcast [32 x [32 x double]]* %corr to i8*, !taffo.initweight !21, !taffo.info !17
  %stddev4 = bitcast [32 x double]* %stddev to i8*, !taffo.initweight !21, !taffo.info !19
  br label %for.cond

for.cond:                                         ; preds = %for.inc16, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc17, %for.inc16 ], !taffo.info !22
  %cmp = icmp slt i32 %i.0, 28, !taffo.initweight !24, !taffo.info !25
  br i1 %cmp, label %for.body, label %for.end18, !taffo.initweight !26, !taffo.info !25

for.body:                                         ; preds = %for.cond
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !27
  %cmp10 = icmp slt i32 %j.0, 32, !taffo.initweight !24, !taffo.info !29
  br i1 %cmp10, label %for.body11, label %for.end, !taffo.initweight !26, !taffo.info !29

for.body11:                                       ; preds = %for.cond9
  %mul = mul nsw i32 %i.0, %j.0, !taffo.initweight !24, !taffo.info !30
  %conv = sitofp i32 %mul to double, !taffo.initweight !26, !taffo.info !25
  %div = fdiv double %conv, 3.200000e+01, !taffo.initweight !32, !taffo.info !33, !taffo.constinfo !35
  %conv12 = sitofp i32 %i.0 to double, !taffo.initweight !24, !taffo.info !30
  %add = fadd double %div, %conv12, !taffo.initweight !26, !taffo.info !38
  %div13 = fdiv double %add, 2.800000e+01, !taffo.initweight !32, !taffo.info !40, !taffo.constinfo !42
  %idxprom = sext i32 %i.0 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom, !taffo.initweight !21, !taffo.info !15
  %idxprom14 = sext i32 %j.0 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx15 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx, i64 0, i64 %idxprom14, !taffo.initweight !24, !taffo.info !15
  store double %div13, double* %arrayidx15, align 8, !taffo.initweight !26, !taffo.info !15
  br label %for.inc

for.inc:                                          ; preds = %for.body11
  %inc = add nsw i32 %j.0, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc16

for.inc16:                                        ; preds = %for.end
  %inc17 = add nsw i32 %i.0, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond

for.end18:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc43, %for.end18
  %j.1 = phi i32 [ 0, %for.end18 ], [ %inc44, %for.inc43 ], !taffo.info !27
  %cmp21 = icmp slt i32 %j.1, 32, !taffo.initweight !24, !taffo.info !29
  br i1 %cmp21, label %for.body23, label %for.end45, !taffo.initweight !26, !taffo.info !29

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx25 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom24, !taffo.initweight !21, !taffo.info !12
  store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.initweight !24, !taffo.info !12, !taffo.constinfo !48
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc37, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc38, %for.inc37 ], !taffo.info !22
  %cmp27 = icmp slt i32 %i.1, 28, !taffo.initweight !24, !taffo.info !25
  br i1 %cmp27, label %for.body29, label %for.end39, !taffo.initweight !26, !taffo.info !25

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx31 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom30, !taffo.initweight !21, !taffo.info !15
  %idxprom32 = sext i32 %j.1 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx33 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx31, i64 0, i64 %idxprom32, !taffo.initweight !24, !taffo.info !15
  %0 = load double, double* %arrayidx33, align 8, !taffo.initweight !26, !taffo.info !15
  %idxprom34 = sext i32 %j.1 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx35 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom34, !taffo.initweight !21, !taffo.info !12
  %1 = load double, double* %arrayidx35, align 8, !taffo.initweight !24, !taffo.info !12
  %add36 = fadd double %1, %0, !taffo.initweight !26, !taffo.info !50
  store double %add36, double* %arrayidx35, align 8, !taffo.initweight !24, !taffo.info !12
  br label %for.inc37

for.inc37:                                        ; preds = %for.body29
  %inc38 = add nsw i32 %i.1, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond26

for.end39:                                        ; preds = %for.cond26
  %idxprom40 = sext i32 %j.1 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx41 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom40, !taffo.initweight !21, !taffo.info !12
  %2 = load double, double* %arrayidx41, align 8, !taffo.initweight !24, !taffo.info !12
  %div42 = fdiv double %2, 2.800000e+01, !taffo.initweight !24, !taffo.info !52, !taffo.constinfo !42
  store double %div42, double* %arrayidx41, align 8, !taffo.initweight !24, !taffo.info !12
  br label %for.inc43

for.inc43:                                        ; preds = %for.end39
  %inc44 = add nsw i32 %j.1, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond20

for.end45:                                        ; preds = %for.cond20
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc91, %for.end45
  %j.2 = phi i32 [ 0, %for.end45 ], [ %inc92, %for.inc91 ], !taffo.info !27
  %cmp47 = icmp slt i32 %j.2, 32, !taffo.initweight !24, !taffo.info !29
  br i1 %cmp47, label %for.body49, label %for.end93, !taffo.initweight !26, !taffo.info !29

for.body49:                                       ; preds = %for.cond46
  %idxprom50 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx51 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom50, !taffo.initweight !21, !taffo.info !19
  store double 0.000000e+00, double* %arrayidx51, align 8, !taffo.initweight !24, !taffo.info !19, !taffo.constinfo !48
  br label %for.cond52

for.cond52:                                       ; preds = %for.inc73, %for.body49
  %i.2 = phi i32 [ 0, %for.body49 ], [ %inc74, %for.inc73 ], !taffo.info !22
  %cmp53 = icmp slt i32 %i.2, 28, !taffo.initweight !24, !taffo.info !25
  br i1 %cmp53, label %for.body55, label %for.end75, !taffo.initweight !26, !taffo.info !25

for.body55:                                       ; preds = %for.cond52
  %idxprom56 = sext i32 %i.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx57 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom56, !taffo.initweight !21, !taffo.info !15
  %idxprom58 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx59 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx57, i64 0, i64 %idxprom58, !taffo.initweight !24, !taffo.info !15
  %3 = load double, double* %arrayidx59, align 8, !taffo.initweight !26, !taffo.info !15
  %idxprom60 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx61 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom60, !taffo.initweight !21, !taffo.info !12
  %4 = load double, double* %arrayidx61, align 8, !taffo.initweight !24, !taffo.info !12
  %sub = fsub double %3, %4, !taffo.initweight !26, !taffo.info !50
  %idxprom62 = sext i32 %i.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx63 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom62, !taffo.initweight !21, !taffo.info !15
  %idxprom64 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx65 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx63, i64 0, i64 %idxprom64, !taffo.initweight !24, !taffo.info !15
  %5 = load double, double* %arrayidx65, align 8, !taffo.initweight !26, !taffo.info !15
  %idxprom66 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx67 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom66, !taffo.initweight !21, !taffo.info !12
  %6 = load double, double* %arrayidx67, align 8, !taffo.initweight !24, !taffo.info !12
  %sub68 = fsub double %5, %6, !taffo.initweight !26, !taffo.info !50
  %mul69 = fmul double %sub, %sub68, !taffo.initweight !32, !taffo.info !54
  %idxprom70 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx71 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom70, !taffo.initweight !21, !taffo.info !19
  %7 = load double, double* %arrayidx71, align 8, !taffo.initweight !24, !taffo.info !19
  %add72 = fadd double %7, %mul69, !taffo.initweight !26, !taffo.info !56
  store double %add72, double* %arrayidx71, align 8, !taffo.initweight !24, !taffo.info !19
  br label %for.inc73

for.inc73:                                        ; preds = %for.body55
  %inc74 = add nsw i32 %i.2, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond52

for.end75:                                        ; preds = %for.cond52
  %idxprom76 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx77 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom76, !taffo.initweight !21, !taffo.info !19
  %8 = load double, double* %arrayidx77, align 8, !taffo.initweight !24, !taffo.info !19
  %div78 = fdiv double %8, 2.800000e+01, !taffo.initweight !24, !taffo.info !58, !taffo.constinfo !42
  store double %div78, double* %arrayidx77, align 8, !taffo.initweight !24, !taffo.info !19
  %idxprom79 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx80 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom79, !taffo.initweight !21, !taffo.info !19
  %9 = load double, double* %arrayidx80, align 8, !taffo.initweight !24, !taffo.info !19
  %call = call double @sqrt(double %9) #1, !taffo.initweight !26, !taffo.info !60, !taffo.constinfo !47
  %idxprom81 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx82 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom81, !taffo.initweight !21, !taffo.info !19
  store double %call, double* %arrayidx82, align 8, !taffo.initweight !24, !taffo.info !19
  %idxprom83 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx84 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom83, !taffo.initweight !21, !taffo.info !19
  %10 = load double, double* %arrayidx84, align 8, !taffo.initweight !24, !taffo.info !19
  %cmp85 = fcmp ole double %10, 1.000000e-01, !taffo.initweight !24, !taffo.info !62
  br i1 %cmp85, label %cond.true, label %cond.false, !taffo.initweight !26, !taffo.info !64

cond.true:                                        ; preds = %for.end75
  br label %cond.end

cond.false:                                       ; preds = %for.end75
  %idxprom87 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx88 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom87, !taffo.initweight !21, !taffo.info !19
  %11 = load double, double* %arrayidx88, align 8, !taffo.initweight !24, !taffo.info !19
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond = phi double [ 1.000000e+00, %cond.true ], [ %11, %cond.false ], !taffo.initweight !26, !taffo.info !19
  %idxprom89 = sext i32 %j.2 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx90 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom89, !taffo.initweight !21, !taffo.info !19
  store double %cond, double* %arrayidx90, align 8, !taffo.initweight !24, !taffo.info !19
  br label %for.inc91

for.inc91:                                        ; preds = %cond.end
  %inc92 = add nsw i32 %j.2, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond46

for.end93:                                        ; preds = %for.cond46
  br label %for.cond94

for.cond94:                                       ; preds = %for.inc121, %for.end93
  %i.3 = phi i32 [ 0, %for.end93 ], [ %inc122, %for.inc121 ], !taffo.info !22
  %cmp95 = icmp slt i32 %i.3, 28, !taffo.initweight !24, !taffo.info !25
  br i1 %cmp95, label %for.body97, label %for.end123, !taffo.initweight !26, !taffo.info !25

for.body97:                                       ; preds = %for.cond94
  br label %for.cond98

for.cond98:                                       ; preds = %for.inc118, %for.body97
  %j.3 = phi i32 [ 0, %for.body97 ], [ %inc119, %for.inc118 ], !taffo.info !27
  %cmp99 = icmp slt i32 %j.3, 32, !taffo.initweight !24, !taffo.info !29
  br i1 %cmp99, label %for.body101, label %for.end120, !taffo.initweight !26, !taffo.info !29

for.body101:                                      ; preds = %for.cond98
  %idxprom102 = sext i32 %j.3 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx103 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom102, !taffo.initweight !21, !taffo.info !12
  %12 = load double, double* %arrayidx103, align 8, !taffo.initweight !24, !taffo.info !12
  %idxprom104 = sext i32 %i.3 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx105 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom104, !taffo.initweight !21, !taffo.info !15
  %idxprom106 = sext i32 %j.3 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx107 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx105, i64 0, i64 %idxprom106, !taffo.initweight !24, !taffo.info !15
  %13 = load double, double* %arrayidx107, align 8, !taffo.initweight !26, !taffo.info !15
  %sub108 = fsub double %13, %12, !taffo.initweight !26, !taffo.info !50
  store double %sub108, double* %arrayidx107, align 8, !taffo.initweight !26, !taffo.info !15
  %call109 = call double @sqrt(double 2.800000e+01) #1, !taffo.initweight !24, !taffo.info !65, !taffo.constinfo !67
  %idxprom110 = sext i32 %j.3 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx111 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom110, !taffo.initweight !21, !taffo.info !19
  %14 = load double, double* %arrayidx111, align 8, !taffo.initweight !24, !taffo.info !19
  %mul112 = fmul double %call109, %14, !taffo.initweight !26, !taffo.info !68
  %idxprom113 = sext i32 %i.3 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx114 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom113, !taffo.initweight !21, !taffo.info !15
  %idxprom115 = sext i32 %j.3 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx116 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx114, i64 0, i64 %idxprom115, !taffo.initweight !24, !taffo.info !15
  %15 = load double, double* %arrayidx116, align 8, !taffo.initweight !26, !taffo.info !15
  %div117 = fdiv double %15, %mul112, !taffo.initweight !32, !taffo.info !70
  store double %div117, double* %arrayidx116, align 8, !taffo.initweight !26, !taffo.info !15
  br label %for.inc118

for.inc118:                                       ; preds = %for.body101
  %inc119 = add nsw i32 %j.3, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond98

for.end120:                                       ; preds = %for.cond98
  br label %for.inc121

for.inc121:                                       ; preds = %for.end120
  %inc122 = add nsw i32 %i.3, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond94

for.end123:                                       ; preds = %for.cond94
  br label %for.cond124

for.cond124:                                      ; preds = %for.inc173, %for.end123
  %i.4 = phi i32 [ 0, %for.end123 ], [ %inc174, %for.inc173 ], !taffo.info !22
  %cmp125 = icmp slt i32 %i.4, 31, !taffo.initweight !24, !taffo.info !25
  br i1 %cmp125, label %for.body127, label %for.end175, !taffo.initweight !26, !taffo.info !25

for.body127:                                      ; preds = %for.cond124
  %idxprom128 = sext i32 %i.4 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx129 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom128, !taffo.initweight !21, !taffo.info !17
  %idxprom130 = sext i32 %i.4 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx131 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx129, i64 0, i64 %idxprom130, !taffo.initweight !24, !taffo.info !17
  store double 1.000000e+00, double* %arrayidx131, align 8, !taffo.initweight !26, !taffo.info !17, !taffo.constinfo !72
  %add132 = add nsw i32 %i.4, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond133

for.cond133:                                      ; preds = %for.inc170, %for.body127
  %j.4 = phi i32 [ %add132, %for.body127 ], [ %inc171, %for.inc170 ], !taffo.info !22
  %cmp134 = icmp slt i32 %j.4, 32, !taffo.initweight !24, !taffo.info !29
  br i1 %cmp134, label %for.body136, label %for.end172, !taffo.initweight !26, !taffo.info !29

for.body136:                                      ; preds = %for.cond133
  %idxprom137 = sext i32 %i.4 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx138 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom137, !taffo.initweight !21, !taffo.info !17
  %idxprom139 = sext i32 %j.4 to i64, !taffo.initweight !24, !taffo.info !25
  %arrayidx140 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx138, i64 0, i64 %idxprom139, !taffo.initweight !24, !taffo.info !17
  store double 0.000000e+00, double* %arrayidx140, align 8, !taffo.initweight !26, !taffo.info !17, !taffo.constinfo !48
  br label %for.cond141

for.cond141:                                      ; preds = %for.inc159, %for.body136
  %k.0 = phi i32 [ 0, %for.body136 ], [ %inc160, %for.inc159 ], !taffo.info !27
  %cmp142 = icmp slt i32 %k.0, 28, !taffo.initweight !24, !taffo.info !29
  br i1 %cmp142, label %for.body144, label %for.end161, !taffo.initweight !26, !taffo.info !29

for.body144:                                      ; preds = %for.cond141
  %idxprom145 = sext i32 %k.0 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx146 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom145, !taffo.initweight !21, !taffo.info !15
  %idxprom147 = sext i32 %i.4 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx148 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx146, i64 0, i64 %idxprom147, !taffo.initweight !24, !taffo.info !15
  %16 = load double, double* %arrayidx148, align 8, !taffo.initweight !26, !taffo.info !15
  %idxprom149 = sext i32 %k.0 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx150 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom149, !taffo.initweight !21, !taffo.info !15
  %idxprom151 = sext i32 %j.4 to i64, !taffo.initweight !24, !taffo.info !25
  %arrayidx152 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx150, i64 0, i64 %idxprom151, !taffo.initweight !24, !taffo.info !15
  %17 = load double, double* %arrayidx152, align 8, !taffo.initweight !26, !taffo.info !15
  %mul153 = fmul double %16, %17, !taffo.initweight !32, !taffo.info !74
  %idxprom154 = sext i32 %i.4 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx155 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom154, !taffo.initweight !21, !taffo.info !17
  %idxprom156 = sext i32 %j.4 to i64, !taffo.initweight !24, !taffo.info !25
  %arrayidx157 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx155, i64 0, i64 %idxprom156, !taffo.initweight !24, !taffo.info !17
  %18 = load double, double* %arrayidx157, align 8, !taffo.initweight !26, !taffo.info !17
  %add158 = fadd double %18, %mul153, !taffo.initweight !32, !taffo.info !76
  store double %add158, double* %arrayidx157, align 8, !taffo.initweight !26, !taffo.info !17
  br label %for.inc159

for.inc159:                                       ; preds = %for.body144
  %inc160 = add nsw i32 %k.0, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond141

for.end161:                                       ; preds = %for.cond141
  %idxprom162 = sext i32 %i.4 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx163 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom162, !taffo.initweight !21, !taffo.info !17
  %idxprom164 = sext i32 %j.4 to i64, !taffo.initweight !24, !taffo.info !25
  %arrayidx165 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx163, i64 0, i64 %idxprom164, !taffo.initweight !24, !taffo.info !17
  %19 = load double, double* %arrayidx165, align 8, !taffo.initweight !26, !taffo.info !17
  %idxprom166 = sext i32 %j.4 to i64, !taffo.initweight !24, !taffo.info !25
  %arrayidx167 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom166, !taffo.initweight !21, !taffo.info !17
  %idxprom168 = sext i32 %i.4 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx169 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx167, i64 0, i64 %idxprom168, !taffo.initweight !24, !taffo.info !17
  store double %19, double* %arrayidx169, align 8, !taffo.initweight !26, !taffo.info !17
  br label %for.inc170

for.inc170:                                       ; preds = %for.end161
  %inc171 = add nsw i32 %j.4, 1, !taffo.initweight !24, !taffo.info !78, !taffo.constinfo !47
  br label %for.cond133

for.end172:                                       ; preds = %for.cond133
  br label %for.inc173

for.inc173:                                       ; preds = %for.end172
  %inc174 = add nsw i32 %i.4, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond124

for.end175:                                       ; preds = %for.cond124
  %arrayidx176 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 31, !taffo.initweight !21, !taffo.info !17
  %arrayidx177 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx176, i64 0, i64 31, !taffo.initweight !24, !taffo.info !17
  store double 1.000000e+00, double* %arrayidx177, align 8, !taffo.initweight !26, !taffo.info !17, !taffo.constinfo !72
  br label %for.cond178

for.cond178:                                      ; preds = %for.inc195, %for.end175
  %i.5 = phi i32 [ 0, %for.end175 ], [ %inc196, %for.inc195 ], !taffo.info !22
  %cmp179 = icmp slt i32 %i.5, 32, !taffo.initweight !24, !taffo.info !25
  br i1 %cmp179, label %for.body181, label %for.end197, !taffo.initweight !26, !taffo.info !25

for.body181:                                      ; preds = %for.cond178
  br label %for.cond182

for.cond182:                                      ; preds = %for.inc191, %for.body181
  %j.5 = phi i32 [ 0, %for.body181 ], [ %inc192, %for.inc191 ], !taffo.info !27
  %cmp183 = icmp slt i32 %j.5, 32, !taffo.initweight !24, !taffo.info !29
  br i1 %cmp183, label %for.body185, label %for.end193, !taffo.initweight !26, !taffo.info !29

for.body185:                                      ; preds = %for.cond182
  %idxprom186 = sext i32 %i.5 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx187 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom186, !taffo.initweight !21, !taffo.info !17
  %idxprom188 = sext i32 %j.5 to i64, !taffo.initweight !24, !taffo.info !30
  %arrayidx189 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx187, i64 0, i64 %idxprom188, !taffo.initweight !24, !taffo.info !17
  %20 = load double, double* %arrayidx189, align 8, !taffo.initweight !26, !taffo.info !17
  %call190 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.9, i32 0, i32 0), double %20), !taffo.initweight !32, !taffo.info !17, !taffo.constinfo !80
  br label %for.inc191

for.inc191:                                       ; preds = %for.body185
  %inc192 = add nsw i32 %j.5, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond182

for.end193:                                       ; preds = %for.cond182
  %call194 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.10, i32 0, i32 0)), !taffo.constinfo !47
  br label %for.inc195

for.inc195:                                       ; preds = %for.end193
  %inc196 = add nsw i32 %i.5, 1, !taffo.initweight !24, !taffo.info !45, !taffo.constinfo !47
  br label %for.cond178

for.end197:                                       ; preds = %for.cond178
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !81 !taffo.funinfo !82 void @llvm.var.annotation(i8*, i8*, i8*, i32) #1

; Function Attrs: nounwind
declare !taffo.initweight !83 !taffo.funinfo !84 dso_local double @sqrt(double) #2

declare !taffo.initweight !83 !taffo.funinfo !84 dso_local i32 @printf(i8*, ...) #3

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!8}
!llvm.ident = !{!9}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 1.150000e+02}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.210000e+02}
!4 = !{i1 false, !5, i1 false, i2 0}
!5 = !{double 0.000000e+00, double 1.080000e+02}
!6 = !{i1 false, !7, i1 false, i2 0}
!7 = !{double 0.000000e+00, double 1.000000e+01}
!8 = !{i32 1, !"wchar_size", i32 4}
!9 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!10 = !{}
!11 = !{i32 0}
!12 = !{i1 false, !13, !14, i2 -1}
!13 = !{double -5.000000e+04, double 5.000000e+04}
!14 = !{double 1.000000e-100}
!15 = !{i1 false, !16, !14, i2 -1}
!16 = !{double -1.000000e+01, double 1.000000e+01}
!17 = !{i1 false, !18, !14, i2 -1}
!18 = !{double 0.000000e+00, double 5.000000e+00}
!19 = !{i1 false, !20, !14, i2 -1}
!20 = !{double -4.096000e+03, double 4.096000e+03}
!21 = !{i32 1}
!22 = !{i1 false, !23, i1 false, i2 0}
!23 = !{double 0.000000e+00, double 2.800000e+01}
!24 = !{i32 2}
!25 = !{i1 false, !23, i1 false, i2 -2}
!26 = !{i32 3}
!27 = !{i1 false, !28, i1 false, i2 0}
!28 = !{double 0.000000e+00, double 3.200000e+01}
!29 = !{i1 false, !28, i1 false, i2 -2}
!30 = !{i1 false, !31, i1 false, i2 -2}
!31 = !{double 0.000000e+00, double 0.000000e+00}
!32 = !{i32 4}
!33 = !{i1 false, !34, i1 false, i2 -2}
!34 = !{double 0.000000e+00, double 8.750000e-01}
!35 = !{i1 false, !36}
!36 = !{i1 false, !37, i1 false, i2 0}
!37 = !{double 3.200000e+01, double 3.200000e+01}
!38 = !{i1 false, !39, i1 false, i2 -2}
!39 = !{double 0.000000e+00, double 2.887500e+01}
!40 = !{i1 false, !41, i1 false, i2 -2}
!41 = !{double 0.000000e+00, double 1.031250e+00}
!42 = !{i1 false, !43}
!43 = !{i1 false, !44, i1 false, i2 0}
!44 = !{double 2.800000e+01, double 2.800000e+01}
!45 = !{i1 false, !46, i1 false, i2 -2}
!46 = !{double 1.000000e+00, double 1.000000e+00}
!47 = !{i1 false, i1 false}
!48 = !{!49, i1 false}
!49 = !{i1 false, !31, i1 false, i2 0}
!50 = !{i1 false, !51, !14, i2 -1}
!51 = !{double -5.001000e+04, double 5.001000e+04}
!52 = !{i1 false, !53, !14, i2 1}
!53 = !{double 0xC09BE6DB6DB6DB6E, double 0x409BE6DB6DB6DB6E}
!54 = !{i1 false, !55, !14, i2 -1}
!55 = !{double 0xC1E2A24774800000, double 0x41E2A24774800000}
!56 = !{i1 false, !57, !14, i2 -1}
!57 = !{double 0xC1E2A24974800000, double 0x41E2A24974800000}
!58 = !{i1 false, !59, !14, i2 1}
!59 = !{double 0xC062492492492492, double 0x4062492492492492}
!60 = !{i1 false, !61, !14, i2 -1}
!61 = !{double 0.000000e+00, double 6.400000e+01}
!62 = !{i1 false, !63, i1 false, i2 1}
!63 = !{double 0.000000e+00, double 1.000000e+00}
!64 = !{i1 false, i1 false, i1 false, i2 1}
!65 = !{i1 false, !66, !14, i2 1}
!66 = !{double 0x40152A7FA9D2F8EA, double 0x40152A7FA9D2F8EA}
!67 = !{!43, i1 false}
!68 = !{i1 false, !69, !14, i2 -1}
!69 = !{double 0xC0D52A7FA9D2F8EA, double 0x40D52A7FA9D2F8EA}
!70 = !{i1 false, !71, !14, i2 -1}
!71 = !{double 0xBF3E3CB66051F5E0, double 0x3F3E3CB66051F5E0}
!72 = !{!73, i1 false}
!73 = !{i1 false, !46, i1 false, i2 0}
!74 = !{i1 false, !75, !14, i2 -1}
!75 = !{double -1.000000e+02, double 1.000000e+02}
!76 = !{i1 false, !77, !14, i2 -1}
!77 = !{double -1.000000e+02, double 1.050000e+02}
!78 = !{i1 false, !79, i1 false, i2 -2}
!79 = !{double 1.000000e+00, double 2.900000e+01}
!80 = !{i1 false, i1 false, i1 false}
!81 = !{i32 -1, i32 -1, i32 -1, i32 -1}
!82 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
!83 = !{i32 -1}
!84 = !{i32 0, i1 false}
