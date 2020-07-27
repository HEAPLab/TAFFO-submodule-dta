	.text
	.file	"corr.c"
	.globl	gettime                 # -- Begin function gettime
	.p2align	4, 0x90
	.type	gettime,@function
gettime:                                # @gettime
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movb	$0, %al
	callq	clock
	cltq
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	gettime, .Lfunc_end0-gettime
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_START   # -- Begin function TIMING_CPUCLOCK_START
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_START,@function
TIMING_CPUCLOCK_START:                  # @TIMING_CPUCLOCK_START
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	callq	gettime
	movq	%rax, time_that_takes
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end1:
	.size	TIMING_CPUCLOCK_START, .Lfunc_end1-TIMING_CPUCLOCK_START
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_TOGGLE  # -- Begin function TIMING_CPUCLOCK_TOGGLE
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_TOGGLE,@function
TIMING_CPUCLOCK_TOGGLE:                 # @TIMING_CPUCLOCK_TOGGLE
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	callq	gettime
	subq	time_that_takes, %rax
	movq	%rax, time_that_takes
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end2:
	.size	TIMING_CPUCLOCK_TOGGLE, .Lfunc_end2-TIMING_CPUCLOCK_TOGGLE
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_S       # -- Begin function TIMING_CPUCLOCK_S
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_S,@function
TIMING_CPUCLOCK_S:                      # @TIMING_CPUCLOCK_S
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movq	time_that_takes, %rax
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end3:
	.size	TIMING_CPUCLOCK_S, .Lfunc_end3-TIMING_CPUCLOCK_S
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_PRINT   # -- Begin function TIMING_CPUCLOCK_PRINT
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_PRINT,@function
TIMING_CPUCLOCK_PRINT:                  # @TIMING_CPUCLOCK_PRINT
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	movq	stderr, %rdi
	movq	time_that_takes, %rdx
	movabsq	$.L.str, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -4(%rbp)          # 4-byte Spill
	addq	$16, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end4:
	.size	TIMING_CPUCLOCK_PRINT, .Lfunc_end4-TIMING_CPUCLOCK_PRINT
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function main
.LCPI5_0:
	.long	1065353216              # float 1
.LCPI5_2:
	.long	1036831949              # float 0.100000001
.LCPI5_3:
	.long	1105199104              # float 28
.LCPI5_4:
	.long	1107296256              # float 32
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3
.LCPI5_1:
	.quad	4628574517030027264     # double 28
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$8080, %rsp             # imm = 0x1F90
	callq	TIMING_CPUCLOCK_START
	xorl	%eax, %eax
	movl	%eax, -7940(%rbp)       # 4-byte Spill
.LBB5_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_3 Depth 2
	movl	-7940(%rbp), %eax       # 4-byte Reload
	cvtsi2ssl	%eax, %xmm0
	cmpl	$28, %eax
	movl	%eax, -7944(%rbp)       # 4-byte Spill
	movss	%xmm0, -7948(%rbp)      # 4-byte Spill
	jge	.LBB5_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB5_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -7952(%rbp)       # 4-byte Spill
	jmp	.LBB5_3
.LBB5_3:                                # %for.cond9
                                        #   Parent Loop BB5_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-7952(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -7956(%rbp)       # 4-byte Spill
	jge	.LBB5_6
# %bb.4:                                # %for.body11
                                        #   in Loop: Header=BB5_3 Depth=2
	movss	.LCPI5_3(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI5_4(%rip), %xmm1   # xmm1 = mem[0],zero,zero,zero
	movl	-7944(%rbp), %eax       # 4-byte Reload
	movl	-7956(%rbp), %ecx       # 4-byte Reload
	imull	%ecx, %eax
	cvtsi2ssl	%eax, %xmm2
	divss	%xmm1, %xmm2
	movss	-7948(%rbp), %xmm1      # 4-byte Reload
                                        # xmm1 = mem[0],zero,zero,zero
	addss	%xmm1, %xmm2
	divss	%xmm0, %xmm2
	movl	-7944(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rdx
	shlq	$7, %rdx
	leaq	-3712(%rbp), %rsi
	addq	%rdx, %rsi
	movslq	%ecx, %rdx
	movss	%xmm2, (%rsi,%rdx,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB5_3 Depth=2
	movl	-7956(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7952(%rbp)       # 4-byte Spill
	jmp	.LBB5_3
.LBB5_6:                                # %for.end
                                        #   in Loop: Header=BB5_1 Depth=1
	jmp	.LBB5_7
.LBB5_7:                                # %for.inc16
                                        #   in Loop: Header=BB5_1 Depth=1
	movl	-7944(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7940(%rbp)       # 4-byte Spill
	jmp	.LBB5_1
.LBB5_8:                                # %for.end18
	xorl	%eax, %eax
	movl	%eax, -7960(%rbp)       # 4-byte Spill
	jmp	.LBB5_9
.LBB5_9:                                # %for.cond20
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_11 Depth 2
	movl	-7960(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -7964(%rbp)       # 4-byte Spill
	jge	.LBB5_16
# %bb.10:                               # %for.body23
                                        #   in Loop: Header=BB5_9 Depth=1
	xorl	%eax, %eax
	movl	-7964(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	xorps	%xmm0, %xmm0
	movss	%xmm0, -128(%rbp,%rdx,4)
	movl	%eax, -7968(%rbp)       # 4-byte Spill
.LBB5_11:                               # %for.cond26
                                        #   Parent Loop BB5_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-7968(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -7972(%rbp)       # 4-byte Spill
	jge	.LBB5_14
# %bb.12:                               # %for.body29
                                        #   in Loop: Header=BB5_11 Depth=2
	movl	-7972(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-7964(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	movss	(%rdx,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	movslq	%esi, %rcx
	addss	-128(%rbp,%rcx,4), %xmm0
	movss	%xmm0, -128(%rbp,%rcx,4)
# %bb.13:                               # %for.inc37
                                        #   in Loop: Header=BB5_11 Depth=2
	movl	-7972(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7968(%rbp)       # 4-byte Spill
	jmp	.LBB5_11
.LBB5_14:                               # %for.end39
                                        #   in Loop: Header=BB5_9 Depth=1
	movss	.LCPI5_3(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	-7964(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	-128(%rbp,%rcx,4), %xmm1 # xmm1 = mem[0],zero,zero,zero
	divss	%xmm0, %xmm1
	movss	%xmm1, -128(%rbp,%rcx,4)
# %bb.15:                               # %for.inc43
                                        #   in Loop: Header=BB5_9 Depth=1
	movl	-7964(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7960(%rbp)       # 4-byte Spill
	jmp	.LBB5_9
.LBB5_16:                               # %for.end45
	xorl	%eax, %eax
	movl	%eax, -7976(%rbp)       # 4-byte Spill
	jmp	.LBB5_17
.LBB5_17:                               # %for.cond46
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_19 Depth 2
	movl	-7976(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -7980(%rbp)       # 4-byte Spill
	jge	.LBB5_27
# %bb.18:                               # %for.body49
                                        #   in Loop: Header=BB5_17 Depth=1
	xorl	%eax, %eax
	movl	-7980(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	xorps	%xmm0, %xmm0
	movss	%xmm0, -7936(%rbp,%rdx,4)
	movl	%eax, -7984(%rbp)       # 4-byte Spill
.LBB5_19:                               # %for.cond52
                                        #   Parent Loop BB5_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-7984(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -7988(%rbp)       # 4-byte Spill
	jge	.LBB5_22
# %bb.20:                               # %for.body55
                                        #   in Loop: Header=BB5_19 Depth=2
	movl	-7988(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-7980(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	movslq	%edi, %rcx
	subss	-128(%rbp,%rcx,4), %xmm0
	movslq	%eax, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movss	(%rdx,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	movslq	%edi, %rcx
	subss	-128(%rbp,%rcx,4), %xmm1
	cvtss2sd	%xmm0, %xmm0
	cvtss2sd	%xmm1, %xmm1
	mulsd	%xmm1, %xmm0
	movslq	%edi, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm1 # xmm1 = mem[0],zero,zero,zero
	cvtsd2ss	%xmm0, %xmm0
	addss	%xmm0, %xmm1
	movss	%xmm1, -7936(%rbp,%rcx,4)
# %bb.21:                               # %for.inc73
                                        #   in Loop: Header=BB5_19 Depth=2
	movl	-7988(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7984(%rbp)       # 4-byte Spill
	jmp	.LBB5_19
.LBB5_22:                               # %for.end75
                                        #   in Loop: Header=BB5_17 Depth=1
	movss	.LCPI5_2(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI5_3(%rip), %xmm1   # xmm1 = mem[0],zero,zero,zero
	movl	-7980(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm2 # xmm2 = mem[0],zero,zero,zero
	divss	%xmm1, %xmm2
	movss	%xmm2, -7936(%rbp,%rcx,4)
	movslq	%eax, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm1 # xmm1 = mem[0],zero,zero,zero
	cvtss2sd	%xmm1, %xmm1
	movss	%xmm0, -7992(%rbp)      # 4-byte Spill
	movaps	%xmm1, %xmm0
	callq	sqrt
	movl	-7980(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	cvtsd2ss	%xmm0, %xmm0
	movss	%xmm0, -7936(%rbp,%rcx,4)
	movslq	%eax, %rcx
	movss	-7992(%rbp), %xmm0      # 4-byte Reload
                                        # xmm0 = mem[0],zero,zero,zero
	ucomiss	-7936(%rbp,%rcx,4), %xmm0
	jb	.LBB5_24
# %bb.23:                               # %cond.true
                                        #   in Loop: Header=BB5_17 Depth=1
	movss	.LCPI5_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, -7996(%rbp)      # 4-byte Spill
	jmp	.LBB5_25
.LBB5_24:                               # %cond.false
                                        #   in Loop: Header=BB5_17 Depth=1
	movl	-7980(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm0 # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, -7996(%rbp)      # 4-byte Spill
.LBB5_25:                               # %cond.end
                                        #   in Loop: Header=BB5_17 Depth=1
	movss	-7996(%rbp), %xmm0      # 4-byte Reload
                                        # xmm0 = mem[0],zero,zero,zero
	movl	-7980(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	%xmm0, -7936(%rbp,%rcx,4)
# %bb.26:                               # %for.inc91
                                        #   in Loop: Header=BB5_17 Depth=1
	movl	-7980(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7976(%rbp)       # 4-byte Spill
	jmp	.LBB5_17
.LBB5_27:                               # %for.end93
	xorl	%eax, %eax
	movl	%eax, -8000(%rbp)       # 4-byte Spill
	jmp	.LBB5_28
.LBB5_28:                               # %for.cond94
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_30 Depth 2
	movl	-8000(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -8004(%rbp)       # 4-byte Spill
	jge	.LBB5_35
# %bb.29:                               # %for.body97
                                        #   in Loop: Header=BB5_28 Depth=1
	xorl	%eax, %eax
	movl	%eax, -8008(%rbp)       # 4-byte Spill
	jmp	.LBB5_30
.LBB5_30:                               # %for.cond98
                                        #   Parent Loop BB5_28 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-8008(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8012(%rbp)       # 4-byte Spill
	jge	.LBB5_33
# %bb.31:                               # %for.body101
                                        #   in Loop: Header=BB5_30 Depth=2
	movl	-8012(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	-128(%rbp,%rcx,4), %xmm0 # xmm0 = mem[0],zero,zero,zero
	movl	-8004(%rbp), %edx       # 4-byte Reload
	movslq	%edx, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rsi
	movq	%rsi, %rdi
	addq	%rcx, %rdi
	movslq	%eax, %rcx
	movss	(%rdi,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	subss	%xmm0, %xmm1
	movss	%xmm1, (%rdi,%rcx,4)
	movsd	.LCPI5_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	%rsi, -8024(%rbp)       # 8-byte Spill
	callq	sqrt
	movl	-8012(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm1 # xmm1 = mem[0],zero,zero,zero
	cvtss2sd	%xmm1, %xmm1
	mulsd	%xmm1, %xmm0
	movl	-8004(%rbp), %edx       # 4-byte Reload
	movslq	%edx, %rcx
	shlq	$7, %rcx
	movq	-8024(%rbp), %rsi       # 8-byte Reload
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	movss	(%rsi,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	cvtsd2ss	%xmm0, %xmm0
	divss	%xmm0, %xmm1
	movss	%xmm1, (%rsi,%rcx,4)
# %bb.32:                               # %for.inc118
                                        #   in Loop: Header=BB5_30 Depth=2
	movl	-8012(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8008(%rbp)       # 4-byte Spill
	jmp	.LBB5_30
.LBB5_33:                               # %for.end120
                                        #   in Loop: Header=BB5_28 Depth=1
	jmp	.LBB5_34
.LBB5_34:                               # %for.inc121
                                        #   in Loop: Header=BB5_28 Depth=1
	movl	-8004(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8000(%rbp)       # 4-byte Spill
	jmp	.LBB5_28
.LBB5_35:                               # %for.end123
	xorl	%eax, %eax
	movl	%eax, -8028(%rbp)       # 4-byte Spill
	jmp	.LBB5_36
.LBB5_36:                               # %for.cond124
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_38 Depth 2
                                        #       Child Loop BB5_40 Depth 3
	movl	-8028(%rbp), %eax       # 4-byte Reload
	cmpl	$31, %eax
	movl	%eax, -8032(%rbp)       # 4-byte Spill
	jge	.LBB5_47
# %bb.37:                               # %for.body127
                                        #   in Loop: Header=BB5_36 Depth=1
	movss	.LCPI5_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	-8032(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movss	%xmm0, (%rdx,%rcx,4)
	addl	$1, %eax
	movl	%eax, -8036(%rbp)       # 4-byte Spill
.LBB5_38:                               # %for.cond133
                                        #   Parent Loop BB5_36 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_40 Depth 3
	movl	-8036(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8040(%rbp)       # 4-byte Spill
	jge	.LBB5_45
# %bb.39:                               # %for.body136
                                        #   in Loop: Header=BB5_38 Depth=2
	xorl	%eax, %eax
	movl	-8032(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	shlq	$7, %rdx
	leaq	-7808(%rbp), %rsi
	addq	%rdx, %rsi
	movl	-8040(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rdx
	xorps	%xmm0, %xmm0
	movss	%xmm0, (%rsi,%rdx,4)
	movl	%eax, -8044(%rbp)       # 4-byte Spill
.LBB5_40:                               # %for.cond141
                                        #   Parent Loop BB5_36 Depth=1
                                        #     Parent Loop BB5_38 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-8044(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -8048(%rbp)       # 4-byte Spill
	jge	.LBB5_43
# %bb.41:                               # %for.body144
                                        #   in Loop: Header=BB5_40 Depth=3
	movl	-8048(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-8032(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	movslq	%eax, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movl	-8040(%rbp), %r8d       # 4-byte Reload
	movslq	%r8d, %rcx
	movss	(%rdx,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	cvtss2sd	%xmm1, %xmm1
	mulsd	%xmm1, %xmm0
	movslq	%edi, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%r8d, %rcx
	movss	(%rdx,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	cvtsd2ss	%xmm0, %xmm0
	addss	%xmm0, %xmm1
	movss	%xmm1, (%rdx,%rcx,4)
# %bb.42:                               # %for.inc159
                                        #   in Loop: Header=BB5_40 Depth=3
	movl	-8048(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8044(%rbp)       # 4-byte Spill
	jmp	.LBB5_40
.LBB5_43:                               # %for.end161
                                        #   in Loop: Header=BB5_38 Depth=2
	movl	-8032(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-8040(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	movslq	%edi, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movss	%xmm0, (%rdx,%rcx,4)
# %bb.44:                               # %for.inc170
                                        #   in Loop: Header=BB5_38 Depth=2
	movl	-8040(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8036(%rbp)       # 4-byte Spill
	jmp	.LBB5_38
.LBB5_45:                               # %for.end172
                                        #   in Loop: Header=BB5_36 Depth=1
	jmp	.LBB5_46
.LBB5_46:                               # %for.inc173
                                        #   in Loop: Header=BB5_36 Depth=1
	movl	-8032(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8028(%rbp)       # 4-byte Spill
	jmp	.LBB5_36
.LBB5_47:                               # %for.end175
	xorl	%eax, %eax
	movss	.LCPI5_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, -3716(%rbp)
	movl	%eax, -8052(%rbp)       # 4-byte Spill
.LBB5_48:                               # %for.cond178
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_50 Depth 2
	movl	-8052(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8056(%rbp)       # 4-byte Spill
	jge	.LBB5_55
# %bb.49:                               # %for.body181
                                        #   in Loop: Header=BB5_48 Depth=1
	xorl	%eax, %eax
	movl	%eax, -8060(%rbp)       # 4-byte Spill
	jmp	.LBB5_50
.LBB5_50:                               # %for.cond182
                                        #   Parent Loop BB5_48 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-8060(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8064(%rbp)       # 4-byte Spill
	jge	.LBB5_53
# %bb.51:                               # %for.body185
                                        #   in Loop: Header=BB5_50 Depth=2
	movl	-8056(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-8064(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	movss	(%rdx,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	movabsq	$.L.str.10, %rdi
	movb	$1, %al
	callq	printf
	movl	%eax, -8068(%rbp)       # 4-byte Spill
# %bb.52:                               # %for.inc191
                                        #   in Loop: Header=BB5_50 Depth=2
	movl	-8064(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8060(%rbp)       # 4-byte Spill
	jmp	.LBB5_50
.LBB5_53:                               # %for.end193
                                        #   in Loop: Header=BB5_48 Depth=1
	movabsq	$.L.str.11, %rdi
	movb	$0, %al
	callq	printf
	movl	%eax, -8072(%rbp)       # 4-byte Spill
# %bb.54:                               # %for.inc195
                                        #   in Loop: Header=BB5_48 Depth=1
	movl	-8056(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8052(%rbp)       # 4-byte Spill
	jmp	.LBB5_48
.LBB5_55:                               # %for.end197
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	addq	$8080, %rsp             # imm = 0x1F90
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end5:
	.size	main, .Lfunc_end5-main
	.cfi_endproc
                                        # -- End function
	.type	time_that_takes,@object # @time_that_takes
	.comm	time_that_takes,8,8
	.type	.L.str,@object          # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"%ld"
	.size	.L.str, 4

	.type	.L.str.10,@object       # @.str.10
.L.str.10:
	.asciz	"%.16lf "
	.size	.L.str.10, 8

	.type	.L.str.11,@object       # @.str.11
.L.str.11:
	.asciz	"\n"
	.size	.L.str.11, 2


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym gettime
	.addrsig_sym clock
	.addrsig_sym TIMING_CPUCLOCK_START
	.addrsig_sym TIMING_CPUCLOCK_TOGGLE
	.addrsig_sym TIMING_CPUCLOCK_PRINT
	.addrsig_sym fprintf
	.addrsig_sym sqrt
	.addrsig_sym printf
	.addrsig_sym time_that_takes
	.addrsig_sym stderr
