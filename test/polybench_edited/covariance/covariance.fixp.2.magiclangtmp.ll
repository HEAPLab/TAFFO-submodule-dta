; ModuleID = 'polybench_edited/covariance/covariance.fixp.1.magiclangtmp.ll'
source_filename = "polybench_edited/covariance/covariance.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

@.str = private unnamed_addr constant [35 x i8] c"scalar(range(-10000, 10000) final)\00", section "llvm.metadata"
@.str.1 = private unnamed_addr constant [41 x i8] c"polybench_edited/covariance/covariance.c\00", section "llvm.metadata"
@.str.2 = private unnamed_addr constant [36 x i8] c"scalar(range(-10000, 100000) final)\00", section "llvm.metadata"
@.str.3 = private unnamed_addr constant [33 x i8] c"scalar(range(-5000, 5000) final)\00", section "llvm.metadata"
@.str.4 = private unnamed_addr constant [31 x i8] c"scalar(range(1, 100) disabled)\00", section "llvm.metadata"
@stdout = external dso_local global %struct._IO_FILE*, align 8
@.str.5 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1
@.str.6 = private unnamed_addr constant [4 x i8] c"%f \00", align 1

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main(i32 %argc, i8** %argv) #0 !taffo.initweight !2 !taffo.funinfo !3 {
entry:
  %retval = alloca i32, align 4
  %argc.addr = alloca i32, align 4
  %argv.addr = alloca i8**, align 8
  %n = alloca i32, align 4
  %m = alloca i32, align 4
  %float_n = alloca double, align 8, !taffo.initweight !4, !taffo.info !5
  %data = alloca [100 x [80 x double]], align 16, !taffo.initweight !4, !taffo.info !5
  %cov = alloca [100 x [80 x double]], align 16, !taffo.initweight !4, !taffo.info !7
  %mean = alloca [80 x double], align 16, !taffo.initweight !4, !taffo.info !9
  %i = alloca i32, align 4, !taffo.initweight !4, !taffo.info !11
  %j = alloca i32, align 4, !taffo.initweight !4, !taffo.info !11
  %k = alloca i32, align 4, !taffo.initweight !4, !taffo.info !11
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  store i32 100, i32* %n, align 4
  store i32 80, i32* %m, align 4
  %float_n1 = bitcast double* %float_n to i8*, !taffo.initweight !13, !taffo.info !5
  %data2 = bitcast [100 x [80 x double]]* %data to i8*, !taffo.initweight !13, !taffo.info !5
  %cov3 = bitcast [100 x [80 x double]]* %cov to i8*, !taffo.initweight !13, !taffo.info !7
  %mean4 = bitcast [80 x double]* %mean to i8*, !taffo.initweight !13, !taffo.info !9
  %i5 = bitcast i32* %i to i8*, !taffo.initweight !13, !taffo.info !11
  %j6 = bitcast i32* %j to i8*, !taffo.initweight !13, !taffo.info !11
  %k7 = bitcast i32* %k to i8*, !taffo.initweight !13, !taffo.info !11
  %0 = load i32, i32* %n, align 4
  %conv = sitofp i32 %0 to double
  store double %conv, double* %float_n, align 8, !taffo.initweight !13, !taffo.info !5
  store i32 0, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond

for.cond:                                         ; preds = %for.inc17, %entry
  %1 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp = icmp slt i32 %1, 100, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp, label %for.body, label %for.end19, !taffo.initweight !15, !taffo.info !11

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond9

for.cond9:                                        ; preds = %for.inc, %for.body
  %2 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp10 = icmp slt i32 %2, 80, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp10, label %for.body12, label %for.end, !taffo.initweight !15, !taffo.info !11

for.body12:                                       ; preds = %for.cond9
  %3 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %conv13 = sitofp i32 %3 to double, !taffo.initweight !14, !taffo.info !11
  %4 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %conv14 = sitofp i32 %4 to double, !taffo.initweight !14, !taffo.info !11
  %mul = fmul double %conv13, %conv14, !taffo.initweight !15, !taffo.info !11
  %div = fdiv double %mul, 8.000000e+01, !taffo.initweight !16, !taffo.info !11
  %5 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom = sext i32 %5 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom, !taffo.initweight !13, !taffo.info !5
  %6 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom15 = sext i32 %6 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx16 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx, i64 0, i64 %idxprom15, !taffo.initweight !14, !taffo.info !5
  store double %div, double* %arrayidx16, align 8, !taffo.initweight !15, !taffo.info !5
  br label %for.inc

for.inc:                                          ; preds = %for.body12
  %7 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %inc = add nsw i32 %7, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond9

for.end:                                          ; preds = %for.cond9
  br label %for.inc17

for.inc17:                                        ; preds = %for.end
  %8 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %inc18 = add nsw i32 %8, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc18, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond

for.end19:                                        ; preds = %for.cond
  store i32 0, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond20

for.cond20:                                       ; preds = %for.inc42, %for.end19
  %9 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp21 = icmp slt i32 %9, 80, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp21, label %for.body23, label %for.end44, !taffo.initweight !15, !taffo.info !11

for.body23:                                       ; preds = %for.cond20
  %10 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom24 = sext i32 %10 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx25 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom24, !taffo.initweight !13, !taffo.info !9
  store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.initweight !14, !taffo.info !9
  store i32 0, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond26

for.cond26:                                       ; preds = %for.inc36, %for.body23
  %11 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp27 = icmp slt i32 %11, 100, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp27, label %for.body29, label %for.end38, !taffo.initweight !15, !taffo.info !11

for.body29:                                       ; preds = %for.cond26
  %12 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom30 = sext i32 %12 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx31 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom30, !taffo.initweight !13, !taffo.info !5
  %13 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom32 = sext i32 %13 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx33 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx31, i64 0, i64 %idxprom32, !taffo.initweight !14, !taffo.info !5
  %14 = load double, double* %arrayidx33, align 8, !taffo.initweight !15, !taffo.info !5
  %15 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom34 = sext i32 %15 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx35 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom34, !taffo.initweight !13, !taffo.info !9
  %16 = load double, double* %arrayidx35, align 8, !taffo.initweight !14, !taffo.info !9
  %add = fadd double %16, %14, !taffo.initweight !15, !taffo.info !9
  store double %add, double* %arrayidx35, align 8, !taffo.initweight !14, !taffo.info !9
  br label %for.inc36

for.inc36:                                        ; preds = %for.body29
  %17 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %inc37 = add nsw i32 %17, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc37, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond26

for.end38:                                        ; preds = %for.cond26
  %18 = load double, double* %float_n, align 8, !taffo.initweight !13, !taffo.info !5
  %19 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom39 = sext i32 %19 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx40 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom39, !taffo.initweight !13, !taffo.info !9
  %20 = load double, double* %arrayidx40, align 8, !taffo.initweight !14, !taffo.info !9
  %div41 = fdiv double %20, %18, !taffo.initweight !14, !taffo.info !5
  store double %div41, double* %arrayidx40, align 8, !taffo.initweight !14, !taffo.info !9
  br label %for.inc42

for.inc42:                                        ; preds = %for.end38
  %21 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %inc43 = add nsw i32 %21, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc43, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond20

for.end44:                                        ; preds = %for.cond20
  store i32 0, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond45

for.cond45:                                       ; preds = %for.inc62, %for.end44
  %22 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp46 = icmp slt i32 %22, 100, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp46, label %for.body48, label %for.end64, !taffo.initweight !15, !taffo.info !11

for.body48:                                       ; preds = %for.cond45
  store i32 0, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond49

for.cond49:                                       ; preds = %for.inc59, %for.body48
  %23 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp50 = icmp slt i32 %23, 80, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp50, label %for.body52, label %for.end61, !taffo.initweight !15, !taffo.info !11

for.body52:                                       ; preds = %for.cond49
  %24 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom53 = sext i32 %24 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx54 = getelementptr inbounds [80 x double], [80 x double]* %mean, i64 0, i64 %idxprom53, !taffo.initweight !13, !taffo.info !9
  %25 = load double, double* %arrayidx54, align 8, !taffo.initweight !14, !taffo.info !9
  %26 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom55 = sext i32 %26 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx56 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom55, !taffo.initweight !13, !taffo.info !5
  %27 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom57 = sext i32 %27 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx58 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx56, i64 0, i64 %idxprom57, !taffo.initweight !14, !taffo.info !5
  %28 = load double, double* %arrayidx58, align 8, !taffo.initweight !15, !taffo.info !5
  %sub = fsub double %28, %25, !taffo.initweight !15, !taffo.info !9
  store double %sub, double* %arrayidx58, align 8, !taffo.initweight !15, !taffo.info !5
  br label %for.inc59

for.inc59:                                        ; preds = %for.body52
  %29 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %inc60 = add nsw i32 %29, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc60, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond49

for.end61:                                        ; preds = %for.cond49
  br label %for.inc62

for.inc62:                                        ; preds = %for.end61
  %30 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %inc63 = add nsw i32 %30, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc63, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond45

for.end64:                                        ; preds = %for.cond45
  store i32 0, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond65

for.cond65:                                       ; preds = %for.inc114, %for.end64
  %31 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp66 = icmp slt i32 %31, 80, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp66, label %for.body68, label %for.end116, !taffo.initweight !15, !taffo.info !11

for.body68:                                       ; preds = %for.cond65
  %32 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  store i32 %32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond69

for.cond69:                                       ; preds = %for.inc111, %for.body68
  %33 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp70 = icmp slt i32 %33, 80, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp70, label %for.body72, label %for.end113, !taffo.initweight !15, !taffo.info !11

for.body72:                                       ; preds = %for.cond69
  %34 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom73 = sext i32 %34 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx74 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom73, !taffo.initweight !13, !taffo.info !7
  %35 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom75 = sext i32 %35 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx76 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx74, i64 0, i64 %idxprom75, !taffo.initweight !14, !taffo.info !7
  store double 0.000000e+00, double* %arrayidx76, align 8, !taffo.initweight !15, !taffo.info !7
  store i32 0, i32* %k, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond77

for.cond77:                                       ; preds = %for.inc95, %for.body72
  %36 = load i32, i32* %k, align 4, !taffo.initweight !13, !taffo.info !11
  %cmp78 = icmp slt i32 %36, 100, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp78, label %for.body80, label %for.end97, !taffo.initweight !15, !taffo.info !11

for.body80:                                       ; preds = %for.cond77
  %37 = load i32, i32* %k, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom81 = sext i32 %37 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx82 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom81, !taffo.initweight !13, !taffo.info !5
  %38 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom83 = sext i32 %38 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx84 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx82, i64 0, i64 %idxprom83, !taffo.initweight !14, !taffo.info !5
  %39 = load double, double* %arrayidx84, align 8, !taffo.initweight !15, !taffo.info !5
  %40 = load i32, i32* %k, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom85 = sext i32 %40 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx86 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %data, i64 0, i64 %idxprom85, !taffo.initweight !13, !taffo.info !5
  %41 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom87 = sext i32 %41 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx88 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx86, i64 0, i64 %idxprom87, !taffo.initweight !14, !taffo.info !5
  %42 = load double, double* %arrayidx88, align 8, !taffo.initweight !15, !taffo.info !5
  %mul89 = fmul double %39, %42, !taffo.initweight !16, !taffo.info !5
  %43 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom90 = sext i32 %43 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx91 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom90, !taffo.initweight !13, !taffo.info !7
  %44 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom92 = sext i32 %44 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx93 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx91, i64 0, i64 %idxprom92, !taffo.initweight !14, !taffo.info !7
  %45 = load double, double* %arrayidx93, align 8, !taffo.initweight !15, !taffo.info !7
  %add94 = fadd double %45, %mul89, !taffo.initweight !16, !taffo.info !7
  store double %add94, double* %arrayidx93, align 8, !taffo.initweight !15, !taffo.info !7
  br label %for.inc95

for.inc95:                                        ; preds = %for.body80
  %46 = load i32, i32* %k, align 4, !taffo.initweight !13, !taffo.info !11
  %inc96 = add nsw i32 %46, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc96, i32* %k, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond77

for.end97:                                        ; preds = %for.cond77
  %47 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom98 = sext i32 %47 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx99 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom98, !taffo.initweight !13, !taffo.info !7
  %48 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom100 = sext i32 %48 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx101 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx99, i64 0, i64 %idxprom100, !taffo.initweight !14, !taffo.info !7
  %49 = load double, double* %arrayidx101, align 8, !taffo.initweight !15, !taffo.info !7
  %div102 = fdiv double %49, 9.900000e+01, !taffo.initweight !16, !taffo.info !7
  store double %div102, double* %arrayidx101, align 8, !taffo.initweight !15, !taffo.info !7
  %50 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom103 = sext i32 %50 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx104 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom103, !taffo.initweight !13, !taffo.info !7
  %51 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom105 = sext i32 %51 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx106 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx104, i64 0, i64 %idxprom105, !taffo.initweight !14, !taffo.info !7
  %52 = load double, double* %arrayidx106, align 8, !taffo.initweight !15, !taffo.info !7
  %53 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom107 = sext i32 %53 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx108 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom107, !taffo.initweight !13, !taffo.info !7
  %54 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom109 = sext i32 %54 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx110 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx108, i64 0, i64 %idxprom109, !taffo.initweight !14, !taffo.info !7
  store double %52, double* %arrayidx110, align 8, !taffo.initweight !15, !taffo.info !7
  br label %for.inc111

for.inc111:                                       ; preds = %for.end97
  %55 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %inc112 = add nsw i32 %55, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc112, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond69

for.end113:                                       ; preds = %for.cond69
  br label %for.inc114

for.inc114:                                       ; preds = %for.end113
  %56 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %inc115 = add nsw i32 %56, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc115, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond65

for.end116:                                       ; preds = %for.cond65
  store i32 0, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond117

for.cond117:                                      ; preds = %for.inc137, %for.end116
  %57 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %58 = load i32, i32* %m, align 4
  %cmp118 = icmp slt i32 %57, %58, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp118, label %for.body120, label %for.end139, !taffo.initweight !15, !taffo.info !11

for.body120:                                      ; preds = %for.cond117
  store i32 0, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond121

for.cond121:                                      ; preds = %for.inc134, %for.body120
  %59 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %60 = load i32, i32* %m, align 4
  %cmp122 = icmp slt i32 %59, %60, !taffo.initweight !14, !taffo.info !11
  br i1 %cmp122, label %for.body124, label %for.end136, !taffo.initweight !15, !taffo.info !11

for.body124:                                      ; preds = %for.cond121
  %61 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %62 = load i32, i32* %m, align 4
  %mul125 = mul nsw i32 %61, %62, !taffo.initweight !14, !taffo.info !11
  %63 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %add126 = add nsw i32 %mul125, %63, !taffo.initweight !14, !taffo.info !11
  %rem = srem i32 %add126, 20, !taffo.initweight !15, !taffo.info !11
  %cmp127 = icmp eq i32 %rem, 0, !taffo.initweight !16, !taffo.info !11
  br i1 %cmp127, label %if.then, label %if.end, !taffo.initweight !17, !taffo.info !11

if.then:                                          ; preds = %for.body124
  %64 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %call = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %64, i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.5, i32 0, i32 0))
  br label %if.end

if.end:                                           ; preds = %if.then, %for.body124
  %65 = load %struct._IO_FILE*, %struct._IO_FILE** @stdout, align 8
  %66 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom129 = sext i32 %66 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx130 = getelementptr inbounds [100 x [80 x double]], [100 x [80 x double]]* %cov, i64 0, i64 %idxprom129, !taffo.initweight !13, !taffo.info !7
  %67 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %idxprom131 = sext i32 %67 to i64, !taffo.initweight !14, !taffo.info !11
  %arrayidx132 = getelementptr inbounds [80 x double], [80 x double]* %arrayidx130, i64 0, i64 %idxprom131, !taffo.initweight !14, !taffo.info !7
  %68 = load double, double* %arrayidx132, align 8, !taffo.initweight !15, !taffo.info !7
  %call133 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %65, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.6, i32 0, i32 0), double %68), !taffo.initweight !16, !taffo.info !7
  br label %for.inc134

for.inc134:                                       ; preds = %if.end
  %69 = load i32, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  %inc135 = add nsw i32 %69, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc135, i32* %j, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond121

for.end136:                                       ; preds = %for.cond121
  br label %for.inc137

for.inc137:                                       ; preds = %for.end136
  %70 = load i32, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  %inc138 = add nsw i32 %70, 1, !taffo.initweight !14, !taffo.info !11
  store i32 %inc138, i32* %i, align 4, !taffo.initweight !13, !taffo.info !11
  br label %for.cond117

for.end139:                                       ; preds = %for.cond117
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !18 !taffo.funinfo !19 void @llvm.var.annotation(i8*, i8*, i8*, i32) #1

declare !taffo.initweight !2 !taffo.funinfo !3 dso_local i32 @fprintf(%struct._IO_FILE*, i8*, ...) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind }
attributes #2 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!2 = !{i32 -1, i32 -1}
!3 = !{i32 0, i1 false, i32 0, i1 false}
!4 = !{i32 0}
!5 = !{i1 false, !6, i1 false, i2 -1}
!6 = !{double -1.000000e+04, double 1.000000e+04}
!7 = !{i1 false, !8, i1 false, i2 -1}
!8 = !{double -1.000000e+04, double 1.000000e+05}
!9 = !{i1 false, !10, i1 false, i2 -1}
!10 = !{double -5.000000e+03, double 5.000000e+03}
!11 = !{i1 false, !12, i1 false, i2 0}
!12 = !{double 1.000000e+00, double 1.000000e+02}
!13 = !{i32 1}
!14 = !{i32 2}
!15 = !{i32 3}
!16 = !{i32 4}
!17 = !{i32 5}
!18 = !{i32 -1, i32 -1, i32 -1, i32 -1}
!19 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
