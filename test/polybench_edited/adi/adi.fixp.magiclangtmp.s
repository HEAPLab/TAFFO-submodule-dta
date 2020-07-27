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
	.section	.rodata.cst16,"aM",@progbits,16
	.p2align	4               # -- Begin function main
.LCPI5_0:
	.quad	2                       # 0x2
	.quad	3                       # 0x3
.LCPI5_1:
	.long	1374389535              # 0x51eb851f
	.long	1374389535              # 0x51eb851f
	.long	1374389535              # 0x51eb851f
	.long	1374389535              # 0x51eb851f
.LCPI5_2:
	.long	2147483616              # 0x7fffffe0
	.long	2147483616              # 0x7fffffe0
	.long	2147483616              # 0x7fffffe0
	.long	2147483616              # 0x7fffffe0
.LCPI5_3:
	.quad	4                       # 0x4
	.quad	4                       # 0x4
.LCPI5_4:
	.quad	8                       # 0x8
	.quad	8                       # 0x8
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3
.LCPI5_5:
	.quad	4481081629233643520     # double 3.7252902984619141E-9
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
	subq	$640040, %rsp           # imm = 0x9C428
	.cfi_offset %rbx, -56
	.cfi_offset %r12, -48
	.cfi_offset %r13, -40
	.cfi_offset %r14, -32
	.cfi_offset %r15, -24
	callq	TIMING_CPUCLOCK_START
	leaq	-480080(%rbp), %rax
	xorl	%ecx, %ecx
	movl	$1, %edx
	movq	%rdx, %xmm9
	pslldq	$8, %xmm9               # xmm9 = zero,zero,zero,zero,zero,zero,zero,zero,xmm9[0,1,2,3,4,5,6,7]
	movdqa	.LCPI5_0(%rip), %xmm8   # xmm8 = [2,3]
	movdqa	.LCPI5_1(%rip), %xmm2   # xmm2 = [1374389535,1374389535,1374389535,1374389535]
	movdqa	.LCPI5_2(%rip), %xmm10  # xmm10 = [2147483616,2147483616,2147483616,2147483616]
	movdqa	.LCPI5_3(%rip), %xmm11  # xmm11 = [4,4]
	movdqa	.LCPI5_4(%rip), %xmm5   # xmm5 = [8,8]
	.p2align	4, 0x90
.LBB5_1:                                # %vector.ph
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_2 Depth 2
	leaq	200(%rcx), %rdx
	movq	%rdx, %xmm1
	pshufd	$68, %xmm1, %xmm4       # xmm4 = xmm1[0,1,0,1]
	movl	$4, %edx
	movdqa	%xmm9, %xmm7
	movdqa	%xmm8, %xmm1
	.p2align	4, 0x90
.LBB5_2:                                # %vector.body
                                        #   Parent Loop BB5_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movdqa	%xmm4, %xmm6
	psubq	%xmm7, %xmm6
	movdqa	%xmm4, %xmm0
	psubq	%xmm1, %xmm0
	shufps	$136, %xmm0, %xmm6      # xmm6 = xmm6[0,2],xmm0[0,2]
	pslld	$23, %xmm6
	pshufd	$245, %xmm6, %xmm0      # xmm0 = xmm6[1,1,3,3]
	pmuludq	%xmm2, %xmm6
	pshufd	$237, %xmm6, %xmm6      # xmm6 = xmm6[1,3,2,3]
	pmuludq	%xmm2, %xmm0
	pshufd	$237, %xmm0, %xmm0      # xmm0 = xmm0[1,3,2,3]
	punpckldq	%xmm0, %xmm6    # xmm6 = xmm6[0],xmm0[0],xmm6[1],xmm0[1]
	psrld	$1, %xmm6
	pand	%xmm10, %xmm6
	movdqa	%xmm6, -16(%rax,%rdx,4)
	movdqa	%xmm1, %xmm0
	paddq	%xmm11, %xmm0
	movdqa	%xmm7, %xmm6
	paddq	%xmm11, %xmm6
	movdqa	%xmm4, %xmm3
	psubq	%xmm6, %xmm3
	movdqa	%xmm4, %xmm6
	psubq	%xmm0, %xmm6
	shufps	$136, %xmm6, %xmm3      # xmm3 = xmm3[0,2],xmm6[0,2]
	pslld	$23, %xmm3
	pshufd	$245, %xmm3, %xmm0      # xmm0 = xmm3[1,1,3,3]
	pmuludq	%xmm2, %xmm3
	pshufd	$237, %xmm3, %xmm3      # xmm3 = xmm3[1,3,2,3]
	pmuludq	%xmm2, %xmm0
	pshufd	$237, %xmm0, %xmm0      # xmm0 = xmm0[1,3,2,3]
	punpckldq	%xmm0, %xmm3    # xmm3 = xmm3[0],xmm0[0],xmm3[1],xmm0[1]
	psrld	$1, %xmm3
	pand	%xmm10, %xmm3
	movdqa	%xmm3, (%rax,%rdx,4)
	paddq	%xmm5, %xmm7
	paddq	%xmm5, %xmm1
	addq	$8, %rdx
	cmpq	$204, %rdx
	jne	.LBB5_2
# %bb.3:                                # %for.inc13
                                        #   in Loop: Header=BB5_1 Depth=1
	addq	$1, %rcx
	addq	$800, %rax              # imm = 0x320
	cmpq	$200, %rcx
	jne	.LBB5_1
# %bb.4:                                # %for.end15
	movl	$10737418, DX.fixp(%rip) # imm = 0xA3D70A
	movl	$10737418, DY.fixp(%rip) # imm = 0xA3D70A
	movl	$21474836, DT.fixp(%rip) # imm = 0x147AE14
	movl	$-2147483648, B1.fixp(%rip) # imm = 0x80000000
	movl	$-2147483648, B2.fixp(%rip) # imm = 0x80000000
	movl	$-939518471, mul1.fixp(%rip) # imm = 0xC80015F9
	movl	$-939518471, mul2.fixp(%rip) # imm = 0xC80015F9
	movl	$-1677724412, a.fixp(%rip) # imm = 0x9BFFF504
	movl	$-935324167, b.fixp(%rip) # imm = 0xC84015F9
	movl	$-1677724412, c.fixp(%rip) # imm = 0x9BFFF504
	movl	$-1677724412, d.fixp(%rip) # imm = 0x9BFFF504
	movl	$-931129863, e.fixp(%rip) # imm = 0xC88015F9
	movl	$-1677724412, f.fixp(%rip) # imm = 0x9BFFF504
	leaq	-159276(%rbp), %r8
	movl	$1, %eax
	.p2align	4, 0x90
.LBB5_5:                                # %for.cond31.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_6 Depth 2
                                        #       Child Loop BB5_7 Depth 3
                                        #       Child Loop BB5_9 Depth 3
                                        #     Child Loop BB5_12 Depth 2
                                        #       Child Loop BB5_13 Depth 3
                                        #       Child Loop BB5_15 Depth 3
	movl	%eax, -60(%rbp)         # 4-byte Spill
	movl	$1, %r10d
	leaq	-481676(%rbp), %rax
	movq	%rax, %rbx
	leaq	-320080(%rbp), %r13
	leaq	-160080(%rbp), %r12
	leaq	-319276(%rbp), %r11
	leaq	-479272(%rbp), %r9
	.p2align	4, 0x90
.LBB5_6:                                # %for.body34
                                        #   Parent Loop BB5_5 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_7 Depth 3
                                        #       Child Loop BB5_9 Depth 3
	movq	%rbx, -56(%rbp)         # 8-byte Spill
	movl	$536870912, -640080(%rbp,%r10,4) # imm = 0x20000000
	imulq	$800, %r10, %rax        # imm = 0x320
	movl	$0, -160080(%rbp,%rax)
	movl	$4194304, -320080(%rbp,%rax) # imm = 0x400000
	leaq	1(%r10), %rax
	movq	%rax, -72(%rbp)         # 8-byte Spill
	xorl	%esi, %esi
	movl	$4194304, %ecx          # imm = 0x400000
	movq	%r9, -48(%rbp)          # 8-byte Spill
	xorl	%edi, %edi
	movabsq	$3607389340247785472, %r15 # imm = 0x3210057E00000000
	movabsq	$1759221553037312, %r14 # imm = 0x64000AFC00000
	.p2align	4, 0x90
.LBB5_7:                                # %for.body50
                                        #   Parent Loop BB5_5 Depth=1
                                        #     Parent Loop BB5_6 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movslq	%edi, %rax
	imulq	$-1677724412, %rax, %rbx # imm = 0x9BFFF504
	addq	%r15, %rbx
	sarq	$32, %rbx
	movq	%r14, %rax
	xorl	%edx, %edx
	idivq	%rbx
	movq	%rax, %rdi
	shll	$8, %edi
	movl	%edi, (%r8,%rsi,4)
	movslq	-8(%r9), %rax
	imulq	$1677724412, %rax, %rax # imm = 0x64000AFC
	shrq	$32, %rax
	movslq	-4(%r9), %rdx
	imulq	$-418382527, %rdx, %rdx # imm = 0xE70FFD41
	shrq	$29, %rdx
	addl	%eax, %edx
	movslq	(%r9), %rax
	imulq	$-1677724412, %rax, %rax # imm = 0x9BFFF504
	shrq	$32, %rax
	subl	%eax, %edx
	movslq	%ecx, %rax
	imulq	$-1677724412, %rax, %rax # imm = 0x9BFFF504
	shrq	$31, %rax
	shrl	$6, %edx
	subl	%eax, %edx
	shll	$9, %edx
	movslq	%edx, %rax
	shlq	$20, %rax
	cqto
	idivq	%rbx
	movq	%rax, %rcx
	shll	$7, %ecx
	sarl	$7, %ecx
	movl	%ecx, (%r11,%rsi,4)
	addq	$1, %rsi
	addq	$800, %r9               # imm = 0x320
	cmpq	$198, %rsi
	jne	.LBB5_7
# %bb.8:                                # %for.end111
                                        #   in Loop: Header=BB5_6 Depth=2
	movl	$536870912, -480880(%rbp,%r10,4) # imm = 0x20000000
	movl	$536870912, %edx        # imm = 0x20000000
	movl	$398, %eax              # imm = 0x18E
	movq	-56(%rbp), %rbx         # 8-byte Reload
	movq	%rbx, %rcx
	.p2align	4, 0x90
.LBB5_9:                                # %for.body118
                                        #   Parent Loop BB5_5 Depth=1
                                        #     Parent Loop BB5_6 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movslq	(%r12,%rax,4), %rsi
	movslq	%edx, %rdi
	imulq	%rsi, %rdi
	shrq	$30, %rdi
	movl	(%r13,%rax,4), %edx
	shll	$7, %edx
	addl	%edi, %edx
	andl	$-128, %edx
	movl	%edx, (%rcx)
	addq	$-1, %rax
	addq	$-800, %rcx             # imm = 0xFCE0
	cmpq	$200, %rax
	jne	.LBB5_9
# %bb.10:                               # %for.inc140
                                        #   in Loop: Header=BB5_6 Depth=2
	addq	$800, %r8               # imm = 0x320
	movq	-48(%rbp), %r9          # 8-byte Reload
	addq	$4, %r9
	addq	$800, %r11              # imm = 0x320
	addq	$800, %r12              # imm = 0x320
	addq	$800, %r13              # imm = 0x320
	addq	$4, %rbx
	movq	-72(%rbp), %rax         # 8-byte Reload
	movq	%rax, %r10
	cmpq	$199, %rax
	jne	.LBB5_6
# %bb.11:                               # %for.body146.preheader
                                        #   in Loop: Header=BB5_5 Depth=1
	movl	$1, %eax
	leaq	-480080(%rbp), %r11
	leaq	-320080(%rbp), %r12
	leaq	-160080(%rbp), %r13
	leaq	-319276(%rbp), %rsi
	leaq	-638476(%rbp), %rbx
	leaq	-159276(%rbp), %r9
	movabsq	$3611892939875155968, %r14 # imm = 0x3220057E00000000
	.p2align	4, 0x90
.LBB5_12:                               # %for.body146
                                        #   Parent Loop BB5_5 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB5_13 Depth 3
                                        #       Child Loop BB5_15 Depth 3
	imulq	$800, %rax, %rcx        # imm = 0x320
	movl	$268435456, -480080(%rbp,%rcx) # imm = 0x10000000
	movl	$0, -160080(%rbp,%rcx)
	movq	%rcx, -48(%rbp)         # 8-byte Spill
	movl	$4194304, -320080(%rbp,%rcx) # imm = 0x400000
	addq	$1, %rax
	movq	%rax, -56(%rbp)         # 8-byte Spill
	xorl	%r15d, %r15d
	movl	$4194304, %edi          # imm = 0x400000
	xorl	%ecx, %ecx
	movabsq	$3518443106074624, %r10 # imm = 0xC80015F800000
	.p2align	4, 0x90
.LBB5_13:                               # %for.body162
                                        #   Parent Loop BB5_5 Depth=1
                                        #     Parent Loop BB5_12 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movslq	%ecx, %rax
	imulq	$-1677724412, %rax, %r8 # imm = 0x9BFFF504
	addq	%r14, %r8
	sarq	$32, %r8
	movq	%r10, %rax
	xorl	%edx, %edx
	idivq	%r8
	movq	%rax, %rcx
	shll	$7, %ecx
	movl	%ecx, (%r9,%r15,4)
	movslq	-1600(%rbx,%r15,4), %rax
	imulq	$1677724412, %rax, %rax # imm = 0x64000AFC
	shrq	$32, %rax
	movslq	-800(%rbx,%r15,4), %rdx
	imulq	$-837813630, %rdx, %rdx # imm = 0xCE0FFA82
	shrq	$30, %rdx
	addl	%eax, %edx
	movslq	(%rbx,%r15,4), %rax
	imulq	$-1677724412, %rax, %rax # imm = 0x9BFFF504
	shrq	$32, %rax
	subl	%eax, %edx
	movslq	%edi, %rax
	imulq	$-1677724412, %rax, %rax # imm = 0x9BFFF504
	shrq	$31, %rax
	shrl	$5, %edx
	subl	%eax, %edx
	shll	$8, %edx
	movslq	%edx, %rax
	shlq	$21, %rax
	cqto
	idivq	%r8
	movq	%rax, %rdi
	shll	$7, %edi
	sarl	$7, %edi
	movl	%edi, (%rsi,%r15,4)
	addq	$1, %r15
	cmpq	$198, %r15
	jne	.LBB5_13
# %bb.14:                               # %for.end223
                                        #   in Loop: Header=BB5_12 Depth=2
	movq	-48(%rbp), %rax         # 8-byte Reload
	movl	$268435456, -479284(%rbp,%rax) # imm = 0x10000000
	movl	$268435456, %ecx        # imm = 0x10000000
	movl	$398, %eax              # imm = 0x18E
	.p2align	4, 0x90
.LBB5_15:                               # %for.body230
                                        #   Parent Loop BB5_5 Depth=1
                                        #     Parent Loop BB5_12 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movslq	(%r13,%rax,4), %rdx
	movslq	%ecx, %rdi
	imulq	%rdx, %rdi
	shrq	$30, %rdi
	movl	(%r12,%rax,4), %ecx
	shll	$6, %ecx
	addl	%edi, %ecx
	andl	$-64, %ecx
	movl	%ecx, (%r11,%rax,4)
	addq	$-1, %rax
	cmpq	$200, %rax
	jne	.LBB5_15
# %bb.16:                               # %for.inc253
                                        #   in Loop: Header=BB5_12 Depth=2
	addq	$800, %r9               # imm = 0x320
	addq	$800, %rbx              # imm = 0x320
	addq	$800, %rsi              # imm = 0x320
	addq	$800, %r13              # imm = 0x320
	addq	$800, %r12              # imm = 0x320
	addq	$800, %r11              # imm = 0x320
	movq	-56(%rbp), %rax         # 8-byte Reload
	cmpq	$199, %rax
	jne	.LBB5_12
# %bb.17:                               # %for.inc256
                                        #   in Loop: Header=BB5_5 Depth=1
	movl	-60(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	cmpl	$101, %eax
	leaq	-159276(%rbp), %r8
	jne	.LBB5_5
# %bb.18:                               # %for.cond263.preheader.preheader
	leaq	-480080(%rbp), %r12
	xorl	%eax, %eax
	movl	$3435973837, %r15d      # imm = 0xCCCCCCCD
	xorl	%ebx, %ebx
	xorl	%ecx, %ecx
	.p2align	4, 0x90
.LBB5_19:                               # %for.cond263.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_20 Depth 2
	movq	%rcx, -48(%rbp)         # 8-byte Spill
	movq	%rax, -56(%rbp)         # 8-byte Spill
	movl	%eax, %r14d
	xorl	%r13d, %r13d
	.p2align	4, 0x90
.LBB5_20:                               # %for.body266
                                        #   Parent Loop BB5_19 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	%r14d, %eax
	imulq	%r15, %rax
	shrq	$36, %rax
	leal	(%rax,%rax,4), %eax
	leal	(%rbx,%rax,4), %eax
	cmpl	%r13d, %eax
	jne	.LBB5_22
# %bb.21:                               # %if.then
                                        #   in Loop: Header=BB5_20 Depth=2
	movq	stdout(%rip), %rsi
	movl	$10, %edi
	callq	fputc
.LBB5_22:                               # %if.end
                                        #   in Loop: Header=BB5_20 Depth=2
	movq	stdout(%rip), %rdi
	xorps	%xmm0, %xmm0
	cvtsi2sdl	(%r12,%r13,4), %xmm0
	mulsd	.LCPI5_5(%rip), %xmm0
	movl	$.L.str.8, %esi
	movb	$1, %al
	callq	fprintf
	addq	$1, %r13
	addl	$1, %r14d
	cmpq	$200, %r13
	jne	.LBB5_20
# %bb.23:                               # %for.inc279
                                        #   in Loop: Header=BB5_19 Depth=1
	movq	-48(%rbp), %rcx         # 8-byte Reload
	addq	$1, %rcx
	addq	$800, %r12              # imm = 0x320
	addl	$-200, %ebx
	movq	-56(%rbp), %rax         # 8-byte Reload
	addl	$200, %eax
	cmpq	$200, %rcx
	jne	.LBB5_19
# %bb.24:                               # %for.end281
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	addq	$640040, %rsp           # imm = 0x9C428
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
	.type	.L.str.8,@object        # @.str.8
.L.str.8:
	.asciz	"%0.16lf "
	.size	.L.str.8, 9

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

	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
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
