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
	xorl	%eax, %eax
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
	movq	%rax, time_that_takes(%rip)
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
	subq	time_that_takes(%rip), %rax
	movq	%rax, time_that_takes(%rip)
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
	movq	time_that_takes(%rip), %rax
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
	movq	stderr(%rip), %rdi
	movq	time_that_takes(%rip), %rdx
	movl	$.L.str, %esi
	xorl	%eax, %eax
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	jmp	fprintf                 # TAILCALL
.Lfunc_end4:
	.size	TIMING_CPUCLOCK_PRINT, .Lfunc_end4-TIMING_CPUCLOCK_PRINT
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI5_0:
	.quad	4530621225134718976     # double 7.62939453125E-6
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
	pushq	%r13
	pushq	%r12
	pushq	%rbx
	subq	$512056, %rsp           # imm = 0x7D038
	.cfi_offset %rbx, -56
	.cfi_offset %r12, -48
	.cfi_offset %r13, -40
	.cfi_offset %r14, -32
	.cfi_offset %r15, -24
	callq	TIMING_CPUCLOCK_START
	movabsq	$6710886400, %r8        # imm = 0x190000000
	leaq	-512096(%rbp), %r9
	leaq	-256096(%rbp), %r11
	xorl	%r10d, %r10d
	movl	$3435973837, %r12d      # imm = 0xCCCCCCCD
	.p2align	4, 0x90
.LBB5_1:                                # %for.cond7.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_2 Depth 2
                                        #       Child Loop BB5_3 Depth 3
	movq	%r11, %rdx
	movq	%r9, %rcx
	movq	%r8, %r14
	xorl	%r15d, %r15d
	.p2align	4, 0x90
.LBB5_2:                                # %for.cond10.preheader
                                        #   Parent Loop BB5_1 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_3 Depth 3
	movq	%r14, %rsi
	xorl	%ebx, %ebx
	.p2align	4, 0x90
.LBB5_3:                                # %for.body12
                                        #   Parent Loop BB5_1 Depth=1
                                        #     Parent Loop BB5_2 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movq	%rsi, %rax
	shrq	$3, %rax
	movl	%eax, %eax
	imulq	%r12, %rax
	movq	%rax, %rdi
	shrq	$41, %rdi
	shrq	$40, %rax
	movl	%eax, (%rcx,%rbx,4)
	movl	%edi, (%rdx,%rbx,4)
	addq	$1, %rbx
	addq	$-167772160, %rsi       # imm = 0xF6000000
	cmpq	$40, %rbx
	jne	.LBB5_3
# %bb.4:                                # %for.inc25
                                        #   in Loop: Header=BB5_2 Depth=2
	addq	$1, %r15
	addq	$167772160, %r14        # imm = 0xA000000
	addq	$160, %rcx
	addq	$160, %rdx
	cmpq	$40, %r15
	jne	.LBB5_2
# %bb.5:                                # %for.inc28
                                        #   in Loop: Header=BB5_1 Depth=1
	addq	$1, %r10
	addq	$167772160, %r8         # imm = 0xA000000
	addq	$6400, %r9              # imm = 0x1900
	addq	$6400, %r11             # imm = 0x1900
	cmpq	$40, %r10
	jne	.LBB5_1
# %bb.6:                                # %for.cond35.preheader.preheader
	movl	$1, %eax
	.p2align	4, 0x90
.LBB5_7:                                # %for.cond35.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_8 Depth 2
                                        #       Child Loop BB5_9 Depth 3
                                        #         Child Loop BB5_10 Depth 4
                                        #     Child Loop BB5_14 Depth 2
                                        #       Child Loop BB5_15 Depth 3
                                        #         Child Loop BB5_16 Depth 4
	movl	%eax, -48(%rbp)         # 4-byte Spill
	movl	$1, %r15d
	leaq	-505532(%rbp), %r12
	leaq	-243132(%rbp), %r11
	.p2align	4, 0x90
.LBB5_8:                                # %for.cond39.preheader
                                        #   Parent Loop BB5_7 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_9 Depth 3
                                        #         Child Loop BB5_10 Depth 4
	leaq	1(%r15), %rax
	movq	%rax, -56(%rbp)         # 8-byte Spill
	movq	%r12, -64(%rbp)         # 8-byte Spill
	movq	%r11, %r13
	movl	$1, %r14d
	.p2align	4, 0x90
.LBB5_9:                                # %for.cond43.preheader
                                        #   Parent Loop BB5_7 Depth=1
                                        #     Parent Loop BB5_8 Depth=2
                                        # =>    This Loop Header: Depth=3
                                        #         Child Loop BB5_10 Depth 4
	imulq	$6400, %r15, %rdx       # imm = 0x1900
	addq	%rbp, %rdx
	addq	$-256096, %rdx          # imm = 0xFFFC17A0
	leaq	(%r14,%r14,4), %rdi
	leaq	1(%r14), %r14
	shlq	$5, %rdi
	movl	4(%rdi,%rdx), %edx
	xorl	%edi, %edi
	.p2align	4, 0x90
.LBB5_10:                               # %for.body46
                                        #   Parent Loop BB5_7 Depth=1
                                        #     Parent Loop BB5_8 Depth=2
                                        #       Parent Loop BB5_9 Depth=3
                                        # =>      This Inner Loop Header: Depth=4
	movl	(%r13,%rdi,4), %r8d
	leal	(,%rdx,4), %r9d
	addl	%r8d, %r8d
	subl	%r9d, %r8d
	movl	-12800(%r13,%rdi,4), %r10d
	leal	(%r8,%r10,2), %ecx
	movl	-6240(%r13,%rdi,4), %eax
	addl	%eax, %eax
	subl	%r9d, %eax
	movl	-6560(%r13,%rdi,4), %ebx
	leal	(%rax,%rbx,2), %eax
	sarl	$2, %ecx
	sarl	$2, %eax
	addl	%ecx, %eax
	movl	-6396(%r13,%rdi,4), %ecx
	leal	(%rcx,%rcx), %ebx
	subl	%r9d, %ebx
	movl	-6404(%r13,%rdi,4), %esi
	leal	(%rbx,%rsi,2), %esi
	sarl	%eax
	sarl	$3, %esi
	leal	(%rsi,%rdx,2), %edx
	addl	%eax, %edx
	movl	%edx, (%r12,%rdi,4)
	addq	$1, %rdi
	movl	%ecx, %edx
	cmpq	$38, %rdi
	jne	.LBB5_10
# %bb.11:                               # %for.inc137
                                        #   in Loop: Header=BB5_9 Depth=3
	addq	$160, %r13
	addq	$160, %r12
	cmpq	$39, %r14
	jne	.LBB5_9
# %bb.12:                               # %for.inc140
                                        #   in Loop: Header=BB5_8 Depth=2
	addq	$6400, %r11             # imm = 0x1900
	movq	-64(%rbp), %r12         # 8-byte Reload
	addq	$6400, %r12             # imm = 0x1900
	movq	-56(%rbp), %rax         # 8-byte Reload
	movq	%rax, %r15
	cmpq	$39, %rax
	jne	.LBB5_8
# %bb.13:                               # %for.cond147.preheader.preheader
                                        #   in Loop: Header=BB5_7 Depth=1
	movl	$1, %r8d
	leaq	-249532(%rbp), %r12
	leaq	-499132(%rbp), %r13
	.p2align	4, 0x90
.LBB5_14:                               # %for.cond147.preheader
                                        #   Parent Loop BB5_7 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_15 Depth 3
                                        #         Child Loop BB5_16 Depth 4
	leaq	1(%r8), %r15
	movq	%r12, %r10
	movq	%r13, %r11
	movl	$1, %r9d
	.p2align	4, 0x90
.LBB5_15:                               # %for.cond151.preheader
                                        #   Parent Loop BB5_7 Depth=1
                                        #     Parent Loop BB5_14 Depth=2
                                        # =>    This Loop Header: Depth=3
                                        #         Child Loop BB5_16 Depth 4
	imulq	$6400, %r8, %rsi        # imm = 0x1900
	addq	%rbp, %rsi
	addq	$-512096, %rsi          # imm = 0xFFF82FA0
	leaq	(%r9,%r9,4), %rbx
	leaq	1(%r9), %r9
	shlq	$5, %rbx
	movl	4(%rbx,%rsi), %esi
	xorl	%ebx, %ebx
	.p2align	4, 0x90
.LBB5_16:                               # %for.body154
                                        #   Parent Loop BB5_7 Depth=1
                                        #     Parent Loop BB5_14 Depth=2
                                        #       Parent Loop BB5_15 Depth=3
                                        # =>      This Inner Loop Header: Depth=4
	movl	(%r11,%rbx,4), %ecx
	sarl	$2, %ecx
	sarl	%esi
	subl	%esi, %ecx
	movl	-12800(%r11,%rbx,4), %eax
	sarl	$2, %eax
	addl	%ecx, %eax
	sarl	%eax
	movl	-6240(%r11,%rbx,4), %ecx
	sarl	$2, %ecx
	subl	%esi, %ecx
	movl	-6560(%r11,%rbx,4), %edi
	sarl	$2, %edi
	addl	%ecx, %edi
	sarl	%edi
	addl	%eax, %edi
	movl	-6396(%r11,%rbx,4), %eax
	movl	%eax, %ecx
	sarl	$2, %ecx
	subl	%esi, %ecx
	movl	-6404(%r11,%rbx,4), %edx
	sarl	$2, %edx
	addl	%ecx, %edx
	sarl	%edi
	sarl	$2, %edx
	addl	%esi, %edx
	addl	%edi, %edx
	movl	%edx, (%r10,%rbx,4)
	addq	$1, %rbx
	movl	%eax, %esi
	cmpq	$38, %rbx
	jne	.LBB5_16
# %bb.17:                               # %for.inc245
                                        #   in Loop: Header=BB5_15 Depth=3
	addq	$160, %r11
	addq	$160, %r10
	cmpq	$39, %r9
	jne	.LBB5_15
# %bb.18:                               # %for.inc248
                                        #   in Loop: Header=BB5_14 Depth=2
	addq	$6400, %r13             # imm = 0x1900
	addq	$6400, %r12             # imm = 0x1900
	movq	%r15, %r8
	cmpq	$39, %r15
	jne	.LBB5_14
# %bb.19:                               # %for.inc251
                                        #   in Loop: Header=BB5_7 Depth=1
	movl	-48(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	cmpl	$101, %eax
	jne	.LBB5_7
# %bb.20:                               # %for.cond258.preheader.preheader
	xorl	%eax, %eax
	leaq	-256096(%rbp), %r15
	movl	$3435973837, %ebx       # imm = 0xCCCCCCCD
	xorl	%r12d, %r12d
	xorl	%edx, %edx
	.p2align	4, 0x90
.LBB5_21:                               # %for.cond258.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_22 Depth 2
                                        #       Child Loop BB5_23 Depth 3
	movq	%rdx, -80(%rbp)         # 8-byte Spill
	movq	%r15, -88(%rbp)         # 8-byte Spill
	movq	%rax, -96(%rbp)         # 8-byte Spill
	movl	%eax, %r14d
	movl	%r12d, -68(%rbp)        # 4-byte Spill
	xorl	%eax, %eax
	.p2align	4, 0x90
.LBB5_22:                               # %for.cond262.preheader
                                        #   Parent Loop BB5_21 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_23 Depth 3
	movq	%rax, -48(%rbp)         # 8-byte Spill
	movl	%r14d, -64(%rbp)        # 4-byte Spill
	movl	%r12d, -56(%rbp)        # 4-byte Spill
	xorl	%r13d, %r13d
	.p2align	4, 0x90
.LBB5_23:                               # %for.body265
                                        #   Parent Loop BB5_21 Depth=1
                                        #     Parent Loop BB5_22 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	%r14d, %eax
	imulq	%rbx, %rax
	shrq	$36, %rax
	leal	(%rax,%rax,4), %eax
	shll	$2, %eax
	addl	%r12d, %eax
	jne	.LBB5_25
# %bb.24:                               # %if.then
                                        #   in Loop: Header=BB5_23 Depth=3
	movq	stdout(%rip), %rsi
	movl	$10, %edi
	callq	fputc
.LBB5_25:                               # %if.end
                                        #   in Loop: Header=BB5_23 Depth=3
	movq	stdout(%rip), %rdi
	xorps	%xmm0, %xmm0
	cvtsi2sdl	(%r15,%r13,4), %xmm0
	mulsd	.LCPI5_0(%rip), %xmm0
	movl	$.L.str.5, %esi
	movb	$1, %al
	callq	fprintf
	addq	$1, %r13
	addl	$-1, %r12d
	addl	$1, %r14d
	cmpq	$40, %r13
	jne	.LBB5_23
# %bb.26:                               # %for.inc283
                                        #   in Loop: Header=BB5_22 Depth=2
	movq	-48(%rbp), %rax         # 8-byte Reload
	addq	$1, %rax
	movl	-56(%rbp), %r12d        # 4-byte Reload
	addl	$-40, %r12d
	movl	-64(%rbp), %r14d        # 4-byte Reload
	addl	$40, %r14d
	addq	$160, %r15
	cmpq	$40, %rax
	jne	.LBB5_22
# %bb.27:                               # %for.inc286
                                        #   in Loop: Header=BB5_21 Depth=1
	movq	-80(%rbp), %rdx         # 8-byte Reload
	addq	$1, %rdx
	movl	-68(%rbp), %r12d        # 4-byte Reload
	addl	$-1600, %r12d           # imm = 0xF9C0
	movq	-96(%rbp), %rax         # 8-byte Reload
	addl	$1600, %eax             # imm = 0x640
	movq	-88(%rbp), %r15         # 8-byte Reload
	addq	$6400, %r15             # imm = 0x1900
	cmpq	$40, %rdx
	jne	.LBB5_21
# %bb.28:                               # %for.end288
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	addq	$512056, %rsp           # imm = 0x7D038
	popq	%rbx
	popq	%r12
	popq	%r13
	popq	%r14
	popq	%r15
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

	.type	.L.str.5,@object        # @.str.5
.L.str.5:
	.asciz	"%0.16lf "
	.size	.L.str.5, 9


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
