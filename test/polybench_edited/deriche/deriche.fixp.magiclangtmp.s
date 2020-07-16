	.text
	.file	"deriche.c"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI0_0:
	.quad	-4620693217682128896    # double -0.5
.LCPI0_1:
	.quad	4611686018427387904     # double 2
.LCPI0_2:
	.quad	-4625196817309499392    # double -0.25
.LCPI0_3:
	.quad	4728779608739020800     # double 134217728
.LCPI0_4:
	.quad	4602678819172646912     # double 0.5
.LCPI0_5:
	.quad	4607182418800017408     # double 1
.LCPI0_6:
	.quad	4742290407621132288     # double 1073741824
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
	subq	$393568, %rsp           # imm = 0x60160
	.cfi_offset %rbx, -48
	.cfi_offset %r12, -40
	.cfi_offset %r14, -32
	.cfi_offset %r15, -24
	xorl	%eax, %eax
	movl	%eax, -393252(%rbp)     # 4-byte Spill
.LBB0_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
	movl	-393252(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393256(%rbp)     # 4-byte Spill
	jge	.LBB0_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -393260(%rbp)     # 4-byte Spill
	jmp	.LBB0_3
.LBB0_3:                                # %for.cond8
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393260(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393264(%rbp)     # 4-byte Spill
	jge	.LBB0_6
# %bb.4:                                # %for.body10
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-393256(%rbp), %eax     # 4-byte Reload
	imull	$313, %eax, %ecx        # imm = 0x139
	movl	-393264(%rbp), %edx     # 4-byte Reload
	imull	$991, %edx, %esi        # imm = 0x3DF
	addl	%esi, %ecx
	movl	%ecx, %eax
	cltd
	movl	$65536, %ecx            # imm = 0x10000
	idivl	%ecx
	shll	$24, %edx
	movl	%edx, %ecx
	movl	%ecx, %edi
	movq	%rdi, %rax
	xorl	%ecx, %ecx
	movl	%ecx, %edx
	movl	$65535, %edi            # imm = 0xFFFF
	divq	%rdi
	movl	%eax, %ecx
	movl	-393256(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rax
	shlq	$9, %rax
	leaq	-98336(%rbp), %rdi
	addq	%rax, %rdi
	movl	-393264(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rax
	shll	$3, %ecx
	movl	%ecx, (%rdi,%rax,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-393264(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393260(%rbp)     # 4-byte Spill
	jmp	.LBB0_3
.LBB0_6:                                # %for.end
                                        #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_7
.LBB0_7:                                # %for.inc14
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-393256(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393252(%rbp)     # 4-byte Spill
	jmp	.LBB0_1
.LBB0_8:                                # %for.end16
	movsd	.LCPI0_2(%rip), %xmm0   # xmm0 = mem[0],zero
	callq	exp
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_5(%rip), %xmm2   # xmm2 = mem[0],zero
	subsd	%xmm0, %xmm2
	movaps	%xmm1, %xmm0
	movsd	%xmm2, -393272(%rbp)    # 8-byte Spill
	callq	exp
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_5(%rip), %xmm2   # xmm2 = mem[0],zero
	subsd	%xmm0, %xmm2
	movsd	-393272(%rbp), %xmm0    # 8-byte Reload
                                        # xmm0 = mem[0],zero
	mulsd	%xmm2, %xmm0
	movsd	%xmm0, -393280(%rbp)    # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	.LCPI0_4(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_5(%rip), %xmm2   # xmm2 = mem[0],zero
	movaps	%xmm1, %xmm3
	mulsd	%xmm0, %xmm3
	addsd	%xmm3, %xmm2
	movaps	%xmm1, %xmm0
	movsd	%xmm2, -393288(%rbp)    # 8-byte Spill
	callq	exp
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	-393288(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	subsd	%xmm0, %xmm2
	movsd	-393280(%rbp), %xmm0    # 8-byte Reload
                                        # xmm0 = mem[0],zero
	divsd	%xmm2, %xmm0
	movsd	%xmm0, -393296(%rbp)    # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_3(%rip), %xmm2   # xmm2 = mem[0],zero
	movaps	%xmm2, %xmm3
	movsd	-393296(%rbp), %xmm4    # 8-byte Reload
                                        # xmm4 = mem[0],zero
	mulsd	%xmm4, %xmm3
	cvttsd2si	%xmm3, %eax
	mulsd	%xmm0, %xmm2
	cvttsd2si	%xmm2, %ecx
	movslq	%eax, %rdx
	movslq	%ecx, %rsi
	imulq	%rsi, %rdx
	sarq	$27, %rdx
	movl	%edx, %eax
	movslq	%eax, %rdx
	imulq	$-3, %rdx, %rdx
	sarq	$2, %rdx
	movl	%edx, %eax
	movaps	%xmm1, %xmm0
	movl	%eax, -393300(%rbp)     # 4-byte Spill
	callq	exp
	movsd	.LCPI0_0(%rip), %xmm1   # xmm1 = mem[0],zero
	xorl	%eax, %eax
	movsd	.LCPI0_3(%rip), %xmm2   # xmm2 = mem[0],zero
	movaps	%xmm2, %xmm3
	movsd	-393296(%rbp), %xmm4    # 8-byte Reload
                                        # xmm4 = mem[0],zero
	mulsd	%xmm4, %xmm3
	cvttsd2si	%xmm3, %ecx
	movaps	%xmm2, %xmm3
	mulsd	%xmm0, %xmm3
	cvttsd2si	%xmm3, %edi
	movslq	%ecx, %rdx
	movslq	%edi, %rsi
	imulq	%rsi, %rdx
	sarq	$27, %rdx
	movl	%edx, %ecx
	movslq	%ecx, %rdx
	imulq	$5, %rdx, %rdx
	sarq	$2, %rdx
	movl	%edx, %ecx
	mulsd	%xmm4, %xmm2
	cvttsd2si	%xmm2, %edi
	subl	%edi, %eax
	movaps	%xmm1, %xmm0
	movl	%ecx, -393304(%rbp)     # 4-byte Spill
	movl	%eax, -393308(%rbp)     # 4-byte Spill
	callq	exp
	movsd	.LCPI0_1(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_2(%rip), %xmm2   # xmm2 = mem[0],zero
	movsd	.LCPI0_3(%rip), %xmm3   # xmm3 = mem[0],zero
	mulsd	%xmm0, %xmm3
	cvttsd2si	%xmm3, %eax
	movl	-393308(%rbp), %ecx     # 4-byte Reload
	movslq	%ecx, %rdx
	movslq	%eax, %rsi
	imulq	%rsi, %rdx
	sarq	$27, %rdx
	movl	%edx, %eax
	movaps	%xmm1, %xmm0
	movaps	%xmm2, %xmm1
	movl	%eax, -393312(%rbp)     # 4-byte Spill
	callq	pow
	movsd	.LCPI0_0(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	%xmm0, -393320(%rbp)    # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	xorl	%eax, %eax
	movq	%xmm0, %rdx
	movabsq	$-9223372036854775808, %rsi # imm = 0x8000000000000000
	xorq	%rsi, %rdx
	movq	%rdx, %xmm0
	movsd	%xmm0, -393328(%rbp)    # 8-byte Spill
	movl	%eax, -393332(%rbp)     # 4-byte Spill
.LBB0_9:                                # %for.cond61
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_11 Depth 2
	movl	-393332(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393336(%rbp)     # 4-byte Spill
	jge	.LBB0_16
# %bb.10:                               # %for.body64
                                        #   in Loop: Header=BB0_9 Depth=1
	xorl	%eax, %eax
	movl	%eax, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%ecx, -393340(%rbp)     # 4-byte Spill
	movl	%edx, -393344(%rbp)     # 4-byte Spill
	movl	%esi, -393348(%rbp)     # 4-byte Spill
	movl	%eax, -393352(%rbp)     # 4-byte Spill
	jmp	.LBB0_11
.LBB0_11:                               # %for.cond65
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393352(%rbp), %eax     # 4-byte Reload
	movl	-393348(%rbp), %ecx     # 4-byte Reload
	movl	-393344(%rbp), %edx     # 4-byte Reload
	movl	-393340(%rbp), %esi     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393356(%rbp)     # 4-byte Spill
	movl	%ecx, -393360(%rbp)     # 4-byte Spill
	movl	%edx, -393364(%rbp)     # 4-byte Spill
	movl	%esi, -393368(%rbp)     # 4-byte Spill
	jge	.LBB0_14
# %bb.12:                               # %for.body68
                                        #   in Loop: Header=BB0_11 Depth=2
	movsd	.LCPI0_6(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_3(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-393336(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-98336(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-393356(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movsd	-393296(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r9d
	movslq	%r9d, %rcx
	movslq	%r8d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %r8d
	movl	-393300(%rbp), %r9d     # 4-byte Reload
	movslq	%r9d, %rcx
	movl	-393360(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$24, %rcx
	movl	%ecx, %r11d
	sarl	$3, %r11d
	addl	%r11d, %r8d
	movaps	%xmm0, %xmm1
	movsd	-393320(%rbp), %xmm3    # 8-byte Reload
                                        # xmm3 = mem[0],zero
	mulsd	%xmm3, %xmm1
	cvttsd2si	%xmm1, %r11d
	movslq	%r11d, %rcx
	movl	-393364(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %ebx
	shll	$3, %r8d
	addl	%ebx, %r8d
	movsd	-393328(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %ebx
	movslq	%ebx, %rcx
	movl	-393368(%rbp), %ebx     # 4-byte Reload
	movslq	%ebx, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %r14d
	addl	%r14d, %r8d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rsi
	movq	%rsi, %r15
	addq	%rcx, %r15
	movslq	%edi, %rcx
	sarl	$3, %r8d
	movl	%r8d, (%r15,%rcx,4)
	movslq	%eax, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r14d
	movl	%r8d, -393372(%rbp)     # 4-byte Spill
	movl	%r14d, -393376(%rbp)    # 4-byte Spill
# %bb.13:                               # %for.inc92
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-393356(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	-393364(%rbp), %ecx     # 4-byte Reload
	movl	-393376(%rbp), %edx     # 4-byte Reload
	movl	-393372(%rbp), %esi     # 4-byte Reload
	movl	%ecx, -393340(%rbp)     # 4-byte Spill
	movl	%edx, -393344(%rbp)     # 4-byte Spill
	movl	%esi, -393348(%rbp)     # 4-byte Spill
	movl	%eax, -393352(%rbp)     # 4-byte Spill
	jmp	.LBB0_11
.LBB0_14:                               # %for.end94
                                        #   in Loop: Header=BB0_9 Depth=1
	jmp	.LBB0_15
.LBB0_15:                               # %for.inc95
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-393336(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393332(%rbp)     # 4-byte Spill
	jmp	.LBB0_9
.LBB0_16:                               # %for.end97
	xorl	%eax, %eax
	movl	%eax, -393380(%rbp)     # 4-byte Spill
	jmp	.LBB0_17
.LBB0_17:                               # %for.cond98
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_19 Depth 2
	movl	-393380(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393384(%rbp)     # 4-byte Spill
	jge	.LBB0_24
# %bb.18:                               # %for.body101
                                        #   in Loop: Header=BB0_17 Depth=1
	xorl	%eax, %eax
	movl	$127, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%eax, %edi
	movl	%edx, -393388(%rbp)     # 4-byte Spill
	movl	%esi, -393392(%rbp)     # 4-byte Spill
	movl	%ecx, -393396(%rbp)     # 4-byte Spill
	movl	%edi, -393400(%rbp)     # 4-byte Spill
	movl	%eax, -393404(%rbp)     # 4-byte Spill
	jmp	.LBB0_19
.LBB0_19:                               # %for.cond102
                                        #   Parent Loop BB0_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393404(%rbp), %eax     # 4-byte Reload
	movl	-393400(%rbp), %ecx     # 4-byte Reload
	movl	-393396(%rbp), %edx     # 4-byte Reload
	movl	-393392(%rbp), %esi     # 4-byte Reload
	movl	-393388(%rbp), %edi     # 4-byte Reload
	cmpl	$0, %edx
	movl	%eax, -393408(%rbp)     # 4-byte Spill
	movl	%ecx, -393412(%rbp)     # 4-byte Spill
	movl	%edx, -393416(%rbp)     # 4-byte Spill
	movl	%esi, -393420(%rbp)     # 4-byte Spill
	movl	%edi, -393424(%rbp)     # 4-byte Spill
	jl	.LBB0_22
# %bb.20:                               # %for.body105
                                        #   in Loop: Header=BB0_19 Depth=2
	movsd	.LCPI0_6(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-393304(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	movl	-393420(%rbp), %edx     # 4-byte Reload
	movslq	%edx, %rsi
	imulq	%rsi, %rcx
	sarq	$24, %rcx
	movl	%ecx, %edi
	movl	-393312(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rcx
	movl	-393424(%rbp), %r9d     # 4-byte Reload
	movslq	%r9d, %rsi
	imulq	%rsi, %rcx
	sarq	$24, %rcx
	movl	%ecx, %r10d
	addl	%r10d, %edi
	movaps	%xmm0, %xmm1
	movsd	-393320(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r10d
	movslq	%r10d, %rcx
	movl	-393412(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %r11d
	addl	%r11d, %edi
	movsd	-393328(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %r11d
	movslq	%r11d, %rcx
	movl	-393408(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %ebx
	addl	%ebx, %edi
	movl	-393384(%rbp), %ebx     # 4-byte Reload
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rsi
	movq	%rsi, %r14
	addq	%rcx, %r14
	movl	-393416(%rbp), %r15d    # 4-byte Reload
	movslq	%r15d, %rcx
	sarl	$3, %edi
	movl	%edi, (%r14,%rcx,4)
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	leaq	-98336(%rbp), %r14
	addq	%rcx, %r14
	movslq	%r15d, %rcx
	movl	(%r14,%rcx,4), %edi
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rsi
	movslq	%r15d, %rcx
	movl	(%rsi,%rcx,4), %r12d
	movl	%edi, -393428(%rbp)     # 4-byte Spill
	movl	%r12d, -393432(%rbp)    # 4-byte Spill
# %bb.21:                               # %for.inc125
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-393416(%rbp), %eax     # 4-byte Reload
	addl	$-1, %eax
	movl	-393420(%rbp), %ecx     # 4-byte Reload
	movl	-393428(%rbp), %edx     # 4-byte Reload
	movl	-393432(%rbp), %esi     # 4-byte Reload
	movl	-393412(%rbp), %edi     # 4-byte Reload
	movl	%ecx, -393388(%rbp)     # 4-byte Spill
	movl	%edx, -393392(%rbp)     # 4-byte Spill
	movl	%eax, -393396(%rbp)     # 4-byte Spill
	movl	%esi, -393400(%rbp)     # 4-byte Spill
	movl	%edi, -393404(%rbp)     # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end126
                                        #   in Loop: Header=BB0_17 Depth=1
	jmp	.LBB0_23
.LBB0_23:                               # %for.inc127
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-393384(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393380(%rbp)     # 4-byte Spill
	jmp	.LBB0_17
.LBB0_24:                               # %for.end129
	xorl	%eax, %eax
	movl	%eax, -393436(%rbp)     # 4-byte Spill
	jmp	.LBB0_25
.LBB0_25:                               # %for.cond130
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_27 Depth 2
	movl	-393436(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393440(%rbp)     # 4-byte Spill
	jge	.LBB0_32
# %bb.26:                               # %for.body133
                                        #   in Loop: Header=BB0_25 Depth=1
	xorl	%eax, %eax
	movl	%eax, -393444(%rbp)     # 4-byte Spill
	jmp	.LBB0_27
.LBB0_27:                               # %for.cond134
                                        #   Parent Loop BB0_25 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393444(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393448(%rbp)     # 4-byte Spill
	jge	.LBB0_30
# %bb.28:                               # %for.body137
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-393440(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-393448(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	addl	(%rdx,%rcx,4), %edi
	movslq	%edi, %rcx
	shlq	$0, %rcx
	movl	%ecx, %edi
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-196640(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	%edi, (%rdx,%rcx,4)
# %bb.29:                               # %for.inc152
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-393448(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393444(%rbp)     # 4-byte Spill
	jmp	.LBB0_27
.LBB0_30:                               # %for.end154
                                        #   in Loop: Header=BB0_25 Depth=1
	jmp	.LBB0_31
.LBB0_31:                               # %for.inc155
                                        #   in Loop: Header=BB0_25 Depth=1
	movl	-393440(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393436(%rbp)     # 4-byte Spill
	jmp	.LBB0_25
.LBB0_32:                               # %for.end157
	xorl	%eax, %eax
	movl	%eax, -393452(%rbp)     # 4-byte Spill
	jmp	.LBB0_33
.LBB0_33:                               # %for.cond158
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_35 Depth 2
	movl	-393452(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393456(%rbp)     # 4-byte Spill
	jge	.LBB0_40
# %bb.34:                               # %for.body161
                                        #   in Loop: Header=BB0_33 Depth=1
	xorl	%eax, %eax
	movl	%eax, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%ecx, -393460(%rbp)     # 4-byte Spill
	movl	%edx, -393464(%rbp)     # 4-byte Spill
	movl	%esi, -393468(%rbp)     # 4-byte Spill
	movl	%eax, -393472(%rbp)     # 4-byte Spill
	jmp	.LBB0_35
.LBB0_35:                               # %for.cond162
                                        #   Parent Loop BB0_33 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393472(%rbp), %eax     # 4-byte Reload
	movl	-393468(%rbp), %ecx     # 4-byte Reload
	movl	-393464(%rbp), %edx     # 4-byte Reload
	movl	-393460(%rbp), %esi     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393476(%rbp)     # 4-byte Spill
	movl	%ecx, -393480(%rbp)     # 4-byte Spill
	movl	%edx, -393484(%rbp)     # 4-byte Spill
	movl	%esi, -393488(%rbp)     # 4-byte Spill
	jge	.LBB0_38
# %bb.36:                               # %for.body165
                                        #   in Loop: Header=BB0_35 Depth=2
	movsd	.LCPI0_6(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_3(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-393476(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-196640(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-393456(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movsd	-393296(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r9d
	movslq	%r9d, %rcx
	movslq	%r8d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %r8d
	movl	-393300(%rbp), %r9d     # 4-byte Reload
	movslq	%r9d, %rcx
	movl	-393480(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$24, %rcx
	movl	%ecx, %r11d
	sarl	$3, %r11d
	addl	%r11d, %r8d
	movaps	%xmm0, %xmm1
	movsd	-393320(%rbp), %xmm3    # 8-byte Reload
                                        # xmm3 = mem[0],zero
	mulsd	%xmm3, %xmm1
	cvttsd2si	%xmm1, %r11d
	movslq	%r11d, %rcx
	movl	-393484(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %ebx
	shll	$3, %r8d
	addl	%ebx, %r8d
	movsd	-393328(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %ebx
	movslq	%ebx, %rcx
	movl	-393488(%rbp), %ebx     # 4-byte Reload
	movslq	%ebx, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %r14d
	addl	%r14d, %r8d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rsi
	movq	%rsi, %r15
	addq	%rcx, %r15
	movslq	%edi, %rcx
	sarl	$3, %r8d
	movl	%r8d, (%r15,%rcx,4)
	movslq	%eax, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r14d
	movl	%r8d, -393492(%rbp)     # 4-byte Spill
	movl	%r14d, -393496(%rbp)    # 4-byte Spill
# %bb.37:                               # %for.inc189
                                        #   in Loop: Header=BB0_35 Depth=2
	movl	-393476(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	-393484(%rbp), %ecx     # 4-byte Reload
	movl	-393496(%rbp), %edx     # 4-byte Reload
	movl	-393492(%rbp), %esi     # 4-byte Reload
	movl	%ecx, -393460(%rbp)     # 4-byte Spill
	movl	%edx, -393464(%rbp)     # 4-byte Spill
	movl	%esi, -393468(%rbp)     # 4-byte Spill
	movl	%eax, -393472(%rbp)     # 4-byte Spill
	jmp	.LBB0_35
.LBB0_38:                               # %for.end191
                                        #   in Loop: Header=BB0_33 Depth=1
	jmp	.LBB0_39
.LBB0_39:                               # %for.inc192
                                        #   in Loop: Header=BB0_33 Depth=1
	movl	-393456(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393452(%rbp)     # 4-byte Spill
	jmp	.LBB0_33
.LBB0_40:                               # %for.end194
	xorl	%eax, %eax
	movl	%eax, -393500(%rbp)     # 4-byte Spill
	jmp	.LBB0_41
.LBB0_41:                               # %for.cond195
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_43 Depth 2
	movl	-393500(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393504(%rbp)     # 4-byte Spill
	jge	.LBB0_48
# %bb.42:                               # %for.body198
                                        #   in Loop: Header=BB0_41 Depth=1
	xorl	%eax, %eax
	movl	$191, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%eax, %edi
	movl	%ecx, -393508(%rbp)     # 4-byte Spill
	movl	%edx, -393512(%rbp)     # 4-byte Spill
	movl	%esi, -393516(%rbp)     # 4-byte Spill
	movl	%edi, -393520(%rbp)     # 4-byte Spill
	movl	%eax, -393524(%rbp)     # 4-byte Spill
	jmp	.LBB0_43
.LBB0_43:                               # %for.cond199
                                        #   Parent Loop BB0_41 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393524(%rbp), %eax     # 4-byte Reload
	movl	-393520(%rbp), %ecx     # 4-byte Reload
	movl	-393516(%rbp), %edx     # 4-byte Reload
	movl	-393512(%rbp), %esi     # 4-byte Reload
	movl	-393508(%rbp), %edi     # 4-byte Reload
	cmpl	$0, %edi
	movl	%eax, -393528(%rbp)     # 4-byte Spill
	movl	%ecx, -393532(%rbp)     # 4-byte Spill
	movl	%edx, -393536(%rbp)     # 4-byte Spill
	movl	%esi, -393540(%rbp)     # 4-byte Spill
	movl	%edi, -393544(%rbp)     # 4-byte Spill
	jl	.LBB0_46
# %bb.44:                               # %for.body202
                                        #   in Loop: Header=BB0_43 Depth=2
	movsd	.LCPI0_6(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-393304(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	movl	-393540(%rbp), %edx     # 4-byte Reload
	movslq	%edx, %rsi
	imulq	%rsi, %rcx
	sarq	$24, %rcx
	movl	%ecx, %edi
	movl	-393312(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rcx
	movl	-393536(%rbp), %r9d     # 4-byte Reload
	movslq	%r9d, %rsi
	imulq	%rsi, %rcx
	sarq	$24, %rcx
	movl	%ecx, %r10d
	addl	%r10d, %edi
	movaps	%xmm0, %xmm1
	movsd	-393320(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r10d
	movslq	%r10d, %rcx
	movl	-393532(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %r11d
	addl	%r11d, %edi
	movsd	-393328(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %r11d
	movslq	%r11d, %rcx
	movl	-393528(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$27, %rcx
	movl	%ecx, %ebx
	addl	%ebx, %edi
	movl	-393544(%rbp), %ebx     # 4-byte Reload
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rsi
	movq	%rsi, %r14
	addq	%rcx, %r14
	movl	-393504(%rbp), %r15d    # 4-byte Reload
	movslq	%r15d, %rcx
	sarl	$3, %edi
	movl	%edi, (%r14,%rcx,4)
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	leaq	-196640(%rbp), %r14
	addq	%rcx, %r14
	movslq	%r15d, %rcx
	movl	(%r14,%rcx,4), %edi
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rsi
	movslq	%r15d, %rcx
	movl	(%rsi,%rcx,4), %r12d
	movl	%edi, -393548(%rbp)     # 4-byte Spill
	movl	%r12d, -393552(%rbp)    # 4-byte Spill
# %bb.45:                               # %for.inc222
                                        #   in Loop: Header=BB0_43 Depth=2
	movl	-393544(%rbp), %eax     # 4-byte Reload
	addl	$-1, %eax
	movl	-393548(%rbp), %ecx     # 4-byte Reload
	movl	-393540(%rbp), %edx     # 4-byte Reload
	movl	-393552(%rbp), %esi     # 4-byte Reload
	movl	-393532(%rbp), %edi     # 4-byte Reload
	movl	%eax, -393508(%rbp)     # 4-byte Spill
	movl	%ecx, -393512(%rbp)     # 4-byte Spill
	movl	%edx, -393516(%rbp)     # 4-byte Spill
	movl	%esi, -393520(%rbp)     # 4-byte Spill
	movl	%edi, -393524(%rbp)     # 4-byte Spill
	jmp	.LBB0_43
.LBB0_46:                               # %for.end224
                                        #   in Loop: Header=BB0_41 Depth=1
	jmp	.LBB0_47
.LBB0_47:                               # %for.inc225
                                        #   in Loop: Header=BB0_41 Depth=1
	movl	-393504(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393500(%rbp)     # 4-byte Spill
	jmp	.LBB0_41
.LBB0_48:                               # %for.end227
	xorl	%eax, %eax
	movl	%eax, -393556(%rbp)     # 4-byte Spill
	jmp	.LBB0_49
.LBB0_49:                               # %for.cond228
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_51 Depth 2
	movl	-393556(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393560(%rbp)     # 4-byte Spill
	jge	.LBB0_56
# %bb.50:                               # %for.body231
                                        #   in Loop: Header=BB0_49 Depth=1
	xorl	%eax, %eax
	movl	%eax, -393564(%rbp)     # 4-byte Spill
	jmp	.LBB0_51
.LBB0_51:                               # %for.cond232
                                        #   Parent Loop BB0_49 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393564(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393568(%rbp)     # 4-byte Spill
	jge	.LBB0_54
# %bb.52:                               # %for.body235
                                        #   in Loop: Header=BB0_51 Depth=2
	movl	-393560(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-393568(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	addl	(%rdx,%rcx,4), %edi
	movslq	%edi, %rcx
	shlq	$0, %rcx
	movl	%ecx, %edi
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-196640(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	%edi, (%rdx,%rcx,4)
# %bb.53:                               # %for.inc250
                                        #   in Loop: Header=BB0_51 Depth=2
	movl	-393568(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393564(%rbp)     # 4-byte Spill
	jmp	.LBB0_51
.LBB0_54:                               # %for.end252
                                        #   in Loop: Header=BB0_49 Depth=1
	jmp	.LBB0_55
.LBB0_55:                               # %for.inc253
                                        #   in Loop: Header=BB0_49 Depth=1
	movl	-393560(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393556(%rbp)     # 4-byte Spill
	jmp	.LBB0_49
.LBB0_56:                               # %for.end255
	xorl	%eax, %eax
	movl	%eax, -393572(%rbp)     # 4-byte Spill
	jmp	.LBB0_57
.LBB0_57:                               # %for.cond256
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_59 Depth 2
	movl	-393572(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393576(%rbp)     # 4-byte Spill
	jge	.LBB0_66
# %bb.58:                               # %for.body259
                                        #   in Loop: Header=BB0_57 Depth=1
	xorl	%eax, %eax
	movl	%eax, -393580(%rbp)     # 4-byte Spill
	jmp	.LBB0_59
.LBB0_59:                               # %for.cond260
                                        #   Parent Loop BB0_57 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393580(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393584(%rbp)     # 4-byte Spill
	jge	.LBB0_64
# %bb.60:                               # %for.body263
                                        #   in Loop: Header=BB0_59 Depth=2
	movl	-393576(%rbp), %eax     # 4-byte Reload
	shll	$7, %eax
	movl	-393584(%rbp), %ecx     # 4-byte Reload
	addl	%ecx, %eax
	cltd
	movl	$20, %esi
	idivl	%esi
	cmpl	$0, %edx
	jne	.LBB0_62
# %bb.61:                               # %if.then
                                        #   in Loop: Header=BB0_59 Depth=2
	movq	stdout, %rdi
	movabsq	$.L.str.6, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -393588(%rbp)     # 4-byte Spill
.LBB0_62:                               # %if.end
                                        #   in Loop: Header=BB0_59 Depth=2
	movsd	.LCPI0_3(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-393576(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-196640(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-393584(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	cvtsi2sdl	%r8d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.7, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -393592(%rbp)     # 4-byte Spill
# %bb.63:                               # %for.inc275
                                        #   in Loop: Header=BB0_59 Depth=2
	movl	-393584(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393580(%rbp)     # 4-byte Spill
	jmp	.LBB0_59
.LBB0_64:                               # %for.end277
                                        #   in Loop: Header=BB0_57 Depth=1
	jmp	.LBB0_65
.LBB0_65:                               # %for.inc278
                                        #   in Loop: Header=BB0_57 Depth=1
	movl	-393576(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393572(%rbp)     # 4-byte Spill
	jmp	.LBB0_57
.LBB0_66:                               # %for.end280
	xorl	%eax, %eax
	addq	$393568, %rsp           # imm = 0x60160
	popq	%rbx
	popq	%r12
	popq	%r14
	popq	%r15
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.L.str.6,@object        # @.str.6
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str.6:
	.asciz	"\n"
	.size	.L.str.6, 2

	.type	.L.str.7,@object        # @.str.7
.L.str.7:
	.asciz	"%.16lf "
	.size	.L.str.7, 8


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym exp
	.addrsig_sym pow
	.addrsig_sym fprintf
	.addrsig_sym stdout
