


#Stuff for @_fict_ = common dso_local global [100 x double] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
_fict__fixbits = solver.IntVar(0, 23, '_fict__fixbits')
_fict__fixp = solver.IntVar(0, 1, '_fict__fixp')
_fict__float = solver.IntVar(0, 1, '_fict__float')
_fict__double = solver.IntVar(0, 1, '_fict__double')
_fict__enob = solver.IntVar(-10000, 10000, '_fict__enob')
solver.Add( + (1)*_fict__enob + (-1)*_fict__fixbits + (10000)*_fict__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_fict__enob + (10000)*_fict__float<=10149)    #Enob constraint for float
solver.Add( + (1)*_fict__enob + (10000)*_fict__double<=11074)    #Enob constraint for double
solver.Add( + (1)*_fict__fixbits + (-10000)*_fict__fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*_fict__enob<=333)    #Enob constraint for error maximal
enobCostObj =  + (-1)*_fict__enob
solver.Add( + (1)*_fict__fixp + (1)*_fict__float + (1)*_fict__double==1)    #Exactly one selected type
solver.Add( + (1)*_fict__fixbits + (-10000)*_fict__fixp<=0)    #If not fix, frac part to zero



#Stuff for @ex = common dso_local global [200 x [240 x double]] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
ex_fixbits = solver.IntVar(0, 23, 'ex_fixbits')
ex_fixp = solver.IntVar(0, 1, 'ex_fixp')
ex_float = solver.IntVar(0, 1, 'ex_float')
ex_double = solver.IntVar(0, 1, 'ex_double')
ex_enob = solver.IntVar(-10000, 10000, 'ex_enob')
solver.Add( + (1)*ex_enob + (-1)*ex_fixbits + (10000)*ex_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ex_enob + (10000)*ex_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ex_enob + (10000)*ex_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ex_fixbits + (-10000)*ex_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*ex_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*ex_enob
solver.Add( + (1)*ex_fixp + (1)*ex_float + (1)*ex_double==1)    #Exactly one selected type
solver.Add( + (1)*ex_fixbits + (-10000)*ex_fixp<=0)    #If not fix, frac part to zero



#Stuff for @ey = common dso_local global [200 x [240 x double]] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
ey_fixbits = solver.IntVar(0, 23, 'ey_fixbits')
ey_fixp = solver.IntVar(0, 1, 'ey_fixp')
ey_float = solver.IntVar(0, 1, 'ey_float')
ey_double = solver.IntVar(0, 1, 'ey_double')
ey_enob = solver.IntVar(-10000, 10000, 'ey_enob')
solver.Add( + (1)*ey_enob + (-1)*ey_fixbits + (10000)*ey_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ey_enob + (10000)*ey_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ey_enob + (10000)*ey_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ey_fixbits + (-10000)*ey_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*ey_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*ey_enob
solver.Add( + (1)*ey_fixp + (1)*ey_float + (1)*ey_double==1)    #Exactly one selected type
solver.Add( + (1)*ey_fixbits + (-10000)*ey_fixp<=0)    #If not fix, frac part to zero



#Stuff for @hz = common dso_local global [200 x [240 x double]] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
hz_fixbits = solver.IntVar(0, 23, 'hz_fixbits')
hz_fixp = solver.IntVar(0, 1, 'hz_fixp')
hz_float = solver.IntVar(0, 1, 'hz_float')
hz_double = solver.IntVar(0, 1, 'hz_double')
hz_enob = solver.IntVar(-10000, 10000, 'hz_enob')
solver.Add( + (1)*hz_enob + (-1)*hz_fixbits + (10000)*hz_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*hz_enob + (10000)*hz_float<=10149)    #Enob constraint for float
solver.Add( + (1)*hz_enob + (10000)*hz_double<=11074)    #Enob constraint for double
solver.Add( + (1)*hz_fixbits + (-10000)*hz_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*hz_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*hz_enob
solver.Add( + (1)*hz_fixp + (1)*hz_float + (1)*hz_double==1)    #Exactly one selected type
solver.Add( + (1)*hz_fixbits + (-10000)*hz_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %i.0 to double, !taffo.info !20, !taffo.initweight !21
main_conv_fixbits = solver.IntVar(0, 23, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   store double %conv, double* %arrayidx, align 8, !taffo.info !24, !taffo.initweight !21
main_conv_CAST_store_fixbits = solver.IntVar(0, 23, 'main_conv_CAST_store_fixbits')
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
solver.Add( + (1)*_fict__fixp + (-1)*main_conv_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*_fict__float + (-1)*main_conv_CAST_store_float==0)    #float equality
solver.Add( + (1)*_fict__double + (-1)*main_conv_CAST_store_double==0)    #double equality
solver.Add( + (1)*_fict__fixbits + (-1)*main_conv_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
_fict__enob_storeENOB = solver.IntVar(-10000, 10000, '_fict__enob_storeENOB')
solver.Add( + (1)*_fict__enob_storeENOB + (-1)*_fict__fixbits + (10000)*_fict__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_fict__enob_storeENOB + (10000)*_fict__float<=10149)    #Enob constraint for float
solver.Add( + (1)*_fict__enob_storeENOB + (10000)*_fict__double<=11074)    #Enob constraint for double
solver.Add( + (1)*_fict__enob_storeENOB + (-1)*main_conv_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv12 = sitofp i32 %i.1 to double, !taffo.info !20, !taffo.initweight !21
main_conv12_fixbits = solver.IntVar(0, 23, 'main_conv12_fixbits')
main_conv12_fixp = solver.IntVar(0, 1, 'main_conv12_fixp')
main_conv12_float = solver.IntVar(0, 1, 'main_conv12_float')
main_conv12_double = solver.IntVar(0, 1, 'main_conv12_double')
main_conv12_enob = solver.IntVar(-10000, 10000, 'main_conv12_enob')
solver.Add( + (1)*main_conv12_enob + (-1)*main_conv12_fixbits + (10000)*main_conv12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv12_enob + (10000)*main_conv12_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv12_enob + (10000)*main_conv12_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv12_fixbits + (-10000)*main_conv12_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv12_enob
solver.Add( + (1)*main_conv12_fixp + (1)*main_conv12_float + (1)*main_conv12_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv12_fixbits + (-10000)*main_conv12_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv12_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv13 = sitofp i32 %add to double, !taffo.info !28, !taffo.initweight !22
main_conv13_fixbits = solver.IntVar(0, 23, 'main_conv13_fixbits')
main_conv13_fixp = solver.IntVar(0, 1, 'main_conv13_fixp')
main_conv13_float = solver.IntVar(0, 1, 'main_conv13_float')
main_conv13_double = solver.IntVar(0, 1, 'main_conv13_double')
main_conv13_enob = solver.IntVar(-10000, 10000, 'main_conv13_enob')
solver.Add( + (1)*main_conv13_enob + (-1)*main_conv13_fixbits + (10000)*main_conv13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv13_enob + (10000)*main_conv13_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv13_enob + (10000)*main_conv13_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv13_fixbits + (-10000)*main_conv13_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv13_enob
solver.Add( + (1)*main_conv13_fixp + (1)*main_conv13_float + (1)*main_conv13_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv13_fixbits + (-10000)*main_conv13_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv13_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %mul = fmul double %conv12, %conv13, !taffo.info !29, !taffo.initweight !22
main_conv12_CAST_mul_fixbits = solver.IntVar(0, 23, 'main_conv12_CAST_mul_fixbits')
main_conv12_CAST_mul_fixp = solver.IntVar(0, 1, 'main_conv12_CAST_mul_fixp')
main_conv12_CAST_mul_float = solver.IntVar(0, 1, 'main_conv12_CAST_mul_float')
main_conv12_CAST_mul_double = solver.IntVar(0, 1, 'main_conv12_CAST_mul_double')
solver.Add( + (1)*main_conv12_CAST_mul_fixp + (1)*main_conv12_CAST_mul_float + (1)*main_conv12_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv12_CAST_mul_fixbits + (-10000)*main_conv12_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C1_main_conv12_CAST_mul')
C2_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C2_main_conv12_CAST_mul')
solver.Add( + (1)*main_conv12_fixbits + (-1)*main_conv12_CAST_mul_fixbits + (-10000)*C1_main_conv12_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv12_fixbits + (1)*main_conv12_CAST_mul_fixbits + (-10000)*C2_main_conv12_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv12_CAST_mul
castCostObj +=  + (1)*C2_main_conv12_CAST_mul
C3_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C3_main_conv12_CAST_mul')
C4_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C4_main_conv12_CAST_mul')
C5_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C5_main_conv12_CAST_mul')
C6_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C6_main_conv12_CAST_mul')
C7_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C7_main_conv12_CAST_mul')
C8_main_conv12_CAST_mul = solver.IntVar(0, 1, 'C8_main_conv12_CAST_mul')
solver.Add( + (1)*main_conv12_fixp + (1)*main_conv12_CAST_mul_float + (-1)*C3_main_conv12_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv12_CAST_mul
solver.Add( + (1)*main_conv12_float + (1)*main_conv12_CAST_mul_fixp + (-1)*C4_main_conv12_CAST_mul<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv12_CAST_mul
solver.Add( + (1)*main_conv12_fixp + (1)*main_conv12_CAST_mul_double + (-1)*C5_main_conv12_CAST_mul<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv12_CAST_mul
solver.Add( + (1)*main_conv12_double + (1)*main_conv12_CAST_mul_fixp + (-1)*C6_main_conv12_CAST_mul<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv12_CAST_mul
solver.Add( + (1)*main_conv12_float + (1)*main_conv12_CAST_mul_double + (-1)*C7_main_conv12_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv12_CAST_mul
solver.Add( + (1)*main_conv12_double + (1)*main_conv12_CAST_mul_float + (-1)*C8_main_conv12_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv12_CAST_mul



#Constraint for cast for   %mul = fmul double %conv12, %conv13, !taffo.info !29, !taffo.initweight !22
main_conv13_CAST_mul_fixbits = solver.IntVar(0, 23, 'main_conv13_CAST_mul_fixbits')
main_conv13_CAST_mul_fixp = solver.IntVar(0, 1, 'main_conv13_CAST_mul_fixp')
main_conv13_CAST_mul_float = solver.IntVar(0, 1, 'main_conv13_CAST_mul_float')
main_conv13_CAST_mul_double = solver.IntVar(0, 1, 'main_conv13_CAST_mul_double')
solver.Add( + (1)*main_conv13_CAST_mul_fixp + (1)*main_conv13_CAST_mul_float + (1)*main_conv13_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv13_CAST_mul_fixbits + (-10000)*main_conv13_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C1_main_conv13_CAST_mul')
C2_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C2_main_conv13_CAST_mul')
solver.Add( + (1)*main_conv13_fixbits + (-1)*main_conv13_CAST_mul_fixbits + (-10000)*C1_main_conv13_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv13_fixbits + (1)*main_conv13_CAST_mul_fixbits + (-10000)*C2_main_conv13_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv13_CAST_mul
castCostObj +=  + (1)*C2_main_conv13_CAST_mul
C3_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C3_main_conv13_CAST_mul')
C4_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C4_main_conv13_CAST_mul')
C5_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C5_main_conv13_CAST_mul')
C6_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C6_main_conv13_CAST_mul')
C7_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C7_main_conv13_CAST_mul')
C8_main_conv13_CAST_mul = solver.IntVar(0, 1, 'C8_main_conv13_CAST_mul')
solver.Add( + (1)*main_conv13_fixp + (1)*main_conv13_CAST_mul_float + (-1)*C3_main_conv13_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv13_CAST_mul
solver.Add( + (1)*main_conv13_float + (1)*main_conv13_CAST_mul_fixp + (-1)*C4_main_conv13_CAST_mul<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv13_CAST_mul
solver.Add( + (1)*main_conv13_fixp + (1)*main_conv13_CAST_mul_double + (-1)*C5_main_conv13_CAST_mul<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv13_CAST_mul
solver.Add( + (1)*main_conv13_double + (1)*main_conv13_CAST_mul_fixp + (-1)*C6_main_conv13_CAST_mul<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv13_CAST_mul
solver.Add( + (1)*main_conv13_float + (1)*main_conv13_CAST_mul_double + (-1)*C7_main_conv13_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv13_CAST_mul
solver.Add( + (1)*main_conv13_double + (1)*main_conv13_CAST_mul_float + (-1)*C8_main_conv13_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv13_CAST_mul



#Stuff for   %mul = fmul double %conv12, %conv13, !taffo.info !29, !taffo.initweight !22
main_mul_fixbits = solver.IntVar(0, 15, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj +=  + (-1)*main_mul_enob
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv12_CAST_mul_fixp + (-1)*main_conv13_CAST_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_conv12_CAST_mul_float + (-1)*main_conv13_CAST_mul_float==0)    #float equality
solver.Add( + (1)*main_conv12_CAST_mul_double + (-1)*main_conv13_CAST_mul_double==0)    #double equality
solver.Add( + (1)*main_conv12_CAST_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_conv12_CAST_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*main_conv12_CAST_mul_double + (-1)*main_mul_double==0)    #double equality
mathCostObj =  + (1.62391)*main_mul_fixp
mathCostObj +=  + (2.64722)*main_mul_float
mathCostObj +=  + (4.02255)*main_mul_double
main_main_mul_enob_1 = solver.IntVar(0, 1, 'main_main_mul_enob_1')
main_main_mul_enob_2 = solver.IntVar(0, 1, 'main_main_mul_enob_2')
solver.Add( + (1)*main_main_mul_enob_1 + (1)*main_main_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul_enob + (-1)*main_conv13_enob + (-10000)*main_main_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul_enob + (-1)*main_conv12_enob + (-10000)*main_main_mul_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for   %conv14 = sitofp i32 200 to double, !taffo.info !31
main_conv14_fixbits = solver.IntVar(0, 24, 'main_conv14_fixbits')
main_conv14_fixp = solver.IntVar(0, 1, 'main_conv14_fixp')
main_conv14_float = solver.IntVar(0, 1, 'main_conv14_float')
main_conv14_double = solver.IntVar(0, 1, 'main_conv14_double')
main_conv14_enob = solver.IntVar(-10000, 10000, 'main_conv14_enob')
solver.Add( + (1)*main_conv14_enob + (-1)*main_conv14_fixbits + (10000)*main_conv14_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv14_enob + (10000)*main_conv14_float<=10016)    #Enob constraint for float
solver.Add( + (1)*main_conv14_enob + (10000)*main_conv14_double<=10045)    #Enob constraint for double
solver.Add( + (1)*main_conv14_fixbits + (-10000)*main_conv14_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*main_conv14_enob
solver.Add( + (1)*main_conv14_fixp + (1)*main_conv14_float + (1)*main_conv14_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv14_fixbits + (-10000)*main_conv14_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv14_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div = fdiv double %mul, %conv14, !taffo.info !28, !taffo.initweight !33
main_mul_CAST_div_fixbits = solver.IntVar(0, 15, 'main_mul_CAST_div_fixbits')
main_mul_CAST_div_fixp = solver.IntVar(0, 1, 'main_mul_CAST_div_fixp')
main_mul_CAST_div_float = solver.IntVar(0, 1, 'main_mul_CAST_div_float')
main_mul_CAST_div_double = solver.IntVar(0, 1, 'main_mul_CAST_div_double')
solver.Add( + (1)*main_mul_CAST_div_fixp + (1)*main_mul_CAST_div_float + (1)*main_mul_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul_CAST_div_fixbits + (-10000)*main_mul_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul_CAST_div = solver.IntVar(0, 1, 'C1_main_mul_CAST_div')
C2_main_mul_CAST_div = solver.IntVar(0, 1, 'C2_main_mul_CAST_div')
solver.Add( + (1)*main_mul_fixbits + (-1)*main_mul_CAST_div_fixbits + (-10000)*C1_main_mul_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul_fixbits + (1)*main_mul_CAST_div_fixbits + (-10000)*C2_main_mul_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul_CAST_div
castCostObj +=  + (1)*C2_main_mul_CAST_div
C3_main_mul_CAST_div = solver.IntVar(0, 1, 'C3_main_mul_CAST_div')
C4_main_mul_CAST_div = solver.IntVar(0, 1, 'C4_main_mul_CAST_div')
C5_main_mul_CAST_div = solver.IntVar(0, 1, 'C5_main_mul_CAST_div')
C6_main_mul_CAST_div = solver.IntVar(0, 1, 'C6_main_mul_CAST_div')
C7_main_mul_CAST_div = solver.IntVar(0, 1, 'C7_main_mul_CAST_div')
C8_main_mul_CAST_div = solver.IntVar(0, 1, 'C8_main_mul_CAST_div')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_div_float + (-1)*C3_main_mul_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul_CAST_div
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_div_fixp + (-1)*C4_main_mul_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul_CAST_div
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_div_double + (-1)*C5_main_mul_CAST_div<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul_CAST_div
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_div_fixp + (-1)*C6_main_mul_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul_CAST_div
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_div_double + (-1)*C7_main_mul_CAST_div<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul_CAST_div
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_div_float + (-1)*C8_main_mul_CAST_div<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul_CAST_div



#Constraint for cast for   %div = fdiv double %mul, %conv14, !taffo.info !28, !taffo.initweight !33
main_conv14_CAST_div_fixbits = solver.IntVar(0, 24, 'main_conv14_CAST_div_fixbits')
main_conv14_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv14_CAST_div_fixp')
main_conv14_CAST_div_float = solver.IntVar(0, 1, 'main_conv14_CAST_div_float')
main_conv14_CAST_div_double = solver.IntVar(0, 1, 'main_conv14_CAST_div_double')
solver.Add( + (1)*main_conv14_CAST_div_fixp + (1)*main_conv14_CAST_div_float + (1)*main_conv14_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv14_CAST_div_fixbits + (-10000)*main_conv14_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv14_CAST_div = solver.IntVar(0, 1, 'C1_main_conv14_CAST_div')
C2_main_conv14_CAST_div = solver.IntVar(0, 1, 'C2_main_conv14_CAST_div')
solver.Add( + (1)*main_conv14_fixbits + (-1)*main_conv14_CAST_div_fixbits + (-10000)*C1_main_conv14_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv14_fixbits + (1)*main_conv14_CAST_div_fixbits + (-10000)*C2_main_conv14_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv14_CAST_div
castCostObj +=  + (1)*C2_main_conv14_CAST_div
C3_main_conv14_CAST_div = solver.IntVar(0, 1, 'C3_main_conv14_CAST_div')
C4_main_conv14_CAST_div = solver.IntVar(0, 1, 'C4_main_conv14_CAST_div')
C5_main_conv14_CAST_div = solver.IntVar(0, 1, 'C5_main_conv14_CAST_div')
C6_main_conv14_CAST_div = solver.IntVar(0, 1, 'C6_main_conv14_CAST_div')
C7_main_conv14_CAST_div = solver.IntVar(0, 1, 'C7_main_conv14_CAST_div')
C8_main_conv14_CAST_div = solver.IntVar(0, 1, 'C8_main_conv14_CAST_div')
solver.Add( + (1)*main_conv14_fixp + (1)*main_conv14_CAST_div_float + (-1)*C3_main_conv14_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv14_CAST_div
solver.Add( + (1)*main_conv14_float + (1)*main_conv14_CAST_div_fixp + (-1)*C4_main_conv14_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv14_CAST_div
solver.Add( + (1)*main_conv14_fixp + (1)*main_conv14_CAST_div_double + (-1)*C5_main_conv14_CAST_div<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv14_CAST_div
solver.Add( + (1)*main_conv14_double + (1)*main_conv14_CAST_div_fixp + (-1)*C6_main_conv14_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv14_CAST_div
solver.Add( + (1)*main_conv14_float + (1)*main_conv14_CAST_div_double + (-1)*C7_main_conv14_CAST_div<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv14_CAST_div
solver.Add( + (1)*main_conv14_double + (1)*main_conv14_CAST_div_float + (-1)*C8_main_conv14_CAST_div<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv14_CAST_div



#Stuff for   %div = fdiv double %mul, %conv14, !taffo.info !28, !taffo.initweight !33
main_div_fixbits = solver.IntVar(0, 23, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul_CAST_div_fixp + (-1)*main_conv14_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div_float + (-1)*main_conv14_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div_double + (-1)*main_conv14_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_mul_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div_fixp
mathCostObj +=  + (5.60026)*main_div_float
mathCostObj +=  + (18.3266)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*main_conv14_enob + (-10000)*main_main_div_enob_1<=1040)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_mul_enob + (-10000)*main_main_div_enob_2<=8)    #Enob: propagation in division 2



#Constraint for cast for   store double %div, double* %arrayidx18, align 8, !taffo.info !12, !taffo.initweight !22
main_div_CAST_store_fixbits = solver.IntVar(0, 23, 'main_div_CAST_store_fixbits')
main_div_CAST_store_fixp = solver.IntVar(0, 1, 'main_div_CAST_store_fixp')
main_div_CAST_store_float = solver.IntVar(0, 1, 'main_div_CAST_store_float')
main_div_CAST_store_double = solver.IntVar(0, 1, 'main_div_CAST_store_double')
solver.Add( + (1)*main_div_CAST_store_fixp + (1)*main_div_CAST_store_float + (1)*main_div_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div_CAST_store_fixbits + (-10000)*main_div_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div_CAST_store = solver.IntVar(0, 1, 'C1_main_div_CAST_store')
C2_main_div_CAST_store = solver.IntVar(0, 1, 'C2_main_div_CAST_store')
solver.Add( + (1)*main_div_fixbits + (-1)*main_div_CAST_store_fixbits + (-10000)*C1_main_div_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div_fixbits + (1)*main_div_CAST_store_fixbits + (-10000)*C2_main_div_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div_CAST_store
castCostObj +=  + (1)*C2_main_div_CAST_store
C3_main_div_CAST_store = solver.IntVar(0, 1, 'C3_main_div_CAST_store')
C4_main_div_CAST_store = solver.IntVar(0, 1, 'C4_main_div_CAST_store')
C5_main_div_CAST_store = solver.IntVar(0, 1, 'C5_main_div_CAST_store')
C6_main_div_CAST_store = solver.IntVar(0, 1, 'C6_main_div_CAST_store')
C7_main_div_CAST_store = solver.IntVar(0, 1, 'C7_main_div_CAST_store')
C8_main_div_CAST_store = solver.IntVar(0, 1, 'C8_main_div_CAST_store')
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_float + (-1)*C3_main_div_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_fixp + (-1)*C4_main_div_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div_CAST_store
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_double + (-1)*C5_main_div_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_fixp + (-1)*C6_main_div_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_double + (-1)*C7_main_div_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_float + (-1)*C8_main_div_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div_CAST_store
solver.Add( + (1)*ex_fixp + (-1)*main_div_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*ex_float + (-1)*main_div_CAST_store_float==0)    #float equality
solver.Add( + (1)*ex_double + (-1)*main_div_CAST_store_double==0)    #double equality
solver.Add( + (1)*ex_fixbits + (-1)*main_div_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
ex_enob_storeENOB = solver.IntVar(-10000, 10000, 'ex_enob_storeENOB')
solver.Add( + (1)*ex_enob_storeENOB + (-1)*ex_fixbits + (10000)*ex_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ex_enob_storeENOB + (10000)*ex_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ex_enob_storeENOB + (10000)*ex_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ex_enob_storeENOB + (-1)*main_div_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv19 = sitofp i32 %i.1 to double, !taffo.info !20, !taffo.initweight !21
main_conv19_fixbits = solver.IntVar(0, 23, 'main_conv19_fixbits')
main_conv19_fixp = solver.IntVar(0, 1, 'main_conv19_fixp')
main_conv19_float = solver.IntVar(0, 1, 'main_conv19_float')
main_conv19_double = solver.IntVar(0, 1, 'main_conv19_double')
main_conv19_enob = solver.IntVar(-10000, 10000, 'main_conv19_enob')
solver.Add( + (1)*main_conv19_enob + (-1)*main_conv19_fixbits + (10000)*main_conv19_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv19_enob + (10000)*main_conv19_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv19_enob + (10000)*main_conv19_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv19_fixbits + (-10000)*main_conv19_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv19_enob
solver.Add( + (1)*main_conv19_fixp + (1)*main_conv19_float + (1)*main_conv19_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv19_fixbits + (-10000)*main_conv19_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv19_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv21 = sitofp i32 %add20 to double, !taffo.info !28, !taffo.initweight !22
main_conv21_fixbits = solver.IntVar(0, 23, 'main_conv21_fixbits')
main_conv21_fixp = solver.IntVar(0, 1, 'main_conv21_fixp')
main_conv21_float = solver.IntVar(0, 1, 'main_conv21_float')
main_conv21_double = solver.IntVar(0, 1, 'main_conv21_double')
main_conv21_enob = solver.IntVar(-10000, 10000, 'main_conv21_enob')
solver.Add( + (1)*main_conv21_enob + (-1)*main_conv21_fixbits + (10000)*main_conv21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv21_enob + (10000)*main_conv21_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv21_enob + (10000)*main_conv21_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv21_fixbits + (-10000)*main_conv21_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv21_enob
solver.Add( + (1)*main_conv21_fixp + (1)*main_conv21_float + (1)*main_conv21_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv21_fixbits + (-10000)*main_conv21_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv21_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %mul22 = fmul double %conv19, %conv21, !taffo.info !29, !taffo.initweight !22
main_conv19_CAST_mul22_fixbits = solver.IntVar(0, 23, 'main_conv19_CAST_mul22_fixbits')
main_conv19_CAST_mul22_fixp = solver.IntVar(0, 1, 'main_conv19_CAST_mul22_fixp')
main_conv19_CAST_mul22_float = solver.IntVar(0, 1, 'main_conv19_CAST_mul22_float')
main_conv19_CAST_mul22_double = solver.IntVar(0, 1, 'main_conv19_CAST_mul22_double')
solver.Add( + (1)*main_conv19_CAST_mul22_fixp + (1)*main_conv19_CAST_mul22_float + (1)*main_conv19_CAST_mul22_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv19_CAST_mul22_fixbits + (-10000)*main_conv19_CAST_mul22_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C1_main_conv19_CAST_mul22')
C2_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C2_main_conv19_CAST_mul22')
solver.Add( + (1)*main_conv19_fixbits + (-1)*main_conv19_CAST_mul22_fixbits + (-10000)*C1_main_conv19_CAST_mul22<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv19_fixbits + (1)*main_conv19_CAST_mul22_fixbits + (-10000)*C2_main_conv19_CAST_mul22<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv19_CAST_mul22
castCostObj +=  + (1)*C2_main_conv19_CAST_mul22
C3_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C3_main_conv19_CAST_mul22')
C4_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C4_main_conv19_CAST_mul22')
C5_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C5_main_conv19_CAST_mul22')
C6_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C6_main_conv19_CAST_mul22')
C7_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C7_main_conv19_CAST_mul22')
C8_main_conv19_CAST_mul22 = solver.IntVar(0, 1, 'C8_main_conv19_CAST_mul22')
solver.Add( + (1)*main_conv19_fixp + (1)*main_conv19_CAST_mul22_float + (-1)*C3_main_conv19_CAST_mul22<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv19_CAST_mul22
solver.Add( + (1)*main_conv19_float + (1)*main_conv19_CAST_mul22_fixp + (-1)*C4_main_conv19_CAST_mul22<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv19_CAST_mul22
solver.Add( + (1)*main_conv19_fixp + (1)*main_conv19_CAST_mul22_double + (-1)*C5_main_conv19_CAST_mul22<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv19_CAST_mul22
solver.Add( + (1)*main_conv19_double + (1)*main_conv19_CAST_mul22_fixp + (-1)*C6_main_conv19_CAST_mul22<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv19_CAST_mul22
solver.Add( + (1)*main_conv19_float + (1)*main_conv19_CAST_mul22_double + (-1)*C7_main_conv19_CAST_mul22<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv19_CAST_mul22
solver.Add( + (1)*main_conv19_double + (1)*main_conv19_CAST_mul22_float + (-1)*C8_main_conv19_CAST_mul22<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv19_CAST_mul22



#Constraint for cast for   %mul22 = fmul double %conv19, %conv21, !taffo.info !29, !taffo.initweight !22
main_conv21_CAST_mul22_fixbits = solver.IntVar(0, 23, 'main_conv21_CAST_mul22_fixbits')
main_conv21_CAST_mul22_fixp = solver.IntVar(0, 1, 'main_conv21_CAST_mul22_fixp')
main_conv21_CAST_mul22_float = solver.IntVar(0, 1, 'main_conv21_CAST_mul22_float')
main_conv21_CAST_mul22_double = solver.IntVar(0, 1, 'main_conv21_CAST_mul22_double')
solver.Add( + (1)*main_conv21_CAST_mul22_fixp + (1)*main_conv21_CAST_mul22_float + (1)*main_conv21_CAST_mul22_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv21_CAST_mul22_fixbits + (-10000)*main_conv21_CAST_mul22_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C1_main_conv21_CAST_mul22')
C2_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C2_main_conv21_CAST_mul22')
solver.Add( + (1)*main_conv21_fixbits + (-1)*main_conv21_CAST_mul22_fixbits + (-10000)*C1_main_conv21_CAST_mul22<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv21_fixbits + (1)*main_conv21_CAST_mul22_fixbits + (-10000)*C2_main_conv21_CAST_mul22<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv21_CAST_mul22
castCostObj +=  + (1)*C2_main_conv21_CAST_mul22
C3_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C3_main_conv21_CAST_mul22')
C4_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C4_main_conv21_CAST_mul22')
C5_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C5_main_conv21_CAST_mul22')
C6_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C6_main_conv21_CAST_mul22')
C7_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C7_main_conv21_CAST_mul22')
C8_main_conv21_CAST_mul22 = solver.IntVar(0, 1, 'C8_main_conv21_CAST_mul22')
solver.Add( + (1)*main_conv21_fixp + (1)*main_conv21_CAST_mul22_float + (-1)*C3_main_conv21_CAST_mul22<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv21_CAST_mul22
solver.Add( + (1)*main_conv21_float + (1)*main_conv21_CAST_mul22_fixp + (-1)*C4_main_conv21_CAST_mul22<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv21_CAST_mul22
solver.Add( + (1)*main_conv21_fixp + (1)*main_conv21_CAST_mul22_double + (-1)*C5_main_conv21_CAST_mul22<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv21_CAST_mul22
solver.Add( + (1)*main_conv21_double + (1)*main_conv21_CAST_mul22_fixp + (-1)*C6_main_conv21_CAST_mul22<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv21_CAST_mul22
solver.Add( + (1)*main_conv21_float + (1)*main_conv21_CAST_mul22_double + (-1)*C7_main_conv21_CAST_mul22<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv21_CAST_mul22
solver.Add( + (1)*main_conv21_double + (1)*main_conv21_CAST_mul22_float + (-1)*C8_main_conv21_CAST_mul22<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv21_CAST_mul22



#Stuff for   %mul22 = fmul double %conv19, %conv21, !taffo.info !29, !taffo.initweight !22
main_mul22_fixbits = solver.IntVar(0, 15, 'main_mul22_fixbits')
main_mul22_fixp = solver.IntVar(0, 1, 'main_mul22_fixp')
main_mul22_float = solver.IntVar(0, 1, 'main_mul22_float')
main_mul22_double = solver.IntVar(0, 1, 'main_mul22_double')
main_mul22_enob = solver.IntVar(-10000, 10000, 'main_mul22_enob')
solver.Add( + (1)*main_mul22_enob + (-1)*main_mul22_fixbits + (10000)*main_mul22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul22_enob + (10000)*main_mul22_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul22_enob + (10000)*main_mul22_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul22_fixbits + (-10000)*main_mul22_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj +=  + (-1)*main_mul22_enob
solver.Add( + (1)*main_mul22_fixp + (1)*main_mul22_float + (1)*main_mul22_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul22_fixbits + (-10000)*main_mul22_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv19_CAST_mul22_fixp + (-1)*main_conv21_CAST_mul22_fixp==0)    #fix equality
solver.Add( + (1)*main_conv19_CAST_mul22_float + (-1)*main_conv21_CAST_mul22_float==0)    #float equality
solver.Add( + (1)*main_conv19_CAST_mul22_double + (-1)*main_conv21_CAST_mul22_double==0)    #double equality
solver.Add( + (1)*main_conv19_CAST_mul22_fixp + (-1)*main_mul22_fixp==0)    #fix equality
solver.Add( + (1)*main_conv19_CAST_mul22_float + (-1)*main_mul22_float==0)    #float equality
solver.Add( + (1)*main_conv19_CAST_mul22_double + (-1)*main_mul22_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul22_fixp
mathCostObj +=  + (2.64722)*main_mul22_float
mathCostObj +=  + (4.02255)*main_mul22_double
main_main_mul22_enob_1 = solver.IntVar(0, 1, 'main_main_mul22_enob_1')
main_main_mul22_enob_2 = solver.IntVar(0, 1, 'main_main_mul22_enob_2')
solver.Add( + (1)*main_main_mul22_enob_1 + (1)*main_main_mul22_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul22_enob + (-1)*main_conv21_enob + (-10000)*main_main_mul22_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul22_enob + (-1)*main_conv19_enob + (-10000)*main_main_mul22_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for   %conv23 = sitofp i32 240 to double, !taffo.info !34
main_conv23_fixbits = solver.IntVar(0, 24, 'main_conv23_fixbits')
main_conv23_fixp = solver.IntVar(0, 1, 'main_conv23_fixp')
main_conv23_float = solver.IntVar(0, 1, 'main_conv23_float')
main_conv23_double = solver.IntVar(0, 1, 'main_conv23_double')
main_conv23_enob = solver.IntVar(-10000, 10000, 'main_conv23_enob')
solver.Add( + (1)*main_conv23_enob + (-1)*main_conv23_fixbits + (10000)*main_conv23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv23_enob + (10000)*main_conv23_float<=10016)    #Enob constraint for float
solver.Add( + (1)*main_conv23_enob + (10000)*main_conv23_double<=10045)    #Enob constraint for double
solver.Add( + (1)*main_conv23_fixbits + (-10000)*main_conv23_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*main_conv23_enob
solver.Add( + (1)*main_conv23_fixp + (1)*main_conv23_float + (1)*main_conv23_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv23_fixbits + (-10000)*main_conv23_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv23_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div24 = fdiv double %mul22, %conv23, !taffo.info !20, !taffo.initweight !33
main_mul22_CAST_div24_fixbits = solver.IntVar(0, 15, 'main_mul22_CAST_div24_fixbits')
main_mul22_CAST_div24_fixp = solver.IntVar(0, 1, 'main_mul22_CAST_div24_fixp')
main_mul22_CAST_div24_float = solver.IntVar(0, 1, 'main_mul22_CAST_div24_float')
main_mul22_CAST_div24_double = solver.IntVar(0, 1, 'main_mul22_CAST_div24_double')
solver.Add( + (1)*main_mul22_CAST_div24_fixp + (1)*main_mul22_CAST_div24_float + (1)*main_mul22_CAST_div24_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul22_CAST_div24_fixbits + (-10000)*main_mul22_CAST_div24_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C1_main_mul22_CAST_div24')
C2_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C2_main_mul22_CAST_div24')
solver.Add( + (1)*main_mul22_fixbits + (-1)*main_mul22_CAST_div24_fixbits + (-10000)*C1_main_mul22_CAST_div24<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul22_fixbits + (1)*main_mul22_CAST_div24_fixbits + (-10000)*C2_main_mul22_CAST_div24<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul22_CAST_div24
castCostObj +=  + (1)*C2_main_mul22_CAST_div24
C3_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C3_main_mul22_CAST_div24')
C4_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C4_main_mul22_CAST_div24')
C5_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C5_main_mul22_CAST_div24')
C6_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C6_main_mul22_CAST_div24')
C7_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C7_main_mul22_CAST_div24')
C8_main_mul22_CAST_div24 = solver.IntVar(0, 1, 'C8_main_mul22_CAST_div24')
solver.Add( + (1)*main_mul22_fixp + (1)*main_mul22_CAST_div24_float + (-1)*C3_main_mul22_CAST_div24<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul22_CAST_div24
solver.Add( + (1)*main_mul22_float + (1)*main_mul22_CAST_div24_fixp + (-1)*C4_main_mul22_CAST_div24<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul22_CAST_div24
solver.Add( + (1)*main_mul22_fixp + (1)*main_mul22_CAST_div24_double + (-1)*C5_main_mul22_CAST_div24<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul22_CAST_div24
solver.Add( + (1)*main_mul22_double + (1)*main_mul22_CAST_div24_fixp + (-1)*C6_main_mul22_CAST_div24<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul22_CAST_div24
solver.Add( + (1)*main_mul22_float + (1)*main_mul22_CAST_div24_double + (-1)*C7_main_mul22_CAST_div24<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul22_CAST_div24
solver.Add( + (1)*main_mul22_double + (1)*main_mul22_CAST_div24_float + (-1)*C8_main_mul22_CAST_div24<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul22_CAST_div24



#Constraint for cast for   %div24 = fdiv double %mul22, %conv23, !taffo.info !20, !taffo.initweight !33
main_conv23_CAST_div24_fixbits = solver.IntVar(0, 24, 'main_conv23_CAST_div24_fixbits')
main_conv23_CAST_div24_fixp = solver.IntVar(0, 1, 'main_conv23_CAST_div24_fixp')
main_conv23_CAST_div24_float = solver.IntVar(0, 1, 'main_conv23_CAST_div24_float')
main_conv23_CAST_div24_double = solver.IntVar(0, 1, 'main_conv23_CAST_div24_double')
solver.Add( + (1)*main_conv23_CAST_div24_fixp + (1)*main_conv23_CAST_div24_float + (1)*main_conv23_CAST_div24_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv23_CAST_div24_fixbits + (-10000)*main_conv23_CAST_div24_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C1_main_conv23_CAST_div24')
C2_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C2_main_conv23_CAST_div24')
solver.Add( + (1)*main_conv23_fixbits + (-1)*main_conv23_CAST_div24_fixbits + (-10000)*C1_main_conv23_CAST_div24<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv23_fixbits + (1)*main_conv23_CAST_div24_fixbits + (-10000)*C2_main_conv23_CAST_div24<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv23_CAST_div24
castCostObj +=  + (1)*C2_main_conv23_CAST_div24
C3_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C3_main_conv23_CAST_div24')
C4_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C4_main_conv23_CAST_div24')
C5_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C5_main_conv23_CAST_div24')
C6_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C6_main_conv23_CAST_div24')
C7_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C7_main_conv23_CAST_div24')
C8_main_conv23_CAST_div24 = solver.IntVar(0, 1, 'C8_main_conv23_CAST_div24')
solver.Add( + (1)*main_conv23_fixp + (1)*main_conv23_CAST_div24_float + (-1)*C3_main_conv23_CAST_div24<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv23_CAST_div24
solver.Add( + (1)*main_conv23_float + (1)*main_conv23_CAST_div24_fixp + (-1)*C4_main_conv23_CAST_div24<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv23_CAST_div24
solver.Add( + (1)*main_conv23_fixp + (1)*main_conv23_CAST_div24_double + (-1)*C5_main_conv23_CAST_div24<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv23_CAST_div24
solver.Add( + (1)*main_conv23_double + (1)*main_conv23_CAST_div24_fixp + (-1)*C6_main_conv23_CAST_div24<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv23_CAST_div24
solver.Add( + (1)*main_conv23_float + (1)*main_conv23_CAST_div24_double + (-1)*C7_main_conv23_CAST_div24<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv23_CAST_div24
solver.Add( + (1)*main_conv23_double + (1)*main_conv23_CAST_div24_float + (-1)*C8_main_conv23_CAST_div24<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv23_CAST_div24



#Stuff for   %div24 = fdiv double %mul22, %conv23, !taffo.info !20, !taffo.initweight !33
main_div24_fixbits = solver.IntVar(0, 23, 'main_div24_fixbits')
main_div24_fixp = solver.IntVar(0, 1, 'main_div24_fixp')
main_div24_float = solver.IntVar(0, 1, 'main_div24_float')
main_div24_double = solver.IntVar(0, 1, 'main_div24_double')
main_div24_enob = solver.IntVar(-10000, 10000, 'main_div24_enob')
solver.Add( + (1)*main_div24_enob + (-1)*main_div24_fixbits + (10000)*main_div24_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div24_enob + (10000)*main_div24_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div24_enob + (10000)*main_div24_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div24_fixbits + (-10000)*main_div24_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_div24_enob
solver.Add( + (1)*main_div24_fixp + (1)*main_div24_float + (1)*main_div24_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div24_fixbits + (-10000)*main_div24_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul22_CAST_div24_fixp + (-1)*main_conv23_CAST_div24_fixp==0)    #fix equality
solver.Add( + (1)*main_mul22_CAST_div24_float + (-1)*main_conv23_CAST_div24_float==0)    #float equality
solver.Add( + (1)*main_mul22_CAST_div24_double + (-1)*main_conv23_CAST_div24_double==0)    #double equality
solver.Add( + (1)*main_mul22_CAST_div24_fixp + (-1)*main_div24_fixp==0)    #fix equality
solver.Add( + (1)*main_mul22_CAST_div24_float + (-1)*main_div24_float==0)    #float equality
solver.Add( + (1)*main_mul22_CAST_div24_double + (-1)*main_div24_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div24_fixp
mathCostObj +=  + (5.60026)*main_div24_float
mathCostObj +=  + (18.3266)*main_div24_double
main_main_div24_enob_1 = solver.IntVar(0, 1, 'main_main_div24_enob_1')
main_main_div24_enob_2 = solver.IntVar(0, 1, 'main_main_div24_enob_2')
solver.Add( + (1)*main_main_div24_enob_1 + (1)*main_main_div24_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div24_enob + (-1)*main_conv23_enob + (-10000)*main_main_div24_enob_1<=1040)    #Enob: propagation in division 1
solver.Add( + (1)*main_div24_enob + (-1)*main_mul22_enob + (-10000)*main_main_div24_enob_2<=8)    #Enob: propagation in division 2



#Constraint for cast for   store double %div24, double* %arrayidx28, align 8, !taffo.info !12, !taffo.initweight !22
main_div24_CAST_store_fixbits = solver.IntVar(0, 23, 'main_div24_CAST_store_fixbits')
main_div24_CAST_store_fixp = solver.IntVar(0, 1, 'main_div24_CAST_store_fixp')
main_div24_CAST_store_float = solver.IntVar(0, 1, 'main_div24_CAST_store_float')
main_div24_CAST_store_double = solver.IntVar(0, 1, 'main_div24_CAST_store_double')
solver.Add( + (1)*main_div24_CAST_store_fixp + (1)*main_div24_CAST_store_float + (1)*main_div24_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div24_CAST_store_fixbits + (-10000)*main_div24_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div24_CAST_store = solver.IntVar(0, 1, 'C1_main_div24_CAST_store')
C2_main_div24_CAST_store = solver.IntVar(0, 1, 'C2_main_div24_CAST_store')
solver.Add( + (1)*main_div24_fixbits + (-1)*main_div24_CAST_store_fixbits + (-10000)*C1_main_div24_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div24_fixbits + (1)*main_div24_CAST_store_fixbits + (-10000)*C2_main_div24_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div24_CAST_store
castCostObj +=  + (1)*C2_main_div24_CAST_store
C3_main_div24_CAST_store = solver.IntVar(0, 1, 'C3_main_div24_CAST_store')
C4_main_div24_CAST_store = solver.IntVar(0, 1, 'C4_main_div24_CAST_store')
C5_main_div24_CAST_store = solver.IntVar(0, 1, 'C5_main_div24_CAST_store')
C6_main_div24_CAST_store = solver.IntVar(0, 1, 'C6_main_div24_CAST_store')
C7_main_div24_CAST_store = solver.IntVar(0, 1, 'C7_main_div24_CAST_store')
C8_main_div24_CAST_store = solver.IntVar(0, 1, 'C8_main_div24_CAST_store')
solver.Add( + (1)*main_div24_fixp + (1)*main_div24_CAST_store_float + (-1)*C3_main_div24_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div24_CAST_store
solver.Add( + (1)*main_div24_float + (1)*main_div24_CAST_store_fixp + (-1)*C4_main_div24_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div24_CAST_store
solver.Add( + (1)*main_div24_fixp + (1)*main_div24_CAST_store_double + (-1)*C5_main_div24_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div24_CAST_store
solver.Add( + (1)*main_div24_double + (1)*main_div24_CAST_store_fixp + (-1)*C6_main_div24_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div24_CAST_store
solver.Add( + (1)*main_div24_float + (1)*main_div24_CAST_store_double + (-1)*C7_main_div24_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div24_CAST_store
solver.Add( + (1)*main_div24_double + (1)*main_div24_CAST_store_float + (-1)*C8_main_div24_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div24_CAST_store
solver.Add( + (1)*ey_fixp + (-1)*main_div24_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*ey_float + (-1)*main_div24_CAST_store_float==0)    #float equality
solver.Add( + (1)*ey_double + (-1)*main_div24_CAST_store_double==0)    #double equality
solver.Add( + (1)*ey_fixbits + (-1)*main_div24_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
ey_enob_storeENOB = solver.IntVar(-10000, 10000, 'ey_enob_storeENOB')
solver.Add( + (1)*ey_enob_storeENOB + (-1)*ey_fixbits + (10000)*ey_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ey_enob_storeENOB + (10000)*ey_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ey_enob_storeENOB + (10000)*ey_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ey_enob_storeENOB + (-1)*main_div24_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv29 = sitofp i32 %i.1 to double, !taffo.info !20, !taffo.initweight !21
main_conv29_fixbits = solver.IntVar(0, 23, 'main_conv29_fixbits')
main_conv29_fixp = solver.IntVar(0, 1, 'main_conv29_fixp')
main_conv29_float = solver.IntVar(0, 1, 'main_conv29_float')
main_conv29_double = solver.IntVar(0, 1, 'main_conv29_double')
main_conv29_enob = solver.IntVar(-10000, 10000, 'main_conv29_enob')
solver.Add( + (1)*main_conv29_enob + (-1)*main_conv29_fixbits + (10000)*main_conv29_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv29_enob + (10000)*main_conv29_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv29_enob + (10000)*main_conv29_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv29_fixbits + (-10000)*main_conv29_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv29_enob
solver.Add( + (1)*main_conv29_fixp + (1)*main_conv29_float + (1)*main_conv29_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv29_fixbits + (-10000)*main_conv29_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv29_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv31 = sitofp i32 %add30 to double, !taffo.info !28, !taffo.initweight !22
main_conv31_fixbits = solver.IntVar(0, 23, 'main_conv31_fixbits')
main_conv31_fixp = solver.IntVar(0, 1, 'main_conv31_fixp')
main_conv31_float = solver.IntVar(0, 1, 'main_conv31_float')
main_conv31_double = solver.IntVar(0, 1, 'main_conv31_double')
main_conv31_enob = solver.IntVar(-10000, 10000, 'main_conv31_enob')
solver.Add( + (1)*main_conv31_enob + (-1)*main_conv31_fixbits + (10000)*main_conv31_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv31_enob + (10000)*main_conv31_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv31_enob + (10000)*main_conv31_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv31_fixbits + (-10000)*main_conv31_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv31_enob
solver.Add( + (1)*main_conv31_fixp + (1)*main_conv31_float + (1)*main_conv31_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv31_fixbits + (-10000)*main_conv31_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv31_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %mul32 = fmul double %conv29, %conv31, !taffo.info !29, !taffo.initweight !22
main_conv29_CAST_mul32_fixbits = solver.IntVar(0, 23, 'main_conv29_CAST_mul32_fixbits')
main_conv29_CAST_mul32_fixp = solver.IntVar(0, 1, 'main_conv29_CAST_mul32_fixp')
main_conv29_CAST_mul32_float = solver.IntVar(0, 1, 'main_conv29_CAST_mul32_float')
main_conv29_CAST_mul32_double = solver.IntVar(0, 1, 'main_conv29_CAST_mul32_double')
solver.Add( + (1)*main_conv29_CAST_mul32_fixp + (1)*main_conv29_CAST_mul32_float + (1)*main_conv29_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv29_CAST_mul32_fixbits + (-10000)*main_conv29_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C1_main_conv29_CAST_mul32')
C2_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C2_main_conv29_CAST_mul32')
solver.Add( + (1)*main_conv29_fixbits + (-1)*main_conv29_CAST_mul32_fixbits + (-10000)*C1_main_conv29_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv29_fixbits + (1)*main_conv29_CAST_mul32_fixbits + (-10000)*C2_main_conv29_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv29_CAST_mul32
castCostObj +=  + (1)*C2_main_conv29_CAST_mul32
C3_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C3_main_conv29_CAST_mul32')
C4_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C4_main_conv29_CAST_mul32')
C5_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C5_main_conv29_CAST_mul32')
C6_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C6_main_conv29_CAST_mul32')
C7_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C7_main_conv29_CAST_mul32')
C8_main_conv29_CAST_mul32 = solver.IntVar(0, 1, 'C8_main_conv29_CAST_mul32')
solver.Add( + (1)*main_conv29_fixp + (1)*main_conv29_CAST_mul32_float + (-1)*C3_main_conv29_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv29_CAST_mul32
solver.Add( + (1)*main_conv29_float + (1)*main_conv29_CAST_mul32_fixp + (-1)*C4_main_conv29_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv29_CAST_mul32
solver.Add( + (1)*main_conv29_fixp + (1)*main_conv29_CAST_mul32_double + (-1)*C5_main_conv29_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv29_CAST_mul32
solver.Add( + (1)*main_conv29_double + (1)*main_conv29_CAST_mul32_fixp + (-1)*C6_main_conv29_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv29_CAST_mul32
solver.Add( + (1)*main_conv29_float + (1)*main_conv29_CAST_mul32_double + (-1)*C7_main_conv29_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv29_CAST_mul32
solver.Add( + (1)*main_conv29_double + (1)*main_conv29_CAST_mul32_float + (-1)*C8_main_conv29_CAST_mul32<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv29_CAST_mul32



#Constraint for cast for   %mul32 = fmul double %conv29, %conv31, !taffo.info !29, !taffo.initweight !22
main_conv31_CAST_mul32_fixbits = solver.IntVar(0, 23, 'main_conv31_CAST_mul32_fixbits')
main_conv31_CAST_mul32_fixp = solver.IntVar(0, 1, 'main_conv31_CAST_mul32_fixp')
main_conv31_CAST_mul32_float = solver.IntVar(0, 1, 'main_conv31_CAST_mul32_float')
main_conv31_CAST_mul32_double = solver.IntVar(0, 1, 'main_conv31_CAST_mul32_double')
solver.Add( + (1)*main_conv31_CAST_mul32_fixp + (1)*main_conv31_CAST_mul32_float + (1)*main_conv31_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv31_CAST_mul32_fixbits + (-10000)*main_conv31_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C1_main_conv31_CAST_mul32')
C2_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C2_main_conv31_CAST_mul32')
solver.Add( + (1)*main_conv31_fixbits + (-1)*main_conv31_CAST_mul32_fixbits + (-10000)*C1_main_conv31_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv31_fixbits + (1)*main_conv31_CAST_mul32_fixbits + (-10000)*C2_main_conv31_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv31_CAST_mul32
castCostObj +=  + (1)*C2_main_conv31_CAST_mul32
C3_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C3_main_conv31_CAST_mul32')
C4_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C4_main_conv31_CAST_mul32')
C5_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C5_main_conv31_CAST_mul32')
C6_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C6_main_conv31_CAST_mul32')
C7_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C7_main_conv31_CAST_mul32')
C8_main_conv31_CAST_mul32 = solver.IntVar(0, 1, 'C8_main_conv31_CAST_mul32')
solver.Add( + (1)*main_conv31_fixp + (1)*main_conv31_CAST_mul32_float + (-1)*C3_main_conv31_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv31_CAST_mul32
solver.Add( + (1)*main_conv31_float + (1)*main_conv31_CAST_mul32_fixp + (-1)*C4_main_conv31_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv31_CAST_mul32
solver.Add( + (1)*main_conv31_fixp + (1)*main_conv31_CAST_mul32_double + (-1)*C5_main_conv31_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv31_CAST_mul32
solver.Add( + (1)*main_conv31_double + (1)*main_conv31_CAST_mul32_fixp + (-1)*C6_main_conv31_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv31_CAST_mul32
solver.Add( + (1)*main_conv31_float + (1)*main_conv31_CAST_mul32_double + (-1)*C7_main_conv31_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv31_CAST_mul32
solver.Add( + (1)*main_conv31_double + (1)*main_conv31_CAST_mul32_float + (-1)*C8_main_conv31_CAST_mul32<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv31_CAST_mul32



#Stuff for   %mul32 = fmul double %conv29, %conv31, !taffo.info !29, !taffo.initweight !22
main_mul32_fixbits = solver.IntVar(0, 15, 'main_mul32_fixbits')
main_mul32_fixp = solver.IntVar(0, 1, 'main_mul32_fixp')
main_mul32_float = solver.IntVar(0, 1, 'main_mul32_float')
main_mul32_double = solver.IntVar(0, 1, 'main_mul32_double')
main_mul32_enob = solver.IntVar(-10000, 10000, 'main_mul32_enob')
solver.Add( + (1)*main_mul32_enob + (-1)*main_mul32_fixbits + (10000)*main_mul32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul32_enob + (10000)*main_mul32_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul32_enob + (10000)*main_mul32_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul32_fixbits + (-10000)*main_mul32_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj +=  + (-1)*main_mul32_enob
solver.Add( + (1)*main_mul32_fixp + (1)*main_mul32_float + (1)*main_mul32_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul32_fixbits + (-10000)*main_mul32_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv29_CAST_mul32_fixp + (-1)*main_conv31_CAST_mul32_fixp==0)    #fix equality
solver.Add( + (1)*main_conv29_CAST_mul32_float + (-1)*main_conv31_CAST_mul32_float==0)    #float equality
solver.Add( + (1)*main_conv29_CAST_mul32_double + (-1)*main_conv31_CAST_mul32_double==0)    #double equality
solver.Add( + (1)*main_conv29_CAST_mul32_fixp + (-1)*main_mul32_fixp==0)    #fix equality
solver.Add( + (1)*main_conv29_CAST_mul32_float + (-1)*main_mul32_float==0)    #float equality
solver.Add( + (1)*main_conv29_CAST_mul32_double + (-1)*main_mul32_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul32_fixp
mathCostObj +=  + (2.64722)*main_mul32_float
mathCostObj +=  + (4.02255)*main_mul32_double
main_main_mul32_enob_1 = solver.IntVar(0, 1, 'main_main_mul32_enob_1')
main_main_mul32_enob_2 = solver.IntVar(0, 1, 'main_main_mul32_enob_2')
solver.Add( + (1)*main_main_mul32_enob_1 + (1)*main_main_mul32_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul32_enob + (-1)*main_conv31_enob + (-10000)*main_main_mul32_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul32_enob + (-1)*main_conv29_enob + (-10000)*main_main_mul32_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for   %conv33 = sitofp i32 200 to double, !taffo.info !31
main_conv33_fixbits = solver.IntVar(0, 24, 'main_conv33_fixbits')
main_conv33_fixp = solver.IntVar(0, 1, 'main_conv33_fixp')
main_conv33_float = solver.IntVar(0, 1, 'main_conv33_float')
main_conv33_double = solver.IntVar(0, 1, 'main_conv33_double')
main_conv33_enob = solver.IntVar(-10000, 10000, 'main_conv33_enob')
solver.Add( + (1)*main_conv33_enob + (-1)*main_conv33_fixbits + (10000)*main_conv33_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv33_enob + (10000)*main_conv33_float<=10016)    #Enob constraint for float
solver.Add( + (1)*main_conv33_enob + (10000)*main_conv33_double<=10045)    #Enob constraint for double
solver.Add( + (1)*main_conv33_fixbits + (-10000)*main_conv33_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*main_conv33_enob
solver.Add( + (1)*main_conv33_fixp + (1)*main_conv33_float + (1)*main_conv33_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv33_fixbits + (-10000)*main_conv33_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv33_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div34 = fdiv double %mul32, %conv33, !taffo.info !28, !taffo.initweight !33
main_mul32_CAST_div34_fixbits = solver.IntVar(0, 15, 'main_mul32_CAST_div34_fixbits')
main_mul32_CAST_div34_fixp = solver.IntVar(0, 1, 'main_mul32_CAST_div34_fixp')
main_mul32_CAST_div34_float = solver.IntVar(0, 1, 'main_mul32_CAST_div34_float')
main_mul32_CAST_div34_double = solver.IntVar(0, 1, 'main_mul32_CAST_div34_double')
solver.Add( + (1)*main_mul32_CAST_div34_fixp + (1)*main_mul32_CAST_div34_float + (1)*main_mul32_CAST_div34_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul32_CAST_div34_fixbits + (-10000)*main_mul32_CAST_div34_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C1_main_mul32_CAST_div34')
C2_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C2_main_mul32_CAST_div34')
solver.Add( + (1)*main_mul32_fixbits + (-1)*main_mul32_CAST_div34_fixbits + (-10000)*C1_main_mul32_CAST_div34<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul32_fixbits + (1)*main_mul32_CAST_div34_fixbits + (-10000)*C2_main_mul32_CAST_div34<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul32_CAST_div34
castCostObj +=  + (1)*C2_main_mul32_CAST_div34
C3_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C3_main_mul32_CAST_div34')
C4_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C4_main_mul32_CAST_div34')
C5_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C5_main_mul32_CAST_div34')
C6_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C6_main_mul32_CAST_div34')
C7_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C7_main_mul32_CAST_div34')
C8_main_mul32_CAST_div34 = solver.IntVar(0, 1, 'C8_main_mul32_CAST_div34')
solver.Add( + (1)*main_mul32_fixp + (1)*main_mul32_CAST_div34_float + (-1)*C3_main_mul32_CAST_div34<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul32_CAST_div34
solver.Add( + (1)*main_mul32_float + (1)*main_mul32_CAST_div34_fixp + (-1)*C4_main_mul32_CAST_div34<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul32_CAST_div34
solver.Add( + (1)*main_mul32_fixp + (1)*main_mul32_CAST_div34_double + (-1)*C5_main_mul32_CAST_div34<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul32_CAST_div34
solver.Add( + (1)*main_mul32_double + (1)*main_mul32_CAST_div34_fixp + (-1)*C6_main_mul32_CAST_div34<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul32_CAST_div34
solver.Add( + (1)*main_mul32_float + (1)*main_mul32_CAST_div34_double + (-1)*C7_main_mul32_CAST_div34<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul32_CAST_div34
solver.Add( + (1)*main_mul32_double + (1)*main_mul32_CAST_div34_float + (-1)*C8_main_mul32_CAST_div34<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul32_CAST_div34



#Constraint for cast for   %div34 = fdiv double %mul32, %conv33, !taffo.info !28, !taffo.initweight !33
main_conv33_CAST_div34_fixbits = solver.IntVar(0, 24, 'main_conv33_CAST_div34_fixbits')
main_conv33_CAST_div34_fixp = solver.IntVar(0, 1, 'main_conv33_CAST_div34_fixp')
main_conv33_CAST_div34_float = solver.IntVar(0, 1, 'main_conv33_CAST_div34_float')
main_conv33_CAST_div34_double = solver.IntVar(0, 1, 'main_conv33_CAST_div34_double')
solver.Add( + (1)*main_conv33_CAST_div34_fixp + (1)*main_conv33_CAST_div34_float + (1)*main_conv33_CAST_div34_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv33_CAST_div34_fixbits + (-10000)*main_conv33_CAST_div34_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C1_main_conv33_CAST_div34')
C2_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C2_main_conv33_CAST_div34')
solver.Add( + (1)*main_conv33_fixbits + (-1)*main_conv33_CAST_div34_fixbits + (-10000)*C1_main_conv33_CAST_div34<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv33_fixbits + (1)*main_conv33_CAST_div34_fixbits + (-10000)*C2_main_conv33_CAST_div34<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv33_CAST_div34
castCostObj +=  + (1)*C2_main_conv33_CAST_div34
C3_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C3_main_conv33_CAST_div34')
C4_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C4_main_conv33_CAST_div34')
C5_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C5_main_conv33_CAST_div34')
C6_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C6_main_conv33_CAST_div34')
C7_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C7_main_conv33_CAST_div34')
C8_main_conv33_CAST_div34 = solver.IntVar(0, 1, 'C8_main_conv33_CAST_div34')
solver.Add( + (1)*main_conv33_fixp + (1)*main_conv33_CAST_div34_float + (-1)*C3_main_conv33_CAST_div34<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv33_CAST_div34
solver.Add( + (1)*main_conv33_float + (1)*main_conv33_CAST_div34_fixp + (-1)*C4_main_conv33_CAST_div34<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv33_CAST_div34
solver.Add( + (1)*main_conv33_fixp + (1)*main_conv33_CAST_div34_double + (-1)*C5_main_conv33_CAST_div34<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv33_CAST_div34
solver.Add( + (1)*main_conv33_double + (1)*main_conv33_CAST_div34_fixp + (-1)*C6_main_conv33_CAST_div34<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv33_CAST_div34
solver.Add( + (1)*main_conv33_float + (1)*main_conv33_CAST_div34_double + (-1)*C7_main_conv33_CAST_div34<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv33_CAST_div34
solver.Add( + (1)*main_conv33_double + (1)*main_conv33_CAST_div34_float + (-1)*C8_main_conv33_CAST_div34<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv33_CAST_div34



#Stuff for   %div34 = fdiv double %mul32, %conv33, !taffo.info !28, !taffo.initweight !33
main_div34_fixbits = solver.IntVar(0, 23, 'main_div34_fixbits')
main_div34_fixp = solver.IntVar(0, 1, 'main_div34_fixp')
main_div34_float = solver.IntVar(0, 1, 'main_div34_float')
main_div34_double = solver.IntVar(0, 1, 'main_div34_double')
main_div34_enob = solver.IntVar(-10000, 10000, 'main_div34_enob')
solver.Add( + (1)*main_div34_enob + (-1)*main_div34_fixbits + (10000)*main_div34_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div34_enob + (10000)*main_div34_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div34_enob + (10000)*main_div34_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div34_fixbits + (-10000)*main_div34_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_div34_enob
solver.Add( + (1)*main_div34_fixp + (1)*main_div34_float + (1)*main_div34_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div34_fixbits + (-10000)*main_div34_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul32_CAST_div34_fixp + (-1)*main_conv33_CAST_div34_fixp==0)    #fix equality
solver.Add( + (1)*main_mul32_CAST_div34_float + (-1)*main_conv33_CAST_div34_float==0)    #float equality
solver.Add( + (1)*main_mul32_CAST_div34_double + (-1)*main_conv33_CAST_div34_double==0)    #double equality
solver.Add( + (1)*main_mul32_CAST_div34_fixp + (-1)*main_div34_fixp==0)    #fix equality
solver.Add( + (1)*main_mul32_CAST_div34_float + (-1)*main_div34_float==0)    #float equality
solver.Add( + (1)*main_mul32_CAST_div34_double + (-1)*main_div34_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div34_fixp
mathCostObj +=  + (5.60026)*main_div34_float
mathCostObj +=  + (18.3266)*main_div34_double
main_main_div34_enob_1 = solver.IntVar(0, 1, 'main_main_div34_enob_1')
main_main_div34_enob_2 = solver.IntVar(0, 1, 'main_main_div34_enob_2')
solver.Add( + (1)*main_main_div34_enob_1 + (1)*main_main_div34_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div34_enob + (-1)*main_conv33_enob + (-10000)*main_main_div34_enob_1<=1040)    #Enob: propagation in division 1
solver.Add( + (1)*main_div34_enob + (-1)*main_mul32_enob + (-10000)*main_main_div34_enob_2<=8)    #Enob: propagation in division 2



#Constraint for cast for   store double %div34, double* %arrayidx38, align 8, !taffo.info !12, !taffo.initweight !22
main_div34_CAST_store_fixbits = solver.IntVar(0, 23, 'main_div34_CAST_store_fixbits')
main_div34_CAST_store_fixp = solver.IntVar(0, 1, 'main_div34_CAST_store_fixp')
main_div34_CAST_store_float = solver.IntVar(0, 1, 'main_div34_CAST_store_float')
main_div34_CAST_store_double = solver.IntVar(0, 1, 'main_div34_CAST_store_double')
solver.Add( + (1)*main_div34_CAST_store_fixp + (1)*main_div34_CAST_store_float + (1)*main_div34_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div34_CAST_store_fixbits + (-10000)*main_div34_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div34_CAST_store = solver.IntVar(0, 1, 'C1_main_div34_CAST_store')
C2_main_div34_CAST_store = solver.IntVar(0, 1, 'C2_main_div34_CAST_store')
solver.Add( + (1)*main_div34_fixbits + (-1)*main_div34_CAST_store_fixbits + (-10000)*C1_main_div34_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div34_fixbits + (1)*main_div34_CAST_store_fixbits + (-10000)*C2_main_div34_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div34_CAST_store
castCostObj +=  + (1)*C2_main_div34_CAST_store
C3_main_div34_CAST_store = solver.IntVar(0, 1, 'C3_main_div34_CAST_store')
C4_main_div34_CAST_store = solver.IntVar(0, 1, 'C4_main_div34_CAST_store')
C5_main_div34_CAST_store = solver.IntVar(0, 1, 'C5_main_div34_CAST_store')
C6_main_div34_CAST_store = solver.IntVar(0, 1, 'C6_main_div34_CAST_store')
C7_main_div34_CAST_store = solver.IntVar(0, 1, 'C7_main_div34_CAST_store')
C8_main_div34_CAST_store = solver.IntVar(0, 1, 'C8_main_div34_CAST_store')
solver.Add( + (1)*main_div34_fixp + (1)*main_div34_CAST_store_float + (-1)*C3_main_div34_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div34_CAST_store
solver.Add( + (1)*main_div34_float + (1)*main_div34_CAST_store_fixp + (-1)*C4_main_div34_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div34_CAST_store
solver.Add( + (1)*main_div34_fixp + (1)*main_div34_CAST_store_double + (-1)*C5_main_div34_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div34_CAST_store
solver.Add( + (1)*main_div34_double + (1)*main_div34_CAST_store_fixp + (-1)*C6_main_div34_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div34_CAST_store
solver.Add( + (1)*main_div34_float + (1)*main_div34_CAST_store_double + (-1)*C7_main_div34_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div34_CAST_store
solver.Add( + (1)*main_div34_double + (1)*main_div34_CAST_store_float + (-1)*C8_main_div34_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div34_CAST_store
solver.Add( + (1)*hz_fixp + (-1)*main_div34_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*hz_float + (-1)*main_div34_CAST_store_float==0)    #float equality
solver.Add( + (1)*hz_double + (-1)*main_div34_CAST_store_double==0)    #double equality
solver.Add( + (1)*hz_fixbits + (-1)*main_div34_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
hz_enob_storeENOB = solver.IntVar(-10000, 10000, 'hz_enob_storeENOB')
solver.Add( + (1)*hz_enob_storeENOB + (-1)*hz_fixbits + (10000)*hz_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*hz_enob_storeENOB + (10000)*hz_float<=10149)    #Enob constraint for float
solver.Add( + (1)*hz_enob_storeENOB + (10000)*hz_double<=11074)    #Enob constraint for double
solver.Add( + (1)*hz_enob_storeENOB + (-1)*main_div34_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
_fict__enob_memphi_main_tmp = solver.IntVar(-10000, 10000, '_fict__enob_memphi_main_tmp')
solver.Add( + (1)*_fict__enob_memphi_main_tmp + (-1)*_fict__enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
solver.Add( + (1)*main_main_tmp_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*_fict__enob_memphi_main_tmp + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp, double* %arrayidx58, align 8, !taffo.info !12, !taffo.initweight !22
_fict__CAST_store_fixbits = solver.IntVar(0, 23, '_fict__CAST_store_fixbits')
_fict__CAST_store_fixp = solver.IntVar(0, 1, '_fict__CAST_store_fixp')
_fict__CAST_store_float = solver.IntVar(0, 1, '_fict__CAST_store_float')
_fict__CAST_store_double = solver.IntVar(0, 1, '_fict__CAST_store_double')
solver.Add( + (1)*_fict__CAST_store_fixp + (1)*_fict__CAST_store_float + (1)*_fict__CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*_fict__CAST_store_fixbits + (-10000)*_fict__CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1__fict__CAST_store = solver.IntVar(0, 1, 'C1__fict__CAST_store')
C2__fict__CAST_store = solver.IntVar(0, 1, 'C2__fict__CAST_store')
solver.Add( + (1)*_fict__fixbits + (-1)*_fict__CAST_store_fixbits + (-10000)*C1__fict__CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*_fict__fixbits + (1)*_fict__CAST_store_fixbits + (-10000)*C2__fict__CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1__fict__CAST_store
castCostObj +=  + (1)*C2__fict__CAST_store
C3__fict__CAST_store = solver.IntVar(0, 1, 'C3__fict__CAST_store')
C4__fict__CAST_store = solver.IntVar(0, 1, 'C4__fict__CAST_store')
C5__fict__CAST_store = solver.IntVar(0, 1, 'C5__fict__CAST_store')
C6__fict__CAST_store = solver.IntVar(0, 1, 'C6__fict__CAST_store')
C7__fict__CAST_store = solver.IntVar(0, 1, 'C7__fict__CAST_store')
C8__fict__CAST_store = solver.IntVar(0, 1, 'C8__fict__CAST_store')
solver.Add( + (1)*_fict__fixp + (1)*_fict__CAST_store_float + (-1)*C3__fict__CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3__fict__CAST_store
solver.Add( + (1)*_fict__float + (1)*_fict__CAST_store_fixp + (-1)*C4__fict__CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4__fict__CAST_store
solver.Add( + (1)*_fict__fixp + (1)*_fict__CAST_store_double + (-1)*C5__fict__CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5__fict__CAST_store
solver.Add( + (1)*_fict__double + (1)*_fict__CAST_store_fixp + (-1)*C6__fict__CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6__fict__CAST_store
solver.Add( + (1)*_fict__float + (1)*_fict__CAST_store_double + (-1)*C7__fict__CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7__fict__CAST_store
solver.Add( + (1)*_fict__double + (1)*_fict__CAST_store_float + (-1)*C8__fict__CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8__fict__CAST_store
solver.Add( + (1)*ey_fixp + (-1)*_fict__CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*ey_float + (-1)*_fict__CAST_store_float==0)    #float equality
solver.Add( + (1)*ey_double + (-1)*_fict__CAST_store_double==0)    #double equality
solver.Add( + (1)*ey_fixbits + (-1)*_fict__CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
ey_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'ey_enob_storeENOB_storeENOB')
solver.Add( + (1)*ey_enob_storeENOB_storeENOB + (-1)*ey_fixbits + (10000)*ey_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ey_enob_storeENOB_storeENOB + (10000)*ey_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ey_enob_storeENOB_storeENOB + (10000)*ey_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ey_enob_storeENOB_storeENOB + (-1)*_fict__enob_memphi_main_tmp<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
ey_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'ey_enob_memphi_main_tmp1')
solver.Add( + (1)*ey_enob_memphi_main_tmp1 + (-1)*ey_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
main_main_tmp1_enob_3 = solver.IntVar(0, 1, 'main_main_tmp1_enob_3')
main_main_tmp1_enob_4 = solver.IntVar(0, 1, 'main_main_tmp1_enob_4')
main_main_tmp1_enob_5 = solver.IntVar(0, 1, 'main_main_tmp1_enob_5')
main_main_tmp1_enob_6 = solver.IntVar(0, 1, 'main_main_tmp1_enob_6')
solver.Add( + (1)*main_main_tmp1_enob_1 + (1)*main_main_tmp1_enob_2 + (1)*main_main_tmp1_enob_3 + (1)*main_main_tmp1_enob_4 + (1)*main_main_tmp1_enob_5 + (1)*main_main_tmp1_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp1 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp1 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp1_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp1 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_5<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
hz_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'hz_enob_memphi_main_tmp2')
solver.Add( + (1)*hz_enob_memphi_main_tmp2 + (-1)*hz_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
main_main_tmp2_enob_3 = solver.IntVar(0, 1, 'main_main_tmp2_enob_3')
main_main_tmp2_enob_4 = solver.IntVar(0, 1, 'main_main_tmp2_enob_4')
main_main_tmp2_enob_5 = solver.IntVar(0, 1, 'main_main_tmp2_enob_5')
main_main_tmp2_enob_6 = solver.IntVar(0, 1, 'main_main_tmp2_enob_6')
solver.Add( + (1)*main_main_tmp2_enob_1 + (1)*main_main_tmp2_enob_2 + (1)*main_main_tmp2_enob_3 + (1)*main_main_tmp2_enob_4 + (1)*main_main_tmp2_enob_5 + (1)*main_main_tmp2_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp2 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp2 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp2_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp2 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
hz_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'hz_enob_memphi_main_tmp3')
solver.Add( + (1)*hz_enob_memphi_main_tmp3 + (-1)*hz_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
main_main_tmp3_enob_5 = solver.IntVar(0, 1, 'main_main_tmp3_enob_5')
main_main_tmp3_enob_6 = solver.IntVar(0, 1, 'main_main_tmp3_enob_6')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3 + (1)*main_main_tmp3_enob_4 + (1)*main_main_tmp3_enob_5 + (1)*main_main_tmp3_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp3 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp3_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp3 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp3 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub82 = fsub double %tmp2, %tmp3, !taffo.info !39, !taffo.initweight !33
hz_CAST_sub82_fixbits = solver.IntVar(0, 23, 'hz_CAST_sub82_fixbits')
hz_CAST_sub82_fixp = solver.IntVar(0, 1, 'hz_CAST_sub82_fixp')
hz_CAST_sub82_float = solver.IntVar(0, 1, 'hz_CAST_sub82_float')
hz_CAST_sub82_double = solver.IntVar(0, 1, 'hz_CAST_sub82_double')
solver.Add( + (1)*hz_CAST_sub82_fixp + (1)*hz_CAST_sub82_float + (1)*hz_CAST_sub82_double==1)    #exactly 1 type
solver.Add( + (1)*hz_CAST_sub82_fixbits + (-10000)*hz_CAST_sub82_fixp<=0)    #If no fix, fix frac part = 0
C1_hz_CAST_sub82 = solver.IntVar(0, 1, 'C1_hz_CAST_sub82')
C2_hz_CAST_sub82 = solver.IntVar(0, 1, 'C2_hz_CAST_sub82')
solver.Add( + (1)*hz_fixbits + (-1)*hz_CAST_sub82_fixbits + (-10000)*C1_hz_CAST_sub82<=0)    #Shift cost 1
solver.Add( + (-1)*hz_fixbits + (1)*hz_CAST_sub82_fixbits + (-10000)*C2_hz_CAST_sub82<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_hz_CAST_sub82
castCostObj +=  + (1)*C2_hz_CAST_sub82
C3_hz_CAST_sub82 = solver.IntVar(0, 1, 'C3_hz_CAST_sub82')
C4_hz_CAST_sub82 = solver.IntVar(0, 1, 'C4_hz_CAST_sub82')
C5_hz_CAST_sub82 = solver.IntVar(0, 1, 'C5_hz_CAST_sub82')
C6_hz_CAST_sub82 = solver.IntVar(0, 1, 'C6_hz_CAST_sub82')
C7_hz_CAST_sub82 = solver.IntVar(0, 1, 'C7_hz_CAST_sub82')
C8_hz_CAST_sub82 = solver.IntVar(0, 1, 'C8_hz_CAST_sub82')
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub82_float + (-1)*C3_hz_CAST_sub82<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_hz_CAST_sub82
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub82_fixp + (-1)*C4_hz_CAST_sub82<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_hz_CAST_sub82
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub82_double + (-1)*C5_hz_CAST_sub82<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_hz_CAST_sub82
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub82_fixp + (-1)*C6_hz_CAST_sub82<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_hz_CAST_sub82
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub82_double + (-1)*C7_hz_CAST_sub82<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_hz_CAST_sub82
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub82_float + (-1)*C8_hz_CAST_sub82<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_hz_CAST_sub82



#Constraint for cast for   %sub82 = fsub double %tmp2, %tmp3, !taffo.info !39, !taffo.initweight !33
hz_CAST_sub82_0_fixbits = solver.IntVar(0, 23, 'hz_CAST_sub82_0_fixbits')
hz_CAST_sub82_0_fixp = solver.IntVar(0, 1, 'hz_CAST_sub82_0_fixp')
hz_CAST_sub82_0_float = solver.IntVar(0, 1, 'hz_CAST_sub82_0_float')
hz_CAST_sub82_0_double = solver.IntVar(0, 1, 'hz_CAST_sub82_0_double')
solver.Add( + (1)*hz_CAST_sub82_0_fixp + (1)*hz_CAST_sub82_0_float + (1)*hz_CAST_sub82_0_double==1)    #exactly 1 type
solver.Add( + (1)*hz_CAST_sub82_0_fixbits + (-10000)*hz_CAST_sub82_0_fixp<=0)    #If no fix, fix frac part = 0
C1_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C1_hz_CAST_sub82_0')
C2_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C2_hz_CAST_sub82_0')
solver.Add( + (1)*hz_fixbits + (-1)*hz_CAST_sub82_0_fixbits + (-10000)*C1_hz_CAST_sub82_0<=0)    #Shift cost 1
solver.Add( + (-1)*hz_fixbits + (1)*hz_CAST_sub82_0_fixbits + (-10000)*C2_hz_CAST_sub82_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_hz_CAST_sub82_0
castCostObj +=  + (1)*C2_hz_CAST_sub82_0
C3_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C3_hz_CAST_sub82_0')
C4_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C4_hz_CAST_sub82_0')
C5_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C5_hz_CAST_sub82_0')
C6_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C6_hz_CAST_sub82_0')
C7_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C7_hz_CAST_sub82_0')
C8_hz_CAST_sub82_0 = solver.IntVar(0, 1, 'C8_hz_CAST_sub82_0')
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub82_0_float + (-1)*C3_hz_CAST_sub82_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_hz_CAST_sub82_0
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub82_0_fixp + (-1)*C4_hz_CAST_sub82_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_hz_CAST_sub82_0
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub82_0_double + (-1)*C5_hz_CAST_sub82_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_hz_CAST_sub82_0
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub82_0_fixp + (-1)*C6_hz_CAST_sub82_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_hz_CAST_sub82_0
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub82_0_double + (-1)*C7_hz_CAST_sub82_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_hz_CAST_sub82_0
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub82_0_float + (-1)*C8_hz_CAST_sub82_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_hz_CAST_sub82_0



#Stuff for   %sub82 = fsub double %tmp2, %tmp3, !taffo.info !39, !taffo.initweight !33
main_sub82_fixbits = solver.IntVar(0, 22, 'main_sub82_fixbits')
main_sub82_fixp = solver.IntVar(0, 1, 'main_sub82_fixp')
main_sub82_float = solver.IntVar(0, 1, 'main_sub82_float')
main_sub82_double = solver.IntVar(0, 1, 'main_sub82_double')
main_sub82_enob = solver.IntVar(-10000, 10000, 'main_sub82_enob')
solver.Add( + (1)*main_sub82_enob + (-1)*main_sub82_fixbits + (10000)*main_sub82_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub82_enob + (10000)*main_sub82_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub82_enob + (10000)*main_sub82_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub82_fixbits + (-10000)*main_sub82_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_sub82_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub82_enob
solver.Add( + (1)*main_sub82_fixp + (1)*main_sub82_float + (1)*main_sub82_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub82_fixbits + (-10000)*main_sub82_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*hz_CAST_sub82_fixp + (-1)*hz_CAST_sub82_0_fixp==0)    #fix equality
solver.Add( + (1)*hz_CAST_sub82_float + (-1)*hz_CAST_sub82_0_float==0)    #float equality
solver.Add( + (1)*hz_CAST_sub82_double + (-1)*hz_CAST_sub82_0_double==0)    #double equality
solver.Add( + (1)*hz_CAST_sub82_fixbits + (-1)*hz_CAST_sub82_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*hz_CAST_sub82_fixp + (-1)*main_sub82_fixp==0)    #fix equality
solver.Add( + (1)*hz_CAST_sub82_float + (-1)*main_sub82_float==0)    #float equality
solver.Add( + (1)*hz_CAST_sub82_double + (-1)*main_sub82_double==0)    #double equality
solver.Add( + (1)*hz_CAST_sub82_fixbits + (-1)*main_sub82_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub82_fixp
mathCostObj +=  + (2.33125)*main_sub82_float
mathCostObj +=  + (2.72422)*main_sub82_double
solver.Add( + (1)*main_sub82_enob + (-1)*hz_enob_memphi_main_tmp2<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub82_enob + (-1)*hz_enob_memphi_main_tmp3<=0)    #Enob propagation in sub second addend



#Stuff for double 5.000000e-01
ConstantValue__fixbits = solver.IntVar(0, 31, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-01
ConstantValue__0_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-01
ConstantValue__1_fixbits = solver.IntVar(0, 31, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul83 = fmul double 5.000000e-01, %sub82, !taffo.info !12, !taffo.initweight !41, !taffo.constinfo !42
ConstantValue__1_CAST_mul83_fixbits = solver.IntVar(0, 31, 'ConstantValue__1_CAST_mul83_fixbits')
ConstantValue__1_CAST_mul83_fixp = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul83_fixp')
ConstantValue__1_CAST_mul83_float = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul83_float')
ConstantValue__1_CAST_mul83_double = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul83_double')
solver.Add( + (1)*ConstantValue__1_CAST_mul83_fixp + (1)*ConstantValue__1_CAST_mul83_float + (1)*ConstantValue__1_CAST_mul83_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__1_CAST_mul83_fixbits + (-10000)*ConstantValue__1_CAST_mul83_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C1_ConstantValue__1_CAST_mul83')
C2_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C2_ConstantValue__1_CAST_mul83')
solver.Add( + (1)*ConstantValue__1_fixbits + (-1)*ConstantValue__1_CAST_mul83_fixbits + (-10000)*C1_ConstantValue__1_CAST_mul83<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__1_fixbits + (1)*ConstantValue__1_CAST_mul83_fixbits + (-10000)*C2_ConstantValue__1_CAST_mul83<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__1_CAST_mul83
castCostObj +=  + (1)*C2_ConstantValue__1_CAST_mul83
C3_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C3_ConstantValue__1_CAST_mul83')
C4_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C4_ConstantValue__1_CAST_mul83')
C5_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C5_ConstantValue__1_CAST_mul83')
C6_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C6_ConstantValue__1_CAST_mul83')
C7_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C7_ConstantValue__1_CAST_mul83')
C8_ConstantValue__1_CAST_mul83 = solver.IntVar(0, 1, 'C8_ConstantValue__1_CAST_mul83')
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_mul83_float + (-1)*C3_ConstantValue__1_CAST_mul83<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__1_CAST_mul83
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_mul83_fixp + (-1)*C4_ConstantValue__1_CAST_mul83<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__1_CAST_mul83
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_mul83_double + (-1)*C5_ConstantValue__1_CAST_mul83<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__1_CAST_mul83
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_mul83_fixp + (-1)*C6_ConstantValue__1_CAST_mul83<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__1_CAST_mul83
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_mul83_double + (-1)*C7_ConstantValue__1_CAST_mul83<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__1_CAST_mul83
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_mul83_float + (-1)*C8_ConstantValue__1_CAST_mul83<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__1_CAST_mul83



#Constraint for cast for   %mul83 = fmul double 5.000000e-01, %sub82, !taffo.info !12, !taffo.initweight !41, !taffo.constinfo !42
main_sub82_CAST_mul83_fixbits = solver.IntVar(0, 22, 'main_sub82_CAST_mul83_fixbits')
main_sub82_CAST_mul83_fixp = solver.IntVar(0, 1, 'main_sub82_CAST_mul83_fixp')
main_sub82_CAST_mul83_float = solver.IntVar(0, 1, 'main_sub82_CAST_mul83_float')
main_sub82_CAST_mul83_double = solver.IntVar(0, 1, 'main_sub82_CAST_mul83_double')
solver.Add( + (1)*main_sub82_CAST_mul83_fixp + (1)*main_sub82_CAST_mul83_float + (1)*main_sub82_CAST_mul83_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub82_CAST_mul83_fixbits + (-10000)*main_sub82_CAST_mul83_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C1_main_sub82_CAST_mul83')
C2_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C2_main_sub82_CAST_mul83')
solver.Add( + (1)*main_sub82_fixbits + (-1)*main_sub82_CAST_mul83_fixbits + (-10000)*C1_main_sub82_CAST_mul83<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub82_fixbits + (1)*main_sub82_CAST_mul83_fixbits + (-10000)*C2_main_sub82_CAST_mul83<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub82_CAST_mul83
castCostObj +=  + (1)*C2_main_sub82_CAST_mul83
C3_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C3_main_sub82_CAST_mul83')
C4_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C4_main_sub82_CAST_mul83')
C5_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C5_main_sub82_CAST_mul83')
C6_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C6_main_sub82_CAST_mul83')
C7_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C7_main_sub82_CAST_mul83')
C8_main_sub82_CAST_mul83 = solver.IntVar(0, 1, 'C8_main_sub82_CAST_mul83')
solver.Add( + (1)*main_sub82_fixp + (1)*main_sub82_CAST_mul83_float + (-1)*C3_main_sub82_CAST_mul83<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub82_CAST_mul83
solver.Add( + (1)*main_sub82_float + (1)*main_sub82_CAST_mul83_fixp + (-1)*C4_main_sub82_CAST_mul83<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub82_CAST_mul83
solver.Add( + (1)*main_sub82_fixp + (1)*main_sub82_CAST_mul83_double + (-1)*C5_main_sub82_CAST_mul83<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub82_CAST_mul83
solver.Add( + (1)*main_sub82_double + (1)*main_sub82_CAST_mul83_fixp + (-1)*C6_main_sub82_CAST_mul83<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub82_CAST_mul83
solver.Add( + (1)*main_sub82_float + (1)*main_sub82_CAST_mul83_double + (-1)*C7_main_sub82_CAST_mul83<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub82_CAST_mul83
solver.Add( + (1)*main_sub82_double + (1)*main_sub82_CAST_mul83_float + (-1)*C8_main_sub82_CAST_mul83<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub82_CAST_mul83



#Stuff for   %mul83 = fmul double 5.000000e-01, %sub82, !taffo.info !12, !taffo.initweight !41, !taffo.constinfo !42
main_mul83_fixbits = solver.IntVar(0, 23, 'main_mul83_fixbits')
main_mul83_fixp = solver.IntVar(0, 1, 'main_mul83_fixp')
main_mul83_float = solver.IntVar(0, 1, 'main_mul83_float')
main_mul83_double = solver.IntVar(0, 1, 'main_mul83_double')
main_mul83_enob = solver.IntVar(-10000, 10000, 'main_mul83_enob')
solver.Add( + (1)*main_mul83_enob + (-1)*main_mul83_fixbits + (10000)*main_mul83_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul83_enob + (10000)*main_mul83_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul83_enob + (10000)*main_mul83_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul83_fixbits + (-10000)*main_mul83_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_mul83_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul83_enob
solver.Add( + (1)*main_mul83_fixp + (1)*main_mul83_float + (1)*main_mul83_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul83_fixbits + (-10000)*main_mul83_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__1_CAST_mul83_fixp + (-1)*main_sub82_CAST_mul83_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__1_CAST_mul83_float + (-1)*main_sub82_CAST_mul83_float==0)    #float equality
solver.Add( + (1)*ConstantValue__1_CAST_mul83_double + (-1)*main_sub82_CAST_mul83_double==0)    #double equality
solver.Add( + (1)*ConstantValue__1_CAST_mul83_fixp + (-1)*main_mul83_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__1_CAST_mul83_float + (-1)*main_mul83_float==0)    #float equality
solver.Add( + (1)*ConstantValue__1_CAST_mul83_double + (-1)*main_mul83_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul83_fixp
mathCostObj +=  + (2.64722)*main_mul83_float
mathCostObj +=  + (4.02255)*main_mul83_double
main_main_mul83_enob_1 = solver.IntVar(0, 1, 'main_main_mul83_enob_1')
main_main_mul83_enob_2 = solver.IntVar(0, 1, 'main_main_mul83_enob_2')
solver.Add( + (1)*main_main_mul83_enob_1 + (1)*main_main_mul83_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul83_enob + (-1)*main_sub82_enob + (-10000)*main_main_mul83_enob_1<=1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul83_enob + (-1)*ConstantValue__enob + (-10000)*main_main_mul83_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub84 = fsub double %tmp1, %mul83, !taffo.info !39, !taffo.initweight !33
ey_CAST_sub84_fixbits = solver.IntVar(0, 23, 'ey_CAST_sub84_fixbits')
ey_CAST_sub84_fixp = solver.IntVar(0, 1, 'ey_CAST_sub84_fixp')
ey_CAST_sub84_float = solver.IntVar(0, 1, 'ey_CAST_sub84_float')
ey_CAST_sub84_double = solver.IntVar(0, 1, 'ey_CAST_sub84_double')
solver.Add( + (1)*ey_CAST_sub84_fixp + (1)*ey_CAST_sub84_float + (1)*ey_CAST_sub84_double==1)    #exactly 1 type
solver.Add( + (1)*ey_CAST_sub84_fixbits + (-10000)*ey_CAST_sub84_fixp<=0)    #If no fix, fix frac part = 0
C1_ey_CAST_sub84 = solver.IntVar(0, 1, 'C1_ey_CAST_sub84')
C2_ey_CAST_sub84 = solver.IntVar(0, 1, 'C2_ey_CAST_sub84')
solver.Add( + (1)*ey_fixbits + (-1)*ey_CAST_sub84_fixbits + (-10000)*C1_ey_CAST_sub84<=0)    #Shift cost 1
solver.Add( + (-1)*ey_fixbits + (1)*ey_CAST_sub84_fixbits + (-10000)*C2_ey_CAST_sub84<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ey_CAST_sub84
castCostObj +=  + (1)*C2_ey_CAST_sub84
C3_ey_CAST_sub84 = solver.IntVar(0, 1, 'C3_ey_CAST_sub84')
C4_ey_CAST_sub84 = solver.IntVar(0, 1, 'C4_ey_CAST_sub84')
C5_ey_CAST_sub84 = solver.IntVar(0, 1, 'C5_ey_CAST_sub84')
C6_ey_CAST_sub84 = solver.IntVar(0, 1, 'C6_ey_CAST_sub84')
C7_ey_CAST_sub84 = solver.IntVar(0, 1, 'C7_ey_CAST_sub84')
C8_ey_CAST_sub84 = solver.IntVar(0, 1, 'C8_ey_CAST_sub84')
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_sub84_float + (-1)*C3_ey_CAST_sub84<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ey_CAST_sub84
solver.Add( + (1)*ey_float + (1)*ey_CAST_sub84_fixp + (-1)*C4_ey_CAST_sub84<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ey_CAST_sub84
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_sub84_double + (-1)*C5_ey_CAST_sub84<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ey_CAST_sub84
solver.Add( + (1)*ey_double + (1)*ey_CAST_sub84_fixp + (-1)*C6_ey_CAST_sub84<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ey_CAST_sub84
solver.Add( + (1)*ey_float + (1)*ey_CAST_sub84_double + (-1)*C7_ey_CAST_sub84<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ey_CAST_sub84
solver.Add( + (1)*ey_double + (1)*ey_CAST_sub84_float + (-1)*C8_ey_CAST_sub84<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ey_CAST_sub84



#Constraint for cast for   %sub84 = fsub double %tmp1, %mul83, !taffo.info !39, !taffo.initweight !33
main_mul83_CAST_sub84_fixbits = solver.IntVar(0, 23, 'main_mul83_CAST_sub84_fixbits')
main_mul83_CAST_sub84_fixp = solver.IntVar(0, 1, 'main_mul83_CAST_sub84_fixp')
main_mul83_CAST_sub84_float = solver.IntVar(0, 1, 'main_mul83_CAST_sub84_float')
main_mul83_CAST_sub84_double = solver.IntVar(0, 1, 'main_mul83_CAST_sub84_double')
solver.Add( + (1)*main_mul83_CAST_sub84_fixp + (1)*main_mul83_CAST_sub84_float + (1)*main_mul83_CAST_sub84_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul83_CAST_sub84_fixbits + (-10000)*main_mul83_CAST_sub84_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C1_main_mul83_CAST_sub84')
C2_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C2_main_mul83_CAST_sub84')
solver.Add( + (1)*main_mul83_fixbits + (-1)*main_mul83_CAST_sub84_fixbits + (-10000)*C1_main_mul83_CAST_sub84<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul83_fixbits + (1)*main_mul83_CAST_sub84_fixbits + (-10000)*C2_main_mul83_CAST_sub84<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul83_CAST_sub84
castCostObj +=  + (1)*C2_main_mul83_CAST_sub84
C3_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C3_main_mul83_CAST_sub84')
C4_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C4_main_mul83_CAST_sub84')
C5_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C5_main_mul83_CAST_sub84')
C6_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C6_main_mul83_CAST_sub84')
C7_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C7_main_mul83_CAST_sub84')
C8_main_mul83_CAST_sub84 = solver.IntVar(0, 1, 'C8_main_mul83_CAST_sub84')
solver.Add( + (1)*main_mul83_fixp + (1)*main_mul83_CAST_sub84_float + (-1)*C3_main_mul83_CAST_sub84<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul83_CAST_sub84
solver.Add( + (1)*main_mul83_float + (1)*main_mul83_CAST_sub84_fixp + (-1)*C4_main_mul83_CAST_sub84<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul83_CAST_sub84
solver.Add( + (1)*main_mul83_fixp + (1)*main_mul83_CAST_sub84_double + (-1)*C5_main_mul83_CAST_sub84<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul83_CAST_sub84
solver.Add( + (1)*main_mul83_double + (1)*main_mul83_CAST_sub84_fixp + (-1)*C6_main_mul83_CAST_sub84<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul83_CAST_sub84
solver.Add( + (1)*main_mul83_float + (1)*main_mul83_CAST_sub84_double + (-1)*C7_main_mul83_CAST_sub84<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul83_CAST_sub84
solver.Add( + (1)*main_mul83_double + (1)*main_mul83_CAST_sub84_float + (-1)*C8_main_mul83_CAST_sub84<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul83_CAST_sub84



#Stuff for   %sub84 = fsub double %tmp1, %mul83, !taffo.info !39, !taffo.initweight !33
main_sub84_fixbits = solver.IntVar(0, 22, 'main_sub84_fixbits')
main_sub84_fixp = solver.IntVar(0, 1, 'main_sub84_fixp')
main_sub84_float = solver.IntVar(0, 1, 'main_sub84_float')
main_sub84_double = solver.IntVar(0, 1, 'main_sub84_double')
main_sub84_enob = solver.IntVar(-10000, 10000, 'main_sub84_enob')
solver.Add( + (1)*main_sub84_enob + (-1)*main_sub84_fixbits + (10000)*main_sub84_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub84_enob + (10000)*main_sub84_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub84_enob + (10000)*main_sub84_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub84_fixbits + (-10000)*main_sub84_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_sub84_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub84_enob
solver.Add( + (1)*main_sub84_fixp + (1)*main_sub84_float + (1)*main_sub84_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub84_fixbits + (-10000)*main_sub84_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ey_CAST_sub84_fixp + (-1)*main_mul83_CAST_sub84_fixp==0)    #fix equality
solver.Add( + (1)*ey_CAST_sub84_float + (-1)*main_mul83_CAST_sub84_float==0)    #float equality
solver.Add( + (1)*ey_CAST_sub84_double + (-1)*main_mul83_CAST_sub84_double==0)    #double equality
solver.Add( + (1)*ey_CAST_sub84_fixbits + (-1)*main_mul83_CAST_sub84_fixbits==0)    #same fractional bit
solver.Add( + (1)*ey_CAST_sub84_fixp + (-1)*main_sub84_fixp==0)    #fix equality
solver.Add( + (1)*ey_CAST_sub84_float + (-1)*main_sub84_float==0)    #float equality
solver.Add( + (1)*ey_CAST_sub84_double + (-1)*main_sub84_double==0)    #double equality
solver.Add( + (1)*ey_CAST_sub84_fixbits + (-1)*main_sub84_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub84_fixp
mathCostObj +=  + (2.33125)*main_sub84_float
mathCostObj +=  + (2.72422)*main_sub84_double
solver.Add( + (1)*main_sub84_enob + (-1)*ey_enob_memphi_main_tmp1<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub84_enob + (-1)*main_mul83_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub84, double* %arrayidx88, align 8, !taffo.info !12, !taffo.initweight !22
main_sub84_CAST_store_fixbits = solver.IntVar(0, 22, 'main_sub84_CAST_store_fixbits')
main_sub84_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub84_CAST_store_fixp')
main_sub84_CAST_store_float = solver.IntVar(0, 1, 'main_sub84_CAST_store_float')
main_sub84_CAST_store_double = solver.IntVar(0, 1, 'main_sub84_CAST_store_double')
solver.Add( + (1)*main_sub84_CAST_store_fixp + (1)*main_sub84_CAST_store_float + (1)*main_sub84_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub84_CAST_store_fixbits + (-10000)*main_sub84_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub84_CAST_store = solver.IntVar(0, 1, 'C1_main_sub84_CAST_store')
C2_main_sub84_CAST_store = solver.IntVar(0, 1, 'C2_main_sub84_CAST_store')
solver.Add( + (1)*main_sub84_fixbits + (-1)*main_sub84_CAST_store_fixbits + (-10000)*C1_main_sub84_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub84_fixbits + (1)*main_sub84_CAST_store_fixbits + (-10000)*C2_main_sub84_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub84_CAST_store
castCostObj +=  + (1)*C2_main_sub84_CAST_store
C3_main_sub84_CAST_store = solver.IntVar(0, 1, 'C3_main_sub84_CAST_store')
C4_main_sub84_CAST_store = solver.IntVar(0, 1, 'C4_main_sub84_CAST_store')
C5_main_sub84_CAST_store = solver.IntVar(0, 1, 'C5_main_sub84_CAST_store')
C6_main_sub84_CAST_store = solver.IntVar(0, 1, 'C6_main_sub84_CAST_store')
C7_main_sub84_CAST_store = solver.IntVar(0, 1, 'C7_main_sub84_CAST_store')
C8_main_sub84_CAST_store = solver.IntVar(0, 1, 'C8_main_sub84_CAST_store')
solver.Add( + (1)*main_sub84_fixp + (1)*main_sub84_CAST_store_float + (-1)*C3_main_sub84_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub84_CAST_store
solver.Add( + (1)*main_sub84_float + (1)*main_sub84_CAST_store_fixp + (-1)*C4_main_sub84_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub84_CAST_store
solver.Add( + (1)*main_sub84_fixp + (1)*main_sub84_CAST_store_double + (-1)*C5_main_sub84_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub84_CAST_store
solver.Add( + (1)*main_sub84_double + (1)*main_sub84_CAST_store_fixp + (-1)*C6_main_sub84_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub84_CAST_store
solver.Add( + (1)*main_sub84_float + (1)*main_sub84_CAST_store_double + (-1)*C7_main_sub84_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub84_CAST_store
solver.Add( + (1)*main_sub84_double + (1)*main_sub84_CAST_store_float + (-1)*C8_main_sub84_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub84_CAST_store
solver.Add( + (1)*ey_fixp + (-1)*main_sub84_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*ey_float + (-1)*main_sub84_CAST_store_float==0)    #float equality
solver.Add( + (1)*ey_double + (-1)*main_sub84_CAST_store_double==0)    #double equality
solver.Add( + (1)*ey_fixbits + (-1)*main_sub84_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
ey_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'ey_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*ey_enob_storeENOB_storeENOB_storeENOB + (-1)*ey_fixbits + (10000)*ey_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*ey_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*ey_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ey_enob_storeENOB_storeENOB_storeENOB + (-1)*main_sub84_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp1 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp2 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp3 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
ex_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'ex_enob_memphi_main_tmp4')
solver.Add( + (1)*ex_enob_memphi_main_tmp4 + (-1)*ex_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
main_main_tmp4_enob_4 = solver.IntVar(0, 1, 'main_main_tmp4_enob_4')
main_main_tmp4_enob_5 = solver.IntVar(0, 1, 'main_main_tmp4_enob_5')
main_main_tmp4_enob_6 = solver.IntVar(0, 1, 'main_main_tmp4_enob_6')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3 + (1)*main_main_tmp4_enob_4 + (1)*main_main_tmp4_enob_5 + (1)*main_main_tmp4_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp4 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp4_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp4 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp4 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp4 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_5<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
hz_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'hz_enob_memphi_main_tmp5')
solver.Add( + (1)*hz_enob_memphi_main_tmp5 + (-1)*hz_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
main_main_tmp5_enob_4 = solver.IntVar(0, 1, 'main_main_tmp5_enob_4')
main_main_tmp5_enob_5 = solver.IntVar(0, 1, 'main_main_tmp5_enob_5')
main_main_tmp5_enob_6 = solver.IntVar(0, 1, 'main_main_tmp5_enob_6')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3 + (1)*main_main_tmp5_enob_4 + (1)*main_main_tmp5_enob_5 + (1)*main_main_tmp5_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp5 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp5_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp5 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp5_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp5 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp5 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
hz_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'hz_enob_memphi_main_tmp6')
solver.Add( + (1)*hz_enob_memphi_main_tmp6 + (-1)*hz_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
main_main_tmp6_enob_3 = solver.IntVar(0, 1, 'main_main_tmp6_enob_3')
main_main_tmp6_enob_4 = solver.IntVar(0, 1, 'main_main_tmp6_enob_4')
main_main_tmp6_enob_5 = solver.IntVar(0, 1, 'main_main_tmp6_enob_5')
main_main_tmp6_enob_6 = solver.IntVar(0, 1, 'main_main_tmp6_enob_6')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2 + (1)*main_main_tmp6_enob_3 + (1)*main_main_tmp6_enob_4 + (1)*main_main_tmp6_enob_5 + (1)*main_main_tmp6_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp6 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp6_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp6 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp6_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp6 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp6 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub116 = fsub double %tmp5, %tmp6, !taffo.info !39, !taffo.initweight !33
hz_CAST_sub116_fixbits = solver.IntVar(0, 23, 'hz_CAST_sub116_fixbits')
hz_CAST_sub116_fixp = solver.IntVar(0, 1, 'hz_CAST_sub116_fixp')
hz_CAST_sub116_float = solver.IntVar(0, 1, 'hz_CAST_sub116_float')
hz_CAST_sub116_double = solver.IntVar(0, 1, 'hz_CAST_sub116_double')
solver.Add( + (1)*hz_CAST_sub116_fixp + (1)*hz_CAST_sub116_float + (1)*hz_CAST_sub116_double==1)    #exactly 1 type
solver.Add( + (1)*hz_CAST_sub116_fixbits + (-10000)*hz_CAST_sub116_fixp<=0)    #If no fix, fix frac part = 0
C1_hz_CAST_sub116 = solver.IntVar(0, 1, 'C1_hz_CAST_sub116')
C2_hz_CAST_sub116 = solver.IntVar(0, 1, 'C2_hz_CAST_sub116')
solver.Add( + (1)*hz_fixbits + (-1)*hz_CAST_sub116_fixbits + (-10000)*C1_hz_CAST_sub116<=0)    #Shift cost 1
solver.Add( + (-1)*hz_fixbits + (1)*hz_CAST_sub116_fixbits + (-10000)*C2_hz_CAST_sub116<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_hz_CAST_sub116
castCostObj +=  + (1)*C2_hz_CAST_sub116
C3_hz_CAST_sub116 = solver.IntVar(0, 1, 'C3_hz_CAST_sub116')
C4_hz_CAST_sub116 = solver.IntVar(0, 1, 'C4_hz_CAST_sub116')
C5_hz_CAST_sub116 = solver.IntVar(0, 1, 'C5_hz_CAST_sub116')
C6_hz_CAST_sub116 = solver.IntVar(0, 1, 'C6_hz_CAST_sub116')
C7_hz_CAST_sub116 = solver.IntVar(0, 1, 'C7_hz_CAST_sub116')
C8_hz_CAST_sub116 = solver.IntVar(0, 1, 'C8_hz_CAST_sub116')
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub116_float + (-1)*C3_hz_CAST_sub116<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_hz_CAST_sub116
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub116_fixp + (-1)*C4_hz_CAST_sub116<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_hz_CAST_sub116
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub116_double + (-1)*C5_hz_CAST_sub116<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_hz_CAST_sub116
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub116_fixp + (-1)*C6_hz_CAST_sub116<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_hz_CAST_sub116
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub116_double + (-1)*C7_hz_CAST_sub116<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_hz_CAST_sub116
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub116_float + (-1)*C8_hz_CAST_sub116<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_hz_CAST_sub116



#Constraint for cast for   %sub116 = fsub double %tmp5, %tmp6, !taffo.info !39, !taffo.initweight !33
hz_CAST_sub116_0_fixbits = solver.IntVar(0, 23, 'hz_CAST_sub116_0_fixbits')
hz_CAST_sub116_0_fixp = solver.IntVar(0, 1, 'hz_CAST_sub116_0_fixp')
hz_CAST_sub116_0_float = solver.IntVar(0, 1, 'hz_CAST_sub116_0_float')
hz_CAST_sub116_0_double = solver.IntVar(0, 1, 'hz_CAST_sub116_0_double')
solver.Add( + (1)*hz_CAST_sub116_0_fixp + (1)*hz_CAST_sub116_0_float + (1)*hz_CAST_sub116_0_double==1)    #exactly 1 type
solver.Add( + (1)*hz_CAST_sub116_0_fixbits + (-10000)*hz_CAST_sub116_0_fixp<=0)    #If no fix, fix frac part = 0
C1_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C1_hz_CAST_sub116_0')
C2_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C2_hz_CAST_sub116_0')
solver.Add( + (1)*hz_fixbits + (-1)*hz_CAST_sub116_0_fixbits + (-10000)*C1_hz_CAST_sub116_0<=0)    #Shift cost 1
solver.Add( + (-1)*hz_fixbits + (1)*hz_CAST_sub116_0_fixbits + (-10000)*C2_hz_CAST_sub116_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_hz_CAST_sub116_0
castCostObj +=  + (1)*C2_hz_CAST_sub116_0
C3_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C3_hz_CAST_sub116_0')
C4_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C4_hz_CAST_sub116_0')
C5_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C5_hz_CAST_sub116_0')
C6_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C6_hz_CAST_sub116_0')
C7_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C7_hz_CAST_sub116_0')
C8_hz_CAST_sub116_0 = solver.IntVar(0, 1, 'C8_hz_CAST_sub116_0')
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub116_0_float + (-1)*C3_hz_CAST_sub116_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_hz_CAST_sub116_0
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub116_0_fixp + (-1)*C4_hz_CAST_sub116_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_hz_CAST_sub116_0
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub116_0_double + (-1)*C5_hz_CAST_sub116_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_hz_CAST_sub116_0
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub116_0_fixp + (-1)*C6_hz_CAST_sub116_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_hz_CAST_sub116_0
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub116_0_double + (-1)*C7_hz_CAST_sub116_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_hz_CAST_sub116_0
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub116_0_float + (-1)*C8_hz_CAST_sub116_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_hz_CAST_sub116_0



#Stuff for   %sub116 = fsub double %tmp5, %tmp6, !taffo.info !39, !taffo.initweight !33
main_sub116_fixbits = solver.IntVar(0, 22, 'main_sub116_fixbits')
main_sub116_fixp = solver.IntVar(0, 1, 'main_sub116_fixp')
main_sub116_float = solver.IntVar(0, 1, 'main_sub116_float')
main_sub116_double = solver.IntVar(0, 1, 'main_sub116_double')
main_sub116_enob = solver.IntVar(-10000, 10000, 'main_sub116_enob')
solver.Add( + (1)*main_sub116_enob + (-1)*main_sub116_fixbits + (10000)*main_sub116_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub116_enob + (10000)*main_sub116_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub116_enob + (10000)*main_sub116_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub116_fixbits + (-10000)*main_sub116_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_sub116_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub116_enob
solver.Add( + (1)*main_sub116_fixp + (1)*main_sub116_float + (1)*main_sub116_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub116_fixbits + (-10000)*main_sub116_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*hz_CAST_sub116_fixp + (-1)*hz_CAST_sub116_0_fixp==0)    #fix equality
solver.Add( + (1)*hz_CAST_sub116_float + (-1)*hz_CAST_sub116_0_float==0)    #float equality
solver.Add( + (1)*hz_CAST_sub116_double + (-1)*hz_CAST_sub116_0_double==0)    #double equality
solver.Add( + (1)*hz_CAST_sub116_fixbits + (-1)*hz_CAST_sub116_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*hz_CAST_sub116_fixp + (-1)*main_sub116_fixp==0)    #fix equality
solver.Add( + (1)*hz_CAST_sub116_float + (-1)*main_sub116_float==0)    #float equality
solver.Add( + (1)*hz_CAST_sub116_double + (-1)*main_sub116_double==0)    #double equality
solver.Add( + (1)*hz_CAST_sub116_fixbits + (-1)*main_sub116_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub116_fixp
mathCostObj +=  + (2.33125)*main_sub116_float
mathCostObj +=  + (2.72422)*main_sub116_double
solver.Add( + (1)*main_sub116_enob + (-1)*hz_enob_memphi_main_tmp5<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub116_enob + (-1)*hz_enob_memphi_main_tmp6<=0)    #Enob propagation in sub second addend



#Stuff for double 5.000000e-01
ConstantValue__2_fixbits = solver.IntVar(0, 31, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-01
ConstantValue__3_fixbits = solver.IntVar(0, 31, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-01
ConstantValue__4_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul117 = fmul double 5.000000e-01, %sub116, !taffo.info !12, !taffo.initweight !41, !taffo.constinfo !42
ConstantValue__4_CAST_mul117_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_CAST_mul117_fixbits')
ConstantValue__4_CAST_mul117_fixp = solver.IntVar(0, 1, 'ConstantValue__4_CAST_mul117_fixp')
ConstantValue__4_CAST_mul117_float = solver.IntVar(0, 1, 'ConstantValue__4_CAST_mul117_float')
ConstantValue__4_CAST_mul117_double = solver.IntVar(0, 1, 'ConstantValue__4_CAST_mul117_double')
solver.Add( + (1)*ConstantValue__4_CAST_mul117_fixp + (1)*ConstantValue__4_CAST_mul117_float + (1)*ConstantValue__4_CAST_mul117_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__4_CAST_mul117_fixbits + (-10000)*ConstantValue__4_CAST_mul117_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C1_ConstantValue__4_CAST_mul117')
C2_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C2_ConstantValue__4_CAST_mul117')
solver.Add( + (1)*ConstantValue__4_fixbits + (-1)*ConstantValue__4_CAST_mul117_fixbits + (-10000)*C1_ConstantValue__4_CAST_mul117<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__4_fixbits + (1)*ConstantValue__4_CAST_mul117_fixbits + (-10000)*C2_ConstantValue__4_CAST_mul117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__4_CAST_mul117
castCostObj +=  + (1)*C2_ConstantValue__4_CAST_mul117
C3_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_mul117')
C4_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_mul117')
C5_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_mul117')
C6_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_mul117')
C7_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_mul117')
C8_ConstantValue__4_CAST_mul117 = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_mul117')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_mul117_float + (-1)*C3_ConstantValue__4_CAST_mul117<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__4_CAST_mul117
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_mul117_fixp + (-1)*C4_ConstantValue__4_CAST_mul117<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__4_CAST_mul117
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_mul117_double + (-1)*C5_ConstantValue__4_CAST_mul117<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__4_CAST_mul117
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_mul117_fixp + (-1)*C6_ConstantValue__4_CAST_mul117<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__4_CAST_mul117
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_mul117_double + (-1)*C7_ConstantValue__4_CAST_mul117<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__4_CAST_mul117
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_mul117_float + (-1)*C8_ConstantValue__4_CAST_mul117<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__4_CAST_mul117



#Constraint for cast for   %mul117 = fmul double 5.000000e-01, %sub116, !taffo.info !12, !taffo.initweight !41, !taffo.constinfo !42
main_sub116_CAST_mul117_fixbits = solver.IntVar(0, 22, 'main_sub116_CAST_mul117_fixbits')
main_sub116_CAST_mul117_fixp = solver.IntVar(0, 1, 'main_sub116_CAST_mul117_fixp')
main_sub116_CAST_mul117_float = solver.IntVar(0, 1, 'main_sub116_CAST_mul117_float')
main_sub116_CAST_mul117_double = solver.IntVar(0, 1, 'main_sub116_CAST_mul117_double')
solver.Add( + (1)*main_sub116_CAST_mul117_fixp + (1)*main_sub116_CAST_mul117_float + (1)*main_sub116_CAST_mul117_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub116_CAST_mul117_fixbits + (-10000)*main_sub116_CAST_mul117_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C1_main_sub116_CAST_mul117')
C2_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C2_main_sub116_CAST_mul117')
solver.Add( + (1)*main_sub116_fixbits + (-1)*main_sub116_CAST_mul117_fixbits + (-10000)*C1_main_sub116_CAST_mul117<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub116_fixbits + (1)*main_sub116_CAST_mul117_fixbits + (-10000)*C2_main_sub116_CAST_mul117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub116_CAST_mul117
castCostObj +=  + (1)*C2_main_sub116_CAST_mul117
C3_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C3_main_sub116_CAST_mul117')
C4_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C4_main_sub116_CAST_mul117')
C5_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C5_main_sub116_CAST_mul117')
C6_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C6_main_sub116_CAST_mul117')
C7_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C7_main_sub116_CAST_mul117')
C8_main_sub116_CAST_mul117 = solver.IntVar(0, 1, 'C8_main_sub116_CAST_mul117')
solver.Add( + (1)*main_sub116_fixp + (1)*main_sub116_CAST_mul117_float + (-1)*C3_main_sub116_CAST_mul117<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub116_CAST_mul117
solver.Add( + (1)*main_sub116_float + (1)*main_sub116_CAST_mul117_fixp + (-1)*C4_main_sub116_CAST_mul117<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub116_CAST_mul117
solver.Add( + (1)*main_sub116_fixp + (1)*main_sub116_CAST_mul117_double + (-1)*C5_main_sub116_CAST_mul117<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub116_CAST_mul117
solver.Add( + (1)*main_sub116_double + (1)*main_sub116_CAST_mul117_fixp + (-1)*C6_main_sub116_CAST_mul117<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub116_CAST_mul117
solver.Add( + (1)*main_sub116_float + (1)*main_sub116_CAST_mul117_double + (-1)*C7_main_sub116_CAST_mul117<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub116_CAST_mul117
solver.Add( + (1)*main_sub116_double + (1)*main_sub116_CAST_mul117_float + (-1)*C8_main_sub116_CAST_mul117<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub116_CAST_mul117



#Stuff for   %mul117 = fmul double 5.000000e-01, %sub116, !taffo.info !12, !taffo.initweight !41, !taffo.constinfo !42
main_mul117_fixbits = solver.IntVar(0, 23, 'main_mul117_fixbits')
main_mul117_fixp = solver.IntVar(0, 1, 'main_mul117_fixp')
main_mul117_float = solver.IntVar(0, 1, 'main_mul117_float')
main_mul117_double = solver.IntVar(0, 1, 'main_mul117_double')
main_mul117_enob = solver.IntVar(-10000, 10000, 'main_mul117_enob')
solver.Add( + (1)*main_mul117_enob + (-1)*main_mul117_fixbits + (10000)*main_mul117_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul117_enob + (10000)*main_mul117_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul117_enob + (10000)*main_mul117_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul117_fixbits + (-10000)*main_mul117_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_mul117_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul117_enob
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_float + (1)*main_mul117_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul117_fixbits + (-10000)*main_mul117_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__4_CAST_mul117_fixp + (-1)*main_sub116_CAST_mul117_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__4_CAST_mul117_float + (-1)*main_sub116_CAST_mul117_float==0)    #float equality
solver.Add( + (1)*ConstantValue__4_CAST_mul117_double + (-1)*main_sub116_CAST_mul117_double==0)    #double equality
solver.Add( + (1)*ConstantValue__4_CAST_mul117_fixp + (-1)*main_mul117_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__4_CAST_mul117_float + (-1)*main_mul117_float==0)    #float equality
solver.Add( + (1)*ConstantValue__4_CAST_mul117_double + (-1)*main_mul117_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul117_fixp
mathCostObj +=  + (2.64722)*main_mul117_float
mathCostObj +=  + (4.02255)*main_mul117_double
main_main_mul117_enob_1 = solver.IntVar(0, 1, 'main_main_mul117_enob_1')
main_main_mul117_enob_2 = solver.IntVar(0, 1, 'main_main_mul117_enob_2')
solver.Add( + (1)*main_main_mul117_enob_1 + (1)*main_main_mul117_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul117_enob + (-1)*main_sub116_enob + (-10000)*main_main_mul117_enob_1<=1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul117_enob + (-1)*ConstantValue__2_enob + (-10000)*main_main_mul117_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub118 = fsub double %tmp4, %mul117, !taffo.info !39, !taffo.initweight !33
ex_CAST_sub118_fixbits = solver.IntVar(0, 23, 'ex_CAST_sub118_fixbits')
ex_CAST_sub118_fixp = solver.IntVar(0, 1, 'ex_CAST_sub118_fixp')
ex_CAST_sub118_float = solver.IntVar(0, 1, 'ex_CAST_sub118_float')
ex_CAST_sub118_double = solver.IntVar(0, 1, 'ex_CAST_sub118_double')
solver.Add( + (1)*ex_CAST_sub118_fixp + (1)*ex_CAST_sub118_float + (1)*ex_CAST_sub118_double==1)    #exactly 1 type
solver.Add( + (1)*ex_CAST_sub118_fixbits + (-10000)*ex_CAST_sub118_fixp<=0)    #If no fix, fix frac part = 0
C1_ex_CAST_sub118 = solver.IntVar(0, 1, 'C1_ex_CAST_sub118')
C2_ex_CAST_sub118 = solver.IntVar(0, 1, 'C2_ex_CAST_sub118')
solver.Add( + (1)*ex_fixbits + (-1)*ex_CAST_sub118_fixbits + (-10000)*C1_ex_CAST_sub118<=0)    #Shift cost 1
solver.Add( + (-1)*ex_fixbits + (1)*ex_CAST_sub118_fixbits + (-10000)*C2_ex_CAST_sub118<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ex_CAST_sub118
castCostObj +=  + (1)*C2_ex_CAST_sub118
C3_ex_CAST_sub118 = solver.IntVar(0, 1, 'C3_ex_CAST_sub118')
C4_ex_CAST_sub118 = solver.IntVar(0, 1, 'C4_ex_CAST_sub118')
C5_ex_CAST_sub118 = solver.IntVar(0, 1, 'C5_ex_CAST_sub118')
C6_ex_CAST_sub118 = solver.IntVar(0, 1, 'C6_ex_CAST_sub118')
C7_ex_CAST_sub118 = solver.IntVar(0, 1, 'C7_ex_CAST_sub118')
C8_ex_CAST_sub118 = solver.IntVar(0, 1, 'C8_ex_CAST_sub118')
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_sub118_float + (-1)*C3_ex_CAST_sub118<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ex_CAST_sub118
solver.Add( + (1)*ex_float + (1)*ex_CAST_sub118_fixp + (-1)*C4_ex_CAST_sub118<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ex_CAST_sub118
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_sub118_double + (-1)*C5_ex_CAST_sub118<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ex_CAST_sub118
solver.Add( + (1)*ex_double + (1)*ex_CAST_sub118_fixp + (-1)*C6_ex_CAST_sub118<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ex_CAST_sub118
solver.Add( + (1)*ex_float + (1)*ex_CAST_sub118_double + (-1)*C7_ex_CAST_sub118<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ex_CAST_sub118
solver.Add( + (1)*ex_double + (1)*ex_CAST_sub118_float + (-1)*C8_ex_CAST_sub118<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ex_CAST_sub118



#Constraint for cast for   %sub118 = fsub double %tmp4, %mul117, !taffo.info !39, !taffo.initweight !33
main_mul117_CAST_sub118_fixbits = solver.IntVar(0, 23, 'main_mul117_CAST_sub118_fixbits')
main_mul117_CAST_sub118_fixp = solver.IntVar(0, 1, 'main_mul117_CAST_sub118_fixp')
main_mul117_CAST_sub118_float = solver.IntVar(0, 1, 'main_mul117_CAST_sub118_float')
main_mul117_CAST_sub118_double = solver.IntVar(0, 1, 'main_mul117_CAST_sub118_double')
solver.Add( + (1)*main_mul117_CAST_sub118_fixp + (1)*main_mul117_CAST_sub118_float + (1)*main_mul117_CAST_sub118_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul117_CAST_sub118_fixbits + (-10000)*main_mul117_CAST_sub118_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C1_main_mul117_CAST_sub118')
C2_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C2_main_mul117_CAST_sub118')
solver.Add( + (1)*main_mul117_fixbits + (-1)*main_mul117_CAST_sub118_fixbits + (-10000)*C1_main_mul117_CAST_sub118<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul117_fixbits + (1)*main_mul117_CAST_sub118_fixbits + (-10000)*C2_main_mul117_CAST_sub118<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul117_CAST_sub118
castCostObj +=  + (1)*C2_main_mul117_CAST_sub118
C3_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C3_main_mul117_CAST_sub118')
C4_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C4_main_mul117_CAST_sub118')
C5_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C5_main_mul117_CAST_sub118')
C6_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C6_main_mul117_CAST_sub118')
C7_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C7_main_mul117_CAST_sub118')
C8_main_mul117_CAST_sub118 = solver.IntVar(0, 1, 'C8_main_mul117_CAST_sub118')
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_CAST_sub118_float + (-1)*C3_main_mul117_CAST_sub118<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul117_CAST_sub118
solver.Add( + (1)*main_mul117_float + (1)*main_mul117_CAST_sub118_fixp + (-1)*C4_main_mul117_CAST_sub118<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul117_CAST_sub118
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_CAST_sub118_double + (-1)*C5_main_mul117_CAST_sub118<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul117_CAST_sub118
solver.Add( + (1)*main_mul117_double + (1)*main_mul117_CAST_sub118_fixp + (-1)*C6_main_mul117_CAST_sub118<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul117_CAST_sub118
solver.Add( + (1)*main_mul117_float + (1)*main_mul117_CAST_sub118_double + (-1)*C7_main_mul117_CAST_sub118<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul117_CAST_sub118
solver.Add( + (1)*main_mul117_double + (1)*main_mul117_CAST_sub118_float + (-1)*C8_main_mul117_CAST_sub118<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul117_CAST_sub118



#Stuff for   %sub118 = fsub double %tmp4, %mul117, !taffo.info !39, !taffo.initweight !33
main_sub118_fixbits = solver.IntVar(0, 22, 'main_sub118_fixbits')
main_sub118_fixp = solver.IntVar(0, 1, 'main_sub118_fixp')
main_sub118_float = solver.IntVar(0, 1, 'main_sub118_float')
main_sub118_double = solver.IntVar(0, 1, 'main_sub118_double')
main_sub118_enob = solver.IntVar(-10000, 10000, 'main_sub118_enob')
solver.Add( + (1)*main_sub118_enob + (-1)*main_sub118_fixbits + (10000)*main_sub118_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub118_enob + (10000)*main_sub118_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub118_enob + (10000)*main_sub118_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub118_fixbits + (-10000)*main_sub118_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_sub118_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub118_enob
solver.Add( + (1)*main_sub118_fixp + (1)*main_sub118_float + (1)*main_sub118_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub118_fixbits + (-10000)*main_sub118_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ex_CAST_sub118_fixp + (-1)*main_mul117_CAST_sub118_fixp==0)    #fix equality
solver.Add( + (1)*ex_CAST_sub118_float + (-1)*main_mul117_CAST_sub118_float==0)    #float equality
solver.Add( + (1)*ex_CAST_sub118_double + (-1)*main_mul117_CAST_sub118_double==0)    #double equality
solver.Add( + (1)*ex_CAST_sub118_fixbits + (-1)*main_mul117_CAST_sub118_fixbits==0)    #same fractional bit
solver.Add( + (1)*ex_CAST_sub118_fixp + (-1)*main_sub118_fixp==0)    #fix equality
solver.Add( + (1)*ex_CAST_sub118_float + (-1)*main_sub118_float==0)    #float equality
solver.Add( + (1)*ex_CAST_sub118_double + (-1)*main_sub118_double==0)    #double equality
solver.Add( + (1)*ex_CAST_sub118_fixbits + (-1)*main_sub118_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub118_fixp
mathCostObj +=  + (2.33125)*main_sub118_float
mathCostObj +=  + (2.72422)*main_sub118_double
solver.Add( + (1)*main_sub118_enob + (-1)*ex_enob_memphi_main_tmp4<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub118_enob + (-1)*main_mul117_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub118, double* %arrayidx122, align 8, !taffo.info !12, !taffo.initweight !22
main_sub118_CAST_store_fixbits = solver.IntVar(0, 22, 'main_sub118_CAST_store_fixbits')
main_sub118_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub118_CAST_store_fixp')
main_sub118_CAST_store_float = solver.IntVar(0, 1, 'main_sub118_CAST_store_float')
main_sub118_CAST_store_double = solver.IntVar(0, 1, 'main_sub118_CAST_store_double')
solver.Add( + (1)*main_sub118_CAST_store_fixp + (1)*main_sub118_CAST_store_float + (1)*main_sub118_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub118_CAST_store_fixbits + (-10000)*main_sub118_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub118_CAST_store = solver.IntVar(0, 1, 'C1_main_sub118_CAST_store')
C2_main_sub118_CAST_store = solver.IntVar(0, 1, 'C2_main_sub118_CAST_store')
solver.Add( + (1)*main_sub118_fixbits + (-1)*main_sub118_CAST_store_fixbits + (-10000)*C1_main_sub118_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub118_fixbits + (1)*main_sub118_CAST_store_fixbits + (-10000)*C2_main_sub118_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub118_CAST_store
castCostObj +=  + (1)*C2_main_sub118_CAST_store
C3_main_sub118_CAST_store = solver.IntVar(0, 1, 'C3_main_sub118_CAST_store')
C4_main_sub118_CAST_store = solver.IntVar(0, 1, 'C4_main_sub118_CAST_store')
C5_main_sub118_CAST_store = solver.IntVar(0, 1, 'C5_main_sub118_CAST_store')
C6_main_sub118_CAST_store = solver.IntVar(0, 1, 'C6_main_sub118_CAST_store')
C7_main_sub118_CAST_store = solver.IntVar(0, 1, 'C7_main_sub118_CAST_store')
C8_main_sub118_CAST_store = solver.IntVar(0, 1, 'C8_main_sub118_CAST_store')
solver.Add( + (1)*main_sub118_fixp + (1)*main_sub118_CAST_store_float + (-1)*C3_main_sub118_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub118_CAST_store
solver.Add( + (1)*main_sub118_float + (1)*main_sub118_CAST_store_fixp + (-1)*C4_main_sub118_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub118_CAST_store
solver.Add( + (1)*main_sub118_fixp + (1)*main_sub118_CAST_store_double + (-1)*C5_main_sub118_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub118_CAST_store
solver.Add( + (1)*main_sub118_double + (1)*main_sub118_CAST_store_fixp + (-1)*C6_main_sub118_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub118_CAST_store
solver.Add( + (1)*main_sub118_float + (1)*main_sub118_CAST_store_double + (-1)*C7_main_sub118_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub118_CAST_store
solver.Add( + (1)*main_sub118_double + (1)*main_sub118_CAST_store_float + (-1)*C8_main_sub118_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub118_CAST_store
solver.Add( + (1)*ex_fixp + (-1)*main_sub118_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*ex_float + (-1)*main_sub118_CAST_store_float==0)    #float equality
solver.Add( + (1)*ex_double + (-1)*main_sub118_CAST_store_double==0)    #double equality
solver.Add( + (1)*ex_fixbits + (-1)*main_sub118_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
ex_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'ex_enob_storeENOB_storeENOB')
solver.Add( + (1)*ex_enob_storeENOB_storeENOB + (-1)*ex_fixbits + (10000)*ex_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ex_enob_storeENOB_storeENOB + (10000)*ex_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ex_enob_storeENOB_storeENOB + (10000)*ex_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ex_enob_storeENOB_storeENOB + (-1)*main_sub118_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp1 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp2 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp3 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp4 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp5 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp6 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_5<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
hz_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'hz_enob_memphi_main_tmp7')
solver.Add( + (1)*hz_enob_memphi_main_tmp7 + (-1)*hz_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
main_main_tmp7_enob_2 = solver.IntVar(0, 1, 'main_main_tmp7_enob_2')
main_main_tmp7_enob_3 = solver.IntVar(0, 1, 'main_main_tmp7_enob_3')
main_main_tmp7_enob_4 = solver.IntVar(0, 1, 'main_main_tmp7_enob_4')
main_main_tmp7_enob_5 = solver.IntVar(0, 1, 'main_main_tmp7_enob_5')
main_main_tmp7_enob_6 = solver.IntVar(0, 1, 'main_main_tmp7_enob_6')
solver.Add( + (1)*main_main_tmp7_enob_1 + (1)*main_main_tmp7_enob_2 + (1)*main_main_tmp7_enob_3 + (1)*main_main_tmp7_enob_4 + (1)*main_main_tmp7_enob_5 + (1)*main_main_tmp7_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp7 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp7 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp7_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp7 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp7 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp7 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_5<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
ex_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'ex_enob_memphi_main_tmp8')
solver.Add( + (1)*ex_enob_memphi_main_tmp8 + (-1)*ex_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
main_main_tmp8_enob_2 = solver.IntVar(0, 1, 'main_main_tmp8_enob_2')
main_main_tmp8_enob_3 = solver.IntVar(0, 1, 'main_main_tmp8_enob_3')
main_main_tmp8_enob_4 = solver.IntVar(0, 1, 'main_main_tmp8_enob_4')
main_main_tmp8_enob_5 = solver.IntVar(0, 1, 'main_main_tmp8_enob_5')
main_main_tmp8_enob_6 = solver.IntVar(0, 1, 'main_main_tmp8_enob_6')
solver.Add( + (1)*main_main_tmp8_enob_1 + (1)*main_main_tmp8_enob_2 + (1)*main_main_tmp8_enob_3 + (1)*main_main_tmp8_enob_4 + (1)*main_main_tmp8_enob_5 + (1)*main_main_tmp8_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp8 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp8 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp8_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp8 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp8 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp8 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_6<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
ex_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'ex_enob_memphi_main_tmp9')
solver.Add( + (1)*ex_enob_memphi_main_tmp9 + (-1)*ex_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_1 = solver.IntVar(0, 1, 'main_main_tmp9_enob_1')
main_main_tmp9_enob_2 = solver.IntVar(0, 1, 'main_main_tmp9_enob_2')
main_main_tmp9_enob_3 = solver.IntVar(0, 1, 'main_main_tmp9_enob_3')
main_main_tmp9_enob_4 = solver.IntVar(0, 1, 'main_main_tmp9_enob_4')
main_main_tmp9_enob_5 = solver.IntVar(0, 1, 'main_main_tmp9_enob_5')
main_main_tmp9_enob_6 = solver.IntVar(0, 1, 'main_main_tmp9_enob_6')
solver.Add( + (1)*main_main_tmp9_enob_1 + (1)*main_main_tmp9_enob_2 + (1)*main_main_tmp9_enob_3 + (1)*main_main_tmp9_enob_4 + (1)*main_main_tmp9_enob_5 + (1)*main_main_tmp9_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp9 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp9_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp9 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp9_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp9 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp9 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp9 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_6<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub150 = fsub double %tmp8, %tmp9, !taffo.info !39, !taffo.initweight !33
ex_CAST_sub150_fixbits = solver.IntVar(0, 23, 'ex_CAST_sub150_fixbits')
ex_CAST_sub150_fixp = solver.IntVar(0, 1, 'ex_CAST_sub150_fixp')
ex_CAST_sub150_float = solver.IntVar(0, 1, 'ex_CAST_sub150_float')
ex_CAST_sub150_double = solver.IntVar(0, 1, 'ex_CAST_sub150_double')
solver.Add( + (1)*ex_CAST_sub150_fixp + (1)*ex_CAST_sub150_float + (1)*ex_CAST_sub150_double==1)    #exactly 1 type
solver.Add( + (1)*ex_CAST_sub150_fixbits + (-10000)*ex_CAST_sub150_fixp<=0)    #If no fix, fix frac part = 0
C1_ex_CAST_sub150 = solver.IntVar(0, 1, 'C1_ex_CAST_sub150')
C2_ex_CAST_sub150 = solver.IntVar(0, 1, 'C2_ex_CAST_sub150')
solver.Add( + (1)*ex_fixbits + (-1)*ex_CAST_sub150_fixbits + (-10000)*C1_ex_CAST_sub150<=0)    #Shift cost 1
solver.Add( + (-1)*ex_fixbits + (1)*ex_CAST_sub150_fixbits + (-10000)*C2_ex_CAST_sub150<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ex_CAST_sub150
castCostObj +=  + (1)*C2_ex_CAST_sub150
C3_ex_CAST_sub150 = solver.IntVar(0, 1, 'C3_ex_CAST_sub150')
C4_ex_CAST_sub150 = solver.IntVar(0, 1, 'C4_ex_CAST_sub150')
C5_ex_CAST_sub150 = solver.IntVar(0, 1, 'C5_ex_CAST_sub150')
C6_ex_CAST_sub150 = solver.IntVar(0, 1, 'C6_ex_CAST_sub150')
C7_ex_CAST_sub150 = solver.IntVar(0, 1, 'C7_ex_CAST_sub150')
C8_ex_CAST_sub150 = solver.IntVar(0, 1, 'C8_ex_CAST_sub150')
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_sub150_float + (-1)*C3_ex_CAST_sub150<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ex_CAST_sub150
solver.Add( + (1)*ex_float + (1)*ex_CAST_sub150_fixp + (-1)*C4_ex_CAST_sub150<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ex_CAST_sub150
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_sub150_double + (-1)*C5_ex_CAST_sub150<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ex_CAST_sub150
solver.Add( + (1)*ex_double + (1)*ex_CAST_sub150_fixp + (-1)*C6_ex_CAST_sub150<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ex_CAST_sub150
solver.Add( + (1)*ex_float + (1)*ex_CAST_sub150_double + (-1)*C7_ex_CAST_sub150<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ex_CAST_sub150
solver.Add( + (1)*ex_double + (1)*ex_CAST_sub150_float + (-1)*C8_ex_CAST_sub150<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ex_CAST_sub150



#Constraint for cast for   %sub150 = fsub double %tmp8, %tmp9, !taffo.info !39, !taffo.initweight !33
ex_CAST_sub150_0_fixbits = solver.IntVar(0, 23, 'ex_CAST_sub150_0_fixbits')
ex_CAST_sub150_0_fixp = solver.IntVar(0, 1, 'ex_CAST_sub150_0_fixp')
ex_CAST_sub150_0_float = solver.IntVar(0, 1, 'ex_CAST_sub150_0_float')
ex_CAST_sub150_0_double = solver.IntVar(0, 1, 'ex_CAST_sub150_0_double')
solver.Add( + (1)*ex_CAST_sub150_0_fixp + (1)*ex_CAST_sub150_0_float + (1)*ex_CAST_sub150_0_double==1)    #exactly 1 type
solver.Add( + (1)*ex_CAST_sub150_0_fixbits + (-10000)*ex_CAST_sub150_0_fixp<=0)    #If no fix, fix frac part = 0
C1_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C1_ex_CAST_sub150_0')
C2_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C2_ex_CAST_sub150_0')
solver.Add( + (1)*ex_fixbits + (-1)*ex_CAST_sub150_0_fixbits + (-10000)*C1_ex_CAST_sub150_0<=0)    #Shift cost 1
solver.Add( + (-1)*ex_fixbits + (1)*ex_CAST_sub150_0_fixbits + (-10000)*C2_ex_CAST_sub150_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ex_CAST_sub150_0
castCostObj +=  + (1)*C2_ex_CAST_sub150_0
C3_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C3_ex_CAST_sub150_0')
C4_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C4_ex_CAST_sub150_0')
C5_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C5_ex_CAST_sub150_0')
C6_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C6_ex_CAST_sub150_0')
C7_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C7_ex_CAST_sub150_0')
C8_ex_CAST_sub150_0 = solver.IntVar(0, 1, 'C8_ex_CAST_sub150_0')
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_sub150_0_float + (-1)*C3_ex_CAST_sub150_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ex_CAST_sub150_0
solver.Add( + (1)*ex_float + (1)*ex_CAST_sub150_0_fixp + (-1)*C4_ex_CAST_sub150_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ex_CAST_sub150_0
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_sub150_0_double + (-1)*C5_ex_CAST_sub150_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ex_CAST_sub150_0
solver.Add( + (1)*ex_double + (1)*ex_CAST_sub150_0_fixp + (-1)*C6_ex_CAST_sub150_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ex_CAST_sub150_0
solver.Add( + (1)*ex_float + (1)*ex_CAST_sub150_0_double + (-1)*C7_ex_CAST_sub150_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ex_CAST_sub150_0
solver.Add( + (1)*ex_double + (1)*ex_CAST_sub150_0_float + (-1)*C8_ex_CAST_sub150_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ex_CAST_sub150_0



#Stuff for   %sub150 = fsub double %tmp8, %tmp9, !taffo.info !39, !taffo.initweight !33
main_sub150_fixbits = solver.IntVar(0, 22, 'main_sub150_fixbits')
main_sub150_fixp = solver.IntVar(0, 1, 'main_sub150_fixp')
main_sub150_float = solver.IntVar(0, 1, 'main_sub150_float')
main_sub150_double = solver.IntVar(0, 1, 'main_sub150_double')
main_sub150_enob = solver.IntVar(-10000, 10000, 'main_sub150_enob')
solver.Add( + (1)*main_sub150_enob + (-1)*main_sub150_fixbits + (10000)*main_sub150_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub150_enob + (10000)*main_sub150_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub150_enob + (10000)*main_sub150_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub150_fixbits + (-10000)*main_sub150_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_sub150_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub150_enob
solver.Add( + (1)*main_sub150_fixp + (1)*main_sub150_float + (1)*main_sub150_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub150_fixbits + (-10000)*main_sub150_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ex_CAST_sub150_fixp + (-1)*ex_CAST_sub150_0_fixp==0)    #fix equality
solver.Add( + (1)*ex_CAST_sub150_float + (-1)*ex_CAST_sub150_0_float==0)    #float equality
solver.Add( + (1)*ex_CAST_sub150_double + (-1)*ex_CAST_sub150_0_double==0)    #double equality
solver.Add( + (1)*ex_CAST_sub150_fixbits + (-1)*ex_CAST_sub150_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*ex_CAST_sub150_fixp + (-1)*main_sub150_fixp==0)    #fix equality
solver.Add( + (1)*ex_CAST_sub150_float + (-1)*main_sub150_float==0)    #float equality
solver.Add( + (1)*ex_CAST_sub150_double + (-1)*main_sub150_double==0)    #double equality
solver.Add( + (1)*ex_CAST_sub150_fixbits + (-1)*main_sub150_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub150_fixp
mathCostObj +=  + (2.33125)*main_sub150_float
mathCostObj +=  + (2.72422)*main_sub150_double
solver.Add( + (1)*main_sub150_enob + (-1)*ex_enob_memphi_main_tmp8<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub150_enob + (-1)*ex_enob_memphi_main_tmp9<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
ey_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'ey_enob_memphi_main_tmp10')
solver.Add( + (1)*ey_enob_memphi_main_tmp10 + (-1)*ey_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_1 = solver.IntVar(0, 1, 'main_main_tmp10_enob_1')
main_main_tmp10_enob_2 = solver.IntVar(0, 1, 'main_main_tmp10_enob_2')
main_main_tmp10_enob_3 = solver.IntVar(0, 1, 'main_main_tmp10_enob_3')
main_main_tmp10_enob_4 = solver.IntVar(0, 1, 'main_main_tmp10_enob_4')
main_main_tmp10_enob_5 = solver.IntVar(0, 1, 'main_main_tmp10_enob_5')
main_main_tmp10_enob_6 = solver.IntVar(0, 1, 'main_main_tmp10_enob_6')
solver.Add( + (1)*main_main_tmp10_enob_1 + (1)*main_main_tmp10_enob_2 + (1)*main_main_tmp10_enob_3 + (1)*main_main_tmp10_enob_4 + (1)*main_main_tmp10_enob_5 + (1)*main_main_tmp10_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp10 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp10_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp10 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp10_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp10 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp10 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp10 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_6<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add156 = fadd double %sub150, %tmp10, !taffo.info !45, !taffo.initweight !33
main_sub150_CAST_add156_fixbits = solver.IntVar(0, 22, 'main_sub150_CAST_add156_fixbits')
main_sub150_CAST_add156_fixp = solver.IntVar(0, 1, 'main_sub150_CAST_add156_fixp')
main_sub150_CAST_add156_float = solver.IntVar(0, 1, 'main_sub150_CAST_add156_float')
main_sub150_CAST_add156_double = solver.IntVar(0, 1, 'main_sub150_CAST_add156_double')
solver.Add( + (1)*main_sub150_CAST_add156_fixp + (1)*main_sub150_CAST_add156_float + (1)*main_sub150_CAST_add156_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub150_CAST_add156_fixbits + (-10000)*main_sub150_CAST_add156_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C1_main_sub150_CAST_add156')
C2_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C2_main_sub150_CAST_add156')
solver.Add( + (1)*main_sub150_fixbits + (-1)*main_sub150_CAST_add156_fixbits + (-10000)*C1_main_sub150_CAST_add156<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub150_fixbits + (1)*main_sub150_CAST_add156_fixbits + (-10000)*C2_main_sub150_CAST_add156<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub150_CAST_add156
castCostObj +=  + (1)*C2_main_sub150_CAST_add156
C3_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C3_main_sub150_CAST_add156')
C4_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C4_main_sub150_CAST_add156')
C5_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C5_main_sub150_CAST_add156')
C6_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C6_main_sub150_CAST_add156')
C7_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C7_main_sub150_CAST_add156')
C8_main_sub150_CAST_add156 = solver.IntVar(0, 1, 'C8_main_sub150_CAST_add156')
solver.Add( + (1)*main_sub150_fixp + (1)*main_sub150_CAST_add156_float + (-1)*C3_main_sub150_CAST_add156<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub150_CAST_add156
solver.Add( + (1)*main_sub150_float + (1)*main_sub150_CAST_add156_fixp + (-1)*C4_main_sub150_CAST_add156<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub150_CAST_add156
solver.Add( + (1)*main_sub150_fixp + (1)*main_sub150_CAST_add156_double + (-1)*C5_main_sub150_CAST_add156<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub150_CAST_add156
solver.Add( + (1)*main_sub150_double + (1)*main_sub150_CAST_add156_fixp + (-1)*C6_main_sub150_CAST_add156<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub150_CAST_add156
solver.Add( + (1)*main_sub150_float + (1)*main_sub150_CAST_add156_double + (-1)*C7_main_sub150_CAST_add156<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub150_CAST_add156
solver.Add( + (1)*main_sub150_double + (1)*main_sub150_CAST_add156_float + (-1)*C8_main_sub150_CAST_add156<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub150_CAST_add156



#Constraint for cast for   %add156 = fadd double %sub150, %tmp10, !taffo.info !45, !taffo.initweight !33
ey_CAST_add156_fixbits = solver.IntVar(0, 23, 'ey_CAST_add156_fixbits')
ey_CAST_add156_fixp = solver.IntVar(0, 1, 'ey_CAST_add156_fixp')
ey_CAST_add156_float = solver.IntVar(0, 1, 'ey_CAST_add156_float')
ey_CAST_add156_double = solver.IntVar(0, 1, 'ey_CAST_add156_double')
solver.Add( + (1)*ey_CAST_add156_fixp + (1)*ey_CAST_add156_float + (1)*ey_CAST_add156_double==1)    #exactly 1 type
solver.Add( + (1)*ey_CAST_add156_fixbits + (-10000)*ey_CAST_add156_fixp<=0)    #If no fix, fix frac part = 0
C1_ey_CAST_add156 = solver.IntVar(0, 1, 'C1_ey_CAST_add156')
C2_ey_CAST_add156 = solver.IntVar(0, 1, 'C2_ey_CAST_add156')
solver.Add( + (1)*ey_fixbits + (-1)*ey_CAST_add156_fixbits + (-10000)*C1_ey_CAST_add156<=0)    #Shift cost 1
solver.Add( + (-1)*ey_fixbits + (1)*ey_CAST_add156_fixbits + (-10000)*C2_ey_CAST_add156<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ey_CAST_add156
castCostObj +=  + (1)*C2_ey_CAST_add156
C3_ey_CAST_add156 = solver.IntVar(0, 1, 'C3_ey_CAST_add156')
C4_ey_CAST_add156 = solver.IntVar(0, 1, 'C4_ey_CAST_add156')
C5_ey_CAST_add156 = solver.IntVar(0, 1, 'C5_ey_CAST_add156')
C6_ey_CAST_add156 = solver.IntVar(0, 1, 'C6_ey_CAST_add156')
C7_ey_CAST_add156 = solver.IntVar(0, 1, 'C7_ey_CAST_add156')
C8_ey_CAST_add156 = solver.IntVar(0, 1, 'C8_ey_CAST_add156')
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_add156_float + (-1)*C3_ey_CAST_add156<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ey_CAST_add156
solver.Add( + (1)*ey_float + (1)*ey_CAST_add156_fixp + (-1)*C4_ey_CAST_add156<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ey_CAST_add156
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_add156_double + (-1)*C5_ey_CAST_add156<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ey_CAST_add156
solver.Add( + (1)*ey_double + (1)*ey_CAST_add156_fixp + (-1)*C6_ey_CAST_add156<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ey_CAST_add156
solver.Add( + (1)*ey_float + (1)*ey_CAST_add156_double + (-1)*C7_ey_CAST_add156<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ey_CAST_add156
solver.Add( + (1)*ey_double + (1)*ey_CAST_add156_float + (-1)*C8_ey_CAST_add156<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ey_CAST_add156



#Stuff for   %add156 = fadd double %sub150, %tmp10, !taffo.info !45, !taffo.initweight !33
main_add156_fixbits = solver.IntVar(0, 21, 'main_add156_fixbits')
main_add156_fixp = solver.IntVar(0, 1, 'main_add156_fixp')
main_add156_float = solver.IntVar(0, 1, 'main_add156_float')
main_add156_double = solver.IntVar(0, 1, 'main_add156_double')
main_add156_enob = solver.IntVar(-10000, 10000, 'main_add156_enob')
solver.Add( + (1)*main_add156_enob + (-1)*main_add156_fixbits + (10000)*main_add156_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add156_enob + (10000)*main_add156_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add156_enob + (10000)*main_add156_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add156_fixbits + (-10000)*main_add156_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_add156_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add156_enob
solver.Add( + (1)*main_add156_fixp + (1)*main_add156_float + (1)*main_add156_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add156_fixbits + (-10000)*main_add156_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub150_CAST_add156_fixp + (-1)*ey_CAST_add156_fixp==0)    #fix equality
solver.Add( + (1)*main_sub150_CAST_add156_float + (-1)*ey_CAST_add156_float==0)    #float equality
solver.Add( + (1)*main_sub150_CAST_add156_double + (-1)*ey_CAST_add156_double==0)    #double equality
solver.Add( + (1)*main_sub150_CAST_add156_fixbits + (-1)*ey_CAST_add156_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub150_CAST_add156_fixp + (-1)*main_add156_fixp==0)    #fix equality
solver.Add( + (1)*main_sub150_CAST_add156_float + (-1)*main_add156_float==0)    #float equality
solver.Add( + (1)*main_sub150_CAST_add156_double + (-1)*main_add156_double==0)    #double equality
solver.Add( + (1)*main_sub150_CAST_add156_fixbits + (-1)*main_add156_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add156_fixp
mathCostObj +=  + (2.33125)*main_add156_float
mathCostObj +=  + (2.72422)*main_add156_double
solver.Add( + (1)*main_add156_enob + (-1)*main_sub150_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add156_enob + (-1)*ey_enob_memphi_main_tmp10<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
ey_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'ey_enob_memphi_main_tmp11')
solver.Add( + (1)*ey_enob_memphi_main_tmp11 + (-1)*ey_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_1 = solver.IntVar(0, 1, 'main_main_tmp11_enob_1')
main_main_tmp11_enob_2 = solver.IntVar(0, 1, 'main_main_tmp11_enob_2')
main_main_tmp11_enob_3 = solver.IntVar(0, 1, 'main_main_tmp11_enob_3')
main_main_tmp11_enob_4 = solver.IntVar(0, 1, 'main_main_tmp11_enob_4')
main_main_tmp11_enob_5 = solver.IntVar(0, 1, 'main_main_tmp11_enob_5')
main_main_tmp11_enob_6 = solver.IntVar(0, 1, 'main_main_tmp11_enob_6')
solver.Add( + (1)*main_main_tmp11_enob_1 + (1)*main_main_tmp11_enob_2 + (1)*main_main_tmp11_enob_3 + (1)*main_main_tmp11_enob_4 + (1)*main_main_tmp11_enob_5 + (1)*main_main_tmp11_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp11 + (-1)*_fict__enob_storeENOB + (10000)*main_main_tmp11_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp11 + (-1)*hz_enob_storeENOB + (10000)*main_main_tmp11_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp11 + (-1)*ex_enob_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp11 + (-1)*ey_enob_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp11 + (-1)*ey_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_6<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub161 = fsub double %add156, %tmp11, !taffo.info !47, !taffo.initweight !33
main_add156_CAST_sub161_fixbits = solver.IntVar(0, 21, 'main_add156_CAST_sub161_fixbits')
main_add156_CAST_sub161_fixp = solver.IntVar(0, 1, 'main_add156_CAST_sub161_fixp')
main_add156_CAST_sub161_float = solver.IntVar(0, 1, 'main_add156_CAST_sub161_float')
main_add156_CAST_sub161_double = solver.IntVar(0, 1, 'main_add156_CAST_sub161_double')
solver.Add( + (1)*main_add156_CAST_sub161_fixp + (1)*main_add156_CAST_sub161_float + (1)*main_add156_CAST_sub161_double==1)    #exactly 1 type
solver.Add( + (1)*main_add156_CAST_sub161_fixbits + (-10000)*main_add156_CAST_sub161_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C1_main_add156_CAST_sub161')
C2_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C2_main_add156_CAST_sub161')
solver.Add( + (1)*main_add156_fixbits + (-1)*main_add156_CAST_sub161_fixbits + (-10000)*C1_main_add156_CAST_sub161<=0)    #Shift cost 1
solver.Add( + (-1)*main_add156_fixbits + (1)*main_add156_CAST_sub161_fixbits + (-10000)*C2_main_add156_CAST_sub161<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add156_CAST_sub161
castCostObj +=  + (1)*C2_main_add156_CAST_sub161
C3_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C3_main_add156_CAST_sub161')
C4_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C4_main_add156_CAST_sub161')
C5_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C5_main_add156_CAST_sub161')
C6_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C6_main_add156_CAST_sub161')
C7_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C7_main_add156_CAST_sub161')
C8_main_add156_CAST_sub161 = solver.IntVar(0, 1, 'C8_main_add156_CAST_sub161')
solver.Add( + (1)*main_add156_fixp + (1)*main_add156_CAST_sub161_float + (-1)*C3_main_add156_CAST_sub161<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add156_CAST_sub161
solver.Add( + (1)*main_add156_float + (1)*main_add156_CAST_sub161_fixp + (-1)*C4_main_add156_CAST_sub161<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add156_CAST_sub161
solver.Add( + (1)*main_add156_fixp + (1)*main_add156_CAST_sub161_double + (-1)*C5_main_add156_CAST_sub161<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add156_CAST_sub161
solver.Add( + (1)*main_add156_double + (1)*main_add156_CAST_sub161_fixp + (-1)*C6_main_add156_CAST_sub161<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add156_CAST_sub161
solver.Add( + (1)*main_add156_float + (1)*main_add156_CAST_sub161_double + (-1)*C7_main_add156_CAST_sub161<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add156_CAST_sub161
solver.Add( + (1)*main_add156_double + (1)*main_add156_CAST_sub161_float + (-1)*C8_main_add156_CAST_sub161<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add156_CAST_sub161



#Constraint for cast for   %sub161 = fsub double %add156, %tmp11, !taffo.info !47, !taffo.initweight !33
ey_CAST_sub161_fixbits = solver.IntVar(0, 23, 'ey_CAST_sub161_fixbits')
ey_CAST_sub161_fixp = solver.IntVar(0, 1, 'ey_CAST_sub161_fixp')
ey_CAST_sub161_float = solver.IntVar(0, 1, 'ey_CAST_sub161_float')
ey_CAST_sub161_double = solver.IntVar(0, 1, 'ey_CAST_sub161_double')
solver.Add( + (1)*ey_CAST_sub161_fixp + (1)*ey_CAST_sub161_float + (1)*ey_CAST_sub161_double==1)    #exactly 1 type
solver.Add( + (1)*ey_CAST_sub161_fixbits + (-10000)*ey_CAST_sub161_fixp<=0)    #If no fix, fix frac part = 0
C1_ey_CAST_sub161 = solver.IntVar(0, 1, 'C1_ey_CAST_sub161')
C2_ey_CAST_sub161 = solver.IntVar(0, 1, 'C2_ey_CAST_sub161')
solver.Add( + (1)*ey_fixbits + (-1)*ey_CAST_sub161_fixbits + (-10000)*C1_ey_CAST_sub161<=0)    #Shift cost 1
solver.Add( + (-1)*ey_fixbits + (1)*ey_CAST_sub161_fixbits + (-10000)*C2_ey_CAST_sub161<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ey_CAST_sub161
castCostObj +=  + (1)*C2_ey_CAST_sub161
C3_ey_CAST_sub161 = solver.IntVar(0, 1, 'C3_ey_CAST_sub161')
C4_ey_CAST_sub161 = solver.IntVar(0, 1, 'C4_ey_CAST_sub161')
C5_ey_CAST_sub161 = solver.IntVar(0, 1, 'C5_ey_CAST_sub161')
C6_ey_CAST_sub161 = solver.IntVar(0, 1, 'C6_ey_CAST_sub161')
C7_ey_CAST_sub161 = solver.IntVar(0, 1, 'C7_ey_CAST_sub161')
C8_ey_CAST_sub161 = solver.IntVar(0, 1, 'C8_ey_CAST_sub161')
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_sub161_float + (-1)*C3_ey_CAST_sub161<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ey_CAST_sub161
solver.Add( + (1)*ey_float + (1)*ey_CAST_sub161_fixp + (-1)*C4_ey_CAST_sub161<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ey_CAST_sub161
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_sub161_double + (-1)*C5_ey_CAST_sub161<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ey_CAST_sub161
solver.Add( + (1)*ey_double + (1)*ey_CAST_sub161_fixp + (-1)*C6_ey_CAST_sub161<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ey_CAST_sub161
solver.Add( + (1)*ey_float + (1)*ey_CAST_sub161_double + (-1)*C7_ey_CAST_sub161<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ey_CAST_sub161
solver.Add( + (1)*ey_double + (1)*ey_CAST_sub161_float + (-1)*C8_ey_CAST_sub161<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ey_CAST_sub161



#Stuff for   %sub161 = fsub double %add156, %tmp11, !taffo.info !47, !taffo.initweight !33
main_sub161_fixbits = solver.IntVar(0, 21, 'main_sub161_fixbits')
main_sub161_fixp = solver.IntVar(0, 1, 'main_sub161_fixp')
main_sub161_float = solver.IntVar(0, 1, 'main_sub161_float')
main_sub161_double = solver.IntVar(0, 1, 'main_sub161_double')
main_sub161_enob = solver.IntVar(-10000, 10000, 'main_sub161_enob')
solver.Add( + (1)*main_sub161_enob + (-1)*main_sub161_fixbits + (10000)*main_sub161_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub161_enob + (10000)*main_sub161_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub161_enob + (10000)*main_sub161_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub161_fixbits + (-10000)*main_sub161_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_sub161_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub161_enob
solver.Add( + (1)*main_sub161_fixp + (1)*main_sub161_float + (1)*main_sub161_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub161_fixbits + (-10000)*main_sub161_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add156_CAST_sub161_fixp + (-1)*ey_CAST_sub161_fixp==0)    #fix equality
solver.Add( + (1)*main_add156_CAST_sub161_float + (-1)*ey_CAST_sub161_float==0)    #float equality
solver.Add( + (1)*main_add156_CAST_sub161_double + (-1)*ey_CAST_sub161_double==0)    #double equality
solver.Add( + (1)*main_add156_CAST_sub161_fixbits + (-1)*ey_CAST_sub161_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add156_CAST_sub161_fixp + (-1)*main_sub161_fixp==0)    #fix equality
solver.Add( + (1)*main_add156_CAST_sub161_float + (-1)*main_sub161_float==0)    #float equality
solver.Add( + (1)*main_add156_CAST_sub161_double + (-1)*main_sub161_double==0)    #double equality
solver.Add( + (1)*main_add156_CAST_sub161_fixbits + (-1)*main_sub161_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub161_fixp
mathCostObj +=  + (2.33125)*main_sub161_float
mathCostObj +=  + (2.72422)*main_sub161_double
solver.Add( + (1)*main_sub161_enob + (-1)*main_add156_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub161_enob + (-1)*ey_enob_memphi_main_tmp11<=0)    #Enob propagation in sub second addend



#Stuff for double 0x3FE6666666666666
ConstantValue__5_fixbits = solver.IntVar(0, 31, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FE6666666666666
ConstantValue__6_fixbits = solver.IntVar(0, 31, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FE6666666666666
ConstantValue__7_fixbits = solver.IntVar(0, 31, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul162 = fmul double 0x3FE6666666666666, %sub161, !taffo.info !49, !taffo.initweight !41, !taffo.constinfo !51
ConstantValue__7_CAST_mul162_fixbits = solver.IntVar(0, 31, 'ConstantValue__7_CAST_mul162_fixbits')
ConstantValue__7_CAST_mul162_fixp = solver.IntVar(0, 1, 'ConstantValue__7_CAST_mul162_fixp')
ConstantValue__7_CAST_mul162_float = solver.IntVar(0, 1, 'ConstantValue__7_CAST_mul162_float')
ConstantValue__7_CAST_mul162_double = solver.IntVar(0, 1, 'ConstantValue__7_CAST_mul162_double')
solver.Add( + (1)*ConstantValue__7_CAST_mul162_fixp + (1)*ConstantValue__7_CAST_mul162_float + (1)*ConstantValue__7_CAST_mul162_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__7_CAST_mul162_fixbits + (-10000)*ConstantValue__7_CAST_mul162_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C1_ConstantValue__7_CAST_mul162')
C2_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C2_ConstantValue__7_CAST_mul162')
solver.Add( + (1)*ConstantValue__7_fixbits + (-1)*ConstantValue__7_CAST_mul162_fixbits + (-10000)*C1_ConstantValue__7_CAST_mul162<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__7_fixbits + (1)*ConstantValue__7_CAST_mul162_fixbits + (-10000)*C2_ConstantValue__7_CAST_mul162<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__7_CAST_mul162
castCostObj +=  + (1)*C2_ConstantValue__7_CAST_mul162
C3_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C3_ConstantValue__7_CAST_mul162')
C4_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C4_ConstantValue__7_CAST_mul162')
C5_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C5_ConstantValue__7_CAST_mul162')
C6_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C6_ConstantValue__7_CAST_mul162')
C7_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C7_ConstantValue__7_CAST_mul162')
C8_ConstantValue__7_CAST_mul162 = solver.IntVar(0, 1, 'C8_ConstantValue__7_CAST_mul162')
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_mul162_float + (-1)*C3_ConstantValue__7_CAST_mul162<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__7_CAST_mul162
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_mul162_fixp + (-1)*C4_ConstantValue__7_CAST_mul162<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__7_CAST_mul162
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_mul162_double + (-1)*C5_ConstantValue__7_CAST_mul162<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__7_CAST_mul162
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_mul162_fixp + (-1)*C6_ConstantValue__7_CAST_mul162<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__7_CAST_mul162
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_mul162_double + (-1)*C7_ConstantValue__7_CAST_mul162<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__7_CAST_mul162
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_mul162_float + (-1)*C8_ConstantValue__7_CAST_mul162<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__7_CAST_mul162



#Constraint for cast for   %mul162 = fmul double 0x3FE6666666666666, %sub161, !taffo.info !49, !taffo.initweight !41, !taffo.constinfo !51
main_sub161_CAST_mul162_fixbits = solver.IntVar(0, 21, 'main_sub161_CAST_mul162_fixbits')
main_sub161_CAST_mul162_fixp = solver.IntVar(0, 1, 'main_sub161_CAST_mul162_fixp')
main_sub161_CAST_mul162_float = solver.IntVar(0, 1, 'main_sub161_CAST_mul162_float')
main_sub161_CAST_mul162_double = solver.IntVar(0, 1, 'main_sub161_CAST_mul162_double')
solver.Add( + (1)*main_sub161_CAST_mul162_fixp + (1)*main_sub161_CAST_mul162_float + (1)*main_sub161_CAST_mul162_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub161_CAST_mul162_fixbits + (-10000)*main_sub161_CAST_mul162_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C1_main_sub161_CAST_mul162')
C2_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C2_main_sub161_CAST_mul162')
solver.Add( + (1)*main_sub161_fixbits + (-1)*main_sub161_CAST_mul162_fixbits + (-10000)*C1_main_sub161_CAST_mul162<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub161_fixbits + (1)*main_sub161_CAST_mul162_fixbits + (-10000)*C2_main_sub161_CAST_mul162<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub161_CAST_mul162
castCostObj +=  + (1)*C2_main_sub161_CAST_mul162
C3_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C3_main_sub161_CAST_mul162')
C4_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C4_main_sub161_CAST_mul162')
C5_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C5_main_sub161_CAST_mul162')
C6_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C6_main_sub161_CAST_mul162')
C7_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C7_main_sub161_CAST_mul162')
C8_main_sub161_CAST_mul162 = solver.IntVar(0, 1, 'C8_main_sub161_CAST_mul162')
solver.Add( + (1)*main_sub161_fixp + (1)*main_sub161_CAST_mul162_float + (-1)*C3_main_sub161_CAST_mul162<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub161_CAST_mul162
solver.Add( + (1)*main_sub161_float + (1)*main_sub161_CAST_mul162_fixp + (-1)*C4_main_sub161_CAST_mul162<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub161_CAST_mul162
solver.Add( + (1)*main_sub161_fixp + (1)*main_sub161_CAST_mul162_double + (-1)*C5_main_sub161_CAST_mul162<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub161_CAST_mul162
solver.Add( + (1)*main_sub161_double + (1)*main_sub161_CAST_mul162_fixp + (-1)*C6_main_sub161_CAST_mul162<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub161_CAST_mul162
solver.Add( + (1)*main_sub161_float + (1)*main_sub161_CAST_mul162_double + (-1)*C7_main_sub161_CAST_mul162<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub161_CAST_mul162
solver.Add( + (1)*main_sub161_double + (1)*main_sub161_CAST_mul162_float + (-1)*C8_main_sub161_CAST_mul162<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub161_CAST_mul162



#Stuff for   %mul162 = fmul double 0x3FE6666666666666, %sub161, !taffo.info !49, !taffo.initweight !41, !taffo.constinfo !51
main_mul162_fixbits = solver.IntVar(0, 21, 'main_mul162_fixbits')
main_mul162_fixp = solver.IntVar(0, 1, 'main_mul162_fixp')
main_mul162_float = solver.IntVar(0, 1, 'main_mul162_float')
main_mul162_double = solver.IntVar(0, 1, 'main_mul162_double')
main_mul162_enob = solver.IntVar(-10000, 10000, 'main_mul162_enob')
solver.Add( + (1)*main_mul162_enob + (-1)*main_mul162_fixbits + (10000)*main_mul162_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul162_enob + (10000)*main_mul162_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul162_enob + (10000)*main_mul162_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul162_fixbits + (-10000)*main_mul162_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_mul162_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul162_enob
solver.Add( + (1)*main_mul162_fixp + (1)*main_mul162_float + (1)*main_mul162_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul162_fixbits + (-10000)*main_mul162_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__7_CAST_mul162_fixp + (-1)*main_sub161_CAST_mul162_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__7_CAST_mul162_float + (-1)*main_sub161_CAST_mul162_float==0)    #float equality
solver.Add( + (1)*ConstantValue__7_CAST_mul162_double + (-1)*main_sub161_CAST_mul162_double==0)    #double equality
solver.Add( + (1)*ConstantValue__7_CAST_mul162_fixp + (-1)*main_mul162_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__7_CAST_mul162_float + (-1)*main_mul162_float==0)    #float equality
solver.Add( + (1)*ConstantValue__7_CAST_mul162_double + (-1)*main_mul162_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul162_fixp
mathCostObj +=  + (2.64722)*main_mul162_float
mathCostObj +=  + (4.02255)*main_mul162_double
main_main_mul162_enob_1 = solver.IntVar(0, 1, 'main_main_mul162_enob_1')
main_main_mul162_enob_2 = solver.IntVar(0, 1, 'main_main_mul162_enob_2')
solver.Add( + (1)*main_main_mul162_enob_1 + (1)*main_main_mul162_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul162_enob + (-1)*main_sub161_enob + (-10000)*main_main_mul162_enob_1<=1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul162_enob + (-1)*ConstantValue__5_enob + (-10000)*main_main_mul162_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub163 = fsub double %tmp7, %mul162, !taffo.info !54, !taffo.initweight !33
hz_CAST_sub163_fixbits = solver.IntVar(0, 23, 'hz_CAST_sub163_fixbits')
hz_CAST_sub163_fixp = solver.IntVar(0, 1, 'hz_CAST_sub163_fixp')
hz_CAST_sub163_float = solver.IntVar(0, 1, 'hz_CAST_sub163_float')
hz_CAST_sub163_double = solver.IntVar(0, 1, 'hz_CAST_sub163_double')
solver.Add( + (1)*hz_CAST_sub163_fixp + (1)*hz_CAST_sub163_float + (1)*hz_CAST_sub163_double==1)    #exactly 1 type
solver.Add( + (1)*hz_CAST_sub163_fixbits + (-10000)*hz_CAST_sub163_fixp<=0)    #If no fix, fix frac part = 0
C1_hz_CAST_sub163 = solver.IntVar(0, 1, 'C1_hz_CAST_sub163')
C2_hz_CAST_sub163 = solver.IntVar(0, 1, 'C2_hz_CAST_sub163')
solver.Add( + (1)*hz_fixbits + (-1)*hz_CAST_sub163_fixbits + (-10000)*C1_hz_CAST_sub163<=0)    #Shift cost 1
solver.Add( + (-1)*hz_fixbits + (1)*hz_CAST_sub163_fixbits + (-10000)*C2_hz_CAST_sub163<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_hz_CAST_sub163
castCostObj +=  + (1)*C2_hz_CAST_sub163
C3_hz_CAST_sub163 = solver.IntVar(0, 1, 'C3_hz_CAST_sub163')
C4_hz_CAST_sub163 = solver.IntVar(0, 1, 'C4_hz_CAST_sub163')
C5_hz_CAST_sub163 = solver.IntVar(0, 1, 'C5_hz_CAST_sub163')
C6_hz_CAST_sub163 = solver.IntVar(0, 1, 'C6_hz_CAST_sub163')
C7_hz_CAST_sub163 = solver.IntVar(0, 1, 'C7_hz_CAST_sub163')
C8_hz_CAST_sub163 = solver.IntVar(0, 1, 'C8_hz_CAST_sub163')
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub163_float + (-1)*C3_hz_CAST_sub163<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_hz_CAST_sub163
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub163_fixp + (-1)*C4_hz_CAST_sub163<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_hz_CAST_sub163
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_sub163_double + (-1)*C5_hz_CAST_sub163<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_hz_CAST_sub163
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub163_fixp + (-1)*C6_hz_CAST_sub163<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_hz_CAST_sub163
solver.Add( + (1)*hz_float + (1)*hz_CAST_sub163_double + (-1)*C7_hz_CAST_sub163<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_hz_CAST_sub163
solver.Add( + (1)*hz_double + (1)*hz_CAST_sub163_float + (-1)*C8_hz_CAST_sub163<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_hz_CAST_sub163



#Constraint for cast for   %sub163 = fsub double %tmp7, %mul162, !taffo.info !54, !taffo.initweight !33
main_mul162_CAST_sub163_fixbits = solver.IntVar(0, 21, 'main_mul162_CAST_sub163_fixbits')
main_mul162_CAST_sub163_fixp = solver.IntVar(0, 1, 'main_mul162_CAST_sub163_fixp')
main_mul162_CAST_sub163_float = solver.IntVar(0, 1, 'main_mul162_CAST_sub163_float')
main_mul162_CAST_sub163_double = solver.IntVar(0, 1, 'main_mul162_CAST_sub163_double')
solver.Add( + (1)*main_mul162_CAST_sub163_fixp + (1)*main_mul162_CAST_sub163_float + (1)*main_mul162_CAST_sub163_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul162_CAST_sub163_fixbits + (-10000)*main_mul162_CAST_sub163_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C1_main_mul162_CAST_sub163')
C2_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C2_main_mul162_CAST_sub163')
solver.Add( + (1)*main_mul162_fixbits + (-1)*main_mul162_CAST_sub163_fixbits + (-10000)*C1_main_mul162_CAST_sub163<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul162_fixbits + (1)*main_mul162_CAST_sub163_fixbits + (-10000)*C2_main_mul162_CAST_sub163<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul162_CAST_sub163
castCostObj +=  + (1)*C2_main_mul162_CAST_sub163
C3_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C3_main_mul162_CAST_sub163')
C4_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C4_main_mul162_CAST_sub163')
C5_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C5_main_mul162_CAST_sub163')
C6_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C6_main_mul162_CAST_sub163')
C7_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C7_main_mul162_CAST_sub163')
C8_main_mul162_CAST_sub163 = solver.IntVar(0, 1, 'C8_main_mul162_CAST_sub163')
solver.Add( + (1)*main_mul162_fixp + (1)*main_mul162_CAST_sub163_float + (-1)*C3_main_mul162_CAST_sub163<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul162_CAST_sub163
solver.Add( + (1)*main_mul162_float + (1)*main_mul162_CAST_sub163_fixp + (-1)*C4_main_mul162_CAST_sub163<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul162_CAST_sub163
solver.Add( + (1)*main_mul162_fixp + (1)*main_mul162_CAST_sub163_double + (-1)*C5_main_mul162_CAST_sub163<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul162_CAST_sub163
solver.Add( + (1)*main_mul162_double + (1)*main_mul162_CAST_sub163_fixp + (-1)*C6_main_mul162_CAST_sub163<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul162_CAST_sub163
solver.Add( + (1)*main_mul162_float + (1)*main_mul162_CAST_sub163_double + (-1)*C7_main_mul162_CAST_sub163<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul162_CAST_sub163
solver.Add( + (1)*main_mul162_double + (1)*main_mul162_CAST_sub163_float + (-1)*C8_main_mul162_CAST_sub163<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul162_CAST_sub163



#Stuff for   %sub163 = fsub double %tmp7, %mul162, !taffo.info !54, !taffo.initweight !33
main_sub163_fixbits = solver.IntVar(0, 21, 'main_sub163_fixbits')
main_sub163_fixp = solver.IntVar(0, 1, 'main_sub163_fixp')
main_sub163_float = solver.IntVar(0, 1, 'main_sub163_float')
main_sub163_double = solver.IntVar(0, 1, 'main_sub163_double')
main_sub163_enob = solver.IntVar(-10000, 10000, 'main_sub163_enob')
solver.Add( + (1)*main_sub163_enob + (-1)*main_sub163_fixbits + (10000)*main_sub163_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub163_enob + (10000)*main_sub163_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub163_enob + (10000)*main_sub163_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub163_fixbits + (-10000)*main_sub163_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_sub163_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub163_enob
solver.Add( + (1)*main_sub163_fixp + (1)*main_sub163_float + (1)*main_sub163_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub163_fixbits + (-10000)*main_sub163_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*hz_CAST_sub163_fixp + (-1)*main_mul162_CAST_sub163_fixp==0)    #fix equality
solver.Add( + (1)*hz_CAST_sub163_float + (-1)*main_mul162_CAST_sub163_float==0)    #float equality
solver.Add( + (1)*hz_CAST_sub163_double + (-1)*main_mul162_CAST_sub163_double==0)    #double equality
solver.Add( + (1)*hz_CAST_sub163_fixbits + (-1)*main_mul162_CAST_sub163_fixbits==0)    #same fractional bit
solver.Add( + (1)*hz_CAST_sub163_fixp + (-1)*main_sub163_fixp==0)    #fix equality
solver.Add( + (1)*hz_CAST_sub163_float + (-1)*main_sub163_float==0)    #float equality
solver.Add( + (1)*hz_CAST_sub163_double + (-1)*main_sub163_double==0)    #double equality
solver.Add( + (1)*hz_CAST_sub163_fixbits + (-1)*main_sub163_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub163_fixp
mathCostObj +=  + (2.33125)*main_sub163_float
mathCostObj +=  + (2.72422)*main_sub163_double
solver.Add( + (1)*main_sub163_enob + (-1)*hz_enob_memphi_main_tmp7<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub163_enob + (-1)*main_mul162_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub163, double* %arrayidx167, align 8, !taffo.info !12, !taffo.initweight !22
main_sub163_CAST_store_fixbits = solver.IntVar(0, 21, 'main_sub163_CAST_store_fixbits')
main_sub163_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub163_CAST_store_fixp')
main_sub163_CAST_store_float = solver.IntVar(0, 1, 'main_sub163_CAST_store_float')
main_sub163_CAST_store_double = solver.IntVar(0, 1, 'main_sub163_CAST_store_double')
solver.Add( + (1)*main_sub163_CAST_store_fixp + (1)*main_sub163_CAST_store_float + (1)*main_sub163_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub163_CAST_store_fixbits + (-10000)*main_sub163_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub163_CAST_store = solver.IntVar(0, 1, 'C1_main_sub163_CAST_store')
C2_main_sub163_CAST_store = solver.IntVar(0, 1, 'C2_main_sub163_CAST_store')
solver.Add( + (1)*main_sub163_fixbits + (-1)*main_sub163_CAST_store_fixbits + (-10000)*C1_main_sub163_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub163_fixbits + (1)*main_sub163_CAST_store_fixbits + (-10000)*C2_main_sub163_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub163_CAST_store
castCostObj +=  + (1)*C2_main_sub163_CAST_store
C3_main_sub163_CAST_store = solver.IntVar(0, 1, 'C3_main_sub163_CAST_store')
C4_main_sub163_CAST_store = solver.IntVar(0, 1, 'C4_main_sub163_CAST_store')
C5_main_sub163_CAST_store = solver.IntVar(0, 1, 'C5_main_sub163_CAST_store')
C6_main_sub163_CAST_store = solver.IntVar(0, 1, 'C6_main_sub163_CAST_store')
C7_main_sub163_CAST_store = solver.IntVar(0, 1, 'C7_main_sub163_CAST_store')
C8_main_sub163_CAST_store = solver.IntVar(0, 1, 'C8_main_sub163_CAST_store')
solver.Add( + (1)*main_sub163_fixp + (1)*main_sub163_CAST_store_float + (-1)*C3_main_sub163_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub163_CAST_store
solver.Add( + (1)*main_sub163_float + (1)*main_sub163_CAST_store_fixp + (-1)*C4_main_sub163_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub163_CAST_store
solver.Add( + (1)*main_sub163_fixp + (1)*main_sub163_CAST_store_double + (-1)*C5_main_sub163_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub163_CAST_store
solver.Add( + (1)*main_sub163_double + (1)*main_sub163_CAST_store_fixp + (-1)*C6_main_sub163_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub163_CAST_store
solver.Add( + (1)*main_sub163_float + (1)*main_sub163_CAST_store_double + (-1)*C7_main_sub163_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub163_CAST_store
solver.Add( + (1)*main_sub163_double + (1)*main_sub163_CAST_store_float + (-1)*C8_main_sub163_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub163_CAST_store
solver.Add( + (1)*hz_fixp + (-1)*main_sub163_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*hz_float + (-1)*main_sub163_CAST_store_float==0)    #float equality
solver.Add( + (1)*hz_double + (-1)*main_sub163_CAST_store_double==0)    #double equality
solver.Add( + (1)*hz_fixbits + (-1)*main_sub163_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
hz_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'hz_enob_storeENOB_storeENOB')
solver.Add( + (1)*hz_enob_storeENOB_storeENOB + (-1)*hz_fixbits + (10000)*hz_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*hz_enob_storeENOB_storeENOB + (10000)*hz_float<=10149)    #Enob constraint for float
solver.Add( + (1)*hz_enob_storeENOB_storeENOB + (10000)*hz_double<=11074)    #Enob constraint for double
solver.Add( + (1)*hz_enob_storeENOB_storeENOB + (-1)*main_sub163_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp1 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp2 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp3 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp4 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp5 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp6 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*hz_enob_memphi_main_tmp7 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp8 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ex_enob_memphi_main_tmp9 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp10 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*ey_enob_memphi_main_tmp11 + (-1)*hz_enob_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
ex_enob_memphi_main_tmp14 = solver.IntVar(-10000, 10000, 'ex_enob_memphi_main_tmp14')
solver.Add( + (1)*ex_enob_memphi_main_tmp14 + (-1)*ex_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call193 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp13, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp14), !taffo.info !12, !taffo.initweight !33, !taffo.constinfo !61
ex_CAST_call193_fixbits = solver.IntVar(0, 23, 'ex_CAST_call193_fixbits')
ex_CAST_call193_fixp = solver.IntVar(0, 1, 'ex_CAST_call193_fixp')
ex_CAST_call193_float = solver.IntVar(0, 1, 'ex_CAST_call193_float')
ex_CAST_call193_double = solver.IntVar(0, 1, 'ex_CAST_call193_double')
solver.Add( + (1)*ex_CAST_call193_fixp + (1)*ex_CAST_call193_float + (1)*ex_CAST_call193_double==1)    #exactly 1 type
solver.Add( + (1)*ex_CAST_call193_fixbits + (-10000)*ex_CAST_call193_fixp<=0)    #If no fix, fix frac part = 0
C1_ex_CAST_call193 = solver.IntVar(0, 1, 'C1_ex_CAST_call193')
C2_ex_CAST_call193 = solver.IntVar(0, 1, 'C2_ex_CAST_call193')
solver.Add( + (1)*ex_fixbits + (-1)*ex_CAST_call193_fixbits + (-10000)*C1_ex_CAST_call193<=0)    #Shift cost 1
solver.Add( + (-1)*ex_fixbits + (1)*ex_CAST_call193_fixbits + (-10000)*C2_ex_CAST_call193<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ex_CAST_call193
castCostObj +=  + (1)*C2_ex_CAST_call193
C3_ex_CAST_call193 = solver.IntVar(0, 1, 'C3_ex_CAST_call193')
C4_ex_CAST_call193 = solver.IntVar(0, 1, 'C4_ex_CAST_call193')
C5_ex_CAST_call193 = solver.IntVar(0, 1, 'C5_ex_CAST_call193')
C6_ex_CAST_call193 = solver.IntVar(0, 1, 'C6_ex_CAST_call193')
C7_ex_CAST_call193 = solver.IntVar(0, 1, 'C7_ex_CAST_call193')
C8_ex_CAST_call193 = solver.IntVar(0, 1, 'C8_ex_CAST_call193')
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_call193_float + (-1)*C3_ex_CAST_call193<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ex_CAST_call193
solver.Add( + (1)*ex_float + (1)*ex_CAST_call193_fixp + (-1)*C4_ex_CAST_call193<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ex_CAST_call193
solver.Add( + (1)*ex_fixp + (1)*ex_CAST_call193_double + (-1)*C5_ex_CAST_call193<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ex_CAST_call193
solver.Add( + (1)*ex_double + (1)*ex_CAST_call193_fixp + (-1)*C6_ex_CAST_call193<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ex_CAST_call193
solver.Add( + (1)*ex_float + (1)*ex_CAST_call193_double + (-1)*C7_ex_CAST_call193<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ex_CAST_call193
solver.Add( + (1)*ex_double + (1)*ex_CAST_call193_float + (-1)*C8_ex_CAST_call193<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ex_CAST_call193
solver.Add( + (1)*ex_CAST_call193_double==1)    #Type constraint for argument value

#Restriction for new enob [LOAD]
ey_enob_memphi_main_tmp17 = solver.IntVar(-10000, 10000, 'ey_enob_memphi_main_tmp17')
solver.Add( + (1)*ey_enob_memphi_main_tmp17 + (-1)*ey_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call220 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp16, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp17), !taffo.info !12, !taffo.initweight !33, !taffo.constinfo !61
ey_CAST_call220_fixbits = solver.IntVar(0, 23, 'ey_CAST_call220_fixbits')
ey_CAST_call220_fixp = solver.IntVar(0, 1, 'ey_CAST_call220_fixp')
ey_CAST_call220_float = solver.IntVar(0, 1, 'ey_CAST_call220_float')
ey_CAST_call220_double = solver.IntVar(0, 1, 'ey_CAST_call220_double')
solver.Add( + (1)*ey_CAST_call220_fixp + (1)*ey_CAST_call220_float + (1)*ey_CAST_call220_double==1)    #exactly 1 type
solver.Add( + (1)*ey_CAST_call220_fixbits + (-10000)*ey_CAST_call220_fixp<=0)    #If no fix, fix frac part = 0
C1_ey_CAST_call220 = solver.IntVar(0, 1, 'C1_ey_CAST_call220')
C2_ey_CAST_call220 = solver.IntVar(0, 1, 'C2_ey_CAST_call220')
solver.Add( + (1)*ey_fixbits + (-1)*ey_CAST_call220_fixbits + (-10000)*C1_ey_CAST_call220<=0)    #Shift cost 1
solver.Add( + (-1)*ey_fixbits + (1)*ey_CAST_call220_fixbits + (-10000)*C2_ey_CAST_call220<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ey_CAST_call220
castCostObj +=  + (1)*C2_ey_CAST_call220
C3_ey_CAST_call220 = solver.IntVar(0, 1, 'C3_ey_CAST_call220')
C4_ey_CAST_call220 = solver.IntVar(0, 1, 'C4_ey_CAST_call220')
C5_ey_CAST_call220 = solver.IntVar(0, 1, 'C5_ey_CAST_call220')
C6_ey_CAST_call220 = solver.IntVar(0, 1, 'C6_ey_CAST_call220')
C7_ey_CAST_call220 = solver.IntVar(0, 1, 'C7_ey_CAST_call220')
C8_ey_CAST_call220 = solver.IntVar(0, 1, 'C8_ey_CAST_call220')
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_call220_float + (-1)*C3_ey_CAST_call220<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ey_CAST_call220
solver.Add( + (1)*ey_float + (1)*ey_CAST_call220_fixp + (-1)*C4_ey_CAST_call220<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ey_CAST_call220
solver.Add( + (1)*ey_fixp + (1)*ey_CAST_call220_double + (-1)*C5_ey_CAST_call220<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ey_CAST_call220
solver.Add( + (1)*ey_double + (1)*ey_CAST_call220_fixp + (-1)*C6_ey_CAST_call220<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ey_CAST_call220
solver.Add( + (1)*ey_float + (1)*ey_CAST_call220_double + (-1)*C7_ey_CAST_call220<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ey_CAST_call220
solver.Add( + (1)*ey_double + (1)*ey_CAST_call220_float + (-1)*C8_ey_CAST_call220<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ey_CAST_call220
solver.Add( + (1)*ey_CAST_call220_double==1)    #Type constraint for argument value

#Restriction for new enob [LOAD]
hz_enob_memphi_main_tmp20 = solver.IntVar(-10000, 10000, 'hz_enob_memphi_main_tmp20')
solver.Add( + (1)*hz_enob_memphi_main_tmp20 + (-1)*hz_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call247 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp19, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp20), !taffo.info !12, !taffo.initweight !33, !taffo.constinfo !61
hz_CAST_call247_fixbits = solver.IntVar(0, 23, 'hz_CAST_call247_fixbits')
hz_CAST_call247_fixp = solver.IntVar(0, 1, 'hz_CAST_call247_fixp')
hz_CAST_call247_float = solver.IntVar(0, 1, 'hz_CAST_call247_float')
hz_CAST_call247_double = solver.IntVar(0, 1, 'hz_CAST_call247_double')
solver.Add( + (1)*hz_CAST_call247_fixp + (1)*hz_CAST_call247_float + (1)*hz_CAST_call247_double==1)    #exactly 1 type
solver.Add( + (1)*hz_CAST_call247_fixbits + (-10000)*hz_CAST_call247_fixp<=0)    #If no fix, fix frac part = 0
C1_hz_CAST_call247 = solver.IntVar(0, 1, 'C1_hz_CAST_call247')
C2_hz_CAST_call247 = solver.IntVar(0, 1, 'C2_hz_CAST_call247')
solver.Add( + (1)*hz_fixbits + (-1)*hz_CAST_call247_fixbits + (-10000)*C1_hz_CAST_call247<=0)    #Shift cost 1
solver.Add( + (-1)*hz_fixbits + (1)*hz_CAST_call247_fixbits + (-10000)*C2_hz_CAST_call247<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_hz_CAST_call247
castCostObj +=  + (1)*C2_hz_CAST_call247
C3_hz_CAST_call247 = solver.IntVar(0, 1, 'C3_hz_CAST_call247')
C4_hz_CAST_call247 = solver.IntVar(0, 1, 'C4_hz_CAST_call247')
C5_hz_CAST_call247 = solver.IntVar(0, 1, 'C5_hz_CAST_call247')
C6_hz_CAST_call247 = solver.IntVar(0, 1, 'C6_hz_CAST_call247')
C7_hz_CAST_call247 = solver.IntVar(0, 1, 'C7_hz_CAST_call247')
C8_hz_CAST_call247 = solver.IntVar(0, 1, 'C8_hz_CAST_call247')
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_call247_float + (-1)*C3_hz_CAST_call247<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_hz_CAST_call247
solver.Add( + (1)*hz_float + (1)*hz_CAST_call247_fixp + (-1)*C4_hz_CAST_call247<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_hz_CAST_call247
solver.Add( + (1)*hz_fixp + (1)*hz_CAST_call247_double + (-1)*C5_hz_CAST_call247<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_hz_CAST_call247
solver.Add( + (1)*hz_double + (1)*hz_CAST_call247_fixp + (-1)*C6_hz_CAST_call247<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_hz_CAST_call247
solver.Add( + (1)*hz_float + (1)*hz_CAST_call247_double + (-1)*C7_hz_CAST_call247<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_hz_CAST_call247
solver.Add( + (1)*hz_double + (1)*hz_CAST_call247_float + (-1)*C8_hz_CAST_call247<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_hz_CAST_call247
solver.Add( + (1)*hz_CAST_call247_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 895.129+ 1 * enobCostObj / 19092+ 1000 * mathCostObj / 100.909)

# Model declaration end.