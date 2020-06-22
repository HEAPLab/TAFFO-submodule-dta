


#Stuff for @mean = common dso_local global [10 x double] zeroinitializer, align 16, !taffo.initweight !0, !taffo.info !1
mean_fixbits = solver.IntVar(0, 16, 'mean_fixbits')
mean_fixp = solver.IntVar(0, 1, 'mean_fixp')
mean_float = solver.IntVar(0, 1, 'mean_float')
mean_double = solver.IntVar(0, 1, 'mean_double')
mean_enob = solver.IntVar(-10000, 10000, 'mean_enob')
solver.Add( + (1)*mean_enob + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_enob<=4)    #Enob constraint for error maximal
solver.Add( + (1)*mean_double<=0)    #Disable double data type
objectiveFunction =  + (-1)*mean_enob
solver.Add( + (1)*mean_fixp + (1)*mean_float + (1)*mean_double==1)    #Exactly one selected type
solver.Add( + (1)*mean_fixbits + (-10000)*mean_fixp<=0)    #If not fix, frac part to zero



#Stuff for @data = common dso_local global [10 x [10 x double]] zeroinitializer, align 16, !taffo.initweight !0, !taffo.info !4
data_fixbits = solver.IntVar(0, 29, 'data_fixbits')
data_fixp = solver.IntVar(0, 1, 'data_fixp')
data_float = solver.IntVar(0, 1, 'data_float')
data_double = solver.IntVar(0, 1, 'data_double')
data_enob = solver.IntVar(-10000, 10000, 'data_enob')
solver.Add( + (1)*data_enob + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_double<=0)    #Disable double data type
objectiveFunction +=  + (-1)*data_enob
solver.Add( + (1)*data_fixp + (1)*data_float + (1)*data_double==1)    #Exactly one selected type
solver.Add( + (1)*data_fixbits + (-10000)*data_fixp<=0)    #If not fix, frac part to zero



#Stuff for @float_n = common dso_local global double 0.000000e+00, align 8, !taffo.initweight !0, !taffo.info !6
float_n_fixbits = solver.IntVar(0, 20, 'float_n_fixbits')
float_n_fixp = solver.IntVar(0, 1, 'float_n_fixp')
float_n_float = solver.IntVar(0, 1, 'float_n_float')
float_n_double = solver.IntVar(0, 1, 'float_n_double')
float_n_enob = solver.IntVar(-10000, 10000, 'float_n_enob')
solver.Add( + (1)*float_n_enob + (-1)*float_n_fixbits + (10000)*float_n_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*float_n_enob + (10000)*float_n_float<=10149)    #Enob constraint for float
solver.Add( + (1)*float_n_enob + (10000)*float_n_double<=11074)    #Enob constraint for double
solver.Add( + (1)*float_n_double<=0)    #Disable double data type
objectiveFunction +=  + (-1)*float_n_enob
solver.Add( + (1)*float_n_fixp + (1)*float_n_float + (1)*float_n_double==1)    #Exactly one selected type
solver.Add( + (1)*float_n_fixbits + (-10000)*float_n_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__fixbits = solver.IntVar(0, 32, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx, align 8, !taffo.initweight !16, !taffo.info !1, !taffo.constinfo !17
ConstantValue__CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__CAST_store_fixbits')
ConstantValue__CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__CAST_store_fixp')
ConstantValue__CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__CAST_store_float')
ConstantValue__CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__CAST_store_double')
solver.Add( + (1)*ConstantValue__CAST_store_fixp + (1)*ConstantValue__CAST_store_float + (1)*ConstantValue__CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__CAST_store_fixbits + (-10000)*ConstantValue__CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__CAST_store')
C2_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__CAST_store')
solver.Add( + (1)*ConstantValue__fixbits + (-1)*ConstantValue__CAST_store_fixbits + (-10000)*C1_ConstantValue__CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__fixbits + (1)*ConstantValue__CAST_store_fixbits + (-10000)*C2_ConstantValue__CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__CAST_store
objectiveFunction +=  + (50)*C2_ConstantValue__CAST_store
C3_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__CAST_store')
C4_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__CAST_store')
C5_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__CAST_store')
C6_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__CAST_store')
C7_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__CAST_store')
C8_ConstantValue__CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__CAST_store')
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__CAST_store_float + (-1)*C3_ConstantValue__CAST_store<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_ConstantValue__CAST_store
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__CAST_store_fixp + (-1)*C4_ConstantValue__CAST_store<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_ConstantValue__CAST_store
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__CAST_store_double + (-1)*C5_ConstantValue__CAST_store<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_ConstantValue__CAST_store
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__CAST_store_fixp + (-1)*C6_ConstantValue__CAST_store<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_ConstantValue__CAST_store
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__CAST_store_double + (-1)*C7_ConstantValue__CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__CAST_store
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__CAST_store_float + (-1)*C8_ConstantValue__CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__CAST_store
solver.Add( + (1)*mean_fixp + (-1)*ConstantValue__CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*ConstantValue__CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*ConstantValue__CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*ConstantValue__CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob
data_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp')
solver.Add( + (1)*data_enob_memphi_main_tmp + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob
mean_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp1')
solver.Add( + (1)*mean_enob_memphi_main_tmp1 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
solver.Add( + (1)*main_main_tmp1_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add = fadd double %tmp1, %tmp, !taffo.initweight !20, !taffo.info !1
mean_CAST_add_fixbits = solver.IntVar(0, 16, 'mean_CAST_add_fixbits')
mean_CAST_add_fixp = solver.IntVar(0, 1, 'mean_CAST_add_fixp')
mean_CAST_add_float = solver.IntVar(0, 1, 'mean_CAST_add_float')
mean_CAST_add_double = solver.IntVar(0, 1, 'mean_CAST_add_double')
solver.Add( + (1)*mean_CAST_add_fixp + (1)*mean_CAST_add_float + (1)*mean_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_add_fixbits + (-10000)*mean_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_add = solver.IntVar(0, 1, 'C1_mean_CAST_add')
C2_mean_CAST_add = solver.IntVar(0, 1, 'C2_mean_CAST_add')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_add_fixbits + (-10000)*C1_mean_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_add_fixbits + (-10000)*C2_mean_CAST_add<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_mean_CAST_add
objectiveFunction +=  + (50)*C2_mean_CAST_add
C3_mean_CAST_add = solver.IntVar(0, 1, 'C3_mean_CAST_add')
C4_mean_CAST_add = solver.IntVar(0, 1, 'C4_mean_CAST_add')
C5_mean_CAST_add = solver.IntVar(0, 1, 'C5_mean_CAST_add')
C6_mean_CAST_add = solver.IntVar(0, 1, 'C6_mean_CAST_add')
C7_mean_CAST_add = solver.IntVar(0, 1, 'C7_mean_CAST_add')
C8_mean_CAST_add = solver.IntVar(0, 1, 'C8_mean_CAST_add')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_add_float + (-1)*C3_mean_CAST_add<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_mean_CAST_add
solver.Add( + (1)*mean_float + (1)*mean_CAST_add_fixp + (-1)*C4_mean_CAST_add<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_mean_CAST_add
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_add_double + (-1)*C5_mean_CAST_add<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_mean_CAST_add
solver.Add( + (1)*mean_double + (1)*mean_CAST_add_fixp + (-1)*C6_mean_CAST_add<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_mean_CAST_add
solver.Add( + (1)*mean_float + (1)*mean_CAST_add_double + (-1)*C7_mean_CAST_add<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_mean_CAST_add
solver.Add( + (1)*mean_double + (1)*mean_CAST_add_float + (-1)*C8_mean_CAST_add<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_mean_CAST_add



#Constraint for cast for   %add = fadd double %tmp1, %tmp, !taffo.initweight !20, !taffo.info !1
data_CAST_add_fixbits = solver.IntVar(0, 29, 'data_CAST_add_fixbits')
data_CAST_add_fixp = solver.IntVar(0, 1, 'data_CAST_add_fixp')
data_CAST_add_float = solver.IntVar(0, 1, 'data_CAST_add_float')
data_CAST_add_double = solver.IntVar(0, 1, 'data_CAST_add_double')
solver.Add( + (1)*data_CAST_add_fixp + (1)*data_CAST_add_float + (1)*data_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_add_fixbits + (-10000)*data_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_add = solver.IntVar(0, 1, 'C1_data_CAST_add')
C2_data_CAST_add = solver.IntVar(0, 1, 'C2_data_CAST_add')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_add_fixbits + (-10000)*C1_data_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_add_fixbits + (-10000)*C2_data_CAST_add<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_data_CAST_add
objectiveFunction +=  + (50)*C2_data_CAST_add
C3_data_CAST_add = solver.IntVar(0, 1, 'C3_data_CAST_add')
C4_data_CAST_add = solver.IntVar(0, 1, 'C4_data_CAST_add')
C5_data_CAST_add = solver.IntVar(0, 1, 'C5_data_CAST_add')
C6_data_CAST_add = solver.IntVar(0, 1, 'C6_data_CAST_add')
C7_data_CAST_add = solver.IntVar(0, 1, 'C7_data_CAST_add')
C8_data_CAST_add = solver.IntVar(0, 1, 'C8_data_CAST_add')
solver.Add( + (1)*data_fixp + (1)*data_CAST_add_float + (-1)*C3_data_CAST_add<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_data_CAST_add
solver.Add( + (1)*data_float + (1)*data_CAST_add_fixp + (-1)*C4_data_CAST_add<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_data_CAST_add
solver.Add( + (1)*data_fixp + (1)*data_CAST_add_double + (-1)*C5_data_CAST_add<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_data_CAST_add
solver.Add( + (1)*data_double + (1)*data_CAST_add_fixp + (-1)*C6_data_CAST_add<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_data_CAST_add
solver.Add( + (1)*data_float + (1)*data_CAST_add_double + (-1)*C7_data_CAST_add<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_data_CAST_add
solver.Add( + (1)*data_double + (1)*data_CAST_add_float + (-1)*C8_data_CAST_add<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_data_CAST_add



#Stuff for   %add = fadd double %tmp1, %tmp, !taffo.initweight !20, !taffo.info !1
main_add_fixbits = solver.IntVar(0, 16, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
main_add_enob = solver.IntVar(-10000, 10000, 'main_add_enob')
solver.Add( + (1)*main_add_enob + (-1)*main_add_fixbits + (10000)*main_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add_enob + (10000)*main_add_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add_enob + (10000)*main_add_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add_enob<=4)    #Enob constraint for error maximal
solver.Add( + (1)*main_add_double<=0)    #Disable double data type
objectiveFunction +=  + (-1)*main_add_enob
solver.Add( + (1)*main_add_fixp + (1)*main_add_float + (1)*main_add_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*mean_CAST_add_fixp + (-1)*data_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_add_float + (-1)*data_CAST_add_float==0)    #float equality
solver.Add( + (1)*mean_CAST_add_double + (-1)*data_CAST_add_double==0)    #double equality
solver.Add( + (1)*mean_CAST_add_fixbits + (-1)*data_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*mean_CAST_add_fixp + (-1)*main_add_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_add_float + (-1)*main_add_float==0)    #float equality
solver.Add( + (1)*mean_CAST_add_double + (-1)*main_add_double==0)    #double equality
solver.Add( + (1)*mean_CAST_add_fixbits + (-1)*main_add_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_add_fixp
objectiveFunction +=  + (174.493)*main_add_float
objectiveFunction +=  + (664.928)*main_add_double
solver.Add( + (1)*main_add_enob + (-1)*mean_enob_memphi_main_tmp1<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*data_enob_memphi_main_tmp<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add, double* %arrayidx9, align 8, !taffo.initweight !16, !taffo.info !1
main_add_CAST_store_fixbits = solver.IntVar(0, 16, 'main_add_CAST_store_fixbits')
main_add_CAST_store_fixp = solver.IntVar(0, 1, 'main_add_CAST_store_fixp')
main_add_CAST_store_float = solver.IntVar(0, 1, 'main_add_CAST_store_float')
main_add_CAST_store_double = solver.IntVar(0, 1, 'main_add_CAST_store_double')
solver.Add( + (1)*main_add_CAST_store_fixp + (1)*main_add_CAST_store_float + (1)*main_add_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add_CAST_store_fixbits + (-10000)*main_add_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add_CAST_store = solver.IntVar(0, 1, 'C1_main_add_CAST_store')
C2_main_add_CAST_store = solver.IntVar(0, 1, 'C2_main_add_CAST_store')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add_CAST_store_fixbits + (-10000)*C1_main_add_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add_fixbits + (1)*main_add_CAST_store_fixbits + (-10000)*C2_main_add_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_add_CAST_store
objectiveFunction +=  + (50)*C2_main_add_CAST_store
C3_main_add_CAST_store = solver.IntVar(0, 1, 'C3_main_add_CAST_store')
C4_main_add_CAST_store = solver.IntVar(0, 1, 'C4_main_add_CAST_store')
C5_main_add_CAST_store = solver.IntVar(0, 1, 'C5_main_add_CAST_store')
C6_main_add_CAST_store = solver.IntVar(0, 1, 'C6_main_add_CAST_store')
C7_main_add_CAST_store = solver.IntVar(0, 1, 'C7_main_add_CAST_store')
C8_main_add_CAST_store = solver.IntVar(0, 1, 'C8_main_add_CAST_store')
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_float + (-1)*C3_main_add_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_fixp + (-1)*C4_main_add_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_main_add_CAST_store
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_double + (-1)*C5_main_add_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_fixp + (-1)*C6_main_add_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_double + (-1)*C7_main_add_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_float + (-1)*C8_main_add_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_add_CAST_store
solver.Add( + (1)*mean_fixp + (-1)*main_add_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*main_add_CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*main_add_CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*main_add_CAST_store_fixbits==0)    #same fractional bit

#Restriction for new enob
mean_enob_storeENOB = solver.IntVar(-10000, 10000, 'mean_enob_storeENOB')
solver.Add( + (1)*mean_enob_storeENOB + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob_storeENOB + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob_storeENOB + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_enob_storeENOB + (-1)*main_add_enob<=0)    #Enob constraint ENOB propagation in load/store



#Constraint for cast for   %tmp1 = load double, double* %arrayidx9, align 8, !taffo.initweight !16, !taffo.info !1
main_add_CAST_tmp1_fixbits = solver.IntVar(0, 16, 'main_add_CAST_tmp1_fixbits')
main_add_CAST_tmp1_fixp = solver.IntVar(0, 1, 'main_add_CAST_tmp1_fixp')
main_add_CAST_tmp1_float = solver.IntVar(0, 1, 'main_add_CAST_tmp1_float')
main_add_CAST_tmp1_double = solver.IntVar(0, 1, 'main_add_CAST_tmp1_double')
solver.Add( + (1)*main_add_CAST_tmp1_fixp + (1)*main_add_CAST_tmp1_float + (1)*main_add_CAST_tmp1_double==1)    #exactly 1 type
solver.Add( + (1)*main_add_CAST_tmp1_fixbits + (-10000)*main_add_CAST_tmp1_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C1_main_add_CAST_tmp1')
C2_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C2_main_add_CAST_tmp1')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add_CAST_tmp1_fixbits + (-10000)*C1_main_add_CAST_tmp1<=0)    #Shift cost 1
solver.Add( + (-1)*main_add_fixbits + (1)*main_add_CAST_tmp1_fixbits + (-10000)*C2_main_add_CAST_tmp1<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_add_CAST_tmp1
objectiveFunction +=  + (50)*C2_main_add_CAST_tmp1
C3_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C3_main_add_CAST_tmp1')
C4_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C4_main_add_CAST_tmp1')
C5_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C5_main_add_CAST_tmp1')
C6_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C6_main_add_CAST_tmp1')
C7_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C7_main_add_CAST_tmp1')
C8_main_add_CAST_tmp1 = solver.IntVar(0, 1, 'C8_main_add_CAST_tmp1')
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_tmp1_float + (-1)*C3_main_add_CAST_tmp1<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_main_add_CAST_tmp1
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_tmp1_fixp + (-1)*C4_main_add_CAST_tmp1<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_main_add_CAST_tmp1
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_tmp1_double + (-1)*C5_main_add_CAST_tmp1<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_main_add_CAST_tmp1
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_tmp1_fixp + (-1)*C6_main_add_CAST_tmp1<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_main_add_CAST_tmp1
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_tmp1_double + (-1)*C7_main_add_CAST_tmp1<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_add_CAST_tmp1
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_tmp1_float + (-1)*C8_main_add_CAST_tmp1<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_add_CAST_tmp1
solver.Add( + (1)*mean_fixp + (-1)*main_add_CAST_tmp1_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*main_add_CAST_tmp1_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*main_add_CAST_tmp1_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*main_add_CAST_tmp1_fixbits==0)    #same fractional bit
solver.Add( + (1)*mean_enob_memphi_main_tmp1 + (-1)*mean_enob_storeENOB + (-10000)*main_main_tmp1_enob_1<=0)    #Enob: forcing phi enob

#Restriction for new enob
float_n_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'float_n_enob_memphi_main_tmp2')
solver.Add( + (1)*float_n_enob_memphi_main_tmp2 + (-1)*float_n_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob
mean_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp3')
solver.Add( + (1)*mean_enob_memphi_main_tmp3 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
solver.Add( + (1)*main_main_tmp3_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %tmp3 = load double, double* %arrayidx11, align 8, !taffo.initweight !16, !taffo.info !1
main_add_CAST_tmp3_fixbits = solver.IntVar(0, 16, 'main_add_CAST_tmp3_fixbits')
main_add_CAST_tmp3_fixp = solver.IntVar(0, 1, 'main_add_CAST_tmp3_fixp')
main_add_CAST_tmp3_float = solver.IntVar(0, 1, 'main_add_CAST_tmp3_float')
main_add_CAST_tmp3_double = solver.IntVar(0, 1, 'main_add_CAST_tmp3_double')
solver.Add( + (1)*main_add_CAST_tmp3_fixp + (1)*main_add_CAST_tmp3_float + (1)*main_add_CAST_tmp3_double==1)    #exactly 1 type
solver.Add( + (1)*main_add_CAST_tmp3_fixbits + (-10000)*main_add_CAST_tmp3_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C1_main_add_CAST_tmp3')
C2_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C2_main_add_CAST_tmp3')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add_CAST_tmp3_fixbits + (-10000)*C1_main_add_CAST_tmp3<=0)    #Shift cost 1
solver.Add( + (-1)*main_add_fixbits + (1)*main_add_CAST_tmp3_fixbits + (-10000)*C2_main_add_CAST_tmp3<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_add_CAST_tmp3
objectiveFunction +=  + (50)*C2_main_add_CAST_tmp3
C3_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C3_main_add_CAST_tmp3')
C4_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C4_main_add_CAST_tmp3')
C5_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C5_main_add_CAST_tmp3')
C6_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C6_main_add_CAST_tmp3')
C7_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C7_main_add_CAST_tmp3')
C8_main_add_CAST_tmp3 = solver.IntVar(0, 1, 'C8_main_add_CAST_tmp3')
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_tmp3_float + (-1)*C3_main_add_CAST_tmp3<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_main_add_CAST_tmp3
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_tmp3_fixp + (-1)*C4_main_add_CAST_tmp3<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_main_add_CAST_tmp3
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_tmp3_double + (-1)*C5_main_add_CAST_tmp3<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_main_add_CAST_tmp3
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_tmp3_fixp + (-1)*C6_main_add_CAST_tmp3<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_main_add_CAST_tmp3
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_tmp3_double + (-1)*C7_main_add_CAST_tmp3<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_add_CAST_tmp3
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_tmp3_float + (-1)*C8_main_add_CAST_tmp3<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_add_CAST_tmp3
solver.Add( + (1)*mean_fixp + (-1)*main_add_CAST_tmp3_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*main_add_CAST_tmp3_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*main_add_CAST_tmp3_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*main_add_CAST_tmp3_fixbits==0)    #same fractional bit
solver.Add( + (1)*mean_enob_memphi_main_tmp3 + (-1)*mean_enob_storeENOB + (-10000)*main_main_tmp3_enob_1<=0)    #Enob: forcing phi enob



#Constraint for cast for   %div = fdiv double %tmp3, %tmp2, !taffo.initweight !16, !taffo.info !6
mean_CAST_div_fixbits = solver.IntVar(0, 16, 'mean_CAST_div_fixbits')
mean_CAST_div_fixp = solver.IntVar(0, 1, 'mean_CAST_div_fixp')
mean_CAST_div_float = solver.IntVar(0, 1, 'mean_CAST_div_float')
mean_CAST_div_double = solver.IntVar(0, 1, 'mean_CAST_div_double')
solver.Add( + (1)*mean_CAST_div_fixp + (1)*mean_CAST_div_float + (1)*mean_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_div_fixbits + (-10000)*mean_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_div = solver.IntVar(0, 1, 'C1_mean_CAST_div')
C2_mean_CAST_div = solver.IntVar(0, 1, 'C2_mean_CAST_div')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_div_fixbits + (-10000)*C1_mean_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_div_fixbits + (-10000)*C2_mean_CAST_div<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_mean_CAST_div
objectiveFunction +=  + (50)*C2_mean_CAST_div
C3_mean_CAST_div = solver.IntVar(0, 1, 'C3_mean_CAST_div')
C4_mean_CAST_div = solver.IntVar(0, 1, 'C4_mean_CAST_div')
C5_mean_CAST_div = solver.IntVar(0, 1, 'C5_mean_CAST_div')
C6_mean_CAST_div = solver.IntVar(0, 1, 'C6_mean_CAST_div')
C7_mean_CAST_div = solver.IntVar(0, 1, 'C7_mean_CAST_div')
C8_mean_CAST_div = solver.IntVar(0, 1, 'C8_mean_CAST_div')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_div_float + (-1)*C3_mean_CAST_div<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_mean_CAST_div
solver.Add( + (1)*mean_float + (1)*mean_CAST_div_fixp + (-1)*C4_mean_CAST_div<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_mean_CAST_div
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_div_double + (-1)*C5_mean_CAST_div<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_mean_CAST_div
solver.Add( + (1)*mean_double + (1)*mean_CAST_div_fixp + (-1)*C6_mean_CAST_div<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_mean_CAST_div
solver.Add( + (1)*mean_float + (1)*mean_CAST_div_double + (-1)*C7_mean_CAST_div<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_mean_CAST_div
solver.Add( + (1)*mean_double + (1)*mean_CAST_div_float + (-1)*C8_mean_CAST_div<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_mean_CAST_div



#Constraint for cast for   %div = fdiv double %tmp3, %tmp2, !taffo.initweight !16, !taffo.info !6
float_n_CAST_div_fixbits = solver.IntVar(0, 20, 'float_n_CAST_div_fixbits')
float_n_CAST_div_fixp = solver.IntVar(0, 1, 'float_n_CAST_div_fixp')
float_n_CAST_div_float = solver.IntVar(0, 1, 'float_n_CAST_div_float')
float_n_CAST_div_double = solver.IntVar(0, 1, 'float_n_CAST_div_double')
solver.Add( + (1)*float_n_CAST_div_fixp + (1)*float_n_CAST_div_float + (1)*float_n_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*float_n_CAST_div_fixbits + (-10000)*float_n_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_float_n_CAST_div = solver.IntVar(0, 1, 'C1_float_n_CAST_div')
C2_float_n_CAST_div = solver.IntVar(0, 1, 'C2_float_n_CAST_div')
solver.Add( + (1)*float_n_fixbits + (-1)*float_n_CAST_div_fixbits + (-10000)*C1_float_n_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*float_n_fixbits + (1)*float_n_CAST_div_fixbits + (-10000)*C2_float_n_CAST_div<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_float_n_CAST_div
objectiveFunction +=  + (50)*C2_float_n_CAST_div
C3_float_n_CAST_div = solver.IntVar(0, 1, 'C3_float_n_CAST_div')
C4_float_n_CAST_div = solver.IntVar(0, 1, 'C4_float_n_CAST_div')
C5_float_n_CAST_div = solver.IntVar(0, 1, 'C5_float_n_CAST_div')
C6_float_n_CAST_div = solver.IntVar(0, 1, 'C6_float_n_CAST_div')
C7_float_n_CAST_div = solver.IntVar(0, 1, 'C7_float_n_CAST_div')
C8_float_n_CAST_div = solver.IntVar(0, 1, 'C8_float_n_CAST_div')
solver.Add( + (1)*float_n_fixp + (1)*float_n_CAST_div_float + (-1)*C3_float_n_CAST_div<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_float_n_CAST_div
solver.Add( + (1)*float_n_float + (1)*float_n_CAST_div_fixp + (-1)*C4_float_n_CAST_div<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_float_n_CAST_div
solver.Add( + (1)*float_n_fixp + (1)*float_n_CAST_div_double + (-1)*C5_float_n_CAST_div<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_float_n_CAST_div
solver.Add( + (1)*float_n_double + (1)*float_n_CAST_div_fixp + (-1)*C6_float_n_CAST_div<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_float_n_CAST_div
solver.Add( + (1)*float_n_float + (1)*float_n_CAST_div_double + (-1)*C7_float_n_CAST_div<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_float_n_CAST_div
solver.Add( + (1)*float_n_double + (1)*float_n_CAST_div_float + (-1)*C8_float_n_CAST_div<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_float_n_CAST_div



#Stuff for   %div = fdiv double %tmp3, %tmp2, !taffo.initweight !16, !taffo.info !6
main_div_fixbits = solver.IntVar(0, 20, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_double<=0)    #Disable double data type
objectiveFunction +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*mean_CAST_div_fixp + (-1)*float_n_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_div_float + (-1)*float_n_CAST_div_float==0)    #float equality
solver.Add( + (1)*mean_CAST_div_double + (-1)*float_n_CAST_div_double==0)    #double equality
solver.Add( + (1)*mean_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*mean_CAST_div_double + (-1)*main_div_double==0)    #double equality
objectiveFunction +=  + (161.159)*main_div_fixp
objectiveFunction +=  + (625.227)*main_div_float
objectiveFunction +=  + (768.154)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*float_n_enob_memphi_main_tmp2 + (-10000)*main_main_div_enob_1<=1048)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*mean_enob_memphi_main_tmp3 + (-10000)*main_main_div_enob_2<=1048)    #Enob: propagation in division 2



#Constraint for cast for   store double %div, double* %arrayidx11, align 8, !taffo.initweight !16, !taffo.info !1
main_div_CAST_store_fixbits = solver.IntVar(0, 20, 'main_div_CAST_store_fixbits')
main_div_CAST_store_fixp = solver.IntVar(0, 1, 'main_div_CAST_store_fixp')
main_div_CAST_store_float = solver.IntVar(0, 1, 'main_div_CAST_store_float')
main_div_CAST_store_double = solver.IntVar(0, 1, 'main_div_CAST_store_double')
solver.Add( + (1)*main_div_CAST_store_fixp + (1)*main_div_CAST_store_float + (1)*main_div_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div_CAST_store_fixbits + (-10000)*main_div_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div_CAST_store = solver.IntVar(0, 1, 'C1_main_div_CAST_store')
C2_main_div_CAST_store = solver.IntVar(0, 1, 'C2_main_div_CAST_store')
solver.Add( + (1)*main_div_fixbits + (-1)*main_div_CAST_store_fixbits + (-10000)*C1_main_div_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div_fixbits + (1)*main_div_CAST_store_fixbits + (-10000)*C2_main_div_CAST_store<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_main_div_CAST_store
objectiveFunction +=  + (50)*C2_main_div_CAST_store
C3_main_div_CAST_store = solver.IntVar(0, 1, 'C3_main_div_CAST_store')
C4_main_div_CAST_store = solver.IntVar(0, 1, 'C4_main_div_CAST_store')
C5_main_div_CAST_store = solver.IntVar(0, 1, 'C5_main_div_CAST_store')
C6_main_div_CAST_store = solver.IntVar(0, 1, 'C6_main_div_CAST_store')
C7_main_div_CAST_store = solver.IntVar(0, 1, 'C7_main_div_CAST_store')
C8_main_div_CAST_store = solver.IntVar(0, 1, 'C8_main_div_CAST_store')
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_float + (-1)*C3_main_div_CAST_store<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_fixp + (-1)*C4_main_div_CAST_store<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_main_div_CAST_store
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_double + (-1)*C5_main_div_CAST_store<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_fixp + (-1)*C6_main_div_CAST_store<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_double + (-1)*C7_main_div_CAST_store<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_float + (-1)*C8_main_div_CAST_store<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_main_div_CAST_store
solver.Add( + (1)*mean_fixp + (-1)*main_div_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*main_div_CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*main_div_CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*main_div_CAST_store_fixbits==0)    #same fractional bit

#Restriction for new enob
mean_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'mean_enob_storeENOB_storeENOB')
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (-1)*main_div_enob<=0)    #Enob constraint ENOB propagation in load/store
solver.Minimize(objectiveFunction)

# Model declaration end.