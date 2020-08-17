	.text
	.file	"heat-3d.c"
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
	.quad	4683743612465315840     # double 131072
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
	subq	$112, %rsp
	callq	TAFFO_DUMPCONFIG
	callq	TIMING_CPUCLOCK_START
	xorl	%eax, %eax
	movl	%eax, -4(%rbp)          # 4-byte Spill
.LBB6_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_3 Depth 2
                                        #       Child Loop BB6_5 Depth 3
	movl	-4(%rbp), %eax          # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -8(%rbp)          # 4-byte Spill
	jge	.LBB6_12
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB6_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -12(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_3:                                # %for.cond5
                                        #   Parent Loop BB6_1 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_5 Depth 3
	movl	-12(%rbp), %eax         # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jge	.LBB6_10
# %bb.4:                                # %for.body7
                                        #   in Loop: Header=BB6_3 Depth=2
	xorl	%eax, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jmp	.LBB6_5
.LBB6_5:                                # %for.cond8
                                        #   Parent Loop BB6_1 Depth=1
                                        #     Parent Loop BB6_3 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-20(%rbp), %eax         # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -24(%rbp)         # 4-byte Spill
	jge	.LBB6_8
# %bb.6:                                # %for.body10
                                        #   in Loop: Header=BB6_5 Depth=3
	movl	-8(%rbp), %eax          # 4-byte Reload
	movl	-16(%rbp), %ecx         # 4-byte Reload
	addl	%ecx, %eax
	movl	$40, %edx
	movl	-24(%rbp), %esi         # 4-byte Reload
	subl	%esi, %edx
	addl	%edx, %eax
	shll	$24, %eax
	movl	%eax, %eax
	movl	%eax, %edi
	imulq	$10, %rdi, %rdi
	shrq	$3, %rdi
	movl	%edi, %eax
	movl	%eax, %eax
	movl	%eax, %edi
	shlq	$26, %rdi
	movq	%rdi, %rax
	xorl	%edx, %edx
                                        # kill: def $rdx killed $edx
	movl	$2684354560, %edi       # imm = 0xA0000000
	divq	%rdi
	shlq	$5, %rax
	movl	%eax, %r8d
	movl	-8(%rbp), %r9d          # 4-byte Reload
	movslq	%r9d, %rax
	imulq	$6400, %rax, %rax       # imm = 0x1900
	movabsq	$B.fixp, %rdi
	addq	%rax, %rdi
	movslq	%ecx, %rax
	imulq	$160, %rax, %rax
	addq	%rax, %rdi
	movslq	%esi, %rax
	movl	%r8d, %r10d
	shrl	$8, %r10d
	movl	%r10d, (%rdi,%rax,4)
	movslq	%r9d, %rax
	imulq	$6400, %rax, %rax       # imm = 0x1900
	movabsq	$A.fixp, %rdi
	addq	%rax, %rdi
	movslq	%ecx, %rax
	imulq	$160, %rax, %rax
	addq	%rax, %rdi
	movslq	%esi, %rax
	shrl	$9, %r8d
	movl	%r8d, (%rdi,%rax,4)
# %bb.7:                                # %for.inc
                                        #   in Loop: Header=BB6_5 Depth=3
	movl	-24(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jmp	.LBB6_5
.LBB6_8:                                # %for.end
                                        #   in Loop: Header=BB6_3 Depth=2
	jmp	.LBB6_9
.LBB6_9:                                # %for.inc23
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-16(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -12(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_10:                               # %for.end25
                                        #   in Loop: Header=BB6_1 Depth=1
	jmp	.LBB6_11
.LBB6_11:                               # %for.inc26
                                        #   in Loop: Header=BB6_1 Depth=1
	movl	-8(%rbp), %eax          # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -4(%rbp)          # 4-byte Spill
	jmp	.LBB6_1
.LBB6_12:                               # %for.end28
	movl	$1, %eax
	movl	%eax, -28(%rbp)         # 4-byte Spill
	jmp	.LBB6_13
.LBB6_13:                               # %for.cond29
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_15 Depth 2
                                        #       Child Loop BB6_17 Depth 3
                                        #         Child Loop BB6_19 Depth 4
                                        #     Child Loop BB6_27 Depth 2
                                        #       Child Loop BB6_29 Depth 3
                                        #         Child Loop BB6_31 Depth 4
	movl	-28(%rbp), %eax         # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jg	.LBB6_40
# %bb.14:                               # %for.body32
                                        #   in Loop: Header=BB6_13 Depth=1
	movl	$1, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_15
.LBB6_15:                               # %for.cond33
                                        #   Parent Loop BB6_13 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_17 Depth 3
                                        #         Child Loop BB6_19 Depth 4
	movl	-36(%rbp), %eax         # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jge	.LBB6_26
# %bb.16:                               # %for.body36
                                        #   in Loop: Header=BB6_15 Depth=2
	movl	$1, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jmp	.LBB6_17
.LBB6_17:                               # %for.cond37
                                        #   Parent Loop BB6_13 Depth=1
                                        #     Parent Loop BB6_15 Depth=2
                                        # =>    This Loop Header: Depth=3
                                        #         Child Loop BB6_19 Depth 4
	movl	-44(%rbp), %eax         # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -48(%rbp)         # 4-byte Spill
	jge	.LBB6_24
# %bb.18:                               # %for.body40
                                        #   in Loop: Header=BB6_17 Depth=3
	movl	$1, %eax
	movl	%eax, -52(%rbp)         # 4-byte Spill
	jmp	.LBB6_19
.LBB6_19:                               # %for.cond41
                                        #   Parent Loop BB6_13 Depth=1
                                        #     Parent Loop BB6_15 Depth=2
                                        #       Parent Loop BB6_17 Depth=3
                                        # =>      This Inner Loop Header: Depth=4
	movl	-52(%rbp), %eax         # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -56(%rbp)         # 4-byte Spill
	jge	.LBB6_22
# %bb.20:                               # %for.body44
                                        #   in Loop: Header=BB6_19 Depth=4
	movl	-40(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movabsq	$A.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-48(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-56(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movl	-40(%rbp), %r9d         # 4-byte Reload
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movslq	(%rsi,%rcx,4), %rcx
	shlq	$1, %rcx
	shlq	$1, %rcx
	movl	%ecx, %r10d
	shll	$1, %r8d
	subl	%r10d, %r8d
	subl	$1, %r9d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r9d
	shll	$1, %r9d
	addl	%r9d, %r8d
	movslq	%r8d, %rcx
	shlq	$0, %rcx
	sarq	$1, %rcx
	movl	%ecx, %r8d
	movl	-40(%rbp), %r9d         # 4-byte Reload
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %eax
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-48(%rbp), %r10d        # 4-byte Reload
	movslq	%r10d, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movslq	(%rsi,%rcx,4), %rcx
	shlq	$1, %rcx
	shlq	$1, %rcx
	movl	%ecx, %r11d
	shll	$1, %eax
	subl	%r11d, %eax
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	subl	$1, %r10d
	movslq	%r10d, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r10d
	shll	$1, %r10d
	addl	%r10d, %eax
	movslq	%eax, %rcx
	shlq	$0, %rcx
	sarq	$1, %rcx
	movl	%ecx, %eax
	sarl	$1, %r8d
	sarl	$1, %eax
	addl	%eax, %r8d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-48(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	addl	$1, %edi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %edi
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-56(%rbp), %r10d        # 4-byte Reload
	movslq	%r10d, %rcx
	movslq	(%rsi,%rcx,4), %rcx
	shlq	$1, %rcx
	shlq	$1, %rcx
	movl	%ecx, %r11d
	shll	$1, %edi
	subl	%r11d, %edi
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	subl	$1, %r10d
	movslq	%r10d, %rcx
	movl	(%rsi,%rcx,4), %r10d
	shll	$1, %r10d
	addl	%r10d, %edi
	movslq	%edi, %rcx
	shlq	$0, %rcx
	sarq	$2, %rcx
	movl	%ecx, %edi
	sarl	$1, %r8d
	sarl	$1, %edi
	addl	%edi, %r8d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-56(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r10d
	shll	$1, %r10d
	addl	%r10d, %r8d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movabsq	$B.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	%r8d, (%rdx,%rcx,4)
# %bb.21:                               # %for.inc132
                                        #   in Loop: Header=BB6_19 Depth=4
	movl	-56(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -52(%rbp)         # 4-byte Spill
	jmp	.LBB6_19
.LBB6_22:                               # %for.end134
                                        #   in Loop: Header=BB6_17 Depth=3
	jmp	.LBB6_23
.LBB6_23:                               # %for.inc135
                                        #   in Loop: Header=BB6_17 Depth=3
	movl	-48(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jmp	.LBB6_17
.LBB6_24:                               # %for.end137
                                        #   in Loop: Header=BB6_15 Depth=2
	jmp	.LBB6_25
.LBB6_25:                               # %for.inc138
                                        #   in Loop: Header=BB6_15 Depth=2
	movl	-40(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_15
.LBB6_26:                               # %for.end140
                                        #   in Loop: Header=BB6_13 Depth=1
	movl	$1, %eax
	movl	%eax, -60(%rbp)         # 4-byte Spill
	jmp	.LBB6_27
.LBB6_27:                               # %for.cond141
                                        #   Parent Loop BB6_13 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_29 Depth 3
                                        #         Child Loop BB6_31 Depth 4
	movl	-60(%rbp), %eax         # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -64(%rbp)         # 4-byte Spill
	jge	.LBB6_38
# %bb.28:                               # %for.body144
                                        #   in Loop: Header=BB6_27 Depth=2
	movl	$1, %eax
	movl	%eax, -68(%rbp)         # 4-byte Spill
	jmp	.LBB6_29
.LBB6_29:                               # %for.cond145
                                        #   Parent Loop BB6_13 Depth=1
                                        #     Parent Loop BB6_27 Depth=2
                                        # =>    This Loop Header: Depth=3
                                        #         Child Loop BB6_31 Depth 4
	movl	-68(%rbp), %eax         # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -72(%rbp)         # 4-byte Spill
	jge	.LBB6_36
# %bb.30:                               # %for.body148
                                        #   in Loop: Header=BB6_29 Depth=3
	movl	$1, %eax
	movl	%eax, -76(%rbp)         # 4-byte Spill
	jmp	.LBB6_31
.LBB6_31:                               # %for.cond149
                                        #   Parent Loop BB6_13 Depth=1
                                        #     Parent Loop BB6_27 Depth=2
                                        #       Parent Loop BB6_29 Depth=3
                                        # =>      This Inner Loop Header: Depth=4
	movl	-76(%rbp), %eax         # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -80(%rbp)         # 4-byte Spill
	jge	.LBB6_34
# %bb.32:                               # %for.body152
                                        #   in Loop: Header=BB6_31 Depth=4
	movl	-64(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movabsq	$B.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-72(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-80(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movl	-64(%rbp), %r9d         # 4-byte Reload
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movslq	(%rsi,%rcx,4), %rcx
	shlq	$1, %rcx
	sarq	$1, %rcx
	movl	%ecx, %r10d
	sarl	$2, %r8d
	sarl	$1, %r10d
	subl	%r10d, %r8d
	subl	$1, %r9d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r9d
	sarl	$2, %r9d
	addl	%r9d, %r8d
	movslq	%r8d, %rcx
	shlq	$0, %rcx
	sarq	$1, %rcx
	movl	%ecx, %r8d
	movl	-64(%rbp), %r9d         # 4-byte Reload
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %eax
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-72(%rbp), %r10d        # 4-byte Reload
	movslq	%r10d, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movslq	(%rsi,%rcx,4), %rcx
	shlq	$1, %rcx
	sarq	$1, %rcx
	movl	%ecx, %r11d
	sarl	$2, %eax
	sarl	$1, %r11d
	subl	%r11d, %eax
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	subl	$1, %r10d
	movslq	%r10d, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r10d
	sarl	$2, %r10d
	addl	%r10d, %eax
	movslq	%eax, %rcx
	shlq	$0, %rcx
	sarq	$1, %rcx
	movl	%ecx, %eax
	addl	%eax, %r8d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-72(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	addl	$1, %edi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %edi
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-80(%rbp), %r10d        # 4-byte Reload
	movslq	%r10d, %rcx
	movslq	(%rsi,%rcx,4), %rcx
	shlq	$1, %rcx
	sarq	$1, %rcx
	movl	%ecx, %r11d
	sarl	$2, %edi
	sarl	$1, %r11d
	subl	%r11d, %edi
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	subl	$1, %r10d
	movslq	%r10d, %rcx
	movl	(%rsi,%rcx,4), %r10d
	sarl	$2, %r10d
	addl	%r10d, %edi
	movslq	%edi, %rcx
	shlq	$0, %rcx
	sarq	$1, %rcx
	movl	%ecx, %edi
	sarl	$1, %r8d
	sarl	$1, %edi
	addl	%edi, %r8d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-80(%rbp), %edi         # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r10d
	sarl	$1, %r10d
	addl	%r10d, %r8d
	movslq	%r9d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movabsq	$A.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	%r8d, (%rdx,%rcx,4)
# %bb.33:                               # %for.inc240
                                        #   in Loop: Header=BB6_31 Depth=4
	movl	-80(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -76(%rbp)         # 4-byte Spill
	jmp	.LBB6_31
.LBB6_34:                               # %for.end242
                                        #   in Loop: Header=BB6_29 Depth=3
	jmp	.LBB6_35
.LBB6_35:                               # %for.inc243
                                        #   in Loop: Header=BB6_29 Depth=3
	movl	-72(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -68(%rbp)         # 4-byte Spill
	jmp	.LBB6_29
.LBB6_36:                               # %for.end245
                                        #   in Loop: Header=BB6_27 Depth=2
	jmp	.LBB6_37
.LBB6_37:                               # %for.inc246
                                        #   in Loop: Header=BB6_27 Depth=2
	movl	-64(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -60(%rbp)         # 4-byte Spill
	jmp	.LBB6_27
.LBB6_38:                               # %for.end248
                                        #   in Loop: Header=BB6_13 Depth=1
	jmp	.LBB6_39
.LBB6_39:                               # %for.inc249
                                        #   in Loop: Header=BB6_13 Depth=1
	movl	-32(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -28(%rbp)         # 4-byte Spill
	jmp	.LBB6_13
.LBB6_40:                               # %for.end251
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	movl	%eax, -84(%rbp)         # 4-byte Spill
.LBB6_41:                               # %for.cond252
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_43 Depth 2
                                        #       Child Loop BB6_45 Depth 3
	movl	-84(%rbp), %eax         # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -88(%rbp)         # 4-byte Spill
	jge	.LBB6_54
# %bb.42:                               # %for.body255
                                        #   in Loop: Header=BB6_41 Depth=1
	xorl	%eax, %eax
	movl	%eax, -92(%rbp)         # 4-byte Spill
	jmp	.LBB6_43
.LBB6_43:                               # %for.cond256
                                        #   Parent Loop BB6_41 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB6_45 Depth 3
	movl	-92(%rbp), %eax         # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -96(%rbp)         # 4-byte Spill
	jge	.LBB6_52
# %bb.44:                               # %for.body259
                                        #   in Loop: Header=BB6_43 Depth=2
	xorl	%eax, %eax
	movl	%eax, -100(%rbp)        # 4-byte Spill
	jmp	.LBB6_45
.LBB6_45:                               # %for.cond260
                                        #   Parent Loop BB6_41 Depth=1
                                        #     Parent Loop BB6_43 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-100(%rbp), %eax        # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -104(%rbp)        # 4-byte Spill
	jge	.LBB6_50
# %bb.46:                               # %for.body263
                                        #   in Loop: Header=BB6_45 Depth=3
	movl	-88(%rbp), %eax         # 4-byte Reload
	imull	$40, %eax, %ecx
	imull	$40, %ecx, %ecx
	movl	-96(%rbp), %edx         # 4-byte Reload
	imull	$40, %edx, %esi
	addl	%esi, %ecx
	movl	-104(%rbp), %esi        # 4-byte Reload
	addl	%esi, %ecx
	movl	%ecx, %eax
	cltd
	movl	$20, %ecx
	idivl	%ecx
	cmpl	$0, %edx
	jne	.LBB6_48
# %bb.47:                               # %if.then
                                        #   in Loop: Header=BB6_45 Depth=3
	movq	stdout, %rdi
	movabsq	$.L.str.3, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -108(%rbp)        # 4-byte Spill
.LBB6_48:                               # %if.end
                                        #   in Loop: Header=BB6_45 Depth=3
	movsd	.LCPI6_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-88(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movabsq	$A.fixp, %rdx
	addq	%rcx, %rdx
	movl	-96(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-104(%rbp), %r8d        # 4-byte Reload
	movslq	%r8d, %rcx
	movl	(%rdx,%rcx,4), %r9d
	cvtsi2sdl	%r9d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.4, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -112(%rbp)        # 4-byte Spill
# %bb.49:                               # %for.inc278
                                        #   in Loop: Header=BB6_45 Depth=3
	movl	-104(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -100(%rbp)        # 4-byte Spill
	jmp	.LBB6_45
.LBB6_50:                               # %for.end280
                                        #   in Loop: Header=BB6_43 Depth=2
	jmp	.LBB6_51
.LBB6_51:                               # %for.inc281
                                        #   in Loop: Header=BB6_43 Depth=2
	movl	-96(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -92(%rbp)         # 4-byte Spill
	jmp	.LBB6_43
.LBB6_52:                               # %for.end283
                                        #   in Loop: Header=BB6_41 Depth=1
	jmp	.LBB6_53
.LBB6_53:                               # %for.inc284
                                        #   in Loop: Header=BB6_41 Depth=1
	movl	-88(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -84(%rbp)         # 4-byte Spill
	jmp	.LBB6_41
.LBB6_54:                               # %for.end286
	xorl	%eax, %eax
	addq	$112, %rsp
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

	.type	B,@object               # @B
	.comm	B,512000,16
	.type	A,@object               # @A
	.comm	A,512000,16
	.type	.L.str.3,@object        # @.str.3
.L.str.3:
	.asciz	"\n"
	.size	.L.str.3, 2

	.type	.L.str.4,@object        # @.str.4
.L.str.4:
	.asciz	"%0.16lf "
	.size	.L.str.4, 9

	.type	B.fixp,@object          # @B.fixp
	.comm	B.fixp,256000,16
	.type	A.fixp,@object          # @A.fixp
	.comm	A.fixp,256000,16

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
	.addrsig_sym time_that_takes
	.addrsig_sym stderr
	.addrsig_sym B
	.addrsig_sym A
	.addrsig_sym stdout
	.addrsig_sym B.fixp
	.addrsig_sym A.fixp
