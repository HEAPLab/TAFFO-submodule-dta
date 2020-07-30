	.text
	.file	"adi.c"
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
	.quad	4733283208366391296     # double 268435456
.LCPI6_1:
	.quad	4737786807993761792     # double 536870912
.LCPI6_2:
	.quad	4607182418800017408     # double 1
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
	pushq	%rbx
	subq	$152, %rsp
	.cfi_offset %rbx, -24
	movl	%edi, -12(%rbp)         # 4-byte Spill
	movq	%rsi, -24(%rbp)         # 8-byte Spill
	callq	TAFFO_DUMPCONFIG
	callq	TIMING_CPUCLOCK_START
	xorl	%edi, %edi
	movl	%edi, -28(%rbp)         # 4-byte Spill
.LBB6_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_3 Depth 2
	movl	-28(%rbp), %eax         # 4-byte Reload
	cmpl	$20, %eax
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jge	.LBB6_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB6_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_3:                                # %for.cond3
                                        #   Parent Loop BB6_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-36(%rbp), %eax         # 4-byte Reload
	cmpl	$20, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jge	.LBB6_6
# %bb.4:                                # %for.body5
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-32(%rbp), %eax         # 4-byte Reload
	addl	$20, %eax
	movl	-40(%rbp), %ecx         # 4-byte Reload
	subl	%ecx, %eax
	shll	$23, %eax
	movl	%eax, %eax
	movl	%eax, %edx
	shlq	$27, %rdx
	movq	%rdx, %rax
	xorl	%esi, %esi
	movl	%esi, %edx
	movl	$2684354560, %edi       # imm = 0xA0000000
	divq	%rdi
	shlq	$4, %rax
	movl	%eax, %esi
	movl	-32(%rbp), %r8d         # 4-byte Reload
	movslq	%r8d, %rax
	imulq	$80, %rax, %rax
	movabsq	$u.fixp, %rdi
	addq	%rax, %rdi
	movslq	%ecx, %rax
	shll	$1, %esi
	movl	%esi, (%rdi,%rax,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-40(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_6:                                # %for.end
                                        #   in Loop: Header=BB6_1 Depth=1
	jmp	.LBB6_7
.LBB6_7:                                # %for.inc9
                                        #   in Loop: Header=BB6_1 Depth=1
	movl	-32(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -28(%rbp)         # 4-byte Spill
	jmp	.LBB6_1
.LBB6_8:                                # %for.end11
	xorl	%eax, %eax
	movl	$107374182, DX.fixp     # imm = 0x6666666
	movl	$107374182, DY.fixp     # imm = 0x6666666
	movl	$107374182, DT.fixp     # imm = 0x6666666
	movl	$-2147483648, B1.fixp   # imm = 0x80000000
	movl	$-2147483648, B2.fixp   # imm = 0x80000000
	movl	B1.fixp, %ecx
	movl	DT.fixp, %edx
	movl	%ecx, %ecx
	movl	%ecx, %esi
	movl	%edx, %ecx
	movl	%ecx, %edi
	imulq	%rdi, %rsi
	shrq	$31, %rsi
	movl	%esi, %ecx
	movl	DX.fixp, %edx
	movl	DX.fixp, %r8d
	movl	%edx, %edx
	movl	%edx, %esi
	movl	%r8d, %edx
	movl	%edx, %edi
	imulq	%rdi, %rsi
	shrq	$31, %rsi
	movl	%esi, %edx
	movl	%ecx, %ecx
	movl	%ecx, %esi
	shlq	$31, %rsi
	movl	%edx, %ecx
	movl	%ecx, %edi
	movl	%eax, -44(%rbp)         # 4-byte Spill
	movq	%rsi, %rax
	xorl	%ecx, %ecx
	movl	%ecx, %edx
	divq	%rdi
	shrq	$4, %rax
	movl	%eax, %ecx
	movl	%ecx, mul1.fixp
	movl	B2.fixp, %ecx
	movl	DT.fixp, %r8d
	movl	%ecx, %ecx
	movl	%ecx, %eax
	movl	%r8d, %ecx
	movl	%ecx, %esi
	imulq	%rsi, %rax
	shrq	$31, %rax
	movl	%eax, %ecx
	movl	DY.fixp, %r8d
	movl	DY.fixp, %r9d
	movl	%r8d, %r8d
	movl	%r8d, %eax
	movl	%r9d, %r8d
	movl	%r8d, %esi
	imulq	%rsi, %rax
	shrq	$31, %rax
	movl	%eax, %r8d
	movl	%ecx, %ecx
	movl	%ecx, %eax
	shlq	$31, %rax
	movl	%r8d, %ecx
	movl	%ecx, %esi
	xorl	%ecx, %ecx
	movl	%ecx, %edx
	divq	%rsi
	shrq	$4, %rax
	movl	%eax, %ecx
	movl	%ecx, mul2.fixp
	movl	mul1.fixp, %ecx
	shrl	$1, %ecx
	movl	-44(%rbp), %r8d         # 4-byte Reload
	subl	%ecx, %r8d
	movslq	%r8d, %rax
	cqto
	movl	$2, %esi
	idivq	%rsi
	movl	%eax, %ecx
	shll	$1, %ecx
	movl	%ecx, a.fixp
	movl	mul1.fixp, %ecx
	addl	$67108864, %ecx         # imm = 0x4000000
	movl	%ecx, b.fixp
	movl	a.fixp, %ecx
	movl	%ecx, c.fixp
	movl	mul2.fixp, %ecx
	shrl	$1, %ecx
	movl	-44(%rbp), %r8d         # 4-byte Reload
	subl	%ecx, %r8d
	movslq	%r8d, %rax
	cqto
	idivq	%rsi
	movl	%eax, %ecx
	shll	$1, %ecx
	movl	%ecx, d.fixp
	movl	mul2.fixp, %ecx
	addl	$134217728, %ecx        # imm = 0x8000000
	movl	%ecx, e.fixp
	movl	d.fixp, %ecx
	movl	%ecx, f.fixp
	movl	$1, %ecx
	movl	%ecx, -48(%rbp)         # 4-byte Spill
.LBB6_9:                                # %for.cond23
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_11 Depth 2
                                        #       Child Loop BB6_13 Depth 3
                                        #       Child Loop BB6_17 Depth 3
                                        #     Child Loop BB6_23 Depth 2
                                        #       Child Loop BB6_25 Depth 3
                                        #       Child Loop BB6_29 Depth 3
	movl	-48(%rbp), %eax         # 4-byte Reload
	cmpl	$20, %eax
	movl	%eax, -52(%rbp)         # 4-byte Spill
	jg	.LBB6_36
# %bb.10:                               # %for.body26
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	$1, %eax
	movl	%eax, -56(%rbp)         # 4-byte Spill
	jmp	.LBB6_11
.LBB6_11:                               # %for.cond27
                                        #   Parent Loop BB6_9 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_13 Depth 3
                                        #       Child Loop BB6_17 Depth 3
	movl	-56(%rbp), %eax         # 4-byte Reload
	cmpl	$19, %eax
	movl	%eax, -60(%rbp)         # 4-byte Spill
	jge	.LBB6_22
# %bb.12:                               # %for.body30
                                        #   in Loop: Header=BB6_11 Depth=2
	movsd	.LCPI6_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI6_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-60(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movsd	%xmm1, v(,%rcx,8)
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$p.fixp, %rdx
	addq	%rcx, %rdx
	movl	$0, (%rdx)
	movslq	%eax, %rcx
	mulsd	v(,%rcx,8), %xmm0
	cvttsd2si	%xmm0, %esi
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$q.fixp, %rdx
	addq	%rcx, %rdx
	sarl	$7, %esi
	movl	%esi, (%rdx)
	movl	$1, %esi
	movl	%esi, -64(%rbp)         # 4-byte Spill
.LBB6_13:                               # %for.cond41
                                        #   Parent Loop BB6_9 Depth=1
                                        #     Parent Loop BB6_11 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-64(%rbp), %eax         # 4-byte Reload
	cmpl	$19, %eax
	movl	%eax, -68(%rbp)         # 4-byte Spill
	jge	.LBB6_16
# %bb.14:                               # %for.body44
                                        #   in Loop: Header=BB6_13 Depth=3
	xorl	%eax, %eax
	movl	%eax, %ecx
	subl	c.fixp, %ecx
	movl	a.fixp, %edx
	movl	-60(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rdi
	imulq	$80, %rdi, %rdi
	movabsq	$p.fixp, %r8
	movq	%r8, %r9
	addq	%rdi, %r9
	movl	-68(%rbp), %r10d        # 4-byte Reload
	subl	$1, %r10d
	movslq	%r10d, %rdi
	movl	(%r9,%rdi,4), %r10d
	movslq	%edx, %rdi
	movslq	%r10d, %r9
	imulq	%r9, %rdi
	sarq	$31, %rdi
	movl	%edi, %edx
	movl	b.fixp, %r10d
	shrl	$1, %r10d
	addl	%r10d, %edx
	movslq	%ecx, %rdi
	shlq	$25, %rdi
	movslq	%edx, %r9
	movl	%eax, -72(%rbp)         # 4-byte Spill
	movq	%rdi, %rax
	cqto
	idivq	%r9
	shlq	$4, %rax
	movl	%eax, %ecx
	movslq	%esi, %rax
	imulq	$80, %rax, %rax
	movq	%r8, %rdi
	addq	%rax, %rdi
	movl	-68(%rbp), %r10d        # 4-byte Reload
	movslq	%r10d, %rax
	movl	%ecx, (%rdi,%rax,4)
	movl	-72(%rbp), %ecx         # 4-byte Reload
	subl	d.fixp, %ecx
	movslq	%r10d, %rax
	imulq	$80, %rax, %rax
	movabsq	$u.fixp, %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	subl	$1, %esi
	movslq	%esi, %rax
	movl	(%r9,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r9
	imulq	%r9, %rax
	sarq	$31, %rax
	movl	%eax, %ecx
	movslq	d.fixp, %rax
	shlq	$1, %rax
	sarq	$1, %rax
	movl	%eax, %esi
	sarl	$2, %esi
	addl	$16777216, %esi         # imm = 0x1000000
	movslq	%r10d, %rax
	imulq	$80, %rax, %rax
	movq	%rdi, %r9
	addq	%rax, %r9
	movl	-60(%rbp), %r11d        # 4-byte Reload
	movslq	%r11d, %rax
	movl	(%r9,%rax,4), %ebx
	movslq	%esi, %rax
	movslq	%ebx, %r9
	imulq	%r9, %rax
	sarq	$28, %rax
	movl	%eax, %esi
	sarl	$1, %ecx
	sarl	$1, %esi
	addl	%esi, %ecx
	movl	f.fixp, %esi
	movslq	%r10d, %rax
	imulq	$80, %rax, %rax
	addq	%rax, %rdi
	addl	$1, %r11d
	movslq	%r11d, %rax
	movl	(%rdi,%rax,4), %r11d
	movslq	%esi, %rax
	movslq	%r11d, %rdi
	imulq	%rdi, %rax
	sarq	$32, %rax
	movl	%eax, %esi
	subl	%esi, %ecx
	movl	a.fixp, %esi
	movl	-60(%rbp), %r11d        # 4-byte Reload
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	movabsq	$q.fixp, %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	subl	$1, %r10d
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %r10d
	movslq	%esi, %rax
	movslq	%r10d, %r9
	imulq	%r9, %rax
	sarq	$31, %rax
	movl	%eax, %esi
	sarl	$6, %ecx
	subl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	movq	%rdi, %r9
	addq	%rax, %r9
	movl	-68(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rax
	shll	$5, %ecx
	movl	%ecx, (%r9,%rax,4)
	movl	a.fixp, %ecx
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	addq	%rax, %r8
	subl	$1, %esi
	movslq	%esi, %rax
	movl	(%r8,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r8
	imulq	%r8, %rax
	sarq	$31, %rax
	movl	%eax, %ecx
	movl	b.fixp, %esi
	shrl	$1, %esi
	addl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	addq	%rax, %rdi
	movl	-68(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rax
	movslq	(%rdi,%rax,4), %r8
	shlq	$25, %r8
	movslq	%ecx, %r9
	movq	%rax, -80(%rbp)         # 8-byte Spill
	movq	%r8, %rax
	cqto
	idivq	%r9
	shlq	$3, %rax
	movl	%eax, %ecx
	sarl	$3, %ecx
	movq	-80(%rbp), %rax         # 8-byte Reload
	movl	%ecx, (%rdi,%rax,4)
# %bb.15:                               # %for.inc103
                                        #   in Loop: Header=BB6_13 Depth=3
	movl	-68(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64(%rbp)         # 4-byte Spill
	jmp	.LBB6_13
.LBB6_16:                               # %for.end105
                                        #   in Loop: Header=BB6_11 Depth=2
	movsd	.LCPI6_2(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-60(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movsd	%xmm0, v+3040(,%rcx,8)
	movl	$18, %edx
	movl	%edx, -84(%rbp)         # 4-byte Spill
.LBB6_17:                               # %for.cond108
                                        #   Parent Loop BB6_9 Depth=1
                                        #     Parent Loop BB6_11 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-84(%rbp), %eax         # 4-byte Reload
	cmpl	$1, %eax
	movl	%eax, -88(%rbp)         # 4-byte Spill
	jl	.LBB6_20
# %bb.18:                               # %for.body111
                                        #   in Loop: Header=BB6_17 Depth=3
	movl	-60(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$p.fixp, %rdx
	addq	%rcx, %rdx
	movl	-88(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	addl	$1, %esi
	movslq	%esi, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$v.fixp, %rdx
	movq	%rdx, %r8
	addq	%rcx, %r8
	movslq	%eax, %rcx
	movl	(%r8,%rcx,4), %esi
	movslq	%edi, %rcx
	movslq	%esi, %r8
	imulq	%r8, %rcx
	sarq	$30, %rcx
	movl	%ecx, %esi
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$q.fixp, %r8
	addq	%rcx, %r8
	movl	-88(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%r8,%rcx,4), %r9d
	sarl	$7, %esi
	addl	%r9d, %esi
	movslq	%edi, %rcx
	imulq	$80, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	shll	$7, %esi
	movl	%esi, (%rdx,%rcx,4)
# %bb.19:                               # %for.inc131
                                        #   in Loop: Header=BB6_17 Depth=3
	movl	-88(%rbp), %eax         # 4-byte Reload
	addl	$-1, %eax
	movl	%eax, -84(%rbp)         # 4-byte Spill
	jmp	.LBB6_17
.LBB6_20:                               # %for.end132
                                        #   in Loop: Header=BB6_11 Depth=2
	jmp	.LBB6_21
.LBB6_21:                               # %for.inc133
                                        #   in Loop: Header=BB6_11 Depth=2
	movl	-60(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -56(%rbp)         # 4-byte Spill
	jmp	.LBB6_11
.LBB6_22:                               # %for.end135
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	$1, %eax
	movl	%eax, -92(%rbp)         # 4-byte Spill
	jmp	.LBB6_23
.LBB6_23:                               # %for.cond136
                                        #   Parent Loop BB6_9 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_25 Depth 3
                                        #       Child Loop BB6_29 Depth 3
	movl	-92(%rbp), %eax         # 4-byte Reload
	cmpl	$19, %eax
	movl	%eax, -96(%rbp)         # 4-byte Spill
	jge	.LBB6_34
# %bb.24:                               # %for.body139
                                        #   in Loop: Header=BB6_23 Depth=2
	movl	-96(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$u.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	$268435456, (%rsi)      # imm = 0x10000000
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$p.fixp, %rsi
	addq	%rcx, %rsi
	movl	$0, (%rsi)
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	addq	%rcx, %rdx
	movl	(%rdx), %edi
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$q.fixp, %rdx
	addq	%rcx, %rdx
	sarl	$6, %edi
	movl	%edi, (%rdx)
	movl	$1, %edi
	movl	%edi, -100(%rbp)        # 4-byte Spill
.LBB6_25:                               # %for.cond152
                                        #   Parent Loop BB6_9 Depth=1
                                        #     Parent Loop BB6_23 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-100(%rbp), %eax        # 4-byte Reload
	cmpl	$19, %eax
	movl	%eax, -104(%rbp)        # 4-byte Spill
	jge	.LBB6_28
# %bb.26:                               # %for.body155
                                        #   in Loop: Header=BB6_25 Depth=3
	xorl	%eax, %eax
	movl	%eax, %ecx
	subl	f.fixp, %ecx
	movl	d.fixp, %edx
	movl	-96(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rdi
	imulq	$80, %rdi, %rdi
	movabsq	$p.fixp, %r8
	movq	%r8, %r9
	addq	%rdi, %r9
	movl	-104(%rbp), %r10d       # 4-byte Reload
	subl	$1, %r10d
	movslq	%r10d, %rdi
	movl	(%r9,%rdi,4), %r10d
	movslq	%edx, %rdi
	movslq	%r10d, %r9
	imulq	%r9, %rdi
	sarq	$31, %rdi
	movl	%edi, %edx
	movl	e.fixp, %r10d
	shrl	$1, %r10d
	addl	%r10d, %edx
	movslq	%ecx, %rdi
	shlq	$26, %rdi
	movslq	%edx, %r9
	movl	%eax, -108(%rbp)        # 4-byte Spill
	movq	%rdi, %rax
	cqto
	idivq	%r9
	shlq	$3, %rax
	movl	%eax, %ecx
	movslq	%esi, %rax
	imulq	$80, %rax, %rax
	movq	%r8, %rdi
	addq	%rax, %rdi
	movl	-104(%rbp), %r10d       # 4-byte Reload
	movslq	%r10d, %rax
	movl	%ecx, (%rdi,%rax,4)
	movl	-108(%rbp), %ecx        # 4-byte Reload
	subl	a.fixp, %ecx
	subl	$1, %esi
	movslq	%esi, %rax
	imulq	$80, %rax, %rax
	movabsq	$v.fixp, %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r9
	imulq	%r9, %rax
	sarq	$31, %rax
	movl	%eax, %ecx
	movslq	a.fixp, %rax
	shlq	$1, %rax
	sarq	$1, %rax
	movl	%eax, %esi
	sarl	$1, %esi
	addl	$16777216, %esi         # imm = 0x1000000
	movl	-96(%rbp), %r11d        # 4-byte Reload
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	movq	%rdi, %r9
	addq	%rax, %r9
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %ebx
	movslq	%esi, %rax
	movslq	%ebx, %r9
	imulq	%r9, %rax
	sarq	$29, %rax
	movl	%eax, %esi
	sarl	$1, %ecx
	sarl	$1, %esi
	addl	%esi, %ecx
	movl	c.fixp, %esi
	addl	$1, %r11d
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	addq	%rax, %rdi
	movslq	%r10d, %rax
	movl	(%rdi,%rax,4), %r11d
	movslq	%esi, %rax
	movslq	%r11d, %rdi
	imulq	%rdi, %rax
	sarq	$32, %rax
	movl	%eax, %esi
	subl	%esi, %ecx
	movl	d.fixp, %esi
	movl	-96(%rbp), %r11d        # 4-byte Reload
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	movabsq	$q.fixp, %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	subl	$1, %r10d
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %r10d
	movslq	%esi, %rax
	movslq	%r10d, %r9
	imulq	%r9, %rax
	sarq	$31, %rax
	movl	%eax, %esi
	sarl	$5, %ecx
	subl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	movq	%rdi, %r9
	addq	%rax, %r9
	movl	-104(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rax
	shll	$4, %ecx
	movl	%ecx, (%r9,%rax,4)
	movl	d.fixp, %ecx
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	addq	%rax, %r8
	subl	$1, %esi
	movslq	%esi, %rax
	movl	(%r8,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r8
	imulq	%r8, %rax
	sarq	$31, %rax
	movl	%eax, %ecx
	movl	e.fixp, %esi
	sarl	$1, %ecx
	shrl	$2, %esi
	addl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$80, %rax, %rax
	addq	%rax, %rdi
	movl	-104(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rax
	movslq	(%rdi,%rax,4), %r8
	shlq	$25, %r8
	movslq	%ecx, %r9
	movq	%rax, -120(%rbp)        # 8-byte Spill
	movq	%r8, %rax
	cqto
	idivq	%r9
	shlq	$3, %rax
	movl	%eax, %ecx
	sarl	$3, %ecx
	movq	-120(%rbp), %rax        # 8-byte Reload
	movl	%ecx, (%rdi,%rax,4)
# %bb.27:                               # %for.inc214
                                        #   in Loop: Header=BB6_25 Depth=3
	movl	-104(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -100(%rbp)        # 4-byte Spill
	jmp	.LBB6_25
.LBB6_28:                               # %for.end216
                                        #   in Loop: Header=BB6_23 Depth=2
	movl	-96(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$u.fixp, %rdx
	addq	%rcx, %rdx
	movl	$268435456, 76(%rdx)    # imm = 0x10000000
	movl	$18, %esi
	movl	%esi, -124(%rbp)        # 4-byte Spill
.LBB6_29:                               # %for.cond220
                                        #   Parent Loop BB6_9 Depth=1
                                        #     Parent Loop BB6_23 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-124(%rbp), %eax        # 4-byte Reload
	cmpl	$1, %eax
	movl	%eax, -128(%rbp)        # 4-byte Spill
	jl	.LBB6_32
# %bb.30:                               # %for.body223
                                        #   in Loop: Header=BB6_29 Depth=3
	movl	-96(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$p.fixp, %rdx
	addq	%rcx, %rdx
	movl	-128(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$u.fixp, %rdx
	movq	%rdx, %r8
	addq	%rcx, %r8
	addl	$1, %esi
	movslq	%esi, %rcx
	movl	(%r8,%rcx,4), %esi
	movslq	%edi, %rcx
	movslq	%esi, %r8
	imulq	%r8, %rcx
	sarq	$30, %rcx
	movl	%ecx, %esi
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$q.fixp, %r8
	addq	%rcx, %r8
	movl	-128(%rbp), %edi        # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%r8,%rcx,4), %r9d
	sarl	$6, %esi
	addl	%r9d, %esi
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	shll	$6, %esi
	movl	%esi, (%rdx,%rcx,4)
# %bb.31:                               # %for.inc243
                                        #   in Loop: Header=BB6_29 Depth=3
	movl	-128(%rbp), %eax        # 4-byte Reload
	addl	$-1, %eax
	movl	%eax, -124(%rbp)        # 4-byte Spill
	jmp	.LBB6_29
.LBB6_32:                               # %for.end245
                                        #   in Loop: Header=BB6_23 Depth=2
	jmp	.LBB6_33
.LBB6_33:                               # %for.inc246
                                        #   in Loop: Header=BB6_23 Depth=2
	movl	-96(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -92(%rbp)         # 4-byte Spill
	jmp	.LBB6_23
.LBB6_34:                               # %for.end248
                                        #   in Loop: Header=BB6_9 Depth=1
	jmp	.LBB6_35
.LBB6_35:                               # %for.inc249
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	-52(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -48(%rbp)         # 4-byte Spill
	jmp	.LBB6_9
.LBB6_36:                               # %for.end251
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	movl	%eax, -132(%rbp)        # 4-byte Spill
.LBB6_37:                               # %for.cond252
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_39 Depth 2
	movl	-132(%rbp), %eax        # 4-byte Reload
	cmpl	$20, %eax
	movl	%eax, -136(%rbp)        # 4-byte Spill
	jge	.LBB6_46
# %bb.38:                               # %for.body255
                                        #   in Loop: Header=BB6_37 Depth=1
	xorl	%eax, %eax
	movl	%eax, -140(%rbp)        # 4-byte Spill
	jmp	.LBB6_39
.LBB6_39:                               # %for.cond256
                                        #   Parent Loop BB6_37 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-140(%rbp), %eax        # 4-byte Reload
	cmpl	$20, %eax
	movl	%eax, -144(%rbp)        # 4-byte Spill
	jge	.LBB6_44
# %bb.40:                               # %for.body259
                                        #   in Loop: Header=BB6_39 Depth=2
	movl	-136(%rbp), %eax        # 4-byte Reload
	imull	$20, %eax, %ecx
	movl	-144(%rbp), %edx        # 4-byte Reload
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
	movabsq	$.L.str.3, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -148(%rbp)        # 4-byte Spill
.LBB6_42:                               # %if.end
                                        #   in Loop: Header=BB6_39 Depth=2
	movsd	.LCPI6_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-136(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$80, %rcx, %rcx
	movabsq	$u.fixp, %rdx
	addq	%rcx, %rdx
	movl	-144(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	cvtsi2sdl	%r8d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.4, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -152(%rbp)        # 4-byte Spill
# %bb.43:                               # %for.inc269
                                        #   in Loop: Header=BB6_39 Depth=2
	movl	-144(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -140(%rbp)        # 4-byte Spill
	jmp	.LBB6_39
.LBB6_44:                               # %for.end271
                                        #   in Loop: Header=BB6_37 Depth=1
	jmp	.LBB6_45
.LBB6_45:                               # %for.inc272
                                        #   in Loop: Header=BB6_37 Depth=1
	movl	-136(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -132(%rbp)        # 4-byte Spill
	jmp	.LBB6_37
.LBB6_46:                               # %for.end274
	xorl	%eax, %eax
	addq	$152, %rsp
	popq	%rbx
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

	.type	u,@object               # @u
	.comm	u,3200,16
	.type	DX,@object              # @DX
	.comm	DX,8,8
	.type	DY,@object              # @DY
	.comm	DY,8,8
	.type	DT,@object              # @DT
	.comm	DT,8,8
	.type	B1,@object              # @B1
	.comm	B1,8,8
	.type	B2,@object              # @B2
	.comm	B2,8,8
	.type	mul1,@object            # @mul1
	.comm	mul1,8,8
	.type	mul2,@object            # @mul2
	.comm	mul2,8,8
	.type	a,@object               # @a
	.comm	a,8,8
	.type	b,@object               # @b
	.comm	b,8,8
	.type	c,@object               # @c
	.comm	c,8,8
	.type	d,@object               # @d
	.comm	d,8,8
	.type	e,@object               # @e
	.comm	e,8,8
	.type	f,@object               # @f
	.comm	f,8,8
	.type	v,@object               # @v
	.comm	v,3200,16
	.type	p,@object               # @p
	.comm	p,3200,16
	.type	q,@object               # @q
	.comm	q,3200,16
	.type	.L.str.3,@object        # @.str.3
.L.str.3:
	.asciz	"\n"
	.size	.L.str.3, 2

	.type	.L.str.4,@object        # @.str.4
.L.str.4:
	.asciz	"%0.16lf "
	.size	.L.str.4, 9

	.type	u.fixp,@object          # @u.fixp
	.comm	u.fixp,1600,16
	.type	DX.fixp,@object         # @DX.fixp
	.comm	DX.fixp,4,8
	.type	DY.fixp,@object         # @DY.fixp
	.comm	DY.fixp,4,8
	.type	DT.fixp,@object         # @DT.fixp
	.comm	DT.fixp,4,8
	.type	B1.fixp,@object         # @B1.fixp
	.comm	B1.fixp,4,8
	.type	B2.fixp,@object         # @B2.fixp
	.comm	B2.fixp,4,8
	.type	mul1.fixp,@object       # @mul1.fixp
	.comm	mul1.fixp,4,8
	.type	mul2.fixp,@object       # @mul2.fixp
	.comm	mul2.fixp,4,8
	.type	a.fixp,@object          # @a.fixp
	.comm	a.fixp,4,8
	.type	b.fixp,@object          # @b.fixp
	.comm	b.fixp,4,8
	.type	c.fixp,@object          # @c.fixp
	.comm	c.fixp,4,8
	.type	d.fixp,@object          # @d.fixp
	.comm	d.fixp,4,8
	.type	e.fixp,@object          # @e.fixp
	.comm	e.fixp,4,8
	.type	f.fixp,@object          # @f.fixp
	.comm	f.fixp,4,8
	.type	v.fixp,@object          # @v.fixp
	.comm	v.fixp,1600,16
	.type	p.fixp,@object          # @p.fixp
	.comm	p.fixp,1600,16
	.type	q.fixp,@object          # @q.fixp
	.comm	q.fixp,1600,16

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
	.addrsig_sym u
	.addrsig_sym DX
	.addrsig_sym DY
	.addrsig_sym DT
	.addrsig_sym B1
	.addrsig_sym B2
	.addrsig_sym mul1
	.addrsig_sym mul2
	.addrsig_sym a
	.addrsig_sym b
	.addrsig_sym c
	.addrsig_sym d
	.addrsig_sym e
	.addrsig_sym f
	.addrsig_sym v
	.addrsig_sym p
	.addrsig_sym q
	.addrsig_sym stdout
	.addrsig_sym u.fixp
	.addrsig_sym DX.fixp
	.addrsig_sym DY.fixp
	.addrsig_sym DT.fixp
	.addrsig_sym B1.fixp
	.addrsig_sym B2.fixp
	.addrsig_sym mul1.fixp
	.addrsig_sym mul2.fixp
	.addrsig_sym a.fixp
	.addrsig_sym b.fixp
	.addrsig_sym c.fixp
	.addrsig_sym d.fixp
	.addrsig_sym e.fixp
	.addrsig_sym f.fixp
	.addrsig_sym v.fixp
	.addrsig_sym p.fixp
	.addrsig_sym q.fixp
