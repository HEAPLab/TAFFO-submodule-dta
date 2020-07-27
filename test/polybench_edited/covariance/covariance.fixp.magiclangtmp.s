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
	.quad	4458563631096791040     # double 1.1641532182693481E-10
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
	subq	$96472, %rsp            # imm = 0x178D8
	.cfi_offset %rbx, -56
	.cfi_offset %r12, -48
	.cfi_offset %r13, -40
	.cfi_offset %r14, -32
	.cfi_offset %r15, -24
	callq	TIMING_CPUCLOCK_START
	leaq	-32512(%rbp), %rdi
	xorl	%r11d, %r11d
	movabsq	$-3689348814741910323, %r8 # imm = 0xCCCCCCCCCCCCCCCD
	movabsq	$1125899906842624, %r9  # imm = 0x4000000000000
	movabsq	$2251799813685248, %r10 # imm = 0x8000000000000
	xorl	%r15d, %r15d
	xorl	%r14d, %r14d
	.p2align	4, 0x90
.LBB5_1:                                # %for.cond9.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_2 Depth 2
	movl	$1, %ebx
	xorl	%ecx, %ecx
	.p2align	4, 0x90
.LBB5_2:                                # %for.body12
                                        #   Parent Loop BB5_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movq	%rcx, %rax
	mulq	%r8
	movq	%rdx, %rsi
	shrq	$38, %rsi
	shrl	%esi
	andl	$16777215, %esi         # imm = 0xFFFFFF
	leaq	(%r15,%rcx), %rax
	mulq	%r8
	movl	%esi, -4(%rdi,%rbx,4)
	shrq	$38, %rdx
	shrl	%edx
	andl	$16777215, %edx         # imm = 0xFFFFFF
	movl	%edx, (%rdi,%rbx,4)
	addq	%r11, %rcx
	addq	$2, %rbx
	cmpq	$81, %rbx
	jne	.LBB5_2
# %bb.3:                                # %for.inc17
                                        #   in Loop: Header=BB5_1 Depth=1
	addq	$1, %r14
	addq	%r9, %r15
	addq	%r10, %r11
	addq	$320, %rdi              # imm = 0x140
	cmpq	$100, %r14
	jne	.LBB5_1
# %bb.4:                                # %for.body23.preheader
	leaq	-32512(%rbp), %rax
	xorl	%ecx, %ecx
	.p2align	4, 0x90
.LBB5_5:                                # %for.body23
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_6 Depth 2
	movl	$0, -512(%rbp,%rcx,4)
	xorl	%edx, %edx
	xorl	%esi, %esi
	.p2align	4, 0x90
.LBB5_6:                                # %for.body29
                                        #   Parent Loop BB5_5 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	(%rax,%rdx), %edi
	movl	320(%rax,%rdx), %ebx
	leal	(%rsi,%rdi,2), %esi
	leal	(%rsi,%rbx,2), %esi
	movl	640(%rax,%rdx), %edi
	leal	(%rsi,%rdi,2), %esi
	movl	960(%rax,%rdx), %edi
	leal	(%rsi,%rdi,2), %esi
	movl	1280(%rax,%rdx), %edi
	leal	(%rsi,%rdi,2), %esi
	addq	$1600, %rdx             # imm = 0x640
	cmpq	$32000, %rdx            # imm = 0x7D00
	jne	.LBB5_6
# %bb.7:                                # %for.end38
                                        #   in Loop: Header=BB5_5 Depth=1
	movslq	%esi, %rdx
	imulq	$1374389535, %rdx, %rdx # imm = 0x51EB851F
	movq	%rdx, %rsi
	shrq	$63, %rsi
	sarq	$37, %rdx
	addl	%esi, %edx
	andl	$-2, %edx
	movl	%edx, -512(%rbp,%rcx,4)
	addq	$1, %rcx
	addq	$4, %rax
	cmpq	$80, %rcx
	jne	.LBB5_5
# %bb.8:                                # %vector.ph.preheader
	movdqa	-512(%rbp), %xmm0
	movdqa	-496(%rbp), %xmm1
	movdqa	-480(%rbp), %xmm2
	movdqa	-464(%rbp), %xmm3
	psrad	$1, %xmm0
	movdqa	%xmm0, -80(%rbp)        # 16-byte Spill
	psrad	$1, %xmm1
	movdqa	%xmm1, -64(%rbp)        # 16-byte Spill
	psrad	$1, %xmm2
	movdqa	%xmm2, -192(%rbp)       # 16-byte Spill
	psrad	$1, %xmm3
	movdqa	%xmm3, -176(%rbp)       # 16-byte Spill
	movdqa	-448(%rbp), %xmm0
	psrad	$1, %xmm0
	movdqa	%xmm0, -160(%rbp)       # 16-byte Spill
	movdqa	-432(%rbp), %xmm0
	psrad	$1, %xmm0
	movdqa	%xmm0, -144(%rbp)       # 16-byte Spill
	movdqa	-416(%rbp), %xmm0
	psrad	$1, %xmm0
	movdqa	%xmm0, -128(%rbp)       # 16-byte Spill
	movdqa	-400(%rbp), %xmm0
	psrad	$1, %xmm0
	movdqa	%xmm0, -112(%rbp)       # 16-byte Spill
	movdqa	-384(%rbp), %xmm0
	psrad	$1, %xmm0
	movdqa	%xmm0, -96(%rbp)        # 16-byte Spill
	movdqa	-368(%rbp), %xmm1
	psrad	$1, %xmm1
	movdqa	-352(%rbp), %xmm2
	psrad	$1, %xmm2
	movdqa	-336(%rbp), %xmm3
	psrad	$1, %xmm3
	movdqa	-320(%rbp), %xmm4
	psrad	$1, %xmm4
	movdqa	-304(%rbp), %xmm5
	psrad	$1, %xmm5
	movdqa	-288(%rbp), %xmm6
	psrad	$1, %xmm6
	movdqa	-272(%rbp), %xmm7
	psrad	$1, %xmm7
	movdqa	-256(%rbp), %xmm8
	psrad	$1, %xmm8
	movdqa	-240(%rbp), %xmm9
	psrad	$1, %xmm9
	movdqa	-224(%rbp), %xmm10
	psrad	$1, %xmm10
	movdqa	-208(%rbp), %xmm11
	psrad	$1, %xmm11
	movl	$304, %eax              # imm = 0x130
	.p2align	4, 0x90
.LBB5_9:                                # %vector.ph
                                        # =>This Inner Loop Header: Depth=1
	movdqa	-32816(%rbp,%rax), %xmm12
	psubd	-80(%rbp), %xmm12       # 16-byte Folded Reload
	movdqa	-32800(%rbp,%rax), %xmm13
	movdqa	-32784(%rbp,%rax), %xmm14
	movdqa	-32768(%rbp,%rax), %xmm15
	movdqa	%xmm12, -32816(%rbp,%rax)
	psubd	-64(%rbp), %xmm13       # 16-byte Folded Reload
	movdqa	%xmm13, -32800(%rbp,%rax)
	psubd	-192(%rbp), %xmm14      # 16-byte Folded Reload
	movdqa	%xmm14, -32784(%rbp,%rax)
	psubd	-176(%rbp), %xmm15      # 16-byte Folded Reload
	movdqa	%xmm15, -32768(%rbp,%rax)
	movdqa	-32752(%rbp,%rax), %xmm0
	psubd	-160(%rbp), %xmm0       # 16-byte Folded Reload
	movdqa	%xmm0, -32752(%rbp,%rax)
	movdqa	-32736(%rbp,%rax), %xmm0
	psubd	-144(%rbp), %xmm0       # 16-byte Folded Reload
	movdqa	%xmm0, -32736(%rbp,%rax)
	movdqa	-32720(%rbp,%rax), %xmm0
	psubd	-128(%rbp), %xmm0       # 16-byte Folded Reload
	movdqa	%xmm0, -32720(%rbp,%rax)
	movdqa	-32704(%rbp,%rax), %xmm0
	psubd	-112(%rbp), %xmm0       # 16-byte Folded Reload
	movdqa	%xmm0, -32704(%rbp,%rax)
	movdqa	-32688(%rbp,%rax), %xmm0
	psubd	-96(%rbp), %xmm0        # 16-byte Folded Reload
	movdqa	%xmm0, -32688(%rbp,%rax)
	movdqa	-32672(%rbp,%rax), %xmm0
	psubd	%xmm1, %xmm0
	movdqa	%xmm0, -32672(%rbp,%rax)
	movdqa	-32656(%rbp,%rax), %xmm0
	psubd	%xmm2, %xmm0
	movdqa	%xmm0, -32656(%rbp,%rax)
	movdqa	-32640(%rbp,%rax), %xmm0
	psubd	%xmm3, %xmm0
	movdqa	%xmm0, -32640(%rbp,%rax)
	movdqa	-32624(%rbp,%rax), %xmm0
	psubd	%xmm4, %xmm0
	movdqa	%xmm0, -32624(%rbp,%rax)
	movdqa	-32608(%rbp,%rax), %xmm0
	psubd	%xmm5, %xmm0
	movdqa	%xmm0, -32608(%rbp,%rax)
	movdqa	-32592(%rbp,%rax), %xmm0
	psubd	%xmm6, %xmm0
	movdqa	%xmm0, -32592(%rbp,%rax)
	movdqa	-32576(%rbp,%rax), %xmm0
	psubd	%xmm7, %xmm0
	movdqa	%xmm0, -32576(%rbp,%rax)
	movdqa	-32560(%rbp,%rax), %xmm0
	psubd	%xmm8, %xmm0
	movdqa	%xmm0, -32560(%rbp,%rax)
	movdqa	-32544(%rbp,%rax), %xmm0
	psubd	%xmm9, %xmm0
	movdqa	%xmm0, -32544(%rbp,%rax)
	movdqa	-32528(%rbp,%rax), %xmm0
	psubd	%xmm10, %xmm0
	movdqa	%xmm0, -32528(%rbp,%rax)
	movdqa	-32512(%rbp,%rax), %xmm0
	psubd	%xmm11, %xmm0
	movdqa	%xmm0, -32512(%rbp,%rax)
	addq	$320, %rax              # imm = 0x140
	cmpq	$32304, %rax            # imm = 0x7E30
	jne	.LBB5_9
# %bb.10:                               # %for.body72.lr.ph.preheader
	leaq	-32512(%rbp), %rbx
	xorl	%r9d, %r9d
	movabsq	$-6521576187675094005, %r8 # imm = 0xA57EB50295FAD40B
	.p2align	4, 0x90
.LBB5_11:                               # %for.body72.lr.ph
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_12 Depth 2
                                        #       Child Loop BB5_13 Depth 3
	movq	%rbx, %rsi
	movq	%r9, %r11
	.p2align	4, 0x90
.LBB5_12:                               # %for.body72
                                        #   Parent Loop BB5_11 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_13 Depth 3
	leaq	(%r9,%r9,4), %rax
	shlq	$7, %rax
	addq	%rbp, %rax
	addq	$-96512, %rax           # imm = 0xFFFE8700
	leaq	(%rax,%r11,8), %r10
	movq	$0, (%rax,%r11,8)
	xorl	%eax, %eax
	xorl	%ecx, %ecx
	.p2align	4, 0x90
.LBB5_13:                               # %for.body80
                                        #   Parent Loop BB5_11 Depth=1
                                        #     Parent Loop BB5_12 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movslq	(%rbx,%rax), %rdx
	movslq	(%rsi,%rax), %rdi
	imulq	%rdx, %rdi
	shrq	$30, %rdi
	movslq	%edi, %rdx
	shlq	$29, %rdx
	addq	%rcx, %rdx
	movslq	320(%rbx,%rax), %rcx
	movslq	320(%rsi,%rax), %rdi
	imulq	%rcx, %rdi
	shrq	$30, %rdi
	movslq	%edi, %rcx
	shlq	$29, %rcx
	addq	%rdx, %rcx
	addq	$640, %rax              # imm = 0x280
	cmpq	$32000, %rax            # imm = 0x7D00
	jne	.LBB5_13
# %bb.14:                               # %for.end97
                                        #   in Loop: Header=BB5_12 Depth=2
	movq	%rcx, %rax
	imulq	%r8
	addq	%rcx, %rdx
	movq	%rdx, %rax
	shrq	$63, %rax
	sarq	$6, %rdx
	addq	%rax, %rdx
	andq	$-67108864, %rdx        # imm = 0xFC000000
	movq	%rdx, (%r10)
	leaq	(%r11,%r11,4), %rax
	shlq	$7, %rax
	addq	%rbp, %rax
	addq	$-96512, %rax           # imm = 0xFFFE8700
	movq	%rdx, (%rax,%r9,8)
	addq	$1, %r11
	addq	$4, %rsi
	cmpq	$80, %r11
	jne	.LBB5_12
# %bb.15:                               # %for.inc114
                                        #   in Loop: Header=BB5_11 Depth=1
	addq	$1, %r9
	addq	$4, %rbx
	cmpq	$80, %r9
	jne	.LBB5_11
# %bb.16:                               # %for.cond121.preheader.preheader
	leaq	-96512(%rbp), %r12
	xorl	%eax, %eax
	movl	$3435973837, %r15d      # imm = 0xCCCCCCCD
	xorl	%ebx, %ebx
	xorl	%ecx, %ecx
	.p2align	4, 0x90
.LBB5_17:                               # %for.cond121.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_18 Depth 2
	movq	%rcx, -64(%rbp)         # 8-byte Spill
	movq	%rax, -80(%rbp)         # 8-byte Spill
	movl	%eax, %r14d
	xorl	%r13d, %r13d
	.p2align	4, 0x90
.LBB5_18:                               # %for.body124
                                        #   Parent Loop BB5_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	%r14d, %eax
	imulq	%r15, %rax
	shrq	$36, %rax
	leal	(%rax,%rax,4), %eax
	leal	(%rbx,%rax,4), %eax
	cmpl	%r13d, %eax
	jne	.LBB5_20
# %bb.19:                               # %if.then
                                        #   in Loop: Header=BB5_18 Depth=2
	movq	stdout(%rip), %rsi
	movl	$10, %edi
	callq	fputc
.LBB5_20:                               # %if.end
                                        #   in Loop: Header=BB5_18 Depth=2
	movq	stdout(%rip), %rdi
	xorps	%xmm0, %xmm0
	cvtsi2sdq	(%r12,%r13,8), %xmm0
	mulsd	.LCPI5_0(%rip), %xmm0
	movl	$.L.str.7, %esi
	movb	$1, %al
	callq	fprintf
	addq	$1, %r13
	addl	$1, %r14d
	cmpq	$80, %r13
	jne	.LBB5_18
# %bb.21:                               # %for.inc137
                                        #   in Loop: Header=BB5_17 Depth=1
	movq	-64(%rbp), %rcx         # 8-byte Reload
	addq	$1, %rcx
	addq	$640, %r12              # imm = 0x280
	addl	$-80, %ebx
	movq	-80(%rbp), %rax         # 8-byte Reload
	addl	$80, %eax
	cmpq	$80, %rcx
	jne	.LBB5_17
# %bb.22:                               # %for.end139
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	addq	$96472, %rsp            # imm = 0x178D8
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

	.type	.L.str.7,@object        # @.str.7
.L.str.7:
	.asciz	"%.16lf "
	.size	.L.str.7, 8


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
