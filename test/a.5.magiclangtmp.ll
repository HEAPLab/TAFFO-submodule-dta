; ModuleID = 'a.4.magiclangtmp.ll'
source_filename = "cconv.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [3 x i8] c"%f\00", align 1, !taffo.info !0
@.str.1 = private unnamed_addr constant [5 x i8] c"%f, \00", align 1, !taffo.info !0

; Function Attrs: noinline nounwind uwtable
define dso_local void @arrayLoad(float* %array, i32 %elem) #0 !taffo.initweight !4 !taffo.equivalentChild !5 !taffo.funinfo !6 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc, %for.inc ]
  %cmp = icmp slt i32 %i.0, %elem
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %idxprom = sext i32 %i.0 to i64
  %arrayidx = getelementptr inbounds float, float* %array, i64 %idxprom
  %call = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), float* %arrayidx), !taffo.constinfo !7
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %inc = add nsw i32 %i.0, 1, !taffo.constinfo !8
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

declare !taffo.initweight !9 !taffo.funinfo !10 dso_local i32 @__isoc99_scanf(i8*, ...) #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @arrayInit(float* %array, i32 %elem, float %value) #0 !taffo.initweight !11 !taffo.funinfo !12 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc, %for.inc ]
  %cmp = icmp slt i32 %i.0, %elem
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %idxprom = sext i32 %i.0 to i64
  %arrayidx = getelementptr inbounds float, float* %array, i64 %idxprom
  store float %value, float* %arrayidx, align 4
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %inc = add nsw i32 %i.0, 1, !taffo.constinfo !8
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local void @printArray(float* %array, i32 %elem) #0 !taffo.initweight !4 !taffo.funinfo !6 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc, %for.inc ]
  %cmp = icmp slt i32 %i.0, %elem
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %idxprom = sext i32 %i.0 to i64
  %arrayidx = getelementptr inbounds float, float* %array, i64 %idxprom
  %0 = load float, float* %arrayidx, align 4
  %conv = fpext float %0 to double
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.1, i32 0, i32 0), double %conv), !taffo.constinfo !7
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %inc = add nsw i32 %i.0, 1, !taffo.constinfo !8
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

declare !taffo.initweight !9 !taffo.funinfo !10 dso_local i32 @printf(i8*, ...) #1

; Function Attrs: noinline nounwind uwtable
define dso_local void @cconv(float* %xn, float* %h, float* %res, i32 %elem) #0 !taffo.initweight !13 !taffo.equivalentChild !14 !taffo.funinfo !15 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.inc9, %entry
  %n.0 = phi i32 [ 0, %entry ], [ %inc10, %for.inc9 ]
  %cmp = icmp slt i32 %n.0, %elem
  br i1 %cmp, label %for.body, label %for.end11

for.body:                                         ; preds = %for.cond
  br label %for.cond1

for.cond1:                                        ; preds = %for.inc, %for.body
  %i.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ]
  %cmp2 = icmp slt i32 %i.0, %elem
  br i1 %cmp2, label %for.body3, label %for.end

for.body3:                                        ; preds = %for.cond1
  %idxprom = sext i32 %i.0 to i64
  %arrayidx = getelementptr inbounds float, float* %h, i64 %idxprom
  %0 = load float, float* %arrayidx, align 4
  %sub = sub nsw i32 %n.0, %i.0
  %add = add nsw i32 %sub, 10, !taffo.constinfo !8
  %rem = srem i32 %add, 10, !taffo.constinfo !8
  %idxprom4 = sext i32 %rem to i64
  %arrayidx5 = getelementptr inbounds float, float* %xn, i64 %idxprom4
  %1 = load float, float* %arrayidx5, align 4
  %mul = fmul float %0, %1
  %idxprom6 = sext i32 %n.0 to i64
  %arrayidx7 = getelementptr inbounds float, float* %res, i64 %idxprom6
  %2 = load float, float* %arrayidx7, align 4
  %add8 = fadd float %2, %mul
  store float %add8, float* %arrayidx7, align 4
  br label %for.inc

for.inc:                                          ; preds = %for.body3
  %inc = add nsw i32 %i.0, 1, !taffo.constinfo !8
  br label %for.cond1

for.end:                                          ; preds = %for.cond1
  br label %for.inc9

for.inc9:                                         ; preds = %for.end
  %inc10 = add nsw i32 %n.0, 1, !taffo.constinfo !8
  br label %for.cond

for.end11:                                        ; preds = %for.cond
  ret void
}

; Function Attrs: noinline nounwind uwtable
define dso_local i32 @main() #0 !taffo.initweight !16 !taffo.funinfo !16 {
entry:
  %xn = alloca [10 x float], align 16, !taffo.info !17, !taffo.initweight !20
  %h = alloca [10 x float], align 16, !taffo.info !17, !taffo.initweight !20
  %res = alloca [10 x float], align 16
  %arraydecay = getelementptr inbounds [10 x float], [10 x float]* %xn, i32 0, i32 0, !taffo.info !17, !taffo.initweight !21
  call void @arrayLoad.1_fixp(float* %arraydecay, i32 10), !taffo.info !22, !taffo.constinfo !7
  %arraydecay3 = getelementptr inbounds [10 x float], [10 x float]* %h, i32 0, i32 0, !taffo.info !17, !taffo.initweight !21
  call void @arrayLoad.1_fixp(float* %arraydecay3, i32 10), !taffo.info !22, !taffo.constinfo !7
  %arraydecay4 = getelementptr inbounds [10 x float], [10 x float]* %res, i32 0, i32 0
  call void @arrayInit(float* %arraydecay4, i32 10, float 0.000000e+00), !taffo.constinfo !23
  %arraydecay5 = getelementptr inbounds [10 x float], [10 x float]* %xn, i32 0, i32 0, !taffo.info !17, !taffo.initweight !21
  %arraydecay6 = getelementptr inbounds [10 x float], [10 x float]* %h, i32 0, i32 0, !taffo.info !17, !taffo.initweight !21
  %arraydecay7 = getelementptr inbounds [10 x float], [10 x float]* %res, i32 0, i32 0
  call void @cconv.2_fixp(float* %arraydecay5, float* %arraydecay6, float* %arraydecay7, i32 10), !taffo.info !22, !taffo.constinfo !26
  %arraydecay8 = getelementptr inbounds [10 x float], [10 x float]* %res, i32 0, i32 0
  call void @printArray(float* %arraydecay8, i32 10), !taffo.constinfo !7
  ret i32 0
}

; Function Attrs: noinline nounwind uwtable
define internal void @arrayLoad.1_fixp(float* %array, i32 %elem) #0 !taffo.initweight !27 !taffo.funinfo !28 !taffo.sourceFunction !29 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %i.0 = phi i32 [ 0, %entry ], [ %inc, %for.inc ]
  %cmp = icmp slt i32 %i.0, %elem
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %idxprom = sext i32 %i.0 to i64
  %arrayidx = getelementptr inbounds float, float* %array, i64 %idxprom
  %call = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), float* %arrayidx), !taffo.constinfo !7
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %inc = add nsw i32 %i.0, 1, !taffo.constinfo !8
  br label %for.cond

for.end:                                          ; preds = %for.cond
  ret void
}

; Function Attrs: noinline nounwind uwtable
define internal void @cconv.2_fixp(float* %xn, float* %h, float* %res, i32 %elem) #0 !taffo.initweight !30 !taffo.funinfo !31 !taffo.sourceFunction !32 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.inc9, %entry
  %n.0 = phi i32 [ 0, %entry ], [ %inc10, %for.inc9 ]
  %cmp = icmp slt i32 %n.0, %elem
  br i1 %cmp, label %for.body, label %for.end11

for.body:                                         ; preds = %for.cond
  br label %for.cond1

for.cond1:                                        ; preds = %for.inc, %for.body
  %i.0 = phi i32 [ 0, %for.body ], [ %inc, %for.inc ]
  %cmp2 = icmp slt i32 %i.0, %elem
  br i1 %cmp2, label %for.body3, label %for.end

for.body3:                                        ; preds = %for.cond1
  %idxprom = sext i32 %i.0 to i64
  %arrayidx = getelementptr inbounds float, float* %h, i64 %idxprom
  %0 = load float, float* %arrayidx, align 4
  %sub = sub nsw i32 %n.0, %i.0
  %add = add nsw i32 %sub, 10, !taffo.constinfo !8
  %rem = srem i32 %add, 10, !taffo.constinfo !8
  %idxprom4 = sext i32 %rem to i64
  %arrayidx5 = getelementptr inbounds float, float* %xn, i64 %idxprom4
  %1 = load float, float* %arrayidx5, align 4
  %mul = fmul float %0, %1
  %idxprom6 = sext i32 %n.0 to i64
  %arrayidx7 = getelementptr inbounds float, float* %res, i64 %idxprom6
  %2 = load float, float* %arrayidx7, align 4
  %add8 = fadd float %2, %mul
  store float %add8, float* %arrayidx7, align 4
  br label %for.inc

for.inc:                                          ; preds = %for.body3
  %inc = add nsw i32 %i.0, 1, !taffo.constinfo !8
  br label %for.cond1

for.end:                                          ; preds = %for.cond1
  br label %for.inc9

for.inc9:                                         ; preds = %for.end
  %inc10 = add nsw i32 %n.0, 1, !taffo.constinfo !8
  br label %for.cond

for.end11:                                        ; preds = %for.cond
  ret void
}

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!2}
!llvm.ident = !{!3}

!0 = !{i1 false, !1, i1 false, i2 0}
!1 = !{double 0.000000e+00, double 1.020000e+02}
!2 = !{i32 1, !"wchar_size", i32 4}
!3 = !{!"clang version 8.0.1 (tags/RELEASE_801/final)"}
!4 = !{i32 -1, i32 -1}
!5 = distinct !{null, null}
!6 = !{i32 0, i1 false, i32 0, i1 false}
!7 = !{i1 false, i1 false, i1 false}
!8 = !{i1 false, i1 false}
!9 = !{i32 -1}
!10 = !{i32 0, i1 false}
!11 = !{i32 -1, i32 -1, i32 -1}
!12 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
!13 = !{i32 -1, i32 -1, i32 -1, i32 -1}
!14 = distinct !{null}
!15 = !{i32 0, i1 false, i32 0, i1 false, i32 0, i1 false, i32 0, i1 false}
!16 = !{}
!17 = !{!18, !19, i1 false, i2 1}
!18 = !{!"float", i32 0, double 2.000000e+01}
!19 = !{double 1.000000e+00, double 2.000000e+01}
!20 = !{i32 0}
!21 = !{i32 1}
!22 = !{i1 false, !19, i1 false, i2 1}
!23 = !{i1 false, i1 false, !24, i1 false}
!24 = !{i1 false, !25, i1 false, i2 0}
!25 = !{double 0.000000e+00, double 0.000000e+00}
!26 = !{i1 false, i1 false, i1 false, i1 false, i1 false}
!27 = !{i32 2, i32 -1}
!28 = !{i32 1, !17, i32 0, i1 false}
!29 = !{void (float*, i32)* @arrayLoad}
!30 = !{i32 2, i32 2, i32 -1, i32 -1}
!31 = !{i32 1, !17, i32 1, !17, i32 0, i1 false, i32 0, i1 false}
!32 = !{void (float*, float*, float*, i32)* @cconv}
