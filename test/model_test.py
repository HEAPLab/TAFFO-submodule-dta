


#Stuff for   %mean = alloca [32 x float], align 16, !taffo.info !13, !taffo.initweight !16
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



#Stuff for   %data = alloca [28 x [32 x float]], align 16, !taffo.info !17, !taffo.initweight !16
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



#Stuff for   %corr = alloca [32 x [32 x float]], align 16, !taffo.info !19, !taffo.initweight !16
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



#Stuff for   %stddev = alloca [32 x float], align 16, !taffo.info !21, !taffo.initweight !16
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



#Stuff for float 3.200000e+01
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



#Stuff for float 2.800000e+01
ConstantValue__0_fixbits = solver.IntVar(0, 27, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Stuff for float 0.000000e+00
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



#Constraint for cast for   store float 0.000000e+00, float* %arrayidx25, align 4, !taffo.info !13, !taffo.initweight !26, !taffo.constinfo !38
ConstantValue__1_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__1_CAST_store_fixbits')
ConstantValue__1_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_fixp')
ConstantValue__1_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_float')
ConstantValue__1_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_double')
solver.Add( + (1)*ConstantValue__1_CAST_store_fixp + (1)*ConstantValue__1_CAST_store_float + (1)*ConstantValue__1_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__1_CAST_store_fixbits + (-10000)*ConstantValue__1_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__1_CAST_store')
C2_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__1_CAST_store')
solver.Add( + (1)*ConstantValue__1_fixbits + (-1)*ConstantValue__1_CAST_store_fixbits + (-10000)*C1_ConstantValue__1_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__1_fixbits + (1)*ConstantValue__1_CAST_store_fixbits + (-10000)*C2_ConstantValue__1_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__1_CAST_store
objectiveFunction +=  + (50)*C2_ConstantValue__1_CAST_store
C3_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__1_CAST_store')
C4_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__1_CAST_store')
C5_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__1_CAST_store')
C6_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__1_CAST_store')
C7_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__1_CAST_store')
C8_ConstantValue__1_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__1_CAST_store')
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_store_float + (-1)*C3_ConstantValue__1_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__1_CAST_store
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_store_fixp + (-1)*C4_ConstantValue__1_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__1_CAST_store
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_store_double + (-1)*C5_ConstantValue__1_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__1_CAST_store
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_store_fixp + (-1)*C6_ConstantValue__1_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__1_CAST_store
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_store_double + (-1)*C7_ConstantValue__1_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__1_CAST_store
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_store_float + (-1)*C8_ConstantValue__1_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__1_CAST_store
solver.Add( + (1)*main_mean_fixp + (-1)*ConstantValue__1_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_mean_float + (-1)*ConstantValue__1_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_mean_double + (-1)*ConstantValue__1_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_mean_fixbits + (-1)*ConstantValue__1_CAST_store_fixbits==0)    #same fractional bit

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



#Constraint for cast for   %add36 = fadd float %tmp1, %tmp, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   %add36 = fadd float %tmp1, %tmp, !taffo.info !13, !taffo.initweight !27
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



#Stuff for   %add36 = fadd float %tmp1, %tmp, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   store float %add36, float* %arrayidx35, align 4, !taffo.info !13, !taffo.initweight !26
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



#Stuff for   %conv40 = sitofp i32 28 to float, !taffo.info !41, !taffo.initweight !26
main_conv40_fixbits = solver.IntVar(0, 20, 'main_conv40_fixbits')
main_conv40_fixp = solver.IntVar(0, 1, 'main_conv40_fixp')
main_conv40_float = solver.IntVar(0, 1, 'main_conv40_float')
main_conv40_double = solver.IntVar(0, 1, 'main_conv40_double')
main_conv40_enob = solver.IntVar(-10000, 10000, 'main_conv40_enob')
solver.Add( + (1)*main_conv40_enob + (-1)*main_conv40_fixbits + (10000)*main_conv40_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv40_enob + (10000)*main_conv40_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_conv40_enob + (10000)*main_conv40_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_conv40_fixbits + (-10000)*main_conv40_fixp>=-9981)    #Limit the lower number of frac bits20
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



#Constraint for cast for   %div43 = fdiv float %tmp2, %conv40, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   %div43 = fdiv float %tmp2, %conv40, !taffo.info !13, !taffo.initweight !27
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



#Stuff for   %div43 = fdiv float %tmp2, %conv40, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   store float %div43, float* %arrayidx42, align 4, !taffo.info !13, !taffo.initweight !26
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



#Constraint for cast for   store float 0.000000e+00, float* %arrayidx52, align 4, !taffo.info !21, !taffo.initweight !26, !taffo.constinfo !38
ConstantValue__1_CAST_store_0_fixbits = solver.IntVar(0, 32, 'ConstantValue__1_CAST_store_0_fixbits')
ConstantValue__1_CAST_store_0_fixp = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_0_fixp')
ConstantValue__1_CAST_store_0_float = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_0_float')
ConstantValue__1_CAST_store_0_double = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_0_double')
solver.Add( + (1)*ConstantValue__1_CAST_store_0_fixp + (1)*ConstantValue__1_CAST_store_0_float + (1)*ConstantValue__1_CAST_store_0_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__1_CAST_store_0_fixbits + (-10000)*ConstantValue__1_CAST_store_0_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C1_ConstantValue__1_CAST_store_0')
C2_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C2_ConstantValue__1_CAST_store_0')
solver.Add( + (1)*ConstantValue__1_fixbits + (-1)*ConstantValue__1_CAST_store_0_fixbits + (-10000)*C1_ConstantValue__1_CAST_store_0<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__1_fixbits + (1)*ConstantValue__1_CAST_store_0_fixbits + (-10000)*C2_ConstantValue__1_CAST_store_0<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__1_CAST_store_0
objectiveFunction +=  + (50)*C2_ConstantValue__1_CAST_store_0
C3_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C3_ConstantValue__1_CAST_store_0')
C4_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C4_ConstantValue__1_CAST_store_0')
C5_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C5_ConstantValue__1_CAST_store_0')
C6_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C6_ConstantValue__1_CAST_store_0')
C7_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C7_ConstantValue__1_CAST_store_0')
C8_ConstantValue__1_CAST_store_0 = solver.IntVar(0, 1, 'C8_ConstantValue__1_CAST_store_0')
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_store_0_float + (-1)*C3_ConstantValue__1_CAST_store_0<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__1_CAST_store_0
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_store_0_fixp + (-1)*C4_ConstantValue__1_CAST_store_0<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__1_CAST_store_0
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_store_0_double + (-1)*C5_ConstantValue__1_CAST_store_0<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__1_CAST_store_0
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_store_0_fixp + (-1)*C6_ConstantValue__1_CAST_store_0<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__1_CAST_store_0
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_store_0_double + (-1)*C7_ConstantValue__1_CAST_store_0<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__1_CAST_store_0
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_store_0_float + (-1)*C8_ConstantValue__1_CAST_store_0<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__1_CAST_store_0
solver.Add( + (1)*main_stddev_fixp + (-1)*ConstantValue__1_CAST_store_0_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_float + (-1)*ConstantValue__1_CAST_store_0_float==0)    #float equality
solver.Add( + (1)*main_stddev_double + (-1)*ConstantValue__1_CAST_store_0_double==0)    #double equality
solver.Add( + (1)*main_stddev_fixbits + (-1)*ConstantValue__1_CAST_store_0_fixbits==0)    #same fractional bit

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



#Constraint for cast for   %sub = fsub float %tmp3, %tmp4, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   %sub = fsub float %tmp3, %tmp4, !taffo.info !13, !taffo.initweight !27
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



#Stuff for   %sub = fsub float %tmp3, %tmp4, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   %sub69 = fsub float %tmp5, %tmp6, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   %sub69 = fsub float %tmp5, %tmp6, !taffo.info !13, !taffo.initweight !27
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



#Stuff for   %sub69 = fsub float %tmp5, %tmp6, !taffo.info !13, !taffo.initweight !27
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



#Constraint for cast for   %mul70 = fmul float %sub, %sub69, !taffo.info !13, !taffo.initweight !30
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



#Constraint for cast for   %mul70 = fmul float %sub, %sub69, !taffo.info !13, !taffo.initweight !30
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



#Stuff for   %mul70 = fmul float %sub, %sub69, !taffo.info !13, !taffo.initweight !30
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



#Constraint for cast for   %add73 = fadd float %tmp7, %mul70, !taffo.info !21, !taffo.initweight !27
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



#Constraint for cast for   %add73 = fadd float %tmp7, %mul70, !taffo.info !21, !taffo.initweight !27
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



#Stuff for   %add73 = fadd float %tmp7, %mul70, !taffo.info !21, !taffo.initweight !27
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



#Constraint for cast for   store float %add73, float* %arrayidx72, align 4, !taffo.info !21, !taffo.initweight !26
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



#Stuff for   %conv77 = sitofp i32 28 to float, !taffo.info !41, !taffo.initweight !26
main_conv77_fixbits = solver.IntVar(0, 20, 'main_conv77_fixbits')
main_conv77_fixp = solver.IntVar(0, 1, 'main_conv77_fixp')
main_conv77_float = solver.IntVar(0, 1, 'main_conv77_float')
main_conv77_double = solver.IntVar(0, 1, 'main_conv77_double')
main_conv77_enob = solver.IntVar(-10000, 10000, 'main_conv77_enob')
solver.Add( + (1)*main_conv77_enob + (-1)*main_conv77_fixbits + (10000)*main_conv77_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv77_enob + (10000)*main_conv77_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_conv77_enob + (10000)*main_conv77_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_conv77_fixbits + (-10000)*main_conv77_fixp>=-9981)    #Limit the lower number of frac bits20
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



#Constraint for cast for   %div80 = fdiv float %tmp8, %conv77, !taffo.info !21, !taffo.initweight !27
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



#Constraint for cast for   %div80 = fdiv float %tmp8, %conv77, !taffo.info !21, !taffo.initweight !27
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



#Stuff for   %div80 = fdiv float %tmp8, %conv77, !taffo.info !21, !taffo.initweight !27
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



#Constraint for cast for   store float %div80, float* %arrayidx79, align 4, !taffo.info !21, !taffo.initweight !26
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



#Stuff for   %call = call double @sqrt(double %conv83) #1, !taffo.info !21, !taffo.initweight !30, !taffo.constinfo !37
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



#Constraint for cast for   %call = call double @sqrt(double %conv83) #1, !taffo.info !21, !taffo.initweight !30, !taffo.constinfo !37
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



#Constraint for cast for   store float %conv84, float* %arrayidx86, align 4, !taffo.info !21, !taffo.initweight !26
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



#Stuff for float 0x3FB99999A0000000
ConstantValue__2_fixbits = solver.IntVar(0, 31, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10027)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10056)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cmp89 = fcmp ole float %tmp10, 0x3FB99999A0000000, !taffo.info !44, !taffo.initweight !26
main_stddev_CAST_cmp89_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_cmp89_fixbits')
main_stddev_CAST_cmp89_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_cmp89_fixp')
main_stddev_CAST_cmp89_float = solver.IntVar(0, 1, 'main_stddev_CAST_cmp89_float')
main_stddev_CAST_cmp89_double = solver.IntVar(0, 1, 'main_stddev_CAST_cmp89_double')
solver.Add( + (1)*main_stddev_CAST_cmp89_fixp + (1)*main_stddev_CAST_cmp89_float + (1)*main_stddev_CAST_cmp89_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_cmp89_fixbits + (-10000)*main_stddev_CAST_cmp89_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_cmp89')
C2_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_cmp89')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_cmp89_fixbits + (-10000)*C1_main_stddev_CAST_cmp89<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_cmp89_fixbits + (-10000)*C2_main_stddev_CAST_cmp89<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_stddev_CAST_cmp89
objectiveFunction +=  + (50)*C2_main_stddev_CAST_cmp89
C3_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_cmp89')
C4_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_cmp89')
C5_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_cmp89')
C6_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_cmp89')
C7_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_cmp89')
C8_main_stddev_CAST_cmp89 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_cmp89')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cmp89_float + (-1)*C3_main_stddev_CAST_cmp89<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_cmp89
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cmp89_fixp + (-1)*C4_main_stddev_CAST_cmp89<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_cmp89
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_cmp89_double + (-1)*C5_main_stddev_CAST_cmp89<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_cmp89
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cmp89_fixp + (-1)*C6_main_stddev_CAST_cmp89<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_cmp89
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_cmp89_double + (-1)*C7_main_stddev_CAST_cmp89<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_cmp89
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_cmp89_float + (-1)*C8_main_stddev_CAST_cmp89<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_cmp89



#Constraint for cast for   %cmp89 = fcmp ole float %tmp10, 0x3FB99999A0000000, !taffo.info !44, !taffo.initweight !26
ConstantValue__2_CAST_cmp89_fixbits = solver.IntVar(0, 31, 'ConstantValue__2_CAST_cmp89_fixbits')
ConstantValue__2_CAST_cmp89_fixp = solver.IntVar(0, 1, 'ConstantValue__2_CAST_cmp89_fixp')
ConstantValue__2_CAST_cmp89_float = solver.IntVar(0, 1, 'ConstantValue__2_CAST_cmp89_float')
ConstantValue__2_CAST_cmp89_double = solver.IntVar(0, 1, 'ConstantValue__2_CAST_cmp89_double')
solver.Add( + (1)*ConstantValue__2_CAST_cmp89_fixp + (1)*ConstantValue__2_CAST_cmp89_float + (1)*ConstantValue__2_CAST_cmp89_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__2_CAST_cmp89_fixbits + (-10000)*ConstantValue__2_CAST_cmp89_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C1_ConstantValue__2_CAST_cmp89')
C2_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C2_ConstantValue__2_CAST_cmp89')
solver.Add( + (1)*ConstantValue__2_fixbits + (-1)*ConstantValue__2_CAST_cmp89_fixbits + (-10000)*C1_ConstantValue__2_CAST_cmp89<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__2_fixbits + (1)*ConstantValue__2_CAST_cmp89_fixbits + (-10000)*C2_ConstantValue__2_CAST_cmp89<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__2_CAST_cmp89
objectiveFunction +=  + (50)*C2_ConstantValue__2_CAST_cmp89
C3_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C3_ConstantValue__2_CAST_cmp89')
C4_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C4_ConstantValue__2_CAST_cmp89')
C5_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C5_ConstantValue__2_CAST_cmp89')
C6_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C6_ConstantValue__2_CAST_cmp89')
C7_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C7_ConstantValue__2_CAST_cmp89')
C8_ConstantValue__2_CAST_cmp89 = solver.IntVar(0, 1, 'C8_ConstantValue__2_CAST_cmp89')
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_CAST_cmp89_float + (-1)*C3_ConstantValue__2_CAST_cmp89<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__2_CAST_cmp89
solver.Add( + (1)*ConstantValue__2_float + (1)*ConstantValue__2_CAST_cmp89_fixp + (-1)*C4_ConstantValue__2_CAST_cmp89<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__2_CAST_cmp89
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_CAST_cmp89_double + (-1)*C5_ConstantValue__2_CAST_cmp89<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__2_CAST_cmp89
solver.Add( + (1)*ConstantValue__2_double + (1)*ConstantValue__2_CAST_cmp89_fixp + (-1)*C6_ConstantValue__2_CAST_cmp89<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__2_CAST_cmp89
solver.Add( + (1)*ConstantValue__2_float + (1)*ConstantValue__2_CAST_cmp89_double + (-1)*C7_ConstantValue__2_CAST_cmp89<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__2_CAST_cmp89
solver.Add( + (1)*ConstantValue__2_double + (1)*ConstantValue__2_CAST_cmp89_float + (-1)*C8_ConstantValue__2_CAST_cmp89<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__2_CAST_cmp89
solver.Add( + (1)*main_stddev_CAST_cmp89_fixp + (-1)*ConstantValue__2_CAST_cmp89_fixp==0)    #fix equality
solver.Add( + (1)*main_stddev_CAST_cmp89_float + (-1)*ConstantValue__2_CAST_cmp89_float==0)    #float equality
solver.Add( + (1)*main_stddev_CAST_cmp89_double + (-1)*ConstantValue__2_CAST_cmp89_double==0)    #double equality
solver.Add( + (1)*main_stddev_CAST_cmp89_fixbits + (-1)*ConstantValue__2_CAST_cmp89_fixbits==0)    #same fractional bit

#Restriction for new enob [LOAD]
main_stddev_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'main_stddev_enob_memphi_main_tmp11')
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp11 + (-1)*main_stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_0 = solver.IntVar(0, 1, 'main_main_tmp11_enob_0')
solver.Add( + (1)*main_main_tmp11_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_stddev_enob_memphi_main_tmp11 + (-1)*main_stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %conv93, %cond.false ], !taffo.info !21, !taffo.initweight !30
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
ConstantValue__3_fixbits = solver.IntVar(0, 31, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero
main_main_cond_enob_1 = solver.IntVar(0, 1, 'main_main_cond_enob_1')
solver.Add( + (1)*main_main_cond_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %conv93, %cond.false ], !taffo.info !21, !taffo.initweight !30
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



#Constraint for cast for   store float %conv94, float* %arrayidx96, align 4, !taffo.info !21, !taffo.initweight !26
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



#Constraint for cast for   %sub114 = fsub float %tmp13, %tmp12, !taffo.info !13, !taffo.initweight !27
main_data_CAST_sub114_fixbits = solver.IntVar(0, 30, 'main_data_CAST_sub114_fixbits')
main_data_CAST_sub114_fixp = solver.IntVar(0, 1, 'main_data_CAST_sub114_fixp')
main_data_CAST_sub114_float = solver.IntVar(0, 1, 'main_data_CAST_sub114_float')
main_data_CAST_sub114_double = solver.IntVar(0, 1, 'main_data_CAST_sub114_double')
solver.Add( + (1)*main_data_CAST_sub114_fixp + (1)*main_data_CAST_sub114_float + (1)*main_data_CAST_sub114_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_sub114_fixbits + (-10000)*main_data_CAST_sub114_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C1_main_data_CAST_sub114')
C2_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C2_main_data_CAST_sub114')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_sub114_fixbits + (-10000)*C1_main_data_CAST_sub114<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_sub114_fixbits + (-10000)*C2_main_data_CAST_sub114<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_sub114
objectiveFunction +=  + (50)*C2_main_data_CAST_sub114
C3_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C3_main_data_CAST_sub114')
C4_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C4_main_data_CAST_sub114')
C5_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C5_main_data_CAST_sub114')
C6_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C6_main_data_CAST_sub114')
C7_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C7_main_data_CAST_sub114')
C8_main_data_CAST_sub114 = solver.IntVar(0, 1, 'C8_main_data_CAST_sub114')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub114_float + (-1)*C3_main_data_CAST_sub114<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_sub114
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub114_fixp + (-1)*C4_main_data_CAST_sub114<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_sub114
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_sub114_double + (-1)*C5_main_data_CAST_sub114<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_sub114
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub114_fixp + (-1)*C6_main_data_CAST_sub114<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_sub114
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_sub114_double + (-1)*C7_main_data_CAST_sub114<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_sub114
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_sub114_float + (-1)*C8_main_data_CAST_sub114<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_sub114



#Constraint for cast for   %sub114 = fsub float %tmp13, %tmp12, !taffo.info !13, !taffo.initweight !27
main_mean_CAST_sub114_fixbits = solver.IntVar(0, 15, 'main_mean_CAST_sub114_fixbits')
main_mean_CAST_sub114_fixp = solver.IntVar(0, 1, 'main_mean_CAST_sub114_fixp')
main_mean_CAST_sub114_float = solver.IntVar(0, 1, 'main_mean_CAST_sub114_float')
main_mean_CAST_sub114_double = solver.IntVar(0, 1, 'main_mean_CAST_sub114_double')
solver.Add( + (1)*main_mean_CAST_sub114_fixp + (1)*main_mean_CAST_sub114_float + (1)*main_mean_CAST_sub114_double==1)    #exactly 1 type
solver.Add( + (1)*main_mean_CAST_sub114_fixbits + (-10000)*main_mean_CAST_sub114_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C1_main_mean_CAST_sub114')
C2_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C2_main_mean_CAST_sub114')
solver.Add( + (1)*main_mean_fixbits + (-1)*main_mean_CAST_sub114_fixbits + (-10000)*C1_main_mean_CAST_sub114<=0)    #Shift cost 1
solver.Add( + (-1)*main_mean_fixbits + (1)*main_mean_CAST_sub114_fixbits + (-10000)*C2_main_mean_CAST_sub114<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mean_CAST_sub114
objectiveFunction +=  + (50)*C2_main_mean_CAST_sub114
C3_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C3_main_mean_CAST_sub114')
C4_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C4_main_mean_CAST_sub114')
C5_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C5_main_mean_CAST_sub114')
C6_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C6_main_mean_CAST_sub114')
C7_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C7_main_mean_CAST_sub114')
C8_main_mean_CAST_sub114 = solver.IntVar(0, 1, 'C8_main_mean_CAST_sub114')
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub114_float + (-1)*C3_main_mean_CAST_sub114<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mean_CAST_sub114
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub114_fixp + (-1)*C4_main_mean_CAST_sub114<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mean_CAST_sub114
solver.Add( + (1)*main_mean_fixp + (1)*main_mean_CAST_sub114_double + (-1)*C5_main_mean_CAST_sub114<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mean_CAST_sub114
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub114_fixp + (-1)*C6_main_mean_CAST_sub114<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mean_CAST_sub114
solver.Add( + (1)*main_mean_float + (1)*main_mean_CAST_sub114_double + (-1)*C7_main_mean_CAST_sub114<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mean_CAST_sub114
solver.Add( + (1)*main_mean_double + (1)*main_mean_CAST_sub114_float + (-1)*C8_main_mean_CAST_sub114<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mean_CAST_sub114



#Stuff for   %sub114 = fsub float %tmp13, %tmp12, !taffo.info !13, !taffo.initweight !27
main_sub114_fixbits = solver.IntVar(0, 15, 'main_sub114_fixbits')
main_sub114_fixp = solver.IntVar(0, 1, 'main_sub114_fixp')
main_sub114_float = solver.IntVar(0, 1, 'main_sub114_float')
main_sub114_double = solver.IntVar(0, 1, 'main_sub114_double')
main_sub114_enob = solver.IntVar(-10000, 10000, 'main_sub114_enob')
solver.Add( + (1)*main_sub114_enob + (-1)*main_sub114_fixbits + (10000)*main_sub114_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub114_enob + (10000)*main_sub114_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub114_enob + (10000)*main_sub114_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub114_fixbits + (-10000)*main_sub114_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub114_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_sub114_enob
solver.Add( + (1)*main_sub114_fixp + (1)*main_sub114_float + (1)*main_sub114_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub114_fixbits + (-10000)*main_sub114_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_sub114_fixp + (-1)*main_mean_CAST_sub114_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub114_float + (-1)*main_mean_CAST_sub114_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub114_double + (-1)*main_mean_CAST_sub114_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub114_fixbits + (-1)*main_mean_CAST_sub114_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_data_CAST_sub114_fixp + (-1)*main_sub114_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_sub114_float + (-1)*main_sub114_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_sub114_double + (-1)*main_sub114_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_sub114_fixbits + (-1)*main_sub114_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_sub114_fixp
objectiveFunction +=  + (300)*main_sub114_float
objectiveFunction +=  + (664.928)*main_sub114_double
solver.Add( + (1)*main_sub114_enob + (-1)*main_data_enob_memphi_main_tmp13<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub114_enob + (-1)*main_mean_enob_memphi_main_tmp12<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store float %sub114, float* %arrayidx113, align 4, !taffo.info !17, !taffo.initweight !27
main_sub114_CAST_store_fixbits = solver.IntVar(0, 15, 'main_sub114_CAST_store_fixbits')
main_sub114_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub114_CAST_store_fixp')
main_sub114_CAST_store_float = solver.IntVar(0, 1, 'main_sub114_CAST_store_float')
main_sub114_CAST_store_double = solver.IntVar(0, 1, 'main_sub114_CAST_store_double')
solver.Add( + (1)*main_sub114_CAST_store_fixp + (1)*main_sub114_CAST_store_float + (1)*main_sub114_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub114_CAST_store_fixbits + (-10000)*main_sub114_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub114_CAST_store = solver.IntVar(0, 1, 'C1_main_sub114_CAST_store')
C2_main_sub114_CAST_store = solver.IntVar(0, 1, 'C2_main_sub114_CAST_store')
solver.Add( + (1)*main_sub114_fixbits + (-1)*main_sub114_CAST_store_fixbits + (-10000)*C1_main_sub114_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub114_fixbits + (1)*main_sub114_CAST_store_fixbits + (-10000)*C2_main_sub114_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_sub114_CAST_store
objectiveFunction +=  + (50)*C2_main_sub114_CAST_store
C3_main_sub114_CAST_store = solver.IntVar(0, 1, 'C3_main_sub114_CAST_store')
C4_main_sub114_CAST_store = solver.IntVar(0, 1, 'C4_main_sub114_CAST_store')
C5_main_sub114_CAST_store = solver.IntVar(0, 1, 'C5_main_sub114_CAST_store')
C6_main_sub114_CAST_store = solver.IntVar(0, 1, 'C6_main_sub114_CAST_store')
C7_main_sub114_CAST_store = solver.IntVar(0, 1, 'C7_main_sub114_CAST_store')
C8_main_sub114_CAST_store = solver.IntVar(0, 1, 'C8_main_sub114_CAST_store')
solver.Add( + (1)*main_sub114_fixp + (1)*main_sub114_CAST_store_float + (-1)*C3_main_sub114_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_sub114_CAST_store
solver.Add( + (1)*main_sub114_float + (1)*main_sub114_CAST_store_fixp + (-1)*C4_main_sub114_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_sub114_CAST_store
solver.Add( + (1)*main_sub114_fixp + (1)*main_sub114_CAST_store_double + (-1)*C5_main_sub114_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_sub114_CAST_store
solver.Add( + (1)*main_sub114_double + (1)*main_sub114_CAST_store_fixp + (-1)*C6_main_sub114_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_sub114_CAST_store
solver.Add( + (1)*main_sub114_float + (1)*main_sub114_CAST_store_double + (-1)*C7_main_sub114_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_sub114_CAST_store
solver.Add( + (1)*main_sub114_double + (1)*main_sub114_CAST_store_float + (-1)*C8_main_sub114_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_sub114_CAST_store
solver.Add( + (1)*main_data_fixp + (-1)*main_sub114_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_data_float + (-1)*main_sub114_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_data_double + (-1)*main_sub114_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_data_fixbits + (-1)*main_sub114_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_data_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_data_enob_storeENOB')
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob_storeENOB + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_enob_storeENOB + (-1)*main_sub114_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv115 = sitofp i32 28 to double, !taffo.info !41, !taffo.initweight !26
main_conv115_fixbits = solver.IntVar(0, 20, 'main_conv115_fixbits')
main_conv115_fixp = solver.IntVar(0, 1, 'main_conv115_fixp')
main_conv115_float = solver.IntVar(0, 1, 'main_conv115_float')
main_conv115_double = solver.IntVar(0, 1, 'main_conv115_double')
main_conv115_enob = solver.IntVar(-10000, 10000, 'main_conv115_enob')
solver.Add( + (1)*main_conv115_enob + (-1)*main_conv115_fixbits + (10000)*main_conv115_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv115_enob + (10000)*main_conv115_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_conv115_enob + (10000)*main_conv115_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_conv115_fixbits + (-10000)*main_conv115_fixp>=-9981)    #Limit the lower number of frac bits20
objectiveFunction +=  + (-1)*main_conv115_enob
solver.Add( + (1)*main_conv115_fixp + (1)*main_conv115_float + (1)*main_conv115_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv115_fixbits + (-10000)*main_conv115_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call116 = call double @sqrt(double %conv115) #1, !taffo.info !41, !taffo.initweight !27, !taffo.constinfo !37
main_call116_fixbits = solver.IntVar(0, 20, 'main_call116_fixbits')
main_call116_fixp = solver.IntVar(0, 1, 'main_call116_fixp')
main_call116_float = solver.IntVar(0, 1, 'main_call116_float')
main_call116_double = solver.IntVar(0, 1, 'main_call116_double')
main_call116_enob = solver.IntVar(-10000, 10000, 'main_call116_enob')
solver.Add( + (1)*main_call116_enob + (-1)*main_call116_fixbits + (10000)*main_call116_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call116_enob + (10000)*main_call116_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_call116_enob + (10000)*main_call116_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_call116_fixbits + (-10000)*main_call116_fixp>=-9981)    #Limit the lower number of frac bits20
objectiveFunction +=  + (-1)*main_call116_enob
solver.Add( + (1)*main_call116_fixp + (1)*main_call116_float + (1)*main_call116_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call116_fixbits + (-10000)*main_call116_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call116_double==1)    #Type constraint for return value



#Constraint for cast for   %call116 = call double @sqrt(double %conv115) #1, !taffo.info !41, !taffo.initweight !27, !taffo.constinfo !37
main_conv115_CAST_call116_fixbits = solver.IntVar(0, 20, 'main_conv115_CAST_call116_fixbits')
main_conv115_CAST_call116_fixp = solver.IntVar(0, 1, 'main_conv115_CAST_call116_fixp')
main_conv115_CAST_call116_float = solver.IntVar(0, 1, 'main_conv115_CAST_call116_float')
main_conv115_CAST_call116_double = solver.IntVar(0, 1, 'main_conv115_CAST_call116_double')
solver.Add( + (1)*main_conv115_CAST_call116_fixp + (1)*main_conv115_CAST_call116_float + (1)*main_conv115_CAST_call116_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv115_CAST_call116_fixbits + (-10000)*main_conv115_CAST_call116_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C1_main_conv115_CAST_call116')
C2_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C2_main_conv115_CAST_call116')
solver.Add( + (1)*main_conv115_fixbits + (-1)*main_conv115_CAST_call116_fixbits + (-10000)*C1_main_conv115_CAST_call116<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv115_fixbits + (1)*main_conv115_CAST_call116_fixbits + (-10000)*C2_main_conv115_CAST_call116<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_conv115_CAST_call116
objectiveFunction +=  + (50)*C2_main_conv115_CAST_call116
C3_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C3_main_conv115_CAST_call116')
C4_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C4_main_conv115_CAST_call116')
C5_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C5_main_conv115_CAST_call116')
C6_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C6_main_conv115_CAST_call116')
C7_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C7_main_conv115_CAST_call116')
C8_main_conv115_CAST_call116 = solver.IntVar(0, 1, 'C8_main_conv115_CAST_call116')
solver.Add( + (1)*main_conv115_fixp + (1)*main_conv115_CAST_call116_float + (-1)*C3_main_conv115_CAST_call116<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_conv115_CAST_call116
solver.Add( + (1)*main_conv115_float + (1)*main_conv115_CAST_call116_fixp + (-1)*C4_main_conv115_CAST_call116<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_conv115_CAST_call116
solver.Add( + (1)*main_conv115_fixp + (1)*main_conv115_CAST_call116_double + (-1)*C5_main_conv115_CAST_call116<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_conv115_CAST_call116
solver.Add( + (1)*main_conv115_double + (1)*main_conv115_CAST_call116_fixp + (-1)*C6_main_conv115_CAST_call116<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_conv115_CAST_call116
solver.Add( + (1)*main_conv115_float + (1)*main_conv115_CAST_call116_double + (-1)*C7_main_conv115_CAST_call116<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_conv115_CAST_call116
solver.Add( + (1)*main_conv115_double + (1)*main_conv115_CAST_call116_float + (-1)*C8_main_conv115_CAST_call116<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_conv115_CAST_call116
solver.Add( + (1)*main_conv115_CAST_call116_double==1)    #Type constraint for argument value

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



#Constraint for cast for   %mul120 = fmul double %call116, %conv119, !taffo.info !21, !taffo.initweight !30
main_call116_CAST_mul120_fixbits = solver.IntVar(0, 20, 'main_call116_CAST_mul120_fixbits')
main_call116_CAST_mul120_fixp = solver.IntVar(0, 1, 'main_call116_CAST_mul120_fixp')
main_call116_CAST_mul120_float = solver.IntVar(0, 1, 'main_call116_CAST_mul120_float')
main_call116_CAST_mul120_double = solver.IntVar(0, 1, 'main_call116_CAST_mul120_double')
solver.Add( + (1)*main_call116_CAST_mul120_fixp + (1)*main_call116_CAST_mul120_float + (1)*main_call116_CAST_mul120_double==1)    #exactly 1 type
solver.Add( + (1)*main_call116_CAST_mul120_fixbits + (-10000)*main_call116_CAST_mul120_fixp<=0)    #If no fix, fix frac part = 0
C1_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C1_main_call116_CAST_mul120')
C2_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C2_main_call116_CAST_mul120')
solver.Add( + (1)*main_call116_fixbits + (-1)*main_call116_CAST_mul120_fixbits + (-10000)*C1_main_call116_CAST_mul120<=0)    #Shift cost 1
solver.Add( + (-1)*main_call116_fixbits + (1)*main_call116_CAST_mul120_fixbits + (-10000)*C2_main_call116_CAST_mul120<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_call116_CAST_mul120
objectiveFunction +=  + (50)*C2_main_call116_CAST_mul120
C3_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C3_main_call116_CAST_mul120')
C4_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C4_main_call116_CAST_mul120')
C5_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C5_main_call116_CAST_mul120')
C6_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C6_main_call116_CAST_mul120')
C7_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C7_main_call116_CAST_mul120')
C8_main_call116_CAST_mul120 = solver.IntVar(0, 1, 'C8_main_call116_CAST_mul120')
solver.Add( + (1)*main_call116_fixp + (1)*main_call116_CAST_mul120_float + (-1)*C3_main_call116_CAST_mul120<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_call116_CAST_mul120
solver.Add( + (1)*main_call116_float + (1)*main_call116_CAST_mul120_fixp + (-1)*C4_main_call116_CAST_mul120<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_call116_CAST_mul120
solver.Add( + (1)*main_call116_fixp + (1)*main_call116_CAST_mul120_double + (-1)*C5_main_call116_CAST_mul120<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_call116_CAST_mul120
solver.Add( + (1)*main_call116_double + (1)*main_call116_CAST_mul120_fixp + (-1)*C6_main_call116_CAST_mul120<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_call116_CAST_mul120
solver.Add( + (1)*main_call116_float + (1)*main_call116_CAST_mul120_double + (-1)*C7_main_call116_CAST_mul120<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_call116_CAST_mul120
solver.Add( + (1)*main_call116_double + (1)*main_call116_CAST_mul120_float + (-1)*C8_main_call116_CAST_mul120<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_call116_CAST_mul120



#Constraint for cast for   %mul120 = fmul double %call116, %conv119, !taffo.info !21, !taffo.initweight !30
main_stddev_CAST_mul120_fixbits = solver.IntVar(0, 18, 'main_stddev_CAST_mul120_fixbits')
main_stddev_CAST_mul120_fixp = solver.IntVar(0, 1, 'main_stddev_CAST_mul120_fixp')
main_stddev_CAST_mul120_float = solver.IntVar(0, 1, 'main_stddev_CAST_mul120_float')
main_stddev_CAST_mul120_double = solver.IntVar(0, 1, 'main_stddev_CAST_mul120_double')
solver.Add( + (1)*main_stddev_CAST_mul120_fixp + (1)*main_stddev_CAST_mul120_float + (1)*main_stddev_CAST_mul120_double==1)    #exactly 1 type
solver.Add( + (1)*main_stddev_CAST_mul120_fixbits + (-10000)*main_stddev_CAST_mul120_fixp<=0)    #If no fix, fix frac part = 0
C1_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C1_main_stddev_CAST_mul120')
C2_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C2_main_stddev_CAST_mul120')
solver.Add( + (1)*main_stddev_fixbits + (-1)*main_stddev_CAST_mul120_fixbits + (-10000)*C1_main_stddev_CAST_mul120<=0)    #Shift cost 1
solver.Add( + (-1)*main_stddev_fixbits + (1)*main_stddev_CAST_mul120_fixbits + (-10000)*C2_main_stddev_CAST_mul120<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_stddev_CAST_mul120
objectiveFunction +=  + (50)*C2_main_stddev_CAST_mul120
C3_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C3_main_stddev_CAST_mul120')
C4_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C4_main_stddev_CAST_mul120')
C5_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C5_main_stddev_CAST_mul120')
C6_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C6_main_stddev_CAST_mul120')
C7_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C7_main_stddev_CAST_mul120')
C8_main_stddev_CAST_mul120 = solver.IntVar(0, 1, 'C8_main_stddev_CAST_mul120')
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_mul120_float + (-1)*C3_main_stddev_CAST_mul120<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_stddev_CAST_mul120
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_mul120_fixp + (-1)*C4_main_stddev_CAST_mul120<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_stddev_CAST_mul120
solver.Add( + (1)*main_stddev_fixp + (1)*main_stddev_CAST_mul120_double + (-1)*C5_main_stddev_CAST_mul120<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_stddev_CAST_mul120
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_mul120_fixp + (-1)*C6_main_stddev_CAST_mul120<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_stddev_CAST_mul120
solver.Add( + (1)*main_stddev_float + (1)*main_stddev_CAST_mul120_double + (-1)*C7_main_stddev_CAST_mul120<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_stddev_CAST_mul120
solver.Add( + (1)*main_stddev_double + (1)*main_stddev_CAST_mul120_float + (-1)*C8_main_stddev_CAST_mul120<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_stddev_CAST_mul120



#Stuff for   %mul120 = fmul double %call116, %conv119, !taffo.info !21, !taffo.initweight !30
main_mul120_fixbits = solver.IntVar(0, 18, 'main_mul120_fixbits')
main_mul120_fixp = solver.IntVar(0, 1, 'main_mul120_fixp')
main_mul120_float = solver.IntVar(0, 1, 'main_mul120_float')
main_mul120_double = solver.IntVar(0, 1, 'main_mul120_double')
main_mul120_enob = solver.IntVar(-10000, 10000, 'main_mul120_enob')
solver.Add( + (1)*main_mul120_enob + (-1)*main_mul120_fixbits + (10000)*main_mul120_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul120_enob + (10000)*main_mul120_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul120_enob + (10000)*main_mul120_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul120_fixbits + (-10000)*main_mul120_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_mul120_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_mul120_enob
solver.Add( + (1)*main_mul120_fixp + (1)*main_mul120_float + (1)*main_mul120_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul120_fixbits + (-10000)*main_mul120_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call116_CAST_mul120_fixp + (-1)*main_stddev_CAST_mul120_fixp==0)    #fix equality
solver.Add( + (1)*main_call116_CAST_mul120_float + (-1)*main_stddev_CAST_mul120_float==0)    #float equality
solver.Add( + (1)*main_call116_CAST_mul120_double + (-1)*main_stddev_CAST_mul120_double==0)    #double equality
solver.Add( + (1)*main_call116_CAST_mul120_fixp + (-1)*main_mul120_fixp==0)    #fix equality
solver.Add( + (1)*main_call116_CAST_mul120_float + (-1)*main_mul120_float==0)    #float equality
solver.Add( + (1)*main_call116_CAST_mul120_double + (-1)*main_mul120_double==0)    #double equality
objectiveFunction +=  + (165.217)*main_mul120_fixp
objectiveFunction +=  + (600)*main_mul120_float
objectiveFunction +=  + (1225.51)*main_mul120_double
main_main_mul120_enob_1 = solver.IntVar(0, 1, 'main_main_mul120_enob_1')
main_main_mul120_enob_2 = solver.IntVar(0, 1, 'main_main_mul120_enob_2')
solver.Add( + (1)*main_main_mul120_enob_1 + (1)*main_main_mul120_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul120_enob + (-1)*main_stddev_enob_memphi_main_tmp14 + (-10000)*main_main_mul120_enob_1<=0)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul120_enob + (-1)*main_call116_enob + (-10000)*main_main_mul120_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_data_enob_memphi_main_tmp15 = solver.IntVar(-10000, 10000, 'main_data_enob_memphi_main_tmp15')
solver.Add( + (1)*main_data_enob_memphi_main_tmp15 + (-1)*main_data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp15_enob_0 = solver.IntVar(0, 1, 'main_main_tmp15_enob_0')
solver.Add( + (1)*main_main_tmp15_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp15 + (-1)*main_data_enob_storeENOB + (10000)*main_main_tmp15_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div126 = fdiv double %conv125, %mul120, !taffo.info !17, !taffo.initweight !43
main_data_CAST_div126_fixbits = solver.IntVar(0, 30, 'main_data_CAST_div126_fixbits')
main_data_CAST_div126_fixp = solver.IntVar(0, 1, 'main_data_CAST_div126_fixp')
main_data_CAST_div126_float = solver.IntVar(0, 1, 'main_data_CAST_div126_float')
main_data_CAST_div126_double = solver.IntVar(0, 1, 'main_data_CAST_div126_double')
solver.Add( + (1)*main_data_CAST_div126_fixp + (1)*main_data_CAST_div126_float + (1)*main_data_CAST_div126_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_div126_fixbits + (-10000)*main_data_CAST_div126_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_div126 = solver.IntVar(0, 1, 'C1_main_data_CAST_div126')
C2_main_data_CAST_div126 = solver.IntVar(0, 1, 'C2_main_data_CAST_div126')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_div126_fixbits + (-10000)*C1_main_data_CAST_div126<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_div126_fixbits + (-10000)*C2_main_data_CAST_div126<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_div126
objectiveFunction +=  + (50)*C2_main_data_CAST_div126
C3_main_data_CAST_div126 = solver.IntVar(0, 1, 'C3_main_data_CAST_div126')
C4_main_data_CAST_div126 = solver.IntVar(0, 1, 'C4_main_data_CAST_div126')
C5_main_data_CAST_div126 = solver.IntVar(0, 1, 'C5_main_data_CAST_div126')
C6_main_data_CAST_div126 = solver.IntVar(0, 1, 'C6_main_data_CAST_div126')
C7_main_data_CAST_div126 = solver.IntVar(0, 1, 'C7_main_data_CAST_div126')
C8_main_data_CAST_div126 = solver.IntVar(0, 1, 'C8_main_data_CAST_div126')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_div126_float + (-1)*C3_main_data_CAST_div126<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_div126
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_div126_fixp + (-1)*C4_main_data_CAST_div126<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_div126
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_div126_double + (-1)*C5_main_data_CAST_div126<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_div126
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_div126_fixp + (-1)*C6_main_data_CAST_div126<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_div126
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_div126_double + (-1)*C7_main_data_CAST_div126<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_div126
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_div126_float + (-1)*C8_main_data_CAST_div126<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_div126



#Constraint for cast for   %div126 = fdiv double %conv125, %mul120, !taffo.info !17, !taffo.initweight !43
main_mul120_CAST_div126_fixbits = solver.IntVar(0, 18, 'main_mul120_CAST_div126_fixbits')
main_mul120_CAST_div126_fixp = solver.IntVar(0, 1, 'main_mul120_CAST_div126_fixp')
main_mul120_CAST_div126_float = solver.IntVar(0, 1, 'main_mul120_CAST_div126_float')
main_mul120_CAST_div126_double = solver.IntVar(0, 1, 'main_mul120_CAST_div126_double')
solver.Add( + (1)*main_mul120_CAST_div126_fixp + (1)*main_mul120_CAST_div126_float + (1)*main_mul120_CAST_div126_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul120_CAST_div126_fixbits + (-10000)*main_mul120_CAST_div126_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C1_main_mul120_CAST_div126')
C2_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C2_main_mul120_CAST_div126')
solver.Add( + (1)*main_mul120_fixbits + (-1)*main_mul120_CAST_div126_fixbits + (-10000)*C1_main_mul120_CAST_div126<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul120_fixbits + (1)*main_mul120_CAST_div126_fixbits + (-10000)*C2_main_mul120_CAST_div126<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mul120_CAST_div126
objectiveFunction +=  + (50)*C2_main_mul120_CAST_div126
C3_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C3_main_mul120_CAST_div126')
C4_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C4_main_mul120_CAST_div126')
C5_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C5_main_mul120_CAST_div126')
C6_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C6_main_mul120_CAST_div126')
C7_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C7_main_mul120_CAST_div126')
C8_main_mul120_CAST_div126 = solver.IntVar(0, 1, 'C8_main_mul120_CAST_div126')
solver.Add( + (1)*main_mul120_fixp + (1)*main_mul120_CAST_div126_float + (-1)*C3_main_mul120_CAST_div126<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mul120_CAST_div126
solver.Add( + (1)*main_mul120_float + (1)*main_mul120_CAST_div126_fixp + (-1)*C4_main_mul120_CAST_div126<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mul120_CAST_div126
solver.Add( + (1)*main_mul120_fixp + (1)*main_mul120_CAST_div126_double + (-1)*C5_main_mul120_CAST_div126<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mul120_CAST_div126
solver.Add( + (1)*main_mul120_double + (1)*main_mul120_CAST_div126_fixp + (-1)*C6_main_mul120_CAST_div126<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mul120_CAST_div126
solver.Add( + (1)*main_mul120_float + (1)*main_mul120_CAST_div126_double + (-1)*C7_main_mul120_CAST_div126<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mul120_CAST_div126
solver.Add( + (1)*main_mul120_double + (1)*main_mul120_CAST_div126_float + (-1)*C8_main_mul120_CAST_div126<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mul120_CAST_div126



#Stuff for   %div126 = fdiv double %conv125, %mul120, !taffo.info !17, !taffo.initweight !43
main_div126_fixbits = solver.IntVar(0, 30, 'main_div126_fixbits')
main_div126_fixp = solver.IntVar(0, 1, 'main_div126_fixp')
main_div126_float = solver.IntVar(0, 1, 'main_div126_float')
main_div126_double = solver.IntVar(0, 1, 'main_div126_double')
main_div126_enob = solver.IntVar(-10000, 10000, 'main_div126_enob')
solver.Add( + (1)*main_div126_enob + (-1)*main_div126_fixbits + (10000)*main_div126_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div126_enob + (10000)*main_div126_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div126_enob + (10000)*main_div126_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div126_fixbits + (-10000)*main_div126_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_div126_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_div126_enob
solver.Add( + (1)*main_div126_fixp + (1)*main_div126_float + (1)*main_div126_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div126_fixbits + (-10000)*main_div126_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_div126_fixp + (-1)*main_mul120_CAST_div126_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_div126_float + (-1)*main_mul120_CAST_div126_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_div126_double + (-1)*main_mul120_CAST_div126_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_div126_fixp + (-1)*main_div126_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_div126_float + (-1)*main_div126_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_div126_double + (-1)*main_div126_double==0)    #double equality
objectiveFunction +=  + (161.159)*main_div126_fixp
objectiveFunction +=  + (600)*main_div126_float
objectiveFunction +=  + (1200)*main_div126_double
main_main_div126_enob_1 = solver.IntVar(0, 1, 'main_main_div126_enob_1')
main_main_div126_enob_2 = solver.IntVar(0, 1, 'main_main_div126_enob_2')
solver.Add( + (1)*main_main_div126_enob_1 + (1)*main_main_div126_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div126_enob + (-1)*main_mul120_enob + (-10000)*main_main_div126_enob_1<=1048)    #Enob: propagation in division 1
solver.Add( + (1)*main_div126_enob + (-1)*main_data_enob_memphi_main_tmp15 + (-10000)*main_main_div126_enob_2<=1048)    #Enob: propagation in division 2



#Constraint for cast for   store float %conv127, float* %arrayidx124, align 4, !taffo.info !17, !taffo.initweight !27
main_div126_CAST_store_fixbits = solver.IntVar(0, 30, 'main_div126_CAST_store_fixbits')
main_div126_CAST_store_fixp = solver.IntVar(0, 1, 'main_div126_CAST_store_fixp')
main_div126_CAST_store_float = solver.IntVar(0, 1, 'main_div126_CAST_store_float')
main_div126_CAST_store_double = solver.IntVar(0, 1, 'main_div126_CAST_store_double')
solver.Add( + (1)*main_div126_CAST_store_fixp + (1)*main_div126_CAST_store_float + (1)*main_div126_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div126_CAST_store_fixbits + (-10000)*main_div126_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div126_CAST_store = solver.IntVar(0, 1, 'C1_main_div126_CAST_store')
C2_main_div126_CAST_store = solver.IntVar(0, 1, 'C2_main_div126_CAST_store')
solver.Add( + (1)*main_div126_fixbits + (-1)*main_div126_CAST_store_fixbits + (-10000)*C1_main_div126_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div126_fixbits + (1)*main_div126_CAST_store_fixbits + (-10000)*C2_main_div126_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_div126_CAST_store
objectiveFunction +=  + (50)*C2_main_div126_CAST_store
C3_main_div126_CAST_store = solver.IntVar(0, 1, 'C3_main_div126_CAST_store')
C4_main_div126_CAST_store = solver.IntVar(0, 1, 'C4_main_div126_CAST_store')
C5_main_div126_CAST_store = solver.IntVar(0, 1, 'C5_main_div126_CAST_store')
C6_main_div126_CAST_store = solver.IntVar(0, 1, 'C6_main_div126_CAST_store')
C7_main_div126_CAST_store = solver.IntVar(0, 1, 'C7_main_div126_CAST_store')
C8_main_div126_CAST_store = solver.IntVar(0, 1, 'C8_main_div126_CAST_store')
solver.Add( + (1)*main_div126_fixp + (1)*main_div126_CAST_store_float + (-1)*C3_main_div126_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_div126_CAST_store
solver.Add( + (1)*main_div126_float + (1)*main_div126_CAST_store_fixp + (-1)*C4_main_div126_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_div126_CAST_store
solver.Add( + (1)*main_div126_fixp + (1)*main_div126_CAST_store_double + (-1)*C5_main_div126_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_div126_CAST_store
solver.Add( + (1)*main_div126_double + (1)*main_div126_CAST_store_fixp + (-1)*C6_main_div126_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_div126_CAST_store
solver.Add( + (1)*main_div126_float + (1)*main_div126_CAST_store_double + (-1)*C7_main_div126_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_div126_CAST_store
solver.Add( + (1)*main_div126_double + (1)*main_div126_CAST_store_float + (-1)*C8_main_div126_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_div126_CAST_store
solver.Add( + (1)*main_data_fixp + (-1)*main_div126_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_data_float + (-1)*main_div126_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_data_double + (-1)*main_div126_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_data_fixbits + (-1)*main_div126_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_data_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_data_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (-1)*main_data_fixbits + (10000)*main_data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (10000)*main_data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (10000)*main_data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_data_enob_storeENOB_storeENOB + (-1)*main_div126_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_data_enob_memphi_main_tmp13 + (-1)*main_data_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_4<=10000)    #Enob: forcing MEM phi enob



#Stuff for float 1.000000e+00
ConstantValue__4_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store float 1.000000e+00, float* %arrayidx141, align 4, !taffo.info !19, !taffo.initweight !27, !taffo.constinfo !46
ConstantValue__4_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_CAST_store_fixbits')
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
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__4_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__4_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__4_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__4_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Constraint for cast for   store float 0.000000e+00, float* %arrayidx150, align 4, !taffo.info !19, !taffo.initweight !27, !taffo.constinfo !38
ConstantValue__1_CAST_store_1_fixbits = solver.IntVar(0, 32, 'ConstantValue__1_CAST_store_1_fixbits')
ConstantValue__1_CAST_store_1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_1_fixp')
ConstantValue__1_CAST_store_1_float = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_1_float')
ConstantValue__1_CAST_store_1_double = solver.IntVar(0, 1, 'ConstantValue__1_CAST_store_1_double')
solver.Add( + (1)*ConstantValue__1_CAST_store_1_fixp + (1)*ConstantValue__1_CAST_store_1_float + (1)*ConstantValue__1_CAST_store_1_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__1_CAST_store_1_fixbits + (-10000)*ConstantValue__1_CAST_store_1_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C1_ConstantValue__1_CAST_store_1')
C2_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C2_ConstantValue__1_CAST_store_1')
solver.Add( + (1)*ConstantValue__1_fixbits + (-1)*ConstantValue__1_CAST_store_1_fixbits + (-10000)*C1_ConstantValue__1_CAST_store_1<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__1_fixbits + (1)*ConstantValue__1_CAST_store_1_fixbits + (-10000)*C2_ConstantValue__1_CAST_store_1<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__1_CAST_store_1
objectiveFunction +=  + (50)*C2_ConstantValue__1_CAST_store_1
C3_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C3_ConstantValue__1_CAST_store_1')
C4_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C4_ConstantValue__1_CAST_store_1')
C5_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C5_ConstantValue__1_CAST_store_1')
C6_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C6_ConstantValue__1_CAST_store_1')
C7_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C7_ConstantValue__1_CAST_store_1')
C8_ConstantValue__1_CAST_store_1 = solver.IntVar(0, 1, 'C8_ConstantValue__1_CAST_store_1')
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_store_1_float + (-1)*C3_ConstantValue__1_CAST_store_1<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__1_CAST_store_1
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_store_1_fixp + (-1)*C4_ConstantValue__1_CAST_store_1<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__1_CAST_store_1
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_store_1_double + (-1)*C5_ConstantValue__1_CAST_store_1<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__1_CAST_store_1
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_store_1_fixp + (-1)*C6_ConstantValue__1_CAST_store_1<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__1_CAST_store_1
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_store_1_double + (-1)*C7_ConstantValue__1_CAST_store_1<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__1_CAST_store_1
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_store_1_float + (-1)*C8_ConstantValue__1_CAST_store_1<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__1_CAST_store_1
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__1_CAST_store_1_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__1_CAST_store_1_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__1_CAST_store_1_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__1_CAST_store_1_fixbits==0)    #same fractional bit

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



#Constraint for cast for   %mul163 = fmul float %tmp16, %tmp17, !taffo.info !17, !taffo.initweight !30
main_data_CAST_mul163_fixbits = solver.IntVar(0, 30, 'main_data_CAST_mul163_fixbits')
main_data_CAST_mul163_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul163_fixp')
main_data_CAST_mul163_float = solver.IntVar(0, 1, 'main_data_CAST_mul163_float')
main_data_CAST_mul163_double = solver.IntVar(0, 1, 'main_data_CAST_mul163_double')
solver.Add( + (1)*main_data_CAST_mul163_fixp + (1)*main_data_CAST_mul163_float + (1)*main_data_CAST_mul163_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul163_fixbits + (-10000)*main_data_CAST_mul163_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul163')
C2_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul163')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul163_fixbits + (-10000)*C1_main_data_CAST_mul163<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul163_fixbits + (-10000)*C2_main_data_CAST_mul163<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_mul163
objectiveFunction +=  + (50)*C2_main_data_CAST_mul163
C3_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul163')
C4_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul163')
C5_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul163')
C6_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul163')
C7_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul163')
C8_main_data_CAST_mul163 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul163')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul163_float + (-1)*C3_main_data_CAST_mul163<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_mul163
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul163_fixp + (-1)*C4_main_data_CAST_mul163<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_mul163
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul163_double + (-1)*C5_main_data_CAST_mul163<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_mul163
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul163_fixp + (-1)*C6_main_data_CAST_mul163<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_mul163
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul163_double + (-1)*C7_main_data_CAST_mul163<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_mul163
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul163_float + (-1)*C8_main_data_CAST_mul163<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_mul163



#Constraint for cast for   %mul163 = fmul float %tmp16, %tmp17, !taffo.info !17, !taffo.initweight !30
main_data_CAST_mul163_0_fixbits = solver.IntVar(0, 30, 'main_data_CAST_mul163_0_fixbits')
main_data_CAST_mul163_0_fixp = solver.IntVar(0, 1, 'main_data_CAST_mul163_0_fixp')
main_data_CAST_mul163_0_float = solver.IntVar(0, 1, 'main_data_CAST_mul163_0_float')
main_data_CAST_mul163_0_double = solver.IntVar(0, 1, 'main_data_CAST_mul163_0_double')
solver.Add( + (1)*main_data_CAST_mul163_0_fixp + (1)*main_data_CAST_mul163_0_float + (1)*main_data_CAST_mul163_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_data_CAST_mul163_0_fixbits + (-10000)*main_data_CAST_mul163_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C1_main_data_CAST_mul163_0')
C2_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C2_main_data_CAST_mul163_0')
solver.Add( + (1)*main_data_fixbits + (-1)*main_data_CAST_mul163_0_fixbits + (-10000)*C1_main_data_CAST_mul163_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_data_fixbits + (1)*main_data_CAST_mul163_0_fixbits + (-10000)*C2_main_data_CAST_mul163_0<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_data_CAST_mul163_0
objectiveFunction +=  + (50)*C2_main_data_CAST_mul163_0
C3_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C3_main_data_CAST_mul163_0')
C4_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C4_main_data_CAST_mul163_0')
C5_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C5_main_data_CAST_mul163_0')
C6_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C6_main_data_CAST_mul163_0')
C7_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C7_main_data_CAST_mul163_0')
C8_main_data_CAST_mul163_0 = solver.IntVar(0, 1, 'C8_main_data_CAST_mul163_0')
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul163_0_float + (-1)*C3_main_data_CAST_mul163_0<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_data_CAST_mul163_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul163_0_fixp + (-1)*C4_main_data_CAST_mul163_0<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_data_CAST_mul163_0
solver.Add( + (1)*main_data_fixp + (1)*main_data_CAST_mul163_0_double + (-1)*C5_main_data_CAST_mul163_0<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_data_CAST_mul163_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul163_0_fixp + (-1)*C6_main_data_CAST_mul163_0<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_data_CAST_mul163_0
solver.Add( + (1)*main_data_float + (1)*main_data_CAST_mul163_0_double + (-1)*C7_main_data_CAST_mul163_0<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_data_CAST_mul163_0
solver.Add( + (1)*main_data_double + (1)*main_data_CAST_mul163_0_float + (-1)*C8_main_data_CAST_mul163_0<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_data_CAST_mul163_0



#Stuff for   %mul163 = fmul float %tmp16, %tmp17, !taffo.info !17, !taffo.initweight !30
main_mul163_fixbits = solver.IntVar(0, 30, 'main_mul163_fixbits')
main_mul163_fixp = solver.IntVar(0, 1, 'main_mul163_fixp')
main_mul163_float = solver.IntVar(0, 1, 'main_mul163_float')
main_mul163_double = solver.IntVar(0, 1, 'main_mul163_double')
main_mul163_enob = solver.IntVar(-10000, 10000, 'main_mul163_enob')
solver.Add( + (1)*main_mul163_enob + (-1)*main_mul163_fixbits + (10000)*main_mul163_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul163_enob + (10000)*main_mul163_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul163_enob + (10000)*main_mul163_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul163_fixbits + (-10000)*main_mul163_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_mul163_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_mul163_enob
solver.Add( + (1)*main_mul163_fixp + (1)*main_mul163_float + (1)*main_mul163_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul163_fixbits + (-10000)*main_mul163_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_data_CAST_mul163_fixp + (-1)*main_data_CAST_mul163_0_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul163_float + (-1)*main_data_CAST_mul163_0_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul163_double + (-1)*main_data_CAST_mul163_0_double==0)    #double equality
solver.Add( + (1)*main_data_CAST_mul163_fixp + (-1)*main_mul163_fixp==0)    #fix equality
solver.Add( + (1)*main_data_CAST_mul163_float + (-1)*main_mul163_float==0)    #float equality
solver.Add( + (1)*main_data_CAST_mul163_double + (-1)*main_mul163_double==0)    #double equality
objectiveFunction +=  + (165.217)*main_mul163_fixp
objectiveFunction +=  + (600)*main_mul163_float
objectiveFunction +=  + (1225.51)*main_mul163_double
main_main_mul163_enob_1 = solver.IntVar(0, 1, 'main_main_mul163_enob_1')
main_main_mul163_enob_2 = solver.IntVar(0, 1, 'main_main_mul163_enob_2')
solver.Add( + (1)*main_main_mul163_enob_1 + (1)*main_main_mul163_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul163_enob + (-1)*main_data_enob_memphi_main_tmp17 + (-10000)*main_main_mul163_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul163_enob + (-1)*main_data_enob_memphi_main_tmp16 + (-10000)*main_main_mul163_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp18 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp18')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp18 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp18_enob_1 = solver.IntVar(0, 1, 'main_main_tmp18_enob_1')
solver.Add( + (1)*main_main_tmp18_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add168 = fadd float %tmp18, %mul163, !taffo.info !19, !taffo.initweight !30
main_corr_CAST_add168_fixbits = solver.IntVar(0, 29, 'main_corr_CAST_add168_fixbits')
main_corr_CAST_add168_fixp = solver.IntVar(0, 1, 'main_corr_CAST_add168_fixp')
main_corr_CAST_add168_float = solver.IntVar(0, 1, 'main_corr_CAST_add168_float')
main_corr_CAST_add168_double = solver.IntVar(0, 1, 'main_corr_CAST_add168_double')
solver.Add( + (1)*main_corr_CAST_add168_fixp + (1)*main_corr_CAST_add168_float + (1)*main_corr_CAST_add168_double==1)    #exactly 1 type
solver.Add( + (1)*main_corr_CAST_add168_fixbits + (-10000)*main_corr_CAST_add168_fixp<=0)    #If no fix, fix frac part = 0
C1_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C1_main_corr_CAST_add168')
C2_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C2_main_corr_CAST_add168')
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_add168_fixbits + (-10000)*C1_main_corr_CAST_add168<=0)    #Shift cost 1
solver.Add( + (-1)*main_corr_fixbits + (1)*main_corr_CAST_add168_fixbits + (-10000)*C2_main_corr_CAST_add168<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_corr_CAST_add168
objectiveFunction +=  + (50)*C2_main_corr_CAST_add168
C3_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C3_main_corr_CAST_add168')
C4_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C4_main_corr_CAST_add168')
C5_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C5_main_corr_CAST_add168')
C6_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C6_main_corr_CAST_add168')
C7_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C7_main_corr_CAST_add168')
C8_main_corr_CAST_add168 = solver.IntVar(0, 1, 'C8_main_corr_CAST_add168')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_add168_float + (-1)*C3_main_corr_CAST_add168<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_corr_CAST_add168
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_add168_fixp + (-1)*C4_main_corr_CAST_add168<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_corr_CAST_add168
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_add168_double + (-1)*C5_main_corr_CAST_add168<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_corr_CAST_add168
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_add168_fixp + (-1)*C6_main_corr_CAST_add168<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_corr_CAST_add168
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_add168_double + (-1)*C7_main_corr_CAST_add168<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_corr_CAST_add168
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_add168_float + (-1)*C8_main_corr_CAST_add168<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_corr_CAST_add168



#Constraint for cast for   %add168 = fadd float %tmp18, %mul163, !taffo.info !19, !taffo.initweight !30
main_mul163_CAST_add168_fixbits = solver.IntVar(0, 30, 'main_mul163_CAST_add168_fixbits')
main_mul163_CAST_add168_fixp = solver.IntVar(0, 1, 'main_mul163_CAST_add168_fixp')
main_mul163_CAST_add168_float = solver.IntVar(0, 1, 'main_mul163_CAST_add168_float')
main_mul163_CAST_add168_double = solver.IntVar(0, 1, 'main_mul163_CAST_add168_double')
solver.Add( + (1)*main_mul163_CAST_add168_fixp + (1)*main_mul163_CAST_add168_float + (1)*main_mul163_CAST_add168_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul163_CAST_add168_fixbits + (-10000)*main_mul163_CAST_add168_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C1_main_mul163_CAST_add168')
C2_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C2_main_mul163_CAST_add168')
solver.Add( + (1)*main_mul163_fixbits + (-1)*main_mul163_CAST_add168_fixbits + (-10000)*C1_main_mul163_CAST_add168<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul163_fixbits + (1)*main_mul163_CAST_add168_fixbits + (-10000)*C2_main_mul163_CAST_add168<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_mul163_CAST_add168
objectiveFunction +=  + (50)*C2_main_mul163_CAST_add168
C3_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C3_main_mul163_CAST_add168')
C4_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C4_main_mul163_CAST_add168')
C5_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C5_main_mul163_CAST_add168')
C6_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C6_main_mul163_CAST_add168')
C7_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C7_main_mul163_CAST_add168')
C8_main_mul163_CAST_add168 = solver.IntVar(0, 1, 'C8_main_mul163_CAST_add168')
solver.Add( + (1)*main_mul163_fixp + (1)*main_mul163_CAST_add168_float + (-1)*C3_main_mul163_CAST_add168<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_mul163_CAST_add168
solver.Add( + (1)*main_mul163_float + (1)*main_mul163_CAST_add168_fixp + (-1)*C4_main_mul163_CAST_add168<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_mul163_CAST_add168
solver.Add( + (1)*main_mul163_fixp + (1)*main_mul163_CAST_add168_double + (-1)*C5_main_mul163_CAST_add168<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_mul163_CAST_add168
solver.Add( + (1)*main_mul163_double + (1)*main_mul163_CAST_add168_fixp + (-1)*C6_main_mul163_CAST_add168<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_mul163_CAST_add168
solver.Add( + (1)*main_mul163_float + (1)*main_mul163_CAST_add168_double + (-1)*C7_main_mul163_CAST_add168<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_mul163_CAST_add168
solver.Add( + (1)*main_mul163_double + (1)*main_mul163_CAST_add168_float + (-1)*C8_main_mul163_CAST_add168<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_mul163_CAST_add168



#Stuff for   %add168 = fadd float %tmp18, %mul163, !taffo.info !19, !taffo.initweight !30
main_add168_fixbits = solver.IntVar(0, 29, 'main_add168_fixbits')
main_add168_fixp = solver.IntVar(0, 1, 'main_add168_fixp')
main_add168_float = solver.IntVar(0, 1, 'main_add168_float')
main_add168_double = solver.IntVar(0, 1, 'main_add168_double')
main_add168_enob = solver.IntVar(-10000, 10000, 'main_add168_enob')
solver.Add( + (1)*main_add168_enob + (-1)*main_add168_fixbits + (10000)*main_add168_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add168_enob + (10000)*main_add168_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add168_enob + (10000)*main_add168_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add168_fixbits + (-10000)*main_add168_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_add168_enob<=4)    #Enob constraint for error maximal
objectiveFunction +=  + (-1)*main_add168_enob
solver.Add( + (1)*main_add168_fixp + (1)*main_add168_float + (1)*main_add168_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add168_fixbits + (-10000)*main_add168_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_corr_CAST_add168_fixp + (-1)*main_mul163_CAST_add168_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_CAST_add168_float + (-1)*main_mul163_CAST_add168_float==0)    #float equality
solver.Add( + (1)*main_corr_CAST_add168_double + (-1)*main_mul163_CAST_add168_double==0)    #double equality
solver.Add( + (1)*main_corr_CAST_add168_fixbits + (-1)*main_mul163_CAST_add168_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_corr_CAST_add168_fixp + (-1)*main_add168_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_CAST_add168_float + (-1)*main_add168_float==0)    #float equality
solver.Add( + (1)*main_corr_CAST_add168_double + (-1)*main_add168_double==0)    #double equality
solver.Add( + (1)*main_corr_CAST_add168_fixbits + (-1)*main_add168_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_add168_fixp
objectiveFunction +=  + (300)*main_add168_float
objectiveFunction +=  + (664.928)*main_add168_double
solver.Add( + (1)*main_add168_enob + (-1)*main_corr_enob_memphi_main_tmp18<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add168_enob + (-1)*main_mul163_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store float %add168, float* %arrayidx167, align 4, !taffo.info !19, !taffo.initweight !27
main_add168_CAST_store_fixbits = solver.IntVar(0, 29, 'main_add168_CAST_store_fixbits')
main_add168_CAST_store_fixp = solver.IntVar(0, 1, 'main_add168_CAST_store_fixp')
main_add168_CAST_store_float = solver.IntVar(0, 1, 'main_add168_CAST_store_float')
main_add168_CAST_store_double = solver.IntVar(0, 1, 'main_add168_CAST_store_double')
solver.Add( + (1)*main_add168_CAST_store_fixp + (1)*main_add168_CAST_store_float + (1)*main_add168_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add168_CAST_store_fixbits + (-10000)*main_add168_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add168_CAST_store = solver.IntVar(0, 1, 'C1_main_add168_CAST_store')
C2_main_add168_CAST_store = solver.IntVar(0, 1, 'C2_main_add168_CAST_store')
solver.Add( + (1)*main_add168_fixbits + (-1)*main_add168_CAST_store_fixbits + (-10000)*C1_main_add168_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add168_fixbits + (1)*main_add168_CAST_store_fixbits + (-10000)*C2_main_add168_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_add168_CAST_store
objectiveFunction +=  + (50)*C2_main_add168_CAST_store
C3_main_add168_CAST_store = solver.IntVar(0, 1, 'C3_main_add168_CAST_store')
C4_main_add168_CAST_store = solver.IntVar(0, 1, 'C4_main_add168_CAST_store')
C5_main_add168_CAST_store = solver.IntVar(0, 1, 'C5_main_add168_CAST_store')
C6_main_add168_CAST_store = solver.IntVar(0, 1, 'C6_main_add168_CAST_store')
C7_main_add168_CAST_store = solver.IntVar(0, 1, 'C7_main_add168_CAST_store')
C8_main_add168_CAST_store = solver.IntVar(0, 1, 'C8_main_add168_CAST_store')
solver.Add( + (1)*main_add168_fixp + (1)*main_add168_CAST_store_float + (-1)*C3_main_add168_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_add168_CAST_store
solver.Add( + (1)*main_add168_float + (1)*main_add168_CAST_store_fixp + (-1)*C4_main_add168_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_add168_CAST_store
solver.Add( + (1)*main_add168_fixp + (1)*main_add168_CAST_store_double + (-1)*C5_main_add168_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_add168_CAST_store
solver.Add( + (1)*main_add168_double + (1)*main_add168_CAST_store_fixp + (-1)*C6_main_add168_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_add168_CAST_store
solver.Add( + (1)*main_add168_float + (1)*main_add168_CAST_store_double + (-1)*C7_main_add168_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_add168_CAST_store
solver.Add( + (1)*main_add168_double + (1)*main_add168_CAST_store_float + (-1)*C8_main_add168_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_add168_CAST_store
solver.Add( + (1)*main_corr_fixp + (-1)*main_add168_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*main_add168_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*main_add168_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*main_add168_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_corr_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_corr_enob_storeENOB')
solver.Add( + (1)*main_corr_enob_storeENOB + (-1)*main_corr_fixbits + (10000)*main_corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_corr_enob_storeENOB + (10000)*main_corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_corr_enob_storeENOB + (10000)*main_corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_corr_enob_storeENOB + (-1)*main_add168_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_corr_enob_memphi_main_tmp18 + (-1)*main_corr_enob_storeENOB + (10000)*main_main_tmp18_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp19 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp19')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp19 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp19_enob_1 = solver.IntVar(0, 1, 'main_main_tmp19_enob_1')
solver.Add( + (1)*main_main_tmp19_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_corr_enob_memphi_main_tmp19 + (-1)*main_corr_enob_storeENOB + (10000)*main_main_tmp19_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store float %tmp19, float* %arrayidx179, align 4, !taffo.info !19, !taffo.initweight !27
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



#Constraint for cast for   store float 1.000000e+00, float* %arrayidx187, align 4, !taffo.info !19, !taffo.initweight !27, !taffo.constinfo !46
ConstantValue__4_CAST_store_0_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_CAST_store_0_fixbits')
ConstantValue__4_CAST_store_0_fixp = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_0_fixp')
ConstantValue__4_CAST_store_0_float = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_0_float')
ConstantValue__4_CAST_store_0_double = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_0_double')
solver.Add( + (1)*ConstantValue__4_CAST_store_0_fixp + (1)*ConstantValue__4_CAST_store_0_float + (1)*ConstantValue__4_CAST_store_0_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__4_CAST_store_0_fixbits + (-10000)*ConstantValue__4_CAST_store_0_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C1_ConstantValue__4_CAST_store_0')
C2_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C2_ConstantValue__4_CAST_store_0')
solver.Add( + (1)*ConstantValue__4_fixbits + (-1)*ConstantValue__4_CAST_store_0_fixbits + (-10000)*C1_ConstantValue__4_CAST_store_0<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__4_fixbits + (1)*ConstantValue__4_CAST_store_0_fixbits + (-10000)*C2_ConstantValue__4_CAST_store_0<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__4_CAST_store_0
objectiveFunction +=  + (50)*C2_ConstantValue__4_CAST_store_0
C3_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_store_0')
C4_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_store_0')
C5_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_store_0')
C6_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_store_0')
C7_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_store_0')
C8_ConstantValue__4_CAST_store_0 = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_store_0')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_0_float + (-1)*C3_ConstantValue__4_CAST_store_0<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_ConstantValue__4_CAST_store_0
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_0_fixp + (-1)*C4_ConstantValue__4_CAST_store_0<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_ConstantValue__4_CAST_store_0
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_0_double + (-1)*C5_ConstantValue__4_CAST_store_0<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_ConstantValue__4_CAST_store_0
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_0_fixp + (-1)*C6_ConstantValue__4_CAST_store_0<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_ConstantValue__4_CAST_store_0
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_0_double + (-1)*C7_ConstantValue__4_CAST_store_0<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__4_CAST_store_0
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_0_float + (-1)*C8_ConstantValue__4_CAST_store_0<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__4_CAST_store_0
solver.Add( + (1)*main_corr_fixp + (-1)*ConstantValue__4_CAST_store_0_fixp==0)    #fix equality
solver.Add( + (1)*main_corr_float + (-1)*ConstantValue__4_CAST_store_0_float==0)    #float equality
solver.Add( + (1)*main_corr_double + (-1)*ConstantValue__4_CAST_store_0_double==0)    #double equality
solver.Add( + (1)*main_corr_fixbits + (-1)*ConstantValue__4_CAST_store_0_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_corr_enob_memphi_main_tmp20 = solver.IntVar(-10000, 10000, 'main_corr_enob_memphi_main_tmp20')
solver.Add( + (1)*main_corr_enob_memphi_main_tmp20 + (-1)*main_corr_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call202 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.10, i32 0, i32 0), double %conv201), !taffo.info !19, !taffo.initweight !43, !taffo.constinfo !49
main_corr_CAST_call202_fixbits = solver.IntVar(0, 29, 'main_corr_CAST_call202_fixbits')
main_corr_CAST_call202_fixp = solver.IntVar(0, 1, 'main_corr_CAST_call202_fixp')
main_corr_CAST_call202_float = solver.IntVar(0, 1, 'main_corr_CAST_call202_float')
main_corr_CAST_call202_double = solver.IntVar(0, 1, 'main_corr_CAST_call202_double')
solver.Add( + (1)*main_corr_CAST_call202_fixp + (1)*main_corr_CAST_call202_float + (1)*main_corr_CAST_call202_double==1)    #exactly 1 type
solver.Add( + (1)*main_corr_CAST_call202_fixbits + (-10000)*main_corr_CAST_call202_fixp<=0)    #If no fix, fix frac part = 0
C1_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C1_main_corr_CAST_call202')
C2_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C2_main_corr_CAST_call202')
solver.Add( + (1)*main_corr_fixbits + (-1)*main_corr_CAST_call202_fixbits + (-10000)*C1_main_corr_CAST_call202<=0)    #Shift cost 1
solver.Add( + (-1)*main_corr_fixbits + (1)*main_corr_CAST_call202_fixbits + (-10000)*C2_main_corr_CAST_call202<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_corr_CAST_call202
objectiveFunction +=  + (50)*C2_main_corr_CAST_call202
C3_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C3_main_corr_CAST_call202')
C4_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C4_main_corr_CAST_call202')
C5_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C5_main_corr_CAST_call202')
C6_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C6_main_corr_CAST_call202')
C7_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C7_main_corr_CAST_call202')
C8_main_corr_CAST_call202 = solver.IntVar(0, 1, 'C8_main_corr_CAST_call202')
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_call202_float + (-1)*C3_main_corr_CAST_call202<=1)    #Fix to float
objectiveFunction +=  + (312.613)*C3_main_corr_CAST_call202
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_call202_fixp + (-1)*C4_main_corr_CAST_call202<=1)    #Float to fix
objectiveFunction +=  + (73.6232)*C4_main_corr_CAST_call202
solver.Add( + (1)*main_corr_fixp + (1)*main_corr_CAST_call202_double + (-1)*C5_main_corr_CAST_call202<=1)    #Fix to double
objectiveFunction +=  + (581.033)*C5_main_corr_CAST_call202
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_call202_fixp + (-1)*C6_main_corr_CAST_call202<=1)    #Double to fix
objectiveFunction +=  + (796.087)*C6_main_corr_CAST_call202
solver.Add( + (1)*main_corr_float + (1)*main_corr_CAST_call202_double + (-1)*C7_main_corr_CAST_call202<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_corr_CAST_call202
solver.Add( + (1)*main_corr_double + (1)*main_corr_CAST_call202_float + (-1)*C8_main_corr_CAST_call202<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_corr_CAST_call202
solver.Add( + (1)*main_corr_CAST_call202_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(objectiveFunction)

# Model declaration end.