	.text
	.file	"heat-3d.c"
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function main
.LCPI0_0:
	.long	1040187392              # float 0.125
.LCPI0_1:
	.long	1073741824              # float 2
.LCPI0_2:
	.long	1283457024              # float 67108864
.LCPI0_3:
	.long	1065353216              # float 1
.LCPI0_4:
	.long	1092616192              # float 10
.LCPI0_5:
	.long	1241513984              # float 2097152
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
	subq	$512112, %rsp           # imm = 0x7D070
	xorl	%eax, %eax
	movl	%eax, -512004(%rbp)     # 4-byte Spill
.LBB0_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
                                        #       Child Loop BB0_5 Depth 3
	movl	-512004(%rbp), %eax     # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -512008(%rbp)     # 4-byte Spill
	jge	.LBB0_12
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -512012(%rbp)     # 4-byte Spill
	jmp	.LBB0_3
.LBB0_3:                                # %for.cond7
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_5 Depth 3
	movl	-512012(%rbp), %eax     # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -512016(%rbp)     # 4-byte Spill
	jge	.LBB0_10
# %bb.4:                                # %for.body9
                                        #   in Loop: Header=BB0_3 Depth=2
	xorl	%eax, %eax
	movl	%eax, -512020(%rbp)     # 4-byte Spill
	jmp	.LBB0_5
.LBB0_5:                                # %for.cond10
                                        #   Parent Loop BB0_1 Depth=1
                                        #     Parent Loop BB0_3 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-512020(%rbp), %eax     # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -512024(%rbp)     # 4-byte Spill
	jge	.LBB0_8
# %bb.6:                                # %for.body12
                                        #   in Loop: Header=BB0_5 Depth=3
	movss	.LCPI0_2(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	-512008(%rbp), %eax     # 4-byte Reload
	movl	-512016(%rbp), %ecx     # 4-byte Reload
	addl	%ecx, %eax
	movl	$40, %edx
	movl	-512024(%rbp), %esi     # 4-byte Reload
	subl	%esi, %edx
	addl	%edx, %eax
	cvtsi2ssl	%eax, %xmm1
	movss	.LCPI0_3(%rip), %xmm2   # xmm2 = mem[0],zero,zero,zero
	divss	%xmm2, %xmm1
	movss	.LCPI0_4(%rip), %xmm2   # xmm2 = mem[0],zero,zero,zero
	mulss	%xmm2, %xmm1
	movss	.LCPI0_5(%rip), %xmm2   # xmm2 = mem[0],zero,zero,zero
	mulss	%xmm2, %xmm1
	cvttss2si	%xmm1, %rdi
	movl	%edi, %eax
	movl	%eax, %eax
                                        # kill: def $rax killed $eax
	movabsq	$-3689348814741910323, %rdi # imm = 0xCCCCCCCCCCCCCCCD
	mulq	%rdi
	movl	%edx, %r8d
	andl	$-32, %r8d
	movl	%r8d, %eax
	cvtsi2ssq	%rax, %xmm1
	movss	.LCPI0_2(%rip), %xmm2   # xmm2 = mem[0],zero,zero,zero
	movaps	%xmm1, %xmm3
	divss	%xmm2, %xmm3
	divss	%xmm0, %xmm1
	movl	-512008(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rax
	imulq	$6400, %rax, %rax       # imm = 0x1900
	leaq	-512000(%rbp), %rdx
	addq	%rax, %rdx
	movslq	%ecx, %rax
	imulq	$160, %rax, %rax
	addq	%rax, %rdx
	movslq	%esi, %rax
	movss	%xmm3, (%rdx,%rax,4)
	movslq	%r8d, %rax
	imulq	$6400, %rax, %rax       # imm = 0x1900
	leaq	-256000(%rbp), %rdx
	addq	%rax, %rdx
	movslq	%ecx, %rax
	imulq	$160, %rax, %rax
	addq	%rax, %rdx
	movslq	%esi, %rax
	movss	%xmm1, (%rdx,%rax,4)
# %bb.7:                                # %for.inc
                                        #   in Loop: Header=BB0_5 Depth=3
	movl	-512024(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512020(%rbp)     # 4-byte Spill
	jmp	.LBB0_5
.LBB0_8:                                # %for.end
                                        #   in Loop: Header=BB0_3 Depth=2
	jmp	.LBB0_9
.LBB0_9:                                # %for.inc25
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-512016(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512012(%rbp)     # 4-byte Spill
	jmp	.LBB0_3
.LBB0_10:                               # %for.end27
                                        #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_11
.LBB0_11:                               # %for.inc28
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-512008(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512004(%rbp)     # 4-byte Spill
	jmp	.LBB0_1
.LBB0_12:                               # %for.end30
	movl	$1, %eax
	movl	%eax, -512028(%rbp)     # 4-byte Spill
	jmp	.LBB0_13
.LBB0_13:                               # %for.cond31
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_15 Depth 2
                                        #       Child Loop BB0_17 Depth 3
                                        #         Child Loop BB0_19 Depth 4
                                        #     Child Loop BB0_27 Depth 2
                                        #       Child Loop BB0_29 Depth 3
                                        #         Child Loop BB0_31 Depth 4
	movl	-512028(%rbp), %eax     # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -512032(%rbp)     # 4-byte Spill
	jg	.LBB0_40
# %bb.14:                               # %for.body34
                                        #   in Loop: Header=BB0_13 Depth=1
	movl	$1, %eax
	movl	%eax, -512036(%rbp)     # 4-byte Spill
	jmp	.LBB0_15
.LBB0_15:                               # %for.cond35
                                        #   Parent Loop BB0_13 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_17 Depth 3
                                        #         Child Loop BB0_19 Depth 4
	movl	-512036(%rbp), %eax     # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -512040(%rbp)     # 4-byte Spill
	jge	.LBB0_26
# %bb.16:                               # %for.body38
                                        #   in Loop: Header=BB0_15 Depth=2
	movl	$1, %eax
	movl	%eax, -512044(%rbp)     # 4-byte Spill
	jmp	.LBB0_17
.LBB0_17:                               # %for.cond39
                                        #   Parent Loop BB0_13 Depth=1
                                        #     Parent Loop BB0_15 Depth=2
                                        # =>    This Loop Header: Depth=3
                                        #         Child Loop BB0_19 Depth 4
	movl	-512044(%rbp), %eax     # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -512048(%rbp)     # 4-byte Spill
	jge	.LBB0_24
# %bb.18:                               # %for.body42
                                        #   in Loop: Header=BB0_17 Depth=3
	movl	$1, %eax
	movl	%eax, -512052(%rbp)     # 4-byte Spill
	jmp	.LBB0_19
.LBB0_19:                               # %for.cond43
                                        #   Parent Loop BB0_13 Depth=1
                                        #     Parent Loop BB0_15 Depth=2
                                        #       Parent Loop BB0_17 Depth=3
                                        # =>      This Inner Loop Header: Depth=4
	movl	-512052(%rbp), %eax     # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -512056(%rbp)     # 4-byte Spill
	jge	.LBB0_22
# %bb.20:                               # %for.body46
                                        #   in Loop: Header=BB0_19 Depth=4
	movss	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI0_1(%rip), %xmm1   # xmm1 = mem[0],zero,zero,zero
	movl	-512040(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	leaq	-256000(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-512048(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-512056(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm2    # xmm2 = mem[0],zero,zero,zero
	movl	-512040(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movaps	%xmm1, %xmm3
	mulss	(%rsi,%rcx,4), %xmm3
	subss	%xmm3, %xmm2
	subl	$1, %r8d
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	addss	(%rsi,%rcx,4), %xmm2
	movaps	%xmm0, %xmm3
	mulss	%xmm2, %xmm3
	movl	-512040(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm2    # xmm2 = mem[0],zero,zero,zero
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-512048(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movaps	%xmm1, %xmm4
	mulss	(%rsi,%rcx,4), %xmm4
	subss	%xmm4, %xmm2
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	subl	$1, %eax
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	addss	(%rsi,%rcx,4), %xmm2
	movaps	%xmm0, %xmm4
	mulss	%xmm2, %xmm4
	addss	%xmm4, %xmm3
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-512048(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	addl	$1, %edi
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm2    # xmm2 = mem[0],zero,zero,zero
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-512056(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	mulss	(%rsi,%rcx,4), %xmm1
	subss	%xmm1, %xmm2
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	subl	$1, %edi
	movslq	%edi, %rcx
	addss	(%rsi,%rcx,4), %xmm2
	mulss	%xmm2, %xmm0
	addss	%xmm0, %xmm3
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-512056(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	addss	(%rdx,%rcx,4), %xmm3
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	leaq	-512000(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movss	%xmm3, (%rdx,%rcx,4)
# %bb.21:                               # %for.inc134
                                        #   in Loop: Header=BB0_19 Depth=4
	movl	-512056(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512052(%rbp)     # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end136
                                        #   in Loop: Header=BB0_17 Depth=3
	jmp	.LBB0_23
.LBB0_23:                               # %for.inc137
                                        #   in Loop: Header=BB0_17 Depth=3
	movl	-512048(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512044(%rbp)     # 4-byte Spill
	jmp	.LBB0_17
.LBB0_24:                               # %for.end139
                                        #   in Loop: Header=BB0_15 Depth=2
	jmp	.LBB0_25
.LBB0_25:                               # %for.inc140
                                        #   in Loop: Header=BB0_15 Depth=2
	movl	-512040(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512036(%rbp)     # 4-byte Spill
	jmp	.LBB0_15
.LBB0_26:                               # %for.end142
                                        #   in Loop: Header=BB0_13 Depth=1
	movl	$1, %eax
	movl	%eax, -512060(%rbp)     # 4-byte Spill
	jmp	.LBB0_27
.LBB0_27:                               # %for.cond143
                                        #   Parent Loop BB0_13 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_29 Depth 3
                                        #         Child Loop BB0_31 Depth 4
	movl	-512060(%rbp), %eax     # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -512064(%rbp)     # 4-byte Spill
	jge	.LBB0_38
# %bb.28:                               # %for.body146
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	$1, %eax
	movl	%eax, -512068(%rbp)     # 4-byte Spill
	jmp	.LBB0_29
.LBB0_29:                               # %for.cond147
                                        #   Parent Loop BB0_13 Depth=1
                                        #     Parent Loop BB0_27 Depth=2
                                        # =>    This Loop Header: Depth=3
                                        #         Child Loop BB0_31 Depth 4
	movl	-512068(%rbp), %eax     # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -512072(%rbp)     # 4-byte Spill
	jge	.LBB0_36
# %bb.30:                               # %for.body150
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	$1, %eax
	movl	%eax, -512076(%rbp)     # 4-byte Spill
	jmp	.LBB0_31
.LBB0_31:                               # %for.cond151
                                        #   Parent Loop BB0_13 Depth=1
                                        #     Parent Loop BB0_27 Depth=2
                                        #       Parent Loop BB0_29 Depth=3
                                        # =>      This Inner Loop Header: Depth=4
	movl	-512076(%rbp), %eax     # 4-byte Reload
	cmpl	$39, %eax
	movl	%eax, -512080(%rbp)     # 4-byte Spill
	jge	.LBB0_34
# %bb.32:                               # %for.body154
                                        #   in Loop: Header=BB0_31 Depth=4
	movss	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI0_1(%rip), %xmm1   # xmm1 = mem[0],zero,zero,zero
	movl	-512064(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	leaq	-512000(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-512072(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-512080(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm2    # xmm2 = mem[0],zero,zero,zero
	movl	-512064(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movaps	%xmm1, %xmm3
	mulss	(%rsi,%rcx,4), %xmm3
	subss	%xmm3, %xmm2
	subl	$1, %r8d
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	addss	(%rsi,%rcx,4), %xmm2
	movaps	%xmm0, %xmm3
	mulss	%xmm2, %xmm3
	movl	-512064(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	addl	$1, %eax
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm2    # xmm2 = mem[0],zero,zero,zero
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-512072(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	movaps	%xmm1, %xmm4
	mulss	(%rsi,%rcx,4), %xmm4
	subss	%xmm4, %xmm2
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	subl	$1, %eax
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movslq	%edi, %rcx
	addss	(%rsi,%rcx,4), %xmm2
	movaps	%xmm0, %xmm4
	mulss	%xmm2, %xmm4
	addss	%xmm4, %xmm3
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-512072(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	addl	$1, %edi
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm2    # xmm2 = mem[0],zero,zero,zero
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	movl	-512080(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	mulss	(%rsi,%rcx,4), %xmm1
	subss	%xmm1, %xmm2
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rsi
	subl	$1, %edi
	movslq	%edi, %rcx
	addss	(%rsi,%rcx,4), %xmm2
	mulss	%xmm2, %xmm0
	addss	%xmm0, %xmm3
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-512080(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	addss	(%rdx,%rcx,4), %xmm3
	movslq	%r8d, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	leaq	-256000(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movss	%xmm3, (%rdx,%rcx,4)
# %bb.33:                               # %for.inc242
                                        #   in Loop: Header=BB0_31 Depth=4
	movl	-512080(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512076(%rbp)     # 4-byte Spill
	jmp	.LBB0_31
.LBB0_34:                               # %for.end244
                                        #   in Loop: Header=BB0_29 Depth=3
	jmp	.LBB0_35
.LBB0_35:                               # %for.inc245
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	-512072(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512068(%rbp)     # 4-byte Spill
	jmp	.LBB0_29
.LBB0_36:                               # %for.end247
                                        #   in Loop: Header=BB0_27 Depth=2
	jmp	.LBB0_37
.LBB0_37:                               # %for.inc248
                                        #   in Loop: Header=BB0_27 Depth=2
	movl	-512064(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512060(%rbp)     # 4-byte Spill
	jmp	.LBB0_27
.LBB0_38:                               # %for.end250
                                        #   in Loop: Header=BB0_13 Depth=1
	jmp	.LBB0_39
.LBB0_39:                               # %for.inc251
                                        #   in Loop: Header=BB0_13 Depth=1
	movl	-512032(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512028(%rbp)     # 4-byte Spill
	jmp	.LBB0_13
.LBB0_40:                               # %for.end253
	xorl	%eax, %eax
	movl	%eax, -512084(%rbp)     # 4-byte Spill
	jmp	.LBB0_41
.LBB0_41:                               # %for.cond254
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_43 Depth 2
                                        #       Child Loop BB0_45 Depth 3
	movl	-512084(%rbp), %eax     # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -512088(%rbp)     # 4-byte Spill
	jge	.LBB0_54
# %bb.42:                               # %for.body257
                                        #   in Loop: Header=BB0_41 Depth=1
	xorl	%eax, %eax
	movl	%eax, -512092(%rbp)     # 4-byte Spill
	jmp	.LBB0_43
.LBB0_43:                               # %for.cond258
                                        #   Parent Loop BB0_41 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_45 Depth 3
	movl	-512092(%rbp), %eax     # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -512096(%rbp)     # 4-byte Spill
	jge	.LBB0_52
# %bb.44:                               # %for.body261
                                        #   in Loop: Header=BB0_43 Depth=2
	xorl	%eax, %eax
	movl	%eax, -512100(%rbp)     # 4-byte Spill
	jmp	.LBB0_45
.LBB0_45:                               # %for.cond262
                                        #   Parent Loop BB0_41 Depth=1
                                        #     Parent Loop BB0_43 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-512100(%rbp), %eax     # 4-byte Reload
	cmpl	$40, %eax
	movl	%eax, -512104(%rbp)     # 4-byte Spill
	jge	.LBB0_50
# %bb.46:                               # %for.body265
                                        #   in Loop: Header=BB0_45 Depth=3
	movl	-512088(%rbp), %eax     # 4-byte Reload
	imull	$40, %eax, %ecx
	imull	$40, %ecx, %ecx
	movl	-512096(%rbp), %edx     # 4-byte Reload
	imull	$40, %edx, %esi
	addl	%esi, %ecx
	movl	-512104(%rbp), %esi     # 4-byte Reload
	addl	%esi, %ecx
	movl	%ecx, %eax
	cltd
	movl	$20, %ecx
	idivl	%ecx
	cmpl	$0, %edx
	jne	.LBB0_48
# %bb.47:                               # %if.then
                                        #   in Loop: Header=BB0_45 Depth=3
	movq	stdout, %rdi
	movabsq	$.L.str.3, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -512108(%rbp)     # 4-byte Spill
.LBB0_48:                               # %if.end
                                        #   in Loop: Header=BB0_45 Depth=3
	movq	stdout, %rdi
	movl	-512088(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$6400, %rcx, %rcx       # imm = 0x1900
	leaq	-256000(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-512096(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	imulq	$160, %rcx, %rcx
	addq	%rcx, %rdx
	movl	-512104(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rcx
	movss	(%rdx,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	movabsq	$.L.str.4, %rcx
	movq	%rcx, %rsi
	movb	$1, %al
	callq	fprintf
	movl	%eax, -512112(%rbp)     # 4-byte Spill
# %bb.49:                               # %for.inc280
                                        #   in Loop: Header=BB0_45 Depth=3
	movl	-512104(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512100(%rbp)     # 4-byte Spill
	jmp	.LBB0_45
.LBB0_50:                               # %for.end282
                                        #   in Loop: Header=BB0_43 Depth=2
	jmp	.LBB0_51
.LBB0_51:                               # %for.inc283
                                        #   in Loop: Header=BB0_43 Depth=2
	movl	-512096(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512092(%rbp)     # 4-byte Spill
	jmp	.LBB0_43
.LBB0_52:                               # %for.end285
                                        #   in Loop: Header=BB0_41 Depth=1
	jmp	.LBB0_53
.LBB0_53:                               # %for.inc286
                                        #   in Loop: Header=BB0_41 Depth=1
	movl	-512088(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -512084(%rbp)     # 4-byte Spill
	jmp	.LBB0_41
.LBB0_54:                               # %for.end288
	xorl	%eax, %eax
	addq	$512112, %rsp           # imm = 0x7D070
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.L.str.3,@object        # @.str.3
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str.3:
	.asciz	"\n"
	.size	.L.str.3, 2

	.type	.L.str.4,@object        # @.str.4
.L.str.4:
	.asciz	"%0.16lf "
	.size	.L.str.4, 9


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym fprintf
	.addrsig_sym stdout
