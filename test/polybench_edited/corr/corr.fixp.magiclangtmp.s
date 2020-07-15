	.text
	.file	"corr.c"
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function main
.LCPI0_0:
	.long	1065353216              # float 1
.LCPI0_1:
	.long	1308622848              # float 536870912
.LCPI0_2:
	.long	1317011456              # float 1.07374182E+9
.LCPI0_3:
	.long	1216348160              # float 262144
.LCPI0_6:
	.long	1191182336              # float 32768
.LCPI0_7:
	.long	1036831949              # float 0.100000001
.LCPI0_8:
	.long	1233125376              # float 1048576
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3
.LCPI0_4:
	.quad	4688247212092686336     # double 262144
.LCPI0_5:
	.quad	4628574517030027264     # double 28
.LCPI0_9:
	.quad	4629700416936869888     # double 32
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
	subq	$8096, %rsp             # imm = 0x1FA0
	xorl	%eax, %eax
	movl	%eax, -7940(%rbp)       # 4-byte Spill
.LBB0_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
	movl	-7940(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -7944(%rbp)       # 4-byte Spill
	jge	.LBB0_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -7948(%rbp)       # 4-byte Spill
	jmp	.LBB0_3
.LBB0_3:                                # %for.cond9
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-7948(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -7952(%rbp)       # 4-byte Spill
	jge	.LBB0_6
# %bb.4:                                # %for.body11
                                        #   in Loop: Header=BB0_3 Depth=2
	movsd	.LCPI0_5(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_9(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-7944(%rbp), %eax       # 4-byte Reload
	movl	-7952(%rbp), %ecx       # 4-byte Reload
	imull	%ecx, %eax
	cvtsi2sdl	%eax, %xmm2
	divsd	%xmm1, %xmm2
	movl	-7944(%rbp), %eax       # 4-byte Reload
	cvtsi2sdl	%eax, %xmm1
	addsd	%xmm1, %xmm2
	divsd	%xmm0, %xmm2
	cvtsd2ss	%xmm2, %xmm0
	movslq	%eax, %rdx
	shlq	$7, %rdx
	leaq	-3712(%rbp), %rsi
	addq	%rdx, %rsi
	movslq	%ecx, %rdx
	movss	%xmm0, (%rsi,%rdx,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-7952(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7948(%rbp)       # 4-byte Spill
	jmp	.LBB0_3
.LBB0_6:                                # %for.end
                                        #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_7
.LBB0_7:                                # %for.inc16
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-7944(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7940(%rbp)       # 4-byte Spill
	jmp	.LBB0_1
.LBB0_8:                                # %for.end18
	xorl	%eax, %eax
	movl	%eax, -7956(%rbp)       # 4-byte Spill
	jmp	.LBB0_9
.LBB0_9:                                # %for.cond20
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_11 Depth 2
	movl	-7956(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -7960(%rbp)       # 4-byte Spill
	jge	.LBB0_16
# %bb.10:                               # %for.body23
                                        #   in Loop: Header=BB0_9 Depth=1
	xorl	%eax, %eax
	movl	-7960(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	movl	$0, -128(%rbp,%rdx,4)
	movl	%eax, -7964(%rbp)       # 4-byte Spill
.LBB0_11:                               # %for.cond26
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-7964(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -7968(%rbp)       # 4-byte Spill
	jge	.LBB0_14
# %bb.12:                               # %for.body29
                                        #   in Loop: Header=BB0_11 Depth=2
	movss	.LCPI0_6(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	-7968(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-7960(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	movss	(%rdx,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	movslq	%esi, %rcx
	movl	-128(%rbp,%rcx,4), %edi
	mulss	%xmm1, %xmm0
	cvttss2si	%xmm0, %r8d
	addl	%r8d, %edi
	movl	%edi, -128(%rbp,%rcx,4)
# %bb.13:                               # %for.inc37
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-7968(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7964(%rbp)       # 4-byte Spill
	jmp	.LBB0_11
.LBB0_14:                               # %for.end39
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-7960(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movslq	-128(%rbp,%rcx,4), %rdx
	movq	%rdx, %rax
	xorl	%esi, %esi
	movl	%esi, %edx
	movl	$28, %edi
	divq	%rdi
	shlq	$5, %rax
	movl	%eax, %esi
	shrl	$5, %esi
	movl	%esi, -128(%rbp,%rcx,4)
# %bb.15:                               # %for.inc43
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-7960(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7956(%rbp)       # 4-byte Spill
	jmp	.LBB0_9
.LBB0_16:                               # %for.end45
	xorl	%eax, %eax
	movl	%eax, -7972(%rbp)       # 4-byte Spill
	jmp	.LBB0_17
.LBB0_17:                               # %for.cond46
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_19 Depth 2
	movl	-7972(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -7976(%rbp)       # 4-byte Spill
	jge	.LBB0_27
# %bb.18:                               # %for.body49
                                        #   in Loop: Header=BB0_17 Depth=1
	xorl	%eax, %eax
	movl	-7976(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	xorps	%xmm0, %xmm0
	movss	%xmm0, -7936(%rbp,%rdx,4)
	movl	%eax, -7980(%rbp)       # 4-byte Spill
.LBB0_19:                               # %for.cond52
                                        #   Parent Loop BB0_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-7980(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -7984(%rbp)       # 4-byte Spill
	jge	.LBB0_22
# %bb.20:                               # %for.body55
                                        #   in Loop: Header=BB0_19 Depth=2
	movss	.LCPI0_6(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	-7984(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-7976(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	movslq	%edi, %rcx
	movl	-128(%rbp,%rcx,4), %r8d
	movaps	%xmm0, %xmm2
	mulss	%xmm1, %xmm2
	cvttss2si	%xmm2, %r9d
	subl	%r8d, %r9d
	movslq	%eax, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movss	(%rdx,%rcx,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	movslq	%edi, %rcx
	movl	-128(%rbp,%rcx,4), %r8d
	movaps	%xmm0, %xmm2
	mulss	%xmm1, %xmm2
	cvttss2si	%xmm2, %r10d
	subl	%r8d, %r10d
	movslq	%r9d, %rcx
	movslq	%r10d, %rdx
	imulq	%rdx, %rcx
	sarq	$15, %rcx
	movl	%ecx, %r8d
	cvtsi2ssl	%r8d, %xmm1
	divss	%xmm0, %xmm1
	movslq	%edi, %rcx
	addss	-7936(%rbp,%rcx,4), %xmm1
	movss	%xmm1, -7936(%rbp,%rcx,4)
# %bb.21:                               # %for.inc73
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-7984(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7980(%rbp)       # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end75
                                        #   in Loop: Header=BB0_17 Depth=1
	movss	.LCPI0_7(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI0_8(%rip), %xmm1   # xmm1 = mem[0],zero,zero,zero
	movl	-7976(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movq	%rcx, %rdx
	movss	-7936(%rbp,%rcx,4), %xmm2 # xmm2 = mem[0],zero,zero,zero
	movss	.LCPI0_8(%rip), %xmm3   # xmm3 = mem[0],zero,zero,zero
	mulss	%xmm3, %xmm2
	cvttss2si	%xmm2, %rcx
	movl	%ecx, %esi
	movl	%esi, %esi
	movl	%esi, %ecx
	shrq	$2, %rcx
	movabsq	$5270498306774157605, %rdi # imm = 0x4924924924924925
	movq	%rcx, %rax
	movq	%rdx, -7992(%rbp)       # 8-byte Spill
	mulq	%rdi
	shrq	%rdx
	movl	%edx, %esi
	cvtsi2ssl	%esi, %xmm2
	divss	%xmm1, %xmm2
	movq	-7992(%rbp), %rax       # 8-byte Reload
	movss	%xmm2, -7936(%rbp,%rax,4)
	movl	-7976(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm1 # xmm1 = mem[0],zero,zero,zero
	cvtss2sd	%xmm1, %xmm1
	movss	%xmm0, -7996(%rbp)      # 4-byte Spill
	movaps	%xmm1, %xmm0
	callq	sqrt
	movl	-7976(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rax
	cvtsd2ss	%xmm0, %xmm0
	movss	%xmm0, -7936(%rbp,%rax,4)
	movslq	%esi, %rax
	movss	-7996(%rbp), %xmm0      # 4-byte Reload
                                        # xmm0 = mem[0],zero,zero,zero
	ucomiss	-7936(%rbp,%rax,4), %xmm0
	jb	.LBB0_24
# %bb.23:                               # %cond.true
                                        #   in Loop: Header=BB0_17 Depth=1
	movss	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, -8000(%rbp)      # 4-byte Spill
	jmp	.LBB0_25
.LBB0_24:                               # %cond.false
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-7976(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm0 # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, -8000(%rbp)      # 4-byte Spill
.LBB0_25:                               # %cond.end
                                        #   in Loop: Header=BB0_17 Depth=1
	movss	-8000(%rbp), %xmm0      # 4-byte Reload
                                        # xmm0 = mem[0],zero,zero,zero
	movl	-7976(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	%xmm0, -7936(%rbp,%rcx,4)
# %bb.26:                               # %for.inc91
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-7976(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7972(%rbp)       # 4-byte Spill
	jmp	.LBB0_17
.LBB0_27:                               # %for.end93
	xorl	%eax, %eax
	movl	%eax, -8004(%rbp)       # 4-byte Spill
	jmp	.LBB0_28
.LBB0_28:                               # %for.cond94
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_30 Depth 2
	movl	-8004(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -8008(%rbp)       # 4-byte Spill
	jge	.LBB0_35
# %bb.29:                               # %for.body97
                                        #   in Loop: Header=BB0_28 Depth=1
	xorl	%eax, %eax
	movl	%eax, -8012(%rbp)       # 4-byte Spill
	jmp	.LBB0_30
.LBB0_30:                               # %for.cond98
                                        #   Parent Loop BB0_28 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-8012(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8016(%rbp)       # 4-byte Spill
	jge	.LBB0_33
# %bb.31:                               # %for.body101
                                        #   in Loop: Header=BB0_30 Depth=2
	movss	.LCPI0_2(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	.LCPI0_3(%rip), %xmm1   # xmm1 = mem[0],zero,zero,zero
	movsd	.LCPI0_4(%rip), %xmm2   # xmm2 = mem[0],zero
	movss	.LCPI0_6(%rip), %xmm3   # xmm3 = mem[0],zero,zero,zero
	movl	-8016(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movl	-128(%rbp,%rcx,4), %edx
	movl	-8008(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdi
	movq	%rdi, %r8
	addq	%rcx, %r8
	movslq	%eax, %rcx
	movaps	%xmm3, %xmm4
	mulss	(%r8,%rcx,4), %xmm4
	cvttss2si	%xmm4, %r9d
	subl	%edx, %r9d
	cvtsi2ssl	%r9d, %xmm4
	divss	%xmm3, %xmm4
	movss	%xmm4, (%r8,%rcx,4)
	movsd	.LCPI0_5(%rip), %xmm3   # xmm3 = mem[0],zero
	movss	%xmm0, -8020(%rbp)      # 4-byte Spill
	movaps	%xmm3, %xmm0
	movss	%xmm1, -8024(%rbp)      # 4-byte Spill
	movsd	%xmm2, -8032(%rbp)      # 8-byte Spill
	movq	%rdi, -8040(%rbp)       # 8-byte Spill
	callq	sqrt
	movl	-8016(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movss	-7936(%rbp,%rcx,4), %xmm1 # xmm1 = mem[0],zero,zero,zero
	movsd	-8032(%rbp), %xmm2      # 8-byte Reload
                                        # xmm2 = mem[0],zero
	mulsd	%xmm0, %xmm2
	cvttsd2si	%xmm2, %edx
	movss	-8024(%rbp), %xmm0      # 4-byte Reload
                                        # xmm0 = mem[0],zero,zero,zero
	mulss	%xmm1, %xmm0
	cvttss2si	%xmm0, %esi
	movslq	%edx, %rcx
	movslq	%esi, %rdi
	imulq	%rdi, %rcx
	sarq	$18, %rcx
	movl	%ecx, %edx
	movl	-8008(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	shlq	$7, %rcx
	movq	-8040(%rbp), %rdi       # 8-byte Reload
	addq	%rcx, %rdi
	movslq	%eax, %rcx
	movss	-8020(%rbp), %xmm0      # 4-byte Reload
                                        # xmm0 = mem[0],zero,zero,zero
	mulss	(%rdi,%rcx,4), %xmm0
	cvttss2si	%xmm0, %r9d
	movslq	%r9d, %r8
	shlq	$18, %r8
	movslq	%edx, %r10
	movq	%r8, %rax
	cqto
	idivq	%r10
	movl	%eax, %r9d
	cvtsi2ssl	%r9d, %xmm0
	movss	-8020(%rbp), %xmm1      # 4-byte Reload
                                        # xmm1 = mem[0],zero,zero,zero
	divss	%xmm1, %xmm0
	movss	%xmm0, (%rdi,%rcx,4)
# %bb.32:                               # %for.inc118
                                        #   in Loop: Header=BB0_30 Depth=2
	movl	-8016(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8012(%rbp)       # 4-byte Spill
	jmp	.LBB0_30
.LBB0_33:                               # %for.end120
                                        #   in Loop: Header=BB0_28 Depth=1
	jmp	.LBB0_34
.LBB0_34:                               # %for.inc121
                                        #   in Loop: Header=BB0_28 Depth=1
	movl	-8008(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8004(%rbp)       # 4-byte Spill
	jmp	.LBB0_28
.LBB0_35:                               # %for.end123
	xorl	%eax, %eax
	movl	%eax, -8044(%rbp)       # 4-byte Spill
	jmp	.LBB0_36
.LBB0_36:                               # %for.cond124
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_38 Depth 2
                                        #       Child Loop BB0_40 Depth 3
	movl	-8044(%rbp), %eax       # 4-byte Reload
	cmpl	$31, %eax
	movl	%eax, -8048(%rbp)       # 4-byte Spill
	jge	.LBB0_47
# %bb.37:                               # %for.body127
                                        #   in Loop: Header=BB0_36 Depth=1
	movss	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	-8048(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movss	%xmm0, (%rdx,%rcx,4)
	addl	$1, %eax
	movl	%eax, -8052(%rbp)       # 4-byte Spill
.LBB0_38:                               # %for.cond133
                                        #   Parent Loop BB0_36 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_40 Depth 3
	movl	-8052(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8056(%rbp)       # 4-byte Spill
	jge	.LBB0_45
# %bb.39:                               # %for.body136
                                        #   in Loop: Header=BB0_38 Depth=2
	xorl	%eax, %eax
	movl	-8048(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	shlq	$7, %rdx
	leaq	-7808(%rbp), %rsi
	addq	%rdx, %rsi
	movl	-8056(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rdx
	xorps	%xmm0, %xmm0
	movss	%xmm0, (%rsi,%rdx,4)
	movl	%eax, -8060(%rbp)       # 4-byte Spill
.LBB0_40:                               # %for.cond141
                                        #   Parent Loop BB0_36 Depth=1
                                        #     Parent Loop BB0_38 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-8060(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -8064(%rbp)       # 4-byte Spill
	jge	.LBB0_43
# %bb.41:                               # %for.body144
                                        #   in Loop: Header=BB0_40 Depth=3
	movss	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movl	-8064(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp,%rcx), %rcx
	movl	-8048(%rbp), %edx       # 4-byte Reload
	movslq	%edx, %rsi
	movss	(%rcx,%rsi,4), %xmm1    # xmm1 = mem[0],zero,zero,zero
	movl	-8056(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %r8
	movss	(%rcx,%r8,4), %xmm2     # xmm2 = mem[0],zero,zero,zero
	movss	.LCPI0_1(%rip), %xmm3   # xmm3 = mem[0],zero,zero,zero
	mulss	%xmm3, %xmm1
	cvttss2si	%xmm1, %r9d
	mulss	%xmm3, %xmm2
	cvttss2si	%xmm2, %r10d
	movslq	%r9d, %rcx
	movslq	%r10d, %r11
	imulq	%r11, %rcx
	shrq	$29, %rcx
	movl	%ecx, %r9d
	shlq	$7, %rsi
	leaq	-7808(%rbp,%rsi), %rcx
	movq	%r8, %rsi
	movss	(%rcx,%r8,4), %xmm1     # xmm1 = mem[0],zero,zero,zero
	mulss	%xmm3, %xmm1
	cvttss2si	%xmm1, %r8
	movl	%r8d, %r10d
	addl	%r9d, %r10d
	movl	%r10d, %r8d
	cvtsi2ssq	%r8, %xmm1
	divss	%xmm0, %xmm1
	movss	%xmm1, (%rcx,%rsi,4)
# %bb.42:                               # %for.inc159
                                        #   in Loop: Header=BB0_40 Depth=3
	movl	-8064(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8060(%rbp)       # 4-byte Spill
	jmp	.LBB0_40
.LBB0_43:                               # %for.end161
                                        #   in Loop: Header=BB0_38 Depth=2
	movl	-8048(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-8056(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movss	(%rsi,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	movslq	%edi, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movss	%xmm0, (%rdx,%rcx,4)
# %bb.44:                               # %for.inc170
                                        #   in Loop: Header=BB0_38 Depth=2
	movl	-8056(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8052(%rbp)       # 4-byte Spill
	jmp	.LBB0_38
.LBB0_45:                               # %for.end172
                                        #   in Loop: Header=BB0_36 Depth=1
	jmp	.LBB0_46
.LBB0_46:                               # %for.inc173
                                        #   in Loop: Header=BB0_36 Depth=1
	movl	-8048(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8044(%rbp)       # 4-byte Spill
	jmp	.LBB0_36
.LBB0_47:                               # %for.end175
	xorl	%eax, %eax
	movss	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, -3716(%rbp)
	movl	%eax, -8068(%rbp)       # 4-byte Spill
.LBB0_48:                               # %for.cond178
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_50 Depth 2
	movl	-8068(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8072(%rbp)       # 4-byte Spill
	jge	.LBB0_55
# %bb.49:                               # %for.body181
                                        #   in Loop: Header=BB0_48 Depth=1
	xorl	%eax, %eax
	movl	%eax, -8076(%rbp)       # 4-byte Spill
	jmp	.LBB0_50
.LBB0_50:                               # %for.cond182
                                        #   Parent Loop BB0_48 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-8076(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8080(%rbp)       # 4-byte Spill
	jge	.LBB0_53
# %bb.51:                               # %for.body185
                                        #   in Loop: Header=BB0_50 Depth=2
	movl	-8072(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-8080(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	movss	(%rdx,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	movabsq	$.L.str.9, %rdi
	movb	$1, %al
	callq	printf
	movl	%eax, -8084(%rbp)       # 4-byte Spill
# %bb.52:                               # %for.inc191
                                        #   in Loop: Header=BB0_50 Depth=2
	movl	-8080(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8076(%rbp)       # 4-byte Spill
	jmp	.LBB0_50
.LBB0_53:                               # %for.end193
                                        #   in Loop: Header=BB0_48 Depth=1
	movabsq	$.L.str.10, %rdi
	movb	$0, %al
	callq	printf
	movl	%eax, -8088(%rbp)       # 4-byte Spill
# %bb.54:                               # %for.inc195
                                        #   in Loop: Header=BB0_48 Depth=1
	movl	-8072(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8068(%rbp)       # 4-byte Spill
	jmp	.LBB0_48
.LBB0_55:                               # %for.end197
	xorl	%eax, %eax
	addq	$8096, %rsp             # imm = 0x1FA0
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	.L.str.9,@object        # @.str.9
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str.9:
	.asciz	"%.10f "
	.size	.L.str.9, 7

	.type	.L.str.10,@object       # @.str.10
.L.str.10:
	.asciz	"\n"
	.size	.L.str.10, 2


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym sqrt
	.addrsig_sym printf
