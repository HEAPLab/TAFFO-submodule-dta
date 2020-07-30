	.text
	.file	"covariance.c"
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
	callq	clock
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
	.globl	TAFFO_DUMPCONFIG        # -- Begin function TAFFO_DUMPCONFIG
	.p2align	4, 0x90
	.type	TAFFO_DUMPCONFIG,@function
TAFFO_DUMPCONFIG:                       # @TAFFO_DUMPCONFIG
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end5:
	.size	TAFFO_DUMPCONFIG, .Lfunc_end5-TAFFO_DUMPCONFIG
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI6_0:
	.quad	4647714815446351872     # double 512
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
	subq	$128, %rsp
	movl	%edi, -4(%rbp)          # 4-byte Spill
	movq	%rsi, -16(%rbp)         # 8-byte Spill
	callq	TAFFO_DUMPCONFIG
	callq	TIMING_CPUCLOCK_START
	xorl	%edi, %edi
	movl	%edi, -20(%rbp)         # 4-byte Spill
.LBB6_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_3 Depth 2
	movl	-20(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -24(%rbp)         # 4-byte Spill
	jge	.LBB6_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB6_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -28(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_3:                                # %for.cond6
                                        #   Parent Loop BB6_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-28(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jge	.LBB6_6
# %bb.4:                                # %for.body9
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-24(%rbp), %eax         # 4-byte Reload
	shll	$25, %eax
	movl	-32(%rbp), %ecx         # 4-byte Reload
	shll	$25, %ecx
	movl	%eax, %eax
	movl	%eax, %edx
	movl	%ecx, %eax
	movl	%eax, %esi
	imulq	%rsi, %rdx
	shrq	$32, %rdx
	movl	%edx, %eax
	movl	%eax, %eax
                                        # kill: def $rax killed $eax
	xorl	%ecx, %ecx
	movl	%ecx, %edx
	movl	$28, %esi
	divq	%rsi
	shlq	$5, %rax
	movl	%eax, %ecx
	movl	-24(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rax
	imulq	$112, %rax, %rax
	movabsq	$data.fixp, %rsi
	addq	%rax, %rsi
	movl	-32(%rbp), %r8d         # 4-byte Reload
	movslq	%r8d, %rax
	shrl	$14, %ecx
	movl	%ecx, (%rsi,%rax,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-32(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -28(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_6:                                # %for.end
                                        #   in Loop: Header=BB6_1 Depth=1
	jmp	.LBB6_7
.LBB6_7:                                # %for.inc14
                                        #   in Loop: Header=BB6_1 Depth=1
	movl	-24(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jmp	.LBB6_1
.LBB6_8:                                # %for.end16
	xorl	%eax, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_9
.LBB6_9:                                # %for.cond17
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_11 Depth 2
	movl	-36(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jge	.LBB6_16
# %bb.10:                               # %for.body20
                                        #   in Loop: Header=BB6_9 Depth=1
	xorl	%eax, %eax
	movl	-40(%rbp), %ecx         # 4-byte Reload
	movslq	%ecx, %rdx
	movl	$0, mean.fixp(,%rdx,4)
	movl	%eax, -44(%rbp)         # 4-byte Spill
.LBB6_11:                               # %for.cond23
                                        #   Parent Loop BB6_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-44(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -48(%rbp)         # 4-byte Spill
	jge	.LBB6_14
# %bb.12:                               # %for.body26
                                        #   in Loop: Header=BB6_11 Depth=2
	movl	-48(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$data.fixp, %rdx
	addq	%rcx, %rdx
	movl	-40(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%esi, %rcx
	movl	mean.fixp(,%rcx,4), %r8d
	sarl	$3, %edi
	addl	%edi, %r8d
	movl	%r8d, mean.fixp(,%rcx,4)
# %bb.13:                               # %for.inc33
                                        #   in Loop: Header=BB6_11 Depth=2
	movl	-48(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jmp	.LBB6_11
.LBB6_14:                               # %for.end35
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	-40(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movslq	mean.fixp(,%rcx,4), %rdx
	shlq	$26, %rdx
	movq	%rdx, %rax
	cqto
	movl	$2147483648, %esi       # imm = 0x80000000
	idivq	%rsi
	shlq	$7, %rax
	movl	%eax, %edi
	sarl	$7, %edi
	movl	%edi, mean.fixp(,%rcx,4)
# %bb.15:                               # %for.inc39
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	-40(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_9
.LBB6_16:                               # %for.end41
	xorl	%eax, %eax
	movl	%eax, -52(%rbp)         # 4-byte Spill
	jmp	.LBB6_17
.LBB6_17:                               # %for.cond42
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_19 Depth 2
	movl	-52(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -56(%rbp)         # 4-byte Spill
	jge	.LBB6_24
# %bb.18:                               # %for.body45
                                        #   in Loop: Header=BB6_17 Depth=1
	xorl	%eax, %eax
	movl	%eax, -60(%rbp)         # 4-byte Spill
	jmp	.LBB6_19
.LBB6_19:                               # %for.cond46
                                        #   Parent Loop BB6_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-60(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -64(%rbp)         # 4-byte Spill
	jge	.LBB6_22
# %bb.20:                               # %for.body49
                                        #   in Loop: Header=BB6_19 Depth=2
	movl	-64(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movl	mean.fixp(,%rcx,4), %edx
	movl	-56(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$data.fixp, %rdi
	addq	%rcx, %rdi
	movslq	%eax, %rcx
	movl	(%rdi,%rcx,4), %r8d
	sarl	$3, %r8d
	subl	%edx, %r8d
	shll	$3, %r8d
	movl	%r8d, (%rdi,%rcx,4)
# %bb.21:                               # %for.inc56
                                        #   in Loop: Header=BB6_19 Depth=2
	movl	-64(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -60(%rbp)         # 4-byte Spill
	jmp	.LBB6_19
.LBB6_22:                               # %for.end58
                                        #   in Loop: Header=BB6_17 Depth=1
	jmp	.LBB6_23
.LBB6_23:                               # %for.inc59
                                        #   in Loop: Header=BB6_17 Depth=1
	movl	-56(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -52(%rbp)         # 4-byte Spill
	jmp	.LBB6_17
.LBB6_24:                               # %for.end61
	xorl	%eax, %eax
	movl	%eax, -68(%rbp)         # 4-byte Spill
	jmp	.LBB6_25
.LBB6_25:                               # %for.cond62
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_27 Depth 2
                                        #       Child Loop BB6_29 Depth 3
	movl	-68(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -72(%rbp)         # 4-byte Spill
	jge	.LBB6_36
# %bb.26:                               # %for.body65
                                        #   in Loop: Header=BB6_25 Depth=1
	movl	-72(%rbp), %eax         # 4-byte Reload
	movl	%eax, -76(%rbp)         # 4-byte Spill
	jmp	.LBB6_27
.LBB6_27:                               # %for.cond66
                                        #   Parent Loop BB6_25 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_29 Depth 3
	movl	-76(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -80(%rbp)         # 4-byte Spill
	jge	.LBB6_34
# %bb.28:                               # %for.body69
                                        #   in Loop: Header=BB6_27 Depth=2
	xorl	%eax, %eax
	movl	-72(%rbp), %ecx         # 4-byte Reload
	movslq	%ecx, %rdx
	imulq	$112, %rdx, %rdx
	movabsq	$cov.fixp, %rsi
	addq	%rdx, %rsi
	movl	-80(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rdx
	movl	$0, (%rsi,%rdx,4)
	movl	%eax, -84(%rbp)         # 4-byte Spill
.LBB6_29:                               # %for.cond74
                                        #   Parent Loop BB6_25 Depth=1
                                        #     Parent Loop BB6_27 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-84(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -88(%rbp)         # 4-byte Spill
	jge	.LBB6_32
# %bb.30:                               # %for.body77
                                        #   in Loop: Header=BB6_29 Depth=3
	movl	-88(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$data.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-72(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-80(%rbp), %r9d         # 4-byte Reload
	movslq	%r9d, %rcx
	movl	(%rdx,%rcx,4), %r10d
	movslq	%r8d, %rcx
	movslq	%r10d, %rdx
	imulq	%rdx, %rcx
	shlq	$2, %rcx
	movslq	%edi, %rdx
	imulq	$112, %rdx, %rdx
	movabsq	$cov.fixp, %rsi
	addq	%rdx, %rsi
	movslq	%r9d, %rdx
	movslq	(%rsi,%rdx,4), %r11
	shlq	$11, %r11
	addq	%rcx, %r11
	sarq	$11, %r11
	movl	%r11d, %r8d
	movl	%r8d, (%rsi,%rdx,4)
# %bb.31:                               # %for.inc92
                                        #   in Loop: Header=BB6_29 Depth=3
	movl	-88(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -84(%rbp)         # 4-byte Spill
	jmp	.LBB6_29
.LBB6_32:                               # %for.end94
                                        #   in Loop: Header=BB6_27 Depth=2
	movl	-72(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$cov.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-80(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movslq	(%rsi,%rcx,4), %r8
	movq	%r8, %rax
	movq	%rdx, -96(%rbp)         # 8-byte Spill
	cqto
	movl	$31, %r8d
	idivq	%r8
	shlq	$5, %rax
	movl	%eax, %r9d
	sarl	$5, %r9d
	movl	%r9d, (%rsi,%rcx,4)
	movl	-72(%rbp), %r9d         # 4-byte Reload
	movslq	%r9d, %rax
	imulq	$112, %rax, %rax
	movq	-96(%rbp), %rcx         # 8-byte Reload
	addq	%rax, %rcx
	movslq	%edi, %rax
	movl	(%rcx,%rax,4), %r10d
	movslq	%edi, %rax
	imulq	$112, %rax, %rax
	movq	-96(%rbp), %rcx         # 8-byte Reload
	addq	%rax, %rcx
	movslq	%r9d, %rax
	movl	%r10d, (%rcx,%rax,4)
# %bb.33:                               # %for.inc108
                                        #   in Loop: Header=BB6_27 Depth=2
	movl	-80(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -76(%rbp)         # 4-byte Spill
	jmp	.LBB6_27
.LBB6_34:                               # %for.end110
                                        #   in Loop: Header=BB6_25 Depth=1
	jmp	.LBB6_35
.LBB6_35:                               # %for.inc111
                                        #   in Loop: Header=BB6_25 Depth=1
	movl	-72(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -68(%rbp)         # 4-byte Spill
	jmp	.LBB6_25
.LBB6_36:                               # %for.end113
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	movl	%eax, -100(%rbp)        # 4-byte Spill
.LBB6_37:                               # %for.cond114
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_39 Depth 2
	movl	-100(%rbp), %eax        # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -104(%rbp)        # 4-byte Spill
	jge	.LBB6_46
# %bb.38:                               # %for.body117
                                        #   in Loop: Header=BB6_37 Depth=1
	xorl	%eax, %eax
	movl	%eax, -108(%rbp)        # 4-byte Spill
	jmp	.LBB6_39
.LBB6_39:                               # %for.cond118
                                        #   Parent Loop BB6_37 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-108(%rbp), %eax        # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -112(%rbp)        # 4-byte Spill
	jge	.LBB6_44
# %bb.40:                               # %for.body121
                                        #   in Loop: Header=BB6_39 Depth=2
	movl	-104(%rbp), %eax        # 4-byte Reload
	imull	$28, %eax, %ecx
	movl	-112(%rbp), %edx        # 4-byte Reload
	addl	%edx, %ecx
	movl	%ecx, %eax
	cltd
	movl	$20, %ecx
	idivl	%ecx
	cmpl	$0, %edx
	jne	.LBB6_42
# %bb.41:                               # %if.then
                                        #   in Loop: Header=BB6_39 Depth=2
	movq	stdout, %rdi
	movabsq	$.L.str.4, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -116(%rbp)        # 4-byte Spill
.LBB6_42:                               # %if.end
                                        #   in Loop: Header=BB6_39 Depth=2
	movsd	.LCPI6_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-104(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$cov.fixp, %rdx
	addq	%rcx, %rdx
	movl	-112(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	cvtsi2sdl	%r8d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.5, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -120(%rbp)        # 4-byte Spill
# %bb.43:                               # %for.inc131
                                        #   in Loop: Header=BB6_39 Depth=2
	movl	-112(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -108(%rbp)        # 4-byte Spill
	jmp	.LBB6_39
.LBB6_44:                               # %for.end133
                                        #   in Loop: Header=BB6_37 Depth=1
	jmp	.LBB6_45
.LBB6_45:                               # %for.inc134
                                        #   in Loop: Header=BB6_37 Depth=1
	movl	-104(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -100(%rbp)        # 4-byte Spill
	jmp	.LBB6_37
.LBB6_46:                               # %for.end136
	xorl	%eax, %eax
	addq	$128, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end6:
	.size	main, .Lfunc_end6-main
	.cfi_endproc
                                        # -- End function
	.type	time_that_takes,@object # @time_that_takes
	.comm	time_that_takes,8,8
	.type	.L.str,@object          # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"%ld"
	.size	.L.str, 4

	.type	data,@object            # @data
	.comm	data,7168,16
	.type	mean,@object            # @mean
	.comm	mean,224,16
	.type	cov,@object             # @cov
	.comm	cov,7168,16
	.type	.L.str.4,@object        # @.str.4
.L.str.4:
	.asciz	"\n"
	.size	.L.str.4, 2

	.type	.L.str.5,@object        # @.str.5
.L.str.5:
	.asciz	"%.16lf "
	.size	.L.str.5, 8

	.type	data.fixp,@object       # @data.fixp
	.comm	data.fixp,3584,16
	.type	mean.fixp,@object       # @mean.fixp
	.comm	mean.fixp,112,16
	.type	cov.fixp,@object        # @cov.fixp
	.comm	cov.fixp,3584,16

	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym gettime
	.addrsig_sym clock
	.addrsig_sym TIMING_CPUCLOCK_START
	.addrsig_sym TIMING_CPUCLOCK_TOGGLE
	.addrsig_sym TIMING_CPUCLOCK_PRINT
	.addrsig_sym fprintf
	.addrsig_sym TAFFO_DUMPCONFIG
	.addrsig_sym time_that_takes
	.addrsig_sym stderr
	.addrsig_sym data
	.addrsig_sym mean
	.addrsig_sym cov
	.addrsig_sym stdout
	.addrsig_sym data.fixp
	.addrsig_sym mean.fixp
	.addrsig_sym cov.fixp
