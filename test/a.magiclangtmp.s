	.text
	.file	"cconv.c"
	.globl	arrayLoad               # -- Begin function arrayLoad
	.p2align	4, 0x90
	.type	arrayLoad,@function
arrayLoad:                              # @arrayLoad
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	xorl	%eax, %eax
	movq	%rdi, -8(%rbp)          # 8-byte Spill
	movl	%esi, -12(%rbp)         # 4-byte Spill
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jmp	.LBB0_1
.LBB0_1:                                # %for.cond
                                        # =>This Inner Loop Header: Depth=1
	movl	-16(%rbp), %eax         # 4-byte Reload
	movl	-12(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jge	.LBB0_4
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-20(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$2, %rcx
	movq	-8(%rbp), %rdx          # 8-byte Reload
	addq	%rcx, %rdx
	movabsq	$.L.str, %rdi
	movq	%rdx, %rsi
	movb	$0, %al
	callq	__isoc99_scanf
	movl	%eax, -24(%rbp)         # 4-byte Spill
# %bb.3:                                # %for.inc
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-20(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jmp	.LBB0_1
.LBB0_4:                                # %for.end
	addq	$32, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	arrayLoad, .Lfunc_end0-arrayLoad
	.cfi_endproc
                                        # -- End function
	.globl	arrayInit               # -- Begin function arrayInit
	.p2align	4, 0x90
	.type	arrayInit,@function
arrayInit:                              # @arrayInit
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	xorl	%eax, %eax
	movq	%rdi, -8(%rbp)          # 8-byte Spill
	movl	%esi, -12(%rbp)         # 4-byte Spill
	movss	%xmm0, -16(%rbp)        # 4-byte Spill
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jmp	.LBB1_1
.LBB1_1:                                # %for.cond
                                        # =>This Inner Loop Header: Depth=1
	movl	-20(%rbp), %eax         # 4-byte Reload
	movl	-12(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -24(%rbp)         # 4-byte Spill
	jge	.LBB1_4
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB1_1 Depth=1
	movl	-24(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movq	-8(%rbp), %rdx          # 8-byte Reload
	movss	-16(%rbp), %xmm0        # 4-byte Reload
                                        # xmm0 = mem[0],zero,zero,zero
	movss	%xmm0, (%rdx,%rcx,4)
# %bb.3:                                # %for.inc
                                        #   in Loop: Header=BB1_1 Depth=1
	movl	-24(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jmp	.LBB1_1
.LBB1_4:                                # %for.end
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end1:
	.size	arrayInit, .Lfunc_end1-arrayInit
	.cfi_endproc
                                        # -- End function
	.globl	printArray              # -- Begin function printArray
	.p2align	4, 0x90
	.type	printArray,@function
printArray:                             # @printArray
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	xorl	%eax, %eax
	movq	%rdi, -8(%rbp)          # 8-byte Spill
	movl	%esi, -12(%rbp)         # 4-byte Spill
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jmp	.LBB2_1
.LBB2_1:                                # %for.cond
                                        # =>This Inner Loop Header: Depth=1
	movl	-16(%rbp), %eax         # 4-byte Reload
	movl	-12(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jge	.LBB2_4
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB2_1 Depth=1
	movl	-20(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movq	-8(%rbp), %rdx          # 8-byte Reload
	movss	(%rdx,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	cvtss2sd	%xmm0, %xmm0
	movabsq	$.L.str.1, %rdi
	movb	$1, %al
	callq	printf
	movl	%eax, -24(%rbp)         # 4-byte Spill
# %bb.3:                                # %for.inc
                                        #   in Loop: Header=BB2_1 Depth=1
	movl	-20(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jmp	.LBB2_1
.LBB2_4:                                # %for.end
	addq	$32, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end2:
	.size	printArray, .Lfunc_end2-printArray
	.cfi_endproc
                                        # -- End function
	.globl	cconv                   # -- Begin function cconv
	.p2align	4, 0x90
	.type	cconv,@function
cconv:                                  # @cconv
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	xorl	%eax, %eax
	movq	%rdi, -8(%rbp)          # 8-byte Spill
	movq	%rsi, -16(%rbp)         # 8-byte Spill
	movq	%rdx, -24(%rbp)         # 8-byte Spill
	movl	%ecx, -28(%rbp)         # 4-byte Spill
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jmp	.LBB3_1
.LBB3_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB3_3 Depth 2
	movl	-32(%rbp), %eax         # 4-byte Reload
	movl	-28(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jge	.LBB3_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB3_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jmp	.LBB3_3
.LBB3_3:                                # %for.cond1
                                        #   Parent Loop BB3_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-40(%rbp), %eax         # 4-byte Reload
	movl	-28(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jge	.LBB3_6
# %bb.4:                                # %for.body3
                                        #   in Loop: Header=BB3_3 Depth=2
	movl	-44(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movq	-16(%rbp), %rdx         # 8-byte Reload
	movss	(%rdx,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	movl	-36(%rbp), %esi         # 4-byte Reload
	subl	%eax, %esi
	addl	$10, %esi
	movl	%esi, %eax
	cltd
	movl	$10, %esi
	idivl	%esi
	movslq	%edx, %rcx
	movq	-8(%rbp), %rdi          # 8-byte Reload
	mulss	(%rdi,%rcx,4), %xmm0
	movl	-36(%rbp), %edx         # 4-byte Reload
	movslq	%edx, %rcx
	movq	-24(%rbp), %r8          # 8-byte Reload
	addss	(%r8,%rcx,4), %xmm0
	movss	%xmm0, (%r8,%rcx,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB3_3 Depth=2
	movl	-44(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jmp	.LBB3_3
.LBB3_6:                                # %for.end
                                        #   in Loop: Header=BB3_1 Depth=1
	jmp	.LBB3_7
.LBB3_7:                                # %for.inc9
                                        #   in Loop: Header=BB3_1 Depth=1
	movl	-36(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jmp	.LBB3_1
.LBB3_8:                                # %for.end11
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end3:
	.size	cconv, .Lfunc_end3-cconv
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
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
	subq	$144, %rsp
	leaq	-48(%rbp), %rdi
	movl	$10, %esi
	callq	arrayLoad.1_fixp
	leaq	-96(%rbp), %rdi
	movl	$10, %esi
	callq	arrayLoad.1_fixp
	leaq	-144(%rbp), %rdi
	movl	$10, %esi
	xorps	%xmm0, %xmm0
	callq	arrayInit
	leaq	-144(%rbp), %rdx
	leaq	-96(%rbp), %rsi
	leaq	-48(%rbp), %rdi
	movl	$10, %ecx
	callq	cconv.2_fixp
	leaq	-144(%rbp), %rdi
	movl	$10, %esi
	callq	printArray
	xorl	%eax, %eax
	addq	$144, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end4:
	.size	main, .Lfunc_end4-main
	.cfi_endproc
                                        # -- End function
	.p2align	4, 0x90         # -- Begin function arrayLoad.1_fixp
	.type	arrayLoad.1_fixp,@function
arrayLoad.1_fixp:                       # @arrayLoad.1_fixp
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	xorl	%eax, %eax
	movq	%rdi, -8(%rbp)          # 8-byte Spill
	movl	%esi, -12(%rbp)         # 4-byte Spill
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jmp	.LBB5_1
.LBB5_1:                                # %for.cond
                                        # =>This Inner Loop Header: Depth=1
	movl	-16(%rbp), %eax         # 4-byte Reload
	movl	-12(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -20(%rbp)         # 4-byte Spill
	jge	.LBB5_4
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB5_1 Depth=1
	movl	-20(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	shlq	$2, %rcx
	movq	-8(%rbp), %rdx          # 8-byte Reload
	addq	%rcx, %rdx
	movabsq	$.L.str, %rdi
	movq	%rdx, %rsi
	movb	$0, %al
	callq	__isoc99_scanf
	movl	%eax, -24(%rbp)         # 4-byte Spill
# %bb.3:                                # %for.inc
                                        #   in Loop: Header=BB5_1 Depth=1
	movl	-20(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -16(%rbp)         # 4-byte Spill
	jmp	.LBB5_1
.LBB5_4:                                # %for.end
	addq	$32, %rsp
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end5:
	.size	arrayLoad.1_fixp, .Lfunc_end5-arrayLoad.1_fixp
	.cfi_endproc
                                        # -- End function
	.p2align	4, 0x90         # -- Begin function cconv.2_fixp
	.type	cconv.2_fixp,@function
cconv.2_fixp:                           # @cconv.2_fixp
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	xorl	%eax, %eax
	movq	%rdi, -8(%rbp)          # 8-byte Spill
	movq	%rsi, -16(%rbp)         # 8-byte Spill
	movq	%rdx, -24(%rbp)         # 8-byte Spill
	movl	%ecx, -28(%rbp)         # 4-byte Spill
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jmp	.LBB6_1
.LBB6_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB6_3 Depth 2
	movl	-32(%rbp), %eax         # 4-byte Reload
	movl	-28(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -36(%rbp)         # 4-byte Spill
	jge	.LBB6_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB6_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_3:                                # %for.cond1
                                        #   Parent Loop BB6_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-40(%rbp), %eax         # 4-byte Reload
	movl	-28(%rbp), %ecx         # 4-byte Reload
	cmpl	%ecx, %eax
	movl	%eax, -44(%rbp)         # 4-byte Spill
	jge	.LBB6_6
# %bb.4:                                # %for.body3
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-44(%rbp), %eax         # 4-byte Reload
	movslq	%eax, %rcx
	movq	-16(%rbp), %rdx         # 8-byte Reload
	movss	(%rdx,%rcx,4), %xmm0    # xmm0 = mem[0],zero,zero,zero
	movl	-36(%rbp), %esi         # 4-byte Reload
	subl	%eax, %esi
	addl	$10, %esi
	movl	%esi, %eax
	cltd
	movl	$10, %esi
	idivl	%esi
	movslq	%edx, %rcx
	movq	-8(%rbp), %rdi          # 8-byte Reload
	mulss	(%rdi,%rcx,4), %xmm0
	movl	-36(%rbp), %edx         # 4-byte Reload
	movslq	%edx, %rcx
	movq	-24(%rbp), %r8          # 8-byte Reload
	addss	(%r8,%rcx,4), %xmm0
	movss	%xmm0, (%r8,%rcx,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB6_3 Depth=2
	movl	-44(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -40(%rbp)         # 4-byte Spill
	jmp	.LBB6_3
.LBB6_6:                                # %for.end
                                        #   in Loop: Header=BB6_1 Depth=1
	jmp	.LBB6_7
.LBB6_7:                                # %for.inc9
                                        #   in Loop: Header=BB6_1 Depth=1
	movl	-36(%rbp), %eax         # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -32(%rbp)         # 4-byte Spill
	jmp	.LBB6_1
.LBB6_8:                                # %for.end11
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end6:
	.size	cconv.2_fixp, .Lfunc_end6-cconv.2_fixp
	.cfi_endproc
                                        # -- End function
	.type	.L.str,@object          # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"%f"
	.size	.L.str, 3

	.type	.L.str.1,@object        # @.str.1
.L.str.1:
	.asciz	"%f, "
	.size	.L.str.1, 5


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
	.addrsig_sym __isoc99_scanf
	.addrsig_sym arrayInit
	.addrsig_sym printArray
	.addrsig_sym printf
	.addrsig_sym arrayLoad.1_fixp
	.addrsig_sym cconv.2_fixp
