	.text
	.file	"deriche.c"
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
	.quad	-4620693217682128896    # double -0.5
.LCPI6_1:
	.quad	4611686018427387904     # double 2
.LCPI6_2:
	.quad	-4625196817309499392    # double -0.25
.LCPI6_3:
	.quad	4607182418800017408     # double 1
.LCPI6_4:
	.quad	4602678819172646912     # double 0.5
.LCPI6_5:
	.quad	4742290407621132288     # double 1073741824
.LCPI6_6:
	.quad	4746794007248502784     # double 2147483648
.LCPI6_7:
	.quad	4728779608739020800     # double 134217728
.LCPI6_8:
	.quad	4737786807993761792     # double 536870912
.LCPI6_9:
	.quad	4733283208366391296     # double 268435456
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
	pushq	%r15
	pushq	%r14
	pushq	%r12
	pushq	%rbx
	subq	$400, %rsp              # imm = 0x190
	.cfi_offset %rbx, -48
	.cfi_offset %r12, -40
	.cfi_offset %r14, -32
	.cfi_offset %r15, -24
	callq	TAFFO_DUMPCONFIG
	callq	TIMING_CPUCLOCK_START
	xorl	%eax, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
.LBB6_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_3 Depth 2
	movl	-36(%rbp), %eax         # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jge	.LBB6_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB6_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_3:                                # %for.cond4
                                        #   Parent Loop BB6_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-44(%rbp), %eax         # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -48(%rbp)         # 4-byte Spill
	jge	.LBB6_6
# %bb.4:                                # %for.body6
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-40(%rbp), %eax         # 4-byte Reload
	imull	$313, %eax, %ecx        # imm = 0x139
	movl	-48(%rbp), %edx         # 4-byte Reload
	imull	$991, %edx, %esi        # imm = 0x3DF
	addl	%esi, %ecx
	movl	%ecx, %eax
	cltd
	movl	$65536, %ecx            # imm = 0x10000
	idivl	%ecx
	shll	$14, %edx
	movslq	%edx, %rdi
	movq	%rdi, %rax
	cqto
	movl	$65535, %edi            # imm = 0xFFFF
	idivq	%rdi
	shlq	$15, %rax
	movl	%eax, %ecx
	movl	-40(%rbp), %esi         # 4-byte Reload
	movslq	%esi, %rax
	shlq	$8, %rax
	movabsq	$imgIn.fixp, %rdi
	addq	%rax, %rdi
	movl	-48(%rbp), %r8d         # 4-byte Reload
	movslq	%r8d, %rax
	movl	%ecx, (%rdi,%rax,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-48(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_6:                                # %for.end
                                        #   in Loop: Header=BB6_1 Depth=1
	jmp	.LBB6_7
.LBB6_7:                                # %for.inc10
                                        #   in Loop: Header=BB6_1 Depth=1
	movl	-40(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jmp	.LBB6_1
.LBB6_8:                                # %for.end12
	movsd	.LCPI6_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI6_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI6_2(%rip), %xmm2   # xmm2 = mem[0],zero
	movsd	%xmm0, -56(%rbp)        # 8-byte Spill
	movaps	%xmm2, %xmm0
	movsd	%xmm1, -64(%rbp)        # 8-byte Spill
	movsd	%xmm2, -72(%rbp)        # 8-byte Spill
	callq	exp
	movsd	.LCPI6_3(%rip), %xmm1   # xmm1 = mem[0],zero
	movaps	%xmm1, %xmm2
	subsd	%xmm0, %xmm2
	movsd	-72(%rbp), %xmm0        # 8-byte Reload
                                        # xmm0 = mem[0],zero
	movsd	%xmm1, -80(%rbp)        # 8-byte Spill
	movsd	%xmm2, -88(%rbp)        # 8-byte Spill
	callq	exp
	movsd	-80(%rbp), %xmm1        # 8-byte Reload
                                        # xmm1 = mem[0],zero
	subsd	%xmm0, %xmm1
	movsd	-88(%rbp), %xmm0        # 8-byte Reload
                                        # xmm0 = mem[0],zero
	mulsd	%xmm1, %xmm0
	movsd	-72(%rbp), %xmm1        # 8-byte Reload
                                        # xmm1 = mem[0],zero
	movsd	%xmm0, -96(%rbp)        # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	.LCPI6_4(%rip), %xmm1   # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	movsd	-80(%rbp), %xmm2        # 8-byte Reload
                                        # xmm2 = mem[0],zero
	addsd	%xmm2, %xmm0
	movsd	%xmm0, -104(%rbp)       # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	-104(%rbp), %xmm1       # 8-byte Reload
                                        # xmm1 = mem[0],zero
	subsd	%xmm0, %xmm1
	movsd	-96(%rbp), %xmm0        # 8-byte Reload
                                        # xmm0 = mem[0],zero
	divsd	%xmm1, %xmm0
	movsd	-72(%rbp), %xmm1        # 8-byte Reload
                                        # xmm1 = mem[0],zero
	movsd	%xmm0, -112(%rbp)       # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	.LCPI6_5(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	-112(%rbp), %xmm2       # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm1, %xmm2
	cvttsd2si	%xmm2, %eax
	movsd	.LCPI6_6(%rip), %xmm1   # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movslq	%eax, %rdx
	movl	%ecx, %esi
	movl	%esi, %esi
	movl	%esi, %ecx
	movq	%rdx, %rdi
	imulq	%rcx, %rdi
	shrq	$31, %rdi
	movl	%edi, %esi
	movslq	%esi, %rcx
	leaq	(%rcx,%rcx,2), %rcx
	negq	%rcx
	shrq	$2, %rcx
	movl	%ecx, %esi
	movsd	-72(%rbp), %xmm0        # 8-byte Reload
                                        # xmm0 = mem[0],zero
	movl	%eax, -116(%rbp)        # 4-byte Spill
	movsd	%xmm1, -128(%rbp)       # 8-byte Spill
	movq	%rdx, -136(%rbp)        # 8-byte Spill
	movl	%esi, -140(%rbp)        # 4-byte Spill
	callq	exp
	movsd	-128(%rbp), %xmm1       # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movl	%ecx, %eax
	movl	%eax, %eax
	movl	%eax, %ecx
	movq	-136(%rbp), %rdx        # 8-byte Reload
	imulq	%rcx, %rdx
	shrq	$31, %rdx
	movl	%edx, %eax
	movslq	%eax, %rcx
	leaq	(%rcx,%rcx,4), %rcx
	shrq	$2, %rcx
	movl	%ecx, %eax
	movl	-116(%rbp), %esi        # 4-byte Reload
	addl	%esi, %esi
	negl	%esi
	movsd	.LCPI6_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	%eax, -144(%rbp)        # 4-byte Spill
	movl	%esi, -148(%rbp)        # 4-byte Spill
	callq	exp
	movsd	-128(%rbp), %xmm1       # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movl	%ecx, %eax
	movl	-148(%rbp), %esi        # 4-byte Reload
	movl	%esi, %r8d
	movl	%r8d, %ecx
	movl	%eax, %eax
	movl	%eax, %edx
	imulq	%rdx, %rcx
	sarq	$32, %rcx
	movl	%ecx, %eax
	movsd	-56(%rbp), %xmm0        # 8-byte Reload
                                        # xmm0 = mem[0],zero
	movsd	-64(%rbp), %xmm1        # 8-byte Reload
                                        # xmm1 = mem[0],zero
	movl	%eax, -152(%rbp)        # 4-byte Spill
	callq	pow
	movsd	.LCPI6_0(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	%xmm0, -160(%rbp)       # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	xorl	%eax, %eax
	movq	%xmm0, %rcx
	movabsq	$-9223372036854775808, %rdx # imm = 0x8000000000000000
	xorq	%rdx, %rcx
	movq	%rcx, %xmm0
	movsd	%xmm0, -168(%rbp)       # 8-byte Spill
	movl	%eax, -172(%rbp)        # 4-byte Spill
.LBB6_9:                                # %for.cond57
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_11 Depth 2
	movl	-172(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -176(%rbp)        # 4-byte Spill
	jge	.LBB6_16
# %bb.10:                               # %for.body60
                                        #   in Loop: Header=BB6_9 Depth=1
	xorl	%eax, %eax
	movl	%eax, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%ecx, -180(%rbp)        # 4-byte Spill
	movl	%edx, -184(%rbp)        # 4-byte Spill
	movl	%esi, -188(%rbp)        # 4-byte Spill
	movl	%eax, -192(%rbp)        # 4-byte Spill
	jmp	.LBB6_11
.LBB6_11:                               # %for.cond61
                                        #   Parent Loop BB6_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-192(%rbp), %eax        # 4-byte Reload
	movl	-188(%rbp), %ecx        # 4-byte Reload
	movl	-184(%rbp), %edx        # 4-byte Reload
	movl	-180(%rbp), %esi        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -196(%rbp)        # 4-byte Spill
	movl	%ecx, -200(%rbp)        # 4-byte Spill
	movl	%edx, -204(%rbp)        # 4-byte Spill
	movl	%esi, -208(%rbp)        # 4-byte Spill
	jge	.LBB6_14
# %bb.12:                               # %for.body64
                                        #   in Loop: Header=BB6_11 Depth=2
	movsd	.LCPI6_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI6_8(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-176(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$imgIn.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-196(%rbp), %edi        # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movaps	%xmm0, %xmm2
	movsd	-112(%rbp), %xmm3       # 8-byte Reload
                                        # xmm3 = mem[0],zero
	mulsd	%xmm3, %xmm2
	cvttsd2si	%xmm2, %r9d
	movslq	%r9d, %rcx
	movslq	%r8d, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r8d
	movl	-140(%rbp), %r9d        # 4-byte Reload
	movslq	%r9d, %rcx
	movl	-200(%rbp), %r10d       # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r11d
	addl	%r11d, %r8d
	movsd	-160(%rbp), %xmm2       # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r11d
	movslq	%r11d, %rcx
	movl	-204(%rbp), %r11d       # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %ebx
	sarl	$1, %r8d
	sarl	$1, %ebx
	addl	%ebx, %r8d
	movsd	-168(%rbp), %xmm1       # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %ebx
	movslq	%ebx, %rcx
	movl	-208(%rbp), %ebx        # 4-byte Reload
	movslq	%ebx, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r14d
	addl	%r14d, %r8d
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$_y1.fixp, %rsi
	movq	%rsi, %r15
	addq	%rcx, %r15
	movslq	%edi, %rcx
	movl	%r8d, (%r15,%rcx,4)
	movslq	%eax, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	movslq	%eax, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r14d
	movl	%r8d, -212(%rbp)        # 4-byte Spill
	movl	%r14d, -216(%rbp)       # 4-byte Spill
# %bb.13:                               # %for.inc88
                                        #   in Loop: Header=BB6_11 Depth=2
	movl	-196(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	-204(%rbp), %ecx        # 4-byte Reload
	movl	-216(%rbp), %edx        # 4-byte Reload
	movl	-212(%rbp), %esi        # 4-byte Reload
	movl	%ecx, -180(%rbp)        # 4-byte Spill
	movl	%edx, -184(%rbp)        # 4-byte Spill
	movl	%esi, -188(%rbp)        # 4-byte Spill
	movl	%eax, -192(%rbp)        # 4-byte Spill
	jmp	.LBB6_11
.LBB6_14:                               # %for.end90
                                        #   in Loop: Header=BB6_9 Depth=1
	jmp	.LBB6_15
.LBB6_15:                               # %for.inc91
                                        #   in Loop: Header=BB6_9 Depth=1
	movl	-176(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -172(%rbp)        # 4-byte Spill
	jmp	.LBB6_9
.LBB6_16:                               # %for.end93
	xorl	%eax, %eax
	movl	%eax, -220(%rbp)        # 4-byte Spill
	jmp	.LBB6_17
.LBB6_17:                               # %for.cond94
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_19 Depth 2
	movl	-220(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -224(%rbp)        # 4-byte Spill
	jge	.LBB6_24
# %bb.18:                               # %for.body97
                                        #   in Loop: Header=BB6_17 Depth=1
	xorl	%eax, %eax
	movl	$63, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%eax, %edi
	movl	%edx, -228(%rbp)        # 4-byte Spill
	movl	%esi, -232(%rbp)        # 4-byte Spill
	movl	%ecx, -236(%rbp)        # 4-byte Spill
	movl	%edi, -240(%rbp)        # 4-byte Spill
	movl	%eax, -244(%rbp)        # 4-byte Spill
	jmp	.LBB6_19
.LBB6_19:                               # %for.cond98
                                        #   Parent Loop BB6_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-244(%rbp), %eax        # 4-byte Reload
	movl	-240(%rbp), %ecx        # 4-byte Reload
	movl	-236(%rbp), %edx        # 4-byte Reload
	movl	-232(%rbp), %esi        # 4-byte Reload
	movl	-228(%rbp), %edi        # 4-byte Reload
	cmpl	$0, %edx
	movl	%eax, -248(%rbp)        # 4-byte Spill
	movl	%ecx, -252(%rbp)        # 4-byte Spill
	movl	%edx, -256(%rbp)        # 4-byte Spill
	movl	%esi, -260(%rbp)        # 4-byte Spill
	movl	%edi, -264(%rbp)        # 4-byte Spill
	jl	.LBB6_22
# %bb.20:                               # %for.body101
                                        #   in Loop: Header=BB6_19 Depth=2
	movsd	.LCPI6_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI6_8(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-144(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	movl	-260(%rbp), %edx        # 4-byte Reload
	movslq	%edx, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %edi
	movl	-152(%rbp), %r8d        # 4-byte Reload
	movslq	%r8d, %rcx
	movl	-264(%rbp), %r9d        # 4-byte Reload
	movslq	%r9d, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r10d
	addl	%r10d, %edi
	movsd	-160(%rbp), %xmm2       # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r10d
	movslq	%r10d, %rcx
	movl	-252(%rbp), %r10d       # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %r11d
	sarl	$1, %edi
	sarl	$1, %r11d
	addl	%r11d, %edi
	movsd	-168(%rbp), %xmm1       # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %r11d
	movslq	%r11d, %rcx
	movl	-248(%rbp), %r11d       # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %ebx
	addl	%ebx, %edi
	movl	-224(%rbp), %ebx        # 4-byte Reload
	movslq	%ebx, %rcx
	shlq	$8, %rcx
	movabsq	$y2.fixp, %rsi
	movq	%rsi, %r14
	addq	%rcx, %r14
	movl	-256(%rbp), %r15d       # 4-byte Reload
	movslq	%r15d, %rcx
	movl	%edi, (%r14,%rcx,4)
	movslq	%ebx, %rcx
	shlq	$8, %rcx
	movabsq	$imgIn.fixp, %r14
	addq	%rcx, %r14
	movslq	%r15d, %rcx
	movl	(%r14,%rcx,4), %edi
	movslq	%ebx, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rsi
	movslq	%r15d, %rcx
	movl	(%rsi,%rcx,4), %r12d
	movl	%edi, -268(%rbp)        # 4-byte Spill
	movl	%r12d, -272(%rbp)       # 4-byte Spill
# %bb.21:                               # %for.inc121
                                        #   in Loop: Header=BB6_19 Depth=2
	movl	-256(%rbp), %eax        # 4-byte Reload
	addl	$-1, %eax
	movl	-260(%rbp), %ecx        # 4-byte Reload
	movl	-268(%rbp), %edx        # 4-byte Reload
	movl	-272(%rbp), %esi        # 4-byte Reload
	movl	-252(%rbp), %edi        # 4-byte Reload
	movl	%ecx, -228(%rbp)        # 4-byte Spill
	movl	%edx, -232(%rbp)        # 4-byte Spill
	movl	%eax, -236(%rbp)        # 4-byte Spill
	movl	%esi, -240(%rbp)        # 4-byte Spill
	movl	%edi, -244(%rbp)        # 4-byte Spill
	jmp	.LBB6_19
.LBB6_22:                               # %for.end122
                                        #   in Loop: Header=BB6_17 Depth=1
	jmp	.LBB6_23
.LBB6_23:                               # %for.inc123
                                        #   in Loop: Header=BB6_17 Depth=1
	movl	-224(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -220(%rbp)        # 4-byte Spill
	jmp	.LBB6_17
.LBB6_24:                               # %for.end125
	xorl	%eax, %eax
	movl	%eax, -276(%rbp)        # 4-byte Spill
	jmp	.LBB6_25
.LBB6_25:                               # %for.cond126
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_27 Depth 2
	movl	-276(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -280(%rbp)        # 4-byte Spill
	jge	.LBB6_32
# %bb.26:                               # %for.body129
                                        #   in Loop: Header=BB6_25 Depth=1
	xorl	%eax, %eax
	movl	%eax, -284(%rbp)        # 4-byte Spill
	jmp	.LBB6_27
.LBB6_27:                               # %for.cond130
                                        #   Parent Loop BB6_25 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-284(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -288(%rbp)        # 4-byte Spill
	jge	.LBB6_30
# %bb.28:                               # %for.body133
                                        #   in Loop: Header=BB6_27 Depth=2
	movl	-280(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$_y1.fixp, %rdx
	addq	%rcx, %rdx
	movl	-288(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$y2.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	sarl	$1, %edi
	sarl	$1, %r8d
	addl	%r8d, %edi
	movslq	%edi, %rcx
	shlq	$0, %rcx
	movl	%ecx, %edi
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$imgOut.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	%edi, (%rdx,%rcx,4)
# %bb.29:                               # %for.inc148
                                        #   in Loop: Header=BB6_27 Depth=2
	movl	-288(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -284(%rbp)        # 4-byte Spill
	jmp	.LBB6_27
.LBB6_30:                               # %for.end150
                                        #   in Loop: Header=BB6_25 Depth=1
	jmp	.LBB6_31
.LBB6_31:                               # %for.inc151
                                        #   in Loop: Header=BB6_25 Depth=1
	movl	-280(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -276(%rbp)        # 4-byte Spill
	jmp	.LBB6_25
.LBB6_32:                               # %for.end153
	xorl	%eax, %eax
	movl	%eax, -292(%rbp)        # 4-byte Spill
	jmp	.LBB6_33
.LBB6_33:                               # %for.cond154
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_35 Depth 2
	movl	-292(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -296(%rbp)        # 4-byte Spill
	jge	.LBB6_40
# %bb.34:                               # %for.body157
                                        #   in Loop: Header=BB6_33 Depth=1
	xorl	%eax, %eax
	movl	%eax, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%ecx, -300(%rbp)        # 4-byte Spill
	movl	%edx, -304(%rbp)        # 4-byte Spill
	movl	%esi, -308(%rbp)        # 4-byte Spill
	movl	%eax, -312(%rbp)        # 4-byte Spill
	jmp	.LBB6_35
.LBB6_35:                               # %for.cond158
                                        #   Parent Loop BB6_33 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-312(%rbp), %eax        # 4-byte Reload
	movl	-308(%rbp), %ecx        # 4-byte Reload
	movl	-304(%rbp), %edx        # 4-byte Reload
	movl	-300(%rbp), %esi        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -316(%rbp)        # 4-byte Spill
	movl	%ecx, -320(%rbp)        # 4-byte Spill
	movl	%edx, -324(%rbp)        # 4-byte Spill
	movl	%esi, -328(%rbp)        # 4-byte Spill
	jge	.LBB6_38
# %bb.36:                               # %for.body161
                                        #   in Loop: Header=BB6_35 Depth=2
	movsd	.LCPI6_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI6_9(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-316(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$imgOut.fixp, %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-296(%rbp), %edi        # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movaps	%xmm0, %xmm2
	movsd	-112(%rbp), %xmm3       # 8-byte Reload
                                        # xmm3 = mem[0],zero
	mulsd	%xmm3, %xmm2
	cvttsd2si	%xmm2, %r9d
	movslq	%r9d, %rcx
	movslq	%r8d, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r8d
	movl	-140(%rbp), %r9d        # 4-byte Reload
	movslq	%r9d, %rcx
	movl	-320(%rbp), %r10d       # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %r11d
	shll	$1, %r8d
	sarl	$1, %r11d
	addl	%r11d, %r8d
	movsd	-160(%rbp), %xmm2       # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r11d
	movslq	%r11d, %rcx
	movl	-324(%rbp), %r11d       # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %ebx
	addl	%ebx, %r8d
	movsd	-168(%rbp), %xmm1       # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %ebx
	movslq	%ebx, %rcx
	movl	-328(%rbp), %ebx        # 4-byte Reload
	movslq	%ebx, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r14d
	addl	%r14d, %r8d
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$_y1.fixp, %rsi
	movq	%rsi, %r15
	addq	%rcx, %r15
	movslq	%edi, %rcx
	movl	%r8d, (%r15,%rcx,4)
	movslq	%eax, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	movslq	%eax, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r14d
	movl	%r8d, -332(%rbp)        # 4-byte Spill
	movl	%r14d, -336(%rbp)       # 4-byte Spill
# %bb.37:                               # %for.inc185
                                        #   in Loop: Header=BB6_35 Depth=2
	movl	-316(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	-324(%rbp), %ecx        # 4-byte Reload
	movl	-336(%rbp), %edx        # 4-byte Reload
	movl	-332(%rbp), %esi        # 4-byte Reload
	movl	%ecx, -300(%rbp)        # 4-byte Spill
	movl	%edx, -304(%rbp)        # 4-byte Spill
	movl	%esi, -308(%rbp)        # 4-byte Spill
	movl	%eax, -312(%rbp)        # 4-byte Spill
	jmp	.LBB6_35
.LBB6_38:                               # %for.end187
                                        #   in Loop: Header=BB6_33 Depth=1
	jmp	.LBB6_39
.LBB6_39:                               # %for.inc188
                                        #   in Loop: Header=BB6_33 Depth=1
	movl	-296(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -292(%rbp)        # 4-byte Spill
	jmp	.LBB6_33
.LBB6_40:                               # %for.end190
	xorl	%eax, %eax
	movl	%eax, -340(%rbp)        # 4-byte Spill
	jmp	.LBB6_41
.LBB6_41:                               # %for.cond191
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_43 Depth 2
	movl	-340(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -344(%rbp)        # 4-byte Spill
	jge	.LBB6_48
# %bb.42:                               # %for.body194
                                        #   in Loop: Header=BB6_41 Depth=1
	xorl	%eax, %eax
	movl	$63, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%eax, %edi
	movl	%ecx, -348(%rbp)        # 4-byte Spill
	movl	%edx, -352(%rbp)        # 4-byte Spill
	movl	%esi, -356(%rbp)        # 4-byte Spill
	movl	%edi, -360(%rbp)        # 4-byte Spill
	movl	%eax, -364(%rbp)        # 4-byte Spill
	jmp	.LBB6_43
.LBB6_43:                               # %for.cond195
                                        #   Parent Loop BB6_41 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-364(%rbp), %eax        # 4-byte Reload
	movl	-360(%rbp), %ecx        # 4-byte Reload
	movl	-356(%rbp), %edx        # 4-byte Reload
	movl	-352(%rbp), %esi        # 4-byte Reload
	movl	-348(%rbp), %edi        # 4-byte Reload
	cmpl	$0, %edi
	movl	%eax, -368(%rbp)        # 4-byte Spill
	movl	%ecx, -372(%rbp)        # 4-byte Spill
	movl	%edx, -376(%rbp)        # 4-byte Spill
	movl	%esi, -380(%rbp)        # 4-byte Spill
	movl	%edi, -384(%rbp)        # 4-byte Spill
	jl	.LBB6_46
# %bb.44:                               # %for.body198
                                        #   in Loop: Header=BB6_43 Depth=2
	movsd	.LCPI6_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI6_8(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-144(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	movl	-380(%rbp), %edx        # 4-byte Reload
	movslq	%edx, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %edi
	movl	-152(%rbp), %r8d        # 4-byte Reload
	movslq	%r8d, %rcx
	movl	-376(%rbp), %r9d        # 4-byte Reload
	movslq	%r9d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %r10d
	addl	%r10d, %edi
	movsd	-160(%rbp), %xmm2       # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r10d
	movslq	%r10d, %rcx
	movl	-372(%rbp), %r10d       # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %r11d
	sarl	$1, %edi
	sarl	$1, %r11d
	addl	%r11d, %edi
	movsd	-168(%rbp), %xmm1       # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %r11d
	movslq	%r11d, %rcx
	movl	-368(%rbp), %r11d       # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %ebx
	addl	%ebx, %edi
	movl	-384(%rbp), %ebx        # 4-byte Reload
	movslq	%ebx, %rcx
	shlq	$8, %rcx
	movabsq	$y2.fixp, %rsi
	movq	%rsi, %r14
	addq	%rcx, %r14
	movl	-344(%rbp), %r15d       # 4-byte Reload
	movslq	%r15d, %rcx
	movl	%edi, (%r14,%rcx,4)
	movslq	%ebx, %rcx
	shlq	$8, %rcx
	movabsq	$imgOut.fixp, %r14
	addq	%rcx, %r14
	movslq	%r15d, %rcx
	movl	(%r14,%rcx,4), %edi
	movslq	%ebx, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rsi
	movslq	%r15d, %rcx
	movl	(%rsi,%rcx,4), %r12d
	movl	%edi, -388(%rbp)        # 4-byte Spill
	movl	%r12d, -392(%rbp)       # 4-byte Spill
# %bb.45:                               # %for.inc218
                                        #   in Loop: Header=BB6_43 Depth=2
	movl	-384(%rbp), %eax        # 4-byte Reload
	addl	$-1, %eax
	movl	-388(%rbp), %ecx        # 4-byte Reload
	movl	-380(%rbp), %edx        # 4-byte Reload
	movl	-392(%rbp), %esi        # 4-byte Reload
	movl	-372(%rbp), %edi        # 4-byte Reload
	movl	%eax, -348(%rbp)        # 4-byte Spill
	movl	%ecx, -352(%rbp)        # 4-byte Spill
	movl	%edx, -356(%rbp)        # 4-byte Spill
	movl	%esi, -360(%rbp)        # 4-byte Spill
	movl	%edi, -364(%rbp)        # 4-byte Spill
	jmp	.LBB6_43
.LBB6_46:                               # %for.end220
                                        #   in Loop: Header=BB6_41 Depth=1
	jmp	.LBB6_47
.LBB6_47:                               # %for.inc221
                                        #   in Loop: Header=BB6_41 Depth=1
	movl	-344(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -340(%rbp)        # 4-byte Spill
	jmp	.LBB6_41
.LBB6_48:                               # %for.end223
	xorl	%eax, %eax
	movl	%eax, -396(%rbp)        # 4-byte Spill
	jmp	.LBB6_49
.LBB6_49:                               # %for.cond224
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_51 Depth 2
	movl	-396(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -400(%rbp)        # 4-byte Spill
	jge	.LBB6_56
# %bb.50:                               # %for.body227
                                        #   in Loop: Header=BB6_49 Depth=1
	xorl	%eax, %eax
	movl	%eax, -404(%rbp)        # 4-byte Spill
	jmp	.LBB6_51
.LBB6_51:                               # %for.cond228
                                        #   Parent Loop BB6_49 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-404(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -408(%rbp)        # 4-byte Spill
	jge	.LBB6_54
# %bb.52:                               # %for.body231
                                        #   in Loop: Header=BB6_51 Depth=2
	movl	-400(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$_y1.fixp, %rdx
	addq	%rcx, %rdx
	movl	-408(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$y2.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	sarl	$1, %edi
	sarl	$1, %r8d
	addl	%r8d, %edi
	movslq	%edi, %rcx
	shlq	$0, %rcx
	movl	%ecx, %edi
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$imgOut.fixp, %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	%edi, (%rdx,%rcx,4)
# %bb.53:                               # %for.inc246
                                        #   in Loop: Header=BB6_51 Depth=2
	movl	-408(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -404(%rbp)        # 4-byte Spill
	jmp	.LBB6_51
.LBB6_54:                               # %for.end248
                                        #   in Loop: Header=BB6_49 Depth=1
	jmp	.LBB6_55
.LBB6_55:                               # %for.inc249
                                        #   in Loop: Header=BB6_49 Depth=1
	movl	-400(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -396(%rbp)        # 4-byte Spill
	jmp	.LBB6_49
.LBB6_56:                               # %for.end251
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	movl	%eax, -412(%rbp)        # 4-byte Spill
.LBB6_57:                               # %for.cond252
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_59 Depth 2
	movl	-412(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -416(%rbp)        # 4-byte Spill
	jge	.LBB6_66
# %bb.58:                               # %for.body255
                                        #   in Loop: Header=BB6_57 Depth=1
	xorl	%eax, %eax
	movl	%eax, -420(%rbp)        # 4-byte Spill
	jmp	.LBB6_59
.LBB6_59:                               # %for.cond256
                                        #   Parent Loop BB6_57 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-420(%rbp), %eax        # 4-byte Reload
	cmpl	$64, %eax
	movl	%eax, -424(%rbp)        # 4-byte Spill
	jge	.LBB6_64
# %bb.60:                               # %for.body259
                                        #   in Loop: Header=BB6_59 Depth=2
	movl	-416(%rbp), %eax        # 4-byte Reload
	shll	$6, %eax
	movl	-424(%rbp), %ecx        # 4-byte Reload
	addl	%ecx, %eax
	cltd
	movl	$20, %esi
	idivl	%esi
	cmpl	$0, %edx
	jne	.LBB6_62
# %bb.61:                               # %if.then
                                        #   in Loop: Header=BB6_59 Depth=2
	movq	stdout, %rdi
	movabsq	$.L.str.6, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -428(%rbp)        # 4-byte Spill
.LBB6_62:                               # %if.end
                                        #   in Loop: Header=BB6_59 Depth=2
	movsd	.LCPI6_7(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-416(%rbp), %eax        # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	movabsq	$imgOut.fixp, %rdx
	addq	%rcx, %rdx
	movl	-424(%rbp), %esi        # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	cvtsi2sdl	%r8d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.7, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -432(%rbp)        # 4-byte Spill
# %bb.63:                               # %for.inc271
                                        #   in Loop: Header=BB6_59 Depth=2
	movl	-424(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -420(%rbp)        # 4-byte Spill
	jmp	.LBB6_59
.LBB6_64:                               # %for.end273
                                        #   in Loop: Header=BB6_57 Depth=1
	jmp	.LBB6_65
.LBB6_65:                               # %for.inc274
                                        #   in Loop: Header=BB6_57 Depth=1
	movl	-416(%rbp), %eax        # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -412(%rbp)        # 4-byte Spill
	jmp	.LBB6_57
.LBB6_66:                               # %for.end276
	xorl	%eax, %eax
	addq	$400, %rsp              # imm = 0x190
	popq	%rbx
	popq	%r12
	popq	%r14
	popq	%r15
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

	.type	imgIn,@object           # @imgIn
	.comm	imgIn,32768,16
	.type	_y1,@object             # @_y1
	.comm	_y1,32768,16
	.type	y2,@object              # @y2
	.comm	y2,32768,16
	.type	imgOut,@object          # @imgOut
	.comm	imgOut,32768,16
	.type	.L.str.6,@object        # @.str.6
.L.str.6:
	.asciz	"\n"
	.size	.L.str.6, 2

	.type	.L.str.7,@object        # @.str.7
.L.str.7:
	.asciz	"%.16lf "
	.size	.L.str.7, 8

	.type	imgIn.fixp,@object      # @imgIn.fixp
	.comm	imgIn.fixp,16384,16
	.type	_y1.fixp,@object        # @_y1.fixp
	.comm	_y1.fixp,16384,16
	.type	y2.fixp,@object         # @y2.fixp
	.comm	y2.fixp,16384,16
	.type	imgOut.fixp,@object     # @imgOut.fixp
	.comm	imgOut.fixp,16384,16

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
	.addrsig_sym exp
	.addrsig_sym pow
	.addrsig_sym time_that_takes
	.addrsig_sym stderr
	.addrsig_sym imgIn
	.addrsig_sym _y1
	.addrsig_sym y2
	.addrsig_sym imgOut
	.addrsig_sym stdout
	.addrsig_sym imgIn.fixp
	.addrsig_sym _y1.fixp
	.addrsig_sym y2.fixp
	.addrsig_sym imgOut.fixp
