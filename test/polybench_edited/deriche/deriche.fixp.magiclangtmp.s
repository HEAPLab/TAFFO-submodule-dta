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
	.quad	4607182418800017408     # double 1
.LCPI0_4:
	.quad	4602678819172646912     # double 0.5
.LCPI0_5:
	.quad	4742290407621132288     # double 1073741824
.LCPI0_6:
	.quad	4746794007248502784     # double 2147483648
.LCPI0_7:
	.quad	4737786807993761792     # double 536870912
.LCPI0_8:
	.quad	4733283208366391296     # double 268435456
.LCPI0_9:
	.quad	4679239875398991872     # double 65535
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
	subq	$393600, %rsp           # imm = 0x60180
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
	movl	%ecx, %esi
	sarl	$31, %esi
	shrl	$16, %esi
	movl	%ecx, %edi
	addl	%esi, %edi
	andl	$-65536, %edi           # imm = 0xFFFF0000
	subl	%edi, %ecx
	cvtsi2sdl	%ecx, %xmm0
	movsd	.LCPI0_9(%rip), %xmm1   # xmm1 = mem[0],zero
	divsd	%xmm1, %xmm0
	movsd	.LCPI0_5(%rip), %xmm1   # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %r8
	movl	%r8d, %ecx
	movslq	%eax, %r8
	shlq	$9, %r8
	leaq	-98336(%rbp), %r9
	addq	%r8, %r9
	movslq	%edx, %r8
	movl	%ecx, (%r9,%r8,4)
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
	movsd	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_2(%rip), %xmm2   # xmm2 = mem[0],zero
	movsd	%xmm0, -393272(%rbp)    # 8-byte Spill
	movaps	%xmm2, %xmm0
	movsd	%xmm1, -393280(%rbp)    # 8-byte Spill
	movsd	%xmm2, -393288(%rbp)    # 8-byte Spill
	callq	exp
	movsd	.LCPI0_3(%rip), %xmm1   # xmm1 = mem[0],zero
	movaps	%xmm1, %xmm2
	subsd	%xmm0, %xmm2
	movsd	-393288(%rbp), %xmm0    # 8-byte Reload
                                        # xmm0 = mem[0],zero
	movsd	%xmm1, -393296(%rbp)    # 8-byte Spill
	movsd	%xmm2, -393304(%rbp)    # 8-byte Spill
	callq	exp
	movsd	-393296(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	subsd	%xmm0, %xmm1
	movsd	-393304(%rbp), %xmm0    # 8-byte Reload
                                        # xmm0 = mem[0],zero
	mulsd	%xmm1, %xmm0
	movsd	-393288(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	movsd	%xmm0, -393312(%rbp)    # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	.LCPI0_4(%rip), %xmm1   # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	movsd	-393296(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	addsd	%xmm2, %xmm0
	movsd	%xmm0, -393320(%rbp)    # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	-393320(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	subsd	%xmm0, %xmm1
	movsd	-393312(%rbp), %xmm0    # 8-byte Reload
                                        # xmm0 = mem[0],zero
	divsd	%xmm1, %xmm0
	movsd	-393288(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	movsd	%xmm0, -393328(%rbp)    # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	movsd	.LCPI0_5(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	-393328(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm1, %xmm2
	cvttsd2si	%xmm2, %eax
	movsd	.LCPI0_6(%rip), %xmm1   # xmm1 = mem[0],zero
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
	shrq	%rcx
	movl	%ecx, %esi
	movsd	-393288(%rbp), %xmm0    # 8-byte Reload
                                        # xmm0 = mem[0],zero
	movl	%eax, -393332(%rbp)     # 4-byte Spill
	movsd	%xmm1, -393344(%rbp)    # 8-byte Spill
	movq	%rdx, -393352(%rbp)     # 8-byte Spill
	movl	%esi, -393356(%rbp)     # 4-byte Spill
	callq	exp
	movsd	-393344(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movl	%ecx, %eax
	movl	%eax, %eax
	movl	%eax, %ecx
	movq	-393352(%rbp), %rdx     # 8-byte Reload
	imulq	%rcx, %rdx
	shrq	$31, %rdx
	movl	%edx, %eax
	movslq	%eax, %rcx
	leaq	(%rcx,%rcx,4), %rcx
	shrq	$2, %rcx
	movl	%ecx, %eax
	movl	-393332(%rbp), %esi     # 4-byte Reload
	addl	%esi, %esi
	negl	%esi
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	%eax, -393360(%rbp)     # 4-byte Spill
	movl	%esi, -393364(%rbp)     # 4-byte Spill
	callq	exp
	movsd	-393344(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movl	%ecx, %eax
	movl	-393364(%rbp), %esi     # 4-byte Reload
	movl	%esi, %r8d
	movl	%r8d, %ecx
	movl	%eax, %eax
	movl	%eax, %edx
	imulq	%rdx, %rcx
	shrq	$31, %rcx
	movl	%ecx, %eax
	movsd	-393272(%rbp), %xmm0    # 8-byte Reload
                                        # xmm0 = mem[0],zero
	movsd	-393280(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	movl	%eax, -393368(%rbp)     # 4-byte Spill
	callq	pow
	movsd	.LCPI0_0(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	%xmm0, -393376(%rbp)    # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	exp
	xorl	%eax, %eax
	movq	%xmm0, %rcx
	movabsq	$-9223372036854775808, %rdx # imm = 0x8000000000000000
	xorq	%rdx, %rcx
	movq	%rcx, %xmm0
	movsd	%xmm0, -393384(%rbp)    # 8-byte Spill
	movl	%eax, -393388(%rbp)     # 4-byte Spill
.LBB0_9:                                # %for.cond61
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_11 Depth 2
	movl	-393388(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393392(%rbp)     # 4-byte Spill
	jge	.LBB0_16
# %bb.10:                               # %for.body64
                                        #   in Loop: Header=BB0_9 Depth=1
	xorl	%eax, %eax
	movl	%eax, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%ecx, -393396(%rbp)     # 4-byte Spill
	movl	%edx, -393400(%rbp)     # 4-byte Spill
	movl	%esi, -393404(%rbp)     # 4-byte Spill
	movl	%eax, -393408(%rbp)     # 4-byte Spill
	jmp	.LBB0_11
.LBB0_11:                               # %for.cond65
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393408(%rbp), %eax     # 4-byte Reload
	movl	-393404(%rbp), %ecx     # 4-byte Reload
	movl	-393400(%rbp), %edx     # 4-byte Reload
	movl	-393396(%rbp), %esi     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393412(%rbp)     # 4-byte Spill
	movl	%ecx, -393416(%rbp)     # 4-byte Spill
	movl	%edx, -393420(%rbp)     # 4-byte Spill
	movl	%esi, -393424(%rbp)     # 4-byte Spill
	jge	.LBB0_14
# %bb.12:                               # %for.body68
                                        #   in Loop: Header=BB0_11 Depth=2
	movsd	.LCPI0_8(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_5(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_7(%rip), %xmm2   # xmm2 = mem[0],zero
	movl	-393392(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-98336(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-393412(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movaps	%xmm1, %xmm3
	movsd	-393328(%rbp), %xmm4    # 8-byte Reload
                                        # xmm4 = mem[0],zero
	mulsd	%xmm4, %xmm3
	cvttsd2si	%xmm3, %r9d
	movslq	%r9d, %rcx
	movl	%r8d, %r8d
	movl	%r8d, %esi
	imulq	%rsi, %rcx
	sarq	$31, %rcx
	movl	%ecx, %r8d
	movl	-393356(%rbp), %r9d     # 4-byte Reload
	movl	%r9d, %r10d
	movl	%r10d, %ecx
	movl	-393416(%rbp), %r10d    # 4-byte Reload
	movl	%r10d, %r11d
	movl	%r11d, %esi
	imulq	%rsi, %rcx
	shrq	$31, %rcx
	movl	%ecx, %r11d
	shrl	$1, %r11d
	addl	%r11d, %r8d
	movsd	-393376(%rbp), %xmm3    # 8-byte Reload
                                        # xmm3 = mem[0],zero
	mulsd	%xmm3, %xmm2
	cvttsd2si	%xmm2, %r11d
	movslq	%r11d, %rcx
	movl	-393420(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %ebx
	sarl	$1, %r8d
	sarl	$1, %ebx
	addl	%ebx, %r8d
	movsd	-393384(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %ebx
	movslq	%ebx, %rcx
	movl	-393424(%rbp), %ebx     # 4-byte Reload
	movl	%ebx, %r14d
	movl	%r14d, %esi
	imulq	%rsi, %rcx
	shrq	$30, %rcx
	movl	%ecx, %r14d
	shrl	$4, %r14d
	addl	%r14d, %r8d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rsi
	movq	%rsi, %r15
	addq	%rcx, %r15
	movslq	%edi, %rcx
	movl	%r8d, (%r15,%rcx,4)
	movslq	%eax, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	movq	%rsi, %rdx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r14d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r12d
	cvtsi2sdl	%r12d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.5, %rcx
	movq	%rcx, %rdi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	movl	%r8d, -393428(%rbp)     # 4-byte Spill
	movl	%r14d, -393432(%rbp)    # 4-byte Spill
	callq	printf
	movl	%eax, -393436(%rbp)     # 4-byte Spill
# %bb.13:                               # %for.inc97
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-393412(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	-393420(%rbp), %ecx     # 4-byte Reload
	shll	$4, %ecx
	movl	-393432(%rbp), %edx     # 4-byte Reload
	movl	-393428(%rbp), %esi     # 4-byte Reload
	movl	%ecx, -393396(%rbp)     # 4-byte Spill
	movl	%edx, -393400(%rbp)     # 4-byte Spill
	movl	%esi, -393404(%rbp)     # 4-byte Spill
	movl	%eax, -393408(%rbp)     # 4-byte Spill
	jmp	.LBB0_11
.LBB0_14:                               # %for.end99
                                        #   in Loop: Header=BB0_9 Depth=1
	jmp	.LBB0_15
.LBB0_15:                               # %for.inc100
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-393392(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393388(%rbp)     # 4-byte Spill
	jmp	.LBB0_9
.LBB0_16:                               # %for.end102
	xorl	%eax, %eax
	movl	%eax, -393440(%rbp)     # 4-byte Spill
	jmp	.LBB0_17
.LBB0_17:                               # %for.cond103
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_19 Depth 2
	movl	-393440(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393444(%rbp)     # 4-byte Spill
	jge	.LBB0_24
# %bb.18:                               # %for.body106
                                        #   in Loop: Header=BB0_17 Depth=1
	xorl	%eax, %eax
	movl	$127, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%eax, %edi
	movl	%edx, -393448(%rbp)     # 4-byte Spill
	movl	%esi, -393452(%rbp)     # 4-byte Spill
	movl	%ecx, -393456(%rbp)     # 4-byte Spill
	movl	%edi, -393460(%rbp)     # 4-byte Spill
	movl	%eax, -393464(%rbp)     # 4-byte Spill
	jmp	.LBB0_19
.LBB0_19:                               # %for.cond107
                                        #   Parent Loop BB0_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393464(%rbp), %eax     # 4-byte Reload
	movl	-393460(%rbp), %ecx     # 4-byte Reload
	movl	-393456(%rbp), %edx     # 4-byte Reload
	movl	-393452(%rbp), %esi     # 4-byte Reload
	movl	-393448(%rbp), %edi     # 4-byte Reload
	cmpl	$0, %edx
	movl	%eax, -393468(%rbp)     # 4-byte Spill
	movl	%ecx, -393472(%rbp)     # 4-byte Spill
	movl	%edx, -393476(%rbp)     # 4-byte Spill
	movl	%esi, -393480(%rbp)     # 4-byte Spill
	movl	%edi, -393484(%rbp)     # 4-byte Spill
	jl	.LBB0_22
# %bb.20:                               # %for.body110
                                        #   in Loop: Header=BB0_19 Depth=2
	movsd	.LCPI0_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_7(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-393360(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	movl	-393480(%rbp), %edx     # 4-byte Reload
	movl	%edx, %esi
	movl	%esi, %edi
	imulq	%rdi, %rcx
	shrq	$30, %rcx
	movl	%ecx, %esi
	movl	-393368(%rbp), %r8d     # 4-byte Reload
	movl	%r8d, %r9d
	movl	%r9d, %ecx
	movl	-393484(%rbp), %r9d     # 4-byte Reload
	movl	%r9d, %r10d
	movl	%r10d, %edi
	imulq	%rdi, %rcx
	shrq	$30, %rcx
	movl	%ecx, %r10d
	shrl	$1, %esi
	shrl	$2, %r10d
	addl	%r10d, %esi
	movsd	-393376(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r10d
	movslq	%r10d, %rcx
	movl	-393472(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rdi
	imulq	%rdi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %r11d
	sarl	$1, %esi
	sarl	$1, %r11d
	addl	%r11d, %esi
	movsd	-393384(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %r11d
	movslq	%r11d, %rcx
	movl	-393468(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rdi
	imulq	%rdi, %rcx
	shrq	$26, %rcx
	movl	%ecx, %ebx
	shrl	$4, %ebx
	addl	%ebx, %esi
	movl	-393444(%rbp), %ebx     # 4-byte Reload
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rdi
	movq	%rdi, %r14
	addq	%rcx, %r14
	movl	-393476(%rbp), %r15d    # 4-byte Reload
	movslq	%r15d, %rcx
	movl	%esi, (%r14,%rcx,4)
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	leaq	-98336(%rbp), %r14
	addq	%rcx, %r14
	movslq	%r15d, %rcx
	movl	(%r14,%rcx,4), %esi
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	addq	%rcx, %rdi
	movslq	%r15d, %rcx
	movl	(%rdi,%rcx,4), %r12d
	movl	%esi, -393488(%rbp)     # 4-byte Spill
	movl	%r12d, -393492(%rbp)    # 4-byte Spill
# %bb.21:                               # %for.inc130
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-393476(%rbp), %eax     # 4-byte Reload
	addl	$-1, %eax
	movl	-393480(%rbp), %ecx     # 4-byte Reload
	movl	-393488(%rbp), %edx     # 4-byte Reload
	movl	-393492(%rbp), %esi     # 4-byte Reload
	movl	-393472(%rbp), %edi     # 4-byte Reload
	movl	%ecx, -393448(%rbp)     # 4-byte Spill
	movl	%edx, -393452(%rbp)     # 4-byte Spill
	movl	%eax, -393456(%rbp)     # 4-byte Spill
	movl	%esi, -393460(%rbp)     # 4-byte Spill
	movl	%edi, -393464(%rbp)     # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end131
                                        #   in Loop: Header=BB0_17 Depth=1
	jmp	.LBB0_23
.LBB0_23:                               # %for.inc132
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-393444(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393440(%rbp)     # 4-byte Spill
	jmp	.LBB0_17
.LBB0_24:                               # %for.end134
	xorl	%eax, %eax
	movl	%eax, -393496(%rbp)     # 4-byte Spill
	jmp	.LBB0_25
.LBB0_25:                               # %for.cond135
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_27 Depth 2
	movl	-393496(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393500(%rbp)     # 4-byte Spill
	jge	.LBB0_32
# %bb.26:                               # %for.body138
                                        #   in Loop: Header=BB0_25 Depth=1
	xorl	%eax, %eax
	movl	%eax, -393504(%rbp)     # 4-byte Spill
	jmp	.LBB0_27
.LBB0_27:                               # %for.cond139
                                        #   Parent Loop BB0_25 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393504(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393508(%rbp)     # 4-byte Spill
	jge	.LBB0_30
# %bb.28:                               # %for.body142
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-393500(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-393508(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rdx
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
	shlq	$9, %rcx
	leaq	-196640(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	%edi, (%rdx,%rcx,4)
# %bb.29:                               # %for.inc157
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-393508(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393504(%rbp)     # 4-byte Spill
	jmp	.LBB0_27
.LBB0_30:                               # %for.end159
                                        #   in Loop: Header=BB0_25 Depth=1
	jmp	.LBB0_31
.LBB0_31:                               # %for.inc160
                                        #   in Loop: Header=BB0_25 Depth=1
	movl	-393500(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393496(%rbp)     # 4-byte Spill
	jmp	.LBB0_25
.LBB0_32:                               # %for.end162
	xorl	%eax, %eax
	movl	%eax, -393512(%rbp)     # 4-byte Spill
	jmp	.LBB0_33
.LBB0_33:                               # %for.cond163
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_35 Depth 2
	movl	-393512(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393516(%rbp)     # 4-byte Spill
	jge	.LBB0_40
# %bb.34:                               # %for.body166
                                        #   in Loop: Header=BB0_33 Depth=1
	xorl	%eax, %eax
	movl	%eax, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%ecx, -393520(%rbp)     # 4-byte Spill
	movl	%edx, -393524(%rbp)     # 4-byte Spill
	movl	%esi, -393528(%rbp)     # 4-byte Spill
	movl	%eax, -393532(%rbp)     # 4-byte Spill
	jmp	.LBB0_35
.LBB0_35:                               # %for.cond167
                                        #   Parent Loop BB0_33 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393532(%rbp), %eax     # 4-byte Reload
	movl	-393528(%rbp), %ecx     # 4-byte Reload
	movl	-393524(%rbp), %edx     # 4-byte Reload
	movl	-393520(%rbp), %esi     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393536(%rbp)     # 4-byte Spill
	movl	%ecx, -393540(%rbp)     # 4-byte Spill
	movl	%edx, -393544(%rbp)     # 4-byte Spill
	movl	%esi, -393548(%rbp)     # 4-byte Spill
	jge	.LBB0_38
# %bb.36:                               # %for.body170
                                        #   in Loop: Header=BB0_35 Depth=2
	movsd	.LCPI0_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_8(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-393536(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-196640(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-393516(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movaps	%xmm0, %xmm2
	movsd	-393328(%rbp), %xmm3    # 8-byte Reload
                                        # xmm3 = mem[0],zero
	mulsd	%xmm3, %xmm2
	cvttsd2si	%xmm2, %r9d
	movslq	%r9d, %rcx
	movslq	%r8d, %rsi
	imulq	%rsi, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r8d
	movl	-393356(%rbp), %r9d     # 4-byte Reload
	movl	%r9d, %r10d
	movl	%r10d, %ecx
	movl	-393540(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	shrq	$27, %rcx
	movl	%ecx, %r11d
	shll	$1, %r8d
	shrl	$3, %r11d
	addl	%r11d, %r8d
	movsd	-393376(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r11d
	movslq	%r11d, %rcx
	movl	-393544(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %ebx
	addl	%ebx, %r8d
	movsd	-393384(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %ebx
	movslq	%ebx, %rcx
	movl	-393548(%rbp), %ebx     # 4-byte Reload
	movl	%ebx, %r14d
	movl	%r14d, %esi
	imulq	%rsi, %rcx
	shrq	$30, %rcx
	movl	%ecx, %r14d
	shrl	$4, %r14d
	addl	%r14d, %r8d
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rsi
	movq	%rsi, %r15
	addq	%rcx, %r15
	movslq	%edi, %rcx
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
	movl	%r8d, -393552(%rbp)     # 4-byte Spill
	movl	%r14d, -393556(%rbp)    # 4-byte Spill
# %bb.37:                               # %for.inc194
                                        #   in Loop: Header=BB0_35 Depth=2
	movl	-393536(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	-393544(%rbp), %ecx     # 4-byte Reload
	shll	$4, %ecx
	movl	-393556(%rbp), %edx     # 4-byte Reload
	movl	-393552(%rbp), %esi     # 4-byte Reload
	movl	%ecx, -393520(%rbp)     # 4-byte Spill
	movl	%edx, -393524(%rbp)     # 4-byte Spill
	movl	%esi, -393528(%rbp)     # 4-byte Spill
	movl	%eax, -393532(%rbp)     # 4-byte Spill
	jmp	.LBB0_35
.LBB0_38:                               # %for.end196
                                        #   in Loop: Header=BB0_33 Depth=1
	jmp	.LBB0_39
.LBB0_39:                               # %for.inc197
                                        #   in Loop: Header=BB0_33 Depth=1
	movl	-393516(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393512(%rbp)     # 4-byte Spill
	jmp	.LBB0_33
.LBB0_40:                               # %for.end199
	xorl	%eax, %eax
	movl	%eax, -393560(%rbp)     # 4-byte Spill
	jmp	.LBB0_41
.LBB0_41:                               # %for.cond200
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_43 Depth 2
	movl	-393560(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393564(%rbp)     # 4-byte Spill
	jge	.LBB0_48
# %bb.42:                               # %for.body203
                                        #   in Loop: Header=BB0_41 Depth=1
	xorl	%eax, %eax
	movl	$191, %ecx
	movl	%eax, %edx
	movl	%eax, %esi
	movl	%eax, %edi
	movl	%ecx, -393568(%rbp)     # 4-byte Spill
	movl	%edx, -393572(%rbp)     # 4-byte Spill
	movl	%esi, -393576(%rbp)     # 4-byte Spill
	movl	%edi, -393580(%rbp)     # 4-byte Spill
	movl	%eax, -393584(%rbp)     # 4-byte Spill
	jmp	.LBB0_43
.LBB0_43:                               # %for.cond204
                                        #   Parent Loop BB0_41 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393584(%rbp), %eax     # 4-byte Reload
	movl	-393580(%rbp), %ecx     # 4-byte Reload
	movl	-393576(%rbp), %edx     # 4-byte Reload
	movl	-393572(%rbp), %esi     # 4-byte Reload
	movl	-393568(%rbp), %edi     # 4-byte Reload
	cmpl	$0, %edi
	movl	%eax, -393588(%rbp)     # 4-byte Spill
	movl	%ecx, -393592(%rbp)     # 4-byte Spill
	movl	%edx, -393596(%rbp)     # 4-byte Spill
	movl	%esi, -393600(%rbp)     # 4-byte Spill
	movl	%edi, -393604(%rbp)     # 4-byte Spill
	jl	.LBB0_46
# %bb.44:                               # %for.body207
                                        #   in Loop: Header=BB0_43 Depth=2
	movsd	.LCPI0_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_7(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-393360(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	movl	-393600(%rbp), %edx     # 4-byte Reload
	movslq	%edx, %rsi
	imulq	%rsi, %rcx
	shrq	$25, %rcx
	movl	%ecx, %edi
	movl	-393368(%rbp), %r8d     # 4-byte Reload
	movl	%r8d, %r9d
	movl	%r9d, %ecx
	movl	-393596(%rbp), %r9d     # 4-byte Reload
	movslq	%r9d, %rsi
	imulq	%rsi, %rcx
	shrq	$27, %rcx
	movl	%ecx, %r10d
	shrl	$3, %edi
	shrl	$2, %r10d
	addl	%r10d, %edi
	movsd	-393376(%rbp), %xmm2    # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm2, %xmm1
	cvttsd2si	%xmm1, %r10d
	movslq	%r10d, %rcx
	movl	-393592(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rsi
	imulq	%rsi, %rcx
	sarq	$28, %rcx
	movl	%ecx, %r11d
	sarl	$1, %edi
	sarl	$1, %r11d
	addl	%r11d, %edi
	movsd	-393384(%rbp), %xmm1    # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %r11d
	movslq	%r11d, %rcx
	movl	-393588(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rsi
	imulq	%rsi, %rcx
	shrq	$26, %rcx
	movl	%ecx, %ebx
	shrl	$4, %ebx
	addl	%ebx, %edi
	movl	-393604(%rbp), %ebx     # 4-byte Reload
	movslq	%ebx, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rsi
	movq	%rsi, %r14
	addq	%rcx, %r14
	movl	-393564(%rbp), %r15d    # 4-byte Reload
	movslq	%r15d, %rcx
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
	movl	%edi, -393608(%rbp)     # 4-byte Spill
	movl	%r12d, -393612(%rbp)    # 4-byte Spill
# %bb.45:                               # %for.inc227
                                        #   in Loop: Header=BB0_43 Depth=2
	movl	-393604(%rbp), %eax     # 4-byte Reload
	addl	$-1, %eax
	movl	-393608(%rbp), %ecx     # 4-byte Reload
	movl	-393600(%rbp), %edx     # 4-byte Reload
	movl	-393612(%rbp), %esi     # 4-byte Reload
	movl	-393592(%rbp), %edi     # 4-byte Reload
	movl	%eax, -393568(%rbp)     # 4-byte Spill
	movl	%ecx, -393572(%rbp)     # 4-byte Spill
	movl	%edx, -393576(%rbp)     # 4-byte Spill
	movl	%esi, -393580(%rbp)     # 4-byte Spill
	movl	%edi, -393584(%rbp)     # 4-byte Spill
	jmp	.LBB0_43
.LBB0_46:                               # %for.end229
                                        #   in Loop: Header=BB0_41 Depth=1
	jmp	.LBB0_47
.LBB0_47:                               # %for.inc230
                                        #   in Loop: Header=BB0_41 Depth=1
	movl	-393564(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393560(%rbp)     # 4-byte Spill
	jmp	.LBB0_41
.LBB0_48:                               # %for.end232
	xorl	%eax, %eax
	movl	%eax, -393616(%rbp)     # 4-byte Spill
	jmp	.LBB0_49
.LBB0_49:                               # %for.cond233
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_51 Depth 2
	movl	-393616(%rbp), %eax     # 4-byte Reload
	cmpl	$192, %eax
	movl	%eax, -393620(%rbp)     # 4-byte Spill
	jge	.LBB0_56
# %bb.50:                               # %for.body236
                                        #   in Loop: Header=BB0_49 Depth=1
	xorl	%eax, %eax
	movl	%eax, -393624(%rbp)     # 4-byte Spill
	jmp	.LBB0_51
.LBB0_51:                               # %for.cond237
                                        #   Parent Loop BB0_49 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-393624(%rbp), %eax     # 4-byte Reload
	cmpl	$128, %eax
	movl	%eax, -393628(%rbp)     # 4-byte Spill
	jge	.LBB0_54
# %bb.52:                               # %for.body240
                                        #   in Loop: Header=BB0_51 Depth=2
	movl	-393620(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-294944(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-393628(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	shlq	$9, %rcx
	leaq	-393248(%rbp), %rdx
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
	shlq	$9, %rcx
	leaq	-196640(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%esi, %rcx
	movl	%edi, (%rdx,%rcx,4)
# %bb.53:                               # %for.inc255
                                        #   in Loop: Header=BB0_51 Depth=2
	movl	-393628(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393624(%rbp)     # 4-byte Spill
	jmp	.LBB0_51
.LBB0_54:                               # %for.end257
                                        #   in Loop: Header=BB0_49 Depth=1
	jmp	.LBB0_55
.LBB0_55:                               # %for.inc258
                                        #   in Loop: Header=BB0_49 Depth=1
	movl	-393620(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -393616(%rbp)     # 4-byte Spill
	jmp	.LBB0_49
.LBB0_56:                               # %for.end260
	xorl	%eax, %eax
	addq	$393600, %rsp           # imm = 0x60180
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
	.type	.L.str.5,@object        # @.str.5
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str.5:
	.asciz	"%.16f "
	.size	.L.str.5, 7


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym exp
	.addrsig_sym pow
	.addrsig_sym printf
