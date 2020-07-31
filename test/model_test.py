


#Stuff for   %path = alloca [60 x [60 x double]], align 16, !taffo.info !13, !taffo.initweight !16
main_path_fixbits = solver.IntVar(0, 7, 'main_path_fixbits')
main_path_fixp = solver.IntVar(0, 1, 'main_path_fixp')
main_path_float = solver.IntVar(0, 1, 'main_path_float')
main_path_double = solver.IntVar(0, 1, 'main_path_double')
main_path_enob = solver.IntVar(-10000, 10000, 'main_path_enob')
solver.Add( + (1)*main_path_enob + (-1)*main_path_fixbits + (10000)*main_path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_path_enob + (10000)*main_path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_path_enob + (10000)*main_path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_path_fixbits + (-10000)*main_path_fixp>=-9994)    #Limit the lower number of frac bits7
solver.Add( + (1)*main_path_enob<=333)    #Enob constraint for error maximal
enobCostObj =  + (-1)*main_path_enob
solver.Add( + (1)*main_path_fixp + (1)*main_path_float + (1)*main_path_double==1)    #Exactly one selected type
solver.Add( + (1)*main_path_fixbits + (-10000)*main_path_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %add to double, !taffo.info !34, !taffo.initweight !37
main_conv_fixbits = solver.IntVar(0, 27, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   store double %conv, double* %arrayidx8, align 8, !taffo.info !40, !taffo.initweight !26
main_conv_CAST_store_fixbits = solver.IntVar(0, 27, 'main_conv_CAST_store_fixbits')
main_conv_CAST_store_fixp = solver.IntVar(0, 1, 'main_conv_CAST_store_fixp')
main_conv_CAST_store_float = solver.IntVar(0, 1, 'main_conv_CAST_store_float')
main_conv_CAST_store_double = solver.IntVar(0, 1, 'main_conv_CAST_store_double')
solver.Add( + (1)*main_conv_CAST_store_fixp + (1)*main_conv_CAST_store_float + (1)*main_conv_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv_CAST_store_fixbits + (-10000)*main_conv_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv_CAST_store = solver.IntVar(0, 1, 'C1_main_conv_CAST_store')
C2_main_conv_CAST_store = solver.IntVar(0, 1, 'C2_main_conv_CAST_store')
solver.Add( + (1)*main_conv_fixbits + (-1)*main_conv_CAST_store_fixbits + (-10000)*C1_main_conv_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv_fixbits + (1)*main_conv_CAST_store_fixbits + (-10000)*C2_main_conv_CAST_store<=0)    #Shift cost 2
castCostObj =  + (1)*C1_main_conv_CAST_store
castCostObj +=  + (1)*C2_main_conv_CAST_store
C3_main_conv_CAST_store = solver.IntVar(0, 1, 'C3_main_conv_CAST_store')
C4_main_conv_CAST_store = solver.IntVar(0, 1, 'C4_main_conv_CAST_store')
C5_main_conv_CAST_store = solver.IntVar(0, 1, 'C5_main_conv_CAST_store')
C6_main_conv_CAST_store = solver.IntVar(0, 1, 'C6_main_conv_CAST_store')
C7_main_conv_CAST_store = solver.IntVar(0, 1, 'C7_main_conv_CAST_store')
C8_main_conv_CAST_store = solver.IntVar(0, 1, 'C8_main_conv_CAST_store')
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_store_float + (-1)*C3_main_conv_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv_CAST_store
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_store_fixp + (-1)*C4_main_conv_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv_CAST_store
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_store_double + (-1)*C5_main_conv_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv_CAST_store
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_store_fixp + (-1)*C6_main_conv_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv_CAST_store
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_store_double + (-1)*C7_main_conv_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv_CAST_store
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_store_float + (-1)*C8_main_conv_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv_CAST_store
solver.Add( + (1)*main_path_fixp + (-1)*main_conv_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_path_float + (-1)*main_conv_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_path_double + (-1)*main_conv_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_path_fixbits + (-1)*main_conv_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_path_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_path_enob_storeENOB')
solver.Add( + (1)*main_path_enob_storeENOB + (-1)*main_path_fixbits + (10000)*main_path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_path_enob_storeENOB + (10000)*main_path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_path_enob_storeENOB + (10000)*main_path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_path_enob_storeENOB + (-1)*main_conv_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for double 9.990000e+02
ConstantValue__fixbits = solver.IntVar(0, 22, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10014)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10043)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 9.990000e+02
ConstantValue__0_fixbits = solver.IntVar(0, 22, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10014)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10043)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 9.990000e+02, double* %arrayidx25, align 8, !taffo.info !40, !taffo.initweight !26, !taffo.constinfo !46
ConstantValue__0_CAST_store_fixbits = solver.IntVar(0, 22, 'ConstantValue__0_CAST_store_fixbits')
ConstantValue__0_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_fixp')
ConstantValue__0_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_float')
ConstantValue__0_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_double')
solver.Add( + (1)*ConstantValue__0_CAST_store_fixp + (1)*ConstantValue__0_CAST_store_float + (1)*ConstantValue__0_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__0_CAST_store_fixbits + (-10000)*ConstantValue__0_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__0_CAST_store')
C2_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__0_CAST_store')
solver.Add( + (1)*ConstantValue__0_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits + (-10000)*C1_ConstantValue__0_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__0_fixbits + (1)*ConstantValue__0_CAST_store_fixbits + (-10000)*C2_ConstantValue__0_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__0_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__0_CAST_store
C3_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__0_CAST_store')
C4_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__0_CAST_store')
C5_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__0_CAST_store')
C6_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__0_CAST_store')
C7_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__0_CAST_store')
C8_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__0_CAST_store')
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_CAST_store_float + (-1)*C3_ConstantValue__0_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C4_ConstantValue__0_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_CAST_store_double + (-1)*C5_ConstantValue__0_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C6_ConstantValue__0_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_double + (-1)*C7_ConstantValue__0_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_float + (-1)*C8_ConstantValue__0_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__0_CAST_store
solver.Add( + (1)*main_path_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_path_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_path_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_path_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_path_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'main_path_enob_memphi_main_tmp')
solver.Add( + (1)*main_path_enob_memphi_main_tmp + (-1)*main_path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_2 = solver.IntVar(0, 1, 'main_main_tmp_enob_2')
main_main_tmp_enob_3 = solver.IntVar(0, 1, 'main_main_tmp_enob_3')
main_main_tmp_enob_4 = solver.IntVar(0, 1, 'main_main_tmp_enob_4')
solver.Add( + (1)*main_main_tmp_enob_2 + (1)*main_main_tmp_enob_3 + (1)*main_main_tmp_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp + (-1)*main_path_enob_storeENOB + (10000)*main_main_tmp_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_path_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'main_path_enob_memphi_main_tmp1')
solver.Add( + (1)*main_path_enob_memphi_main_tmp1 + (-1)*main_path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
main_main_tmp1_enob_3 = solver.IntVar(0, 1, 'main_main_tmp1_enob_3')
main_main_tmp1_enob_4 = solver.IntVar(0, 1, 'main_main_tmp1_enob_4')
solver.Add( + (1)*main_main_tmp1_enob_2 + (1)*main_main_tmp1_enob_3 + (1)*main_main_tmp1_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp1 + (-1)*main_path_enob_storeENOB + (10000)*main_main_tmp1_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_path_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_path_enob_memphi_main_tmp2')
solver.Add( + (1)*main_path_enob_memphi_main_tmp2 + (-1)*main_path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
main_main_tmp2_enob_3 = solver.IntVar(0, 1, 'main_main_tmp2_enob_3')
main_main_tmp2_enob_4 = solver.IntVar(0, 1, 'main_main_tmp2_enob_4')
solver.Add( + (1)*main_main_tmp2_enob_2 + (1)*main_main_tmp2_enob_3 + (1)*main_main_tmp2_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp2 + (-1)*main_path_enob_storeENOB + (10000)*main_main_tmp2_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_path_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'main_path_enob_memphi_main_tmp3')
solver.Add( + (1)*main_path_enob_memphi_main_tmp3 + (-1)*main_path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
solver.Add( + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3 + (1)*main_main_tmp3_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp3 + (-1)*main_path_enob_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_path_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'main_path_enob_memphi_main_tmp4')
solver.Add( + (1)*main_path_enob_memphi_main_tmp4 + (-1)*main_path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
main_main_tmp4_enob_4 = solver.IntVar(0, 1, 'main_main_tmp4_enob_4')
solver.Add( + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3 + (1)*main_main_tmp4_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp4 + (-1)*main_path_enob_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add63 = fadd double %tmp3, %tmp4, !taffo.info !57, !taffo.initweight !36
main_path_CAST_add63_fixbits = solver.IntVar(0, 7, 'main_path_CAST_add63_fixbits')
main_path_CAST_add63_fixp = solver.IntVar(0, 1, 'main_path_CAST_add63_fixp')
main_path_CAST_add63_float = solver.IntVar(0, 1, 'main_path_CAST_add63_float')
main_path_CAST_add63_double = solver.IntVar(0, 1, 'main_path_CAST_add63_double')
solver.Add( + (1)*main_path_CAST_add63_fixp + (1)*main_path_CAST_add63_float + (1)*main_path_CAST_add63_double==1)    #exactly 1 type
solver.Add( + (1)*main_path_CAST_add63_fixbits + (-10000)*main_path_CAST_add63_fixp<=0)    #If no fix, fix frac part = 0
C1_main_path_CAST_add63 = solver.IntVar(0, 1, 'C1_main_path_CAST_add63')
C2_main_path_CAST_add63 = solver.IntVar(0, 1, 'C2_main_path_CAST_add63')
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_add63_fixbits + (-10000)*C1_main_path_CAST_add63<=0)    #Shift cost 1
solver.Add( + (-1)*main_path_fixbits + (1)*main_path_CAST_add63_fixbits + (-10000)*C2_main_path_CAST_add63<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_path_CAST_add63
castCostObj +=  + (1)*C2_main_path_CAST_add63
C3_main_path_CAST_add63 = solver.IntVar(0, 1, 'C3_main_path_CAST_add63')
C4_main_path_CAST_add63 = solver.IntVar(0, 1, 'C4_main_path_CAST_add63')
C5_main_path_CAST_add63 = solver.IntVar(0, 1, 'C5_main_path_CAST_add63')
C6_main_path_CAST_add63 = solver.IntVar(0, 1, 'C6_main_path_CAST_add63')
C7_main_path_CAST_add63 = solver.IntVar(0, 1, 'C7_main_path_CAST_add63')
C8_main_path_CAST_add63 = solver.IntVar(0, 1, 'C8_main_path_CAST_add63')
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add63_float + (-1)*C3_main_path_CAST_add63<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_path_CAST_add63
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add63_fixp + (-1)*C4_main_path_CAST_add63<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_path_CAST_add63
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add63_double + (-1)*C5_main_path_CAST_add63<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_path_CAST_add63
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add63_fixp + (-1)*C6_main_path_CAST_add63<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_path_CAST_add63
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add63_double + (-1)*C7_main_path_CAST_add63<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_path_CAST_add63
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add63_float + (-1)*C8_main_path_CAST_add63<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_path_CAST_add63



#Constraint for cast for   %add63 = fadd double %tmp3, %tmp4, !taffo.info !57, !taffo.initweight !36
main_path_CAST_add63_0_fixbits = solver.IntVar(0, 7, 'main_path_CAST_add63_0_fixbits')
main_path_CAST_add63_0_fixp = solver.IntVar(0, 1, 'main_path_CAST_add63_0_fixp')
main_path_CAST_add63_0_float = solver.IntVar(0, 1, 'main_path_CAST_add63_0_float')
main_path_CAST_add63_0_double = solver.IntVar(0, 1, 'main_path_CAST_add63_0_double')
solver.Add( + (1)*main_path_CAST_add63_0_fixp + (1)*main_path_CAST_add63_0_float + (1)*main_path_CAST_add63_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_path_CAST_add63_0_fixbits + (-10000)*main_path_CAST_add63_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C1_main_path_CAST_add63_0')
C2_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C2_main_path_CAST_add63_0')
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_add63_0_fixbits + (-10000)*C1_main_path_CAST_add63_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_path_fixbits + (1)*main_path_CAST_add63_0_fixbits + (-10000)*C2_main_path_CAST_add63_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_path_CAST_add63_0
castCostObj +=  + (1)*C2_main_path_CAST_add63_0
C3_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C3_main_path_CAST_add63_0')
C4_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C4_main_path_CAST_add63_0')
C5_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C5_main_path_CAST_add63_0')
C6_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C6_main_path_CAST_add63_0')
C7_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C7_main_path_CAST_add63_0')
C8_main_path_CAST_add63_0 = solver.IntVar(0, 1, 'C8_main_path_CAST_add63_0')
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add63_0_float + (-1)*C3_main_path_CAST_add63_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_path_CAST_add63_0
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add63_0_fixp + (-1)*C4_main_path_CAST_add63_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_path_CAST_add63_0
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add63_0_double + (-1)*C5_main_path_CAST_add63_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_path_CAST_add63_0
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add63_0_fixp + (-1)*C6_main_path_CAST_add63_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_path_CAST_add63_0
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add63_0_double + (-1)*C7_main_path_CAST_add63_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_path_CAST_add63_0
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add63_0_float + (-1)*C8_main_path_CAST_add63_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_path_CAST_add63_0



#Stuff for   %add63 = fadd double %tmp3, %tmp4, !taffo.info !57, !taffo.initweight !36
main_add63_fixbits = solver.IntVar(0, 6, 'main_add63_fixbits')
main_add63_fixp = solver.IntVar(0, 1, 'main_add63_fixp')
main_add63_float = solver.IntVar(0, 1, 'main_add63_float')
main_add63_double = solver.IntVar(0, 1, 'main_add63_double')
main_add63_enob = solver.IntVar(-10000, 10000, 'main_add63_enob')
solver.Add( + (1)*main_add63_enob + (-1)*main_add63_fixbits + (10000)*main_add63_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add63_enob + (10000)*main_add63_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add63_enob + (10000)*main_add63_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add63_fixbits + (-10000)*main_add63_fixp>=-9995)    #Limit the lower number of frac bits6
solver.Add( + (1)*main_add63_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add63_enob
solver.Add( + (1)*main_add63_fixp + (1)*main_add63_float + (1)*main_add63_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add63_fixbits + (-10000)*main_add63_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_path_CAST_add63_fixp + (-1)*main_path_CAST_add63_0_fixp==0)    #fix equality
solver.Add( + (1)*main_path_CAST_add63_float + (-1)*main_path_CAST_add63_0_float==0)    #float equality
solver.Add( + (1)*main_path_CAST_add63_double + (-1)*main_path_CAST_add63_0_double==0)    #double equality
solver.Add( + (1)*main_path_CAST_add63_fixbits + (-1)*main_path_CAST_add63_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_path_CAST_add63_fixp + (-1)*main_add63_fixp==0)    #fix equality
solver.Add( + (1)*main_path_CAST_add63_float + (-1)*main_add63_float==0)    #float equality
solver.Add( + (1)*main_path_CAST_add63_double + (-1)*main_add63_double==0)    #double equality
solver.Add( + (1)*main_path_CAST_add63_fixbits + (-1)*main_add63_fixbits==0)    #same fractional bit
mathCostObj =  + (1.24179)*main_add63_fixp
mathCostObj +=  + (2.33125)*main_add63_float
mathCostObj +=  + (2.72422)*main_add63_double
solver.Add( + (1)*main_add63_enob + (-1)*main_path_enob_memphi_main_tmp3<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add63_enob + (-1)*main_path_enob_memphi_main_tmp4<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %cmp64 = fcmp olt double %tmp2, %add63, !taffo.info !59, !taffo.initweight !36
main_path_CAST_cmp64_fixbits = solver.IntVar(0, 7, 'main_path_CAST_cmp64_fixbits')
main_path_CAST_cmp64_fixp = solver.IntVar(0, 1, 'main_path_CAST_cmp64_fixp')
main_path_CAST_cmp64_float = solver.IntVar(0, 1, 'main_path_CAST_cmp64_float')
main_path_CAST_cmp64_double = solver.IntVar(0, 1, 'main_path_CAST_cmp64_double')
solver.Add( + (1)*main_path_CAST_cmp64_fixp + (1)*main_path_CAST_cmp64_float + (1)*main_path_CAST_cmp64_double==1)    #exactly 1 type
solver.Add( + (1)*main_path_CAST_cmp64_fixbits + (-10000)*main_path_CAST_cmp64_fixp<=0)    #If no fix, fix frac part = 0
C1_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C1_main_path_CAST_cmp64')
C2_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C2_main_path_CAST_cmp64')
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_cmp64_fixbits + (-10000)*C1_main_path_CAST_cmp64<=0)    #Shift cost 1
solver.Add( + (-1)*main_path_fixbits + (1)*main_path_CAST_cmp64_fixbits + (-10000)*C2_main_path_CAST_cmp64<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_path_CAST_cmp64
castCostObj +=  + (1)*C2_main_path_CAST_cmp64
C3_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C3_main_path_CAST_cmp64')
C4_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C4_main_path_CAST_cmp64')
C5_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C5_main_path_CAST_cmp64')
C6_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C6_main_path_CAST_cmp64')
C7_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C7_main_path_CAST_cmp64')
C8_main_path_CAST_cmp64 = solver.IntVar(0, 1, 'C8_main_path_CAST_cmp64')
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_cmp64_float + (-1)*C3_main_path_CAST_cmp64<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_path_CAST_cmp64
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_cmp64_fixp + (-1)*C4_main_path_CAST_cmp64<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_path_CAST_cmp64
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_cmp64_double + (-1)*C5_main_path_CAST_cmp64<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_path_CAST_cmp64
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_cmp64_fixp + (-1)*C6_main_path_CAST_cmp64<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_path_CAST_cmp64
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_cmp64_double + (-1)*C7_main_path_CAST_cmp64<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_path_CAST_cmp64
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_cmp64_float + (-1)*C8_main_path_CAST_cmp64<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_path_CAST_cmp64



#Constraint for cast for   %cmp64 = fcmp olt double %tmp2, %add63, !taffo.info !59, !taffo.initweight !36
main_add63_CAST_cmp64_fixbits = solver.IntVar(0, 6, 'main_add63_CAST_cmp64_fixbits')
main_add63_CAST_cmp64_fixp = solver.IntVar(0, 1, 'main_add63_CAST_cmp64_fixp')
main_add63_CAST_cmp64_float = solver.IntVar(0, 1, 'main_add63_CAST_cmp64_float')
main_add63_CAST_cmp64_double = solver.IntVar(0, 1, 'main_add63_CAST_cmp64_double')
solver.Add( + (1)*main_add63_CAST_cmp64_fixp + (1)*main_add63_CAST_cmp64_float + (1)*main_add63_CAST_cmp64_double==1)    #exactly 1 type
solver.Add( + (1)*main_add63_CAST_cmp64_fixbits + (-10000)*main_add63_CAST_cmp64_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C1_main_add63_CAST_cmp64')
C2_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C2_main_add63_CAST_cmp64')
solver.Add( + (1)*main_add63_fixbits + (-1)*main_add63_CAST_cmp64_fixbits + (-10000)*C1_main_add63_CAST_cmp64<=0)    #Shift cost 1
solver.Add( + (-1)*main_add63_fixbits + (1)*main_add63_CAST_cmp64_fixbits + (-10000)*C2_main_add63_CAST_cmp64<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add63_CAST_cmp64
castCostObj +=  + (1)*C2_main_add63_CAST_cmp64
C3_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C3_main_add63_CAST_cmp64')
C4_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C4_main_add63_CAST_cmp64')
C5_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C5_main_add63_CAST_cmp64')
C6_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C6_main_add63_CAST_cmp64')
C7_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C7_main_add63_CAST_cmp64')
C8_main_add63_CAST_cmp64 = solver.IntVar(0, 1, 'C8_main_add63_CAST_cmp64')
solver.Add( + (1)*main_add63_fixp + (1)*main_add63_CAST_cmp64_float + (-1)*C3_main_add63_CAST_cmp64<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add63_CAST_cmp64
solver.Add( + (1)*main_add63_float + (1)*main_add63_CAST_cmp64_fixp + (-1)*C4_main_add63_CAST_cmp64<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add63_CAST_cmp64
solver.Add( + (1)*main_add63_fixp + (1)*main_add63_CAST_cmp64_double + (-1)*C5_main_add63_CAST_cmp64<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add63_CAST_cmp64
solver.Add( + (1)*main_add63_double + (1)*main_add63_CAST_cmp64_fixp + (-1)*C6_main_add63_CAST_cmp64<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add63_CAST_cmp64
solver.Add( + (1)*main_add63_float + (1)*main_add63_CAST_cmp64_double + (-1)*C7_main_add63_CAST_cmp64<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add63_CAST_cmp64
solver.Add( + (1)*main_add63_double + (1)*main_add63_CAST_cmp64_float + (-1)*C8_main_add63_CAST_cmp64<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add63_CAST_cmp64
solver.Add( + (1)*main_path_CAST_cmp64_fixp + (-1)*main_add63_CAST_cmp64_fixp==0)    #fix equality
solver.Add( + (1)*main_path_CAST_cmp64_float + (-1)*main_add63_CAST_cmp64_float==0)    #float equality
solver.Add( + (1)*main_path_CAST_cmp64_double + (-1)*main_add63_CAST_cmp64_double==0)    #double equality
solver.Add( + (1)*main_path_CAST_cmp64_fixbits + (-1)*main_add63_CAST_cmp64_fixbits==0)    #same fractional bit

#Restriction for new enob [LOAD]
main_path_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'main_path_enob_memphi_main_tmp5')
solver.Add( + (1)*main_path_enob_memphi_main_tmp5 + (-1)*main_path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
main_main_tmp5_enob_4 = solver.IntVar(0, 1, 'main_main_tmp5_enob_4')
solver.Add( + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3 + (1)*main_main_tmp5_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp5 + (-1)*main_path_enob_storeENOB + (10000)*main_main_tmp5_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp5, double* %arrayidx74, align 8, !taffo.info !40, !taffo.initweight !26
main_path_CAST_store_fixbits = solver.IntVar(0, 7, 'main_path_CAST_store_fixbits')
main_path_CAST_store_fixp = solver.IntVar(0, 1, 'main_path_CAST_store_fixp')
main_path_CAST_store_float = solver.IntVar(0, 1, 'main_path_CAST_store_float')
main_path_CAST_store_double = solver.IntVar(0, 1, 'main_path_CAST_store_double')
solver.Add( + (1)*main_path_CAST_store_fixp + (1)*main_path_CAST_store_float + (1)*main_path_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_path_CAST_store_fixbits + (-10000)*main_path_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_path_CAST_store = solver.IntVar(0, 1, 'C1_main_path_CAST_store')
C2_main_path_CAST_store = solver.IntVar(0, 1, 'C2_main_path_CAST_store')
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_store_fixbits + (-10000)*C1_main_path_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_path_fixbits + (1)*main_path_CAST_store_fixbits + (-10000)*C2_main_path_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_path_CAST_store
castCostObj +=  + (1)*C2_main_path_CAST_store
C3_main_path_CAST_store = solver.IntVar(0, 1, 'C3_main_path_CAST_store')
C4_main_path_CAST_store = solver.IntVar(0, 1, 'C4_main_path_CAST_store')
C5_main_path_CAST_store = solver.IntVar(0, 1, 'C5_main_path_CAST_store')
C6_main_path_CAST_store = solver.IntVar(0, 1, 'C6_main_path_CAST_store')
C7_main_path_CAST_store = solver.IntVar(0, 1, 'C7_main_path_CAST_store')
C8_main_path_CAST_store = solver.IntVar(0, 1, 'C8_main_path_CAST_store')
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_store_float + (-1)*C3_main_path_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_path_CAST_store
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_store_fixp + (-1)*C4_main_path_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_path_CAST_store
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_store_double + (-1)*C5_main_path_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_path_CAST_store
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_store_fixp + (-1)*C6_main_path_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_path_CAST_store
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_store_double + (-1)*C7_main_path_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_path_CAST_store
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_store_float + (-1)*C8_main_path_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_path_CAST_store
solver.Add( + (1)*main_path_fixp + (-1)*main_path_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_path_float + (-1)*main_path_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_path_double + (-1)*main_path_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_path_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_path_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB + (-1)*main_path_fixbits + (10000)*main_path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB + (10000)*main_path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB + (10000)*main_path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB + (-1)*main_path_enob_memphi_main_tmp5<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp + (-1)*main_path_enob_storeENOB_storeENOB + (10000)*main_main_tmp_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp1 + (-1)*main_path_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp2 + (-1)*main_path_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp3 + (-1)*main_path_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp4 + (-1)*main_path_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp5 + (-1)*main_path_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add75 = fadd double %tmp, %tmp1, !taffo.info !60, !taffo.initweight !23
main_path_CAST_add75_fixbits = solver.IntVar(0, 7, 'main_path_CAST_add75_fixbits')
main_path_CAST_add75_fixp = solver.IntVar(0, 1, 'main_path_CAST_add75_fixp')
main_path_CAST_add75_float = solver.IntVar(0, 1, 'main_path_CAST_add75_float')
main_path_CAST_add75_double = solver.IntVar(0, 1, 'main_path_CAST_add75_double')
solver.Add( + (1)*main_path_CAST_add75_fixp + (1)*main_path_CAST_add75_float + (1)*main_path_CAST_add75_double==1)    #exactly 1 type
solver.Add( + (1)*main_path_CAST_add75_fixbits + (-10000)*main_path_CAST_add75_fixp<=0)    #If no fix, fix frac part = 0
C1_main_path_CAST_add75 = solver.IntVar(0, 1, 'C1_main_path_CAST_add75')
C2_main_path_CAST_add75 = solver.IntVar(0, 1, 'C2_main_path_CAST_add75')
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_add75_fixbits + (-10000)*C1_main_path_CAST_add75<=0)    #Shift cost 1
solver.Add( + (-1)*main_path_fixbits + (1)*main_path_CAST_add75_fixbits + (-10000)*C2_main_path_CAST_add75<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_path_CAST_add75
castCostObj +=  + (1)*C2_main_path_CAST_add75
C3_main_path_CAST_add75 = solver.IntVar(0, 1, 'C3_main_path_CAST_add75')
C4_main_path_CAST_add75 = solver.IntVar(0, 1, 'C4_main_path_CAST_add75')
C5_main_path_CAST_add75 = solver.IntVar(0, 1, 'C5_main_path_CAST_add75')
C6_main_path_CAST_add75 = solver.IntVar(0, 1, 'C6_main_path_CAST_add75')
C7_main_path_CAST_add75 = solver.IntVar(0, 1, 'C7_main_path_CAST_add75')
C8_main_path_CAST_add75 = solver.IntVar(0, 1, 'C8_main_path_CAST_add75')
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add75_float + (-1)*C3_main_path_CAST_add75<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_path_CAST_add75
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add75_fixp + (-1)*C4_main_path_CAST_add75<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_path_CAST_add75
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add75_double + (-1)*C5_main_path_CAST_add75<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_path_CAST_add75
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add75_fixp + (-1)*C6_main_path_CAST_add75<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_path_CAST_add75
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add75_double + (-1)*C7_main_path_CAST_add75<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_path_CAST_add75
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add75_float + (-1)*C8_main_path_CAST_add75<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_path_CAST_add75



#Constraint for cast for   %add75 = fadd double %tmp, %tmp1, !taffo.info !60, !taffo.initweight !23
main_path_CAST_add75_0_fixbits = solver.IntVar(0, 7, 'main_path_CAST_add75_0_fixbits')
main_path_CAST_add75_0_fixp = solver.IntVar(0, 1, 'main_path_CAST_add75_0_fixp')
main_path_CAST_add75_0_float = solver.IntVar(0, 1, 'main_path_CAST_add75_0_float')
main_path_CAST_add75_0_double = solver.IntVar(0, 1, 'main_path_CAST_add75_0_double')
solver.Add( + (1)*main_path_CAST_add75_0_fixp + (1)*main_path_CAST_add75_0_float + (1)*main_path_CAST_add75_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_path_CAST_add75_0_fixbits + (-10000)*main_path_CAST_add75_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C1_main_path_CAST_add75_0')
C2_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C2_main_path_CAST_add75_0')
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_add75_0_fixbits + (-10000)*C1_main_path_CAST_add75_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_path_fixbits + (1)*main_path_CAST_add75_0_fixbits + (-10000)*C2_main_path_CAST_add75_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_path_CAST_add75_0
castCostObj +=  + (1)*C2_main_path_CAST_add75_0
C3_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C3_main_path_CAST_add75_0')
C4_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C4_main_path_CAST_add75_0')
C5_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C5_main_path_CAST_add75_0')
C6_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C6_main_path_CAST_add75_0')
C7_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C7_main_path_CAST_add75_0')
C8_main_path_CAST_add75_0 = solver.IntVar(0, 1, 'C8_main_path_CAST_add75_0')
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add75_0_float + (-1)*C3_main_path_CAST_add75_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_path_CAST_add75_0
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add75_0_fixp + (-1)*C4_main_path_CAST_add75_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_path_CAST_add75_0
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_add75_0_double + (-1)*C5_main_path_CAST_add75_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_path_CAST_add75_0
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add75_0_fixp + (-1)*C6_main_path_CAST_add75_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_path_CAST_add75_0
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_add75_0_double + (-1)*C7_main_path_CAST_add75_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_path_CAST_add75_0
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_add75_0_float + (-1)*C8_main_path_CAST_add75_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_path_CAST_add75_0



#Stuff for   %add75 = fadd double %tmp, %tmp1, !taffo.info !60, !taffo.initweight !23
main_add75_fixbits = solver.IntVar(0, 7, 'main_add75_fixbits')
main_add75_fixp = solver.IntVar(0, 1, 'main_add75_fixp')
main_add75_float = solver.IntVar(0, 1, 'main_add75_float')
main_add75_double = solver.IntVar(0, 1, 'main_add75_double')
main_add75_enob = solver.IntVar(-10000, 10000, 'main_add75_enob')
solver.Add( + (1)*main_add75_enob + (-1)*main_add75_fixbits + (10000)*main_add75_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add75_enob + (10000)*main_add75_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add75_enob + (10000)*main_add75_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add75_fixbits + (-10000)*main_add75_fixp>=-9994)    #Limit the lower number of frac bits7
enobCostObj +=  + (-1)*main_add75_enob
solver.Add( + (1)*main_add75_fixp + (1)*main_add75_float + (1)*main_add75_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add75_fixbits + (-10000)*main_add75_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_path_CAST_add75_fixp + (-1)*main_path_CAST_add75_0_fixp==0)    #fix equality
solver.Add( + (1)*main_path_CAST_add75_float + (-1)*main_path_CAST_add75_0_float==0)    #float equality
solver.Add( + (1)*main_path_CAST_add75_double + (-1)*main_path_CAST_add75_0_double==0)    #double equality
solver.Add( + (1)*main_path_CAST_add75_fixbits + (-1)*main_path_CAST_add75_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_path_CAST_add75_fixp + (-1)*main_add75_fixp==0)    #fix equality
solver.Add( + (1)*main_path_CAST_add75_float + (-1)*main_add75_float==0)    #float equality
solver.Add( + (1)*main_path_CAST_add75_double + (-1)*main_add75_double==0)    #double equality
solver.Add( + (1)*main_path_CAST_add75_fixbits + (-1)*main_add75_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add75_fixp
mathCostObj +=  + (2.33125)*main_add75_float
mathCostObj +=  + (2.72422)*main_add75_double
solver.Add( + (1)*main_add75_enob + (-1)*main_path_enob_memphi_main_tmp<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add75_enob + (-1)*main_path_enob_memphi_main_tmp1<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add75, double* %arrayidx79, align 8, !taffo.info !40, !taffo.initweight !26
main_add75_CAST_store_fixbits = solver.IntVar(0, 7, 'main_add75_CAST_store_fixbits')
main_add75_CAST_store_fixp = solver.IntVar(0, 1, 'main_add75_CAST_store_fixp')
main_add75_CAST_store_float = solver.IntVar(0, 1, 'main_add75_CAST_store_float')
main_add75_CAST_store_double = solver.IntVar(0, 1, 'main_add75_CAST_store_double')
solver.Add( + (1)*main_add75_CAST_store_fixp + (1)*main_add75_CAST_store_float + (1)*main_add75_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add75_CAST_store_fixbits + (-10000)*main_add75_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add75_CAST_store = solver.IntVar(0, 1, 'C1_main_add75_CAST_store')
C2_main_add75_CAST_store = solver.IntVar(0, 1, 'C2_main_add75_CAST_store')
solver.Add( + (1)*main_add75_fixbits + (-1)*main_add75_CAST_store_fixbits + (-10000)*C1_main_add75_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add75_fixbits + (1)*main_add75_CAST_store_fixbits + (-10000)*C2_main_add75_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add75_CAST_store
castCostObj +=  + (1)*C2_main_add75_CAST_store
C3_main_add75_CAST_store = solver.IntVar(0, 1, 'C3_main_add75_CAST_store')
C4_main_add75_CAST_store = solver.IntVar(0, 1, 'C4_main_add75_CAST_store')
C5_main_add75_CAST_store = solver.IntVar(0, 1, 'C5_main_add75_CAST_store')
C6_main_add75_CAST_store = solver.IntVar(0, 1, 'C6_main_add75_CAST_store')
C7_main_add75_CAST_store = solver.IntVar(0, 1, 'C7_main_add75_CAST_store')
C8_main_add75_CAST_store = solver.IntVar(0, 1, 'C8_main_add75_CAST_store')
solver.Add( + (1)*main_add75_fixp + (1)*main_add75_CAST_store_float + (-1)*C3_main_add75_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add75_CAST_store
solver.Add( + (1)*main_add75_float + (1)*main_add75_CAST_store_fixp + (-1)*C4_main_add75_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add75_CAST_store
solver.Add( + (1)*main_add75_fixp + (1)*main_add75_CAST_store_double + (-1)*C5_main_add75_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add75_CAST_store
solver.Add( + (1)*main_add75_double + (1)*main_add75_CAST_store_fixp + (-1)*C6_main_add75_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add75_CAST_store
solver.Add( + (1)*main_add75_float + (1)*main_add75_CAST_store_double + (-1)*C7_main_add75_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add75_CAST_store
solver.Add( + (1)*main_add75_double + (1)*main_add75_CAST_store_float + (-1)*C8_main_add75_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add75_CAST_store
solver.Add( + (1)*main_path_fixp + (-1)*main_add75_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_path_float + (-1)*main_add75_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_path_double + (-1)*main_add75_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_path_fixbits + (-1)*main_add75_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_path_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_path_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB_storeENOB + (-1)*main_path_fixbits + (10000)*main_path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_path_enob_storeENOB_storeENOB_storeENOB + (-1)*main_add75_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp + (-1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp1 + (-1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp2 + (-1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp3 + (-1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp4 + (-1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp5 + (-1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_path_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_path_enob_memphi_main_tmp8')
solver.Add( + (1)*main_path_enob_memphi_main_tmp8 + (-1)*main_path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_2 = solver.IntVar(0, 1, 'main_main_tmp8_enob_2')
main_main_tmp8_enob_3 = solver.IntVar(0, 1, 'main_main_tmp8_enob_3')
main_main_tmp8_enob_4 = solver.IntVar(0, 1, 'main_main_tmp8_enob_4')
solver.Add( + (1)*main_main_tmp8_enob_2 + (1)*main_main_tmp8_enob_3 + (1)*main_main_tmp8_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp8 + (-1)*main_path_enob_storeENOB + (10000)*main_main_tmp8_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp8 + (-1)*main_path_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_path_enob_memphi_main_tmp8 + (-1)*main_path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call109 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp7, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp8), !taffo.info !40, !taffo.initweight !36, !taffo.constinfo !71
main_path_CAST_call109_fixbits = solver.IntVar(0, 7, 'main_path_CAST_call109_fixbits')
main_path_CAST_call109_fixp = solver.IntVar(0, 1, 'main_path_CAST_call109_fixp')
main_path_CAST_call109_float = solver.IntVar(0, 1, 'main_path_CAST_call109_float')
main_path_CAST_call109_double = solver.IntVar(0, 1, 'main_path_CAST_call109_double')
solver.Add( + (1)*main_path_CAST_call109_fixp + (1)*main_path_CAST_call109_float + (1)*main_path_CAST_call109_double==1)    #exactly 1 type
solver.Add( + (1)*main_path_CAST_call109_fixbits + (-10000)*main_path_CAST_call109_fixp<=0)    #If no fix, fix frac part = 0
C1_main_path_CAST_call109 = solver.IntVar(0, 1, 'C1_main_path_CAST_call109')
C2_main_path_CAST_call109 = solver.IntVar(0, 1, 'C2_main_path_CAST_call109')
solver.Add( + (1)*main_path_fixbits + (-1)*main_path_CAST_call109_fixbits + (-10000)*C1_main_path_CAST_call109<=0)    #Shift cost 1
solver.Add( + (-1)*main_path_fixbits + (1)*main_path_CAST_call109_fixbits + (-10000)*C2_main_path_CAST_call109<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_path_CAST_call109
castCostObj +=  + (1)*C2_main_path_CAST_call109
C3_main_path_CAST_call109 = solver.IntVar(0, 1, 'C3_main_path_CAST_call109')
C4_main_path_CAST_call109 = solver.IntVar(0, 1, 'C4_main_path_CAST_call109')
C5_main_path_CAST_call109 = solver.IntVar(0, 1, 'C5_main_path_CAST_call109')
C6_main_path_CAST_call109 = solver.IntVar(0, 1, 'C6_main_path_CAST_call109')
C7_main_path_CAST_call109 = solver.IntVar(0, 1, 'C7_main_path_CAST_call109')
C8_main_path_CAST_call109 = solver.IntVar(0, 1, 'C8_main_path_CAST_call109')
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_call109_float + (-1)*C3_main_path_CAST_call109<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_path_CAST_call109
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_call109_fixp + (-1)*C4_main_path_CAST_call109<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_path_CAST_call109
solver.Add( + (1)*main_path_fixp + (1)*main_path_CAST_call109_double + (-1)*C5_main_path_CAST_call109<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_path_CAST_call109
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_call109_fixp + (-1)*C6_main_path_CAST_call109<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_path_CAST_call109
solver.Add( + (1)*main_path_float + (1)*main_path_CAST_call109_double + (-1)*C7_main_path_CAST_call109<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_path_CAST_call109
solver.Add( + (1)*main_path_double + (1)*main_path_CAST_call109_float + (-1)*C8_main_path_CAST_call109<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_path_CAST_call109
solver.Add( + (1)*main_path_CAST_call109_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 218.809+ 1 * enobCostObj / 2814+ 1000 * mathCostObj / 5.44845)

# Model declaration end.