	.text
	.file	"covariance.c"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI0_0:
	.quad	4755801206503243776     # double 8589934592
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
	pushq	%rbx
	subq	$96456, %rsp            # imm = 0x178C8
	.cfi_offset %rbx, -24
	xorl	%eax, %eax
	movl	%edi, -96340(%rbp)      # 4-byte Spill
	movq	%rsi, -96352(%rbp)      # 8-byte Spill
	movl	%eax, -96356(%rbp)      # 4-byte Spill
.LBB0_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
	movl	-96356(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -96360(%rbp)      # 4-byte Spill
	jge	.LBB0_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -96364(%rbp)      # 4-byte Spill
	jmp	.LBB0_3
.LBB0_3:                                # %for.cond9
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-96364(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -96368(%rbp)      # 4-byte Spill
	jge	.LBB0_6
# %bb.4:                                # %for.body12
                                        #   in Loop: Header=BB0_3 Depth=2
	movsd	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-96360(%rbp), %eax      # 4-byte Reload
	cvtsi2sdl	%eax, %xmm2
	movl	-96368(%rbp), %ecx      # 4-byte Reload
	cvtsi2sdl	%ecx, %xmm3
	mulsd	%xmm3, %xmm2
	divsd	%xmm1, %xmm2
	mulsd	%xmm2, %xmm0
	cvttsd2si	%xmm0, %edx
	movslq	%eax, %rsi
	imulq	$320, %rsi, %rsi        # imm = 0x140
	leaq	-32016(%rbp), %rdi
	addq	%rsi, %rdi
	movslq	%ecx, %rsi
	movl	%edx, (%rdi,%rsi,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-96368(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96364(%rbp)      # 4-byte Spill
	jmp	.LBB0_3
.LBB0_6:                                # %for.end
                                        #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_7
.LBB0_7:                                # %for.inc17
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-96360(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96356(%rbp)      # 4-byte Spill
	jmp	.LBB0_1
.LBB0_8:                                # %for.end19
	xorl	%eax, %eax
	movl	%eax, -96372(%rbp)      # 4-byte Spill
	jmp	.LBB0_9
.LBB0_9:                                # %for.cond20
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_11 Depth 2
	movl	-96372(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -96376(%rbp)      # 4-byte Spill
	jge	.LBB0_16
# %bb.10:                               # %for.body23
                                        #   in Loop: Header=BB0_9 Depth=1
	xorl	%eax, %eax
	movl	-96376(%rbp), %ecx      # 4-byte Reload
	movslq	%ecx, %rdx
	movl	$0, -96336(%rbp,%rdx,4)
	movl	%eax, -96380(%rbp)      # 4-byte Spill
.LBB0_11:                               # %for.cond26
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-96380(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -96384(%rbp)      # 4-byte Spill
	jge	.LBB0_14
# %bb.12:                               # %for.body29
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-96384(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-32016(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-96376(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%esi, %rcx
	movl	-96336(%rbp,%rcx,4), %r8d
	sarl	$1, %r8d
	addl	%edi, %r8d
	shll	$1, %r8d
	movl	%r8d, -96336(%rbp,%rcx,4)
# %bb.13:                               # %for.inc36
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-96384(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96380(%rbp)      # 4-byte Spill
	jmp	.LBB0_11
.LBB0_14:                               # %for.end38
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-96376(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movslq	-96336(%rbp,%rcx,4), %rdx
	movq	%rdx, %rax
	cqto
	movl	$100, %esi
	idivq	%rsi
	sarq	$1, %rax
	movl	%eax, %edi
	shll	$1, %edi
	movl	%edi, -96336(%rbp,%rcx,4)
# %bb.15:                               # %for.inc42
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-96376(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96372(%rbp)      # 4-byte Spill
	jmp	.LBB0_9
.LBB0_16:                               # %for.end44
	xorl	%eax, %eax
	movl	%eax, -96388(%rbp)      # 4-byte Spill
	jmp	.LBB0_17
.LBB0_17:                               # %for.cond45
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_19 Depth 2
	movl	-96388(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -96392(%rbp)      # 4-byte Spill
	jge	.LBB0_24
# %bb.18:                               # %for.body48
                                        #   in Loop: Header=BB0_17 Depth=1
	xorl	%eax, %eax
	movl	%eax, -96396(%rbp)      # 4-byte Spill
	jmp	.LBB0_19
.LBB0_19:                               # %for.cond49
                                        #   Parent Loop BB0_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-96396(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -96400(%rbp)      # 4-byte Spill
	jge	.LBB0_22
# %bb.20:                               # %for.body52
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-96400(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movl	-96336(%rbp,%rcx,4), %edx
	movl	-96392(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-32016(%rbp), %rdi
	addq	%rcx, %rdi
	movslq	%eax, %rcx
	movl	(%rdi,%rcx,4), %r8d
	sarl	$1, %edx
	subl	%edx, %r8d
	movl	%r8d, (%rdi,%rcx,4)
# %bb.21:                               # %for.inc59
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-96400(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96396(%rbp)      # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end61
                                        #   in Loop: Header=BB0_17 Depth=1
	jmp	.LBB0_23
.LBB0_23:                               # %for.inc62
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-96392(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96388(%rbp)      # 4-byte Spill
	jmp	.LBB0_17
.LBB0_24:                               # %for.end64
	xorl	%eax, %eax
	movl	%eax, -96404(%rbp)      # 4-byte Spill
	jmp	.LBB0_25
.LBB0_25:                               # %for.cond65
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_27 Depth 2
                                        #       Child Loop BB0_29 Depth 3
	movl	-96404(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -96408(%rbp)      # 4-byte Spill
	jge	.LBB0_36
# %bb.26:                               # %for.body68
                                        #   in Loop: Header=BB0_25 Depth=1
	movl	-96408(%rbp), %eax      # 4-byte Reload
	movl	%eax, -96412(%rbp)      # 4-byte Spill
	jmp	.LBB0_27
.LBB0_27:                               # %for.cond69
                                        #   Parent Loop BB0_25 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_29 Depth 3
	movl	-96412(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -96416(%rbp)      # 4-byte Spill
	jge	.LBB0_34
# %bb.28:                               # %for.body72
                                        #   in Loop: Header=BB0_27 Depth=2
	xorl	%eax, %eax
	movl	-96408(%rbp), %ecx      # 4-byte Reload
	movslq	%ecx, %rdx
	imulq	$640, %rdx, %rdx        # imm = 0x280
	leaq	-96016(%rbp), %rsi
	addq	%rdx, %rsi
	movl	-96416(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rdx
	movq	$0, (%rsi,%rdx,8)
	movl	%eax, -96420(%rbp)      # 4-byte Spill
.LBB0_29:                               # %for.cond77
                                        #   Parent Loop BB0_25 Depth=1
                                        #     Parent Loop BB0_27 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-96420(%rbp), %eax      # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -96424(%rbp)      # 4-byte Spill
	jge	.LBB0_32
# %bb.30:                               # %for.body80
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	-96424(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	leaq	-32016(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-96408(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%eax, %rcx
	imulq	$320, %rcx, %rcx        # imm = 0x140
	addq	%rcx, %rdx
	movl	-96416(%rbp), %r9d      # 4-byte Reload
	movslq	%r9d, %rcx
	movl	(%rdx,%rcx,4), %r10d
	movslq	%r8d, %rcx
	movslq	%r10d, %rdx
	imulq	%rdx, %rcx
	sarq	$30, %rcx
	movl	%ecx, %r8d
	movslq	%edi, %rcx
	imulq	$640, %rcx, %rcx        # imm = 0x280
	leaq	-96016(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%r9d, %rcx
	movq	(%rdx,%rcx,8), %rsi
	movslq	%r8d, %r11
	shlq	$29, %r11
	addq	%r11, %rsi
	movq	%rsi, (%rdx,%rcx,8)
# %bb.31:                               # %for.inc95
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	-96424(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96420(%rbp)      # 4-byte Spill
	jmp	.LBB0_29
.LBB0_32:                               # %for.end97
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-96408(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	leaq	(%rcx,%rcx,4), %rcx
	shlq	$7, %rcx
	leaq	-96016(%rbp,%rcx), %rcx
	movl	-96416(%rbp), %edx      # 4-byte Reload
	movslq	%edx, %rsi
	movq	%rsi, %rdi
	movq	(%rcx,%rsi,8), %rsi
	movq	%rsi, %r8
	sarq	$63, %r8
	xorl	%r9d, %r9d
	movl	%r9d, %r10d
	movl	$99, %r11d
	movq	%rdi, -96432(%rbp)      # 8-byte Spill
	movq	%rsi, %rdi
	movq	%r8, %rsi
	movq	%r11, %rdx
	movq	%rcx, -96440(%rbp)      # 8-byte Spill
	movq	%r10, %rcx
	callq	__divti3
	shrq	$26, %rax
	movl	%eax, %r9d
	movslq	%r9d, %rax
	shlq	$26, %rax
	movq	-96440(%rbp), %rcx      # 8-byte Reload
	movq	-96432(%rbp), %rdx      # 8-byte Reload
	movq	%rax, (%rcx,%rdx,8)
	movl	-96408(%rbp), %r9d      # 4-byte Reload
	movslq	%r9d, %rax
	imulq	$640, %rax, %rax        # imm = 0x280
	leaq	-96016(%rbp), %rsi
	movq	%rsi, %rdi
	addq	%rax, %rdi
	movl	-96416(%rbp), %ebx      # 4-byte Reload
	movslq	%ebx, %rax
	movq	(%rdi,%rax,8), %rax
	movslq	%ebx, %rdi
	imulq	$640, %rdi, %rdi        # imm = 0x280
	addq	%rdi, %rsi
	movslq	%r9d, %rdi
	movq	%rax, (%rsi,%rdi,8)
# %bb.33:                               # %for.inc111
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-96416(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96412(%rbp)      # 4-byte Spill
	jmp	.LBB0_27
.LBB0_34:                               # %for.end113
                                        #   in Loop: Header=BB0_25 Depth=1
	jmp	.LBB0_35
.LBB0_35:                               # %for.inc114
                                        #   in Loop: Header=BB0_25 Depth=1
	movl	-96408(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96404(%rbp)      # 4-byte Spill
	jmp	.LBB0_25
.LBB0_36:                               # %for.end116
	xorl	%eax, %eax
	movl	%eax, -96444(%rbp)      # 4-byte Spill
	jmp	.LBB0_37
.LBB0_37:                               # %for.cond117
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_39 Depth 2
	movl	-96444(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -96448(%rbp)      # 4-byte Spill
	jge	.LBB0_46
# %bb.38:                               # %for.body120
                                        #   in Loop: Header=BB0_37 Depth=1
	xorl	%eax, %eax
	movl	%eax, -96452(%rbp)      # 4-byte Spill
	jmp	.LBB0_39
.LBB0_39:                               # %for.cond121
                                        #   Parent Loop BB0_37 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-96452(%rbp), %eax      # 4-byte Reload
	cmpl	$80, %eax
	movl	%eax, -96456(%rbp)      # 4-byte Spill
	jge	.LBB0_44
# %bb.40:                               # %for.body124
                                        #   in Loop: Header=BB0_39 Depth=2
	movl	-96448(%rbp), %eax      # 4-byte Reload
	imull	$80, %eax, %ecx
	movl	-96456(%rbp), %edx      # 4-byte Reload
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
	movl	%eax, -96460(%rbp)      # 4-byte Spill
.LBB0_42:                               # %if.end
                                        #   in Loop: Header=BB0_39 Depth=2
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-96448(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$640, %rcx, %rcx        # imm = 0x280
	leaq	-96016(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-96456(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	movq	(%rdx,%rcx,8), %rcx
	cvtsi2sdq	%rcx, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.6, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -96464(%rbp)      # 4-byte Spill
# %bb.43:                               # %for.inc134
                                        #   in Loop: Header=BB0_39 Depth=2
	movl	-96456(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96452(%rbp)      # 4-byte Spill
	jmp	.LBB0_39
.LBB0_44:                               # %for.end136
                                        #   in Loop: Header=BB0_37 Depth=1
	jmp	.LBB0_45
.LBB0_45:                               # %for.inc137
                                        #   in Loop: Header=BB0_37 Depth=1
	movl	-96448(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -96444(%rbp)      # 4-byte Spill
	jmp	.LBB0_37
.LBB0_46:                               # %for.end139
	xorl	%eax, %eax
	addq	$96456, %rsp            # imm = 0x178C8
	popq	%rbx
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
