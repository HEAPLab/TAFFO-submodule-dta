


#Stuff for @A = common dso_local global [20 x [20 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
A_fixbits = solver.IntVar(0, 31, 'A_fixbits')
A_fixp = solver.IntVar(0, 1, 'A_fixp')
A_float = solver.IntVar(0, 1, 'A_float')
A_double = solver.IntVar(0, 1, 'A_double')
A_enob = solver.IntVar(-10000, 10000, 'A_enob')
solver.Add( + (1)*A_enob + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_fixbits + (-10000)*A_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*A_enob<=333)    #Enob constraint for error maximal
enobCostObj =  + (-1)*A_enob
solver.Add( + (1)*A_fixp + (1)*A_float + (1)*A_double==1)    #Exactly one selected type
solver.Add( + (1)*A_fixbits + (-10000)*A_fixp<=0)    #If not fix, frac part to zero



#Stuff for @B = common dso_local global [20 x [30 x double]] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
B_fixbits = solver.IntVar(0, 22, 'B_fixbits')
B_fixp = solver.IntVar(0, 1, 'B_fixp')
B_float = solver.IntVar(0, 1, 'B_float')
B_double = solver.IntVar(0, 1, 'B_double')
B_enob = solver.IntVar(-10000, 10000, 'B_enob')
solver.Add( + (1)*B_enob + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_fixbits + (-10000)*B_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*B_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*B_enob
solver.Add( + (1)*B_fixp + (1)*B_float + (1)*B_double==1)    #Exactly one selected type
solver.Add( + (1)*B_fixbits + (-10000)*B_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %rem to double, !taffo.info !27, !taffo.initweight !30
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



#Stuff for   %conv7 = sitofp i32 20 to double, !taffo.info !31
main_conv7_fixbits = solver.IntVar(0, 27, 'main_conv7_fixbits')
main_conv7_fixp = solver.IntVar(0, 1, 'main_conv7_fixp')
main_conv7_float = solver.IntVar(0, 1, 'main_conv7_float')
main_conv7_double = solver.IntVar(0, 1, 'main_conv7_double')
main_conv7_enob = solver.IntVar(-10000, 10000, 'main_conv7_enob')
solver.Add( + (1)*main_conv7_enob + (-1)*main_conv7_fixbits + (10000)*main_conv7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv7_enob + (10000)*main_conv7_float<=10019)    #Enob constraint for float
solver.Add( + (1)*main_conv7_enob + (10000)*main_conv7_double<=10048)    #Enob constraint for double
solver.Add( + (1)*main_conv7_fixbits + (-10000)*main_conv7_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv7_enob
solver.Add( + (1)*main_conv7_fixp + (1)*main_conv7_float + (1)*main_conv7_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv7_fixbits + (-10000)*main_conv7_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv7_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div = fdiv double %conv, %conv7, !taffo.info !33, !taffo.initweight !34
main_conv_CAST_div_fixbits = solver.IntVar(0, 27, 'main_conv_CAST_div_fixbits')
main_conv_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv_CAST_div_fixp')
main_conv_CAST_div_float = solver.IntVar(0, 1, 'main_conv_CAST_div_float')
main_conv_CAST_div_double = solver.IntVar(0, 1, 'main_conv_CAST_div_double')
solver.Add( + (1)*main_conv_CAST_div_fixp + (1)*main_conv_CAST_div_float + (1)*main_conv_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv_CAST_div_fixbits + (-10000)*main_conv_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv_CAST_div = solver.IntVar(0, 1, 'C1_main_conv_CAST_div')
C2_main_conv_CAST_div = solver.IntVar(0, 1, 'C2_main_conv_CAST_div')
solver.Add( + (1)*main_conv_fixbits + (-1)*main_conv_CAST_div_fixbits + (-10000)*C1_main_conv_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv_fixbits + (1)*main_conv_CAST_div_fixbits + (-10000)*C2_main_conv_CAST_div<=0)    #Shift cost 2
castCostObj =  + (1)*C1_main_conv_CAST_div
castCostObj +=  + (1)*C2_main_conv_CAST_div
C3_main_conv_CAST_div = solver.IntVar(0, 1, 'C3_main_conv_CAST_div')
C4_main_conv_CAST_div = solver.IntVar(0, 1, 'C4_main_conv_CAST_div')
C5_main_conv_CAST_div = solver.IntVar(0, 1, 'C5_main_conv_CAST_div')
C6_main_conv_CAST_div = solver.IntVar(0, 1, 'C6_main_conv_CAST_div')
C7_main_conv_CAST_div = solver.IntVar(0, 1, 'C7_main_conv_CAST_div')
C8_main_conv_CAST_div = solver.IntVar(0, 1, 'C8_main_conv_CAST_div')
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_div_float + (-1)*C3_main_conv_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_conv_CAST_div
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div_fixp + (-1)*C4_main_conv_CAST_div<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_conv_CAST_div
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_div_double + (-1)*C5_main_conv_CAST_div<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_conv_CAST_div
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div_fixp + (-1)*C6_main_conv_CAST_div<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_conv_CAST_div
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div_double + (-1)*C7_main_conv_CAST_div<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_conv_CAST_div
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div_float + (-1)*C8_main_conv_CAST_div<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_conv_CAST_div



#Constraint for cast for   %div = fdiv double %conv, %conv7, !taffo.info !33, !taffo.initweight !34
main_conv7_CAST_div_fixbits = solver.IntVar(0, 27, 'main_conv7_CAST_div_fixbits')
main_conv7_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv7_CAST_div_fixp')
main_conv7_CAST_div_float = solver.IntVar(0, 1, 'main_conv7_CAST_div_float')
main_conv7_CAST_div_double = solver.IntVar(0, 1, 'main_conv7_CAST_div_double')
solver.Add( + (1)*main_conv7_CAST_div_fixp + (1)*main_conv7_CAST_div_float + (1)*main_conv7_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv7_CAST_div_fixbits + (-10000)*main_conv7_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv7_CAST_div = solver.IntVar(0, 1, 'C1_main_conv7_CAST_div')
C2_main_conv7_CAST_div = solver.IntVar(0, 1, 'C2_main_conv7_CAST_div')
solver.Add( + (1)*main_conv7_fixbits + (-1)*main_conv7_CAST_div_fixbits + (-10000)*C1_main_conv7_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv7_fixbits + (1)*main_conv7_CAST_div_fixbits + (-10000)*C2_main_conv7_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv7_CAST_div
castCostObj +=  + (1)*C2_main_conv7_CAST_div
C3_main_conv7_CAST_div = solver.IntVar(0, 1, 'C3_main_conv7_CAST_div')
C4_main_conv7_CAST_div = solver.IntVar(0, 1, 'C4_main_conv7_CAST_div')
C5_main_conv7_CAST_div = solver.IntVar(0, 1, 'C5_main_conv7_CAST_div')
C6_main_conv7_CAST_div = solver.IntVar(0, 1, 'C6_main_conv7_CAST_div')
C7_main_conv7_CAST_div = solver.IntVar(0, 1, 'C7_main_conv7_CAST_div')
C8_main_conv7_CAST_div = solver.IntVar(0, 1, 'C8_main_conv7_CAST_div')
solver.Add( + (1)*main_conv7_fixp + (1)*main_conv7_CAST_div_float + (-1)*C3_main_conv7_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_conv7_CAST_div
solver.Add( + (1)*main_conv7_float + (1)*main_conv7_CAST_div_fixp + (-1)*C4_main_conv7_CAST_div<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_conv7_CAST_div
solver.Add( + (1)*main_conv7_fixp + (1)*main_conv7_CAST_div_double + (-1)*C5_main_conv7_CAST_div<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_conv7_CAST_div
solver.Add( + (1)*main_conv7_double + (1)*main_conv7_CAST_div_fixp + (-1)*C6_main_conv7_CAST_div<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_conv7_CAST_div
solver.Add( + (1)*main_conv7_float + (1)*main_conv7_CAST_div_double + (-1)*C7_main_conv7_CAST_div<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_conv7_CAST_div
solver.Add( + (1)*main_conv7_double + (1)*main_conv7_CAST_div_float + (-1)*C8_main_conv7_CAST_div<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_conv7_CAST_div



#Stuff for   %div = fdiv double %conv, %conv7, !taffo.info !33, !taffo.initweight !34
main_div_fixbits = solver.IntVar(0, 31, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_conv7_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_conv7_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_conv7_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj =  + (13.2477)*main_div_fixp
mathCostObj +=  + (6.64202)*main_div_float
mathCostObj +=  + (7.0892)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*main_conv7_enob + (-10000)*main_main_div_enob_1<=1032)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_conv_enob + (-10000)*main_main_div_enob_2<=4)    #Enob: propagation in division 2



#Constraint for cast for   store double %div, double* %arrayidx9, align 8, !taffo.info !37, !taffo.initweight !24
main_div_CAST_store_fixbits = solver.IntVar(0, 31, 'main_div_CAST_store_fixbits')
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
castCostObj +=  + (6.64554)*C3_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_fixp + (-1)*C4_main_div_CAST_store<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_div_CAST_store
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_double + (-1)*C5_main_div_CAST_store<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_fixp + (-1)*C6_main_div_CAST_store<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_double + (-1)*C7_main_div_CAST_store<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_float + (-1)*C8_main_div_CAST_store<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_div_CAST_store
solver.Add( + (1)*A_fixp + (-1)*main_div_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*A_float + (-1)*main_div_CAST_store_float==0)    #float equality
solver.Add( + (1)*A_double + (-1)*main_div_CAST_store_double==0)    #double equality
solver.Add( + (1)*A_fixbits + (-1)*main_div_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
A_enob_storeENOB = solver.IntVar(-10000, 10000, 'A_enob_storeENOB')
solver.Add( + (1)*A_enob_storeENOB + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob_storeENOB + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob_storeENOB + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_enob_storeENOB + (-1)*main_div_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for double 1.000000e+00
ConstantValue__fixbits = solver.IntVar(0, 31, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__0_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx13, align 8, !taffo.info !37, !taffo.initweight !24, !taffo.constinfo !38
ConstantValue__0_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_CAST_store_fixbits')
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
castCostObj +=  + (6.64554)*C3_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C4_ConstantValue__0_CAST_store<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_CAST_store_double + (-1)*C5_ConstantValue__0_CAST_store<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C6_ConstantValue__0_CAST_store<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_double + (-1)*C7_ConstantValue__0_CAST_store<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_float + (-1)*C8_ConstantValue__0_CAST_store<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_ConstantValue__0_CAST_store
solver.Add( + (1)*A_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*A_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*A_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*A_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for   %conv20 = sitofp i32 %rem19 to double, !taffo.info !43, !taffo.initweight !34
main_conv20_fixbits = solver.IntVar(0, 27, 'main_conv20_fixbits')
main_conv20_fixp = solver.IntVar(0, 1, 'main_conv20_fixp')
main_conv20_float = solver.IntVar(0, 1, 'main_conv20_float')
main_conv20_double = solver.IntVar(0, 1, 'main_conv20_double')
main_conv20_enob = solver.IntVar(-10000, 10000, 'main_conv20_enob')
solver.Add( + (1)*main_conv20_enob + (-1)*main_conv20_fixbits + (10000)*main_conv20_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv20_enob + (10000)*main_conv20_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv20_enob + (10000)*main_conv20_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv20_fixbits + (-10000)*main_conv20_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv20_enob
solver.Add( + (1)*main_conv20_fixp + (1)*main_conv20_float + (1)*main_conv20_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv20_fixbits + (-10000)*main_conv20_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv20_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv21 = sitofp i32 30 to double, !taffo.info !45
main_conv21_fixbits = solver.IntVar(0, 27, 'main_conv21_fixbits')
main_conv21_fixp = solver.IntVar(0, 1, 'main_conv21_fixp')
main_conv21_float = solver.IntVar(0, 1, 'main_conv21_float')
main_conv21_double = solver.IntVar(0, 1, 'main_conv21_double')
main_conv21_enob = solver.IntVar(-10000, 10000, 'main_conv21_enob')
solver.Add( + (1)*main_conv21_enob + (-1)*main_conv21_fixbits + (10000)*main_conv21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv21_enob + (10000)*main_conv21_float<=10019)    #Enob constraint for float
solver.Add( + (1)*main_conv21_enob + (10000)*main_conv21_double<=10048)    #Enob constraint for double
solver.Add( + (1)*main_conv21_fixbits + (-10000)*main_conv21_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv21_enob
solver.Add( + (1)*main_conv21_fixp + (1)*main_conv21_float + (1)*main_conv21_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv21_fixbits + (-10000)*main_conv21_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv21_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div22 = fdiv double %conv20, %conv21, !taffo.info !33, !taffo.initweight !47
main_conv20_CAST_div22_fixbits = solver.IntVar(0, 27, 'main_conv20_CAST_div22_fixbits')
main_conv20_CAST_div22_fixp = solver.IntVar(0, 1, 'main_conv20_CAST_div22_fixp')
main_conv20_CAST_div22_float = solver.IntVar(0, 1, 'main_conv20_CAST_div22_float')
main_conv20_CAST_div22_double = solver.IntVar(0, 1, 'main_conv20_CAST_div22_double')
solver.Add( + (1)*main_conv20_CAST_div22_fixp + (1)*main_conv20_CAST_div22_float + (1)*main_conv20_CAST_div22_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv20_CAST_div22_fixbits + (-10000)*main_conv20_CAST_div22_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C1_main_conv20_CAST_div22')
C2_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C2_main_conv20_CAST_div22')
solver.Add( + (1)*main_conv20_fixbits + (-1)*main_conv20_CAST_div22_fixbits + (-10000)*C1_main_conv20_CAST_div22<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv20_fixbits + (1)*main_conv20_CAST_div22_fixbits + (-10000)*C2_main_conv20_CAST_div22<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv20_CAST_div22
castCostObj +=  + (1)*C2_main_conv20_CAST_div22
C3_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C3_main_conv20_CAST_div22')
C4_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C4_main_conv20_CAST_div22')
C5_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C5_main_conv20_CAST_div22')
C6_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C6_main_conv20_CAST_div22')
C7_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C7_main_conv20_CAST_div22')
C8_main_conv20_CAST_div22 = solver.IntVar(0, 1, 'C8_main_conv20_CAST_div22')
solver.Add( + (1)*main_conv20_fixp + (1)*main_conv20_CAST_div22_float + (-1)*C3_main_conv20_CAST_div22<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_conv20_CAST_div22
solver.Add( + (1)*main_conv20_float + (1)*main_conv20_CAST_div22_fixp + (-1)*C4_main_conv20_CAST_div22<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_conv20_CAST_div22
solver.Add( + (1)*main_conv20_fixp + (1)*main_conv20_CAST_div22_double + (-1)*C5_main_conv20_CAST_div22<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_conv20_CAST_div22
solver.Add( + (1)*main_conv20_double + (1)*main_conv20_CAST_div22_fixp + (-1)*C6_main_conv20_CAST_div22<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_conv20_CAST_div22
solver.Add( + (1)*main_conv20_float + (1)*main_conv20_CAST_div22_double + (-1)*C7_main_conv20_CAST_div22<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_conv20_CAST_div22
solver.Add( + (1)*main_conv20_double + (1)*main_conv20_CAST_div22_float + (-1)*C8_main_conv20_CAST_div22<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_conv20_CAST_div22



#Constraint for cast for   %div22 = fdiv double %conv20, %conv21, !taffo.info !33, !taffo.initweight !47
main_conv21_CAST_div22_fixbits = solver.IntVar(0, 27, 'main_conv21_CAST_div22_fixbits')
main_conv21_CAST_div22_fixp = solver.IntVar(0, 1, 'main_conv21_CAST_div22_fixp')
main_conv21_CAST_div22_float = solver.IntVar(0, 1, 'main_conv21_CAST_div22_float')
main_conv21_CAST_div22_double = solver.IntVar(0, 1, 'main_conv21_CAST_div22_double')
solver.Add( + (1)*main_conv21_CAST_div22_fixp + (1)*main_conv21_CAST_div22_float + (1)*main_conv21_CAST_div22_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv21_CAST_div22_fixbits + (-10000)*main_conv21_CAST_div22_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C1_main_conv21_CAST_div22')
C2_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C2_main_conv21_CAST_div22')
solver.Add( + (1)*main_conv21_fixbits + (-1)*main_conv21_CAST_div22_fixbits + (-10000)*C1_main_conv21_CAST_div22<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv21_fixbits + (1)*main_conv21_CAST_div22_fixbits + (-10000)*C2_main_conv21_CAST_div22<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv21_CAST_div22
castCostObj +=  + (1)*C2_main_conv21_CAST_div22
C3_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C3_main_conv21_CAST_div22')
C4_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C4_main_conv21_CAST_div22')
C5_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C5_main_conv21_CAST_div22')
C6_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C6_main_conv21_CAST_div22')
C7_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C7_main_conv21_CAST_div22')
C8_main_conv21_CAST_div22 = solver.IntVar(0, 1, 'C8_main_conv21_CAST_div22')
solver.Add( + (1)*main_conv21_fixp + (1)*main_conv21_CAST_div22_float + (-1)*C3_main_conv21_CAST_div22<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_conv21_CAST_div22
solver.Add( + (1)*main_conv21_float + (1)*main_conv21_CAST_div22_fixp + (-1)*C4_main_conv21_CAST_div22<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_conv21_CAST_div22
solver.Add( + (1)*main_conv21_fixp + (1)*main_conv21_CAST_div22_double + (-1)*C5_main_conv21_CAST_div22<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_conv21_CAST_div22
solver.Add( + (1)*main_conv21_double + (1)*main_conv21_CAST_div22_fixp + (-1)*C6_main_conv21_CAST_div22<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_conv21_CAST_div22
solver.Add( + (1)*main_conv21_float + (1)*main_conv21_CAST_div22_double + (-1)*C7_main_conv21_CAST_div22<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_conv21_CAST_div22
solver.Add( + (1)*main_conv21_double + (1)*main_conv21_CAST_div22_float + (-1)*C8_main_conv21_CAST_div22<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_conv21_CAST_div22



#Stuff for   %div22 = fdiv double %conv20, %conv21, !taffo.info !33, !taffo.initweight !47
main_div22_fixbits = solver.IntVar(0, 31, 'main_div22_fixbits')
main_div22_fixp = solver.IntVar(0, 1, 'main_div22_fixp')
main_div22_float = solver.IntVar(0, 1, 'main_div22_float')
main_div22_double = solver.IntVar(0, 1, 'main_div22_double')
main_div22_enob = solver.IntVar(-10000, 10000, 'main_div22_enob')
solver.Add( + (1)*main_div22_enob + (-1)*main_div22_fixbits + (10000)*main_div22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div22_enob + (10000)*main_div22_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div22_enob + (10000)*main_div22_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div22_fixbits + (-10000)*main_div22_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*main_div22_enob
solver.Add( + (1)*main_div22_fixp + (1)*main_div22_float + (1)*main_div22_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div22_fixbits + (-10000)*main_div22_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv20_CAST_div22_fixp + (-1)*main_conv21_CAST_div22_fixp==0)    #fix equality
solver.Add( + (1)*main_conv20_CAST_div22_float + (-1)*main_conv21_CAST_div22_float==0)    #float equality
solver.Add( + (1)*main_conv20_CAST_div22_double + (-1)*main_conv21_CAST_div22_double==0)    #double equality
solver.Add( + (1)*main_conv20_CAST_div22_fixp + (-1)*main_div22_fixp==0)    #fix equality
solver.Add( + (1)*main_conv20_CAST_div22_float + (-1)*main_div22_float==0)    #float equality
solver.Add( + (1)*main_conv20_CAST_div22_double + (-1)*main_div22_double==0)    #double equality
mathCostObj +=  + (13.2477)*main_div22_fixp
mathCostObj +=  + (6.64202)*main_div22_float
mathCostObj +=  + (7.0892)*main_div22_double
main_main_div22_enob_1 = solver.IntVar(0, 1, 'main_main_div22_enob_1')
main_main_div22_enob_2 = solver.IntVar(0, 1, 'main_main_div22_enob_2')
solver.Add( + (1)*main_main_div22_enob_1 + (1)*main_main_div22_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div22_enob + (-1)*main_conv21_enob + (-10000)*main_main_div22_enob_1<=1034)    #Enob: propagation in division 1
solver.Add( + (1)*main_div22_enob + (-1)*main_conv20_enob + (-10000)*main_main_div22_enob_2<=5)    #Enob: propagation in division 2



#Constraint for cast for   store double %div22, double* %arrayidx26, align 8, !taffo.info !12, !taffo.initweight !24
main_div22_CAST_store_fixbits = solver.IntVar(0, 31, 'main_div22_CAST_store_fixbits')
main_div22_CAST_store_fixp = solver.IntVar(0, 1, 'main_div22_CAST_store_fixp')
main_div22_CAST_store_float = solver.IntVar(0, 1, 'main_div22_CAST_store_float')
main_div22_CAST_store_double = solver.IntVar(0, 1, 'main_div22_CAST_store_double')
solver.Add( + (1)*main_div22_CAST_store_fixp + (1)*main_div22_CAST_store_float + (1)*main_div22_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div22_CAST_store_fixbits + (-10000)*main_div22_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div22_CAST_store = solver.IntVar(0, 1, 'C1_main_div22_CAST_store')
C2_main_div22_CAST_store = solver.IntVar(0, 1, 'C2_main_div22_CAST_store')
solver.Add( + (1)*main_div22_fixbits + (-1)*main_div22_CAST_store_fixbits + (-10000)*C1_main_div22_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div22_fixbits + (1)*main_div22_CAST_store_fixbits + (-10000)*C2_main_div22_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div22_CAST_store
castCostObj +=  + (1)*C2_main_div22_CAST_store
C3_main_div22_CAST_store = solver.IntVar(0, 1, 'C3_main_div22_CAST_store')
C4_main_div22_CAST_store = solver.IntVar(0, 1, 'C4_main_div22_CAST_store')
C5_main_div22_CAST_store = solver.IntVar(0, 1, 'C5_main_div22_CAST_store')
C6_main_div22_CAST_store = solver.IntVar(0, 1, 'C6_main_div22_CAST_store')
C7_main_div22_CAST_store = solver.IntVar(0, 1, 'C7_main_div22_CAST_store')
C8_main_div22_CAST_store = solver.IntVar(0, 1, 'C8_main_div22_CAST_store')
solver.Add( + (1)*main_div22_fixp + (1)*main_div22_CAST_store_float + (-1)*C3_main_div22_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_div22_CAST_store
solver.Add( + (1)*main_div22_float + (1)*main_div22_CAST_store_fixp + (-1)*C4_main_div22_CAST_store<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_div22_CAST_store
solver.Add( + (1)*main_div22_fixp + (1)*main_div22_CAST_store_double + (-1)*C5_main_div22_CAST_store<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_div22_CAST_store
solver.Add( + (1)*main_div22_double + (1)*main_div22_CAST_store_fixp + (-1)*C6_main_div22_CAST_store<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_div22_CAST_store
solver.Add( + (1)*main_div22_float + (1)*main_div22_CAST_store_double + (-1)*C7_main_div22_CAST_store<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_div22_CAST_store
solver.Add( + (1)*main_div22_double + (1)*main_div22_CAST_store_float + (-1)*C8_main_div22_CAST_store<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_div22_CAST_store
solver.Add( + (1)*B_fixp + (-1)*main_div22_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B_float + (-1)*main_div22_CAST_store_float==0)    #float equality
solver.Add( + (1)*B_double + (-1)*main_div22_CAST_store_double==0)    #double equality
solver.Add( + (1)*B_fixbits + (-1)*main_div22_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
B_enob_storeENOB = solver.IntVar(-10000, 10000, 'B_enob_storeENOB')
solver.Add( + (1)*B_enob_storeENOB + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob_storeENOB + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob_storeENOB + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_enob_storeENOB + (-1)*main_div22_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp')
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_2 = solver.IntVar(0, 1, 'main_main_tmp_enob_2')
solver.Add( + (1)*main_main_tmp_enob_2==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*B_enob_storeENOB + (10000)*main_main_tmp_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp1')
solver.Add( + (1)*B_enob_memphi_main_tmp1 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
main_main_tmp1_enob_3 = solver.IntVar(0, 1, 'main_main_tmp1_enob_3')
main_main_tmp1_enob_4 = solver.IntVar(0, 1, 'main_main_tmp1_enob_4')
solver.Add( + (1)*main_main_tmp1_enob_2 + (1)*main_main_tmp1_enob_3 + (1)*main_main_tmp1_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp1 + (-1)*B_enob_storeENOB + (10000)*main_main_tmp1_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !49, !taffo.initweight !30
A_CAST_mul_fixbits = solver.IntVar(0, 31, 'A_CAST_mul_fixbits')
A_CAST_mul_fixp = solver.IntVar(0, 1, 'A_CAST_mul_fixp')
A_CAST_mul_float = solver.IntVar(0, 1, 'A_CAST_mul_float')
A_CAST_mul_double = solver.IntVar(0, 1, 'A_CAST_mul_double')
solver.Add( + (1)*A_CAST_mul_fixp + (1)*A_CAST_mul_float + (1)*A_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_mul_fixbits + (-10000)*A_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_mul = solver.IntVar(0, 1, 'C1_A_CAST_mul')
C2_A_CAST_mul = solver.IntVar(0, 1, 'C2_A_CAST_mul')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_mul_fixbits + (-10000)*C1_A_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_mul_fixbits + (-10000)*C2_A_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_mul
castCostObj +=  + (1)*C2_A_CAST_mul
C3_A_CAST_mul = solver.IntVar(0, 1, 'C3_A_CAST_mul')
C4_A_CAST_mul = solver.IntVar(0, 1, 'C4_A_CAST_mul')
C5_A_CAST_mul = solver.IntVar(0, 1, 'C5_A_CAST_mul')
C6_A_CAST_mul = solver.IntVar(0, 1, 'C6_A_CAST_mul')
C7_A_CAST_mul = solver.IntVar(0, 1, 'C7_A_CAST_mul')
C8_A_CAST_mul = solver.IntVar(0, 1, 'C8_A_CAST_mul')
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul_float + (-1)*C3_A_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_A_CAST_mul
solver.Add( + (1)*A_float + (1)*A_CAST_mul_fixp + (-1)*C4_A_CAST_mul<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_A_CAST_mul
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul_double + (-1)*C5_A_CAST_mul<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_A_CAST_mul
solver.Add( + (1)*A_double + (1)*A_CAST_mul_fixp + (-1)*C6_A_CAST_mul<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_A_CAST_mul
solver.Add( + (1)*A_float + (1)*A_CAST_mul_double + (-1)*C7_A_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_A_CAST_mul
solver.Add( + (1)*A_double + (1)*A_CAST_mul_float + (-1)*C8_A_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_A_CAST_mul



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !49, !taffo.initweight !30
B_CAST_mul_fixbits = solver.IntVar(0, 22, 'B_CAST_mul_fixbits')
B_CAST_mul_fixp = solver.IntVar(0, 1, 'B_CAST_mul_fixp')
B_CAST_mul_float = solver.IntVar(0, 1, 'B_CAST_mul_float')
B_CAST_mul_double = solver.IntVar(0, 1, 'B_CAST_mul_double')
solver.Add( + (1)*B_CAST_mul_fixp + (1)*B_CAST_mul_float + (1)*B_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_mul_fixbits + (-10000)*B_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_mul = solver.IntVar(0, 1, 'C1_B_CAST_mul')
C2_B_CAST_mul = solver.IntVar(0, 1, 'C2_B_CAST_mul')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_mul_fixbits + (-10000)*C1_B_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_mul_fixbits + (-10000)*C2_B_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_mul
castCostObj +=  + (1)*C2_B_CAST_mul
C3_B_CAST_mul = solver.IntVar(0, 1, 'C3_B_CAST_mul')
C4_B_CAST_mul = solver.IntVar(0, 1, 'C4_B_CAST_mul')
C5_B_CAST_mul = solver.IntVar(0, 1, 'C5_B_CAST_mul')
C6_B_CAST_mul = solver.IntVar(0, 1, 'C6_B_CAST_mul')
C7_B_CAST_mul = solver.IntVar(0, 1, 'C7_B_CAST_mul')
C8_B_CAST_mul = solver.IntVar(0, 1, 'C8_B_CAST_mul')
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul_float + (-1)*C3_B_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_B_CAST_mul
solver.Add( + (1)*B_float + (1)*B_CAST_mul_fixp + (-1)*C4_B_CAST_mul<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_B_CAST_mul
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul_double + (-1)*C5_B_CAST_mul<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_B_CAST_mul
solver.Add( + (1)*B_double + (1)*B_CAST_mul_fixp + (-1)*C6_B_CAST_mul<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_B_CAST_mul
solver.Add( + (1)*B_float + (1)*B_CAST_mul_double + (-1)*C7_B_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_B_CAST_mul
solver.Add( + (1)*B_double + (1)*B_CAST_mul_float + (-1)*C8_B_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_B_CAST_mul



#Stuff for   %mul = fmul double %tmp, %tmp1, !taffo.info !49, !taffo.initweight !30
main_mul_fixbits = solver.IntVar(0, 22, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_mul_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul_enob
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*A_CAST_mul_fixp + (-1)*B_CAST_mul_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_mul_float + (-1)*B_CAST_mul_float==0)    #float equality
solver.Add( + (1)*A_CAST_mul_double + (-1)*B_CAST_mul_double==0)    #double equality
solver.Add( + (1)*A_CAST_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*A_CAST_mul_double + (-1)*main_mul_double==0)    #double equality
mathCostObj +=  + (2.64906)*main_mul_fixp
mathCostObj +=  + (4.52523)*main_mul_float
mathCostObj +=  + (3.01526)*main_mul_double
main_main_mul_enob_1 = solver.IntVar(0, 1, 'main_main_mul_enob_1')
main_main_mul_enob_2 = solver.IntVar(0, 1, 'main_main_mul_enob_2')
solver.Add( + (1)*main_main_mul_enob_1 + (1)*main_main_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul_enob + (-1)*B_enob_memphi_main_tmp1 + (-10000)*main_main_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul_enob + (-1)*A_enob_memphi_main_tmp + (-10000)*main_main_mul_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp2')
solver.Add( + (1)*B_enob_memphi_main_tmp2 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
main_main_tmp2_enob_3 = solver.IntVar(0, 1, 'main_main_tmp2_enob_3')
main_main_tmp2_enob_4 = solver.IntVar(0, 1, 'main_main_tmp2_enob_4')
solver.Add( + (1)*main_main_tmp2_enob_2 + (1)*main_main_tmp2_enob_3 + (1)*main_main_tmp2_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp2 + (-1)*B_enob_storeENOB + (10000)*main_main_tmp2_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add58 = fadd double %tmp2, %mul, !taffo.info !50, !taffo.initweight !30
B_CAST_add58_fixbits = solver.IntVar(0, 22, 'B_CAST_add58_fixbits')
B_CAST_add58_fixp = solver.IntVar(0, 1, 'B_CAST_add58_fixp')
B_CAST_add58_float = solver.IntVar(0, 1, 'B_CAST_add58_float')
B_CAST_add58_double = solver.IntVar(0, 1, 'B_CAST_add58_double')
solver.Add( + (1)*B_CAST_add58_fixp + (1)*B_CAST_add58_float + (1)*B_CAST_add58_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_add58_fixbits + (-10000)*B_CAST_add58_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_add58 = solver.IntVar(0, 1, 'C1_B_CAST_add58')
C2_B_CAST_add58 = solver.IntVar(0, 1, 'C2_B_CAST_add58')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_add58_fixbits + (-10000)*C1_B_CAST_add58<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_add58_fixbits + (-10000)*C2_B_CAST_add58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_add58
castCostObj +=  + (1)*C2_B_CAST_add58
C3_B_CAST_add58 = solver.IntVar(0, 1, 'C3_B_CAST_add58')
C4_B_CAST_add58 = solver.IntVar(0, 1, 'C4_B_CAST_add58')
C5_B_CAST_add58 = solver.IntVar(0, 1, 'C5_B_CAST_add58')
C6_B_CAST_add58 = solver.IntVar(0, 1, 'C6_B_CAST_add58')
C7_B_CAST_add58 = solver.IntVar(0, 1, 'C7_B_CAST_add58')
C8_B_CAST_add58 = solver.IntVar(0, 1, 'C8_B_CAST_add58')
solver.Add( + (1)*B_fixp + (1)*B_CAST_add58_float + (-1)*C3_B_CAST_add58<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_B_CAST_add58
solver.Add( + (1)*B_float + (1)*B_CAST_add58_fixp + (-1)*C4_B_CAST_add58<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_B_CAST_add58
solver.Add( + (1)*B_fixp + (1)*B_CAST_add58_double + (-1)*C5_B_CAST_add58<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_B_CAST_add58
solver.Add( + (1)*B_double + (1)*B_CAST_add58_fixp + (-1)*C6_B_CAST_add58<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_B_CAST_add58
solver.Add( + (1)*B_float + (1)*B_CAST_add58_double + (-1)*C7_B_CAST_add58<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_B_CAST_add58
solver.Add( + (1)*B_double + (1)*B_CAST_add58_float + (-1)*C8_B_CAST_add58<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_B_CAST_add58



#Constraint for cast for   %add58 = fadd double %tmp2, %mul, !taffo.info !50, !taffo.initweight !30
main_mul_CAST_add58_fixbits = solver.IntVar(0, 22, 'main_mul_CAST_add58_fixbits')
main_mul_CAST_add58_fixp = solver.IntVar(0, 1, 'main_mul_CAST_add58_fixp')
main_mul_CAST_add58_float = solver.IntVar(0, 1, 'main_mul_CAST_add58_float')
main_mul_CAST_add58_double = solver.IntVar(0, 1, 'main_mul_CAST_add58_double')
solver.Add( + (1)*main_mul_CAST_add58_fixp + (1)*main_mul_CAST_add58_float + (1)*main_mul_CAST_add58_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul_CAST_add58_fixbits + (-10000)*main_mul_CAST_add58_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C1_main_mul_CAST_add58')
C2_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C2_main_mul_CAST_add58')
solver.Add( + (1)*main_mul_fixbits + (-1)*main_mul_CAST_add58_fixbits + (-10000)*C1_main_mul_CAST_add58<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul_fixbits + (1)*main_mul_CAST_add58_fixbits + (-10000)*C2_main_mul_CAST_add58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul_CAST_add58
castCostObj +=  + (1)*C2_main_mul_CAST_add58
C3_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C3_main_mul_CAST_add58')
C4_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C4_main_mul_CAST_add58')
C5_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C5_main_mul_CAST_add58')
C6_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C6_main_mul_CAST_add58')
C7_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C7_main_mul_CAST_add58')
C8_main_mul_CAST_add58 = solver.IntVar(0, 1, 'C8_main_mul_CAST_add58')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_add58_float + (-1)*C3_main_mul_CAST_add58<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_mul_CAST_add58
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_add58_fixp + (-1)*C4_main_mul_CAST_add58<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_mul_CAST_add58
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_add58_double + (-1)*C5_main_mul_CAST_add58<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_mul_CAST_add58
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_add58_fixp + (-1)*C6_main_mul_CAST_add58<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_mul_CAST_add58
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_add58_double + (-1)*C7_main_mul_CAST_add58<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_mul_CAST_add58
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_add58_float + (-1)*C8_main_mul_CAST_add58<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_mul_CAST_add58



#Stuff for   %add58 = fadd double %tmp2, %mul, !taffo.info !50, !taffo.initweight !30
main_add58_fixbits = solver.IntVar(0, 21, 'main_add58_fixbits')
main_add58_fixp = solver.IntVar(0, 1, 'main_add58_fixp')
main_add58_float = solver.IntVar(0, 1, 'main_add58_float')
main_add58_double = solver.IntVar(0, 1, 'main_add58_double')
main_add58_enob = solver.IntVar(-10000, 10000, 'main_add58_enob')
solver.Add( + (1)*main_add58_enob + (-1)*main_add58_fixbits + (10000)*main_add58_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add58_enob + (10000)*main_add58_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add58_enob + (10000)*main_add58_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add58_fixbits + (-10000)*main_add58_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_add58_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add58_enob
solver.Add( + (1)*main_add58_fixp + (1)*main_add58_float + (1)*main_add58_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add58_fixbits + (-10000)*main_add58_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*B_CAST_add58_fixp + (-1)*main_mul_CAST_add58_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_add58_float + (-1)*main_mul_CAST_add58_float==0)    #float equality
solver.Add( + (1)*B_CAST_add58_double + (-1)*main_mul_CAST_add58_double==0)    #double equality
solver.Add( + (1)*B_CAST_add58_fixbits + (-1)*main_mul_CAST_add58_fixbits==0)    #same fractional bit
solver.Add( + (1)*B_CAST_add58_fixp + (-1)*main_add58_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_add58_float + (-1)*main_add58_float==0)    #float equality
solver.Add( + (1)*B_CAST_add58_double + (-1)*main_add58_double==0)    #double equality
solver.Add( + (1)*B_CAST_add58_fixbits + (-1)*main_add58_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.43251)*main_add58_fixp
mathCostObj +=  + (1.47242)*main_add58_float
mathCostObj +=  + (2.6385)*main_add58_double
solver.Add( + (1)*main_add58_enob + (-1)*B_enob_memphi_main_tmp2<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add58_enob + (-1)*main_mul_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add58, double* %arrayidx57, align 8, !taffo.info !12, !taffo.initweight !24
main_add58_CAST_store_fixbits = solver.IntVar(0, 21, 'main_add58_CAST_store_fixbits')
main_add58_CAST_store_fixp = solver.IntVar(0, 1, 'main_add58_CAST_store_fixp')
main_add58_CAST_store_float = solver.IntVar(0, 1, 'main_add58_CAST_store_float')
main_add58_CAST_store_double = solver.IntVar(0, 1, 'main_add58_CAST_store_double')
solver.Add( + (1)*main_add58_CAST_store_fixp + (1)*main_add58_CAST_store_float + (1)*main_add58_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add58_CAST_store_fixbits + (-10000)*main_add58_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add58_CAST_store = solver.IntVar(0, 1, 'C1_main_add58_CAST_store')
C2_main_add58_CAST_store = solver.IntVar(0, 1, 'C2_main_add58_CAST_store')
solver.Add( + (1)*main_add58_fixbits + (-1)*main_add58_CAST_store_fixbits + (-10000)*C1_main_add58_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add58_fixbits + (1)*main_add58_CAST_store_fixbits + (-10000)*C2_main_add58_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add58_CAST_store
castCostObj +=  + (1)*C2_main_add58_CAST_store
C3_main_add58_CAST_store = solver.IntVar(0, 1, 'C3_main_add58_CAST_store')
C4_main_add58_CAST_store = solver.IntVar(0, 1, 'C4_main_add58_CAST_store')
C5_main_add58_CAST_store = solver.IntVar(0, 1, 'C5_main_add58_CAST_store')
C6_main_add58_CAST_store = solver.IntVar(0, 1, 'C6_main_add58_CAST_store')
C7_main_add58_CAST_store = solver.IntVar(0, 1, 'C7_main_add58_CAST_store')
C8_main_add58_CAST_store = solver.IntVar(0, 1, 'C8_main_add58_CAST_store')
solver.Add( + (1)*main_add58_fixp + (1)*main_add58_CAST_store_float + (-1)*C3_main_add58_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_add58_CAST_store
solver.Add( + (1)*main_add58_float + (1)*main_add58_CAST_store_fixp + (-1)*C4_main_add58_CAST_store<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_add58_CAST_store
solver.Add( + (1)*main_add58_fixp + (1)*main_add58_CAST_store_double + (-1)*C5_main_add58_CAST_store<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_add58_CAST_store
solver.Add( + (1)*main_add58_double + (1)*main_add58_CAST_store_fixp + (-1)*C6_main_add58_CAST_store<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_add58_CAST_store
solver.Add( + (1)*main_add58_float + (1)*main_add58_CAST_store_double + (-1)*C7_main_add58_CAST_store<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_add58_CAST_store
solver.Add( + (1)*main_add58_double + (1)*main_add58_CAST_store_float + (-1)*C8_main_add58_CAST_store<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_add58_CAST_store
solver.Add( + (1)*B_fixp + (-1)*main_add58_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B_float + (-1)*main_add58_CAST_store_float==0)    #float equality
solver.Add( + (1)*B_double + (-1)*main_add58_CAST_store_double==0)    #double equality
solver.Add( + (1)*B_fixbits + (-1)*main_add58_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
B_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'B_enob_storeENOB_storeENOB')
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (-1)*main_add58_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp1 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp2 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp3')
solver.Add( + (1)*B_enob_memphi_main_tmp3 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
solver.Add( + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3 + (1)*main_main_tmp3_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp3 + (-1)*B_enob_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp3 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.500000e+00
ConstantValue__1_fixbits = solver.IntVar(0, 30, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.500000e+00
ConstantValue__2_fixbits = solver.IntVar(0, 30, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.500000e+00
ConstantValue__3_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul66 = fmul double 1.500000e+00, %tmp3, !taffo.info !54, !taffo.initweight !23, !taffo.constinfo !56
ConstantValue__3_CAST_mul66_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_CAST_mul66_fixbits')
ConstantValue__3_CAST_mul66_fixp = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul66_fixp')
ConstantValue__3_CAST_mul66_float = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul66_float')
ConstantValue__3_CAST_mul66_double = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul66_double')
solver.Add( + (1)*ConstantValue__3_CAST_mul66_fixp + (1)*ConstantValue__3_CAST_mul66_float + (1)*ConstantValue__3_CAST_mul66_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__3_CAST_mul66_fixbits + (-10000)*ConstantValue__3_CAST_mul66_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C1_ConstantValue__3_CAST_mul66')
C2_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C2_ConstantValue__3_CAST_mul66')
solver.Add( + (1)*ConstantValue__3_fixbits + (-1)*ConstantValue__3_CAST_mul66_fixbits + (-10000)*C1_ConstantValue__3_CAST_mul66<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__3_fixbits + (1)*ConstantValue__3_CAST_mul66_fixbits + (-10000)*C2_ConstantValue__3_CAST_mul66<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__3_CAST_mul66
castCostObj +=  + (1)*C2_ConstantValue__3_CAST_mul66
C3_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C3_ConstantValue__3_CAST_mul66')
C4_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C4_ConstantValue__3_CAST_mul66')
C5_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C5_ConstantValue__3_CAST_mul66')
C6_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C6_ConstantValue__3_CAST_mul66')
C7_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C7_ConstantValue__3_CAST_mul66')
C8_ConstantValue__3_CAST_mul66 = solver.IntVar(0, 1, 'C8_ConstantValue__3_CAST_mul66')
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul66_float + (-1)*C3_ConstantValue__3_CAST_mul66<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_ConstantValue__3_CAST_mul66
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul66_fixp + (-1)*C4_ConstantValue__3_CAST_mul66<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_ConstantValue__3_CAST_mul66
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul66_double + (-1)*C5_ConstantValue__3_CAST_mul66<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_ConstantValue__3_CAST_mul66
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul66_fixp + (-1)*C6_ConstantValue__3_CAST_mul66<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_ConstantValue__3_CAST_mul66
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul66_double + (-1)*C7_ConstantValue__3_CAST_mul66<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_ConstantValue__3_CAST_mul66
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul66_float + (-1)*C8_ConstantValue__3_CAST_mul66<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_ConstantValue__3_CAST_mul66



#Constraint for cast for   %mul66 = fmul double 1.500000e+00, %tmp3, !taffo.info !54, !taffo.initweight !23, !taffo.constinfo !56
B_CAST_mul66_fixbits = solver.IntVar(0, 22, 'B_CAST_mul66_fixbits')
B_CAST_mul66_fixp = solver.IntVar(0, 1, 'B_CAST_mul66_fixp')
B_CAST_mul66_float = solver.IntVar(0, 1, 'B_CAST_mul66_float')
B_CAST_mul66_double = solver.IntVar(0, 1, 'B_CAST_mul66_double')
solver.Add( + (1)*B_CAST_mul66_fixp + (1)*B_CAST_mul66_float + (1)*B_CAST_mul66_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_mul66_fixbits + (-10000)*B_CAST_mul66_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_mul66 = solver.IntVar(0, 1, 'C1_B_CAST_mul66')
C2_B_CAST_mul66 = solver.IntVar(0, 1, 'C2_B_CAST_mul66')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_mul66_fixbits + (-10000)*C1_B_CAST_mul66<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_mul66_fixbits + (-10000)*C2_B_CAST_mul66<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_mul66
castCostObj +=  + (1)*C2_B_CAST_mul66
C3_B_CAST_mul66 = solver.IntVar(0, 1, 'C3_B_CAST_mul66')
C4_B_CAST_mul66 = solver.IntVar(0, 1, 'C4_B_CAST_mul66')
C5_B_CAST_mul66 = solver.IntVar(0, 1, 'C5_B_CAST_mul66')
C6_B_CAST_mul66 = solver.IntVar(0, 1, 'C6_B_CAST_mul66')
C7_B_CAST_mul66 = solver.IntVar(0, 1, 'C7_B_CAST_mul66')
C8_B_CAST_mul66 = solver.IntVar(0, 1, 'C8_B_CAST_mul66')
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul66_float + (-1)*C3_B_CAST_mul66<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_B_CAST_mul66
solver.Add( + (1)*B_float + (1)*B_CAST_mul66_fixp + (-1)*C4_B_CAST_mul66<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_B_CAST_mul66
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul66_double + (-1)*C5_B_CAST_mul66<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_B_CAST_mul66
solver.Add( + (1)*B_double + (1)*B_CAST_mul66_fixp + (-1)*C6_B_CAST_mul66<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_B_CAST_mul66
solver.Add( + (1)*B_float + (1)*B_CAST_mul66_double + (-1)*C7_B_CAST_mul66<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_B_CAST_mul66
solver.Add( + (1)*B_double + (1)*B_CAST_mul66_float + (-1)*C8_B_CAST_mul66<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_B_CAST_mul66



#Stuff for   %mul66 = fmul double 1.500000e+00, %tmp3, !taffo.info !54, !taffo.initweight !23, !taffo.constinfo !56
main_mul66_fixbits = solver.IntVar(0, 22, 'main_mul66_fixbits')
main_mul66_fixp = solver.IntVar(0, 1, 'main_mul66_fixp')
main_mul66_float = solver.IntVar(0, 1, 'main_mul66_float')
main_mul66_double = solver.IntVar(0, 1, 'main_mul66_double')
main_mul66_enob = solver.IntVar(-10000, 10000, 'main_mul66_enob')
solver.Add( + (1)*main_mul66_enob + (-1)*main_mul66_fixbits + (10000)*main_mul66_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul66_enob + (10000)*main_mul66_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul66_enob + (10000)*main_mul66_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul66_fixbits + (-10000)*main_mul66_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_mul66_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul66_enob
solver.Add( + (1)*main_mul66_fixp + (1)*main_mul66_float + (1)*main_mul66_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul66_fixbits + (-10000)*main_mul66_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__3_CAST_mul66_fixp + (-1)*B_CAST_mul66_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul66_float + (-1)*B_CAST_mul66_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul66_double + (-1)*B_CAST_mul66_double==0)    #double equality
solver.Add( + (1)*ConstantValue__3_CAST_mul66_fixp + (-1)*main_mul66_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul66_float + (-1)*main_mul66_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul66_double + (-1)*main_mul66_double==0)    #double equality
mathCostObj +=  + (2.64906)*main_mul66_fixp
mathCostObj +=  + (4.52523)*main_mul66_float
mathCostObj +=  + (3.01526)*main_mul66_double
main_main_mul66_enob_1 = solver.IntVar(0, 1, 'main_main_mul66_enob_1')
main_main_mul66_enob_2 = solver.IntVar(0, 1, 'main_main_mul66_enob_2')
solver.Add( + (1)*main_main_mul66_enob_1 + (1)*main_main_mul66_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul66_enob + (-1)*B_enob_memphi_main_tmp3 + (-10000)*main_main_mul66_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul66_enob + (-1)*ConstantValue__1_enob + (-10000)*main_main_mul66_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   store double %mul66, double* %arrayidx70, align 8, !taffo.info !12, !taffo.initweight !24
main_mul66_CAST_store_fixbits = solver.IntVar(0, 22, 'main_mul66_CAST_store_fixbits')
main_mul66_CAST_store_fixp = solver.IntVar(0, 1, 'main_mul66_CAST_store_fixp')
main_mul66_CAST_store_float = solver.IntVar(0, 1, 'main_mul66_CAST_store_float')
main_mul66_CAST_store_double = solver.IntVar(0, 1, 'main_mul66_CAST_store_double')
solver.Add( + (1)*main_mul66_CAST_store_fixp + (1)*main_mul66_CAST_store_float + (1)*main_mul66_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul66_CAST_store_fixbits + (-10000)*main_mul66_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul66_CAST_store = solver.IntVar(0, 1, 'C1_main_mul66_CAST_store')
C2_main_mul66_CAST_store = solver.IntVar(0, 1, 'C2_main_mul66_CAST_store')
solver.Add( + (1)*main_mul66_fixbits + (-1)*main_mul66_CAST_store_fixbits + (-10000)*C1_main_mul66_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul66_fixbits + (1)*main_mul66_CAST_store_fixbits + (-10000)*C2_main_mul66_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul66_CAST_store
castCostObj +=  + (1)*C2_main_mul66_CAST_store
C3_main_mul66_CAST_store = solver.IntVar(0, 1, 'C3_main_mul66_CAST_store')
C4_main_mul66_CAST_store = solver.IntVar(0, 1, 'C4_main_mul66_CAST_store')
C5_main_mul66_CAST_store = solver.IntVar(0, 1, 'C5_main_mul66_CAST_store')
C6_main_mul66_CAST_store = solver.IntVar(0, 1, 'C6_main_mul66_CAST_store')
C7_main_mul66_CAST_store = solver.IntVar(0, 1, 'C7_main_mul66_CAST_store')
C8_main_mul66_CAST_store = solver.IntVar(0, 1, 'C8_main_mul66_CAST_store')
solver.Add( + (1)*main_mul66_fixp + (1)*main_mul66_CAST_store_float + (-1)*C3_main_mul66_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_main_mul66_CAST_store
solver.Add( + (1)*main_mul66_float + (1)*main_mul66_CAST_store_fixp + (-1)*C4_main_mul66_CAST_store<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_main_mul66_CAST_store
solver.Add( + (1)*main_mul66_fixp + (1)*main_mul66_CAST_store_double + (-1)*C5_main_mul66_CAST_store<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_main_mul66_CAST_store
solver.Add( + (1)*main_mul66_double + (1)*main_mul66_CAST_store_fixp + (-1)*C6_main_mul66_CAST_store<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_main_mul66_CAST_store
solver.Add( + (1)*main_mul66_float + (1)*main_mul66_CAST_store_double + (-1)*C7_main_mul66_CAST_store<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_main_mul66_CAST_store
solver.Add( + (1)*main_mul66_double + (1)*main_mul66_CAST_store_float + (-1)*C8_main_mul66_CAST_store<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_main_mul66_CAST_store
solver.Add( + (1)*B_fixp + (-1)*main_mul66_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B_float + (-1)*main_mul66_CAST_store_float==0)    #float equality
solver.Add( + (1)*B_double + (-1)*main_mul66_CAST_store_double==0)    #double equality
solver.Add( + (1)*B_fixbits + (-1)*main_mul66_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
B_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'B_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*B_enob_storeENOB_storeENOB_storeENOB + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob_storeENOB_storeENOB_storeENOB + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob_storeENOB_storeENOB_storeENOB + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_enob_storeENOB_storeENOB_storeENOB + (-1)*main_mul66_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp1 + (-1)*B_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp2 + (-1)*B_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp3 + (-1)*B_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp6')
solver.Add( + (1)*B_enob_memphi_main_tmp6 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call94 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp5, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp6), !taffo.info !12, !taffo.initweight !30, !taffo.constinfo !60
B_CAST_call94_fixbits = solver.IntVar(0, 22, 'B_CAST_call94_fixbits')
B_CAST_call94_fixp = solver.IntVar(0, 1, 'B_CAST_call94_fixp')
B_CAST_call94_float = solver.IntVar(0, 1, 'B_CAST_call94_float')
B_CAST_call94_double = solver.IntVar(0, 1, 'B_CAST_call94_double')
solver.Add( + (1)*B_CAST_call94_fixp + (1)*B_CAST_call94_float + (1)*B_CAST_call94_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_call94_fixbits + (-10000)*B_CAST_call94_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_call94 = solver.IntVar(0, 1, 'C1_B_CAST_call94')
C2_B_CAST_call94 = solver.IntVar(0, 1, 'C2_B_CAST_call94')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_call94_fixbits + (-10000)*C1_B_CAST_call94<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_call94_fixbits + (-10000)*C2_B_CAST_call94<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_call94
castCostObj +=  + (1)*C2_B_CAST_call94
C3_B_CAST_call94 = solver.IntVar(0, 1, 'C3_B_CAST_call94')
C4_B_CAST_call94 = solver.IntVar(0, 1, 'C4_B_CAST_call94')
C5_B_CAST_call94 = solver.IntVar(0, 1, 'C5_B_CAST_call94')
C6_B_CAST_call94 = solver.IntVar(0, 1, 'C6_B_CAST_call94')
C7_B_CAST_call94 = solver.IntVar(0, 1, 'C7_B_CAST_call94')
C8_B_CAST_call94 = solver.IntVar(0, 1, 'C8_B_CAST_call94')
solver.Add( + (1)*B_fixp + (1)*B_CAST_call94_float + (-1)*C3_B_CAST_call94<=1)    #Fix to float
castCostObj +=  + (6.64554)*C3_B_CAST_call94
solver.Add( + (1)*B_float + (1)*B_CAST_call94_fixp + (-1)*C4_B_CAST_call94<=1)    #Float to fix
castCostObj +=  + (4.527)*C4_B_CAST_call94
solver.Add( + (1)*B_fixp + (1)*B_CAST_call94_double + (-1)*C5_B_CAST_call94<=1)    #Fix to double
castCostObj +=  + (7.54108)*C5_B_CAST_call94
solver.Add( + (1)*B_double + (1)*B_CAST_call94_fixp + (-1)*C6_B_CAST_call94<=1)    #Double to fix
castCostObj +=  + (3.31338)*C6_B_CAST_call94
solver.Add( + (1)*B_float + (1)*B_CAST_call94_double + (-1)*C7_B_CAST_call94<=1)    #Float to double
castCostObj +=  + (1.69718)*C7_B_CAST_call94
solver.Add( + (1)*B_double + (1)*B_CAST_call94_float + (-1)*C8_B_CAST_call94<=1)    #Double to float
castCostObj +=  + (1.39671)*C8_B_CAST_call94
solver.Add( + (1)*B_CAST_call94_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1 * castCostObj / 120.657+ 100000 * enobCostObj / 6057+ 1 * mathCostObj / 38.1843)

# Model declaration end.