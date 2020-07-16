	.text
	.file	"corr.c"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI0_0:
	.quad	4737786807993761792     # double 536870912
.LCPI0_1:
	.quad	4628574517030027264     # double 28
.LCPI0_2:
	.quad	4697254411347427328     # double 1048576
.LCPI0_3:
	.quad	4688247212092686336     # double 262144
.LCPI0_4:
	.quad	4728779608739020800     # double 134217728
.LCPI0_5:
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
	subq	$8064, %rsp             # imm = 0x1F80
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
	movsd	.LCPI0_4(%rip), %xmm0   # xmm0 = mem[0],zero
	movsd	.LCPI0_1(%rip), %xmm1   # xmm1 = mem[0],zero
	movsd	.LCPI0_5(%rip), %xmm2   # xmm2 = mem[0],zero
	movl	-7944(%rbp), %eax       # 4-byte Reload
	movl	-7952(%rbp), %ecx       # 4-byte Reload
	imull	%ecx, %eax
	cvtsi2sdl	%eax, %xmm3
	divsd	%xmm2, %xmm3
	movl	-7944(%rbp), %eax       # 4-byte Reload
	cvtsi2sdl	%eax, %xmm2
	addsd	%xmm2, %xmm3
	divsd	%xmm1, %xmm3
	mulsd	%xmm3, %xmm0
	cvttsd2si	%xmm0, %edx
	movslq	%eax, %rsi
	shlq	$7, %rsi
	leaq	-3712(%rbp), %rdi
	addq	%rsi, %rdi
	movslq	%ecx, %rsi
	movl	%edx, (%rdi,%rsi,4)
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
	movl	-7968(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-7960(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%esi, %rcx
	movl	-128(%rbp,%rcx,4), %r8d
	sarl	$12, %edi
	addl	%edi, %r8d
	movl	%r8d, -128(%rbp,%rcx,4)
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
	movl	$0, -7936(%rbp,%rdx,4)
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
	movl	-7984(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-7976(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%edi, %rcx
	movl	-128(%rbp,%rcx,4), %r9d
	sarl	$12, %r8d
	subl	%r9d, %r8d
	movslq	%eax, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	movl	(%rdx,%rcx,4), %r9d
	movslq	%edi, %rcx
	movl	-128(%rbp,%rcx,4), %r10d
	sarl	$12, %r9d
	subl	%r10d, %r9d
	movslq	%r8d, %rcx
	movslq	%r9d, %rdx
	imulq	%rdx, %rcx
	sarq	$15, %rcx
	movl	%ecx, %r8d
	movslq	%edi, %rcx
	movl	-7936(%rbp,%rcx,4), %r9d
	shll	$3, %r8d
	addl	%r8d, %r9d
	movl	%r9d, -7936(%rbp,%rcx,4)
# %bb.21:                               # %for.inc73
                                        #   in Loop: Header=BB0_19 Depth=2
	movl	-7984(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7980(%rbp)       # 4-byte Spill
	jmp	.LBB0_19
.LBB0_22:                               # %for.end75
                                        #   in Loop: Header=BB0_17 Depth=1
	movsd	.LCPI0_3(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-7976(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movslq	-7936(%rbp,%rcx,4), %rdx
	movq	%rdx, %rax
	xorl	%esi, %esi
	movl	%esi, %edx
	movl	$28, %edi
	divq	%rdi
	shlq	$2, %rax
	movl	%eax, %esi
	shrl	$2, %esi
	movl	%esi, -7936(%rbp,%rcx,4)
	movl	-7976(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rax
	movl	-7936(%rbp,%rax,4), %r8d
	cvtsi2sdl	%r8d, %xmm1
	divsd	%xmm0, %xmm1
	movsd	%xmm0, -7992(%rbp)      # 8-byte Spill
	movaps	%xmm1, %xmm0
	callq	sqrt
	movsd	-7992(%rbp), %xmm1      # 8-byte Reload
                                        # xmm1 = mem[0],zero
	mulsd	%xmm0, %xmm1
	cvttsd2si	%xmm1, %esi
	movl	-7976(%rbp), %r8d       # 4-byte Reload
	movslq	%r8d, %rax
	movl	%esi, -7936(%rbp,%rax,4)
	movslq	%r8d, %rax
	cmpl	$26214, -7936(%rbp,%rax,4) # imm = 0x6666
	jg	.LBB0_24
# %bb.23:                               # %cond.true
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	$262144, %eax           # imm = 0x40000
	movl	%eax, -7996(%rbp)       # 4-byte Spill
	jmp	.LBB0_25
.LBB0_24:                               # %cond.false
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-7976(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movl	-7936(%rbp,%rcx,4), %edx
	movl	%edx, -7996(%rbp)       # 4-byte Spill
.LBB0_25:                               # %cond.end
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-7996(%rbp), %eax       # 4-byte Reload
	movl	-7976(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	movl	%eax, -7936(%rbp,%rdx,4)
# %bb.26:                               # %for.inc91
                                        #   in Loop: Header=BB0_17 Depth=1
	movl	-7976(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -7972(%rbp)       # 4-byte Spill
	jmp	.LBB0_17
.LBB0_27:                               # %for.end93
	xorl	%eax, %eax
	movl	%eax, -8000(%rbp)       # 4-byte Spill
	jmp	.LBB0_28
.LBB0_28:                               # %for.cond94
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_30 Depth 2
	movl	-8000(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -8004(%rbp)       # 4-byte Spill
	jge	.LBB0_35
# %bb.29:                               # %for.body97
                                        #   in Loop: Header=BB0_28 Depth=1
	xorl	%eax, %eax
	movl	%eax, -8008(%rbp)       # 4-byte Spill
	jmp	.LBB0_30
.LBB0_30:                               # %for.cond98
                                        #   Parent Loop BB0_28 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-8008(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8012(%rbp)       # 4-byte Spill
	jge	.LBB0_33
# %bb.31:                               # %for.body101
                                        #   in Loop: Header=BB0_30 Depth=2
	movl	-8012(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	movl	-128(%rbp,%rcx,4), %edx
	movl	-8004(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rdi
	shlq	$7, %rdi
	leaq	-3712(%rbp,%rdi), %rdi
	movl	(%rdi,%rcx,4), %r8d
	shrl	$12, %r8d
	subl	%edx, %r8d
	shll	$12, %r8d
	movl	%r8d, (%rdi,%rcx,4)
	movsd	.LCPI0_1(%rip), %xmm0   # xmm0 = mem[0],zero
	callq	sqrt
	movsd	.LCPI0_2(%rip), %xmm1   # xmm1 = mem[0],zero
	mulsd	%xmm1, %xmm0
	cvttsd2si	%xmm0, %rcx
	movl	%ecx, %eax
	movl	-8012(%rbp), %edx       # 4-byte Reload
	movslq	%edx, %rcx
	movl	-7936(%rbp,%rcx,4), %esi
	movl	%eax, %eax
	movl	%eax, %ecx
	movslq	%esi, %rdi
	imulq	%rdi, %rcx
	sarq	$20, %rcx
	movl	%ecx, %eax
	movl	-8004(%rbp), %esi       # 4-byte Reload
	movslq	%esi, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdi
	addq	%rcx, %rdi
	movslq	%edx, %rcx
	movslq	(%rdi,%rcx,4), %r9
	shlq	$18, %r9
	movslq	%eax, %r10
	movq	%r9, %rax
	cqto
	idivq	%r10
	movl	%eax, %r8d
	movl	%r8d, (%rdi,%rcx,4)
# %bb.32:                               # %for.inc118
                                        #   in Loop: Header=BB0_30 Depth=2
	movl	-8012(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8008(%rbp)       # 4-byte Spill
	jmp	.LBB0_30
.LBB0_33:                               # %for.end120
                                        #   in Loop: Header=BB0_28 Depth=1
	jmp	.LBB0_34
.LBB0_34:                               # %for.inc121
                                        #   in Loop: Header=BB0_28 Depth=1
	movl	-8004(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8000(%rbp)       # 4-byte Spill
	jmp	.LBB0_28
.LBB0_35:                               # %for.end123
	xorl	%eax, %eax
	movl	%eax, -8016(%rbp)       # 4-byte Spill
	jmp	.LBB0_36
.LBB0_36:                               # %for.cond124
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_38 Depth 2
                                        #       Child Loop BB0_40 Depth 3
	movl	-8016(%rbp), %eax       # 4-byte Reload
	cmpl	$31, %eax
	movl	%eax, -8020(%rbp)       # 4-byte Spill
	jge	.LBB0_47
# %bb.37:                               # %for.body127
                                        #   in Loop: Header=BB0_36 Depth=1
	movl	-8020(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movl	$536870912, (%rdx,%rcx,4) # imm = 0x20000000
	addl	$1, %eax
	movl	%eax, -8024(%rbp)       # 4-byte Spill
.LBB0_38:                               # %for.cond133
                                        #   Parent Loop BB0_36 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_40 Depth 3
	movl	-8024(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8028(%rbp)       # 4-byte Spill
	jge	.LBB0_45
# %bb.39:                               # %for.body136
                                        #   in Loop: Header=BB0_38 Depth=2
	xorl	%eax, %eax
	movl	-8020(%rbp), %ecx       # 4-byte Reload
	movslq	%ecx, %rdx
	shlq	$7, %rdx
	leaq	-7808(%rbp), %rsi
	addq	%rdx, %rsi
	movl	-8028(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rdx
	movl	$0, (%rsi,%rdx,4)
	movl	%eax, -8032(%rbp)       # 4-byte Spill
.LBB0_40:                               # %for.cond141
                                        #   Parent Loop BB0_36 Depth=1
                                        #     Parent Loop BB0_38 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-8032(%rbp), %eax       # 4-byte Reload
	cmpl	$28, %eax
	movl	%eax, -8036(%rbp)       # 4-byte Spill
	jge	.LBB0_43
# %bb.41:                               # %for.body144
                                        #   in Loop: Header=BB0_40 Depth=3
	movl	-8036(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-3712(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-8020(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%eax, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movl	-8028(%rbp), %r9d       # 4-byte Reload
	movslq	%r9d, %rcx
	movl	(%rdx,%rcx,4), %r10d
	movslq	%r8d, %rcx
	movslq	%r10d, %rdx
	imulq	%rdx, %rcx
	sarq	$27, %rcx
	movl	%ecx, %r8d
	movslq	%edi, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	addq	%rcx, %rdx
	movslq	%r9d, %rcx
	movl	(%rdx,%rcx,4), %r10d
	shll	$2, %r8d
	addl	%r8d, %r10d
	movl	%r10d, (%rdx,%rcx,4)
# %bb.42:                               # %for.inc159
                                        #   in Loop: Header=BB0_40 Depth=3
	movl	-8036(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8032(%rbp)       # 4-byte Spill
	jmp	.LBB0_40
.LBB0_43:                               # %for.end161
                                        #   in Loop: Header=BB0_38 Depth=2
	movl	-8020(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	-8028(%rbp), %edi       # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%rsi,%rcx,4), %r8d
	movslq	%edi, %rcx
	shlq	$7, %rcx
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	movl	%r8d, (%rdx,%rcx,4)
# %bb.44:                               # %for.inc170
                                        #   in Loop: Header=BB0_38 Depth=2
	movl	-8028(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8024(%rbp)       # 4-byte Spill
	jmp	.LBB0_38
.LBB0_45:                               # %for.end172
                                        #   in Loop: Header=BB0_36 Depth=1
	jmp	.LBB0_46
.LBB0_46:                               # %for.inc173
                                        #   in Loop: Header=BB0_36 Depth=1
	movl	-8020(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8016(%rbp)       # 4-byte Spill
	jmp	.LBB0_36
.LBB0_47:                               # %for.end175
	xorl	%eax, %eax
	movl	$536870912, -3716(%rbp) # imm = 0x20000000
	movl	%eax, -8040(%rbp)       # 4-byte Spill
.LBB0_48:                               # %for.cond178
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_50 Depth 2
	movl	-8040(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8044(%rbp)       # 4-byte Spill
	jge	.LBB0_55
# %bb.49:                               # %for.body181
                                        #   in Loop: Header=BB0_48 Depth=1
	xorl	%eax, %eax
	movl	%eax, -8048(%rbp)       # 4-byte Spill
	jmp	.LBB0_50
.LBB0_50:                               # %for.cond182
                                        #   Parent Loop BB0_48 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-8048(%rbp), %eax       # 4-byte Reload
	cmpl	$32, %eax
	movl	%eax, -8052(%rbp)       # 4-byte Spill
	jge	.LBB0_53
# %bb.51:                               # %for.body185
                                        #   in Loop: Header=BB0_50 Depth=2
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movl	-8044(%rbp), %eax       # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$7, %rcx
	leaq	-7808(%rbp,%rcx), %rcx
	movl	-8052(%rbp), %edx       # 4-byte Reload
	movslq	%edx, %rsi
	movl	(%rcx,%rsi,4), %edi
	movl	%edi, %ecx
	cvtsi2sdq	%rcx, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.9, %rdi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	printf
	movl	%eax, -8056(%rbp)       # 4-byte Spill
# %bb.52:                               # %for.inc191
                                        #   in Loop: Header=BB0_50 Depth=2
	movl	-8052(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8048(%rbp)       # 4-byte Spill
	jmp	.LBB0_50
.LBB0_53:                               # %for.end193
                                        #   in Loop: Header=BB0_48 Depth=1
	movabsq	$.L.str.10, %rdi
	movb	$0, %al
	callq	printf
	movl	%eax, -8060(%rbp)       # 4-byte Spill
# %bb.54:                               # %for.inc195
                                        #   in Loop: Header=BB0_48 Depth=1
	movl	-8044(%rbp), %eax       # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -8040(%rbp)       # 4-byte Spill
	jmp	.LBB0_48
.LBB0_55:                               # %for.end197
	xorl	%eax, %eax
	addq	$8064, %rsp             # imm = 0x1F80
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
	.asciz	"%.16lf "
	.size	.L.str.9, 8

	.type	.L.str.10,@object       # @.str.10
.L.str.10:
	.asciz	"\n"
	.size	.L.str.10, 2


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym sqrt
	.addrsig_sym printf
