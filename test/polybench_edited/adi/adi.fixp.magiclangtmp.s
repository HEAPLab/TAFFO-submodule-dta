	.text
	.file	"adi.c"
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI0_0:
	.quad	4733283208366391296     # double 268435456
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
	subq	$640152, %rsp           # imm = 0x9C498
	.cfi_offset %rbx, -24
	xorl	%eax, %eax
	movl	%edi, -640020(%rbp)     # 4-byte Spill
	movq	%rsi, -640032(%rbp)     # 8-byte Spill
	movl	%eax, -640036(%rbp)     # 4-byte Spill
.LBB0_1:                                # %for.cond
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_3 Depth 2
	movl	-640036(%rbp), %eax     # 4-byte Reload
	cmpl	$200, %eax
	movl	%eax, -640040(%rbp)     # 4-byte Spill
	jge	.LBB0_8
# %bb.2:                                # %for.body
                                        #   in Loop: Header=BB0_1 Depth=1
	xorl	%eax, %eax
	movl	%eax, -640044(%rbp)     # 4-byte Spill
	jmp	.LBB0_3
.LBB0_3:                                # %for.cond7
                                        #   Parent Loop BB0_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-640044(%rbp), %eax     # 4-byte Reload
	cmpl	$200, %eax
	movl	%eax, -640048(%rbp)     # 4-byte Spill
	jge	.LBB0_6
# %bb.4:                                # %for.body9
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-640040(%rbp), %eax     # 4-byte Reload
	addl	$200, %eax
	movl	-640048(%rbp), %ecx     # 4-byte Reload
	subl	%ecx, %eax
	shll	$23, %eax
	movl	%eax, %eax
                                        # kill: def $rax killed $eax
	xorl	%edx, %edx
                                        # kill: def $rdx killed $edx
	movl	$200, %esi
	divq	%rsi
	shlq	$7, %rax
	movl	%eax, %edi
	movl	-640040(%rbp), %r8d     # 4-byte Reload
	movslq	%r8d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	leaq	-160016(%rbp), %rsi
	addq	%rax, %rsi
	movslq	%ecx, %rax
	shrl	$2, %edi
	movl	%edi, (%rsi,%rax,4)
# %bb.5:                                # %for.inc
                                        #   in Loop: Header=BB0_3 Depth=2
	movl	-640048(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640044(%rbp)     # 4-byte Spill
	jmp	.LBB0_3
.LBB0_6:                                # %for.end
                                        #   in Loop: Header=BB0_1 Depth=1
	jmp	.LBB0_7
.LBB0_7:                                # %for.inc13
                                        #   in Loop: Header=BB0_1 Depth=1
	movl	-640040(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640036(%rbp)     # 4-byte Spill
	jmp	.LBB0_1
.LBB0_8:                                # %for.end15
	xorl	%eax, %eax
	movl	$10737418, DX.fixp      # imm = 0xA3D70A
	movl	$10737418, DY.fixp      # imm = 0xA3D70A
	movl	$21474836, DT.fixp      # imm = 0x147AE14
	movl	$-2147483648, B1.fixp   # imm = 0x80000000
	movl	$-2147483648, B2.fixp   # imm = 0x80000000
	movl	B1.fixp, %ecx
	movl	DT.fixp, %edx
	movl	%ecx, %ecx
	movl	%ecx, %esi
	movl	%edx, %ecx
	movl	%ecx, %edi
	imulq	%rdi, %rsi
	shrq	$31, %rsi
	movl	%esi, %ecx
	movl	DX.fixp, %edx
	movl	DX.fixp, %r8d
	movl	%edx, %edx
	movl	%edx, %esi
	movl	%r8d, %edx
	movl	%edx, %edi
	imulq	%rdi, %rsi
	shrq	$31, %rsi
	movl	%esi, %edx
	movl	%ecx, %ecx
	movl	%ecx, %esi
	shlq	$31, %rsi
	movl	%edx, %ecx
	movl	%ecx, %edi
	movl	%eax, -640052(%rbp)     # 4-byte Spill
	movq	%rsi, %rax
	xorl	%ecx, %ecx
	movl	%ecx, %edx
	divq	%rdi
	shrq	$8, %rax
	movl	%eax, %ecx
	movl	%ecx, mul1.fixp
	movl	B2.fixp, %ecx
	movl	DT.fixp, %r8d
	movl	%ecx, %ecx
	movl	%ecx, %eax
	movl	%r8d, %ecx
	movl	%ecx, %esi
	imulq	%rsi, %rax
	shrq	$31, %rax
	movl	%eax, %ecx
	movl	DY.fixp, %r8d
	movl	DY.fixp, %r9d
	movl	%r8d, %r8d
	movl	%r8d, %eax
	movl	%r9d, %r8d
	movl	%r8d, %esi
	imulq	%rsi, %rax
	shrq	$31, %rax
	movl	%eax, %r8d
	movl	%ecx, %ecx
	movl	%ecx, %eax
	shlq	$31, %rax
	movl	%r8d, %ecx
	movl	%ecx, %esi
	xorl	%ecx, %ecx
	movl	%ecx, %edx
	divq	%rsi
	shrq	$8, %rax
	movl	%eax, %ecx
	movl	%ecx, mul2.fixp
	movl	mul1.fixp, %ecx
	shrl	$1, %ecx
	movl	-640052(%rbp), %r8d     # 4-byte Reload
	subl	%ecx, %r8d
	movslq	%r8d, %rax
	cqto
	movl	$2, %esi
	idivq	%rsi
	movl	%eax, %ecx
	shll	$1, %ecx
	movl	%ecx, a.fixp
	movl	mul1.fixp, %ecx
	addl	$4194304, %ecx          # imm = 0x400000
	movl	%ecx, b.fixp
	movl	a.fixp, %ecx
	movl	%ecx, c.fixp
	movl	mul2.fixp, %ecx
	shrl	$1, %ecx
	movl	-640052(%rbp), %r8d     # 4-byte Reload
	subl	%ecx, %r8d
	movslq	%r8d, %rax
	cqto
	idivq	%rsi
	movl	%eax, %ecx
	shll	$1, %ecx
	movl	%ecx, d.fixp
	movl	mul2.fixp, %ecx
	addl	$8388608, %ecx          # imm = 0x800000
	movl	%ecx, e.fixp
	movl	d.fixp, %ecx
	movl	%ecx, f.fixp
	movl	$1, %ecx
	movl	%ecx, -640056(%rbp)     # 4-byte Spill
.LBB0_9:                                # %for.cond27
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_11 Depth 2
                                        #       Child Loop BB0_13 Depth 3
                                        #       Child Loop BB0_17 Depth 3
                                        #     Child Loop BB0_23 Depth 2
                                        #       Child Loop BB0_25 Depth 3
                                        #       Child Loop BB0_29 Depth 3
	movl	-640056(%rbp), %eax     # 4-byte Reload
	cmpl	$100, %eax
	movl	%eax, -640060(%rbp)     # 4-byte Spill
	jg	.LBB0_36
# %bb.10:                               # %for.body30
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	$1, %eax
	movl	%eax, -640064(%rbp)     # 4-byte Spill
	jmp	.LBB0_11
.LBB0_11:                               # %for.cond31
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_13 Depth 3
                                        #       Child Loop BB0_17 Depth 3
	movl	-640064(%rbp), %eax     # 4-byte Reload
	cmpl	$199, %eax
	movl	%eax, -640068(%rbp)     # 4-byte Spill
	jge	.LBB0_22
# %bb.12:                               # %for.body34
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-640068(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	movl	$536870912, -320016(%rbp,%rcx,4) # imm = 0x20000000
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-480016(%rbp), %rdx
	addq	%rcx, %rdx
	movl	$0, (%rdx)
	movslq	%eax, %rcx
	movl	-320016(%rbp,%rcx,4), %esi
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-640016(%rbp), %rdx
	addq	%rcx, %rdx
	sarl	$7, %esi
	movl	%esi, (%rdx)
	movl	$1, %esi
	movl	%esi, -640072(%rbp)     # 4-byte Spill
.LBB0_13:                               # %for.cond47
                                        #   Parent Loop BB0_9 Depth=1
                                        #     Parent Loop BB0_11 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-640072(%rbp), %eax     # 4-byte Reload
	cmpl	$199, %eax
	movl	%eax, -640076(%rbp)     # 4-byte Spill
	jge	.LBB0_16
# %bb.14:                               # %for.body50
                                        #   in Loop: Header=BB0_13 Depth=3
	xorl	%eax, %eax
	movl	%eax, %ecx
	subl	c.fixp, %ecx
	movl	a.fixp, %edx
	movl	-640068(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rdi
	imulq	$800, %rdi, %rdi        # imm = 0x320
	leaq	-480016(%rbp), %r8
	movq	%r8, %r9
	addq	%rdi, %r9
	movl	-640076(%rbp), %r10d    # 4-byte Reload
	subl	$1, %r10d
	movslq	%r10d, %rdi
	movl	(%r9,%rdi,4), %r10d
	movslq	%edx, %rdi
	movslq	%r10d, %r9
	imulq	%r9, %rdi
	sarq	$32, %rdi
	movl	%edi, %edx
	movl	b.fixp, %r10d
	shrl	$2, %r10d
	addl	%r10d, %edx
	movslq	%ecx, %rdi
	shlq	$20, %rdi
	movslq	%edx, %r9
	movl	%eax, -640080(%rbp)     # 4-byte Spill
	movq	%rdi, %rax
	cqto
	idivq	%r9
	shlq	$8, %rax
	movl	%eax, %ecx
	movslq	%esi, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	movq	%r8, %rdi
	addq	%rax, %rdi
	movl	-640076(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rax
	movl	%ecx, (%rdi,%rax,4)
	movl	-640080(%rbp), %ecx     # 4-byte Reload
	subl	d.fixp, %ecx
	movslq	%r10d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	leaq	-160016(%rbp), %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	subl	$1, %esi
	movslq	%esi, %rax
	movl	(%r9,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r9
	imulq	%r9, %rax
	sarq	$32, %rax
	movl	%eax, %ecx
	movslq	d.fixp, %rax
	shlq	$1, %rax
	sarq	$1, %rax
	movl	%eax, %esi
	sarl	$2, %esi
	addl	$1048576, %esi          # imm = 0x100000
	movslq	%r10d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	movq	%rdi, %r9
	addq	%rax, %r9
	movl	-640068(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rax
	movl	(%r9,%rax,4), %ebx
	movslq	%esi, %rax
	movslq	%ebx, %r9
	imulq	%r9, %rax
	sarq	$29, %rax
	movl	%eax, %esi
	addl	%esi, %ecx
	movl	f.fixp, %esi
	movslq	%r10d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	addq	%rax, %rdi
	addl	$1, %r11d
	movslq	%r11d, %rax
	movl	(%rdi,%rax,4), %r11d
	movslq	%esi, %rax
	movslq	%r11d, %rdi
	imulq	%rdi, %rax
	sarq	$32, %rax
	movl	%eax, %esi
	subl	%esi, %ecx
	movl	a.fixp, %esi
	movl	-640068(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	leaq	-640016(%rbp), %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	subl	$1, %r10d
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %r10d
	movslq	%esi, %rax
	movslq	%r10d, %r9
	imulq	%r9, %rax
	sarq	$31, %rax
	movl	%eax, %esi
	sarl	$6, %ecx
	subl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	movq	%rdi, %r9
	addq	%rax, %r9
	movl	-640076(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rax
	shll	$9, %ecx
	movl	%ecx, (%r9,%rax,4)
	movl	a.fixp, %ecx
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	addq	%rax, %r8
	subl	$1, %esi
	movslq	%esi, %rax
	movl	(%r8,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r8
	imulq	%r8, %rax
	sarq	$32, %rax
	movl	%eax, %ecx
	movl	b.fixp, %esi
	shrl	$2, %esi
	addl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	addq	%rax, %rdi
	movl	-640076(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rax
	movslq	(%rdi,%rax,4), %r8
	shlq	$20, %r8
	movslq	%ecx, %r9
	movq	%rax, -640088(%rbp)     # 8-byte Spill
	movq	%r8, %rax
	cqto
	idivq	%r9
	shlq	$7, %rax
	movl	%eax, %ecx
	sarl	$7, %ecx
	movq	-640088(%rbp), %rax     # 8-byte Reload
	movl	%ecx, (%rdi,%rax,4)
# %bb.15:                               # %for.inc109
                                        #   in Loop: Header=BB0_13 Depth=3
	movl	-640076(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640072(%rbp)     # 4-byte Spill
	jmp	.LBB0_13
.LBB0_16:                               # %for.end111
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-640068(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	movl	$536870912, -160816(%rbp,%rcx,4) # imm = 0x20000000
	movl	$198, %edx
	movl	%edx, -640092(%rbp)     # 4-byte Spill
.LBB0_17:                               # %for.cond115
                                        #   Parent Loop BB0_9 Depth=1
                                        #     Parent Loop BB0_11 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-640092(%rbp), %eax     # 4-byte Reload
	cmpl	$1, %eax
	movl	%eax, -640096(%rbp)     # 4-byte Spill
	jl	.LBB0_20
# %bb.18:                               # %for.body118
                                        #   in Loop: Header=BB0_17 Depth=3
	movl	-640068(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-480016(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-640096(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	addl	$1, %esi
	movslq	%esi, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-320016(%rbp), %rdx
	movq	%rdx, %r8
	addq	%rcx, %r8
	movslq	%eax, %rcx
	movl	(%r8,%rcx,4), %esi
	movslq	%edi, %rcx
	movslq	%esi, %r8
	imulq	%r8, %rcx
	sarq	$30, %rcx
	movl	%ecx, %esi
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-640016(%rbp), %r8
	addq	%rcx, %r8
	movl	-640096(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%r8,%rcx,4), %r9d
	sarl	$7, %esi
	addl	%r9d, %esi
	movslq	%edi, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	addq	%rcx, %rdx
	movslq	%eax, %rcx
	shll	$7, %esi
	movl	%esi, (%rdx,%rcx,4)
# %bb.19:                               # %for.inc138
                                        #   in Loop: Header=BB0_17 Depth=3
	movl	-640096(%rbp), %eax     # 4-byte Reload
	addl	$-1, %eax
	movl	%eax, -640092(%rbp)     # 4-byte Spill
	jmp	.LBB0_17
.LBB0_20:                               # %for.end139
                                        #   in Loop: Header=BB0_11 Depth=2
	jmp	.LBB0_21
.LBB0_21:                               # %for.inc140
                                        #   in Loop: Header=BB0_11 Depth=2
	movl	-640068(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640064(%rbp)     # 4-byte Spill
	jmp	.LBB0_11
.LBB0_22:                               # %for.end142
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	$1, %eax
	movl	%eax, -640100(%rbp)     # 4-byte Spill
	jmp	.LBB0_23
.LBB0_23:                               # %for.cond143
                                        #   Parent Loop BB0_9 Depth=1
                                        # =>  This Loop Header: Depth=2
                                        #       Child Loop BB0_25 Depth 3
                                        #       Child Loop BB0_29 Depth 3
	movl	-640100(%rbp), %eax     # 4-byte Reload
	cmpl	$199, %eax
	movl	%eax, -640104(%rbp)     # 4-byte Spill
	jge	.LBB0_34
# %bb.24:                               # %for.body146
                                        #   in Loop: Header=BB0_23 Depth=2
	movl	-640104(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-160016(%rbp), %rdx
	movq	%rdx, %rsi
	addq	%rcx, %rsi
	movl	$268435456, (%rsi)      # imm = 0x10000000
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-480016(%rbp), %rsi
	addq	%rcx, %rsi
	movl	$0, (%rsi)
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	addq	%rcx, %rdx
	movl	(%rdx), %edi
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-640016(%rbp), %rdx
	addq	%rcx, %rdx
	sarl	$6, %edi
	movl	%edi, (%rdx)
	movl	$1, %edi
	movl	%edi, -640108(%rbp)     # 4-byte Spill
.LBB0_25:                               # %for.cond159
                                        #   Parent Loop BB0_9 Depth=1
                                        #     Parent Loop BB0_23 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-640108(%rbp), %eax     # 4-byte Reload
	cmpl	$199, %eax
	movl	%eax, -640112(%rbp)     # 4-byte Spill
	jge	.LBB0_28
# %bb.26:                               # %for.body162
                                        #   in Loop: Header=BB0_25 Depth=3
	xorl	%eax, %eax
	movl	%eax, %ecx
	subl	f.fixp, %ecx
	movl	d.fixp, %edx
	movl	-640104(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rdi
	imulq	$800, %rdi, %rdi        # imm = 0x320
	leaq	-480016(%rbp), %r8
	movq	%r8, %r9
	addq	%rdi, %r9
	movl	-640112(%rbp), %r10d    # 4-byte Reload
	subl	$1, %r10d
	movslq	%r10d, %rdi
	movl	(%r9,%rdi,4), %r10d
	movslq	%edx, %rdi
	movslq	%r10d, %r9
	imulq	%r9, %rdi
	sarq	$32, %rdi
	movl	%edi, %edx
	movl	e.fixp, %r10d
	shrl	$2, %r10d
	addl	%r10d, %edx
	movslq	%ecx, %rdi
	shlq	$21, %rdi
	movslq	%edx, %r9
	movl	%eax, -640116(%rbp)     # 4-byte Spill
	movq	%rdi, %rax
	cqto
	idivq	%r9
	shlq	$7, %rax
	movl	%eax, %ecx
	movslq	%esi, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	movq	%r8, %rdi
	addq	%rax, %rdi
	movl	-640112(%rbp), %r10d    # 4-byte Reload
	movslq	%r10d, %rax
	movl	%ecx, (%rdi,%rax,4)
	movl	-640116(%rbp), %ecx     # 4-byte Reload
	subl	a.fixp, %ecx
	subl	$1, %esi
	movslq	%esi, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	leaq	-320016(%rbp), %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r9
	imulq	%r9, %rax
	sarq	$32, %rax
	movl	%eax, %ecx
	movslq	a.fixp, %rax
	shlq	$1, %rax
	sarq	$1, %rax
	movl	%eax, %esi
	sarl	$1, %esi
	addl	$1048576, %esi          # imm = 0x100000
	movl	-640104(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	movq	%rdi, %r9
	addq	%rax, %r9
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %ebx
	movslq	%esi, %rax
	movslq	%ebx, %r9
	imulq	%r9, %rax
	sarq	$30, %rax
	movl	%eax, %esi
	addl	%esi, %ecx
	movl	c.fixp, %esi
	addl	$1, %r11d
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	addq	%rax, %rdi
	movslq	%r10d, %rax
	movl	(%rdi,%rax,4), %r11d
	movslq	%esi, %rax
	movslq	%r11d, %rdi
	imulq	%rdi, %rax
	sarq	$32, %rax
	movl	%eax, %esi
	subl	%esi, %ecx
	movl	d.fixp, %esi
	movl	-640104(%rbp), %r11d    # 4-byte Reload
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	leaq	-640016(%rbp), %rdi
	movq	%rdi, %r9
	addq	%rax, %r9
	subl	$1, %r10d
	movslq	%r10d, %rax
	movl	(%r9,%rax,4), %r10d
	movslq	%esi, %rax
	movslq	%r10d, %r9
	imulq	%r9, %rax
	sarq	$31, %rax
	movl	%eax, %esi
	sarl	$5, %ecx
	subl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	movq	%rdi, %r9
	addq	%rax, %r9
	movl	-640112(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rax
	shll	$8, %ecx
	movl	%ecx, (%r9,%rax,4)
	movl	d.fixp, %ecx
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	addq	%rax, %r8
	subl	$1, %esi
	movslq	%esi, %rax
	movl	(%r8,%rax,4), %esi
	movslq	%ecx, %rax
	movslq	%esi, %r8
	imulq	%r8, %rax
	sarq	$32, %rax
	movl	%eax, %ecx
	movl	e.fixp, %esi
	shrl	$2, %esi
	addl	%esi, %ecx
	movslq	%r11d, %rax
	imulq	$800, %rax, %rax        # imm = 0x320
	addq	%rax, %rdi
	movl	-640112(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rax
	movslq	(%rdi,%rax,4), %r8
	shlq	$21, %r8
	movslq	%ecx, %r9
	movq	%rax, -640128(%rbp)     # 8-byte Spill
	movq	%r8, %rax
	cqto
	idivq	%r9
	shlq	$7, %rax
	movl	%eax, %ecx
	sarl	$7, %ecx
	movq	-640128(%rbp), %rax     # 8-byte Reload
	movl	%ecx, (%rdi,%rax,4)
# %bb.27:                               # %for.inc221
                                        #   in Loop: Header=BB0_25 Depth=3
	movl	-640112(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640108(%rbp)     # 4-byte Spill
	jmp	.LBB0_25
.LBB0_28:                               # %for.end223
                                        #   in Loop: Header=BB0_23 Depth=2
	movl	-640104(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-160016(%rbp), %rdx
	addq	%rcx, %rdx
	movl	$268435456, 796(%rdx)   # imm = 0x10000000
	movl	$198, %esi
	movl	%esi, -640132(%rbp)     # 4-byte Spill
.LBB0_29:                               # %for.cond227
                                        #   Parent Loop BB0_9 Depth=1
                                        #     Parent Loop BB0_23 Depth=2
                                        # =>    This Inner Loop Header: Depth=3
	movl	-640132(%rbp), %eax     # 4-byte Reload
	cmpl	$1, %eax
	movl	%eax, -640136(%rbp)     # 4-byte Spill
	jl	.LBB0_32
# %bb.30:                               # %for.body230
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	-640104(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-480016(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-640136(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %edi
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-160016(%rbp), %rdx
	movq	%rdx, %r8
	addq	%rcx, %r8
	addl	$1, %esi
	movslq	%esi, %rcx
	movl	(%r8,%rcx,4), %esi
	movslq	%edi, %rcx
	movslq	%esi, %r8
	imulq	%r8, %rcx
	sarq	$30, %rcx
	movl	%ecx, %esi
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-640016(%rbp), %r8
	addq	%rcx, %r8
	movl	-640136(%rbp), %edi     # 4-byte Reload
	movslq	%edi, %rcx
	movl	(%r8,%rcx,4), %r9d
	sarl	$6, %esi
	addl	%r9d, %esi
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	addq	%rcx, %rdx
	movslq	%edi, %rcx
	shll	$6, %esi
	movl	%esi, (%rdx,%rcx,4)
# %bb.31:                               # %for.inc250
                                        #   in Loop: Header=BB0_29 Depth=3
	movl	-640136(%rbp), %eax     # 4-byte Reload
	addl	$-1, %eax
	movl	%eax, -640132(%rbp)     # 4-byte Spill
	jmp	.LBB0_29
.LBB0_32:                               # %for.end252
                                        #   in Loop: Header=BB0_23 Depth=2
	jmp	.LBB0_33
.LBB0_33:                               # %for.inc253
                                        #   in Loop: Header=BB0_23 Depth=2
	movl	-640104(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640100(%rbp)     # 4-byte Spill
	jmp	.LBB0_23
.LBB0_34:                               # %for.end255
                                        #   in Loop: Header=BB0_9 Depth=1
	jmp	.LBB0_35
.LBB0_35:                               # %for.inc256
                                        #   in Loop: Header=BB0_9 Depth=1
	movl	-640060(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640056(%rbp)     # 4-byte Spill
	jmp	.LBB0_9
.LBB0_36:                               # %for.end258
	xorl	%eax, %eax
	movl	%eax, -640140(%rbp)     # 4-byte Spill
	jmp	.LBB0_37
.LBB0_37:                               # %for.cond259
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB0_39 Depth 2
	movl	-640140(%rbp), %eax     # 4-byte Reload
	cmpl	$200, %eax
	movl	%eax, -640144(%rbp)     # 4-byte Spill
	jge	.LBB0_46
# %bb.38:                               # %for.body262
                                        #   in Loop: Header=BB0_37 Depth=1
	xorl	%eax, %eax
	movl	%eax, -640148(%rbp)     # 4-byte Spill
	jmp	.LBB0_39
.LBB0_39:                               # %for.cond263
                                        #   Parent Loop BB0_37 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	-640148(%rbp), %eax     # 4-byte Reload
	cmpl	$200, %eax
	movl	%eax, -640152(%rbp)     # 4-byte Spill
	jge	.LBB0_44
# %bb.40:                               # %for.body266
                                        #   in Loop: Header=BB0_39 Depth=2
	movl	-640144(%rbp), %eax     # 4-byte Reload
	imull	$200, %eax, %ecx
	movl	-640152(%rbp), %edx     # 4-byte Reload
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
	movabsq	$.L.str.6, %rsi
	movb	$0, %al
	callq	fprintf
	movl	%eax, -640156(%rbp)     # 4-byte Spill
.LBB0_42:                               # %if.end
                                        #   in Loop: Header=BB0_39 Depth=2
	movsd	.LCPI0_0(%rip), %xmm0   # xmm0 = mem[0],zero
	movq	stdout, %rdi
	movl	-640144(%rbp), %eax     # 4-byte Reload
	movslq	%eax, %rcx
	imulq	$800, %rcx, %rcx        # imm = 0x320
	leaq	-160016(%rbp), %rdx
	addq	%rcx, %rdx
	movl	-640152(%rbp), %esi     # 4-byte Reload
	movslq	%esi, %rcx
	movl	(%rdx,%rcx,4), %r8d
	cvtsi2sdl	%r8d, %xmm1
	divsd	%xmm0, %xmm1
	movabsq	$.L.str.7, %rcx
	movq	%rcx, %rsi
	movaps	%xmm1, %xmm0
	movb	$1, %al
	callq	fprintf
	movl	%eax, -640160(%rbp)     # 4-byte Spill
# %bb.43:                               # %for.inc276
                                        #   in Loop: Header=BB0_39 Depth=2
	movl	-640152(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640148(%rbp)     # 4-byte Spill
	jmp	.LBB0_39
.LBB0_44:                               # %for.end278
                                        #   in Loop: Header=BB0_37 Depth=1
	jmp	.LBB0_45
.LBB0_45:                               # %for.inc279
                                        #   in Loop: Header=BB0_37 Depth=1
	movl	-640144(%rbp), %eax     # 4-byte Reload
	addl	$1, %eax
	movl	%eax, -640140(%rbp)     # 4-byte Spill
	jmp	.LBB0_37
.LBB0_46:                               # %for.end281
	xorl	%eax, %eax
	addq	$640152, %rsp           # imm = 0x9C498
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
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
	.type	.L.str.6,@object        # @.str.6
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str.6:
	.asciz	"\n"
	.size	.L.str.6, 2

	.type	.L.str.7,@object        # @.str.7
.L.str.7:
	.asciz	"%0.16lf "
	.size	.L.str.7, 9

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
	.addrsig_sym fprintf
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
	.addrsig_sym stdout
	.addrsig_sym DX.fixp
	.addrsig_sym DY.fixp
	.addrsig_sym DT.fixp
	.addrsig_sym B1.fixp
	.addrsig_sym B2.fixp
	.addrsig_sym mul1.fixp
	.addrsig_sym mul2.fixp
	.addrsig_sym a.fixp
	.addrsig_sym b.fixp
	.addrsig_sym c.fixp
	.addrsig_sym d.fixp
	.addrsig_sym e.fixp
	.addrsig_sym f.fixp
