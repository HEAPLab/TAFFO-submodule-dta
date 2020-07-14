	.text
	.file	"corr.c"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI0_0:
	.quad	4607182418800017408     # double 1
.LCPI0_1:
	.quad	4628574517030027264     # double 28
.LCPI0_2:
	.quad	4591870180066957722     # double 0.10000000000000001
.LCPI0_3:
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
	subq	$16016, %rsp            # imm = 0x3E90
	xorl	%eax, %eax
	movl	%eax, -15876(%rbp)      # 4-byte Spill
.LBB0_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
	movl	-15876(%rbp), %eax      # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -15880(%rbp)      # 4-byte Spill
	jge	.LBB0_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -15884(%rbp)      # 4-byte Spill
	jmp	.LBB0_3
.LBB0_3:                                # %for.cond9
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-15884(%rbp), %eax      # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -15888(%rbp)      # 4-byte Spill
	jge	.LBB0_6
# %bb.4:                                # %for.body11
                                        #   in Loop: Header=BB0_3 Depth=2
	movsd	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_3(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-15880(%rbp), %eax      # 4-byte Reload
	movl	-15888(%rbp), %ecx      # 4-byte Reload
	imull	%ecx, %eax
	cvtsi2sdl	%eax, %xmm2
	divsd	%xmm1, %xmm2
	movl	-15880(%rbp), %eax      # 4-byte Reload
	cvtsi2sdl	%eax, %xmm1
	addsd	%xmm1, %xmm2
	divsd	%xmm0, %xmm2
	movslq	%eax, %rdx
	shlq	$8, %rdx
	leaq	-7424(%rbp), %rsi
	addq	%rdx, %rsi
	movslq	%ecx, %rdx
	movsd	%xmm2, (%rsi,%rdx,8)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-15888(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15884(%rbp)      # 4-byte Spill
	jmp	.LBB0_3
.LBB0_6:                                # %for.end
                                        #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_7
.LBB0_7:                                # %for.inc16
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-15880(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15876(%rbp)      # 4-byte Spill
	jmp	.LBB0_1
.LBB0_8:                                # %for.end18
	xorl	%eax, %eax
	movl	%eax, -15892(%rbp)      # 4-byte Spill
	jmp	.LBB0_9
.LBB0_9:                                # %for.cond20
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_11 Depth 2
	movl	-15892(%rbp), %eax      # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -15896(%rbp)      # 4-byte Spill
	jge	.LBB0_16
# %bb.10:                               # %for.body23
                                        #   in Loop: Header=BB0_9 Depth=1
	xorl	%eax, %eax
	movl	-15896(%rbp), %ecx      # 4-byte Reload
	movslq	%ecx, %rdx
	xorps	%xmm0, %xmm0
	movsd	%xmm0, -256(%rbp,%rdx,8)
	movl	%eax, -15900(%rbp)      # 4-byte Spill
.LBB0_11:                               # %for.cond26
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-15900(%rbp), %eax      # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -15904(%rbp)      # 4-byte Spill
	jge	.LBB0_14
# %bb.12:                               # %for.body29
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-15904(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	leaq	-7424(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-15896(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	movsd	(%rdx,%rcx,8), %xmm0    # xmm0 = mem[0],zero
	movslq	%esi, %rcx
	addsd	-256(%rbp,%rcx,8), %xmm0
	movsd	%xmm0, -256(%rbp,%rcx,8)
# %bb.13:                               # %for.inc37
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-15904(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15900(%rbp)      # 4-byte Spill
	jmp	.LBB0_11
.LBB0_14:                               # %for.end39
                                        #   in Loop: Header=BB0_9 Depth=1
	movsd	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-15896(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movsd	-256(%rbp,%rcx,8), %xmm1 # xmm1 = mem[0],zero
	divsd	%xmm0, %xmm1
	movsd	%xmm1, -256(%rbp,%rcx,8)
# %bb.15:                               # %for.inc43
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-15896(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15892(%rbp)      # 4-byte Spill
	jmp	.LBB0_9
.LBB0_16:                               # %for.end45
	xorl	%eax, %eax
	movl	%eax, -15908(%rbp)      # 4-byte Spill
	jmp	.LBB0_17
.LBB0_17:                               # %for.cond46
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_19 Depth 2
	movl	-15908(%rbp), %eax      # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -15912(%rbp)      # 4-byte Spill
	jge	.LBB0_27
# %bb.18:                               # %for.body49
                                        #   in Loop: Header=BB0_17 Depth=1
	xorl	%eax, %eax
	movl	-15912(%rbp), %ecx      # 4-byte Reload
	movslq	%ecx, %rdx
	xorps	%xmm0, %xmm0
	movsd	%xmm0, -15872(%rbp,%rdx,8)
	movl	%eax, -15916(%rbp)      # 4-byte Spill
.LBB0_19:                               # %for.cond52
                                        #   Parent Loop BB0_17 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-15916(%rbp), %eax      # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -15920(%rbp)      # 4-byte Spill
	jge	.LBB0_22
# %bb.20:                               # %for.body55
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-15920(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	leaq	-7424(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-15912(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rcx
	movsd	(%rsi,%rcx,8), %xmm0    # xmm0 = mem[0],zero
	movslq	%edi, %rcx
	subsd	-256(%rbp,%rcx,8), %xmm0
	movslq	%eax, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movsd	(%rdx,%rcx,8), %xmm1    # xmm1 = mem[0],zero
	movslq	%edi, %rcx
	subsd	-256(%rbp,%rcx,8), %xmm1
	mulsd	%xmm1, %xmm0
	movslq	%edi, %rcx
	addsd	-15872(%rbp,%rcx,8), %xmm0
	movsd	%xmm0, -15872(%rbp,%rcx,8)
# %bb.21:                               # %for.inc73
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-15920(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15916(%rbp)      # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end75
                                        #   in Loop: Header=BB0_17 Depth=1
	movsd	.LCPI0_2(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_1(%rip), %xmm1   # xmm1 = mem[0],zero
	movl	-15912(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movsd	-15872(%rbp,%rcx,8), %xmm2 # xmm2 = mem[0],zero
	divsd	%xmm1, %xmm2
	movsd	%xmm2, -15872(%rbp,%rcx,8)
	movslq	%eax, %rcx
	movsd	-15872(%rbp,%rcx,8), %xmm1 # xmm1 = mem[0],zero
	movsd	%xmm0, -15928(%rbp)     # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	sqrt
	movl	-15912(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movsd	%xmm0, -15872(%rbp,%rcx,8)
	movslq	%eax, %rcx
	movsd	-15928(%rbp), %xmm0     # 8-byte Reload
                                        # xmm0 = mem[0],zero
	ucomisd	-15872(%rbp,%rcx,8), %xmm0
	jb	.LBB0_24
# %bb.23:                               # %cond.true
                                        #   in Loop: Header=BB0_17 Depth=1
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	%xmm0, -15936(%rbp)     # 8-byte Spill
	jmp	.LBB0_25
.LBB0_24:                               # %cond.false
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-15912(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movsd	-15872(%rbp,%rcx,8), %xmm0 # xmm0 = mem[0],zero
	movsd	%xmm0, -15936(%rbp)     # 8-byte Spill
.LBB0_25:                               # %cond.end
                                        #   in Loop: Header=BB0_17 Depth=1
	movsd	-15936(%rbp), %xmm0     # 8-byte Reload
                                        # xmm0 = mem[0],zero
	movl	-15912(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movsd	%xmm0, -15872(%rbp,%rcx,8)
# %bb.26:                               # %for.inc91
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-15912(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15908(%rbp)      # 4-byte Spill
	jmp	.LBB0_17
.LBB0_27:                               # %for.end93
	xorl	%eax, %eax
	movl	%eax, -15940(%rbp)      # 4-byte Spill
	jmp	.LBB0_28
.LBB0_28:                               # %for.cond94
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_30 Depth 2
	movl	-15940(%rbp), %eax      # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -15944(%rbp)      # 4-byte Spill
	jge	.LBB0_35
# %bb.29:                               # %for.body97
                                        #   in Loop: Header=BB0_28 Depth=1
	xorl	%eax, %eax
	movl	%eax, -15948(%rbp)      # 4-byte Spill
	jmp	.LBB0_30
.LBB0_30:                               # %for.cond98
                                        #   Parent Loop BB0_28 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-15948(%rbp), %eax      # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -15952(%rbp)      # 4-byte Spill
	jge	.LBB0_33
# %bb.31:                               # %for.body101
                                        #   in Loop: Header=BB0_30 Depth=2
	movl	-15952(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	movsd	-256(%rbp,%rcx,8), %xmm0 # xmm0 = mem[0],zero
	movl	-15944(%rbp), %edx      # 4-byte Reload
	movslq	%edx, %rcx
	shlq	$8, %rcx
	leaq	-7424(%rbp), %rsi
	movq	%rsi, %rdi
	addq	%rcx, %rdi
	movslq	%eax, %rcx
	movsd	(%rdi,%rcx,8), %xmm1    # xmm1 = mem[0],zero
	subsd	%xmm0, %xmm1
	movsd	%xmm1, (%rdi,%rcx,8)
	movsd	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	%rsi, -15960(%rbp)      # 8-byte Spill
	callq	sqrt
	movl	-15952(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	mulsd	-15872(%rbp,%rcx,8), %xmm0
	movl	-15944(%rbp), %edx      # 4-byte Reload
	movslq	%edx, %rcx
	shlq	$8, %rcx
	movq	-15960(%rbp), %rsi      # 8-byte Reload
	addq	%rcx, %rsi
	movslq	%eax, %rcx
	movsd	(%rsi,%rcx,8), %xmm1    # xmm1 = mem[0],zero
	divsd	%xmm0, %xmm1
	movsd	%xmm1, (%rsi,%rcx,8)
# %bb.32:                               # %for.inc118
                                        #   in Loop: Header=BB0_30 Depth=2
	movl	-15952(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15948(%rbp)      # 4-byte Spill
	jmp	.LBB0_30
.LBB0_33:                               # %for.end120
                                        #   in Loop: Header=BB0_28 Depth=1
	jmp	.LBB0_34
.LBB0_34:                               # %for.inc121
                                        #   in Loop: Header=BB0_28 Depth=1
	movl	-15944(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15940(%rbp)      # 4-byte Spill
	jmp	.LBB0_28
.LBB0_35:                               # %for.end123
	xorl	%eax, %eax
	movl	%eax, -15964(%rbp)      # 4-byte Spill
	jmp	.LBB0_36
.LBB0_36:                               # %for.cond124
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_38 Depth 2
                                        #       Child Loop BB0_40 Depth 3
	movl	-15964(%rbp), %eax      # 4-byte Reload
	cmpl	$31, %eax
	movl	%eax, -15968(%rbp)      # 4-byte Spill
	jge	.LBB0_47
# %bb.37:                               # %for.body127
                                        #   in Loop: Header=BB0_36 Depth=1
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-15968(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	leaq	-15616(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movsd	%xmm0, (%rdx,%rcx,8)
	addl	$1, %eax
	movl	%eax, -15972(%rbp)      # 4-byte Spill
.LBB0_38:                               # %for.cond133
                                        #   Parent Loop BB0_36 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_40 Depth 3
	movl	-15972(%rbp), %eax      # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -15976(%rbp)      # 4-byte Spill
	jge	.LBB0_45
# %bb.39:                               # %for.body136
                                        #   in Loop: Header=BB0_38 Depth=2
	xorl	%eax, %eax
	movl	-15968(%rbp), %ecx      # 4-byte Reload
	movslq	%ecx, %rdx
	shlq	$8, %rdx
	leaq	-15616(%rbp), %rsi
	addq	%rdx, %rsi
	movl	-15976(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rdx
	xorps	%xmm0, %xmm0
	movsd	%xmm0, (%rsi,%rdx,8)
	movl	%eax, -15980(%rbp)      # 4-byte Spill
.LBB0_40:                               # %for.cond141
                                        #   Parent Loop BB0_36 Depth=1
                                        #     Parent Loop BB0_38 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-15980(%rbp), %eax      # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -15984(%rbp)      # 4-byte Spill
	jge	.LBB0_43
# %bb.41:                               # %for.body144
                                        #   in Loop: Header=BB0_40 Depth=3
	movl	-15984(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	leaq	-7424(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-15968(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rcx
	movsd	(%rsi,%rcx,8), %xmm0    # xmm0 = mem[0],zero
	movslq	%eax, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rdx
	movl	-15976(%rbp), %r8d      # 4-byte Reload
	movslq	%r8d, %rcx
	mulsd	(%rdx,%rcx,8), %xmm0
	movslq	%edi, %rcx
	shlq	$8, %rcx
	leaq	-15616(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%r8d, %rcx
	addsd	(%rdx,%rcx,8), %xmm0
	movsd	%xmm0, (%rdx,%rcx,8)
# %bb.42:                               # %for.inc159
                                        #   in Loop: Header=BB0_40 Depth=3
	movl	-15984(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15980(%rbp)      # 4-byte Spill
	jmp	.LBB0_40
.LBB0_43:                               # %for.end161
                                        #   in Loop: Header=BB0_38 Depth=2
	movl	-15968(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	leaq	-15616(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-15976(%rbp), %edi      # 4-byte Reload
	movslq	%edi, %rcx
	movsd	(%rsi,%rcx,8), %xmm0    # xmm0 = mem[0],zero
	movslq	%edi, %rcx
	shlq	$8, %rcx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movsd	%xmm0, (%rdx,%rcx,8)
# %bb.44:                               # %for.inc170
                                        #   in Loop: Header=BB0_38 Depth=2
	movl	-15976(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15972(%rbp)      # 4-byte Spill
	jmp	.LBB0_38
.LBB0_45:                               # %for.end172
                                        #   in Loop: Header=BB0_36 Depth=1
	jmp	.LBB0_46
.LBB0_46:                               # %for.inc173
                                        #   in Loop: Header=BB0_36 Depth=1
	movl	-15968(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15964(%rbp)      # 4-byte Spill
	jmp	.LBB0_36
.LBB0_47:                               # %for.end175
	xorl	%eax, %eax
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	%xmm0, -7432(%rbp)
	movl	%eax, -15988(%rbp)      # 4-byte Spill
.LBB0_48:                               # %for.cond178
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_50 Depth 2
	movl	-15988(%rbp), %eax      # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -15992(%rbp)      # 4-byte Spill
	jge	.LBB0_55
# %bb.49:                               # %for.body181
                                        #   in Loop: Header=BB0_48 Depth=1
	xorl	%eax, %eax
	movl	%eax, -15996(%rbp)      # 4-byte Spill
	jmp	.LBB0_50
.LBB0_50:                               # %for.cond182
                                        #   Parent Loop BB0_48 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-15996(%rbp), %eax      # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -16000(%rbp)      # 4-byte Spill
	jge	.LBB0_53
# %bb.51:                               # %for.body185
                                        #   in Loop: Header=BB0_50 Depth=2
	movl	-15992(%rbp), %eax      # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$8, %rcx
	leaq	-15616(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-16000(%rbp), %esi      # 4-byte Reload
	movslq	%esi, %rcx
	movsd	(%rdx,%rcx,8), %xmm0    # xmm0 = mem[0],zero
	movabsq	$.L.str.9, %rdi
	movb	$1, %al
	callq	printf
	movl	%eax, -16004(%rbp)      # 4-byte Spill
# %bb.52:                               # %for.inc191
                                        #   in Loop: Header=BB0_50 Depth=2
	movl	-16000(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15996(%rbp)      # 4-byte Spill
	jmp	.LBB0_50
.LBB0_53:                               # %for.end193
                                        #   in Loop: Header=BB0_48 Depth=1
	movabsq	$.L.str.10, %rdi
	movb	$0, %al
	callq	printf
	movl	%eax, -16008(%rbp)      # 4-byte Spill
# %bb.54:                               # %for.inc195
                                        #   in Loop: Header=BB0_48 Depth=1
	movl	-15992(%rbp), %eax      # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -15988(%rbp)      # 4-byte Spill
	jmp	.LBB0_48
.LBB0_55:                               # %for.end197
	xorl	%eax, %eax
	addq	$16016, %rsp            # imm = 0x3E90
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
