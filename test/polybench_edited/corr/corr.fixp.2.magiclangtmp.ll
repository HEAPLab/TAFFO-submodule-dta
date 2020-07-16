; ModuleID = 'polybench_edited/corr/corr.fixp.1.magiclangtmp.ll'
source_filename = "polybench_edited/corr/corr.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [49 x i8] c"scalar(range(-50000, 50000) final error(1e-100))\00", section "llvm.metadata"
@.str.1 = private unnamed_addr constant [29 x i8] c"polybench_edited/corr/corr.c\00", section "llvm.metadata"
@.str.2 = private unnamed_addr constant [43 x i8] c"scalar(range(-10, 10) error(1e-100) final)\00", section "llvm.metadata"
@.str.3 = private unnamed_addr constant [40 x i8] c"scalar(range(0, 5) error(1e-100) final)\00", section "llvm.metadata"
@.str.4 = private unnamed_addr constant [46 x i8] c"scalar(range(-4096,4096) error(1e-100) final)\00", section "llvm.metadata"
@.str.5 = private unnamed_addr constant [36 x i8] c"scalar(range(0, 28) final disabled)\00", section "llvm.metadata"
@.str.6 = private unnamed_addr constant [36 x i8] c"scalar(range(0, 32) final disabled)\00", section "llvm.metadata"
@.str.7 = private unnamed_addr constant [37 x i8] c"scalar(range(1, 3000) error(1e-100))\00", section "llvm.metadata"
@.str.8 = private unnamed_addr constant [9 x i8] c"scalar()\00", section "llvm.metadata"
@.str.9 = private unnamed_addr constant [8 x i8] c"%.16lf \00", align 1
@.str.10 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !2 !taffo.funinfo !2 {
entry:
  %retval = alloca i32, align 4
  %mean = alloca [32 x double], align 16, !taffo.initweight !3, !taffo.info !4
  %data = alloca [28 x [32 x double]], align 16, !taffo.initweight !3, !taffo.info !7
  %corr = alloca [32 x [32 x double]], align 16, !taffo.initweight !3, !taffo.info !9
  %stddev = alloca [32 x double], align 16, !taffo.initweight !3, !taffo.info !11
  %i = alloca i32, align 4, !taffo.initweight !3, !taffo.info !13
  %j = alloca i32, align 4, !taffo.initweight !3, !taffo.info !15
  %k = alloca i32, align 4, !taffo.initweight !3, !taffo.info !15
  %float_n = alloca double, align 8, !taffo.initweight !3, !taffo.info !17
  %eps = alloca double, align 8, !taffo.initweight !3, !taffo.info !19
  store i32 0, i32* %retval, align 4
  %mean1 = bitcast [32 x double]* %mean to i8*, !taffo.initweight !20, !taffo.info !4
  %data2 = bitcast [28 x [32 x double]]* %data to i8*, !taffo.initweight !20, !taffo.info !7
  %corr3 = bitcast [32 x [32 x double]]* %corr to i8*, !taffo.initweight !20, !taffo.info !9
  %stddev4 = bitcast [32 x double]* %stddev to i8*, !taffo.initweight !20, !taffo.info !11
  %i5 = bitcast i32* %i to i8*, !taffo.initweight !20, !taffo.info !13
  %j6 = bitcast i32* %j to i8*, !taffo.initweight !20, !taffo.info !15
  %k7 = bitcast i32* %k to i8*, !taffo.initweight !20, !taffo.info !15
  %float_n8 = bitcast double* %float_n to i8*, !taffo.initweight !20, !taffo.info !17
  store double 2.800000e+01, double* %float_n, align 8, !taffo.initweight !20, !taffo.info !17
  store i32 0, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond

for.cond:                                         ; preds = %for.inc16, %entry
  %0 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %cmp = icmp slt i32 %0, 28, !taffo.initweight !21, !taffo.info !13
  br i1 %cmp, label %for.body, label %for.end18, !taffo.initweight !22, !taffo.info !13

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %1 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %cmp10 = icmp slt i32 %1, 32, !taffo.initweight !21, !taffo.info !15
  br i1 %cmp10, label %for.body11, label %for.end, !taffo.initweight !22, !taffo.info !15

for.body11:                                       ; preds = %for.cond9
  %2 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %3 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %mul = mul nsw i32 %2, %3, !taffo.initweight !21, !taffo.info !13
  %conv = sitofp i32 %mul to double, !taffo.initweight !22, !taffo.info !13
  %div = fdiv double %conv, 3.200000e+01, !taffo.initweight !23, !taffo.info !13
  %4 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %conv12 = sitofp i32 %4 to double, !taffo.initweight !21, !taffo.info !13
  %add = fadd double %div, %conv12, !taffo.initweight !22, !taffo.info !13
  %div13 = fdiv double %add, 2.800000e+01, !taffo.initweight !23, !taffo.info !13
  %5 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom = sext i32 %5 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom, !taffo.initweight !20, !taffo.info !7
  %6 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom14 = sext i32 %6 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx15 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx, i64 0, i64 %idxprom14, !taffo.initweight !21, !taffo.info !7
  store double %div13, double* %arrayidx15, align 8, !taffo.initweight !22, !taffo.info !7
  br label %for.inc

for.inc:                                          ; preds = %for.body11
  %7 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %inc = add nsw i32 %7, 1, !taffo.initweight !21, !taffo.info !15
  store i32 %inc, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc16

for.inc16:                                        ; preds = %for.end
  %8 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %inc17 = add nsw i32 %8, 1, !taffo.initweight !21, !taffo.info !13
  store i32 %inc17, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond

for.end18:                                        ; preds = %for.cond
  %eps19 = bitcast double* %eps to i8*, !taffo.initweight !20, !taffo.info !19
  store double 1.000000e-01, double* %eps, align 8, !taffo.initweight !20, !taffo.info !19
  store i32 0, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc43, %for.end18
  %9 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %cmp21 = icmp slt i32 %9, 32, !taffo.initweight !21, !taffo.info !15
  br i1 %cmp21, label %for.body23, label %for.end45, !taffo.initweight !22, !taffo.info !15

for.body23:                                       ; preds = %for.cond20
  %10 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom24 = sext i32 %10 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx25 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom24, !taffo.initweight !20, !taffo.info !4
  store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.initweight !21, !taffo.info !4
  store i32 0, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc37, %for.body23
  %11 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %cmp27 = icmp slt i32 %11, 28, !taffo.initweight !21, !taffo.info !13
  br i1 %cmp27, label %for.body29, label %for.end39, !taffo.initweight !22, !taffo.info !13

for.body29:                                       ; preds = %for.cond26
  %12 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom30 = sext i32 %12 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx31 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom30, !taffo.initweight !20, !taffo.info !7
  %13 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom32 = sext i32 %13 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx33 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx31, i64 0, i64 %idxprom32, !taffo.initweight !21, !taffo.info !7
  %14 = load double, double* %arrayidx33, align 8, !taffo.initweight !22, !taffo.info !7
  %15 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom34 = sext i32 %15 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx35 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom34, !taffo.initweight !20, !taffo.info !4
  %16 = load double, double* %arrayidx35, align 8, !taffo.initweight !21, !taffo.info !4
  %add36 = fadd double %16, %14, !taffo.initweight !22, !taffo.info !4
  store double %add36, double* %arrayidx35, align 8, !taffo.initweight !21, !taffo.info !4
  br label %for.inc37

for.inc37:                                        ; preds = %for.body29
  %17 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %inc38 = add nsw i32 %17, 1, !taffo.initweight !21, !taffo.info !13
  store i32 %inc38, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond26

for.end39:                                        ; preds = %for.cond26
  %18 = load double, double* %float_n, align 8, !taffo.initweight !20, !taffo.info !17
  %19 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom40 = sext i32 %19 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx41 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom40, !taffo.initweight !20, !taffo.info !4
  %20 = load double, double* %arrayidx41, align 8, !taffo.initweight !21, !taffo.info !4
  %div42 = fdiv double %20, %18, !taffo.initweight !21, !taffo.info !17
  store double %div42, double* %arrayidx41, align 8, !taffo.initweight !21, !taffo.info !4
  br label %for.inc43

for.inc43:                                        ; preds = %for.end39
  %21 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %inc44 = add nsw i32 %21, 1, !taffo.initweight !21, !taffo.info !15
  store i32 %inc44, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond20

for.end45:                                        ; preds = %for.cond20
  store i32 0, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond46

for.cond46:                                       ; preds = %for.inc91, %for.end45
  %22 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %cmp47 = icmp slt i32 %22, 32, !taffo.initweight !21, !taffo.info !15
  br i1 %cmp47, label %for.body49, label %for.end93, !taffo.initweight !22, !taffo.info !15

for.body49:                                       ; preds = %for.cond46
  %23 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom50 = sext i32 %23 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx51 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom50, !taffo.initweight !20, !taffo.info !11
  store double 0.000000e+00, double* %arrayidx51, align 8, !taffo.initweight !21, !taffo.info !11
  store i32 0, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond52

for.cond52:                                       ; preds = %for.inc73, %for.body49
  %24 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %cmp53 = icmp slt i32 %24, 28, !taffo.initweight !21, !taffo.info !13
  br i1 %cmp53, label %for.body55, label %for.end75, !taffo.initweight !22, !taffo.info !13

for.body55:                                       ; preds = %for.cond52
  %25 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom56 = sext i32 %25 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx57 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom56, !taffo.initweight !20, !taffo.info !7
  %26 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom58 = sext i32 %26 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx59 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx57, i64 0, i64 %idxprom58, !taffo.initweight !21, !taffo.info !7
  %27 = load double, double* %arrayidx59, align 8, !taffo.initweight !22, !taffo.info !7
  %28 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom60 = sext i32 %28 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx61 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom60, !taffo.initweight !20, !taffo.info !4
  %29 = load double, double* %arrayidx61, align 8, !taffo.initweight !21, !taffo.info !4
  %sub = fsub double %27, %29, !taffo.initweight !22, !taffo.info !4
  %30 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom62 = sext i32 %30 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx63 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom62, !taffo.initweight !20, !taffo.info !7
  %31 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom64 = sext i32 %31 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx65 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx63, i64 0, i64 %idxprom64, !taffo.initweight !21, !taffo.info !7
  %32 = load double, double* %arrayidx65, align 8, !taffo.initweight !22, !taffo.info !7
  %33 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom66 = sext i32 %33 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx67 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom66, !taffo.initweight !20, !taffo.info !4
  %34 = load double, double* %arrayidx67, align 8, !taffo.initweight !21, !taffo.info !4
  %sub68 = fsub double %32, %34, !taffo.initweight !22, !taffo.info !4
  %mul69 = fmul double %sub, %sub68, !taffo.initweight !23, !taffo.info !4
  %35 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom70 = sext i32 %35 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx71 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom70, !taffo.initweight !20, !taffo.info !11
  %36 = load double, double* %arrayidx71, align 8, !taffo.initweight !21, !taffo.info !11
  %add72 = fadd double %36, %mul69, !taffo.initweight !22, !taffo.info !11
  store double %add72, double* %arrayidx71, align 8, !taffo.initweight !21, !taffo.info !11
  br label %for.inc73

for.inc73:                                        ; preds = %for.body55
  %37 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %inc74 = add nsw i32 %37, 1, !taffo.initweight !21, !taffo.info !13
  store i32 %inc74, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond52

for.end75:                                        ; preds = %for.cond52
  %38 = load double, double* %float_n, align 8, !taffo.initweight !20, !taffo.info !17
  %39 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom76 = sext i32 %39 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx77 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom76, !taffo.initweight !20, !taffo.info !11
  %40 = load double, double* %arrayidx77, align 8, !taffo.initweight !21, !taffo.info !11
  %div78 = fdiv double %40, %38, !taffo.initweight !21, !taffo.info !17
  store double %div78, double* %arrayidx77, align 8, !taffo.initweight !21, !taffo.info !11
  %41 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom79 = sext i32 %41 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx80 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom79, !taffo.initweight !20, !taffo.info !11
  %42 = load double, double* %arrayidx80, align 8, !taffo.initweight !21, !taffo.info !11
  %call = call double @sqrt(double %42) #1, !taffo.initweight !22, !taffo.info !11
  %43 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom81 = sext i32 %43 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx82 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom81, !taffo.initweight !20, !taffo.info !11
  store double %call, double* %arrayidx82, align 8, !taffo.initweight !21, !taffo.info !11
  %44 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom83 = sext i32 %44 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx84 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom83, !taffo.initweight !20, !taffo.info !11
  %45 = load double, double* %arrayidx84, align 8, !taffo.initweight !21, !taffo.info !11
  %46 = load double, double* %eps, align 8, !taffo.initweight !20, !taffo.info !19
  %cmp85 = fcmp ole double %45, %46, !taffo.initweight !21, !taffo.info !19
  br i1 %cmp85, label %cond.true, label %cond.false, !taffo.initweight !22, !taffo.info !19

cond.true:                                        ; preds = %for.end75
  br label %cond.end

cond.false:                                       ; preds = %for.end75
  %47 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom87 = sext i32 %47 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx88 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom87, !taffo.initweight !20, !taffo.info !11
  %48 = load double, double* %arrayidx88, align 8, !taffo.initweight !21, !taffo.info !11
  br label %cond.end

cond.end:                                         ; preds = %cond.false, %cond.true
  %cond = phi double [ 1.000000e+00, %cond.true ], [ %48, %cond.false ], !taffo.initweight !22, !taffo.info !11
  %49 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom89 = sext i32 %49 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx90 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom89, !taffo.initweight !20, !taffo.info !11
  store double %cond, double* %arrayidx90, align 8, !taffo.initweight !21, !taffo.info !11
  br label %for.inc91

for.inc91:                                        ; preds = %cond.end
  %50 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %inc92 = add nsw i32 %50, 1, !taffo.initweight !21, !taffo.info !15
  store i32 %inc92, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond46

for.end93:                                        ; preds = %for.cond46
  store i32 0, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond94

for.cond94:                                       ; preds = %for.inc121, %for.end93
  %51 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %cmp95 = icmp slt i32 %51, 28, !taffo.initweight !21, !taffo.info !13
  br i1 %cmp95, label %for.body97, label %for.end123, !taffo.initweight !22, !taffo.info !13

for.body97:                                       ; preds = %for.cond94
  store i32 0, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond98

for.cond98:                                       ; preds = %for.inc118, %for.body97
  %52 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %cmp99 = icmp slt i32 %52, 32, !taffo.initweight !21, !taffo.info !15
  br i1 %cmp99, label %for.body101, label %for.end120, !taffo.initweight !22, !taffo.info !15

for.body101:                                      ; preds = %for.cond98
  %53 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom102 = sext i32 %53 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx103 = getelementptr inbounds [32 x double], [32 x double]* %mean, i64 0, i64 %idxprom102, !taffo.initweight !20, !taffo.info !4
  %54 = load double, double* %arrayidx103, align 8, !taffo.initweight !21, !taffo.info !4
  %55 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom104 = sext i32 %55 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx105 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom104, !taffo.initweight !20, !taffo.info !7
  %56 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom106 = sext i32 %56 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx107 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx105, i64 0, i64 %idxprom106, !taffo.initweight !21, !taffo.info !7
  %57 = load double, double* %arrayidx107, align 8, !taffo.initweight !22, !taffo.info !7
  %sub108 = fsub double %57, %54, !taffo.initweight !22, !taffo.info !4
  store double %sub108, double* %arrayidx107, align 8, !taffo.initweight !22, !taffo.info !7
  %58 = load double, double* %float_n, align 8, !taffo.initweight !20, !taffo.info !17
  %call109 = call double @sqrt(double %58) #1, !taffo.initweight !21, !taffo.info !17
  %59 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom110 = sext i32 %59 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx111 = getelementptr inbounds [32 x double], [32 x double]* %stddev, i64 0, i64 %idxprom110, !taffo.initweight !20, !taffo.info !11
  %60 = load double, double* %arrayidx111, align 8, !taffo.initweight !21, !taffo.info !11
  %mul112 = fmul double %call109, %60, !taffo.initweight !22, !taffo.info !11
  %61 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom113 = sext i32 %61 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx114 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom113, !taffo.initweight !20, !taffo.info !7
  %62 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom115 = sext i32 %62 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx116 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx114, i64 0, i64 %idxprom115, !taffo.initweight !21, !taffo.info !7
  %63 = load double, double* %arrayidx116, align 8, !taffo.initweight !22, !taffo.info !7
  %div117 = fdiv double %63, %mul112, !taffo.initweight !23, !taffo.info !7
  store double %div117, double* %arrayidx116, align 8, !taffo.initweight !22, !taffo.info !7
  br label %for.inc118

for.inc118:                                       ; preds = %for.body101
  %64 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %inc119 = add nsw i32 %64, 1, !taffo.initweight !21, !taffo.info !15
  store i32 %inc119, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond98

for.end120:                                       ; preds = %for.cond98
  br label %for.inc121

for.inc121:                                       ; preds = %for.end120
  %65 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %inc122 = add nsw i32 %65, 1, !taffo.initweight !21, !taffo.info !13
  store i32 %inc122, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond94

for.end123:                                       ; preds = %for.cond94
  store i32 0, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond124

for.cond124:                                      ; preds = %for.inc173, %for.end123
  %66 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %cmp125 = icmp slt i32 %66, 31, !taffo.initweight !21, !taffo.info !13
  br i1 %cmp125, label %for.body127, label %for.end175, !taffo.initweight !22, !taffo.info !13

for.body127:                                      ; preds = %for.cond124
  %67 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom128 = sext i32 %67 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx129 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom128, !taffo.initweight !20, !taffo.info !9
  %68 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom130 = sext i32 %68 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx131 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx129, i64 0, i64 %idxprom130, !taffo.initweight !21, !taffo.info !9
  store double 1.000000e+00, double* %arrayidx131, align 8, !taffo.initweight !22, !taffo.info !9
  %69 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %add132 = add nsw i32 %69, 1, !taffo.initweight !21, !taffo.info !13
  store i32 %add132, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond133

for.cond133:                                      ; preds = %for.inc170, %for.body127
  %70 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %cmp134 = icmp slt i32 %70, 32, !taffo.initweight !21, !taffo.info !15
  br i1 %cmp134, label %for.body136, label %for.end172, !taffo.initweight !22, !taffo.info !15

for.body136:                                      ; preds = %for.cond133
  %71 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom137 = sext i32 %71 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx138 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom137, !taffo.initweight !20, !taffo.info !9
  %72 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom139 = sext i32 %72 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx140 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx138, i64 0, i64 %idxprom139, !taffo.initweight !21, !taffo.info !9
  store double 0.000000e+00, double* %arrayidx140, align 8, !taffo.initweight !22, !taffo.info !9
  store i32 0, i32* %k, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond141

for.cond141:                                      ; preds = %for.inc159, %for.body136
  %73 = load i32, i32* %k, align 4, !taffo.initweight !20, !taffo.info !15
  %cmp142 = icmp slt i32 %73, 28, !taffo.initweight !21, !taffo.info !15
  br i1 %cmp142, label %for.body144, label %for.end161, !taffo.initweight !22, !taffo.info !15

for.body144:                                      ; preds = %for.cond141
  %74 = load i32, i32* %k, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom145 = sext i32 %74 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx146 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom145, !taffo.initweight !20, !taffo.info !7
  %75 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom147 = sext i32 %75 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx148 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx146, i64 0, i64 %idxprom147, !taffo.initweight !21, !taffo.info !7
  %76 = load double, double* %arrayidx148, align 8, !taffo.initweight !22, !taffo.info !7
  %77 = load i32, i32* %k, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom149 = sext i32 %77 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx150 = getelementptr inbounds [28 x [32 x double]], [28 x [32 x double]]* %data, i64 0, i64 %idxprom149, !taffo.initweight !20, !taffo.info !7
  %78 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom151 = sext i32 %78 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx152 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx150, i64 0, i64 %idxprom151, !taffo.initweight !21, !taffo.info !7
  %79 = load double, double* %arrayidx152, align 8, !taffo.initweight !22, !taffo.info !7
  %mul153 = fmul double %76, %79, !taffo.initweight !23, !taffo.info !7
  %80 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom154 = sext i32 %80 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx155 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom154, !taffo.initweight !20, !taffo.info !9
  %81 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom156 = sext i32 %81 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx157 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx155, i64 0, i64 %idxprom156, !taffo.initweight !21, !taffo.info !9
  %82 = load double, double* %arrayidx157, align 8, !taffo.initweight !22, !taffo.info !9
  %add158 = fadd double %82, %mul153, !taffo.initweight !23, !taffo.info !9
  store double %add158, double* %arrayidx157, align 8, !taffo.initweight !22, !taffo.info !9
  br label %for.inc159

for.inc159:                                       ; preds = %for.body144
  %83 = load i32, i32* %k, align 4, !taffo.initweight !20, !taffo.info !15
  %inc160 = add nsw i32 %83, 1, !taffo.initweight !21, !taffo.info !15
  store i32 %inc160, i32* %k, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond141

for.end161:                                       ; preds = %for.cond141
  %84 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom162 = sext i32 %84 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx163 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom162, !taffo.initweight !20, !taffo.info !9
  %85 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom164 = sext i32 %85 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx165 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx163, i64 0, i64 %idxprom164, !taffo.initweight !21, !taffo.info !9
  %86 = load double, double* %arrayidx165, align 8, !taffo.initweight !22, !taffo.info !9
  %87 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom166 = sext i32 %87 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx167 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom166, !taffo.initweight !20, !taffo.info !9
  %88 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom168 = sext i32 %88 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx169 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx167, i64 0, i64 %idxprom168, !taffo.initweight !21, !taffo.info !9
  store double %86, double* %arrayidx169, align 8, !taffo.initweight !22, !taffo.info !9
  br label %for.inc170

for.inc170:                                       ; preds = %for.end161
  %89 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %inc171 = add nsw i32 %89, 1, !taffo.initweight !21, !taffo.info !15
  store i32 %inc171, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond133

for.end172:                                       ; preds = %for.cond133
  br label %for.inc173

for.inc173:                                       ; preds = %for.end172
  %90 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %inc174 = add nsw i32 %90, 1, !taffo.initweight !21, !taffo.info !13
  store i32 %inc174, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond124

for.end175:                                       ; preds = %for.cond124
  %arrayidx176 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 31, !taffo.initweight !20, !taffo.info !9
  %arrayidx177 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx176, i64 0, i64 31, !taffo.initweight !21, !taffo.info !9
  store double 1.000000e+00, double* %arrayidx177, align 8, !taffo.initweight !22, !taffo.info !9
  store i32 0, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond178

for.cond178:                                      ; preds = %for.inc195, %for.end175
  %91 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %cmp179 = icmp slt i32 %91, 32, !taffo.initweight !21, !taffo.info !13
  br i1 %cmp179, label %for.body181, label %for.end197, !taffo.initweight !22, !taffo.info !13

for.body181:                                      ; preds = %for.cond178
  store i32 0, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond182

for.cond182:                                      ; preds = %for.inc191, %for.body181
  %92 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %cmp183 = icmp slt i32 %92, 32, !taffo.initweight !21, !taffo.info !15
  br i1 %cmp183, label %for.body185, label %for.end193, !taffo.initweight !22, !taffo.info !15

for.body185:                                      ; preds = %for.cond182
  %93 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %idxprom186 = sext i32 %93 to i64, !taffo.initweight !21, !taffo.info !13
  %arrayidx187 = getelementptr inbounds [32 x [32 x double]], [32 x [32 x double]]* %corr, i64 0, i64 %idxprom186, !taffo.initweight !20, !taffo.info !9
  %94 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %idxprom188 = sext i32 %94 to i64, !taffo.initweight !21, !taffo.info !15
  %arrayidx189 = getelementptr inbounds [32 x double], [32 x double]* %arrayidx187, i64 0, i64 %idxprom188, !taffo.initweight !21, !taffo.info !9
  %95 = load double, double* %arrayidx189, align 8, !taffo.initweight !22, !taffo.info !9
  %call190 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.9, i32 0, i32 0), double %95), !taffo.initweight !23, !taffo.info !9
  br label %for.inc191

for.inc191:                                       ; preds = %for.body185
  %96 = load i32, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  %inc192 = add nsw i32 %96, 1, !taffo.initweight !21, !taffo.info !15
  store i32 %inc192, i32* %j, align 4, !taffo.initweight !20, !taffo.info !15
  br label %for.cond182

for.end193:                                       ; preds = %for.cond182
  %call194 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.10, i32 0, i32 0))
  br label %for.inc195

for.inc195:                                       ; preds = %for.end193
  %97 = load i32, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  %inc196 = add nsw i32 %97, 1, !taffo.initweight !21, !taffo.info !13
  store i32 %inc196, i32* %i, align 4, !taffo.initweight !20, !taffo.info !13
  br label %for.cond178

for.end197:                                       ; preds = %for.cond178
  %98 = load i32, i32* %retval, align 4
  ret i32 %98
}

; Function Attrs: nounwind
declare !taffo.initweight !24 !taffo.funinfo !25 void @llvm.var.annotation(i8*, i8*, i8*, i32) #1

; Function Attrs: nounwind
declare !taffo.initweight !26 !taffo.funinfo !27 dso_local double @sqrt(double) #2

declare !taffo.initweight !26 !taffo.funinfo !27 dso_local i32 @printf(i8*, ...) #3

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!2 = !{}
!3 = !{i32 0}
!4 = !{i1 false, !5, !6, i2 -1}
!5 = !{double -5.000000e+04, double 5.000000e+04}
!6 = !{double 1.000000e-100}
!7 = !{i1 false, !8, !6, i2 -1}
!8 = !{double -1.000000e+01, double 1.000000e+01}
!9 = !{i1 false, !10, !6, i2 -1}
!10 = !{double 0.000000e+00, double 5.000000e+00}
!11 = !{i1 false, !12, !6, i2 -1}
!12 = !{double -4.096000e+03, double 4.096000e+03}
!13 = !{i1 false, !14, i1 false, i2 -2}
!14 = !{double 0.000000e+00, double 2.800000e+01}
!15 = !{i1 false, !16, i1 false, i2 -2}
!16 = !{double 0.000000e+00, double 3.200000e+01}
!17 = !{i1 false, !18, !6, i2 1}
!18 = !{double 1.000000e+00, double 3.000000e+03}
!19 = !{i1 false, i1 false, i1 false, i2 1}
!20 = !{i32 1}
!21 = !{i32 2}
!22 = !{i32 3}
!23 = !{i32 4}
!24 = !{i32 -1, i32 -1, i32 -1, i32 -1}
!25 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
!26 = !{i32 -1}
!27 = !{i32 0, i1 false}
