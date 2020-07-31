


#Stuff for @path = common dso_local global [60 x [60 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
path_fixbits = solver.IntVar(0, 7, 'path_fixbits')
path_fixp = solver.IntVar(0, 1, 'path_fixp')
path_float = solver.IntVar(0, 1, 'path_float')
path_double = solver.IntVar(0, 1, 'path_double')
path_enob = solver.IntVar(-10000, 10000, 'path_enob')
solver.Add( + (1)*path_enob + (-1)*path_fixbits + (10000)*path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*path_enob + (10000)*path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*path_enob + (10000)*path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*path_fixbits + (-10000)*path_fixp>=-9994)    #Limit the lower number of frac bits7
solver.Add( + (1)*path_enob<=333)    #Enob constraint for error maximal
enobCostObj =  + (-1)*path_enob
solver.Add( + (1)*path_fixp + (1)*path_float + (1)*path_double==1)    #Exactly one selected type
solver.Add( + (1)*path_fixbits + (-10000)*path_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %add to double, !taffo.info !33, !taffo.initweight !36
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



#Constraint for cast for   store double %conv, double* %arrayidx7, align 8, !taffo.info !40, !taffo.initweight !25
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
solver.Add( + (1)*path_fixp + (-1)*main_conv_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*path_float + (-1)*main_conv_CAST_store_float==0)    #float equality
solver.Add( + (1)*path_double + (-1)*main_conv_CAST_store_double==0)    #double equality
solver.Add( + (1)*path_fixbits + (-1)*main_conv_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
path_enob_storeENOB = solver.IntVar(-10000, 10000, 'path_enob_storeENOB')
solver.Add( + (1)*path_enob_storeENOB + (-1)*path_fixbits + (10000)*path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*path_enob_storeENOB + (10000)*path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*path_enob_storeENOB + (10000)*path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*path_enob_storeENOB + (-1)*main_conv_enob<=0)    #Enob constraint ENOB propagation in load/store



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



#Constraint for cast for   store double 9.990000e+02, double* %arrayidx24, align 8, !taffo.info !40, !taffo.initweight !25, !taffo.constinfo !46
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
solver.Add( + (1)*path_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*path_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*path_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*path_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
path_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'path_enob_memphi_main_tmp')
solver.Add( + (1)*path_enob_memphi_main_tmp + (-1)*path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_2 = solver.IntVar(0, 1, 'main_main_tmp_enob_2')
main_main_tmp_enob_3 = solver.IntVar(0, 1, 'main_main_tmp_enob_3')
main_main_tmp_enob_4 = solver.IntVar(0, 1, 'main_main_tmp_enob_4')
solver.Add( + (1)*main_main_tmp_enob_2 + (1)*main_main_tmp_enob_3 + (1)*main_main_tmp_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp + (-1)*path_enob_storeENOB + (10000)*main_main_tmp_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
path_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'path_enob_memphi_main_tmp1')
solver.Add( + (1)*path_enob_memphi_main_tmp1 + (-1)*path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
main_main_tmp1_enob_3 = solver.IntVar(0, 1, 'main_main_tmp1_enob_3')
main_main_tmp1_enob_4 = solver.IntVar(0, 1, 'main_main_tmp1_enob_4')
solver.Add( + (1)*main_main_tmp1_enob_2 + (1)*main_main_tmp1_enob_3 + (1)*main_main_tmp1_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp1 + (-1)*path_enob_storeENOB + (10000)*main_main_tmp1_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
path_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'path_enob_memphi_main_tmp2')
solver.Add( + (1)*path_enob_memphi_main_tmp2 + (-1)*path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
main_main_tmp2_enob_3 = solver.IntVar(0, 1, 'main_main_tmp2_enob_3')
main_main_tmp2_enob_4 = solver.IntVar(0, 1, 'main_main_tmp2_enob_4')
solver.Add( + (1)*main_main_tmp2_enob_2 + (1)*main_main_tmp2_enob_3 + (1)*main_main_tmp2_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp2 + (-1)*path_enob_storeENOB + (10000)*main_main_tmp2_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
path_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'path_enob_memphi_main_tmp3')
solver.Add( + (1)*path_enob_memphi_main_tmp3 + (-1)*path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
solver.Add( + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3 + (1)*main_main_tmp3_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp3 + (-1)*path_enob_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
path_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'path_enob_memphi_main_tmp4')
solver.Add( + (1)*path_enob_memphi_main_tmp4 + (-1)*path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
main_main_tmp4_enob_4 = solver.IntVar(0, 1, 'main_main_tmp4_enob_4')
solver.Add( + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3 + (1)*main_main_tmp4_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp4 + (-1)*path_enob_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add62 = fadd double %tmp3, %tmp4, !taffo.info !57, !taffo.initweight !35
path_CAST_add62_fixbits = solver.IntVar(0, 7, 'path_CAST_add62_fixbits')
path_CAST_add62_fixp = solver.IntVar(0, 1, 'path_CAST_add62_fixp')
path_CAST_add62_float = solver.IntVar(0, 1, 'path_CAST_add62_float')
path_CAST_add62_double = solver.IntVar(0, 1, 'path_CAST_add62_double')
solver.Add( + (1)*path_CAST_add62_fixp + (1)*path_CAST_add62_float + (1)*path_CAST_add62_double==1)    #exactly 1 type
solver.Add( + (1)*path_CAST_add62_fixbits + (-10000)*path_CAST_add62_fixp<=0)    #If no fix, fix frac part = 0
C1_path_CAST_add62 = solver.IntVar(0, 1, 'C1_path_CAST_add62')
C2_path_CAST_add62 = solver.IntVar(0, 1, 'C2_path_CAST_add62')
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_add62_fixbits + (-10000)*C1_path_CAST_add62<=0)    #Shift cost 1
solver.Add( + (-1)*path_fixbits + (1)*path_CAST_add62_fixbits + (-10000)*C2_path_CAST_add62<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_path_CAST_add62
castCostObj +=  + (1)*C2_path_CAST_add62
C3_path_CAST_add62 = solver.IntVar(0, 1, 'C3_path_CAST_add62')
C4_path_CAST_add62 = solver.IntVar(0, 1, 'C4_path_CAST_add62')
C5_path_CAST_add62 = solver.IntVar(0, 1, 'C5_path_CAST_add62')
C6_path_CAST_add62 = solver.IntVar(0, 1, 'C6_path_CAST_add62')
C7_path_CAST_add62 = solver.IntVar(0, 1, 'C7_path_CAST_add62')
C8_path_CAST_add62 = solver.IntVar(0, 1, 'C8_path_CAST_add62')
solver.Add( + (1)*path_fixp + (1)*path_CAST_add62_float + (-1)*C3_path_CAST_add62<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_path_CAST_add62
solver.Add( + (1)*path_float + (1)*path_CAST_add62_fixp + (-1)*C4_path_CAST_add62<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_path_CAST_add62
solver.Add( + (1)*path_fixp + (1)*path_CAST_add62_double + (-1)*C5_path_CAST_add62<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_path_CAST_add62
solver.Add( + (1)*path_double + (1)*path_CAST_add62_fixp + (-1)*C6_path_CAST_add62<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_path_CAST_add62
solver.Add( + (1)*path_float + (1)*path_CAST_add62_double + (-1)*C7_path_CAST_add62<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_path_CAST_add62
solver.Add( + (1)*path_double + (1)*path_CAST_add62_float + (-1)*C8_path_CAST_add62<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_path_CAST_add62



#Constraint for cast for   %add62 = fadd double %tmp3, %tmp4, !taffo.info !57, !taffo.initweight !35
path_CAST_add62_0_fixbits = solver.IntVar(0, 7, 'path_CAST_add62_0_fixbits')
path_CAST_add62_0_fixp = solver.IntVar(0, 1, 'path_CAST_add62_0_fixp')
path_CAST_add62_0_float = solver.IntVar(0, 1, 'path_CAST_add62_0_float')
path_CAST_add62_0_double = solver.IntVar(0, 1, 'path_CAST_add62_0_double')
solver.Add( + (1)*path_CAST_add62_0_fixp + (1)*path_CAST_add62_0_float + (1)*path_CAST_add62_0_double==1)    #exactly 1 type
solver.Add( + (1)*path_CAST_add62_0_fixbits + (-10000)*path_CAST_add62_0_fixp<=0)    #If no fix, fix frac part = 0
C1_path_CAST_add62_0 = solver.IntVar(0, 1, 'C1_path_CAST_add62_0')
C2_path_CAST_add62_0 = solver.IntVar(0, 1, 'C2_path_CAST_add62_0')
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_add62_0_fixbits + (-10000)*C1_path_CAST_add62_0<=0)    #Shift cost 1
solver.Add( + (-1)*path_fixbits + (1)*path_CAST_add62_0_fixbits + (-10000)*C2_path_CAST_add62_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_path_CAST_add62_0
castCostObj +=  + (1)*C2_path_CAST_add62_0
C3_path_CAST_add62_0 = solver.IntVar(0, 1, 'C3_path_CAST_add62_0')
C4_path_CAST_add62_0 = solver.IntVar(0, 1, 'C4_path_CAST_add62_0')
C5_path_CAST_add62_0 = solver.IntVar(0, 1, 'C5_path_CAST_add62_0')
C6_path_CAST_add62_0 = solver.IntVar(0, 1, 'C6_path_CAST_add62_0')
C7_path_CAST_add62_0 = solver.IntVar(0, 1, 'C7_path_CAST_add62_0')
C8_path_CAST_add62_0 = solver.IntVar(0, 1, 'C8_path_CAST_add62_0')
solver.Add( + (1)*path_fixp + (1)*path_CAST_add62_0_float + (-1)*C3_path_CAST_add62_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_path_CAST_add62_0
solver.Add( + (1)*path_float + (1)*path_CAST_add62_0_fixp + (-1)*C4_path_CAST_add62_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_path_CAST_add62_0
solver.Add( + (1)*path_fixp + (1)*path_CAST_add62_0_double + (-1)*C5_path_CAST_add62_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_path_CAST_add62_0
solver.Add( + (1)*path_double + (1)*path_CAST_add62_0_fixp + (-1)*C6_path_CAST_add62_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_path_CAST_add62_0
solver.Add( + (1)*path_float + (1)*path_CAST_add62_0_double + (-1)*C7_path_CAST_add62_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_path_CAST_add62_0
solver.Add( + (1)*path_double + (1)*path_CAST_add62_0_float + (-1)*C8_path_CAST_add62_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_path_CAST_add62_0



#Stuff for   %add62 = fadd double %tmp3, %tmp4, !taffo.info !57, !taffo.initweight !35
main_add62_fixbits = solver.IntVar(0, 6, 'main_add62_fixbits')
main_add62_fixp = solver.IntVar(0, 1, 'main_add62_fixp')
main_add62_float = solver.IntVar(0, 1, 'main_add62_float')
main_add62_double = solver.IntVar(0, 1, 'main_add62_double')
main_add62_enob = solver.IntVar(-10000, 10000, 'main_add62_enob')
solver.Add( + (1)*main_add62_enob + (-1)*main_add62_fixbits + (10000)*main_add62_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add62_enob + (10000)*main_add62_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add62_enob + (10000)*main_add62_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add62_fixbits + (-10000)*main_add62_fixp>=-9995)    #Limit the lower number of frac bits6
solver.Add( + (1)*main_add62_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add62_enob
solver.Add( + (1)*main_add62_fixp + (1)*main_add62_float + (1)*main_add62_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add62_fixbits + (-10000)*main_add62_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*path_CAST_add62_fixp + (-1)*path_CAST_add62_0_fixp==0)    #fix equality
solver.Add( + (1)*path_CAST_add62_float + (-1)*path_CAST_add62_0_float==0)    #float equality
solver.Add( + (1)*path_CAST_add62_double + (-1)*path_CAST_add62_0_double==0)    #double equality
solver.Add( + (1)*path_CAST_add62_fixbits + (-1)*path_CAST_add62_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*path_CAST_add62_fixp + (-1)*main_add62_fixp==0)    #fix equality
solver.Add( + (1)*path_CAST_add62_float + (-1)*main_add62_float==0)    #float equality
solver.Add( + (1)*path_CAST_add62_double + (-1)*main_add62_double==0)    #double equality
solver.Add( + (1)*path_CAST_add62_fixbits + (-1)*main_add62_fixbits==0)    #same fractional bit
mathCostObj =  + (1.24179)*main_add62_fixp
mathCostObj +=  + (2.33125)*main_add62_float
mathCostObj +=  + (2.72422)*main_add62_double
solver.Add( + (1)*main_add62_enob + (-1)*path_enob_memphi_main_tmp3<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add62_enob + (-1)*path_enob_memphi_main_tmp4<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %cmp63 = fcmp olt double %tmp2, %add62, !taffo.info !59, !taffo.initweight !35
path_CAST_cmp63_fixbits = solver.IntVar(0, 7, 'path_CAST_cmp63_fixbits')
path_CAST_cmp63_fixp = solver.IntVar(0, 1, 'path_CAST_cmp63_fixp')
path_CAST_cmp63_float = solver.IntVar(0, 1, 'path_CAST_cmp63_float')
path_CAST_cmp63_double = solver.IntVar(0, 1, 'path_CAST_cmp63_double')
solver.Add( + (1)*path_CAST_cmp63_fixp + (1)*path_CAST_cmp63_float + (1)*path_CAST_cmp63_double==1)    #exactly 1 type
solver.Add( + (1)*path_CAST_cmp63_fixbits + (-10000)*path_CAST_cmp63_fixp<=0)    #If no fix, fix frac part = 0
C1_path_CAST_cmp63 = solver.IntVar(0, 1, 'C1_path_CAST_cmp63')
C2_path_CAST_cmp63 = solver.IntVar(0, 1, 'C2_path_CAST_cmp63')
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_cmp63_fixbits + (-10000)*C1_path_CAST_cmp63<=0)    #Shift cost 1
solver.Add( + (-1)*path_fixbits + (1)*path_CAST_cmp63_fixbits + (-10000)*C2_path_CAST_cmp63<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_path_CAST_cmp63
castCostObj +=  + (1)*C2_path_CAST_cmp63
C3_path_CAST_cmp63 = solver.IntVar(0, 1, 'C3_path_CAST_cmp63')
C4_path_CAST_cmp63 = solver.IntVar(0, 1, 'C4_path_CAST_cmp63')
C5_path_CAST_cmp63 = solver.IntVar(0, 1, 'C5_path_CAST_cmp63')
C6_path_CAST_cmp63 = solver.IntVar(0, 1, 'C6_path_CAST_cmp63')
C7_path_CAST_cmp63 = solver.IntVar(0, 1, 'C7_path_CAST_cmp63')
C8_path_CAST_cmp63 = solver.IntVar(0, 1, 'C8_path_CAST_cmp63')
solver.Add( + (1)*path_fixp + (1)*path_CAST_cmp63_float + (-1)*C3_path_CAST_cmp63<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_path_CAST_cmp63
solver.Add( + (1)*path_float + (1)*path_CAST_cmp63_fixp + (-1)*C4_path_CAST_cmp63<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_path_CAST_cmp63
solver.Add( + (1)*path_fixp + (1)*path_CAST_cmp63_double + (-1)*C5_path_CAST_cmp63<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_path_CAST_cmp63
solver.Add( + (1)*path_double + (1)*path_CAST_cmp63_fixp + (-1)*C6_path_CAST_cmp63<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_path_CAST_cmp63
solver.Add( + (1)*path_float + (1)*path_CAST_cmp63_double + (-1)*C7_path_CAST_cmp63<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_path_CAST_cmp63
solver.Add( + (1)*path_double + (1)*path_CAST_cmp63_float + (-1)*C8_path_CAST_cmp63<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_path_CAST_cmp63



#Constraint for cast for   %cmp63 = fcmp olt double %tmp2, %add62, !taffo.info !59, !taffo.initweight !35
main_add62_CAST_cmp63_fixbits = solver.IntVar(0, 6, 'main_add62_CAST_cmp63_fixbits')
main_add62_CAST_cmp63_fixp = solver.IntVar(0, 1, 'main_add62_CAST_cmp63_fixp')
main_add62_CAST_cmp63_float = solver.IntVar(0, 1, 'main_add62_CAST_cmp63_float')
main_add62_CAST_cmp63_double = solver.IntVar(0, 1, 'main_add62_CAST_cmp63_double')
solver.Add( + (1)*main_add62_CAST_cmp63_fixp + (1)*main_add62_CAST_cmp63_float + (1)*main_add62_CAST_cmp63_double==1)    #exactly 1 type
solver.Add( + (1)*main_add62_CAST_cmp63_fixbits + (-10000)*main_add62_CAST_cmp63_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C1_main_add62_CAST_cmp63')
C2_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C2_main_add62_CAST_cmp63')
solver.Add( + (1)*main_add62_fixbits + (-1)*main_add62_CAST_cmp63_fixbits + (-10000)*C1_main_add62_CAST_cmp63<=0)    #Shift cost 1
solver.Add( + (-1)*main_add62_fixbits + (1)*main_add62_CAST_cmp63_fixbits + (-10000)*C2_main_add62_CAST_cmp63<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add62_CAST_cmp63
castCostObj +=  + (1)*C2_main_add62_CAST_cmp63
C3_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C3_main_add62_CAST_cmp63')
C4_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C4_main_add62_CAST_cmp63')
C5_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C5_main_add62_CAST_cmp63')
C6_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C6_main_add62_CAST_cmp63')
C7_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C7_main_add62_CAST_cmp63')
C8_main_add62_CAST_cmp63 = solver.IntVar(0, 1, 'C8_main_add62_CAST_cmp63')
solver.Add( + (1)*main_add62_fixp + (1)*main_add62_CAST_cmp63_float + (-1)*C3_main_add62_CAST_cmp63<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add62_CAST_cmp63
solver.Add( + (1)*main_add62_float + (1)*main_add62_CAST_cmp63_fixp + (-1)*C4_main_add62_CAST_cmp63<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add62_CAST_cmp63
solver.Add( + (1)*main_add62_fixp + (1)*main_add62_CAST_cmp63_double + (-1)*C5_main_add62_CAST_cmp63<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add62_CAST_cmp63
solver.Add( + (1)*main_add62_double + (1)*main_add62_CAST_cmp63_fixp + (-1)*C6_main_add62_CAST_cmp63<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add62_CAST_cmp63
solver.Add( + (1)*main_add62_float + (1)*main_add62_CAST_cmp63_double + (-1)*C7_main_add62_CAST_cmp63<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add62_CAST_cmp63
solver.Add( + (1)*main_add62_double + (1)*main_add62_CAST_cmp63_float + (-1)*C8_main_add62_CAST_cmp63<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add62_CAST_cmp63
solver.Add( + (1)*path_CAST_cmp63_fixp + (-1)*main_add62_CAST_cmp63_fixp==0)    #fix equality
solver.Add( + (1)*path_CAST_cmp63_float + (-1)*main_add62_CAST_cmp63_float==0)    #float equality
solver.Add( + (1)*path_CAST_cmp63_double + (-1)*main_add62_CAST_cmp63_double==0)    #double equality
solver.Add( + (1)*path_CAST_cmp63_fixbits + (-1)*main_add62_CAST_cmp63_fixbits==0)    #same fractional bit

#Restriction for new enob [LOAD]
path_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'path_enob_memphi_main_tmp5')
solver.Add( + (1)*path_enob_memphi_main_tmp5 + (-1)*path_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
main_main_tmp5_enob_4 = solver.IntVar(0, 1, 'main_main_tmp5_enob_4')
solver.Add( + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3 + (1)*main_main_tmp5_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp5 + (-1)*path_enob_storeENOB + (10000)*main_main_tmp5_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp5, double* %arrayidx73, align 8, !taffo.info !40, !taffo.initweight !25
path_CAST_store_fixbits = solver.IntVar(0, 7, 'path_CAST_store_fixbits')
path_CAST_store_fixp = solver.IntVar(0, 1, 'path_CAST_store_fixp')
path_CAST_store_float = solver.IntVar(0, 1, 'path_CAST_store_float')
path_CAST_store_double = solver.IntVar(0, 1, 'path_CAST_store_double')
solver.Add( + (1)*path_CAST_store_fixp + (1)*path_CAST_store_float + (1)*path_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*path_CAST_store_fixbits + (-10000)*path_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_path_CAST_store = solver.IntVar(0, 1, 'C1_path_CAST_store')
C2_path_CAST_store = solver.IntVar(0, 1, 'C2_path_CAST_store')
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_store_fixbits + (-10000)*C1_path_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*path_fixbits + (1)*path_CAST_store_fixbits + (-10000)*C2_path_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_path_CAST_store
castCostObj +=  + (1)*C2_path_CAST_store
C3_path_CAST_store = solver.IntVar(0, 1, 'C3_path_CAST_store')
C4_path_CAST_store = solver.IntVar(0, 1, 'C4_path_CAST_store')
C5_path_CAST_store = solver.IntVar(0, 1, 'C5_path_CAST_store')
C6_path_CAST_store = solver.IntVar(0, 1, 'C6_path_CAST_store')
C7_path_CAST_store = solver.IntVar(0, 1, 'C7_path_CAST_store')
C8_path_CAST_store = solver.IntVar(0, 1, 'C8_path_CAST_store')
solver.Add( + (1)*path_fixp + (1)*path_CAST_store_float + (-1)*C3_path_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_path_CAST_store
solver.Add( + (1)*path_float + (1)*path_CAST_store_fixp + (-1)*C4_path_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_path_CAST_store
solver.Add( + (1)*path_fixp + (1)*path_CAST_store_double + (-1)*C5_path_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_path_CAST_store
solver.Add( + (1)*path_double + (1)*path_CAST_store_fixp + (-1)*C6_path_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_path_CAST_store
solver.Add( + (1)*path_float + (1)*path_CAST_store_double + (-1)*C7_path_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_path_CAST_store
solver.Add( + (1)*path_double + (1)*path_CAST_store_float + (-1)*C8_path_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_path_CAST_store
solver.Add( + (1)*path_fixp + (-1)*path_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*path_float + (-1)*path_CAST_store_float==0)    #float equality
solver.Add( + (1)*path_double + (-1)*path_CAST_store_double==0)    #double equality
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
path_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'path_enob_storeENOB_storeENOB')
solver.Add( + (1)*path_enob_storeENOB_storeENOB + (-1)*path_fixbits + (10000)*path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*path_enob_storeENOB_storeENOB + (10000)*path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*path_enob_storeENOB_storeENOB + (10000)*path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*path_enob_storeENOB_storeENOB + (-1)*path_enob_memphi_main_tmp5<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp + (-1)*path_enob_storeENOB_storeENOB + (10000)*main_main_tmp_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp1 + (-1)*path_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp2 + (-1)*path_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp3 + (-1)*path_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp4 + (-1)*path_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp5 + (-1)*path_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add74 = fadd double %tmp, %tmp1, !taffo.info !60, !taffo.initweight !22
path_CAST_add74_fixbits = solver.IntVar(0, 7, 'path_CAST_add74_fixbits')
path_CAST_add74_fixp = solver.IntVar(0, 1, 'path_CAST_add74_fixp')
path_CAST_add74_float = solver.IntVar(0, 1, 'path_CAST_add74_float')
path_CAST_add74_double = solver.IntVar(0, 1, 'path_CAST_add74_double')
solver.Add( + (1)*path_CAST_add74_fixp + (1)*path_CAST_add74_float + (1)*path_CAST_add74_double==1)    #exactly 1 type
solver.Add( + (1)*path_CAST_add74_fixbits + (-10000)*path_CAST_add74_fixp<=0)    #If no fix, fix frac part = 0
C1_path_CAST_add74 = solver.IntVar(0, 1, 'C1_path_CAST_add74')
C2_path_CAST_add74 = solver.IntVar(0, 1, 'C2_path_CAST_add74')
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_add74_fixbits + (-10000)*C1_path_CAST_add74<=0)    #Shift cost 1
solver.Add( + (-1)*path_fixbits + (1)*path_CAST_add74_fixbits + (-10000)*C2_path_CAST_add74<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_path_CAST_add74
castCostObj +=  + (1)*C2_path_CAST_add74
C3_path_CAST_add74 = solver.IntVar(0, 1, 'C3_path_CAST_add74')
C4_path_CAST_add74 = solver.IntVar(0, 1, 'C4_path_CAST_add74')
C5_path_CAST_add74 = solver.IntVar(0, 1, 'C5_path_CAST_add74')
C6_path_CAST_add74 = solver.IntVar(0, 1, 'C6_path_CAST_add74')
C7_path_CAST_add74 = solver.IntVar(0, 1, 'C7_path_CAST_add74')
C8_path_CAST_add74 = solver.IntVar(0, 1, 'C8_path_CAST_add74')
solver.Add( + (1)*path_fixp + (1)*path_CAST_add74_float + (-1)*C3_path_CAST_add74<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_path_CAST_add74
solver.Add( + (1)*path_float + (1)*path_CAST_add74_fixp + (-1)*C4_path_CAST_add74<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_path_CAST_add74
solver.Add( + (1)*path_fixp + (1)*path_CAST_add74_double + (-1)*C5_path_CAST_add74<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_path_CAST_add74
solver.Add( + (1)*path_double + (1)*path_CAST_add74_fixp + (-1)*C6_path_CAST_add74<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_path_CAST_add74
solver.Add( + (1)*path_float + (1)*path_CAST_add74_double + (-1)*C7_path_CAST_add74<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_path_CAST_add74
solver.Add( + (1)*path_double + (1)*path_CAST_add74_float + (-1)*C8_path_CAST_add74<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_path_CAST_add74



#Constraint for cast for   %add74 = fadd double %tmp, %tmp1, !taffo.info !60, !taffo.initweight !22
path_CAST_add74_0_fixbits = solver.IntVar(0, 7, 'path_CAST_add74_0_fixbits')
path_CAST_add74_0_fixp = solver.IntVar(0, 1, 'path_CAST_add74_0_fixp')
path_CAST_add74_0_float = solver.IntVar(0, 1, 'path_CAST_add74_0_float')
path_CAST_add74_0_double = solver.IntVar(0, 1, 'path_CAST_add74_0_double')
solver.Add( + (1)*path_CAST_add74_0_fixp + (1)*path_CAST_add74_0_float + (1)*path_CAST_add74_0_double==1)    #exactly 1 type
solver.Add( + (1)*path_CAST_add74_0_fixbits + (-10000)*path_CAST_add74_0_fixp<=0)    #If no fix, fix frac part = 0
C1_path_CAST_add74_0 = solver.IntVar(0, 1, 'C1_path_CAST_add74_0')
C2_path_CAST_add74_0 = solver.IntVar(0, 1, 'C2_path_CAST_add74_0')
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_add74_0_fixbits + (-10000)*C1_path_CAST_add74_0<=0)    #Shift cost 1
solver.Add( + (-1)*path_fixbits + (1)*path_CAST_add74_0_fixbits + (-10000)*C2_path_CAST_add74_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_path_CAST_add74_0
castCostObj +=  + (1)*C2_path_CAST_add74_0
C3_path_CAST_add74_0 = solver.IntVar(0, 1, 'C3_path_CAST_add74_0')
C4_path_CAST_add74_0 = solver.IntVar(0, 1, 'C4_path_CAST_add74_0')
C5_path_CAST_add74_0 = solver.IntVar(0, 1, 'C5_path_CAST_add74_0')
C6_path_CAST_add74_0 = solver.IntVar(0, 1, 'C6_path_CAST_add74_0')
C7_path_CAST_add74_0 = solver.IntVar(0, 1, 'C7_path_CAST_add74_0')
C8_path_CAST_add74_0 = solver.IntVar(0, 1, 'C8_path_CAST_add74_0')
solver.Add( + (1)*path_fixp + (1)*path_CAST_add74_0_float + (-1)*C3_path_CAST_add74_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_path_CAST_add74_0
solver.Add( + (1)*path_float + (1)*path_CAST_add74_0_fixp + (-1)*C4_path_CAST_add74_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_path_CAST_add74_0
solver.Add( + (1)*path_fixp + (1)*path_CAST_add74_0_double + (-1)*C5_path_CAST_add74_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_path_CAST_add74_0
solver.Add( + (1)*path_double + (1)*path_CAST_add74_0_fixp + (-1)*C6_path_CAST_add74_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_path_CAST_add74_0
solver.Add( + (1)*path_float + (1)*path_CAST_add74_0_double + (-1)*C7_path_CAST_add74_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_path_CAST_add74_0
solver.Add( + (1)*path_double + (1)*path_CAST_add74_0_float + (-1)*C8_path_CAST_add74_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_path_CAST_add74_0



#Stuff for   %add74 = fadd double %tmp, %tmp1, !taffo.info !60, !taffo.initweight !22
main_add74_fixbits = solver.IntVar(0, 7, 'main_add74_fixbits')
main_add74_fixp = solver.IntVar(0, 1, 'main_add74_fixp')
main_add74_float = solver.IntVar(0, 1, 'main_add74_float')
main_add74_double = solver.IntVar(0, 1, 'main_add74_double')
main_add74_enob = solver.IntVar(-10000, 10000, 'main_add74_enob')
solver.Add( + (1)*main_add74_enob + (-1)*main_add74_fixbits + (10000)*main_add74_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add74_enob + (10000)*main_add74_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add74_enob + (10000)*main_add74_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add74_fixbits + (-10000)*main_add74_fixp>=-9994)    #Limit the lower number of frac bits7
enobCostObj +=  + (-1)*main_add74_enob
solver.Add( + (1)*main_add74_fixp + (1)*main_add74_float + (1)*main_add74_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add74_fixbits + (-10000)*main_add74_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*path_CAST_add74_fixp + (-1)*path_CAST_add74_0_fixp==0)    #fix equality
solver.Add( + (1)*path_CAST_add74_float + (-1)*path_CAST_add74_0_float==0)    #float equality
solver.Add( + (1)*path_CAST_add74_double + (-1)*path_CAST_add74_0_double==0)    #double equality
solver.Add( + (1)*path_CAST_add74_fixbits + (-1)*path_CAST_add74_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*path_CAST_add74_fixp + (-1)*main_add74_fixp==0)    #fix equality
solver.Add( + (1)*path_CAST_add74_float + (-1)*main_add74_float==0)    #float equality
solver.Add( + (1)*path_CAST_add74_double + (-1)*main_add74_double==0)    #double equality
solver.Add( + (1)*path_CAST_add74_fixbits + (-1)*main_add74_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add74_fixp
mathCostObj +=  + (2.33125)*main_add74_float
mathCostObj +=  + (2.72422)*main_add74_double
solver.Add( + (1)*main_add74_enob + (-1)*path_enob_memphi_main_tmp<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add74_enob + (-1)*path_enob_memphi_main_tmp1<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add74, double* %arrayidx78, align 8, !taffo.info !40, !taffo.initweight !25
main_add74_CAST_store_fixbits = solver.IntVar(0, 7, 'main_add74_CAST_store_fixbits')
main_add74_CAST_store_fixp = solver.IntVar(0, 1, 'main_add74_CAST_store_fixp')
main_add74_CAST_store_float = solver.IntVar(0, 1, 'main_add74_CAST_store_float')
main_add74_CAST_store_double = solver.IntVar(0, 1, 'main_add74_CAST_store_double')
solver.Add( + (1)*main_add74_CAST_store_fixp + (1)*main_add74_CAST_store_float + (1)*main_add74_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add74_CAST_store_fixbits + (-10000)*main_add74_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add74_CAST_store = solver.IntVar(0, 1, 'C1_main_add74_CAST_store')
C2_main_add74_CAST_store = solver.IntVar(0, 1, 'C2_main_add74_CAST_store')
solver.Add( + (1)*main_add74_fixbits + (-1)*main_add74_CAST_store_fixbits + (-10000)*C1_main_add74_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add74_fixbits + (1)*main_add74_CAST_store_fixbits + (-10000)*C2_main_add74_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add74_CAST_store
castCostObj +=  + (1)*C2_main_add74_CAST_store
C3_main_add74_CAST_store = solver.IntVar(0, 1, 'C3_main_add74_CAST_store')
C4_main_add74_CAST_store = solver.IntVar(0, 1, 'C4_main_add74_CAST_store')
C5_main_add74_CAST_store = solver.IntVar(0, 1, 'C5_main_add74_CAST_store')
C6_main_add74_CAST_store = solver.IntVar(0, 1, 'C6_main_add74_CAST_store')
C7_main_add74_CAST_store = solver.IntVar(0, 1, 'C7_main_add74_CAST_store')
C8_main_add74_CAST_store = solver.IntVar(0, 1, 'C8_main_add74_CAST_store')
solver.Add( + (1)*main_add74_fixp + (1)*main_add74_CAST_store_float + (-1)*C3_main_add74_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add74_CAST_store
solver.Add( + (1)*main_add74_float + (1)*main_add74_CAST_store_fixp + (-1)*C4_main_add74_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add74_CAST_store
solver.Add( + (1)*main_add74_fixp + (1)*main_add74_CAST_store_double + (-1)*C5_main_add74_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add74_CAST_store
solver.Add( + (1)*main_add74_double + (1)*main_add74_CAST_store_fixp + (-1)*C6_main_add74_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add74_CAST_store
solver.Add( + (1)*main_add74_float + (1)*main_add74_CAST_store_double + (-1)*C7_main_add74_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add74_CAST_store
solver.Add( + (1)*main_add74_double + (1)*main_add74_CAST_store_float + (-1)*C8_main_add74_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add74_CAST_store
solver.Add( + (1)*path_fixp + (-1)*main_add74_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*path_float + (-1)*main_add74_CAST_store_float==0)    #float equality
solver.Add( + (1)*path_double + (-1)*main_add74_CAST_store_double==0)    #double equality
solver.Add( + (1)*path_fixbits + (-1)*main_add74_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
path_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'path_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*path_enob_storeENOB_storeENOB_storeENOB + (-1)*path_fixbits + (10000)*path_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*path_float<=10149)    #Enob constraint for float
solver.Add( + (1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*path_double<=11074)    #Enob constraint for double
solver.Add( + (1)*path_enob_storeENOB_storeENOB_storeENOB + (-1)*main_add74_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp + (-1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp1 + (-1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp2 + (-1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp3 + (-1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp4 + (-1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*path_enob_memphi_main_tmp5 + (-1)*path_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
path_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'path_enob_memphi_main_tmp8')
solver.Add( + (1)*path_enob_memphi_main_tmp8 + (-1)*path_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call108 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp7, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.5, i32 0, i32 0), double %tmp8), !taffo.info !40, !taffo.initweight !35, !taffo.constinfo !71
path_CAST_call108_fixbits = solver.IntVar(0, 7, 'path_CAST_call108_fixbits')
path_CAST_call108_fixp = solver.IntVar(0, 1, 'path_CAST_call108_fixp')
path_CAST_call108_float = solver.IntVar(0, 1, 'path_CAST_call108_float')
path_CAST_call108_double = solver.IntVar(0, 1, 'path_CAST_call108_double')
solver.Add( + (1)*path_CAST_call108_fixp + (1)*path_CAST_call108_float + (1)*path_CAST_call108_double==1)    #exactly 1 type
solver.Add( + (1)*path_CAST_call108_fixbits + (-10000)*path_CAST_call108_fixp<=0)    #If no fix, fix frac part = 0
C1_path_CAST_call108 = solver.IntVar(0, 1, 'C1_path_CAST_call108')
C2_path_CAST_call108 = solver.IntVar(0, 1, 'C2_path_CAST_call108')
solver.Add( + (1)*path_fixbits + (-1)*path_CAST_call108_fixbits + (-10000)*C1_path_CAST_call108<=0)    #Shift cost 1
solver.Add( + (-1)*path_fixbits + (1)*path_CAST_call108_fixbits + (-10000)*C2_path_CAST_call108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_path_CAST_call108
castCostObj +=  + (1)*C2_path_CAST_call108
C3_path_CAST_call108 = solver.IntVar(0, 1, 'C3_path_CAST_call108')
C4_path_CAST_call108 = solver.IntVar(0, 1, 'C4_path_CAST_call108')
C5_path_CAST_call108 = solver.IntVar(0, 1, 'C5_path_CAST_call108')
C6_path_CAST_call108 = solver.IntVar(0, 1, 'C6_path_CAST_call108')
C7_path_CAST_call108 = solver.IntVar(0, 1, 'C7_path_CAST_call108')
C8_path_CAST_call108 = solver.IntVar(0, 1, 'C8_path_CAST_call108')
solver.Add( + (1)*path_fixp + (1)*path_CAST_call108_float + (-1)*C3_path_CAST_call108<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_path_CAST_call108
solver.Add( + (1)*path_float + (1)*path_CAST_call108_fixp + (-1)*C4_path_CAST_call108<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_path_CAST_call108
solver.Add( + (1)*path_fixp + (1)*path_CAST_call108_double + (-1)*C5_path_CAST_call108<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_path_CAST_call108
solver.Add( + (1)*path_double + (1)*path_CAST_call108_fixp + (-1)*C6_path_CAST_call108<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_path_CAST_call108
solver.Add( + (1)*path_float + (1)*path_CAST_call108_double + (-1)*C7_path_CAST_call108<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_path_CAST_call108
solver.Add( + (1)*path_double + (1)*path_CAST_call108_float + (-1)*C8_path_CAST_call108<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_path_CAST_call108
solver.Add( + (1)*path_CAST_call108_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 218.809+ 1 * enobCostObj / 2814+ 1000 * mathCostObj / 5.44845)

# Model declaration end.