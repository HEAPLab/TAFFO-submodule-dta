; ModuleID = 'polybench_edited/covariance/covariance.fixp.3.magiclangtmp.ll'
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
  %data = alloca [100 x [80 x double]], align 16, !taffo.info !8, !taffo.initweight !12
  %cov = alloca [100 x [80 x double]], align 16, !taffo.info !13, !taffo.initweight !12
  %mean = alloca [80 x double], align 16, !taffo.info !16, !taffo.initweight !12
  %data2 = bitcast [100 x [80 x double]]* %data to i8*, !taffo.info !18, !taffo.initweight !19
  %cov3 = bitcast [100 x [80 x double]]* %cov to i8*, !taffo.info !20, !taffo.initweight !19
  %mean4 = bitcast [80 x double]* %mean to i8*, !taffo.info !21, !taffo.initweight !19
  %conv = sitofp i32 100 to double, !taffo.info !23
  br label %for.cond

for.cond:                                         ; preds = %for.inc17, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc18, %for.inc17 ], !taffo.info !25
  %cmp = icmp slt i32 %i.0, 100, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp, label %for.body, label %for.end19, !taffo.info !30, !taffo.initweight !32

for.body:                                         ; preds = %for.cond
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !25
  %cmp10 = icmp slt i32 %j.0, 80, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp10, label %for.body12, label %for.end, !taffo.info !30, !taffo.initweight !32

for.body12:                                       ; preds = %for.cond9
  %conv13 = sitofp i32 %i.0 to double, !taffo.info !33, !taffo.initweight !29
  %conv14 = sitofp i32 %j.0 to double, !taffo.info !33, !taffo.initweight !29
  %mul = fmul double %conv13, %conv14, !taffo.info !33, !taffo.initweight !32
  %div = fdiv double %mul, 8.000000e+01, !taffo.info !33, !taffo.initweight !35, !taffo.constinfo !36
  %idxprom = sext i32 %i.0 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom, !taffo.info !8, !taffo.initweight !19
  %idxprom15 = sext i32 %j.0 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx16 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx, i64 0, i64 %idxprom15, !taffo.info !8, !taffo.initweight !29
  store double %div, double* %arrayidx16, align 8, !taffo.info !39, !taffo.initweight !32
  br label %for.inc

for.inc:                                          ; preds = %for.body12
  %inc = add nsw i32 %j.0, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc17

for.inc17:                                        ; preds = %for.end
  %inc18 = add nsw i32 %i.0, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond

for.end19:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc42, %for.end19
  %j.1 = phi i32 [ 0, %for.end19 ], [ %inc43, %for.inc42 ], !taffo.info !25
  %cmp21 = icmp slt i32 %j.1, 80, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp21, label %for.body23, label %for.end44, !taffo.info !30, !taffo.initweight !32

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx25 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom24, !taffo.info !16, !taffo.initweight !19
  store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.info !41, !taffo.initweight !29, !taffo.constinfo !42
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc36, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc37, %for.inc36 ], !taffo.info !25
  %cmp27 = icmp slt i32 %i.1, 100, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp27, label %for.body29, label %for.end38, !taffo.info !30, !taffo.initweight !32

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx31 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom30, !taffo.info !8, !taffo.initweight !19
  %idxprom32 = sext i32 %j.1 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx33 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx31, i64 0, i64 %idxprom32, !taffo.info !8, !taffo.initweight !29
  %tmp = load double, double* %arrayidx33, align 8, !taffo.info !8, !taffo.initweight !32
  %idxprom34 = sext i32 %j.1 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx35 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom34, !taffo.info !16, !taffo.initweight !19
  %tmp1 = load double, double* %arrayidx35, align 8, !taffo.info !16, !taffo.initweight !29
  %add = fadd double %tmp1, %tmp, !taffo.info !43, !taffo.initweight !32
  store double %add, double* %arrayidx35, align 8, !taffo.info !41, !taffo.initweight !29
  br label %for.inc36

for.inc36:                                        ; preds = %for.body29
  %inc37 = add nsw i32 %i.1, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond26

for.end38:                                        ; preds = %for.cond26
  %idxprom39 = sext i32 %j.1 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx40 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom39, !taffo.info !16, !taffo.initweight !19
  %tmp2 = load double, double* %arrayidx40, align 8, !taffo.info !16, !taffo.initweight !29
  %div41 = fdiv double %tmp2, %conv, !taffo.info !45, !taffo.initweight !29
  store double %div41, double* %arrayidx40, align 8, !taffo.info !41, !taffo.initweight !29
  br label %for.inc42

for.inc42:                                        ; preds = %for.end38
  %inc43 = add nsw i32 %j.1, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond20

for.end44:                                        ; preds = %for.cond20
  br label %for.cond45

for.cond45:                                       ; preds = %for.inc62, %for.end44
  %i.2 = phi i32 [ 0, %for.end44 ], [ %inc63, %for.inc62 ], !taffo.info !25
  %cmp46 = icmp slt i32 %i.2, 100, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp46, label %for.body48, label %for.end64, !taffo.info !30, !taffo.initweight !32

for.body48:                                       ; preds = %for.cond45
  br label %for.cond49

for.cond49:                                       ; preds = %for.inc59, %for.body48
  %j.2 = phi i32 [ 0, %for.body48 ], [ %inc60, %for.inc59 ], !taffo.info !25
  %cmp50 = icmp slt i32 %j.2, 80, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp50, label %for.body52, label %for.end61, !taffo.info !30, !taffo.initweight !32

for.body52:                                       ; preds = %for.cond49
  %idxprom53 = sext i32 %j.2 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx54 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom53, !taffo.info !16, !taffo.initweight !19
  %tmp3 = load double, double* %arrayidx54, align 8, !taffo.info !16, !taffo.initweight !29
  %idxprom55 = sext i32 %i.2 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx56 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom55, !taffo.info !8, !taffo.initweight !19
  %idxprom57 = sext i32 %j.2 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx58 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx56, i64 0, i64 %idxprom57, !taffo.info !8, !taffo.initweight !29
  %tmp4 = load double, double* %arrayidx58, align 8, !taffo.info !8, !taffo.initweight !32
  %sub = fsub double %tmp4, %tmp3, !taffo.info !43, !taffo.initweight !32
  store double %sub, double* %arrayidx58, align 8, !taffo.info !39, !taffo.initweight !32
  br label %for.inc59

for.inc59:                                        ; preds = %for.body52
  %inc60 = add nsw i32 %j.2, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond49

for.end61:                                        ; preds = %for.cond49
  br label %for.inc62

for.inc62:                                        ; preds = %for.end61
  %inc63 = add nsw i32 %i.2, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond45

for.end64:                                        ; preds = %for.cond45
  br label %for.cond65

for.cond65:                                       ; preds = %for.inc114, %for.end64
  %i.3 = phi i32 [ 0, %for.end64 ], [ %inc115, %for.inc114 ], !taffo.info !25
  %cmp66 = icmp slt i32 %i.3, 80, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp66, label %for.body68, label %for.end116, !taffo.info !30, !taffo.initweight !32

for.body68:                                       ; preds = %for.cond65
  br label %for.cond69

for.cond69:                                       ; preds = %for.inc111, %for.body68
  %j.3 = phi i32 [ %i.3, %for.body68 ], [ %inc112, %for.inc111 ], !taffo.info !25
  %cmp70 = icmp slt i32 %j.3, 80, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp70, label %for.body72, label %for.end113, !taffo.info !30, !taffo.initweight !32

for.body72:                                       ; preds = %for.cond69
  %idxprom73 = sext i32 %i.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx74 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom73, !taffo.info !13, !taffo.initweight !19
  %idxprom75 = sext i32 %j.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx76 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx74, i64 0, i64 %idxprom75, !taffo.info !13, !taffo.initweight !29
  store double 0.000000e+00, double* %arrayidx76, align 8, !taffo.info !48, !taffo.initweight !32, !taffo.constinfo !42
  br label %for.cond77

for.cond77:                                       ; preds = %for.inc95, %for.body72
  %k.0 = phi i32 [ 0, %for.body72 ], [ %inc96, %for.inc95 ], !taffo.info !25
  %cmp78 = icmp slt i32 %k.0, 100, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp78, label %for.body80, label %for.end97, !taffo.info !30, !taffo.initweight !32

for.body80:                                       ; preds = %for.cond77
  %idxprom81 = sext i32 %k.0 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx82 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom81, !taffo.info !8, !taffo.initweight !19
  %idxprom83 = sext i32 %i.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx84 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx82, i64 0, i64 %idxprom83, !taffo.info !8, !taffo.initweight !29
  %tmp5 = load double, double* %arrayidx84, align 8, !taffo.info !8, !taffo.initweight !32
  %idxprom85 = sext i32 %k.0 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx86 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom85, !taffo.info !8, !taffo.initweight !19
  %idxprom87 = sext i32 %j.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx88 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx86, i64 0, i64 %idxprom87, !taffo.info !8, !taffo.initweight !29
  %tmp6 = load double, double* %arrayidx88, align 8, !taffo.info !8, !taffo.initweight !32
  %mul89 = fmul double %tmp5, %tmp6, !taffo.info !50, !taffo.initweight !35
  %idxprom90 = sext i32 %i.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx91 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom90, !taffo.info !13, !taffo.initweight !19
  %idxprom92 = sext i32 %j.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx93 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx91, i64 0, i64 %idxprom92, !taffo.info !13, !taffo.initweight !29
  %tmp7 = load double, double* %arrayidx93, align 8, !taffo.info !52, !taffo.initweight !32
  %add94 = fadd double %tmp7, %mul89, !taffo.info !13, !taffo.initweight !35
  store double %add94, double* %arrayidx93, align 8, !taffo.info !48, !taffo.initweight !32
  br label %for.inc95

for.inc95:                                        ; preds = %for.body80
  %inc96 = add nsw i32 %k.0, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond77

for.end97:                                        ; preds = %for.cond77
  %idxprom98 = sext i32 %i.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx99 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom98, !taffo.info !13, !taffo.initweight !19
  %idxprom100 = sext i32 %j.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx101 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx99, i64 0, i64 %idxprom100, !taffo.info !13, !taffo.initweight !29
  %tmp8 = load double, double* %arrayidx101, align 8, !taffo.info !13, !taffo.initweight !32
  %div102 = fdiv double %tmp8, 9.900000e+01, !taffo.info !53, !taffo.initweight !35, !taffo.constinfo !56
  store double %div102, double* %arrayidx101, align 8, !taffo.info !48, !taffo.initweight !32
  %idxprom103 = sext i32 %i.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx104 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom103, !taffo.info !13, !taffo.initweight !19
  %idxprom105 = sext i32 %j.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx106 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx104, i64 0, i64 %idxprom105, !taffo.info !13, !taffo.initweight !29
  %tmp9 = load double, double* %arrayidx106, align 8, !taffo.info !13, !taffo.initweight !32
  %idxprom107 = sext i32 %j.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx108 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom107, !taffo.info !13, !taffo.initweight !19
  %idxprom109 = sext i32 %i.3 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx110 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx108, i64 0, i64 %idxprom109, !taffo.info !13, !taffo.initweight !29
  store double %tmp9, double* %arrayidx110, align 8, !taffo.info !48, !taffo.initweight !32
  br label %for.inc111

for.inc111:                                       ; preds = %for.end97
  %inc112 = add nsw i32 %j.3, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond69

for.end113:                                       ; preds = %for.cond69
  br label %for.inc114

for.inc114:                                       ; preds = %for.end113
  %inc115 = add nsw i32 %i.3, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond65

for.end116:                                       ; preds = %for.cond65
  br label %for.cond117

for.cond117:                                      ; preds = %for.inc137, %for.end116
  %i.4 = phi i32 [ 0, %for.end116 ], [ %inc138, %for.inc137 ], !taffo.info !25
  %cmp118 = icmp slt i32 %i.4, 80, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp118, label %for.body120, label %for.end139, !taffo.info !30, !taffo.initweight !32

for.body120:                                      ; preds = %for.cond117
  br label %for.cond121

for.cond121:                                      ; preds = %for.inc134, %for.body120
  %j.4 = phi i32 [ 0, %for.body120 ], [ %inc135, %for.inc134 ], !taffo.info !25
  %cmp122 = icmp slt i32 %j.4, 80, !taffo.info !27, !taffo.initweight !29
  br i1 %cmp122, label %for.body124, label %for.end136, !taffo.info !30, !taffo.initweight !32

for.body124:                                      ; preds = %for.cond121
  %mul125 = mul nsw i32 %i.4, 80, !taffo.info !33, !taffo.initweight !29, !taffo.constinfo !40
  %add126 = add nsw i32 %mul125, %j.4, !taffo.info !33, !taffo.initweight !29
  %rem = srem i32 %add126, 20, !taffo.info !59, !taffo.initweight !32, !taffo.constinfo !40
  %cmp127 = icmp eq i32 %rem, 0, !taffo.info !25, !taffo.initweight !35
  br i1 %cmp127, label %if.then, label %if.end, !taffo.info !30, !taffo.initweight !61

if.then:                                          ; preds = %for.body124
  %tmp10 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp10, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.5, i32 0, i32 0)), !taffo.constinfo !62
  br label %if.end

if.end:                                           ; preds = %if.then, %for.body124
  %tmp11 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %idxprom129 = sext i32 %i.4 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx130 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom129, !taffo.info !13, !taffo.initweight !19
  %idxprom131 = sext i32 %j.4 to i64, !taffo.info !33, !taffo.initweight !29
  %arrayidx132 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx130, i64 0, i64 %idxprom131, !taffo.info !13, !taffo.initweight !29
  %tmp12 = load double, double* %arrayidx132, align 8, !taffo.info !13, !taffo.initweight !32
  %call133 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp11, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.6, i32 0, i32 0), double %tmp12), !taffo.info !20, !taffo.initweight !35, !taffo.constinfo !63
  br label %for.inc134

for.inc134:                                       ; preds = %if.end
  %inc135 = add nsw i32 %j.4, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
  br label %for.cond121

for.end136:                                       ; preds = %for.cond121
  br label %for.inc137

for.inc137:                                       ; preds = %for.end136
  %inc138 = add nsw i32 %i.4, 1, !taffo.info !27, !taffo.initweight !29, !taffo.constinfo !40
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
!12 = !{i32 0}
!13 = !{!14, !15, !11, i2 1}
!14 = !{!"fixp", i32 -32, i32 4}
!15 = !{double -1.000100e+08, double 1.001000e+08}
!16 = !{!9, !17, !11, i2 -1}
!17 = !{double -5.000000e+03, double 5.000000e+03}
!18 = !{!9, i1 false, !11, i2 -1}
!19 = !{i32 1}
!20 = !{!14, i1 false, !11, i2 1}
!21 = !{!22, i1 false, !11, i2 -1}
!22 = !{!"fixp", i32 -32, i32 18}
!23 = !{i1 false, !24, i1 false, i2 0}
!24 = !{double 1.000000e+02, double 1.000000e+02}
!25 = !{i1 false, !26, i1 false, i2 0}
!26 = !{double 0.000000e+00, double 1.000000e+00}
!27 = !{i1 false, !28, i1 false, i2 0}
!28 = !{double 1.000000e+00, double 1.000000e+00}
!29 = !{i32 2}
!30 = !{i1 false, !31, i1 false, i2 0}
!31 = !{double 1.000000e+00, double 1.000000e+02}
!32 = !{i32 3}
!33 = !{i1 false, !34, i1 false, i2 0}
!34 = !{double 0.000000e+00, double 0.000000e+00}
!35 = !{i32 4}
!36 = !{i1 false, !37}
!37 = !{i1 false, !38, i1 false, i2 0}
!38 = !{double 8.000000e+01, double 8.000000e+01}
!39 = !{i1 false, !10, !11, i2 -1}
!40 = !{i1 false, i1 false}
!41 = !{i1 false, !17, !11, i2 -1}
!42 = !{!33, i1 false}
!43 = !{!9, !44, !11, i2 -1}
!44 = !{double -1.500000e+04, double 1.500000e+04}
!45 = !{!46, !47, !11, i2 -1}
!46 = !{!"fixp", i32 -32, i32 25}
!47 = !{double -5.000000e+01, double 5.000000e+01}
!48 = !{i1 false, !49, !11, i2 1}
!49 = !{double -1.000000e+04, double 1.000000e+05}
!50 = !{!14, !51, !11, i2 -1}
!51 = !{double -1.000000e+08, double 1.000000e+08}
!52 = !{!14, !49, !11, i2 1}
!53 = !{!54, !55, !11, i2 1}
!54 = !{!"fixp", i32 -32, i32 11}
!55 = !{double 0xC12ED4340A57EB50, double 0x412EDB4E38E38E39}
!56 = !{i1 false, !57}
!57 = !{i1 false, !58, i1 false, i2 0}
!58 = !{double 9.900000e+01, double 9.900000e+01}
!59 = !{i1 false, !60, i1 false, i2 0}
!60 = !{double -2.000000e+01, double 0.000000e+00}
!61 = !{i32 5}
!62 = !{i1 false, i1 false, i1 false}
!63 = !{i1 false, i1 false, i1 false, i1 false}
