	.text
	.file	"deriche.c"
	.globl	gettime                 # -- Begin function gettime
	.p2align	4, 0x90
	.type	gettime,@function
gettime:                                # @gettime
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	xorl	%eax, %eax
	callq	clock
	cltq
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end0:
	.size	gettime, .Lfunc_end0-gettime
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_START   # -- Begin function TIMING_CPUCLOCK_START
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_START,@function
TIMING_CPUCLOCK_START:                  # @TIMING_CPUCLOCK_START
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	callq	gettime
	movq	%rax, time_that_takes(%rip)
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end1:
	.size	TIMING_CPUCLOCK_START, .Lfunc_end1-TIMING_CPUCLOCK_START
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_TOGGLE  # -- Begin function TIMING_CPUCLOCK_TOGGLE
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_TOGGLE,@function
TIMING_CPUCLOCK_TOGGLE:                 # @TIMING_CPUCLOCK_TOGGLE
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	callq	gettime
	subq	time_that_takes(%rip), %rax
	movq	%rax, time_that_takes(%rip)
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end2:
	.size	TIMING_CPUCLOCK_TOGGLE, .Lfunc_end2-TIMING_CPUCLOCK_TOGGLE
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_S       # -- Begin function TIMING_CPUCLOCK_S
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_S,@function
TIMING_CPUCLOCK_S:                      # @TIMING_CPUCLOCK_S
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movq	time_that_takes(%rip), %rax
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end3:
	.size	TIMING_CPUCLOCK_S, .Lfunc_end3-TIMING_CPUCLOCK_S
	.cfi_endproc
                                        # -- End function
	.globl	TIMING_CPUCLOCK_PRINT   # -- Begin function TIMING_CPUCLOCK_PRINT
	.p2align	4, 0x90
	.type	TIMING_CPUCLOCK_PRINT,@function
TIMING_CPUCLOCK_PRINT:                  # @TIMING_CPUCLOCK_PRINT
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	movq	stderr(%rip), %rdi
	movq	time_that_takes(%rip), %rdx
	movl	$.L.str, %esi
	xorl	%eax, %eax
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	jmp	fprintf                 # TAILCALL
.Lfunc_end4:
	.size	TIMING_CPUCLOCK_PRINT, .Lfunc_end4-TIMING_CPUCLOCK_PRINT
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst8,"aM",@progbits,8
	.p2align	3               # -- Begin function main
.LCPI5_0:
	.quad	4485585228861014016     # double 7.4505805969238281E-9
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
	pushq	%r13
	pushq	%r12
	pushq	%rbx
	subq	$393240, %rsp           # imm = 0x60018
	.cfi_offset %rbx, -56
	.cfi_offset %r12, -48
	.cfi_offset %r13, -40
	.cfi_offset %r14, -32
	.cfi_offset %r15, -24
	callq	TIMING_CPUCLOCK_START
	leaq	-393276(%rbp), %rax
	movl	$16236544, %r8d         # imm = 0xF7C000
	xorl	%edx, %edx
	movl	$2147516417, %esi       # imm = 0x80008001
	.p2align	4, 0x90
.LBB5_1:                                # %for.cond8.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_2 Depth 2
	movl	%r8d, %edi
	xorl	%ebx, %ebx
	.p2align	4, 0x90
.LBB5_2:                                # %for.body10
                                        #   Parent Loop BB5_1 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	leal	-16236544(%rdi), %ecx
	andl	$1073725440, %ecx       # imm = 0x3FFFC000
	imulq	%rsi, %rcx
	shrq	$32, %rcx
	andl	$1073709056, %ecx       # imm = 0x3FFF8000
	movl	%ecx, -4(%rax,%rbx,4)
	movl	%edi, %ecx
	andl	$1073725440, %ecx       # imm = 0x3FFFC000
	imulq	%rsi, %rcx
	shrq	$32, %rcx
	andl	$1073709056, %ecx       # imm = 0x3FFF8000
	movl	%ecx, (%rax,%rbx,4)
	addq	$2, %rbx
	addl	$32473088, %edi         # imm = 0x1EF8000
	cmpq	$128, %rbx
	jne	.LBB5_2
# %bb.3:                                # %for.inc14
                                        #   in Loop: Header=BB5_1 Depth=1
	addq	$1, %rdx
	addl	$5128192, %r8d          # imm = 0x4E4000
	addq	$512, %rax              # imm = 0x200
	cmpq	$192, %rdx
	jne	.LBB5_1
# %bb.4:                                # %for.cond65.preheader.preheader
	leaq	-393280(%rbp), %r9
	leaq	-294976(%rbp), %r10
	xorl	%r8d, %r8d
	.p2align	4, 0x90
.LBB5_5:                                # %for.cond65.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_6 Depth 2
	xorl	%esi, %esi
	xorl	%ebx, %ebx
	xorl	%edi, %edi
	xorl	%edx, %edx
	.p2align	4, 0x90
.LBB5_6:                                # %for.body68
                                        #   Parent Loop BB5_5 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movslq	%edx, %r11
	movl	%edi, %edx
	movslq	%ebx, %rdi
	movslq	(%r9,%rsi,4), %rbx
	imulq	$-202595388, %rbx, %rcx # imm = 0xF3ECA3C4
	shrq	$30, %rcx
	imulq	$118336085, %rdi, %rax  # imm = 0x70DAA55
	shrq	$30, %rax
	addl	%ecx, %eax
	movslq	%edx, %rcx
	imulq	$451452825, %rcx, %rcx  # imm = 0x1AE89F99
	shrq	$28, %rcx
	sarl	%eax
	sarl	%ecx
	imulq	$-651257336, %r11, %rdi # imm = 0xD92E9A08
	shrq	$30, %rdi
	addl	%ecx, %edi
	addl	%eax, %edi
	movl	%edi, (%r10,%rsi,4)
	addq	$1, %rsi
                                        # kill: def $ebx killed $ebx killed $rbx
	cmpq	$128, %rsi
	jne	.LBB5_6
# %bb.7:                                # %for.inc95
                                        #   in Loop: Header=BB5_5 Depth=1
	addq	$1, %r8
	addq	$512, %r9               # imm = 0x200
	addq	$512, %r10              # imm = 0x200
	cmpq	$192, %r8
	jne	.LBB5_5
# %bb.8:                                # %for.cond102.preheader.preheader
	leaq	-196672(%rbp), %r9
	leaq	-393280(%rbp), %r10
	xorl	%r8d, %r8d
	.p2align	4, 0x90
.LBB5_9:                                # %for.cond102.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_10 Depth 2
	movl	$127, %esi
	xorl	%ebx, %ebx
	xorl	%edi, %edi
	xorl	%edx, %edx
	xorl	%eax, %eax
	.p2align	4, 0x90
.LBB5_10:                               # %for.body105
                                        #   Parent Loop BB5_9 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	cltq
	movslq	%edx, %rcx
	imulq	$-197226809, %rcx, %rcx # imm = 0xF43E8EC7
	shrq	$30, %rcx
	imulq	$122880314, %rax, %rax  # imm = 0x753013A
	shrq	$30, %rax
	addl	%ecx, %eax
	movslq	%edi, %rcx
	imulq	$451452825, %rcx, %rcx  # imm = 0x1AE89F99
	shrq	$28, %rcx
	sarl	%eax
	sarl	%ecx
	addl	%eax, %ecx
	movslq	%ebx, %rax
	movl	%edi, %ebx
	imulq	$-651257336, %rax, %rdi # imm = 0xD92E9A08
	shrq	$30, %rdi
	addl	%ecx, %edi
	movl	%edi, (%r9,%rsi,4)
	movl	%edx, %eax
	movl	(%r10,%rsi,4), %edx
	addq	$-1, %rsi
                                        # kill: def $edi killed $edi killed $rdi
	cmpq	$-1, %rsi
	jne	.LBB5_10
# %bb.11:                               # %for.inc127
                                        #   in Loop: Header=BB5_9 Depth=1
	addq	$1, %r8
	addq	$512, %r9               # imm = 0x200
	addq	$512, %r10              # imm = 0x200
	cmpq	$192, %r8
	jne	.LBB5_9
# %bb.12:                               # %vector.ph.preheader
	movl	$496, %eax              # imm = 0x1F0
	.p2align	4, 0x90
.LBB5_13:                               # %vector.ph
                                        # =>This Inner Loop Header: Depth=1
	movdqa	-295472(%rbp,%rax), %xmm0
	movdqa	-295456(%rbp,%rax), %xmm1
	movdqa	-295440(%rbp,%rax), %xmm2
	movdqa	-295424(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	movdqa	-197168(%rbp,%rax), %xmm4
	movdqa	-197152(%rbp,%rax), %xmm5
	movdqa	-197136(%rbp,%rax), %xmm6
	movdqa	-197120(%rbp,%rax), %xmm7
	psrad	$1, %xmm4
	paddd	%xmm0, %xmm4
	psrad	$1, %xmm5
	paddd	%xmm1, %xmm5
	movdqa	%xmm4, -98864(%rbp,%rax)
	movdqa	%xmm5, -98848(%rbp,%rax)
	psrad	$1, %xmm2
	psrad	$1, %xmm3
	psrad	$1, %xmm6
	paddd	%xmm2, %xmm6
	psrad	$1, %xmm7
	paddd	%xmm3, %xmm7
	movdqa	%xmm6, -98832(%rbp,%rax)
	movdqa	%xmm7, -98816(%rbp,%rax)
	movdqa	-295408(%rbp,%rax), %xmm0
	movdqa	-295392(%rbp,%rax), %xmm1
	movdqa	-197104(%rbp,%rax), %xmm2
	movdqa	-197088(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98800(%rbp,%rax)
	movdqa	%xmm3, -98784(%rbp,%rax)
	movdqa	-295376(%rbp,%rax), %xmm0
	movdqa	-295360(%rbp,%rax), %xmm1
	movdqa	-295344(%rbp,%rax), %xmm2
	movdqa	-295328(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	movdqa	-197072(%rbp,%rax), %xmm4
	movdqa	-197056(%rbp,%rax), %xmm5
	movdqa	-197040(%rbp,%rax), %xmm6
	movdqa	-197024(%rbp,%rax), %xmm7
	psrad	$1, %xmm4
	paddd	%xmm0, %xmm4
	psrad	$1, %xmm5
	paddd	%xmm1, %xmm5
	movdqa	%xmm4, -98768(%rbp,%rax)
	movdqa	%xmm5, -98752(%rbp,%rax)
	psrad	$1, %xmm2
	psrad	$1, %xmm3
	psrad	$1, %xmm6
	paddd	%xmm2, %xmm6
	psrad	$1, %xmm7
	paddd	%xmm3, %xmm7
	movdqa	%xmm6, -98736(%rbp,%rax)
	movdqa	%xmm7, -98720(%rbp,%rax)
	movdqa	-295312(%rbp,%rax), %xmm0
	movdqa	-295296(%rbp,%rax), %xmm1
	movdqa	-197008(%rbp,%rax), %xmm2
	movdqa	-196992(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98704(%rbp,%rax)
	movdqa	%xmm3, -98688(%rbp,%rax)
	movdqa	-295280(%rbp,%rax), %xmm0
	movdqa	-295264(%rbp,%rax), %xmm1
	movdqa	-295248(%rbp,%rax), %xmm2
	movdqa	-295232(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	movdqa	-196976(%rbp,%rax), %xmm4
	movdqa	-196960(%rbp,%rax), %xmm5
	movdqa	-196944(%rbp,%rax), %xmm6
	movdqa	-196928(%rbp,%rax), %xmm7
	psrad	$1, %xmm4
	paddd	%xmm0, %xmm4
	psrad	$1, %xmm5
	paddd	%xmm1, %xmm5
	movdqa	%xmm4, -98672(%rbp,%rax)
	movdqa	%xmm5, -98656(%rbp,%rax)
	psrad	$1, %xmm2
	psrad	$1, %xmm3
	psrad	$1, %xmm6
	paddd	%xmm2, %xmm6
	psrad	$1, %xmm7
	paddd	%xmm3, %xmm7
	movdqa	%xmm6, -98640(%rbp,%rax)
	movdqa	%xmm7, -98624(%rbp,%rax)
	movdqa	-295216(%rbp,%rax), %xmm0
	movdqa	-295200(%rbp,%rax), %xmm1
	movdqa	-196912(%rbp,%rax), %xmm2
	movdqa	-196896(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98608(%rbp,%rax)
	movdqa	%xmm3, -98592(%rbp,%rax)
	movdqa	-295184(%rbp,%rax), %xmm0
	movdqa	-295168(%rbp,%rax), %xmm1
	movdqa	-196880(%rbp,%rax), %xmm2
	movdqa	-196864(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98576(%rbp,%rax)
	movdqa	%xmm3, -98560(%rbp,%rax)
	movdqa	-295152(%rbp,%rax), %xmm0
	movdqa	-295136(%rbp,%rax), %xmm1
	movdqa	-196848(%rbp,%rax), %xmm2
	movdqa	-196832(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98544(%rbp,%rax)
	movdqa	%xmm3, -98528(%rbp,%rax)
	movdqa	-295120(%rbp,%rax), %xmm0
	movdqa	-295104(%rbp,%rax), %xmm1
	movdqa	-196816(%rbp,%rax), %xmm2
	movdqa	-196800(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98512(%rbp,%rax)
	movdqa	%xmm3, -98496(%rbp,%rax)
	movdqa	-295088(%rbp,%rax), %xmm0
	movdqa	-295072(%rbp,%rax), %xmm1
	movdqa	-196784(%rbp,%rax), %xmm2
	movdqa	-196768(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98480(%rbp,%rax)
	movdqa	%xmm3, -98464(%rbp,%rax)
	movdqa	-295056(%rbp,%rax), %xmm0
	movdqa	-295040(%rbp,%rax), %xmm1
	movdqa	-196752(%rbp,%rax), %xmm2
	movdqa	-196736(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98448(%rbp,%rax)
	movdqa	%xmm3, -98432(%rbp,%rax)
	movdqa	-295024(%rbp,%rax), %xmm0
	movdqa	-295008(%rbp,%rax), %xmm1
	movdqa	-196720(%rbp,%rax), %xmm2
	movdqa	-196704(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98416(%rbp,%rax)
	movdqa	%xmm3, -98400(%rbp,%rax)
	movdqa	-294992(%rbp,%rax), %xmm0
	movdqa	-294976(%rbp,%rax), %xmm1
	movdqa	-196688(%rbp,%rax), %xmm2
	movdqa	-196672(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98384(%rbp,%rax)
	movdqa	%xmm3, -98368(%rbp,%rax)
	addq	$512, %rax              # imm = 0x200
	cmpq	$98800, %rax            # imm = 0x181F0
	jne	.LBB5_13
# %bb.14:                               # %for.cond162.preheader.preheader
	leaq	-98368(%rbp), %r9
	leaq	-294976(%rbp), %r10
	xorl	%r8d, %r8d
	.p2align	4, 0x90
.LBB5_15:                               # %for.cond162.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_16 Depth 2
	xorl	%esi, %esi
	xorl	%edx, %edx
	xorl	%edi, %edi
	xorl	%ebx, %ebx
	.p2align	4, 0x90
.LBB5_16:                               # %for.body165
                                        #   Parent Loop BB5_15 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movslq	%ebx, %r11
	movl	%edi, %ebx
	movslq	%edx, %rdx
	movslq	(%r9,%rsi), %r14
	imulq	$-202595388, %r14, %rax # imm = 0xF3ECA3C4
	imulq	$118336085, %rdx, %rdx  # imm = 0x70DAA55
	shrq	$28, %rdx
	shrq	$29, %rax
	andl	$-2, %eax
	sarl	%edx
	movslq	%edi, %rdi
	imulq	$225726412, %rdi, %rcx  # imm = 0xD744FCC
	shrq	$28, %rcx
	imulq	$-651257336, %r11, %rdi # imm = 0xD92E9A08
	shrq	$30, %rdi
	addl	%ecx, %edi
	addl	%edx, %edi
	addl	%eax, %edi
	movl	%edi, (%r10,%rsi)
	addq	$512, %rsi              # imm = 0x200
	movl	%r14d, %edx
	cmpq	$98304, %rsi            # imm = 0x18000
	jne	.LBB5_16
# %bb.17:                               # %for.inc192
                                        #   in Loop: Header=BB5_15 Depth=1
	addq	$1, %r8
	addq	$4, %r9
	addq	$4, %r10
	cmpq	$128, %r8
	jne	.LBB5_15
# %bb.18:                               # %for.cond199.preheader.preheader
	leaq	-196672(%rbp), %r9
	leaq	-98368(%rbp), %r10
	xorl	%r8d, %r8d
	.p2align	4, 0x90
.LBB5_19:                               # %for.cond199.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_20 Depth 2
	movl	$97792, %esi            # imm = 0x17E00
	xorl	%edx, %edx
	xorl	%edi, %edi
	xorl	%ebx, %ebx
	xorl	%eax, %eax
	.p2align	4, 0x90
.LBB5_20:                               # %for.body202
                                        #   Parent Loop BB5_19 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movslq	%eax, %rcx
	imulq	$-197226809, %rcx, %rcx # imm = 0xF43E8EC7
	shrq	$28, %rcx
	movslq	%ebx, %rbx
	imulq	$122880314, %rbx, %rbx  # imm = 0x753013A
	shrq	$28, %rbx
	addl	%ecx, %ebx
	movslq	%edi, %rcx
	imulq	$451452825, %rcx, %rcx  # imm = 0x1AE89F99
	shrq	$28, %rcx
	sarl	%ebx
	sarl	%ecx
	addl	%ebx, %ecx
	movslq	%edx, %rbx
	movl	%edi, %edx
	imulq	$-651257336, %rbx, %rdi # imm = 0xD92E9A08
	shrq	$30, %rdi
	addl	%ecx, %edi
	movl	%edi, (%r9,%rsi)
	movl	%eax, %ebx
	movl	(%r10,%rsi), %eax
	addq	$-512, %rsi             # imm = 0xFE00
                                        # kill: def $edi killed $edi killed $rdi
	cmpq	$-512, %rsi             # imm = 0xFE00
	jne	.LBB5_20
# %bb.21:                               # %for.inc225
                                        #   in Loop: Header=BB5_19 Depth=1
	addq	$1, %r8
	addq	$4, %r9
	addq	$4, %r10
	cmpq	$128, %r8
	jne	.LBB5_19
# %bb.22:                               # %vector.ph88.preheader
	movl	$496, %eax              # imm = 0x1F0
	.p2align	4, 0x90
.LBB5_23:                               # %vector.ph88
                                        # =>This Inner Loop Header: Depth=1
	movdqa	-295472(%rbp,%rax), %xmm0
	movdqa	-295456(%rbp,%rax), %xmm1
	movdqa	-295440(%rbp,%rax), %xmm2
	movdqa	-295424(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	movdqa	-197168(%rbp,%rax), %xmm4
	movdqa	-197152(%rbp,%rax), %xmm5
	movdqa	-197136(%rbp,%rax), %xmm6
	movdqa	-197120(%rbp,%rax), %xmm7
	psrad	$1, %xmm4
	paddd	%xmm0, %xmm4
	psrad	$1, %xmm5
	paddd	%xmm1, %xmm5
	movdqa	%xmm4, -98864(%rbp,%rax)
	movdqa	%xmm5, -98848(%rbp,%rax)
	psrad	$1, %xmm2
	psrad	$1, %xmm3
	psrad	$1, %xmm6
	paddd	%xmm2, %xmm6
	psrad	$1, %xmm7
	paddd	%xmm3, %xmm7
	movdqa	%xmm6, -98832(%rbp,%rax)
	movdqa	%xmm7, -98816(%rbp,%rax)
	movdqa	-295408(%rbp,%rax), %xmm0
	movdqa	-295392(%rbp,%rax), %xmm1
	movdqa	-197104(%rbp,%rax), %xmm2
	movdqa	-197088(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98800(%rbp,%rax)
	movdqa	%xmm3, -98784(%rbp,%rax)
	movdqa	-295376(%rbp,%rax), %xmm0
	movdqa	-295360(%rbp,%rax), %xmm1
	movdqa	-295344(%rbp,%rax), %xmm2
	movdqa	-295328(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	movdqa	-197072(%rbp,%rax), %xmm4
	movdqa	-197056(%rbp,%rax), %xmm5
	movdqa	-197040(%rbp,%rax), %xmm6
	movdqa	-197024(%rbp,%rax), %xmm7
	psrad	$1, %xmm4
	paddd	%xmm0, %xmm4
	psrad	$1, %xmm5
	paddd	%xmm1, %xmm5
	movdqa	%xmm4, -98768(%rbp,%rax)
	movdqa	%xmm5, -98752(%rbp,%rax)
	psrad	$1, %xmm2
	psrad	$1, %xmm3
	psrad	$1, %xmm6
	paddd	%xmm2, %xmm6
	psrad	$1, %xmm7
	paddd	%xmm3, %xmm7
	movdqa	%xmm6, -98736(%rbp,%rax)
	movdqa	%xmm7, -98720(%rbp,%rax)
	movdqa	-295312(%rbp,%rax), %xmm0
	movdqa	-295296(%rbp,%rax), %xmm1
	movdqa	-197008(%rbp,%rax), %xmm2
	movdqa	-196992(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98704(%rbp,%rax)
	movdqa	%xmm3, -98688(%rbp,%rax)
	movdqa	-295280(%rbp,%rax), %xmm0
	movdqa	-295264(%rbp,%rax), %xmm1
	movdqa	-295248(%rbp,%rax), %xmm2
	movdqa	-295232(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	movdqa	-196976(%rbp,%rax), %xmm4
	movdqa	-196960(%rbp,%rax), %xmm5
	movdqa	-196944(%rbp,%rax), %xmm6
	movdqa	-196928(%rbp,%rax), %xmm7
	psrad	$1, %xmm4
	paddd	%xmm0, %xmm4
	psrad	$1, %xmm5
	paddd	%xmm1, %xmm5
	movdqa	%xmm4, -98672(%rbp,%rax)
	movdqa	%xmm5, -98656(%rbp,%rax)
	psrad	$1, %xmm2
	psrad	$1, %xmm3
	psrad	$1, %xmm6
	paddd	%xmm2, %xmm6
	psrad	$1, %xmm7
	paddd	%xmm3, %xmm7
	movdqa	%xmm6, -98640(%rbp,%rax)
	movdqa	%xmm7, -98624(%rbp,%rax)
	movdqa	-295216(%rbp,%rax), %xmm0
	movdqa	-295200(%rbp,%rax), %xmm1
	movdqa	-196912(%rbp,%rax), %xmm2
	movdqa	-196896(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98608(%rbp,%rax)
	movdqa	%xmm3, -98592(%rbp,%rax)
	movdqa	-295184(%rbp,%rax), %xmm0
	movdqa	-295168(%rbp,%rax), %xmm1
	movdqa	-196880(%rbp,%rax), %xmm2
	movdqa	-196864(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98576(%rbp,%rax)
	movdqa	%xmm3, -98560(%rbp,%rax)
	movdqa	-295152(%rbp,%rax), %xmm0
	movdqa	-295136(%rbp,%rax), %xmm1
	movdqa	-196848(%rbp,%rax), %xmm2
	movdqa	-196832(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98544(%rbp,%rax)
	movdqa	%xmm3, -98528(%rbp,%rax)
	movdqa	-295120(%rbp,%rax), %xmm0
	movdqa	-295104(%rbp,%rax), %xmm1
	movdqa	-196816(%rbp,%rax), %xmm2
	movdqa	-196800(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98512(%rbp,%rax)
	movdqa	%xmm3, -98496(%rbp,%rax)
	movdqa	-295088(%rbp,%rax), %xmm0
	movdqa	-295072(%rbp,%rax), %xmm1
	movdqa	-196784(%rbp,%rax), %xmm2
	movdqa	-196768(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98480(%rbp,%rax)
	movdqa	%xmm3, -98464(%rbp,%rax)
	movdqa	-295056(%rbp,%rax), %xmm0
	movdqa	-295040(%rbp,%rax), %xmm1
	movdqa	-196752(%rbp,%rax), %xmm2
	movdqa	-196736(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98448(%rbp,%rax)
	movdqa	%xmm3, -98432(%rbp,%rax)
	movdqa	-295024(%rbp,%rax), %xmm0
	movdqa	-295008(%rbp,%rax), %xmm1
	movdqa	-196720(%rbp,%rax), %xmm2
	movdqa	-196704(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98416(%rbp,%rax)
	movdqa	%xmm3, -98400(%rbp,%rax)
	movdqa	-294992(%rbp,%rax), %xmm0
	movdqa	-294976(%rbp,%rax), %xmm1
	movdqa	-196688(%rbp,%rax), %xmm2
	movdqa	-196672(%rbp,%rax), %xmm3
	psrad	$1, %xmm0
	psrad	$1, %xmm1
	psrad	$1, %xmm2
	paddd	%xmm0, %xmm2
	psrad	$1, %xmm3
	paddd	%xmm1, %xmm3
	movdqa	%xmm2, -98384(%rbp,%rax)
	movdqa	%xmm3, -98368(%rbp,%rax)
	addq	$512, %rax              # imm = 0x200
	cmpq	$98800, %rax            # imm = 0x181F0
	jne	.LBB5_23
# %bb.24:                               # %for.cond260.preheader.preheader
	leaq	-98368(%rbp), %r12
	xorl	%eax, %eax
	movl	$3435973837, %r15d      # imm = 0xCCCCCCCD
	xorl	%ebx, %ebx
	xorl	%ecx, %ecx
	.p2align	4, 0x90
.LBB5_25:                               # %for.cond260.preheader
                                        # =>This Loop Header: Depth=1
                                        #     Child Loop BB5_26 Depth 2
	movq	%rcx, -48(%rbp)         # 8-byte Spill
	movq	%rax, -56(%rbp)         # 8-byte Spill
	movl	%eax, %r14d
	xorl	%r13d, %r13d
	.p2align	4, 0x90
.LBB5_26:                               # %for.body263
                                        #   Parent Loop BB5_25 Depth=1
                                        # =>  This Inner Loop Header: Depth=2
	movl	%r14d, %eax
	imulq	%r15, %rax
	shrq	$36, %rax
	leal	(%rax,%rax,4), %eax
	leal	(%rbx,%rax,4), %eax
	cmpl	%r13d, %eax
	jne	.LBB5_28
# %bb.27:                               # %if.then
                                        #   in Loop: Header=BB5_26 Depth=2
	movq	stdout(%rip), %rsi
	movl	$10, %edi
	callq	fputc
.LBB5_28:                               # %if.end
                                        #   in Loop: Header=BB5_26 Depth=2
	movq	stdout(%rip), %rdi
	xorps	%xmm0, %xmm0
	cvtsi2sdl	(%r12,%r13,4), %xmm0
	mulsd	.LCPI5_0(%rip), %xmm0
	movl	$.L.str.7, %esi
	movb	$1, %al
	callq	fprintf
	addq	$1, %r13
	addl	$1, %r14d
	cmpq	$128, %r13
	jne	.LBB5_26
# %bb.29:                               # %for.inc278
                                        #   in Loop: Header=BB5_25 Depth=1
	movq	-48(%rbp), %rcx         # 8-byte Reload
	addq	$1, %rcx
	addq	$512, %r12              # imm = 0x200
	addl	$-128, %ebx
	movq	-56(%rbp), %rax         # 8-byte Reload
	subl	$-128, %eax
	cmpq	$192, %rcx
	jne	.LBB5_25
# %bb.30:                               # %for.end280
	callq	TIMING_CPUCLOCK_TOGGLE
	callq	TIMING_CPUCLOCK_PRINT
	xorl	%eax, %eax
	addq	$393240, %rsp           # imm = 0x60018
	popq	%rbx
	popq	%r12
	popq	%r13
	popq	%r14
	popq	%r15
	popq	%rbp
	.cfi_def_cfa %rsp, 8
	retq
.Lfunc_end5:
	.size	main, .Lfunc_end5-main
	.cfi_endproc
                                        # -- End function
	.type	time_that_takes,@object # @time_that_takes
	.comm	time_that_takes,8,8
	.type	.L.str,@object          # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"%ld"
	.size	.L.str, 4

	.type	.L.str.7,@object        # @.str.7
.L.str.7:
	.asciz	"%.16lf "
	.size	.L.str.7, 8


	.ident	"clang version 8.0.1 (tags/RELEASE_801/final)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
