


#Stuff for   %mean = alloca [32 x double], align 16, !taffo.info !11, !taffo.initweight !14
main_mean_fixbits = solver.IntVar(0, 15, 'main_mean_fixbits')
main_mean_fixp = solver.IntVar(0, 1, 'main_mean_fixp')
main_mean_float = solver.IntVar(0, 1, 'main_mean_float')
main_mean_double = solver.IntVar(0, 1, 'main_mean_double')
main_mean_enob = solver.IntVar(-10000, 10000, 'main_mean_enob')
solver.Add( + (1)*main_mean_enob + (-1)*main_mean_fixbits + (10000)*main_mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mean_enob + (10000)*main_mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mean_enob + (10000)*main_mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mean_fixbits + (-10000)*main_mean_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_mean_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mean_double<=0)    #Disable double data type
enobCostObj =  + (-1)*main_mean_enob
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_float + (1)*main_mean_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mean_fixbits + (-10000)*main_mean_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %data = alloca [28 x [32 x double]], align 16, !taffo.info !15, !taffo.initweight !14
main_data_fixbits = solver.IntVar(0, 27, 'main_data_fixbits')
main_data_fixp = solver.IntVar(0, 1, 'main_data_fixp')
main_data_float = solver.IntVar(0, 1, 'main_data_float')
main_data_double = solver.IntVar(0, 1, 'main_data_double')
main_data_enob = solver.IntVar(-10000, 10000, 'main_data_enob')
solver.Add( + (1)*main_data_enob + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_fixbits + (-10000)*main_data_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_data_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_data_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_data_enob
solver.Add( + (1)*main_data_fixp + (1)*main_data_float + (1)*main_data_double==1)    #Exactly one selected type
solver.Add( + (1)*main_data_fixbits + (-10000)*main_data_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %corr = alloca [32 x [32 x double]], align 16, !taffo.info !17, !taffo.initweight !14
main_corr_fixbits = solver.IntVar(0, 29, 'main_corr_fixbits')
main_corr_fixp = solver.IntVar(0, 1, 'main_corr_fixp')
main_corr_float = solver.IntVar(0, 1, 'main_corr_float')
main_corr_double = solver.IntVar(0, 1, 'main_corr_double')
main_corr_enob = solver.IntVar(-10000, 10000, 'main_corr_enob')
solver.Add( + (1)*main_corr_enob + (-1)*main_corr_fixbits + (10000)*main_corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_corr_enob + (10000)*main_corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_corr_enob + (10000)*main_corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_corr_fixbits + (-10000)*main_corr_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_corr_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_corr_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_corr_enob
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_float + (1)*main_corr_double==1)    #Exactly one selected type
solver.Add( + (1)*main_corr_fixbits + (-10000)*main_corr_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %stddev = alloca [32 x double], align 16, !taffo.info !19, !taffo.initweight !14
main_stddev_fixbits = solver.IntVar(0, 18, 'main_stddev_fixbits')
main_stddev_fixp = solver.IntVar(0, 1, 'main_stddev_fixp')
main_stddev_float = solver.IntVar(0, 1, 'main_stddev_float')
main_stddev_double = solver.IntVar(0, 1, 'main_stddev_double')
main_stddev_enob = solver.IntVar(-10000, 10000, 'main_stddev_enob')
solver.Add( + (1)*main_stddev_enob + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_fixbits + (-10000)*main_stddev_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_stddev_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_stddev_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_stddev_enob
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_float + (1)*main_stddev_double==1)    #Exactly one selected type
solver.Add( + (1)*main_stddev_fixbits + (-10000)*main_stddev_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 3.200000e+01
ConstantValue__fixbits = solver.IntVar(0, 26, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 3.200000e+01
ConstantValue__0_fixbits = solver.IntVar(0, 26, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__0_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.800000e+01
ConstantValue__1_fixbits = solver.IntVar(0, 27, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__1_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.800000e+01
ConstantValue__2_fixbits = solver.IntVar(0, 27, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__2_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



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
solver.Add( + (1)*ConstantValue__3_double<=0)    #Disable double data type
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
solver.Add( + (1)*ConstantValue__4_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.info !11, !taffo.initweight !24, !taffo.constinfo !36
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
castCostObj =  + (1)*C1_ConstantValue__4_CAST_store
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
solver.Add( + (1)*main_mean_fixp + (-1)*ConstantValue__4_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_float + (-1)*ConstantValue__4_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_mean_double + (-1)*ConstantValue__4_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_mean_fixbits + (-1)*ConstantValue__4_CAST_store_fixbits==0)    #same fractional bit

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



#Constraint for cast for   %add36 = fadd double %tmp1, %tmp, !taffo.info !11, !taffo.initweight !25
main_mean_CAST_add36_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_add36_fixbits')
main_mean_CAST_add36_fixp = solver.IntVar(0, 1, 'main_mean_CAST_add36_fixp')
main_mean_CAST_add36_float = solver.IntVar(0, 1, 'main_mean_CAST_add36_float')
main_mean_CAST_add36_double = solver.IntVar(0, 1, 'main_mean_CAST_add36_double')
solver.Add( + (1)*main_mean_CAST_add36_fixp + (1)*main_mean_CAST_add36_float + (1)*main_mean_CAST_add36_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_add36_fixbits + (-10000)*main_mean_CAST_add36_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C1_main_mean_CAST_add36')
C2_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C2_main_mean_CAST_add36')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_add36_fixbits + (-10000)*C1_main_mean_CAST_add36<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_add36_fixbits + (-10000)*C2_main_mean_CAST_add36<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mean_CAST_add36
castCostObj +=  + (1)*C2_main_mean_CAST_add36
C3_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C3_main_mean_CAST_add36')
C4_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C4_main_mean_CAST_add36')
C5_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C5_main_mean_CAST_add36')
C6_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C6_main_mean_CAST_add36')
C7_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C7_main_mean_CAST_add36')
C8_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C8_main_mean_CAST_add36')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_add36_float + (-1)*C3_main_mean_CAST_add36<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mean_CAST_add36
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_add36_fixp + (-1)*C4_main_mean_CAST_add36<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mean_CAST_add36
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_add36_double + (-1)*C5_main_mean_CAST_add36<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mean_CAST_add36
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_add36_fixp + (-1)*C6_main_mean_CAST_add36<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mean_CAST_add36
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_add36_double + (-1)*C7_main_mean_CAST_add36<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mean_CAST_add36
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_add36_float + (-1)*C8_main_mean_CAST_add36<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mean_CAST_add36



#Constraint for cast for   %add36 = fadd double %tmp1, %tmp, !taffo.info !11, !taffo.initweight !25
main_data_CAST_add36_fixbits = solver.IntVar(0, 27, 'main_data_CAST_add36_fixbits')
main_data_CAST_add36_fixp = solver.IntVar(0, 1, 'main_data_CAST_add36_fixp')
main_data_CAST_add36_float = solver.IntVar(0, 1, 'main_data_CAST_add36_float')
main_data_CAST_add36_double = solver.IntVar(0, 1, 'main_data_CAST_add36_double')
solver.Add( + (1)*main_data_CAST_add36_fixp + (1)*main_data_CAST_add36_float + (1)*main_data_CAST_add36_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_add36_fixbits + (-10000)*main_data_CAST_add36_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_add36 = solver.IntVar(0, 1, 'C1_main_data_CAST_add36')
C2_main_data_CAST_add36 = solver.IntVar(0, 1, 'C2_main_data_CAST_add36')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_add36_fixbits + (-10000)*C1_main_data_CAST_add36<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_add36_fixbits + (-10000)*C2_main_data_CAST_add36<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_add36
castCostObj +=  + (1)*C2_main_data_CAST_add36
C3_main_data_CAST_add36 = solver.IntVar(0, 1, 'C3_main_data_CAST_add36')
C4_main_data_CAST_add36 = solver.IntVar(0, 1, 'C4_main_data_CAST_add36')
C5_main_data_CAST_add36 = solver.IntVar(0, 1, 'C5_main_data_CAST_add36')
C6_main_data_CAST_add36 = solver.IntVar(0, 1, 'C6_main_data_CAST_add36')
C7_main_data_CAST_add36 = solver.IntVar(0, 1, 'C7_main_data_CAST_add36')
C8_main_data_CAST_add36 = solver.IntVar(0, 1, 'C8_main_data_CAST_add36')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_add36_float + (-1)*C3_main_data_CAST_add36<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_add36
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_add36_fixp + (-1)*C4_main_data_CAST_add36<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_add36
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_add36_double + (-1)*C5_main_data_CAST_add36<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_add36
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_add36_fixp + (-1)*C6_main_data_CAST_add36<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_add36
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_add36_double + (-1)*C7_main_data_CAST_add36<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_add36
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_add36_float + (-1)*C8_main_data_CAST_add36<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_add36



#Stuff for   %add36 = fadd double %tmp1, %tmp, !taffo.info !11, !taffo.initweight !25
main_add36_fixbits = solver.IntVar(0, 15, 'main_add36_fixbits')
main_add36_fixp = solver.IntVar(0, 1, 'main_add36_fixp')
main_add36_float = solver.IntVar(0, 1, 'main_add36_float')
main_add36_double = solver.IntVar(0, 1, 'main_add36_double')
main_add36_enob = solver.IntVar(-10000, 10000, 'main_add36_enob')
solver.Add( + (1)*main_add36_enob + (-1)*main_add36_fixbits + (10000)*main_add36_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add36_enob + (10000)*main_add36_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add36_enob + (10000)*main_add36_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add36_fixbits + (-10000)*main_add36_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add36_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add36_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add36_enob
solver.Add( + (1)*main_add36_fixp + (1)*main_add36_float + (1)*main_add36_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add36_fixbits + (-10000)*main_add36_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mean_CAST_add36_fixp + (-1)*main_data_CAST_add36_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_add36_float + (-1)*main_data_CAST_add36_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_add36_double + (-1)*main_data_CAST_add36_double==0)    #double equality
solver.Add( + (1)*main_mean_CAST_add36_fixbits + (-1)*main_data_CAST_add36_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mean_CAST_add36_fixp + (-1)*main_add36_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_add36_float + (-1)*main_add36_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_add36_double + (-1)*main_add36_double==0)    #double equality
solver.Add( + (1)*main_mean_CAST_add36_fixbits + (-1)*main_add36_fixbits==0)    #same fractional bit
mathCostObj =  + (1.27246)*main_add36_fixp
mathCostObj +=  + (3)*main_add36_float
mathCostObj +=  + (6.64928)*main_add36_double
solver.Add( + (1)*main_add36_enob + (-1)*main_mean_enob_memphi_main_tmp1<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add36_enob + (-1)*main_data_enob_memphi_main_tmp<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add36, double* %arrayidx35, align 8, !taffo.info !11, !taffo.initweight !24
main_add36_CAST_store_fixbits = solver.IntVar(0, 15, 'main_add36_CAST_store_fixbits')
main_add36_CAST_store_fixp = solver.IntVar(0, 1, 'main_add36_CAST_store_fixp')
main_add36_CAST_store_float = solver.IntVar(0, 1, 'main_add36_CAST_store_float')
main_add36_CAST_store_double = solver.IntVar(0, 1, 'main_add36_CAST_store_double')
solver.Add( + (1)*main_add36_CAST_store_fixp + (1)*main_add36_CAST_store_float + (1)*main_add36_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add36_CAST_store_fixbits + (-10000)*main_add36_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add36_CAST_store = solver.IntVar(0, 1, 'C1_main_add36_CAST_store')
C2_main_add36_CAST_store = solver.IntVar(0, 1, 'C2_main_add36_CAST_store')
solver.Add( + (1)*main_add36_fixbits + (-1)*main_add36_CAST_store_fixbits + (-10000)*C1_main_add36_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add36_fixbits + (1)*main_add36_CAST_store_fixbits + (-10000)*C2_main_add36_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add36_CAST_store
castCostObj +=  + (1)*C2_main_add36_CAST_store
C3_main_add36_CAST_store = solver.IntVar(0, 1, 'C3_main_add36_CAST_store')
C4_main_add36_CAST_store = solver.IntVar(0, 1, 'C4_main_add36_CAST_store')
C5_main_add36_CAST_store = solver.IntVar(0, 1, 'C5_main_add36_CAST_store')
C6_main_add36_CAST_store = solver.IntVar(0, 1, 'C6_main_add36_CAST_store')
C7_main_add36_CAST_store = solver.IntVar(0, 1, 'C7_main_add36_CAST_store')
C8_main_add36_CAST_store = solver.IntVar(0, 1, 'C8_main_add36_CAST_store')
solver.Add( + (1)*main_add36_fixp + (1)*main_add36_CAST_store_float + (-1)*C3_main_add36_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add36_CAST_store
solver.Add( + (1)*main_add36_float + (1)*main_add36_CAST_store_fixp + (-1)*C4_main_add36_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add36_CAST_store
solver.Add( + (1)*main_add36_fixp + (1)*main_add36_CAST_store_double + (-1)*C5_main_add36_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add36_CAST_store
solver.Add( + (1)*main_add36_double + (1)*main_add36_CAST_store_fixp + (-1)*C6_main_add36_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add36_CAST_store
solver.Add( + (1)*main_add36_float + (1)*main_add36_CAST_store_double + (-1)*C7_main_add36_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add36_CAST_store
solver.Add( + (1)*main_add36_double + (1)*main_add36_CAST_store_float + (-1)*C8_main_add36_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add36_CAST_store
solver.Add( + (1)*main_mean_fixp + (-1)*main_add36_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_float + (-1)*main_add36_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_mean_double + (-1)*main_add36_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_mean_fixbits + (-1)*main_add36_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_mean_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_mean_enob_storeENOB')
solver.Add( + (1)*main_mean_enob_storeENOB + (-1)*main_mean_fixbits + (10000)*main_mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mean_enob_storeENOB + (10000)*main_mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mean_enob_storeENOB + (10000)*main_mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mean_enob_storeENOB + (-1)*main_add36_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp1 + (-1)*main_mean_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp2')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp2 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
solver.Add( + (1)*main_main_tmp2_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp2 + (-1)*main_mean_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.800000e+01
ConstantValue__5_fixbits = solver.IntVar(0, 27, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__5_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.800000e+01
ConstantValue__6_fixbits = solver.IntVar(0, 27, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__6_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div42 = fdiv double %tmp2, 2.800000e+01, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !32
main_mean_CAST_div42_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_div42_fixbits')
main_mean_CAST_div42_fixp = solver.IntVar(0, 1, 'main_mean_CAST_div42_fixp')
main_mean_CAST_div42_float = solver.IntVar(0, 1, 'main_mean_CAST_div42_float')
main_mean_CAST_div42_double = solver.IntVar(0, 1, 'main_mean_CAST_div42_double')
solver.Add( + (1)*main_mean_CAST_div42_fixp + (1)*main_mean_CAST_div42_float + (1)*main_mean_CAST_div42_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_div42_fixbits + (-10000)*main_mean_CAST_div42_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C1_main_mean_CAST_div42')
C2_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C2_main_mean_CAST_div42')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_div42_fixbits + (-10000)*C1_main_mean_CAST_div42<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_div42_fixbits + (-10000)*C2_main_mean_CAST_div42<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mean_CAST_div42
castCostObj +=  + (1)*C2_main_mean_CAST_div42
C3_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C3_main_mean_CAST_div42')
C4_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C4_main_mean_CAST_div42')
C5_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C5_main_mean_CAST_div42')
C6_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C6_main_mean_CAST_div42')
C7_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C7_main_mean_CAST_div42')
C8_main_mean_CAST_div42 = solver.IntVar(0, 1, 'C8_main_mean_CAST_div42')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_div42_float + (-1)*C3_main_mean_CAST_div42<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mean_CAST_div42
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_div42_fixp + (-1)*C4_main_mean_CAST_div42<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mean_CAST_div42
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_div42_double + (-1)*C5_main_mean_CAST_div42<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mean_CAST_div42
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_div42_fixp + (-1)*C6_main_mean_CAST_div42<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mean_CAST_div42
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_div42_double + (-1)*C7_main_mean_CAST_div42<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mean_CAST_div42
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_div42_float + (-1)*C8_main_mean_CAST_div42<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mean_CAST_div42



#Stuff for double 2.800000e+01
ConstantValue__7_fixbits = solver.IntVar(0, 27, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__7_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div42 = fdiv double %tmp2, 2.800000e+01, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !32
ConstantValue__7_CAST_div42_fixbits = solver.IntVar(0, 27, 'ConstantValue__7_CAST_div42_fixbits')
ConstantValue__7_CAST_div42_fixp = solver.IntVar(0, 1, 'ConstantValue__7_CAST_div42_fixp')
ConstantValue__7_CAST_div42_float = solver.IntVar(0, 1, 'ConstantValue__7_CAST_div42_float')
ConstantValue__7_CAST_div42_double = solver.IntVar(0, 1, 'ConstantValue__7_CAST_div42_double')
solver.Add( + (1)*ConstantValue__7_CAST_div42_fixp + (1)*ConstantValue__7_CAST_div42_float + (1)*ConstantValue__7_CAST_div42_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__7_CAST_div42_fixbits + (-10000)*ConstantValue__7_CAST_div42_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C1_ConstantValue__7_CAST_div42')
C2_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C2_ConstantValue__7_CAST_div42')
solver.Add( + (1)*ConstantValue__7_fixbits + (-1)*ConstantValue__7_CAST_div42_fixbits + (-10000)*C1_ConstantValue__7_CAST_div42<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__7_fixbits + (1)*ConstantValue__7_CAST_div42_fixbits + (-10000)*C2_ConstantValue__7_CAST_div42<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__7_CAST_div42
castCostObj +=  + (1)*C2_ConstantValue__7_CAST_div42
C3_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C3_ConstantValue__7_CAST_div42')
C4_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C4_ConstantValue__7_CAST_div42')
C5_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C5_ConstantValue__7_CAST_div42')
C6_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C6_ConstantValue__7_CAST_div42')
C7_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C7_ConstantValue__7_CAST_div42')
C8_ConstantValue__7_CAST_div42 = solver.IntVar(0, 1, 'C8_ConstantValue__7_CAST_div42')
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_div42_float + (-1)*C3_ConstantValue__7_CAST_div42<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__7_CAST_div42
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_div42_fixp + (-1)*C4_ConstantValue__7_CAST_div42<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__7_CAST_div42
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_div42_double + (-1)*C5_ConstantValue__7_CAST_div42<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__7_CAST_div42
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_div42_fixp + (-1)*C6_ConstantValue__7_CAST_div42<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__7_CAST_div42
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_div42_double + (-1)*C7_ConstantValue__7_CAST_div42<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__7_CAST_div42
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_div42_float + (-1)*C8_ConstantValue__7_CAST_div42<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__7_CAST_div42



#Stuff for   %div42 = fdiv double %tmp2, 2.800000e+01, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !32
main_div42_fixbits = solver.IntVar(0, 20, 'main_div42_fixbits')
main_div42_fixp = solver.IntVar(0, 1, 'main_div42_fixp')
main_div42_float = solver.IntVar(0, 1, 'main_div42_float')
main_div42_double = solver.IntVar(0, 1, 'main_div42_double')
main_div42_enob = solver.IntVar(-10000, 10000, 'main_div42_enob')
solver.Add( + (1)*main_div42_enob + (-1)*main_div42_fixbits + (10000)*main_div42_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div42_enob + (10000)*main_div42_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_div42_enob + (10000)*main_div42_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_div42_fixbits + (-10000)*main_div42_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_div42_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_div42_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div42_enob
solver.Add( + (1)*main_div42_fixp + (1)*main_div42_float + (1)*main_div42_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div42_fixbits + (-10000)*main_div42_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mean_CAST_div42_fixp + (-1)*ConstantValue__7_CAST_div42_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_div42_float + (-1)*ConstantValue__7_CAST_div42_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_div42_double + (-1)*ConstantValue__7_CAST_div42_double==0)    #double equality
solver.Add( + (1)*main_mean_CAST_div42_fixp + (-1)*main_div42_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_div42_float + (-1)*main_div42_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_div42_double + (-1)*main_div42_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div42_fixp
mathCostObj +=  + (6)*main_div42_float
mathCostObj +=  + (12)*main_div42_double
main_main_div42_enob_1 = solver.IntVar(0, 1, 'main_main_div42_enob_1')
main_main_div42_enob_2 = solver.IntVar(0, 1, 'main_main_div42_enob_2')
solver.Add( + (1)*main_main_div42_enob_1 + (1)*main_main_div42_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div42_enob + (-1)*ConstantValue__5_enob + (-10000)*main_main_div42_enob_1<=3072)    #Enob: propagation in division 1
solver.Add( + (1)*main_div42_enob + (-1)*main_mean_enob_memphi_main_tmp2 + (-10000)*main_main_div42_enob_2<=3072)    #Enob: propagation in division 2



#Constraint for cast for   store double %div42, double* %arrayidx41, align 8, !taffo.info !11, !taffo.initweight !24
main_div42_CAST_store_fixbits = solver.IntVar(0, 20, 'main_div42_CAST_store_fixbits')
main_div42_CAST_store_fixp = solver.IntVar(0, 1, 'main_div42_CAST_store_fixp')
main_div42_CAST_store_float = solver.IntVar(0, 1, 'main_div42_CAST_store_float')
main_div42_CAST_store_double = solver.IntVar(0, 1, 'main_div42_CAST_store_double')
solver.Add( + (1)*main_div42_CAST_store_fixp + (1)*main_div42_CAST_store_float + (1)*main_div42_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div42_CAST_store_fixbits + (-10000)*main_div42_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div42_CAST_store = solver.IntVar(0, 1, 'C1_main_div42_CAST_store')
C2_main_div42_CAST_store = solver.IntVar(0, 1, 'C2_main_div42_CAST_store')
solver.Add( + (1)*main_div42_fixbits + (-1)*main_div42_CAST_store_fixbits + (-10000)*C1_main_div42_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div42_fixbits + (1)*main_div42_CAST_store_fixbits + (-10000)*C2_main_div42_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div42_CAST_store
castCostObj +=  + (1)*C2_main_div42_CAST_store
C3_main_div42_CAST_store = solver.IntVar(0, 1, 'C3_main_div42_CAST_store')
C4_main_div42_CAST_store = solver.IntVar(0, 1, 'C4_main_div42_CAST_store')
C5_main_div42_CAST_store = solver.IntVar(0, 1, 'C5_main_div42_CAST_store')
C6_main_div42_CAST_store = solver.IntVar(0, 1, 'C6_main_div42_CAST_store')
C7_main_div42_CAST_store = solver.IntVar(0, 1, 'C7_main_div42_CAST_store')
C8_main_div42_CAST_store = solver.IntVar(0, 1, 'C8_main_div42_CAST_store')
solver.Add( + (1)*main_div42_fixp + (1)*main_div42_CAST_store_float + (-1)*C3_main_div42_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div42_CAST_store
solver.Add( + (1)*main_div42_float + (1)*main_div42_CAST_store_fixp + (-1)*C4_main_div42_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div42_CAST_store
solver.Add( + (1)*main_div42_fixp + (1)*main_div42_CAST_store_double + (-1)*C5_main_div42_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div42_CAST_store
solver.Add( + (1)*main_div42_double + (1)*main_div42_CAST_store_fixp + (-1)*C6_main_div42_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div42_CAST_store
solver.Add( + (1)*main_div42_float + (1)*main_div42_CAST_store_double + (-1)*C7_main_div42_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div42_CAST_store
solver.Add( + (1)*main_div42_double + (1)*main_div42_CAST_store_float + (-1)*C8_main_div42_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div42_CAST_store
solver.Add( + (1)*main_mean_fixp + (-1)*main_div42_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_float + (-1)*main_div42_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_mean_double + (-1)*main_div42_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_mean_fixbits + (-1)*main_div42_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_mean_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_mean_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (-1)*main_mean_fixbits + (10000)*main_mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (-1)*main_div42_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for double 0.000000e+00
ConstantValue__8_fixbits = solver.IntVar(0, 32, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__8_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__9_fixbits = solver.IntVar(0, 32, 'ConstantValue__9_fixbits')
ConstantValue__9_fixp = solver.IntVar(0, 1, 'ConstantValue__9_fixp')
ConstantValue__9_float = solver.IntVar(0, 1, 'ConstantValue__9_float')
ConstantValue__9_double = solver.IntVar(0, 1, 'ConstantValue__9_double')
ConstantValue__9_enob = solver.IntVar(-10000, 10000, 'ConstantValue__9_enob')
solver.Add( + (1)*ConstantValue__9_enob + (-1)*ConstantValue__9_fixbits + (10000)*ConstantValue__9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__9_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_float + (1)*ConstantValue__9_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx51, align 8, !taffo.info !19, !taffo.initweight !24, !taffo.constinfo !36
ConstantValue__9_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__9_CAST_store_fixbits')
ConstantValue__9_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__9_CAST_store_fixp')
ConstantValue__9_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__9_CAST_store_float')
ConstantValue__9_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__9_CAST_store_double')
solver.Add( + (1)*ConstantValue__9_CAST_store_fixp + (1)*ConstantValue__9_CAST_store_float + (1)*ConstantValue__9_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__9_CAST_store_fixbits + (-10000)*ConstantValue__9_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__9_CAST_store')
C2_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__9_CAST_store')
solver.Add( + (1)*ConstantValue__9_fixbits + (-1)*ConstantValue__9_CAST_store_fixbits + (-10000)*C1_ConstantValue__9_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__9_fixbits + (1)*ConstantValue__9_CAST_store_fixbits + (-10000)*C2_ConstantValue__9_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__9_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__9_CAST_store
C3_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__9_CAST_store')
C4_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__9_CAST_store')
C5_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__9_CAST_store')
C6_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__9_CAST_store')
C7_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__9_CAST_store')
C8_ConstantValue__9_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__9_CAST_store')
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_CAST_store_float + (-1)*C3_ConstantValue__9_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__9_CAST_store
solver.Add( + (1)*ConstantValue__9_float + (1)*ConstantValue__9_CAST_store_fixp + (-1)*C4_ConstantValue__9_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__9_CAST_store
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_CAST_store_double + (-1)*C5_ConstantValue__9_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__9_CAST_store
solver.Add( + (1)*ConstantValue__9_double + (1)*ConstantValue__9_CAST_store_fixp + (-1)*C6_ConstantValue__9_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__9_CAST_store
solver.Add( + (1)*ConstantValue__9_float + (1)*ConstantValue__9_CAST_store_double + (-1)*C7_ConstantValue__9_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__9_CAST_store
solver.Add( + (1)*ConstantValue__9_double + (1)*ConstantValue__9_CAST_store_float + (-1)*C8_ConstantValue__9_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__9_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*ConstantValue__9_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*ConstantValue__9_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*ConstantValue__9_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*ConstantValue__9_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp3')
solver.Add( + (1)*main_data_enob_memphi_main_tmp3 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
solver.Add( + (1)*main_main_tmp3_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp4')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp4 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp4 + (-1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub = fsub double %tmp3, %tmp4, !taffo.info !11, !taffo.initweight !25
main_data_CAST_sub_fixbits = solver.IntVar(0, 27, 'main_data_CAST_sub_fixbits')
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



#Constraint for cast for   %sub = fsub double %tmp3, %tmp4, !taffo.info !11, !taffo.initweight !25
main_mean_CAST_sub_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_sub_fixbits')
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



#Stuff for   %sub = fsub double %tmp3, %tmp4, !taffo.info !11, !taffo.initweight !25
main_sub_fixbits = solver.IntVar(0, 15, 'main_sub_fixbits')
main_sub_fixp = solver.IntVar(0, 1, 'main_sub_fixp')
main_sub_float = solver.IntVar(0, 1, 'main_sub_float')
main_sub_double = solver.IntVar(0, 1, 'main_sub_double')
main_sub_enob = solver.IntVar(-10000, 10000, 'main_sub_enob')
solver.Add( + (1)*main_sub_enob + (-1)*main_sub_fixbits + (10000)*main_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_sub_double<=0)    #Disable double data type
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
solver.Add( + (1)*main_sub_enob + (-1)*main_data_enob_memphi_main_tmp3<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub_enob + (-1)*main_mean_enob_memphi_main_tmp4<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp5')
solver.Add( + (1)*main_data_enob_memphi_main_tmp5 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
solver.Add( + (1)*main_main_tmp5_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp6')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp6 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp6 + (-1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub68 = fsub double %tmp5, %tmp6, !taffo.info !11, !taffo.initweight !25
main_data_CAST_sub68_fixbits = solver.IntVar(0, 27, 'main_data_CAST_sub68_fixbits')
main_data_CAST_sub68_fixp = solver.IntVar(0, 1, 'main_data_CAST_sub68_fixp')
main_data_CAST_sub68_float = solver.IntVar(0, 1, 'main_data_CAST_sub68_float')
main_data_CAST_sub68_double = solver.IntVar(0, 1, 'main_data_CAST_sub68_double')
solver.Add( + (1)*main_data_CAST_sub68_fixp + (1)*main_data_CAST_sub68_float + (1)*main_data_CAST_sub68_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_sub68_fixbits + (-10000)*main_data_CAST_sub68_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C1_main_data_CAST_sub68')
C2_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C2_main_data_CAST_sub68')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_sub68_fixbits + (-10000)*C1_main_data_CAST_sub68<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_sub68_fixbits + (-10000)*C2_main_data_CAST_sub68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_sub68
castCostObj +=  + (1)*C2_main_data_CAST_sub68
C3_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C3_main_data_CAST_sub68')
C4_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C4_main_data_CAST_sub68')
C5_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C5_main_data_CAST_sub68')
C6_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C6_main_data_CAST_sub68')
C7_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C7_main_data_CAST_sub68')
C8_main_data_CAST_sub68 = solver.IntVar(0, 1, 'C8_main_data_CAST_sub68')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub68_float + (-1)*C3_main_data_CAST_sub68<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_sub68
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub68_fixp + (-1)*C4_main_data_CAST_sub68<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_sub68
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub68_double + (-1)*C5_main_data_CAST_sub68<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_sub68
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub68_fixp + (-1)*C6_main_data_CAST_sub68<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_sub68
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub68_double + (-1)*C7_main_data_CAST_sub68<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_sub68
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub68_float + (-1)*C8_main_data_CAST_sub68<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_sub68



#Constraint for cast for   %sub68 = fsub double %tmp5, %tmp6, !taffo.info !11, !taffo.initweight !25
main_mean_CAST_sub68_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_sub68_fixbits')
main_mean_CAST_sub68_fixp = solver.IntVar(0, 1, 'main_mean_CAST_sub68_fixp')
main_mean_CAST_sub68_float = solver.IntVar(0, 1, 'main_mean_CAST_sub68_float')
main_mean_CAST_sub68_double = solver.IntVar(0, 1, 'main_mean_CAST_sub68_double')
solver.Add( + (1)*main_mean_CAST_sub68_fixp + (1)*main_mean_CAST_sub68_float + (1)*main_mean_CAST_sub68_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_sub68_fixbits + (-10000)*main_mean_CAST_sub68_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C1_main_mean_CAST_sub68')
C2_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C2_main_mean_CAST_sub68')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_sub68_fixbits + (-10000)*C1_main_mean_CAST_sub68<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_sub68_fixbits + (-10000)*C2_main_mean_CAST_sub68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mean_CAST_sub68
castCostObj +=  + (1)*C2_main_mean_CAST_sub68
C3_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C3_main_mean_CAST_sub68')
C4_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C4_main_mean_CAST_sub68')
C5_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C5_main_mean_CAST_sub68')
C6_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C6_main_mean_CAST_sub68')
C7_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C7_main_mean_CAST_sub68')
C8_main_mean_CAST_sub68 = solver.IntVar(0, 1, 'C8_main_mean_CAST_sub68')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub68_float + (-1)*C3_main_mean_CAST_sub68<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mean_CAST_sub68
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub68_fixp + (-1)*C4_main_mean_CAST_sub68<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mean_CAST_sub68
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub68_double + (-1)*C5_main_mean_CAST_sub68<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mean_CAST_sub68
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub68_fixp + (-1)*C6_main_mean_CAST_sub68<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mean_CAST_sub68
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub68_double + (-1)*C7_main_mean_CAST_sub68<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mean_CAST_sub68
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub68_float + (-1)*C8_main_mean_CAST_sub68<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mean_CAST_sub68



#Stuff for   %sub68 = fsub double %tmp5, %tmp6, !taffo.info !11, !taffo.initweight !25
main_sub68_fixbits = solver.IntVar(0, 15, 'main_sub68_fixbits')
main_sub68_fixp = solver.IntVar(0, 1, 'main_sub68_fixp')
main_sub68_float = solver.IntVar(0, 1, 'main_sub68_float')
main_sub68_double = solver.IntVar(0, 1, 'main_sub68_double')
main_sub68_enob = solver.IntVar(-10000, 10000, 'main_sub68_enob')
solver.Add( + (1)*main_sub68_enob + (-1)*main_sub68_fixbits + (10000)*main_sub68_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub68_enob + (10000)*main_sub68_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub68_enob + (10000)*main_sub68_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub68_fixbits + (-10000)*main_sub68_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub68_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_sub68_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub68_enob
solver.Add( + (1)*main_sub68_fixp + (1)*main_sub68_float + (1)*main_sub68_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub68_fixbits + (-10000)*main_sub68_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_sub68_fixp + (-1)*main_mean_CAST_sub68_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub68_float + (-1)*main_mean_CAST_sub68_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub68_double + (-1)*main_mean_CAST_sub68_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub68_fixbits + (-1)*main_mean_CAST_sub68_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_data_CAST_sub68_fixp + (-1)*main_sub68_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub68_float + (-1)*main_sub68_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub68_double + (-1)*main_sub68_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub68_fixbits + (-1)*main_sub68_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub68_fixp
mathCostObj +=  + (3)*main_sub68_float
mathCostObj +=  + (6.64928)*main_sub68_double
solver.Add( + (1)*main_sub68_enob + (-1)*main_data_enob_memphi_main_tmp5<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub68_enob + (-1)*main_mean_enob_memphi_main_tmp6<=0)    #Enob propagation in sub second addend



#Constraint for cast for   %mul69 = fmul double %sub, %sub68, !taffo.info !11, !taffo.initweight !28
main_sub_CAST_mul69_fixbits = solver.IntVar(0, 15, 'main_sub_CAST_mul69_fixbits')
main_sub_CAST_mul69_fixp = solver.IntVar(0, 1, 'main_sub_CAST_mul69_fixp')
main_sub_CAST_mul69_float = solver.IntVar(0, 1, 'main_sub_CAST_mul69_float')
main_sub_CAST_mul69_double = solver.IntVar(0, 1, 'main_sub_CAST_mul69_double')
solver.Add( + (1)*main_sub_CAST_mul69_fixp + (1)*main_sub_CAST_mul69_float + (1)*main_sub_CAST_mul69_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub_CAST_mul69_fixbits + (-10000)*main_sub_CAST_mul69_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C1_main_sub_CAST_mul69')
C2_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C2_main_sub_CAST_mul69')
solver.Add( + (1)*main_sub_fixbits + (-1)*main_sub_CAST_mul69_fixbits + (-10000)*C1_main_sub_CAST_mul69<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub_fixbits + (1)*main_sub_CAST_mul69_fixbits + (-10000)*C2_main_sub_CAST_mul69<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub_CAST_mul69
castCostObj +=  + (1)*C2_main_sub_CAST_mul69
C3_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C3_main_sub_CAST_mul69')
C4_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C4_main_sub_CAST_mul69')
C5_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C5_main_sub_CAST_mul69')
C6_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C6_main_sub_CAST_mul69')
C7_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C7_main_sub_CAST_mul69')
C8_main_sub_CAST_mul69 = solver.IntVar(0, 1, 'C8_main_sub_CAST_mul69')
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_mul69_float + (-1)*C3_main_sub_CAST_mul69<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub_CAST_mul69
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_mul69_fixp + (-1)*C4_main_sub_CAST_mul69<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub_CAST_mul69
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_mul69_double + (-1)*C5_main_sub_CAST_mul69<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub_CAST_mul69
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_mul69_fixp + (-1)*C6_main_sub_CAST_mul69<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub_CAST_mul69
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_mul69_double + (-1)*C7_main_sub_CAST_mul69<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub_CAST_mul69
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_mul69_float + (-1)*C8_main_sub_CAST_mul69<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub_CAST_mul69



#Constraint for cast for   %mul69 = fmul double %sub, %sub68, !taffo.info !11, !taffo.initweight !28
main_sub68_CAST_mul69_fixbits = solver.IntVar(0, 15, 'main_sub68_CAST_mul69_fixbits')
main_sub68_CAST_mul69_fixp = solver.IntVar(0, 1, 'main_sub68_CAST_mul69_fixp')
main_sub68_CAST_mul69_float = solver.IntVar(0, 1, 'main_sub68_CAST_mul69_float')
main_sub68_CAST_mul69_double = solver.IntVar(0, 1, 'main_sub68_CAST_mul69_double')
solver.Add( + (1)*main_sub68_CAST_mul69_fixp + (1)*main_sub68_CAST_mul69_float + (1)*main_sub68_CAST_mul69_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub68_CAST_mul69_fixbits + (-10000)*main_sub68_CAST_mul69_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C1_main_sub68_CAST_mul69')
C2_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C2_main_sub68_CAST_mul69')
solver.Add( + (1)*main_sub68_fixbits + (-1)*main_sub68_CAST_mul69_fixbits + (-10000)*C1_main_sub68_CAST_mul69<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub68_fixbits + (1)*main_sub68_CAST_mul69_fixbits + (-10000)*C2_main_sub68_CAST_mul69<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub68_CAST_mul69
castCostObj +=  + (1)*C2_main_sub68_CAST_mul69
C3_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C3_main_sub68_CAST_mul69')
C4_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C4_main_sub68_CAST_mul69')
C5_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C5_main_sub68_CAST_mul69')
C6_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C6_main_sub68_CAST_mul69')
C7_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C7_main_sub68_CAST_mul69')
C8_main_sub68_CAST_mul69 = solver.IntVar(0, 1, 'C8_main_sub68_CAST_mul69')
solver.Add( + (1)*main_sub68_fixp + (1)*main_sub68_CAST_mul69_float + (-1)*C3_main_sub68_CAST_mul69<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub68_CAST_mul69
solver.Add( + (1)*main_sub68_float + (1)*main_sub68_CAST_mul69_fixp + (-1)*C4_main_sub68_CAST_mul69<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub68_CAST_mul69
solver.Add( + (1)*main_sub68_fixp + (1)*main_sub68_CAST_mul69_double + (-1)*C5_main_sub68_CAST_mul69<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub68_CAST_mul69
solver.Add( + (1)*main_sub68_double + (1)*main_sub68_CAST_mul69_fixp + (-1)*C6_main_sub68_CAST_mul69<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub68_CAST_mul69
solver.Add( + (1)*main_sub68_float + (1)*main_sub68_CAST_mul69_double + (-1)*C7_main_sub68_CAST_mul69<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub68_CAST_mul69
solver.Add( + (1)*main_sub68_double + (1)*main_sub68_CAST_mul69_float + (-1)*C8_main_sub68_CAST_mul69<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub68_CAST_mul69



#Stuff for   %mul69 = fmul double %sub, %sub68, !taffo.info !11, !taffo.initweight !28
main_mul69_fixbits = solver.IntVar(0, 15, 'main_mul69_fixbits')
main_mul69_fixp = solver.IntVar(0, 1, 'main_mul69_fixp')
main_mul69_float = solver.IntVar(0, 1, 'main_mul69_float')
main_mul69_double = solver.IntVar(0, 1, 'main_mul69_double')
main_mul69_enob = solver.IntVar(-10000, 10000, 'main_mul69_enob')
solver.Add( + (1)*main_mul69_enob + (-1)*main_mul69_fixbits + (10000)*main_mul69_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul69_enob + (10000)*main_mul69_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul69_enob + (10000)*main_mul69_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul69_fixbits + (-10000)*main_mul69_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_mul69_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul69_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul69_enob
solver.Add( + (1)*main_mul69_fixp + (1)*main_mul69_float + (1)*main_mul69_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul69_fixbits + (-10000)*main_mul69_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub_CAST_mul69_fixp + (-1)*main_sub68_CAST_mul69_fixp==0)    #fix equality
solver.Add( + (1)*main_sub_CAST_mul69_float + (-1)*main_sub68_CAST_mul69_float==0)    #float equality
solver.Add( + (1)*main_sub_CAST_mul69_double + (-1)*main_sub68_CAST_mul69_double==0)    #double equality
solver.Add( + (1)*main_sub_CAST_mul69_fixp + (-1)*main_mul69_fixp==0)    #fix equality
solver.Add( + (1)*main_sub_CAST_mul69_float + (-1)*main_mul69_float==0)    #float equality
solver.Add( + (1)*main_sub_CAST_mul69_double + (-1)*main_mul69_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul69_fixp
mathCostObj +=  + (6)*main_mul69_float
mathCostObj +=  + (12.2551)*main_mul69_double
main_main_mul69_enob_1 = solver.IntVar(0, 1, 'main_main_mul69_enob_1')
main_main_mul69_enob_2 = solver.IntVar(0, 1, 'main_main_mul69_enob_2')
solver.Add( + (1)*main_main_mul69_enob_1 + (1)*main_main_mul69_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul69_enob + (-1)*main_sub68_enob + (-10000)*main_main_mul69_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul69_enob + (-1)*main_sub_enob + (-10000)*main_main_mul69_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp7')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp7 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
solver.Add( + (1)*main_main_tmp7_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add72 = fadd double %tmp7, %mul69, !taffo.info !19, !taffo.initweight !25
main_stddev_CAST_add72_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_add72_fixbits')
main_stddev_CAST_add72_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_add72_fixp')
main_stddev_CAST_add72_float = solver.IntVar(0, 1, 'main_stddev_CAST_add72_float')
main_stddev_CAST_add72_double = solver.IntVar(0, 1, 'main_stddev_CAST_add72_double')
solver.Add( + (1)*main_stddev_CAST_add72_fixp + (1)*main_stddev_CAST_add72_float + (1)*main_stddev_CAST_add72_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_add72_fixbits + (-10000)*main_stddev_CAST_add72_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_add72')
C2_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_add72')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_add72_fixbits + (-10000)*C1_main_stddev_CAST_add72<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_add72_fixbits + (-10000)*C2_main_stddev_CAST_add72<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_stddev_CAST_add72
castCostObj +=  + (1)*C2_main_stddev_CAST_add72
C3_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_add72')
C4_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_add72')
C5_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_add72')
C6_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_add72')
C7_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_add72')
C8_main_stddev_CAST_add72 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_add72')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_add72_float + (-1)*C3_main_stddev_CAST_add72<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_stddev_CAST_add72
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_add72_fixp + (-1)*C4_main_stddev_CAST_add72<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_stddev_CAST_add72
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_add72_double + (-1)*C5_main_stddev_CAST_add72<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_stddev_CAST_add72
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_add72_fixp + (-1)*C6_main_stddev_CAST_add72<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_stddev_CAST_add72
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_add72_double + (-1)*C7_main_stddev_CAST_add72<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_stddev_CAST_add72
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_add72_float + (-1)*C8_main_stddev_CAST_add72<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_stddev_CAST_add72



#Constraint for cast for   %add72 = fadd double %tmp7, %mul69, !taffo.info !19, !taffo.initweight !25
main_mul69_CAST_add72_fixbits = solver.IntVar(0, 15, 'main_mul69_CAST_add72_fixbits')
main_mul69_CAST_add72_fixp = solver.IntVar(0, 1, 'main_mul69_CAST_add72_fixp')
main_mul69_CAST_add72_float = solver.IntVar(0, 1, 'main_mul69_CAST_add72_float')
main_mul69_CAST_add72_double = solver.IntVar(0, 1, 'main_mul69_CAST_add72_double')
solver.Add( + (1)*main_mul69_CAST_add72_fixp + (1)*main_mul69_CAST_add72_float + (1)*main_mul69_CAST_add72_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul69_CAST_add72_fixbits + (-10000)*main_mul69_CAST_add72_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C1_main_mul69_CAST_add72')
C2_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C2_main_mul69_CAST_add72')
solver.Add( + (1)*main_mul69_fixbits + (-1)*main_mul69_CAST_add72_fixbits + (-10000)*C1_main_mul69_CAST_add72<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul69_fixbits + (1)*main_mul69_CAST_add72_fixbits + (-10000)*C2_main_mul69_CAST_add72<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul69_CAST_add72
castCostObj +=  + (1)*C2_main_mul69_CAST_add72
C3_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C3_main_mul69_CAST_add72')
C4_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C4_main_mul69_CAST_add72')
C5_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C5_main_mul69_CAST_add72')
C6_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C6_main_mul69_CAST_add72')
C7_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C7_main_mul69_CAST_add72')
C8_main_mul69_CAST_add72 = solver.IntVar(0, 1, 'C8_main_mul69_CAST_add72')
solver.Add( + (1)*main_mul69_fixp + (1)*main_mul69_CAST_add72_float + (-1)*C3_main_mul69_CAST_add72<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul69_CAST_add72
solver.Add( + (1)*main_mul69_float + (1)*main_mul69_CAST_add72_fixp + (-1)*C4_main_mul69_CAST_add72<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul69_CAST_add72
solver.Add( + (1)*main_mul69_fixp + (1)*main_mul69_CAST_add72_double + (-1)*C5_main_mul69_CAST_add72<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul69_CAST_add72
solver.Add( + (1)*main_mul69_double + (1)*main_mul69_CAST_add72_fixp + (-1)*C6_main_mul69_CAST_add72<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul69_CAST_add72
solver.Add( + (1)*main_mul69_float + (1)*main_mul69_CAST_add72_double + (-1)*C7_main_mul69_CAST_add72<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul69_CAST_add72
solver.Add( + (1)*main_mul69_double + (1)*main_mul69_CAST_add72_float + (-1)*C8_main_mul69_CAST_add72<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul69_CAST_add72



#Stuff for   %add72 = fadd double %tmp7, %mul69, !taffo.info !19, !taffo.initweight !25
main_add72_fixbits = solver.IntVar(0, 18, 'main_add72_fixbits')
main_add72_fixp = solver.IntVar(0, 1, 'main_add72_fixp')
main_add72_float = solver.IntVar(0, 1, 'main_add72_float')
main_add72_double = solver.IntVar(0, 1, 'main_add72_double')
main_add72_enob = solver.IntVar(-10000, 10000, 'main_add72_enob')
solver.Add( + (1)*main_add72_enob + (-1)*main_add72_fixbits + (10000)*main_add72_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add72_enob + (10000)*main_add72_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add72_enob + (10000)*main_add72_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add72_fixbits + (-10000)*main_add72_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_add72_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add72_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add72_enob
solver.Add( + (1)*main_add72_fixp + (1)*main_add72_float + (1)*main_add72_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add72_fixbits + (-10000)*main_add72_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_stddev_CAST_add72_fixp + (-1)*main_mul69_CAST_add72_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_add72_float + (-1)*main_mul69_CAST_add72_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_add72_double + (-1)*main_mul69_CAST_add72_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_add72_fixbits + (-1)*main_mul69_CAST_add72_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_stddev_CAST_add72_fixp + (-1)*main_add72_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_add72_float + (-1)*main_add72_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_add72_double + (-1)*main_add72_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_add72_fixbits + (-1)*main_add72_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add72_fixp
mathCostObj +=  + (3)*main_add72_float
mathCostObj +=  + (6.64928)*main_add72_double
solver.Add( + (1)*main_add72_enob + (-1)*main_stddev_enob_memphi_main_tmp7<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add72_enob + (-1)*main_mul69_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add72, double* %arrayidx71, align 8, !taffo.info !19, !taffo.initweight !24
main_add72_CAST_store_fixbits = solver.IntVar(0, 18, 'main_add72_CAST_store_fixbits')
main_add72_CAST_store_fixp = solver.IntVar(0, 1, 'main_add72_CAST_store_fixp')
main_add72_CAST_store_float = solver.IntVar(0, 1, 'main_add72_CAST_store_float')
main_add72_CAST_store_double = solver.IntVar(0, 1, 'main_add72_CAST_store_double')
solver.Add( + (1)*main_add72_CAST_store_fixp + (1)*main_add72_CAST_store_float + (1)*main_add72_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add72_CAST_store_fixbits + (-10000)*main_add72_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add72_CAST_store = solver.IntVar(0, 1, 'C1_main_add72_CAST_store')
C2_main_add72_CAST_store = solver.IntVar(0, 1, 'C2_main_add72_CAST_store')
solver.Add( + (1)*main_add72_fixbits + (-1)*main_add72_CAST_store_fixbits + (-10000)*C1_main_add72_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add72_fixbits + (1)*main_add72_CAST_store_fixbits + (-10000)*C2_main_add72_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add72_CAST_store
castCostObj +=  + (1)*C2_main_add72_CAST_store
C3_main_add72_CAST_store = solver.IntVar(0, 1, 'C3_main_add72_CAST_store')
C4_main_add72_CAST_store = solver.IntVar(0, 1, 'C4_main_add72_CAST_store')
C5_main_add72_CAST_store = solver.IntVar(0, 1, 'C5_main_add72_CAST_store')
C6_main_add72_CAST_store = solver.IntVar(0, 1, 'C6_main_add72_CAST_store')
C7_main_add72_CAST_store = solver.IntVar(0, 1, 'C7_main_add72_CAST_store')
C8_main_add72_CAST_store = solver.IntVar(0, 1, 'C8_main_add72_CAST_store')
solver.Add( + (1)*main_add72_fixp + (1)*main_add72_CAST_store_float + (-1)*C3_main_add72_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add72_CAST_store
solver.Add( + (1)*main_add72_float + (1)*main_add72_CAST_store_fixp + (-1)*C4_main_add72_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add72_CAST_store
solver.Add( + (1)*main_add72_fixp + (1)*main_add72_CAST_store_double + (-1)*C5_main_add72_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add72_CAST_store
solver.Add( + (1)*main_add72_double + (1)*main_add72_CAST_store_fixp + (-1)*C6_main_add72_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add72_CAST_store
solver.Add( + (1)*main_add72_float + (1)*main_add72_CAST_store_double + (-1)*C7_main_add72_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add72_CAST_store
solver.Add( + (1)*main_add72_double + (1)*main_add72_CAST_store_float + (-1)*C8_main_add72_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add72_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*main_add72_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*main_add72_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*main_add72_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_add72_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_stddev_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_stddev_enob_storeENOB')
solver.Add( + (1)*main_stddev_enob_storeENOB + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob_storeENOB + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob_storeENOB + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_enob_storeENOB + (-1)*main_add72_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp7 + (-1)*main_stddev_enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp8')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp8 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
solver.Add( + (1)*main_main_tmp8_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp8 + (-1)*main_stddev_enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.800000e+01
ConstantValue__10_fixbits = solver.IntVar(0, 27, 'ConstantValue__10_fixbits')
ConstantValue__10_fixp = solver.IntVar(0, 1, 'ConstantValue__10_fixp')
ConstantValue__10_float = solver.IntVar(0, 1, 'ConstantValue__10_float')
ConstantValue__10_double = solver.IntVar(0, 1, 'ConstantValue__10_double')
ConstantValue__10_enob = solver.IntVar(-10000, 10000, 'ConstantValue__10_enob')
solver.Add( + (1)*ConstantValue__10_enob + (-1)*ConstantValue__10_fixbits + (10000)*ConstantValue__10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__10_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_float + (1)*ConstantValue__10_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.800000e+01
ConstantValue__11_fixbits = solver.IntVar(0, 27, 'ConstantValue__11_fixbits')
ConstantValue__11_fixp = solver.IntVar(0, 1, 'ConstantValue__11_fixp')
ConstantValue__11_float = solver.IntVar(0, 1, 'ConstantValue__11_float')
ConstantValue__11_double = solver.IntVar(0, 1, 'ConstantValue__11_double')
ConstantValue__11_enob = solver.IntVar(-10000, 10000, 'ConstantValue__11_enob')
solver.Add( + (1)*ConstantValue__11_enob + (-1)*ConstantValue__11_fixbits + (10000)*ConstantValue__11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__11_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_float + (1)*ConstantValue__11_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div78 = fdiv double %tmp8, 2.800000e+01, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !32
main_stddev_CAST_div78_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_div78_fixbits')
main_stddev_CAST_div78_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_div78_fixp')
main_stddev_CAST_div78_float = solver.IntVar(0, 1, 'main_stddev_CAST_div78_float')
main_stddev_CAST_div78_double = solver.IntVar(0, 1, 'main_stddev_CAST_div78_double')
solver.Add( + (1)*main_stddev_CAST_div78_fixp + (1)*main_stddev_CAST_div78_float + (1)*main_stddev_CAST_div78_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_div78_fixbits + (-10000)*main_stddev_CAST_div78_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_div78')
C2_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_div78')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_div78_fixbits + (-10000)*C1_main_stddev_CAST_div78<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_div78_fixbits + (-10000)*C2_main_stddev_CAST_div78<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_stddev_CAST_div78
castCostObj +=  + (1)*C2_main_stddev_CAST_div78
C3_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_div78')
C4_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_div78')
C5_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_div78')
C6_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_div78')
C7_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_div78')
C8_main_stddev_CAST_div78 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_div78')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_div78_float + (-1)*C3_main_stddev_CAST_div78<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_stddev_CAST_div78
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_div78_fixp + (-1)*C4_main_stddev_CAST_div78<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_stddev_CAST_div78
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_div78_double + (-1)*C5_main_stddev_CAST_div78<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_stddev_CAST_div78
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_div78_fixp + (-1)*C6_main_stddev_CAST_div78<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_stddev_CAST_div78
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_div78_double + (-1)*C7_main_stddev_CAST_div78<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_stddev_CAST_div78
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_div78_float + (-1)*C8_main_stddev_CAST_div78<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_stddev_CAST_div78



#Stuff for double 2.800000e+01
ConstantValue__12_fixbits = solver.IntVar(0, 27, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__12_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div78 = fdiv double %tmp8, 2.800000e+01, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !32
ConstantValue__12_CAST_div78_fixbits = solver.IntVar(0, 27, 'ConstantValue__12_CAST_div78_fixbits')
ConstantValue__12_CAST_div78_fixp = solver.IntVar(0, 1, 'ConstantValue__12_CAST_div78_fixp')
ConstantValue__12_CAST_div78_float = solver.IntVar(0, 1, 'ConstantValue__12_CAST_div78_float')
ConstantValue__12_CAST_div78_double = solver.IntVar(0, 1, 'ConstantValue__12_CAST_div78_double')
solver.Add( + (1)*ConstantValue__12_CAST_div78_fixp + (1)*ConstantValue__12_CAST_div78_float + (1)*ConstantValue__12_CAST_div78_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__12_CAST_div78_fixbits + (-10000)*ConstantValue__12_CAST_div78_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C1_ConstantValue__12_CAST_div78')
C2_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C2_ConstantValue__12_CAST_div78')
solver.Add( + (1)*ConstantValue__12_fixbits + (-1)*ConstantValue__12_CAST_div78_fixbits + (-10000)*C1_ConstantValue__12_CAST_div78<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__12_fixbits + (1)*ConstantValue__12_CAST_div78_fixbits + (-10000)*C2_ConstantValue__12_CAST_div78<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__12_CAST_div78
castCostObj +=  + (1)*C2_ConstantValue__12_CAST_div78
C3_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C3_ConstantValue__12_CAST_div78')
C4_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C4_ConstantValue__12_CAST_div78')
C5_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C5_ConstantValue__12_CAST_div78')
C6_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C6_ConstantValue__12_CAST_div78')
C7_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C7_ConstantValue__12_CAST_div78')
C8_ConstantValue__12_CAST_div78 = solver.IntVar(0, 1, 'C8_ConstantValue__12_CAST_div78')
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_div78_float + (-1)*C3_ConstantValue__12_CAST_div78<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__12_CAST_div78
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_div78_fixp + (-1)*C4_ConstantValue__12_CAST_div78<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__12_CAST_div78
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_div78_double + (-1)*C5_ConstantValue__12_CAST_div78<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__12_CAST_div78
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_div78_fixp + (-1)*C6_ConstantValue__12_CAST_div78<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__12_CAST_div78
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_div78_double + (-1)*C7_ConstantValue__12_CAST_div78<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__12_CAST_div78
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_div78_float + (-1)*C8_ConstantValue__12_CAST_div78<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__12_CAST_div78



#Stuff for   %div78 = fdiv double %tmp8, 2.800000e+01, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !32
main_div78_fixbits = solver.IntVar(0, 20, 'main_div78_fixbits')
main_div78_fixp = solver.IntVar(0, 1, 'main_div78_fixp')
main_div78_float = solver.IntVar(0, 1, 'main_div78_float')
main_div78_double = solver.IntVar(0, 1, 'main_div78_double')
main_div78_enob = solver.IntVar(-10000, 10000, 'main_div78_enob')
solver.Add( + (1)*main_div78_enob + (-1)*main_div78_fixbits + (10000)*main_div78_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div78_enob + (10000)*main_div78_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_div78_enob + (10000)*main_div78_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_div78_fixbits + (-10000)*main_div78_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_div78_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_div78_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div78_enob
solver.Add( + (1)*main_div78_fixp + (1)*main_div78_float + (1)*main_div78_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div78_fixbits + (-10000)*main_div78_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_stddev_CAST_div78_fixp + (-1)*ConstantValue__12_CAST_div78_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_div78_float + (-1)*ConstantValue__12_CAST_div78_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_div78_double + (-1)*ConstantValue__12_CAST_div78_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_div78_fixp + (-1)*main_div78_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_div78_float + (-1)*main_div78_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_div78_double + (-1)*main_div78_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div78_fixp
mathCostObj +=  + (6)*main_div78_float
mathCostObj +=  + (12)*main_div78_double
main_main_div78_enob_1 = solver.IntVar(0, 1, 'main_main_div78_enob_1')
main_main_div78_enob_2 = solver.IntVar(0, 1, 'main_main_div78_enob_2')
solver.Add( + (1)*main_main_div78_enob_1 + (1)*main_main_div78_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div78_enob + (-1)*ConstantValue__10_enob + (-10000)*main_main_div78_enob_1<=3072)    #Enob: propagation in division 1
solver.Add( + (1)*main_div78_enob + (-1)*main_stddev_enob_memphi_main_tmp8 + (-10000)*main_main_div78_enob_2<=3072)    #Enob: propagation in division 2



#Constraint for cast for   store double %div78, double* %arrayidx77, align 8, !taffo.info !19, !taffo.initweight !24
main_div78_CAST_store_fixbits = solver.IntVar(0, 20, 'main_div78_CAST_store_fixbits')
main_div78_CAST_store_fixp = solver.IntVar(0, 1, 'main_div78_CAST_store_fixp')
main_div78_CAST_store_float = solver.IntVar(0, 1, 'main_div78_CAST_store_float')
main_div78_CAST_store_double = solver.IntVar(0, 1, 'main_div78_CAST_store_double')
solver.Add( + (1)*main_div78_CAST_store_fixp + (1)*main_div78_CAST_store_float + (1)*main_div78_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div78_CAST_store_fixbits + (-10000)*main_div78_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div78_CAST_store = solver.IntVar(0, 1, 'C1_main_div78_CAST_store')
C2_main_div78_CAST_store = solver.IntVar(0, 1, 'C2_main_div78_CAST_store')
solver.Add( + (1)*main_div78_fixbits + (-1)*main_div78_CAST_store_fixbits + (-10000)*C1_main_div78_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div78_fixbits + (1)*main_div78_CAST_store_fixbits + (-10000)*C2_main_div78_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div78_CAST_store
castCostObj +=  + (1)*C2_main_div78_CAST_store
C3_main_div78_CAST_store = solver.IntVar(0, 1, 'C3_main_div78_CAST_store')
C4_main_div78_CAST_store = solver.IntVar(0, 1, 'C4_main_div78_CAST_store')
C5_main_div78_CAST_store = solver.IntVar(0, 1, 'C5_main_div78_CAST_store')
C6_main_div78_CAST_store = solver.IntVar(0, 1, 'C6_main_div78_CAST_store')
C7_main_div78_CAST_store = solver.IntVar(0, 1, 'C7_main_div78_CAST_store')
C8_main_div78_CAST_store = solver.IntVar(0, 1, 'C8_main_div78_CAST_store')
solver.Add( + (1)*main_div78_fixp + (1)*main_div78_CAST_store_float + (-1)*C3_main_div78_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div78_CAST_store
solver.Add( + (1)*main_div78_float + (1)*main_div78_CAST_store_fixp + (-1)*C4_main_div78_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div78_CAST_store
solver.Add( + (1)*main_div78_fixp + (1)*main_div78_CAST_store_double + (-1)*C5_main_div78_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div78_CAST_store
solver.Add( + (1)*main_div78_double + (1)*main_div78_CAST_store_fixp + (-1)*C6_main_div78_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div78_CAST_store
solver.Add( + (1)*main_div78_float + (1)*main_div78_CAST_store_double + (-1)*C7_main_div78_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div78_CAST_store
solver.Add( + (1)*main_div78_double + (1)*main_div78_CAST_store_float + (-1)*C8_main_div78_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div78_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*main_div78_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*main_div78_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*main_div78_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_div78_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_stddev_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_stddev_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (-1)*main_div78_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp9')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp9 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
solver.Add( + (1)*main_main_tmp9_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp9 + (-1)*main_stddev_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %call = call double @sqrt(double %tmp9) #1, !taffo.info !19, !taffo.initweight !25, !taffo.constinfo !35
main_call_fixbits = solver.IntVar(0, 18, 'main_call_fixbits')
main_call_fixp = solver.IntVar(0, 1, 'main_call_fixp')
main_call_float = solver.IntVar(0, 1, 'main_call_float')
main_call_double = solver.IntVar(0, 1, 'main_call_double')
main_call_enob = solver.IntVar(-10000, 10000, 'main_call_enob')
solver.Add( + (1)*main_call_enob + (-1)*main_call_fixbits + (10000)*main_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call_enob + (10000)*main_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_call_enob + (10000)*main_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_call_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_call_enob
solver.Add( + (1)*main_call_fixp + (1)*main_call_float + (1)*main_call_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call_double==1)    #Type constraint for return value



#Constraint for cast for   %call = call double @sqrt(double %tmp9) #1, !taffo.info !19, !taffo.initweight !25, !taffo.constinfo !35
main_stddev_CAST_call_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_call_fixbits')
main_stddev_CAST_call_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_call_fixp')
main_stddev_CAST_call_float = solver.IntVar(0, 1, 'main_stddev_CAST_call_float')
main_stddev_CAST_call_double = solver.IntVar(0, 1, 'main_stddev_CAST_call_double')
solver.Add( + (1)*main_stddev_CAST_call_fixp + (1)*main_stddev_CAST_call_float + (1)*main_stddev_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_call_fixbits + (-10000)*main_stddev_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_call = solver.IntVar(0, 1, 'C1_main_stddev_CAST_call')
C2_main_stddev_CAST_call = solver.IntVar(0, 1, 'C2_main_stddev_CAST_call')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_call_fixbits + (-10000)*C1_main_stddev_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_call_fixbits + (-10000)*C2_main_stddev_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_stddev_CAST_call
castCostObj +=  + (1)*C2_main_stddev_CAST_call
C3_main_stddev_CAST_call = solver.IntVar(0, 1, 'C3_main_stddev_CAST_call')
C4_main_stddev_CAST_call = solver.IntVar(0, 1, 'C4_main_stddev_CAST_call')
C5_main_stddev_CAST_call = solver.IntVar(0, 1, 'C5_main_stddev_CAST_call')
C6_main_stddev_CAST_call = solver.IntVar(0, 1, 'C6_main_stddev_CAST_call')
C7_main_stddev_CAST_call = solver.IntVar(0, 1, 'C7_main_stddev_CAST_call')
C8_main_stddev_CAST_call = solver.IntVar(0, 1, 'C8_main_stddev_CAST_call')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_call_float + (-1)*C3_main_stddev_CAST_call<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_call_fixp + (-1)*C4_main_stddev_CAST_call<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_call_double + (-1)*C5_main_stddev_CAST_call<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_call_fixp + (-1)*C6_main_stddev_CAST_call<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_call_double + (-1)*C7_main_stddev_CAST_call<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_call_float + (-1)*C8_main_stddev_CAST_call<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_CAST_call_double==1)    #Type constraint for argument value



#Constraint for cast for   store double %call, double* %arrayidx82, align 8, !taffo.info !19, !taffo.initweight !24
main_call_CAST_store_fixbits = solver.IntVar(0, 18, 'main_call_CAST_store_fixbits')
main_call_CAST_store_fixp = solver.IntVar(0, 1, 'main_call_CAST_store_fixp')
main_call_CAST_store_float = solver.IntVar(0, 1, 'main_call_CAST_store_float')
main_call_CAST_store_double = solver.IntVar(0, 1, 'main_call_CAST_store_double')
solver.Add( + (1)*main_call_CAST_store_fixp + (1)*main_call_CAST_store_float + (1)*main_call_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_call_CAST_store_fixbits + (-10000)*main_call_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_call_CAST_store = solver.IntVar(0, 1, 'C1_main_call_CAST_store')
C2_main_call_CAST_store = solver.IntVar(0, 1, 'C2_main_call_CAST_store')
solver.Add( + (1)*main_call_fixbits + (-1)*main_call_CAST_store_fixbits + (-10000)*C1_main_call_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_call_fixbits + (1)*main_call_CAST_store_fixbits + (-10000)*C2_main_call_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_call_CAST_store
castCostObj +=  + (1)*C2_main_call_CAST_store
C3_main_call_CAST_store = solver.IntVar(0, 1, 'C3_main_call_CAST_store')
C4_main_call_CAST_store = solver.IntVar(0, 1, 'C4_main_call_CAST_store')
C5_main_call_CAST_store = solver.IntVar(0, 1, 'C5_main_call_CAST_store')
C6_main_call_CAST_store = solver.IntVar(0, 1, 'C6_main_call_CAST_store')
C7_main_call_CAST_store = solver.IntVar(0, 1, 'C7_main_call_CAST_store')
C8_main_call_CAST_store = solver.IntVar(0, 1, 'C8_main_call_CAST_store')
solver.Add( + (1)*main_call_fixp + (1)*main_call_CAST_store_float + (-1)*C3_main_call_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_call_CAST_store
solver.Add( + (1)*main_call_float + (1)*main_call_CAST_store_fixp + (-1)*C4_main_call_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_call_CAST_store
solver.Add( + (1)*main_call_fixp + (1)*main_call_CAST_store_double + (-1)*C5_main_call_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_call_CAST_store
solver.Add( + (1)*main_call_double + (1)*main_call_CAST_store_fixp + (-1)*C6_main_call_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_call_CAST_store
solver.Add( + (1)*main_call_float + (1)*main_call_CAST_store_double + (-1)*C7_main_call_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_call_CAST_store
solver.Add( + (1)*main_call_double + (1)*main_call_CAST_store_float + (-1)*C8_main_call_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_call_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*main_call_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*main_call_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*main_call_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_call_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_stddev_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_stddev_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (-1)*main_call_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp10')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp10 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_0 = solver.IntVar(0, 1, 'main_main_tmp10_enob_0')
solver.Add( + (1)*main_main_tmp10_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp10 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.000000e-01
ConstantValue__13_fixbits = solver.IntVar(0, 31, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10027)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=10056)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__13_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_float + (1)*ConstantValue__13_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cmp85 = fcmp ole double %tmp10, 1.000000e-01, !taffo.info !41, !taffo.initweight !24
main_stddev_CAST_cmp85_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_cmp85_fixbits')
main_stddev_CAST_cmp85_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_cmp85_fixp')
main_stddev_CAST_cmp85_float = solver.IntVar(0, 1, 'main_stddev_CAST_cmp85_float')
main_stddev_CAST_cmp85_double = solver.IntVar(0, 1, 'main_stddev_CAST_cmp85_double')
solver.Add( + (1)*main_stddev_CAST_cmp85_fixp + (1)*main_stddev_CAST_cmp85_float + (1)*main_stddev_CAST_cmp85_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_cmp85_fixbits + (-10000)*main_stddev_CAST_cmp85_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_cmp85')
C2_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_cmp85')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_cmp85_fixbits + (-10000)*C1_main_stddev_CAST_cmp85<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_cmp85_fixbits + (-10000)*C2_main_stddev_CAST_cmp85<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_stddev_CAST_cmp85
castCostObj +=  + (1)*C2_main_stddev_CAST_cmp85
C3_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_cmp85')
C4_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_cmp85')
C5_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_cmp85')
C6_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_cmp85')
C7_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_cmp85')
C8_main_stddev_CAST_cmp85 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_cmp85')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cmp85_float + (-1)*C3_main_stddev_CAST_cmp85<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_stddev_CAST_cmp85
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cmp85_fixp + (-1)*C4_main_stddev_CAST_cmp85<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_stddev_CAST_cmp85
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cmp85_double + (-1)*C5_main_stddev_CAST_cmp85<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_stddev_CAST_cmp85
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cmp85_fixp + (-1)*C6_main_stddev_CAST_cmp85<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_stddev_CAST_cmp85
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cmp85_double + (-1)*C7_main_stddev_CAST_cmp85<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_stddev_CAST_cmp85
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cmp85_float + (-1)*C8_main_stddev_CAST_cmp85<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_stddev_CAST_cmp85



#Stuff for double 1.000000e-01
ConstantValue__14_fixbits = solver.IntVar(0, 31, 'ConstantValue__14_fixbits')
ConstantValue__14_fixp = solver.IntVar(0, 1, 'ConstantValue__14_fixp')
ConstantValue__14_float = solver.IntVar(0, 1, 'ConstantValue__14_float')
ConstantValue__14_double = solver.IntVar(0, 1, 'ConstantValue__14_double')
ConstantValue__14_enob = solver.IntVar(-10000, 10000, 'ConstantValue__14_enob')
solver.Add( + (1)*ConstantValue__14_enob + (-1)*ConstantValue__14_fixbits + (10000)*ConstantValue__14_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_float<=10027)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_double<=10056)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__14_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_float + (1)*ConstantValue__14_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cmp85 = fcmp ole double %tmp10, 1.000000e-01, !taffo.info !41, !taffo.initweight !24
ConstantValue__14_CAST_cmp85_fixbits = solver.IntVar(0, 31, 'ConstantValue__14_CAST_cmp85_fixbits')
ConstantValue__14_CAST_cmp85_fixp = solver.IntVar(0, 1, 'ConstantValue__14_CAST_cmp85_fixp')
ConstantValue__14_CAST_cmp85_float = solver.IntVar(0, 1, 'ConstantValue__14_CAST_cmp85_float')
ConstantValue__14_CAST_cmp85_double = solver.IntVar(0, 1, 'ConstantValue__14_CAST_cmp85_double')
solver.Add( + (1)*ConstantValue__14_CAST_cmp85_fixp + (1)*ConstantValue__14_CAST_cmp85_float + (1)*ConstantValue__14_CAST_cmp85_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__14_CAST_cmp85_fixbits + (-10000)*ConstantValue__14_CAST_cmp85_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C1_ConstantValue__14_CAST_cmp85')
C2_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C2_ConstantValue__14_CAST_cmp85')
solver.Add( + (1)*ConstantValue__14_fixbits + (-1)*ConstantValue__14_CAST_cmp85_fixbits + (-10000)*C1_ConstantValue__14_CAST_cmp85<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__14_fixbits + (1)*ConstantValue__14_CAST_cmp85_fixbits + (-10000)*C2_ConstantValue__14_CAST_cmp85<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__14_CAST_cmp85
castCostObj +=  + (1)*C2_ConstantValue__14_CAST_cmp85
C3_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C3_ConstantValue__14_CAST_cmp85')
C4_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C4_ConstantValue__14_CAST_cmp85')
C5_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C5_ConstantValue__14_CAST_cmp85')
C6_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C6_ConstantValue__14_CAST_cmp85')
C7_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C7_ConstantValue__14_CAST_cmp85')
C8_ConstantValue__14_CAST_cmp85 = solver.IntVar(0, 1, 'C8_ConstantValue__14_CAST_cmp85')
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_cmp85_float + (-1)*C3_ConstantValue__14_CAST_cmp85<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__14_CAST_cmp85
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_cmp85_fixp + (-1)*C4_ConstantValue__14_CAST_cmp85<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__14_CAST_cmp85
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_cmp85_double + (-1)*C5_ConstantValue__14_CAST_cmp85<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__14_CAST_cmp85
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_cmp85_fixp + (-1)*C6_ConstantValue__14_CAST_cmp85<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__14_CAST_cmp85
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_cmp85_double + (-1)*C7_ConstantValue__14_CAST_cmp85<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__14_CAST_cmp85
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_cmp85_float + (-1)*C8_ConstantValue__14_CAST_cmp85<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__14_CAST_cmp85
solver.Add( + (1)*main_stddev_CAST_cmp85_fixp + (-1)*ConstantValue__14_CAST_cmp85_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_cmp85_float + (-1)*ConstantValue__14_CAST_cmp85_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_cmp85_double + (-1)*ConstantValue__14_CAST_cmp85_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_cmp85_fixbits + (-1)*ConstantValue__14_CAST_cmp85_fixbits==0)    #same fractional bit

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp11')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp11 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_0 = solver.IntVar(0, 1, 'main_main_tmp11_enob_0')
solver.Add( + (1)*main_main_tmp11_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp11 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !19, !taffo.initweight !25
main_cond_fixbits = solver.IntVar(0, 18, 'main_cond_fixbits')
main_cond_fixp = solver.IntVar(0, 1, 'main_cond_fixp')
main_cond_float = solver.IntVar(0, 1, 'main_cond_float')
main_cond_double = solver.IntVar(0, 1, 'main_cond_double')
main_cond_enob = solver.IntVar(-10000, 10000, 'main_cond_enob')
solver.Add( + (1)*main_cond_enob + (-1)*main_cond_fixbits + (10000)*main_cond_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_cond_enob + (10000)*main_cond_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_cond_enob + (10000)*main_cond_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_cond_fixbits + (-10000)*main_cond_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_cond_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_cond_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_cond_enob
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_float + (1)*main_cond_double==1)    #Exactly one selected type
solver.Add( + (1)*main_cond_fixbits + (-10000)*main_cond_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__15_fixbits = solver.IntVar(0, 31, 'ConstantValue__15_fixbits')
ConstantValue__15_fixp = solver.IntVar(0, 1, 'ConstantValue__15_fixp')
ConstantValue__15_float = solver.IntVar(0, 1, 'ConstantValue__15_float')
ConstantValue__15_double = solver.IntVar(0, 1, 'ConstantValue__15_double')
ConstantValue__15_enob = solver.IntVar(-10000, 10000, 'ConstantValue__15_enob')
solver.Add( + (1)*ConstantValue__15_enob + (-1)*ConstantValue__15_fixbits + (10000)*ConstantValue__15_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__15_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__15_fixp + (1)*ConstantValue__15_float + (1)*ConstantValue__15_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp<=0)    #If not fix, frac part to zero
main_main_cond_enob_1 = solver.IntVar(0, 1, 'main_main_cond_enob_1')
solver.Add( + (1)*main_main_cond_enob_1==1)    #Enob: one selected constraint



#Stuff for double 1.000000e+00
ConstantValue__16_fixbits = solver.IntVar(0, 31, 'ConstantValue__16_fixbits')
ConstantValue__16_fixp = solver.IntVar(0, 1, 'ConstantValue__16_fixp')
ConstantValue__16_float = solver.IntVar(0, 1, 'ConstantValue__16_float')
ConstantValue__16_double = solver.IntVar(0, 1, 'ConstantValue__16_double')
ConstantValue__16_enob = solver.IntVar(-10000, 10000, 'ConstantValue__16_enob')
solver.Add( + (1)*ConstantValue__16_enob + (-1)*ConstantValue__16_fixbits + (10000)*ConstantValue__16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__16_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !19, !taffo.initweight !25
main_stddev_CAST_cond_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_cond_fixbits')
main_stddev_CAST_cond_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_cond_fixp')
main_stddev_CAST_cond_float = solver.IntVar(0, 1, 'main_stddev_CAST_cond_float')
main_stddev_CAST_cond_double = solver.IntVar(0, 1, 'main_stddev_CAST_cond_double')
solver.Add( + (1)*main_stddev_CAST_cond_fixp + (1)*main_stddev_CAST_cond_float + (1)*main_stddev_CAST_cond_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_cond_fixbits + (-10000)*main_stddev_CAST_cond_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C1_main_stddev_CAST_cond')
C2_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C2_main_stddev_CAST_cond')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_cond_fixbits + (-10000)*C1_main_stddev_CAST_cond<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_cond_fixbits + (-10000)*C2_main_stddev_CAST_cond<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_stddev_CAST_cond
castCostObj +=  + (1)*C2_main_stddev_CAST_cond
C3_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C3_main_stddev_CAST_cond')
C4_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C4_main_stddev_CAST_cond')
C5_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C5_main_stddev_CAST_cond')
C6_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C6_main_stddev_CAST_cond')
C7_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C7_main_stddev_CAST_cond')
C8_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C8_main_stddev_CAST_cond')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cond_float + (-1)*C3_main_stddev_CAST_cond<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cond_fixp + (-1)*C4_main_stddev_CAST_cond<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cond_double + (-1)*C5_main_stddev_CAST_cond<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cond_fixp + (-1)*C6_main_stddev_CAST_cond<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cond_double + (-1)*C7_main_stddev_CAST_cond<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cond_float + (-1)*C8_main_stddev_CAST_cond<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_stddev_CAST_cond
solver.Add( + (1)*main_cond_fixp + (-1)*main_stddev_CAST_cond_fixp==0)    #fix equality
solver.Add( + (1)*main_cond_float + (-1)*main_stddev_CAST_cond_float==0)    #float equality
solver.Add( + (1)*main_cond_double + (-1)*main_stddev_CAST_cond_double==0)    #double equality
solver.Add( + (1)*main_cond_fixbits + (-1)*main_stddev_CAST_cond_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_cond_enob + (-1)*main_stddev_enob_memphi_main_tmp11 + (10000)*main_main_cond_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   store double %cond, double* %arrayidx90, align 8, !taffo.info !19, !taffo.initweight !24
main_cond_CAST_store_fixbits = solver.IntVar(0, 18, 'main_cond_CAST_store_fixbits')
main_cond_CAST_store_fixp = solver.IntVar(0, 1, 'main_cond_CAST_store_fixp')
main_cond_CAST_store_float = solver.IntVar(0, 1, 'main_cond_CAST_store_float')
main_cond_CAST_store_double = solver.IntVar(0, 1, 'main_cond_CAST_store_double')
solver.Add( + (1)*main_cond_CAST_store_fixp + (1)*main_cond_CAST_store_float + (1)*main_cond_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_cond_CAST_store_fixbits + (-10000)*main_cond_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_cond_CAST_store = solver.IntVar(0, 1, 'C1_main_cond_CAST_store')
C2_main_cond_CAST_store = solver.IntVar(0, 1, 'C2_main_cond_CAST_store')
solver.Add( + (1)*main_cond_fixbits + (-1)*main_cond_CAST_store_fixbits + (-10000)*C1_main_cond_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_cond_fixbits + (1)*main_cond_CAST_store_fixbits + (-10000)*C2_main_cond_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_cond_CAST_store
castCostObj +=  + (1)*C2_main_cond_CAST_store
C3_main_cond_CAST_store = solver.IntVar(0, 1, 'C3_main_cond_CAST_store')
C4_main_cond_CAST_store = solver.IntVar(0, 1, 'C4_main_cond_CAST_store')
C5_main_cond_CAST_store = solver.IntVar(0, 1, 'C5_main_cond_CAST_store')
C6_main_cond_CAST_store = solver.IntVar(0, 1, 'C6_main_cond_CAST_store')
C7_main_cond_CAST_store = solver.IntVar(0, 1, 'C7_main_cond_CAST_store')
C8_main_cond_CAST_store = solver.IntVar(0, 1, 'C8_main_cond_CAST_store')
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_CAST_store_float + (-1)*C3_main_cond_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_cond_CAST_store
solver.Add( + (1)*main_cond_float + (1)*main_cond_CAST_store_fixp + (-1)*C4_main_cond_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_cond_CAST_store
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_CAST_store_double + (-1)*C5_main_cond_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_cond_CAST_store
solver.Add( + (1)*main_cond_double + (1)*main_cond_CAST_store_fixp + (-1)*C6_main_cond_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_cond_CAST_store
solver.Add( + (1)*main_cond_float + (1)*main_cond_CAST_store_double + (-1)*C7_main_cond_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_cond_CAST_store
solver.Add( + (1)*main_cond_double + (1)*main_cond_CAST_store_float + (-1)*C8_main_cond_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_cond_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*main_cond_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*main_cond_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*main_cond_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_cond_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_cond_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp12')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp12 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp12_enob_1 = solver.IntVar(0, 1, 'main_main_tmp12_enob_1')
main_main_tmp12_enob_2 = solver.IntVar(0, 1, 'main_main_tmp12_enob_2')
solver.Add( + (1)*main_main_tmp12_enob_1 + (1)*main_main_tmp12_enob_2==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp12 + (-1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp13 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp13')
solver.Add( + (1)*main_data_enob_memphi_main_tmp13 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp13_enob_1 = solver.IntVar(0, 1, 'main_main_tmp13_enob_1')
main_main_tmp13_enob_2 = solver.IntVar(0, 1, 'main_main_tmp13_enob_2')
main_main_tmp13_enob_3 = solver.IntVar(0, 1, 'main_main_tmp13_enob_3')
main_main_tmp13_enob_4 = solver.IntVar(0, 1, 'main_main_tmp13_enob_4')
solver.Add( + (1)*main_main_tmp13_enob_1 + (1)*main_main_tmp13_enob_2 + (1)*main_main_tmp13_enob_3 + (1)*main_main_tmp13_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp13 + (-1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp13 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub108 = fsub double %tmp13, %tmp12, !taffo.info !11, !taffo.initweight !25
main_data_CAST_sub108_fixbits = solver.IntVar(0, 27, 'main_data_CAST_sub108_fixbits')
main_data_CAST_sub108_fixp = solver.IntVar(0, 1, 'main_data_CAST_sub108_fixp')
main_data_CAST_sub108_float = solver.IntVar(0, 1, 'main_data_CAST_sub108_float')
main_data_CAST_sub108_double = solver.IntVar(0, 1, 'main_data_CAST_sub108_double')
solver.Add( + (1)*main_data_CAST_sub108_fixp + (1)*main_data_CAST_sub108_float + (1)*main_data_CAST_sub108_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_sub108_fixbits + (-10000)*main_data_CAST_sub108_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C1_main_data_CAST_sub108')
C2_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C2_main_data_CAST_sub108')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_sub108_fixbits + (-10000)*C1_main_data_CAST_sub108<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_sub108_fixbits + (-10000)*C2_main_data_CAST_sub108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_sub108
castCostObj +=  + (1)*C2_main_data_CAST_sub108
C3_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C3_main_data_CAST_sub108')
C4_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C4_main_data_CAST_sub108')
C5_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C5_main_data_CAST_sub108')
C6_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C6_main_data_CAST_sub108')
C7_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C7_main_data_CAST_sub108')
C8_main_data_CAST_sub108 = solver.IntVar(0, 1, 'C8_main_data_CAST_sub108')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub108_float + (-1)*C3_main_data_CAST_sub108<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_sub108
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub108_fixp + (-1)*C4_main_data_CAST_sub108<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_sub108
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub108_double + (-1)*C5_main_data_CAST_sub108<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_sub108
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub108_fixp + (-1)*C6_main_data_CAST_sub108<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_sub108
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub108_double + (-1)*C7_main_data_CAST_sub108<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_sub108
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub108_float + (-1)*C8_main_data_CAST_sub108<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_sub108



#Constraint for cast for   %sub108 = fsub double %tmp13, %tmp12, !taffo.info !11, !taffo.initweight !25
main_mean_CAST_sub108_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_sub108_fixbits')
main_mean_CAST_sub108_fixp = solver.IntVar(0, 1, 'main_mean_CAST_sub108_fixp')
main_mean_CAST_sub108_float = solver.IntVar(0, 1, 'main_mean_CAST_sub108_float')
main_mean_CAST_sub108_double = solver.IntVar(0, 1, 'main_mean_CAST_sub108_double')
solver.Add( + (1)*main_mean_CAST_sub108_fixp + (1)*main_mean_CAST_sub108_float + (1)*main_mean_CAST_sub108_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_sub108_fixbits + (-10000)*main_mean_CAST_sub108_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C1_main_mean_CAST_sub108')
C2_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C2_main_mean_CAST_sub108')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_sub108_fixbits + (-10000)*C1_main_mean_CAST_sub108<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_sub108_fixbits + (-10000)*C2_main_mean_CAST_sub108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mean_CAST_sub108
castCostObj +=  + (1)*C2_main_mean_CAST_sub108
C3_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C3_main_mean_CAST_sub108')
C4_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C4_main_mean_CAST_sub108')
C5_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C5_main_mean_CAST_sub108')
C6_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C6_main_mean_CAST_sub108')
C7_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C7_main_mean_CAST_sub108')
C8_main_mean_CAST_sub108 = solver.IntVar(0, 1, 'C8_main_mean_CAST_sub108')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub108_float + (-1)*C3_main_mean_CAST_sub108<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mean_CAST_sub108
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub108_fixp + (-1)*C4_main_mean_CAST_sub108<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mean_CAST_sub108
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub108_double + (-1)*C5_main_mean_CAST_sub108<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mean_CAST_sub108
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub108_fixp + (-1)*C6_main_mean_CAST_sub108<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mean_CAST_sub108
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub108_double + (-1)*C7_main_mean_CAST_sub108<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mean_CAST_sub108
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub108_float + (-1)*C8_main_mean_CAST_sub108<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mean_CAST_sub108



#Stuff for   %sub108 = fsub double %tmp13, %tmp12, !taffo.info !11, !taffo.initweight !25
main_sub108_fixbits = solver.IntVar(0, 15, 'main_sub108_fixbits')
main_sub108_fixp = solver.IntVar(0, 1, 'main_sub108_fixp')
main_sub108_float = solver.IntVar(0, 1, 'main_sub108_float')
main_sub108_double = solver.IntVar(0, 1, 'main_sub108_double')
main_sub108_enob = solver.IntVar(-10000, 10000, 'main_sub108_enob')
solver.Add( + (1)*main_sub108_enob + (-1)*main_sub108_fixbits + (10000)*main_sub108_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub108_enob + (10000)*main_sub108_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub108_enob + (10000)*main_sub108_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub108_fixbits + (-10000)*main_sub108_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub108_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_sub108_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub108_enob
solver.Add( + (1)*main_sub108_fixp + (1)*main_sub108_float + (1)*main_sub108_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub108_fixbits + (-10000)*main_sub108_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_sub108_fixp + (-1)*main_mean_CAST_sub108_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub108_float + (-1)*main_mean_CAST_sub108_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub108_double + (-1)*main_mean_CAST_sub108_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub108_fixbits + (-1)*main_mean_CAST_sub108_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_data_CAST_sub108_fixp + (-1)*main_sub108_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub108_float + (-1)*main_sub108_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub108_double + (-1)*main_sub108_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub108_fixbits + (-1)*main_sub108_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub108_fixp
mathCostObj +=  + (3)*main_sub108_float
mathCostObj +=  + (6.64928)*main_sub108_double
solver.Add( + (1)*main_sub108_enob + (-1)*main_data_enob_memphi_main_tmp13<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub108_enob + (-1)*main_mean_enob_memphi_main_tmp12<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub108, double* %arrayidx107, align 8, !taffo.info !15, !taffo.initweight !25
main_sub108_CAST_store_fixbits = solver.IntVar(0, 15, 'main_sub108_CAST_store_fixbits')
main_sub108_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub108_CAST_store_fixp')
main_sub108_CAST_store_float = solver.IntVar(0, 1, 'main_sub108_CAST_store_float')
main_sub108_CAST_store_double = solver.IntVar(0, 1, 'main_sub108_CAST_store_double')
solver.Add( + (1)*main_sub108_CAST_store_fixp + (1)*main_sub108_CAST_store_float + (1)*main_sub108_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub108_CAST_store_fixbits + (-10000)*main_sub108_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub108_CAST_store = solver.IntVar(0, 1, 'C1_main_sub108_CAST_store')
C2_main_sub108_CAST_store = solver.IntVar(0, 1, 'C2_main_sub108_CAST_store')
solver.Add( + (1)*main_sub108_fixbits + (-1)*main_sub108_CAST_store_fixbits + (-10000)*C1_main_sub108_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub108_fixbits + (1)*main_sub108_CAST_store_fixbits + (-10000)*C2_main_sub108_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub108_CAST_store
castCostObj +=  + (1)*C2_main_sub108_CAST_store
C3_main_sub108_CAST_store = solver.IntVar(0, 1, 'C3_main_sub108_CAST_store')
C4_main_sub108_CAST_store = solver.IntVar(0, 1, 'C4_main_sub108_CAST_store')
C5_main_sub108_CAST_store = solver.IntVar(0, 1, 'C5_main_sub108_CAST_store')
C6_main_sub108_CAST_store = solver.IntVar(0, 1, 'C6_main_sub108_CAST_store')
C7_main_sub108_CAST_store = solver.IntVar(0, 1, 'C7_main_sub108_CAST_store')
C8_main_sub108_CAST_store = solver.IntVar(0, 1, 'C8_main_sub108_CAST_store')
solver.Add( + (1)*main_sub108_fixp + (1)*main_sub108_CAST_store_float + (-1)*C3_main_sub108_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub108_CAST_store
solver.Add( + (1)*main_sub108_float + (1)*main_sub108_CAST_store_fixp + (-1)*C4_main_sub108_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub108_CAST_store
solver.Add( + (1)*main_sub108_fixp + (1)*main_sub108_CAST_store_double + (-1)*C5_main_sub108_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub108_CAST_store
solver.Add( + (1)*main_sub108_double + (1)*main_sub108_CAST_store_fixp + (-1)*C6_main_sub108_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub108_CAST_store
solver.Add( + (1)*main_sub108_float + (1)*main_sub108_CAST_store_double + (-1)*C7_main_sub108_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub108_CAST_store
solver.Add( + (1)*main_sub108_double + (1)*main_sub108_CAST_store_float + (-1)*C8_main_sub108_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub108_CAST_store
solver.Add( + (1)*main_data_fixp + (-1)*main_sub108_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_data_float + (-1)*main_sub108_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_data_double + (-1)*main_sub108_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_data_fixbits + (-1)*main_sub108_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_data_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_data_enob_storeENOB')
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_sub108_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %call109 = call double @sqrt(double 2.800000e+01) #1, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !42
main_call109_fixbits = solver.IntVar(0, 20, 'main_call109_fixbits')
main_call109_fixp = solver.IntVar(0, 1, 'main_call109_fixp')
main_call109_float = solver.IntVar(0, 1, 'main_call109_float')
main_call109_double = solver.IntVar(0, 1, 'main_call109_double')
main_call109_enob = solver.IntVar(-10000, 10000, 'main_call109_enob')
solver.Add( + (1)*main_call109_enob + (-1)*main_call109_fixbits + (10000)*main_call109_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call109_enob + (10000)*main_call109_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_call109_enob + (10000)*main_call109_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_call109_fixbits + (-10000)*main_call109_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_call109_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_call109_enob
solver.Add( + (1)*main_call109_fixp + (1)*main_call109_float + (1)*main_call109_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call109_fixbits + (-10000)*main_call109_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call109_double==1)    #Type constraint for return value



#Stuff for double 2.800000e+01
ConstantValue__17_fixbits = solver.IntVar(0, 27, 'ConstantValue__17_fixbits')
ConstantValue__17_fixp = solver.IntVar(0, 1, 'ConstantValue__17_fixp')
ConstantValue__17_float = solver.IntVar(0, 1, 'ConstantValue__17_float')
ConstantValue__17_double = solver.IntVar(0, 1, 'ConstantValue__17_double')
ConstantValue__17_enob = solver.IntVar(-10000, 10000, 'ConstantValue__17_enob')
solver.Add( + (1)*ConstantValue__17_enob + (-1)*ConstantValue__17_fixbits + (10000)*ConstantValue__17_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__17_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_float + (1)*ConstantValue__17_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.800000e+01
ConstantValue__18_fixbits = solver.IntVar(0, 27, 'ConstantValue__18_fixbits')
ConstantValue__18_fixp = solver.IntVar(0, 1, 'ConstantValue__18_fixp')
ConstantValue__18_float = solver.IntVar(0, 1, 'ConstantValue__18_float')
ConstantValue__18_double = solver.IntVar(0, 1, 'ConstantValue__18_double')
ConstantValue__18_enob = solver.IntVar(-10000, 10000, 'ConstantValue__18_enob')
solver.Add( + (1)*ConstantValue__18_enob + (-1)*ConstantValue__18_fixbits + (10000)*ConstantValue__18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__18_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__18_fixp + (1)*ConstantValue__18_float + (1)*ConstantValue__18_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call109 = call double @sqrt(double 2.800000e+01) #1, !taffo.info !39, !taffo.initweight !24, !taffo.constinfo !42
ConstantValue__18_CAST_call109_fixbits = solver.IntVar(0, 27, 'ConstantValue__18_CAST_call109_fixbits')
ConstantValue__18_CAST_call109_fixp = solver.IntVar(0, 1, 'ConstantValue__18_CAST_call109_fixp')
ConstantValue__18_CAST_call109_float = solver.IntVar(0, 1, 'ConstantValue__18_CAST_call109_float')
ConstantValue__18_CAST_call109_double = solver.IntVar(0, 1, 'ConstantValue__18_CAST_call109_double')
solver.Add( + (1)*ConstantValue__18_CAST_call109_fixp + (1)*ConstantValue__18_CAST_call109_float + (1)*ConstantValue__18_CAST_call109_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__18_CAST_call109_fixbits + (-10000)*ConstantValue__18_CAST_call109_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C1_ConstantValue__18_CAST_call109')
C2_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C2_ConstantValue__18_CAST_call109')
solver.Add( + (1)*ConstantValue__18_fixbits + (-1)*ConstantValue__18_CAST_call109_fixbits + (-10000)*C1_ConstantValue__18_CAST_call109<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__18_fixbits + (1)*ConstantValue__18_CAST_call109_fixbits + (-10000)*C2_ConstantValue__18_CAST_call109<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__18_CAST_call109
castCostObj +=  + (1)*C2_ConstantValue__18_CAST_call109
C3_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C3_ConstantValue__18_CAST_call109')
C4_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C4_ConstantValue__18_CAST_call109')
C5_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C5_ConstantValue__18_CAST_call109')
C6_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C6_ConstantValue__18_CAST_call109')
C7_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C7_ConstantValue__18_CAST_call109')
C8_ConstantValue__18_CAST_call109 = solver.IntVar(0, 1, 'C8_ConstantValue__18_CAST_call109')
solver.Add( + (1)*ConstantValue__18_fixp + (1)*ConstantValue__18_CAST_call109_float + (-1)*C3_ConstantValue__18_CAST_call109<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__18_CAST_call109
solver.Add( + (1)*ConstantValue__18_float + (1)*ConstantValue__18_CAST_call109_fixp + (-1)*C4_ConstantValue__18_CAST_call109<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__18_CAST_call109
solver.Add( + (1)*ConstantValue__18_fixp + (1)*ConstantValue__18_CAST_call109_double + (-1)*C5_ConstantValue__18_CAST_call109<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__18_CAST_call109
solver.Add( + (1)*ConstantValue__18_double + (1)*ConstantValue__18_CAST_call109_fixp + (-1)*C6_ConstantValue__18_CAST_call109<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__18_CAST_call109
solver.Add( + (1)*ConstantValue__18_float + (1)*ConstantValue__18_CAST_call109_double + (-1)*C7_ConstantValue__18_CAST_call109<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__18_CAST_call109
solver.Add( + (1)*ConstantValue__18_double + (1)*ConstantValue__18_CAST_call109_float + (-1)*C8_ConstantValue__18_CAST_call109<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__18_CAST_call109
solver.Add( + (1)*ConstantValue__18_CAST_call109_double==1)    #Type constraint for argument value

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp14 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp14')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp14 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp14_enob_1 = solver.IntVar(0, 1, 'main_main_tmp14_enob_1')
main_main_tmp14_enob_2 = solver.IntVar(0, 1, 'main_main_tmp14_enob_2')
main_main_tmp14_enob_3 = solver.IntVar(0, 1, 'main_main_tmp14_enob_3')
solver.Add( + (1)*main_main_tmp14_enob_1 + (1)*main_main_tmp14_enob_2 + (1)*main_main_tmp14_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp14 + (-1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp14_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp14 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp14_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul112 = fmul double %call109, %tmp14, !taffo.info !19, !taffo.initweight !25
main_call109_CAST_mul112_fixbits = solver.IntVar(0, 20, 'main_call109_CAST_mul112_fixbits')
main_call109_CAST_mul112_fixp = solver.IntVar(0, 1, 'main_call109_CAST_mul112_fixp')
main_call109_CAST_mul112_float = solver.IntVar(0, 1, 'main_call109_CAST_mul112_float')
main_call109_CAST_mul112_double = solver.IntVar(0, 1, 'main_call109_CAST_mul112_double')
solver.Add( + (1)*main_call109_CAST_mul112_fixp + (1)*main_call109_CAST_mul112_float + (1)*main_call109_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*main_call109_CAST_mul112_fixbits + (-10000)*main_call109_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C1_main_call109_CAST_mul112')
C2_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C2_main_call109_CAST_mul112')
solver.Add( + (1)*main_call109_fixbits + (-1)*main_call109_CAST_mul112_fixbits + (-10000)*C1_main_call109_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*main_call109_fixbits + (1)*main_call109_CAST_mul112_fixbits + (-10000)*C2_main_call109_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_call109_CAST_mul112
castCostObj +=  + (1)*C2_main_call109_CAST_mul112
C3_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C3_main_call109_CAST_mul112')
C4_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C4_main_call109_CAST_mul112')
C5_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C5_main_call109_CAST_mul112')
C6_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C6_main_call109_CAST_mul112')
C7_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C7_main_call109_CAST_mul112')
C8_main_call109_CAST_mul112 = solver.IntVar(0, 1, 'C8_main_call109_CAST_mul112')
solver.Add( + (1)*main_call109_fixp + (1)*main_call109_CAST_mul112_float + (-1)*C3_main_call109_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_call109_CAST_mul112
solver.Add( + (1)*main_call109_float + (1)*main_call109_CAST_mul112_fixp + (-1)*C4_main_call109_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_call109_CAST_mul112
solver.Add( + (1)*main_call109_fixp + (1)*main_call109_CAST_mul112_double + (-1)*C5_main_call109_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_call109_CAST_mul112
solver.Add( + (1)*main_call109_double + (1)*main_call109_CAST_mul112_fixp + (-1)*C6_main_call109_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_call109_CAST_mul112
solver.Add( + (1)*main_call109_float + (1)*main_call109_CAST_mul112_double + (-1)*C7_main_call109_CAST_mul112<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_call109_CAST_mul112
solver.Add( + (1)*main_call109_double + (1)*main_call109_CAST_mul112_float + (-1)*C8_main_call109_CAST_mul112<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_call109_CAST_mul112



#Constraint for cast for   %mul112 = fmul double %call109, %tmp14, !taffo.info !19, !taffo.initweight !25
main_stddev_CAST_mul112_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_mul112_fixbits')
main_stddev_CAST_mul112_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_mul112_fixp')
main_stddev_CAST_mul112_float = solver.IntVar(0, 1, 'main_stddev_CAST_mul112_float')
main_stddev_CAST_mul112_double = solver.IntVar(0, 1, 'main_stddev_CAST_mul112_double')
solver.Add( + (1)*main_stddev_CAST_mul112_fixp + (1)*main_stddev_CAST_mul112_float + (1)*main_stddev_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_mul112_fixbits + (-10000)*main_stddev_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_mul112')
C2_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_mul112')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_mul112_fixbits + (-10000)*C1_main_stddev_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_mul112_fixbits + (-10000)*C2_main_stddev_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_stddev_CAST_mul112
castCostObj +=  + (1)*C2_main_stddev_CAST_mul112
C3_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_mul112')
C4_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_mul112')
C5_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_mul112')
C6_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_mul112')
C7_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_mul112')
C8_main_stddev_CAST_mul112 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_mul112')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_mul112_float + (-1)*C3_main_stddev_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_stddev_CAST_mul112
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_mul112_fixp + (-1)*C4_main_stddev_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_stddev_CAST_mul112
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_mul112_double + (-1)*C5_main_stddev_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_stddev_CAST_mul112
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_mul112_fixp + (-1)*C6_main_stddev_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_stddev_CAST_mul112
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_mul112_double + (-1)*C7_main_stddev_CAST_mul112<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_stddev_CAST_mul112
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_mul112_float + (-1)*C8_main_stddev_CAST_mul112<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_stddev_CAST_mul112



#Stuff for   %mul112 = fmul double %call109, %tmp14, !taffo.info !19, !taffo.initweight !25
main_mul112_fixbits = solver.IntVar(0, 18, 'main_mul112_fixbits')
main_mul112_fixp = solver.IntVar(0, 1, 'main_mul112_fixp')
main_mul112_float = solver.IntVar(0, 1, 'main_mul112_float')
main_mul112_double = solver.IntVar(0, 1, 'main_mul112_double')
main_mul112_enob = solver.IntVar(-10000, 10000, 'main_mul112_enob')
solver.Add( + (1)*main_mul112_enob + (-1)*main_mul112_fixbits + (10000)*main_mul112_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_mul112_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul112_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul112_enob
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_float + (1)*main_mul112_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call109_CAST_mul112_fixp + (-1)*main_stddev_CAST_mul112_fixp==0)    #fix equality
solver.Add( + (1)*main_call109_CAST_mul112_float + (-1)*main_stddev_CAST_mul112_float==0)    #float equality
solver.Add( + (1)*main_call109_CAST_mul112_double + (-1)*main_stddev_CAST_mul112_double==0)    #double equality
solver.Add( + (1)*main_call109_CAST_mul112_fixp + (-1)*main_mul112_fixp==0)    #fix equality
solver.Add( + (1)*main_call109_CAST_mul112_float + (-1)*main_mul112_float==0)    #float equality
solver.Add( + (1)*main_call109_CAST_mul112_double + (-1)*main_mul112_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul112_fixp
mathCostObj +=  + (6)*main_mul112_float
mathCostObj +=  + (12.2551)*main_mul112_double
main_main_mul112_enob_1 = solver.IntVar(0, 1, 'main_main_mul112_enob_1')
main_main_mul112_enob_2 = solver.IntVar(0, 1, 'main_main_mul112_enob_2')
solver.Add( + (1)*main_main_mul112_enob_1 + (1)*main_main_mul112_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul112_enob + (-1)*main_stddev_enob_memphi_main_tmp14 + (-10000)*main_main_mul112_enob_1<=0)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul112_enob + (-1)*main_call109_enob + (-10000)*main_main_mul112_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp15 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp15')
solver.Add( + (1)*main_data_enob_memphi_main_tmp15 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp15_enob_0 = solver.IntVar(0, 1, 'main_main_tmp15_enob_0')
solver.Add( + (1)*main_main_tmp15_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp15 + (-1)*main_data_enob_storeENOB + (10000)*main_main_tmp15_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div117 = fdiv double %tmp15, %mul112, !taffo.info !15, !taffo.initweight !28
main_data_CAST_div117_fixbits = solver.IntVar(0, 27, 'main_data_CAST_div117_fixbits')
main_data_CAST_div117_fixp = solver.IntVar(0, 1, 'main_data_CAST_div117_fixp')
main_data_CAST_div117_float = solver.IntVar(0, 1, 'main_data_CAST_div117_float')
main_data_CAST_div117_double = solver.IntVar(0, 1, 'main_data_CAST_div117_double')
solver.Add( + (1)*main_data_CAST_div117_fixp + (1)*main_data_CAST_div117_float + (1)*main_data_CAST_div117_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_div117_fixbits + (-10000)*main_data_CAST_div117_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_div117 = solver.IntVar(0, 1, 'C1_main_data_CAST_div117')
C2_main_data_CAST_div117 = solver.IntVar(0, 1, 'C2_main_data_CAST_div117')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_div117_fixbits + (-10000)*C1_main_data_CAST_div117<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_div117_fixbits + (-10000)*C2_main_data_CAST_div117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_div117
castCostObj +=  + (1)*C2_main_data_CAST_div117
C3_main_data_CAST_div117 = solver.IntVar(0, 1, 'C3_main_data_CAST_div117')
C4_main_data_CAST_div117 = solver.IntVar(0, 1, 'C4_main_data_CAST_div117')
C5_main_data_CAST_div117 = solver.IntVar(0, 1, 'C5_main_data_CAST_div117')
C6_main_data_CAST_div117 = solver.IntVar(0, 1, 'C6_main_data_CAST_div117')
C7_main_data_CAST_div117 = solver.IntVar(0, 1, 'C7_main_data_CAST_div117')
C8_main_data_CAST_div117 = solver.IntVar(0, 1, 'C8_main_data_CAST_div117')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_div117_float + (-1)*C3_main_data_CAST_div117<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_div117
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_div117_fixp + (-1)*C4_main_data_CAST_div117<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_div117
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_div117_double + (-1)*C5_main_data_CAST_div117<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_div117
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_div117_fixp + (-1)*C6_main_data_CAST_div117<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_div117
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_div117_double + (-1)*C7_main_data_CAST_div117<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_div117
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_div117_float + (-1)*C8_main_data_CAST_div117<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_div117



#Constraint for cast for   %div117 = fdiv double %tmp15, %mul112, !taffo.info !15, !taffo.initweight !28
main_mul112_CAST_div117_fixbits = solver.IntVar(0, 18, 'main_mul112_CAST_div117_fixbits')
main_mul112_CAST_div117_fixp = solver.IntVar(0, 1, 'main_mul112_CAST_div117_fixp')
main_mul112_CAST_div117_float = solver.IntVar(0, 1, 'main_mul112_CAST_div117_float')
main_mul112_CAST_div117_double = solver.IntVar(0, 1, 'main_mul112_CAST_div117_double')
solver.Add( + (1)*main_mul112_CAST_div117_fixp + (1)*main_mul112_CAST_div117_float + (1)*main_mul112_CAST_div117_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul112_CAST_div117_fixbits + (-10000)*main_mul112_CAST_div117_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C1_main_mul112_CAST_div117')
C2_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C2_main_mul112_CAST_div117')
solver.Add( + (1)*main_mul112_fixbits + (-1)*main_mul112_CAST_div117_fixbits + (-10000)*C1_main_mul112_CAST_div117<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul112_fixbits + (1)*main_mul112_CAST_div117_fixbits + (-10000)*C2_main_mul112_CAST_div117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul112_CAST_div117
castCostObj +=  + (1)*C2_main_mul112_CAST_div117
C3_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C3_main_mul112_CAST_div117')
C4_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C4_main_mul112_CAST_div117')
C5_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C5_main_mul112_CAST_div117')
C6_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C6_main_mul112_CAST_div117')
C7_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C7_main_mul112_CAST_div117')
C8_main_mul112_CAST_div117 = solver.IntVar(0, 1, 'C8_main_mul112_CAST_div117')
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_CAST_div117_float + (-1)*C3_main_mul112_CAST_div117<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul112_CAST_div117
solver.Add( + (1)*main_mul112_float + (1)*main_mul112_CAST_div117_fixp + (-1)*C4_main_mul112_CAST_div117<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul112_CAST_div117
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_CAST_div117_double + (-1)*C5_main_mul112_CAST_div117<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul112_CAST_div117
solver.Add( + (1)*main_mul112_double + (1)*main_mul112_CAST_div117_fixp + (-1)*C6_main_mul112_CAST_div117<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul112_CAST_div117
solver.Add( + (1)*main_mul112_float + (1)*main_mul112_CAST_div117_double + (-1)*C7_main_mul112_CAST_div117<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul112_CAST_div117
solver.Add( + (1)*main_mul112_double + (1)*main_mul112_CAST_div117_float + (-1)*C8_main_mul112_CAST_div117<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul112_CAST_div117



#Stuff for   %div117 = fdiv double %tmp15, %mul112, !taffo.info !15, !taffo.initweight !28
main_div117_fixbits = solver.IntVar(0, 27, 'main_div117_fixbits')
main_div117_fixp = solver.IntVar(0, 1, 'main_div117_fixp')
main_div117_float = solver.IntVar(0, 1, 'main_div117_float')
main_div117_double = solver.IntVar(0, 1, 'main_div117_double')
main_div117_enob = solver.IntVar(-10000, 10000, 'main_div117_enob')
solver.Add( + (1)*main_div117_enob + (-1)*main_div117_fixbits + (10000)*main_div117_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div117_enob + (10000)*main_div117_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div117_enob + (10000)*main_div117_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div117_fixbits + (-10000)*main_div117_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_div117_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_div117_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div117_enob
solver.Add( + (1)*main_div117_fixp + (1)*main_div117_float + (1)*main_div117_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div117_fixbits + (-10000)*main_div117_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_div117_fixp + (-1)*main_mul112_CAST_div117_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_div117_float + (-1)*main_mul112_CAST_div117_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_div117_double + (-1)*main_mul112_CAST_div117_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_div117_fixp + (-1)*main_div117_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_div117_float + (-1)*main_div117_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_div117_double + (-1)*main_div117_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div117_fixp
mathCostObj +=  + (6)*main_div117_float
mathCostObj +=  + (12)*main_div117_double
main_main_div117_enob_1 = solver.IntVar(0, 1, 'main_main_div117_enob_1')
main_main_div117_enob_2 = solver.IntVar(0, 1, 'main_main_div117_enob_2')
solver.Add( + (1)*main_main_div117_enob_1 + (1)*main_main_div117_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div117_enob + (-1)*main_mul112_enob + (-10000)*main_main_div117_enob_1<=1048)    #Enob: propagation in division 1
solver.Add( + (1)*main_div117_enob + (-1)*main_data_enob_memphi_main_tmp15 + (-10000)*main_main_div117_enob_2<=1048)    #Enob: propagation in division 2



#Constraint for cast for   store double %div117, double* %arrayidx116, align 8, !taffo.info !15, !taffo.initweight !25
main_div117_CAST_store_fixbits = solver.IntVar(0, 27, 'main_div117_CAST_store_fixbits')
main_div117_CAST_store_fixp = solver.IntVar(0, 1, 'main_div117_CAST_store_fixp')
main_div117_CAST_store_float = solver.IntVar(0, 1, 'main_div117_CAST_store_float')
main_div117_CAST_store_double = solver.IntVar(0, 1, 'main_div117_CAST_store_double')
solver.Add( + (1)*main_div117_CAST_store_fixp + (1)*main_div117_CAST_store_float + (1)*main_div117_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div117_CAST_store_fixbits + (-10000)*main_div117_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div117_CAST_store = solver.IntVar(0, 1, 'C1_main_div117_CAST_store')
C2_main_div117_CAST_store = solver.IntVar(0, 1, 'C2_main_div117_CAST_store')
solver.Add( + (1)*main_div117_fixbits + (-1)*main_div117_CAST_store_fixbits + (-10000)*C1_main_div117_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div117_fixbits + (1)*main_div117_CAST_store_fixbits + (-10000)*C2_main_div117_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div117_CAST_store
castCostObj +=  + (1)*C2_main_div117_CAST_store
C3_main_div117_CAST_store = solver.IntVar(0, 1, 'C3_main_div117_CAST_store')
C4_main_div117_CAST_store = solver.IntVar(0, 1, 'C4_main_div117_CAST_store')
C5_main_div117_CAST_store = solver.IntVar(0, 1, 'C5_main_div117_CAST_store')
C6_main_div117_CAST_store = solver.IntVar(0, 1, 'C6_main_div117_CAST_store')
C7_main_div117_CAST_store = solver.IntVar(0, 1, 'C7_main_div117_CAST_store')
C8_main_div117_CAST_store = solver.IntVar(0, 1, 'C8_main_div117_CAST_store')
solver.Add( + (1)*main_div117_fixp + (1)*main_div117_CAST_store_float + (-1)*C3_main_div117_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div117_CAST_store
solver.Add( + (1)*main_div117_float + (1)*main_div117_CAST_store_fixp + (-1)*C4_main_div117_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div117_CAST_store
solver.Add( + (1)*main_div117_fixp + (1)*main_div117_CAST_store_double + (-1)*C5_main_div117_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div117_CAST_store
solver.Add( + (1)*main_div117_double + (1)*main_div117_CAST_store_fixp + (-1)*C6_main_div117_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div117_CAST_store
solver.Add( + (1)*main_div117_float + (1)*main_div117_CAST_store_double + (-1)*C7_main_div117_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div117_CAST_store
solver.Add( + (1)*main_div117_double + (1)*main_div117_CAST_store_float + (-1)*C8_main_div117_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div117_CAST_store
solver.Add( + (1)*main_data_fixp + (-1)*main_div117_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_data_float + (-1)*main_div117_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_data_double + (-1)*main_div117_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_data_fixbits + (-1)*main_div117_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_data_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_data_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (-1)*main_div117_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp13 + (-1)*main_data_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_4<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.000000e+00
ConstantValue__19_fixbits = solver.IntVar(0, 31, 'ConstantValue__19_fixbits')
ConstantValue__19_fixp = solver.IntVar(0, 1, 'ConstantValue__19_fixp')
ConstantValue__19_float = solver.IntVar(0, 1, 'ConstantValue__19_float')
ConstantValue__19_double = solver.IntVar(0, 1, 'ConstantValue__19_double')
ConstantValue__19_enob = solver.IntVar(-10000, 10000, 'ConstantValue__19_enob')
solver.Add( + (1)*ConstantValue__19_enob + (-1)*ConstantValue__19_fixbits + (10000)*ConstantValue__19_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__19_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_float + (1)*ConstantValue__19_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__20_fixbits = solver.IntVar(0, 31, 'ConstantValue__20_fixbits')
ConstantValue__20_fixp = solver.IntVar(0, 1, 'ConstantValue__20_fixp')
ConstantValue__20_float = solver.IntVar(0, 1, 'ConstantValue__20_float')
ConstantValue__20_double = solver.IntVar(0, 1, 'ConstantValue__20_double')
ConstantValue__20_enob = solver.IntVar(-10000, 10000, 'ConstantValue__20_enob')
solver.Add( + (1)*ConstantValue__20_enob + (-1)*ConstantValue__20_fixbits + (10000)*ConstantValue__20_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__20_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_float + (1)*ConstantValue__20_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx131, align 8, !taffo.info !17, !taffo.initweight !25, !taffo.constinfo !43
ConstantValue__20_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__20_CAST_store_fixbits')
ConstantValue__20_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__20_CAST_store_fixp')
ConstantValue__20_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__20_CAST_store_float')
ConstantValue__20_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__20_CAST_store_double')
solver.Add( + (1)*ConstantValue__20_CAST_store_fixp + (1)*ConstantValue__20_CAST_store_float + (1)*ConstantValue__20_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__20_CAST_store_fixbits + (-10000)*ConstantValue__20_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__20_CAST_store')
C2_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__20_CAST_store')
solver.Add( + (1)*ConstantValue__20_fixbits + (-1)*ConstantValue__20_CAST_store_fixbits + (-10000)*C1_ConstantValue__20_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__20_fixbits + (1)*ConstantValue__20_CAST_store_fixbits + (-10000)*C2_ConstantValue__20_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__20_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__20_CAST_store
C3_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__20_CAST_store')
C4_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__20_CAST_store')
C5_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__20_CAST_store')
C6_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__20_CAST_store')
C7_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__20_CAST_store')
C8_ConstantValue__20_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__20_CAST_store')
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_CAST_store_float + (-1)*C3_ConstantValue__20_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__20_CAST_store
solver.Add( + (1)*ConstantValue__20_float + (1)*ConstantValue__20_CAST_store_fixp + (-1)*C4_ConstantValue__20_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__20_CAST_store
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_CAST_store_double + (-1)*C5_ConstantValue__20_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__20_CAST_store
solver.Add( + (1)*ConstantValue__20_double + (1)*ConstantValue__20_CAST_store_fixp + (-1)*C6_ConstantValue__20_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__20_CAST_store
solver.Add( + (1)*ConstantValue__20_float + (1)*ConstantValue__20_CAST_store_double + (-1)*C7_ConstantValue__20_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__20_CAST_store
solver.Add( + (1)*ConstantValue__20_double + (1)*ConstantValue__20_CAST_store_float + (-1)*C8_ConstantValue__20_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__20_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__20_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__20_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__20_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__20_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 0.000000e+00
ConstantValue__21_fixbits = solver.IntVar(0, 32, 'ConstantValue__21_fixbits')
ConstantValue__21_fixp = solver.IntVar(0, 1, 'ConstantValue__21_fixp')
ConstantValue__21_float = solver.IntVar(0, 1, 'ConstantValue__21_float')
ConstantValue__21_double = solver.IntVar(0, 1, 'ConstantValue__21_double')
ConstantValue__21_enob = solver.IntVar(-10000, 10000, 'ConstantValue__21_enob')
solver.Add( + (1)*ConstantValue__21_enob + (-1)*ConstantValue__21_fixbits + (10000)*ConstantValue__21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__21_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__21_fixp + (1)*ConstantValue__21_float + (1)*ConstantValue__21_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__22_fixbits = solver.IntVar(0, 32, 'ConstantValue__22_fixbits')
ConstantValue__22_fixp = solver.IntVar(0, 1, 'ConstantValue__22_fixp')
ConstantValue__22_float = solver.IntVar(0, 1, 'ConstantValue__22_float')
ConstantValue__22_double = solver.IntVar(0, 1, 'ConstantValue__22_double')
ConstantValue__22_enob = solver.IntVar(-10000, 10000, 'ConstantValue__22_enob')
solver.Add( + (1)*ConstantValue__22_enob + (-1)*ConstantValue__22_fixbits + (10000)*ConstantValue__22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__22_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_float + (1)*ConstantValue__22_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx140, align 8, !taffo.info !17, !taffo.initweight !25, !taffo.constinfo !36
ConstantValue__22_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__22_CAST_store_fixbits')
ConstantValue__22_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__22_CAST_store_fixp')
ConstantValue__22_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__22_CAST_store_float')
ConstantValue__22_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__22_CAST_store_double')
solver.Add( + (1)*ConstantValue__22_CAST_store_fixp + (1)*ConstantValue__22_CAST_store_float + (1)*ConstantValue__22_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__22_CAST_store_fixbits + (-10000)*ConstantValue__22_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__22_CAST_store')
C2_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__22_CAST_store')
solver.Add( + (1)*ConstantValue__22_fixbits + (-1)*ConstantValue__22_CAST_store_fixbits + (-10000)*C1_ConstantValue__22_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__22_fixbits + (1)*ConstantValue__22_CAST_store_fixbits + (-10000)*C2_ConstantValue__22_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__22_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__22_CAST_store
C3_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__22_CAST_store')
C4_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__22_CAST_store')
C5_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__22_CAST_store')
C6_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__22_CAST_store')
C7_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__22_CAST_store')
C8_ConstantValue__22_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__22_CAST_store')
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_CAST_store_float + (-1)*C3_ConstantValue__22_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__22_CAST_store
solver.Add( + (1)*ConstantValue__22_float + (1)*ConstantValue__22_CAST_store_fixp + (-1)*C4_ConstantValue__22_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__22_CAST_store
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_CAST_store_double + (-1)*C5_ConstantValue__22_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__22_CAST_store
solver.Add( + (1)*ConstantValue__22_double + (1)*ConstantValue__22_CAST_store_fixp + (-1)*C6_ConstantValue__22_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__22_CAST_store
solver.Add( + (1)*ConstantValue__22_float + (1)*ConstantValue__22_CAST_store_double + (-1)*C7_ConstantValue__22_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__22_CAST_store
solver.Add( + (1)*ConstantValue__22_double + (1)*ConstantValue__22_CAST_store_float + (-1)*C8_ConstantValue__22_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__22_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__22_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__22_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__22_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__22_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp16 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp16')
solver.Add( + (1)*main_data_enob_memphi_main_tmp16 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp16_enob_1 = solver.IntVar(0, 1, 'main_main_tmp16_enob_1')
main_main_tmp16_enob_2 = solver.IntVar(0, 1, 'main_main_tmp16_enob_2')
main_main_tmp16_enob_3 = solver.IntVar(0, 1, 'main_main_tmp16_enob_3')
main_main_tmp16_enob_4 = solver.IntVar(0, 1, 'main_main_tmp16_enob_4')
solver.Add( + (1)*main_main_tmp16_enob_1 + (1)*main_main_tmp16_enob_2 + (1)*main_main_tmp16_enob_3 + (1)*main_main_tmp16_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp16 + (-1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp16 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp16 + (-1)*main_data_enob_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp17 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp17')
solver.Add( + (1)*main_data_enob_memphi_main_tmp17 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp17_enob_1 = solver.IntVar(0, 1, 'main_main_tmp17_enob_1')
main_main_tmp17_enob_2 = solver.IntVar(0, 1, 'main_main_tmp17_enob_2')
main_main_tmp17_enob_3 = solver.IntVar(0, 1, 'main_main_tmp17_enob_3')
main_main_tmp17_enob_4 = solver.IntVar(0, 1, 'main_main_tmp17_enob_4')
solver.Add( + (1)*main_main_tmp17_enob_1 + (1)*main_main_tmp17_enob_2 + (1)*main_main_tmp17_enob_3 + (1)*main_main_tmp17_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp17 + (-1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp17 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp17 + (-1)*main_data_enob_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul153 = fmul double %tmp16, %tmp17, !taffo.info !15, !taffo.initweight !28
main_data_CAST_mul153_fixbits = solver.IntVar(0, 27, 'main_data_CAST_mul153_fixbits')
main_data_CAST_mul153_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul153_fixp')
main_data_CAST_mul153_float = solver.IntVar(0, 1, 'main_data_CAST_mul153_float')
main_data_CAST_mul153_double = solver.IntVar(0, 1, 'main_data_CAST_mul153_double')
solver.Add( + (1)*main_data_CAST_mul153_fixp + (1)*main_data_CAST_mul153_float + (1)*main_data_CAST_mul153_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul153_fixbits + (-10000)*main_data_CAST_mul153_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul153')
C2_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul153')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul153_fixbits + (-10000)*C1_main_data_CAST_mul153<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul153_fixbits + (-10000)*C2_main_data_CAST_mul153<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_mul153
castCostObj +=  + (1)*C2_main_data_CAST_mul153
C3_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul153')
C4_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul153')
C5_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul153')
C6_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul153')
C7_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul153')
C8_main_data_CAST_mul153 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul153')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul153_float + (-1)*C3_main_data_CAST_mul153<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_mul153
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul153_fixp + (-1)*C4_main_data_CAST_mul153<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_mul153
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul153_double + (-1)*C5_main_data_CAST_mul153<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_mul153
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul153_fixp + (-1)*C6_main_data_CAST_mul153<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_mul153
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul153_double + (-1)*C7_main_data_CAST_mul153<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_mul153
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul153_float + (-1)*C8_main_data_CAST_mul153<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_mul153



#Constraint for cast for   %mul153 = fmul double %tmp16, %tmp17, !taffo.info !15, !taffo.initweight !28
main_data_CAST_mul153_0_fixbits = solver.IntVar(0, 27, 'main_data_CAST_mul153_0_fixbits')
main_data_CAST_mul153_0_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul153_0_fixp')
main_data_CAST_mul153_0_float = solver.IntVar(0, 1, 'main_data_CAST_mul153_0_float')
main_data_CAST_mul153_0_double = solver.IntVar(0, 1, 'main_data_CAST_mul153_0_double')
solver.Add( + (1)*main_data_CAST_mul153_0_fixp + (1)*main_data_CAST_mul153_0_float + (1)*main_data_CAST_mul153_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul153_0_fixbits + (-10000)*main_data_CAST_mul153_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul153_0')
C2_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul153_0')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul153_0_fixbits + (-10000)*C1_main_data_CAST_mul153_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul153_0_fixbits + (-10000)*C2_main_data_CAST_mul153_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_data_CAST_mul153_0
castCostObj +=  + (1)*C2_main_data_CAST_mul153_0
C3_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul153_0')
C4_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul153_0')
C5_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul153_0')
C6_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul153_0')
C7_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul153_0')
C8_main_data_CAST_mul153_0 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul153_0')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul153_0_float + (-1)*C3_main_data_CAST_mul153_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_data_CAST_mul153_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul153_0_fixp + (-1)*C4_main_data_CAST_mul153_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_data_CAST_mul153_0
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul153_0_double + (-1)*C5_main_data_CAST_mul153_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_data_CAST_mul153_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul153_0_fixp + (-1)*C6_main_data_CAST_mul153_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_data_CAST_mul153_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul153_0_double + (-1)*C7_main_data_CAST_mul153_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_data_CAST_mul153_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul153_0_float + (-1)*C8_main_data_CAST_mul153_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_data_CAST_mul153_0



#Stuff for   %mul153 = fmul double %tmp16, %tmp17, !taffo.info !15, !taffo.initweight !28
main_mul153_fixbits = solver.IntVar(0, 27, 'main_mul153_fixbits')
main_mul153_fixp = solver.IntVar(0, 1, 'main_mul153_fixp')
main_mul153_float = solver.IntVar(0, 1, 'main_mul153_float')
main_mul153_double = solver.IntVar(0, 1, 'main_mul153_double')
main_mul153_enob = solver.IntVar(-10000, 10000, 'main_mul153_enob')
solver.Add( + (1)*main_mul153_enob + (-1)*main_mul153_fixbits + (10000)*main_mul153_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul153_enob + (10000)*main_mul153_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul153_enob + (10000)*main_mul153_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul153_fixbits + (-10000)*main_mul153_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_mul153_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul153_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul153_enob
solver.Add( + (1)*main_mul153_fixp + (1)*main_mul153_float + (1)*main_mul153_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul153_fixbits + (-10000)*main_mul153_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_mul153_fixp + (-1)*main_data_CAST_mul153_0_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul153_float + (-1)*main_data_CAST_mul153_0_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul153_double + (-1)*main_data_CAST_mul153_0_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_mul153_fixp + (-1)*main_mul153_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul153_float + (-1)*main_mul153_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul153_double + (-1)*main_mul153_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul153_fixp
mathCostObj +=  + (6)*main_mul153_float
mathCostObj +=  + (12.2551)*main_mul153_double
main_main_mul153_enob_1 = solver.IntVar(0, 1, 'main_main_mul153_enob_1')
main_main_mul153_enob_2 = solver.IntVar(0, 1, 'main_main_mul153_enob_2')
solver.Add( + (1)*main_main_mul153_enob_1 + (1)*main_main_mul153_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul153_enob + (-1)*main_data_enob_memphi_main_tmp17 + (-10000)*main_main_mul153_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul153_enob + (-1)*main_data_enob_memphi_main_tmp16 + (-10000)*main_main_mul153_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp18 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp18')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp18 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp18_enob_1 = solver.IntVar(0, 1, 'main_main_tmp18_enob_1')
solver.Add( + (1)*main_main_tmp18_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add158 = fadd double %tmp18, %mul153, !taffo.info !17, !taffo.initweight !28
main_corr_CAST_add158_fixbits = solver.IntVar(0, 29, 'main_corr_CAST_add158_fixbits')
main_corr_CAST_add158_fixp = solver.IntVar(0, 1, 'main_corr_CAST_add158_fixp')
main_corr_CAST_add158_float = solver.IntVar(0, 1, 'main_corr_CAST_add158_float')
main_corr_CAST_add158_double = solver.IntVar(0, 1, 'main_corr_CAST_add158_double')
solver.Add( + (1)*main_corr_CAST_add158_fixp + (1)*main_corr_CAST_add158_float + (1)*main_corr_CAST_add158_double==1)    #exactly 1 type
solver.Add( + (1)*main_corr_CAST_add158_fixbits + (-10000)*main_corr_CAST_add158_fixp<=0)    #If no fix, fix frac part = 0
C1_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C1_main_corr_CAST_add158')
C2_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C2_main_corr_CAST_add158')
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_add158_fixbits + (-10000)*C1_main_corr_CAST_add158<=0)    #Shift cost 1
solver.Add( + (-1)*main_corr_fixbits + (1)*main_corr_CAST_add158_fixbits + (-10000)*C2_main_corr_CAST_add158<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_corr_CAST_add158
castCostObj +=  + (1)*C2_main_corr_CAST_add158
C3_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C3_main_corr_CAST_add158')
C4_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C4_main_corr_CAST_add158')
C5_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C5_main_corr_CAST_add158')
C6_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C6_main_corr_CAST_add158')
C7_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C7_main_corr_CAST_add158')
C8_main_corr_CAST_add158 = solver.IntVar(0, 1, 'C8_main_corr_CAST_add158')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_add158_float + (-1)*C3_main_corr_CAST_add158<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_corr_CAST_add158
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_add158_fixp + (-1)*C4_main_corr_CAST_add158<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_corr_CAST_add158
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_add158_double + (-1)*C5_main_corr_CAST_add158<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_corr_CAST_add158
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_add158_fixp + (-1)*C6_main_corr_CAST_add158<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_corr_CAST_add158
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_add158_double + (-1)*C7_main_corr_CAST_add158<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_corr_CAST_add158
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_add158_float + (-1)*C8_main_corr_CAST_add158<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_corr_CAST_add158



#Constraint for cast for   %add158 = fadd double %tmp18, %mul153, !taffo.info !17, !taffo.initweight !28
main_mul153_CAST_add158_fixbits = solver.IntVar(0, 27, 'main_mul153_CAST_add158_fixbits')
main_mul153_CAST_add158_fixp = solver.IntVar(0, 1, 'main_mul153_CAST_add158_fixp')
main_mul153_CAST_add158_float = solver.IntVar(0, 1, 'main_mul153_CAST_add158_float')
main_mul153_CAST_add158_double = solver.IntVar(0, 1, 'main_mul153_CAST_add158_double')
solver.Add( + (1)*main_mul153_CAST_add158_fixp + (1)*main_mul153_CAST_add158_float + (1)*main_mul153_CAST_add158_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul153_CAST_add158_fixbits + (-10000)*main_mul153_CAST_add158_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C1_main_mul153_CAST_add158')
C2_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C2_main_mul153_CAST_add158')
solver.Add( + (1)*main_mul153_fixbits + (-1)*main_mul153_CAST_add158_fixbits + (-10000)*C1_main_mul153_CAST_add158<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul153_fixbits + (1)*main_mul153_CAST_add158_fixbits + (-10000)*C2_main_mul153_CAST_add158<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul153_CAST_add158
castCostObj +=  + (1)*C2_main_mul153_CAST_add158
C3_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C3_main_mul153_CAST_add158')
C4_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C4_main_mul153_CAST_add158')
C5_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C5_main_mul153_CAST_add158')
C6_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C6_main_mul153_CAST_add158')
C7_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C7_main_mul153_CAST_add158')
C8_main_mul153_CAST_add158 = solver.IntVar(0, 1, 'C8_main_mul153_CAST_add158')
solver.Add( + (1)*main_mul153_fixp + (1)*main_mul153_CAST_add158_float + (-1)*C3_main_mul153_CAST_add158<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul153_CAST_add158
solver.Add( + (1)*main_mul153_float + (1)*main_mul153_CAST_add158_fixp + (-1)*C4_main_mul153_CAST_add158<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul153_CAST_add158
solver.Add( + (1)*main_mul153_fixp + (1)*main_mul153_CAST_add158_double + (-1)*C5_main_mul153_CAST_add158<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul153_CAST_add158
solver.Add( + (1)*main_mul153_double + (1)*main_mul153_CAST_add158_fixp + (-1)*C6_main_mul153_CAST_add158<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul153_CAST_add158
solver.Add( + (1)*main_mul153_float + (1)*main_mul153_CAST_add158_double + (-1)*C7_main_mul153_CAST_add158<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul153_CAST_add158
solver.Add( + (1)*main_mul153_double + (1)*main_mul153_CAST_add158_float + (-1)*C8_main_mul153_CAST_add158<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul153_CAST_add158



#Stuff for   %add158 = fadd double %tmp18, %mul153, !taffo.info !17, !taffo.initweight !28
main_add158_fixbits = solver.IntVar(0, 29, 'main_add158_fixbits')
main_add158_fixp = solver.IntVar(0, 1, 'main_add158_fixp')
main_add158_float = solver.IntVar(0, 1, 'main_add158_float')
main_add158_double = solver.IntVar(0, 1, 'main_add158_double')
main_add158_enob = solver.IntVar(-10000, 10000, 'main_add158_enob')
solver.Add( + (1)*main_add158_enob + (-1)*main_add158_fixbits + (10000)*main_add158_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add158_enob + (10000)*main_add158_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add158_enob + (10000)*main_add158_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add158_fixbits + (-10000)*main_add158_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_add158_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add158_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add158_enob
solver.Add( + (1)*main_add158_fixp + (1)*main_add158_float + (1)*main_add158_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add158_fixbits + (-10000)*main_add158_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_corr_CAST_add158_fixp + (-1)*main_mul153_CAST_add158_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_CAST_add158_float + (-1)*main_mul153_CAST_add158_float==0)    #float equality
solver.Add( + (1)*main_corr_CAST_add158_double + (-1)*main_mul153_CAST_add158_double==0)    #double equality
solver.Add( + (1)*main_corr_CAST_add158_fixbits + (-1)*main_mul153_CAST_add158_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_corr_CAST_add158_fixp + (-1)*main_add158_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_CAST_add158_float + (-1)*main_add158_float==0)    #float equality
solver.Add( + (1)*main_corr_CAST_add158_double + (-1)*main_add158_double==0)    #double equality
solver.Add( + (1)*main_corr_CAST_add158_fixbits + (-1)*main_add158_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add158_fixp
mathCostObj +=  + (3)*main_add158_float
mathCostObj +=  + (6.64928)*main_add158_double
solver.Add( + (1)*main_add158_enob + (-1)*main_corr_enob_memphi_main_tmp18<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add158_enob + (-1)*main_mul153_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add158, double* %arrayidx157, align 8, !taffo.info !17, !taffo.initweight !25
main_add158_CAST_store_fixbits = solver.IntVar(0, 29, 'main_add158_CAST_store_fixbits')
main_add158_CAST_store_fixp = solver.IntVar(0, 1, 'main_add158_CAST_store_fixp')
main_add158_CAST_store_float = solver.IntVar(0, 1, 'main_add158_CAST_store_float')
main_add158_CAST_store_double = solver.IntVar(0, 1, 'main_add158_CAST_store_double')
solver.Add( + (1)*main_add158_CAST_store_fixp + (1)*main_add158_CAST_store_float + (1)*main_add158_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add158_CAST_store_fixbits + (-10000)*main_add158_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add158_CAST_store = solver.IntVar(0, 1, 'C1_main_add158_CAST_store')
C2_main_add158_CAST_store = solver.IntVar(0, 1, 'C2_main_add158_CAST_store')
solver.Add( + (1)*main_add158_fixbits + (-1)*main_add158_CAST_store_fixbits + (-10000)*C1_main_add158_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add158_fixbits + (1)*main_add158_CAST_store_fixbits + (-10000)*C2_main_add158_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add158_CAST_store
castCostObj +=  + (1)*C2_main_add158_CAST_store
C3_main_add158_CAST_store = solver.IntVar(0, 1, 'C3_main_add158_CAST_store')
C4_main_add158_CAST_store = solver.IntVar(0, 1, 'C4_main_add158_CAST_store')
C5_main_add158_CAST_store = solver.IntVar(0, 1, 'C5_main_add158_CAST_store')
C6_main_add158_CAST_store = solver.IntVar(0, 1, 'C6_main_add158_CAST_store')
C7_main_add158_CAST_store = solver.IntVar(0, 1, 'C7_main_add158_CAST_store')
C8_main_add158_CAST_store = solver.IntVar(0, 1, 'C8_main_add158_CAST_store')
solver.Add( + (1)*main_add158_fixp + (1)*main_add158_CAST_store_float + (-1)*C3_main_add158_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add158_CAST_store
solver.Add( + (1)*main_add158_float + (1)*main_add158_CAST_store_fixp + (-1)*C4_main_add158_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add158_CAST_store
solver.Add( + (1)*main_add158_fixp + (1)*main_add158_CAST_store_double + (-1)*C5_main_add158_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add158_CAST_store
solver.Add( + (1)*main_add158_double + (1)*main_add158_CAST_store_fixp + (-1)*C6_main_add158_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add158_CAST_store
solver.Add( + (1)*main_add158_float + (1)*main_add158_CAST_store_double + (-1)*C7_main_add158_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add158_CAST_store
solver.Add( + (1)*main_add158_double + (1)*main_add158_CAST_store_float + (-1)*C8_main_add158_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add158_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*main_add158_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*main_add158_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*main_add158_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*main_add158_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_corr_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_corr_enob_storeENOB')
solver.Add( + (1)*main_corr_enob_storeENOB + (-1)*main_corr_fixbits + (10000)*main_corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_corr_enob_storeENOB + (10000)*main_corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_corr_enob_storeENOB + (10000)*main_corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_corr_enob_storeENOB + (-1)*main_add158_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_corr_enob_memphi_main_tmp18 + (-1)*main_corr_enob_storeENOB + (10000)*main_main_tmp18_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp19 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp19')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp19 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp19_enob_1 = solver.IntVar(0, 1, 'main_main_tmp19_enob_1')
solver.Add( + (1)*main_main_tmp19_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_corr_enob_memphi_main_tmp19 + (-1)*main_corr_enob_storeENOB + (10000)*main_main_tmp19_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp19, double* %arrayidx169, align 8, !taffo.info !17, !taffo.initweight !25
main_corr_CAST_store_fixbits = solver.IntVar(0, 29, 'main_corr_CAST_store_fixbits')
main_corr_CAST_store_fixp = solver.IntVar(0, 1, 'main_corr_CAST_store_fixp')
main_corr_CAST_store_float = solver.IntVar(0, 1, 'main_corr_CAST_store_float')
main_corr_CAST_store_double = solver.IntVar(0, 1, 'main_corr_CAST_store_double')
solver.Add( + (1)*main_corr_CAST_store_fixp + (1)*main_corr_CAST_store_float + (1)*main_corr_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_corr_CAST_store_fixbits + (-10000)*main_corr_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_corr_CAST_store = solver.IntVar(0, 1, 'C1_main_corr_CAST_store')
C2_main_corr_CAST_store = solver.IntVar(0, 1, 'C2_main_corr_CAST_store')
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_store_fixbits + (-10000)*C1_main_corr_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_corr_fixbits + (1)*main_corr_CAST_store_fixbits + (-10000)*C2_main_corr_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_corr_CAST_store
castCostObj +=  + (1)*C2_main_corr_CAST_store
C3_main_corr_CAST_store = solver.IntVar(0, 1, 'C3_main_corr_CAST_store')
C4_main_corr_CAST_store = solver.IntVar(0, 1, 'C4_main_corr_CAST_store')
C5_main_corr_CAST_store = solver.IntVar(0, 1, 'C5_main_corr_CAST_store')
C6_main_corr_CAST_store = solver.IntVar(0, 1, 'C6_main_corr_CAST_store')
C7_main_corr_CAST_store = solver.IntVar(0, 1, 'C7_main_corr_CAST_store')
C8_main_corr_CAST_store = solver.IntVar(0, 1, 'C8_main_corr_CAST_store')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_store_float + (-1)*C3_main_corr_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_corr_CAST_store
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_store_fixp + (-1)*C4_main_corr_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_corr_CAST_store
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_store_double + (-1)*C5_main_corr_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_corr_CAST_store
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_store_fixp + (-1)*C6_main_corr_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_corr_CAST_store
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_store_double + (-1)*C7_main_corr_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_corr_CAST_store
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_store_float + (-1)*C8_main_corr_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_corr_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*main_corr_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*main_corr_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*main_corr_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_corr_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_corr_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_corr_enob_storeENOB_storeENOB + (-1)*main_corr_fixbits + (10000)*main_corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_corr_enob_storeENOB_storeENOB + (10000)*main_corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_corr_enob_storeENOB_storeENOB + (10000)*main_corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_corr_enob_storeENOB_storeENOB + (-1)*main_corr_enob_memphi_main_tmp19<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for double 1.000000e+00
ConstantValue__23_fixbits = solver.IntVar(0, 31, 'ConstantValue__23_fixbits')
ConstantValue__23_fixp = solver.IntVar(0, 1, 'ConstantValue__23_fixp')
ConstantValue__23_float = solver.IntVar(0, 1, 'ConstantValue__23_float')
ConstantValue__23_double = solver.IntVar(0, 1, 'ConstantValue__23_double')
ConstantValue__23_enob = solver.IntVar(-10000, 10000, 'ConstantValue__23_enob')
solver.Add( + (1)*ConstantValue__23_enob + (-1)*ConstantValue__23_fixbits + (10000)*ConstantValue__23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__23_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_float + (1)*ConstantValue__23_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__24_fixbits = solver.IntVar(0, 31, 'ConstantValue__24_fixbits')
ConstantValue__24_fixp = solver.IntVar(0, 1, 'ConstantValue__24_fixp')
ConstantValue__24_float = solver.IntVar(0, 1, 'ConstantValue__24_float')
ConstantValue__24_double = solver.IntVar(0, 1, 'ConstantValue__24_double')
ConstantValue__24_enob = solver.IntVar(-10000, 10000, 'ConstantValue__24_enob')
solver.Add( + (1)*ConstantValue__24_enob + (-1)*ConstantValue__24_fixbits + (10000)*ConstantValue__24_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__24_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__24_fixp + (1)*ConstantValue__24_float + (1)*ConstantValue__24_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx177, align 8, !taffo.info !17, !taffo.initweight !25, !taffo.constinfo !43
ConstantValue__24_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__24_CAST_store_fixbits')
ConstantValue__24_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__24_CAST_store_fixp')
ConstantValue__24_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__24_CAST_store_float')
ConstantValue__24_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__24_CAST_store_double')
solver.Add( + (1)*ConstantValue__24_CAST_store_fixp + (1)*ConstantValue__24_CAST_store_float + (1)*ConstantValue__24_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__24_CAST_store_fixbits + (-10000)*ConstantValue__24_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__24_CAST_store')
C2_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__24_CAST_store')
solver.Add( + (1)*ConstantValue__24_fixbits + (-1)*ConstantValue__24_CAST_store_fixbits + (-10000)*C1_ConstantValue__24_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__24_fixbits + (1)*ConstantValue__24_CAST_store_fixbits + (-10000)*C2_ConstantValue__24_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__24_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__24_CAST_store
C3_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__24_CAST_store')
C4_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__24_CAST_store')
C5_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__24_CAST_store')
C6_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__24_CAST_store')
C7_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__24_CAST_store')
C8_ConstantValue__24_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__24_CAST_store')
solver.Add( + (1)*ConstantValue__24_fixp + (1)*ConstantValue__24_CAST_store_float + (-1)*C3_ConstantValue__24_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__24_CAST_store
solver.Add( + (1)*ConstantValue__24_float + (1)*ConstantValue__24_CAST_store_fixp + (-1)*C4_ConstantValue__24_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__24_CAST_store
solver.Add( + (1)*ConstantValue__24_fixp + (1)*ConstantValue__24_CAST_store_double + (-1)*C5_ConstantValue__24_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__24_CAST_store
solver.Add( + (1)*ConstantValue__24_double + (1)*ConstantValue__24_CAST_store_fixp + (-1)*C6_ConstantValue__24_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__24_CAST_store
solver.Add( + (1)*ConstantValue__24_float + (1)*ConstantValue__24_CAST_store_double + (-1)*C7_ConstantValue__24_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__24_CAST_store
solver.Add( + (1)*ConstantValue__24_double + (1)*ConstantValue__24_CAST_store_float + (-1)*C8_ConstantValue__24_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__24_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__24_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__24_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__24_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__24_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp20 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp20')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp20 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call190 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.9, i32 0, i32 0), double %tmp20), !taffo.info !17, !taffo.initweight !28, !taffo.constinfo !46
main_corr_CAST_call190_fixbits = solver.IntVar(0, 29, 'main_corr_CAST_call190_fixbits')
main_corr_CAST_call190_fixp = solver.IntVar(0, 1, 'main_corr_CAST_call190_fixp')
main_corr_CAST_call190_float = solver.IntVar(0, 1, 'main_corr_CAST_call190_float')
main_corr_CAST_call190_double = solver.IntVar(0, 1, 'main_corr_CAST_call190_double')
solver.Add( + (1)*main_corr_CAST_call190_fixp + (1)*main_corr_CAST_call190_float + (1)*main_corr_CAST_call190_double==1)    #exactly 1 type
solver.Add( + (1)*main_corr_CAST_call190_fixbits + (-10000)*main_corr_CAST_call190_fixp<=0)    #If no fix, fix frac part = 0
C1_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C1_main_corr_CAST_call190')
C2_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C2_main_corr_CAST_call190')
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_call190_fixbits + (-10000)*C1_main_corr_CAST_call190<=0)    #Shift cost 1
solver.Add( + (-1)*main_corr_fixbits + (1)*main_corr_CAST_call190_fixbits + (-10000)*C2_main_corr_CAST_call190<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_corr_CAST_call190
castCostObj +=  + (1)*C2_main_corr_CAST_call190
C3_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C3_main_corr_CAST_call190')
C4_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C4_main_corr_CAST_call190')
C5_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C5_main_corr_CAST_call190')
C6_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C6_main_corr_CAST_call190')
C7_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C7_main_corr_CAST_call190')
C8_main_corr_CAST_call190 = solver.IntVar(0, 1, 'C8_main_corr_CAST_call190')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_call190_float + (-1)*C3_main_corr_CAST_call190<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_corr_CAST_call190
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_call190_fixp + (-1)*C4_main_corr_CAST_call190<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_corr_CAST_call190
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_call190_double + (-1)*C5_main_corr_CAST_call190<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_corr_CAST_call190
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_call190_fixp + (-1)*C6_main_corr_CAST_call190<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_corr_CAST_call190
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_call190_double + (-1)*C7_main_corr_CAST_call190<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_corr_CAST_call190
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_call190_float + (-1)*C8_main_corr_CAST_call190<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_corr_CAST_call190
solver.Add( + (1)*main_corr_CAST_call190_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(50 * castCostObj / 716.478+ 50 * enobCostObj / 5484+ 50 * mathCostObj / 112.661)

# Model declaration end.