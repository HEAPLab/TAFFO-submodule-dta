


#Stuff for @array = common dso_local global [10 x double] zeroinitializer, align 16, !taffo.initweight !0, !taffo.info !1
array_fixbits = solver.IntVar(0, 21, 'array_fixbits')
array_fixp = solver.IntVar(0, 1, 'array_fixp')
array_float = solver.IntVar(0, 1, 'array_float')
array_double = solver.IntVar(0, 1, 'array_double')
array_enob = solver.IntVar(-10000, 10000, 'array_enob')
solver.Add( + (1)*array_enob + (-1)*array_fixbits + (10000)*array_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*array_enob + (10000)*array_float<=10021)    #Enob constraint for float
solver.Add( + (1)*array_enob + (10000)*array_double<=10050)    #Enob constraint for double
solver.Add( + (1)*array_double<=0)    #Disable double data type
objectiveFunction =  + (-100)*array_enob
solver.Add( + (1)*array_fixp + (1)*array_float + (1)*array_double==1)    #Exactly one selected type
solver.Add( + (1)*array_fixbits + (-10000)*array_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
array_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'array_enob_memphi_main_tmp')
solver.Add( + (1)*array_enob_memphi_main_tmp + (-1)*array_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
solver.Add( + (1)*main_main_tmp_enob_1==1)    #Enob: one selected constraint



#Stuff for double 1.000000e+00
ConstantValue__fixbits = solver.IntVar(0, 31, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add = fadd double %tmp, 1.000000e+00, !taffo.initweight !14, !taffo.info !1, !taffo.constinfo !15
array_CAST_add_fixbits = solver.IntVar(0, 21, 'array_CAST_add_fixbits')
array_CAST_add_fixp = solver.IntVar(0, 1, 'array_CAST_add_fixp')
array_CAST_add_float = solver.IntVar(0, 1, 'array_CAST_add_float')
array_CAST_add_double = solver.IntVar(0, 1, 'array_CAST_add_double')
solver.Add( + (1)*array_CAST_add_fixp + (1)*array_CAST_add_float + (1)*array_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*array_CAST_add_fixbits + (-10000)*array_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_array_CAST_add = solver.IntVar(0, 1, 'C1_array_CAST_add')
C2_array_CAST_add = solver.IntVar(0, 1, 'C2_array_CAST_add')
solver.Add( + (1)*array_fixbits + (-1)*array_CAST_add_fixbits + (-10000)*C1_array_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*array_fixbits + (1)*array_CAST_add_fixbits + (-10000)*C2_array_CAST_add<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_array_CAST_add
objectiveFunction +=  + (50)*C2_array_CAST_add
C3_array_CAST_add = solver.IntVar(0, 1, 'C3_array_CAST_add')
C4_array_CAST_add = solver.IntVar(0, 1, 'C4_array_CAST_add')
C5_array_CAST_add = solver.IntVar(0, 1, 'C5_array_CAST_add')
C6_array_CAST_add = solver.IntVar(0, 1, 'C6_array_CAST_add')
C7_array_CAST_add = solver.IntVar(0, 1, 'C7_array_CAST_add')
C8_array_CAST_add = solver.IntVar(0, 1, 'C8_array_CAST_add')
solver.Add( + (1)*array_fixp + (1)*array_CAST_add_float + (-1)*C3_array_CAST_add<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_array_CAST_add
solver.Add( + (1)*array_float + (1)*array_CAST_add_fixp + (-1)*C4_array_CAST_add<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_array_CAST_add
solver.Add( + (1)*array_fixp + (1)*array_CAST_add_double + (-1)*C5_array_CAST_add<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_array_CAST_add
solver.Add( + (1)*array_double + (1)*array_CAST_add_fixp + (-1)*C6_array_CAST_add<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_array_CAST_add
solver.Add( + (1)*array_float + (1)*array_CAST_add_double + (-1)*C7_array_CAST_add<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_array_CAST_add
solver.Add( + (1)*array_double + (1)*array_CAST_add_float + (-1)*C8_array_CAST_add<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_array_CAST_add



#Constraint for cast for   %add = fadd double %tmp, 1.000000e+00, !taffo.initweight !14, !taffo.info !1, !taffo.constinfo !15
ConstantValue__CAST_add_fixbits = solver.IntVar(0, 31, 'ConstantValue__CAST_add_fixbits')
ConstantValue__CAST_add_fixp = solver.IntVar(0, 1, 'ConstantValue__CAST_add_fixp')
ConstantValue__CAST_add_float = solver.IntVar(0, 1, 'ConstantValue__CAST_add_float')
ConstantValue__CAST_add_double = solver.IntVar(0, 1, 'ConstantValue__CAST_add_double')
solver.Add( + (1)*ConstantValue__CAST_add_fixp + (1)*ConstantValue__CAST_add_float + (1)*ConstantValue__CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__CAST_add_fixbits + (-10000)*ConstantValue__CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C1_ConstantValue__CAST_add')
C2_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C2_ConstantValue__CAST_add')
solver.Add( + (1)*ConstantValue__fixbits + (-1)*ConstantValue__CAST_add_fixbits + (-10000)*C1_ConstantValue__CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__fixbits + (1)*ConstantValue__CAST_add_fixbits + (-10000)*C2_ConstantValue__CAST_add<=0)    #Shift cost 2
objectiveFunction +=  + (50)*C1_ConstantValue__CAST_add
objectiveFunction +=  + (50)*C2_ConstantValue__CAST_add
C3_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C3_ConstantValue__CAST_add')
C4_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C4_ConstantValue__CAST_add')
C5_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C5_ConstantValue__CAST_add')
C6_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C6_ConstantValue__CAST_add')
C7_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C7_ConstantValue__CAST_add')
C8_ConstantValue__CAST_add = solver.IntVar(0, 1, 'C8_ConstantValue__CAST_add')
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__CAST_add_float + (-1)*C3_ConstantValue__CAST_add<=1)    #Fix to float
objectiveFunction +=  + (362.613)*C3_ConstantValue__CAST_add
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__CAST_add_fixp + (-1)*C4_ConstantValue__CAST_add<=1)    #Float to fix
objectiveFunction +=  + (123.623)*C4_ConstantValue__CAST_add
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__CAST_add_double + (-1)*C5_ConstantValue__CAST_add<=1)    #Fix to double
objectiveFunction +=  + (631.033)*C5_ConstantValue__CAST_add
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__CAST_add_fixp + (-1)*C6_ConstantValue__CAST_add<=1)    #Double to fix
objectiveFunction +=  + (846.087)*C6_ConstantValue__CAST_add
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__CAST_add_double + (-1)*C7_ConstantValue__CAST_add<=1)    #Float to double
objectiveFunction +=  + (224.348)*C7_ConstantValue__CAST_add
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__CAST_add_float + (-1)*C8_ConstantValue__CAST_add<=1)    #Double to float
objectiveFunction +=  + (265.217)*C8_ConstantValue__CAST_add



#Stuff for   %add = fadd double %tmp, 1.000000e+00, !taffo.initweight !14, !taffo.info !1, !taffo.constinfo !15
main_add_fixbits = solver.IntVar(0, 21, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
main_add_enob = solver.IntVar(-10000, 10000, 'main_add_enob')
solver.Add( + (1)*main_add_enob + (-1)*main_add_fixbits + (10000)*main_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add_enob + (10000)*main_add_float<=10021)    #Enob constraint for float
solver.Add( + (1)*main_add_enob + (10000)*main_add_double<=10050)    #Enob constraint for double
solver.Add( + (1)*main_add_double<=0)    #Disable double data type
objectiveFunction +=  + (-100)*main_add_enob
solver.Add( + (1)*main_add_fixp + (1)*main_add_float + (1)*main_add_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*array_CAST_add_fixp + (-1)*ConstantValue__CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*array_CAST_add_float + (-1)*ConstantValue__CAST_add_float==0)    #float equality
solver.Add( + (1)*array_CAST_add_double + (-1)*ConstantValue__CAST_add_double==0)    #double equality
solver.Add( + (1)*array_CAST_add_fixbits + (-1)*ConstantValue__CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*array_CAST_add_fixp + (-1)*main_add_fixp==0)    #fix equality
solver.Add( + (1)*array_CAST_add_float + (-1)*main_add_float==0)    #float equality
solver.Add( + (1)*array_CAST_add_double + (-1)*main_add_double==0)    #double equality
solver.Add( + (1)*array_CAST_add_fixbits + (-1)*main_add_fixbits==0)    #same fractional bit
objectiveFunction +=  + (127.246)*main_add_fixp
objectiveFunction +=  + (174.493)*main_add_float
objectiveFunction +=  + (664.928)*main_add_double
solver.Add( + (1)*main_add_enob + (-1)*array_enob_memphi_main_tmp<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*ConstantValue__enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add, double* %arrayidx2, align 8, !taffo.initweight !13, !taffo.info !1
main_add_CAST_store_fixbits = solver.IntVar(0, 21, 'main_add_CAST_store_fixbits')
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
solver.Add( + (1)*array_fixp + (-1)*main_add_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*array_float + (-1)*main_add_CAST_store_float==0)    #float equality
solver.Add( + (1)*array_double + (-1)*main_add_CAST_store_double==0)    #double equality
solver.Add( + (1)*array_fixbits + (-1)*main_add_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
array_enob_storeENOB = solver.IntVar(-10000, 10000, 'array_enob_storeENOB')
solver.Add( + (1)*array_enob_storeENOB + (-1)*array_fixbits + (10000)*array_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*array_enob_storeENOB + (10000)*array_float<=10021)    #Enob constraint for float
solver.Add( + (1)*array_enob_storeENOB + (10000)*array_double<=10050)    #Enob constraint for double
solver.Add( + (1)*array_enob_storeENOB + (-1)*main_add_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*array_enob_memphi_main_tmp + (-1)*array_enob_memphi_main_tmp + (-10000)*main_main_tmp_enob_1<=0)    #Enob: forcing MEM phi enob
solver.Minimize(objectiveFunction)

# Model declaration end.