; ModuleID = 'a.1.magiclangtmp.ll'
source_filename = "cconv.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [3 x i8] c"%f\00", align 1
@.str.1 = private unnamed_addr constant [5 x i8] c"%f, \00", align 1
@.str.2 = private unnamed_addr constant [21 x i8] c"scalar(range(1, 20))\00", section "llvm.metadata"
@.str.3 = private unnamed_addr constant [8 x i8] c"cconv.c\00", section "llvm.metadata"

; Function Attrs: noinline nounwind uwtable
define dso_local void @arrayLoad(float* %array, i32 %elem) #0 !taffo.initweight !2 !taffo.equivalentChild !3 !taffo.funinfo !4 {
entry:
  %array.addr = alloca float*, align 8
  %elem.addr = alloca i32, align 4
  %i = alloca i32, align 4
  store float* %array, float** %array.addr, align 8
  store i32 %elem, i32* %elem.addr, align 4
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %0 = load i32, i32* %i, align 4
  %1 = load i32, i32* %elem.addr, align 4
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %2 = load float*, float** %array.addr, align 8
  %3 = load i32, i32* %i, align 4
  %idxprom = sext i32 %3 to i64
  %arrayidx = getelementptr inbounds float, float* %2, i64 %idxprom
  %call = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), float* %arrayidx)
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %4 = load i32, i32* %i, align 4
  %inc = add nsw i32 %4, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

declare !taffo.initweight !5 !taffo.funinfo !6 dso_local i32 @__isoc99_scanf(i8*, ...) #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @arrayInit(float* %array, i32 %elem, float %value) #0 !taffo.initweight !7 !taffo.funinfo !8 {
entry:
  %array.addr = alloca float*, align 8
  %elem.addr = alloca i32, align 4
  %value.addr = alloca float, align 4
  %i = alloca i32, align 4
  store float* %array, float** %array.addr, align 8
  store i32 %elem, i32* %elem.addr, align 4
  store float %value, float* %value.addr, align 4
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %0 = load i32, i32* %i, align 4
  %1 = load i32, i32* %elem.addr, align 4
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %2 = load float, float* %value.addr, align 4
  %3 = load float*, float** %array.addr, align 8
  %4 = load i32, i32* %i, align 4
  %idxprom = sext i32 %4 to i64
  %arrayidx = getelementptr inbounds float, float* %3, i64 %idxprom
  store float %2, float* %arrayidx, align 4
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %5 = load i32, i32* %i, align 4
  %inc = add nsw i32 %5, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @printArray(float* %array, i32 %elem) #0 !taffo.initweight !2 !taffo.funinfo !4 {
entry:
  %array.addr = alloca float*, align 8
  %elem.addr = alloca i32, align 4
  %i = alloca i32, align 4
  store float* %array, float** %array.addr, align 8
  store i32 %elem, i32* %elem.addr, align 4
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %0 = load i32, i32* %i, align 4
  %1 = load i32, i32* %elem.addr, align 4
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %2 = load float*, float** %array.addr, align 8
  %3 = load i32, i32* %i, align 4
  %idxprom = sext i32 %3 to i64
  %arrayidx = getelementptr inbounds float, float* %2, i64 %idxprom
  %4 = load float, float* %arrayidx, align 4
  %conv = fpext float %4 to double
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.1, i32 0, i32 0), double %conv)
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %5 = load i32, i32* %i, align 4
  %inc = add nsw i32 %5, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

declare !taffo.initweight !5 !taffo.funinfo !6 dso_local i32 @printf(i8*, ...) #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @cconv(float* %xn, float* %h, float* %res, i32 %elem) #0 !taffo.initweight !9 !taffo.equivalentChild !10 !taffo.funinfo !11 {
entry:
  %xn.addr = alloca float*, align 8
  %h.addr = alloca float*, align 8
  %res.addr = alloca float*, align 8
  %elem.addr = alloca i32, align 4
  %n = alloca i32, align 4
  %i = alloca i32, align 4
  store float* %xn, float** %xn.addr, align 8
  store float* %h, float** %h.addr, align 8
  store float* %res, float** %res.addr, align 8
  store i32 %elem, i32* %elem.addr, align 4
  store i32 0, i32* %n, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc9, %entry
  %0 = load i32, i32* %n, align 4
  %1 = load i32, i32* %elem.addr, align 4
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %for.body, label %for.end11

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %i, align 4
  br label %for.cond1

for.cond1:                                        ; preds = %for.inc, %for.body
  %2 = load i32, i32* %i, align 4
  %3 = load i32, i32* %elem.addr, align 4
  %cmp2 = icmp slt i32 %2, %3
  br i1 %cmp2, label %for.body3, label %for.end

for.body3:                                        ; preds = %for.cond1
  %4 = load float*, float** %h.addr, align 8
  %5 = load i32, i32* %i, align 4
  %idxprom = sext i32 %5 to i64
  %arrayidx = getelementptr inbounds float, float* %4, i64 %idxprom
  %6 = load float, float* %arrayidx, align 4
  %7 = load float*, float** %xn.addr, align 8
  %8 = load i32, i32* %n, align 4
  %9 = load i32, i32* %i, align 4
  %sub = sub nsw i32 %8, %9
  %add = add nsw i32 %sub, 10
  %rem = srem i32 %add, 10
  %idxprom4 = sext i32 %rem to i64
  %arrayidx5 = getelementptr inbounds float, float* %7, i64 %idxprom4
  %10 = load float, float* %arrayidx5, align 4
  %mul = fmul float %6, %10
  %11 = load float*, float** %res.addr, align 8
  %12 = load i32, i32* %n, align 4
  %idxprom6 = sext i32 %12 to i64
  %arrayidx7 = getelementptr inbounds float, float* %11, i64 %idxprom6
  %13 = load float, float* %arrayidx7, align 4
  %add8 = fadd float %13, %mul
  store float %add8, float* %arrayidx7, align 4
  br label %for.inc

for.inc:                                          ; preds = %for.body3
  %14 = load i32, i32* %i, align 4
  %inc = add nsw i32 %14, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond1

for.end:                                          ; preds = %for.cond1
  br label %for.inc9

for.inc9:                                         ; preds = %for.end
  %15 = load i32, i32* %n, align 4
  %inc10 = add nsw i32 %15, 1
  store i32 %inc10, i32* %n, align 4
  br label %for.cond

for.end11:                                        ; preds = %for.cond
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !12 !taffo.funinfo !12 {
entry:
  %xn = alloca [10 x float], align 16, !taffo.initweight !13, !taffo.info !14
  %h = alloca [10 x float], align 16, !taffo.initweight !13, !taffo.info !14
  %res = alloca [10 x float], align 16
  %xn1 = bitcast [10 x float]* %xn to i8*, !taffo.initweight !16, !taffo.info !14
  %h2 = bitcast [10 x float]* %h to i8*, !taffo.initweight !16, !taffo.info !14
  %arraydecay = getelementptr inbounds [10 x float], [10 x float]* %xn, i32 0, i32 0, !taffo.initweight !16, !taffo.info !14
  call void @arrayLoad.1(float* %arraydecay, i32 10), !taffo.initweight !17, !taffo.info !14, !taffo.originalCall !18
  %arraydecay3 = getelementptr inbounds [10 x float], [10 x float]* %h, i32 0, i32 0, !taffo.initweight !16, !taffo.info !14
  call void @arrayLoad.3(float* %arraydecay3, i32 10), !taffo.initweight !17, !taffo.info !14, !taffo.originalCall !18
  %arraydecay4 = getelementptr inbounds [10 x float], [10 x float]* %res, i32 0, i32 0
  call void @arrayInit(float* %arraydecay4, i32 10, float 0.000000e+00)
  %arraydecay5 = getelementptr inbounds [10 x float], [10 x float]* %xn, i32 0, i32 0, !taffo.initweight !16, !taffo.info !14
  %arraydecay6 = getelementptr inbounds [10 x float], [10 x float]* %h, i32 0, i32 0, !taffo.initweight !16, !taffo.info !14
  %arraydecay7 = getelementptr inbounds [10 x float], [10 x float]* %res, i32 0, i32 0
  call void @cconv.2(float* %arraydecay5, float* %arraydecay6, float* %arraydecay7, i32 10), !taffo.initweight !17, !taffo.info !14, !taffo.originalCall !19
  %arraydecay8 = getelementptr inbounds [10 x float], [10 x float]* %res, i32 0, i32 0
  call void @printArray(float* %arraydecay8, i32 10)
  ret i32 0
}

; Function Attrs: nounwind
declare !taffo.initweight !9 !taffo.funinfo !11 void @llvm.var.annotation(i8*, i8*, i8*, i32) #2

; Function Attrs: noinline nounwind uwtable
define internal void @arrayLoad.1(float* %array, i32 %elem) #0 !taffo.initweight !20 !taffo.sourceFunction !18 !taffo.funinfo !21 {
entry:
  %array.addr = alloca float*, align 8
  %elem.addr = alloca i32, align 4
  %i = alloca i32, align 4
  store float* %array, float** %array.addr, align 8
  store i32 %elem, i32* %elem.addr, align 4
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %0 = load i32, i32* %i, align 4
  %1 = load i32, i32* %elem.addr, align 4
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %2 = load float*, float** %array.addr, align 8
  %3 = load i32, i32* %i, align 4
  %idxprom = sext i32 %3 to i64
  %arrayidx = getelementptr inbounds float, float* %2, i64 %idxprom
  %call = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), float* %arrayidx)
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %4 = load i32, i32* %i, align 4
  %inc = add nsw i32 %4, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

; Function Attrs: noinline nounwind uwtable
define internal void @cconv.2(float* %xn, float* %h, float* %res, i32 %elem) #0 !taffo.initweight !22 !taffo.sourceFunction !19 !taffo.funinfo !23 {
entry:
  %xn.addr = alloca float*, align 8
  %h.addr = alloca float*, align 8
  %res.addr = alloca float*, align 8
  %elem.addr = alloca i32, align 4
  %n = alloca i32, align 4
  %i = alloca i32, align 4
  store float* %xn, float** %xn.addr, align 8
  store float* %h, float** %h.addr, align 8
  store float* %res, float** %res.addr, align 8
  store i32 %elem, i32* %elem.addr, align 4
  store i32 0, i32* %n, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc9, %entry
  %0 = load i32, i32* %n, align 4
  %1 = load i32, i32* %elem.addr, align 4
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %for.body, label %for.end11

for.body:                                         ; preds = %for.cond
  store i32 0, i32* %i, align 4
  br label %for.cond1

for.cond1:                                        ; preds = %for.inc, %for.body
  %2 = load i32, i32* %i, align 4
  %3 = load i32, i32* %elem.addr, align 4
  %cmp2 = icmp slt i32 %2, %3
  br i1 %cmp2, label %for.body3, label %for.end

for.body3:                                        ; preds = %for.cond1
  %4 = load float*, float** %h.addr, align 8
  %5 = load i32, i32* %i, align 4
  %idxprom = sext i32 %5 to i64
  %arrayidx = getelementptr inbounds float, float* %4, i64 %idxprom
  %6 = load float, float* %arrayidx, align 4
  %7 = load float*, float** %xn.addr, align 8
  %8 = load i32, i32* %n, align 4
  %9 = load i32, i32* %i, align 4
  %sub = sub nsw i32 %8, %9
  %add = add nsw i32 %sub, 10
  %rem = srem i32 %add, 10
  %idxprom4 = sext i32 %rem to i64
  %arrayidx5 = getelementptr inbounds float, float* %7, i64 %idxprom4
  %10 = load float, float* %arrayidx5, align 4
  %mul = fmul float %6, %10
  %11 = load float*, float** %res.addr, align 8
  %12 = load i32, i32* %n, align 4
  %idxprom6 = sext i32 %12 to i64
  %arrayidx7 = getelementptr inbounds float, float* %11, i64 %idxprom6
  %13 = load float, float* %arrayidx7, align 4
  %add8 = fadd float %13, %mul
  store float %add8, float* %arrayidx7, align 4
  br label %for.inc

for.inc:                                          ; preds = %for.body3
  %14 = load i32, i32* %i, align 4
  %inc = add nsw i32 %14, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond1

for.end:                                          ; preds = %for.cond1
  br label %for.inc9

for.inc9:                                         ; preds = %for.end
  %15 = load i32, i32* %n, align 4
  %inc10 = add nsw i32 %15, 1
  store i32 %inc10, i32* %n, align 4
  br label %for.cond

for.end11:                                        ; preds = %for.cond
  ret void
}

; Function Attrs: noinline nounwind uwtable
define internal void @arrayLoad.3(float* %array, i32 %elem) #0 !taffo.initweight !20 !taffo.sourceFunction !18 !taffo.funinfo !21 {
entry:
  %array.addr = alloca float*, align 8
  %elem.addr = alloca i32, align 4
  %i = alloca i32, align 4
  store float* %array, float** %array.addr, align 8
  store i32 %elem, i32* %elem.addr, align 4
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %0 = load i32, i32* %i, align 4
  %1 = load i32, i32* %elem.addr, align 4
  %cmp = icmp slt i32 %0, %1
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %2 = load float*, float** %array.addr, align 8
  %3 = load i32, i32* %i, align 4
  %idxprom = sext i32 %3 to i64
  %arrayidx = getelementptr inbounds float, float* %2, i64 %idxprom
  %call = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), float* %arrayidx)
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %4 = load i32, i32* %i, align 4
  %inc = add nsw i32 %4, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!2 = !{i32 -1, i32 -1}
!3 = !{void (float*, i32)* @arrayLoad.1, void (float*, i32)* @arrayLoad.3}
!4 = !{i32 0, i1 false, i32 0, i1 false}
!5 = !{i32 -1}
!6 = !{i32 0, i1 false}
!7 = !{i32 -1, i32 -1, i32 -1}
!8 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
!9 = !{i32 -1, i32 -1, i32 -1, i32 -1}
!10 = !{void (float*, float*, float*, i32)* @cconv.2}
!11 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
!12 = !{}
!13 = !{i32 0}
!14 = !{i1 false, !15, i1 false, i2 1}
!15 = !{double 1.000000e+00, double 2.000000e+01}
!16 = !{i32 1}
!17 = !{i32 2}
!18 = !{void (float*, i32)* @arrayLoad}
!19 = !{void (float*, float*, float*, i32)* @cconv}
!20 = !{i32 2, i32 -1}
!21 = !{i32 1, !14, i32 0, i1 false}
!22 = !{i32 2, i32 2, i32 -1, i32 -1}
!23 = !{i32 1, !14, i32 1, !14, i32 0, i1 false, i32 0, i1 false}
