; ModuleID = 'polybench_edited/corr/corr.fixp.4.magiclangtmp.ll'
source_filename = "polybench_edited/corr/corr.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str.9 = private unnamed_addr constant [7 x i8] c"%.10f \00", align 1, !taffo.info !0
@.str.10 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !2

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !6 !taffo.funinfo !6 {
entry:
  %mean = alloca [32 x double], align 16, !taffo.info !7, !taffo.initweight !11
  %data = alloca [28 x [32 x double]], align 16, !taffo.info !12, !taffo.initweight !11
  %corr = alloca [32 x [32 x double]], align 16, !taffo.info !14, !taffo.initweight !11
  %stddev = alloca [32 x double], align 16, !taffo.info !16, !taffo.initweight !11
  br label %for.cond

for.cond:                                         ; preds = %for.inc16, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc17, %for.inc16 ]
  %cmp = icmp slt i32 %i.0, 28, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp, label %for.body, label %for.end18, !taffo.info !18, !taffo.initweight !21

for.body:                                         ; preds = %for.cond
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %j.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ]
  %cmp10 = icmp slt i32 %j.0, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp10, label %for.body11, label %for.end, !taffo.info !22, !taffo.initweight !21

for.body11:                                       ; preds = %for.cond9
  %mul = mul nsw i32 %i.0, %j.0, !taffo.info !18, !taffo.initweight !20
  %conv = sitofp i32 %mul to double, !taffo.info !18, !taffo.initweight !21
  %div = fdiv double %conv, 3.200000e+01, !taffo.info !18, !taffo.initweight !24, !taffo.constinfo !25
  %conv12 = sitofp i32 %i.0 to double, !taffo.info !18, !taffo.initweight !20
  %add = fadd double %div, %conv12, !taffo.info !18, !taffo.initweight !21
  %div13 = fdiv double %add, 2.800000e+01, !taffo.info !18, !taffo.initweight !24, !taffo.constinfo !28
  %idxprom = sext i32 %i.0 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom, !taffo.info !12, !taffo.initweight !31
  %idxprom14 = sext i32 %j.0 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx15.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx.flt.2flp, i64 0, i64 %idxprom14, !taffo.info !12, !taffo.initweight !20
  store double %div13, double* %arrayidx15.flt.2flp, align 8, !taffo.info !32
  br label %for.inc

for.inc:                                          ; preds = %for.body11
  %inc = add nsw i32 %j.0, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc16

for.inc16:                                        ; preds = %for.end
  %inc17 = add nsw i32 %i.0, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond

for.end18:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc43, %for.end18
  %j.1 = phi i32 [ 0, %for.end18 ], [ %inc44, %for.inc43 ]
  %cmp21 = icmp slt i32 %j.1, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp21, label %for.body23, label %for.end45, !taffo.info !22, !taffo.initweight !21

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx25.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom24, !taffo.info !7, !taffo.initweight !31
  store double 0.000000e+00, double* %arrayidx25.flt.2flp, align 8, !taffo.info !34, !taffo.constinfo !35
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc37, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc38, %for.inc37 ]
  %cmp27 = icmp slt i32 %i.1, 28, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp27, label %for.body29, label %for.end39, !taffo.info !18, !taffo.initweight !21

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx31.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom30, !taffo.info !12, !taffo.initweight !31
  %idxprom32 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx33.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx31.flt.2flp, i64 0, i64 %idxprom32, !taffo.info !12, !taffo.initweight !20
  %tmp.flt.fallback.2flp = load double, double* %arrayidx33.flt.2flp, align 8, !taffo.info !12, !taffo.initweight !21
  %idxprom34 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx35.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom34, !taffo.info !7, !taffo.initweight !31
  %tmp1.flt.fallback.2flp = load double, double* %arrayidx35.flt.2flp, align 8, !taffo.info !7, !taffo.initweight !20
  %add36.2flp = fadd double %tmp1.flt.fallback.2flp, %tmp.flt.fallback.2flp, !taffo.info !7
  store double %add36.2flp, double* %arrayidx35.flt.2flp, align 8, !taffo.info !34
  br label %for.inc37

for.inc37:                                        ; preds = %for.body29
  %inc38 = add nsw i32 %i.1, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond26

for.end39:                                        ; preds = %for.cond26
  %idxprom40 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx41.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom40, !taffo.info !7, !taffo.initweight !31
  %tmp2.flt.fallback.2flp = load double, double* %arrayidx41.flt.2flp, align 8, !taffo.info !7, !taffo.initweight !20
  %div42.2flp = fdiv double %tmp2.flt.fallback.2flp, 2.800000e+01, !taffo.info !38, !taffo.constinfo !28
  store double %div42.2flp, double* %arrayidx41.flt.2flp, align 8, !taffo.info !34
  br label %for.inc43

for.inc43:                                        ; preds = %for.end39
  %inc44 = add nsw i32 %j.1, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond20

for.end45:                                        ; preds = %for.cond20
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc91, %for.end45
  %j.2 = phi i32 [ 0, %for.end45 ], [ %inc92, %for.inc91 ]
  %cmp47 = icmp slt i32 %j.2, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp47, label %for.body49, label %for.end93, !taffo.info !22, !taffo.initweight !21

for.body49:                                       ; preds = %for.cond46
  %idxprom50 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx51.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom50, !taffo.info !16, !taffo.initweight !31
  store double 0.000000e+00, double* %arrayidx51.flt.2flp, align 8, !taffo.info !40, !taffo.constinfo !35
  br label %for.cond52

for.cond52:                                       ; preds = %for.inc73, %for.body49
  %i.2 = phi i32 [ 0, %for.body49 ], [ %inc74, %for.inc73 ]
  %cmp53 = icmp slt i32 %i.2, 28, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp53, label %for.body55, label %for.end75, !taffo.info !18, !taffo.initweight !21

for.body55:                                       ; preds = %for.cond52
  %idxprom56 = sext i32 %i.2 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx57.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom56, !taffo.info !12, !taffo.initweight !31
  %idxprom58 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx59.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx57.flt.2flp, i64 0, i64 %idxprom58, !taffo.info !12, !taffo.initweight !20
  %tmp3.flt.fallback.2flp = load double, double* %arrayidx59.flt.2flp, align 8, !taffo.info !12, !taffo.initweight !21
  %idxprom60 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx61.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom60, !taffo.info !7, !taffo.initweight !31
  %tmp4.flt.fallback.2flp = load double, double* %arrayidx61.flt.2flp, align 8, !taffo.info !7, !taffo.initweight !20
  %sub.2flp = fsub double %tmp3.flt.fallback.2flp, %tmp4.flt.fallback.2flp, !taffo.info !7
  %idxprom62 = sext i32 %i.2 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx63.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom62, !taffo.info !12, !taffo.initweight !31
  %idxprom64 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx65.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx63.flt.2flp, i64 0, i64 %idxprom64, !taffo.info !12, !taffo.initweight !20
  %tmp5.flt.fallback.2flp = load double, double* %arrayidx65.flt.2flp, align 8, !taffo.info !12, !taffo.initweight !21
  %idxprom66 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx67.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom66, !taffo.info !7, !taffo.initweight !31
  %tmp6.flt.fallback.2flp = load double, double* %arrayidx67.flt.2flp, align 8, !taffo.info !7, !taffo.initweight !20
  %sub68.2flp = fsub double %tmp5.flt.fallback.2flp, %tmp6.flt.fallback.2flp, !taffo.info !7
  %mul69.2flp = fmul double %sub.2flp, %sub68.2flp, !taffo.info !7
  %idxprom70 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx71.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom70, !taffo.info !16, !taffo.initweight !31
  %tmp7.flt.fallback.2flp = load double, double* %arrayidx71.flt.2flp, align 8, !taffo.info !16, !taffo.initweight !20
  %add72.2flp = fadd double %tmp7.flt.fallback.2flp, %mul69.2flp, !taffo.info !16
  store double %add72.2flp, double* %arrayidx71.flt.2flp, align 8, !taffo.info !40
  br label %for.inc73

for.inc73:                                        ; preds = %for.body55
  %inc74 = add nsw i32 %i.2, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond52

for.end75:                                        ; preds = %for.cond52
  %idxprom76 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx77.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom76, !taffo.info !16, !taffo.initweight !31
  %tmp8.flt.fallback.2flp = load double, double* %arrayidx77.flt.2flp, align 8, !taffo.info !16, !taffo.initweight !20
  %div78.2flp = fdiv double %tmp8.flt.fallback.2flp, 2.800000e+01, !taffo.info !38, !taffo.constinfo !28
  store double %div78.2flp, double* %arrayidx77.flt.2flp, align 8, !taffo.info !40
  %idxprom79 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx80.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom79, !taffo.info !16, !taffo.initweight !31
  %tmp9.flt.fallback.2flp = load double, double* %arrayidx80.flt.2flp, align 8, !taffo.info !16, !taffo.initweight !20
  %call.flt.fallback.2flp = call double @sqrt(double %tmp9.flt.fallback.2flp) #3, !taffo.info !16, !taffo.initweight !21, !taffo.constinfo !33
  %idxprom81 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx82.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom81, !taffo.info !16, !taffo.initweight !31
  store double %call.flt.fallback.2flp, double* %arrayidx82.flt.2flp, align 8, !taffo.info !40
  %idxprom83 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx84.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom83, !taffo.info !16, !taffo.initweight !31
  %tmp10.flt.fallback.2flp = load double, double* %arrayidx84.flt.2flp, align 8, !taffo.info !16, !taffo.initweight !20
  %0 = fcmp ole double %tmp10.flt.fallback.2flp, 1.000000e-01, !taffo.info !41
  br i1 %0, label %cond.true, label %cond.false, !taffo.info !43, !taffo.initweight !21

cond.true:                                        ; preds = %for.end75
  br label %cond.end

cond.false:                                       ; preds = %for.end75
  %idxprom87 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx88.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom87, !taffo.info !16, !taffo.initweight !31
  %tmp11.flt.fallback.2flp = load double, double* %arrayidx88.flt.2flp, align 8, !taffo.info !16, !taffo.initweight !20
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond.2flp = phi double [ 1.000000e+00, %cond.true ], [ %tmp11.flt.fallback.2flp, %cond.false ], !taffo.info !16
  %idxprom89 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx90.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom89, !taffo.info !16, !taffo.initweight !31
  store double %cond.2flp, double* %arrayidx90.flt.2flp, align 8, !taffo.info !40
  br label %for.inc91

for.inc91:                                        ; preds = %cond.end
  %inc92 = add nsw i32 %j.2, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond46

for.end93:                                        ; preds = %for.cond46
  br label %for.cond94

for.cond94:                                       ; preds = %for.inc121, %for.end93
  %i.3 = phi i32 [ 0, %for.end93 ], [ %inc122, %for.inc121 ]
  %cmp95 = icmp slt i32 %i.3, 28, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp95, label %for.body97, label %for.end123, !taffo.info !18, !taffo.initweight !21

for.body97:                                       ; preds = %for.cond94
  br label %for.cond98

for.cond98:                                       ; preds = %for.inc118, %for.body97
  %j.3 = phi i32 [ 0, %for.body97 ], [ %inc119, %for.inc118 ]
  %cmp99 = icmp slt i32 %j.3, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp99, label %for.body101, label %for.end120, !taffo.info !22, !taffo.initweight !21

for.body101:                                      ; preds = %for.cond98
  %idxprom102 = sext i32 %j.3 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx103.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom102, !taffo.info !7, !taffo.initweight !31
  %tmp12.flt.fallback.2flp = load double, double* %arrayidx103.flt.2flp, align 8, !taffo.info !7, !taffo.initweight !20
  %idxprom104 = sext i32 %i.3 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx105.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom104, !taffo.info !12, !taffo.initweight !31
  %idxprom106 = sext i32 %j.3 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx107.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx105.flt.2flp, i64 0, i64 %idxprom106, !taffo.info !12, !taffo.initweight !20
  %tmp13.flt.fallback.2flp = load double, double* %arrayidx107.flt.2flp, align 8, !taffo.info !12, !taffo.initweight !21
  %sub108.2flp = fsub double %tmp13.flt.fallback.2flp, %tmp12.flt.fallback.2flp, !taffo.info !7
  store double %sub108.2flp, double* %arrayidx107.flt.2flp, align 8, !taffo.info !32
  %call109.flt.fallback.2flp = call double @sqrt(double 2.800000e+01) #3, !taffo.info !38, !taffo.initweight !20, !taffo.constinfo !44
  %idxprom110 = sext i32 %j.3 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx111.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom110, !taffo.info !16, !taffo.initweight !31
  %tmp14.flt.fallback.2flp = load double, double* %arrayidx111.flt.2flp, align 8, !taffo.info !16, !taffo.initweight !20
  %mul112.2flp = fmul double %call109.flt.fallback.2flp, %tmp14.flt.fallback.2flp, !taffo.info !16
  %idxprom113 = sext i32 %i.3 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx114.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom113, !taffo.info !12, !taffo.initweight !31
  %idxprom115 = sext i32 %j.3 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx116.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx114.flt.2flp, i64 0, i64 %idxprom115, !taffo.info !12, !taffo.initweight !20
  %tmp15.flt.fallback.2flp = load double, double* %arrayidx116.flt.2flp, align 8, !taffo.info !12, !taffo.initweight !21
  %div117.2flp = fdiv double %tmp15.flt.fallback.2flp, %mul112.2flp, !taffo.info !12
  store double %div117.2flp, double* %arrayidx116.flt.2flp, align 8, !taffo.info !32
  br label %for.inc118

for.inc118:                                       ; preds = %for.body101
  %inc119 = add nsw i32 %j.3, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond98

for.end120:                                       ; preds = %for.cond98
  br label %for.inc121

for.inc121:                                       ; preds = %for.end120
  %inc122 = add nsw i32 %i.3, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond94

for.end123:                                       ; preds = %for.cond94
  br label %for.cond124

for.cond124:                                      ; preds = %for.inc173, %for.end123
  %i.4 = phi i32 [ 0, %for.end123 ], [ %inc174, %for.inc173 ]
  %cmp125 = icmp slt i32 %i.4, 31, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp125, label %for.body127, label %for.end175, !taffo.info !18, !taffo.initweight !21

for.body127:                                      ; preds = %for.cond124
  %idxprom128 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx129.flt.2flp = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom128, !taffo.info !14, !taffo.initweight !31
  %idxprom130 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx131.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx129.flt.2flp, i64 0, i64 %idxprom130, !taffo.info !14, !taffo.initweight !20
  store double 1.000000e+00, double* %arrayidx131.flt.2flp, align 8, !taffo.info !45, !taffo.constinfo !46
  %add132 = add nsw i32 %i.4, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond133

for.cond133:                                      ; preds = %for.inc170, %for.body127
  %j.4 = phi i32 [ %add132, %for.body127 ], [ %inc171, %for.inc170 ]
  %cmp134 = icmp slt i32 %j.4, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp134, label %for.body136, label %for.end172, !taffo.info !22, !taffo.initweight !21

for.body136:                                      ; preds = %for.cond133
  %idxprom137 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx138.flt.2flp = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom137, !taffo.info !14, !taffo.initweight !31
  %idxprom139 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx140.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx138.flt.2flp, i64 0, i64 %idxprom139, !taffo.info !14, !taffo.initweight !20
  store double 0.000000e+00, double* %arrayidx140.flt.2flp, align 8, !taffo.info !45, !taffo.constinfo !35
  br label %for.cond141

for.cond141:                                      ; preds = %for.inc159, %for.body136
  %k.0 = phi i32 [ 0, %for.body136 ], [ %inc160, %for.inc159 ]
  %cmp142 = icmp slt i32 %k.0, 28, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp142, label %for.body144, label %for.end161, !taffo.info !22, !taffo.initweight !21

for.body144:                                      ; preds = %for.cond141
  %idxprom145 = sext i32 %k.0 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx146.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom145, !taffo.info !12, !taffo.initweight !31
  %idxprom147 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx148.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx146.flt.2flp, i64 0, i64 %idxprom147, !taffo.info !12, !taffo.initweight !20
  %tmp16.flt.fallback.2flp = load double, double* %arrayidx148.flt.2flp, align 8, !taffo.info !12, !taffo.initweight !21
  %idxprom149 = sext i32 %k.0 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx150.flt.2flp = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom149, !taffo.info !12, !taffo.initweight !31
  %idxprom151 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx152.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx150.flt.2flp, i64 0, i64 %idxprom151, !taffo.info !12, !taffo.initweight !20
  %tmp17.flt.fallback.2flp = load double, double* %arrayidx152.flt.2flp, align 8, !taffo.info !12, !taffo.initweight !21
  %mul153.2flp = fmul double %tmp16.flt.fallback.2flp, %tmp17.flt.fallback.2flp, !taffo.info !12
  %idxprom154 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx155.flt.2flp = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom154, !taffo.info !14, !taffo.initweight !31
  %idxprom156 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx157.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx155.flt.2flp, i64 0, i64 %idxprom156, !taffo.info !14, !taffo.initweight !20
  %tmp18.flt.fallback.2flp = load double, double* %arrayidx157.flt.2flp, align 8, !taffo.info !14, !taffo.initweight !21
  %add158.2flp = fadd double %tmp18.flt.fallback.2flp, %mul153.2flp, !taffo.info !14
  store double %add158.2flp, double* %arrayidx157.flt.2flp, align 8, !taffo.info !45
  br label %for.inc159

for.inc159:                                       ; preds = %for.body144
  %inc160 = add nsw i32 %k.0, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond141

for.end161:                                       ; preds = %for.cond141
  %idxprom162 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx163.flt.2flp = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom162, !taffo.info !14, !taffo.initweight !31
  %idxprom164 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx165.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx163.flt.2flp, i64 0, i64 %idxprom164, !taffo.info !14, !taffo.initweight !20
  %tmp19.flt.fallback.2flp = load double, double* %arrayidx165.flt.2flp, align 8, !taffo.info !14, !taffo.initweight !21
  %idxprom166 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx167.flt.2flp = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom166, !taffo.info !14, !taffo.initweight !31
  %idxprom168 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx169.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx167.flt.2flp, i64 0, i64 %idxprom168, !taffo.info !14, !taffo.initweight !20
  store double %tmp19.flt.fallback.2flp, double* %arrayidx169.flt.2flp, align 8, !taffo.info !45
  br label %for.inc170

for.inc170:                                       ; preds = %for.end161
  %inc171 = add nsw i32 %j.4, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond133

for.end172:                                       ; preds = %for.cond133
  br label %for.inc173

for.inc173:                                       ; preds = %for.end172
  %inc174 = add nsw i32 %i.4, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond124

for.end175:                                       ; preds = %for.cond124
  %arrayidx176.flt.2flp = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 31, !taffo.info !14, !taffo.initweight !31
  %arrayidx177.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx176.flt.2flp, i64 0, i64 31, !taffo.info !14, !taffo.initweight !20
  store double 1.000000e+00, double* %arrayidx177.flt.2flp, align 8, !taffo.info !45, !taffo.constinfo !46
  br label %for.cond178

for.cond178:                                      ; preds = %for.inc195, %for.end175
  %i.5 = phi i32 [ 0, %for.end175 ], [ %inc196, %for.inc195 ]
  %cmp179 = icmp slt i32 %i.5, 32, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp179, label %for.body181, label %for.end197, !taffo.info !18, !taffo.initweight !21

for.body181:                                      ; preds = %for.cond178
  br label %for.cond182

for.cond182:                                      ; preds = %for.inc191, %for.body181
  %j.5 = phi i32 [ 0, %for.body181 ], [ %inc192, %for.inc191 ]
  %cmp183 = icmp slt i32 %j.5, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp183, label %for.body185, label %for.end193, !taffo.info !22, !taffo.initweight !21

for.body185:                                      ; preds = %for.cond182
  %idxprom186 = sext i32 %i.5 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx187.flt.2flp = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom186, !taffo.info !14, !taffo.initweight !31
  %idxprom188 = sext i32 %j.5 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx189.flt.2flp = getelementptr inbounds [32 x double], [32 x double]* %arrayidx187.flt.2flp, i64 0, i64 %idxprom188, !taffo.info !14, !taffo.initweight !20
  %tmp20.flt.fallback.2flp = load double, double* %arrayidx189.flt.2flp, align 8, !taffo.info !14, !taffo.initweight !21
  %call190.flt = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str.9, i32 0, i32 0), double %tmp20.flt.fallback.2flp), !taffo.info !49, !taffo.initweight !24, !taffo.constinfo !51
  br label %for.inc191

for.inc191:                                       ; preds = %for.body185
  %inc192 = add nsw i32 %j.5, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond182

for.end193:                                       ; preds = %for.cond182
  %call194 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.10, i32 0, i32 0)), !taffo.constinfo !33
  br label %for.inc195

for.inc195:                                       ; preds = %for.end193
  %inc196 = add nsw i32 %i.5, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !33
  br label %for.cond178

for.end197:                                       ; preds = %for.cond178
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !52 !taffo.funinfo !53 dso_local double @sqrt(double) #1

declare !taffo.initweight !52 !taffo.funinfo !53 dso_local i32 @printf(i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!4}
!llvm.ident = !{!5}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 1.020000e+02}
!2 = !{i1 false, !3, i1 false, i2 0}
!3 = !{double 0.000000e+00, double 1.000000e+01}
!4 = !{i32 1, !"wchar_size", i32 4}
!5 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!6 = !{}
!7 = !{!8, !9, !10, i2 -1}
!8 = !{!"float", i32 2, double 0.000000e+00}
!9 = !{double -5.000000e+04, double 5.000000e+04}
!10 = !{double 1.000000e-100}
!11 = !{i32 0}
!12 = !{!8, !13, !10, i2 -1}
!13 = !{double -5.000000e-01, double 5.000000e-01}
!14 = !{!8, !15, !10, i2 -1}
!15 = !{double 0.000000e+00, double 5.000000e+00}
!16 = !{!8, !17, !10, i2 -1}
!17 = !{double -4.096000e+03, double 4.096000e+03}
!18 = !{i1 false, !19, i1 false, i2 -2}
!19 = !{double 0.000000e+00, double 2.800000e+01}
!20 = !{i32 2}
!21 = !{i32 3}
!22 = !{i1 false, !23, i1 false, i2 -2}
!23 = !{double 0.000000e+00, double 3.200000e+01}
!24 = !{i32 4}
!25 = !{i1 false, !26}
!26 = !{i1 false, !27, i1 false, i2 0}
!27 = !{double 3.200000e+01, double 3.200000e+01}
!28 = !{i1 false, !29}
!29 = !{i1 false, !30, i1 false, i2 0}
!30 = !{double 2.800000e+01, double 2.800000e+01}
!31 = !{i32 1}
!32 = !{i1 false, !13, !10, i2 -1}
!33 = !{i1 false, i1 false}
!34 = !{i1 false, !9, !10, i2 -1}
!35 = !{!36, i1 false}
!36 = !{i1 false, !37, i1 false, i2 0}
!37 = !{double 0.000000e+00, double 0.000000e+00}
!38 = !{!8, !39, !10, i2 1}
!39 = !{double 1.000000e+00, double 3.000000e+03}
!40 = !{i1 false, !17, !10, i2 -1}
!41 = !{!42, i1 false, !10, i2 -1}
!42 = !{!"fixp", i32 -32, i32 18}
!43 = !{i1 false, i1 false, i1 false, i2 1}
!44 = !{!29, i1 false}
!45 = !{i1 false, !15, !10, i2 -1}
!46 = !{!47, i1 false}
!47 = !{i1 false, !48, i1 false, i2 0}
!48 = !{double 1.000000e+00, double 1.000000e+00}
!49 = !{!50, i1 false, !10, i2 -1}
!50 = !{!"fixp", i32 32, i32 29}
!51 = !{i1 false, i1 false, i1 false}
!52 = !{i32 -1}
!53 = !{i32 0, i1 false}
