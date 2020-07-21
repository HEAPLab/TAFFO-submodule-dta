	.text
	.file	"covariance.c"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI0_0:
	.quad	4625196817309499392     # double 16
.LCPI0_1:
	.quad	4683743612465315840     # double 131072
.LCPI0_2:
	.quad	4635329916471083008     # double 80
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
	subq	$64448, %rsp            # imm = 0xFBC0
	xorl	%eax, %eax
	movl	%edi, -64324(%rbp)      # 4-byte Spill
	movq	%rsi, -64336(%rbp)      # 8-byte Spill
	movl	%eax, -64340(%rbp)      # 4-byte Spill
.LBB0_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
	movl	-64340(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -64344(%rbp)      # 4-byte Spill
	jge	.LBB0_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -64348(%rbp)      # 4-byte Spill
	jmp	.LBB0_3
.LBB0_3:                                # %for.cond9
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-64348(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -64352(%rbp)      # 4-byte Spill
	jge	.LBB0_6
# %bb.4:                                # %for.body12
                                        #   in Loop: Header=BB0_3 Depth=2
	movsd	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-64344(%rbp), %eax      # 4-byte Reload
	cvtsi2sdl	%eax, %xmm2
	movl	-64352(%rbp), %ecx      # 4-byte Reload
	cvtsi2sdl	%ecx, %xmm3
	mulsd	%xmm3, %xmm2
	divsd	%xmm1, %xmm2
	mulsd	%xmm2, %xmm0
	cvttsd2si	%xmm0, %edx
	movslq	%eax, %rsi
	imulq	$320, %rsi, %rsi        # imm = 0x140
	leaq	-32000(%rbp), %rdi
	addq	%rsi, %rdi
	movslq	%ecx, %rsi
	movl	%edx, (%rdi,%rsi,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-64352(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64348(%rbp)      # 4-byte Spill
	jmp	.LBB0_3
.LBB0_6:                                # %for.end
                                        #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_7
.LBB0_7:                                # %for.inc17
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-64344(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64340(%rbp)      # 4-byte Spill
	jmp	.LBB0_1
.LBB0_8:                                # %for.end19
	xorl	%eax, %eax
	movl	%eax, -64356(%rbp)      # 4-byte Spill
	jmp	.LBB0_9
.LBB0_9:                                # %for.cond20
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_11 Depth 2
	movl	-64356(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -64360(%rbp)      # 4-byte Spill
	jge	.LBB0_16
# %bb.10:                               # %for.body23
                                        #   in Loop: Header=BB0_9 Depth=1
	xorl	%eax, %eax
	movl	-64360(%rbp), %ecx      # 4-byte Reload
	movslq	%ecx, %rdx
	movl	$0, -64320(%rbp,%rdx,4)
	movl	%eax, -64364(%rbp)      # 4-byte Spill
.LBB0_11:                               # %for.cond26
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-64364(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -64368(%rbp)      # 4-byte Spill
	jge	.LBB0_14
# %bb.12:                               # %for.body29
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-64368(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-32000(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-64360(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%esi, %rcx
	addl	-64320(%rbp,%rcx,4), %edi
	movl	%edi, -64320(%rbp,%rcx,4)
# %bb.13:                               # %for.inc36
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-64368(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64364(%rbp)      # 4-byte Spill
	jmp	.LBB0_11
.LBB0_14:                               # %for.end38
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-64360(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movslq	-64320(%rbp,%rcx,4), %rdx
	movq	%rdx, %rax
	cqto
	movl	$100, %esi
	idivq	%rsi
	shlq	$8, %rax
	movl	%eax, %edi
	sarl	$8, %edi
	movl	%edi, -64320(%rbp,%rcx,4)
# %bb.15:                               # %for.inc42
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-64360(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64356(%rbp)      # 4-byte Spill
	jmp	.LBB0_9
.LBB0_16:                               # %for.end44
	xorl	%eax, %eax
	movl	%eax, -64372(%rbp)      # 4-byte Spill
	jmp	.LBB0_17
.LBB0_17:                               # %for.cond45
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_19 Depth 2
	movl	-64372(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -64376(%rbp)      # 4-byte Spill
	jge	.LBB0_24
# %bb.18:                               # %for.body48
                                        #   in Loop: Header=BB0_17 Depth=1
	xorl	%eax, %eax
	movl	%eax, -64380(%rbp)      # 4-byte Spill
	jmp	.LBB0_19
.LBB0_19:                               # %for.cond49
                                        #   Parent Loop BB0_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-64380(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -64384(%rbp)      # 4-byte Spill
	jge	.LBB0_22
# %bb.20:                               # %for.body52
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-64384(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movl	-64320(%rbp,%rcx,4), %edx
	movl	-64376(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-32000(%rbp), %rdi
	addq	%rcx, %rdi
	movslq	%eax, %rcx
	movl	(%rdi,%rcx,4), %r8d
	subl	%edx, %r8d
	movl	%r8d, (%rdi,%rcx,4)
# %bb.21:                               # %for.inc59
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-64384(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64380(%rbp)      # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end61
                                        #   in Loop: Header=BB0_17 Depth=1
	jmp	.LBB0_23
.LBB0_23:                               # %for.inc62
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-64376(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64372(%rbp)      # 4-byte Spill
	jmp	.LBB0_17
.LBB0_24:                               # %for.end64
	xorl	%eax, %eax
	movl	%eax, -64388(%rbp)      # 4-byte Spill
	jmp	.LBB0_25
.LBB0_25:                               # %for.cond65
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_27 Depth 2
                                        #       Child Loop BB0_29 Depth 3
	movl	-64388(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -64392(%rbp)      # 4-byte Spill
	jge	.LBB0_36
# %bb.26:                               # %for.body68
                                        #   in Loop: Header=BB0_25 Depth=1
	movl	-64392(%rbp), %eax      # 4-byte Reload
	movl	%eax, -64396(%rbp)      # 4-byte Spill
	jmp	.LBB0_27
.LBB0_27:                               # %for.cond69
                                        #   Parent Loop BB0_25 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_29 Depth 3
	movl	-64396(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -64400(%rbp)      # 4-byte Spill
	jge	.LBB0_34
# %bb.28:                               # %for.body72
                                        #   in Loop: Header=BB0_27 Depth=2
	xorl	%eax, %eax
	movl	-64392(%rbp), %ecx      # 4-byte Reload
	movslq	%ecx, %rdx
	imulq	$320, %rdx, %rdx        # imm = 0x140
	leaq	-64000(%rbp), %rsi
	addq	%rdx, %rsi
	movl	-64400(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rdx
	movl	$0, (%rsi,%rdx,4)
	movl	%eax, -64404(%rbp)      # 4-byte Spill
.LBB0_29:                               # %for.cond77
                                        #   Parent Loop BB0_25 Depth=1
                                        #     Parent Loop BB0_27 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-64404(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -64408(%rbp)      # 4-byte Spill
	jge	.LBB0_32
# %bb.30:                               # %for.body80
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	-64408(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-32000(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-64392(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	addq	%rcx, %rdx
	movl	-64400(%rbp), %r9d      # 4-byte Reload
	movslq	%r9d, %rcx
	movl	(%rdx,%rcx,4), %r10d
	movslq	%r8d, %rcx
	movslq	%r10d, %rdx
	imulq	%rdx, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r8d
	movslq	%edi, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-64000(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%r9d, %rcx
	addl	(%rdx,%rcx,4), %r8d
	movl	%r8d, (%rdx,%rcx,4)
# %bb.31:                               # %for.inc95
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	-64408(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64404(%rbp)      # 4-byte Spill
	jmp	.LBB0_29
.LBB0_32:                               # %for.end97
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-64392(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-64000(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-64400(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rcx
	movslq	(%rsi,%rcx,4), %r8
	movq	%r8, %rax
	movq	%rdx, -64416(%rbp)      # 8-byte Spill
	cqto
	movl	$99, %r8d
	idivq	%r8
	shlq	$7, %rax
	movl	%eax, %r9d
	sarl	$7, %r9d
	movl	%r9d, (%rsi,%rcx,4)
	movl	-64392(%rbp), %r9d      # 4-byte Reload
	movslq	%r9d, %rax
	imulq	$320, %rax, %rax        # imm = 0x140
	movq	-64416(%rbp), %rcx      # 8-byte Reload
	addq	%rax, %rcx
	movslq	%edi, %rax
	movl	(%rcx,%rax,4), %r10d
	movslq	%edi, %rax
	imulq	$320, %rax, %rax        # imm = 0x140
	movq	-64416(%rbp), %rcx      # 8-byte Reload
	addq	%rax, %rcx
	movslq	%r9d, %rax
	movl	%r10d, (%rcx,%rax,4)
# %bb.33:                               # %for.inc111
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-64400(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64396(%rbp)      # 4-byte Spill
	jmp	.LBB0_27
.LBB0_34:                               # %for.end113
                                        #   in Loop: Header=BB0_25 Depth=1
	jmp	.LBB0_35
.LBB0_35:                               # %for.inc114
                                        #   in Loop: Header=BB0_25 Depth=1
	movl	-64392(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64388(%rbp)      # 4-byte Spill
	jmp	.LBB0_25
.LBB0_36:                               # %for.end116
	xorl	%eax, %eax
	movl	%eax, -64420(%rbp)      # 4-byte Spill
	jmp	.LBB0_37
.LBB0_37:                               # %for.cond117
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_39 Depth 2
	movl	-64420(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -64424(%rbp)      # 4-byte Spill
	jge	.LBB0_46
# %bb.38:                               # %for.body120
                                        #   in Loop: Header=BB0_37 Depth=1
	xorl	%eax, %eax
	movl	%eax, -64428(%rbp)      # 4-byte Spill
	jmp	.LBB0_39
.LBB0_39:                               # %for.cond121
                                        #   Parent Loop BB0_37 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-64428(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -64432(%rbp)      # 4-byte Spill
	jge	.LBB0_44
# %bb.40:                               # %for.body124
                                        #   in Loop: Header=BB0_39 Depth=2
	movl	-64424(%rbp), %eax      # 4-byte Reload
	imull	$80, %eax, %ecx
	movl	-64432(%rbp), %edx      # 4-byte Reload
	addl	%edx, %ecx
	movl	%ecx, %eax
	cltd
	movl	$20, %ecx
	idivl	%ecx
	cmpl	$0, %edx
	jne	.LBB0_42
# %bb.41:                               # %if.then
                                        #   in Loop: Header=BB0_39 Depth=2
	movq	stdout, %rdi
	movabsq	$.L.str.5, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -64436(%rbp)      # 4-byte Spill
.LBB0_42:                               # %if.end
                                        #   in Loop: Header=BB0_39 Depth=2
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-64424(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-64000(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-64432(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	cvtsi2sdl	%r8d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.6, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -64440(%rbp)      # 4-byte Spill
# %bb.43:                               # %for.inc134
                                        #   in Loop: Header=BB0_39 Depth=2
	movl	-64432(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64428(%rbp)      # 4-byte Spill
	jmp	.LBB0_39
.LBB0_44:                               # %for.end136
                                        #   in Loop: Header=BB0_37 Depth=1
	jmp	.LBB0_45
.LBB0_45:                               # %for.inc137
                                        #   in Loop: Header=BB0_37 Depth=1
	movl	-64424(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -64420(%rbp)      # 4-byte Spill
	jmp	.LBB0_37
.LBB0_46:                               # %for.end139
	xorl	%eax, %eax
	addq	$64448, %rsp            # imm = 0xFBC0
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
	.asciz	"\n"
	.size	.L.str.5, 2

	.type	.L.str.6,@object        # @.str.6
.L.str.6:
	.asciz	"%.16lf "
	.size	.L.str.6, 8


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym fprintf
	.addrsig_sym stdout
