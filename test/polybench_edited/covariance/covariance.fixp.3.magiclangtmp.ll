; ModuleID = 'polybench_edited/covariance/covariance.fixp.2.magiclangtmp.ll'
source_filename = "polybench_edited/covariance/covariance.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

@.str = private unnamed_addr constant [35 x i8] c"scalar(range(-10000, 10000) final)\00", section "llvm.metadata", !taffo.info !0
@.str.1 = private unnamed_addr constant [41 x i8] c"polybench_edited/covariance/covariance.c\00", section "llvm.metadata", !taffo.info !2
@.str.2 = private unnamed_addr constant [30 x i8] c"scalar(range(-10000, 100000))\00", section "llvm.metadata", !taffo.info !0
@.str.3 = private unnamed_addr constant [33 x i8] c"scalar(range(-5000, 5000) final)\00", section "llvm.metadata", !taffo.info !0
@.str.4 = private unnamed_addr constant [31 x i8] c"scalar(range(1, 100) disabled)\00", section "llvm.metadata", !taffo.info !0
@stdout = external dso_local global %struct._IO_FILE*, align 8
@.str.5 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !4
@.str.6 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !6

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main(i32 %argc, i8** %argv) #0 !taffo.initweight !10 !taffo.funinfo !11 {
entry:
  %data = alloca [100 x [80 x double]], align 16, !taffo.initweight !12, !taffo.info !13
  %cov = alloca [100 x [80 x double]], align 16, !taffo.initweight !12, !taffo.info !15
  %mean = alloca [80 x double], align 16, !taffo.initweight !12, !taffo.info !17
  %data2 = bitcast [100 x [80 x double]]* %data to i8*, !taffo.initweight !19, !taffo.info !13
  %cov3 = bitcast [100 x [80 x double]]* %cov to i8*, !taffo.initweight !19, !taffo.info !15
  %mean4 = bitcast [80 x double]* %mean to i8*, !taffo.initweight !19, !taffo.info !17
  %conv = sitofp i32 100 to double
  br label %for.cond

for.cond:                                         ; preds = %for.inc17, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc18, %for.inc17 ]
  %cmp = icmp slt i32 %i.0, 100, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp, label %for.body, label %for.end19, !taffo.initweight !23, !taffo.info !21

for.body:                                         ; preds = %for.cond
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ]
  %cmp10 = icmp slt i32 %j.0, 80, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp10, label %for.body12, label %for.end, !taffo.initweight !23, !taffo.info !21

for.body12:                                       ; preds = %for.cond9
  %conv13 = sitofp i32 %i.0 to double, !taffo.initweight !20, !taffo.info !21
  %conv14 = sitofp i32 %j.0 to double, !taffo.initweight !20, !taffo.info !21
  %mul = fmul double %conv13, %conv14, !taffo.initweight !23, !taffo.info !21
  %div = fdiv double %mul, 8.000000e+01, !taffo.initweight !24, !taffo.info !21, !taffo.constinfo !25
  %idxprom = sext i32 %i.0 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom, !taffo.initweight !19, !taffo.info !13
  %idxprom15 = sext i32 %j.0 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx16 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx, i64 0, i64 %idxprom15, !taffo.initweight !20, !taffo.info !13
  store double %div, double* %arrayidx16, align 8, !taffo.initweight !23, !taffo.info !13
  br label %for.inc

for.inc:                                          ; preds = %for.body12
  %inc = add nsw i32 %j.0, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc17

for.inc17:                                        ; preds = %for.end
  %inc18 = add nsw i32 %i.0, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond

for.end19:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc42, %for.end19
  %j.1 = phi i32 [ 0, %for.end19 ], [ %inc43, %for.inc42 ]
  %cmp21 = icmp slt i32 %j.1, 80, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp21, label %for.body23, label %for.end44, !taffo.initweight !23, !taffo.info !21

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx25 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom24, !taffo.initweight !19, !taffo.info !17
  store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.initweight !20, !taffo.info !17, !taffo.constinfo !29
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc36, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc37, %for.inc36 ]
  %cmp27 = icmp slt i32 %i.1, 100, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp27, label %for.body29, label %for.end38, !taffo.initweight !23, !taffo.info !21

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx31 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom30, !taffo.initweight !19, !taffo.info !13
  %idxprom32 = sext i32 %j.1 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx33 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx31, i64 0, i64 %idxprom32, !taffo.initweight !20, !taffo.info !13
  %0 = load double, double* %arrayidx33, align 8, !taffo.initweight !23, !taffo.info !13
  %idxprom34 = sext i32 %j.1 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx35 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom34, !taffo.initweight !19, !taffo.info !17
  %1 = load double, double* %arrayidx35, align 8, !taffo.initweight !20, !taffo.info !17
  %add = fadd double %1, %0, !taffo.initweight !23, !taffo.info !17
  store double %add, double* %arrayidx35, align 8, !taffo.initweight !20, !taffo.info !17
  br label %for.inc36

for.inc36:                                        ; preds = %for.body29
  %inc37 = add nsw i32 %i.1, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond26

for.end38:                                        ; preds = %for.cond26
  %idxprom39 = sext i32 %j.1 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx40 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom39, !taffo.initweight !19, !taffo.info !17
  %2 = load double, double* %arrayidx40, align 8, !taffo.initweight !20, !taffo.info !17
  %div41 = fdiv double %2, %conv, !taffo.initweight !20, !taffo.info !13
  store double %div41, double* %arrayidx40, align 8, !taffo.initweight !20, !taffo.info !17
  br label %for.inc42

for.inc42:                                        ; preds = %for.end38
  %inc43 = add nsw i32 %j.1, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond20

for.end44:                                        ; preds = %for.cond20
  br label %for.cond45

for.cond45:                                       ; preds = %for.inc62, %for.end44
  %i.2 = phi i32 [ 0, %for.end44 ], [ %inc63, %for.inc62 ]
  %cmp46 = icmp slt i32 %i.2, 100, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp46, label %for.body48, label %for.end64, !taffo.initweight !23, !taffo.info !21

for.body48:                                       ; preds = %for.cond45
  br label %for.cond49

for.cond49:                                       ; preds = %for.inc59, %for.body48
  %j.2 = phi i32 [ 0, %for.body48 ], [ %inc60, %for.inc59 ]
  %cmp50 = icmp slt i32 %j.2, 80, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp50, label %for.body52, label %for.end61, !taffo.initweight !23, !taffo.info !21

for.body52:                                       ; preds = %for.cond49
  %idxprom53 = sext i32 %j.2 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx54 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom53, !taffo.initweight !19, !taffo.info !17
  %3 = load double, double* %arrayidx54, align 8, !taffo.initweight !20, !taffo.info !17
  %idxprom55 = sext i32 %i.2 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx56 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom55, !taffo.initweight !19, !taffo.info !13
  %idxprom57 = sext i32 %j.2 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx58 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx56, i64 0, i64 %idxprom57, !taffo.initweight !20, !taffo.info !13
  %4 = load double, double* %arrayidx58, align 8, !taffo.initweight !23, !taffo.info !13
  %sub = fsub double %4, %3, !taffo.initweight !23, !taffo.info !17
  store double %sub, double* %arrayidx58, align 8, !taffo.initweight !23, !taffo.info !13
  br label %for.inc59

for.inc59:                                        ; preds = %for.body52
  %inc60 = add nsw i32 %j.2, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond49

for.end61:                                        ; preds = %for.cond49
  br label %for.inc62

for.inc62:                                        ; preds = %for.end61
  %inc63 = add nsw i32 %i.2, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond45

for.end64:                                        ; preds = %for.cond45
  br label %for.cond65

for.cond65:                                       ; preds = %for.inc114, %for.end64
  %i.3 = phi i32 [ 0, %for.end64 ], [ %inc115, %for.inc114 ]
  %cmp66 = icmp slt i32 %i.3, 80, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp66, label %for.body68, label %for.end116, !taffo.initweight !23, !taffo.info !21

for.body68:                                       ; preds = %for.cond65
  br label %for.cond69

for.cond69:                                       ; preds = %for.inc111, %for.body68
  %j.3 = phi i32 [ %i.3, %for.body68 ], [ %inc112, %for.inc111 ]
  %cmp70 = icmp slt i32 %j.3, 80, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp70, label %for.body72, label %for.end113, !taffo.initweight !23, !taffo.info !21

for.body72:                                       ; preds = %for.cond69
  %idxprom73 = sext i32 %i.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx74 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom73, !taffo.initweight !19, !taffo.info !15
  %idxprom75 = sext i32 %j.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx76 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx74, i64 0, i64 %idxprom75, !taffo.initweight !20, !taffo.info !15
  store double 0.000000e+00, double* %arrayidx76, align 8, !taffo.initweight !23, !taffo.info !15, !taffo.constinfo !29
  br label %for.cond77

for.cond77:                                       ; preds = %for.inc95, %for.body72
  %k.0 = phi i32 [ 0, %for.body72 ], [ %inc96, %for.inc95 ]
  %cmp78 = icmp slt i32 %k.0, 100, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp78, label %for.body80, label %for.end97, !taffo.initweight !23, !taffo.info !21

for.body80:                                       ; preds = %for.cond77
  %idxprom81 = sext i32 %k.0 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx82 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom81, !taffo.initweight !19, !taffo.info !13
  %idxprom83 = sext i32 %i.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx84 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx82, i64 0, i64 %idxprom83, !taffo.initweight !20, !taffo.info !13
  %5 = load double, double* %arrayidx84, align 8, !taffo.initweight !23, !taffo.info !13
  %idxprom85 = sext i32 %k.0 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx86 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom85, !taffo.initweight !19, !taffo.info !13
  %idxprom87 = sext i32 %j.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx88 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx86, i64 0, i64 %idxprom87, !taffo.initweight !20, !taffo.info !13
  %6 = load double, double* %arrayidx88, align 8, !taffo.initweight !23, !taffo.info !13
  %mul89 = fmul double %5, %6, !taffo.initweight !24, !taffo.info !13
  %idxprom90 = sext i32 %i.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx91 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom90, !taffo.initweight !19, !taffo.info !15
  %idxprom92 = sext i32 %j.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx93 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx91, i64 0, i64 %idxprom92, !taffo.initweight !20, !taffo.info !15
  %7 = load double, double* %arrayidx93, align 8, !taffo.initweight !23, !taffo.info !15
  %add94 = fadd double %7, %mul89, !taffo.initweight !24, !taffo.info !15
  store double %add94, double* %arrayidx93, align 8, !taffo.initweight !23, !taffo.info !15
  br label %for.inc95

for.inc95:                                        ; preds = %for.body80
  %inc96 = add nsw i32 %k.0, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond77

for.end97:                                        ; preds = %for.cond77
  %idxprom98 = sext i32 %i.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx99 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom98, !taffo.initweight !19, !taffo.info !15
  %idxprom100 = sext i32 %j.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx101 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx99, i64 0, i64 %idxprom100, !taffo.initweight !20, !taffo.info !15
  %8 = load double, double* %arrayidx101, align 8, !taffo.initweight !23, !taffo.info !15
  %div102 = fdiv double %8, 9.900000e+01, !taffo.initweight !24, !taffo.info !15, !taffo.constinfo !32
  store double %div102, double* %arrayidx101, align 8, !taffo.initweight !23, !taffo.info !15
  %idxprom103 = sext i32 %i.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx104 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom103, !taffo.initweight !19, !taffo.info !15
  %idxprom105 = sext i32 %j.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx106 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx104, i64 0, i64 %idxprom105, !taffo.initweight !20, !taffo.info !15
  %9 = load double, double* %arrayidx106, align 8, !taffo.initweight !23, !taffo.info !15
  %idxprom107 = sext i32 %j.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx108 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom107, !taffo.initweight !19, !taffo.info !15
  %idxprom109 = sext i32 %i.3 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx110 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx108, i64 0, i64 %idxprom109, !taffo.initweight !20, !taffo.info !15
  store double %9, double* %arrayidx110, align 8, !taffo.initweight !23, !taffo.info !15
  br label %for.inc111

for.inc111:                                       ; preds = %for.end97
  %inc112 = add nsw i32 %j.3, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond69

for.end113:                                       ; preds = %for.cond69
  br label %for.inc114

for.inc114:                                       ; preds = %for.end113
  %inc115 = add nsw i32 %i.3, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond65

for.end116:                                       ; preds = %for.cond65
  br label %for.cond117

for.cond117:                                      ; preds = %for.inc137, %for.end116
  %i.4 = phi i32 [ 0, %for.end116 ], [ %inc138, %for.inc137 ]
  %cmp118 = icmp slt i32 %i.4, 80, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp118, label %for.body120, label %for.end139, !taffo.initweight !23, !taffo.info !21

for.body120:                                      ; preds = %for.cond117
  br label %for.cond121

for.cond121:                                      ; preds = %for.inc134, %for.body120
  %j.4 = phi i32 [ 0, %for.body120 ], [ %inc135, %for.inc134 ]
  %cmp122 = icmp slt i32 %j.4, 80, !taffo.initweight !20, !taffo.info !21
  br i1 %cmp122, label %for.body124, label %for.end136, !taffo.initweight !23, !taffo.info !21

for.body124:                                      ; preds = %for.cond121
  %mul125 = mul nsw i32 %i.4, 80, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  %add126 = add nsw i32 %mul125, %j.4, !taffo.initweight !20, !taffo.info !21
  %rem = srem i32 %add126, 20, !taffo.initweight !23, !taffo.info !21, !taffo.constinfo !28
  %cmp127 = icmp eq i32 %rem, 0, !taffo.initweight !24, !taffo.info !21
  br i1 %cmp127, label %if.then, label %if.end, !taffo.initweight !35, !taffo.info !21

if.then:                                          ; preds = %for.body124
  %10 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %10, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.5, i32 0, i32 0)), !taffo.constinfo !36
  br label %if.end

if.end:                                           ; preds = %if.then, %for.body124
  %11 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %idxprom129 = sext i32 %i.4 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx130 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom129, !taffo.initweight !19, !taffo.info !15
  %idxprom131 = sext i32 %j.4 to i64, !taffo.initweight !20, !taffo.info !21
  %arrayidx132 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx130, i64 0, i64 %idxprom131, !taffo.initweight !20, !taffo.info !15
  %12 = load double, double* %arrayidx132, align 8, !taffo.initweight !23, !taffo.info !15
  %call133 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %11, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.6, i32 0, i32 0), double %12), !taffo.initweight !24, !taffo.info !15, !taffo.constinfo !37
  br label %for.inc134

for.inc134:                                       ; preds = %if.end
  %inc135 = add nsw i32 %j.4, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond121

for.end136:                                       ; preds = %for.cond121
  br label %for.inc137

for.inc137:                                       ; preds = %for.end136
  %inc138 = add nsw i32 %i.4, 1, !taffo.initweight !20, !taffo.info !21, !taffo.constinfo !28
  br label %for.cond117

for.end139:                                       ; preds = %for.cond117
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !38 !taffo.funinfo !39 void @llvm.var.annotation(i8*, i8*, i8*, i32) #1

declare !taffo.initweight !10 !taffo.funinfo !11 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!8}
!llvm.ident = !{!9}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 1.150000e+02}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.210000e+02}
!4 = !{i1 false, !5, i1 false, i2 0}
!5 = !{double 0.000000e+00, double 1.000000e+01}
!6 = !{i1 false, !7, i1 false, i2 0}
!7 = !{double 0.000000e+00, double 1.080000e+02}
!8 = !{i32 1, !"wchar_size", i32 4}
!9 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!10 = !{i32 -1, i32 -1}
!11 = !{i32 0, i1 false, i32 0, i1 false}
!12 = !{i32 0}
!13 = !{i1 false, !14, i1 false, i2 -1}
!14 = !{double -1.000000e+04, double 1.000000e+04}
!15 = !{i1 false, !16, i1 false, i2 1}
!16 = !{double -1.000000e+04, double 1.000000e+05}
!17 = !{i1 false, !18, i1 false, i2 -1}
!18 = !{double -5.000000e+03, double 5.000000e+03}
!19 = !{i32 1}
!20 = !{i32 2}
!21 = !{i1 false, !22, i1 false, i2 0}
!22 = !{double 1.000000e+00, double 1.000000e+02}
!23 = !{i32 3}
!24 = !{i32 4}
!25 = !{i1 false, !26}
!26 = !{i1 false, !27, i1 false, i2 0}
!27 = !{double 8.000000e+01, double 8.000000e+01}
!28 = !{i1 false, i1 false}
!29 = !{!30, i1 false}
!30 = !{i1 false, !31, i1 false, i2 0}
!31 = !{double 0.000000e+00, double 0.000000e+00}
!32 = !{i1 false, !33}
!33 = !{i1 false, !34, i1 false, i2 0}
!34 = !{double 9.900000e+01, double 9.900000e+01}
!35 = !{i32 5}
!36 = !{i1 false, i1 false, i1 false}
!37 = !{i1 false, i1 false, i1 false, i1 false}
!38 = !{i32 -1, i32 -1, i32 -1, i32 -1}
!39 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
