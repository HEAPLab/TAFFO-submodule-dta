


#Stuff for   %data = alloca [100 x [80 x double]], align 16, !taffo.info !12, !taffo.initweight !14
main_data_fixbits = solver.IntVar(0, 17, 'main_data_fixbits')
main_data_fixp = solver.IntVar(0, 1, 'main_data_fixp')
main_data_float = solver.IntVar(0, 1, 'main_data_float')
main_data_double = solver.IntVar(0, 1, 'main_data_double')
main_data_enob = solver.IntVar(-10000, 10000, 'main_data_enob')
solver.Add( + (1)*main_data_enob + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_fixbits + (-10000)*main_data_fixp>=-9984)    #Limit the lower number of frac bits17
enobCostObj =  + (-1)*main_data_enob
solver.Add( + (1)*main_data_fixp + (1)*main_data_float + (1)*main_data_double==1)    #Exactly one selected type
solver.Add( + (1)*main_data_fixbits + (-10000)*main_data_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %cov = alloca [100 x [80 x double]], align 16, !taffo.info !15, !taffo.initweight !14
main_cov_fixbits = solver.IntVar(0, 14, 'main_cov_fixbits')
main_cov_fixp = solver.IntVar(0, 1, 'main_cov_fixp')
main_cov_float = solver.IntVar(0, 1, 'main_cov_float')
main_cov_double = solver.IntVar(0, 1, 'main_cov_double')
main_cov_enob = solver.IntVar(-10000, 10000, 'main_cov_enob')
solver.Add( + (1)*main_cov_enob + (-1)*main_cov_fixbits + (10000)*main_cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_cov_enob + (10000)*main_cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_cov_enob + (10000)*main_cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_cov_fixbits + (-10000)*main_cov_fixp>=-9987)    #Limit the lower number of frac bits14
enobCostObj +=  + (-1)*main_cov_enob
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_float + (1)*main_cov_double==1)    #Exactly one selected type
solver.Add( + (1)*main_cov_fixbits + (-10000)*main_cov_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %mean = alloca [80 x double], align 16, !taffo.info !17, !taffo.initweight !14
main_mean_fixbits = solver.IntVar(0, 18, 'main_mean_fixbits')
main_mean_fixp = solver.IntVar(0, 1, 'main_mean_fixp')
main_mean_float = solver.IntVar(0, 1, 'main_mean_float')
main_mean_double = solver.IntVar(0, 1, 'main_mean_double')
main_mean_enob = solver.IntVar(-10000, 10000, 'main_mean_enob')
solver.Add( + (1)*main_mean_enob + (-1)*main_mean_fixbits + (10000)*main_mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mean_enob + (10000)*main_mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mean_enob + (10000)*main_mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mean_fixbits + (-10000)*main_mean_fixp>=-9983)    #Limit the lower number of frac bits18
enobCostObj +=  + (-1)*main_mean_enob
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_float + (1)*main_mean_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mean_fixbits + (-10000)*main_mean_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 8.000000e+01
ConstantValue__fixbits = solver.IntVar(0, 25, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 8.000000e+01
ConstantValue__0_fixbits = solver.IntVar(0, 25, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__1_fixbits = solver.IntVar(0, 32, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__2_fixbits = solver.IntVar(0, 32, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.info !17, !taffo.initweight !22, !taffo.constinfo !29
ConstantValue__2_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__2_CAST_store_fixbits')
ConstantValue__2_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__2_CAST_store_fixp')
ConstantValue__2_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__2_CAST_store_float')
ConstantValue__2_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__2_CAST_store_double')
solver.Add( + (1)*ConstantValue__2_CAST_store_fixp + (1)*ConstantValue__2_CAST_store_float + (1)*ConstantValue__2_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__2_CAST_store_fixbits + (-10000)*ConstantValue__2_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__2_CAST_store')
C2_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__2_CAST_store')
solver.Add( + (1)*ConstantValue__2_fixbits + (-1)*ConstantValue__2_CAST_store_fixbits + (-10000)*C1_ConstantValue__2_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__2_fixbits + (1)*ConstantValue__2_CAST_store_fixbits + (-10000)*C2_ConstantValue__2_CAST_store<=0)    #Shift cost 2
castCostObj =  + (1)*C1_ConstantValue__2_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__2_CAST_store
C3_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__2_CAST_store')
C4_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__2_CAST_store')
C5_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__2_CAST_store')
C6_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__2_CAST_store')
C7_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__2_CAST_store')
C8_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__2_CAST_store')
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_CAST_store_float + (-1)*C3_ConstantValue__2_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_float + (1)*ConstantValue__2_CAST_store_fixp + (-1)*C4_ConstantValue__2_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_CAST_store_double + (-1)*C5_ConstantValue__2_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_double + (1)*ConstantValue__2_CAST_store_fixp + (-1)*C6_ConstantValue__2_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_float + (1)*ConstantValue__2_CAST_store_double + (-1)*C7_ConstantValue__2_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_double + (1)*ConstantValue__2_CAST_store_float + (-1)*C8_ConstantValue__2_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__2_CAST_store
solver.Add( + (1)*main_mean_fixp + (-1)*ConstantValue__2_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_float + (-1)*ConstantValue__2_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_mean_double + (-1)*ConstantValue__2_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_mean_fixbits + (-1)*ConstantValue__2_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp')
solver.Add( + (1)*main_data_enob_memphi_main_tmp + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
solver.Add( + (1)*main_main_tmp_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp1')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp1 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
solver.Add( + (1)*main_main_tmp1_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add = fadd double %tmp1, %tmp, !taffo.info !17, !taffo.initweight !23
main_mean_CAST_add_fixbits = solver.IntVar(0, 18, 'main_mean_CAST_add_fixbits')
main_mean_CAST_add_fixp = solver.IntVar(0, 1, 'main_mean_CAST_add_fixp')
main_mean_CAST_add_float = solver.IntVar(0, 1, 'main_mean_CAST_add_float')
main_mean_CAST_add_double = solver.IntVar(0, 1, 'main_mean_CAST_add_double')
solver.Add( + (1)*main_mean_CAST_add_fixp + (1)*main_mean_CAST_add_float + (1)*main_mean_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_add_fixbits + (-10000)*main_mean_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_add = solver.IntVar(0, 1, 'C1_main_mean_CAST_add')
C2_main_mean_CAST_add = solver.IntVar(0, 1, 'C2_main_mean_CAST_add')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_add_fixbits + (-10000)*C1_main_mean_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_add_fixbits + (-10000)*C2_main_mean_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mean_CAST_add
castCostObj +=  + (1)*C2_main_mean_CAST_add
C3_main_mean_CAST_add = solver.IntVar(0, 1, 'C3_main_mean_CAST_add')
C4_main_mean_CAST_add = solver.IntVar(0, 1, 'C4_main_mean_CAST_add')
C5_main_mean_CAST_add = solver.IntVar(0, 1, 'C5_main_mean_CAST_add')
C6_main_mean_CAST_add = solver.IntVar(0, 1, 'C6_main_mean_CAST_add')
C7_main_mean_CAST_add = solver.IntVar(0, 1, 'C7_main_mean_CAST_add')
C8_main_mean_CAST_add = solver.IntVar(0, 1, 'C8_main_mean_CAST_add')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_add_float + (-1)*C3_main_mean_CAST_add<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mean_CAST_add
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_add_fixp + (-1)*C4_main_mean_CAST_add<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mean_CAST_add
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_add_double + (-1)*C5_main_mean_CAST_add<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mean_CAST_add
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_add_fixp + (-1)*C6_main_mean_CAST_add<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mean_CAST_add
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_add_double + (-1)*C7_main_mean_CAST_add<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mean_CAST_add
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_add_float + (-1)*C8_main_mean_CAST_add<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mean_CAST_add



#Constraint for cast for   %add = fadd double %tmp1, %tmp, !taffo.info !17, !taffo.initweight !23
main_data_CAST_add_fixbits = solver.IntVar(0, 17, 'main_data_CAST_add_fixbits')
main_data_CAST_add_fixp = solver.IntVar(0, 1, 'main_data_CAST_add_fixp')
main_data_CAST_add_float = solver.IntVar(0, 1, 'main_data_CAST_add_float')
main_data_CAST_add_double = solver.IntVar(0, 1, 'main_data_CAST_add_double')
solver.Add( + (1)*main_data_CAST_add_fixp + (1)*main_data_CAST_add_float + (1)*main_data_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_add_fixbits + (-10000)*main_data_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_add = solver.IntVar(0, 1, 'C1_main_data_CAST_add')
C2_main_data_CAST_add = solver.IntVar(0, 1, 'C2_main_data_CAST_add')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_add_fixbits + (-10000)*C1_main_data_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_add_fixbits + (-10000)*C2_main_data_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_add
castCostObj +=  + (1)*C2_main_data_CAST_add
C3_main_data_CAST_add = solver.IntVar(0, 1, 'C3_main_data_CAST_add')
C4_main_data_CAST_add = solver.IntVar(0, 1, 'C4_main_data_CAST_add')
C5_main_data_CAST_add = solver.IntVar(0, 1, 'C5_main_data_CAST_add')
C6_main_data_CAST_add = solver.IntVar(0, 1, 'C6_main_data_CAST_add')
C7_main_data_CAST_add = solver.IntVar(0, 1, 'C7_main_data_CAST_add')
C8_main_data_CAST_add = solver.IntVar(0, 1, 'C8_main_data_CAST_add')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_add_float + (-1)*C3_main_data_CAST_add<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_add
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_add_fixp + (-1)*C4_main_data_CAST_add<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_add
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_add_double + (-1)*C5_main_data_CAST_add<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_add
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_add_fixp + (-1)*C6_main_data_CAST_add<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_add
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_add_double + (-1)*C7_main_data_CAST_add<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_add
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_add_float + (-1)*C8_main_data_CAST_add<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_add



#Stuff for   %add = fadd double %tmp1, %tmp, !taffo.info !17, !taffo.initweight !23
main_add_fixbits = solver.IntVar(0, 18, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
main_add_enob = solver.IntVar(-10000, 10000, 'main_add_enob')
solver.Add( + (1)*main_add_enob + (-1)*main_add_fixbits + (10000)*main_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add_enob + (10000)*main_add_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add_enob + (10000)*main_add_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp>=-9983)    #Limit the lower number of frac bits18
enobCostObj +=  + (-1)*main_add_enob
solver.Add( + (1)*main_add_fixp + (1)*main_add_float + (1)*main_add_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mean_CAST_add_fixp + (-1)*main_data_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_add_float + (-1)*main_data_CAST_add_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_add_double + (-1)*main_data_CAST_add_double==0)    #double equality
solver.Add( + (1)*main_mean_CAST_add_fixbits + (-1)*main_data_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mean_CAST_add_fixp + (-1)*main_add_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_add_float + (-1)*main_add_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_add_double + (-1)*main_add_double==0)    #double equality
solver.Add( + (1)*main_mean_CAST_add_fixbits + (-1)*main_add_fixbits==0)    #same fractional bit
mathCostObj =  + (1.27246)*main_add_fixp
mathCostObj +=  + (3)*main_add_float
mathCostObj +=  + (6.64928)*main_add_double
solver.Add( + (1)*main_add_enob + (-1)*main_mean_enob_memphi_main_tmp1<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*main_data_enob_memphi_main_tmp<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add, double* %arrayidx35, align 8, !taffo.info !17, !taffo.initweight !22
main_add_CAST_store_fixbits = solver.IntVar(0, 18, 'main_add_CAST_store_fixbits')
main_add_CAST_store_fixp = solver.IntVar(0, 1, 'main_add_CAST_store_fixp')
main_add_CAST_store_float = solver.IntVar(0, 1, 'main_add_CAST_store_float')
main_add_CAST_store_double = solver.IntVar(0, 1, 'main_add_CAST_store_double')
solver.Add( + (1)*main_add_CAST_store_fixp + (1)*main_add_CAST_store_float + (1)*main_add_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add_CAST_store_fixbits + (-10000)*main_add_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add_CAST_store = solver.IntVar(0, 1, 'C1_main_add_CAST_store')
C2_main_add_CAST_store = solver.IntVar(0, 1, 'C2_main_add_CAST_store')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add_CAST_store_fixbits + (-10000)*C1_main_add_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add_fixbits + (1)*main_add_CAST_store_fixbits + (-10000)*C2_main_add_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add_CAST_store
castCostObj +=  + (1)*C2_main_add_CAST_store
C3_main_add_CAST_store = solver.IntVar(0, 1, 'C3_main_add_CAST_store')
C4_main_add_CAST_store = solver.IntVar(0, 1, 'C4_main_add_CAST_store')
C5_main_add_CAST_store = solver.IntVar(0, 1, 'C5_main_add_CAST_store')
C6_main_add_CAST_store = solver.IntVar(0, 1, 'C6_main_add_CAST_store')
C7_main_add_CAST_store = solver.IntVar(0, 1, 'C7_main_add_CAST_store')
C8_main_add_CAST_store = solver.IntVar(0, 1, 'C8_main_add_CAST_store')
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_float + (-1)*C3_main_add_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_fixp + (-1)*C4_main_add_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add_CAST_store
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_double + (-1)*C5_main_add_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_fixp + (-1)*C6_main_add_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_double + (-1)*C7_main_add_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_float + (-1)*C8_main_add_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add_CAST_store
solver.Add( + (1)*main_mean_fixp + (-1)*main_add_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_float + (-1)*main_add_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_mean_double + (-1)*main_add_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_mean_fixbits + (-1)*main_add_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_mean_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_mean_enob_storeENOB')
solver.Add( + (1)*main_mean_enob_storeENOB + (-1)*main_mean_fixbits + (10000)*main_mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mean_enob_storeENOB + (10000)*main_mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mean_enob_storeENOB + (10000)*main_mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mean_enob_storeENOB + (-1)*main_add_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp1 + (-1)*main_mean_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp2')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp2 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
solver.Add( + (1)*main_main_tmp2_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp2 + (-1)*main_mean_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp3')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp3 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_2==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp4')
solver.Add( + (1)*main_data_enob_memphi_main_tmp4 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3==1)    #Enob: one selected constraint



#Constraint for cast for   %sub = fsub double %tmp4, %tmp3, !taffo.info !17, !taffo.initweight !23
main_data_CAST_sub_fixbits = solver.IntVar(0, 17, 'main_data_CAST_sub_fixbits')
main_data_CAST_sub_fixp = solver.IntVar(0, 1, 'main_data_CAST_sub_fixp')
main_data_CAST_sub_float = solver.IntVar(0, 1, 'main_data_CAST_sub_float')
main_data_CAST_sub_double = solver.IntVar(0, 1, 'main_data_CAST_sub_double')
solver.Add( + (1)*main_data_CAST_sub_fixp + (1)*main_data_CAST_sub_float + (1)*main_data_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_sub_fixbits + (-10000)*main_data_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_sub = solver.IntVar(0, 1, 'C1_main_data_CAST_sub')
C2_main_data_CAST_sub = solver.IntVar(0, 1, 'C2_main_data_CAST_sub')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_sub_fixbits + (-10000)*C1_main_data_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_sub_fixbits + (-10000)*C2_main_data_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_sub
castCostObj +=  + (1)*C2_main_data_CAST_sub
C3_main_data_CAST_sub = solver.IntVar(0, 1, 'C3_main_data_CAST_sub')
C4_main_data_CAST_sub = solver.IntVar(0, 1, 'C4_main_data_CAST_sub')
C5_main_data_CAST_sub = solver.IntVar(0, 1, 'C5_main_data_CAST_sub')
C6_main_data_CAST_sub = solver.IntVar(0, 1, 'C6_main_data_CAST_sub')
C7_main_data_CAST_sub = solver.IntVar(0, 1, 'C7_main_data_CAST_sub')
C8_main_data_CAST_sub = solver.IntVar(0, 1, 'C8_main_data_CAST_sub')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub_float + (-1)*C3_main_data_CAST_sub<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_sub
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub_fixp + (-1)*C4_main_data_CAST_sub<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_sub
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub_double + (-1)*C5_main_data_CAST_sub<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_sub
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub_fixp + (-1)*C6_main_data_CAST_sub<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_sub
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub_double + (-1)*C7_main_data_CAST_sub<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_sub
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub_float + (-1)*C8_main_data_CAST_sub<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_sub



#Constraint for cast for   %sub = fsub double %tmp4, %tmp3, !taffo.info !17, !taffo.initweight !23
main_mean_CAST_sub_fixbits = solver.IntVar(0, 18, 'main_mean_CAST_sub_fixbits')
main_mean_CAST_sub_fixp = solver.IntVar(0, 1, 'main_mean_CAST_sub_fixp')
main_mean_CAST_sub_float = solver.IntVar(0, 1, 'main_mean_CAST_sub_float')
main_mean_CAST_sub_double = solver.IntVar(0, 1, 'main_mean_CAST_sub_double')
solver.Add( + (1)*main_mean_CAST_sub_fixp + (1)*main_mean_CAST_sub_float + (1)*main_mean_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_sub_fixbits + (-10000)*main_mean_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_sub = solver.IntVar(0, 1, 'C1_main_mean_CAST_sub')
C2_main_mean_CAST_sub = solver.IntVar(0, 1, 'C2_main_mean_CAST_sub')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_sub_fixbits + (-10000)*C1_main_mean_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_sub_fixbits + (-10000)*C2_main_mean_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mean_CAST_sub
castCostObj +=  + (1)*C2_main_mean_CAST_sub
C3_main_mean_CAST_sub = solver.IntVar(0, 1, 'C3_main_mean_CAST_sub')
C4_main_mean_CAST_sub = solver.IntVar(0, 1, 'C4_main_mean_CAST_sub')
C5_main_mean_CAST_sub = solver.IntVar(0, 1, 'C5_main_mean_CAST_sub')
C6_main_mean_CAST_sub = solver.IntVar(0, 1, 'C6_main_mean_CAST_sub')
C7_main_mean_CAST_sub = solver.IntVar(0, 1, 'C7_main_mean_CAST_sub')
C8_main_mean_CAST_sub = solver.IntVar(0, 1, 'C8_main_mean_CAST_sub')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub_float + (-1)*C3_main_mean_CAST_sub<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mean_CAST_sub
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub_fixp + (-1)*C4_main_mean_CAST_sub<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mean_CAST_sub
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub_double + (-1)*C5_main_mean_CAST_sub<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mean_CAST_sub
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub_fixp + (-1)*C6_main_mean_CAST_sub<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mean_CAST_sub
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub_double + (-1)*C7_main_mean_CAST_sub<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mean_CAST_sub
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub_float + (-1)*C8_main_mean_CAST_sub<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mean_CAST_sub



#Stuff for   %sub = fsub double %tmp4, %tmp3, !taffo.info !17, !taffo.initweight !23
main_sub_fixbits = solver.IntVar(0, 18, 'main_sub_fixbits')
main_sub_fixp = solver.IntVar(0, 1, 'main_sub_fixp')
main_sub_float = solver.IntVar(0, 1, 'main_sub_float')
main_sub_double = solver.IntVar(0, 1, 'main_sub_double')
main_sub_enob = solver.IntVar(-10000, 10000, 'main_sub_enob')
solver.Add( + (1)*main_sub_enob + (-1)*main_sub_fixbits + (10000)*main_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp>=-9983)    #Limit the lower number of frac bits18
enobCostObj +=  + (-1)*main_sub_enob
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_float + (1)*main_sub_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_sub_fixp + (-1)*main_mean_CAST_sub_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub_float + (-1)*main_mean_CAST_sub_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub_double + (-1)*main_mean_CAST_sub_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub_fixbits + (-1)*main_mean_CAST_sub_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_data_CAST_sub_fixp + (-1)*main_sub_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub_float + (-1)*main_sub_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub_double + (-1)*main_sub_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub_fixbits + (-1)*main_sub_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub_fixp
mathCostObj +=  + (3)*main_sub_float
mathCostObj +=  + (6.64928)*main_sub_double
solver.Add( + (1)*main_sub_enob + (-1)*main_data_enob_memphi_main_tmp4<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub_enob + (-1)*main_mean_enob_memphi_main_tmp3<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub, double* %arrayidx58, align 8, !taffo.info !12, !taffo.initweight !23
main_sub_CAST_store_fixbits = solver.IntVar(0, 18, 'main_sub_CAST_store_fixbits')
main_sub_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub_CAST_store_fixp')
main_sub_CAST_store_float = solver.IntVar(0, 1, 'main_sub_CAST_store_float')
main_sub_CAST_store_double = solver.IntVar(0, 1, 'main_sub_CAST_store_double')
solver.Add( + (1)*main_sub_CAST_store_fixp + (1)*main_sub_CAST_store_float + (1)*main_sub_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub_CAST_store_fixbits + (-10000)*main_sub_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub_CAST_store = solver.IntVar(0, 1, 'C1_main_sub_CAST_store')
C2_main_sub_CAST_store = solver.IntVar(0, 1, 'C2_main_sub_CAST_store')
solver.Add( + (1)*main_sub_fixbits + (-1)*main_sub_CAST_store_fixbits + (-10000)*C1_main_sub_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub_fixbits + (1)*main_sub_CAST_store_fixbits + (-10000)*C2_main_sub_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub_CAST_store
castCostObj +=  + (1)*C2_main_sub_CAST_store
C3_main_sub_CAST_store = solver.IntVar(0, 1, 'C3_main_sub_CAST_store')
C4_main_sub_CAST_store = solver.IntVar(0, 1, 'C4_main_sub_CAST_store')
C5_main_sub_CAST_store = solver.IntVar(0, 1, 'C5_main_sub_CAST_store')
C6_main_sub_CAST_store = solver.IntVar(0, 1, 'C6_main_sub_CAST_store')
C7_main_sub_CAST_store = solver.IntVar(0, 1, 'C7_main_sub_CAST_store')
C8_main_sub_CAST_store = solver.IntVar(0, 1, 'C8_main_sub_CAST_store')
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_store_float + (-1)*C3_main_sub_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub_CAST_store
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_store_fixp + (-1)*C4_main_sub_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub_CAST_store
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_store_double + (-1)*C5_main_sub_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub_CAST_store
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_store_fixp + (-1)*C6_main_sub_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub_CAST_store
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_store_double + (-1)*C7_main_sub_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub_CAST_store
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_store_float + (-1)*C8_main_sub_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub_CAST_store
solver.Add( + (1)*main_data_fixp + (-1)*main_sub_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_data_float + (-1)*main_sub_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_data_double + (-1)*main_sub_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_data_fixbits + (-1)*main_sub_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_data_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_data_enob_storeENOB')
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_sub_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp4 + (-1)*main_data_enob_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 0.000000e+00
ConstantValue__3_fixbits = solver.IntVar(0, 32, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__4_fixbits = solver.IntVar(0, 32, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx76, align 8, !taffo.info !15, !taffo.initweight !23, !taffo.constinfo !29
ConstantValue__4_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__4_CAST_store_fixbits')
ConstantValue__4_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_fixp')
ConstantValue__4_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_float')
ConstantValue__4_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_double')
solver.Add( + (1)*ConstantValue__4_CAST_store_fixp + (1)*ConstantValue__4_CAST_store_float + (1)*ConstantValue__4_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__4_CAST_store_fixbits + (-10000)*ConstantValue__4_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__4_CAST_store')
C2_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__4_CAST_store')
solver.Add( + (1)*ConstantValue__4_fixbits + (-1)*ConstantValue__4_CAST_store_fixbits + (-10000)*C1_ConstantValue__4_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__4_fixbits + (1)*ConstantValue__4_CAST_store_fixbits + (-10000)*C2_ConstantValue__4_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__4_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__4_CAST_store
C3_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_store')
C4_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_store')
C5_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_store')
C6_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_store')
C7_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_store')
C8_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_store')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_float + (-1)*C3_ConstantValue__4_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_fixp + (-1)*C4_ConstantValue__4_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_double + (-1)*C5_ConstantValue__4_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_fixp + (-1)*C6_ConstantValue__4_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_double + (-1)*C7_ConstantValue__4_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_float + (-1)*C8_ConstantValue__4_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__4_CAST_store
solver.Add( + (1)*main_cov_fixp + (-1)*ConstantValue__4_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_float + (-1)*ConstantValue__4_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_cov_double + (-1)*ConstantValue__4_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_cov_fixbits + (-1)*ConstantValue__4_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp5')
solver.Add( + (1)*main_data_enob_memphi_main_tmp5 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp5 + (-1)*main_data_enob_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp6')
solver.Add( + (1)*main_data_enob_memphi_main_tmp6 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
main_main_tmp6_enob_3 = solver.IntVar(0, 1, 'main_main_tmp6_enob_3')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2 + (1)*main_main_tmp6_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp6 + (-1)*main_data_enob_storeENOB + (10000)*main_main_tmp6_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul89 = fmul double %tmp5, %tmp6, !taffo.info !12, !taffo.initweight !24
main_data_CAST_mul89_fixbits = solver.IntVar(0, 17, 'main_data_CAST_mul89_fixbits')
main_data_CAST_mul89_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul89_fixp')
main_data_CAST_mul89_float = solver.IntVar(0, 1, 'main_data_CAST_mul89_float')
main_data_CAST_mul89_double = solver.IntVar(0, 1, 'main_data_CAST_mul89_double')
solver.Add( + (1)*main_data_CAST_mul89_fixp + (1)*main_data_CAST_mul89_float + (1)*main_data_CAST_mul89_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul89_fixbits + (-10000)*main_data_CAST_mul89_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul89')
C2_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul89')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul89_fixbits + (-10000)*C1_main_data_CAST_mul89<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul89_fixbits + (-10000)*C2_main_data_CAST_mul89<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_mul89
castCostObj +=  + (1)*C2_main_data_CAST_mul89
C3_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul89')
C4_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul89')
C5_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul89')
C6_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul89')
C7_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul89')
C8_main_data_CAST_mul89 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul89')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul89_float + (-1)*C3_main_data_CAST_mul89<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_mul89
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul89_fixp + (-1)*C4_main_data_CAST_mul89<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_mul89
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul89_double + (-1)*C5_main_data_CAST_mul89<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_mul89
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul89_fixp + (-1)*C6_main_data_CAST_mul89<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_mul89
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul89_double + (-1)*C7_main_data_CAST_mul89<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_mul89
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul89_float + (-1)*C8_main_data_CAST_mul89<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_mul89



#Constraint for cast for   %mul89 = fmul double %tmp5, %tmp6, !taffo.info !12, !taffo.initweight !24
main_data_CAST_mul89_0_fixbits = solver.IntVar(0, 17, 'main_data_CAST_mul89_0_fixbits')
main_data_CAST_mul89_0_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul89_0_fixp')
main_data_CAST_mul89_0_float = solver.IntVar(0, 1, 'main_data_CAST_mul89_0_float')
main_data_CAST_mul89_0_double = solver.IntVar(0, 1, 'main_data_CAST_mul89_0_double')
solver.Add( + (1)*main_data_CAST_mul89_0_fixp + (1)*main_data_CAST_mul89_0_float + (1)*main_data_CAST_mul89_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul89_0_fixbits + (-10000)*main_data_CAST_mul89_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul89_0')
C2_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul89_0')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul89_0_fixbits + (-10000)*C1_main_data_CAST_mul89_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul89_0_fixbits + (-10000)*C2_main_data_CAST_mul89_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_mul89_0
castCostObj +=  + (1)*C2_main_data_CAST_mul89_0
C3_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul89_0')
C4_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul89_0')
C5_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul89_0')
C6_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul89_0')
C7_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul89_0')
C8_main_data_CAST_mul89_0 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul89_0')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul89_0_float + (-1)*C3_main_data_CAST_mul89_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_mul89_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul89_0_fixp + (-1)*C4_main_data_CAST_mul89_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_mul89_0
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul89_0_double + (-1)*C5_main_data_CAST_mul89_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_mul89_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul89_0_fixp + (-1)*C6_main_data_CAST_mul89_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_mul89_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul89_0_double + (-1)*C7_main_data_CAST_mul89_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_mul89_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul89_0_float + (-1)*C8_main_data_CAST_mul89_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_mul89_0



#Stuff for   %mul89 = fmul double %tmp5, %tmp6, !taffo.info !12, !taffo.initweight !24
main_mul89_fixbits = solver.IntVar(0, 17, 'main_mul89_fixbits')
main_mul89_fixp = solver.IntVar(0, 1, 'main_mul89_fixp')
main_mul89_float = solver.IntVar(0, 1, 'main_mul89_float')
main_mul89_double = solver.IntVar(0, 1, 'main_mul89_double')
main_mul89_enob = solver.IntVar(-10000, 10000, 'main_mul89_enob')
solver.Add( + (1)*main_mul89_enob + (-1)*main_mul89_fixbits + (10000)*main_mul89_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul89_enob + (10000)*main_mul89_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul89_enob + (10000)*main_mul89_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul89_fixbits + (-10000)*main_mul89_fixp>=-9984)    #Limit the lower number of frac bits17
enobCostObj +=  + (-1)*main_mul89_enob
solver.Add( + (1)*main_mul89_fixp + (1)*main_mul89_float + (1)*main_mul89_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul89_fixbits + (-10000)*main_mul89_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_mul89_fixp + (-1)*main_data_CAST_mul89_0_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul89_float + (-1)*main_data_CAST_mul89_0_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul89_double + (-1)*main_data_CAST_mul89_0_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_mul89_fixp + (-1)*main_mul89_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul89_float + (-1)*main_mul89_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul89_double + (-1)*main_mul89_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul89_fixp
mathCostObj +=  + (6)*main_mul89_float
mathCostObj +=  + (12.2551)*main_mul89_double
main_main_mul89_enob_1 = solver.IntVar(0, 1, 'main_main_mul89_enob_1')
main_main_mul89_enob_2 = solver.IntVar(0, 1, 'main_main_mul89_enob_2')
solver.Add( + (1)*main_main_mul89_enob_1 + (1)*main_main_mul89_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul89_enob + (-1)*main_data_enob_memphi_main_tmp6 + (-10000)*main_main_mul89_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul89_enob + (-1)*main_data_enob_memphi_main_tmp5 + (-10000)*main_main_mul89_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_cov_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'main_cov_enob_memphi_main_tmp7')
solver.Add( + (1)*main_cov_enob_memphi_main_tmp7 + (-1)*main_cov_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
solver.Add( + (1)*main_main_tmp7_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add94 = fadd double %tmp7, %mul89, !taffo.info !15, !taffo.initweight !24
main_cov_CAST_add94_fixbits = solver.IntVar(0, 14, 'main_cov_CAST_add94_fixbits')
main_cov_CAST_add94_fixp = solver.IntVar(0, 1, 'main_cov_CAST_add94_fixp')
main_cov_CAST_add94_float = solver.IntVar(0, 1, 'main_cov_CAST_add94_float')
main_cov_CAST_add94_double = solver.IntVar(0, 1, 'main_cov_CAST_add94_double')
solver.Add( + (1)*main_cov_CAST_add94_fixp + (1)*main_cov_CAST_add94_float + (1)*main_cov_CAST_add94_double==1)    #exactly 1 type
solver.Add( + (1)*main_cov_CAST_add94_fixbits + (-10000)*main_cov_CAST_add94_fixp<=0)    #If no fix, fix frac part = 0
C1_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C1_main_cov_CAST_add94')
C2_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C2_main_cov_CAST_add94')
solver.Add( + (1)*main_cov_fixbits + (-1)*main_cov_CAST_add94_fixbits + (-10000)*C1_main_cov_CAST_add94<=0)    #Shift cost 1
solver.Add( + (-1)*main_cov_fixbits + (1)*main_cov_CAST_add94_fixbits + (-10000)*C2_main_cov_CAST_add94<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_cov_CAST_add94
castCostObj +=  + (1)*C2_main_cov_CAST_add94
C3_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C3_main_cov_CAST_add94')
C4_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C4_main_cov_CAST_add94')
C5_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C5_main_cov_CAST_add94')
C6_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C6_main_cov_CAST_add94')
C7_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C7_main_cov_CAST_add94')
C8_main_cov_CAST_add94 = solver.IntVar(0, 1, 'C8_main_cov_CAST_add94')
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_add94_float + (-1)*C3_main_cov_CAST_add94<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_cov_CAST_add94
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_add94_fixp + (-1)*C4_main_cov_CAST_add94<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_cov_CAST_add94
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_add94_double + (-1)*C5_main_cov_CAST_add94<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_cov_CAST_add94
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_add94_fixp + (-1)*C6_main_cov_CAST_add94<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_cov_CAST_add94
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_add94_double + (-1)*C7_main_cov_CAST_add94<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_cov_CAST_add94
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_add94_float + (-1)*C8_main_cov_CAST_add94<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_cov_CAST_add94



#Constraint for cast for   %add94 = fadd double %tmp7, %mul89, !taffo.info !15, !taffo.initweight !24
main_mul89_CAST_add94_fixbits = solver.IntVar(0, 17, 'main_mul89_CAST_add94_fixbits')
main_mul89_CAST_add94_fixp = solver.IntVar(0, 1, 'main_mul89_CAST_add94_fixp')
main_mul89_CAST_add94_float = solver.IntVar(0, 1, 'main_mul89_CAST_add94_float')
main_mul89_CAST_add94_double = solver.IntVar(0, 1, 'main_mul89_CAST_add94_double')
solver.Add( + (1)*main_mul89_CAST_add94_fixp + (1)*main_mul89_CAST_add94_float + (1)*main_mul89_CAST_add94_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul89_CAST_add94_fixbits + (-10000)*main_mul89_CAST_add94_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C1_main_mul89_CAST_add94')
C2_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C2_main_mul89_CAST_add94')
solver.Add( + (1)*main_mul89_fixbits + (-1)*main_mul89_CAST_add94_fixbits + (-10000)*C1_main_mul89_CAST_add94<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul89_fixbits + (1)*main_mul89_CAST_add94_fixbits + (-10000)*C2_main_mul89_CAST_add94<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul89_CAST_add94
castCostObj +=  + (1)*C2_main_mul89_CAST_add94
C3_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C3_main_mul89_CAST_add94')
C4_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C4_main_mul89_CAST_add94')
C5_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C5_main_mul89_CAST_add94')
C6_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C6_main_mul89_CAST_add94')
C7_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C7_main_mul89_CAST_add94')
C8_main_mul89_CAST_add94 = solver.IntVar(0, 1, 'C8_main_mul89_CAST_add94')
solver.Add( + (1)*main_mul89_fixp + (1)*main_mul89_CAST_add94_float + (-1)*C3_main_mul89_CAST_add94<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul89_CAST_add94
solver.Add( + (1)*main_mul89_float + (1)*main_mul89_CAST_add94_fixp + (-1)*C4_main_mul89_CAST_add94<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul89_CAST_add94
solver.Add( + (1)*main_mul89_fixp + (1)*main_mul89_CAST_add94_double + (-1)*C5_main_mul89_CAST_add94<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul89_CAST_add94
solver.Add( + (1)*main_mul89_double + (1)*main_mul89_CAST_add94_fixp + (-1)*C6_main_mul89_CAST_add94<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul89_CAST_add94
solver.Add( + (1)*main_mul89_float + (1)*main_mul89_CAST_add94_double + (-1)*C7_main_mul89_CAST_add94<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul89_CAST_add94
solver.Add( + (1)*main_mul89_double + (1)*main_mul89_CAST_add94_float + (-1)*C8_main_mul89_CAST_add94<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul89_CAST_add94



#Stuff for   %add94 = fadd double %tmp7, %mul89, !taffo.info !15, !taffo.initweight !24
main_add94_fixbits = solver.IntVar(0, 14, 'main_add94_fixbits')
main_add94_fixp = solver.IntVar(0, 1, 'main_add94_fixp')
main_add94_float = solver.IntVar(0, 1, 'main_add94_float')
main_add94_double = solver.IntVar(0, 1, 'main_add94_double')
main_add94_enob = solver.IntVar(-10000, 10000, 'main_add94_enob')
solver.Add( + (1)*main_add94_enob + (-1)*main_add94_fixbits + (10000)*main_add94_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add94_enob + (10000)*main_add94_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add94_enob + (10000)*main_add94_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add94_fixbits + (-10000)*main_add94_fixp>=-9987)    #Limit the lower number of frac bits14
enobCostObj +=  + (-1)*main_add94_enob
solver.Add( + (1)*main_add94_fixp + (1)*main_add94_float + (1)*main_add94_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add94_fixbits + (-10000)*main_add94_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_cov_CAST_add94_fixp + (-1)*main_mul89_CAST_add94_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_CAST_add94_float + (-1)*main_mul89_CAST_add94_float==0)    #float equality
solver.Add( + (1)*main_cov_CAST_add94_double + (-1)*main_mul89_CAST_add94_double==0)    #double equality
solver.Add( + (1)*main_cov_CAST_add94_fixbits + (-1)*main_mul89_CAST_add94_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_cov_CAST_add94_fixp + (-1)*main_add94_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_CAST_add94_float + (-1)*main_add94_float==0)    #float equality
solver.Add( + (1)*main_cov_CAST_add94_double + (-1)*main_add94_double==0)    #double equality
solver.Add( + (1)*main_cov_CAST_add94_fixbits + (-1)*main_add94_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add94_fixp
mathCostObj +=  + (3)*main_add94_float
mathCostObj +=  + (6.64928)*main_add94_double
solver.Add( + (1)*main_add94_enob + (-1)*main_cov_enob_memphi_main_tmp7<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add94_enob + (-1)*main_mul89_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add94, double* %arrayidx93, align 8, !taffo.info !15, !taffo.initweight !23
main_add94_CAST_store_fixbits = solver.IntVar(0, 14, 'main_add94_CAST_store_fixbits')
main_add94_CAST_store_fixp = solver.IntVar(0, 1, 'main_add94_CAST_store_fixp')
main_add94_CAST_store_float = solver.IntVar(0, 1, 'main_add94_CAST_store_float')
main_add94_CAST_store_double = solver.IntVar(0, 1, 'main_add94_CAST_store_double')
solver.Add( + (1)*main_add94_CAST_store_fixp + (1)*main_add94_CAST_store_float + (1)*main_add94_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add94_CAST_store_fixbits + (-10000)*main_add94_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add94_CAST_store = solver.IntVar(0, 1, 'C1_main_add94_CAST_store')
C2_main_add94_CAST_store = solver.IntVar(0, 1, 'C2_main_add94_CAST_store')
solver.Add( + (1)*main_add94_fixbits + (-1)*main_add94_CAST_store_fixbits + (-10000)*C1_main_add94_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add94_fixbits + (1)*main_add94_CAST_store_fixbits + (-10000)*C2_main_add94_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add94_CAST_store
castCostObj +=  + (1)*C2_main_add94_CAST_store
C3_main_add94_CAST_store = solver.IntVar(0, 1, 'C3_main_add94_CAST_store')
C4_main_add94_CAST_store = solver.IntVar(0, 1, 'C4_main_add94_CAST_store')
C5_main_add94_CAST_store = solver.IntVar(0, 1, 'C5_main_add94_CAST_store')
C6_main_add94_CAST_store = solver.IntVar(0, 1, 'C6_main_add94_CAST_store')
C7_main_add94_CAST_store = solver.IntVar(0, 1, 'C7_main_add94_CAST_store')
C8_main_add94_CAST_store = solver.IntVar(0, 1, 'C8_main_add94_CAST_store')
solver.Add( + (1)*main_add94_fixp + (1)*main_add94_CAST_store_float + (-1)*C3_main_add94_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add94_CAST_store
solver.Add( + (1)*main_add94_float + (1)*main_add94_CAST_store_fixp + (-1)*C4_main_add94_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add94_CAST_store
solver.Add( + (1)*main_add94_fixp + (1)*main_add94_CAST_store_double + (-1)*C5_main_add94_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add94_CAST_store
solver.Add( + (1)*main_add94_double + (1)*main_add94_CAST_store_fixp + (-1)*C6_main_add94_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add94_CAST_store
solver.Add( + (1)*main_add94_float + (1)*main_add94_CAST_store_double + (-1)*C7_main_add94_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add94_CAST_store
solver.Add( + (1)*main_add94_double + (1)*main_add94_CAST_store_float + (-1)*C8_main_add94_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add94_CAST_store
solver.Add( + (1)*main_cov_fixp + (-1)*main_add94_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_float + (-1)*main_add94_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_cov_double + (-1)*main_add94_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_cov_fixbits + (-1)*main_add94_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_cov_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_cov_enob_storeENOB')
solver.Add( + (1)*main_cov_enob_storeENOB + (-1)*main_cov_fixbits + (10000)*main_cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_cov_enob_storeENOB + (10000)*main_cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_cov_enob_storeENOB + (10000)*main_cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_cov_enob_storeENOB + (-1)*main_add94_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_cov_enob_memphi_main_tmp7 + (-1)*main_cov_enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_cov_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_cov_enob_memphi_main_tmp8')
solver.Add( + (1)*main_cov_enob_memphi_main_tmp8 + (-1)*main_cov_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
solver.Add( + (1)*main_main_tmp8_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_cov_enob_memphi_main_tmp8 + (-1)*main_cov_enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 9.900000e+01
ConstantValue__5_fixbits = solver.IntVar(0, 25, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 9.900000e+01
ConstantValue__6_fixbits = solver.IntVar(0, 25, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div102 = fdiv double %tmp8, 9.900000e+01, !taffo.info !15, !taffo.initweight !24, !taffo.constinfo !32
main_cov_CAST_div102_fixbits = solver.IntVar(0, 14, 'main_cov_CAST_div102_fixbits')
main_cov_CAST_div102_fixp = solver.IntVar(0, 1, 'main_cov_CAST_div102_fixp')
main_cov_CAST_div102_float = solver.IntVar(0, 1, 'main_cov_CAST_div102_float')
main_cov_CAST_div102_double = solver.IntVar(0, 1, 'main_cov_CAST_div102_double')
solver.Add( + (1)*main_cov_CAST_div102_fixp + (1)*main_cov_CAST_div102_float + (1)*main_cov_CAST_div102_double==1)    #exactly 1 type
solver.Add( + (1)*main_cov_CAST_div102_fixbits + (-10000)*main_cov_CAST_div102_fixp<=0)    #If no fix, fix frac part = 0
C1_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C1_main_cov_CAST_div102')
C2_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C2_main_cov_CAST_div102')
solver.Add( + (1)*main_cov_fixbits + (-1)*main_cov_CAST_div102_fixbits + (-10000)*C1_main_cov_CAST_div102<=0)    #Shift cost 1
solver.Add( + (-1)*main_cov_fixbits + (1)*main_cov_CAST_div102_fixbits + (-10000)*C2_main_cov_CAST_div102<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_cov_CAST_div102
castCostObj +=  + (1)*C2_main_cov_CAST_div102
C3_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C3_main_cov_CAST_div102')
C4_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C4_main_cov_CAST_div102')
C5_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C5_main_cov_CAST_div102')
C6_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C6_main_cov_CAST_div102')
C7_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C7_main_cov_CAST_div102')
C8_main_cov_CAST_div102 = solver.IntVar(0, 1, 'C8_main_cov_CAST_div102')
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_div102_float + (-1)*C3_main_cov_CAST_div102<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_cov_CAST_div102
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_div102_fixp + (-1)*C4_main_cov_CAST_div102<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_cov_CAST_div102
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_div102_double + (-1)*C5_main_cov_CAST_div102<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_cov_CAST_div102
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_div102_fixp + (-1)*C6_main_cov_CAST_div102<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_cov_CAST_div102
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_div102_double + (-1)*C7_main_cov_CAST_div102<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_cov_CAST_div102
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_div102_float + (-1)*C8_main_cov_CAST_div102<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_cov_CAST_div102



#Stuff for double 9.900000e+01
ConstantValue__7_fixbits = solver.IntVar(0, 25, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div102 = fdiv double %tmp8, 9.900000e+01, !taffo.info !15, !taffo.initweight !24, !taffo.constinfo !32
ConstantValue__7_CAST_div102_fixbits = solver.IntVar(0, 25, 'ConstantValue__7_CAST_div102_fixbits')
ConstantValue__7_CAST_div102_fixp = solver.IntVar(0, 1, 'ConstantValue__7_CAST_div102_fixp')
ConstantValue__7_CAST_div102_float = solver.IntVar(0, 1, 'ConstantValue__7_CAST_div102_float')
ConstantValue__7_CAST_div102_double = solver.IntVar(0, 1, 'ConstantValue__7_CAST_div102_double')
solver.Add( + (1)*ConstantValue__7_CAST_div102_fixp + (1)*ConstantValue__7_CAST_div102_float + (1)*ConstantValue__7_CAST_div102_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__7_CAST_div102_fixbits + (-10000)*ConstantValue__7_CAST_div102_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C1_ConstantValue__7_CAST_div102')
C2_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C2_ConstantValue__7_CAST_div102')
solver.Add( + (1)*ConstantValue__7_fixbits + (-1)*ConstantValue__7_CAST_div102_fixbits + (-10000)*C1_ConstantValue__7_CAST_div102<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__7_fixbits + (1)*ConstantValue__7_CAST_div102_fixbits + (-10000)*C2_ConstantValue__7_CAST_div102<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__7_CAST_div102
castCostObj +=  + (1)*C2_ConstantValue__7_CAST_div102
C3_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C3_ConstantValue__7_CAST_div102')
C4_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C4_ConstantValue__7_CAST_div102')
C5_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C5_ConstantValue__7_CAST_div102')
C6_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C6_ConstantValue__7_CAST_div102')
C7_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C7_ConstantValue__7_CAST_div102')
C8_ConstantValue__7_CAST_div102 = solver.IntVar(0, 1, 'C8_ConstantValue__7_CAST_div102')
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_div102_float + (-1)*C3_ConstantValue__7_CAST_div102<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__7_CAST_div102
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_div102_fixp + (-1)*C4_ConstantValue__7_CAST_div102<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__7_CAST_div102
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_div102_double + (-1)*C5_ConstantValue__7_CAST_div102<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__7_CAST_div102
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_div102_fixp + (-1)*C6_ConstantValue__7_CAST_div102<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__7_CAST_div102
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_div102_double + (-1)*C7_ConstantValue__7_CAST_div102<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__7_CAST_div102
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_div102_float + (-1)*C8_ConstantValue__7_CAST_div102<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__7_CAST_div102



#Stuff for   %div102 = fdiv double %tmp8, 9.900000e+01, !taffo.info !15, !taffo.initweight !24, !taffo.constinfo !32
main_div102_fixbits = solver.IntVar(0, 14, 'main_div102_fixbits')
main_div102_fixp = solver.IntVar(0, 1, 'main_div102_fixp')
main_div102_float = solver.IntVar(0, 1, 'main_div102_float')
main_div102_double = solver.IntVar(0, 1, 'main_div102_double')
main_div102_enob = solver.IntVar(-10000, 10000, 'main_div102_enob')
solver.Add( + (1)*main_div102_enob + (-1)*main_div102_fixbits + (10000)*main_div102_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div102_enob + (10000)*main_div102_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div102_enob + (10000)*main_div102_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div102_fixbits + (-10000)*main_div102_fixp>=-9987)    #Limit the lower number of frac bits14
enobCostObj +=  + (-1)*main_div102_enob
solver.Add( + (1)*main_div102_fixp + (1)*main_div102_float + (1)*main_div102_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div102_fixbits + (-10000)*main_div102_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_cov_CAST_div102_fixp + (-1)*ConstantValue__7_CAST_div102_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_CAST_div102_float + (-1)*ConstantValue__7_CAST_div102_float==0)    #float equality
solver.Add( + (1)*main_cov_CAST_div102_double + (-1)*ConstantValue__7_CAST_div102_double==0)    #double equality
solver.Add( + (1)*main_cov_CAST_div102_fixp + (-1)*main_div102_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_CAST_div102_float + (-1)*main_div102_float==0)    #float equality
solver.Add( + (1)*main_cov_CAST_div102_double + (-1)*main_div102_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div102_fixp
mathCostObj +=  + (6)*main_div102_float
mathCostObj +=  + (12)*main_div102_double
main_main_div102_enob_1 = solver.IntVar(0, 1, 'main_main_div102_enob_1')
main_main_div102_enob_2 = solver.IntVar(0, 1, 'main_main_div102_enob_2')
solver.Add( + (1)*main_main_div102_enob_1 + (1)*main_main_div102_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div102_enob + (-1)*ConstantValue__5_enob + (-10000)*main_main_div102_enob_1<=3072)    #Enob: propagation in division 1
solver.Add( + (1)*main_div102_enob + (-1)*main_cov_enob_memphi_main_tmp8 + (-10000)*main_main_div102_enob_2<=3072)    #Enob: propagation in division 2



#Constraint for cast for   store double %div102, double* %arrayidx101, align 8, !taffo.info !15, !taffo.initweight !23
main_div102_CAST_store_fixbits = solver.IntVar(0, 14, 'main_div102_CAST_store_fixbits')
main_div102_CAST_store_fixp = solver.IntVar(0, 1, 'main_div102_CAST_store_fixp')
main_div102_CAST_store_float = solver.IntVar(0, 1, 'main_div102_CAST_store_float')
main_div102_CAST_store_double = solver.IntVar(0, 1, 'main_div102_CAST_store_double')
solver.Add( + (1)*main_div102_CAST_store_fixp + (1)*main_div102_CAST_store_float + (1)*main_div102_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div102_CAST_store_fixbits + (-10000)*main_div102_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div102_CAST_store = solver.IntVar(0, 1, 'C1_main_div102_CAST_store')
C2_main_div102_CAST_store = solver.IntVar(0, 1, 'C2_main_div102_CAST_store')
solver.Add( + (1)*main_div102_fixbits + (-1)*main_div102_CAST_store_fixbits + (-10000)*C1_main_div102_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div102_fixbits + (1)*main_div102_CAST_store_fixbits + (-10000)*C2_main_div102_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div102_CAST_store
castCostObj +=  + (1)*C2_main_div102_CAST_store
C3_main_div102_CAST_store = solver.IntVar(0, 1, 'C3_main_div102_CAST_store')
C4_main_div102_CAST_store = solver.IntVar(0, 1, 'C4_main_div102_CAST_store')
C5_main_div102_CAST_store = solver.IntVar(0, 1, 'C5_main_div102_CAST_store')
C6_main_div102_CAST_store = solver.IntVar(0, 1, 'C6_main_div102_CAST_store')
C7_main_div102_CAST_store = solver.IntVar(0, 1, 'C7_main_div102_CAST_store')
C8_main_div102_CAST_store = solver.IntVar(0, 1, 'C8_main_div102_CAST_store')
solver.Add( + (1)*main_div102_fixp + (1)*main_div102_CAST_store_float + (-1)*C3_main_div102_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div102_CAST_store
solver.Add( + (1)*main_div102_float + (1)*main_div102_CAST_store_fixp + (-1)*C4_main_div102_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div102_CAST_store
solver.Add( + (1)*main_div102_fixp + (1)*main_div102_CAST_store_double + (-1)*C5_main_div102_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div102_CAST_store
solver.Add( + (1)*main_div102_double + (1)*main_div102_CAST_store_fixp + (-1)*C6_main_div102_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div102_CAST_store
solver.Add( + (1)*main_div102_float + (1)*main_div102_CAST_store_double + (-1)*C7_main_div102_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div102_CAST_store
solver.Add( + (1)*main_div102_double + (1)*main_div102_CAST_store_float + (-1)*C8_main_div102_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div102_CAST_store
solver.Add( + (1)*main_cov_fixp + (-1)*main_div102_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_float + (-1)*main_div102_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_cov_double + (-1)*main_div102_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_cov_fixbits + (-1)*main_div102_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_cov_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_cov_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB + (-1)*main_cov_fixbits + (10000)*main_cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB + (10000)*main_cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB + (10000)*main_cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB + (-1)*main_div102_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_cov_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'main_cov_enob_memphi_main_tmp9')
solver.Add( + (1)*main_cov_enob_memphi_main_tmp9 + (-1)*main_cov_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
solver.Add( + (1)*main_main_tmp9_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_cov_enob_memphi_main_tmp9 + (-1)*main_cov_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp9, double* %arrayidx110, align 8, !taffo.info !15, !taffo.initweight !23
main_cov_CAST_store_fixbits = solver.IntVar(0, 14, 'main_cov_CAST_store_fixbits')
main_cov_CAST_store_fixp = solver.IntVar(0, 1, 'main_cov_CAST_store_fixp')
main_cov_CAST_store_float = solver.IntVar(0, 1, 'main_cov_CAST_store_float')
main_cov_CAST_store_double = solver.IntVar(0, 1, 'main_cov_CAST_store_double')
solver.Add( + (1)*main_cov_CAST_store_fixp + (1)*main_cov_CAST_store_float + (1)*main_cov_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_cov_CAST_store_fixbits + (-10000)*main_cov_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_cov_CAST_store = solver.IntVar(0, 1, 'C1_main_cov_CAST_store')
C2_main_cov_CAST_store = solver.IntVar(0, 1, 'C2_main_cov_CAST_store')
solver.Add( + (1)*main_cov_fixbits + (-1)*main_cov_CAST_store_fixbits + (-10000)*C1_main_cov_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_cov_fixbits + (1)*main_cov_CAST_store_fixbits + (-10000)*C2_main_cov_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_cov_CAST_store
castCostObj +=  + (1)*C2_main_cov_CAST_store
C3_main_cov_CAST_store = solver.IntVar(0, 1, 'C3_main_cov_CAST_store')
C4_main_cov_CAST_store = solver.IntVar(0, 1, 'C4_main_cov_CAST_store')
C5_main_cov_CAST_store = solver.IntVar(0, 1, 'C5_main_cov_CAST_store')
C6_main_cov_CAST_store = solver.IntVar(0, 1, 'C6_main_cov_CAST_store')
C7_main_cov_CAST_store = solver.IntVar(0, 1, 'C7_main_cov_CAST_store')
C8_main_cov_CAST_store = solver.IntVar(0, 1, 'C8_main_cov_CAST_store')
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_store_float + (-1)*C3_main_cov_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_cov_CAST_store
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_store_fixp + (-1)*C4_main_cov_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_cov_CAST_store
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_store_double + (-1)*C5_main_cov_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_cov_CAST_store
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_store_fixp + (-1)*C6_main_cov_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_cov_CAST_store
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_store_double + (-1)*C7_main_cov_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_cov_CAST_store
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_store_float + (-1)*C8_main_cov_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_cov_CAST_store
solver.Add( + (1)*main_cov_fixp + (-1)*main_cov_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_cov_float + (-1)*main_cov_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_cov_double + (-1)*main_cov_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_cov_fixbits + (-1)*main_cov_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_cov_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_cov_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB_storeENOB + (-1)*main_cov_fixbits + (10000)*main_cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB_storeENOB + (10000)*main_cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB_storeENOB + (10000)*main_cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_cov_enob_storeENOB_storeENOB_storeENOB + (-1)*main_cov_enob_memphi_main_tmp9<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_cov_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'main_cov_enob_memphi_main_tmp12')
solver.Add( + (1)*main_cov_enob_memphi_main_tmp12 + (-1)*main_cov_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp12_enob_1 = solver.IntVar(0, 1, 'main_main_tmp12_enob_1')
main_main_tmp12_enob_2 = solver.IntVar(0, 1, 'main_main_tmp12_enob_2')
main_main_tmp12_enob_3 = solver.IntVar(0, 1, 'main_main_tmp12_enob_3')
main_main_tmp12_enob_4 = solver.IntVar(0, 1, 'main_main_tmp12_enob_4')
solver.Add( + (1)*main_main_tmp12_enob_1 + (1)*main_main_tmp12_enob_2 + (1)*main_main_tmp12_enob_3 + (1)*main_main_tmp12_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_cov_enob_memphi_main_tmp12 + (-1)*main_data_enob_storeENOB + (10000)*main_main_tmp12_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_cov_enob_memphi_main_tmp12 + (-1)*main_cov_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call133 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp11, i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.6, i32 0, i32 0), double %tmp12), !taffo.info !15, !taffo.initweight !24, !taffo.constinfo !37
main_cov_CAST_call133_fixbits = solver.IntVar(0, 14, 'main_cov_CAST_call133_fixbits')
main_cov_CAST_call133_fixp = solver.IntVar(0, 1, 'main_cov_CAST_call133_fixp')
main_cov_CAST_call133_float = solver.IntVar(0, 1, 'main_cov_CAST_call133_float')
main_cov_CAST_call133_double = solver.IntVar(0, 1, 'main_cov_CAST_call133_double')
solver.Add( + (1)*main_cov_CAST_call133_fixp + (1)*main_cov_CAST_call133_float + (1)*main_cov_CAST_call133_double==1)    #exactly 1 type
solver.Add( + (1)*main_cov_CAST_call133_fixbits + (-10000)*main_cov_CAST_call133_fixp<=0)    #If no fix, fix frac part = 0
C1_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C1_main_cov_CAST_call133')
C2_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C2_main_cov_CAST_call133')
solver.Add( + (1)*main_cov_fixbits + (-1)*main_cov_CAST_call133_fixbits + (-10000)*C1_main_cov_CAST_call133<=0)    #Shift cost 1
solver.Add( + (-1)*main_cov_fixbits + (1)*main_cov_CAST_call133_fixbits + (-10000)*C2_main_cov_CAST_call133<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_cov_CAST_call133
castCostObj +=  + (1)*C2_main_cov_CAST_call133
C3_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C3_main_cov_CAST_call133')
C4_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C4_main_cov_CAST_call133')
C5_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C5_main_cov_CAST_call133')
C6_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C6_main_cov_CAST_call133')
C7_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C7_main_cov_CAST_call133')
C8_main_cov_CAST_call133 = solver.IntVar(0, 1, 'C8_main_cov_CAST_call133')
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_call133_float + (-1)*C3_main_cov_CAST_call133<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_cov_CAST_call133
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_call133_fixp + (-1)*C4_main_cov_CAST_call133<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_cov_CAST_call133
solver.Add( + (1)*main_cov_fixp + (1)*main_cov_CAST_call133_double + (-1)*C5_main_cov_CAST_call133<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_cov_CAST_call133
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_call133_fixp + (-1)*C6_main_cov_CAST_call133<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_cov_CAST_call133
solver.Add( + (1)*main_cov_float + (1)*main_cov_CAST_call133_double + (-1)*C7_main_cov_CAST_call133<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_cov_CAST_call133
solver.Add( + (1)*main_cov_double + (1)*main_cov_CAST_call133_float + (-1)*C8_main_cov_CAST_call133<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_cov_CAST_call133
solver.Add( + (1)*main_cov_CAST_call133_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(50 * castCostObj / 286.591+ 1 * enobCostObj / 8592+ 100 * mathCostObj / 44.2029)

# Model declaration end.