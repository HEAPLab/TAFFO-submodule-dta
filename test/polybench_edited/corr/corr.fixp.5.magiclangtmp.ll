; ModuleID = 'polybench_edited/corr/corr.fixp.4.magiclangtmp.ll'
source_filename = "polybench_edited/corr/corr.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str.9 = private unnamed_addr constant [7 x i8] c"%.10f \00", align 1, !taffo.info !0
@.str.10 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1, !taffo.info !2

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !6 !taffo.funinfo !6 {
entry:
  %mean.s17_15fixp = alloca [32 x i32], align 16, !taffo.info !7
  %data.1flp = alloca [28 x [32 x float]], align 16, !taffo.info !11
  %corr.1flp = alloca [32 x [32 x float]], align 16, !taffo.info !14
  %stddev.1flp = alloca [32 x float], align 16, !taffo.info !16
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
  %0 = fptrunc double %div13 to float, !taffo.info !18
  %idxprom = sext i32 %i.0 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom, !taffo.info !11
  %idxprom14 = sext i32 %j.0 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx15.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx.1flp, i64 0, i64 %idxprom14, !taffo.info !11
  store float %0, float* %arrayidx15.1flp, align 8, !taffo.info !31
  br label %for.inc

for.inc:                                          ; preds = %for.body11
  %inc = add nsw i32 %j.0, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc16

for.inc16:                                        ; preds = %for.end
  %inc17 = add nsw i32 %i.0, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond

for.end18:                                        ; preds = %for.cond
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc43, %for.end18
  %j.1 = phi i32 [ 0, %for.end18 ], [ %inc44, %for.inc43 ]
  %cmp21 = icmp slt i32 %j.1, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp21, label %for.body23, label %for.end45, !taffo.info !22, !taffo.initweight !21

for.body23:                                       ; preds = %for.cond20
  %idxprom24 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx25.s17_15fixp = getelementptr inbounds [32 x i32], [32 x i32]* %mean.s17_15fixp, i64 0, i64 %idxprom24, !taffo.info !7
  store i32 0, i32* %arrayidx25.s17_15fixp, align 8, !taffo.info !33, !taffo.constinfo !34
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc37, %for.body23
  %i.1 = phi i32 [ 0, %for.body23 ], [ %inc38, %for.inc37 ]
  %cmp27 = icmp slt i32 %i.1, 28, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp27, label %for.body29, label %for.end39, !taffo.info !18, !taffo.initweight !21

for.body29:                                       ; preds = %for.cond26
  %idxprom30 = sext i32 %i.1 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx31.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom30, !taffo.info !11
  %idxprom32 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx33.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx31.1flp, i64 0, i64 %idxprom32, !taffo.info !11
  %tmp.1flp = load float, float* %arrayidx33.1flp, align 8, !taffo.info !11
  %idxprom34 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx35.s17_15fixp = getelementptr inbounds [32 x i32], [32 x i32]* %mean.s17_15fixp, i64 0, i64 %idxprom34, !taffo.info !7
  %tmp1.s17_15fixp = load i32, i32* %arrayidx35.s17_15fixp, align 8, !taffo.info !7
  %1 = fmul float 3.276800e+04, %tmp.1flp, !taffo.info !11
  %2 = fptosi float %1 to i32, !taffo.info !11
  %add36.s17_15fixp = add i32 %tmp1.s17_15fixp, %2, !taffo.info !7
  store i32 %add36.s17_15fixp, i32* %arrayidx35.s17_15fixp, align 8, !taffo.info !33
  br label %for.inc37

for.inc37:                                        ; preds = %for.body29
  %inc38 = add nsw i32 %i.1, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond26

for.end39:                                        ; preds = %for.cond26
  %idxprom40 = sext i32 %j.1 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx41.s17_15fixp = getelementptr inbounds [32 x i32], [32 x i32]* %mean.s17_15fixp, i64 0, i64 %idxprom40, !taffo.info !7
  %tmp2.s17_15fixp = load i32, i32* %arrayidx41.s17_15fixp, align 8, !taffo.info !7
  %3 = sext i32 %tmp2.s17_15fixp to i64, !taffo.info !7
  %4 = udiv i64 %3, 28, !taffo.info !37, !taffo.constinfo !40
  %5 = shl i64 %4, 5, !taffo.info !37, !taffo.constinfo !40
  %div42.u12_20fixp = trunc i64 %5 to i32, !taffo.info !43
  %6 = lshr i32 %div42.u12_20fixp, 5, !taffo.info !43
  store i32 %6, i32* %arrayidx41.s17_15fixp, align 8, !taffo.info !33
  br label %for.inc43

for.inc43:                                        ; preds = %for.end39
  %inc44 = add nsw i32 %j.1, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond20

for.end45:                                        ; preds = %for.cond20
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc91, %for.end45
  %j.2 = phi i32 [ 0, %for.end45 ], [ %inc92, %for.inc91 ]
  %cmp47 = icmp slt i32 %j.2, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp47, label %for.body49, label %for.end93, !taffo.info !22, !taffo.initweight !21

for.body49:                                       ; preds = %for.cond46
  %idxprom50 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx51.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom50, !taffo.info !16
  store float 0.000000e+00, float* %arrayidx51.1flp, align 8, !taffo.info !45, !taffo.constinfo !34
  br label %for.cond52

for.cond52:                                       ; preds = %for.inc73, %for.body49
  %i.2 = phi i32 [ 0, %for.body49 ], [ %inc74, %for.inc73 ]
  %cmp53 = icmp slt i32 %i.2, 28, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp53, label %for.body55, label %for.end75, !taffo.info !18, !taffo.initweight !21

for.body55:                                       ; preds = %for.cond52
  %idxprom56 = sext i32 %i.2 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx57.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom56, !taffo.info !11
  %idxprom58 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx59.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx57.1flp, i64 0, i64 %idxprom58, !taffo.info !11
  %tmp3.1flp = load float, float* %arrayidx59.1flp, align 8, !taffo.info !11
  %idxprom60 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx61.s17_15fixp = getelementptr inbounds [32 x i32], [32 x i32]* %mean.s17_15fixp, i64 0, i64 %idxprom60, !taffo.info !7
  %tmp4.s17_15fixp = load i32, i32* %arrayidx61.s17_15fixp, align 8, !taffo.info !7
  %7 = fmul float 3.276800e+04, %tmp3.1flp, !taffo.info !11
  %8 = fptosi float %7 to i32, !taffo.info !11
  %sub.s17_15fixp = sub i32 %8, %tmp4.s17_15fixp, !taffo.info !7
  %idxprom62 = sext i32 %i.2 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx63.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom62, !taffo.info !11
  %idxprom64 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx65.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx63.1flp, i64 0, i64 %idxprom64, !taffo.info !11
  %tmp5.1flp = load float, float* %arrayidx65.1flp, align 8, !taffo.info !11
  %idxprom66 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx67.s17_15fixp = getelementptr inbounds [32 x i32], [32 x i32]* %mean.s17_15fixp, i64 0, i64 %idxprom66, !taffo.info !7
  %tmp6.s17_15fixp = load i32, i32* %arrayidx67.s17_15fixp, align 8, !taffo.info !7
  %9 = fmul float 3.276800e+04, %tmp5.1flp, !taffo.info !11
  %10 = fptosi float %9 to i32, !taffo.info !11
  %sub68.s17_15fixp = sub i32 %10, %tmp6.s17_15fixp, !taffo.info !7
  %11 = sext i32 %sub.s17_15fixp to i64, !taffo.info !7
  %12 = sext i32 %sub68.s17_15fixp to i64, !taffo.info !7
  %13 = mul i64 %11, %12, !taffo.info !46
  %14 = ashr i64 %13, 15, !taffo.info !46
  %mul69.s17_15fixp = trunc i64 %14 to i32, !taffo.info !7
  %15 = sitofp i32 %mul69.s17_15fixp to float, !taffo.info !7
  %16 = fdiv float %15, 3.276800e+04, !taffo.info !7
  %idxprom70 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx71.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom70, !taffo.info !16
  %tmp7.1flp = load float, float* %arrayidx71.1flp, align 8, !taffo.info !16
  %add72.1flp = fadd float %tmp7.1flp, %16, !taffo.info !16
  store float %add72.1flp, float* %arrayidx71.1flp, align 8, !taffo.info !45
  br label %for.inc73

for.inc73:                                        ; preds = %for.body55
  %inc74 = add nsw i32 %i.2, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond52

for.end75:                                        ; preds = %for.cond52
  %idxprom76 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx77.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom76, !taffo.info !16
  %tmp8.1flp = load float, float* %arrayidx77.1flp, align 8, !taffo.info !16
  %17 = fmul float 0x4130000000000000, %tmp8.1flp, !taffo.info !16
  %18 = fptoui float %17 to i32, !taffo.info !16
  %19 = zext i32 %18 to i64, !taffo.info !16
  %20 = udiv i64 %19, 28, !taffo.info !48, !taffo.constinfo !40
  %div78.u12_20fixp = trunc i64 %20 to i32, !taffo.info !43
  %21 = uitofp i32 %div78.u12_20fixp to float, !taffo.info !43
  %22 = fdiv float %21, 0x4130000000000000, !taffo.info !43
  store float %22, float* %arrayidx77.1flp, align 8, !taffo.info !45
  %idxprom79 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx80.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom79, !taffo.info !16
  %tmp9.1flp = load float, float* %arrayidx80.1flp, align 8, !taffo.info !16
  %23 = fpext float %tmp9.1flp to double, !taffo.info !16
  %call.flt.fallback.2flp = call double @sqrt(double %23) #3, !taffo.info !50, !taffo.initweight !21, !taffo.constinfo !32
  %idxprom81 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx82.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom81, !taffo.info !16
  %24 = fptrunc double %call.flt.fallback.2flp to float, !taffo.info !50
  store float %24, float* %arrayidx82.1flp, align 8, !taffo.info !45
  %idxprom83 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx84.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom83, !taffo.info !16
  %tmp10.1flp = load float, float* %arrayidx84.1flp, align 8, !taffo.info !16
  %25 = fcmp ole float %tmp10.1flp, 0x3FB99999A0000000, !taffo.info !52
  br i1 %25, label %cond.true, label %cond.false, !taffo.info !54, !taffo.initweight !21

cond.true:                                        ; preds = %for.end75
  br label %cond.end

cond.false:                                       ; preds = %for.end75
  %idxprom87 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx88.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom87, !taffo.info !16
  %tmp11.1flp = load float, float* %arrayidx88.1flp, align 8, !taffo.info !16
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond.1flp = phi float [ 1.000000e+00, %cond.true ], [ %tmp11.1flp, %cond.false ], !taffo.info !16
  %idxprom89 = sext i32 %j.2 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx90.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom89, !taffo.info !16
  store float %cond.1flp, float* %arrayidx90.1flp, align 8, !taffo.info !45
  br label %for.inc91

for.inc91:                                        ; preds = %cond.end
  %inc92 = add nsw i32 %j.2, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !32
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
  %arrayidx103.s17_15fixp = getelementptr inbounds [32 x i32], [32 x i32]* %mean.s17_15fixp, i64 0, i64 %idxprom102, !taffo.info !7
  %tmp12.s17_15fixp = load i32, i32* %arrayidx103.s17_15fixp, align 8, !taffo.info !7
  %idxprom104 = sext i32 %i.3 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx105.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom104, !taffo.info !11
  %idxprom106 = sext i32 %j.3 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx107.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx105.1flp, i64 0, i64 %idxprom106, !taffo.info !11
  %tmp13.1flp = load float, float* %arrayidx107.1flp, align 8, !taffo.info !11
  %26 = fmul float 3.276800e+04, %tmp13.1flp, !taffo.info !11
  %27 = fptosi float %26 to i32, !taffo.info !11
  %sub108.s17_15fixp = sub i32 %27, %tmp12.s17_15fixp, !taffo.info !7
  %28 = sitofp i32 %sub108.s17_15fixp to float, !taffo.info !7
  %29 = fdiv float %28, 3.276800e+04, !taffo.info !7
  store float %29, float* %arrayidx107.1flp, align 8, !taffo.info !31
  %call109.flt.fallback.2flp = call double @sqrt(double 2.800000e+01) #3, !taffo.info !55, !taffo.initweight !20, !taffo.constinfo !56
  %idxprom110 = sext i32 %j.3 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx111.1flp = getelementptr inbounds [32 x float], [32 x float]* %stddev.1flp, i64 0, i64 %idxprom110, !taffo.info !16
  %tmp14.1flp = load float, float* %arrayidx111.1flp, align 8, !taffo.info !16
  %30 = fmul double 2.621440e+05, %call109.flt.fallback.2flp, !taffo.info !55, !taffo.constinfo !56
  %31 = fptosi double %30 to i32, !taffo.info !55
  %32 = fmul float 2.621440e+05, %tmp14.1flp, !taffo.info !16
  %33 = fptosi float %32 to i32, !taffo.info !16
  %34 = sext i32 %31 to i64, !taffo.info !55
  %35 = sext i32 %33 to i64, !taffo.info !16
  %36 = mul i64 %34, %35, !taffo.info !57
  %37 = ashr i64 %36, 18, !taffo.info !57
  %mul112.s14_18fixp = trunc i64 %37 to i32, !taffo.info !59
  %idxprom113 = sext i32 %i.3 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx114.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom113, !taffo.info !11
  %idxprom115 = sext i32 %j.3 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx116.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx114.1flp, i64 0, i64 %idxprom115, !taffo.info !11
  %tmp15.1flp = load float, float* %arrayidx116.1flp, align 8, !taffo.info !11
  %38 = fmul float 0x41D0000000000000, %tmp15.1flp, !taffo.info !11
  %39 = fptosi float %38 to i32, !taffo.info !11
  %40 = sext i32 %39 to i64, !taffo.info !11
  %41 = shl i64 %40, 18, !taffo.info !11
  %42 = sext i32 %mul112.s14_18fixp to i64, !taffo.info !59
  %43 = sdiv i64 %41, %42, !taffo.info !60
  %div117.s2_30fixp = trunc i64 %43 to i32, !taffo.info !61
  %44 = sitofp i32 %div117.s2_30fixp to float, !taffo.info !61
  %45 = fdiv float %44, 0x41D0000000000000, !taffo.info !61
  store float %45, float* %arrayidx116.1flp, align 8, !taffo.info !31
  br label %for.inc118

for.inc118:                                       ; preds = %for.body101
  %inc119 = add nsw i32 %j.3, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond98

for.end120:                                       ; preds = %for.cond98
  br label %for.inc121

for.inc121:                                       ; preds = %for.end120
  %inc122 = add nsw i32 %i.3, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond94

for.end123:                                       ; preds = %for.cond94
  br label %for.cond124

for.cond124:                                      ; preds = %for.inc173, %for.end123
  %i.4 = phi i32 [ 0, %for.end123 ], [ %inc174, %for.inc173 ]
  %cmp125 = icmp slt i32 %i.4, 31, !taffo.info !18, !taffo.initweight !20
  br i1 %cmp125, label %for.body127, label %for.end175, !taffo.info !18, !taffo.initweight !21

for.body127:                                      ; preds = %for.cond124
  %idxprom128 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx129.1flp = getelementptr inbounds [32 x [32 x float]], [32 x [32 x float]]* %corr.1flp, i64 0, i64 %idxprom128, !taffo.info !14
  %idxprom130 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx131.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx129.1flp, i64 0, i64 %idxprom130, !taffo.info !14
  store float 1.000000e+00, float* %arrayidx131.1flp, align 8, !taffo.info !63, !taffo.constinfo !64
  %add132 = add nsw i32 %i.4, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond133

for.cond133:                                      ; preds = %for.inc170, %for.body127
  %j.4 = phi i32 [ %add132, %for.body127 ], [ %inc171, %for.inc170 ]
  %cmp134 = icmp slt i32 %j.4, 32, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp134, label %for.body136, label %for.end172, !taffo.info !22, !taffo.initweight !21

for.body136:                                      ; preds = %for.cond133
  %idxprom137 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx138.1flp = getelementptr inbounds [32 x [32 x float]], [32 x [32 x float]]* %corr.1flp, i64 0, i64 %idxprom137, !taffo.info !14
  %idxprom139 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx140.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx138.1flp, i64 0, i64 %idxprom139, !taffo.info !14
  store float 0.000000e+00, float* %arrayidx140.1flp, align 8, !taffo.info !63, !taffo.constinfo !34
  br label %for.cond141

for.cond141:                                      ; preds = %for.inc159, %for.body136
  %k.0 = phi i32 [ 0, %for.body136 ], [ %inc160, %for.inc159 ]
  %cmp142 = icmp slt i32 %k.0, 28, !taffo.info !22, !taffo.initweight !20
  br i1 %cmp142, label %for.body144, label %for.end161, !taffo.info !22, !taffo.initweight !21

for.body144:                                      ; preds = %for.cond141
  %idxprom145 = sext i32 %k.0 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx146.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom145, !taffo.info !11
  %idxprom147 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx148.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx146.1flp, i64 0, i64 %idxprom147, !taffo.info !11
  %tmp16.1flp = load float, float* %arrayidx148.1flp, align 8, !taffo.info !11
  %idxprom149 = sext i32 %k.0 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx150.1flp = getelementptr inbounds [28 x [32 x float]], [28 x [32 x float]]* %data.1flp, i64 0, i64 %idxprom149, !taffo.info !11
  %idxprom151 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx152.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx150.1flp, i64 0, i64 %idxprom151, !taffo.info !11
  %tmp17.1flp = load float, float* %arrayidx152.1flp, align 8, !taffo.info !11
  %46 = fmul float 0x41C0000000000000, %tmp16.1flp, !taffo.info !11
  %47 = fptosi float %46 to i32, !taffo.info !11
  %48 = fmul float 0x41C0000000000000, %tmp17.1flp, !taffo.info !11
  %49 = fptosi float %48 to i32, !taffo.info !11
  %50 = sext i32 %47 to i64, !taffo.info !11
  %51 = sext i32 %49 to i64, !taffo.info !11
  %52 = mul i64 %50, %51, !taffo.info !67
  %53 = ashr i64 %52, 29, !taffo.info !67
  %mul153.s3_29fixp = trunc i64 %53 to i32, !taffo.info !69
  %idxprom154 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx155.1flp = getelementptr inbounds [32 x [32 x float]], [32 x [32 x float]]* %corr.1flp, i64 0, i64 %idxprom154, !taffo.info !14
  %idxprom156 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx157.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx155.1flp, i64 0, i64 %idxprom156, !taffo.info !14
  %tmp18.1flp = load float, float* %arrayidx157.1flp, align 8, !taffo.info !14
  %54 = fmul float 0x41C0000000000000, %tmp18.1flp, !taffo.info !14
  %55 = fptoui float %54 to i32, !taffo.info !14
  %add158.u3_29fixp = add i32 %55, %mul153.s3_29fixp, !taffo.info !71
  %56 = uitofp i32 %add158.u3_29fixp to float, !taffo.info !71
  %57 = fdiv float %56, 0x41C0000000000000, !taffo.info !71
  store float %57, float* %arrayidx157.1flp, align 8, !taffo.info !63
  br label %for.inc159

for.inc159:                                       ; preds = %for.body144
  %inc160 = add nsw i32 %k.0, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond141

for.end161:                                       ; preds = %for.cond141
  %idxprom162 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx163.1flp = getelementptr inbounds [32 x [32 x float]], [32 x [32 x float]]* %corr.1flp, i64 0, i64 %idxprom162, !taffo.info !14
  %idxprom164 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx165.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx163.1flp, i64 0, i64 %idxprom164, !taffo.info !14
  %tmp19.1flp = load float, float* %arrayidx165.1flp, align 8, !taffo.info !14
  %idxprom166 = sext i32 %j.4 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx167.1flp = getelementptr inbounds [32 x [32 x float]], [32 x [32 x float]]* %corr.1flp, i64 0, i64 %idxprom166, !taffo.info !14
  %idxprom168 = sext i32 %i.4 to i64, !taffo.info !18, !taffo.initweight !20
  %arrayidx169.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx167.1flp, i64 0, i64 %idxprom168, !taffo.info !14
  store float %tmp19.1flp, float* %arrayidx169.1flp, align 8, !taffo.info !63
  br label %for.inc170

for.inc170:                                       ; preds = %for.end161
  %inc171 = add nsw i32 %j.4, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond133

for.end172:                                       ; preds = %for.cond133
  br label %for.inc173

for.inc173:                                       ; preds = %for.end172
  %inc174 = add nsw i32 %i.4, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond124

for.end175:                                       ; preds = %for.cond124
  %arrayidx176.1flp = getelementptr inbounds [32 x [32 x float]], [32 x [32 x float]]* %corr.1flp, i64 0, i64 31, !taffo.info !14
  %arrayidx177.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx176.1flp, i64 0, i64 31, !taffo.info !14
  store float 1.000000e+00, float* %arrayidx177.1flp, align 8, !taffo.info !63, !taffo.constinfo !64
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
  %arrayidx187.1flp = getelementptr inbounds [32 x [32 x float]], [32 x [32 x float]]* %corr.1flp, i64 0, i64 %idxprom186, !taffo.info !14
  %idxprom188 = sext i32 %j.5 to i64, !taffo.info !22, !taffo.initweight !20
  %arrayidx189.1flp = getelementptr inbounds [32 x float], [32 x float]* %arrayidx187.1flp, i64 0, i64 %idxprom188, !taffo.info !14
  %tmp20.1flp = load float, float* %arrayidx189.1flp, align 8, !taffo.info !14
  %58 = fpext float %tmp20.1flp to double, !taffo.info !14
  %call190.flt = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str.9, i32 0, i32 0), double %58), !taffo.info !73, !taffo.initweight !24, !taffo.constinfo !74
  br label %for.inc191

for.inc191:                                       ; preds = %for.body185
  %inc192 = add nsw i32 %j.5, 1, !taffo.info !22, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond182

for.end193:                                       ; preds = %for.cond182
  %call194 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.10, i32 0, i32 0)), !taffo.constinfo !32
  br label %for.inc195

for.inc195:                                       ; preds = %for.end193
  %inc196 = add nsw i32 %i.5, 1, !taffo.info !18, !taffo.initweight !20, !taffo.constinfo !32
  br label %for.cond178

for.end197:                                       ; preds = %for.cond178
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !75 !taffo.funinfo !76 dso_local double @sqrt(double) #1

declare !taffo.initweight !75 !taffo.funinfo !76 dso_local i32 @printf(i8*, ...) #2

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
!8 = !{!"fixp", i32 -32, i32 15}
!9 = !{double -5.000000e+04, double 5.000000e+04}
!10 = !{double 1.000000e-100}
!11 = !{!12, !13, !10, i2 -1}
!12 = !{!"float", i32 1, double 0.000000e+00}
!13 = !{double -5.000000e-01, double 5.000000e-01}
!14 = !{!12, !15, !10, i2 -1}
!15 = !{double 0.000000e+00, double 5.000000e+00}
!16 = !{!12, !17, !10, i2 -1}
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
!31 = !{i1 false, !13, !10, i2 -1}
!32 = !{i1 false, i1 false}
!33 = !{i1 false, !9, !10, i2 -1}
!34 = !{!35, i1 false}
!35 = !{i1 false, !36, i1 false, i2 0}
!36 = !{double 0.000000e+00, double 0.000000e+00}
!37 = !{!38, !39, !10, i2 1}
!38 = !{!"fixp", i32 64, i32 15}
!39 = !{double 1.000000e+00, double 3.000000e+03}
!40 = !{i1 false, !41}
!41 = !{!42, !30, i1 false, i2 0}
!42 = !{!"fixp", i32 32, i32 0}
!43 = !{!44, !39, !10, i2 1}
!44 = !{!"fixp", i32 32, i32 20}
!45 = !{i1 false, !17, !10, i2 -1}
!46 = !{!47, !9, !10, i2 -1}
!47 = !{!"fixp", i32 -64, i32 30}
!48 = !{!49, !39, !10, i2 1}
!49 = !{!"fixp", i32 64, i32 20}
!50 = !{!51, !17, !10, i2 -1}
!51 = !{!"float", i32 2, double 0.000000e+00}
!52 = !{!53, i1 false, !10, i2 -1}
!53 = !{!"fixp", i32 -32, i32 18}
!54 = !{i1 false, i1 false, i1 false, i2 1}
!55 = !{!51, !39, !10, i2 1}
!56 = !{!29, i1 false}
!57 = !{!58, !17, !10, i2 -1}
!58 = !{!"fixp", i32 -64, i32 36}
!59 = !{!53, !17, !10, i2 -1}
!60 = !{!47, !13, !10, i2 -1}
!61 = !{!62, !13, !10, i2 -1}
!62 = !{!"fixp", i32 -32, i32 30}
!63 = !{i1 false, !15, !10, i2 -1}
!64 = !{!65, i1 false}
!65 = !{i1 false, !66, i1 false, i2 0}
!66 = !{double 1.000000e+00, double 1.000000e+00}
!67 = !{!68, !13, !10, i2 -1}
!68 = !{!"fixp", i32 -64, i32 58}
!69 = !{!70, !13, !10, i2 -1}
!70 = !{!"fixp", i32 -32, i32 29}
!71 = !{!72, !15, !10, i2 -1}
!72 = !{!"fixp", i32 32, i32 29}
!73 = !{!72, i1 false, !10, i2 -1}
!74 = !{i1 false, i1 false, i1 false}
!75 = !{i32 -1}
!76 = !{i32 0, i1 false}
