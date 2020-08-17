


#Stuff for @data = common dso_local global [260 x [240 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
data_fixbits = solver.IntVar(0, 9, 'data_fixbits')
data_fixp = solver.IntVar(0, 1, 'data_fixp')
data_float = solver.IntVar(0, 1, 'data_float')
data_double = solver.IntVar(0, 1, 'data_double')
data_enob = solver.IntVar(-10000, 10000, 'data_enob')
solver.Add( + (1)*data_enob + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_fixbits + (-10000)*data_fixp>=-9992)    #Limit the lower number of frac bits9
solver.Add( + (1)*data_enob<=333)    #Enob constraint for error maximal
enobCostObj =  + (-1)*data_enob
solver.Add( + (1)*data_fixp + (1)*data_float + (1)*data_double==1)    #Exactly one selected type
solver.Add( + (1)*data_fixbits + (-10000)*data_fixp<=0)    #If not fix, frac part to zero



#Stuff for @mean = common dso_local global [240 x double] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
mean_fixbits = solver.IntVar(0, 6, 'mean_fixbits')
mean_fixp = solver.IntVar(0, 1, 'mean_fixp')
mean_float = solver.IntVar(0, 1, 'mean_float')
mean_double = solver.IntVar(0, 1, 'mean_double')
mean_enob = solver.IntVar(-10000, 10000, 'mean_enob')
solver.Add( + (1)*mean_enob + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_fixbits + (-10000)*mean_fixp>=-9995)    #Limit the lower number of frac bits6
solver.Add( + (1)*mean_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*mean_enob
solver.Add( + (1)*mean_fixp + (1)*mean_float + (1)*mean_double==1)    #Exactly one selected type
solver.Add( + (1)*mean_fixbits + (-10000)*mean_fixp<=0)    #If not fix, frac part to zero



#Stuff for @cov = common dso_local global [260 x [240 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
cov_fixbits = solver.IntVar(0, 9, 'cov_fixbits')
cov_fixp = solver.IntVar(0, 1, 'cov_fixp')
cov_float = solver.IntVar(0, 1, 'cov_float')
cov_double = solver.IntVar(0, 1, 'cov_double')
cov_enob = solver.IntVar(-10000, 10000, 'cov_enob')
solver.Add( + (1)*cov_enob + (-1)*cov_fixbits + (10000)*cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*cov_enob + (10000)*cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*cov_enob + (10000)*cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*cov_fixbits + (-10000)*cov_fixp>=-9992)    #Limit the lower number of frac bits9
solver.Add( + (1)*cov_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*cov_enob
solver.Add( + (1)*cov_fixp + (1)*cov_float + (1)*cov_double==1)    #Exactly one selected type
solver.Add( + (1)*cov_fixbits + (-10000)*cov_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 260 to double, !taffo.info !21
main_conv_fixbits = solver.IntVar(0, 23, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10015)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=10044)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv10 = sitofp i32 %i.0 to double, !taffo.info !29, !taffo.initweight !27
main_conv10_fixbits = solver.IntVar(0, 23, 'main_conv10_fixbits')
main_conv10_fixp = solver.IntVar(0, 1, 'main_conv10_fixp')
main_conv10_float = solver.IntVar(0, 1, 'main_conv10_float')
main_conv10_double = solver.IntVar(0, 1, 'main_conv10_double')
main_conv10_enob = solver.IntVar(-10000, 10000, 'main_conv10_enob')
solver.Add( + (1)*main_conv10_enob + (-1)*main_conv10_fixbits + (10000)*main_conv10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv10_enob + (10000)*main_conv10_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv10_enob + (10000)*main_conv10_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv10_fixbits + (-10000)*main_conv10_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv10_enob
solver.Add( + (1)*main_conv10_fixp + (1)*main_conv10_float + (1)*main_conv10_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv10_fixbits + (-10000)*main_conv10_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv10_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv11 = sitofp i32 %j.0 to double, !taffo.info !29, !taffo.initweight !27
main_conv11_fixbits = solver.IntVar(0, 23, 'main_conv11_fixbits')
main_conv11_fixp = solver.IntVar(0, 1, 'main_conv11_fixp')
main_conv11_float = solver.IntVar(0, 1, 'main_conv11_float')
main_conv11_double = solver.IntVar(0, 1, 'main_conv11_double')
main_conv11_enob = solver.IntVar(-10000, 10000, 'main_conv11_enob')
solver.Add( + (1)*main_conv11_enob + (-1)*main_conv11_fixbits + (10000)*main_conv11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv11_enob + (10000)*main_conv11_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv11_enob + (10000)*main_conv11_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv11_fixbits + (-10000)*main_conv11_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_conv11_enob
solver.Add( + (1)*main_conv11_fixp + (1)*main_conv11_float + (1)*main_conv11_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv11_fixbits + (-10000)*main_conv11_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv11_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %mul = fmul double %conv10, %conv11, !taffo.info !30, !taffo.initweight !28
main_conv10_CAST_mul_fixbits = solver.IntVar(0, 23, 'main_conv10_CAST_mul_fixbits')
main_conv10_CAST_mul_fixp = solver.IntVar(0, 1, 'main_conv10_CAST_mul_fixp')
main_conv10_CAST_mul_float = solver.IntVar(0, 1, 'main_conv10_CAST_mul_float')
main_conv10_CAST_mul_double = solver.IntVar(0, 1, 'main_conv10_CAST_mul_double')
solver.Add( + (1)*main_conv10_CAST_mul_fixp + (1)*main_conv10_CAST_mul_float + (1)*main_conv10_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv10_CAST_mul_fixbits + (-10000)*main_conv10_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C1_main_conv10_CAST_mul')
C2_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C2_main_conv10_CAST_mul')
solver.Add( + (1)*main_conv10_fixbits + (-1)*main_conv10_CAST_mul_fixbits + (-10000)*C1_main_conv10_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv10_fixbits + (1)*main_conv10_CAST_mul_fixbits + (-10000)*C2_main_conv10_CAST_mul<=0)    #Shift cost 2
castCostObj =  + (1)*C1_main_conv10_CAST_mul
castCostObj +=  + (1)*C2_main_conv10_CAST_mul
C3_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C3_main_conv10_CAST_mul')
C4_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C4_main_conv10_CAST_mul')
C5_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C5_main_conv10_CAST_mul')
C6_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C6_main_conv10_CAST_mul')
C7_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C7_main_conv10_CAST_mul')
C8_main_conv10_CAST_mul = solver.IntVar(0, 1, 'C8_main_conv10_CAST_mul')
solver.Add( + (1)*main_conv10_fixp + (1)*main_conv10_CAST_mul_float + (-1)*C3_main_conv10_CAST_mul<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_main_conv10_CAST_mul
solver.Add( + (1)*main_conv10_float + (1)*main_conv10_CAST_mul_fixp + (-1)*C4_main_conv10_CAST_mul<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_conv10_CAST_mul
solver.Add( + (1)*main_conv10_fixp + (1)*main_conv10_CAST_mul_double + (-1)*C5_main_conv10_CAST_mul<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_conv10_CAST_mul
solver.Add( + (1)*main_conv10_double + (1)*main_conv10_CAST_mul_fixp + (-1)*C6_main_conv10_CAST_mul<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_conv10_CAST_mul
solver.Add( + (1)*main_conv10_float + (1)*main_conv10_CAST_mul_double + (-1)*C7_main_conv10_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_conv10_CAST_mul
solver.Add( + (1)*main_conv10_double + (1)*main_conv10_CAST_mul_float + (-1)*C8_main_conv10_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_conv10_CAST_mul



#Constraint for cast for   %mul = fmul double %conv10, %conv11, !taffo.info !30, !taffo.initweight !28
main_conv11_CAST_mul_fixbits = solver.IntVar(0, 23, 'main_conv11_CAST_mul_fixbits')
main_conv11_CAST_mul_fixp = solver.IntVar(0, 1, 'main_conv11_CAST_mul_fixp')
main_conv11_CAST_mul_float = solver.IntVar(0, 1, 'main_conv11_CAST_mul_float')
main_conv11_CAST_mul_double = solver.IntVar(0, 1, 'main_conv11_CAST_mul_double')
solver.Add( + (1)*main_conv11_CAST_mul_fixp + (1)*main_conv11_CAST_mul_float + (1)*main_conv11_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv11_CAST_mul_fixbits + (-10000)*main_conv11_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C1_main_conv11_CAST_mul')
C2_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C2_main_conv11_CAST_mul')
solver.Add( + (1)*main_conv11_fixbits + (-1)*main_conv11_CAST_mul_fixbits + (-10000)*C1_main_conv11_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv11_fixbits + (1)*main_conv11_CAST_mul_fixbits + (-10000)*C2_main_conv11_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv11_CAST_mul
castCostObj +=  + (1)*C2_main_conv11_CAST_mul
C3_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C3_main_conv11_CAST_mul')
C4_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C4_main_conv11_CAST_mul')
C5_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C5_main_conv11_CAST_mul')
C6_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C6_main_conv11_CAST_mul')
C7_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C7_main_conv11_CAST_mul')
C8_main_conv11_CAST_mul = solver.IntVar(0, 1, 'C8_main_conv11_CAST_mul')
solver.Add( + (1)*main_conv11_fixp + (1)*main_conv11_CAST_mul_float + (-1)*C3_main_conv11_CAST_mul<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_main_conv11_CAST_mul
solver.Add( + (1)*main_conv11_float + (1)*main_conv11_CAST_mul_fixp + (-1)*C4_main_conv11_CAST_mul<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_conv11_CAST_mul
solver.Add( + (1)*main_conv11_fixp + (1)*main_conv11_CAST_mul_double + (-1)*C5_main_conv11_CAST_mul<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_conv11_CAST_mul
solver.Add( + (1)*main_conv11_double + (1)*main_conv11_CAST_mul_fixp + (-1)*C6_main_conv11_CAST_mul<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_conv11_CAST_mul
solver.Add( + (1)*main_conv11_float + (1)*main_conv11_CAST_mul_double + (-1)*C7_main_conv11_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_conv11_CAST_mul
solver.Add( + (1)*main_conv11_double + (1)*main_conv11_CAST_mul_float + (-1)*C8_main_conv11_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_conv11_CAST_mul



#Stuff for   %mul = fmul double %conv10, %conv11, !taffo.info !30, !taffo.initweight !28
main_mul_fixbits = solver.IntVar(0, 15, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj +=  + (-1)*main_mul_enob
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv10_CAST_mul_fixp + (-1)*main_conv11_CAST_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_conv10_CAST_mul_float + (-1)*main_conv11_CAST_mul_float==0)    #float equality
solver.Add( + (1)*main_conv10_CAST_mul_double + (-1)*main_conv11_CAST_mul_double==0)    #double equality
solver.Add( + (1)*main_conv10_CAST_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_conv10_CAST_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*main_conv10_CAST_mul_double + (-1)*main_mul_double==0)    #double equality
mathCostObj =  + (1.35882)*main_mul_fixp
mathCostObj +=  + (1.82592)*main_mul_float
mathCostObj +=  + (1.56282)*main_mul_double
main_main_mul_enob_1 = solver.IntVar(0, 1, 'main_main_mul_enob_1')
main_main_mul_enob_2 = solver.IntVar(0, 1, 'main_main_mul_enob_2')
solver.Add( + (1)*main_main_mul_enob_1 + (1)*main_main_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul_enob + (-1)*main_conv11_enob + (-10000)*main_main_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul_enob + (-1)*main_conv10_enob + (-10000)*main_main_mul_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for double 2.400000e+02
ConstantValue__fixbits = solver.IntVar(0, 24, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10016)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10045)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.400000e+02
ConstantValue__0_fixbits = solver.IntVar(0, 24, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10016)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10045)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double %mul, 2.400000e+02, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !35
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
castCostObj +=  + (2.0753)*C3_main_mul_CAST_div
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_div_fixp + (-1)*C4_main_mul_CAST_div<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_mul_CAST_div
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_div_double + (-1)*C5_main_mul_CAST_div<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_mul_CAST_div
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_div_fixp + (-1)*C6_main_mul_CAST_div<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_mul_CAST_div
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_div_double + (-1)*C7_main_mul_CAST_div<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_mul_CAST_div
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_div_float + (-1)*C8_main_mul_CAST_div<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_mul_CAST_div



#Stuff for double 2.400000e+02
ConstantValue__1_fixbits = solver.IntVar(0, 24, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10016)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10045)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double %mul, 2.400000e+02, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !35
ConstantValue__1_CAST_div_fixbits = solver.IntVar(0, 24, 'ConstantValue__1_CAST_div_fixbits')
ConstantValue__1_CAST_div_fixp = solver.IntVar(0, 1, 'ConstantValue__1_CAST_div_fixp')
ConstantValue__1_CAST_div_float = solver.IntVar(0, 1, 'ConstantValue__1_CAST_div_float')
ConstantValue__1_CAST_div_double = solver.IntVar(0, 1, 'ConstantValue__1_CAST_div_double')
solver.Add( + (1)*ConstantValue__1_CAST_div_fixp + (1)*ConstantValue__1_CAST_div_float + (1)*ConstantValue__1_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__1_CAST_div_fixbits + (-10000)*ConstantValue__1_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C1_ConstantValue__1_CAST_div')
C2_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C2_ConstantValue__1_CAST_div')
solver.Add( + (1)*ConstantValue__1_fixbits + (-1)*ConstantValue__1_CAST_div_fixbits + (-10000)*C1_ConstantValue__1_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__1_fixbits + (1)*ConstantValue__1_CAST_div_fixbits + (-10000)*C2_ConstantValue__1_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__1_CAST_div
castCostObj +=  + (1)*C2_ConstantValue__1_CAST_div
C3_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C3_ConstantValue__1_CAST_div')
C4_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C4_ConstantValue__1_CAST_div')
C5_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C5_ConstantValue__1_CAST_div')
C6_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C6_ConstantValue__1_CAST_div')
C7_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C7_ConstantValue__1_CAST_div')
C8_ConstantValue__1_CAST_div = solver.IntVar(0, 1, 'C8_ConstantValue__1_CAST_div')
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_div_float + (-1)*C3_ConstantValue__1_CAST_div<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_div_fixp + (-1)*C4_ConstantValue__1_CAST_div<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_div_double + (-1)*C5_ConstantValue__1_CAST_div<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_div_fixp + (-1)*C6_ConstantValue__1_CAST_div<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_div_double + (-1)*C7_ConstantValue__1_CAST_div<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_div_float + (-1)*C8_ConstantValue__1_CAST_div<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_ConstantValue__1_CAST_div



#Stuff for   %div = fdiv double %mul, 2.400000e+02, !taffo.info !32, !taffo.initweight !34, !taffo.constinfo !35
main_div_fixbits = solver.IntVar(0, 23, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10031)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=10060)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9978)    #Limit the lower number of frac bits23
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul_CAST_div_fixp + (-1)*ConstantValue__1_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div_float + (-1)*ConstantValue__1_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div_double + (-1)*ConstantValue__1_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_mul_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj +=  + (3.97899)*main_div_fixp
mathCostObj +=  + (2.0321)*main_div_float
mathCostObj +=  + (2.21275)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*ConstantValue__enob + (-10000)*main_main_div_enob_1<=16)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_mul_enob + (-10000)*main_main_div_enob_2<=8)    #Enob: propagation in division 2



#Constraint for cast for   store double %div, double* %arrayidx13, align 8, !taffo.info !8, !taffo.initweight !28
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
castCostObj +=  + (2.0753)*C3_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_fixp + (-1)*C4_main_div_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_div_CAST_store
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_double + (-1)*C5_main_div_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_fixp + (-1)*C6_main_div_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_double + (-1)*C7_main_div_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_float + (-1)*C8_main_div_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_div_CAST_store
solver.Add( + (1)*data_fixp + (-1)*main_div_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*data_float + (-1)*main_div_CAST_store_float==0)    #float equality
solver.Add( + (1)*data_double + (-1)*main_div_CAST_store_double==0)    #double equality
solver.Add( + (1)*data_fixbits + (-1)*main_div_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
data_enob_storeENOB = solver.IntVar(-10000, 10000, 'data_enob_storeENOB')
solver.Add( + (1)*data_enob_storeENOB + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob_storeENOB + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob_storeENOB + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_enob_storeENOB + (-1)*main_div_enob<=0)    #Enob constraint ENOB propagation in load/store



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



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx22, align 8, !taffo.info !40, !taffo.initweight !27, !taffo.constinfo !41
ConstantValue__3_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__3_CAST_store_fixbits')
ConstantValue__3_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__3_CAST_store_fixp')
ConstantValue__3_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__3_CAST_store_float')
ConstantValue__3_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__3_CAST_store_double')
solver.Add( + (1)*ConstantValue__3_CAST_store_fixp + (1)*ConstantValue__3_CAST_store_float + (1)*ConstantValue__3_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__3_CAST_store_fixbits + (-10000)*ConstantValue__3_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__3_CAST_store')
C2_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__3_CAST_store')
solver.Add( + (1)*ConstantValue__3_fixbits + (-1)*ConstantValue__3_CAST_store_fixbits + (-10000)*C1_ConstantValue__3_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__3_fixbits + (1)*ConstantValue__3_CAST_store_fixbits + (-10000)*C2_ConstantValue__3_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__3_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__3_CAST_store
C3_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__3_CAST_store')
C4_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__3_CAST_store')
C5_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__3_CAST_store')
C6_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__3_CAST_store')
C7_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__3_CAST_store')
C8_ConstantValue__3_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__3_CAST_store')
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_store_float + (-1)*C3_ConstantValue__3_CAST_store<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_ConstantValue__3_CAST_store
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_store_fixp + (-1)*C4_ConstantValue__3_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_ConstantValue__3_CAST_store
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_store_double + (-1)*C5_ConstantValue__3_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_ConstantValue__3_CAST_store
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_store_fixp + (-1)*C6_ConstantValue__3_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_ConstantValue__3_CAST_store
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_store_double + (-1)*C7_ConstantValue__3_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_ConstantValue__3_CAST_store
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_store_float + (-1)*C8_ConstantValue__3_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_ConstantValue__3_CAST_store
solver.Add( + (1)*mean_fixp + (-1)*ConstantValue__3_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*ConstantValue__3_CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*ConstantValue__3_CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*ConstantValue__3_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp')
solver.Add( + (1)*data_enob_memphi_main_tmp + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
solver.Add( + (1)*main_main_tmp_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp + (-1)*data_enob_storeENOB + (10000)*main_main_tmp_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
mean_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp1')
solver.Add( + (1)*mean_enob_memphi_main_tmp1 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
solver.Add( + (1)*main_main_tmp1_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add = fadd double %tmp1, %tmp, !taffo.info !12, !taffo.initweight !28
mean_CAST_add_fixbits = solver.IntVar(0, 6, 'mean_CAST_add_fixbits')
mean_CAST_add_fixp = solver.IntVar(0, 1, 'mean_CAST_add_fixp')
mean_CAST_add_float = solver.IntVar(0, 1, 'mean_CAST_add_float')
mean_CAST_add_double = solver.IntVar(0, 1, 'mean_CAST_add_double')
solver.Add( + (1)*mean_CAST_add_fixp + (1)*mean_CAST_add_float + (1)*mean_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_add_fixbits + (-10000)*mean_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_add = solver.IntVar(0, 1, 'C1_mean_CAST_add')
C2_mean_CAST_add = solver.IntVar(0, 1, 'C2_mean_CAST_add')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_add_fixbits + (-10000)*C1_mean_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_add_fixbits + (-10000)*C2_mean_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mean_CAST_add
castCostObj +=  + (1)*C2_mean_CAST_add
C3_mean_CAST_add = solver.IntVar(0, 1, 'C3_mean_CAST_add')
C4_mean_CAST_add = solver.IntVar(0, 1, 'C4_mean_CAST_add')
C5_mean_CAST_add = solver.IntVar(0, 1, 'C5_mean_CAST_add')
C6_mean_CAST_add = solver.IntVar(0, 1, 'C6_mean_CAST_add')
C7_mean_CAST_add = solver.IntVar(0, 1, 'C7_mean_CAST_add')
C8_mean_CAST_add = solver.IntVar(0, 1, 'C8_mean_CAST_add')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_add_float + (-1)*C3_mean_CAST_add<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_mean_CAST_add
solver.Add( + (1)*mean_float + (1)*mean_CAST_add_fixp + (-1)*C4_mean_CAST_add<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_mean_CAST_add
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_add_double + (-1)*C5_mean_CAST_add<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_mean_CAST_add
solver.Add( + (1)*mean_double + (1)*mean_CAST_add_fixp + (-1)*C6_mean_CAST_add<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_mean_CAST_add
solver.Add( + (1)*mean_float + (1)*mean_CAST_add_double + (-1)*C7_mean_CAST_add<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_mean_CAST_add
solver.Add( + (1)*mean_double + (1)*mean_CAST_add_float + (-1)*C8_mean_CAST_add<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_mean_CAST_add



#Constraint for cast for   %add = fadd double %tmp1, %tmp, !taffo.info !12, !taffo.initweight !28
data_CAST_add_fixbits = solver.IntVar(0, 9, 'data_CAST_add_fixbits')
data_CAST_add_fixp = solver.IntVar(0, 1, 'data_CAST_add_fixp')
data_CAST_add_float = solver.IntVar(0, 1, 'data_CAST_add_float')
data_CAST_add_double = solver.IntVar(0, 1, 'data_CAST_add_double')
solver.Add( + (1)*data_CAST_add_fixp + (1)*data_CAST_add_float + (1)*data_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_add_fixbits + (-10000)*data_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_add = solver.IntVar(0, 1, 'C1_data_CAST_add')
C2_data_CAST_add = solver.IntVar(0, 1, 'C2_data_CAST_add')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_add_fixbits + (-10000)*C1_data_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_add_fixbits + (-10000)*C2_data_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_add
castCostObj +=  + (1)*C2_data_CAST_add
C3_data_CAST_add = solver.IntVar(0, 1, 'C3_data_CAST_add')
C4_data_CAST_add = solver.IntVar(0, 1, 'C4_data_CAST_add')
C5_data_CAST_add = solver.IntVar(0, 1, 'C5_data_CAST_add')
C6_data_CAST_add = solver.IntVar(0, 1, 'C6_data_CAST_add')
C7_data_CAST_add = solver.IntVar(0, 1, 'C7_data_CAST_add')
C8_data_CAST_add = solver.IntVar(0, 1, 'C8_data_CAST_add')
solver.Add( + (1)*data_fixp + (1)*data_CAST_add_float + (-1)*C3_data_CAST_add<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_data_CAST_add
solver.Add( + (1)*data_float + (1)*data_CAST_add_fixp + (-1)*C4_data_CAST_add<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_data_CAST_add
solver.Add( + (1)*data_fixp + (1)*data_CAST_add_double + (-1)*C5_data_CAST_add<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_data_CAST_add
solver.Add( + (1)*data_double + (1)*data_CAST_add_fixp + (-1)*C6_data_CAST_add<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_data_CAST_add
solver.Add( + (1)*data_float + (1)*data_CAST_add_double + (-1)*C7_data_CAST_add<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_data_CAST_add
solver.Add( + (1)*data_double + (1)*data_CAST_add_float + (-1)*C8_data_CAST_add<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_data_CAST_add



#Stuff for   %add = fadd double %tmp1, %tmp, !taffo.info !12, !taffo.initweight !28
main_add_fixbits = solver.IntVar(0, 6, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
main_add_enob = solver.IntVar(-10000, 10000, 'main_add_enob')
solver.Add( + (1)*main_add_enob + (-1)*main_add_fixbits + (10000)*main_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add_enob + (10000)*main_add_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add_enob + (10000)*main_add_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp>=-9995)    #Limit the lower number of frac bits6
solver.Add( + (1)*main_add_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add_enob
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
mathCostObj +=  + (1.0518)*main_add_fixp
mathCostObj +=  + (1.02933)*main_add_float
mathCostObj +=  + (1.39384)*main_add_double
solver.Add( + (1)*main_add_enob + (-1)*mean_enob_memphi_main_tmp1<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*data_enob_memphi_main_tmp<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add, double* %arrayidx32, align 8, !taffo.info !40, !taffo.initweight !27
main_add_CAST_store_fixbits = solver.IntVar(0, 6, 'main_add_CAST_store_fixbits')
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
castCostObj +=  + (2.0753)*C3_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_fixp + (-1)*C4_main_add_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_add_CAST_store
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_double + (-1)*C5_main_add_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_fixp + (-1)*C6_main_add_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_double + (-1)*C7_main_add_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_float + (-1)*C8_main_add_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_add_CAST_store
solver.Add( + (1)*mean_fixp + (-1)*main_add_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*main_add_CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*main_add_CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*main_add_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
mean_enob_storeENOB = solver.IntVar(-10000, 10000, 'mean_enob_storeENOB')
solver.Add( + (1)*mean_enob_storeENOB + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob_storeENOB + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob_storeENOB + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_enob_storeENOB + (-1)*main_add_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp1 + (-1)*mean_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
mean_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp2')
solver.Add( + (1)*mean_enob_memphi_main_tmp2 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
solver.Add( + (1)*main_main_tmp2_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp2 + (-1)*mean_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div38 = fdiv double %tmp2, %conv, !taffo.info !44, !taffo.initweight !27
mean_CAST_div38_fixbits = solver.IntVar(0, 6, 'mean_CAST_div38_fixbits')
mean_CAST_div38_fixp = solver.IntVar(0, 1, 'mean_CAST_div38_fixp')
mean_CAST_div38_float = solver.IntVar(0, 1, 'mean_CAST_div38_float')
mean_CAST_div38_double = solver.IntVar(0, 1, 'mean_CAST_div38_double')
solver.Add( + (1)*mean_CAST_div38_fixp + (1)*mean_CAST_div38_float + (1)*mean_CAST_div38_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_div38_fixbits + (-10000)*mean_CAST_div38_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_div38 = solver.IntVar(0, 1, 'C1_mean_CAST_div38')
C2_mean_CAST_div38 = solver.IntVar(0, 1, 'C2_mean_CAST_div38')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_div38_fixbits + (-10000)*C1_mean_CAST_div38<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_div38_fixbits + (-10000)*C2_mean_CAST_div38<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mean_CAST_div38
castCostObj +=  + (1)*C2_mean_CAST_div38
C3_mean_CAST_div38 = solver.IntVar(0, 1, 'C3_mean_CAST_div38')
C4_mean_CAST_div38 = solver.IntVar(0, 1, 'C4_mean_CAST_div38')
C5_mean_CAST_div38 = solver.IntVar(0, 1, 'C5_mean_CAST_div38')
C6_mean_CAST_div38 = solver.IntVar(0, 1, 'C6_mean_CAST_div38')
C7_mean_CAST_div38 = solver.IntVar(0, 1, 'C7_mean_CAST_div38')
C8_mean_CAST_div38 = solver.IntVar(0, 1, 'C8_mean_CAST_div38')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_div38_float + (-1)*C3_mean_CAST_div38<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_mean_CAST_div38
solver.Add( + (1)*mean_float + (1)*mean_CAST_div38_fixp + (-1)*C4_mean_CAST_div38<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_mean_CAST_div38
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_div38_double + (-1)*C5_mean_CAST_div38<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_mean_CAST_div38
solver.Add( + (1)*mean_double + (1)*mean_CAST_div38_fixp + (-1)*C6_mean_CAST_div38<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_mean_CAST_div38
solver.Add( + (1)*mean_float + (1)*mean_CAST_div38_double + (-1)*C7_mean_CAST_div38<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_mean_CAST_div38
solver.Add( + (1)*mean_double + (1)*mean_CAST_div38_float + (-1)*C8_mean_CAST_div38<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_mean_CAST_div38



#Constraint for cast for   %div38 = fdiv double %tmp2, %conv, !taffo.info !44, !taffo.initweight !27
main_conv_CAST_div38_fixbits = solver.IntVar(0, 23, 'main_conv_CAST_div38_fixbits')
main_conv_CAST_div38_fixp = solver.IntVar(0, 1, 'main_conv_CAST_div38_fixp')
main_conv_CAST_div38_float = solver.IntVar(0, 1, 'main_conv_CAST_div38_float')
main_conv_CAST_div38_double = solver.IntVar(0, 1, 'main_conv_CAST_div38_double')
solver.Add( + (1)*main_conv_CAST_div38_fixp + (1)*main_conv_CAST_div38_float + (1)*main_conv_CAST_div38_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv_CAST_div38_fixbits + (-10000)*main_conv_CAST_div38_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C1_main_conv_CAST_div38')
C2_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C2_main_conv_CAST_div38')
solver.Add( + (1)*main_conv_fixbits + (-1)*main_conv_CAST_div38_fixbits + (-10000)*C1_main_conv_CAST_div38<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv_fixbits + (1)*main_conv_CAST_div38_fixbits + (-10000)*C2_main_conv_CAST_div38<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv_CAST_div38
castCostObj +=  + (1)*C2_main_conv_CAST_div38
C3_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C3_main_conv_CAST_div38')
C4_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C4_main_conv_CAST_div38')
C5_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C5_main_conv_CAST_div38')
C6_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C6_main_conv_CAST_div38')
C7_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C7_main_conv_CAST_div38')
C8_main_conv_CAST_div38 = solver.IntVar(0, 1, 'C8_main_conv_CAST_div38')
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_div38_float + (-1)*C3_main_conv_CAST_div38<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_main_conv_CAST_div38
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div38_fixp + (-1)*C4_main_conv_CAST_div38<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_conv_CAST_div38
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_div38_double + (-1)*C5_main_conv_CAST_div38<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_conv_CAST_div38
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div38_fixp + (-1)*C6_main_conv_CAST_div38<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_conv_CAST_div38
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div38_double + (-1)*C7_main_conv_CAST_div38<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_conv_CAST_div38
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div38_float + (-1)*C8_main_conv_CAST_div38<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_conv_CAST_div38



#Stuff for   %div38 = fdiv double %tmp2, %conv, !taffo.info !44, !taffo.initweight !27
main_div38_fixbits = solver.IntVar(0, 16, 'main_div38_fixbits')
main_div38_fixp = solver.IntVar(0, 1, 'main_div38_fixp')
main_div38_float = solver.IntVar(0, 1, 'main_div38_float')
main_div38_double = solver.IntVar(0, 1, 'main_div38_double')
main_div38_enob = solver.IntVar(-10000, 10000, 'main_div38_enob')
solver.Add( + (1)*main_div38_enob + (-1)*main_div38_fixbits + (10000)*main_div38_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div38_enob + (10000)*main_div38_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div38_enob + (10000)*main_div38_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div38_fixbits + (-10000)*main_div38_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_div38_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_div38_enob
solver.Add( + (1)*main_div38_fixp + (1)*main_div38_float + (1)*main_div38_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div38_fixbits + (-10000)*main_div38_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*mean_CAST_div38_fixp + (-1)*main_conv_CAST_div38_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_div38_float + (-1)*main_conv_CAST_div38_float==0)    #float equality
solver.Add( + (1)*mean_CAST_div38_double + (-1)*main_conv_CAST_div38_double==0)    #double equality
solver.Add( + (1)*mean_CAST_div38_fixp + (-1)*main_div38_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_div38_float + (-1)*main_div38_float==0)    #float equality
solver.Add( + (1)*mean_CAST_div38_double + (-1)*main_div38_double==0)    #double equality
mathCostObj +=  + (3.97899)*main_div38_fixp
mathCostObj +=  + (2.0321)*main_div38_float
mathCostObj +=  + (2.21275)*main_div38_double
main_main_div38_enob_1 = solver.IntVar(0, 1, 'main_main_div38_enob_1')
main_main_div38_enob_2 = solver.IntVar(0, 1, 'main_main_div38_enob_2')
solver.Add( + (1)*main_main_div38_enob_1 + (1)*main_main_div38_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div38_enob + (-1)*main_conv_enob + (-10000)*main_main_div38_enob_1<=1040)    #Enob: propagation in division 1
solver.Add( + (1)*main_div38_enob + (-1)*mean_enob_memphi_main_tmp2 + (-10000)*main_main_div38_enob_2<=8)    #Enob: propagation in division 2



#Constraint for cast for   store double %div38, double* %arrayidx37, align 8, !taffo.info !40, !taffo.initweight !27
main_div38_CAST_store_fixbits = solver.IntVar(0, 16, 'main_div38_CAST_store_fixbits')
main_div38_CAST_store_fixp = solver.IntVar(0, 1, 'main_div38_CAST_store_fixp')
main_div38_CAST_store_float = solver.IntVar(0, 1, 'main_div38_CAST_store_float')
main_div38_CAST_store_double = solver.IntVar(0, 1, 'main_div38_CAST_store_double')
solver.Add( + (1)*main_div38_CAST_store_fixp + (1)*main_div38_CAST_store_float + (1)*main_div38_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div38_CAST_store_fixbits + (-10000)*main_div38_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div38_CAST_store = solver.IntVar(0, 1, 'C1_main_div38_CAST_store')
C2_main_div38_CAST_store = solver.IntVar(0, 1, 'C2_main_div38_CAST_store')
solver.Add( + (1)*main_div38_fixbits + (-1)*main_div38_CAST_store_fixbits + (-10000)*C1_main_div38_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div38_fixbits + (1)*main_div38_CAST_store_fixbits + (-10000)*C2_main_div38_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div38_CAST_store
castCostObj +=  + (1)*C2_main_div38_CAST_store
C3_main_div38_CAST_store = solver.IntVar(0, 1, 'C3_main_div38_CAST_store')
C4_main_div38_CAST_store = solver.IntVar(0, 1, 'C4_main_div38_CAST_store')
C5_main_div38_CAST_store = solver.IntVar(0, 1, 'C5_main_div38_CAST_store')
C6_main_div38_CAST_store = solver.IntVar(0, 1, 'C6_main_div38_CAST_store')
C7_main_div38_CAST_store = solver.IntVar(0, 1, 'C7_main_div38_CAST_store')
C8_main_div38_CAST_store = solver.IntVar(0, 1, 'C8_main_div38_CAST_store')
solver.Add( + (1)*main_div38_fixp + (1)*main_div38_CAST_store_float + (-1)*C3_main_div38_CAST_store<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_main_div38_CAST_store
solver.Add( + (1)*main_div38_float + (1)*main_div38_CAST_store_fixp + (-1)*C4_main_div38_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_div38_CAST_store
solver.Add( + (1)*main_div38_fixp + (1)*main_div38_CAST_store_double + (-1)*C5_main_div38_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_div38_CAST_store
solver.Add( + (1)*main_div38_double + (1)*main_div38_CAST_store_fixp + (-1)*C6_main_div38_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_div38_CAST_store
solver.Add( + (1)*main_div38_float + (1)*main_div38_CAST_store_double + (-1)*C7_main_div38_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_div38_CAST_store
solver.Add( + (1)*main_div38_double + (1)*main_div38_CAST_store_float + (-1)*C8_main_div38_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_div38_CAST_store
solver.Add( + (1)*mean_fixp + (-1)*main_div38_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*main_div38_CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*main_div38_CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*main_div38_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
mean_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'mean_enob_storeENOB_storeENOB')
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_enob_storeENOB_storeENOB + (-1)*main_div38_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
mean_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp3')
solver.Add( + (1)*mean_enob_memphi_main_tmp3 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_2==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp3 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp3_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp3 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp4')
solver.Add( + (1)*data_enob_memphi_main_tmp4 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp4 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp4_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp4 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub = fsub double %tmp4, %tmp3, !taffo.info !46, !taffo.initweight !28
data_CAST_sub_fixbits = solver.IntVar(0, 9, 'data_CAST_sub_fixbits')
data_CAST_sub_fixp = solver.IntVar(0, 1, 'data_CAST_sub_fixp')
data_CAST_sub_float = solver.IntVar(0, 1, 'data_CAST_sub_float')
data_CAST_sub_double = solver.IntVar(0, 1, 'data_CAST_sub_double')
solver.Add( + (1)*data_CAST_sub_fixp + (1)*data_CAST_sub_float + (1)*data_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_sub_fixbits + (-10000)*data_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_sub = solver.IntVar(0, 1, 'C1_data_CAST_sub')
C2_data_CAST_sub = solver.IntVar(0, 1, 'C2_data_CAST_sub')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_sub_fixbits + (-10000)*C1_data_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_sub_fixbits + (-10000)*C2_data_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_sub
castCostObj +=  + (1)*C2_data_CAST_sub
C3_data_CAST_sub = solver.IntVar(0, 1, 'C3_data_CAST_sub')
C4_data_CAST_sub = solver.IntVar(0, 1, 'C4_data_CAST_sub')
C5_data_CAST_sub = solver.IntVar(0, 1, 'C5_data_CAST_sub')
C6_data_CAST_sub = solver.IntVar(0, 1, 'C6_data_CAST_sub')
C7_data_CAST_sub = solver.IntVar(0, 1, 'C7_data_CAST_sub')
C8_data_CAST_sub = solver.IntVar(0, 1, 'C8_data_CAST_sub')
solver.Add( + (1)*data_fixp + (1)*data_CAST_sub_float + (-1)*C3_data_CAST_sub<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_data_CAST_sub
solver.Add( + (1)*data_float + (1)*data_CAST_sub_fixp + (-1)*C4_data_CAST_sub<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_data_CAST_sub
solver.Add( + (1)*data_fixp + (1)*data_CAST_sub_double + (-1)*C5_data_CAST_sub<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_data_CAST_sub
solver.Add( + (1)*data_double + (1)*data_CAST_sub_fixp + (-1)*C6_data_CAST_sub<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_data_CAST_sub
solver.Add( + (1)*data_float + (1)*data_CAST_sub_double + (-1)*C7_data_CAST_sub<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_data_CAST_sub
solver.Add( + (1)*data_double + (1)*data_CAST_sub_float + (-1)*C8_data_CAST_sub<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_data_CAST_sub



#Constraint for cast for   %sub = fsub double %tmp4, %tmp3, !taffo.info !46, !taffo.initweight !28
mean_CAST_sub_fixbits = solver.IntVar(0, 6, 'mean_CAST_sub_fixbits')
mean_CAST_sub_fixp = solver.IntVar(0, 1, 'mean_CAST_sub_fixp')
mean_CAST_sub_float = solver.IntVar(0, 1, 'mean_CAST_sub_float')
mean_CAST_sub_double = solver.IntVar(0, 1, 'mean_CAST_sub_double')
solver.Add( + (1)*mean_CAST_sub_fixp + (1)*mean_CAST_sub_float + (1)*mean_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_sub_fixbits + (-10000)*mean_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_sub = solver.IntVar(0, 1, 'C1_mean_CAST_sub')
C2_mean_CAST_sub = solver.IntVar(0, 1, 'C2_mean_CAST_sub')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_sub_fixbits + (-10000)*C1_mean_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_sub_fixbits + (-10000)*C2_mean_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mean_CAST_sub
castCostObj +=  + (1)*C2_mean_CAST_sub
C3_mean_CAST_sub = solver.IntVar(0, 1, 'C3_mean_CAST_sub')
C4_mean_CAST_sub = solver.IntVar(0, 1, 'C4_mean_CAST_sub')
C5_mean_CAST_sub = solver.IntVar(0, 1, 'C5_mean_CAST_sub')
C6_mean_CAST_sub = solver.IntVar(0, 1, 'C6_mean_CAST_sub')
C7_mean_CAST_sub = solver.IntVar(0, 1, 'C7_mean_CAST_sub')
C8_mean_CAST_sub = solver.IntVar(0, 1, 'C8_mean_CAST_sub')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_sub_float + (-1)*C3_mean_CAST_sub<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_mean_CAST_sub
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub_fixp + (-1)*C4_mean_CAST_sub<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_mean_CAST_sub
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_sub_double + (-1)*C5_mean_CAST_sub<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_mean_CAST_sub
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub_fixp + (-1)*C6_mean_CAST_sub<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_mean_CAST_sub
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub_double + (-1)*C7_mean_CAST_sub<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_mean_CAST_sub
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub_float + (-1)*C8_mean_CAST_sub<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_mean_CAST_sub



#Stuff for   %sub = fsub double %tmp4, %tmp3, !taffo.info !46, !taffo.initweight !28
main_sub_fixbits = solver.IntVar(0, 6, 'main_sub_fixbits')
main_sub_fixp = solver.IntVar(0, 1, 'main_sub_fixp')
main_sub_float = solver.IntVar(0, 1, 'main_sub_float')
main_sub_double = solver.IntVar(0, 1, 'main_sub_double')
main_sub_enob = solver.IntVar(-10000, 10000, 'main_sub_enob')
solver.Add( + (1)*main_sub_enob + (-1)*main_sub_fixbits + (10000)*main_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp>=-9995)    #Limit the lower number of frac bits6
solver.Add( + (1)*main_sub_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub_enob
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_float + (1)*main_sub_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*data_CAST_sub_fixp + (-1)*mean_CAST_sub_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_sub_float + (-1)*mean_CAST_sub_float==0)    #float equality
solver.Add( + (1)*data_CAST_sub_double + (-1)*mean_CAST_sub_double==0)    #double equality
solver.Add( + (1)*data_CAST_sub_fixbits + (-1)*mean_CAST_sub_fixbits==0)    #same fractional bit
solver.Add( + (1)*data_CAST_sub_fixp + (-1)*main_sub_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_sub_float + (-1)*main_sub_float==0)    #float equality
solver.Add( + (1)*data_CAST_sub_double + (-1)*main_sub_double==0)    #double equality
solver.Add( + (1)*data_CAST_sub_fixbits + (-1)*main_sub_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.0518)*main_sub_fixp
mathCostObj +=  + (1.02933)*main_sub_float
mathCostObj +=  + (1.39384)*main_sub_double
solver.Add( + (1)*main_sub_enob + (-1)*data_enob_memphi_main_tmp4<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub_enob + (-1)*mean_enob_memphi_main_tmp3<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub, double* %arrayidx55, align 8, !taffo.info !8, !taffo.initweight !28
main_sub_CAST_store_fixbits = solver.IntVar(0, 6, 'main_sub_CAST_store_fixbits')
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
castCostObj +=  + (2.0753)*C3_main_sub_CAST_store
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_store_fixp + (-1)*C4_main_sub_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_sub_CAST_store
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_store_double + (-1)*C5_main_sub_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_sub_CAST_store
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_store_fixp + (-1)*C6_main_sub_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_sub_CAST_store
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_store_double + (-1)*C7_main_sub_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_sub_CAST_store
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_store_float + (-1)*C8_main_sub_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_sub_CAST_store
solver.Add( + (1)*data_fixp + (-1)*main_sub_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*data_float + (-1)*main_sub_CAST_store_float==0)    #float equality
solver.Add( + (1)*data_double + (-1)*main_sub_CAST_store_double==0)    #double equality
solver.Add( + (1)*data_fixbits + (-1)*main_sub_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
data_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'data_enob_storeENOB_storeENOB')
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (-1)*main_sub_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp4 + (-1)*data_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



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



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx73, align 8, !taffo.info !8, !taffo.initweight !28, !taffo.constinfo !41
ConstantValue__5_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__5_CAST_store_fixbits')
ConstantValue__5_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__5_CAST_store_fixp')
ConstantValue__5_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__5_CAST_store_float')
ConstantValue__5_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__5_CAST_store_double')
solver.Add( + (1)*ConstantValue__5_CAST_store_fixp + (1)*ConstantValue__5_CAST_store_float + (1)*ConstantValue__5_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__5_CAST_store_fixbits + (-10000)*ConstantValue__5_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__5_CAST_store')
C2_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__5_CAST_store')
solver.Add( + (1)*ConstantValue__5_fixbits + (-1)*ConstantValue__5_CAST_store_fixbits + (-10000)*C1_ConstantValue__5_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__5_fixbits + (1)*ConstantValue__5_CAST_store_fixbits + (-10000)*C2_ConstantValue__5_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__5_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__5_CAST_store
C3_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__5_CAST_store')
C4_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__5_CAST_store')
C5_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__5_CAST_store')
C6_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__5_CAST_store')
C7_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__5_CAST_store')
C8_ConstantValue__5_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__5_CAST_store')
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_CAST_store_float + (-1)*C3_ConstantValue__5_CAST_store<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_ConstantValue__5_CAST_store
solver.Add( + (1)*ConstantValue__5_float + (1)*ConstantValue__5_CAST_store_fixp + (-1)*C4_ConstantValue__5_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_ConstantValue__5_CAST_store
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_CAST_store_double + (-1)*C5_ConstantValue__5_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_ConstantValue__5_CAST_store
solver.Add( + (1)*ConstantValue__5_double + (1)*ConstantValue__5_CAST_store_fixp + (-1)*C6_ConstantValue__5_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_ConstantValue__5_CAST_store
solver.Add( + (1)*ConstantValue__5_float + (1)*ConstantValue__5_CAST_store_double + (-1)*C7_ConstantValue__5_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_ConstantValue__5_CAST_store
solver.Add( + (1)*ConstantValue__5_double + (1)*ConstantValue__5_CAST_store_float + (-1)*C8_ConstantValue__5_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_ConstantValue__5_CAST_store
solver.Add( + (1)*cov_fixp + (-1)*ConstantValue__5_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*cov_float + (-1)*ConstantValue__5_CAST_store_float==0)    #float equality
solver.Add( + (1)*cov_double + (-1)*ConstantValue__5_CAST_store_double==0)    #double equality
solver.Add( + (1)*cov_fixbits + (-1)*ConstantValue__5_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp5')
solver.Add( + (1)*data_enob_memphi_main_tmp5 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp5 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp5_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp5 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp5 + (-1)*data_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp6')
solver.Add( + (1)*data_enob_memphi_main_tmp6 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
main_main_tmp6_enob_3 = solver.IntVar(0, 1, 'main_main_tmp6_enob_3')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2 + (1)*main_main_tmp6_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp6 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp6_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp6 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp6 + (-1)*data_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul86 = fmul double %tmp5, %tmp6, !taffo.info !48, !taffo.initweight !34
data_CAST_mul86_fixbits = solver.IntVar(0, 9, 'data_CAST_mul86_fixbits')
data_CAST_mul86_fixp = solver.IntVar(0, 1, 'data_CAST_mul86_fixp')
data_CAST_mul86_float = solver.IntVar(0, 1, 'data_CAST_mul86_float')
data_CAST_mul86_double = solver.IntVar(0, 1, 'data_CAST_mul86_double')
solver.Add( + (1)*data_CAST_mul86_fixp + (1)*data_CAST_mul86_float + (1)*data_CAST_mul86_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_mul86_fixbits + (-10000)*data_CAST_mul86_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_mul86 = solver.IntVar(0, 1, 'C1_data_CAST_mul86')
C2_data_CAST_mul86 = solver.IntVar(0, 1, 'C2_data_CAST_mul86')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_mul86_fixbits + (-10000)*C1_data_CAST_mul86<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_mul86_fixbits + (-10000)*C2_data_CAST_mul86<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_mul86
castCostObj +=  + (1)*C2_data_CAST_mul86
C3_data_CAST_mul86 = solver.IntVar(0, 1, 'C3_data_CAST_mul86')
C4_data_CAST_mul86 = solver.IntVar(0, 1, 'C4_data_CAST_mul86')
C5_data_CAST_mul86 = solver.IntVar(0, 1, 'C5_data_CAST_mul86')
C6_data_CAST_mul86 = solver.IntVar(0, 1, 'C6_data_CAST_mul86')
C7_data_CAST_mul86 = solver.IntVar(0, 1, 'C7_data_CAST_mul86')
C8_data_CAST_mul86 = solver.IntVar(0, 1, 'C8_data_CAST_mul86')
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul86_float + (-1)*C3_data_CAST_mul86<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_data_CAST_mul86
solver.Add( + (1)*data_float + (1)*data_CAST_mul86_fixp + (-1)*C4_data_CAST_mul86<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_data_CAST_mul86
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul86_double + (-1)*C5_data_CAST_mul86<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_data_CAST_mul86
solver.Add( + (1)*data_double + (1)*data_CAST_mul86_fixp + (-1)*C6_data_CAST_mul86<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_data_CAST_mul86
solver.Add( + (1)*data_float + (1)*data_CAST_mul86_double + (-1)*C7_data_CAST_mul86<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_data_CAST_mul86
solver.Add( + (1)*data_double + (1)*data_CAST_mul86_float + (-1)*C8_data_CAST_mul86<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_data_CAST_mul86



#Constraint for cast for   %mul86 = fmul double %tmp5, %tmp6, !taffo.info !48, !taffo.initweight !34
data_CAST_mul86_0_fixbits = solver.IntVar(0, 9, 'data_CAST_mul86_0_fixbits')
data_CAST_mul86_0_fixp = solver.IntVar(0, 1, 'data_CAST_mul86_0_fixp')
data_CAST_mul86_0_float = solver.IntVar(0, 1, 'data_CAST_mul86_0_float')
data_CAST_mul86_0_double = solver.IntVar(0, 1, 'data_CAST_mul86_0_double')
solver.Add( + (1)*data_CAST_mul86_0_fixp + (1)*data_CAST_mul86_0_float + (1)*data_CAST_mul86_0_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_mul86_0_fixbits + (-10000)*data_CAST_mul86_0_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C1_data_CAST_mul86_0')
C2_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C2_data_CAST_mul86_0')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_mul86_0_fixbits + (-10000)*C1_data_CAST_mul86_0<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_mul86_0_fixbits + (-10000)*C2_data_CAST_mul86_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_mul86_0
castCostObj +=  + (1)*C2_data_CAST_mul86_0
C3_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C3_data_CAST_mul86_0')
C4_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C4_data_CAST_mul86_0')
C5_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C5_data_CAST_mul86_0')
C6_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C6_data_CAST_mul86_0')
C7_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C7_data_CAST_mul86_0')
C8_data_CAST_mul86_0 = solver.IntVar(0, 1, 'C8_data_CAST_mul86_0')
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul86_0_float + (-1)*C3_data_CAST_mul86_0<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_data_CAST_mul86_0
solver.Add( + (1)*data_float + (1)*data_CAST_mul86_0_fixp + (-1)*C4_data_CAST_mul86_0<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_data_CAST_mul86_0
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul86_0_double + (-1)*C5_data_CAST_mul86_0<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_data_CAST_mul86_0
solver.Add( + (1)*data_double + (1)*data_CAST_mul86_0_fixp + (-1)*C6_data_CAST_mul86_0<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_data_CAST_mul86_0
solver.Add( + (1)*data_float + (1)*data_CAST_mul86_0_double + (-1)*C7_data_CAST_mul86_0<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_data_CAST_mul86_0
solver.Add( + (1)*data_double + (1)*data_CAST_mul86_0_float + (-1)*C8_data_CAST_mul86_0<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_data_CAST_mul86_0



#Stuff for   %mul86 = fmul double %tmp5, %tmp6, !taffo.info !48, !taffo.initweight !34
main_mul86_fixbits = solver.IntVar(0, 20, 'main_mul86_fixbits')
main_mul86_fixp = solver.IntVar(0, 1, 'main_mul86_fixp')
main_mul86_float = solver.IntVar(0, 1, 'main_mul86_float')
main_mul86_double = solver.IntVar(0, 1, 'main_mul86_double')
main_mul86_enob = solver.IntVar(-10000, 10000, 'main_mul86_enob')
solver.Add( + (1)*main_mul86_enob + (-1)*main_mul86_fixbits + (10000)*main_mul86_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul86_enob + (10000)*main_mul86_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul86_enob + (10000)*main_mul86_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul86_fixbits + (-10000)*main_mul86_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_mul86_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul86_enob
solver.Add( + (1)*main_mul86_fixp + (1)*main_mul86_float + (1)*main_mul86_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul86_fixbits + (-10000)*main_mul86_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*data_CAST_mul86_fixp + (-1)*data_CAST_mul86_0_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_mul86_float + (-1)*data_CAST_mul86_0_float==0)    #float equality
solver.Add( + (1)*data_CAST_mul86_double + (-1)*data_CAST_mul86_0_double==0)    #double equality
solver.Add( + (1)*data_CAST_mul86_fixp + (-1)*main_mul86_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_mul86_float + (-1)*main_mul86_float==0)    #float equality
solver.Add( + (1)*data_CAST_mul86_double + (-1)*main_mul86_double==0)    #double equality
mathCostObj +=  + (1.35882)*main_mul86_fixp
mathCostObj +=  + (1.82592)*main_mul86_float
mathCostObj +=  + (1.56282)*main_mul86_double
main_main_mul86_enob_1 = solver.IntVar(0, 1, 'main_main_mul86_enob_1')
main_main_mul86_enob_2 = solver.IntVar(0, 1, 'main_main_mul86_enob_2')
solver.Add( + (1)*main_main_mul86_enob_1 + (1)*main_main_mul86_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul86_enob + (-1)*data_enob_memphi_main_tmp6 + (-10000)*main_main_mul86_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul86_enob + (-1)*data_enob_memphi_main_tmp5 + (-10000)*main_main_mul86_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
cov_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'cov_enob_memphi_main_tmp7')
solver.Add( + (1)*cov_enob_memphi_main_tmp7 + (-1)*cov_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
solver.Add( + (1)*main_main_tmp7_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add91 = fadd double %tmp7, %mul86, !taffo.info !50, !taffo.initweight !34
cov_CAST_add91_fixbits = solver.IntVar(0, 9, 'cov_CAST_add91_fixbits')
cov_CAST_add91_fixp = solver.IntVar(0, 1, 'cov_CAST_add91_fixp')
cov_CAST_add91_float = solver.IntVar(0, 1, 'cov_CAST_add91_float')
cov_CAST_add91_double = solver.IntVar(0, 1, 'cov_CAST_add91_double')
solver.Add( + (1)*cov_CAST_add91_fixp + (1)*cov_CAST_add91_float + (1)*cov_CAST_add91_double==1)    #exactly 1 type
solver.Add( + (1)*cov_CAST_add91_fixbits + (-10000)*cov_CAST_add91_fixp<=0)    #If no fix, fix frac part = 0
C1_cov_CAST_add91 = solver.IntVar(0, 1, 'C1_cov_CAST_add91')
C2_cov_CAST_add91 = solver.IntVar(0, 1, 'C2_cov_CAST_add91')
solver.Add( + (1)*cov_fixbits + (-1)*cov_CAST_add91_fixbits + (-10000)*C1_cov_CAST_add91<=0)    #Shift cost 1
solver.Add( + (-1)*cov_fixbits + (1)*cov_CAST_add91_fixbits + (-10000)*C2_cov_CAST_add91<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_cov_CAST_add91
castCostObj +=  + (1)*C2_cov_CAST_add91
C3_cov_CAST_add91 = solver.IntVar(0, 1, 'C3_cov_CAST_add91')
C4_cov_CAST_add91 = solver.IntVar(0, 1, 'C4_cov_CAST_add91')
C5_cov_CAST_add91 = solver.IntVar(0, 1, 'C5_cov_CAST_add91')
C6_cov_CAST_add91 = solver.IntVar(0, 1, 'C6_cov_CAST_add91')
C7_cov_CAST_add91 = solver.IntVar(0, 1, 'C7_cov_CAST_add91')
C8_cov_CAST_add91 = solver.IntVar(0, 1, 'C8_cov_CAST_add91')
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_add91_float + (-1)*C3_cov_CAST_add91<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_cov_CAST_add91
solver.Add( + (1)*cov_float + (1)*cov_CAST_add91_fixp + (-1)*C4_cov_CAST_add91<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_cov_CAST_add91
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_add91_double + (-1)*C5_cov_CAST_add91<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_cov_CAST_add91
solver.Add( + (1)*cov_double + (1)*cov_CAST_add91_fixp + (-1)*C6_cov_CAST_add91<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_cov_CAST_add91
solver.Add( + (1)*cov_float + (1)*cov_CAST_add91_double + (-1)*C7_cov_CAST_add91<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_cov_CAST_add91
solver.Add( + (1)*cov_double + (1)*cov_CAST_add91_float + (-1)*C8_cov_CAST_add91<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_cov_CAST_add91



#Constraint for cast for   %add91 = fadd double %tmp7, %mul86, !taffo.info !50, !taffo.initweight !34
main_mul86_CAST_add91_fixbits = solver.IntVar(0, 20, 'main_mul86_CAST_add91_fixbits')
main_mul86_CAST_add91_fixp = solver.IntVar(0, 1, 'main_mul86_CAST_add91_fixp')
main_mul86_CAST_add91_float = solver.IntVar(0, 1, 'main_mul86_CAST_add91_float')
main_mul86_CAST_add91_double = solver.IntVar(0, 1, 'main_mul86_CAST_add91_double')
solver.Add( + (1)*main_mul86_CAST_add91_fixp + (1)*main_mul86_CAST_add91_float + (1)*main_mul86_CAST_add91_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul86_CAST_add91_fixbits + (-10000)*main_mul86_CAST_add91_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C1_main_mul86_CAST_add91')
C2_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C2_main_mul86_CAST_add91')
solver.Add( + (1)*main_mul86_fixbits + (-1)*main_mul86_CAST_add91_fixbits + (-10000)*C1_main_mul86_CAST_add91<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul86_fixbits + (1)*main_mul86_CAST_add91_fixbits + (-10000)*C2_main_mul86_CAST_add91<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul86_CAST_add91
castCostObj +=  + (1)*C2_main_mul86_CAST_add91
C3_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C3_main_mul86_CAST_add91')
C4_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C4_main_mul86_CAST_add91')
C5_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C5_main_mul86_CAST_add91')
C6_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C6_main_mul86_CAST_add91')
C7_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C7_main_mul86_CAST_add91')
C8_main_mul86_CAST_add91 = solver.IntVar(0, 1, 'C8_main_mul86_CAST_add91')
solver.Add( + (1)*main_mul86_fixp + (1)*main_mul86_CAST_add91_float + (-1)*C3_main_mul86_CAST_add91<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_main_mul86_CAST_add91
solver.Add( + (1)*main_mul86_float + (1)*main_mul86_CAST_add91_fixp + (-1)*C4_main_mul86_CAST_add91<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_mul86_CAST_add91
solver.Add( + (1)*main_mul86_fixp + (1)*main_mul86_CAST_add91_double + (-1)*C5_main_mul86_CAST_add91<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_mul86_CAST_add91
solver.Add( + (1)*main_mul86_double + (1)*main_mul86_CAST_add91_fixp + (-1)*C6_main_mul86_CAST_add91<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_mul86_CAST_add91
solver.Add( + (1)*main_mul86_float + (1)*main_mul86_CAST_add91_double + (-1)*C7_main_mul86_CAST_add91<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_mul86_CAST_add91
solver.Add( + (1)*main_mul86_double + (1)*main_mul86_CAST_add91_float + (-1)*C8_main_mul86_CAST_add91<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_mul86_CAST_add91



#Stuff for   %add91 = fadd double %tmp7, %mul86, !taffo.info !50, !taffo.initweight !34
main_add91_fixbits = solver.IntVar(0, 20, 'main_add91_fixbits')
main_add91_fixp = solver.IntVar(0, 1, 'main_add91_fixp')
main_add91_float = solver.IntVar(0, 1, 'main_add91_float')
main_add91_double = solver.IntVar(0, 1, 'main_add91_double')
main_add91_enob = solver.IntVar(-10000, 10000, 'main_add91_enob')
solver.Add( + (1)*main_add91_enob + (-1)*main_add91_fixbits + (10000)*main_add91_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add91_enob + (10000)*main_add91_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add91_enob + (10000)*main_add91_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add91_fixbits + (-10000)*main_add91_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_add91_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add91_enob
solver.Add( + (1)*main_add91_fixp + (1)*main_add91_float + (1)*main_add91_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add91_fixbits + (-10000)*main_add91_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*cov_CAST_add91_fixp + (-1)*main_mul86_CAST_add91_fixp==0)    #fix equality
solver.Add( + (1)*cov_CAST_add91_float + (-1)*main_mul86_CAST_add91_float==0)    #float equality
solver.Add( + (1)*cov_CAST_add91_double + (-1)*main_mul86_CAST_add91_double==0)    #double equality
solver.Add( + (1)*cov_CAST_add91_fixbits + (-1)*main_mul86_CAST_add91_fixbits==0)    #same fractional bit
solver.Add( + (1)*cov_CAST_add91_fixp + (-1)*main_add91_fixp==0)    #fix equality
solver.Add( + (1)*cov_CAST_add91_float + (-1)*main_add91_float==0)    #float equality
solver.Add( + (1)*cov_CAST_add91_double + (-1)*main_add91_double==0)    #double equality
solver.Add( + (1)*cov_CAST_add91_fixbits + (-1)*main_add91_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.0518)*main_add91_fixp
mathCostObj +=  + (1.02933)*main_add91_float
mathCostObj +=  + (1.39384)*main_add91_double
solver.Add( + (1)*main_add91_enob + (-1)*cov_enob_memphi_main_tmp7<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add91_enob + (-1)*main_mul86_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add91, double* %arrayidx90, align 8, !taffo.info !8, !taffo.initweight !28
main_add91_CAST_store_fixbits = solver.IntVar(0, 20, 'main_add91_CAST_store_fixbits')
main_add91_CAST_store_fixp = solver.IntVar(0, 1, 'main_add91_CAST_store_fixp')
main_add91_CAST_store_float = solver.IntVar(0, 1, 'main_add91_CAST_store_float')
main_add91_CAST_store_double = solver.IntVar(0, 1, 'main_add91_CAST_store_double')
solver.Add( + (1)*main_add91_CAST_store_fixp + (1)*main_add91_CAST_store_float + (1)*main_add91_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add91_CAST_store_fixbits + (-10000)*main_add91_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add91_CAST_store = solver.IntVar(0, 1, 'C1_main_add91_CAST_store')
C2_main_add91_CAST_store = solver.IntVar(0, 1, 'C2_main_add91_CAST_store')
solver.Add( + (1)*main_add91_fixbits + (-1)*main_add91_CAST_store_fixbits + (-10000)*C1_main_add91_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add91_fixbits + (1)*main_add91_CAST_store_fixbits + (-10000)*C2_main_add91_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add91_CAST_store
castCostObj +=  + (1)*C2_main_add91_CAST_store
C3_main_add91_CAST_store = solver.IntVar(0, 1, 'C3_main_add91_CAST_store')
C4_main_add91_CAST_store = solver.IntVar(0, 1, 'C4_main_add91_CAST_store')
C5_main_add91_CAST_store = solver.IntVar(0, 1, 'C5_main_add91_CAST_store')
C6_main_add91_CAST_store = solver.IntVar(0, 1, 'C6_main_add91_CAST_store')
C7_main_add91_CAST_store = solver.IntVar(0, 1, 'C7_main_add91_CAST_store')
C8_main_add91_CAST_store = solver.IntVar(0, 1, 'C8_main_add91_CAST_store')
solver.Add( + (1)*main_add91_fixp + (1)*main_add91_CAST_store_float + (-1)*C3_main_add91_CAST_store<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_main_add91_CAST_store
solver.Add( + (1)*main_add91_float + (1)*main_add91_CAST_store_fixp + (-1)*C4_main_add91_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_add91_CAST_store
solver.Add( + (1)*main_add91_fixp + (1)*main_add91_CAST_store_double + (-1)*C5_main_add91_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_add91_CAST_store
solver.Add( + (1)*main_add91_double + (1)*main_add91_CAST_store_fixp + (-1)*C6_main_add91_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_add91_CAST_store
solver.Add( + (1)*main_add91_float + (1)*main_add91_CAST_store_double + (-1)*C7_main_add91_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_add91_CAST_store
solver.Add( + (1)*main_add91_double + (1)*main_add91_CAST_store_float + (-1)*C8_main_add91_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_add91_CAST_store
solver.Add( + (1)*cov_fixp + (-1)*main_add91_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*cov_float + (-1)*main_add91_CAST_store_float==0)    #float equality
solver.Add( + (1)*cov_double + (-1)*main_add91_CAST_store_double==0)    #double equality
solver.Add( + (1)*cov_fixbits + (-1)*main_add91_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
cov_enob_storeENOB = solver.IntVar(-10000, 10000, 'cov_enob_storeENOB')
solver.Add( + (1)*cov_enob_storeENOB + (-1)*cov_fixbits + (10000)*cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*cov_enob_storeENOB + (10000)*cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*cov_enob_storeENOB + (10000)*cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*cov_enob_storeENOB + (-1)*main_add91_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*cov_enob_memphi_main_tmp7 + (-1)*cov_enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
cov_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'cov_enob_memphi_main_tmp8')
solver.Add( + (1)*cov_enob_memphi_main_tmp8 + (-1)*cov_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
solver.Add( + (1)*main_main_tmp8_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*cov_enob_memphi_main_tmp8 + (-1)*cov_enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.590000e+02
ConstantValue__6_fixbits = solver.IntVar(0, 23, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10015)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10044)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.590000e+02
ConstantValue__7_fixbits = solver.IntVar(0, 23, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10015)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10044)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div99 = fdiv double %tmp8, 2.590000e+02, !taffo.info !52, !taffo.initweight !34, !taffo.constinfo !54
cov_CAST_div99_fixbits = solver.IntVar(0, 9, 'cov_CAST_div99_fixbits')
cov_CAST_div99_fixp = solver.IntVar(0, 1, 'cov_CAST_div99_fixp')
cov_CAST_div99_float = solver.IntVar(0, 1, 'cov_CAST_div99_float')
cov_CAST_div99_double = solver.IntVar(0, 1, 'cov_CAST_div99_double')
solver.Add( + (1)*cov_CAST_div99_fixp + (1)*cov_CAST_div99_float + (1)*cov_CAST_div99_double==1)    #exactly 1 type
solver.Add( + (1)*cov_CAST_div99_fixbits + (-10000)*cov_CAST_div99_fixp<=0)    #If no fix, fix frac part = 0
C1_cov_CAST_div99 = solver.IntVar(0, 1, 'C1_cov_CAST_div99')
C2_cov_CAST_div99 = solver.IntVar(0, 1, 'C2_cov_CAST_div99')
solver.Add( + (1)*cov_fixbits + (-1)*cov_CAST_div99_fixbits + (-10000)*C1_cov_CAST_div99<=0)    #Shift cost 1
solver.Add( + (-1)*cov_fixbits + (1)*cov_CAST_div99_fixbits + (-10000)*C2_cov_CAST_div99<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_cov_CAST_div99
castCostObj +=  + (1)*C2_cov_CAST_div99
C3_cov_CAST_div99 = solver.IntVar(0, 1, 'C3_cov_CAST_div99')
C4_cov_CAST_div99 = solver.IntVar(0, 1, 'C4_cov_CAST_div99')
C5_cov_CAST_div99 = solver.IntVar(0, 1, 'C5_cov_CAST_div99')
C6_cov_CAST_div99 = solver.IntVar(0, 1, 'C6_cov_CAST_div99')
C7_cov_CAST_div99 = solver.IntVar(0, 1, 'C7_cov_CAST_div99')
C8_cov_CAST_div99 = solver.IntVar(0, 1, 'C8_cov_CAST_div99')
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_div99_float + (-1)*C3_cov_CAST_div99<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_cov_CAST_div99
solver.Add( + (1)*cov_float + (1)*cov_CAST_div99_fixp + (-1)*C4_cov_CAST_div99<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_cov_CAST_div99
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_div99_double + (-1)*C5_cov_CAST_div99<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_cov_CAST_div99
solver.Add( + (1)*cov_double + (1)*cov_CAST_div99_fixp + (-1)*C6_cov_CAST_div99<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_cov_CAST_div99
solver.Add( + (1)*cov_float + (1)*cov_CAST_div99_double + (-1)*C7_cov_CAST_div99<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_cov_CAST_div99
solver.Add( + (1)*cov_double + (1)*cov_CAST_div99_float + (-1)*C8_cov_CAST_div99<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_cov_CAST_div99



#Stuff for double 2.590000e+02
ConstantValue__8_fixbits = solver.IntVar(0, 23, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10015)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=10044)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div99 = fdiv double %tmp8, 2.590000e+02, !taffo.info !52, !taffo.initweight !34, !taffo.constinfo !54
ConstantValue__8_CAST_div99_fixbits = solver.IntVar(0, 23, 'ConstantValue__8_CAST_div99_fixbits')
ConstantValue__8_CAST_div99_fixp = solver.IntVar(0, 1, 'ConstantValue__8_CAST_div99_fixp')
ConstantValue__8_CAST_div99_float = solver.IntVar(0, 1, 'ConstantValue__8_CAST_div99_float')
ConstantValue__8_CAST_div99_double = solver.IntVar(0, 1, 'ConstantValue__8_CAST_div99_double')
solver.Add( + (1)*ConstantValue__8_CAST_div99_fixp + (1)*ConstantValue__8_CAST_div99_float + (1)*ConstantValue__8_CAST_div99_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__8_CAST_div99_fixbits + (-10000)*ConstantValue__8_CAST_div99_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C1_ConstantValue__8_CAST_div99')
C2_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C2_ConstantValue__8_CAST_div99')
solver.Add( + (1)*ConstantValue__8_fixbits + (-1)*ConstantValue__8_CAST_div99_fixbits + (-10000)*C1_ConstantValue__8_CAST_div99<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__8_fixbits + (1)*ConstantValue__8_CAST_div99_fixbits + (-10000)*C2_ConstantValue__8_CAST_div99<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__8_CAST_div99
castCostObj +=  + (1)*C2_ConstantValue__8_CAST_div99
C3_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C3_ConstantValue__8_CAST_div99')
C4_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C4_ConstantValue__8_CAST_div99')
C5_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C5_ConstantValue__8_CAST_div99')
C6_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C6_ConstantValue__8_CAST_div99')
C7_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C7_ConstantValue__8_CAST_div99')
C8_ConstantValue__8_CAST_div99 = solver.IntVar(0, 1, 'C8_ConstantValue__8_CAST_div99')
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_div99_float + (-1)*C3_ConstantValue__8_CAST_div99<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_ConstantValue__8_CAST_div99
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_div99_fixp + (-1)*C4_ConstantValue__8_CAST_div99<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_ConstantValue__8_CAST_div99
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_div99_double + (-1)*C5_ConstantValue__8_CAST_div99<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_ConstantValue__8_CAST_div99
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_div99_fixp + (-1)*C6_ConstantValue__8_CAST_div99<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_ConstantValue__8_CAST_div99
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_div99_double + (-1)*C7_ConstantValue__8_CAST_div99<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_ConstantValue__8_CAST_div99
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_div99_float + (-1)*C8_ConstantValue__8_CAST_div99<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_ConstantValue__8_CAST_div99



#Stuff for   %div99 = fdiv double %tmp8, 2.590000e+02, !taffo.info !52, !taffo.initweight !34, !taffo.constinfo !54
main_div99_fixbits = solver.IntVar(0, 18, 'main_div99_fixbits')
main_div99_fixp = solver.IntVar(0, 1, 'main_div99_fixp')
main_div99_float = solver.IntVar(0, 1, 'main_div99_float')
main_div99_double = solver.IntVar(0, 1, 'main_div99_double')
main_div99_enob = solver.IntVar(-10000, 10000, 'main_div99_enob')
solver.Add( + (1)*main_div99_enob + (-1)*main_div99_fixbits + (10000)*main_div99_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div99_enob + (10000)*main_div99_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div99_enob + (10000)*main_div99_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div99_fixbits + (-10000)*main_div99_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_div99_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_div99_enob
solver.Add( + (1)*main_div99_fixp + (1)*main_div99_float + (1)*main_div99_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div99_fixbits + (-10000)*main_div99_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*cov_CAST_div99_fixp + (-1)*ConstantValue__8_CAST_div99_fixp==0)    #fix equality
solver.Add( + (1)*cov_CAST_div99_float + (-1)*ConstantValue__8_CAST_div99_float==0)    #float equality
solver.Add( + (1)*cov_CAST_div99_double + (-1)*ConstantValue__8_CAST_div99_double==0)    #double equality
solver.Add( + (1)*cov_CAST_div99_fixp + (-1)*main_div99_fixp==0)    #fix equality
solver.Add( + (1)*cov_CAST_div99_float + (-1)*main_div99_float==0)    #float equality
solver.Add( + (1)*cov_CAST_div99_double + (-1)*main_div99_double==0)    #double equality
mathCostObj +=  + (3.97899)*main_div99_fixp
mathCostObj +=  + (2.0321)*main_div99_float
mathCostObj +=  + (2.21275)*main_div99_double
main_main_div99_enob_1 = solver.IntVar(0, 1, 'main_main_div99_enob_1')
main_main_div99_enob_2 = solver.IntVar(0, 1, 'main_main_div99_enob_2')
solver.Add( + (1)*main_main_div99_enob_1 + (1)*main_main_div99_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div99_enob + (-1)*ConstantValue__6_enob + (-10000)*main_main_div99_enob_1<=1040)    #Enob: propagation in division 1
solver.Add( + (1)*main_div99_enob + (-1)*cov_enob_memphi_main_tmp8 + (-10000)*main_main_div99_enob_2<=8)    #Enob: propagation in division 2



#Constraint for cast for   store double %div99, double* %arrayidx98, align 8, !taffo.info !8, !taffo.initweight !28
main_div99_CAST_store_fixbits = solver.IntVar(0, 18, 'main_div99_CAST_store_fixbits')
main_div99_CAST_store_fixp = solver.IntVar(0, 1, 'main_div99_CAST_store_fixp')
main_div99_CAST_store_float = solver.IntVar(0, 1, 'main_div99_CAST_store_float')
main_div99_CAST_store_double = solver.IntVar(0, 1, 'main_div99_CAST_store_double')
solver.Add( + (1)*main_div99_CAST_store_fixp + (1)*main_div99_CAST_store_float + (1)*main_div99_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div99_CAST_store_fixbits + (-10000)*main_div99_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div99_CAST_store = solver.IntVar(0, 1, 'C1_main_div99_CAST_store')
C2_main_div99_CAST_store = solver.IntVar(0, 1, 'C2_main_div99_CAST_store')
solver.Add( + (1)*main_div99_fixbits + (-1)*main_div99_CAST_store_fixbits + (-10000)*C1_main_div99_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div99_fixbits + (1)*main_div99_CAST_store_fixbits + (-10000)*C2_main_div99_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div99_CAST_store
castCostObj +=  + (1)*C2_main_div99_CAST_store
C3_main_div99_CAST_store = solver.IntVar(0, 1, 'C3_main_div99_CAST_store')
C4_main_div99_CAST_store = solver.IntVar(0, 1, 'C4_main_div99_CAST_store')
C5_main_div99_CAST_store = solver.IntVar(0, 1, 'C5_main_div99_CAST_store')
C6_main_div99_CAST_store = solver.IntVar(0, 1, 'C6_main_div99_CAST_store')
C7_main_div99_CAST_store = solver.IntVar(0, 1, 'C7_main_div99_CAST_store')
C8_main_div99_CAST_store = solver.IntVar(0, 1, 'C8_main_div99_CAST_store')
solver.Add( + (1)*main_div99_fixp + (1)*main_div99_CAST_store_float + (-1)*C3_main_div99_CAST_store<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_main_div99_CAST_store
solver.Add( + (1)*main_div99_float + (1)*main_div99_CAST_store_fixp + (-1)*C4_main_div99_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_main_div99_CAST_store
solver.Add( + (1)*main_div99_fixp + (1)*main_div99_CAST_store_double + (-1)*C5_main_div99_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_main_div99_CAST_store
solver.Add( + (1)*main_div99_double + (1)*main_div99_CAST_store_fixp + (-1)*C6_main_div99_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_main_div99_CAST_store
solver.Add( + (1)*main_div99_float + (1)*main_div99_CAST_store_double + (-1)*C7_main_div99_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_main_div99_CAST_store
solver.Add( + (1)*main_div99_double + (1)*main_div99_CAST_store_float + (-1)*C8_main_div99_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_main_div99_CAST_store
solver.Add( + (1)*cov_fixp + (-1)*main_div99_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*cov_float + (-1)*main_div99_CAST_store_float==0)    #float equality
solver.Add( + (1)*cov_double + (-1)*main_div99_CAST_store_double==0)    #double equality
solver.Add( + (1)*cov_fixbits + (-1)*main_div99_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
cov_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'cov_enob_storeENOB_storeENOB')
solver.Add( + (1)*cov_enob_storeENOB_storeENOB + (-1)*cov_fixbits + (10000)*cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*cov_enob_storeENOB_storeENOB + (10000)*cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*cov_enob_storeENOB_storeENOB + (10000)*cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*cov_enob_storeENOB_storeENOB + (-1)*main_div99_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
cov_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'cov_enob_memphi_main_tmp9')
solver.Add( + (1)*cov_enob_memphi_main_tmp9 + (-1)*cov_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
solver.Add( + (1)*main_main_tmp9_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*cov_enob_memphi_main_tmp9 + (-1)*cov_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp9, double* %arrayidx107, align 8, !taffo.info !8, !taffo.initweight !28
cov_CAST_store_fixbits = solver.IntVar(0, 9, 'cov_CAST_store_fixbits')
cov_CAST_store_fixp = solver.IntVar(0, 1, 'cov_CAST_store_fixp')
cov_CAST_store_float = solver.IntVar(0, 1, 'cov_CAST_store_float')
cov_CAST_store_double = solver.IntVar(0, 1, 'cov_CAST_store_double')
solver.Add( + (1)*cov_CAST_store_fixp + (1)*cov_CAST_store_float + (1)*cov_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*cov_CAST_store_fixbits + (-10000)*cov_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_cov_CAST_store = solver.IntVar(0, 1, 'C1_cov_CAST_store')
C2_cov_CAST_store = solver.IntVar(0, 1, 'C2_cov_CAST_store')
solver.Add( + (1)*cov_fixbits + (-1)*cov_CAST_store_fixbits + (-10000)*C1_cov_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*cov_fixbits + (1)*cov_CAST_store_fixbits + (-10000)*C2_cov_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_cov_CAST_store
castCostObj +=  + (1)*C2_cov_CAST_store
C3_cov_CAST_store = solver.IntVar(0, 1, 'C3_cov_CAST_store')
C4_cov_CAST_store = solver.IntVar(0, 1, 'C4_cov_CAST_store')
C5_cov_CAST_store = solver.IntVar(0, 1, 'C5_cov_CAST_store')
C6_cov_CAST_store = solver.IntVar(0, 1, 'C6_cov_CAST_store')
C7_cov_CAST_store = solver.IntVar(0, 1, 'C7_cov_CAST_store')
C8_cov_CAST_store = solver.IntVar(0, 1, 'C8_cov_CAST_store')
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_store_float + (-1)*C3_cov_CAST_store<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_cov_CAST_store
solver.Add( + (1)*cov_float + (1)*cov_CAST_store_fixp + (-1)*C4_cov_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_cov_CAST_store
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_store_double + (-1)*C5_cov_CAST_store<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_cov_CAST_store
solver.Add( + (1)*cov_double + (1)*cov_CAST_store_fixp + (-1)*C6_cov_CAST_store<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_cov_CAST_store
solver.Add( + (1)*cov_float + (1)*cov_CAST_store_double + (-1)*C7_cov_CAST_store<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_cov_CAST_store
solver.Add( + (1)*cov_double + (1)*cov_CAST_store_float + (-1)*C8_cov_CAST_store<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_cov_CAST_store
solver.Add( + (1)*cov_fixp + (-1)*cov_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*cov_float + (-1)*cov_CAST_store_float==0)    #float equality
solver.Add( + (1)*cov_double + (-1)*cov_CAST_store_double==0)    #double equality
solver.Add( + (1)*cov_fixbits + (-1)*cov_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
cov_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'cov_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*cov_enob_storeENOB_storeENOB_storeENOB + (-1)*cov_fixbits + (10000)*cov_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*cov_enob_storeENOB_storeENOB_storeENOB + (10000)*cov_float<=10149)    #Enob constraint for float
solver.Add( + (1)*cov_enob_storeENOB_storeENOB_storeENOB + (10000)*cov_double<=11074)    #Enob constraint for double
solver.Add( + (1)*cov_enob_storeENOB_storeENOB_storeENOB + (-1)*cov_enob_memphi_main_tmp9<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
cov_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'cov_enob_memphi_main_tmp12')
solver.Add( + (1)*cov_enob_memphi_main_tmp12 + (-1)*cov_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call130 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp11, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.5, i32 0, i32 0), double %tmp12), !taffo.info !8, !taffo.initweight !34, !taffo.constinfo !63
cov_CAST_call130_fixbits = solver.IntVar(0, 9, 'cov_CAST_call130_fixbits')
cov_CAST_call130_fixp = solver.IntVar(0, 1, 'cov_CAST_call130_fixp')
cov_CAST_call130_float = solver.IntVar(0, 1, 'cov_CAST_call130_float')
cov_CAST_call130_double = solver.IntVar(0, 1, 'cov_CAST_call130_double')
solver.Add( + (1)*cov_CAST_call130_fixp + (1)*cov_CAST_call130_float + (1)*cov_CAST_call130_double==1)    #exactly 1 type
solver.Add( + (1)*cov_CAST_call130_fixbits + (-10000)*cov_CAST_call130_fixp<=0)    #If no fix, fix frac part = 0
C1_cov_CAST_call130 = solver.IntVar(0, 1, 'C1_cov_CAST_call130')
C2_cov_CAST_call130 = solver.IntVar(0, 1, 'C2_cov_CAST_call130')
solver.Add( + (1)*cov_fixbits + (-1)*cov_CAST_call130_fixbits + (-10000)*C1_cov_CAST_call130<=0)    #Shift cost 1
solver.Add( + (-1)*cov_fixbits + (1)*cov_CAST_call130_fixbits + (-10000)*C2_cov_CAST_call130<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_cov_CAST_call130
castCostObj +=  + (1)*C2_cov_CAST_call130
C3_cov_CAST_call130 = solver.IntVar(0, 1, 'C3_cov_CAST_call130')
C4_cov_CAST_call130 = solver.IntVar(0, 1, 'C4_cov_CAST_call130')
C5_cov_CAST_call130 = solver.IntVar(0, 1, 'C5_cov_CAST_call130')
C6_cov_CAST_call130 = solver.IntVar(0, 1, 'C6_cov_CAST_call130')
C7_cov_CAST_call130 = solver.IntVar(0, 1, 'C7_cov_CAST_call130')
C8_cov_CAST_call130 = solver.IntVar(0, 1, 'C8_cov_CAST_call130')
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_call130_float + (-1)*C3_cov_CAST_call130<=1)    #Fix to float
castCostObj +=  + (2.0753)*C3_cov_CAST_call130
solver.Add( + (1)*cov_float + (1)*cov_CAST_call130_fixp + (-1)*C4_cov_CAST_call130<=1)    #Float to fix
castCostObj +=  + (1.87174)*C4_cov_CAST_call130
solver.Add( + (1)*cov_fixp + (1)*cov_CAST_call130_double + (-1)*C5_cov_CAST_call130<=1)    #Fix to double
castCostObj +=  + (2.36291)*C5_cov_CAST_call130
solver.Add( + (1)*cov_double + (1)*cov_CAST_call130_fixp + (-1)*C6_cov_CAST_call130<=1)    #Double to fix
castCostObj +=  + (1.72231)*C6_cov_CAST_call130
solver.Add( + (1)*cov_float + (1)*cov_CAST_call130_double + (-1)*C7_cov_CAST_call130<=1)    #Float to double
castCostObj +=  + (1.18372)*C7_cov_CAST_call130
solver.Add( + (1)*cov_double + (1)*cov_CAST_call130_float + (-1)*C8_cov_CAST_call130<=1)    #Double to float
castCostObj +=  + (1.17146)*C8_cov_CAST_call130
solver.Add( + (1)*cov_CAST_call130_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 61.4356+ 1 * enobCostObj / 5301+ 1000 * mathCostObj / 19.7703)

# Model declaration end.