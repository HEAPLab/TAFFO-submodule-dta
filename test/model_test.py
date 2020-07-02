


#Stuff for   %mean = alloca [32 x double], align 16, !taffo.info !13, !taffo.initweight !16
main_mean_fixbits = solver.IntVar(0, 15, 'main_mean_fixbits')
main_mean_fixp = solver.IntVar(0, 1, 'main_mean_fixp')
main_mean_float = solver.IntVar(0, 1, 'main_mean_float')
main_mean_double = solver.IntVar(0, 1, 'main_mean_double')
main_mean_enob = solver.IntVar(-10000, 10000, 'main_mean_enob')
solver.Add( + (1)*main_mean_enob + (-1)*main_mean_fixbits + (10000)*main_mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mean_enob + (10000)*main_mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mean_enob + (10000)*main_mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mean_fixbits + (-10000)*main_mean_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_mean_enob<=4)    #Enob constraint for error maximal
objectiveFunction =  + (-1)*main_mean_enob
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_float + (1)*main_mean_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mean_fixbits + (-10000)*main_mean_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %data = alloca [28 x [32 x double]], align 16, !taffo.info !17, !taffo.initweight !16
main_data_fixbits = solver.IntVar(0, 30, 'main_data_fixbits')
main_data_fixp = solver.IntVar(0, 1, 'main_data_fixp')
main_data_float = solver.IntVar(0, 1, 'main_data_float')
main_data_double = solver.IntVar(0, 1, 'main_data_double')
main_data_enob = solver.IntVar(-10000, 10000, 'main_data_enob')
solver.Add( + (1)*main_data_enob + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_fixbits + (-10000)*main_data_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_data_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_data_enob
solver.Add( + (1)*main_data_fixp + (1)*main_data_float + (1)*main_data_double==1)    #Exactly one selected type
solver.Add( + (1)*main_data_fixbits + (-10000)*main_data_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %corr = alloca [32 x [32 x double]], align 16, !taffo.info !19, !taffo.initweight !16
main_corr_fixbits = solver.IntVar(0, 29, 'main_corr_fixbits')
main_corr_fixp = solver.IntVar(0, 1, 'main_corr_fixp')
main_corr_float = solver.IntVar(0, 1, 'main_corr_float')
main_corr_double = solver.IntVar(0, 1, 'main_corr_double')
main_corr_enob = solver.IntVar(-10000, 10000, 'main_corr_enob')
solver.Add( + (1)*main_corr_enob + (-1)*main_corr_fixbits + (10000)*main_corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_corr_enob + (10000)*main_corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_corr_enob + (10000)*main_corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_corr_fixbits + (-10000)*main_corr_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_corr_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_corr_enob
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_float + (1)*main_corr_double==1)    #Exactly one selected type
solver.Add( + (1)*main_corr_fixbits + (-10000)*main_corr_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %stddev = alloca [32 x double], align 16, !taffo.info !21, !taffo.initweight !16
main_stddev_fixbits = solver.IntVar(0, 18, 'main_stddev_fixbits')
main_stddev_fixp = solver.IntVar(0, 1, 'main_stddev_fixp')
main_stddev_float = solver.IntVar(0, 1, 'main_stddev_float')
main_stddev_double = solver.IntVar(0, 1, 'main_stddev_double')
main_stddev_enob = solver.IntVar(-10000, 10000, 'main_stddev_enob')
solver.Add( + (1)*main_stddev_enob + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_fixbits + (-10000)*main_stddev_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_stddev_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_stddev_enob
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



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx25, align 8, !taffo.info !13, !taffo.initweight !26, !taffo.constinfo !38
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
objectiveFunction +=  + (50)*C1_ConstantValue__4_CAST_store
objectiveFunction +=  + (50)*C2_ConstantValue__4_CAST_store
C3_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_store')
C4_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_store')
C5_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_store')
C6_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_store')
C7_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_store')
C8_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_store')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_float + (-1)*C3_ConstantValue__4_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_fixp + (-1)*C4_ConstantValue__4_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_double + (-1)*C5_ConstantValue__4_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_fixp + (-1)*C6_ConstantValue__4_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_double + (-1)*C7_ConstantValue__4_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_float + (-1)*C8_ConstantValue__4_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__4_CAST_store
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



#Constraint for cast for   %add36 = fadd double %tmp1, %tmp, !taffo.info !13, !taffo.initweight !27
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
objectiveFunction +=  + (50)*C1_main_mean_CAST_add36
objectiveFunction +=  + (50)*C2_main_mean_CAST_add36
C3_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C3_main_mean_CAST_add36')
C4_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C4_main_mean_CAST_add36')
C5_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C5_main_mean_CAST_add36')
C6_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C6_main_mean_CAST_add36')
C7_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C7_main_mean_CAST_add36')
C8_main_mean_CAST_add36 = solver.IntVar(0, 1, 'C8_main_mean_CAST_add36')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_add36_float + (-1)*C3_main_mean_CAST_add36<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mean_CAST_add36
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_add36_fixp + (-1)*C4_main_mean_CAST_add36<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mean_CAST_add36
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_add36_double + (-1)*C5_main_mean_CAST_add36<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mean_CAST_add36
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_add36_fixp + (-1)*C6_main_mean_CAST_add36<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mean_CAST_add36
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_add36_double + (-1)*C7_main_mean_CAST_add36<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mean_CAST_add36
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_add36_float + (-1)*C8_main_mean_CAST_add36<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mean_CAST_add36



#Constraint for cast for   %add36 = fadd double %tmp1, %tmp, !taffo.info !13, !taffo.initweight !27
main_data_CAST_add36_fixbits = solver.IntVar(0, 30, 'main_data_CAST_add36_fixbits')
main_data_CAST_add36_fixp = solver.IntVar(0, 1, 'main_data_CAST_add36_fixp')
main_data_CAST_add36_float = solver.IntVar(0, 1, 'main_data_CAST_add36_float')
main_data_CAST_add36_double = solver.IntVar(0, 1, 'main_data_CAST_add36_double')
solver.Add( + (1)*main_data_CAST_add36_fixp + (1)*main_data_CAST_add36_float + (1)*main_data_CAST_add36_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_add36_fixbits + (-10000)*main_data_CAST_add36_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_add36 = solver.IntVar(0, 1, 'C1_main_data_CAST_add36')
C2_main_data_CAST_add36 = solver.IntVar(0, 1, 'C2_main_data_CAST_add36')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_add36_fixbits + (-10000)*C1_main_data_CAST_add36<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_add36_fixbits + (-10000)*C2_main_data_CAST_add36<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_add36
objectiveFunction +=  + (50)*C2_main_data_CAST_add36
C3_main_data_CAST_add36 = solver.IntVar(0, 1, 'C3_main_data_CAST_add36')
C4_main_data_CAST_add36 = solver.IntVar(0, 1, 'C4_main_data_CAST_add36')
C5_main_data_CAST_add36 = solver.IntVar(0, 1, 'C5_main_data_CAST_add36')
C6_main_data_CAST_add36 = solver.IntVar(0, 1, 'C6_main_data_CAST_add36')
C7_main_data_CAST_add36 = solver.IntVar(0, 1, 'C7_main_data_CAST_add36')
C8_main_data_CAST_add36 = solver.IntVar(0, 1, 'C8_main_data_CAST_add36')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_add36_float + (-1)*C3_main_data_CAST_add36<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_add36
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_add36_fixp + (-1)*C4_main_data_CAST_add36<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_add36
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_add36_double + (-1)*C5_main_data_CAST_add36<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_add36
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_add36_fixp + (-1)*C6_main_data_CAST_add36<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_add36
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_add36_double + (-1)*C7_main_data_CAST_add36<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_add36
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_add36_float + (-1)*C8_main_data_CAST_add36<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_add36



#Stuff for   %add36 = fadd double %tmp1, %tmp, !taffo.info !13, !taffo.initweight !27
main_add36_fixbits = solver.IntVar(0, 15, 'main_add36_fixbits')
main_add36_fixp = solver.IntVar(0, 1, 'main_add36_fixp')
main_add36_float = solver.IntVar(0, 1, 'main_add36_float')
main_add36_double = solver.IntVar(0, 1, 'main_add36_double')
main_add36_enob = solver.IntVar(-10000, 10000, 'main_add36_enob')
solver.Add( + (1)*main_add36_enob + (-1)*main_add36_fixbits + (10000)*main_add36_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add36_enob + (10000)*main_add36_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add36_enob + (10000)*main_add36_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add36_fixbits + (-10000)*main_add36_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add36_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_add36_enob
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
objectiveFunction +=  + (127.246)*main_add36_fixp
objectiveFunction +=  + (300)*main_add36_float
objectiveFunction +=  + (664.928)*main_add36_double
solver.Add( + (1)*main_add36_enob + (-1)*main_mean_enob_memphi_main_tmp1<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add36_enob + (-1)*main_data_enob_memphi_main_tmp<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add36, double* %arrayidx35, align 8, !taffo.info !13, !taffo.initweight !26
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
objectiveFunction +=  + (50)*C1_main_add36_CAST_store
objectiveFunction +=  + (50)*C2_main_add36_CAST_store
C3_main_add36_CAST_store = solver.IntVar(0, 1, 'C3_main_add36_CAST_store')
C4_main_add36_CAST_store = solver.IntVar(0, 1, 'C4_main_add36_CAST_store')
C5_main_add36_CAST_store = solver.IntVar(0, 1, 'C5_main_add36_CAST_store')
C6_main_add36_CAST_store = solver.IntVar(0, 1, 'C6_main_add36_CAST_store')
C7_main_add36_CAST_store = solver.IntVar(0, 1, 'C7_main_add36_CAST_store')
C8_main_add36_CAST_store = solver.IntVar(0, 1, 'C8_main_add36_CAST_store')
solver.Add( + (1)*main_add36_fixp + (1)*main_add36_CAST_store_float + (-1)*C3_main_add36_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_add36_CAST_store
solver.Add( + (1)*main_add36_float + (1)*main_add36_CAST_store_fixp + (-1)*C4_main_add36_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_add36_CAST_store
solver.Add( + (1)*main_add36_fixp + (1)*main_add36_CAST_store_double + (-1)*C5_main_add36_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_add36_CAST_store
solver.Add( + (1)*main_add36_double + (1)*main_add36_CAST_store_fixp + (-1)*C6_main_add36_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_add36_CAST_store
solver.Add( + (1)*main_add36_float + (1)*main_add36_CAST_store_double + (-1)*C7_main_add36_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_add36_CAST_store
solver.Add( + (1)*main_add36_double + (1)*main_add36_CAST_store_float + (-1)*C8_main_add36_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_add36_CAST_store
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



#Stuff for   %conv40 = sitofp i32 28 to double, !taffo.info !41, !taffo.initweight !26
main_conv40_fixbits = solver.IntVar(0, 20, 'main_conv40_fixbits')
main_conv40_fixp = solver.IntVar(0, 1, 'main_conv40_fixp')
main_conv40_float = solver.IntVar(0, 1, 'main_conv40_float')
main_conv40_double = solver.IntVar(0, 1, 'main_conv40_double')
main_conv40_enob = solver.IntVar(-10000, 10000, 'main_conv40_enob')
solver.Add( + (1)*main_conv40_enob + (-1)*main_conv40_fixbits + (10000)*main_conv40_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv40_enob + (10000)*main_conv40_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_conv40_enob + (10000)*main_conv40_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_conv40_fixbits + (-10000)*main_conv40_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_conv40_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_conv40_enob
solver.Add( + (1)*main_conv40_fixp + (1)*main_conv40_float + (1)*main_conv40_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv40_fixbits + (-10000)*main_conv40_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
main_mean_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_mean_enob_memphi_main_tmp2')
solver.Add( + (1)*main_mean_enob_memphi_main_tmp2 + (-1)*main_mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
solver.Add( + (1)*main_main_tmp2_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_mean_enob_memphi_main_tmp2 + (-1)*main_mean_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div43 = fdiv double %tmp2, %conv40, !taffo.info !13, !taffo.initweight !27
main_mean_CAST_div43_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_div43_fixbits')
main_mean_CAST_div43_fixp = solver.IntVar(0, 1, 'main_mean_CAST_div43_fixp')
main_mean_CAST_div43_float = solver.IntVar(0, 1, 'main_mean_CAST_div43_float')
main_mean_CAST_div43_double = solver.IntVar(0, 1, 'main_mean_CAST_div43_double')
solver.Add( + (1)*main_mean_CAST_div43_fixp + (1)*main_mean_CAST_div43_float + (1)*main_mean_CAST_div43_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_div43_fixbits + (-10000)*main_mean_CAST_div43_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C1_main_mean_CAST_div43')
C2_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C2_main_mean_CAST_div43')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_div43_fixbits + (-10000)*C1_main_mean_CAST_div43<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_div43_fixbits + (-10000)*C2_main_mean_CAST_div43<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mean_CAST_div43
objectiveFunction +=  + (50)*C2_main_mean_CAST_div43
C3_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C3_main_mean_CAST_div43')
C4_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C4_main_mean_CAST_div43')
C5_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C5_main_mean_CAST_div43')
C6_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C6_main_mean_CAST_div43')
C7_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C7_main_mean_CAST_div43')
C8_main_mean_CAST_div43 = solver.IntVar(0, 1, 'C8_main_mean_CAST_div43')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_div43_float + (-1)*C3_main_mean_CAST_div43<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mean_CAST_div43
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_div43_fixp + (-1)*C4_main_mean_CAST_div43<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mean_CAST_div43
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_div43_double + (-1)*C5_main_mean_CAST_div43<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mean_CAST_div43
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_div43_fixp + (-1)*C6_main_mean_CAST_div43<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mean_CAST_div43
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_div43_double + (-1)*C7_main_mean_CAST_div43<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mean_CAST_div43
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_div43_float + (-1)*C8_main_mean_CAST_div43<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mean_CAST_div43



#Constraint for cast for   %div43 = fdiv double %tmp2, %conv40, !taffo.info !13, !taffo.initweight !27
main_conv40_CAST_div43_fixbits = solver.IntVar(0, 20, 'main_conv40_CAST_div43_fixbits')
main_conv40_CAST_div43_fixp = solver.IntVar(0, 1, 'main_conv40_CAST_div43_fixp')
main_conv40_CAST_div43_float = solver.IntVar(0, 1, 'main_conv40_CAST_div43_float')
main_conv40_CAST_div43_double = solver.IntVar(0, 1, 'main_conv40_CAST_div43_double')
solver.Add( + (1)*main_conv40_CAST_div43_fixp + (1)*main_conv40_CAST_div43_float + (1)*main_conv40_CAST_div43_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv40_CAST_div43_fixbits + (-10000)*main_conv40_CAST_div43_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C1_main_conv40_CAST_div43')
C2_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C2_main_conv40_CAST_div43')
solver.Add( + (1)*main_conv40_fixbits + (-1)*main_conv40_CAST_div43_fixbits + (-10000)*C1_main_conv40_CAST_div43<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv40_fixbits + (1)*main_conv40_CAST_div43_fixbits + (-10000)*C2_main_conv40_CAST_div43<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_conv40_CAST_div43
objectiveFunction +=  + (50)*C2_main_conv40_CAST_div43
C3_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C3_main_conv40_CAST_div43')
C4_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C4_main_conv40_CAST_div43')
C5_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C5_main_conv40_CAST_div43')
C6_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C6_main_conv40_CAST_div43')
C7_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C7_main_conv40_CAST_div43')
C8_main_conv40_CAST_div43 = solver.IntVar(0, 1, 'C8_main_conv40_CAST_div43')
solver.Add( + (1)*main_conv40_fixp + (1)*main_conv40_CAST_div43_float + (-1)*C3_main_conv40_CAST_div43<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_conv40_CAST_div43
solver.Add( + (1)*main_conv40_float + (1)*main_conv40_CAST_div43_fixp + (-1)*C4_main_conv40_CAST_div43<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_conv40_CAST_div43
solver.Add( + (1)*main_conv40_fixp + (1)*main_conv40_CAST_div43_double + (-1)*C5_main_conv40_CAST_div43<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_conv40_CAST_div43
solver.Add( + (1)*main_conv40_double + (1)*main_conv40_CAST_div43_fixp + (-1)*C6_main_conv40_CAST_div43<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_conv40_CAST_div43
solver.Add( + (1)*main_conv40_float + (1)*main_conv40_CAST_div43_double + (-1)*C7_main_conv40_CAST_div43<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_conv40_CAST_div43
solver.Add( + (1)*main_conv40_double + (1)*main_conv40_CAST_div43_float + (-1)*C8_main_conv40_CAST_div43<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_conv40_CAST_div43



#Stuff for   %div43 = fdiv double %tmp2, %conv40, !taffo.info !13, !taffo.initweight !27
main_div43_fixbits = solver.IntVar(0, 15, 'main_div43_fixbits')
main_div43_fixp = solver.IntVar(0, 1, 'main_div43_fixp')
main_div43_float = solver.IntVar(0, 1, 'main_div43_float')
main_div43_double = solver.IntVar(0, 1, 'main_div43_double')
main_div43_enob = solver.IntVar(-10000, 10000, 'main_div43_enob')
solver.Add( + (1)*main_div43_enob + (-1)*main_div43_fixbits + (10000)*main_div43_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div43_enob + (10000)*main_div43_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div43_enob + (10000)*main_div43_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div43_fixbits + (-10000)*main_div43_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_div43_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_div43_enob
solver.Add( + (1)*main_div43_fixp + (1)*main_div43_float + (1)*main_div43_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div43_fixbits + (-10000)*main_div43_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mean_CAST_div43_fixp + (-1)*main_conv40_CAST_div43_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_div43_float + (-1)*main_conv40_CAST_div43_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_div43_double + (-1)*main_conv40_CAST_div43_double==0)    #double equality
solver.Add( + (1)*main_mean_CAST_div43_fixp + (-1)*main_div43_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_CAST_div43_float + (-1)*main_div43_float==0)    #float equality
solver.Add( + (1)*main_mean_CAST_div43_double + (-1)*main_div43_double==0)    #double equality
objectiveFunction +=  + (161.159)*main_div43_fixp
objectiveFunction +=  + (600)*main_div43_float
objectiveFunction +=  + (1200)*main_div43_double
main_main_div43_enob_1 = solver.IntVar(0, 1, 'main_main_div43_enob_1')
main_main_div43_enob_2 = solver.IntVar(0, 1, 'main_main_div43_enob_2')
solver.Add( + (1)*main_main_div43_enob_1 + (1)*main_main_div43_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div43_enob + (-1)*main_conv40_enob + (-10000)*main_main_div43_enob_1<=1048)    #Enob: propagation in division 1
solver.Add( + (1)*main_div43_enob + (-1)*main_mean_enob_memphi_main_tmp2 + (-10000)*main_main_div43_enob_2<=24)    #Enob: propagation in division 2



#Constraint for cast for   store double %div43, double* %arrayidx42, align 8, !taffo.info !13, !taffo.initweight !26
main_div43_CAST_store_fixbits = solver.IntVar(0, 15, 'main_div43_CAST_store_fixbits')
main_div43_CAST_store_fixp = solver.IntVar(0, 1, 'main_div43_CAST_store_fixp')
main_div43_CAST_store_float = solver.IntVar(0, 1, 'main_div43_CAST_store_float')
main_div43_CAST_store_double = solver.IntVar(0, 1, 'main_div43_CAST_store_double')
solver.Add( + (1)*main_div43_CAST_store_fixp + (1)*main_div43_CAST_store_float + (1)*main_div43_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div43_CAST_store_fixbits + (-10000)*main_div43_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div43_CAST_store = solver.IntVar(0, 1, 'C1_main_div43_CAST_store')
C2_main_div43_CAST_store = solver.IntVar(0, 1, 'C2_main_div43_CAST_store')
solver.Add( + (1)*main_div43_fixbits + (-1)*main_div43_CAST_store_fixbits + (-10000)*C1_main_div43_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div43_fixbits + (1)*main_div43_CAST_store_fixbits + (-10000)*C2_main_div43_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_div43_CAST_store
objectiveFunction +=  + (50)*C2_main_div43_CAST_store
C3_main_div43_CAST_store = solver.IntVar(0, 1, 'C3_main_div43_CAST_store')
C4_main_div43_CAST_store = solver.IntVar(0, 1, 'C4_main_div43_CAST_store')
C5_main_div43_CAST_store = solver.IntVar(0, 1, 'C5_main_div43_CAST_store')
C6_main_div43_CAST_store = solver.IntVar(0, 1, 'C6_main_div43_CAST_store')
C7_main_div43_CAST_store = solver.IntVar(0, 1, 'C7_main_div43_CAST_store')
C8_main_div43_CAST_store = solver.IntVar(0, 1, 'C8_main_div43_CAST_store')
solver.Add( + (1)*main_div43_fixp + (1)*main_div43_CAST_store_float + (-1)*C3_main_div43_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_div43_CAST_store
solver.Add( + (1)*main_div43_float + (1)*main_div43_CAST_store_fixp + (-1)*C4_main_div43_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_div43_CAST_store
solver.Add( + (1)*main_div43_fixp + (1)*main_div43_CAST_store_double + (-1)*C5_main_div43_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_div43_CAST_store
solver.Add( + (1)*main_div43_double + (1)*main_div43_CAST_store_fixp + (-1)*C6_main_div43_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_div43_CAST_store
solver.Add( + (1)*main_div43_float + (1)*main_div43_CAST_store_double + (-1)*C7_main_div43_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_div43_CAST_store
solver.Add( + (1)*main_div43_double + (1)*main_div43_CAST_store_float + (-1)*C8_main_div43_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_div43_CAST_store
solver.Add( + (1)*main_mean_fixp + (-1)*main_div43_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_float + (-1)*main_div43_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_mean_double + (-1)*main_div43_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_mean_fixbits + (-1)*main_div43_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_mean_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_mean_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (-1)*main_mean_fixbits + (10000)*main_mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (10000)*main_mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mean_enob_storeENOB_storeENOB + (-1)*main_div43_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for double 0.000000e+00
ConstantValue__5_fixbits = solver.IntVar(0, 32, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__6_fixbits = solver.IntVar(0, 32, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx52, align 8, !taffo.info !21, !taffo.initweight !26, !taffo.constinfo !38
ConstantValue__6_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__6_CAST_store_fixbits')
ConstantValue__6_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__6_CAST_store_fixp')
ConstantValue__6_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__6_CAST_store_float')
ConstantValue__6_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__6_CAST_store_double')
solver.Add( + (1)*ConstantValue__6_CAST_store_fixp + (1)*ConstantValue__6_CAST_store_float + (1)*ConstantValue__6_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__6_CAST_store_fixbits + (-10000)*ConstantValue__6_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__6_CAST_store')
C2_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__6_CAST_store')
solver.Add( + (1)*ConstantValue__6_fixbits + (-1)*ConstantValue__6_CAST_store_fixbits + (-10000)*C1_ConstantValue__6_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__6_fixbits + (1)*ConstantValue__6_CAST_store_fixbits + (-10000)*C2_ConstantValue__6_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__6_CAST_store
objectiveFunction +=  + (50)*C2_ConstantValue__6_CAST_store
C3_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__6_CAST_store')
C4_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__6_CAST_store')
C5_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__6_CAST_store')
C6_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__6_CAST_store')
C7_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__6_CAST_store')
C8_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__6_CAST_store')
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_store_float + (-1)*C3_ConstantValue__6_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_store_fixp + (-1)*C4_ConstantValue__6_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_store_double + (-1)*C5_ConstantValue__6_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_store_fixp + (-1)*C6_ConstantValue__6_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_store_double + (-1)*C7_ConstantValue__6_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_store_float + (-1)*C8_ConstantValue__6_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__6_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*ConstantValue__6_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*ConstantValue__6_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*ConstantValue__6_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*ConstantValue__6_CAST_store_fixbits==0)    #same fractional bit

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



#Constraint for cast for   %sub = fsub double %tmp3, %tmp4, !taffo.info !13, !taffo.initweight !27
main_data_CAST_sub_fixbits = solver.IntVar(0, 30, 'main_data_CAST_sub_fixbits')
main_data_CAST_sub_fixp = solver.IntVar(0, 1, 'main_data_CAST_sub_fixp')
main_data_CAST_sub_float = solver.IntVar(0, 1, 'main_data_CAST_sub_float')
main_data_CAST_sub_double = solver.IntVar(0, 1, 'main_data_CAST_sub_double')
solver.Add( + (1)*main_data_CAST_sub_fixp + (1)*main_data_CAST_sub_float + (1)*main_data_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_sub_fixbits + (-10000)*main_data_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_sub = solver.IntVar(0, 1, 'C1_main_data_CAST_sub')
C2_main_data_CAST_sub = solver.IntVar(0, 1, 'C2_main_data_CAST_sub')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_sub_fixbits + (-10000)*C1_main_data_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_sub_fixbits + (-10000)*C2_main_data_CAST_sub<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_sub
objectiveFunction +=  + (50)*C2_main_data_CAST_sub
C3_main_data_CAST_sub = solver.IntVar(0, 1, 'C3_main_data_CAST_sub')
C4_main_data_CAST_sub = solver.IntVar(0, 1, 'C4_main_data_CAST_sub')
C5_main_data_CAST_sub = solver.IntVar(0, 1, 'C5_main_data_CAST_sub')
C6_main_data_CAST_sub = solver.IntVar(0, 1, 'C6_main_data_CAST_sub')
C7_main_data_CAST_sub = solver.IntVar(0, 1, 'C7_main_data_CAST_sub')
C8_main_data_CAST_sub = solver.IntVar(0, 1, 'C8_main_data_CAST_sub')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub_float + (-1)*C3_main_data_CAST_sub<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_sub
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub_fixp + (-1)*C4_main_data_CAST_sub<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_sub
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub_double + (-1)*C5_main_data_CAST_sub<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_sub
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub_fixp + (-1)*C6_main_data_CAST_sub<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_sub
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub_double + (-1)*C7_main_data_CAST_sub<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_sub
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub_float + (-1)*C8_main_data_CAST_sub<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_sub



#Constraint for cast for   %sub = fsub double %tmp3, %tmp4, !taffo.info !13, !taffo.initweight !27
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
objectiveFunction +=  + (50)*C1_main_mean_CAST_sub
objectiveFunction +=  + (50)*C2_main_mean_CAST_sub
C3_main_mean_CAST_sub = solver.IntVar(0, 1, 'C3_main_mean_CAST_sub')
C4_main_mean_CAST_sub = solver.IntVar(0, 1, 'C4_main_mean_CAST_sub')
C5_main_mean_CAST_sub = solver.IntVar(0, 1, 'C5_main_mean_CAST_sub')
C6_main_mean_CAST_sub = solver.IntVar(0, 1, 'C6_main_mean_CAST_sub')
C7_main_mean_CAST_sub = solver.IntVar(0, 1, 'C7_main_mean_CAST_sub')
C8_main_mean_CAST_sub = solver.IntVar(0, 1, 'C8_main_mean_CAST_sub')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub_float + (-1)*C3_main_mean_CAST_sub<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mean_CAST_sub
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub_fixp + (-1)*C4_main_mean_CAST_sub<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mean_CAST_sub
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub_double + (-1)*C5_main_mean_CAST_sub<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mean_CAST_sub
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub_fixp + (-1)*C6_main_mean_CAST_sub<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mean_CAST_sub
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub_double + (-1)*C7_main_mean_CAST_sub<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mean_CAST_sub
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub_float + (-1)*C8_main_mean_CAST_sub<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mean_CAST_sub



#Stuff for   %sub = fsub double %tmp3, %tmp4, !taffo.info !13, !taffo.initweight !27
main_sub_fixbits = solver.IntVar(0, 15, 'main_sub_fixbits')
main_sub_fixp = solver.IntVar(0, 1, 'main_sub_fixp')
main_sub_float = solver.IntVar(0, 1, 'main_sub_float')
main_sub_double = solver.IntVar(0, 1, 'main_sub_double')
main_sub_enob = solver.IntVar(-10000, 10000, 'main_sub_enob')
solver.Add( + (1)*main_sub_enob + (-1)*main_sub_fixbits + (10000)*main_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_sub_enob
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
objectiveFunction +=  + (127.246)*main_sub_fixp
objectiveFunction +=  + (300)*main_sub_float
objectiveFunction +=  + (664.928)*main_sub_double
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



#Constraint for cast for   %sub69 = fsub double %tmp5, %tmp6, !taffo.info !13, !taffo.initweight !27
main_data_CAST_sub69_fixbits = solver.IntVar(0, 30, 'main_data_CAST_sub69_fixbits')
main_data_CAST_sub69_fixp = solver.IntVar(0, 1, 'main_data_CAST_sub69_fixp')
main_data_CAST_sub69_float = solver.IntVar(0, 1, 'main_data_CAST_sub69_float')
main_data_CAST_sub69_double = solver.IntVar(0, 1, 'main_data_CAST_sub69_double')
solver.Add( + (1)*main_data_CAST_sub69_fixp + (1)*main_data_CAST_sub69_float + (1)*main_data_CAST_sub69_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_sub69_fixbits + (-10000)*main_data_CAST_sub69_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C1_main_data_CAST_sub69')
C2_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C2_main_data_CAST_sub69')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_sub69_fixbits + (-10000)*C1_main_data_CAST_sub69<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_sub69_fixbits + (-10000)*C2_main_data_CAST_sub69<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_sub69
objectiveFunction +=  + (50)*C2_main_data_CAST_sub69
C3_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C3_main_data_CAST_sub69')
C4_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C4_main_data_CAST_sub69')
C5_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C5_main_data_CAST_sub69')
C6_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C6_main_data_CAST_sub69')
C7_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C7_main_data_CAST_sub69')
C8_main_data_CAST_sub69 = solver.IntVar(0, 1, 'C8_main_data_CAST_sub69')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub69_float + (-1)*C3_main_data_CAST_sub69<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_sub69
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub69_fixp + (-1)*C4_main_data_CAST_sub69<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_sub69
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub69_double + (-1)*C5_main_data_CAST_sub69<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_sub69
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub69_fixp + (-1)*C6_main_data_CAST_sub69<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_sub69
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub69_double + (-1)*C7_main_data_CAST_sub69<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_sub69
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub69_float + (-1)*C8_main_data_CAST_sub69<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_sub69



#Constraint for cast for   %sub69 = fsub double %tmp5, %tmp6, !taffo.info !13, !taffo.initweight !27
main_mean_CAST_sub69_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_sub69_fixbits')
main_mean_CAST_sub69_fixp = solver.IntVar(0, 1, 'main_mean_CAST_sub69_fixp')
main_mean_CAST_sub69_float = solver.IntVar(0, 1, 'main_mean_CAST_sub69_float')
main_mean_CAST_sub69_double = solver.IntVar(0, 1, 'main_mean_CAST_sub69_double')
solver.Add( + (1)*main_mean_CAST_sub69_fixp + (1)*main_mean_CAST_sub69_float + (1)*main_mean_CAST_sub69_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_sub69_fixbits + (-10000)*main_mean_CAST_sub69_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C1_main_mean_CAST_sub69')
C2_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C2_main_mean_CAST_sub69')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_sub69_fixbits + (-10000)*C1_main_mean_CAST_sub69<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_sub69_fixbits + (-10000)*C2_main_mean_CAST_sub69<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mean_CAST_sub69
objectiveFunction +=  + (50)*C2_main_mean_CAST_sub69
C3_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C3_main_mean_CAST_sub69')
C4_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C4_main_mean_CAST_sub69')
C5_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C5_main_mean_CAST_sub69')
C6_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C6_main_mean_CAST_sub69')
C7_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C7_main_mean_CAST_sub69')
C8_main_mean_CAST_sub69 = solver.IntVar(0, 1, 'C8_main_mean_CAST_sub69')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub69_float + (-1)*C3_main_mean_CAST_sub69<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mean_CAST_sub69
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub69_fixp + (-1)*C4_main_mean_CAST_sub69<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mean_CAST_sub69
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub69_double + (-1)*C5_main_mean_CAST_sub69<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mean_CAST_sub69
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub69_fixp + (-1)*C6_main_mean_CAST_sub69<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mean_CAST_sub69
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub69_double + (-1)*C7_main_mean_CAST_sub69<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mean_CAST_sub69
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub69_float + (-1)*C8_main_mean_CAST_sub69<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mean_CAST_sub69



#Stuff for   %sub69 = fsub double %tmp5, %tmp6, !taffo.info !13, !taffo.initweight !27
main_sub69_fixbits = solver.IntVar(0, 15, 'main_sub69_fixbits')
main_sub69_fixp = solver.IntVar(0, 1, 'main_sub69_fixp')
main_sub69_float = solver.IntVar(0, 1, 'main_sub69_float')
main_sub69_double = solver.IntVar(0, 1, 'main_sub69_double')
main_sub69_enob = solver.IntVar(-10000, 10000, 'main_sub69_enob')
solver.Add( + (1)*main_sub69_enob + (-1)*main_sub69_fixbits + (10000)*main_sub69_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub69_enob + (10000)*main_sub69_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub69_enob + (10000)*main_sub69_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub69_fixbits + (-10000)*main_sub69_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub69_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_sub69_enob
solver.Add( + (1)*main_sub69_fixp + (1)*main_sub69_float + (1)*main_sub69_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub69_fixbits + (-10000)*main_sub69_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_sub69_fixp + (-1)*main_mean_CAST_sub69_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub69_float + (-1)*main_mean_CAST_sub69_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub69_double + (-1)*main_mean_CAST_sub69_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub69_fixbits + (-1)*main_mean_CAST_sub69_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_data_CAST_sub69_fixp + (-1)*main_sub69_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub69_float + (-1)*main_sub69_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub69_double + (-1)*main_sub69_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub69_fixbits + (-1)*main_sub69_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_sub69_fixp
objectiveFunction +=  + (300)*main_sub69_float
objectiveFunction +=  + (664.928)*main_sub69_double
solver.Add( + (1)*main_sub69_enob + (-1)*main_data_enob_memphi_main_tmp5<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub69_enob + (-1)*main_mean_enob_memphi_main_tmp6<=0)    #Enob propagation in sub second addend



#Constraint for cast for   %mul70 = fmul double %sub, %sub69, !taffo.info !13, !taffo.initweight !30
main_sub_CAST_mul70_fixbits = solver.IntVar(0, 15, 'main_sub_CAST_mul70_fixbits')
main_sub_CAST_mul70_fixp = solver.IntVar(0, 1, 'main_sub_CAST_mul70_fixp')
main_sub_CAST_mul70_float = solver.IntVar(0, 1, 'main_sub_CAST_mul70_float')
main_sub_CAST_mul70_double = solver.IntVar(0, 1, 'main_sub_CAST_mul70_double')
solver.Add( + (1)*main_sub_CAST_mul70_fixp + (1)*main_sub_CAST_mul70_float + (1)*main_sub_CAST_mul70_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub_CAST_mul70_fixbits + (-10000)*main_sub_CAST_mul70_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C1_main_sub_CAST_mul70')
C2_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C2_main_sub_CAST_mul70')
solver.Add( + (1)*main_sub_fixbits + (-1)*main_sub_CAST_mul70_fixbits + (-10000)*C1_main_sub_CAST_mul70<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub_fixbits + (1)*main_sub_CAST_mul70_fixbits + (-10000)*C2_main_sub_CAST_mul70<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_sub_CAST_mul70
objectiveFunction +=  + (50)*C2_main_sub_CAST_mul70
C3_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C3_main_sub_CAST_mul70')
C4_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C4_main_sub_CAST_mul70')
C5_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C5_main_sub_CAST_mul70')
C6_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C6_main_sub_CAST_mul70')
C7_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C7_main_sub_CAST_mul70')
C8_main_sub_CAST_mul70 = solver.IntVar(0, 1, 'C8_main_sub_CAST_mul70')
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_mul70_float + (-1)*C3_main_sub_CAST_mul70<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_sub_CAST_mul70
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_mul70_fixp + (-1)*C4_main_sub_CAST_mul70<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_sub_CAST_mul70
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_mul70_double + (-1)*C5_main_sub_CAST_mul70<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_sub_CAST_mul70
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_mul70_fixp + (-1)*C6_main_sub_CAST_mul70<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_sub_CAST_mul70
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_mul70_double + (-1)*C7_main_sub_CAST_mul70<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_sub_CAST_mul70
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_mul70_float + (-1)*C8_main_sub_CAST_mul70<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_sub_CAST_mul70



#Constraint for cast for   %mul70 = fmul double %sub, %sub69, !taffo.info !13, !taffo.initweight !30
main_sub69_CAST_mul70_fixbits = solver.IntVar(0, 15, 'main_sub69_CAST_mul70_fixbits')
main_sub69_CAST_mul70_fixp = solver.IntVar(0, 1, 'main_sub69_CAST_mul70_fixp')
main_sub69_CAST_mul70_float = solver.IntVar(0, 1, 'main_sub69_CAST_mul70_float')
main_sub69_CAST_mul70_double = solver.IntVar(0, 1, 'main_sub69_CAST_mul70_double')
solver.Add( + (1)*main_sub69_CAST_mul70_fixp + (1)*main_sub69_CAST_mul70_float + (1)*main_sub69_CAST_mul70_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub69_CAST_mul70_fixbits + (-10000)*main_sub69_CAST_mul70_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C1_main_sub69_CAST_mul70')
C2_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C2_main_sub69_CAST_mul70')
solver.Add( + (1)*main_sub69_fixbits + (-1)*main_sub69_CAST_mul70_fixbits + (-10000)*C1_main_sub69_CAST_mul70<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub69_fixbits + (1)*main_sub69_CAST_mul70_fixbits + (-10000)*C2_main_sub69_CAST_mul70<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_sub69_CAST_mul70
objectiveFunction +=  + (50)*C2_main_sub69_CAST_mul70
C3_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C3_main_sub69_CAST_mul70')
C4_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C4_main_sub69_CAST_mul70')
C5_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C5_main_sub69_CAST_mul70')
C6_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C6_main_sub69_CAST_mul70')
C7_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C7_main_sub69_CAST_mul70')
C8_main_sub69_CAST_mul70 = solver.IntVar(0, 1, 'C8_main_sub69_CAST_mul70')
solver.Add( + (1)*main_sub69_fixp + (1)*main_sub69_CAST_mul70_float + (-1)*C3_main_sub69_CAST_mul70<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_sub69_CAST_mul70
solver.Add( + (1)*main_sub69_float + (1)*main_sub69_CAST_mul70_fixp + (-1)*C4_main_sub69_CAST_mul70<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_sub69_CAST_mul70
solver.Add( + (1)*main_sub69_fixp + (1)*main_sub69_CAST_mul70_double + (-1)*C5_main_sub69_CAST_mul70<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_sub69_CAST_mul70
solver.Add( + (1)*main_sub69_double + (1)*main_sub69_CAST_mul70_fixp + (-1)*C6_main_sub69_CAST_mul70<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_sub69_CAST_mul70
solver.Add( + (1)*main_sub69_float + (1)*main_sub69_CAST_mul70_double + (-1)*C7_main_sub69_CAST_mul70<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_sub69_CAST_mul70
solver.Add( + (1)*main_sub69_double + (1)*main_sub69_CAST_mul70_float + (-1)*C8_main_sub69_CAST_mul70<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_sub69_CAST_mul70



#Stuff for   %mul70 = fmul double %sub, %sub69, !taffo.info !13, !taffo.initweight !30
main_mul70_fixbits = solver.IntVar(0, 15, 'main_mul70_fixbits')
main_mul70_fixp = solver.IntVar(0, 1, 'main_mul70_fixp')
main_mul70_float = solver.IntVar(0, 1, 'main_mul70_float')
main_mul70_double = solver.IntVar(0, 1, 'main_mul70_double')
main_mul70_enob = solver.IntVar(-10000, 10000, 'main_mul70_enob')
solver.Add( + (1)*main_mul70_enob + (-1)*main_mul70_fixbits + (10000)*main_mul70_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul70_enob + (10000)*main_mul70_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul70_enob + (10000)*main_mul70_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul70_fixbits + (-10000)*main_mul70_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_mul70_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_mul70_enob
solver.Add( + (1)*main_mul70_fixp + (1)*main_mul70_float + (1)*main_mul70_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul70_fixbits + (-10000)*main_mul70_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub_CAST_mul70_fixp + (-1)*main_sub69_CAST_mul70_fixp==0)    #fix equality
solver.Add( + (1)*main_sub_CAST_mul70_float + (-1)*main_sub69_CAST_mul70_float==0)    #float equality
solver.Add( + (1)*main_sub_CAST_mul70_double + (-1)*main_sub69_CAST_mul70_double==0)    #double equality
solver.Add( + (1)*main_sub_CAST_mul70_fixp + (-1)*main_mul70_fixp==0)    #fix equality
solver.Add( + (1)*main_sub_CAST_mul70_float + (-1)*main_mul70_float==0)    #float equality
solver.Add( + (1)*main_sub_CAST_mul70_double + (-1)*main_mul70_double==0)    #double equality
objectiveFunction +=  + (165.217)*main_mul70_fixp
objectiveFunction +=  + (600)*main_mul70_float
objectiveFunction +=  + (1225.51)*main_mul70_double
main_main_mul70_enob_1 = solver.IntVar(0, 1, 'main_main_mul70_enob_1')
main_main_mul70_enob_2 = solver.IntVar(0, 1, 'main_main_mul70_enob_2')
solver.Add( + (1)*main_main_mul70_enob_1 + (1)*main_main_mul70_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul70_enob + (-1)*main_sub69_enob + (-10000)*main_main_mul70_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul70_enob + (-1)*main_sub_enob + (-10000)*main_main_mul70_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp7')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp7 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
solver.Add( + (1)*main_main_tmp7_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add73 = fadd double %tmp7, %mul70, !taffo.info !21, !taffo.initweight !27
main_stddev_CAST_add73_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_add73_fixbits')
main_stddev_CAST_add73_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_add73_fixp')
main_stddev_CAST_add73_float = solver.IntVar(0, 1, 'main_stddev_CAST_add73_float')
main_stddev_CAST_add73_double = solver.IntVar(0, 1, 'main_stddev_CAST_add73_double')
solver.Add( + (1)*main_stddev_CAST_add73_fixp + (1)*main_stddev_CAST_add73_float + (1)*main_stddev_CAST_add73_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_add73_fixbits + (-10000)*main_stddev_CAST_add73_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_add73')
C2_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_add73')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_add73_fixbits + (-10000)*C1_main_stddev_CAST_add73<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_add73_fixbits + (-10000)*C2_main_stddev_CAST_add73<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_stddev_CAST_add73
objectiveFunction +=  + (50)*C2_main_stddev_CAST_add73
C3_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_add73')
C4_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_add73')
C5_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_add73')
C6_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_add73')
C7_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_add73')
C8_main_stddev_CAST_add73 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_add73')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_add73_float + (-1)*C3_main_stddev_CAST_add73<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_add73
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_add73_fixp + (-1)*C4_main_stddev_CAST_add73<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_add73
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_add73_double + (-1)*C5_main_stddev_CAST_add73<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_add73
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_add73_fixp + (-1)*C6_main_stddev_CAST_add73<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_add73
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_add73_double + (-1)*C7_main_stddev_CAST_add73<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_add73
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_add73_float + (-1)*C8_main_stddev_CAST_add73<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_add73



#Constraint for cast for   %add73 = fadd double %tmp7, %mul70, !taffo.info !21, !taffo.initweight !27
main_mul70_CAST_add73_fixbits = solver.IntVar(0, 15, 'main_mul70_CAST_add73_fixbits')
main_mul70_CAST_add73_fixp = solver.IntVar(0, 1, 'main_mul70_CAST_add73_fixp')
main_mul70_CAST_add73_float = solver.IntVar(0, 1, 'main_mul70_CAST_add73_float')
main_mul70_CAST_add73_double = solver.IntVar(0, 1, 'main_mul70_CAST_add73_double')
solver.Add( + (1)*main_mul70_CAST_add73_fixp + (1)*main_mul70_CAST_add73_float + (1)*main_mul70_CAST_add73_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul70_CAST_add73_fixbits + (-10000)*main_mul70_CAST_add73_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C1_main_mul70_CAST_add73')
C2_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C2_main_mul70_CAST_add73')
solver.Add( + (1)*main_mul70_fixbits + (-1)*main_mul70_CAST_add73_fixbits + (-10000)*C1_main_mul70_CAST_add73<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul70_fixbits + (1)*main_mul70_CAST_add73_fixbits + (-10000)*C2_main_mul70_CAST_add73<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mul70_CAST_add73
objectiveFunction +=  + (50)*C2_main_mul70_CAST_add73
C3_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C3_main_mul70_CAST_add73')
C4_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C4_main_mul70_CAST_add73')
C5_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C5_main_mul70_CAST_add73')
C6_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C6_main_mul70_CAST_add73')
C7_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C7_main_mul70_CAST_add73')
C8_main_mul70_CAST_add73 = solver.IntVar(0, 1, 'C8_main_mul70_CAST_add73')
solver.Add( + (1)*main_mul70_fixp + (1)*main_mul70_CAST_add73_float + (-1)*C3_main_mul70_CAST_add73<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mul70_CAST_add73
solver.Add( + (1)*main_mul70_float + (1)*main_mul70_CAST_add73_fixp + (-1)*C4_main_mul70_CAST_add73<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mul70_CAST_add73
solver.Add( + (1)*main_mul70_fixp + (1)*main_mul70_CAST_add73_double + (-1)*C5_main_mul70_CAST_add73<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mul70_CAST_add73
solver.Add( + (1)*main_mul70_double + (1)*main_mul70_CAST_add73_fixp + (-1)*C6_main_mul70_CAST_add73<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mul70_CAST_add73
solver.Add( + (1)*main_mul70_float + (1)*main_mul70_CAST_add73_double + (-1)*C7_main_mul70_CAST_add73<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mul70_CAST_add73
solver.Add( + (1)*main_mul70_double + (1)*main_mul70_CAST_add73_float + (-1)*C8_main_mul70_CAST_add73<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mul70_CAST_add73



#Stuff for   %add73 = fadd double %tmp7, %mul70, !taffo.info !21, !taffo.initweight !27
main_add73_fixbits = solver.IntVar(0, 18, 'main_add73_fixbits')
main_add73_fixp = solver.IntVar(0, 1, 'main_add73_fixp')
main_add73_float = solver.IntVar(0, 1, 'main_add73_float')
main_add73_double = solver.IntVar(0, 1, 'main_add73_double')
main_add73_enob = solver.IntVar(-10000, 10000, 'main_add73_enob')
solver.Add( + (1)*main_add73_enob + (-1)*main_add73_fixbits + (10000)*main_add73_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add73_enob + (10000)*main_add73_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add73_enob + (10000)*main_add73_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add73_fixbits + (-10000)*main_add73_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_add73_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_add73_enob
solver.Add( + (1)*main_add73_fixp + (1)*main_add73_float + (1)*main_add73_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add73_fixbits + (-10000)*main_add73_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_stddev_CAST_add73_fixp + (-1)*main_mul70_CAST_add73_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_add73_float + (-1)*main_mul70_CAST_add73_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_add73_double + (-1)*main_mul70_CAST_add73_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_add73_fixbits + (-1)*main_mul70_CAST_add73_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_stddev_CAST_add73_fixp + (-1)*main_add73_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_add73_float + (-1)*main_add73_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_add73_double + (-1)*main_add73_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_add73_fixbits + (-1)*main_add73_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_add73_fixp
objectiveFunction +=  + (300)*main_add73_float
objectiveFunction +=  + (664.928)*main_add73_double
solver.Add( + (1)*main_add73_enob + (-1)*main_stddev_enob_memphi_main_tmp7<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add73_enob + (-1)*main_mul70_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add73, double* %arrayidx72, align 8, !taffo.info !21, !taffo.initweight !26
main_add73_CAST_store_fixbits = solver.IntVar(0, 18, 'main_add73_CAST_store_fixbits')
main_add73_CAST_store_fixp = solver.IntVar(0, 1, 'main_add73_CAST_store_fixp')
main_add73_CAST_store_float = solver.IntVar(0, 1, 'main_add73_CAST_store_float')
main_add73_CAST_store_double = solver.IntVar(0, 1, 'main_add73_CAST_store_double')
solver.Add( + (1)*main_add73_CAST_store_fixp + (1)*main_add73_CAST_store_float + (1)*main_add73_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add73_CAST_store_fixbits + (-10000)*main_add73_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add73_CAST_store = solver.IntVar(0, 1, 'C1_main_add73_CAST_store')
C2_main_add73_CAST_store = solver.IntVar(0, 1, 'C2_main_add73_CAST_store')
solver.Add( + (1)*main_add73_fixbits + (-1)*main_add73_CAST_store_fixbits + (-10000)*C1_main_add73_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add73_fixbits + (1)*main_add73_CAST_store_fixbits + (-10000)*C2_main_add73_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_add73_CAST_store
objectiveFunction +=  + (50)*C2_main_add73_CAST_store
C3_main_add73_CAST_store = solver.IntVar(0, 1, 'C3_main_add73_CAST_store')
C4_main_add73_CAST_store = solver.IntVar(0, 1, 'C4_main_add73_CAST_store')
C5_main_add73_CAST_store = solver.IntVar(0, 1, 'C5_main_add73_CAST_store')
C6_main_add73_CAST_store = solver.IntVar(0, 1, 'C6_main_add73_CAST_store')
C7_main_add73_CAST_store = solver.IntVar(0, 1, 'C7_main_add73_CAST_store')
C8_main_add73_CAST_store = solver.IntVar(0, 1, 'C8_main_add73_CAST_store')
solver.Add( + (1)*main_add73_fixp + (1)*main_add73_CAST_store_float + (-1)*C3_main_add73_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_add73_CAST_store
solver.Add( + (1)*main_add73_float + (1)*main_add73_CAST_store_fixp + (-1)*C4_main_add73_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_add73_CAST_store
solver.Add( + (1)*main_add73_fixp + (1)*main_add73_CAST_store_double + (-1)*C5_main_add73_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_add73_CAST_store
solver.Add( + (1)*main_add73_double + (1)*main_add73_CAST_store_fixp + (-1)*C6_main_add73_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_add73_CAST_store
solver.Add( + (1)*main_add73_float + (1)*main_add73_CAST_store_double + (-1)*C7_main_add73_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_add73_CAST_store
solver.Add( + (1)*main_add73_double + (1)*main_add73_CAST_store_float + (-1)*C8_main_add73_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_add73_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*main_add73_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*main_add73_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*main_add73_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_add73_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_stddev_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_stddev_enob_storeENOB')
solver.Add( + (1)*main_stddev_enob_storeENOB + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob_storeENOB + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob_storeENOB + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_enob_storeENOB + (-1)*main_add73_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp7 + (-1)*main_stddev_enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %conv77 = sitofp i32 28 to double, !taffo.info !41, !taffo.initweight !26
main_conv77_fixbits = solver.IntVar(0, 20, 'main_conv77_fixbits')
main_conv77_fixp = solver.IntVar(0, 1, 'main_conv77_fixp')
main_conv77_float = solver.IntVar(0, 1, 'main_conv77_float')
main_conv77_double = solver.IntVar(0, 1, 'main_conv77_double')
main_conv77_enob = solver.IntVar(-10000, 10000, 'main_conv77_enob')
solver.Add( + (1)*main_conv77_enob + (-1)*main_conv77_fixbits + (10000)*main_conv77_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv77_enob + (10000)*main_conv77_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_conv77_enob + (10000)*main_conv77_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_conv77_fixbits + (-10000)*main_conv77_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_conv77_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_conv77_enob
solver.Add( + (1)*main_conv77_fixp + (1)*main_conv77_float + (1)*main_conv77_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv77_fixbits + (-10000)*main_conv77_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp8')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp8 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
solver.Add( + (1)*main_main_tmp8_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp8 + (-1)*main_stddev_enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div80 = fdiv double %tmp8, %conv77, !taffo.info !21, !taffo.initweight !27
main_stddev_CAST_div80_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_div80_fixbits')
main_stddev_CAST_div80_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_div80_fixp')
main_stddev_CAST_div80_float = solver.IntVar(0, 1, 'main_stddev_CAST_div80_float')
main_stddev_CAST_div80_double = solver.IntVar(0, 1, 'main_stddev_CAST_div80_double')
solver.Add( + (1)*main_stddev_CAST_div80_fixp + (1)*main_stddev_CAST_div80_float + (1)*main_stddev_CAST_div80_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_div80_fixbits + (-10000)*main_stddev_CAST_div80_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_div80')
C2_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_div80')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_div80_fixbits + (-10000)*C1_main_stddev_CAST_div80<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_div80_fixbits + (-10000)*C2_main_stddev_CAST_div80<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_stddev_CAST_div80
objectiveFunction +=  + (50)*C2_main_stddev_CAST_div80
C3_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_div80')
C4_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_div80')
C5_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_div80')
C6_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_div80')
C7_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_div80')
C8_main_stddev_CAST_div80 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_div80')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_div80_float + (-1)*C3_main_stddev_CAST_div80<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_div80
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_div80_fixp + (-1)*C4_main_stddev_CAST_div80<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_div80
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_div80_double + (-1)*C5_main_stddev_CAST_div80<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_div80
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_div80_fixp + (-1)*C6_main_stddev_CAST_div80<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_div80
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_div80_double + (-1)*C7_main_stddev_CAST_div80<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_div80
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_div80_float + (-1)*C8_main_stddev_CAST_div80<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_div80



#Constraint for cast for   %div80 = fdiv double %tmp8, %conv77, !taffo.info !21, !taffo.initweight !27
main_conv77_CAST_div80_fixbits = solver.IntVar(0, 20, 'main_conv77_CAST_div80_fixbits')
main_conv77_CAST_div80_fixp = solver.IntVar(0, 1, 'main_conv77_CAST_div80_fixp')
main_conv77_CAST_div80_float = solver.IntVar(0, 1, 'main_conv77_CAST_div80_float')
main_conv77_CAST_div80_double = solver.IntVar(0, 1, 'main_conv77_CAST_div80_double')
solver.Add( + (1)*main_conv77_CAST_div80_fixp + (1)*main_conv77_CAST_div80_float + (1)*main_conv77_CAST_div80_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv77_CAST_div80_fixbits + (-10000)*main_conv77_CAST_div80_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C1_main_conv77_CAST_div80')
C2_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C2_main_conv77_CAST_div80')
solver.Add( + (1)*main_conv77_fixbits + (-1)*main_conv77_CAST_div80_fixbits + (-10000)*C1_main_conv77_CAST_div80<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv77_fixbits + (1)*main_conv77_CAST_div80_fixbits + (-10000)*C2_main_conv77_CAST_div80<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_conv77_CAST_div80
objectiveFunction +=  + (50)*C2_main_conv77_CAST_div80
C3_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C3_main_conv77_CAST_div80')
C4_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C4_main_conv77_CAST_div80')
C5_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C5_main_conv77_CAST_div80')
C6_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C6_main_conv77_CAST_div80')
C7_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C7_main_conv77_CAST_div80')
C8_main_conv77_CAST_div80 = solver.IntVar(0, 1, 'C8_main_conv77_CAST_div80')
solver.Add( + (1)*main_conv77_fixp + (1)*main_conv77_CAST_div80_float + (-1)*C3_main_conv77_CAST_div80<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_conv77_CAST_div80
solver.Add( + (1)*main_conv77_float + (1)*main_conv77_CAST_div80_fixp + (-1)*C4_main_conv77_CAST_div80<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_conv77_CAST_div80
solver.Add( + (1)*main_conv77_fixp + (1)*main_conv77_CAST_div80_double + (-1)*C5_main_conv77_CAST_div80<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_conv77_CAST_div80
solver.Add( + (1)*main_conv77_double + (1)*main_conv77_CAST_div80_fixp + (-1)*C6_main_conv77_CAST_div80<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_conv77_CAST_div80
solver.Add( + (1)*main_conv77_float + (1)*main_conv77_CAST_div80_double + (-1)*C7_main_conv77_CAST_div80<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_conv77_CAST_div80
solver.Add( + (1)*main_conv77_double + (1)*main_conv77_CAST_div80_float + (-1)*C8_main_conv77_CAST_div80<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_conv77_CAST_div80



#Stuff for   %div80 = fdiv double %tmp8, %conv77, !taffo.info !21, !taffo.initweight !27
main_div80_fixbits = solver.IntVar(0, 18, 'main_div80_fixbits')
main_div80_fixp = solver.IntVar(0, 1, 'main_div80_fixp')
main_div80_float = solver.IntVar(0, 1, 'main_div80_float')
main_div80_double = solver.IntVar(0, 1, 'main_div80_double')
main_div80_enob = solver.IntVar(-10000, 10000, 'main_div80_enob')
solver.Add( + (1)*main_div80_enob + (-1)*main_div80_fixbits + (10000)*main_div80_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div80_enob + (10000)*main_div80_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div80_enob + (10000)*main_div80_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div80_fixbits + (-10000)*main_div80_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_div80_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_div80_enob
solver.Add( + (1)*main_div80_fixp + (1)*main_div80_float + (1)*main_div80_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div80_fixbits + (-10000)*main_div80_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_stddev_CAST_div80_fixp + (-1)*main_conv77_CAST_div80_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_div80_float + (-1)*main_conv77_CAST_div80_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_div80_double + (-1)*main_conv77_CAST_div80_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_div80_fixp + (-1)*main_div80_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_div80_float + (-1)*main_div80_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_div80_double + (-1)*main_div80_double==0)    #double equality
objectiveFunction +=  + (161.159)*main_div80_fixp
objectiveFunction +=  + (600)*main_div80_float
objectiveFunction +=  + (1200)*main_div80_double
main_main_div80_enob_1 = solver.IntVar(0, 1, 'main_main_div80_enob_1')
main_main_div80_enob_2 = solver.IntVar(0, 1, 'main_main_div80_enob_2')
solver.Add( + (1)*main_main_div80_enob_1 + (1)*main_main_div80_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div80_enob + (-1)*main_conv77_enob + (-10000)*main_main_div80_enob_1<=1048)    #Enob: propagation in division 1
solver.Add( + (1)*main_div80_enob + (-1)*main_stddev_enob_memphi_main_tmp8 + (-10000)*main_main_div80_enob_2<=24)    #Enob: propagation in division 2



#Constraint for cast for   store double %div80, double* %arrayidx79, align 8, !taffo.info !21, !taffo.initweight !26
main_div80_CAST_store_fixbits = solver.IntVar(0, 18, 'main_div80_CAST_store_fixbits')
main_div80_CAST_store_fixp = solver.IntVar(0, 1, 'main_div80_CAST_store_fixp')
main_div80_CAST_store_float = solver.IntVar(0, 1, 'main_div80_CAST_store_float')
main_div80_CAST_store_double = solver.IntVar(0, 1, 'main_div80_CAST_store_double')
solver.Add( + (1)*main_div80_CAST_store_fixp + (1)*main_div80_CAST_store_float + (1)*main_div80_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div80_CAST_store_fixbits + (-10000)*main_div80_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div80_CAST_store = solver.IntVar(0, 1, 'C1_main_div80_CAST_store')
C2_main_div80_CAST_store = solver.IntVar(0, 1, 'C2_main_div80_CAST_store')
solver.Add( + (1)*main_div80_fixbits + (-1)*main_div80_CAST_store_fixbits + (-10000)*C1_main_div80_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div80_fixbits + (1)*main_div80_CAST_store_fixbits + (-10000)*C2_main_div80_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_div80_CAST_store
objectiveFunction +=  + (50)*C2_main_div80_CAST_store
C3_main_div80_CAST_store = solver.IntVar(0, 1, 'C3_main_div80_CAST_store')
C4_main_div80_CAST_store = solver.IntVar(0, 1, 'C4_main_div80_CAST_store')
C5_main_div80_CAST_store = solver.IntVar(0, 1, 'C5_main_div80_CAST_store')
C6_main_div80_CAST_store = solver.IntVar(0, 1, 'C6_main_div80_CAST_store')
C7_main_div80_CAST_store = solver.IntVar(0, 1, 'C7_main_div80_CAST_store')
C8_main_div80_CAST_store = solver.IntVar(0, 1, 'C8_main_div80_CAST_store')
solver.Add( + (1)*main_div80_fixp + (1)*main_div80_CAST_store_float + (-1)*C3_main_div80_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_div80_CAST_store
solver.Add( + (1)*main_div80_float + (1)*main_div80_CAST_store_fixp + (-1)*C4_main_div80_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_div80_CAST_store
solver.Add( + (1)*main_div80_fixp + (1)*main_div80_CAST_store_double + (-1)*C5_main_div80_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_div80_CAST_store
solver.Add( + (1)*main_div80_double + (1)*main_div80_CAST_store_fixp + (-1)*C6_main_div80_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_div80_CAST_store
solver.Add( + (1)*main_div80_float + (1)*main_div80_CAST_store_double + (-1)*C7_main_div80_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_div80_CAST_store
solver.Add( + (1)*main_div80_double + (1)*main_div80_CAST_store_float + (-1)*C8_main_div80_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_div80_CAST_store
solver.Add( + (1)*main_stddev_fixp + (-1)*main_div80_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*main_div80_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*main_div80_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_div80_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_stddev_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_stddev_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (-1)*main_stddev_fixbits + (10000)*main_stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (10000)*main_stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (10000)*main_stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_stddev_enob_storeENOB_storeENOB + (-1)*main_div80_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp9')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp9 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
solver.Add( + (1)*main_main_tmp9_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp9 + (-1)*main_stddev_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %call = call double @sqrt(double %tmp9) #1, !taffo.info !21, !taffo.initweight !27, !taffo.constinfo !37
main_call_fixbits = solver.IntVar(0, 18, 'main_call_fixbits')
main_call_fixp = solver.IntVar(0, 1, 'main_call_fixp')
main_call_float = solver.IntVar(0, 1, 'main_call_float')
main_call_double = solver.IntVar(0, 1, 'main_call_double')
main_call_enob = solver.IntVar(-10000, 10000, 'main_call_enob')
solver.Add( + (1)*main_call_enob + (-1)*main_call_fixbits + (10000)*main_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call_enob + (10000)*main_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_call_enob + (10000)*main_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_call_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_call_enob
solver.Add( + (1)*main_call_fixp + (1)*main_call_float + (1)*main_call_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call_double==1)    #Type constraint for return value



#Constraint for cast for   %call = call double @sqrt(double %tmp9) #1, !taffo.info !21, !taffo.initweight !27, !taffo.constinfo !37
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
objectiveFunction +=  + (50)*C1_main_stddev_CAST_call
objectiveFunction +=  + (50)*C2_main_stddev_CAST_call
C3_main_stddev_CAST_call = solver.IntVar(0, 1, 'C3_main_stddev_CAST_call')
C4_main_stddev_CAST_call = solver.IntVar(0, 1, 'C4_main_stddev_CAST_call')
C5_main_stddev_CAST_call = solver.IntVar(0, 1, 'C5_main_stddev_CAST_call')
C6_main_stddev_CAST_call = solver.IntVar(0, 1, 'C6_main_stddev_CAST_call')
C7_main_stddev_CAST_call = solver.IntVar(0, 1, 'C7_main_stddev_CAST_call')
C8_main_stddev_CAST_call = solver.IntVar(0, 1, 'C8_main_stddev_CAST_call')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_call_float + (-1)*C3_main_stddev_CAST_call<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_call_fixp + (-1)*C4_main_stddev_CAST_call<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_call_double + (-1)*C5_main_stddev_CAST_call<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_call_fixp + (-1)*C6_main_stddev_CAST_call<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_call_double + (-1)*C7_main_stddev_CAST_call<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_call_float + (-1)*C8_main_stddev_CAST_call<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_call
solver.Add( + (1)*main_stddev_CAST_call_double==1)    #Type constraint for argument value



#Constraint for cast for   store double %call, double* %arrayidx84, align 8, !taffo.info !21, !taffo.initweight !26
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
objectiveFunction +=  + (50)*C1_main_call_CAST_store
objectiveFunction +=  + (50)*C2_main_call_CAST_store
C3_main_call_CAST_store = solver.IntVar(0, 1, 'C3_main_call_CAST_store')
C4_main_call_CAST_store = solver.IntVar(0, 1, 'C4_main_call_CAST_store')
C5_main_call_CAST_store = solver.IntVar(0, 1, 'C5_main_call_CAST_store')
C6_main_call_CAST_store = solver.IntVar(0, 1, 'C6_main_call_CAST_store')
C7_main_call_CAST_store = solver.IntVar(0, 1, 'C7_main_call_CAST_store')
C8_main_call_CAST_store = solver.IntVar(0, 1, 'C8_main_call_CAST_store')
solver.Add( + (1)*main_call_fixp + (1)*main_call_CAST_store_float + (-1)*C3_main_call_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_call_CAST_store
solver.Add( + (1)*main_call_float + (1)*main_call_CAST_store_fixp + (-1)*C4_main_call_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_call_CAST_store
solver.Add( + (1)*main_call_fixp + (1)*main_call_CAST_store_double + (-1)*C5_main_call_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_call_CAST_store
solver.Add( + (1)*main_call_double + (1)*main_call_CAST_store_fixp + (-1)*C6_main_call_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_call_CAST_store
solver.Add( + (1)*main_call_float + (1)*main_call_CAST_store_double + (-1)*C7_main_call_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_call_CAST_store
solver.Add( + (1)*main_call_double + (1)*main_call_CAST_store_float + (-1)*C8_main_call_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_call_CAST_store
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
ConstantValue__7_fixbits = solver.IntVar(0, 31, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10027)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10056)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cmp87 = fcmp ole double %tmp10, 1.000000e-01, !taffo.info !43, !taffo.initweight !26
main_stddev_CAST_cmp87_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_cmp87_fixbits')
main_stddev_CAST_cmp87_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_cmp87_fixp')
main_stddev_CAST_cmp87_float = solver.IntVar(0, 1, 'main_stddev_CAST_cmp87_float')
main_stddev_CAST_cmp87_double = solver.IntVar(0, 1, 'main_stddev_CAST_cmp87_double')
solver.Add( + (1)*main_stddev_CAST_cmp87_fixp + (1)*main_stddev_CAST_cmp87_float + (1)*main_stddev_CAST_cmp87_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_cmp87_fixbits + (-10000)*main_stddev_CAST_cmp87_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_cmp87')
C2_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_cmp87')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_cmp87_fixbits + (-10000)*C1_main_stddev_CAST_cmp87<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_cmp87_fixbits + (-10000)*C2_main_stddev_CAST_cmp87<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_stddev_CAST_cmp87
objectiveFunction +=  + (50)*C2_main_stddev_CAST_cmp87
C3_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_cmp87')
C4_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_cmp87')
C5_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_cmp87')
C6_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_cmp87')
C7_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_cmp87')
C8_main_stddev_CAST_cmp87 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_cmp87')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cmp87_float + (-1)*C3_main_stddev_CAST_cmp87<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_cmp87
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cmp87_fixp + (-1)*C4_main_stddev_CAST_cmp87<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_cmp87
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cmp87_double + (-1)*C5_main_stddev_CAST_cmp87<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_cmp87
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cmp87_fixp + (-1)*C6_main_stddev_CAST_cmp87<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_cmp87
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cmp87_double + (-1)*C7_main_stddev_CAST_cmp87<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_cmp87
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cmp87_float + (-1)*C8_main_stddev_CAST_cmp87<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_cmp87



#Stuff for double 1.000000e-01
ConstantValue__8_fixbits = solver.IntVar(0, 31, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10027)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=10056)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cmp87 = fcmp ole double %tmp10, 1.000000e-01, !taffo.info !43, !taffo.initweight !26
ConstantValue__8_CAST_cmp87_fixbits = solver.IntVar(0, 31, 'ConstantValue__8_CAST_cmp87_fixbits')
ConstantValue__8_CAST_cmp87_fixp = solver.IntVar(0, 1, 'ConstantValue__8_CAST_cmp87_fixp')
ConstantValue__8_CAST_cmp87_float = solver.IntVar(0, 1, 'ConstantValue__8_CAST_cmp87_float')
ConstantValue__8_CAST_cmp87_double = solver.IntVar(0, 1, 'ConstantValue__8_CAST_cmp87_double')
solver.Add( + (1)*ConstantValue__8_CAST_cmp87_fixp + (1)*ConstantValue__8_CAST_cmp87_float + (1)*ConstantValue__8_CAST_cmp87_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__8_CAST_cmp87_fixbits + (-10000)*ConstantValue__8_CAST_cmp87_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C1_ConstantValue__8_CAST_cmp87')
C2_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C2_ConstantValue__8_CAST_cmp87')
solver.Add( + (1)*ConstantValue__8_fixbits + (-1)*ConstantValue__8_CAST_cmp87_fixbits + (-10000)*C1_ConstantValue__8_CAST_cmp87<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__8_fixbits + (1)*ConstantValue__8_CAST_cmp87_fixbits + (-10000)*C2_ConstantValue__8_CAST_cmp87<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__8_CAST_cmp87
objectiveFunction +=  + (50)*C2_ConstantValue__8_CAST_cmp87
C3_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C3_ConstantValue__8_CAST_cmp87')
C4_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C4_ConstantValue__8_CAST_cmp87')
C5_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C5_ConstantValue__8_CAST_cmp87')
C6_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C6_ConstantValue__8_CAST_cmp87')
C7_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C7_ConstantValue__8_CAST_cmp87')
C8_ConstantValue__8_CAST_cmp87 = solver.IntVar(0, 1, 'C8_ConstantValue__8_CAST_cmp87')
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_cmp87_float + (-1)*C3_ConstantValue__8_CAST_cmp87<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__8_CAST_cmp87
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_cmp87_fixp + (-1)*C4_ConstantValue__8_CAST_cmp87<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__8_CAST_cmp87
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_cmp87_double + (-1)*C5_ConstantValue__8_CAST_cmp87<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__8_CAST_cmp87
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_cmp87_fixp + (-1)*C6_ConstantValue__8_CAST_cmp87<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__8_CAST_cmp87
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_cmp87_double + (-1)*C7_ConstantValue__8_CAST_cmp87<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__8_CAST_cmp87
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_cmp87_float + (-1)*C8_ConstantValue__8_CAST_cmp87<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__8_CAST_cmp87
solver.Add( + (1)*main_stddev_CAST_cmp87_fixp + (-1)*ConstantValue__8_CAST_cmp87_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_cmp87_float + (-1)*ConstantValue__8_CAST_cmp87_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_cmp87_double + (-1)*ConstantValue__8_CAST_cmp87_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_cmp87_fixbits + (-1)*ConstantValue__8_CAST_cmp87_fixbits==0)    #same fractional bit

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp11')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp11 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_0 = solver.IntVar(0, 1, 'main_main_tmp11_enob_0')
solver.Add( + (1)*main_main_tmp11_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp11 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !21, !taffo.initweight !27
main_cond_fixbits = solver.IntVar(0, 18, 'main_cond_fixbits')
main_cond_fixp = solver.IntVar(0, 1, 'main_cond_fixp')
main_cond_float = solver.IntVar(0, 1, 'main_cond_float')
main_cond_double = solver.IntVar(0, 1, 'main_cond_double')
main_cond_enob = solver.IntVar(-10000, 10000, 'main_cond_enob')
solver.Add( + (1)*main_cond_enob + (-1)*main_cond_fixbits + (10000)*main_cond_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_cond_enob + (10000)*main_cond_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_cond_enob + (10000)*main_cond_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_cond_fixbits + (-10000)*main_cond_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_cond_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_cond_enob
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_float + (1)*main_cond_double==1)    #Exactly one selected type
solver.Add( + (1)*main_cond_fixbits + (-10000)*main_cond_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__9_fixbits = solver.IntVar(0, 31, 'ConstantValue__9_fixbits')
ConstantValue__9_fixp = solver.IntVar(0, 1, 'ConstantValue__9_fixp')
ConstantValue__9_float = solver.IntVar(0, 1, 'ConstantValue__9_float')
ConstantValue__9_double = solver.IntVar(0, 1, 'ConstantValue__9_double')
ConstantValue__9_enob = solver.IntVar(-10000, 10000, 'ConstantValue__9_enob')
solver.Add( + (1)*ConstantValue__9_enob + (-1)*ConstantValue__9_fixbits + (10000)*ConstantValue__9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_float + (1)*ConstantValue__9_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp<=0)    #If not fix, frac part to zero
main_main_cond_enob_1 = solver.IntVar(0, 1, 'main_main_cond_enob_1')
solver.Add( + (1)*main_main_cond_enob_1==1)    #Enob: one selected constraint



#Stuff for double 1.000000e+00
ConstantValue__10_fixbits = solver.IntVar(0, 31, 'ConstantValue__10_fixbits')
ConstantValue__10_fixp = solver.IntVar(0, 1, 'ConstantValue__10_fixp')
ConstantValue__10_float = solver.IntVar(0, 1, 'ConstantValue__10_float')
ConstantValue__10_double = solver.IntVar(0, 1, 'ConstantValue__10_double')
ConstantValue__10_enob = solver.IntVar(-10000, 10000, 'ConstantValue__10_enob')
solver.Add( + (1)*ConstantValue__10_enob + (-1)*ConstantValue__10_fixbits + (10000)*ConstantValue__10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_float + (1)*ConstantValue__10_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !21, !taffo.initweight !27
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
objectiveFunction +=  + (50)*C1_main_stddev_CAST_cond
objectiveFunction +=  + (50)*C2_main_stddev_CAST_cond
C3_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C3_main_stddev_CAST_cond')
C4_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C4_main_stddev_CAST_cond')
C5_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C5_main_stddev_CAST_cond')
C6_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C6_main_stddev_CAST_cond')
C7_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C7_main_stddev_CAST_cond')
C8_main_stddev_CAST_cond = solver.IntVar(0, 1, 'C8_main_stddev_CAST_cond')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cond_float + (-1)*C3_main_stddev_CAST_cond<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cond_fixp + (-1)*C4_main_stddev_CAST_cond<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cond_double + (-1)*C5_main_stddev_CAST_cond<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cond_fixp + (-1)*C6_main_stddev_CAST_cond<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cond_double + (-1)*C7_main_stddev_CAST_cond<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_cond
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cond_float + (-1)*C8_main_stddev_CAST_cond<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_cond
solver.Add( + (1)*main_cond_fixp + (-1)*main_stddev_CAST_cond_fixp==0)    #fix equality
solver.Add( + (1)*main_cond_float + (-1)*main_stddev_CAST_cond_float==0)    #float equality
solver.Add( + (1)*main_cond_double + (-1)*main_stddev_CAST_cond_double==0)    #double equality
solver.Add( + (1)*main_cond_fixbits + (-1)*main_stddev_CAST_cond_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_cond_enob + (-1)*main_stddev_enob_memphi_main_tmp11 + (10000)*main_main_cond_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   store double %cond, double* %arrayidx92, align 8, !taffo.info !21, !taffo.initweight !26
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
objectiveFunction +=  + (50)*C1_main_cond_CAST_store
objectiveFunction +=  + (50)*C2_main_cond_CAST_store
C3_main_cond_CAST_store = solver.IntVar(0, 1, 'C3_main_cond_CAST_store')
C4_main_cond_CAST_store = solver.IntVar(0, 1, 'C4_main_cond_CAST_store')
C5_main_cond_CAST_store = solver.IntVar(0, 1, 'C5_main_cond_CAST_store')
C6_main_cond_CAST_store = solver.IntVar(0, 1, 'C6_main_cond_CAST_store')
C7_main_cond_CAST_store = solver.IntVar(0, 1, 'C7_main_cond_CAST_store')
C8_main_cond_CAST_store = solver.IntVar(0, 1, 'C8_main_cond_CAST_store')
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_CAST_store_float + (-1)*C3_main_cond_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_cond_CAST_store
solver.Add( + (1)*main_cond_float + (1)*main_cond_CAST_store_fixp + (-1)*C4_main_cond_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_cond_CAST_store
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_CAST_store_double + (-1)*C5_main_cond_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_cond_CAST_store
solver.Add( + (1)*main_cond_double + (1)*main_cond_CAST_store_fixp + (-1)*C6_main_cond_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_cond_CAST_store
solver.Add( + (1)*main_cond_float + (1)*main_cond_CAST_store_double + (-1)*C7_main_cond_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_cond_CAST_store
solver.Add( + (1)*main_cond_double + (1)*main_cond_CAST_store_float + (-1)*C8_main_cond_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_cond_CAST_store
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



#Constraint for cast for   %sub110 = fsub double %tmp13, %tmp12, !taffo.info !13, !taffo.initweight !27
main_data_CAST_sub110_fixbits = solver.IntVar(0, 30, 'main_data_CAST_sub110_fixbits')
main_data_CAST_sub110_fixp = solver.IntVar(0, 1, 'main_data_CAST_sub110_fixp')
main_data_CAST_sub110_float = solver.IntVar(0, 1, 'main_data_CAST_sub110_float')
main_data_CAST_sub110_double = solver.IntVar(0, 1, 'main_data_CAST_sub110_double')
solver.Add( + (1)*main_data_CAST_sub110_fixp + (1)*main_data_CAST_sub110_float + (1)*main_data_CAST_sub110_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_sub110_fixbits + (-10000)*main_data_CAST_sub110_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C1_main_data_CAST_sub110')
C2_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C2_main_data_CAST_sub110')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_sub110_fixbits + (-10000)*C1_main_data_CAST_sub110<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_sub110_fixbits + (-10000)*C2_main_data_CAST_sub110<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_sub110
objectiveFunction +=  + (50)*C2_main_data_CAST_sub110
C3_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C3_main_data_CAST_sub110')
C4_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C4_main_data_CAST_sub110')
C5_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C5_main_data_CAST_sub110')
C6_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C6_main_data_CAST_sub110')
C7_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C7_main_data_CAST_sub110')
C8_main_data_CAST_sub110 = solver.IntVar(0, 1, 'C8_main_data_CAST_sub110')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub110_float + (-1)*C3_main_data_CAST_sub110<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_sub110
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub110_fixp + (-1)*C4_main_data_CAST_sub110<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_sub110
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub110_double + (-1)*C5_main_data_CAST_sub110<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_sub110
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub110_fixp + (-1)*C6_main_data_CAST_sub110<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_sub110
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub110_double + (-1)*C7_main_data_CAST_sub110<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_sub110
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub110_float + (-1)*C8_main_data_CAST_sub110<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_sub110



#Constraint for cast for   %sub110 = fsub double %tmp13, %tmp12, !taffo.info !13, !taffo.initweight !27
main_mean_CAST_sub110_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_sub110_fixbits')
main_mean_CAST_sub110_fixp = solver.IntVar(0, 1, 'main_mean_CAST_sub110_fixp')
main_mean_CAST_sub110_float = solver.IntVar(0, 1, 'main_mean_CAST_sub110_float')
main_mean_CAST_sub110_double = solver.IntVar(0, 1, 'main_mean_CAST_sub110_double')
solver.Add( + (1)*main_mean_CAST_sub110_fixp + (1)*main_mean_CAST_sub110_float + (1)*main_mean_CAST_sub110_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_sub110_fixbits + (-10000)*main_mean_CAST_sub110_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C1_main_mean_CAST_sub110')
C2_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C2_main_mean_CAST_sub110')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_sub110_fixbits + (-10000)*C1_main_mean_CAST_sub110<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_sub110_fixbits + (-10000)*C2_main_mean_CAST_sub110<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mean_CAST_sub110
objectiveFunction +=  + (50)*C2_main_mean_CAST_sub110
C3_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C3_main_mean_CAST_sub110')
C4_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C4_main_mean_CAST_sub110')
C5_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C5_main_mean_CAST_sub110')
C6_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C6_main_mean_CAST_sub110')
C7_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C7_main_mean_CAST_sub110')
C8_main_mean_CAST_sub110 = solver.IntVar(0, 1, 'C8_main_mean_CAST_sub110')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub110_float + (-1)*C3_main_mean_CAST_sub110<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mean_CAST_sub110
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub110_fixp + (-1)*C4_main_mean_CAST_sub110<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mean_CAST_sub110
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub110_double + (-1)*C5_main_mean_CAST_sub110<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mean_CAST_sub110
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub110_fixp + (-1)*C6_main_mean_CAST_sub110<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mean_CAST_sub110
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub110_double + (-1)*C7_main_mean_CAST_sub110<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mean_CAST_sub110
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub110_float + (-1)*C8_main_mean_CAST_sub110<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mean_CAST_sub110



#Stuff for   %sub110 = fsub double %tmp13, %tmp12, !taffo.info !13, !taffo.initweight !27
main_sub110_fixbits = solver.IntVar(0, 15, 'main_sub110_fixbits')
main_sub110_fixp = solver.IntVar(0, 1, 'main_sub110_fixp')
main_sub110_float = solver.IntVar(0, 1, 'main_sub110_float')
main_sub110_double = solver.IntVar(0, 1, 'main_sub110_double')
main_sub110_enob = solver.IntVar(-10000, 10000, 'main_sub110_enob')
solver.Add( + (1)*main_sub110_enob + (-1)*main_sub110_fixbits + (10000)*main_sub110_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub110_enob + (10000)*main_sub110_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub110_enob + (10000)*main_sub110_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub110_fixbits + (-10000)*main_sub110_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub110_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_sub110_enob
solver.Add( + (1)*main_sub110_fixp + (1)*main_sub110_float + (1)*main_sub110_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub110_fixbits + (-10000)*main_sub110_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_sub110_fixp + (-1)*main_mean_CAST_sub110_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub110_float + (-1)*main_mean_CAST_sub110_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub110_double + (-1)*main_mean_CAST_sub110_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub110_fixbits + (-1)*main_mean_CAST_sub110_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_data_CAST_sub110_fixp + (-1)*main_sub110_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub110_float + (-1)*main_sub110_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub110_double + (-1)*main_sub110_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub110_fixbits + (-1)*main_sub110_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_sub110_fixp
objectiveFunction +=  + (300)*main_sub110_float
objectiveFunction +=  + (664.928)*main_sub110_double
solver.Add( + (1)*main_sub110_enob + (-1)*main_data_enob_memphi_main_tmp13<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub110_enob + (-1)*main_mean_enob_memphi_main_tmp12<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub110, double* %arrayidx109, align 8, !taffo.info !17, !taffo.initweight !27
main_sub110_CAST_store_fixbits = solver.IntVar(0, 15, 'main_sub110_CAST_store_fixbits')
main_sub110_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub110_CAST_store_fixp')
main_sub110_CAST_store_float = solver.IntVar(0, 1, 'main_sub110_CAST_store_float')
main_sub110_CAST_store_double = solver.IntVar(0, 1, 'main_sub110_CAST_store_double')
solver.Add( + (1)*main_sub110_CAST_store_fixp + (1)*main_sub110_CAST_store_float + (1)*main_sub110_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub110_CAST_store_fixbits + (-10000)*main_sub110_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub110_CAST_store = solver.IntVar(0, 1, 'C1_main_sub110_CAST_store')
C2_main_sub110_CAST_store = solver.IntVar(0, 1, 'C2_main_sub110_CAST_store')
solver.Add( + (1)*main_sub110_fixbits + (-1)*main_sub110_CAST_store_fixbits + (-10000)*C1_main_sub110_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub110_fixbits + (1)*main_sub110_CAST_store_fixbits + (-10000)*C2_main_sub110_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_sub110_CAST_store
objectiveFunction +=  + (50)*C2_main_sub110_CAST_store
C3_main_sub110_CAST_store = solver.IntVar(0, 1, 'C3_main_sub110_CAST_store')
C4_main_sub110_CAST_store = solver.IntVar(0, 1, 'C4_main_sub110_CAST_store')
C5_main_sub110_CAST_store = solver.IntVar(0, 1, 'C5_main_sub110_CAST_store')
C6_main_sub110_CAST_store = solver.IntVar(0, 1, 'C6_main_sub110_CAST_store')
C7_main_sub110_CAST_store = solver.IntVar(0, 1, 'C7_main_sub110_CAST_store')
C8_main_sub110_CAST_store = solver.IntVar(0, 1, 'C8_main_sub110_CAST_store')
solver.Add( + (1)*main_sub110_fixp + (1)*main_sub110_CAST_store_float + (-1)*C3_main_sub110_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_sub110_CAST_store
solver.Add( + (1)*main_sub110_float + (1)*main_sub110_CAST_store_fixp + (-1)*C4_main_sub110_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_sub110_CAST_store
solver.Add( + (1)*main_sub110_fixp + (1)*main_sub110_CAST_store_double + (-1)*C5_main_sub110_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_sub110_CAST_store
solver.Add( + (1)*main_sub110_double + (1)*main_sub110_CAST_store_fixp + (-1)*C6_main_sub110_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_sub110_CAST_store
solver.Add( + (1)*main_sub110_float + (1)*main_sub110_CAST_store_double + (-1)*C7_main_sub110_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_sub110_CAST_store
solver.Add( + (1)*main_sub110_double + (1)*main_sub110_CAST_store_float + (-1)*C8_main_sub110_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_sub110_CAST_store
solver.Add( + (1)*main_data_fixp + (-1)*main_sub110_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_data_float + (-1)*main_sub110_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_data_double + (-1)*main_sub110_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_data_fixbits + (-1)*main_sub110_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_data_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_data_enob_storeENOB')
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_sub110_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv111 = sitofp i32 28 to double, !taffo.info !41, !taffo.initweight !26
main_conv111_fixbits = solver.IntVar(0, 20, 'main_conv111_fixbits')
main_conv111_fixp = solver.IntVar(0, 1, 'main_conv111_fixp')
main_conv111_float = solver.IntVar(0, 1, 'main_conv111_float')
main_conv111_double = solver.IntVar(0, 1, 'main_conv111_double')
main_conv111_enob = solver.IntVar(-10000, 10000, 'main_conv111_enob')
solver.Add( + (1)*main_conv111_enob + (-1)*main_conv111_fixbits + (10000)*main_conv111_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv111_enob + (10000)*main_conv111_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_conv111_enob + (10000)*main_conv111_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_conv111_fixbits + (-10000)*main_conv111_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_conv111_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_conv111_enob
solver.Add( + (1)*main_conv111_fixp + (1)*main_conv111_float + (1)*main_conv111_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv111_fixbits + (-10000)*main_conv111_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call112 = call double @sqrt(double %conv111) #1, !taffo.info !41, !taffo.initweight !27, !taffo.constinfo !37
main_call112_fixbits = solver.IntVar(0, 20, 'main_call112_fixbits')
main_call112_fixp = solver.IntVar(0, 1, 'main_call112_fixp')
main_call112_float = solver.IntVar(0, 1, 'main_call112_float')
main_call112_double = solver.IntVar(0, 1, 'main_call112_double')
main_call112_enob = solver.IntVar(-10000, 10000, 'main_call112_enob')
solver.Add( + (1)*main_call112_enob + (-1)*main_call112_fixbits + (10000)*main_call112_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call112_enob + (10000)*main_call112_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_call112_enob + (10000)*main_call112_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_call112_fixbits + (-10000)*main_call112_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_call112_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_call112_enob
solver.Add( + (1)*main_call112_fixp + (1)*main_call112_float + (1)*main_call112_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call112_fixbits + (-10000)*main_call112_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call112_double==1)    #Type constraint for return value



#Constraint for cast for   %call112 = call double @sqrt(double %conv111) #1, !taffo.info !41, !taffo.initweight !27, !taffo.constinfo !37
main_conv111_CAST_call112_fixbits = solver.IntVar(0, 20, 'main_conv111_CAST_call112_fixbits')
main_conv111_CAST_call112_fixp = solver.IntVar(0, 1, 'main_conv111_CAST_call112_fixp')
main_conv111_CAST_call112_float = solver.IntVar(0, 1, 'main_conv111_CAST_call112_float')
main_conv111_CAST_call112_double = solver.IntVar(0, 1, 'main_conv111_CAST_call112_double')
solver.Add( + (1)*main_conv111_CAST_call112_fixp + (1)*main_conv111_CAST_call112_float + (1)*main_conv111_CAST_call112_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv111_CAST_call112_fixbits + (-10000)*main_conv111_CAST_call112_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C1_main_conv111_CAST_call112')
C2_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C2_main_conv111_CAST_call112')
solver.Add( + (1)*main_conv111_fixbits + (-1)*main_conv111_CAST_call112_fixbits + (-10000)*C1_main_conv111_CAST_call112<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv111_fixbits + (1)*main_conv111_CAST_call112_fixbits + (-10000)*C2_main_conv111_CAST_call112<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_conv111_CAST_call112
objectiveFunction +=  + (50)*C2_main_conv111_CAST_call112
C3_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C3_main_conv111_CAST_call112')
C4_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C4_main_conv111_CAST_call112')
C5_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C5_main_conv111_CAST_call112')
C6_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C6_main_conv111_CAST_call112')
C7_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C7_main_conv111_CAST_call112')
C8_main_conv111_CAST_call112 = solver.IntVar(0, 1, 'C8_main_conv111_CAST_call112')
solver.Add( + (1)*main_conv111_fixp + (1)*main_conv111_CAST_call112_float + (-1)*C3_main_conv111_CAST_call112<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_conv111_CAST_call112
solver.Add( + (1)*main_conv111_float + (1)*main_conv111_CAST_call112_fixp + (-1)*C4_main_conv111_CAST_call112<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_conv111_CAST_call112
solver.Add( + (1)*main_conv111_fixp + (1)*main_conv111_CAST_call112_double + (-1)*C5_main_conv111_CAST_call112<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_conv111_CAST_call112
solver.Add( + (1)*main_conv111_double + (1)*main_conv111_CAST_call112_fixp + (-1)*C6_main_conv111_CAST_call112<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_conv111_CAST_call112
solver.Add( + (1)*main_conv111_float + (1)*main_conv111_CAST_call112_double + (-1)*C7_main_conv111_CAST_call112<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_conv111_CAST_call112
solver.Add( + (1)*main_conv111_double + (1)*main_conv111_CAST_call112_float + (-1)*C8_main_conv111_CAST_call112<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_conv111_CAST_call112
solver.Add( + (1)*main_conv111_CAST_call112_double==1)    #Type constraint for argument value

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



#Constraint for cast for   %mul115 = fmul double %call112, %tmp14, !taffo.info !21, !taffo.initweight !27
main_call112_CAST_mul115_fixbits = solver.IntVar(0, 20, 'main_call112_CAST_mul115_fixbits')
main_call112_CAST_mul115_fixp = solver.IntVar(0, 1, 'main_call112_CAST_mul115_fixp')
main_call112_CAST_mul115_float = solver.IntVar(0, 1, 'main_call112_CAST_mul115_float')
main_call112_CAST_mul115_double = solver.IntVar(0, 1, 'main_call112_CAST_mul115_double')
solver.Add( + (1)*main_call112_CAST_mul115_fixp + (1)*main_call112_CAST_mul115_float + (1)*main_call112_CAST_mul115_double==1)    #exactly 1 type
solver.Add( + (1)*main_call112_CAST_mul115_fixbits + (-10000)*main_call112_CAST_mul115_fixp<=0)    #If no fix, fix frac part = 0
C1_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C1_main_call112_CAST_mul115')
C2_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C2_main_call112_CAST_mul115')
solver.Add( + (1)*main_call112_fixbits + (-1)*main_call112_CAST_mul115_fixbits + (-10000)*C1_main_call112_CAST_mul115<=0)    #Shift cost 1
solver.Add( + (-1)*main_call112_fixbits + (1)*main_call112_CAST_mul115_fixbits + (-10000)*C2_main_call112_CAST_mul115<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_call112_CAST_mul115
objectiveFunction +=  + (50)*C2_main_call112_CAST_mul115
C3_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C3_main_call112_CAST_mul115')
C4_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C4_main_call112_CAST_mul115')
C5_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C5_main_call112_CAST_mul115')
C6_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C6_main_call112_CAST_mul115')
C7_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C7_main_call112_CAST_mul115')
C8_main_call112_CAST_mul115 = solver.IntVar(0, 1, 'C8_main_call112_CAST_mul115')
solver.Add( + (1)*main_call112_fixp + (1)*main_call112_CAST_mul115_float + (-1)*C3_main_call112_CAST_mul115<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_call112_CAST_mul115
solver.Add( + (1)*main_call112_float + (1)*main_call112_CAST_mul115_fixp + (-1)*C4_main_call112_CAST_mul115<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_call112_CAST_mul115
solver.Add( + (1)*main_call112_fixp + (1)*main_call112_CAST_mul115_double + (-1)*C5_main_call112_CAST_mul115<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_call112_CAST_mul115
solver.Add( + (1)*main_call112_double + (1)*main_call112_CAST_mul115_fixp + (-1)*C6_main_call112_CAST_mul115<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_call112_CAST_mul115
solver.Add( + (1)*main_call112_float + (1)*main_call112_CAST_mul115_double + (-1)*C7_main_call112_CAST_mul115<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_call112_CAST_mul115
solver.Add( + (1)*main_call112_double + (1)*main_call112_CAST_mul115_float + (-1)*C8_main_call112_CAST_mul115<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_call112_CAST_mul115



#Constraint for cast for   %mul115 = fmul double %call112, %tmp14, !taffo.info !21, !taffo.initweight !27
main_stddev_CAST_mul115_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_mul115_fixbits')
main_stddev_CAST_mul115_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_mul115_fixp')
main_stddev_CAST_mul115_float = solver.IntVar(0, 1, 'main_stddev_CAST_mul115_float')
main_stddev_CAST_mul115_double = solver.IntVar(0, 1, 'main_stddev_CAST_mul115_double')
solver.Add( + (1)*main_stddev_CAST_mul115_fixp + (1)*main_stddev_CAST_mul115_float + (1)*main_stddev_CAST_mul115_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_mul115_fixbits + (-10000)*main_stddev_CAST_mul115_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_mul115')
C2_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_mul115')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_mul115_fixbits + (-10000)*C1_main_stddev_CAST_mul115<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_mul115_fixbits + (-10000)*C2_main_stddev_CAST_mul115<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_stddev_CAST_mul115
objectiveFunction +=  + (50)*C2_main_stddev_CAST_mul115
C3_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_mul115')
C4_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_mul115')
C5_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_mul115')
C6_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_mul115')
C7_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_mul115')
C8_main_stddev_CAST_mul115 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_mul115')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_mul115_float + (-1)*C3_main_stddev_CAST_mul115<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_mul115
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_mul115_fixp + (-1)*C4_main_stddev_CAST_mul115<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_mul115
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_mul115_double + (-1)*C5_main_stddev_CAST_mul115<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_mul115
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_mul115_fixp + (-1)*C6_main_stddev_CAST_mul115<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_mul115
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_mul115_double + (-1)*C7_main_stddev_CAST_mul115<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_mul115
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_mul115_float + (-1)*C8_main_stddev_CAST_mul115<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_mul115



#Stuff for   %mul115 = fmul double %call112, %tmp14, !taffo.info !21, !taffo.initweight !27
main_mul115_fixbits = solver.IntVar(0, 18, 'main_mul115_fixbits')
main_mul115_fixp = solver.IntVar(0, 1, 'main_mul115_fixp')
main_mul115_float = solver.IntVar(0, 1, 'main_mul115_float')
main_mul115_double = solver.IntVar(0, 1, 'main_mul115_double')
main_mul115_enob = solver.IntVar(-10000, 10000, 'main_mul115_enob')
solver.Add( + (1)*main_mul115_enob + (-1)*main_mul115_fixbits + (10000)*main_mul115_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul115_enob + (10000)*main_mul115_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul115_enob + (10000)*main_mul115_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul115_fixbits + (-10000)*main_mul115_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_mul115_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_mul115_enob
solver.Add( + (1)*main_mul115_fixp + (1)*main_mul115_float + (1)*main_mul115_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul115_fixbits + (-10000)*main_mul115_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call112_CAST_mul115_fixp + (-1)*main_stddev_CAST_mul115_fixp==0)    #fix equality
solver.Add( + (1)*main_call112_CAST_mul115_float + (-1)*main_stddev_CAST_mul115_float==0)    #float equality
solver.Add( + (1)*main_call112_CAST_mul115_double + (-1)*main_stddev_CAST_mul115_double==0)    #double equality
solver.Add( + (1)*main_call112_CAST_mul115_fixp + (-1)*main_mul115_fixp==0)    #fix equality
solver.Add( + (1)*main_call112_CAST_mul115_float + (-1)*main_mul115_float==0)    #float equality
solver.Add( + (1)*main_call112_CAST_mul115_double + (-1)*main_mul115_double==0)    #double equality
objectiveFunction +=  + (165.217)*main_mul115_fixp
objectiveFunction +=  + (600)*main_mul115_float
objectiveFunction +=  + (1225.51)*main_mul115_double
main_main_mul115_enob_1 = solver.IntVar(0, 1, 'main_main_mul115_enob_1')
main_main_mul115_enob_2 = solver.IntVar(0, 1, 'main_main_mul115_enob_2')
solver.Add( + (1)*main_main_mul115_enob_1 + (1)*main_main_mul115_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul115_enob + (-1)*main_stddev_enob_memphi_main_tmp14 + (-10000)*main_main_mul115_enob_1<=0)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul115_enob + (-1)*main_call112_enob + (-10000)*main_main_mul115_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp15 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp15')
solver.Add( + (1)*main_data_enob_memphi_main_tmp15 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp15_enob_0 = solver.IntVar(0, 1, 'main_main_tmp15_enob_0')
solver.Add( + (1)*main_main_tmp15_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp15 + (-1)*main_data_enob_storeENOB + (10000)*main_main_tmp15_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div120 = fdiv double %tmp15, %mul115, !taffo.info !17, !taffo.initweight !30
main_data_CAST_div120_fixbits = solver.IntVar(0, 30, 'main_data_CAST_div120_fixbits')
main_data_CAST_div120_fixp = solver.IntVar(0, 1, 'main_data_CAST_div120_fixp')
main_data_CAST_div120_float = solver.IntVar(0, 1, 'main_data_CAST_div120_float')
main_data_CAST_div120_double = solver.IntVar(0, 1, 'main_data_CAST_div120_double')
solver.Add( + (1)*main_data_CAST_div120_fixp + (1)*main_data_CAST_div120_float + (1)*main_data_CAST_div120_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_div120_fixbits + (-10000)*main_data_CAST_div120_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_div120 = solver.IntVar(0, 1, 'C1_main_data_CAST_div120')
C2_main_data_CAST_div120 = solver.IntVar(0, 1, 'C2_main_data_CAST_div120')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_div120_fixbits + (-10000)*C1_main_data_CAST_div120<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_div120_fixbits + (-10000)*C2_main_data_CAST_div120<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_div120
objectiveFunction +=  + (50)*C2_main_data_CAST_div120
C3_main_data_CAST_div120 = solver.IntVar(0, 1, 'C3_main_data_CAST_div120')
C4_main_data_CAST_div120 = solver.IntVar(0, 1, 'C4_main_data_CAST_div120')
C5_main_data_CAST_div120 = solver.IntVar(0, 1, 'C5_main_data_CAST_div120')
C6_main_data_CAST_div120 = solver.IntVar(0, 1, 'C6_main_data_CAST_div120')
C7_main_data_CAST_div120 = solver.IntVar(0, 1, 'C7_main_data_CAST_div120')
C8_main_data_CAST_div120 = solver.IntVar(0, 1, 'C8_main_data_CAST_div120')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_div120_float + (-1)*C3_main_data_CAST_div120<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_div120
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_div120_fixp + (-1)*C4_main_data_CAST_div120<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_div120
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_div120_double + (-1)*C5_main_data_CAST_div120<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_div120
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_div120_fixp + (-1)*C6_main_data_CAST_div120<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_div120
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_div120_double + (-1)*C7_main_data_CAST_div120<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_div120
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_div120_float + (-1)*C8_main_data_CAST_div120<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_div120



#Constraint for cast for   %div120 = fdiv double %tmp15, %mul115, !taffo.info !17, !taffo.initweight !30
main_mul115_CAST_div120_fixbits = solver.IntVar(0, 18, 'main_mul115_CAST_div120_fixbits')
main_mul115_CAST_div120_fixp = solver.IntVar(0, 1, 'main_mul115_CAST_div120_fixp')
main_mul115_CAST_div120_float = solver.IntVar(0, 1, 'main_mul115_CAST_div120_float')
main_mul115_CAST_div120_double = solver.IntVar(0, 1, 'main_mul115_CAST_div120_double')
solver.Add( + (1)*main_mul115_CAST_div120_fixp + (1)*main_mul115_CAST_div120_float + (1)*main_mul115_CAST_div120_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul115_CAST_div120_fixbits + (-10000)*main_mul115_CAST_div120_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C1_main_mul115_CAST_div120')
C2_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C2_main_mul115_CAST_div120')
solver.Add( + (1)*main_mul115_fixbits + (-1)*main_mul115_CAST_div120_fixbits + (-10000)*C1_main_mul115_CAST_div120<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul115_fixbits + (1)*main_mul115_CAST_div120_fixbits + (-10000)*C2_main_mul115_CAST_div120<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mul115_CAST_div120
objectiveFunction +=  + (50)*C2_main_mul115_CAST_div120
C3_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C3_main_mul115_CAST_div120')
C4_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C4_main_mul115_CAST_div120')
C5_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C5_main_mul115_CAST_div120')
C6_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C6_main_mul115_CAST_div120')
C7_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C7_main_mul115_CAST_div120')
C8_main_mul115_CAST_div120 = solver.IntVar(0, 1, 'C8_main_mul115_CAST_div120')
solver.Add( + (1)*main_mul115_fixp + (1)*main_mul115_CAST_div120_float + (-1)*C3_main_mul115_CAST_div120<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mul115_CAST_div120
solver.Add( + (1)*main_mul115_float + (1)*main_mul115_CAST_div120_fixp + (-1)*C4_main_mul115_CAST_div120<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mul115_CAST_div120
solver.Add( + (1)*main_mul115_fixp + (1)*main_mul115_CAST_div120_double + (-1)*C5_main_mul115_CAST_div120<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mul115_CAST_div120
solver.Add( + (1)*main_mul115_double + (1)*main_mul115_CAST_div120_fixp + (-1)*C6_main_mul115_CAST_div120<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mul115_CAST_div120
solver.Add( + (1)*main_mul115_float + (1)*main_mul115_CAST_div120_double + (-1)*C7_main_mul115_CAST_div120<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mul115_CAST_div120
solver.Add( + (1)*main_mul115_double + (1)*main_mul115_CAST_div120_float + (-1)*C8_main_mul115_CAST_div120<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mul115_CAST_div120



#Stuff for   %div120 = fdiv double %tmp15, %mul115, !taffo.info !17, !taffo.initweight !30
main_div120_fixbits = solver.IntVar(0, 30, 'main_div120_fixbits')
main_div120_fixp = solver.IntVar(0, 1, 'main_div120_fixp')
main_div120_float = solver.IntVar(0, 1, 'main_div120_float')
main_div120_double = solver.IntVar(0, 1, 'main_div120_double')
main_div120_enob = solver.IntVar(-10000, 10000, 'main_div120_enob')
solver.Add( + (1)*main_div120_enob + (-1)*main_div120_fixbits + (10000)*main_div120_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div120_enob + (10000)*main_div120_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div120_enob + (10000)*main_div120_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div120_fixbits + (-10000)*main_div120_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_div120_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_div120_enob
solver.Add( + (1)*main_div120_fixp + (1)*main_div120_float + (1)*main_div120_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div120_fixbits + (-10000)*main_div120_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_div120_fixp + (-1)*main_mul115_CAST_div120_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_div120_float + (-1)*main_mul115_CAST_div120_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_div120_double + (-1)*main_mul115_CAST_div120_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_div120_fixp + (-1)*main_div120_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_div120_float + (-1)*main_div120_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_div120_double + (-1)*main_div120_double==0)    #double equality
objectiveFunction +=  + (161.159)*main_div120_fixp
objectiveFunction +=  + (600)*main_div120_float
objectiveFunction +=  + (1200)*main_div120_double
main_main_div120_enob_1 = solver.IntVar(0, 1, 'main_main_div120_enob_1')
main_main_div120_enob_2 = solver.IntVar(0, 1, 'main_main_div120_enob_2')
solver.Add( + (1)*main_main_div120_enob_1 + (1)*main_main_div120_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div120_enob + (-1)*main_mul115_enob + (-10000)*main_main_div120_enob_1<=1048)    #Enob: propagation in division 1
solver.Add( + (1)*main_div120_enob + (-1)*main_data_enob_memphi_main_tmp15 + (-10000)*main_main_div120_enob_2<=1048)    #Enob: propagation in division 2



#Constraint for cast for   store double %div120, double* %arrayidx119, align 8, !taffo.info !17, !taffo.initweight !27
main_div120_CAST_store_fixbits = solver.IntVar(0, 30, 'main_div120_CAST_store_fixbits')
main_div120_CAST_store_fixp = solver.IntVar(0, 1, 'main_div120_CAST_store_fixp')
main_div120_CAST_store_float = solver.IntVar(0, 1, 'main_div120_CAST_store_float')
main_div120_CAST_store_double = solver.IntVar(0, 1, 'main_div120_CAST_store_double')
solver.Add( + (1)*main_div120_CAST_store_fixp + (1)*main_div120_CAST_store_float + (1)*main_div120_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div120_CAST_store_fixbits + (-10000)*main_div120_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div120_CAST_store = solver.IntVar(0, 1, 'C1_main_div120_CAST_store')
C2_main_div120_CAST_store = solver.IntVar(0, 1, 'C2_main_div120_CAST_store')
solver.Add( + (1)*main_div120_fixbits + (-1)*main_div120_CAST_store_fixbits + (-10000)*C1_main_div120_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div120_fixbits + (1)*main_div120_CAST_store_fixbits + (-10000)*C2_main_div120_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_div120_CAST_store
objectiveFunction +=  + (50)*C2_main_div120_CAST_store
C3_main_div120_CAST_store = solver.IntVar(0, 1, 'C3_main_div120_CAST_store')
C4_main_div120_CAST_store = solver.IntVar(0, 1, 'C4_main_div120_CAST_store')
C5_main_div120_CAST_store = solver.IntVar(0, 1, 'C5_main_div120_CAST_store')
C6_main_div120_CAST_store = solver.IntVar(0, 1, 'C6_main_div120_CAST_store')
C7_main_div120_CAST_store = solver.IntVar(0, 1, 'C7_main_div120_CAST_store')
C8_main_div120_CAST_store = solver.IntVar(0, 1, 'C8_main_div120_CAST_store')
solver.Add( + (1)*main_div120_fixp + (1)*main_div120_CAST_store_float + (-1)*C3_main_div120_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_div120_CAST_store
solver.Add( + (1)*main_div120_float + (1)*main_div120_CAST_store_fixp + (-1)*C4_main_div120_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_div120_CAST_store
solver.Add( + (1)*main_div120_fixp + (1)*main_div120_CAST_store_double + (-1)*C5_main_div120_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_div120_CAST_store
solver.Add( + (1)*main_div120_double + (1)*main_div120_CAST_store_fixp + (-1)*C6_main_div120_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_div120_CAST_store
solver.Add( + (1)*main_div120_float + (1)*main_div120_CAST_store_double + (-1)*C7_main_div120_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_div120_CAST_store
solver.Add( + (1)*main_div120_double + (1)*main_div120_CAST_store_float + (-1)*C8_main_div120_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_div120_CAST_store
solver.Add( + (1)*main_data_fixp + (-1)*main_div120_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_data_float + (-1)*main_div120_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_data_double + (-1)*main_div120_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_data_fixbits + (-1)*main_div120_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_data_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_data_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (-1)*main_div120_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp13 + (-1)*main_data_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_4<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.000000e+00
ConstantValue__11_fixbits = solver.IntVar(0, 31, 'ConstantValue__11_fixbits')
ConstantValue__11_fixp = solver.IntVar(0, 1, 'ConstantValue__11_fixp')
ConstantValue__11_float = solver.IntVar(0, 1, 'ConstantValue__11_float')
ConstantValue__11_double = solver.IntVar(0, 1, 'ConstantValue__11_double')
ConstantValue__11_enob = solver.IntVar(-10000, 10000, 'ConstantValue__11_enob')
solver.Add( + (1)*ConstantValue__11_enob + (-1)*ConstantValue__11_fixbits + (10000)*ConstantValue__11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_float + (1)*ConstantValue__11_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__12_fixbits = solver.IntVar(0, 31, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx134, align 8, !taffo.info !19, !taffo.initweight !27, !taffo.constinfo !44
ConstantValue__12_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__12_CAST_store_fixbits')
ConstantValue__12_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__12_CAST_store_fixp')
ConstantValue__12_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__12_CAST_store_float')
ConstantValue__12_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__12_CAST_store_double')
solver.Add( + (1)*ConstantValue__12_CAST_store_fixp + (1)*ConstantValue__12_CAST_store_float + (1)*ConstantValue__12_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__12_CAST_store_fixbits + (-10000)*ConstantValue__12_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__12_CAST_store')
C2_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__12_CAST_store')
solver.Add( + (1)*ConstantValue__12_fixbits + (-1)*ConstantValue__12_CAST_store_fixbits + (-10000)*C1_ConstantValue__12_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__12_fixbits + (1)*ConstantValue__12_CAST_store_fixbits + (-10000)*C2_ConstantValue__12_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__12_CAST_store
objectiveFunction +=  + (50)*C2_ConstantValue__12_CAST_store
C3_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__12_CAST_store')
C4_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__12_CAST_store')
C5_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__12_CAST_store')
C6_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__12_CAST_store')
C7_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__12_CAST_store')
C8_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__12_CAST_store')
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_store_float + (-1)*C3_ConstantValue__12_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_store_fixp + (-1)*C4_ConstantValue__12_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_store_double + (-1)*C5_ConstantValue__12_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_store_fixp + (-1)*C6_ConstantValue__12_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_store_double + (-1)*C7_ConstantValue__12_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_store_float + (-1)*C8_ConstantValue__12_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__12_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__12_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__12_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__12_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__12_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 0.000000e+00
ConstantValue__13_fixbits = solver.IntVar(0, 32, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_float + (1)*ConstantValue__13_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__14_fixbits = solver.IntVar(0, 32, 'ConstantValue__14_fixbits')
ConstantValue__14_fixp = solver.IntVar(0, 1, 'ConstantValue__14_fixp')
ConstantValue__14_float = solver.IntVar(0, 1, 'ConstantValue__14_float')
ConstantValue__14_double = solver.IntVar(0, 1, 'ConstantValue__14_double')
ConstantValue__14_enob = solver.IntVar(-10000, 10000, 'ConstantValue__14_enob')
solver.Add( + (1)*ConstantValue__14_enob + (-1)*ConstantValue__14_fixbits + (10000)*ConstantValue__14_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_float + (1)*ConstantValue__14_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx143, align 8, !taffo.info !19, !taffo.initweight !27, !taffo.constinfo !38
ConstantValue__14_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__14_CAST_store_fixbits')
ConstantValue__14_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__14_CAST_store_fixp')
ConstantValue__14_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__14_CAST_store_float')
ConstantValue__14_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__14_CAST_store_double')
solver.Add( + (1)*ConstantValue__14_CAST_store_fixp + (1)*ConstantValue__14_CAST_store_float + (1)*ConstantValue__14_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__14_CAST_store_fixbits + (-10000)*ConstantValue__14_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__14_CAST_store')
C2_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__14_CAST_store')
solver.Add( + (1)*ConstantValue__14_fixbits + (-1)*ConstantValue__14_CAST_store_fixbits + (-10000)*C1_ConstantValue__14_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__14_fixbits + (1)*ConstantValue__14_CAST_store_fixbits + (-10000)*C2_ConstantValue__14_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__14_CAST_store
objectiveFunction +=  + (50)*C2_ConstantValue__14_CAST_store
C3_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__14_CAST_store')
C4_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__14_CAST_store')
C5_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__14_CAST_store')
C6_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__14_CAST_store')
C7_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__14_CAST_store')
C8_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__14_CAST_store')
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_store_float + (-1)*C3_ConstantValue__14_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_store_fixp + (-1)*C4_ConstantValue__14_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_store_double + (-1)*C5_ConstantValue__14_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_store_fixp + (-1)*C6_ConstantValue__14_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_store_double + (-1)*C7_ConstantValue__14_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_store_float + (-1)*C8_ConstantValue__14_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__14_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__14_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__14_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__14_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__14_CAST_store_fixbits==0)    #same fractional bit

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



#Constraint for cast for   %mul156 = fmul double %tmp16, %tmp17, !taffo.info !17, !taffo.initweight !30
main_data_CAST_mul156_fixbits = solver.IntVar(0, 30, 'main_data_CAST_mul156_fixbits')
main_data_CAST_mul156_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul156_fixp')
main_data_CAST_mul156_float = solver.IntVar(0, 1, 'main_data_CAST_mul156_float')
main_data_CAST_mul156_double = solver.IntVar(0, 1, 'main_data_CAST_mul156_double')
solver.Add( + (1)*main_data_CAST_mul156_fixp + (1)*main_data_CAST_mul156_float + (1)*main_data_CAST_mul156_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul156_fixbits + (-10000)*main_data_CAST_mul156_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul156')
C2_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul156')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul156_fixbits + (-10000)*C1_main_data_CAST_mul156<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul156_fixbits + (-10000)*C2_main_data_CAST_mul156<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_mul156
objectiveFunction +=  + (50)*C2_main_data_CAST_mul156
C3_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul156')
C4_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul156')
C5_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul156')
C6_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul156')
C7_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul156')
C8_main_data_CAST_mul156 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul156')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul156_float + (-1)*C3_main_data_CAST_mul156<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_mul156
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul156_fixp + (-1)*C4_main_data_CAST_mul156<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_mul156
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul156_double + (-1)*C5_main_data_CAST_mul156<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_mul156
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul156_fixp + (-1)*C6_main_data_CAST_mul156<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_mul156
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul156_double + (-1)*C7_main_data_CAST_mul156<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_mul156
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul156_float + (-1)*C8_main_data_CAST_mul156<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_mul156



#Constraint for cast for   %mul156 = fmul double %tmp16, %tmp17, !taffo.info !17, !taffo.initweight !30
main_data_CAST_mul156_0_fixbits = solver.IntVar(0, 30, 'main_data_CAST_mul156_0_fixbits')
main_data_CAST_mul156_0_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul156_0_fixp')
main_data_CAST_mul156_0_float = solver.IntVar(0, 1, 'main_data_CAST_mul156_0_float')
main_data_CAST_mul156_0_double = solver.IntVar(0, 1, 'main_data_CAST_mul156_0_double')
solver.Add( + (1)*main_data_CAST_mul156_0_fixp + (1)*main_data_CAST_mul156_0_float + (1)*main_data_CAST_mul156_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul156_0_fixbits + (-10000)*main_data_CAST_mul156_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul156_0')
C2_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul156_0')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul156_0_fixbits + (-10000)*C1_main_data_CAST_mul156_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul156_0_fixbits + (-10000)*C2_main_data_CAST_mul156_0<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_mul156_0
objectiveFunction +=  + (50)*C2_main_data_CAST_mul156_0
C3_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul156_0')
C4_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul156_0')
C5_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul156_0')
C6_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul156_0')
C7_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul156_0')
C8_main_data_CAST_mul156_0 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul156_0')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul156_0_float + (-1)*C3_main_data_CAST_mul156_0<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_mul156_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul156_0_fixp + (-1)*C4_main_data_CAST_mul156_0<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_mul156_0
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul156_0_double + (-1)*C5_main_data_CAST_mul156_0<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_mul156_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul156_0_fixp + (-1)*C6_main_data_CAST_mul156_0<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_mul156_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul156_0_double + (-1)*C7_main_data_CAST_mul156_0<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_mul156_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul156_0_float + (-1)*C8_main_data_CAST_mul156_0<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_mul156_0



#Stuff for   %mul156 = fmul double %tmp16, %tmp17, !taffo.info !17, !taffo.initweight !30
main_mul156_fixbits = solver.IntVar(0, 30, 'main_mul156_fixbits')
main_mul156_fixp = solver.IntVar(0, 1, 'main_mul156_fixp')
main_mul156_float = solver.IntVar(0, 1, 'main_mul156_float')
main_mul156_double = solver.IntVar(0, 1, 'main_mul156_double')
main_mul156_enob = solver.IntVar(-10000, 10000, 'main_mul156_enob')
solver.Add( + (1)*main_mul156_enob + (-1)*main_mul156_fixbits + (10000)*main_mul156_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul156_enob + (10000)*main_mul156_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul156_enob + (10000)*main_mul156_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul156_fixbits + (-10000)*main_mul156_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_mul156_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_mul156_enob
solver.Add( + (1)*main_mul156_fixp + (1)*main_mul156_float + (1)*main_mul156_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul156_fixbits + (-10000)*main_mul156_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_mul156_fixp + (-1)*main_data_CAST_mul156_0_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul156_float + (-1)*main_data_CAST_mul156_0_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul156_double + (-1)*main_data_CAST_mul156_0_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_mul156_fixp + (-1)*main_mul156_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul156_float + (-1)*main_mul156_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul156_double + (-1)*main_mul156_double==0)    #double equality
objectiveFunction +=  + (165.217)*main_mul156_fixp
objectiveFunction +=  + (600)*main_mul156_float
objectiveFunction +=  + (1225.51)*main_mul156_double
main_main_mul156_enob_1 = solver.IntVar(0, 1, 'main_main_mul156_enob_1')
main_main_mul156_enob_2 = solver.IntVar(0, 1, 'main_main_mul156_enob_2')
solver.Add( + (1)*main_main_mul156_enob_1 + (1)*main_main_mul156_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul156_enob + (-1)*main_data_enob_memphi_main_tmp17 + (-10000)*main_main_mul156_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul156_enob + (-1)*main_data_enob_memphi_main_tmp16 + (-10000)*main_main_mul156_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp18 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp18')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp18 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp18_enob_1 = solver.IntVar(0, 1, 'main_main_tmp18_enob_1')
solver.Add( + (1)*main_main_tmp18_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add161 = fadd double %tmp18, %mul156, !taffo.info !19, !taffo.initweight !30
main_corr_CAST_add161_fixbits = solver.IntVar(0, 29, 'main_corr_CAST_add161_fixbits')
main_corr_CAST_add161_fixp = solver.IntVar(0, 1, 'main_corr_CAST_add161_fixp')
main_corr_CAST_add161_float = solver.IntVar(0, 1, 'main_corr_CAST_add161_float')
main_corr_CAST_add161_double = solver.IntVar(0, 1, 'main_corr_CAST_add161_double')
solver.Add( + (1)*main_corr_CAST_add161_fixp + (1)*main_corr_CAST_add161_float + (1)*main_corr_CAST_add161_double==1)    #exactly 1 type
solver.Add( + (1)*main_corr_CAST_add161_fixbits + (-10000)*main_corr_CAST_add161_fixp<=0)    #If no fix, fix frac part = 0
C1_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C1_main_corr_CAST_add161')
C2_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C2_main_corr_CAST_add161')
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_add161_fixbits + (-10000)*C1_main_corr_CAST_add161<=0)    #Shift cost 1
solver.Add( + (-1)*main_corr_fixbits + (1)*main_corr_CAST_add161_fixbits + (-10000)*C2_main_corr_CAST_add161<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_corr_CAST_add161
objectiveFunction +=  + (50)*C2_main_corr_CAST_add161
C3_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C3_main_corr_CAST_add161')
C4_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C4_main_corr_CAST_add161')
C5_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C5_main_corr_CAST_add161')
C6_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C6_main_corr_CAST_add161')
C7_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C7_main_corr_CAST_add161')
C8_main_corr_CAST_add161 = solver.IntVar(0, 1, 'C8_main_corr_CAST_add161')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_add161_float + (-1)*C3_main_corr_CAST_add161<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_corr_CAST_add161
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_add161_fixp + (-1)*C4_main_corr_CAST_add161<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_corr_CAST_add161
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_add161_double + (-1)*C5_main_corr_CAST_add161<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_corr_CAST_add161
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_add161_fixp + (-1)*C6_main_corr_CAST_add161<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_corr_CAST_add161
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_add161_double + (-1)*C7_main_corr_CAST_add161<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_corr_CAST_add161
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_add161_float + (-1)*C8_main_corr_CAST_add161<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_corr_CAST_add161



#Constraint for cast for   %add161 = fadd double %tmp18, %mul156, !taffo.info !19, !taffo.initweight !30
main_mul156_CAST_add161_fixbits = solver.IntVar(0, 30, 'main_mul156_CAST_add161_fixbits')
main_mul156_CAST_add161_fixp = solver.IntVar(0, 1, 'main_mul156_CAST_add161_fixp')
main_mul156_CAST_add161_float = solver.IntVar(0, 1, 'main_mul156_CAST_add161_float')
main_mul156_CAST_add161_double = solver.IntVar(0, 1, 'main_mul156_CAST_add161_double')
solver.Add( + (1)*main_mul156_CAST_add161_fixp + (1)*main_mul156_CAST_add161_float + (1)*main_mul156_CAST_add161_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul156_CAST_add161_fixbits + (-10000)*main_mul156_CAST_add161_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C1_main_mul156_CAST_add161')
C2_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C2_main_mul156_CAST_add161')
solver.Add( + (1)*main_mul156_fixbits + (-1)*main_mul156_CAST_add161_fixbits + (-10000)*C1_main_mul156_CAST_add161<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul156_fixbits + (1)*main_mul156_CAST_add161_fixbits + (-10000)*C2_main_mul156_CAST_add161<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mul156_CAST_add161
objectiveFunction +=  + (50)*C2_main_mul156_CAST_add161
C3_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C3_main_mul156_CAST_add161')
C4_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C4_main_mul156_CAST_add161')
C5_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C5_main_mul156_CAST_add161')
C6_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C6_main_mul156_CAST_add161')
C7_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C7_main_mul156_CAST_add161')
C8_main_mul156_CAST_add161 = solver.IntVar(0, 1, 'C8_main_mul156_CAST_add161')
solver.Add( + (1)*main_mul156_fixp + (1)*main_mul156_CAST_add161_float + (-1)*C3_main_mul156_CAST_add161<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mul156_CAST_add161
solver.Add( + (1)*main_mul156_float + (1)*main_mul156_CAST_add161_fixp + (-1)*C4_main_mul156_CAST_add161<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mul156_CAST_add161
solver.Add( + (1)*main_mul156_fixp + (1)*main_mul156_CAST_add161_double + (-1)*C5_main_mul156_CAST_add161<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mul156_CAST_add161
solver.Add( + (1)*main_mul156_double + (1)*main_mul156_CAST_add161_fixp + (-1)*C6_main_mul156_CAST_add161<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mul156_CAST_add161
solver.Add( + (1)*main_mul156_float + (1)*main_mul156_CAST_add161_double + (-1)*C7_main_mul156_CAST_add161<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mul156_CAST_add161
solver.Add( + (1)*main_mul156_double + (1)*main_mul156_CAST_add161_float + (-1)*C8_main_mul156_CAST_add161<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mul156_CAST_add161



#Stuff for   %add161 = fadd double %tmp18, %mul156, !taffo.info !19, !taffo.initweight !30
main_add161_fixbits = solver.IntVar(0, 29, 'main_add161_fixbits')
main_add161_fixp = solver.IntVar(0, 1, 'main_add161_fixp')
main_add161_float = solver.IntVar(0, 1, 'main_add161_float')
main_add161_double = solver.IntVar(0, 1, 'main_add161_double')
main_add161_enob = solver.IntVar(-10000, 10000, 'main_add161_enob')
solver.Add( + (1)*main_add161_enob + (-1)*main_add161_fixbits + (10000)*main_add161_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add161_enob + (10000)*main_add161_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add161_enob + (10000)*main_add161_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add161_fixbits + (-10000)*main_add161_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_add161_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_add161_enob
solver.Add( + (1)*main_add161_fixp + (1)*main_add161_float + (1)*main_add161_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add161_fixbits + (-10000)*main_add161_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_corr_CAST_add161_fixp + (-1)*main_mul156_CAST_add161_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_CAST_add161_float + (-1)*main_mul156_CAST_add161_float==0)    #float equality
solver.Add( + (1)*main_corr_CAST_add161_double + (-1)*main_mul156_CAST_add161_double==0)    #double equality
solver.Add( + (1)*main_corr_CAST_add161_fixbits + (-1)*main_mul156_CAST_add161_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_corr_CAST_add161_fixp + (-1)*main_add161_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_CAST_add161_float + (-1)*main_add161_float==0)    #float equality
solver.Add( + (1)*main_corr_CAST_add161_double + (-1)*main_add161_double==0)    #double equality
solver.Add( + (1)*main_corr_CAST_add161_fixbits + (-1)*main_add161_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_add161_fixp
objectiveFunction +=  + (300)*main_add161_float
objectiveFunction +=  + (664.928)*main_add161_double
solver.Add( + (1)*main_add161_enob + (-1)*main_corr_enob_memphi_main_tmp18<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add161_enob + (-1)*main_mul156_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add161, double* %arrayidx160, align 8, !taffo.info !19, !taffo.initweight !27
main_add161_CAST_store_fixbits = solver.IntVar(0, 29, 'main_add161_CAST_store_fixbits')
main_add161_CAST_store_fixp = solver.IntVar(0, 1, 'main_add161_CAST_store_fixp')
main_add161_CAST_store_float = solver.IntVar(0, 1, 'main_add161_CAST_store_float')
main_add161_CAST_store_double = solver.IntVar(0, 1, 'main_add161_CAST_store_double')
solver.Add( + (1)*main_add161_CAST_store_fixp + (1)*main_add161_CAST_store_float + (1)*main_add161_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add161_CAST_store_fixbits + (-10000)*main_add161_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add161_CAST_store = solver.IntVar(0, 1, 'C1_main_add161_CAST_store')
C2_main_add161_CAST_store = solver.IntVar(0, 1, 'C2_main_add161_CAST_store')
solver.Add( + (1)*main_add161_fixbits + (-1)*main_add161_CAST_store_fixbits + (-10000)*C1_main_add161_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add161_fixbits + (1)*main_add161_CAST_store_fixbits + (-10000)*C2_main_add161_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_add161_CAST_store
objectiveFunction +=  + (50)*C2_main_add161_CAST_store
C3_main_add161_CAST_store = solver.IntVar(0, 1, 'C3_main_add161_CAST_store')
C4_main_add161_CAST_store = solver.IntVar(0, 1, 'C4_main_add161_CAST_store')
C5_main_add161_CAST_store = solver.IntVar(0, 1, 'C5_main_add161_CAST_store')
C6_main_add161_CAST_store = solver.IntVar(0, 1, 'C6_main_add161_CAST_store')
C7_main_add161_CAST_store = solver.IntVar(0, 1, 'C7_main_add161_CAST_store')
C8_main_add161_CAST_store = solver.IntVar(0, 1, 'C8_main_add161_CAST_store')
solver.Add( + (1)*main_add161_fixp + (1)*main_add161_CAST_store_float + (-1)*C3_main_add161_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_add161_CAST_store
solver.Add( + (1)*main_add161_float + (1)*main_add161_CAST_store_fixp + (-1)*C4_main_add161_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_add161_CAST_store
solver.Add( + (1)*main_add161_fixp + (1)*main_add161_CAST_store_double + (-1)*C5_main_add161_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_add161_CAST_store
solver.Add( + (1)*main_add161_double + (1)*main_add161_CAST_store_fixp + (-1)*C6_main_add161_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_add161_CAST_store
solver.Add( + (1)*main_add161_float + (1)*main_add161_CAST_store_double + (-1)*C7_main_add161_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_add161_CAST_store
solver.Add( + (1)*main_add161_double + (1)*main_add161_CAST_store_float + (-1)*C8_main_add161_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_add161_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*main_add161_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*main_add161_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*main_add161_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*main_add161_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_corr_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_corr_enob_storeENOB')
solver.Add( + (1)*main_corr_enob_storeENOB + (-1)*main_corr_fixbits + (10000)*main_corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_corr_enob_storeENOB + (10000)*main_corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_corr_enob_storeENOB + (10000)*main_corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_corr_enob_storeENOB + (-1)*main_add161_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_corr_enob_memphi_main_tmp18 + (-1)*main_corr_enob_storeENOB + (10000)*main_main_tmp18_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp19 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp19')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp19 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp19_enob_1 = solver.IntVar(0, 1, 'main_main_tmp19_enob_1')
solver.Add( + (1)*main_main_tmp19_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_corr_enob_memphi_main_tmp19 + (-1)*main_corr_enob_storeENOB + (10000)*main_main_tmp19_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp19, double* %arrayidx172, align 8, !taffo.info !19, !taffo.initweight !27
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
objectiveFunction +=  + (50)*C1_main_corr_CAST_store
objectiveFunction +=  + (50)*C2_main_corr_CAST_store
C3_main_corr_CAST_store = solver.IntVar(0, 1, 'C3_main_corr_CAST_store')
C4_main_corr_CAST_store = solver.IntVar(0, 1, 'C4_main_corr_CAST_store')
C5_main_corr_CAST_store = solver.IntVar(0, 1, 'C5_main_corr_CAST_store')
C6_main_corr_CAST_store = solver.IntVar(0, 1, 'C6_main_corr_CAST_store')
C7_main_corr_CAST_store = solver.IntVar(0, 1, 'C7_main_corr_CAST_store')
C8_main_corr_CAST_store = solver.IntVar(0, 1, 'C8_main_corr_CAST_store')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_store_float + (-1)*C3_main_corr_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_corr_CAST_store
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_store_fixp + (-1)*C4_main_corr_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_corr_CAST_store
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_store_double + (-1)*C5_main_corr_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_corr_CAST_store
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_store_fixp + (-1)*C6_main_corr_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_corr_CAST_store
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_store_double + (-1)*C7_main_corr_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_corr_CAST_store
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_store_float + (-1)*C8_main_corr_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_corr_CAST_store
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
ConstantValue__15_fixbits = solver.IntVar(0, 31, 'ConstantValue__15_fixbits')
ConstantValue__15_fixp = solver.IntVar(0, 1, 'ConstantValue__15_fixp')
ConstantValue__15_float = solver.IntVar(0, 1, 'ConstantValue__15_float')
ConstantValue__15_double = solver.IntVar(0, 1, 'ConstantValue__15_double')
ConstantValue__15_enob = solver.IntVar(-10000, 10000, 'ConstantValue__15_enob')
solver.Add( + (1)*ConstantValue__15_enob + (-1)*ConstantValue__15_fixbits + (10000)*ConstantValue__15_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__15_fixp + (1)*ConstantValue__15_float + (1)*ConstantValue__15_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp<=0)    #If not fix, frac part to zero



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
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx180, align 8, !taffo.info !19, !taffo.initweight !27, !taffo.constinfo !44
ConstantValue__16_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__16_CAST_store_fixbits')
ConstantValue__16_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__16_CAST_store_fixp')
ConstantValue__16_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__16_CAST_store_float')
ConstantValue__16_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__16_CAST_store_double')
solver.Add( + (1)*ConstantValue__16_CAST_store_fixp + (1)*ConstantValue__16_CAST_store_float + (1)*ConstantValue__16_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__16_CAST_store_fixbits + (-10000)*ConstantValue__16_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__16_CAST_store')
C2_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__16_CAST_store')
solver.Add( + (1)*ConstantValue__16_fixbits + (-1)*ConstantValue__16_CAST_store_fixbits + (-10000)*C1_ConstantValue__16_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__16_fixbits + (1)*ConstantValue__16_CAST_store_fixbits + (-10000)*C2_ConstantValue__16_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__16_CAST_store
objectiveFunction +=  + (50)*C2_ConstantValue__16_CAST_store
C3_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__16_CAST_store')
C4_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__16_CAST_store')
C5_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__16_CAST_store')
C6_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__16_CAST_store')
C7_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__16_CAST_store')
C8_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__16_CAST_store')
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_store_float + (-1)*C3_ConstantValue__16_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_store_fixp + (-1)*C4_ConstantValue__16_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_store_double + (-1)*C5_ConstantValue__16_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_store_fixp + (-1)*C6_ConstantValue__16_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_store_double + (-1)*C7_ConstantValue__16_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_store_float + (-1)*C8_ConstantValue__16_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__16_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__16_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__16_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__16_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__16_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp20 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp20')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp20 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call194 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.10, i32 0, i32 0), double %tmp20), !taffo.info !19, !taffo.initweight !30, !taffo.constinfo !47
main_corr_CAST_call194_fixbits = solver.IntVar(0, 29, 'main_corr_CAST_call194_fixbits')
main_corr_CAST_call194_fixp = solver.IntVar(0, 1, 'main_corr_CAST_call194_fixp')
main_corr_CAST_call194_float = solver.IntVar(0, 1, 'main_corr_CAST_call194_float')
main_corr_CAST_call194_double = solver.IntVar(0, 1, 'main_corr_CAST_call194_double')
solver.Add( + (1)*main_corr_CAST_call194_fixp + (1)*main_corr_CAST_call194_float + (1)*main_corr_CAST_call194_double==1)    #exactly 1 type
solver.Add( + (1)*main_corr_CAST_call194_fixbits + (-10000)*main_corr_CAST_call194_fixp<=0)    #If no fix, fix frac part = 0
C1_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C1_main_corr_CAST_call194')
C2_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C2_main_corr_CAST_call194')
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_call194_fixbits + (-10000)*C1_main_corr_CAST_call194<=0)    #Shift cost 1
solver.Add( + (-1)*main_corr_fixbits + (1)*main_corr_CAST_call194_fixbits + (-10000)*C2_main_corr_CAST_call194<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_corr_CAST_call194
objectiveFunction +=  + (50)*C2_main_corr_CAST_call194
C3_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C3_main_corr_CAST_call194')
C4_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C4_main_corr_CAST_call194')
C5_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C5_main_corr_CAST_call194')
C6_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C6_main_corr_CAST_call194')
C7_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C7_main_corr_CAST_call194')
C8_main_corr_CAST_call194 = solver.IntVar(0, 1, 'C8_main_corr_CAST_call194')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_call194_float + (-1)*C3_main_corr_CAST_call194<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_corr_CAST_call194
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_call194_fixp + (-1)*C4_main_corr_CAST_call194<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_corr_CAST_call194
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_call194_double + (-1)*C5_main_corr_CAST_call194<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_corr_CAST_call194
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_call194_fixp + (-1)*C6_main_corr_CAST_call194<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_corr_CAST_call194
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_call194_double + (-1)*C7_main_corr_CAST_call194<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_corr_CAST_call194
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_call194_float + (-1)*C8_main_corr_CAST_call194<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_corr_CAST_call194
solver.Add( + (1)*main_corr_CAST_call194_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(objectiveFunction)

# Model declaration end.