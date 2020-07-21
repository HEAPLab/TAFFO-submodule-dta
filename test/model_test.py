


#Stuff for   %A = alloca [200 x [200 x double]], align 16, !taffo.info !11, !taffo.initweight !14
main_A_fixbits = solver.IntVar(0, 31, 'main_A_fixbits')
main_A_fixp = solver.IntVar(0, 1, 'main_A_fixp')
main_A_float = solver.IntVar(0, 1, 'main_A_float')
main_A_double = solver.IntVar(0, 1, 'main_A_double')
main_A_enob = solver.IntVar(-10000, 10000, 'main_A_enob')
solver.Add( + (1)*main_A_enob + (-1)*main_A_fixbits + (10000)*main_A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_A_enob + (10000)*main_A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_A_enob + (10000)*main_A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_A_fixbits + (-10000)*main_A_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_A_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_A_double<=0)    #Disable double data type
enobCostObj =  + (-1)*main_A_enob
solver.Add( + (1)*main_A_fixp + (1)*main_A_float + (1)*main_A_double==1)    #Exactly one selected type
solver.Add( + (1)*main_A_fixbits + (-10000)*main_A_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %B = alloca [200 x [240 x double]], align 16, !taffo.info !15, !taffo.initweight !14
main_B_fixbits = solver.IntVar(0, 22, 'main_B_fixbits')
main_B_fixp = solver.IntVar(0, 1, 'main_B_fixp')
main_B_float = solver.IntVar(0, 1, 'main_B_float')
main_B_double = solver.IntVar(0, 1, 'main_B_double')
main_B_enob = solver.IntVar(-10000, 10000, 'main_B_enob')
solver.Add( + (1)*main_B_enob + (-1)*main_B_fixbits + (10000)*main_B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_B_enob + (10000)*main_B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_B_enob + (10000)*main_B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_B_fixbits + (-10000)*main_B_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_B_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_B_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_B_enob
solver.Add( + (1)*main_B_fixp + (1)*main_B_float + (1)*main_B_double==1)    #Exactly one selected type
solver.Add( + (1)*main_B_fixbits + (-10000)*main_B_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__fixbits = solver.IntVar(0, 31, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__0_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__0_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx15, align 8, !taffo.info !33, !taffo.initweight !22, !taffo.constinfo !36
ConstantValue__0_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_CAST_store_fixbits')
ConstantValue__0_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_fixp')
ConstantValue__0_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_float')
ConstantValue__0_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_double')
solver.Add( + (1)*ConstantValue__0_CAST_store_fixp + (1)*ConstantValue__0_CAST_store_float + (1)*ConstantValue__0_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__0_CAST_store_fixbits + (-10000)*ConstantValue__0_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__0_CAST_store')
C2_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__0_CAST_store')
solver.Add( + (1)*ConstantValue__0_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits + (-10000)*C1_ConstantValue__0_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__0_fixbits + (1)*ConstantValue__0_CAST_store_fixbits + (-10000)*C2_ConstantValue__0_CAST_store<=0)    #Shift cost 2
castCostObj =  + (1)*C1_ConstantValue__0_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__0_CAST_store
C3_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__0_CAST_store')
C4_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__0_CAST_store')
C5_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__0_CAST_store')
C6_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__0_CAST_store')
C7_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__0_CAST_store')
C8_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__0_CAST_store')
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_CAST_store_float + (-1)*C3_ConstantValue__0_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C4_ConstantValue__0_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_CAST_store_double + (-1)*C5_ConstantValue__0_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C6_ConstantValue__0_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_double + (-1)*C7_ConstantValue__0_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_float + (-1)*C8_ConstantValue__0_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__0_CAST_store
solver.Add( + (1)*main_A_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_A_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_A_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_A_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp')
solver.Add( + (1)*main_A_enob_memphi_main_tmp + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_2 = solver.IntVar(0, 1, 'main_main_tmp_enob_2')
solver.Add( + (1)*main_main_tmp_enob_2==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_B_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'main_B_enob_memphi_main_tmp1')
solver.Add( + (1)*main_B_enob_memphi_main_tmp1 + (-1)*main_B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
main_main_tmp1_enob_3 = solver.IntVar(0, 1, 'main_main_tmp1_enob_3')
main_main_tmp1_enob_4 = solver.IntVar(0, 1, 'main_main_tmp1_enob_4')
solver.Add( + (1)*main_main_tmp1_enob_2 + (1)*main_main_tmp1_enob_3 + (1)*main_main_tmp1_enob_4==1)    #Enob: one selected constraint



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !45, !taffo.initweight !28
main_A_CAST_mul_fixbits = solver.IntVar(0, 31, 'main_A_CAST_mul_fixbits')
main_A_CAST_mul_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul_fixp')
main_A_CAST_mul_float = solver.IntVar(0, 1, 'main_A_CAST_mul_float')
main_A_CAST_mul_double = solver.IntVar(0, 1, 'main_A_CAST_mul_double')
solver.Add( + (1)*main_A_CAST_mul_fixp + (1)*main_A_CAST_mul_float + (1)*main_A_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul_fixbits + (-10000)*main_A_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul = solver.IntVar(0, 1, 'C1_main_A_CAST_mul')
C2_main_A_CAST_mul = solver.IntVar(0, 1, 'C2_main_A_CAST_mul')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul_fixbits + (-10000)*C1_main_A_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul_fixbits + (-10000)*C2_main_A_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul
castCostObj +=  + (1)*C2_main_A_CAST_mul
C3_main_A_CAST_mul = solver.IntVar(0, 1, 'C3_main_A_CAST_mul')
C4_main_A_CAST_mul = solver.IntVar(0, 1, 'C4_main_A_CAST_mul')
C5_main_A_CAST_mul = solver.IntVar(0, 1, 'C5_main_A_CAST_mul')
C6_main_A_CAST_mul = solver.IntVar(0, 1, 'C6_main_A_CAST_mul')
C7_main_A_CAST_mul = solver.IntVar(0, 1, 'C7_main_A_CAST_mul')
C8_main_A_CAST_mul = solver.IntVar(0, 1, 'C8_main_A_CAST_mul')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul_float + (-1)*C3_main_A_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul_fixp + (-1)*C4_main_A_CAST_mul<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul_double + (-1)*C5_main_A_CAST_mul<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul_fixp + (-1)*C6_main_A_CAST_mul<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul_double + (-1)*C7_main_A_CAST_mul<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul_float + (-1)*C8_main_A_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !45, !taffo.initweight !28
main_B_CAST_mul_fixbits = solver.IntVar(0, 22, 'main_B_CAST_mul_fixbits')
main_B_CAST_mul_fixp = solver.IntVar(0, 1, 'main_B_CAST_mul_fixp')
main_B_CAST_mul_float = solver.IntVar(0, 1, 'main_B_CAST_mul_float')
main_B_CAST_mul_double = solver.IntVar(0, 1, 'main_B_CAST_mul_double')
solver.Add( + (1)*main_B_CAST_mul_fixp + (1)*main_B_CAST_mul_float + (1)*main_B_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_B_CAST_mul_fixbits + (-10000)*main_B_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_B_CAST_mul = solver.IntVar(0, 1, 'C1_main_B_CAST_mul')
C2_main_B_CAST_mul = solver.IntVar(0, 1, 'C2_main_B_CAST_mul')
solver.Add( + (1)*main_B_fixbits + (-1)*main_B_CAST_mul_fixbits + (-10000)*C1_main_B_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_B_fixbits + (1)*main_B_CAST_mul_fixbits + (-10000)*C2_main_B_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_B_CAST_mul
castCostObj +=  + (1)*C2_main_B_CAST_mul
C3_main_B_CAST_mul = solver.IntVar(0, 1, 'C3_main_B_CAST_mul')
C4_main_B_CAST_mul = solver.IntVar(0, 1, 'C4_main_B_CAST_mul')
C5_main_B_CAST_mul = solver.IntVar(0, 1, 'C5_main_B_CAST_mul')
C6_main_B_CAST_mul = solver.IntVar(0, 1, 'C6_main_B_CAST_mul')
C7_main_B_CAST_mul = solver.IntVar(0, 1, 'C7_main_B_CAST_mul')
C8_main_B_CAST_mul = solver.IntVar(0, 1, 'C8_main_B_CAST_mul')
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_mul_float + (-1)*C3_main_B_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_B_CAST_mul
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_mul_fixp + (-1)*C4_main_B_CAST_mul<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_B_CAST_mul
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_mul_double + (-1)*C5_main_B_CAST_mul<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_B_CAST_mul
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_mul_fixp + (-1)*C6_main_B_CAST_mul<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_B_CAST_mul
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_mul_double + (-1)*C7_main_B_CAST_mul<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_B_CAST_mul
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_mul_float + (-1)*C8_main_B_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_B_CAST_mul



#Stuff for   %mul = fmul double %tmp, %tmp1, !taffo.info !45, !taffo.initweight !28
main_mul_fixbits = solver.IntVar(0, 22, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_mul_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul_enob
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul_fixp + (-1)*main_B_CAST_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul_float + (-1)*main_B_CAST_mul_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul_double + (-1)*main_B_CAST_mul_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul_double + (-1)*main_mul_double==0)    #double equality
mathCostObj =  + (1.65217)*main_mul_fixp
mathCostObj +=  + (6)*main_mul_float
mathCostObj +=  + (12.2551)*main_mul_double
main_main_mul_enob_1 = solver.IntVar(0, 1, 'main_main_mul_enob_1')
main_main_mul_enob_2 = solver.IntVar(0, 1, 'main_main_mul_enob_2')
solver.Add( + (1)*main_main_mul_enob_1 + (1)*main_main_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul_enob + (-1)*main_B_enob_memphi_main_tmp1 + (-10000)*main_main_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul_enob + (-1)*main_A_enob_memphi_main_tmp + (-10000)*main_main_mul_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_B_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_B_enob_memphi_main_tmp2')
solver.Add( + (1)*main_B_enob_memphi_main_tmp2 + (-1)*main_B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
main_main_tmp2_enob_3 = solver.IntVar(0, 1, 'main_main_tmp2_enob_3')
main_main_tmp2_enob_4 = solver.IntVar(0, 1, 'main_main_tmp2_enob_4')
solver.Add( + (1)*main_main_tmp2_enob_2 + (1)*main_main_tmp2_enob_3 + (1)*main_main_tmp2_enob_4==1)    #Enob: one selected constraint



#Constraint for cast for   %add60 = fadd double %tmp2, %mul, !taffo.info !46, !taffo.initweight !28
main_B_CAST_add60_fixbits = solver.IntVar(0, 22, 'main_B_CAST_add60_fixbits')
main_B_CAST_add60_fixp = solver.IntVar(0, 1, 'main_B_CAST_add60_fixp')
main_B_CAST_add60_float = solver.IntVar(0, 1, 'main_B_CAST_add60_float')
main_B_CAST_add60_double = solver.IntVar(0, 1, 'main_B_CAST_add60_double')
solver.Add( + (1)*main_B_CAST_add60_fixp + (1)*main_B_CAST_add60_float + (1)*main_B_CAST_add60_double==1)    #exactly 1 type
solver.Add( + (1)*main_B_CAST_add60_fixbits + (-10000)*main_B_CAST_add60_fixp<=0)    #If no fix, fix frac part = 0
C1_main_B_CAST_add60 = solver.IntVar(0, 1, 'C1_main_B_CAST_add60')
C2_main_B_CAST_add60 = solver.IntVar(0, 1, 'C2_main_B_CAST_add60')
solver.Add( + (1)*main_B_fixbits + (-1)*main_B_CAST_add60_fixbits + (-10000)*C1_main_B_CAST_add60<=0)    #Shift cost 1
solver.Add( + (-1)*main_B_fixbits + (1)*main_B_CAST_add60_fixbits + (-10000)*C2_main_B_CAST_add60<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_B_CAST_add60
castCostObj +=  + (1)*C2_main_B_CAST_add60
C3_main_B_CAST_add60 = solver.IntVar(0, 1, 'C3_main_B_CAST_add60')
C4_main_B_CAST_add60 = solver.IntVar(0, 1, 'C4_main_B_CAST_add60')
C5_main_B_CAST_add60 = solver.IntVar(0, 1, 'C5_main_B_CAST_add60')
C6_main_B_CAST_add60 = solver.IntVar(0, 1, 'C6_main_B_CAST_add60')
C7_main_B_CAST_add60 = solver.IntVar(0, 1, 'C7_main_B_CAST_add60')
C8_main_B_CAST_add60 = solver.IntVar(0, 1, 'C8_main_B_CAST_add60')
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_add60_float + (-1)*C3_main_B_CAST_add60<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_B_CAST_add60
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_add60_fixp + (-1)*C4_main_B_CAST_add60<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_B_CAST_add60
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_add60_double + (-1)*C5_main_B_CAST_add60<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_B_CAST_add60
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_add60_fixp + (-1)*C6_main_B_CAST_add60<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_B_CAST_add60
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_add60_double + (-1)*C7_main_B_CAST_add60<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_B_CAST_add60
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_add60_float + (-1)*C8_main_B_CAST_add60<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_B_CAST_add60



#Constraint for cast for   %add60 = fadd double %tmp2, %mul, !taffo.info !46, !taffo.initweight !28
main_mul_CAST_add60_fixbits = solver.IntVar(0, 22, 'main_mul_CAST_add60_fixbits')
main_mul_CAST_add60_fixp = solver.IntVar(0, 1, 'main_mul_CAST_add60_fixp')
main_mul_CAST_add60_float = solver.IntVar(0, 1, 'main_mul_CAST_add60_float')
main_mul_CAST_add60_double = solver.IntVar(0, 1, 'main_mul_CAST_add60_double')
solver.Add( + (1)*main_mul_CAST_add60_fixp + (1)*main_mul_CAST_add60_float + (1)*main_mul_CAST_add60_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul_CAST_add60_fixbits + (-10000)*main_mul_CAST_add60_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C1_main_mul_CAST_add60')
C2_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C2_main_mul_CAST_add60')
solver.Add( + (1)*main_mul_fixbits + (-1)*main_mul_CAST_add60_fixbits + (-10000)*C1_main_mul_CAST_add60<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul_fixbits + (1)*main_mul_CAST_add60_fixbits + (-10000)*C2_main_mul_CAST_add60<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul_CAST_add60
castCostObj +=  + (1)*C2_main_mul_CAST_add60
C3_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C3_main_mul_CAST_add60')
C4_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C4_main_mul_CAST_add60')
C5_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C5_main_mul_CAST_add60')
C6_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C6_main_mul_CAST_add60')
C7_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C7_main_mul_CAST_add60')
C8_main_mul_CAST_add60 = solver.IntVar(0, 1, 'C8_main_mul_CAST_add60')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_add60_float + (-1)*C3_main_mul_CAST_add60<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul_CAST_add60
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_add60_fixp + (-1)*C4_main_mul_CAST_add60<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul_CAST_add60
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_add60_double + (-1)*C5_main_mul_CAST_add60<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul_CAST_add60
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_add60_fixp + (-1)*C6_main_mul_CAST_add60<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul_CAST_add60
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_add60_double + (-1)*C7_main_mul_CAST_add60<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul_CAST_add60
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_add60_float + (-1)*C8_main_mul_CAST_add60<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul_CAST_add60



#Stuff for   %add60 = fadd double %tmp2, %mul, !taffo.info !46, !taffo.initweight !28
main_add60_fixbits = solver.IntVar(0, 21, 'main_add60_fixbits')
main_add60_fixp = solver.IntVar(0, 1, 'main_add60_fixp')
main_add60_float = solver.IntVar(0, 1, 'main_add60_float')
main_add60_double = solver.IntVar(0, 1, 'main_add60_double')
main_add60_enob = solver.IntVar(-10000, 10000, 'main_add60_enob')
solver.Add( + (1)*main_add60_enob + (-1)*main_add60_fixbits + (10000)*main_add60_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add60_enob + (10000)*main_add60_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add60_enob + (10000)*main_add60_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add60_fixbits + (-10000)*main_add60_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_add60_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add60_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add60_enob
solver.Add( + (1)*main_add60_fixp + (1)*main_add60_float + (1)*main_add60_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add60_fixbits + (-10000)*main_add60_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_B_CAST_add60_fixp + (-1)*main_mul_CAST_add60_fixp==0)    #fix equality
solver.Add( + (1)*main_B_CAST_add60_float + (-1)*main_mul_CAST_add60_float==0)    #float equality
solver.Add( + (1)*main_B_CAST_add60_double + (-1)*main_mul_CAST_add60_double==0)    #double equality
solver.Add( + (1)*main_B_CAST_add60_fixbits + (-1)*main_mul_CAST_add60_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_B_CAST_add60_fixp + (-1)*main_add60_fixp==0)    #fix equality
solver.Add( + (1)*main_B_CAST_add60_float + (-1)*main_add60_float==0)    #float equality
solver.Add( + (1)*main_B_CAST_add60_double + (-1)*main_add60_double==0)    #double equality
solver.Add( + (1)*main_B_CAST_add60_fixbits + (-1)*main_add60_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add60_fixp
mathCostObj +=  + (3)*main_add60_float
mathCostObj +=  + (6.64928)*main_add60_double
solver.Add( + (1)*main_add60_enob + (-1)*main_B_enob_memphi_main_tmp2<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add60_enob + (-1)*main_mul_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add60, double* %arrayidx59, align 8, !taffo.info !15, !taffo.initweight !22
main_add60_CAST_store_fixbits = solver.IntVar(0, 21, 'main_add60_CAST_store_fixbits')
main_add60_CAST_store_fixp = solver.IntVar(0, 1, 'main_add60_CAST_store_fixp')
main_add60_CAST_store_float = solver.IntVar(0, 1, 'main_add60_CAST_store_float')
main_add60_CAST_store_double = solver.IntVar(0, 1, 'main_add60_CAST_store_double')
solver.Add( + (1)*main_add60_CAST_store_fixp + (1)*main_add60_CAST_store_float + (1)*main_add60_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add60_CAST_store_fixbits + (-10000)*main_add60_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add60_CAST_store = solver.IntVar(0, 1, 'C1_main_add60_CAST_store')
C2_main_add60_CAST_store = solver.IntVar(0, 1, 'C2_main_add60_CAST_store')
solver.Add( + (1)*main_add60_fixbits + (-1)*main_add60_CAST_store_fixbits + (-10000)*C1_main_add60_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add60_fixbits + (1)*main_add60_CAST_store_fixbits + (-10000)*C2_main_add60_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add60_CAST_store
castCostObj +=  + (1)*C2_main_add60_CAST_store
C3_main_add60_CAST_store = solver.IntVar(0, 1, 'C3_main_add60_CAST_store')
C4_main_add60_CAST_store = solver.IntVar(0, 1, 'C4_main_add60_CAST_store')
C5_main_add60_CAST_store = solver.IntVar(0, 1, 'C5_main_add60_CAST_store')
C6_main_add60_CAST_store = solver.IntVar(0, 1, 'C6_main_add60_CAST_store')
C7_main_add60_CAST_store = solver.IntVar(0, 1, 'C7_main_add60_CAST_store')
C8_main_add60_CAST_store = solver.IntVar(0, 1, 'C8_main_add60_CAST_store')
solver.Add( + (1)*main_add60_fixp + (1)*main_add60_CAST_store_float + (-1)*C3_main_add60_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add60_CAST_store
solver.Add( + (1)*main_add60_float + (1)*main_add60_CAST_store_fixp + (-1)*C4_main_add60_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add60_CAST_store
solver.Add( + (1)*main_add60_fixp + (1)*main_add60_CAST_store_double + (-1)*C5_main_add60_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add60_CAST_store
solver.Add( + (1)*main_add60_double + (1)*main_add60_CAST_store_fixp + (-1)*C6_main_add60_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add60_CAST_store
solver.Add( + (1)*main_add60_float + (1)*main_add60_CAST_store_double + (-1)*C7_main_add60_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add60_CAST_store
solver.Add( + (1)*main_add60_double + (1)*main_add60_CAST_store_float + (-1)*C8_main_add60_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add60_CAST_store
solver.Add( + (1)*main_B_fixp + (-1)*main_add60_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_B_float + (-1)*main_add60_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_B_double + (-1)*main_add60_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_B_fixbits + (-1)*main_add60_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_B_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_B_enob_storeENOB')
solver.Add( + (1)*main_B_enob_storeENOB + (-1)*main_B_fixbits + (10000)*main_B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_B_enob_storeENOB + (10000)*main_B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_B_enob_storeENOB + (10000)*main_B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_B_enob_storeENOB + (-1)*main_add60_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp1 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp1_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp2 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp2_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_B_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'main_B_enob_memphi_main_tmp3')
solver.Add( + (1)*main_B_enob_memphi_main_tmp3 + (-1)*main_B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
solver.Add( + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3 + (1)*main_main_tmp3_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp3 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.500000e+00
ConstantValue__1_fixbits = solver.IntVar(0, 30, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__1_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.500000e+00
ConstantValue__2_fixbits = solver.IntVar(0, 30, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__2_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.500000e+00
ConstantValue__3_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__3_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul68 = fmul double 1.500000e+00, %tmp3, !taffo.info !50, !taffo.initweight !21, !taffo.constinfo !52
ConstantValue__3_CAST_mul68_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_CAST_mul68_fixbits')
ConstantValue__3_CAST_mul68_fixp = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul68_fixp')
ConstantValue__3_CAST_mul68_float = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul68_float')
ConstantValue__3_CAST_mul68_double = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul68_double')
solver.Add( + (1)*ConstantValue__3_CAST_mul68_fixp + (1)*ConstantValue__3_CAST_mul68_float + (1)*ConstantValue__3_CAST_mul68_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__3_CAST_mul68_fixbits + (-10000)*ConstantValue__3_CAST_mul68_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C1_ConstantValue__3_CAST_mul68')
C2_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C2_ConstantValue__3_CAST_mul68')
solver.Add( + (1)*ConstantValue__3_fixbits + (-1)*ConstantValue__3_CAST_mul68_fixbits + (-10000)*C1_ConstantValue__3_CAST_mul68<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__3_fixbits + (1)*ConstantValue__3_CAST_mul68_fixbits + (-10000)*C2_ConstantValue__3_CAST_mul68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__3_CAST_mul68
castCostObj +=  + (1)*C2_ConstantValue__3_CAST_mul68
C3_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C3_ConstantValue__3_CAST_mul68')
C4_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C4_ConstantValue__3_CAST_mul68')
C5_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C5_ConstantValue__3_CAST_mul68')
C6_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C6_ConstantValue__3_CAST_mul68')
C7_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C7_ConstantValue__3_CAST_mul68')
C8_ConstantValue__3_CAST_mul68 = solver.IntVar(0, 1, 'C8_ConstantValue__3_CAST_mul68')
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul68_float + (-1)*C3_ConstantValue__3_CAST_mul68<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__3_CAST_mul68
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul68_fixp + (-1)*C4_ConstantValue__3_CAST_mul68<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__3_CAST_mul68
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul68_double + (-1)*C5_ConstantValue__3_CAST_mul68<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__3_CAST_mul68
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul68_fixp + (-1)*C6_ConstantValue__3_CAST_mul68<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__3_CAST_mul68
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul68_double + (-1)*C7_ConstantValue__3_CAST_mul68<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__3_CAST_mul68
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul68_float + (-1)*C8_ConstantValue__3_CAST_mul68<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__3_CAST_mul68



#Constraint for cast for   %mul68 = fmul double 1.500000e+00, %tmp3, !taffo.info !50, !taffo.initweight !21, !taffo.constinfo !52
main_B_CAST_mul68_fixbits = solver.IntVar(0, 22, 'main_B_CAST_mul68_fixbits')
main_B_CAST_mul68_fixp = solver.IntVar(0, 1, 'main_B_CAST_mul68_fixp')
main_B_CAST_mul68_float = solver.IntVar(0, 1, 'main_B_CAST_mul68_float')
main_B_CAST_mul68_double = solver.IntVar(0, 1, 'main_B_CAST_mul68_double')
solver.Add( + (1)*main_B_CAST_mul68_fixp + (1)*main_B_CAST_mul68_float + (1)*main_B_CAST_mul68_double==1)    #exactly 1 type
solver.Add( + (1)*main_B_CAST_mul68_fixbits + (-10000)*main_B_CAST_mul68_fixp<=0)    #If no fix, fix frac part = 0
C1_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C1_main_B_CAST_mul68')
C2_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C2_main_B_CAST_mul68')
solver.Add( + (1)*main_B_fixbits + (-1)*main_B_CAST_mul68_fixbits + (-10000)*C1_main_B_CAST_mul68<=0)    #Shift cost 1
solver.Add( + (-1)*main_B_fixbits + (1)*main_B_CAST_mul68_fixbits + (-10000)*C2_main_B_CAST_mul68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_B_CAST_mul68
castCostObj +=  + (1)*C2_main_B_CAST_mul68
C3_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C3_main_B_CAST_mul68')
C4_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C4_main_B_CAST_mul68')
C5_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C5_main_B_CAST_mul68')
C6_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C6_main_B_CAST_mul68')
C7_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C7_main_B_CAST_mul68')
C8_main_B_CAST_mul68 = solver.IntVar(0, 1, 'C8_main_B_CAST_mul68')
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_mul68_float + (-1)*C3_main_B_CAST_mul68<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_B_CAST_mul68
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_mul68_fixp + (-1)*C4_main_B_CAST_mul68<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_B_CAST_mul68
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_mul68_double + (-1)*C5_main_B_CAST_mul68<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_B_CAST_mul68
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_mul68_fixp + (-1)*C6_main_B_CAST_mul68<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_B_CAST_mul68
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_mul68_double + (-1)*C7_main_B_CAST_mul68<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_B_CAST_mul68
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_mul68_float + (-1)*C8_main_B_CAST_mul68<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_B_CAST_mul68



#Stuff for   %mul68 = fmul double 1.500000e+00, %tmp3, !taffo.info !50, !taffo.initweight !21, !taffo.constinfo !52
main_mul68_fixbits = solver.IntVar(0, 22, 'main_mul68_fixbits')
main_mul68_fixp = solver.IntVar(0, 1, 'main_mul68_fixp')
main_mul68_float = solver.IntVar(0, 1, 'main_mul68_float')
main_mul68_double = solver.IntVar(0, 1, 'main_mul68_double')
main_mul68_enob = solver.IntVar(-10000, 10000, 'main_mul68_enob')
solver.Add( + (1)*main_mul68_enob + (-1)*main_mul68_fixbits + (10000)*main_mul68_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul68_enob + (10000)*main_mul68_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul68_enob + (10000)*main_mul68_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul68_fixbits + (-10000)*main_mul68_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_mul68_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul68_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul68_enob
solver.Add( + (1)*main_mul68_fixp + (1)*main_mul68_float + (1)*main_mul68_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul68_fixbits + (-10000)*main_mul68_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__3_CAST_mul68_fixp + (-1)*main_B_CAST_mul68_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul68_float + (-1)*main_B_CAST_mul68_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul68_double + (-1)*main_B_CAST_mul68_double==0)    #double equality
solver.Add( + (1)*ConstantValue__3_CAST_mul68_fixp + (-1)*main_mul68_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul68_float + (-1)*main_mul68_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul68_double + (-1)*main_mul68_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul68_fixp
mathCostObj +=  + (6)*main_mul68_float
mathCostObj +=  + (12.2551)*main_mul68_double
main_main_mul68_enob_1 = solver.IntVar(0, 1, 'main_main_mul68_enob_1')
main_main_mul68_enob_2 = solver.IntVar(0, 1, 'main_main_mul68_enob_2')
solver.Add( + (1)*main_main_mul68_enob_1 + (1)*main_main_mul68_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul68_enob + (-1)*main_B_enob_memphi_main_tmp3 + (-10000)*main_main_mul68_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul68_enob + (-1)*ConstantValue__1_enob + (-10000)*main_main_mul68_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   store double %mul68, double* %arrayidx72, align 8, !taffo.info !33, !taffo.initweight !22
main_mul68_CAST_store_fixbits = solver.IntVar(0, 22, 'main_mul68_CAST_store_fixbits')
main_mul68_CAST_store_fixp = solver.IntVar(0, 1, 'main_mul68_CAST_store_fixp')
main_mul68_CAST_store_float = solver.IntVar(0, 1, 'main_mul68_CAST_store_float')
main_mul68_CAST_store_double = solver.IntVar(0, 1, 'main_mul68_CAST_store_double')
solver.Add( + (1)*main_mul68_CAST_store_fixp + (1)*main_mul68_CAST_store_float + (1)*main_mul68_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul68_CAST_store_fixbits + (-10000)*main_mul68_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul68_CAST_store = solver.IntVar(0, 1, 'C1_main_mul68_CAST_store')
C2_main_mul68_CAST_store = solver.IntVar(0, 1, 'C2_main_mul68_CAST_store')
solver.Add( + (1)*main_mul68_fixbits + (-1)*main_mul68_CAST_store_fixbits + (-10000)*C1_main_mul68_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul68_fixbits + (1)*main_mul68_CAST_store_fixbits + (-10000)*C2_main_mul68_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul68_CAST_store
castCostObj +=  + (1)*C2_main_mul68_CAST_store
C3_main_mul68_CAST_store = solver.IntVar(0, 1, 'C3_main_mul68_CAST_store')
C4_main_mul68_CAST_store = solver.IntVar(0, 1, 'C4_main_mul68_CAST_store')
C5_main_mul68_CAST_store = solver.IntVar(0, 1, 'C5_main_mul68_CAST_store')
C6_main_mul68_CAST_store = solver.IntVar(0, 1, 'C6_main_mul68_CAST_store')
C7_main_mul68_CAST_store = solver.IntVar(0, 1, 'C7_main_mul68_CAST_store')
C8_main_mul68_CAST_store = solver.IntVar(0, 1, 'C8_main_mul68_CAST_store')
solver.Add( + (1)*main_mul68_fixp + (1)*main_mul68_CAST_store_float + (-1)*C3_main_mul68_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul68_CAST_store
solver.Add( + (1)*main_mul68_float + (1)*main_mul68_CAST_store_fixp + (-1)*C4_main_mul68_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul68_CAST_store
solver.Add( + (1)*main_mul68_fixp + (1)*main_mul68_CAST_store_double + (-1)*C5_main_mul68_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul68_CAST_store
solver.Add( + (1)*main_mul68_double + (1)*main_mul68_CAST_store_fixp + (-1)*C6_main_mul68_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul68_CAST_store
solver.Add( + (1)*main_mul68_float + (1)*main_mul68_CAST_store_double + (-1)*C7_main_mul68_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul68_CAST_store
solver.Add( + (1)*main_mul68_double + (1)*main_mul68_CAST_store_float + (-1)*C8_main_mul68_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul68_CAST_store
solver.Add( + (1)*main_B_fixp + (-1)*main_mul68_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_B_float + (-1)*main_mul68_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_B_double + (-1)*main_mul68_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_B_fixbits + (-1)*main_mul68_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_B_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_B_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_B_enob_storeENOB_storeENOB + (-1)*main_B_fixbits + (10000)*main_B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_B_enob_storeENOB_storeENOB + (10000)*main_B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_B_enob_storeENOB_storeENOB + (10000)*main_B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_B_enob_storeENOB_storeENOB + (-1)*main_mul68_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp1 + (-1)*main_B_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp2 + (-1)*main_B_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp3 + (-1)*main_B_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_B_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'main_B_enob_memphi_main_tmp6')
solver.Add( + (1)*main_B_enob_memphi_main_tmp6 + (-1)*main_B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
main_main_tmp6_enob_3 = solver.IntVar(0, 1, 'main_main_tmp6_enob_3')
solver.Add( + (1)*main_main_tmp6_enob_2 + (1)*main_main_tmp6_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp6 + (-1)*main_B_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call96 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp5, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp6), !taffo.info !15, !taffo.initweight !28, !taffo.constinfo !58
main_B_CAST_call96_fixbits = solver.IntVar(0, 22, 'main_B_CAST_call96_fixbits')
main_B_CAST_call96_fixp = solver.IntVar(0, 1, 'main_B_CAST_call96_fixp')
main_B_CAST_call96_float = solver.IntVar(0, 1, 'main_B_CAST_call96_float')
main_B_CAST_call96_double = solver.IntVar(0, 1, 'main_B_CAST_call96_double')
solver.Add( + (1)*main_B_CAST_call96_fixp + (1)*main_B_CAST_call96_float + (1)*main_B_CAST_call96_double==1)    #exactly 1 type
solver.Add( + (1)*main_B_CAST_call96_fixbits + (-10000)*main_B_CAST_call96_fixp<=0)    #If no fix, fix frac part = 0
C1_main_B_CAST_call96 = solver.IntVar(0, 1, 'C1_main_B_CAST_call96')
C2_main_B_CAST_call96 = solver.IntVar(0, 1, 'C2_main_B_CAST_call96')
solver.Add( + (1)*main_B_fixbits + (-1)*main_B_CAST_call96_fixbits + (-10000)*C1_main_B_CAST_call96<=0)    #Shift cost 1
solver.Add( + (-1)*main_B_fixbits + (1)*main_B_CAST_call96_fixbits + (-10000)*C2_main_B_CAST_call96<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_B_CAST_call96
castCostObj +=  + (1)*C2_main_B_CAST_call96
C3_main_B_CAST_call96 = solver.IntVar(0, 1, 'C3_main_B_CAST_call96')
C4_main_B_CAST_call96 = solver.IntVar(0, 1, 'C4_main_B_CAST_call96')
C5_main_B_CAST_call96 = solver.IntVar(0, 1, 'C5_main_B_CAST_call96')
C6_main_B_CAST_call96 = solver.IntVar(0, 1, 'C6_main_B_CAST_call96')
C7_main_B_CAST_call96 = solver.IntVar(0, 1, 'C7_main_B_CAST_call96')
C8_main_B_CAST_call96 = solver.IntVar(0, 1, 'C8_main_B_CAST_call96')
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_call96_float + (-1)*C3_main_B_CAST_call96<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_B_CAST_call96
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_call96_fixp + (-1)*C4_main_B_CAST_call96<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_B_CAST_call96
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_call96_double + (-1)*C5_main_B_CAST_call96<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_B_CAST_call96
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_call96_fixp + (-1)*C6_main_B_CAST_call96<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_B_CAST_call96
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_call96_double + (-1)*C7_main_B_CAST_call96<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_B_CAST_call96
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_call96_float + (-1)*C8_main_B_CAST_call96<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_B_CAST_call96
solver.Add( + (1)*main_B_CAST_call96_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(10000 * castCostObj / 159.217+ 1 * enobCostObj / 1665+ 10000 * mathCostObj / 31.1594)

# Model declaration end.