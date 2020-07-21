


#Stuff for   %tmp = alloca [180 x [190 x double]], align 16, !taffo.info !11, !taffo.initweight !14
main_tmp_fixbits = solver.IntVar(0, 16, 'main_tmp_fixbits')
main_tmp_fixp = solver.IntVar(0, 1, 'main_tmp_fixp')
main_tmp_float = solver.IntVar(0, 1, 'main_tmp_float')
main_tmp_double = solver.IntVar(0, 1, 'main_tmp_double')
main_tmp_enob = solver.IntVar(-10000, 10000, 'main_tmp_enob')
solver.Add( + (1)*main_tmp_enob + (-1)*main_tmp_fixbits + (10000)*main_tmp_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_tmp_enob + (10000)*main_tmp_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_tmp_enob + (10000)*main_tmp_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_tmp_fixbits + (-10000)*main_tmp_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_tmp_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_tmp_double<=0)    #Disable double data type
enobCostObj =  + (-1)*main_tmp_enob
solver.Add( + (1)*main_tmp_fixp + (1)*main_tmp_float + (1)*main_tmp_double==1)    #Exactly one selected type
solver.Add( + (1)*main_tmp_fixbits + (-10000)*main_tmp_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %A = alloca [180 x [210 x double]], align 16, !taffo.info !15, !taffo.initweight !14
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
enobCostObj +=  + (-1)*main_A_enob
solver.Add( + (1)*main_A_fixp + (1)*main_A_float + (1)*main_A_double==1)    #Exactly one selected type
solver.Add( + (1)*main_A_fixbits + (-10000)*main_A_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %B = alloca [210 x [190 x double]], align 16, !taffo.info !15, !taffo.initweight !14
main_B_fixbits = solver.IntVar(0, 31, 'main_B_fixbits')
main_B_fixp = solver.IntVar(0, 1, 'main_B_fixp')
main_B_float = solver.IntVar(0, 1, 'main_B_float')
main_B_double = solver.IntVar(0, 1, 'main_B_double')
main_B_enob = solver.IntVar(-10000, 10000, 'main_B_enob')
solver.Add( + (1)*main_B_enob + (-1)*main_B_fixbits + (10000)*main_B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_B_enob + (10000)*main_B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_B_enob + (10000)*main_B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_B_fixbits + (-10000)*main_B_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_B_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_B_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_B_enob
solver.Add( + (1)*main_B_fixp + (1)*main_B_float + (1)*main_B_double==1)    #Exactly one selected type
solver.Add( + (1)*main_B_fixbits + (-10000)*main_B_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %C = alloca [190 x [220 x double]], align 16, !taffo.info !15, !taffo.initweight !14
main_C_fixbits = solver.IntVar(0, 31, 'main_C_fixbits')
main_C_fixp = solver.IntVar(0, 1, 'main_C_fixp')
main_C_float = solver.IntVar(0, 1, 'main_C_float')
main_C_double = solver.IntVar(0, 1, 'main_C_double')
main_C_enob = solver.IntVar(-10000, 10000, 'main_C_enob')
solver.Add( + (1)*main_C_enob + (-1)*main_C_fixbits + (10000)*main_C_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_C_enob + (10000)*main_C_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_C_enob + (10000)*main_C_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_C_fixbits + (-10000)*main_C_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_C_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_C_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_C_enob
solver.Add( + (1)*main_C_fixp + (1)*main_C_float + (1)*main_C_double==1)    #Exactly one selected type
solver.Add( + (1)*main_C_fixbits + (-10000)*main_C_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %D = alloca [180 x [220 x double]], align 16, !taffo.info !11, !taffo.initweight !14
main_D_fixbits = solver.IntVar(0, 16, 'main_D_fixbits')
main_D_fixp = solver.IntVar(0, 1, 'main_D_fixp')
main_D_float = solver.IntVar(0, 1, 'main_D_float')
main_D_double = solver.IntVar(0, 1, 'main_D_double')
main_D_enob = solver.IntVar(-10000, 10000, 'main_D_enob')
solver.Add( + (1)*main_D_enob + (-1)*main_D_fixbits + (10000)*main_D_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_D_enob + (10000)*main_D_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_D_enob + (10000)*main_D_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_D_fixbits + (-10000)*main_D_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_D_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_D_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_D_enob
solver.Add( + (1)*main_D_fixp + (1)*main_D_float + (1)*main_D_double==1)    #Exactly one selected type
solver.Add( + (1)*main_D_fixbits + (-10000)*main_D_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__fixbits = solver.IntVar(0, 32, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__0_fixbits = solver.IntVar(0, 32, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__0_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx103, align 8, !taffo.info !11, !taffo.initweight !22, !taffo.constinfo !54
ConstantValue__0_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__0_CAST_store_fixbits')
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
solver.Add( + (1)*main_tmp_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_tmp_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_tmp_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_tmp_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp1')
solver.Add( + (1)*main_A_enob_memphi_main_tmp1 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
solver.Add( + (1)*main_main_tmp1_enob_1==1)    #Enob: one selected constraint



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



#Constraint for cast for   %mul112 = fmul double 1.500000e+00, %tmp1, !taffo.info !58, !taffo.initweight !21, !taffo.constinfo !60
ConstantValue__3_CAST_mul112_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_CAST_mul112_fixbits')
ConstantValue__3_CAST_mul112_fixp = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul112_fixp')
ConstantValue__3_CAST_mul112_float = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul112_float')
ConstantValue__3_CAST_mul112_double = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul112_double')
solver.Add( + (1)*ConstantValue__3_CAST_mul112_fixp + (1)*ConstantValue__3_CAST_mul112_float + (1)*ConstantValue__3_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__3_CAST_mul112_fixbits + (-10000)*ConstantValue__3_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C1_ConstantValue__3_CAST_mul112')
C2_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C2_ConstantValue__3_CAST_mul112')
solver.Add( + (1)*ConstantValue__3_fixbits + (-1)*ConstantValue__3_CAST_mul112_fixbits + (-10000)*C1_ConstantValue__3_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__3_fixbits + (1)*ConstantValue__3_CAST_mul112_fixbits + (-10000)*C2_ConstantValue__3_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__3_CAST_mul112
castCostObj +=  + (1)*C2_ConstantValue__3_CAST_mul112
C3_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C3_ConstantValue__3_CAST_mul112')
C4_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C4_ConstantValue__3_CAST_mul112')
C5_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C5_ConstantValue__3_CAST_mul112')
C6_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C6_ConstantValue__3_CAST_mul112')
C7_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C7_ConstantValue__3_CAST_mul112')
C8_ConstantValue__3_CAST_mul112 = solver.IntVar(0, 1, 'C8_ConstantValue__3_CAST_mul112')
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul112_float + (-1)*C3_ConstantValue__3_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__3_CAST_mul112
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul112_fixp + (-1)*C4_ConstantValue__3_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__3_CAST_mul112
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul112_double + (-1)*C5_ConstantValue__3_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__3_CAST_mul112
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul112_fixp + (-1)*C6_ConstantValue__3_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__3_CAST_mul112
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul112_double + (-1)*C7_ConstantValue__3_CAST_mul112<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__3_CAST_mul112
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul112_float + (-1)*C8_ConstantValue__3_CAST_mul112<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__3_CAST_mul112



#Constraint for cast for   %mul112 = fmul double 1.500000e+00, %tmp1, !taffo.info !58, !taffo.initweight !21, !taffo.constinfo !60
main_A_CAST_mul112_fixbits = solver.IntVar(0, 31, 'main_A_CAST_mul112_fixbits')
main_A_CAST_mul112_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul112_fixp')
main_A_CAST_mul112_float = solver.IntVar(0, 1, 'main_A_CAST_mul112_float')
main_A_CAST_mul112_double = solver.IntVar(0, 1, 'main_A_CAST_mul112_double')
solver.Add( + (1)*main_A_CAST_mul112_fixp + (1)*main_A_CAST_mul112_float + (1)*main_A_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul112_fixbits + (-10000)*main_A_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul112')
C2_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul112')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul112_fixbits + (-10000)*C1_main_A_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul112_fixbits + (-10000)*C2_main_A_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul112
castCostObj +=  + (1)*C2_main_A_CAST_mul112
C3_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul112')
C4_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul112')
C5_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul112')
C6_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul112')
C7_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul112')
C8_main_A_CAST_mul112 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul112')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul112_float + (-1)*C3_main_A_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul112
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul112_fixp + (-1)*C4_main_A_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul112
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul112_double + (-1)*C5_main_A_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul112
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul112_fixp + (-1)*C6_main_A_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul112
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul112_double + (-1)*C7_main_A_CAST_mul112<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul112
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul112_float + (-1)*C8_main_A_CAST_mul112<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul112



#Stuff for   %mul112 = fmul double 1.500000e+00, %tmp1, !taffo.info !58, !taffo.initweight !21, !taffo.constinfo !60
main_mul112_fixbits = solver.IntVar(0, 30, 'main_mul112_fixbits')
main_mul112_fixp = solver.IntVar(0, 1, 'main_mul112_fixp')
main_mul112_float = solver.IntVar(0, 1, 'main_mul112_float')
main_mul112_double = solver.IntVar(0, 1, 'main_mul112_double')
main_mul112_enob = solver.IntVar(-10000, 10000, 'main_mul112_enob')
solver.Add( + (1)*main_mul112_enob + (-1)*main_mul112_fixbits + (10000)*main_mul112_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_mul112_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul112_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul112_enob
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_float + (1)*main_mul112_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__3_CAST_mul112_fixp + (-1)*main_A_CAST_mul112_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul112_float + (-1)*main_A_CAST_mul112_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul112_double + (-1)*main_A_CAST_mul112_double==0)    #double equality
solver.Add( + (1)*ConstantValue__3_CAST_mul112_fixp + (-1)*main_mul112_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul112_float + (-1)*main_mul112_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul112_double + (-1)*main_mul112_double==0)    #double equality
mathCostObj =  + (1.65217)*main_mul112_fixp
mathCostObj +=  + (6)*main_mul112_float
mathCostObj +=  + (12.2551)*main_mul112_double
main_main_mul112_enob_1 = solver.IntVar(0, 1, 'main_main_mul112_enob_1')
main_main_mul112_enob_2 = solver.IntVar(0, 1, 'main_main_mul112_enob_2')
solver.Add( + (1)*main_main_mul112_enob_1 + (1)*main_main_mul112_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul112_enob + (-1)*main_A_enob_memphi_main_tmp1 + (-10000)*main_main_mul112_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul112_enob + (-1)*ConstantValue__1_enob + (-10000)*main_main_mul112_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_B_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_B_enob_memphi_main_tmp2')
solver.Add( + (1)*main_B_enob_memphi_main_tmp2 + (-1)*main_B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
solver.Add( + (1)*main_main_tmp2_enob_1 + (1)*main_main_tmp2_enob_2==1)    #Enob: one selected constraint



#Constraint for cast for   %mul117 = fmul double %mul112, %tmp2, !taffo.info !58, !taffo.initweight !22
main_mul112_CAST_mul117_fixbits = solver.IntVar(0, 30, 'main_mul112_CAST_mul117_fixbits')
main_mul112_CAST_mul117_fixp = solver.IntVar(0, 1, 'main_mul112_CAST_mul117_fixp')
main_mul112_CAST_mul117_float = solver.IntVar(0, 1, 'main_mul112_CAST_mul117_float')
main_mul112_CAST_mul117_double = solver.IntVar(0, 1, 'main_mul112_CAST_mul117_double')
solver.Add( + (1)*main_mul112_CAST_mul117_fixp + (1)*main_mul112_CAST_mul117_float + (1)*main_mul112_CAST_mul117_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul112_CAST_mul117_fixbits + (-10000)*main_mul112_CAST_mul117_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C1_main_mul112_CAST_mul117')
C2_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C2_main_mul112_CAST_mul117')
solver.Add( + (1)*main_mul112_fixbits + (-1)*main_mul112_CAST_mul117_fixbits + (-10000)*C1_main_mul112_CAST_mul117<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul112_fixbits + (1)*main_mul112_CAST_mul117_fixbits + (-10000)*C2_main_mul112_CAST_mul117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul112_CAST_mul117
castCostObj +=  + (1)*C2_main_mul112_CAST_mul117
C3_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C3_main_mul112_CAST_mul117')
C4_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C4_main_mul112_CAST_mul117')
C5_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C5_main_mul112_CAST_mul117')
C6_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C6_main_mul112_CAST_mul117')
C7_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C7_main_mul112_CAST_mul117')
C8_main_mul112_CAST_mul117 = solver.IntVar(0, 1, 'C8_main_mul112_CAST_mul117')
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_CAST_mul117_float + (-1)*C3_main_mul112_CAST_mul117<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul112_CAST_mul117
solver.Add( + (1)*main_mul112_float + (1)*main_mul112_CAST_mul117_fixp + (-1)*C4_main_mul112_CAST_mul117<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul112_CAST_mul117
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_CAST_mul117_double + (-1)*C5_main_mul112_CAST_mul117<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul112_CAST_mul117
solver.Add( + (1)*main_mul112_double + (1)*main_mul112_CAST_mul117_fixp + (-1)*C6_main_mul112_CAST_mul117<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul112_CAST_mul117
solver.Add( + (1)*main_mul112_float + (1)*main_mul112_CAST_mul117_double + (-1)*C7_main_mul112_CAST_mul117<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul112_CAST_mul117
solver.Add( + (1)*main_mul112_double + (1)*main_mul112_CAST_mul117_float + (-1)*C8_main_mul112_CAST_mul117<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul112_CAST_mul117



#Constraint for cast for   %mul117 = fmul double %mul112, %tmp2, !taffo.info !58, !taffo.initweight !22
main_B_CAST_mul117_fixbits = solver.IntVar(0, 31, 'main_B_CAST_mul117_fixbits')
main_B_CAST_mul117_fixp = solver.IntVar(0, 1, 'main_B_CAST_mul117_fixp')
main_B_CAST_mul117_float = solver.IntVar(0, 1, 'main_B_CAST_mul117_float')
main_B_CAST_mul117_double = solver.IntVar(0, 1, 'main_B_CAST_mul117_double')
solver.Add( + (1)*main_B_CAST_mul117_fixp + (1)*main_B_CAST_mul117_float + (1)*main_B_CAST_mul117_double==1)    #exactly 1 type
solver.Add( + (1)*main_B_CAST_mul117_fixbits + (-10000)*main_B_CAST_mul117_fixp<=0)    #If no fix, fix frac part = 0
C1_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C1_main_B_CAST_mul117')
C2_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C2_main_B_CAST_mul117')
solver.Add( + (1)*main_B_fixbits + (-1)*main_B_CAST_mul117_fixbits + (-10000)*C1_main_B_CAST_mul117<=0)    #Shift cost 1
solver.Add( + (-1)*main_B_fixbits + (1)*main_B_CAST_mul117_fixbits + (-10000)*C2_main_B_CAST_mul117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_B_CAST_mul117
castCostObj +=  + (1)*C2_main_B_CAST_mul117
C3_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C3_main_B_CAST_mul117')
C4_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C4_main_B_CAST_mul117')
C5_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C5_main_B_CAST_mul117')
C6_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C6_main_B_CAST_mul117')
C7_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C7_main_B_CAST_mul117')
C8_main_B_CAST_mul117 = solver.IntVar(0, 1, 'C8_main_B_CAST_mul117')
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_mul117_float + (-1)*C3_main_B_CAST_mul117<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_B_CAST_mul117
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_mul117_fixp + (-1)*C4_main_B_CAST_mul117<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_B_CAST_mul117
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_mul117_double + (-1)*C5_main_B_CAST_mul117<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_B_CAST_mul117
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_mul117_fixp + (-1)*C6_main_B_CAST_mul117<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_B_CAST_mul117
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_mul117_double + (-1)*C7_main_B_CAST_mul117<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_B_CAST_mul117
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_mul117_float + (-1)*C8_main_B_CAST_mul117<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_B_CAST_mul117



#Stuff for   %mul117 = fmul double %mul112, %tmp2, !taffo.info !58, !taffo.initweight !22
main_mul117_fixbits = solver.IntVar(0, 30, 'main_mul117_fixbits')
main_mul117_fixp = solver.IntVar(0, 1, 'main_mul117_fixp')
main_mul117_float = solver.IntVar(0, 1, 'main_mul117_float')
main_mul117_double = solver.IntVar(0, 1, 'main_mul117_double')
main_mul117_enob = solver.IntVar(-10000, 10000, 'main_mul117_enob')
solver.Add( + (1)*main_mul117_enob + (-1)*main_mul117_fixbits + (10000)*main_mul117_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul117_enob + (10000)*main_mul117_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul117_enob + (10000)*main_mul117_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul117_fixbits + (-10000)*main_mul117_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_mul117_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul117_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul117_enob
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_float + (1)*main_mul117_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul117_fixbits + (-10000)*main_mul117_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul112_CAST_mul117_fixp + (-1)*main_B_CAST_mul117_fixp==0)    #fix equality
solver.Add( + (1)*main_mul112_CAST_mul117_float + (-1)*main_B_CAST_mul117_float==0)    #float equality
solver.Add( + (1)*main_mul112_CAST_mul117_double + (-1)*main_B_CAST_mul117_double==0)    #double equality
solver.Add( + (1)*main_mul112_CAST_mul117_fixp + (-1)*main_mul117_fixp==0)    #fix equality
solver.Add( + (1)*main_mul112_CAST_mul117_float + (-1)*main_mul117_float==0)    #float equality
solver.Add( + (1)*main_mul112_CAST_mul117_double + (-1)*main_mul117_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul117_fixp
mathCostObj +=  + (6)*main_mul117_float
mathCostObj +=  + (12.2551)*main_mul117_double
main_main_mul117_enob_1 = solver.IntVar(0, 1, 'main_main_mul117_enob_1')
main_main_mul117_enob_2 = solver.IntVar(0, 1, 'main_main_mul117_enob_2')
solver.Add( + (1)*main_main_mul117_enob_1 + (1)*main_main_mul117_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul117_enob + (-1)*main_B_enob_memphi_main_tmp2 + (-10000)*main_main_mul117_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul117_enob + (-1)*main_mul112_enob + (-10000)*main_main_mul117_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_tmp_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'main_tmp_enob_memphi_main_tmp4')
solver.Add( + (1)*main_tmp_enob_memphi_main_tmp4 + (-1)*main_tmp_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
solver.Add( + (1)*main_main_tmp4_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add122 = fadd double %tmp4, %mul117, !taffo.info !63, !taffo.initweight !33
main_tmp_CAST_add122_fixbits = solver.IntVar(0, 16, 'main_tmp_CAST_add122_fixbits')
main_tmp_CAST_add122_fixp = solver.IntVar(0, 1, 'main_tmp_CAST_add122_fixp')
main_tmp_CAST_add122_float = solver.IntVar(0, 1, 'main_tmp_CAST_add122_float')
main_tmp_CAST_add122_double = solver.IntVar(0, 1, 'main_tmp_CAST_add122_double')
solver.Add( + (1)*main_tmp_CAST_add122_fixp + (1)*main_tmp_CAST_add122_float + (1)*main_tmp_CAST_add122_double==1)    #exactly 1 type
solver.Add( + (1)*main_tmp_CAST_add122_fixbits + (-10000)*main_tmp_CAST_add122_fixp<=0)    #If no fix, fix frac part = 0
C1_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C1_main_tmp_CAST_add122')
C2_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C2_main_tmp_CAST_add122')
solver.Add( + (1)*main_tmp_fixbits + (-1)*main_tmp_CAST_add122_fixbits + (-10000)*C1_main_tmp_CAST_add122<=0)    #Shift cost 1
solver.Add( + (-1)*main_tmp_fixbits + (1)*main_tmp_CAST_add122_fixbits + (-10000)*C2_main_tmp_CAST_add122<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_tmp_CAST_add122
castCostObj +=  + (1)*C2_main_tmp_CAST_add122
C3_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C3_main_tmp_CAST_add122')
C4_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C4_main_tmp_CAST_add122')
C5_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C5_main_tmp_CAST_add122')
C6_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C6_main_tmp_CAST_add122')
C7_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C7_main_tmp_CAST_add122')
C8_main_tmp_CAST_add122 = solver.IntVar(0, 1, 'C8_main_tmp_CAST_add122')
solver.Add( + (1)*main_tmp_fixp + (1)*main_tmp_CAST_add122_float + (-1)*C3_main_tmp_CAST_add122<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_tmp_CAST_add122
solver.Add( + (1)*main_tmp_float + (1)*main_tmp_CAST_add122_fixp + (-1)*C4_main_tmp_CAST_add122<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_tmp_CAST_add122
solver.Add( + (1)*main_tmp_fixp + (1)*main_tmp_CAST_add122_double + (-1)*C5_main_tmp_CAST_add122<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_tmp_CAST_add122
solver.Add( + (1)*main_tmp_double + (1)*main_tmp_CAST_add122_fixp + (-1)*C6_main_tmp_CAST_add122<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_tmp_CAST_add122
solver.Add( + (1)*main_tmp_float + (1)*main_tmp_CAST_add122_double + (-1)*C7_main_tmp_CAST_add122<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_tmp_CAST_add122
solver.Add( + (1)*main_tmp_double + (1)*main_tmp_CAST_add122_float + (-1)*C8_main_tmp_CAST_add122<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_tmp_CAST_add122



#Constraint for cast for   %add122 = fadd double %tmp4, %mul117, !taffo.info !63, !taffo.initweight !33
main_mul117_CAST_add122_fixbits = solver.IntVar(0, 30, 'main_mul117_CAST_add122_fixbits')
main_mul117_CAST_add122_fixp = solver.IntVar(0, 1, 'main_mul117_CAST_add122_fixp')
main_mul117_CAST_add122_float = solver.IntVar(0, 1, 'main_mul117_CAST_add122_float')
main_mul117_CAST_add122_double = solver.IntVar(0, 1, 'main_mul117_CAST_add122_double')
solver.Add( + (1)*main_mul117_CAST_add122_fixp + (1)*main_mul117_CAST_add122_float + (1)*main_mul117_CAST_add122_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul117_CAST_add122_fixbits + (-10000)*main_mul117_CAST_add122_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C1_main_mul117_CAST_add122')
C2_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C2_main_mul117_CAST_add122')
solver.Add( + (1)*main_mul117_fixbits + (-1)*main_mul117_CAST_add122_fixbits + (-10000)*C1_main_mul117_CAST_add122<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul117_fixbits + (1)*main_mul117_CAST_add122_fixbits + (-10000)*C2_main_mul117_CAST_add122<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul117_CAST_add122
castCostObj +=  + (1)*C2_main_mul117_CAST_add122
C3_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C3_main_mul117_CAST_add122')
C4_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C4_main_mul117_CAST_add122')
C5_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C5_main_mul117_CAST_add122')
C6_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C6_main_mul117_CAST_add122')
C7_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C7_main_mul117_CAST_add122')
C8_main_mul117_CAST_add122 = solver.IntVar(0, 1, 'C8_main_mul117_CAST_add122')
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_CAST_add122_float + (-1)*C3_main_mul117_CAST_add122<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul117_CAST_add122
solver.Add( + (1)*main_mul117_float + (1)*main_mul117_CAST_add122_fixp + (-1)*C4_main_mul117_CAST_add122<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul117_CAST_add122
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_CAST_add122_double + (-1)*C5_main_mul117_CAST_add122<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul117_CAST_add122
solver.Add( + (1)*main_mul117_double + (1)*main_mul117_CAST_add122_fixp + (-1)*C6_main_mul117_CAST_add122<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul117_CAST_add122
solver.Add( + (1)*main_mul117_float + (1)*main_mul117_CAST_add122_double + (-1)*C7_main_mul117_CAST_add122<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul117_CAST_add122
solver.Add( + (1)*main_mul117_double + (1)*main_mul117_CAST_add122_float + (-1)*C8_main_mul117_CAST_add122<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul117_CAST_add122



#Stuff for   %add122 = fadd double %tmp4, %mul117, !taffo.info !63, !taffo.initweight !33
main_add122_fixbits = solver.IntVar(0, 16, 'main_add122_fixbits')
main_add122_fixp = solver.IntVar(0, 1, 'main_add122_fixp')
main_add122_float = solver.IntVar(0, 1, 'main_add122_float')
main_add122_double = solver.IntVar(0, 1, 'main_add122_double')
main_add122_enob = solver.IntVar(-10000, 10000, 'main_add122_enob')
solver.Add( + (1)*main_add122_enob + (-1)*main_add122_fixbits + (10000)*main_add122_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add122_enob + (10000)*main_add122_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add122_enob + (10000)*main_add122_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add122_fixbits + (-10000)*main_add122_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_add122_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add122_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add122_enob
solver.Add( + (1)*main_add122_fixp + (1)*main_add122_float + (1)*main_add122_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add122_fixbits + (-10000)*main_add122_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_tmp_CAST_add122_fixp + (-1)*main_mul117_CAST_add122_fixp==0)    #fix equality
solver.Add( + (1)*main_tmp_CAST_add122_float + (-1)*main_mul117_CAST_add122_float==0)    #float equality
solver.Add( + (1)*main_tmp_CAST_add122_double + (-1)*main_mul117_CAST_add122_double==0)    #double equality
solver.Add( + (1)*main_tmp_CAST_add122_fixbits + (-1)*main_mul117_CAST_add122_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_tmp_CAST_add122_fixp + (-1)*main_add122_fixp==0)    #fix equality
solver.Add( + (1)*main_tmp_CAST_add122_float + (-1)*main_add122_float==0)    #float equality
solver.Add( + (1)*main_tmp_CAST_add122_double + (-1)*main_add122_double==0)    #double equality
solver.Add( + (1)*main_tmp_CAST_add122_fixbits + (-1)*main_add122_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add122_fixp
mathCostObj +=  + (3)*main_add122_float
mathCostObj +=  + (6.64928)*main_add122_double
solver.Add( + (1)*main_add122_enob + (-1)*main_tmp_enob_memphi_main_tmp4<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add122_enob + (-1)*main_mul117_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add122, double* %arrayidx121, align 8, !taffo.info !11, !taffo.initweight !22
main_add122_CAST_store_fixbits = solver.IntVar(0, 16, 'main_add122_CAST_store_fixbits')
main_add122_CAST_store_fixp = solver.IntVar(0, 1, 'main_add122_CAST_store_fixp')
main_add122_CAST_store_float = solver.IntVar(0, 1, 'main_add122_CAST_store_float')
main_add122_CAST_store_double = solver.IntVar(0, 1, 'main_add122_CAST_store_double')
solver.Add( + (1)*main_add122_CAST_store_fixp + (1)*main_add122_CAST_store_float + (1)*main_add122_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add122_CAST_store_fixbits + (-10000)*main_add122_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add122_CAST_store = solver.IntVar(0, 1, 'C1_main_add122_CAST_store')
C2_main_add122_CAST_store = solver.IntVar(0, 1, 'C2_main_add122_CAST_store')
solver.Add( + (1)*main_add122_fixbits + (-1)*main_add122_CAST_store_fixbits + (-10000)*C1_main_add122_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add122_fixbits + (1)*main_add122_CAST_store_fixbits + (-10000)*C2_main_add122_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add122_CAST_store
castCostObj +=  + (1)*C2_main_add122_CAST_store
C3_main_add122_CAST_store = solver.IntVar(0, 1, 'C3_main_add122_CAST_store')
C4_main_add122_CAST_store = solver.IntVar(0, 1, 'C4_main_add122_CAST_store')
C5_main_add122_CAST_store = solver.IntVar(0, 1, 'C5_main_add122_CAST_store')
C6_main_add122_CAST_store = solver.IntVar(0, 1, 'C6_main_add122_CAST_store')
C7_main_add122_CAST_store = solver.IntVar(0, 1, 'C7_main_add122_CAST_store')
C8_main_add122_CAST_store = solver.IntVar(0, 1, 'C8_main_add122_CAST_store')
solver.Add( + (1)*main_add122_fixp + (1)*main_add122_CAST_store_float + (-1)*C3_main_add122_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add122_CAST_store
solver.Add( + (1)*main_add122_float + (1)*main_add122_CAST_store_fixp + (-1)*C4_main_add122_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add122_CAST_store
solver.Add( + (1)*main_add122_fixp + (1)*main_add122_CAST_store_double + (-1)*C5_main_add122_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add122_CAST_store
solver.Add( + (1)*main_add122_double + (1)*main_add122_CAST_store_fixp + (-1)*C6_main_add122_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add122_CAST_store
solver.Add( + (1)*main_add122_float + (1)*main_add122_CAST_store_double + (-1)*C7_main_add122_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add122_CAST_store
solver.Add( + (1)*main_add122_double + (1)*main_add122_CAST_store_float + (-1)*C8_main_add122_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add122_CAST_store
solver.Add( + (1)*main_tmp_fixp + (-1)*main_add122_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_tmp_float + (-1)*main_add122_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_tmp_double + (-1)*main_add122_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_tmp_fixbits + (-1)*main_add122_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_tmp_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_tmp_enob_storeENOB')
solver.Add( + (1)*main_tmp_enob_storeENOB + (-1)*main_tmp_fixbits + (10000)*main_tmp_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_tmp_enob_storeENOB + (10000)*main_tmp_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_tmp_enob_storeENOB + (10000)*main_tmp_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_tmp_enob_storeENOB + (-1)*main_add122_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_tmp_enob_memphi_main_tmp4 + (-1)*main_tmp_enob_storeENOB + (10000)*main_main_tmp4_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_D_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'main_D_enob_memphi_main_tmp5')
solver.Add( + (1)*main_D_enob_memphi_main_tmp5 + (-1)*main_D_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
main_main_tmp5_enob_4 = solver.IntVar(0, 1, 'main_main_tmp5_enob_4')
main_main_tmp5_enob_6 = solver.IntVar(0, 1, 'main_main_tmp5_enob_6')
main_main_tmp5_enob_7 = solver.IntVar(0, 1, 'main_main_tmp5_enob_7')
main_main_tmp5_enob_8 = solver.IntVar(0, 1, 'main_main_tmp5_enob_8')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3 + (1)*main_main_tmp5_enob_4 + (1)*main_main_tmp5_enob_6 + (1)*main_main_tmp5_enob_7 + (1)*main_main_tmp5_enob_8==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp5 + (-1)*main_tmp_enob_storeENOB + (10000)*main_main_tmp5_enob_6<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.200000e+00
ConstantValue__4_fixbits = solver.IntVar(0, 30, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__4_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.200000e+00
ConstantValue__5_fixbits = solver.IntVar(0, 30, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__5_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul144 = fmul double %tmp5, 1.200000e+00, !taffo.info !65, !taffo.initweight !21, !taffo.constinfo !67
main_D_CAST_mul144_fixbits = solver.IntVar(0, 16, 'main_D_CAST_mul144_fixbits')
main_D_CAST_mul144_fixp = solver.IntVar(0, 1, 'main_D_CAST_mul144_fixp')
main_D_CAST_mul144_float = solver.IntVar(0, 1, 'main_D_CAST_mul144_float')
main_D_CAST_mul144_double = solver.IntVar(0, 1, 'main_D_CAST_mul144_double')
solver.Add( + (1)*main_D_CAST_mul144_fixp + (1)*main_D_CAST_mul144_float + (1)*main_D_CAST_mul144_double==1)    #exactly 1 type
solver.Add( + (1)*main_D_CAST_mul144_fixbits + (-10000)*main_D_CAST_mul144_fixp<=0)    #If no fix, fix frac part = 0
C1_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C1_main_D_CAST_mul144')
C2_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C2_main_D_CAST_mul144')
solver.Add( + (1)*main_D_fixbits + (-1)*main_D_CAST_mul144_fixbits + (-10000)*C1_main_D_CAST_mul144<=0)    #Shift cost 1
solver.Add( + (-1)*main_D_fixbits + (1)*main_D_CAST_mul144_fixbits + (-10000)*C2_main_D_CAST_mul144<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_D_CAST_mul144
castCostObj +=  + (1)*C2_main_D_CAST_mul144
C3_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C3_main_D_CAST_mul144')
C4_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C4_main_D_CAST_mul144')
C5_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C5_main_D_CAST_mul144')
C6_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C6_main_D_CAST_mul144')
C7_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C7_main_D_CAST_mul144')
C8_main_D_CAST_mul144 = solver.IntVar(0, 1, 'C8_main_D_CAST_mul144')
solver.Add( + (1)*main_D_fixp + (1)*main_D_CAST_mul144_float + (-1)*C3_main_D_CAST_mul144<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_D_CAST_mul144
solver.Add( + (1)*main_D_float + (1)*main_D_CAST_mul144_fixp + (-1)*C4_main_D_CAST_mul144<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_D_CAST_mul144
solver.Add( + (1)*main_D_fixp + (1)*main_D_CAST_mul144_double + (-1)*C5_main_D_CAST_mul144<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_D_CAST_mul144
solver.Add( + (1)*main_D_double + (1)*main_D_CAST_mul144_fixp + (-1)*C6_main_D_CAST_mul144<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_D_CAST_mul144
solver.Add( + (1)*main_D_float + (1)*main_D_CAST_mul144_double + (-1)*C7_main_D_CAST_mul144<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_D_CAST_mul144
solver.Add( + (1)*main_D_double + (1)*main_D_CAST_mul144_float + (-1)*C8_main_D_CAST_mul144<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_D_CAST_mul144



#Stuff for double 1.200000e+00
ConstantValue__6_fixbits = solver.IntVar(0, 30, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__6_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul144 = fmul double %tmp5, 1.200000e+00, !taffo.info !65, !taffo.initweight !21, !taffo.constinfo !67
ConstantValue__6_CAST_mul144_fixbits = solver.IntVar(0, 30, 'ConstantValue__6_CAST_mul144_fixbits')
ConstantValue__6_CAST_mul144_fixp = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul144_fixp')
ConstantValue__6_CAST_mul144_float = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul144_float')
ConstantValue__6_CAST_mul144_double = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul144_double')
solver.Add( + (1)*ConstantValue__6_CAST_mul144_fixp + (1)*ConstantValue__6_CAST_mul144_float + (1)*ConstantValue__6_CAST_mul144_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__6_CAST_mul144_fixbits + (-10000)*ConstantValue__6_CAST_mul144_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C1_ConstantValue__6_CAST_mul144')
C2_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C2_ConstantValue__6_CAST_mul144')
solver.Add( + (1)*ConstantValue__6_fixbits + (-1)*ConstantValue__6_CAST_mul144_fixbits + (-10000)*C1_ConstantValue__6_CAST_mul144<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__6_fixbits + (1)*ConstantValue__6_CAST_mul144_fixbits + (-10000)*C2_ConstantValue__6_CAST_mul144<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__6_CAST_mul144
castCostObj +=  + (1)*C2_ConstantValue__6_CAST_mul144
C3_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C3_ConstantValue__6_CAST_mul144')
C4_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C4_ConstantValue__6_CAST_mul144')
C5_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C5_ConstantValue__6_CAST_mul144')
C6_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C6_ConstantValue__6_CAST_mul144')
C7_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C7_ConstantValue__6_CAST_mul144')
C8_ConstantValue__6_CAST_mul144 = solver.IntVar(0, 1, 'C8_ConstantValue__6_CAST_mul144')
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_mul144_float + (-1)*C3_ConstantValue__6_CAST_mul144<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__6_CAST_mul144
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_mul144_fixp + (-1)*C4_ConstantValue__6_CAST_mul144<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__6_CAST_mul144
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_mul144_double + (-1)*C5_ConstantValue__6_CAST_mul144<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__6_CAST_mul144
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_mul144_fixp + (-1)*C6_ConstantValue__6_CAST_mul144<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__6_CAST_mul144
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_mul144_double + (-1)*C7_ConstantValue__6_CAST_mul144<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__6_CAST_mul144
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_mul144_float + (-1)*C8_ConstantValue__6_CAST_mul144<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__6_CAST_mul144



#Stuff for   %mul144 = fmul double %tmp5, 1.200000e+00, !taffo.info !65, !taffo.initweight !21, !taffo.constinfo !67
main_mul144_fixbits = solver.IntVar(0, 16, 'main_mul144_fixbits')
main_mul144_fixp = solver.IntVar(0, 1, 'main_mul144_fixp')
main_mul144_float = solver.IntVar(0, 1, 'main_mul144_float')
main_mul144_double = solver.IntVar(0, 1, 'main_mul144_double')
main_mul144_enob = solver.IntVar(-10000, 10000, 'main_mul144_enob')
solver.Add( + (1)*main_mul144_enob + (-1)*main_mul144_fixbits + (10000)*main_mul144_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul144_enob + (10000)*main_mul144_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul144_enob + (10000)*main_mul144_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul144_fixbits + (-10000)*main_mul144_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul144_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul144_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul144_enob
solver.Add( + (1)*main_mul144_fixp + (1)*main_mul144_float + (1)*main_mul144_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul144_fixbits + (-10000)*main_mul144_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_D_CAST_mul144_fixp + (-1)*ConstantValue__6_CAST_mul144_fixp==0)    #fix equality
solver.Add( + (1)*main_D_CAST_mul144_float + (-1)*ConstantValue__6_CAST_mul144_float==0)    #float equality
solver.Add( + (1)*main_D_CAST_mul144_double + (-1)*ConstantValue__6_CAST_mul144_double==0)    #double equality
solver.Add( + (1)*main_D_CAST_mul144_fixp + (-1)*main_mul144_fixp==0)    #fix equality
solver.Add( + (1)*main_D_CAST_mul144_float + (-1)*main_mul144_float==0)    #float equality
solver.Add( + (1)*main_D_CAST_mul144_double + (-1)*main_mul144_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul144_fixp
mathCostObj +=  + (6)*main_mul144_float
mathCostObj +=  + (12.2551)*main_mul144_double
main_main_mul144_enob_1 = solver.IntVar(0, 1, 'main_main_mul144_enob_1')
main_main_mul144_enob_2 = solver.IntVar(0, 1, 'main_main_mul144_enob_2')
solver.Add( + (1)*main_main_mul144_enob_1 + (1)*main_main_mul144_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul144_enob + (-1)*ConstantValue__4_enob + (-10000)*main_main_mul144_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul144_enob + (-1)*main_D_enob_memphi_main_tmp5 + (-10000)*main_main_mul144_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   store double %mul144, double* %arrayidx143, align 8, !taffo.info !39, !taffo.initweight !22
main_mul144_CAST_store_fixbits = solver.IntVar(0, 16, 'main_mul144_CAST_store_fixbits')
main_mul144_CAST_store_fixp = solver.IntVar(0, 1, 'main_mul144_CAST_store_fixp')
main_mul144_CAST_store_float = solver.IntVar(0, 1, 'main_mul144_CAST_store_float')
main_mul144_CAST_store_double = solver.IntVar(0, 1, 'main_mul144_CAST_store_double')
solver.Add( + (1)*main_mul144_CAST_store_fixp + (1)*main_mul144_CAST_store_float + (1)*main_mul144_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul144_CAST_store_fixbits + (-10000)*main_mul144_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul144_CAST_store = solver.IntVar(0, 1, 'C1_main_mul144_CAST_store')
C2_main_mul144_CAST_store = solver.IntVar(0, 1, 'C2_main_mul144_CAST_store')
solver.Add( + (1)*main_mul144_fixbits + (-1)*main_mul144_CAST_store_fixbits + (-10000)*C1_main_mul144_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul144_fixbits + (1)*main_mul144_CAST_store_fixbits + (-10000)*C2_main_mul144_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul144_CAST_store
castCostObj +=  + (1)*C2_main_mul144_CAST_store
C3_main_mul144_CAST_store = solver.IntVar(0, 1, 'C3_main_mul144_CAST_store')
C4_main_mul144_CAST_store = solver.IntVar(0, 1, 'C4_main_mul144_CAST_store')
C5_main_mul144_CAST_store = solver.IntVar(0, 1, 'C5_main_mul144_CAST_store')
C6_main_mul144_CAST_store = solver.IntVar(0, 1, 'C6_main_mul144_CAST_store')
C7_main_mul144_CAST_store = solver.IntVar(0, 1, 'C7_main_mul144_CAST_store')
C8_main_mul144_CAST_store = solver.IntVar(0, 1, 'C8_main_mul144_CAST_store')
solver.Add( + (1)*main_mul144_fixp + (1)*main_mul144_CAST_store_float + (-1)*C3_main_mul144_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul144_CAST_store
solver.Add( + (1)*main_mul144_float + (1)*main_mul144_CAST_store_fixp + (-1)*C4_main_mul144_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul144_CAST_store
solver.Add( + (1)*main_mul144_fixp + (1)*main_mul144_CAST_store_double + (-1)*C5_main_mul144_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul144_CAST_store
solver.Add( + (1)*main_mul144_double + (1)*main_mul144_CAST_store_fixp + (-1)*C6_main_mul144_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul144_CAST_store
solver.Add( + (1)*main_mul144_float + (1)*main_mul144_CAST_store_double + (-1)*C7_main_mul144_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul144_CAST_store
solver.Add( + (1)*main_mul144_double + (1)*main_mul144_CAST_store_float + (-1)*C8_main_mul144_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul144_CAST_store
solver.Add( + (1)*main_D_fixp + (-1)*main_mul144_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_D_float + (-1)*main_mul144_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_D_double + (-1)*main_mul144_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_D_fixbits + (-1)*main_mul144_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_D_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_D_enob_storeENOB')
solver.Add( + (1)*main_D_enob_storeENOB + (-1)*main_D_fixbits + (10000)*main_D_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_D_enob_storeENOB + (10000)*main_D_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_D_enob_storeENOB + (10000)*main_D_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_D_enob_storeENOB + (-1)*main_mul144_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp5 + (-1)*main_D_enob_storeENOB + (10000)*main_main_tmp5_enob_7<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_tmp_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'main_tmp_enob_memphi_main_tmp6')
solver.Add( + (1)*main_tmp_enob_memphi_main_tmp6 + (-1)*main_tmp_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
main_main_tmp6_enob_3 = solver.IntVar(0, 1, 'main_main_tmp6_enob_3')
main_main_tmp6_enob_4 = solver.IntVar(0, 1, 'main_main_tmp6_enob_4')
main_main_tmp6_enob_6 = solver.IntVar(0, 1, 'main_main_tmp6_enob_6')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2 + (1)*main_main_tmp6_enob_3 + (1)*main_main_tmp6_enob_4 + (1)*main_main_tmp6_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_tmp_enob_memphi_main_tmp6 + (-1)*main_tmp_enob_storeENOB + (10000)*main_main_tmp6_enob_6<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_C_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'main_C_enob_memphi_main_tmp7')
solver.Add( + (1)*main_C_enob_memphi_main_tmp7 + (-1)*main_C_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
main_main_tmp7_enob_2 = solver.IntVar(0, 1, 'main_main_tmp7_enob_2')
main_main_tmp7_enob_3 = solver.IntVar(0, 1, 'main_main_tmp7_enob_3')
solver.Add( + (1)*main_main_tmp7_enob_1 + (1)*main_main_tmp7_enob_2 + (1)*main_main_tmp7_enob_3==1)    #Enob: one selected constraint



#Constraint for cast for   %mul157 = fmul double %tmp6, %tmp7, !taffo.info !11, !taffo.initweight !33
main_tmp_CAST_mul157_fixbits = solver.IntVar(0, 16, 'main_tmp_CAST_mul157_fixbits')
main_tmp_CAST_mul157_fixp = solver.IntVar(0, 1, 'main_tmp_CAST_mul157_fixp')
main_tmp_CAST_mul157_float = solver.IntVar(0, 1, 'main_tmp_CAST_mul157_float')
main_tmp_CAST_mul157_double = solver.IntVar(0, 1, 'main_tmp_CAST_mul157_double')
solver.Add( + (1)*main_tmp_CAST_mul157_fixp + (1)*main_tmp_CAST_mul157_float + (1)*main_tmp_CAST_mul157_double==1)    #exactly 1 type
solver.Add( + (1)*main_tmp_CAST_mul157_fixbits + (-10000)*main_tmp_CAST_mul157_fixp<=0)    #If no fix, fix frac part = 0
C1_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C1_main_tmp_CAST_mul157')
C2_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C2_main_tmp_CAST_mul157')
solver.Add( + (1)*main_tmp_fixbits + (-1)*main_tmp_CAST_mul157_fixbits + (-10000)*C1_main_tmp_CAST_mul157<=0)    #Shift cost 1
solver.Add( + (-1)*main_tmp_fixbits + (1)*main_tmp_CAST_mul157_fixbits + (-10000)*C2_main_tmp_CAST_mul157<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_tmp_CAST_mul157
castCostObj +=  + (1)*C2_main_tmp_CAST_mul157
C3_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C3_main_tmp_CAST_mul157')
C4_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C4_main_tmp_CAST_mul157')
C5_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C5_main_tmp_CAST_mul157')
C6_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C6_main_tmp_CAST_mul157')
C7_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C7_main_tmp_CAST_mul157')
C8_main_tmp_CAST_mul157 = solver.IntVar(0, 1, 'C8_main_tmp_CAST_mul157')
solver.Add( + (1)*main_tmp_fixp + (1)*main_tmp_CAST_mul157_float + (-1)*C3_main_tmp_CAST_mul157<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_tmp_CAST_mul157
solver.Add( + (1)*main_tmp_float + (1)*main_tmp_CAST_mul157_fixp + (-1)*C4_main_tmp_CAST_mul157<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_tmp_CAST_mul157
solver.Add( + (1)*main_tmp_fixp + (1)*main_tmp_CAST_mul157_double + (-1)*C5_main_tmp_CAST_mul157<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_tmp_CAST_mul157
solver.Add( + (1)*main_tmp_double + (1)*main_tmp_CAST_mul157_fixp + (-1)*C6_main_tmp_CAST_mul157<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_tmp_CAST_mul157
solver.Add( + (1)*main_tmp_float + (1)*main_tmp_CAST_mul157_double + (-1)*C7_main_tmp_CAST_mul157<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_tmp_CAST_mul157
solver.Add( + (1)*main_tmp_double + (1)*main_tmp_CAST_mul157_float + (-1)*C8_main_tmp_CAST_mul157<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_tmp_CAST_mul157



#Constraint for cast for   %mul157 = fmul double %tmp6, %tmp7, !taffo.info !11, !taffo.initweight !33
main_C_CAST_mul157_fixbits = solver.IntVar(0, 31, 'main_C_CAST_mul157_fixbits')
main_C_CAST_mul157_fixp = solver.IntVar(0, 1, 'main_C_CAST_mul157_fixp')
main_C_CAST_mul157_float = solver.IntVar(0, 1, 'main_C_CAST_mul157_float')
main_C_CAST_mul157_double = solver.IntVar(0, 1, 'main_C_CAST_mul157_double')
solver.Add( + (1)*main_C_CAST_mul157_fixp + (1)*main_C_CAST_mul157_float + (1)*main_C_CAST_mul157_double==1)    #exactly 1 type
solver.Add( + (1)*main_C_CAST_mul157_fixbits + (-10000)*main_C_CAST_mul157_fixp<=0)    #If no fix, fix frac part = 0
C1_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C1_main_C_CAST_mul157')
C2_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C2_main_C_CAST_mul157')
solver.Add( + (1)*main_C_fixbits + (-1)*main_C_CAST_mul157_fixbits + (-10000)*C1_main_C_CAST_mul157<=0)    #Shift cost 1
solver.Add( + (-1)*main_C_fixbits + (1)*main_C_CAST_mul157_fixbits + (-10000)*C2_main_C_CAST_mul157<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_C_CAST_mul157
castCostObj +=  + (1)*C2_main_C_CAST_mul157
C3_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C3_main_C_CAST_mul157')
C4_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C4_main_C_CAST_mul157')
C5_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C5_main_C_CAST_mul157')
C6_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C6_main_C_CAST_mul157')
C7_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C7_main_C_CAST_mul157')
C8_main_C_CAST_mul157 = solver.IntVar(0, 1, 'C8_main_C_CAST_mul157')
solver.Add( + (1)*main_C_fixp + (1)*main_C_CAST_mul157_float + (-1)*C3_main_C_CAST_mul157<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_C_CAST_mul157
solver.Add( + (1)*main_C_float + (1)*main_C_CAST_mul157_fixp + (-1)*C4_main_C_CAST_mul157<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_C_CAST_mul157
solver.Add( + (1)*main_C_fixp + (1)*main_C_CAST_mul157_double + (-1)*C5_main_C_CAST_mul157<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_C_CAST_mul157
solver.Add( + (1)*main_C_double + (1)*main_C_CAST_mul157_fixp + (-1)*C6_main_C_CAST_mul157<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_C_CAST_mul157
solver.Add( + (1)*main_C_float + (1)*main_C_CAST_mul157_double + (-1)*C7_main_C_CAST_mul157<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_C_CAST_mul157
solver.Add( + (1)*main_C_double + (1)*main_C_CAST_mul157_float + (-1)*C8_main_C_CAST_mul157<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_C_CAST_mul157



#Stuff for   %mul157 = fmul double %tmp6, %tmp7, !taffo.info !11, !taffo.initweight !33
main_mul157_fixbits = solver.IntVar(0, 16, 'main_mul157_fixbits')
main_mul157_fixp = solver.IntVar(0, 1, 'main_mul157_fixp')
main_mul157_float = solver.IntVar(0, 1, 'main_mul157_float')
main_mul157_double = solver.IntVar(0, 1, 'main_mul157_double')
main_mul157_enob = solver.IntVar(-10000, 10000, 'main_mul157_enob')
solver.Add( + (1)*main_mul157_enob + (-1)*main_mul157_fixbits + (10000)*main_mul157_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul157_enob + (10000)*main_mul157_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul157_enob + (10000)*main_mul157_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul157_fixbits + (-10000)*main_mul157_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul157_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul157_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul157_enob
solver.Add( + (1)*main_mul157_fixp + (1)*main_mul157_float + (1)*main_mul157_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul157_fixbits + (-10000)*main_mul157_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_tmp_CAST_mul157_fixp + (-1)*main_C_CAST_mul157_fixp==0)    #fix equality
solver.Add( + (1)*main_tmp_CAST_mul157_float + (-1)*main_C_CAST_mul157_float==0)    #float equality
solver.Add( + (1)*main_tmp_CAST_mul157_double + (-1)*main_C_CAST_mul157_double==0)    #double equality
solver.Add( + (1)*main_tmp_CAST_mul157_fixp + (-1)*main_mul157_fixp==0)    #fix equality
solver.Add( + (1)*main_tmp_CAST_mul157_float + (-1)*main_mul157_float==0)    #float equality
solver.Add( + (1)*main_tmp_CAST_mul157_double + (-1)*main_mul157_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul157_fixp
mathCostObj +=  + (6)*main_mul157_float
mathCostObj +=  + (12.2551)*main_mul157_double
main_main_mul157_enob_1 = solver.IntVar(0, 1, 'main_main_mul157_enob_1')
main_main_mul157_enob_2 = solver.IntVar(0, 1, 'main_main_mul157_enob_2')
solver.Add( + (1)*main_main_mul157_enob_1 + (1)*main_main_mul157_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul157_enob + (-1)*main_C_enob_memphi_main_tmp7 + (-10000)*main_main_mul157_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul157_enob + (-1)*main_tmp_enob_memphi_main_tmp6 + (-10000)*main_main_mul157_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_D_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_D_enob_memphi_main_tmp8')
solver.Add( + (1)*main_D_enob_memphi_main_tmp8 + (-1)*main_D_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_0 = solver.IntVar(0, 1, 'main_main_tmp8_enob_0')
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
solver.Add( + (1)*main_main_tmp8_enob_0 + (1)*main_main_tmp8_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp8 + (-1)*main_D_enob_storeENOB + (10000)*main_main_tmp8_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add162 = fadd double %tmp8, %mul157, !taffo.info !70, !taffo.initweight !33
main_D_CAST_add162_fixbits = solver.IntVar(0, 16, 'main_D_CAST_add162_fixbits')
main_D_CAST_add162_fixp = solver.IntVar(0, 1, 'main_D_CAST_add162_fixp')
main_D_CAST_add162_float = solver.IntVar(0, 1, 'main_D_CAST_add162_float')
main_D_CAST_add162_double = solver.IntVar(0, 1, 'main_D_CAST_add162_double')
solver.Add( + (1)*main_D_CAST_add162_fixp + (1)*main_D_CAST_add162_float + (1)*main_D_CAST_add162_double==1)    #exactly 1 type
solver.Add( + (1)*main_D_CAST_add162_fixbits + (-10000)*main_D_CAST_add162_fixp<=0)    #If no fix, fix frac part = 0
C1_main_D_CAST_add162 = solver.IntVar(0, 1, 'C1_main_D_CAST_add162')
C2_main_D_CAST_add162 = solver.IntVar(0, 1, 'C2_main_D_CAST_add162')
solver.Add( + (1)*main_D_fixbits + (-1)*main_D_CAST_add162_fixbits + (-10000)*C1_main_D_CAST_add162<=0)    #Shift cost 1
solver.Add( + (-1)*main_D_fixbits + (1)*main_D_CAST_add162_fixbits + (-10000)*C2_main_D_CAST_add162<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_D_CAST_add162
castCostObj +=  + (1)*C2_main_D_CAST_add162
C3_main_D_CAST_add162 = solver.IntVar(0, 1, 'C3_main_D_CAST_add162')
C4_main_D_CAST_add162 = solver.IntVar(0, 1, 'C4_main_D_CAST_add162')
C5_main_D_CAST_add162 = solver.IntVar(0, 1, 'C5_main_D_CAST_add162')
C6_main_D_CAST_add162 = solver.IntVar(0, 1, 'C6_main_D_CAST_add162')
C7_main_D_CAST_add162 = solver.IntVar(0, 1, 'C7_main_D_CAST_add162')
C8_main_D_CAST_add162 = solver.IntVar(0, 1, 'C8_main_D_CAST_add162')
solver.Add( + (1)*main_D_fixp + (1)*main_D_CAST_add162_float + (-1)*C3_main_D_CAST_add162<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_D_CAST_add162
solver.Add( + (1)*main_D_float + (1)*main_D_CAST_add162_fixp + (-1)*C4_main_D_CAST_add162<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_D_CAST_add162
solver.Add( + (1)*main_D_fixp + (1)*main_D_CAST_add162_double + (-1)*C5_main_D_CAST_add162<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_D_CAST_add162
solver.Add( + (1)*main_D_double + (1)*main_D_CAST_add162_fixp + (-1)*C6_main_D_CAST_add162<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_D_CAST_add162
solver.Add( + (1)*main_D_float + (1)*main_D_CAST_add162_double + (-1)*C7_main_D_CAST_add162<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_D_CAST_add162
solver.Add( + (1)*main_D_double + (1)*main_D_CAST_add162_float + (-1)*C8_main_D_CAST_add162<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_D_CAST_add162



#Constraint for cast for   %add162 = fadd double %tmp8, %mul157, !taffo.info !70, !taffo.initweight !33
main_mul157_CAST_add162_fixbits = solver.IntVar(0, 16, 'main_mul157_CAST_add162_fixbits')
main_mul157_CAST_add162_fixp = solver.IntVar(0, 1, 'main_mul157_CAST_add162_fixp')
main_mul157_CAST_add162_float = solver.IntVar(0, 1, 'main_mul157_CAST_add162_float')
main_mul157_CAST_add162_double = solver.IntVar(0, 1, 'main_mul157_CAST_add162_double')
solver.Add( + (1)*main_mul157_CAST_add162_fixp + (1)*main_mul157_CAST_add162_float + (1)*main_mul157_CAST_add162_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul157_CAST_add162_fixbits + (-10000)*main_mul157_CAST_add162_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C1_main_mul157_CAST_add162')
C2_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C2_main_mul157_CAST_add162')
solver.Add( + (1)*main_mul157_fixbits + (-1)*main_mul157_CAST_add162_fixbits + (-10000)*C1_main_mul157_CAST_add162<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul157_fixbits + (1)*main_mul157_CAST_add162_fixbits + (-10000)*C2_main_mul157_CAST_add162<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul157_CAST_add162
castCostObj +=  + (1)*C2_main_mul157_CAST_add162
C3_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C3_main_mul157_CAST_add162')
C4_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C4_main_mul157_CAST_add162')
C5_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C5_main_mul157_CAST_add162')
C6_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C6_main_mul157_CAST_add162')
C7_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C7_main_mul157_CAST_add162')
C8_main_mul157_CAST_add162 = solver.IntVar(0, 1, 'C8_main_mul157_CAST_add162')
solver.Add( + (1)*main_mul157_fixp + (1)*main_mul157_CAST_add162_float + (-1)*C3_main_mul157_CAST_add162<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul157_CAST_add162
solver.Add( + (1)*main_mul157_float + (1)*main_mul157_CAST_add162_fixp + (-1)*C4_main_mul157_CAST_add162<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul157_CAST_add162
solver.Add( + (1)*main_mul157_fixp + (1)*main_mul157_CAST_add162_double + (-1)*C5_main_mul157_CAST_add162<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul157_CAST_add162
solver.Add( + (1)*main_mul157_double + (1)*main_mul157_CAST_add162_fixp + (-1)*C6_main_mul157_CAST_add162<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul157_CAST_add162
solver.Add( + (1)*main_mul157_float + (1)*main_mul157_CAST_add162_double + (-1)*C7_main_mul157_CAST_add162<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul157_CAST_add162
solver.Add( + (1)*main_mul157_double + (1)*main_mul157_CAST_add162_float + (-1)*C8_main_mul157_CAST_add162<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul157_CAST_add162



#Stuff for   %add162 = fadd double %tmp8, %mul157, !taffo.info !70, !taffo.initweight !33
main_add162_fixbits = solver.IntVar(0, 15, 'main_add162_fixbits')
main_add162_fixp = solver.IntVar(0, 1, 'main_add162_fixp')
main_add162_float = solver.IntVar(0, 1, 'main_add162_float')
main_add162_double = solver.IntVar(0, 1, 'main_add162_double')
main_add162_enob = solver.IntVar(-10000, 10000, 'main_add162_enob')
solver.Add( + (1)*main_add162_enob + (-1)*main_add162_fixbits + (10000)*main_add162_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add162_enob + (10000)*main_add162_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add162_enob + (10000)*main_add162_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add162_fixbits + (-10000)*main_add162_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add162_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add162_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add162_enob
solver.Add( + (1)*main_add162_fixp + (1)*main_add162_float + (1)*main_add162_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add162_fixbits + (-10000)*main_add162_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_D_CAST_add162_fixp + (-1)*main_mul157_CAST_add162_fixp==0)    #fix equality
solver.Add( + (1)*main_D_CAST_add162_float + (-1)*main_mul157_CAST_add162_float==0)    #float equality
solver.Add( + (1)*main_D_CAST_add162_double + (-1)*main_mul157_CAST_add162_double==0)    #double equality
solver.Add( + (1)*main_D_CAST_add162_fixbits + (-1)*main_mul157_CAST_add162_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_D_CAST_add162_fixp + (-1)*main_add162_fixp==0)    #fix equality
solver.Add( + (1)*main_D_CAST_add162_float + (-1)*main_add162_float==0)    #float equality
solver.Add( + (1)*main_D_CAST_add162_double + (-1)*main_add162_double==0)    #double equality
solver.Add( + (1)*main_D_CAST_add162_fixbits + (-1)*main_add162_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add162_fixp
mathCostObj +=  + (3)*main_add162_float
mathCostObj +=  + (6.64928)*main_add162_double
solver.Add( + (1)*main_add162_enob + (-1)*main_D_enob_memphi_main_tmp8<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add162_enob + (-1)*main_mul157_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add162, double* %arrayidx161, align 8, !taffo.info !11, !taffo.initweight !22
main_add162_CAST_store_fixbits = solver.IntVar(0, 15, 'main_add162_CAST_store_fixbits')
main_add162_CAST_store_fixp = solver.IntVar(0, 1, 'main_add162_CAST_store_fixp')
main_add162_CAST_store_float = solver.IntVar(0, 1, 'main_add162_CAST_store_float')
main_add162_CAST_store_double = solver.IntVar(0, 1, 'main_add162_CAST_store_double')
solver.Add( + (1)*main_add162_CAST_store_fixp + (1)*main_add162_CAST_store_float + (1)*main_add162_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add162_CAST_store_fixbits + (-10000)*main_add162_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add162_CAST_store = solver.IntVar(0, 1, 'C1_main_add162_CAST_store')
C2_main_add162_CAST_store = solver.IntVar(0, 1, 'C2_main_add162_CAST_store')
solver.Add( + (1)*main_add162_fixbits + (-1)*main_add162_CAST_store_fixbits + (-10000)*C1_main_add162_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add162_fixbits + (1)*main_add162_CAST_store_fixbits + (-10000)*C2_main_add162_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add162_CAST_store
castCostObj +=  + (1)*C2_main_add162_CAST_store
C3_main_add162_CAST_store = solver.IntVar(0, 1, 'C3_main_add162_CAST_store')
C4_main_add162_CAST_store = solver.IntVar(0, 1, 'C4_main_add162_CAST_store')
C5_main_add162_CAST_store = solver.IntVar(0, 1, 'C5_main_add162_CAST_store')
C6_main_add162_CAST_store = solver.IntVar(0, 1, 'C6_main_add162_CAST_store')
C7_main_add162_CAST_store = solver.IntVar(0, 1, 'C7_main_add162_CAST_store')
C8_main_add162_CAST_store = solver.IntVar(0, 1, 'C8_main_add162_CAST_store')
solver.Add( + (1)*main_add162_fixp + (1)*main_add162_CAST_store_float + (-1)*C3_main_add162_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add162_CAST_store
solver.Add( + (1)*main_add162_float + (1)*main_add162_CAST_store_fixp + (-1)*C4_main_add162_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add162_CAST_store
solver.Add( + (1)*main_add162_fixp + (1)*main_add162_CAST_store_double + (-1)*C5_main_add162_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add162_CAST_store
solver.Add( + (1)*main_add162_double + (1)*main_add162_CAST_store_fixp + (-1)*C6_main_add162_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add162_CAST_store
solver.Add( + (1)*main_add162_float + (1)*main_add162_CAST_store_double + (-1)*C7_main_add162_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add162_CAST_store
solver.Add( + (1)*main_add162_double + (1)*main_add162_CAST_store_float + (-1)*C8_main_add162_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add162_CAST_store
solver.Add( + (1)*main_D_fixp + (-1)*main_add162_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_D_float + (-1)*main_add162_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_D_double + (-1)*main_add162_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_D_fixbits + (-1)*main_add162_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_D_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_D_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_D_enob_storeENOB_storeENOB + (-1)*main_D_fixbits + (10000)*main_D_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_D_enob_storeENOB_storeENOB + (10000)*main_D_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_D_enob_storeENOB_storeENOB + (10000)*main_D_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_D_enob_storeENOB_storeENOB + (-1)*main_add162_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp5 + (-1)*main_D_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_8<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp8 + (-1)*main_D_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_D_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'main_D_enob_memphi_main_tmp11')
solver.Add( + (1)*main_D_enob_memphi_main_tmp11 + (-1)*main_D_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_1 = solver.IntVar(0, 1, 'main_main_tmp11_enob_1')
main_main_tmp11_enob_2 = solver.IntVar(0, 1, 'main_main_tmp11_enob_2')
main_main_tmp11_enob_3 = solver.IntVar(0, 1, 'main_main_tmp11_enob_3')
main_main_tmp11_enob_4 = solver.IntVar(0, 1, 'main_main_tmp11_enob_4')
main_main_tmp11_enob_6 = solver.IntVar(0, 1, 'main_main_tmp11_enob_6')
main_main_tmp11_enob_7 = solver.IntVar(0, 1, 'main_main_tmp11_enob_7')
main_main_tmp11_enob_8 = solver.IntVar(0, 1, 'main_main_tmp11_enob_8')
solver.Add( + (1)*main_main_tmp11_enob_1 + (1)*main_main_tmp11_enob_2 + (1)*main_main_tmp11_enob_3 + (1)*main_main_tmp11_enob_4 + (1)*main_main_tmp11_enob_6 + (1)*main_main_tmp11_enob_7 + (1)*main_main_tmp11_enob_8==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp11 + (-1)*main_tmp_enob_storeENOB + (10000)*main_main_tmp11_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp11 + (-1)*main_D_enob_storeENOB + (10000)*main_main_tmp11_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_D_enob_memphi_main_tmp11 + (-1)*main_D_enob_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_8<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call189 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp10, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp11), !taffo.info !11, !taffo.initweight !33, !taffo.constinfo !75
main_D_CAST_call189_fixbits = solver.IntVar(0, 16, 'main_D_CAST_call189_fixbits')
main_D_CAST_call189_fixp = solver.IntVar(0, 1, 'main_D_CAST_call189_fixp')
main_D_CAST_call189_float = solver.IntVar(0, 1, 'main_D_CAST_call189_float')
main_D_CAST_call189_double = solver.IntVar(0, 1, 'main_D_CAST_call189_double')
solver.Add( + (1)*main_D_CAST_call189_fixp + (1)*main_D_CAST_call189_float + (1)*main_D_CAST_call189_double==1)    #exactly 1 type
solver.Add( + (1)*main_D_CAST_call189_fixbits + (-10000)*main_D_CAST_call189_fixp<=0)    #If no fix, fix frac part = 0
C1_main_D_CAST_call189 = solver.IntVar(0, 1, 'C1_main_D_CAST_call189')
C2_main_D_CAST_call189 = solver.IntVar(0, 1, 'C2_main_D_CAST_call189')
solver.Add( + (1)*main_D_fixbits + (-1)*main_D_CAST_call189_fixbits + (-10000)*C1_main_D_CAST_call189<=0)    #Shift cost 1
solver.Add( + (-1)*main_D_fixbits + (1)*main_D_CAST_call189_fixbits + (-10000)*C2_main_D_CAST_call189<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_D_CAST_call189
castCostObj +=  + (1)*C2_main_D_CAST_call189
C3_main_D_CAST_call189 = solver.IntVar(0, 1, 'C3_main_D_CAST_call189')
C4_main_D_CAST_call189 = solver.IntVar(0, 1, 'C4_main_D_CAST_call189')
C5_main_D_CAST_call189 = solver.IntVar(0, 1, 'C5_main_D_CAST_call189')
C6_main_D_CAST_call189 = solver.IntVar(0, 1, 'C6_main_D_CAST_call189')
C7_main_D_CAST_call189 = solver.IntVar(0, 1, 'C7_main_D_CAST_call189')
C8_main_D_CAST_call189 = solver.IntVar(0, 1, 'C8_main_D_CAST_call189')
solver.Add( + (1)*main_D_fixp + (1)*main_D_CAST_call189_float + (-1)*C3_main_D_CAST_call189<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_D_CAST_call189
solver.Add( + (1)*main_D_float + (1)*main_D_CAST_call189_fixp + (-1)*C4_main_D_CAST_call189<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_D_CAST_call189
solver.Add( + (1)*main_D_fixp + (1)*main_D_CAST_call189_double + (-1)*C5_main_D_CAST_call189<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_D_CAST_call189
solver.Add( + (1)*main_D_double + (1)*main_D_CAST_call189_fixp + (-1)*C6_main_D_CAST_call189<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_D_CAST_call189
solver.Add( + (1)*main_D_float + (1)*main_D_CAST_call189_double + (-1)*C7_main_D_CAST_call189<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_D_CAST_call189
solver.Add( + (1)*main_D_double + (1)*main_D_CAST_call189_float + (-1)*C8_main_D_CAST_call189<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_D_CAST_call189
solver.Add( + (1)*main_D_CAST_call189_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(10000 * castCostObj / 270.67+ 1 * enobCostObj / 3663+ 10000 * mathCostObj / 62.3188)

# Model declaration end.