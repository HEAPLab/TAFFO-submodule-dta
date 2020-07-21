; ModuleID = 'polybench_edited/corr/corr.fixp.3.magiclangtmp.ll'
source_filename = "polybench_edited/corr/corr.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str.9 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1, !taffo.info !0
@.str.10 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !2

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !6 !taffo.funinfo !6 {
entry:
  %mean = alloca [32 x double], align 16, !taffo.info !7, !taffo.initweight !11
  %data = alloca [28 x [32 x double]], align 16, !taffo.info !12, !taffo.initweight !11
  %corr = alloca [32 x [32 x double]], align 16, !taffo.info !15, !taffo.initweight !11
  %stddev = alloca [32 x double], align 16, !taffo.info !18, !taffo.initweight !11
  %mean1 = bitcast [32 x double]* %mean to i8*, !taffo.info !21, !taffo.initweight !22
  %data2 = bitcast [28 x [32 x double]]* %data to i8*, !taffo.info !23, !taffo.initweight !22
  %corr3 = bitcast [32 x [32 x double]]* %corr to i8*, !taffo.info !24, !taffo.initweight !22
  %stddev4 = bitcast [32 x double]* %stddev to i8*, !taffo.info !25, !taffo.initweight !22
  br label %for.cond

for.cond:                                         ; preds = %for.inc16, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc17, %for.inc16 ], !taffo.info !26
  %cmp = icmp slt i32 %i.0, 28, !taffo.info !28, !taffo.initweight !29
  br i1 %cmp, label %for.body, label %for.end18, !taffo.info !28, !taffo.initweight !30

for.body:                                         ; preds = %for.cond
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ], !taffo.info !31
  %cmp10 = icmp slt i32 %j.0, 32, !taffo.info !33, !taffo.initweight !29
  br i1 %cmp10, label %for.body11, label %for.end, !taffo.info !33, !taffo.initweight !30

for.body11:                                       ; preds = %for.cond9
  %mul = mul nsw i32 %i.0, %j.0, !taffo.info !34, !taffo.initweight !29
  %conv = sitofp i32 %mul to double, !taffo.info !28, !taffo.initweight !30
  %div = fdiv double %conv, 3.200000e+01, !taffo.info !36, !taffo.initweight !38, !taffo.constinfo !39
  %conv12 = sitofp i32 %i.0 to double, !taffo.info !34, !taffo.initweight !29
  %add = fadd double %div, %conv12, !taffo.info !42, !taffo.initweight !30
  %div13 = fdiv double %add, 2.800000e+01, !taffo.info !44, !taffo.initweight !38, !taffo.constinfo !46
  %idxprom = sext i32 %i.0 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom, !taffo.info !12, !taffo.initweight !22
  %idxprom14 = sext i32 %j.0 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx15 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx, i64 0, i64 %idxprom14, !taffo.info !12, !taffo.initweight !29
  store double %div13, double* %arrayidx15, align 8, !taffo.info !49, !taffo.initweight !30
  br label %for.inc

for.inc:                                          ; preds = %for.body11
  %inc = add nsw i32 %j.0, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc16

for.inc16:                                        ; preds = %for.end
  %inc17 = add nsw i32 %i.0, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond

for.end18:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc43, %for.end18
  %j.1 = phi i32 [ 0, %for.end18 ], [ %inc44, %for.inc43 ], !taffo.info !31
  %cmp21 = icmp slt i32 %j.1, 32, !taffo.info !33, !taffo.initweight !29
  br i1 %cmp21, label %for.body23, label %for.end45, !taffo.info !33, !taffo.initweight !30

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx25 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom24, !taffo.info !7, !taffo.initweight !22
  store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.info !53, !taffo.initweight !29, !taffo.constinfo !54
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc37, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc38, %for.inc37 ], !taffo.info !26
  %cmp27 = icmp slt i32 %i.1, 28, !taffo.info !28, !taffo.initweight !29
  br i1 %cmp27, label %for.body29, label %for.end39, !taffo.info !28, !taffo.initweight !30

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx31 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom30, !taffo.info !12, !taffo.initweight !22
  %idxprom32 = sext i32 %j.1 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx33 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx31, i64 0, i64 %idxprom32, !taffo.info !12, !taffo.initweight !29
  %tmp = load double, double* %arrayidx33, align 8, !taffo.info !12, !taffo.initweight !30
  %idxprom34 = sext i32 %j.1 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx35 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom34, !taffo.info !7, !taffo.initweight !22
  %tmp1 = load double, double* %arrayidx35, align 8, !taffo.info !7, !taffo.initweight !29
  %add36 = fadd double %tmp1, %tmp, !taffo.info !56, !taffo.initweight !30
  store double %add36, double* %arrayidx35, align 8, !taffo.info !53, !taffo.initweight !29
  br label %for.inc37

for.inc37:                                        ; preds = %for.body29
  %inc38 = add nsw i32 %i.1, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond26

for.end39:                                        ; preds = %for.cond26
  %idxprom40 = sext i32 %j.1 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx41 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom40, !taffo.info !7, !taffo.initweight !22
  %tmp2 = load double, double* %arrayidx41, align 8, !taffo.info !7, !taffo.initweight !29
  %div42 = fdiv double %tmp2, 2.800000e+01, !taffo.info !58, !taffo.initweight !29, !taffo.constinfo !46
  store double %div42, double* %arrayidx41, align 8, !taffo.info !53, !taffo.initweight !29
  br label %for.inc43

for.inc43:                                        ; preds = %for.end39
  %inc44 = add nsw i32 %j.1, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond20

for.end45:                                        ; preds = %for.cond20
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc91, %for.end45
  %j.2 = phi i32 [ 0, %for.end45 ], [ %inc92, %for.inc91 ], !taffo.info !31
  %cmp47 = icmp slt i32 %j.2, 32, !taffo.info !33, !taffo.initweight !29
  br i1 %cmp47, label %for.body49, label %for.end93, !taffo.info !33, !taffo.initweight !30

for.body49:                                       ; preds = %for.cond46
  %idxprom50 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx51 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom50, !taffo.info !18, !taffo.initweight !22
  store double 0.000000e+00, double* %arrayidx51, align 8, !taffo.info !61, !taffo.initweight !29, !taffo.constinfo !54
  br label %for.cond52

for.cond52:                                       ; preds = %for.inc73, %for.body49
  %i.2 = phi i32 [ 0, %for.body49 ], [ %inc74, %for.inc73 ], !taffo.info !26
  %cmp53 = icmp slt i32 %i.2, 28, !taffo.info !28, !taffo.initweight !29
  br i1 %cmp53, label %for.body55, label %for.end75, !taffo.info !28, !taffo.initweight !30

for.body55:                                       ; preds = %for.cond52
  %idxprom56 = sext i32 %i.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx57 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom56, !taffo.info !12, !taffo.initweight !22
  %idxprom58 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx59 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx57, i64 0, i64 %idxprom58, !taffo.info !12, !taffo.initweight !29
  %tmp3 = load double, double* %arrayidx59, align 8, !taffo.info !12, !taffo.initweight !30
  %idxprom60 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx61 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom60, !taffo.info !7, !taffo.initweight !22
  %tmp4 = load double, double* %arrayidx61, align 8, !taffo.info !7, !taffo.initweight !29
  %sub = fsub double %tmp3, %tmp4, !taffo.info !56, !taffo.initweight !30
  %idxprom62 = sext i32 %i.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx63 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom62, !taffo.info !12, !taffo.initweight !22
  %idxprom64 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx65 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx63, i64 0, i64 %idxprom64, !taffo.info !12, !taffo.initweight !29
  %tmp5 = load double, double* %arrayidx65, align 8, !taffo.info !12, !taffo.initweight !30
  %idxprom66 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx67 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom66, !taffo.info !7, !taffo.initweight !22
  %tmp6 = load double, double* %arrayidx67, align 8, !taffo.info !7, !taffo.initweight !29
  %sub68 = fsub double %tmp5, %tmp6, !taffo.info !56, !taffo.initweight !30
  %mul69 = fmul double %sub, %sub68, !taffo.info !62, !taffo.initweight !38
  %idxprom70 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx71 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom70, !taffo.info !18, !taffo.initweight !22
  %tmp7 = load double, double* %arrayidx71, align 8, !taffo.info !18, !taffo.initweight !29
  %add72 = fadd double %tmp7, %mul69, !taffo.info !65, !taffo.initweight !30
  store double %add72, double* %arrayidx71, align 8, !taffo.info !61, !taffo.initweight !29
  br label %for.inc73

for.inc73:                                        ; preds = %for.body55
  %inc74 = add nsw i32 %i.2, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond52

for.end75:                                        ; preds = %for.cond52
  %idxprom76 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx77 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom76, !taffo.info !18, !taffo.initweight !22
  %tmp8 = load double, double* %arrayidx77, align 8, !taffo.info !18, !taffo.initweight !29
  %div78 = fdiv double %tmp8, 2.800000e+01, !taffo.info !67, !taffo.initweight !29, !taffo.constinfo !46
  store double %div78, double* %arrayidx77, align 8, !taffo.info !61, !taffo.initweight !29
  %idxprom79 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx80 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom79, !taffo.info !18, !taffo.initweight !22
  %tmp9 = load double, double* %arrayidx80, align 8, !taffo.info !18, !taffo.initweight !29
  %call = call double @sqrt(double %tmp9) #3, !taffo.info !70, !taffo.initweight !30, !taffo.constinfo !52
  %idxprom81 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx82 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom81, !taffo.info !18, !taffo.initweight !22
  store double %call, double* %arrayidx82, align 8, !taffo.info !61, !taffo.initweight !29
  %idxprom83 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx84 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom83, !taffo.info !18, !taffo.initweight !22
  %tmp10 = load double, double* %arrayidx84, align 8, !taffo.info !18, !taffo.initweight !29
  %cmp85 = fcmp ole double %tmp10, 1.000000e-01, !taffo.info !25, !taffo.initweight !29
  br i1 %cmp85, label %cond.true, label %cond.false, !taffo.info !73, !taffo.initweight !30

cond.true:                                        ; preds = %for.end75
  br label %cond.end

cond.false:                                       ; preds = %for.end75
  %idxprom87 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx88 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom87, !taffo.info !18, !taffo.initweight !22
  %tmp11 = load double, double* %arrayidx88, align 8, !taffo.info !18, !taffo.initweight !29
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !18, !taffo.initweight !30
  %idxprom89 = sext i32 %j.2 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx90 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom89, !taffo.info !18, !taffo.initweight !22
  store double %cond, double* %arrayidx90, align 8, !taffo.info !61, !taffo.initweight !29
  br label %for.inc91

for.inc91:                                        ; preds = %cond.end
  %inc92 = add nsw i32 %j.2, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond46

for.end93:                                        ; preds = %for.cond46
  br label %for.cond94

for.cond94:                                       ; preds = %for.inc121, %for.end93
  %i.3 = phi i32 [ 0, %for.end93 ], [ %inc122, %for.inc121 ], !taffo.info !26
  %cmp95 = icmp slt i32 %i.3, 28, !taffo.info !28, !taffo.initweight !29
  br i1 %cmp95, label %for.body97, label %for.end123, !taffo.info !28, !taffo.initweight !30

for.body97:                                       ; preds = %for.cond94
  br label %for.cond98

for.cond98:                                       ; preds = %for.inc118, %for.body97
  %j.3 = phi i32 [ 0, %for.body97 ], [ %inc119, %for.inc118 ], !taffo.info !31
  %cmp99 = icmp slt i32 %j.3, 32, !taffo.info !33, !taffo.initweight !29
  br i1 %cmp99, label %for.body101, label %for.end120, !taffo.info !33, !taffo.initweight !30

for.body101:                                      ; preds = %for.cond98
  %idxprom102 = sext i32 %j.3 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx103 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom102, !taffo.info !7, !taffo.initweight !22
  %tmp12 = load double, double* %arrayidx103, align 8, !taffo.info !7, !taffo.initweight !29
  %idxprom104 = sext i32 %i.3 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx105 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom104, !taffo.info !12, !taffo.initweight !22
  %idxprom106 = sext i32 %j.3 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx107 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx105, i64 0, i64 %idxprom106, !taffo.info !12, !taffo.initweight !29
  %tmp13 = load double, double* %arrayidx107, align 8, !taffo.info !12, !taffo.initweight !30
  %sub108 = fsub double %tmp13, %tmp12, !taffo.info !56, !taffo.initweight !30
  store double %sub108, double* %arrayidx107, align 8, !taffo.info !49, !taffo.initweight !30
  %call109 = call double @sqrt(double 2.800000e+01) #3, !taffo.info !74, !taffo.initweight !29, !taffo.constinfo !76
  %idxprom110 = sext i32 %j.3 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx111 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom110, !taffo.info !18, !taffo.initweight !22
  %tmp14 = load double, double* %arrayidx111, align 8, !taffo.info !77, !taffo.initweight !29
  %mul112 = fmul double %call109, %tmp14, !taffo.info !79, !taffo.initweight !30
  %idxprom113 = sext i32 %i.3 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx114 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom113, !taffo.info !12, !taffo.initweight !22
  %idxprom115 = sext i32 %j.3 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx116 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx114, i64 0, i64 %idxprom115, !taffo.info !12, !taffo.initweight !29
  %tmp15 = load double, double* %arrayidx116, align 8, !taffo.info !12, !taffo.initweight !30
  %div117 = fdiv double %tmp15, %mul112, !taffo.info !81, !taffo.initweight !38
  store double %div117, double* %arrayidx116, align 8, !taffo.info !49, !taffo.initweight !30
  br label %for.inc118

for.inc118:                                       ; preds = %for.body101
  %inc119 = add nsw i32 %j.3, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond98

for.end120:                                       ; preds = %for.cond98
  br label %for.inc121

for.inc121:                                       ; preds = %for.end120
  %inc122 = add nsw i32 %i.3, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond94

for.end123:                                       ; preds = %for.cond94
  br label %for.cond124

for.cond124:                                      ; preds = %for.inc173, %for.end123
  %i.4 = phi i32 [ 0, %for.end123 ], [ %inc174, %for.inc173 ], !taffo.info !26
  %cmp125 = icmp slt i32 %i.4, 31, !taffo.info !28, !taffo.initweight !29
  br i1 %cmp125, label %for.body127, label %for.end175, !taffo.info !28, !taffo.initweight !30

for.body127:                                      ; preds = %for.cond124
  %idxprom128 = sext i32 %i.4 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx129 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom128, !taffo.info !15, !taffo.initweight !22
  %idxprom130 = sext i32 %i.4 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx131 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx129, i64 0, i64 %idxprom130, !taffo.info !15, !taffo.initweight !29
  store double 1.000000e+00, double* %arrayidx131, align 8, !taffo.info !84, !taffo.initweight !30, !taffo.constinfo !85
  %add132 = add nsw i32 %i.4, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond133

for.cond133:                                      ; preds = %for.inc170, %for.body127
  %j.4 = phi i32 [ %add132, %for.body127 ], [ %inc171, %for.inc170 ], !taffo.info !26
  %cmp134 = icmp slt i32 %j.4, 32, !taffo.info !33, !taffo.initweight !29
  br i1 %cmp134, label %for.body136, label %for.end172, !taffo.info !33, !taffo.initweight !30

for.body136:                                      ; preds = %for.cond133
  %idxprom137 = sext i32 %i.4 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx138 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom137, !taffo.info !15, !taffo.initweight !22
  %idxprom139 = sext i32 %j.4 to i64, !taffo.info !28, !taffo.initweight !29
  %arrayidx140 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx138, i64 0, i64 %idxprom139, !taffo.info !15, !taffo.initweight !29
  store double 0.000000e+00, double* %arrayidx140, align 8, !taffo.info !84, !taffo.initweight !30, !taffo.constinfo !54
  br label %for.cond141

for.cond141:                                      ; preds = %for.inc159, %for.body136
  %k.0 = phi i32 [ 0, %for.body136 ], [ %inc160, %for.inc159 ], !taffo.info !31
  %cmp142 = icmp slt i32 %k.0, 28, !taffo.info !33, !taffo.initweight !29
  br i1 %cmp142, label %for.body144, label %for.end161, !taffo.info !33, !taffo.initweight !30

for.body144:                                      ; preds = %for.cond141
  %idxprom145 = sext i32 %k.0 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx146 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom145, !taffo.info !12, !taffo.initweight !22
  %idxprom147 = sext i32 %i.4 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx148 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx146, i64 0, i64 %idxprom147, !taffo.info !12, !taffo.initweight !29
  %tmp16 = load double, double* %arrayidx148, align 8, !taffo.info !12, !taffo.initweight !30
  %idxprom149 = sext i32 %k.0 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx150 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom149, !taffo.info !12, !taffo.initweight !22
  %idxprom151 = sext i32 %j.4 to i64, !taffo.info !28, !taffo.initweight !29
  %arrayidx152 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx150, i64 0, i64 %idxprom151, !taffo.info !12, !taffo.initweight !29
  %tmp17 = load double, double* %arrayidx152, align 8, !taffo.info !12, !taffo.initweight !30
  %mul153 = fmul double %tmp16, %tmp17, !taffo.info !87, !taffo.initweight !38
  %idxprom154 = sext i32 %i.4 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx155 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom154, !taffo.info !15, !taffo.initweight !22
  %idxprom156 = sext i32 %j.4 to i64, !taffo.info !28, !taffo.initweight !29
  %arrayidx157 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx155, i64 0, i64 %idxprom156, !taffo.info !15, !taffo.initweight !29
  %tmp18 = load double, double* %arrayidx157, align 8, !taffo.info !15, !taffo.initweight !30
  %add158 = fadd double %tmp18, %mul153, !taffo.info !90, !taffo.initweight !38
  store double %add158, double* %arrayidx157, align 8, !taffo.info !84, !taffo.initweight !30
  br label %for.inc159

for.inc159:                                       ; preds = %for.body144
  %inc160 = add nsw i32 %k.0, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond141

for.end161:                                       ; preds = %for.cond141
  %idxprom162 = sext i32 %i.4 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx163 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom162, !taffo.info !15, !taffo.initweight !22
  %idxprom164 = sext i32 %j.4 to i64, !taffo.info !28, !taffo.initweight !29
  %arrayidx165 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx163, i64 0, i64 %idxprom164, !taffo.info !15, !taffo.initweight !29
  %tmp19 = load double, double* %arrayidx165, align 8, !taffo.info !15, !taffo.initweight !30
  %idxprom166 = sext i32 %j.4 to i64, !taffo.info !28, !taffo.initweight !29
  %arrayidx167 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom166, !taffo.info !15, !taffo.initweight !22
  %idxprom168 = sext i32 %i.4 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx169 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx167, i64 0, i64 %idxprom168, !taffo.info !15, !taffo.initweight !29
  store double %tmp19, double* %arrayidx169, align 8, !taffo.info !84, !taffo.initweight !30
  br label %for.inc170

for.inc170:                                       ; preds = %for.end161
  %inc171 = add nsw i32 %j.4, 1, !taffo.info !92, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond133

for.end172:                                       ; preds = %for.cond133
  br label %for.inc173

for.inc173:                                       ; preds = %for.end172
  %inc174 = add nsw i32 %i.4, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond124

for.end175:                                       ; preds = %for.cond124
  %arrayidx176 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 31, !taffo.info !15, !taffo.initweight !22
  %arrayidx177 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx176, i64 0, i64 31, !taffo.info !15, !taffo.initweight !29
  store double 1.000000e+00, double* %arrayidx177, align 8, !taffo.info !84, !taffo.initweight !30, !taffo.constinfo !85
  br label %for.cond178

for.cond178:                                      ; preds = %for.inc195, %for.end175
  %i.5 = phi i32 [ 0, %for.end175 ], [ %inc196, %for.inc195 ], !taffo.info !26
  %cmp179 = icmp slt i32 %i.5, 32, !taffo.info !28, !taffo.initweight !29
  br i1 %cmp179, label %for.body181, label %for.end197, !taffo.info !28, !taffo.initweight !30

for.body181:                                      ; preds = %for.cond178
  br label %for.cond182

for.cond182:                                      ; preds = %for.inc191, %for.body181
  %j.5 = phi i32 [ 0, %for.body181 ], [ %inc192, %for.inc191 ], !taffo.info !31
  %cmp183 = icmp slt i32 %j.5, 32, !taffo.info !33, !taffo.initweight !29
  br i1 %cmp183, label %for.body185, label %for.end193, !taffo.info !33, !taffo.initweight !30

for.body185:                                      ; preds = %for.cond182
  %idxprom186 = sext i32 %i.5 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx187 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom186, !taffo.info !15, !taffo.initweight !22
  %idxprom188 = sext i32 %j.5 to i64, !taffo.info !34, !taffo.initweight !29
  %arrayidx189 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx187, i64 0, i64 %idxprom188, !taffo.info !15, !taffo.initweight !29
  %tmp20 = load double, double* %arrayidx189, align 8, !taffo.info !15, !taffo.initweight !30
  %call190 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.9, i32 0, i32 0), double %tmp20), !taffo.info !24, !taffo.initweight !38, !taffo.constinfo !94
  br label %for.inc191

for.inc191:                                       ; preds = %for.body185
  %inc192 = add nsw i32 %j.5, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond182

for.end193:                                       ; preds = %for.cond182
  %call194 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.10, i32 0, i32 0)), !taffo.constinfo !52
  br label %for.inc195

for.inc195:                                       ; preds = %for.end193
  %inc196 = add nsw i32 %i.5, 1, !taffo.info !50, !taffo.initweight !29, !taffo.constinfo !52
  br label %for.cond178

for.end197:                                       ; preds = %for.cond178
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !95 !taffo.funinfo !96 dso_local double @sqrt(double) #1

declare !taffo.initweight !95 !taffo.funinfo !96 dso_local i32 @printf(i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!4}
!llvm.ident = !{!5}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 1.080000e+02}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.000000e+01}
!4 = !{i32 1, !"wchar_size", i32 4}
!5 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!6 = !{}
!7 = !{!8, !9, !10, i2 -1}
!8 = !{!"fixp", i32 -32, i32 15}
!9 = !{double -5.000000e+04, double 5.000000e+04}
!10 = !{double 1.000000e-100}
!11 = !{i32 0}
!12 = !{!13, !14, !10, i2 -1}
!13 = !{!"fixp", i32 -32, i32 27}
!14 = !{double -1.000000e+01, double 1.000000e+01}
!15 = !{!16, !17, !10, i2 -1}
!16 = !{!"fixp", i32 32, i32 29}
!17 = !{double 0.000000e+00, double 5.000000e+00}
!18 = !{!19, !20, !10, i2 -1}
!19 = !{!"fixp", i32 -32, i32 18}
!20 = !{double -4.096000e+03, double 4.096000e+03}
!21 = !{!8, i1 false, !10, i2 -1}
!22 = !{i32 1}
!23 = !{!13, i1 false, !10, i2 -1}
!24 = !{!16, i1 false, !10, i2 -1}
!25 = !{!19, i1 false, !10, i2 -1}
!26 = !{i1 false, !27, i1 false, i2 0}
!27 = !{double 0.000000e+00, double 2.800000e+01}
!28 = !{i1 false, !27, i1 false, i2 -2}
!29 = !{i32 2}
!30 = !{i32 3}
!31 = !{i1 false, !32, i1 false, i2 0}
!32 = !{double 0.000000e+00, double 3.200000e+01}
!33 = !{i1 false, !32, i1 false, i2 -2}
!34 = !{i1 false, !35, i1 false, i2 -2}
!35 = !{double 0.000000e+00, double 0.000000e+00}
!36 = !{i1 false, !37, i1 false, i2 -2}
!37 = !{double 0.000000e+00, double 8.750000e-01}
!38 = !{i32 4}
!39 = !{i1 false, !40}
!40 = !{i1 false, !41, i1 false, i2 0}
!41 = !{double 3.200000e+01, double 3.200000e+01}
!42 = !{i1 false, !43, i1 false, i2 -2}
!43 = !{double 0.000000e+00, double 2.887500e+01}
!44 = !{i1 false, !45, i1 false, i2 -2}
!45 = !{double 0.000000e+00, double 1.031250e+00}
!46 = !{i1 false, !47}
!47 = !{i1 false, !48, i1 false, i2 0}
!48 = !{double 2.800000e+01, double 2.800000e+01}
!49 = !{i1 false, !14, !10, i2 -1}
!50 = !{i1 false, !51, i1 false, i2 -2}
!51 = !{double 1.000000e+00, double 1.000000e+00}
!52 = !{i1 false, i1 false}
!53 = !{i1 false, !9, !10, i2 -1}
!54 = !{!55, i1 false}
!55 = !{i1 false, !35, i1 false, i2 0}
!56 = !{!8, !57, !10, i2 -1}
!57 = !{double -5.001000e+04, double 5.001000e+04}
!58 = !{!59, !60, !10, i2 1}
!59 = !{!"fixp", i32 -32, i32 20}
!60 = !{double 0xC09BE6DB6DB6DB6E, double 0x409BE6DB6DB6DB6E}
!61 = !{i1 false, !20, !10, i2 -1}
!62 = !{!63, !64, !10, i2 -1}
!63 = !{!"fixp", i32 -64, i32 31}
!64 = !{double 0xC1E2A24774800000, double 0x41E2A24774800000}
!65 = !{!63, !66, !10, i2 -1}
!66 = !{double 0xC1E2A24974800000, double 0x41E2A24974800000}
!67 = !{!68, !69, !10, i2 1}
!68 = !{!"fixp", i32 -32, i32 23}
!69 = !{double 0xC062492492492492, double 0x4062492492492492}
!70 = !{!71, !72, !10, i2 -1}
!71 = !{!"fixp", i32 32, i32 25}
!72 = !{double 0.000000e+00, double 6.400000e+01}
!73 = !{i1 false, i1 false, i1 false, i2 1}
!74 = !{!16, !75, !10, i2 1}
!75 = !{double 0x40152A7FA9D2F8EA, double 0x40152A7FA9D2F8EA}
!76 = !{!47, i1 false}
!77 = !{!78, !20, !10, i2 -1}
!78 = !{!"fixp", i32 -32, i32 16}
!79 = !{!78, !80, !10, i2 -1}
!80 = !{double 0xC0D52A7FA9D2F8EA, double 0x40D52A7FA9D2F8EA}
!81 = !{!82, !83, !10, i2 -1}
!82 = !{!"fixp", i32 -32, i32 30}
!83 = !{double 0xBF3E3CB66051F5E0, double 0x3F3E3CB66051F5E0}
!84 = !{i1 false, !17, !10, i2 -1}
!85 = !{!86, i1 false}
!86 = !{i1 false, !51, i1 false, i2 0}
!87 = !{!88, !89, !10, i2 -1}
!88 = !{!"fixp", i32 -32, i32 24}
!89 = !{double -1.000000e+02, double 1.000000e+02}
!90 = !{!88, !91, !10, i2 -1}
!91 = !{double -1.000000e+02, double 1.050000e+02}
!92 = !{i1 false, !93, i1 false, i2 -2}
!93 = !{double 1.000000e+00, double 2.900000e+01}
!94 = !{i1 false, i1 false, i1 false}
!95 = !{i32 -1}
!96 = !{i32 0, i1 false}
