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
	subq	$32, %rsp
	movl	$2, %edi
	leaq	-16(%rbp), %rsi
	callq	clock_gettime
	imulq	$1000000, -16(%rbp), %rsi # imm = 0xF4240
	movq	-8(%rbp), %rcx
	movl	%eax, -20(%rbp)         # 4-byte Spill
	movq	%rcx, %rax
	cqto
	movl	$1000, %ecx             # imm = 0x3E8
	idivq	%rcx
	addq	%rax, %rsi
	movq	%rsi, %rax
	addq	$32, %rsp
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
	.quad	4607182418800017408     # double 1
.LCPI6_1:
	.quad	4737786807993761792     # double 536870912
.LCPI6_2:
	.quad	4629700416936869888     # double 32
.LCPI6_3:
	.quad	4688247212092686336     # double 262144
.LCPI6_4:
	.quad	4719772409484279808     # double 33554432
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
	callq	TAFFO_DUMPCONFIG
	callq	TIMING_CPUCLOCK_START
	xorl	%eax, %eax
	movl	%eax, -4(%rbp)          # 4-byte Spill
.LBB6_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_3 Depth 2
	movl	-4(%rbp), %eax          # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8(%rbp)          # 4-byte Spill
	jge	.LBB6_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB6_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -12(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_3:                                # %for.cond5
                                        #   Parent Loop BB6_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-12(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jge	.LBB6_6
# %bb.4:                                # %for.body7
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-8(%rbp), %eax          # 4-byte Reload
	movl	-16(%rbp), %ecx         # 4-byte Reload
	imull	%ecx, %eax
	shll	$24, %eax
	movl	%eax, %eax
                                        # kill: def $rax killed $eax
	xorl	%edx, %edx
                                        # kill: def $rdx killed $edx
	movl	$28, %esi
	divq	%rsi
	shlq	$4, %rax
	movl	%eax, %edi
	movl	-8(%rbp), %r8d          # 4-byte Reload
	shll	$24, %r8d
	shrl	$4, %edi
	addl	%r8d, %edi
	movl	%edi, %edi
	movl	%edi, %eax
	shrq	$5, %rax
	shlq	$4, %rax
	movl	%eax, %edi
	movl	-8(%rbp), %r8d          # 4-byte Reload
	movslq	%r8d, %rax
	imulq	$112, %rax, %rax
	movabsq	$data.fixp, %rsi
	addq	%rax, %rsi
	movslq	%ecx, %rax
	shrl	$1, %edi
	movl	%edi, (%rsi,%rax,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-16(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -12(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_6:                                # %for.end
                                        #   in Loop: Header=BB6_1 Depth=1
	jmp	.LBB6_7
.LBB6_7:                                # %for.inc12
                                        #   in Loop: Header=BB6_1 Depth=1
	movl	-8(%rbp), %eax          # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -4(%rbp)          # 4-byte Spill
	jmp	.LBB6_1
.LBB6_8:                                # %for.end14
	xorl	%eax, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jmp	.LBB6_9
.LBB6_9:                                # %for.cond16
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_11 Depth 2
	movl	-20(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -24(%rbp)         # 4-byte Spill
	jge	.LBB6_16
# %bb.10:                               # %for.body19
                                        #   in Loop: Header=BB6_9 Depth=1
	xorl	%eax, %eax
	movl	-24(%rbp), %ecx         # 4-byte Reload
	movslq	%ecx, %rdx
	movl	$0, mean.fixp(,%rdx,4)
	movl	%eax, -28(%rbp)         # 4-byte Spill
.LBB6_11:                               # %for.cond22
                                        #   Parent Loop BB6_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-28(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jge	.LBB6_14
# %bb.12:                               # %for.body25
                                        #   in Loop: Header=BB6_11 Depth=2
	movl	-32(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$data.fixp, %rdx
	addq	%rcx, %rdx
	movl	-24(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%esi, %rcx
	movl	mean.fixp(,%rcx,4), %r8d
	sarl	$12, %edi
	addl	%edi, %r8d
	movl	%r8d, mean.fixp(,%rcx,4)
# %bb.13:                               # %for.inc33
                                        #   in Loop: Header=BB6_11 Depth=2
	movl	-32(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -28(%rbp)         # 4-byte Spill
	jmp	.LBB6_11
.LBB6_14:                               # %for.end35
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	-24(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movslq	mean.fixp(,%rcx,4), %rdx
	movq	%rdx, %rax
	cqto
	movl	$32, %esi
	idivq	%rsi
	shlq	$5, %rax
	movl	%eax, %edi
	sarl	$5, %edi
	movl	%edi, mean.fixp(,%rcx,4)
# %bb.15:                               # %for.inc39
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	-24(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jmp	.LBB6_9
.LBB6_16:                               # %for.end41
	xorl	%eax, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_17
.LBB6_17:                               # %for.cond42
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_19 Depth 2
	movl	-36(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jge	.LBB6_27
# %bb.18:                               # %for.body45
                                        #   in Loop: Header=BB6_17 Depth=1
	xorl	%eax, %eax
	movl	-40(%rbp), %ecx         # 4-byte Reload
	movslq	%ecx, %rdx
	movl	$0, stddev.fixp(,%rdx,4)
	movl	%eax, -44(%rbp)         # 4-byte Spill
.LBB6_19:                               # %for.cond48
                                        #   Parent Loop BB6_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-44(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -48(%rbp)         # 4-byte Spill
	jge	.LBB6_22
# %bb.20:                               # %for.body51
                                        #   in Loop: Header=BB6_19 Depth=2
	movl	-48(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$data.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-40(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%edi, %rcx
	movl	mean.fixp(,%rcx,4), %r9d
	sarl	$12, %r8d
	subl	%r9d, %r8d
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r9d
	movslq	%edi, %rcx
	movl	mean.fixp(,%rcx,4), %r10d
	sarl	$12, %r9d
	subl	%r10d, %r9d
	movslq	%r8d, %rcx
	movslq	%r9d, %rdx
	imulq	%rdx, %rcx
	shlq	$1, %rcx
	movslq	%edi, %rdx
	movslq	stddev.fixp(,%rdx,4), %rsi
	shlq	$13, %rsi
	addq	%rcx, %rsi
	sarq	$13, %rsi
	movl	%esi, %r8d
	movl	%r8d, stddev.fixp(,%rdx,4)
# %bb.21:                               # %for.inc69
                                        #   in Loop: Header=BB6_19 Depth=2
	movl	-48(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jmp	.LBB6_19
.LBB6_22:                               # %for.end71
                                        #   in Loop: Header=BB6_17 Depth=1
	movl	-40(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movslq	stddev.fixp(,%rcx,4), %rdx
	movl	%edx, %esi
	sarq	$63, %rdx
	shrq	$59, %rdx
	movl	%edx, %edi
	addl	%edi, %esi
	sarl	$5, %esi
	movl	%esi, stddev.fixp(,%rcx,4)
	cvtsi2sdl	stddev.fixp(,%rcx,4), %xmm0
	movsd	.LCPI6_3(%rip), %xmm1   # xmm1 = mem[0],zero
	divsd	%xmm1, %xmm0
	callq	sqrt
	movsd	.LCPI6_4(%rip), %xmm1   # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movl	%ecx, %eax
	movl	-40(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rcx
	shrl	$7, %eax
	movl	%eax, stddev.fixp(,%rcx,4)
	movslq	%esi, %rcx
	cmpl	$26214, stddev.fixp(,%rcx,4) # imm = 0x6666
	jg	.LBB6_24
# %bb.23:                               # %cond.true
                                        #   in Loop: Header=BB6_17 Depth=1
	movl	$262144, %eax           # imm = 0x40000
	movl	%eax, -52(%rbp)         # 4-byte Spill
	jmp	.LBB6_25
.LBB6_24:                               # %cond.false
                                        #   in Loop: Header=BB6_17 Depth=1
	movl	-40(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movl	stddev.fixp(,%rcx,4), %edx
	movl	%edx, -52(%rbp)         # 4-byte Spill
.LBB6_25:                               # %cond.end
                                        #   in Loop: Header=BB6_17 Depth=1
	movl	-52(%rbp), %eax         # 4-byte Reload
	movl	-40(%rbp), %ecx         # 4-byte Reload
	movslq	%ecx, %rdx
	movl	%eax, stddev.fixp(,%rdx,4)
# %bb.26:                               # %for.inc87
                                        #   in Loop: Header=BB6_17 Depth=1
	movl	-40(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_17
.LBB6_27:                               # %for.end89
	xorl	%eax, %eax
	movl	%eax, -56(%rbp)         # 4-byte Spill
	jmp	.LBB6_28
.LBB6_28:                               # %for.cond90
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_30 Depth 2
	movl	-56(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -60(%rbp)         # 4-byte Spill
	jge	.LBB6_35
# %bb.29:                               # %for.body93
                                        #   in Loop: Header=BB6_28 Depth=1
	xorl	%eax, %eax
	movl	%eax, -64(%rbp)         # 4-byte Spill
	jmp	.LBB6_30
.LBB6_30:                               # %for.cond94
                                        #   Parent Loop BB6_28 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-64(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -68(%rbp)         # 4-byte Spill
	jge	.LBB6_33
# %bb.31:                               # %for.body97
                                        #   in Loop: Header=BB6_30 Depth=2
	movl	-68(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movl	mean.fixp(,%rcx,4), %edx
	movl	-60(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rdi
	imulq	$112, %rdi, %rdi
	movl	data.fixp(%rdi,%rcx,4), %r8d
	shrl	$12, %r8d
	subl	%edx, %r8d
	shll	$12, %r8d
	movl	%r8d, data.fixp(%rdi,%rcx,4)
	movsd	.LCPI6_2(%rip), %xmm0   # xmm0 = mem[0],zero
	callq	sqrt
	movsd	.LCPI6_1(%rip), %xmm1   # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movl	%ecx, %eax
	movl	-68(%rbp), %edx         # 4-byte Reload
	movslq	%edx, %rcx
	movl	stddev.fixp(,%rcx,4), %esi
	movl	%eax, %eax
	movl	%eax, %ecx
	movslq	%esi, %rdi
	imulq	%rdi, %rcx
	sarq	$31, %rcx
	movl	%ecx, %eax
	movl	-60(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$data.fixp, %rdi
	addq	%rcx, %rdi
	movslq	%edx, %rcx
	movslq	(%rdi,%rcx,4), %r9
	shlq	$16, %r9
	movslq	%eax, %r10
	movq	%r9, %rax
	cqto
	idivq	%r10
	shlq	$3, %rax
	movl	%eax, %r8d
	sarl	$3, %r8d
	movl	%r8d, (%rdi,%rcx,4)
# %bb.32:                               # %for.inc114
                                        #   in Loop: Header=BB6_30 Depth=2
	movl	-68(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64(%rbp)         # 4-byte Spill
	jmp	.LBB6_30
.LBB6_33:                               # %for.end116
                                        #   in Loop: Header=BB6_28 Depth=1
	jmp	.LBB6_34
.LBB6_34:                               # %for.inc117
                                        #   in Loop: Header=BB6_28 Depth=1
	movl	-60(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -56(%rbp)         # 4-byte Spill
	jmp	.LBB6_28
.LBB6_35:                               # %for.end119
	xorl	%eax, %eax
	movl	%eax, -72(%rbp)         # 4-byte Spill
	jmp	.LBB6_36
.LBB6_36:                               # %for.cond120
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_38 Depth 2
                                        #       Child Loop BB6_40 Depth 3
	movl	-72(%rbp), %eax         # 4-byte Reload
	cmpl	$27, %eax
	movl	%eax, -76(%rbp)         # 4-byte Spill
	jge	.LBB6_47
# %bb.37:                               # %for.body123
                                        #   in Loop: Header=BB6_36 Depth=1
	movl	-76(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$corr.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movl	$536870912, (%rdx,%rcx,4) # imm = 0x20000000
	addl	$1, %eax
	movl	%eax, -80(%rbp)         # 4-byte Spill
.LBB6_38:                               # %for.cond129
                                        #   Parent Loop BB6_36 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_40 Depth 3
	movl	-80(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -84(%rbp)         # 4-byte Spill
	jge	.LBB6_45
# %bb.39:                               # %for.body132
                                        #   in Loop: Header=BB6_38 Depth=2
	xorl	%eax, %eax
	movl	-76(%rbp), %ecx         # 4-byte Reload
	movslq	%ecx, %rdx
	imulq	$112, %rdx, %rdx
	movabsq	$corr.fixp, %rsi
	addq	%rdx, %rsi
	movl	-84(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rdx
	movl	$0, (%rsi,%rdx,4)
	movl	%eax, -88(%rbp)         # 4-byte Spill
.LBB6_40:                               # %for.cond137
                                        #   Parent Loop BB6_36 Depth=1
                                        #     Parent Loop BB6_38 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-88(%rbp), %eax         # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -92(%rbp)         # 4-byte Spill
	jge	.LBB6_43
# %bb.41:                               # %for.body140
                                        #   in Loop: Header=BB6_40 Depth=3
	movl	-92(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$data.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-76(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-84(%rbp), %r9d         # 4-byte Reload
	movslq	%r9d, %rcx
	movl	(%rdx,%rcx,4), %r10d
	movslq	%r8d, %rcx
	movslq	%r10d, %rdx
	imulq	%rdx, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r8d
	movslq	%edi, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$corr.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%r9d, %rcx
	movl	(%rdx,%rcx,4), %r10d
	shrl	$5, %r10d
	addl	%r8d, %r10d
	shll	$5, %r10d
	movl	%r10d, (%rdx,%rcx,4)
# %bb.42:                               # %for.inc155
                                        #   in Loop: Header=BB6_40 Depth=3
	movl	-92(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -88(%rbp)         # 4-byte Spill
	jmp	.LBB6_40
.LBB6_43:                               # %for.end157
                                        #   in Loop: Header=BB6_38 Depth=2
	movl	-76(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movabsq	$corr.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-84(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%edi, %rcx
	imulq	$112, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movl	%r8d, (%rdx,%rcx,4)
# %bb.44:                               # %for.inc166
                                        #   in Loop: Header=BB6_38 Depth=2
	movl	-84(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -80(%rbp)         # 4-byte Spill
	jmp	.LBB6_38
.LBB6_45:                               # %for.end168
                                        #   in Loop: Header=BB6_36 Depth=1
	jmp	.LBB6_46
.LBB6_46:                               # %for.inc169
                                        #   in Loop: Header=BB6_36 Depth=1
	movl	-76(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -72(%rbp)         # 4-byte Spill
	jmp	.LBB6_36
.LBB6_47:                               # %for.end171
	movsd	.LCPI6_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	%xmm0, corr+6264
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	movl	%eax, -96(%rbp)         # 4-byte Spill
.LBB6_48:                               # %for.cond172
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_50 Depth 2
	movl	-96(%rbp), %eax         # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -100(%rbp)        # 4-byte Spill
	jge	.LBB6_55
# %bb.49:                               # %for.body175
                                        #   in Loop: Header=BB6_48 Depth=1
	xorl	%eax, %eax
	movl	%eax, -104(%rbp)        # 4-byte Spill
	jmp	.LBB6_50
.LBB6_50:                               # %for.cond176
                                        #   Parent Loop BB6_48 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-104(%rbp), %eax        # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -108(%rbp)        # 4-byte Spill
	jge	.LBB6_53
# %bb.51:                               # %for.body179
                                        #   in Loop: Header=BB6_50 Depth=2
	movsd	.LCPI6_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-100(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$112, %rcx, %rcx
	movl	-108(%rbp), %edx        # 4-byte Reload
	movslq	%edx, %rsi
	movl	corr.fixp(%rcx,%rsi,4), %edi
	movl	%edi, %ecx
	cvtsi2sdq	%rcx, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.6, %rdi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	printf
	movl	%eax, -112(%rbp)        # 4-byte Spill
# %bb.52:                               # %for.inc185
                                        #   in Loop: Header=BB6_50 Depth=2
	movl	-108(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -104(%rbp)        # 4-byte Spill
	jmp	.LBB6_50
.LBB6_53:                               # %for.end187
                                        #   in Loop: Header=BB6_48 Depth=1
	movabsq	$.L.str.7, %rdi
	movb	$0, %al
	callq	printf
	movl	%eax, -116(%rbp)        # 4-byte Spill
# %bb.54:                               # %for.inc189
                                        #   in Loop: Header=BB6_48 Depth=1
	movl	-100(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96(%rbp)         # 4-byte Spill
	jmp	.LBB6_48
.LBB6_55:                               # %for.end191
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
	.type	stddev,@object          # @stddev
	.comm	stddev,224,16
	.type	corr,@object            # @corr
	.comm	corr,6272,16
	.type	.L.str.6,@object        # @.str.6
.L.str.6:
	.asciz	"%.16lf "
	.size	.L.str.6, 8

	.type	.L.str.7,@object        # @.str.7
.L.str.7:
	.asciz	"\n"
	.size	.L.str.7, 2

	.type	data.fixp,@object       # @data.fixp
	.comm	data.fixp,3584,16
	.type	mean.fixp,@object       # @mean.fixp
	.comm	mean.fixp,112,16
	.type	stddev.fixp,@object     # @stddev.fixp
	.comm	stddev.fixp,112,16
	.type	corr.fixp,@object       # @corr.fixp
	.comm	corr.fixp,3136,16

	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym gettime
	.addrsig_sym clock_gettime
	.addrsig_sym TIMING_CPUCLOCK_START
	.addrsig_sym TIMING_CPUCLOCK_TOGGLE
	.addrsig_sym TIMING_CPUCLOCK_PRINT
	.addrsig_sym fprintf
	.addrsig_sym TAFFO_DUMPCONFIG
	.addrsig_sym sqrt
	.addrsig_sym printf
	.addrsig_sym time_that_takes
	.addrsig_sym stderr
	.addrsig_sym data
	.addrsig_sym mean
	.addrsig_sym stddev
	.addrsig_sym corr
	.addrsig_sym data.fixp
	.addrsig_sym mean.fixp
	.addrsig_sym stddev.fixp
	.addrsig_sym corr.fixp
