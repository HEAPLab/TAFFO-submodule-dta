


#Stuff for @B = common dso_local global [10 x [10 x [10 x double]]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
B_fixbits = solver.IntVar(0, 17, 'B_fixbits')
B_fixp = solver.IntVar(0, 1, 'B_fixp')
B_float = solver.IntVar(0, 1, 'B_float')
B_double = solver.IntVar(0, 1, 'B_double')
B_enob = solver.IntVar(-10000, 10000, 'B_enob')
solver.Add( + (1)*B_enob + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_fixbits + (-10000)*B_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*B_enob<=333)    #Enob constraint for error maximal
enobCostObj =  + (-1)*B_enob
solver.Add( + (1)*B_fixp + (1)*B_float + (1)*B_double==1)    #Exactly one selected type
solver.Add( + (1)*B_fixbits + (-10000)*B_fixp<=0)    #If not fix, frac part to zero



#Stuff for @A = common dso_local global [10 x [10 x [10 x double]]] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
A_fixbits = solver.IntVar(0, 16, 'A_fixbits')
A_fixp = solver.IntVar(0, 1, 'A_fixp')
A_float = solver.IntVar(0, 1, 'A_float')
A_double = solver.IntVar(0, 1, 'A_double')
A_enob = solver.IntVar(-10000, 10000, 'A_enob')
solver.Add( + (1)*A_enob + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_fixbits + (-10000)*A_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*A_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*A_enob
solver.Add( + (1)*A_fixp + (1)*A_float + (1)*A_double==1)    #Exactly one selected type
solver.Add( + (1)*A_fixbits + (-10000)*A_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %add11 to double, !taffo.info !26, !taffo.initweight !28
main_conv_fixbits = solver.IntVar(0, 24, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*main_conv_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for double 1.000000e+01
ConstantValue__fixbits = solver.IntVar(0, 28, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10020)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10049)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+01
ConstantValue__0_fixbits = solver.IntVar(0, 28, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10020)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10049)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul = fmul double %conv, 1.000000e+01, !taffo.info !29, !taffo.initweight !31, !taffo.constinfo !32
main_conv_CAST_mul_fixbits = solver.IntVar(0, 24, 'main_conv_CAST_mul_fixbits')
main_conv_CAST_mul_fixp = solver.IntVar(0, 1, 'main_conv_CAST_mul_fixp')
main_conv_CAST_mul_float = solver.IntVar(0, 1, 'main_conv_CAST_mul_float')
main_conv_CAST_mul_double = solver.IntVar(0, 1, 'main_conv_CAST_mul_double')
solver.Add( + (1)*main_conv_CAST_mul_fixp + (1)*main_conv_CAST_mul_float + (1)*main_conv_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv_CAST_mul_fixbits + (-10000)*main_conv_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv_CAST_mul = solver.IntVar(0, 1, 'C1_main_conv_CAST_mul')
C2_main_conv_CAST_mul = solver.IntVar(0, 1, 'C2_main_conv_CAST_mul')
solver.Add( + (1)*main_conv_fixbits + (-1)*main_conv_CAST_mul_fixbits + (-10000)*C1_main_conv_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv_fixbits + (1)*main_conv_CAST_mul_fixbits + (-10000)*C2_main_conv_CAST_mul<=0)    #Shift cost 2
castCostObj =  + (1)*C1_main_conv_CAST_mul
castCostObj +=  + (1)*C2_main_conv_CAST_mul
C3_main_conv_CAST_mul = solver.IntVar(0, 1, 'C3_main_conv_CAST_mul')
C4_main_conv_CAST_mul = solver.IntVar(0, 1, 'C4_main_conv_CAST_mul')
C5_main_conv_CAST_mul = solver.IntVar(0, 1, 'C5_main_conv_CAST_mul')
C6_main_conv_CAST_mul = solver.IntVar(0, 1, 'C6_main_conv_CAST_mul')
C7_main_conv_CAST_mul = solver.IntVar(0, 1, 'C7_main_conv_CAST_mul')
C8_main_conv_CAST_mul = solver.IntVar(0, 1, 'C8_main_conv_CAST_mul')
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_mul_float + (-1)*C3_main_conv_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv_CAST_mul
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_mul_fixp + (-1)*C4_main_conv_CAST_mul<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv_CAST_mul
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_mul_double + (-1)*C5_main_conv_CAST_mul<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv_CAST_mul
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_mul_fixp + (-1)*C6_main_conv_CAST_mul<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv_CAST_mul
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_mul_double + (-1)*C7_main_conv_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv_CAST_mul
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_mul_float + (-1)*C8_main_conv_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv_CAST_mul



#Stuff for double 1.000000e+01
ConstantValue__1_fixbits = solver.IntVar(0, 28, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10020)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10049)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul = fmul double %conv, 1.000000e+01, !taffo.info !29, !taffo.initweight !31, !taffo.constinfo !32
ConstantValue__1_CAST_mul_fixbits = solver.IntVar(0, 28, 'ConstantValue__1_CAST_mul_fixbits')
ConstantValue__1_CAST_mul_fixp = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul_fixp')
ConstantValue__1_CAST_mul_float = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul_float')
ConstantValue__1_CAST_mul_double = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul_double')
solver.Add( + (1)*ConstantValue__1_CAST_mul_fixp + (1)*ConstantValue__1_CAST_mul_float + (1)*ConstantValue__1_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__1_CAST_mul_fixbits + (-10000)*ConstantValue__1_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C1_ConstantValue__1_CAST_mul')
C2_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C2_ConstantValue__1_CAST_mul')
solver.Add( + (1)*ConstantValue__1_fixbits + (-1)*ConstantValue__1_CAST_mul_fixbits + (-10000)*C1_ConstantValue__1_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__1_fixbits + (1)*ConstantValue__1_CAST_mul_fixbits + (-10000)*C2_ConstantValue__1_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__1_CAST_mul
castCostObj +=  + (1)*C2_ConstantValue__1_CAST_mul
C3_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C3_ConstantValue__1_CAST_mul')
C4_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C4_ConstantValue__1_CAST_mul')
C5_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C5_ConstantValue__1_CAST_mul')
C6_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C6_ConstantValue__1_CAST_mul')
C7_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C7_ConstantValue__1_CAST_mul')
C8_ConstantValue__1_CAST_mul = solver.IntVar(0, 1, 'C8_ConstantValue__1_CAST_mul')
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_mul_float + (-1)*C3_ConstantValue__1_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__1_CAST_mul
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_mul_fixp + (-1)*C4_ConstantValue__1_CAST_mul<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__1_CAST_mul
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_mul_double + (-1)*C5_ConstantValue__1_CAST_mul<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__1_CAST_mul
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_mul_fixp + (-1)*C6_ConstantValue__1_CAST_mul<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__1_CAST_mul
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_mul_double + (-1)*C7_ConstantValue__1_CAST_mul<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__1_CAST_mul
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_mul_float + (-1)*C8_ConstantValue__1_CAST_mul<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__1_CAST_mul



#Stuff for   %mul = fmul double %conv, 1.000000e+01, !taffo.info !29, !taffo.initweight !31, !taffo.constinfo !32
main_mul_fixbits = solver.IntVar(0, 21, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_mul_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul_enob
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_CAST_mul_fixp + (-1)*ConstantValue__1_CAST_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_mul_float + (-1)*ConstantValue__1_CAST_mul_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_mul_double + (-1)*ConstantValue__1_CAST_mul_double==0)    #double equality
solver.Add( + (1)*main_conv_CAST_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_mul_double + (-1)*main_mul_double==0)    #double equality
mathCostObj =  + (1.62391)*main_mul_fixp
mathCostObj +=  + (2.64722)*main_mul_float
mathCostObj +=  + (4.02255)*main_mul_double
main_main_mul_enob_1 = solver.IntVar(0, 1, 'main_main_mul_enob_1')
main_main_mul_enob_2 = solver.IntVar(0, 1, 'main_main_mul_enob_2')
solver.Add( + (1)*main_main_mul_enob_1 + (1)*main_main_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul_enob + (-1)*ConstantValue__enob + (-10000)*main_main_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul_enob + (-1)*main_conv_enob + (-10000)*main_main_mul_enob_2<=-3)    #Enob: propagation in product 2



#Stuff for   %conv12 = sitofp i32 10 to double, !taffo.info !33
main_conv12_fixbits = solver.IntVar(0, 28, 'main_conv12_fixbits')
main_conv12_fixp = solver.IntVar(0, 1, 'main_conv12_fixp')
main_conv12_float = solver.IntVar(0, 1, 'main_conv12_float')
main_conv12_double = solver.IntVar(0, 1, 'main_conv12_double')
main_conv12_enob = solver.IntVar(-10000, 10000, 'main_conv12_enob')
solver.Add( + (1)*main_conv12_enob + (-1)*main_conv12_fixbits + (10000)*main_conv12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv12_enob + (10000)*main_conv12_float<=10020)    #Enob constraint for float
solver.Add( + (1)*main_conv12_enob + (10000)*main_conv12_double<=10049)    #Enob constraint for double
solver.Add( + (1)*main_conv12_fixbits + (-10000)*main_conv12_fixp>=-9973)    #Limit the lower number of frac bits28
enobCostObj +=  + (-1)*main_conv12_enob
solver.Add( + (1)*main_conv12_fixp + (1)*main_conv12_float + (1)*main_conv12_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv12_fixbits + (-10000)*main_conv12_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv12_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div = fdiv double %mul, %conv12, !taffo.info !26, !taffo.initweight !35
main_mul_CAST_div_fixbits = solver.IntVar(0, 21, 'main_mul_CAST_div_fixbits')
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



#Constraint for cast for   %div = fdiv double %mul, %conv12, !taffo.info !26, !taffo.initweight !35
main_conv12_CAST_div_fixbits = solver.IntVar(0, 28, 'main_conv12_CAST_div_fixbits')
main_conv12_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv12_CAST_div_fixp')
main_conv12_CAST_div_float = solver.IntVar(0, 1, 'main_conv12_CAST_div_float')
main_conv12_CAST_div_double = solver.IntVar(0, 1, 'main_conv12_CAST_div_double')
solver.Add( + (1)*main_conv12_CAST_div_fixp + (1)*main_conv12_CAST_div_float + (1)*main_conv12_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv12_CAST_div_fixbits + (-10000)*main_conv12_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv12_CAST_div = solver.IntVar(0, 1, 'C1_main_conv12_CAST_div')
C2_main_conv12_CAST_div = solver.IntVar(0, 1, 'C2_main_conv12_CAST_div')
solver.Add( + (1)*main_conv12_fixbits + (-1)*main_conv12_CAST_div_fixbits + (-10000)*C1_main_conv12_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv12_fixbits + (1)*main_conv12_CAST_div_fixbits + (-10000)*C2_main_conv12_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv12_CAST_div
castCostObj +=  + (1)*C2_main_conv12_CAST_div
C3_main_conv12_CAST_div = solver.IntVar(0, 1, 'C3_main_conv12_CAST_div')
C4_main_conv12_CAST_div = solver.IntVar(0, 1, 'C4_main_conv12_CAST_div')
C5_main_conv12_CAST_div = solver.IntVar(0, 1, 'C5_main_conv12_CAST_div')
C6_main_conv12_CAST_div = solver.IntVar(0, 1, 'C6_main_conv12_CAST_div')
C7_main_conv12_CAST_div = solver.IntVar(0, 1, 'C7_main_conv12_CAST_div')
C8_main_conv12_CAST_div = solver.IntVar(0, 1, 'C8_main_conv12_CAST_div')
solver.Add( + (1)*main_conv12_fixp + (1)*main_conv12_CAST_div_float + (-1)*C3_main_conv12_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv12_CAST_div
solver.Add( + (1)*main_conv12_float + (1)*main_conv12_CAST_div_fixp + (-1)*C4_main_conv12_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv12_CAST_div
solver.Add( + (1)*main_conv12_fixp + (1)*main_conv12_CAST_div_double + (-1)*C5_main_conv12_CAST_div<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv12_CAST_div
solver.Add( + (1)*main_conv12_double + (1)*main_conv12_CAST_div_fixp + (-1)*C6_main_conv12_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv12_CAST_div
solver.Add( + (1)*main_conv12_float + (1)*main_conv12_CAST_div_double + (-1)*C7_main_conv12_CAST_div<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv12_CAST_div
solver.Add( + (1)*main_conv12_double + (1)*main_conv12_CAST_div_float + (-1)*C8_main_conv12_CAST_div<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv12_CAST_div



#Stuff for   %div = fdiv double %mul, %conv12, !taffo.info !26, !taffo.initweight !35
main_div_fixbits = solver.IntVar(0, 24, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*main_div_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul_CAST_div_fixp + (-1)*main_conv12_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div_float + (-1)*main_conv12_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div_double + (-1)*main_conv12_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_mul_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div_fixp
mathCostObj +=  + (5.60026)*main_div_float
mathCostObj +=  + (18.3266)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*main_conv12_enob + (-10000)*main_main_div_enob_1<=1030)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_mul_enob + (-10000)*main_main_div_enob_2<=3)    #Enob: propagation in division 2



#Constraint for cast for   store double %div, double* %arrayidx16, align 8, !taffo.info !37, !taffo.initweight !28
main_div_CAST_store_fixbits = solver.IntVar(0, 24, 'main_div_CAST_store_fixbits')
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
solver.Add( + (1)*B_fixp + (-1)*main_div_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B_float + (-1)*main_div_CAST_store_float==0)    #float equality
solver.Add( + (1)*B_double + (-1)*main_div_CAST_store_double==0)    #double equality
solver.Add( + (1)*B_fixbits + (-1)*main_div_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
B_enob_storeENOB = solver.IntVar(-10000, 10000, 'B_enob_storeENOB')
solver.Add( + (1)*B_enob_storeENOB + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob_storeENOB + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob_storeENOB + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_enob_storeENOB + (-1)*main_div_enob<=0)    #Enob constraint ENOB propagation in load/store



#Constraint for cast for   store double %div, double* %arrayidx22, align 8, !taffo.info !37, !taffo.initweight !28
main_div_CAST_store_0_fixbits = solver.IntVar(0, 24, 'main_div_CAST_store_0_fixbits')
main_div_CAST_store_0_fixp = solver.IntVar(0, 1, 'main_div_CAST_store_0_fixp')
main_div_CAST_store_0_float = solver.IntVar(0, 1, 'main_div_CAST_store_0_float')
main_div_CAST_store_0_double = solver.IntVar(0, 1, 'main_div_CAST_store_0_double')
solver.Add( + (1)*main_div_CAST_store_0_fixp + (1)*main_div_CAST_store_0_float + (1)*main_div_CAST_store_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_div_CAST_store_0_fixbits + (-10000)*main_div_CAST_store_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C1_main_div_CAST_store_0')
C2_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C2_main_div_CAST_store_0')
solver.Add( + (1)*main_div_fixbits + (-1)*main_div_CAST_store_0_fixbits + (-10000)*C1_main_div_CAST_store_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_div_fixbits + (1)*main_div_CAST_store_0_fixbits + (-10000)*C2_main_div_CAST_store_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div_CAST_store_0
castCostObj +=  + (1)*C2_main_div_CAST_store_0
C3_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C3_main_div_CAST_store_0')
C4_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C4_main_div_CAST_store_0')
C5_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C5_main_div_CAST_store_0')
C6_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C6_main_div_CAST_store_0')
C7_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C7_main_div_CAST_store_0')
C8_main_div_CAST_store_0 = solver.IntVar(0, 1, 'C8_main_div_CAST_store_0')
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_0_float + (-1)*C3_main_div_CAST_store_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div_CAST_store_0
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_0_fixp + (-1)*C4_main_div_CAST_store_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div_CAST_store_0
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_0_double + (-1)*C5_main_div_CAST_store_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div_CAST_store_0
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_0_fixp + (-1)*C6_main_div_CAST_store_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div_CAST_store_0
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_0_double + (-1)*C7_main_div_CAST_store_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div_CAST_store_0
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_0_float + (-1)*C8_main_div_CAST_store_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div_CAST_store_0
solver.Add( + (1)*A_fixp + (-1)*main_div_CAST_store_0_fixp==0)    #fix equality
solver.Add( + (1)*A_float + (-1)*main_div_CAST_store_0_float==0)    #float equality
solver.Add( + (1)*A_double + (-1)*main_div_CAST_store_0_double==0)    #double equality
solver.Add( + (1)*A_fixbits + (-1)*main_div_CAST_store_0_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
A_enob_storeENOB = solver.IntVar(-10000, 10000, 'A_enob_storeENOB')
solver.Add( + (1)*A_enob_storeENOB + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob_storeENOB + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob_storeENOB + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_enob_storeENOB + (-1)*main_div_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp')
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
main_main_tmp_enob_2 = solver.IntVar(0, 1, 'main_main_tmp_enob_2')
main_main_tmp_enob_3 = solver.IntVar(0, 1, 'main_main_tmp_enob_3')
solver.Add( + (1)*main_main_tmp_enob_1 + (1)*main_main_tmp_enob_2 + (1)*main_main_tmp_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob_storeENOB + (10000)*main_main_tmp_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp1')
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
main_main_tmp1_enob_3 = solver.IntVar(0, 1, 'main_main_tmp1_enob_3')
solver.Add( + (1)*main_main_tmp1_enob_1 + (1)*main_main_tmp1_enob_2 + (1)*main_main_tmp1_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__2_fixbits = solver.IntVar(0, 30, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__3_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__4_fixbits = solver.IntVar(0, 30, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul58 = fmul double 2.000000e+00, %tmp1, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
ConstantValue__4_CAST_mul58_fixbits = solver.IntVar(0, 30, 'ConstantValue__4_CAST_mul58_fixbits')
ConstantValue__4_CAST_mul58_fixp = solver.IntVar(0, 1, 'ConstantValue__4_CAST_mul58_fixp')
ConstantValue__4_CAST_mul58_float = solver.IntVar(0, 1, 'ConstantValue__4_CAST_mul58_float')
ConstantValue__4_CAST_mul58_double = solver.IntVar(0, 1, 'ConstantValue__4_CAST_mul58_double')
solver.Add( + (1)*ConstantValue__4_CAST_mul58_fixp + (1)*ConstantValue__4_CAST_mul58_float + (1)*ConstantValue__4_CAST_mul58_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__4_CAST_mul58_fixbits + (-10000)*ConstantValue__4_CAST_mul58_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C1_ConstantValue__4_CAST_mul58')
C2_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C2_ConstantValue__4_CAST_mul58')
solver.Add( + (1)*ConstantValue__4_fixbits + (-1)*ConstantValue__4_CAST_mul58_fixbits + (-10000)*C1_ConstantValue__4_CAST_mul58<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__4_fixbits + (1)*ConstantValue__4_CAST_mul58_fixbits + (-10000)*C2_ConstantValue__4_CAST_mul58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__4_CAST_mul58
castCostObj +=  + (1)*C2_ConstantValue__4_CAST_mul58
C3_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_mul58')
C4_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_mul58')
C5_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_mul58')
C6_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_mul58')
C7_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_mul58')
C8_ConstantValue__4_CAST_mul58 = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_mul58')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_mul58_float + (-1)*C3_ConstantValue__4_CAST_mul58<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__4_CAST_mul58
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_mul58_fixp + (-1)*C4_ConstantValue__4_CAST_mul58<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__4_CAST_mul58
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_mul58_double + (-1)*C5_ConstantValue__4_CAST_mul58<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__4_CAST_mul58
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_mul58_fixp + (-1)*C6_ConstantValue__4_CAST_mul58<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__4_CAST_mul58
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_mul58_double + (-1)*C7_ConstantValue__4_CAST_mul58<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__4_CAST_mul58
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_mul58_float + (-1)*C8_ConstantValue__4_CAST_mul58<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__4_CAST_mul58



#Constraint for cast for   %mul58 = fmul double 2.000000e+00, %tmp1, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
A_CAST_mul58_fixbits = solver.IntVar(0, 16, 'A_CAST_mul58_fixbits')
A_CAST_mul58_fixp = solver.IntVar(0, 1, 'A_CAST_mul58_fixp')
A_CAST_mul58_float = solver.IntVar(0, 1, 'A_CAST_mul58_float')
A_CAST_mul58_double = solver.IntVar(0, 1, 'A_CAST_mul58_double')
solver.Add( + (1)*A_CAST_mul58_fixp + (1)*A_CAST_mul58_float + (1)*A_CAST_mul58_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_mul58_fixbits + (-10000)*A_CAST_mul58_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_mul58 = solver.IntVar(0, 1, 'C1_A_CAST_mul58')
C2_A_CAST_mul58 = solver.IntVar(0, 1, 'C2_A_CAST_mul58')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_mul58_fixbits + (-10000)*C1_A_CAST_mul58<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_mul58_fixbits + (-10000)*C2_A_CAST_mul58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_mul58
castCostObj +=  + (1)*C2_A_CAST_mul58
C3_A_CAST_mul58 = solver.IntVar(0, 1, 'C3_A_CAST_mul58')
C4_A_CAST_mul58 = solver.IntVar(0, 1, 'C4_A_CAST_mul58')
C5_A_CAST_mul58 = solver.IntVar(0, 1, 'C5_A_CAST_mul58')
C6_A_CAST_mul58 = solver.IntVar(0, 1, 'C6_A_CAST_mul58')
C7_A_CAST_mul58 = solver.IntVar(0, 1, 'C7_A_CAST_mul58')
C8_A_CAST_mul58 = solver.IntVar(0, 1, 'C8_A_CAST_mul58')
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul58_float + (-1)*C3_A_CAST_mul58<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_mul58
solver.Add( + (1)*A_float + (1)*A_CAST_mul58_fixp + (-1)*C4_A_CAST_mul58<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_mul58
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul58_double + (-1)*C5_A_CAST_mul58<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_mul58
solver.Add( + (1)*A_double + (1)*A_CAST_mul58_fixp + (-1)*C6_A_CAST_mul58<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_mul58
solver.Add( + (1)*A_float + (1)*A_CAST_mul58_double + (-1)*C7_A_CAST_mul58<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_mul58
solver.Add( + (1)*A_double + (1)*A_CAST_mul58_float + (-1)*C8_A_CAST_mul58<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_mul58



#Stuff for   %mul58 = fmul double 2.000000e+00, %tmp1, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
main_mul58_fixbits = solver.IntVar(0, 17, 'main_mul58_fixbits')
main_mul58_fixp = solver.IntVar(0, 1, 'main_mul58_fixp')
main_mul58_float = solver.IntVar(0, 1, 'main_mul58_float')
main_mul58_double = solver.IntVar(0, 1, 'main_mul58_double')
main_mul58_enob = solver.IntVar(-10000, 10000, 'main_mul58_enob')
solver.Add( + (1)*main_mul58_enob + (-1)*main_mul58_fixbits + (10000)*main_mul58_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul58_enob + (10000)*main_mul58_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul58_enob + (10000)*main_mul58_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul58_fixbits + (-10000)*main_mul58_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_mul58_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul58_enob
solver.Add( + (1)*main_mul58_fixp + (1)*main_mul58_float + (1)*main_mul58_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul58_fixbits + (-10000)*main_mul58_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__4_CAST_mul58_fixp + (-1)*A_CAST_mul58_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__4_CAST_mul58_float + (-1)*A_CAST_mul58_float==0)    #float equality
solver.Add( + (1)*ConstantValue__4_CAST_mul58_double + (-1)*A_CAST_mul58_double==0)    #double equality
solver.Add( + (1)*ConstantValue__4_CAST_mul58_fixp + (-1)*main_mul58_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__4_CAST_mul58_float + (-1)*main_mul58_float==0)    #float equality
solver.Add( + (1)*ConstantValue__4_CAST_mul58_double + (-1)*main_mul58_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul58_fixp
mathCostObj +=  + (2.64722)*main_mul58_float
mathCostObj +=  + (4.02255)*main_mul58_double
main_main_mul58_enob_1 = solver.IntVar(0, 1, 'main_main_mul58_enob_1')
main_main_mul58_enob_2 = solver.IntVar(0, 1, 'main_main_mul58_enob_2')
solver.Add( + (1)*main_main_mul58_enob_1 + (1)*main_main_mul58_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul58_enob + (-1)*A_enob_memphi_main_tmp1 + (-10000)*main_main_mul58_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul58_enob + (-1)*ConstantValue__2_enob + (-10000)*main_main_mul58_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub59 = fsub double %tmp, %mul58, !taffo.info !46, !taffo.initweight !31
A_CAST_sub59_fixbits = solver.IntVar(0, 16, 'A_CAST_sub59_fixbits')
A_CAST_sub59_fixp = solver.IntVar(0, 1, 'A_CAST_sub59_fixp')
A_CAST_sub59_float = solver.IntVar(0, 1, 'A_CAST_sub59_float')
A_CAST_sub59_double = solver.IntVar(0, 1, 'A_CAST_sub59_double')
solver.Add( + (1)*A_CAST_sub59_fixp + (1)*A_CAST_sub59_float + (1)*A_CAST_sub59_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_sub59_fixbits + (-10000)*A_CAST_sub59_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_sub59 = solver.IntVar(0, 1, 'C1_A_CAST_sub59')
C2_A_CAST_sub59 = solver.IntVar(0, 1, 'C2_A_CAST_sub59')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_sub59_fixbits + (-10000)*C1_A_CAST_sub59<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_sub59_fixbits + (-10000)*C2_A_CAST_sub59<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_sub59
castCostObj +=  + (1)*C2_A_CAST_sub59
C3_A_CAST_sub59 = solver.IntVar(0, 1, 'C3_A_CAST_sub59')
C4_A_CAST_sub59 = solver.IntVar(0, 1, 'C4_A_CAST_sub59')
C5_A_CAST_sub59 = solver.IntVar(0, 1, 'C5_A_CAST_sub59')
C6_A_CAST_sub59 = solver.IntVar(0, 1, 'C6_A_CAST_sub59')
C7_A_CAST_sub59 = solver.IntVar(0, 1, 'C7_A_CAST_sub59')
C8_A_CAST_sub59 = solver.IntVar(0, 1, 'C8_A_CAST_sub59')
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub59_float + (-1)*C3_A_CAST_sub59<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_sub59
solver.Add( + (1)*A_float + (1)*A_CAST_sub59_fixp + (-1)*C4_A_CAST_sub59<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_sub59
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub59_double + (-1)*C5_A_CAST_sub59<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_sub59
solver.Add( + (1)*A_double + (1)*A_CAST_sub59_fixp + (-1)*C6_A_CAST_sub59<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_sub59
solver.Add( + (1)*A_float + (1)*A_CAST_sub59_double + (-1)*C7_A_CAST_sub59<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_sub59
solver.Add( + (1)*A_double + (1)*A_CAST_sub59_float + (-1)*C8_A_CAST_sub59<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_sub59



#Constraint for cast for   %sub59 = fsub double %tmp, %mul58, !taffo.info !46, !taffo.initweight !31
main_mul58_CAST_sub59_fixbits = solver.IntVar(0, 17, 'main_mul58_CAST_sub59_fixbits')
main_mul58_CAST_sub59_fixp = solver.IntVar(0, 1, 'main_mul58_CAST_sub59_fixp')
main_mul58_CAST_sub59_float = solver.IntVar(0, 1, 'main_mul58_CAST_sub59_float')
main_mul58_CAST_sub59_double = solver.IntVar(0, 1, 'main_mul58_CAST_sub59_double')
solver.Add( + (1)*main_mul58_CAST_sub59_fixp + (1)*main_mul58_CAST_sub59_float + (1)*main_mul58_CAST_sub59_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul58_CAST_sub59_fixbits + (-10000)*main_mul58_CAST_sub59_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C1_main_mul58_CAST_sub59')
C2_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C2_main_mul58_CAST_sub59')
solver.Add( + (1)*main_mul58_fixbits + (-1)*main_mul58_CAST_sub59_fixbits + (-10000)*C1_main_mul58_CAST_sub59<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul58_fixbits + (1)*main_mul58_CAST_sub59_fixbits + (-10000)*C2_main_mul58_CAST_sub59<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul58_CAST_sub59
castCostObj +=  + (1)*C2_main_mul58_CAST_sub59
C3_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C3_main_mul58_CAST_sub59')
C4_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C4_main_mul58_CAST_sub59')
C5_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C5_main_mul58_CAST_sub59')
C6_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C6_main_mul58_CAST_sub59')
C7_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C7_main_mul58_CAST_sub59')
C8_main_mul58_CAST_sub59 = solver.IntVar(0, 1, 'C8_main_mul58_CAST_sub59')
solver.Add( + (1)*main_mul58_fixp + (1)*main_mul58_CAST_sub59_float + (-1)*C3_main_mul58_CAST_sub59<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul58_CAST_sub59
solver.Add( + (1)*main_mul58_float + (1)*main_mul58_CAST_sub59_fixp + (-1)*C4_main_mul58_CAST_sub59<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul58_CAST_sub59
solver.Add( + (1)*main_mul58_fixp + (1)*main_mul58_CAST_sub59_double + (-1)*C5_main_mul58_CAST_sub59<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul58_CAST_sub59
solver.Add( + (1)*main_mul58_double + (1)*main_mul58_CAST_sub59_fixp + (-1)*C6_main_mul58_CAST_sub59<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul58_CAST_sub59
solver.Add( + (1)*main_mul58_float + (1)*main_mul58_CAST_sub59_double + (-1)*C7_main_mul58_CAST_sub59<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul58_CAST_sub59
solver.Add( + (1)*main_mul58_double + (1)*main_mul58_CAST_sub59_float + (-1)*C8_main_mul58_CAST_sub59<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul58_CAST_sub59



#Stuff for   %sub59 = fsub double %tmp, %mul58, !taffo.info !46, !taffo.initweight !31
main_sub59_fixbits = solver.IntVar(0, 17, 'main_sub59_fixbits')
main_sub59_fixp = solver.IntVar(0, 1, 'main_sub59_fixp')
main_sub59_float = solver.IntVar(0, 1, 'main_sub59_float')
main_sub59_double = solver.IntVar(0, 1, 'main_sub59_double')
main_sub59_enob = solver.IntVar(-10000, 10000, 'main_sub59_enob')
solver.Add( + (1)*main_sub59_enob + (-1)*main_sub59_fixbits + (10000)*main_sub59_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub59_enob + (10000)*main_sub59_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub59_enob + (10000)*main_sub59_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub59_fixbits + (-10000)*main_sub59_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_sub59_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub59_enob
solver.Add( + (1)*main_sub59_fixp + (1)*main_sub59_float + (1)*main_sub59_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub59_fixbits + (-10000)*main_sub59_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*A_CAST_sub59_fixp + (-1)*main_mul58_CAST_sub59_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub59_float + (-1)*main_mul58_CAST_sub59_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub59_double + (-1)*main_mul58_CAST_sub59_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub59_fixbits + (-1)*main_mul58_CAST_sub59_fixbits==0)    #same fractional bit
solver.Add( + (1)*A_CAST_sub59_fixp + (-1)*main_sub59_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub59_float + (-1)*main_sub59_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub59_double + (-1)*main_sub59_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub59_fixbits + (-1)*main_sub59_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub59_fixp
mathCostObj +=  + (2.33125)*main_sub59_float
mathCostObj +=  + (2.72422)*main_sub59_double
solver.Add( + (1)*main_sub59_enob + (-1)*A_enob_memphi_main_tmp<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub59_enob + (-1)*main_mul58_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp2')
solver.Add( + (1)*A_enob_memphi_main_tmp2 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
main_main_tmp2_enob_3 = solver.IntVar(0, 1, 'main_main_tmp2_enob_3')
solver.Add( + (1)*main_main_tmp2_enob_1 + (1)*main_main_tmp2_enob_2 + (1)*main_main_tmp2_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp2 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add67 = fadd double %sub59, %tmp2, !taffo.info !48, !taffo.initweight !31
main_sub59_CAST_add67_fixbits = solver.IntVar(0, 17, 'main_sub59_CAST_add67_fixbits')
main_sub59_CAST_add67_fixp = solver.IntVar(0, 1, 'main_sub59_CAST_add67_fixp')
main_sub59_CAST_add67_float = solver.IntVar(0, 1, 'main_sub59_CAST_add67_float')
main_sub59_CAST_add67_double = solver.IntVar(0, 1, 'main_sub59_CAST_add67_double')
solver.Add( + (1)*main_sub59_CAST_add67_fixp + (1)*main_sub59_CAST_add67_float + (1)*main_sub59_CAST_add67_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub59_CAST_add67_fixbits + (-10000)*main_sub59_CAST_add67_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C1_main_sub59_CAST_add67')
C2_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C2_main_sub59_CAST_add67')
solver.Add( + (1)*main_sub59_fixbits + (-1)*main_sub59_CAST_add67_fixbits + (-10000)*C1_main_sub59_CAST_add67<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub59_fixbits + (1)*main_sub59_CAST_add67_fixbits + (-10000)*C2_main_sub59_CAST_add67<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub59_CAST_add67
castCostObj +=  + (1)*C2_main_sub59_CAST_add67
C3_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C3_main_sub59_CAST_add67')
C4_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C4_main_sub59_CAST_add67')
C5_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C5_main_sub59_CAST_add67')
C6_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C6_main_sub59_CAST_add67')
C7_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C7_main_sub59_CAST_add67')
C8_main_sub59_CAST_add67 = solver.IntVar(0, 1, 'C8_main_sub59_CAST_add67')
solver.Add( + (1)*main_sub59_fixp + (1)*main_sub59_CAST_add67_float + (-1)*C3_main_sub59_CAST_add67<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub59_CAST_add67
solver.Add( + (1)*main_sub59_float + (1)*main_sub59_CAST_add67_fixp + (-1)*C4_main_sub59_CAST_add67<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub59_CAST_add67
solver.Add( + (1)*main_sub59_fixp + (1)*main_sub59_CAST_add67_double + (-1)*C5_main_sub59_CAST_add67<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub59_CAST_add67
solver.Add( + (1)*main_sub59_double + (1)*main_sub59_CAST_add67_fixp + (-1)*C6_main_sub59_CAST_add67<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub59_CAST_add67
solver.Add( + (1)*main_sub59_float + (1)*main_sub59_CAST_add67_double + (-1)*C7_main_sub59_CAST_add67<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub59_CAST_add67
solver.Add( + (1)*main_sub59_double + (1)*main_sub59_CAST_add67_float + (-1)*C8_main_sub59_CAST_add67<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub59_CAST_add67



#Constraint for cast for   %add67 = fadd double %sub59, %tmp2, !taffo.info !48, !taffo.initweight !31
A_CAST_add67_fixbits = solver.IntVar(0, 16, 'A_CAST_add67_fixbits')
A_CAST_add67_fixp = solver.IntVar(0, 1, 'A_CAST_add67_fixp')
A_CAST_add67_float = solver.IntVar(0, 1, 'A_CAST_add67_float')
A_CAST_add67_double = solver.IntVar(0, 1, 'A_CAST_add67_double')
solver.Add( + (1)*A_CAST_add67_fixp + (1)*A_CAST_add67_float + (1)*A_CAST_add67_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_add67_fixbits + (-10000)*A_CAST_add67_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_add67 = solver.IntVar(0, 1, 'C1_A_CAST_add67')
C2_A_CAST_add67 = solver.IntVar(0, 1, 'C2_A_CAST_add67')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_add67_fixbits + (-10000)*C1_A_CAST_add67<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_add67_fixbits + (-10000)*C2_A_CAST_add67<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_add67
castCostObj +=  + (1)*C2_A_CAST_add67
C3_A_CAST_add67 = solver.IntVar(0, 1, 'C3_A_CAST_add67')
C4_A_CAST_add67 = solver.IntVar(0, 1, 'C4_A_CAST_add67')
C5_A_CAST_add67 = solver.IntVar(0, 1, 'C5_A_CAST_add67')
C6_A_CAST_add67 = solver.IntVar(0, 1, 'C6_A_CAST_add67')
C7_A_CAST_add67 = solver.IntVar(0, 1, 'C7_A_CAST_add67')
C8_A_CAST_add67 = solver.IntVar(0, 1, 'C8_A_CAST_add67')
solver.Add( + (1)*A_fixp + (1)*A_CAST_add67_float + (-1)*C3_A_CAST_add67<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_add67
solver.Add( + (1)*A_float + (1)*A_CAST_add67_fixp + (-1)*C4_A_CAST_add67<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_add67
solver.Add( + (1)*A_fixp + (1)*A_CAST_add67_double + (-1)*C5_A_CAST_add67<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_add67
solver.Add( + (1)*A_double + (1)*A_CAST_add67_fixp + (-1)*C6_A_CAST_add67<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_add67
solver.Add( + (1)*A_float + (1)*A_CAST_add67_double + (-1)*C7_A_CAST_add67<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_add67
solver.Add( + (1)*A_double + (1)*A_CAST_add67_float + (-1)*C8_A_CAST_add67<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_add67



#Stuff for   %add67 = fadd double %sub59, %tmp2, !taffo.info !48, !taffo.initweight !31
main_add67_fixbits = solver.IntVar(0, 16, 'main_add67_fixbits')
main_add67_fixp = solver.IntVar(0, 1, 'main_add67_fixp')
main_add67_float = solver.IntVar(0, 1, 'main_add67_float')
main_add67_double = solver.IntVar(0, 1, 'main_add67_double')
main_add67_enob = solver.IntVar(-10000, 10000, 'main_add67_enob')
solver.Add( + (1)*main_add67_enob + (-1)*main_add67_fixbits + (10000)*main_add67_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add67_enob + (10000)*main_add67_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add67_enob + (10000)*main_add67_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add67_fixbits + (-10000)*main_add67_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_add67_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add67_enob
solver.Add( + (1)*main_add67_fixp + (1)*main_add67_float + (1)*main_add67_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add67_fixbits + (-10000)*main_add67_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub59_CAST_add67_fixp + (-1)*A_CAST_add67_fixp==0)    #fix equality
solver.Add( + (1)*main_sub59_CAST_add67_float + (-1)*A_CAST_add67_float==0)    #float equality
solver.Add( + (1)*main_sub59_CAST_add67_double + (-1)*A_CAST_add67_double==0)    #double equality
solver.Add( + (1)*main_sub59_CAST_add67_fixbits + (-1)*A_CAST_add67_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub59_CAST_add67_fixp + (-1)*main_add67_fixp==0)    #fix equality
solver.Add( + (1)*main_sub59_CAST_add67_float + (-1)*main_add67_float==0)    #float equality
solver.Add( + (1)*main_sub59_CAST_add67_double + (-1)*main_add67_double==0)    #double equality
solver.Add( + (1)*main_sub59_CAST_add67_fixbits + (-1)*main_add67_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add67_fixp
mathCostObj +=  + (2.33125)*main_add67_float
mathCostObj +=  + (2.72422)*main_add67_double
solver.Add( + (1)*main_add67_enob + (-1)*main_sub59_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add67_enob + (-1)*A_enob_memphi_main_tmp2<=0)    #Enob propagation in sum second addend



#Stuff for double 1.250000e-01
ConstantValue__5_fixbits = solver.IntVar(0, 31, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__6_fixbits = solver.IntVar(0, 31, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__7_fixbits = solver.IntVar(0, 31, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul68 = fmul double 1.250000e-01, %add67, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
ConstantValue__7_CAST_mul68_fixbits = solver.IntVar(0, 31, 'ConstantValue__7_CAST_mul68_fixbits')
ConstantValue__7_CAST_mul68_fixp = solver.IntVar(0, 1, 'ConstantValue__7_CAST_mul68_fixp')
ConstantValue__7_CAST_mul68_float = solver.IntVar(0, 1, 'ConstantValue__7_CAST_mul68_float')
ConstantValue__7_CAST_mul68_double = solver.IntVar(0, 1, 'ConstantValue__7_CAST_mul68_double')
solver.Add( + (1)*ConstantValue__7_CAST_mul68_fixp + (1)*ConstantValue__7_CAST_mul68_float + (1)*ConstantValue__7_CAST_mul68_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__7_CAST_mul68_fixbits + (-10000)*ConstantValue__7_CAST_mul68_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C1_ConstantValue__7_CAST_mul68')
C2_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C2_ConstantValue__7_CAST_mul68')
solver.Add( + (1)*ConstantValue__7_fixbits + (-1)*ConstantValue__7_CAST_mul68_fixbits + (-10000)*C1_ConstantValue__7_CAST_mul68<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__7_fixbits + (1)*ConstantValue__7_CAST_mul68_fixbits + (-10000)*C2_ConstantValue__7_CAST_mul68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__7_CAST_mul68
castCostObj +=  + (1)*C2_ConstantValue__7_CAST_mul68
C3_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C3_ConstantValue__7_CAST_mul68')
C4_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C4_ConstantValue__7_CAST_mul68')
C5_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C5_ConstantValue__7_CAST_mul68')
C6_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C6_ConstantValue__7_CAST_mul68')
C7_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C7_ConstantValue__7_CAST_mul68')
C8_ConstantValue__7_CAST_mul68 = solver.IntVar(0, 1, 'C8_ConstantValue__7_CAST_mul68')
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_mul68_float + (-1)*C3_ConstantValue__7_CAST_mul68<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__7_CAST_mul68
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_mul68_fixp + (-1)*C4_ConstantValue__7_CAST_mul68<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__7_CAST_mul68
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_mul68_double + (-1)*C5_ConstantValue__7_CAST_mul68<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__7_CAST_mul68
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_mul68_fixp + (-1)*C6_ConstantValue__7_CAST_mul68<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__7_CAST_mul68
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_mul68_double + (-1)*C7_ConstantValue__7_CAST_mul68<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__7_CAST_mul68
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_mul68_float + (-1)*C8_ConstantValue__7_CAST_mul68<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__7_CAST_mul68



#Constraint for cast for   %mul68 = fmul double 1.250000e-01, %add67, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
main_add67_CAST_mul68_fixbits = solver.IntVar(0, 16, 'main_add67_CAST_mul68_fixbits')
main_add67_CAST_mul68_fixp = solver.IntVar(0, 1, 'main_add67_CAST_mul68_fixp')
main_add67_CAST_mul68_float = solver.IntVar(0, 1, 'main_add67_CAST_mul68_float')
main_add67_CAST_mul68_double = solver.IntVar(0, 1, 'main_add67_CAST_mul68_double')
solver.Add( + (1)*main_add67_CAST_mul68_fixp + (1)*main_add67_CAST_mul68_float + (1)*main_add67_CAST_mul68_double==1)    #exactly 1 type
solver.Add( + (1)*main_add67_CAST_mul68_fixbits + (-10000)*main_add67_CAST_mul68_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C1_main_add67_CAST_mul68')
C2_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C2_main_add67_CAST_mul68')
solver.Add( + (1)*main_add67_fixbits + (-1)*main_add67_CAST_mul68_fixbits + (-10000)*C1_main_add67_CAST_mul68<=0)    #Shift cost 1
solver.Add( + (-1)*main_add67_fixbits + (1)*main_add67_CAST_mul68_fixbits + (-10000)*C2_main_add67_CAST_mul68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add67_CAST_mul68
castCostObj +=  + (1)*C2_main_add67_CAST_mul68
C3_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C3_main_add67_CAST_mul68')
C4_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C4_main_add67_CAST_mul68')
C5_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C5_main_add67_CAST_mul68')
C6_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C6_main_add67_CAST_mul68')
C7_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C7_main_add67_CAST_mul68')
C8_main_add67_CAST_mul68 = solver.IntVar(0, 1, 'C8_main_add67_CAST_mul68')
solver.Add( + (1)*main_add67_fixp + (1)*main_add67_CAST_mul68_float + (-1)*C3_main_add67_CAST_mul68<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add67_CAST_mul68
solver.Add( + (1)*main_add67_float + (1)*main_add67_CAST_mul68_fixp + (-1)*C4_main_add67_CAST_mul68<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add67_CAST_mul68
solver.Add( + (1)*main_add67_fixp + (1)*main_add67_CAST_mul68_double + (-1)*C5_main_add67_CAST_mul68<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add67_CAST_mul68
solver.Add( + (1)*main_add67_double + (1)*main_add67_CAST_mul68_fixp + (-1)*C6_main_add67_CAST_mul68<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add67_CAST_mul68
solver.Add( + (1)*main_add67_float + (1)*main_add67_CAST_mul68_double + (-1)*C7_main_add67_CAST_mul68<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add67_CAST_mul68
solver.Add( + (1)*main_add67_double + (1)*main_add67_CAST_mul68_float + (-1)*C8_main_add67_CAST_mul68<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add67_CAST_mul68



#Stuff for   %mul68 = fmul double 1.250000e-01, %add67, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
main_mul68_fixbits = solver.IntVar(0, 19, 'main_mul68_fixbits')
main_mul68_fixp = solver.IntVar(0, 1, 'main_mul68_fixp')
main_mul68_float = solver.IntVar(0, 1, 'main_mul68_float')
main_mul68_double = solver.IntVar(0, 1, 'main_mul68_double')
main_mul68_enob = solver.IntVar(-10000, 10000, 'main_mul68_enob')
solver.Add( + (1)*main_mul68_enob + (-1)*main_mul68_fixbits + (10000)*main_mul68_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul68_enob + (10000)*main_mul68_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul68_enob + (10000)*main_mul68_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul68_fixbits + (-10000)*main_mul68_fixp>=-9982)    #Limit the lower number of frac bits19
solver.Add( + (1)*main_mul68_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul68_enob
solver.Add( + (1)*main_mul68_fixp + (1)*main_mul68_float + (1)*main_mul68_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul68_fixbits + (-10000)*main_mul68_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__7_CAST_mul68_fixp + (-1)*main_add67_CAST_mul68_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__7_CAST_mul68_float + (-1)*main_add67_CAST_mul68_float==0)    #float equality
solver.Add( + (1)*ConstantValue__7_CAST_mul68_double + (-1)*main_add67_CAST_mul68_double==0)    #double equality
solver.Add( + (1)*ConstantValue__7_CAST_mul68_fixp + (-1)*main_mul68_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__7_CAST_mul68_float + (-1)*main_mul68_float==0)    #float equality
solver.Add( + (1)*ConstantValue__7_CAST_mul68_double + (-1)*main_mul68_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul68_fixp
mathCostObj +=  + (2.64722)*main_mul68_float
mathCostObj +=  + (4.02255)*main_mul68_double
main_main_mul68_enob_1 = solver.IntVar(0, 1, 'main_main_mul68_enob_1')
main_main_mul68_enob_2 = solver.IntVar(0, 1, 'main_main_mul68_enob_2')
solver.Add( + (1)*main_main_mul68_enob_1 + (1)*main_main_mul68_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul68_enob + (-1)*main_add67_enob + (-10000)*main_main_mul68_enob_1<=3)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul68_enob + (-1)*ConstantValue__5_enob + (-10000)*main_main_mul68_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp3')
solver.Add( + (1)*A_enob_memphi_main_tmp3 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp3 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp3_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp4')
solver.Add( + (1)*A_enob_memphi_main_tmp4 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp4 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp4_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__8_fixbits = solver.IntVar(0, 30, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__9_fixbits = solver.IntVar(0, 30, 'ConstantValue__9_fixbits')
ConstantValue__9_fixp = solver.IntVar(0, 1, 'ConstantValue__9_fixp')
ConstantValue__9_float = solver.IntVar(0, 1, 'ConstantValue__9_float')
ConstantValue__9_double = solver.IntVar(0, 1, 'ConstantValue__9_double')
ConstantValue__9_enob = solver.IntVar(-10000, 10000, 'ConstantValue__9_enob')
solver.Add( + (1)*ConstantValue__9_enob + (-1)*ConstantValue__9_fixbits + (10000)*ConstantValue__9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_float + (1)*ConstantValue__9_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__10_fixbits = solver.IntVar(0, 30, 'ConstantValue__10_fixbits')
ConstantValue__10_fixp = solver.IntVar(0, 1, 'ConstantValue__10_fixp')
ConstantValue__10_float = solver.IntVar(0, 1, 'ConstantValue__10_float')
ConstantValue__10_double = solver.IntVar(0, 1, 'ConstantValue__10_double')
ConstantValue__10_enob = solver.IntVar(-10000, 10000, 'ConstantValue__10_enob')
solver.Add( + (1)*ConstantValue__10_enob + (-1)*ConstantValue__10_fixbits + (10000)*ConstantValue__10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_float + (1)*ConstantValue__10_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul82 = fmul double 2.000000e+00, %tmp4, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
ConstantValue__10_CAST_mul82_fixbits = solver.IntVar(0, 30, 'ConstantValue__10_CAST_mul82_fixbits')
ConstantValue__10_CAST_mul82_fixp = solver.IntVar(0, 1, 'ConstantValue__10_CAST_mul82_fixp')
ConstantValue__10_CAST_mul82_float = solver.IntVar(0, 1, 'ConstantValue__10_CAST_mul82_float')
ConstantValue__10_CAST_mul82_double = solver.IntVar(0, 1, 'ConstantValue__10_CAST_mul82_double')
solver.Add( + (1)*ConstantValue__10_CAST_mul82_fixp + (1)*ConstantValue__10_CAST_mul82_float + (1)*ConstantValue__10_CAST_mul82_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__10_CAST_mul82_fixbits + (-10000)*ConstantValue__10_CAST_mul82_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C1_ConstantValue__10_CAST_mul82')
C2_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C2_ConstantValue__10_CAST_mul82')
solver.Add( + (1)*ConstantValue__10_fixbits + (-1)*ConstantValue__10_CAST_mul82_fixbits + (-10000)*C1_ConstantValue__10_CAST_mul82<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__10_fixbits + (1)*ConstantValue__10_CAST_mul82_fixbits + (-10000)*C2_ConstantValue__10_CAST_mul82<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__10_CAST_mul82
castCostObj +=  + (1)*C2_ConstantValue__10_CAST_mul82
C3_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C3_ConstantValue__10_CAST_mul82')
C4_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C4_ConstantValue__10_CAST_mul82')
C5_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C5_ConstantValue__10_CAST_mul82')
C6_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C6_ConstantValue__10_CAST_mul82')
C7_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C7_ConstantValue__10_CAST_mul82')
C8_ConstantValue__10_CAST_mul82 = solver.IntVar(0, 1, 'C8_ConstantValue__10_CAST_mul82')
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_CAST_mul82_float + (-1)*C3_ConstantValue__10_CAST_mul82<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__10_CAST_mul82
solver.Add( + (1)*ConstantValue__10_float + (1)*ConstantValue__10_CAST_mul82_fixp + (-1)*C4_ConstantValue__10_CAST_mul82<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__10_CAST_mul82
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_CAST_mul82_double + (-1)*C5_ConstantValue__10_CAST_mul82<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__10_CAST_mul82
solver.Add( + (1)*ConstantValue__10_double + (1)*ConstantValue__10_CAST_mul82_fixp + (-1)*C6_ConstantValue__10_CAST_mul82<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__10_CAST_mul82
solver.Add( + (1)*ConstantValue__10_float + (1)*ConstantValue__10_CAST_mul82_double + (-1)*C7_ConstantValue__10_CAST_mul82<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__10_CAST_mul82
solver.Add( + (1)*ConstantValue__10_double + (1)*ConstantValue__10_CAST_mul82_float + (-1)*C8_ConstantValue__10_CAST_mul82<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__10_CAST_mul82



#Constraint for cast for   %mul82 = fmul double 2.000000e+00, %tmp4, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
A_CAST_mul82_fixbits = solver.IntVar(0, 16, 'A_CAST_mul82_fixbits')
A_CAST_mul82_fixp = solver.IntVar(0, 1, 'A_CAST_mul82_fixp')
A_CAST_mul82_float = solver.IntVar(0, 1, 'A_CAST_mul82_float')
A_CAST_mul82_double = solver.IntVar(0, 1, 'A_CAST_mul82_double')
solver.Add( + (1)*A_CAST_mul82_fixp + (1)*A_CAST_mul82_float + (1)*A_CAST_mul82_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_mul82_fixbits + (-10000)*A_CAST_mul82_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_mul82 = solver.IntVar(0, 1, 'C1_A_CAST_mul82')
C2_A_CAST_mul82 = solver.IntVar(0, 1, 'C2_A_CAST_mul82')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_mul82_fixbits + (-10000)*C1_A_CAST_mul82<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_mul82_fixbits + (-10000)*C2_A_CAST_mul82<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_mul82
castCostObj +=  + (1)*C2_A_CAST_mul82
C3_A_CAST_mul82 = solver.IntVar(0, 1, 'C3_A_CAST_mul82')
C4_A_CAST_mul82 = solver.IntVar(0, 1, 'C4_A_CAST_mul82')
C5_A_CAST_mul82 = solver.IntVar(0, 1, 'C5_A_CAST_mul82')
C6_A_CAST_mul82 = solver.IntVar(0, 1, 'C6_A_CAST_mul82')
C7_A_CAST_mul82 = solver.IntVar(0, 1, 'C7_A_CAST_mul82')
C8_A_CAST_mul82 = solver.IntVar(0, 1, 'C8_A_CAST_mul82')
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul82_float + (-1)*C3_A_CAST_mul82<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_mul82
solver.Add( + (1)*A_float + (1)*A_CAST_mul82_fixp + (-1)*C4_A_CAST_mul82<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_mul82
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul82_double + (-1)*C5_A_CAST_mul82<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_mul82
solver.Add( + (1)*A_double + (1)*A_CAST_mul82_fixp + (-1)*C6_A_CAST_mul82<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_mul82
solver.Add( + (1)*A_float + (1)*A_CAST_mul82_double + (-1)*C7_A_CAST_mul82<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_mul82
solver.Add( + (1)*A_double + (1)*A_CAST_mul82_float + (-1)*C8_A_CAST_mul82<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_mul82



#Stuff for   %mul82 = fmul double 2.000000e+00, %tmp4, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
main_mul82_fixbits = solver.IntVar(0, 17, 'main_mul82_fixbits')
main_mul82_fixp = solver.IntVar(0, 1, 'main_mul82_fixp')
main_mul82_float = solver.IntVar(0, 1, 'main_mul82_float')
main_mul82_double = solver.IntVar(0, 1, 'main_mul82_double')
main_mul82_enob = solver.IntVar(-10000, 10000, 'main_mul82_enob')
solver.Add( + (1)*main_mul82_enob + (-1)*main_mul82_fixbits + (10000)*main_mul82_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul82_enob + (10000)*main_mul82_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul82_enob + (10000)*main_mul82_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul82_fixbits + (-10000)*main_mul82_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_mul82_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul82_enob
solver.Add( + (1)*main_mul82_fixp + (1)*main_mul82_float + (1)*main_mul82_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul82_fixbits + (-10000)*main_mul82_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__10_CAST_mul82_fixp + (-1)*A_CAST_mul82_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__10_CAST_mul82_float + (-1)*A_CAST_mul82_float==0)    #float equality
solver.Add( + (1)*ConstantValue__10_CAST_mul82_double + (-1)*A_CAST_mul82_double==0)    #double equality
solver.Add( + (1)*ConstantValue__10_CAST_mul82_fixp + (-1)*main_mul82_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__10_CAST_mul82_float + (-1)*main_mul82_float==0)    #float equality
solver.Add( + (1)*ConstantValue__10_CAST_mul82_double + (-1)*main_mul82_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul82_fixp
mathCostObj +=  + (2.64722)*main_mul82_float
mathCostObj +=  + (4.02255)*main_mul82_double
main_main_mul82_enob_1 = solver.IntVar(0, 1, 'main_main_mul82_enob_1')
main_main_mul82_enob_2 = solver.IntVar(0, 1, 'main_main_mul82_enob_2')
solver.Add( + (1)*main_main_mul82_enob_1 + (1)*main_main_mul82_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul82_enob + (-1)*A_enob_memphi_main_tmp4 + (-10000)*main_main_mul82_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul82_enob + (-1)*ConstantValue__8_enob + (-10000)*main_main_mul82_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub83 = fsub double %tmp3, %mul82, !taffo.info !46, !taffo.initweight !31
A_CAST_sub83_fixbits = solver.IntVar(0, 16, 'A_CAST_sub83_fixbits')
A_CAST_sub83_fixp = solver.IntVar(0, 1, 'A_CAST_sub83_fixp')
A_CAST_sub83_float = solver.IntVar(0, 1, 'A_CAST_sub83_float')
A_CAST_sub83_double = solver.IntVar(0, 1, 'A_CAST_sub83_double')
solver.Add( + (1)*A_CAST_sub83_fixp + (1)*A_CAST_sub83_float + (1)*A_CAST_sub83_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_sub83_fixbits + (-10000)*A_CAST_sub83_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_sub83 = solver.IntVar(0, 1, 'C1_A_CAST_sub83')
C2_A_CAST_sub83 = solver.IntVar(0, 1, 'C2_A_CAST_sub83')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_sub83_fixbits + (-10000)*C1_A_CAST_sub83<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_sub83_fixbits + (-10000)*C2_A_CAST_sub83<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_sub83
castCostObj +=  + (1)*C2_A_CAST_sub83
C3_A_CAST_sub83 = solver.IntVar(0, 1, 'C3_A_CAST_sub83')
C4_A_CAST_sub83 = solver.IntVar(0, 1, 'C4_A_CAST_sub83')
C5_A_CAST_sub83 = solver.IntVar(0, 1, 'C5_A_CAST_sub83')
C6_A_CAST_sub83 = solver.IntVar(0, 1, 'C6_A_CAST_sub83')
C7_A_CAST_sub83 = solver.IntVar(0, 1, 'C7_A_CAST_sub83')
C8_A_CAST_sub83 = solver.IntVar(0, 1, 'C8_A_CAST_sub83')
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub83_float + (-1)*C3_A_CAST_sub83<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_sub83
solver.Add( + (1)*A_float + (1)*A_CAST_sub83_fixp + (-1)*C4_A_CAST_sub83<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_sub83
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub83_double + (-1)*C5_A_CAST_sub83<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_sub83
solver.Add( + (1)*A_double + (1)*A_CAST_sub83_fixp + (-1)*C6_A_CAST_sub83<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_sub83
solver.Add( + (1)*A_float + (1)*A_CAST_sub83_double + (-1)*C7_A_CAST_sub83<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_sub83
solver.Add( + (1)*A_double + (1)*A_CAST_sub83_float + (-1)*C8_A_CAST_sub83<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_sub83



#Constraint for cast for   %sub83 = fsub double %tmp3, %mul82, !taffo.info !46, !taffo.initweight !31
main_mul82_CAST_sub83_fixbits = solver.IntVar(0, 17, 'main_mul82_CAST_sub83_fixbits')
main_mul82_CAST_sub83_fixp = solver.IntVar(0, 1, 'main_mul82_CAST_sub83_fixp')
main_mul82_CAST_sub83_float = solver.IntVar(0, 1, 'main_mul82_CAST_sub83_float')
main_mul82_CAST_sub83_double = solver.IntVar(0, 1, 'main_mul82_CAST_sub83_double')
solver.Add( + (1)*main_mul82_CAST_sub83_fixp + (1)*main_mul82_CAST_sub83_float + (1)*main_mul82_CAST_sub83_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul82_CAST_sub83_fixbits + (-10000)*main_mul82_CAST_sub83_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C1_main_mul82_CAST_sub83')
C2_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C2_main_mul82_CAST_sub83')
solver.Add( + (1)*main_mul82_fixbits + (-1)*main_mul82_CAST_sub83_fixbits + (-10000)*C1_main_mul82_CAST_sub83<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul82_fixbits + (1)*main_mul82_CAST_sub83_fixbits + (-10000)*C2_main_mul82_CAST_sub83<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul82_CAST_sub83
castCostObj +=  + (1)*C2_main_mul82_CAST_sub83
C3_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C3_main_mul82_CAST_sub83')
C4_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C4_main_mul82_CAST_sub83')
C5_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C5_main_mul82_CAST_sub83')
C6_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C6_main_mul82_CAST_sub83')
C7_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C7_main_mul82_CAST_sub83')
C8_main_mul82_CAST_sub83 = solver.IntVar(0, 1, 'C8_main_mul82_CAST_sub83')
solver.Add( + (1)*main_mul82_fixp + (1)*main_mul82_CAST_sub83_float + (-1)*C3_main_mul82_CAST_sub83<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul82_CAST_sub83
solver.Add( + (1)*main_mul82_float + (1)*main_mul82_CAST_sub83_fixp + (-1)*C4_main_mul82_CAST_sub83<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul82_CAST_sub83
solver.Add( + (1)*main_mul82_fixp + (1)*main_mul82_CAST_sub83_double + (-1)*C5_main_mul82_CAST_sub83<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul82_CAST_sub83
solver.Add( + (1)*main_mul82_double + (1)*main_mul82_CAST_sub83_fixp + (-1)*C6_main_mul82_CAST_sub83<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul82_CAST_sub83
solver.Add( + (1)*main_mul82_float + (1)*main_mul82_CAST_sub83_double + (-1)*C7_main_mul82_CAST_sub83<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul82_CAST_sub83
solver.Add( + (1)*main_mul82_double + (1)*main_mul82_CAST_sub83_float + (-1)*C8_main_mul82_CAST_sub83<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul82_CAST_sub83



#Stuff for   %sub83 = fsub double %tmp3, %mul82, !taffo.info !46, !taffo.initweight !31
main_sub83_fixbits = solver.IntVar(0, 17, 'main_sub83_fixbits')
main_sub83_fixp = solver.IntVar(0, 1, 'main_sub83_fixp')
main_sub83_float = solver.IntVar(0, 1, 'main_sub83_float')
main_sub83_double = solver.IntVar(0, 1, 'main_sub83_double')
main_sub83_enob = solver.IntVar(-10000, 10000, 'main_sub83_enob')
solver.Add( + (1)*main_sub83_enob + (-1)*main_sub83_fixbits + (10000)*main_sub83_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub83_enob + (10000)*main_sub83_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub83_enob + (10000)*main_sub83_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub83_fixbits + (-10000)*main_sub83_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_sub83_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub83_enob
solver.Add( + (1)*main_sub83_fixp + (1)*main_sub83_float + (1)*main_sub83_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub83_fixbits + (-10000)*main_sub83_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*A_CAST_sub83_fixp + (-1)*main_mul82_CAST_sub83_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub83_float + (-1)*main_mul82_CAST_sub83_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub83_double + (-1)*main_mul82_CAST_sub83_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub83_fixbits + (-1)*main_mul82_CAST_sub83_fixbits==0)    #same fractional bit
solver.Add( + (1)*A_CAST_sub83_fixp + (-1)*main_sub83_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub83_float + (-1)*main_sub83_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub83_double + (-1)*main_sub83_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub83_fixbits + (-1)*main_sub83_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub83_fixp
mathCostObj +=  + (2.33125)*main_sub83_float
mathCostObj +=  + (2.72422)*main_sub83_double
solver.Add( + (1)*main_sub83_enob + (-1)*A_enob_memphi_main_tmp3<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub83_enob + (-1)*main_mul82_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp5')
solver.Add( + (1)*A_enob_memphi_main_tmp5 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp5 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp5_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add91 = fadd double %sub83, %tmp5, !taffo.info !48, !taffo.initweight !31
main_sub83_CAST_add91_fixbits = solver.IntVar(0, 17, 'main_sub83_CAST_add91_fixbits')
main_sub83_CAST_add91_fixp = solver.IntVar(0, 1, 'main_sub83_CAST_add91_fixp')
main_sub83_CAST_add91_float = solver.IntVar(0, 1, 'main_sub83_CAST_add91_float')
main_sub83_CAST_add91_double = solver.IntVar(0, 1, 'main_sub83_CAST_add91_double')
solver.Add( + (1)*main_sub83_CAST_add91_fixp + (1)*main_sub83_CAST_add91_float + (1)*main_sub83_CAST_add91_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub83_CAST_add91_fixbits + (-10000)*main_sub83_CAST_add91_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C1_main_sub83_CAST_add91')
C2_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C2_main_sub83_CAST_add91')
solver.Add( + (1)*main_sub83_fixbits + (-1)*main_sub83_CAST_add91_fixbits + (-10000)*C1_main_sub83_CAST_add91<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub83_fixbits + (1)*main_sub83_CAST_add91_fixbits + (-10000)*C2_main_sub83_CAST_add91<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub83_CAST_add91
castCostObj +=  + (1)*C2_main_sub83_CAST_add91
C3_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C3_main_sub83_CAST_add91')
C4_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C4_main_sub83_CAST_add91')
C5_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C5_main_sub83_CAST_add91')
C6_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C6_main_sub83_CAST_add91')
C7_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C7_main_sub83_CAST_add91')
C8_main_sub83_CAST_add91 = solver.IntVar(0, 1, 'C8_main_sub83_CAST_add91')
solver.Add( + (1)*main_sub83_fixp + (1)*main_sub83_CAST_add91_float + (-1)*C3_main_sub83_CAST_add91<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub83_CAST_add91
solver.Add( + (1)*main_sub83_float + (1)*main_sub83_CAST_add91_fixp + (-1)*C4_main_sub83_CAST_add91<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub83_CAST_add91
solver.Add( + (1)*main_sub83_fixp + (1)*main_sub83_CAST_add91_double + (-1)*C5_main_sub83_CAST_add91<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub83_CAST_add91
solver.Add( + (1)*main_sub83_double + (1)*main_sub83_CAST_add91_fixp + (-1)*C6_main_sub83_CAST_add91<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub83_CAST_add91
solver.Add( + (1)*main_sub83_float + (1)*main_sub83_CAST_add91_double + (-1)*C7_main_sub83_CAST_add91<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub83_CAST_add91
solver.Add( + (1)*main_sub83_double + (1)*main_sub83_CAST_add91_float + (-1)*C8_main_sub83_CAST_add91<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub83_CAST_add91



#Constraint for cast for   %add91 = fadd double %sub83, %tmp5, !taffo.info !48, !taffo.initweight !31
A_CAST_add91_fixbits = solver.IntVar(0, 16, 'A_CAST_add91_fixbits')
A_CAST_add91_fixp = solver.IntVar(0, 1, 'A_CAST_add91_fixp')
A_CAST_add91_float = solver.IntVar(0, 1, 'A_CAST_add91_float')
A_CAST_add91_double = solver.IntVar(0, 1, 'A_CAST_add91_double')
solver.Add( + (1)*A_CAST_add91_fixp + (1)*A_CAST_add91_float + (1)*A_CAST_add91_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_add91_fixbits + (-10000)*A_CAST_add91_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_add91 = solver.IntVar(0, 1, 'C1_A_CAST_add91')
C2_A_CAST_add91 = solver.IntVar(0, 1, 'C2_A_CAST_add91')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_add91_fixbits + (-10000)*C1_A_CAST_add91<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_add91_fixbits + (-10000)*C2_A_CAST_add91<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_add91
castCostObj +=  + (1)*C2_A_CAST_add91
C3_A_CAST_add91 = solver.IntVar(0, 1, 'C3_A_CAST_add91')
C4_A_CAST_add91 = solver.IntVar(0, 1, 'C4_A_CAST_add91')
C5_A_CAST_add91 = solver.IntVar(0, 1, 'C5_A_CAST_add91')
C6_A_CAST_add91 = solver.IntVar(0, 1, 'C6_A_CAST_add91')
C7_A_CAST_add91 = solver.IntVar(0, 1, 'C7_A_CAST_add91')
C8_A_CAST_add91 = solver.IntVar(0, 1, 'C8_A_CAST_add91')
solver.Add( + (1)*A_fixp + (1)*A_CAST_add91_float + (-1)*C3_A_CAST_add91<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_add91
solver.Add( + (1)*A_float + (1)*A_CAST_add91_fixp + (-1)*C4_A_CAST_add91<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_add91
solver.Add( + (1)*A_fixp + (1)*A_CAST_add91_double + (-1)*C5_A_CAST_add91<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_add91
solver.Add( + (1)*A_double + (1)*A_CAST_add91_fixp + (-1)*C6_A_CAST_add91<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_add91
solver.Add( + (1)*A_float + (1)*A_CAST_add91_double + (-1)*C7_A_CAST_add91<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_add91
solver.Add( + (1)*A_double + (1)*A_CAST_add91_float + (-1)*C8_A_CAST_add91<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_add91



#Stuff for   %add91 = fadd double %sub83, %tmp5, !taffo.info !48, !taffo.initweight !31
main_add91_fixbits = solver.IntVar(0, 16, 'main_add91_fixbits')
main_add91_fixp = solver.IntVar(0, 1, 'main_add91_fixp')
main_add91_float = solver.IntVar(0, 1, 'main_add91_float')
main_add91_double = solver.IntVar(0, 1, 'main_add91_double')
main_add91_enob = solver.IntVar(-10000, 10000, 'main_add91_enob')
solver.Add( + (1)*main_add91_enob + (-1)*main_add91_fixbits + (10000)*main_add91_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add91_enob + (10000)*main_add91_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add91_enob + (10000)*main_add91_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add91_fixbits + (-10000)*main_add91_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_add91_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add91_enob
solver.Add( + (1)*main_add91_fixp + (1)*main_add91_float + (1)*main_add91_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add91_fixbits + (-10000)*main_add91_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub83_CAST_add91_fixp + (-1)*A_CAST_add91_fixp==0)    #fix equality
solver.Add( + (1)*main_sub83_CAST_add91_float + (-1)*A_CAST_add91_float==0)    #float equality
solver.Add( + (1)*main_sub83_CAST_add91_double + (-1)*A_CAST_add91_double==0)    #double equality
solver.Add( + (1)*main_sub83_CAST_add91_fixbits + (-1)*A_CAST_add91_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub83_CAST_add91_fixp + (-1)*main_add91_fixp==0)    #fix equality
solver.Add( + (1)*main_sub83_CAST_add91_float + (-1)*main_add91_float==0)    #float equality
solver.Add( + (1)*main_sub83_CAST_add91_double + (-1)*main_add91_double==0)    #double equality
solver.Add( + (1)*main_sub83_CAST_add91_fixbits + (-1)*main_add91_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add91_fixp
mathCostObj +=  + (2.33125)*main_add91_float
mathCostObj +=  + (2.72422)*main_add91_double
solver.Add( + (1)*main_add91_enob + (-1)*main_sub83_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add91_enob + (-1)*A_enob_memphi_main_tmp5<=0)    #Enob propagation in sum second addend



#Stuff for double 1.250000e-01
ConstantValue__11_fixbits = solver.IntVar(0, 31, 'ConstantValue__11_fixbits')
ConstantValue__11_fixp = solver.IntVar(0, 1, 'ConstantValue__11_fixp')
ConstantValue__11_float = solver.IntVar(0, 1, 'ConstantValue__11_float')
ConstantValue__11_double = solver.IntVar(0, 1, 'ConstantValue__11_double')
ConstantValue__11_enob = solver.IntVar(-10000, 10000, 'ConstantValue__11_enob')
solver.Add( + (1)*ConstantValue__11_enob + (-1)*ConstantValue__11_fixbits + (10000)*ConstantValue__11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_float + (1)*ConstantValue__11_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__12_fixbits = solver.IntVar(0, 31, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__13_fixbits = solver.IntVar(0, 31, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_float + (1)*ConstantValue__13_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul92 = fmul double 1.250000e-01, %add91, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
ConstantValue__13_CAST_mul92_fixbits = solver.IntVar(0, 31, 'ConstantValue__13_CAST_mul92_fixbits')
ConstantValue__13_CAST_mul92_fixp = solver.IntVar(0, 1, 'ConstantValue__13_CAST_mul92_fixp')
ConstantValue__13_CAST_mul92_float = solver.IntVar(0, 1, 'ConstantValue__13_CAST_mul92_float')
ConstantValue__13_CAST_mul92_double = solver.IntVar(0, 1, 'ConstantValue__13_CAST_mul92_double')
solver.Add( + (1)*ConstantValue__13_CAST_mul92_fixp + (1)*ConstantValue__13_CAST_mul92_float + (1)*ConstantValue__13_CAST_mul92_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__13_CAST_mul92_fixbits + (-10000)*ConstantValue__13_CAST_mul92_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C1_ConstantValue__13_CAST_mul92')
C2_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C2_ConstantValue__13_CAST_mul92')
solver.Add( + (1)*ConstantValue__13_fixbits + (-1)*ConstantValue__13_CAST_mul92_fixbits + (-10000)*C1_ConstantValue__13_CAST_mul92<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__13_fixbits + (1)*ConstantValue__13_CAST_mul92_fixbits + (-10000)*C2_ConstantValue__13_CAST_mul92<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__13_CAST_mul92
castCostObj +=  + (1)*C2_ConstantValue__13_CAST_mul92
C3_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C3_ConstantValue__13_CAST_mul92')
C4_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C4_ConstantValue__13_CAST_mul92')
C5_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C5_ConstantValue__13_CAST_mul92')
C6_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C6_ConstantValue__13_CAST_mul92')
C7_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C7_ConstantValue__13_CAST_mul92')
C8_ConstantValue__13_CAST_mul92 = solver.IntVar(0, 1, 'C8_ConstantValue__13_CAST_mul92')
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_CAST_mul92_float + (-1)*C3_ConstantValue__13_CAST_mul92<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__13_CAST_mul92
solver.Add( + (1)*ConstantValue__13_float + (1)*ConstantValue__13_CAST_mul92_fixp + (-1)*C4_ConstantValue__13_CAST_mul92<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__13_CAST_mul92
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_CAST_mul92_double + (-1)*C5_ConstantValue__13_CAST_mul92<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__13_CAST_mul92
solver.Add( + (1)*ConstantValue__13_double + (1)*ConstantValue__13_CAST_mul92_fixp + (-1)*C6_ConstantValue__13_CAST_mul92<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__13_CAST_mul92
solver.Add( + (1)*ConstantValue__13_float + (1)*ConstantValue__13_CAST_mul92_double + (-1)*C7_ConstantValue__13_CAST_mul92<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__13_CAST_mul92
solver.Add( + (1)*ConstantValue__13_double + (1)*ConstantValue__13_CAST_mul92_float + (-1)*C8_ConstantValue__13_CAST_mul92<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__13_CAST_mul92



#Constraint for cast for   %mul92 = fmul double 1.250000e-01, %add91, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
main_add91_CAST_mul92_fixbits = solver.IntVar(0, 16, 'main_add91_CAST_mul92_fixbits')
main_add91_CAST_mul92_fixp = solver.IntVar(0, 1, 'main_add91_CAST_mul92_fixp')
main_add91_CAST_mul92_float = solver.IntVar(0, 1, 'main_add91_CAST_mul92_float')
main_add91_CAST_mul92_double = solver.IntVar(0, 1, 'main_add91_CAST_mul92_double')
solver.Add( + (1)*main_add91_CAST_mul92_fixp + (1)*main_add91_CAST_mul92_float + (1)*main_add91_CAST_mul92_double==1)    #exactly 1 type
solver.Add( + (1)*main_add91_CAST_mul92_fixbits + (-10000)*main_add91_CAST_mul92_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C1_main_add91_CAST_mul92')
C2_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C2_main_add91_CAST_mul92')
solver.Add( + (1)*main_add91_fixbits + (-1)*main_add91_CAST_mul92_fixbits + (-10000)*C1_main_add91_CAST_mul92<=0)    #Shift cost 1
solver.Add( + (-1)*main_add91_fixbits + (1)*main_add91_CAST_mul92_fixbits + (-10000)*C2_main_add91_CAST_mul92<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add91_CAST_mul92
castCostObj +=  + (1)*C2_main_add91_CAST_mul92
C3_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C3_main_add91_CAST_mul92')
C4_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C4_main_add91_CAST_mul92')
C5_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C5_main_add91_CAST_mul92')
C6_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C6_main_add91_CAST_mul92')
C7_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C7_main_add91_CAST_mul92')
C8_main_add91_CAST_mul92 = solver.IntVar(0, 1, 'C8_main_add91_CAST_mul92')
solver.Add( + (1)*main_add91_fixp + (1)*main_add91_CAST_mul92_float + (-1)*C3_main_add91_CAST_mul92<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add91_CAST_mul92
solver.Add( + (1)*main_add91_float + (1)*main_add91_CAST_mul92_fixp + (-1)*C4_main_add91_CAST_mul92<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add91_CAST_mul92
solver.Add( + (1)*main_add91_fixp + (1)*main_add91_CAST_mul92_double + (-1)*C5_main_add91_CAST_mul92<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add91_CAST_mul92
solver.Add( + (1)*main_add91_double + (1)*main_add91_CAST_mul92_fixp + (-1)*C6_main_add91_CAST_mul92<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add91_CAST_mul92
solver.Add( + (1)*main_add91_float + (1)*main_add91_CAST_mul92_double + (-1)*C7_main_add91_CAST_mul92<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add91_CAST_mul92
solver.Add( + (1)*main_add91_double + (1)*main_add91_CAST_mul92_float + (-1)*C8_main_add91_CAST_mul92<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add91_CAST_mul92



#Stuff for   %mul92 = fmul double 1.250000e-01, %add91, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
main_mul92_fixbits = solver.IntVar(0, 19, 'main_mul92_fixbits')
main_mul92_fixp = solver.IntVar(0, 1, 'main_mul92_fixp')
main_mul92_float = solver.IntVar(0, 1, 'main_mul92_float')
main_mul92_double = solver.IntVar(0, 1, 'main_mul92_double')
main_mul92_enob = solver.IntVar(-10000, 10000, 'main_mul92_enob')
solver.Add( + (1)*main_mul92_enob + (-1)*main_mul92_fixbits + (10000)*main_mul92_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul92_enob + (10000)*main_mul92_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul92_enob + (10000)*main_mul92_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul92_fixbits + (-10000)*main_mul92_fixp>=-9982)    #Limit the lower number of frac bits19
solver.Add( + (1)*main_mul92_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul92_enob
solver.Add( + (1)*main_mul92_fixp + (1)*main_mul92_float + (1)*main_mul92_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul92_fixbits + (-10000)*main_mul92_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__13_CAST_mul92_fixp + (-1)*main_add91_CAST_mul92_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__13_CAST_mul92_float + (-1)*main_add91_CAST_mul92_float==0)    #float equality
solver.Add( + (1)*ConstantValue__13_CAST_mul92_double + (-1)*main_add91_CAST_mul92_double==0)    #double equality
solver.Add( + (1)*ConstantValue__13_CAST_mul92_fixp + (-1)*main_mul92_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__13_CAST_mul92_float + (-1)*main_mul92_float==0)    #float equality
solver.Add( + (1)*ConstantValue__13_CAST_mul92_double + (-1)*main_mul92_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul92_fixp
mathCostObj +=  + (2.64722)*main_mul92_float
mathCostObj +=  + (4.02255)*main_mul92_double
main_main_mul92_enob_1 = solver.IntVar(0, 1, 'main_main_mul92_enob_1')
main_main_mul92_enob_2 = solver.IntVar(0, 1, 'main_main_mul92_enob_2')
solver.Add( + (1)*main_main_mul92_enob_1 + (1)*main_main_mul92_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul92_enob + (-1)*main_add91_enob + (-10000)*main_main_mul92_enob_1<=3)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul92_enob + (-1)*ConstantValue__11_enob + (-10000)*main_main_mul92_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add93 = fadd double %mul68, %mul92, !taffo.info !55, !taffo.initweight !57
main_mul68_CAST_add93_fixbits = solver.IntVar(0, 19, 'main_mul68_CAST_add93_fixbits')
main_mul68_CAST_add93_fixp = solver.IntVar(0, 1, 'main_mul68_CAST_add93_fixp')
main_mul68_CAST_add93_float = solver.IntVar(0, 1, 'main_mul68_CAST_add93_float')
main_mul68_CAST_add93_double = solver.IntVar(0, 1, 'main_mul68_CAST_add93_double')
solver.Add( + (1)*main_mul68_CAST_add93_fixp + (1)*main_mul68_CAST_add93_float + (1)*main_mul68_CAST_add93_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul68_CAST_add93_fixbits + (-10000)*main_mul68_CAST_add93_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C1_main_mul68_CAST_add93')
C2_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C2_main_mul68_CAST_add93')
solver.Add( + (1)*main_mul68_fixbits + (-1)*main_mul68_CAST_add93_fixbits + (-10000)*C1_main_mul68_CAST_add93<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul68_fixbits + (1)*main_mul68_CAST_add93_fixbits + (-10000)*C2_main_mul68_CAST_add93<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul68_CAST_add93
castCostObj +=  + (1)*C2_main_mul68_CAST_add93
C3_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C3_main_mul68_CAST_add93')
C4_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C4_main_mul68_CAST_add93')
C5_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C5_main_mul68_CAST_add93')
C6_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C6_main_mul68_CAST_add93')
C7_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C7_main_mul68_CAST_add93')
C8_main_mul68_CAST_add93 = solver.IntVar(0, 1, 'C8_main_mul68_CAST_add93')
solver.Add( + (1)*main_mul68_fixp + (1)*main_mul68_CAST_add93_float + (-1)*C3_main_mul68_CAST_add93<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul68_CAST_add93
solver.Add( + (1)*main_mul68_float + (1)*main_mul68_CAST_add93_fixp + (-1)*C4_main_mul68_CAST_add93<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul68_CAST_add93
solver.Add( + (1)*main_mul68_fixp + (1)*main_mul68_CAST_add93_double + (-1)*C5_main_mul68_CAST_add93<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul68_CAST_add93
solver.Add( + (1)*main_mul68_double + (1)*main_mul68_CAST_add93_fixp + (-1)*C6_main_mul68_CAST_add93<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul68_CAST_add93
solver.Add( + (1)*main_mul68_float + (1)*main_mul68_CAST_add93_double + (-1)*C7_main_mul68_CAST_add93<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul68_CAST_add93
solver.Add( + (1)*main_mul68_double + (1)*main_mul68_CAST_add93_float + (-1)*C8_main_mul68_CAST_add93<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul68_CAST_add93



#Constraint for cast for   %add93 = fadd double %mul68, %mul92, !taffo.info !55, !taffo.initweight !57
main_mul92_CAST_add93_fixbits = solver.IntVar(0, 19, 'main_mul92_CAST_add93_fixbits')
main_mul92_CAST_add93_fixp = solver.IntVar(0, 1, 'main_mul92_CAST_add93_fixp')
main_mul92_CAST_add93_float = solver.IntVar(0, 1, 'main_mul92_CAST_add93_float')
main_mul92_CAST_add93_double = solver.IntVar(0, 1, 'main_mul92_CAST_add93_double')
solver.Add( + (1)*main_mul92_CAST_add93_fixp + (1)*main_mul92_CAST_add93_float + (1)*main_mul92_CAST_add93_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul92_CAST_add93_fixbits + (-10000)*main_mul92_CAST_add93_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C1_main_mul92_CAST_add93')
C2_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C2_main_mul92_CAST_add93')
solver.Add( + (1)*main_mul92_fixbits + (-1)*main_mul92_CAST_add93_fixbits + (-10000)*C1_main_mul92_CAST_add93<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul92_fixbits + (1)*main_mul92_CAST_add93_fixbits + (-10000)*C2_main_mul92_CAST_add93<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul92_CAST_add93
castCostObj +=  + (1)*C2_main_mul92_CAST_add93
C3_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C3_main_mul92_CAST_add93')
C4_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C4_main_mul92_CAST_add93')
C5_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C5_main_mul92_CAST_add93')
C6_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C6_main_mul92_CAST_add93')
C7_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C7_main_mul92_CAST_add93')
C8_main_mul92_CAST_add93 = solver.IntVar(0, 1, 'C8_main_mul92_CAST_add93')
solver.Add( + (1)*main_mul92_fixp + (1)*main_mul92_CAST_add93_float + (-1)*C3_main_mul92_CAST_add93<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul92_CAST_add93
solver.Add( + (1)*main_mul92_float + (1)*main_mul92_CAST_add93_fixp + (-1)*C4_main_mul92_CAST_add93<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul92_CAST_add93
solver.Add( + (1)*main_mul92_fixp + (1)*main_mul92_CAST_add93_double + (-1)*C5_main_mul92_CAST_add93<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul92_CAST_add93
solver.Add( + (1)*main_mul92_double + (1)*main_mul92_CAST_add93_fixp + (-1)*C6_main_mul92_CAST_add93<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul92_CAST_add93
solver.Add( + (1)*main_mul92_float + (1)*main_mul92_CAST_add93_double + (-1)*C7_main_mul92_CAST_add93<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul92_CAST_add93
solver.Add( + (1)*main_mul92_double + (1)*main_mul92_CAST_add93_float + (-1)*C8_main_mul92_CAST_add93<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul92_CAST_add93



#Stuff for   %add93 = fadd double %mul68, %mul92, !taffo.info !55, !taffo.initweight !57
main_add93_fixbits = solver.IntVar(0, 18, 'main_add93_fixbits')
main_add93_fixp = solver.IntVar(0, 1, 'main_add93_fixp')
main_add93_float = solver.IntVar(0, 1, 'main_add93_float')
main_add93_double = solver.IntVar(0, 1, 'main_add93_double')
main_add93_enob = solver.IntVar(-10000, 10000, 'main_add93_enob')
solver.Add( + (1)*main_add93_enob + (-1)*main_add93_fixbits + (10000)*main_add93_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add93_enob + (10000)*main_add93_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add93_enob + (10000)*main_add93_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add93_fixbits + (-10000)*main_add93_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_add93_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add93_enob
solver.Add( + (1)*main_add93_fixp + (1)*main_add93_float + (1)*main_add93_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add93_fixbits + (-10000)*main_add93_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul68_CAST_add93_fixp + (-1)*main_mul92_CAST_add93_fixp==0)    #fix equality
solver.Add( + (1)*main_mul68_CAST_add93_float + (-1)*main_mul92_CAST_add93_float==0)    #float equality
solver.Add( + (1)*main_mul68_CAST_add93_double + (-1)*main_mul92_CAST_add93_double==0)    #double equality
solver.Add( + (1)*main_mul68_CAST_add93_fixbits + (-1)*main_mul92_CAST_add93_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul68_CAST_add93_fixp + (-1)*main_add93_fixp==0)    #fix equality
solver.Add( + (1)*main_mul68_CAST_add93_float + (-1)*main_add93_float==0)    #float equality
solver.Add( + (1)*main_mul68_CAST_add93_double + (-1)*main_add93_double==0)    #double equality
solver.Add( + (1)*main_mul68_CAST_add93_fixbits + (-1)*main_add93_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add93_fixp
mathCostObj +=  + (2.33125)*main_add93_float
mathCostObj +=  + (2.72422)*main_add93_double
solver.Add( + (1)*main_add93_enob + (-1)*main_mul68_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add93_enob + (-1)*main_mul92_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp6')
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
main_main_tmp6_enob_3 = solver.IntVar(0, 1, 'main_main_tmp6_enob_3')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2 + (1)*main_main_tmp6_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp6_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp7')
solver.Add( + (1)*A_enob_memphi_main_tmp7 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
main_main_tmp7_enob_2 = solver.IntVar(0, 1, 'main_main_tmp7_enob_2')
main_main_tmp7_enob_3 = solver.IntVar(0, 1, 'main_main_tmp7_enob_3')
solver.Add( + (1)*main_main_tmp7_enob_1 + (1)*main_main_tmp7_enob_2 + (1)*main_main_tmp7_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp7 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__14_fixbits = solver.IntVar(0, 30, 'ConstantValue__14_fixbits')
ConstantValue__14_fixp = solver.IntVar(0, 1, 'ConstantValue__14_fixp')
ConstantValue__14_float = solver.IntVar(0, 1, 'ConstantValue__14_float')
ConstantValue__14_double = solver.IntVar(0, 1, 'ConstantValue__14_double')
ConstantValue__14_enob = solver.IntVar(-10000, 10000, 'ConstantValue__14_enob')
solver.Add( + (1)*ConstantValue__14_enob + (-1)*ConstantValue__14_fixbits + (10000)*ConstantValue__14_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_float + (1)*ConstantValue__14_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__15_fixbits = solver.IntVar(0, 30, 'ConstantValue__15_fixbits')
ConstantValue__15_fixp = solver.IntVar(0, 1, 'ConstantValue__15_fixp')
ConstantValue__15_float = solver.IntVar(0, 1, 'ConstantValue__15_float')
ConstantValue__15_double = solver.IntVar(0, 1, 'ConstantValue__15_double')
ConstantValue__15_enob = solver.IntVar(-10000, 10000, 'ConstantValue__15_enob')
solver.Add( + (1)*ConstantValue__15_enob + (-1)*ConstantValue__15_fixbits + (10000)*ConstantValue__15_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__15_fixp + (1)*ConstantValue__15_float + (1)*ConstantValue__15_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__16_fixbits = solver.IntVar(0, 30, 'ConstantValue__16_fixbits')
ConstantValue__16_fixp = solver.IntVar(0, 1, 'ConstantValue__16_fixp')
ConstantValue__16_float = solver.IntVar(0, 1, 'ConstantValue__16_float')
ConstantValue__16_double = solver.IntVar(0, 1, 'ConstantValue__16_double')
ConstantValue__16_enob = solver.IntVar(-10000, 10000, 'ConstantValue__16_enob')
solver.Add( + (1)*ConstantValue__16_enob + (-1)*ConstantValue__16_fixbits + (10000)*ConstantValue__16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul107 = fmul double 2.000000e+00, %tmp7, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
ConstantValue__16_CAST_mul107_fixbits = solver.IntVar(0, 30, 'ConstantValue__16_CAST_mul107_fixbits')
ConstantValue__16_CAST_mul107_fixp = solver.IntVar(0, 1, 'ConstantValue__16_CAST_mul107_fixp')
ConstantValue__16_CAST_mul107_float = solver.IntVar(0, 1, 'ConstantValue__16_CAST_mul107_float')
ConstantValue__16_CAST_mul107_double = solver.IntVar(0, 1, 'ConstantValue__16_CAST_mul107_double')
solver.Add( + (1)*ConstantValue__16_CAST_mul107_fixp + (1)*ConstantValue__16_CAST_mul107_float + (1)*ConstantValue__16_CAST_mul107_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__16_CAST_mul107_fixbits + (-10000)*ConstantValue__16_CAST_mul107_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C1_ConstantValue__16_CAST_mul107')
C2_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C2_ConstantValue__16_CAST_mul107')
solver.Add( + (1)*ConstantValue__16_fixbits + (-1)*ConstantValue__16_CAST_mul107_fixbits + (-10000)*C1_ConstantValue__16_CAST_mul107<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__16_fixbits + (1)*ConstantValue__16_CAST_mul107_fixbits + (-10000)*C2_ConstantValue__16_CAST_mul107<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__16_CAST_mul107
castCostObj +=  + (1)*C2_ConstantValue__16_CAST_mul107
C3_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C3_ConstantValue__16_CAST_mul107')
C4_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C4_ConstantValue__16_CAST_mul107')
C5_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C5_ConstantValue__16_CAST_mul107')
C6_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C6_ConstantValue__16_CAST_mul107')
C7_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C7_ConstantValue__16_CAST_mul107')
C8_ConstantValue__16_CAST_mul107 = solver.IntVar(0, 1, 'C8_ConstantValue__16_CAST_mul107')
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_mul107_float + (-1)*C3_ConstantValue__16_CAST_mul107<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__16_CAST_mul107
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_mul107_fixp + (-1)*C4_ConstantValue__16_CAST_mul107<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__16_CAST_mul107
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_mul107_double + (-1)*C5_ConstantValue__16_CAST_mul107<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__16_CAST_mul107
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_mul107_fixp + (-1)*C6_ConstantValue__16_CAST_mul107<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__16_CAST_mul107
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_mul107_double + (-1)*C7_ConstantValue__16_CAST_mul107<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__16_CAST_mul107
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_mul107_float + (-1)*C8_ConstantValue__16_CAST_mul107<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__16_CAST_mul107



#Constraint for cast for   %mul107 = fmul double 2.000000e+00, %tmp7, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
A_CAST_mul107_fixbits = solver.IntVar(0, 16, 'A_CAST_mul107_fixbits')
A_CAST_mul107_fixp = solver.IntVar(0, 1, 'A_CAST_mul107_fixp')
A_CAST_mul107_float = solver.IntVar(0, 1, 'A_CAST_mul107_float')
A_CAST_mul107_double = solver.IntVar(0, 1, 'A_CAST_mul107_double')
solver.Add( + (1)*A_CAST_mul107_fixp + (1)*A_CAST_mul107_float + (1)*A_CAST_mul107_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_mul107_fixbits + (-10000)*A_CAST_mul107_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_mul107 = solver.IntVar(0, 1, 'C1_A_CAST_mul107')
C2_A_CAST_mul107 = solver.IntVar(0, 1, 'C2_A_CAST_mul107')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_mul107_fixbits + (-10000)*C1_A_CAST_mul107<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_mul107_fixbits + (-10000)*C2_A_CAST_mul107<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_mul107
castCostObj +=  + (1)*C2_A_CAST_mul107
C3_A_CAST_mul107 = solver.IntVar(0, 1, 'C3_A_CAST_mul107')
C4_A_CAST_mul107 = solver.IntVar(0, 1, 'C4_A_CAST_mul107')
C5_A_CAST_mul107 = solver.IntVar(0, 1, 'C5_A_CAST_mul107')
C6_A_CAST_mul107 = solver.IntVar(0, 1, 'C6_A_CAST_mul107')
C7_A_CAST_mul107 = solver.IntVar(0, 1, 'C7_A_CAST_mul107')
C8_A_CAST_mul107 = solver.IntVar(0, 1, 'C8_A_CAST_mul107')
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul107_float + (-1)*C3_A_CAST_mul107<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_mul107
solver.Add( + (1)*A_float + (1)*A_CAST_mul107_fixp + (-1)*C4_A_CAST_mul107<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_mul107
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul107_double + (-1)*C5_A_CAST_mul107<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_mul107
solver.Add( + (1)*A_double + (1)*A_CAST_mul107_fixp + (-1)*C6_A_CAST_mul107<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_mul107
solver.Add( + (1)*A_float + (1)*A_CAST_mul107_double + (-1)*C7_A_CAST_mul107<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_mul107
solver.Add( + (1)*A_double + (1)*A_CAST_mul107_float + (-1)*C8_A_CAST_mul107<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_mul107



#Stuff for   %mul107 = fmul double 2.000000e+00, %tmp7, !taffo.info !41, !taffo.initweight !31, !taffo.constinfo !43
main_mul107_fixbits = solver.IntVar(0, 17, 'main_mul107_fixbits')
main_mul107_fixp = solver.IntVar(0, 1, 'main_mul107_fixp')
main_mul107_float = solver.IntVar(0, 1, 'main_mul107_float')
main_mul107_double = solver.IntVar(0, 1, 'main_mul107_double')
main_mul107_enob = solver.IntVar(-10000, 10000, 'main_mul107_enob')
solver.Add( + (1)*main_mul107_enob + (-1)*main_mul107_fixbits + (10000)*main_mul107_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul107_enob + (10000)*main_mul107_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul107_enob + (10000)*main_mul107_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul107_fixbits + (-10000)*main_mul107_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_mul107_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul107_enob
solver.Add( + (1)*main_mul107_fixp + (1)*main_mul107_float + (1)*main_mul107_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul107_fixbits + (-10000)*main_mul107_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__16_CAST_mul107_fixp + (-1)*A_CAST_mul107_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__16_CAST_mul107_float + (-1)*A_CAST_mul107_float==0)    #float equality
solver.Add( + (1)*ConstantValue__16_CAST_mul107_double + (-1)*A_CAST_mul107_double==0)    #double equality
solver.Add( + (1)*ConstantValue__16_CAST_mul107_fixp + (-1)*main_mul107_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__16_CAST_mul107_float + (-1)*main_mul107_float==0)    #float equality
solver.Add( + (1)*ConstantValue__16_CAST_mul107_double + (-1)*main_mul107_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul107_fixp
mathCostObj +=  + (2.64722)*main_mul107_float
mathCostObj +=  + (4.02255)*main_mul107_double
main_main_mul107_enob_1 = solver.IntVar(0, 1, 'main_main_mul107_enob_1')
main_main_mul107_enob_2 = solver.IntVar(0, 1, 'main_main_mul107_enob_2')
solver.Add( + (1)*main_main_mul107_enob_1 + (1)*main_main_mul107_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul107_enob + (-1)*A_enob_memphi_main_tmp7 + (-10000)*main_main_mul107_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul107_enob + (-1)*ConstantValue__14_enob + (-10000)*main_main_mul107_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub108 = fsub double %tmp6, %mul107, !taffo.info !46, !taffo.initweight !31
A_CAST_sub108_fixbits = solver.IntVar(0, 16, 'A_CAST_sub108_fixbits')
A_CAST_sub108_fixp = solver.IntVar(0, 1, 'A_CAST_sub108_fixp')
A_CAST_sub108_float = solver.IntVar(0, 1, 'A_CAST_sub108_float')
A_CAST_sub108_double = solver.IntVar(0, 1, 'A_CAST_sub108_double')
solver.Add( + (1)*A_CAST_sub108_fixp + (1)*A_CAST_sub108_float + (1)*A_CAST_sub108_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_sub108_fixbits + (-10000)*A_CAST_sub108_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_sub108 = solver.IntVar(0, 1, 'C1_A_CAST_sub108')
C2_A_CAST_sub108 = solver.IntVar(0, 1, 'C2_A_CAST_sub108')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_sub108_fixbits + (-10000)*C1_A_CAST_sub108<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_sub108_fixbits + (-10000)*C2_A_CAST_sub108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_sub108
castCostObj +=  + (1)*C2_A_CAST_sub108
C3_A_CAST_sub108 = solver.IntVar(0, 1, 'C3_A_CAST_sub108')
C4_A_CAST_sub108 = solver.IntVar(0, 1, 'C4_A_CAST_sub108')
C5_A_CAST_sub108 = solver.IntVar(0, 1, 'C5_A_CAST_sub108')
C6_A_CAST_sub108 = solver.IntVar(0, 1, 'C6_A_CAST_sub108')
C7_A_CAST_sub108 = solver.IntVar(0, 1, 'C7_A_CAST_sub108')
C8_A_CAST_sub108 = solver.IntVar(0, 1, 'C8_A_CAST_sub108')
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub108_float + (-1)*C3_A_CAST_sub108<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_sub108
solver.Add( + (1)*A_float + (1)*A_CAST_sub108_fixp + (-1)*C4_A_CAST_sub108<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_sub108
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub108_double + (-1)*C5_A_CAST_sub108<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_sub108
solver.Add( + (1)*A_double + (1)*A_CAST_sub108_fixp + (-1)*C6_A_CAST_sub108<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_sub108
solver.Add( + (1)*A_float + (1)*A_CAST_sub108_double + (-1)*C7_A_CAST_sub108<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_sub108
solver.Add( + (1)*A_double + (1)*A_CAST_sub108_float + (-1)*C8_A_CAST_sub108<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_sub108



#Constraint for cast for   %sub108 = fsub double %tmp6, %mul107, !taffo.info !46, !taffo.initweight !31
main_mul107_CAST_sub108_fixbits = solver.IntVar(0, 17, 'main_mul107_CAST_sub108_fixbits')
main_mul107_CAST_sub108_fixp = solver.IntVar(0, 1, 'main_mul107_CAST_sub108_fixp')
main_mul107_CAST_sub108_float = solver.IntVar(0, 1, 'main_mul107_CAST_sub108_float')
main_mul107_CAST_sub108_double = solver.IntVar(0, 1, 'main_mul107_CAST_sub108_double')
solver.Add( + (1)*main_mul107_CAST_sub108_fixp + (1)*main_mul107_CAST_sub108_float + (1)*main_mul107_CAST_sub108_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul107_CAST_sub108_fixbits + (-10000)*main_mul107_CAST_sub108_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C1_main_mul107_CAST_sub108')
C2_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C2_main_mul107_CAST_sub108')
solver.Add( + (1)*main_mul107_fixbits + (-1)*main_mul107_CAST_sub108_fixbits + (-10000)*C1_main_mul107_CAST_sub108<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul107_fixbits + (1)*main_mul107_CAST_sub108_fixbits + (-10000)*C2_main_mul107_CAST_sub108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul107_CAST_sub108
castCostObj +=  + (1)*C2_main_mul107_CAST_sub108
C3_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C3_main_mul107_CAST_sub108')
C4_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C4_main_mul107_CAST_sub108')
C5_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C5_main_mul107_CAST_sub108')
C6_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C6_main_mul107_CAST_sub108')
C7_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C7_main_mul107_CAST_sub108')
C8_main_mul107_CAST_sub108 = solver.IntVar(0, 1, 'C8_main_mul107_CAST_sub108')
solver.Add( + (1)*main_mul107_fixp + (1)*main_mul107_CAST_sub108_float + (-1)*C3_main_mul107_CAST_sub108<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul107_CAST_sub108
solver.Add( + (1)*main_mul107_float + (1)*main_mul107_CAST_sub108_fixp + (-1)*C4_main_mul107_CAST_sub108<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul107_CAST_sub108
solver.Add( + (1)*main_mul107_fixp + (1)*main_mul107_CAST_sub108_double + (-1)*C5_main_mul107_CAST_sub108<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul107_CAST_sub108
solver.Add( + (1)*main_mul107_double + (1)*main_mul107_CAST_sub108_fixp + (-1)*C6_main_mul107_CAST_sub108<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul107_CAST_sub108
solver.Add( + (1)*main_mul107_float + (1)*main_mul107_CAST_sub108_double + (-1)*C7_main_mul107_CAST_sub108<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul107_CAST_sub108
solver.Add( + (1)*main_mul107_double + (1)*main_mul107_CAST_sub108_float + (-1)*C8_main_mul107_CAST_sub108<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul107_CAST_sub108



#Stuff for   %sub108 = fsub double %tmp6, %mul107, !taffo.info !46, !taffo.initweight !31
main_sub108_fixbits = solver.IntVar(0, 17, 'main_sub108_fixbits')
main_sub108_fixp = solver.IntVar(0, 1, 'main_sub108_fixp')
main_sub108_float = solver.IntVar(0, 1, 'main_sub108_float')
main_sub108_double = solver.IntVar(0, 1, 'main_sub108_double')
main_sub108_enob = solver.IntVar(-10000, 10000, 'main_sub108_enob')
solver.Add( + (1)*main_sub108_enob + (-1)*main_sub108_fixbits + (10000)*main_sub108_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub108_enob + (10000)*main_sub108_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub108_enob + (10000)*main_sub108_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub108_fixbits + (-10000)*main_sub108_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_sub108_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub108_enob
solver.Add( + (1)*main_sub108_fixp + (1)*main_sub108_float + (1)*main_sub108_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub108_fixbits + (-10000)*main_sub108_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*A_CAST_sub108_fixp + (-1)*main_mul107_CAST_sub108_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub108_float + (-1)*main_mul107_CAST_sub108_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub108_double + (-1)*main_mul107_CAST_sub108_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub108_fixbits + (-1)*main_mul107_CAST_sub108_fixbits==0)    #same fractional bit
solver.Add( + (1)*A_CAST_sub108_fixp + (-1)*main_sub108_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub108_float + (-1)*main_sub108_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub108_double + (-1)*main_sub108_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub108_fixbits + (-1)*main_sub108_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub108_fixp
mathCostObj +=  + (2.33125)*main_sub108_float
mathCostObj +=  + (2.72422)*main_sub108_double
solver.Add( + (1)*main_sub108_enob + (-1)*A_enob_memphi_main_tmp6<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub108_enob + (-1)*main_mul107_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp8')
solver.Add( + (1)*A_enob_memphi_main_tmp8 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
main_main_tmp8_enob_2 = solver.IntVar(0, 1, 'main_main_tmp8_enob_2')
main_main_tmp8_enob_3 = solver.IntVar(0, 1, 'main_main_tmp8_enob_3')
solver.Add( + (1)*main_main_tmp8_enob_1 + (1)*main_main_tmp8_enob_2 + (1)*main_main_tmp8_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp8 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add116 = fadd double %sub108, %tmp8, !taffo.info !48, !taffo.initweight !31
main_sub108_CAST_add116_fixbits = solver.IntVar(0, 17, 'main_sub108_CAST_add116_fixbits')
main_sub108_CAST_add116_fixp = solver.IntVar(0, 1, 'main_sub108_CAST_add116_fixp')
main_sub108_CAST_add116_float = solver.IntVar(0, 1, 'main_sub108_CAST_add116_float')
main_sub108_CAST_add116_double = solver.IntVar(0, 1, 'main_sub108_CAST_add116_double')
solver.Add( + (1)*main_sub108_CAST_add116_fixp + (1)*main_sub108_CAST_add116_float + (1)*main_sub108_CAST_add116_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub108_CAST_add116_fixbits + (-10000)*main_sub108_CAST_add116_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C1_main_sub108_CAST_add116')
C2_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C2_main_sub108_CAST_add116')
solver.Add( + (1)*main_sub108_fixbits + (-1)*main_sub108_CAST_add116_fixbits + (-10000)*C1_main_sub108_CAST_add116<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub108_fixbits + (1)*main_sub108_CAST_add116_fixbits + (-10000)*C2_main_sub108_CAST_add116<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub108_CAST_add116
castCostObj +=  + (1)*C2_main_sub108_CAST_add116
C3_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C3_main_sub108_CAST_add116')
C4_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C4_main_sub108_CAST_add116')
C5_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C5_main_sub108_CAST_add116')
C6_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C6_main_sub108_CAST_add116')
C7_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C7_main_sub108_CAST_add116')
C8_main_sub108_CAST_add116 = solver.IntVar(0, 1, 'C8_main_sub108_CAST_add116')
solver.Add( + (1)*main_sub108_fixp + (1)*main_sub108_CAST_add116_float + (-1)*C3_main_sub108_CAST_add116<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub108_CAST_add116
solver.Add( + (1)*main_sub108_float + (1)*main_sub108_CAST_add116_fixp + (-1)*C4_main_sub108_CAST_add116<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub108_CAST_add116
solver.Add( + (1)*main_sub108_fixp + (1)*main_sub108_CAST_add116_double + (-1)*C5_main_sub108_CAST_add116<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub108_CAST_add116
solver.Add( + (1)*main_sub108_double + (1)*main_sub108_CAST_add116_fixp + (-1)*C6_main_sub108_CAST_add116<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub108_CAST_add116
solver.Add( + (1)*main_sub108_float + (1)*main_sub108_CAST_add116_double + (-1)*C7_main_sub108_CAST_add116<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub108_CAST_add116
solver.Add( + (1)*main_sub108_double + (1)*main_sub108_CAST_add116_float + (-1)*C8_main_sub108_CAST_add116<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub108_CAST_add116



#Constraint for cast for   %add116 = fadd double %sub108, %tmp8, !taffo.info !48, !taffo.initweight !31
A_CAST_add116_fixbits = solver.IntVar(0, 16, 'A_CAST_add116_fixbits')
A_CAST_add116_fixp = solver.IntVar(0, 1, 'A_CAST_add116_fixp')
A_CAST_add116_float = solver.IntVar(0, 1, 'A_CAST_add116_float')
A_CAST_add116_double = solver.IntVar(0, 1, 'A_CAST_add116_double')
solver.Add( + (1)*A_CAST_add116_fixp + (1)*A_CAST_add116_float + (1)*A_CAST_add116_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_add116_fixbits + (-10000)*A_CAST_add116_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_add116 = solver.IntVar(0, 1, 'C1_A_CAST_add116')
C2_A_CAST_add116 = solver.IntVar(0, 1, 'C2_A_CAST_add116')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_add116_fixbits + (-10000)*C1_A_CAST_add116<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_add116_fixbits + (-10000)*C2_A_CAST_add116<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_add116
castCostObj +=  + (1)*C2_A_CAST_add116
C3_A_CAST_add116 = solver.IntVar(0, 1, 'C3_A_CAST_add116')
C4_A_CAST_add116 = solver.IntVar(0, 1, 'C4_A_CAST_add116')
C5_A_CAST_add116 = solver.IntVar(0, 1, 'C5_A_CAST_add116')
C6_A_CAST_add116 = solver.IntVar(0, 1, 'C6_A_CAST_add116')
C7_A_CAST_add116 = solver.IntVar(0, 1, 'C7_A_CAST_add116')
C8_A_CAST_add116 = solver.IntVar(0, 1, 'C8_A_CAST_add116')
solver.Add( + (1)*A_fixp + (1)*A_CAST_add116_float + (-1)*C3_A_CAST_add116<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_add116
solver.Add( + (1)*A_float + (1)*A_CAST_add116_fixp + (-1)*C4_A_CAST_add116<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_add116
solver.Add( + (1)*A_fixp + (1)*A_CAST_add116_double + (-1)*C5_A_CAST_add116<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_add116
solver.Add( + (1)*A_double + (1)*A_CAST_add116_fixp + (-1)*C6_A_CAST_add116<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_add116
solver.Add( + (1)*A_float + (1)*A_CAST_add116_double + (-1)*C7_A_CAST_add116<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_add116
solver.Add( + (1)*A_double + (1)*A_CAST_add116_float + (-1)*C8_A_CAST_add116<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_add116



#Stuff for   %add116 = fadd double %sub108, %tmp8, !taffo.info !48, !taffo.initweight !31
main_add116_fixbits = solver.IntVar(0, 16, 'main_add116_fixbits')
main_add116_fixp = solver.IntVar(0, 1, 'main_add116_fixp')
main_add116_float = solver.IntVar(0, 1, 'main_add116_float')
main_add116_double = solver.IntVar(0, 1, 'main_add116_double')
main_add116_enob = solver.IntVar(-10000, 10000, 'main_add116_enob')
solver.Add( + (1)*main_add116_enob + (-1)*main_add116_fixbits + (10000)*main_add116_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add116_enob + (10000)*main_add116_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add116_enob + (10000)*main_add116_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add116_fixbits + (-10000)*main_add116_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_add116_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add116_enob
solver.Add( + (1)*main_add116_fixp + (1)*main_add116_float + (1)*main_add116_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add116_fixbits + (-10000)*main_add116_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub108_CAST_add116_fixp + (-1)*A_CAST_add116_fixp==0)    #fix equality
solver.Add( + (1)*main_sub108_CAST_add116_float + (-1)*A_CAST_add116_float==0)    #float equality
solver.Add( + (1)*main_sub108_CAST_add116_double + (-1)*A_CAST_add116_double==0)    #double equality
solver.Add( + (1)*main_sub108_CAST_add116_fixbits + (-1)*A_CAST_add116_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub108_CAST_add116_fixp + (-1)*main_add116_fixp==0)    #fix equality
solver.Add( + (1)*main_sub108_CAST_add116_float + (-1)*main_add116_float==0)    #float equality
solver.Add( + (1)*main_sub108_CAST_add116_double + (-1)*main_add116_double==0)    #double equality
solver.Add( + (1)*main_sub108_CAST_add116_fixbits + (-1)*main_add116_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add116_fixp
mathCostObj +=  + (2.33125)*main_add116_float
mathCostObj +=  + (2.72422)*main_add116_double
solver.Add( + (1)*main_add116_enob + (-1)*main_sub108_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add116_enob + (-1)*A_enob_memphi_main_tmp8<=0)    #Enob propagation in sum second addend



#Stuff for double 1.250000e-01
ConstantValue__17_fixbits = solver.IntVar(0, 31, 'ConstantValue__17_fixbits')
ConstantValue__17_fixp = solver.IntVar(0, 1, 'ConstantValue__17_fixp')
ConstantValue__17_float = solver.IntVar(0, 1, 'ConstantValue__17_float')
ConstantValue__17_double = solver.IntVar(0, 1, 'ConstantValue__17_double')
ConstantValue__17_enob = solver.IntVar(-10000, 10000, 'ConstantValue__17_enob')
solver.Add( + (1)*ConstantValue__17_enob + (-1)*ConstantValue__17_fixbits + (10000)*ConstantValue__17_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_float + (1)*ConstantValue__17_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__18_fixbits = solver.IntVar(0, 31, 'ConstantValue__18_fixbits')
ConstantValue__18_fixp = solver.IntVar(0, 1, 'ConstantValue__18_fixp')
ConstantValue__18_float = solver.IntVar(0, 1, 'ConstantValue__18_float')
ConstantValue__18_double = solver.IntVar(0, 1, 'ConstantValue__18_double')
ConstantValue__18_enob = solver.IntVar(-10000, 10000, 'ConstantValue__18_enob')
solver.Add( + (1)*ConstantValue__18_enob + (-1)*ConstantValue__18_fixbits + (10000)*ConstantValue__18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__18_fixp + (1)*ConstantValue__18_float + (1)*ConstantValue__18_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__19_fixbits = solver.IntVar(0, 31, 'ConstantValue__19_fixbits')
ConstantValue__19_fixp = solver.IntVar(0, 1, 'ConstantValue__19_fixp')
ConstantValue__19_float = solver.IntVar(0, 1, 'ConstantValue__19_float')
ConstantValue__19_double = solver.IntVar(0, 1, 'ConstantValue__19_double')
ConstantValue__19_enob = solver.IntVar(-10000, 10000, 'ConstantValue__19_enob')
solver.Add( + (1)*ConstantValue__19_enob + (-1)*ConstantValue__19_fixbits + (10000)*ConstantValue__19_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_float + (1)*ConstantValue__19_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul117 = fmul double 1.250000e-01, %add116, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
ConstantValue__19_CAST_mul117_fixbits = solver.IntVar(0, 31, 'ConstantValue__19_CAST_mul117_fixbits')
ConstantValue__19_CAST_mul117_fixp = solver.IntVar(0, 1, 'ConstantValue__19_CAST_mul117_fixp')
ConstantValue__19_CAST_mul117_float = solver.IntVar(0, 1, 'ConstantValue__19_CAST_mul117_float')
ConstantValue__19_CAST_mul117_double = solver.IntVar(0, 1, 'ConstantValue__19_CAST_mul117_double')
solver.Add( + (1)*ConstantValue__19_CAST_mul117_fixp + (1)*ConstantValue__19_CAST_mul117_float + (1)*ConstantValue__19_CAST_mul117_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__19_CAST_mul117_fixbits + (-10000)*ConstantValue__19_CAST_mul117_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C1_ConstantValue__19_CAST_mul117')
C2_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C2_ConstantValue__19_CAST_mul117')
solver.Add( + (1)*ConstantValue__19_fixbits + (-1)*ConstantValue__19_CAST_mul117_fixbits + (-10000)*C1_ConstantValue__19_CAST_mul117<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__19_fixbits + (1)*ConstantValue__19_CAST_mul117_fixbits + (-10000)*C2_ConstantValue__19_CAST_mul117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__19_CAST_mul117
castCostObj +=  + (1)*C2_ConstantValue__19_CAST_mul117
C3_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C3_ConstantValue__19_CAST_mul117')
C4_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C4_ConstantValue__19_CAST_mul117')
C5_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C5_ConstantValue__19_CAST_mul117')
C6_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C6_ConstantValue__19_CAST_mul117')
C7_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C7_ConstantValue__19_CAST_mul117')
C8_ConstantValue__19_CAST_mul117 = solver.IntVar(0, 1, 'C8_ConstantValue__19_CAST_mul117')
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_mul117_float + (-1)*C3_ConstantValue__19_CAST_mul117<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__19_CAST_mul117
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_mul117_fixp + (-1)*C4_ConstantValue__19_CAST_mul117<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__19_CAST_mul117
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_mul117_double + (-1)*C5_ConstantValue__19_CAST_mul117<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__19_CAST_mul117
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_mul117_fixp + (-1)*C6_ConstantValue__19_CAST_mul117<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__19_CAST_mul117
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_mul117_double + (-1)*C7_ConstantValue__19_CAST_mul117<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__19_CAST_mul117
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_mul117_float + (-1)*C8_ConstantValue__19_CAST_mul117<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__19_CAST_mul117



#Constraint for cast for   %mul117 = fmul double 1.250000e-01, %add116, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
main_add116_CAST_mul117_fixbits = solver.IntVar(0, 16, 'main_add116_CAST_mul117_fixbits')
main_add116_CAST_mul117_fixp = solver.IntVar(0, 1, 'main_add116_CAST_mul117_fixp')
main_add116_CAST_mul117_float = solver.IntVar(0, 1, 'main_add116_CAST_mul117_float')
main_add116_CAST_mul117_double = solver.IntVar(0, 1, 'main_add116_CAST_mul117_double')
solver.Add( + (1)*main_add116_CAST_mul117_fixp + (1)*main_add116_CAST_mul117_float + (1)*main_add116_CAST_mul117_double==1)    #exactly 1 type
solver.Add( + (1)*main_add116_CAST_mul117_fixbits + (-10000)*main_add116_CAST_mul117_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C1_main_add116_CAST_mul117')
C2_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C2_main_add116_CAST_mul117')
solver.Add( + (1)*main_add116_fixbits + (-1)*main_add116_CAST_mul117_fixbits + (-10000)*C1_main_add116_CAST_mul117<=0)    #Shift cost 1
solver.Add( + (-1)*main_add116_fixbits + (1)*main_add116_CAST_mul117_fixbits + (-10000)*C2_main_add116_CAST_mul117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add116_CAST_mul117
castCostObj +=  + (1)*C2_main_add116_CAST_mul117
C3_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C3_main_add116_CAST_mul117')
C4_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C4_main_add116_CAST_mul117')
C5_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C5_main_add116_CAST_mul117')
C6_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C6_main_add116_CAST_mul117')
C7_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C7_main_add116_CAST_mul117')
C8_main_add116_CAST_mul117 = solver.IntVar(0, 1, 'C8_main_add116_CAST_mul117')
solver.Add( + (1)*main_add116_fixp + (1)*main_add116_CAST_mul117_float + (-1)*C3_main_add116_CAST_mul117<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add116_CAST_mul117
solver.Add( + (1)*main_add116_float + (1)*main_add116_CAST_mul117_fixp + (-1)*C4_main_add116_CAST_mul117<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add116_CAST_mul117
solver.Add( + (1)*main_add116_fixp + (1)*main_add116_CAST_mul117_double + (-1)*C5_main_add116_CAST_mul117<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add116_CAST_mul117
solver.Add( + (1)*main_add116_double + (1)*main_add116_CAST_mul117_fixp + (-1)*C6_main_add116_CAST_mul117<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add116_CAST_mul117
solver.Add( + (1)*main_add116_float + (1)*main_add116_CAST_mul117_double + (-1)*C7_main_add116_CAST_mul117<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add116_CAST_mul117
solver.Add( + (1)*main_add116_double + (1)*main_add116_CAST_mul117_float + (-1)*C8_main_add116_CAST_mul117<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add116_CAST_mul117



#Stuff for   %mul117 = fmul double 1.250000e-01, %add116, !taffo.info !50, !taffo.initweight !35, !taffo.constinfo !52
main_mul117_fixbits = solver.IntVar(0, 19, 'main_mul117_fixbits')
main_mul117_fixp = solver.IntVar(0, 1, 'main_mul117_fixp')
main_mul117_float = solver.IntVar(0, 1, 'main_mul117_float')
main_mul117_double = solver.IntVar(0, 1, 'main_mul117_double')
main_mul117_enob = solver.IntVar(-10000, 10000, 'main_mul117_enob')
solver.Add( + (1)*main_mul117_enob + (-1)*main_mul117_fixbits + (10000)*main_mul117_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul117_enob + (10000)*main_mul117_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul117_enob + (10000)*main_mul117_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul117_fixbits + (-10000)*main_mul117_fixp>=-9982)    #Limit the lower number of frac bits19
solver.Add( + (1)*main_mul117_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul117_enob
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_float + (1)*main_mul117_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul117_fixbits + (-10000)*main_mul117_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__19_CAST_mul117_fixp + (-1)*main_add116_CAST_mul117_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__19_CAST_mul117_float + (-1)*main_add116_CAST_mul117_float==0)    #float equality
solver.Add( + (1)*ConstantValue__19_CAST_mul117_double + (-1)*main_add116_CAST_mul117_double==0)    #double equality
solver.Add( + (1)*ConstantValue__19_CAST_mul117_fixp + (-1)*main_mul117_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__19_CAST_mul117_float + (-1)*main_mul117_float==0)    #float equality
solver.Add( + (1)*ConstantValue__19_CAST_mul117_double + (-1)*main_mul117_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul117_fixp
mathCostObj +=  + (2.64722)*main_mul117_float
mathCostObj +=  + (4.02255)*main_mul117_double
main_main_mul117_enob_1 = solver.IntVar(0, 1, 'main_main_mul117_enob_1')
main_main_mul117_enob_2 = solver.IntVar(0, 1, 'main_main_mul117_enob_2')
solver.Add( + (1)*main_main_mul117_enob_1 + (1)*main_main_mul117_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul117_enob + (-1)*main_add116_enob + (-10000)*main_main_mul117_enob_1<=3)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul117_enob + (-1)*ConstantValue__17_enob + (-10000)*main_main_mul117_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add118 = fadd double %add93, %mul117, !taffo.info !58, !taffo.initweight !57
main_add93_CAST_add118_fixbits = solver.IntVar(0, 18, 'main_add93_CAST_add118_fixbits')
main_add93_CAST_add118_fixp = solver.IntVar(0, 1, 'main_add93_CAST_add118_fixp')
main_add93_CAST_add118_float = solver.IntVar(0, 1, 'main_add93_CAST_add118_float')
main_add93_CAST_add118_double = solver.IntVar(0, 1, 'main_add93_CAST_add118_double')
solver.Add( + (1)*main_add93_CAST_add118_fixp + (1)*main_add93_CAST_add118_float + (1)*main_add93_CAST_add118_double==1)    #exactly 1 type
solver.Add( + (1)*main_add93_CAST_add118_fixbits + (-10000)*main_add93_CAST_add118_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C1_main_add93_CAST_add118')
C2_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C2_main_add93_CAST_add118')
solver.Add( + (1)*main_add93_fixbits + (-1)*main_add93_CAST_add118_fixbits + (-10000)*C1_main_add93_CAST_add118<=0)    #Shift cost 1
solver.Add( + (-1)*main_add93_fixbits + (1)*main_add93_CAST_add118_fixbits + (-10000)*C2_main_add93_CAST_add118<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add93_CAST_add118
castCostObj +=  + (1)*C2_main_add93_CAST_add118
C3_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C3_main_add93_CAST_add118')
C4_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C4_main_add93_CAST_add118')
C5_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C5_main_add93_CAST_add118')
C6_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C6_main_add93_CAST_add118')
C7_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C7_main_add93_CAST_add118')
C8_main_add93_CAST_add118 = solver.IntVar(0, 1, 'C8_main_add93_CAST_add118')
solver.Add( + (1)*main_add93_fixp + (1)*main_add93_CAST_add118_float + (-1)*C3_main_add93_CAST_add118<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add93_CAST_add118
solver.Add( + (1)*main_add93_float + (1)*main_add93_CAST_add118_fixp + (-1)*C4_main_add93_CAST_add118<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add93_CAST_add118
solver.Add( + (1)*main_add93_fixp + (1)*main_add93_CAST_add118_double + (-1)*C5_main_add93_CAST_add118<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add93_CAST_add118
solver.Add( + (1)*main_add93_double + (1)*main_add93_CAST_add118_fixp + (-1)*C6_main_add93_CAST_add118<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add93_CAST_add118
solver.Add( + (1)*main_add93_float + (1)*main_add93_CAST_add118_double + (-1)*C7_main_add93_CAST_add118<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add93_CAST_add118
solver.Add( + (1)*main_add93_double + (1)*main_add93_CAST_add118_float + (-1)*C8_main_add93_CAST_add118<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add93_CAST_add118



#Constraint for cast for   %add118 = fadd double %add93, %mul117, !taffo.info !58, !taffo.initweight !57
main_mul117_CAST_add118_fixbits = solver.IntVar(0, 19, 'main_mul117_CAST_add118_fixbits')
main_mul117_CAST_add118_fixp = solver.IntVar(0, 1, 'main_mul117_CAST_add118_fixp')
main_mul117_CAST_add118_float = solver.IntVar(0, 1, 'main_mul117_CAST_add118_float')
main_mul117_CAST_add118_double = solver.IntVar(0, 1, 'main_mul117_CAST_add118_double')
solver.Add( + (1)*main_mul117_CAST_add118_fixp + (1)*main_mul117_CAST_add118_float + (1)*main_mul117_CAST_add118_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul117_CAST_add118_fixbits + (-10000)*main_mul117_CAST_add118_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C1_main_mul117_CAST_add118')
C2_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C2_main_mul117_CAST_add118')
solver.Add( + (1)*main_mul117_fixbits + (-1)*main_mul117_CAST_add118_fixbits + (-10000)*C1_main_mul117_CAST_add118<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul117_fixbits + (1)*main_mul117_CAST_add118_fixbits + (-10000)*C2_main_mul117_CAST_add118<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul117_CAST_add118
castCostObj +=  + (1)*C2_main_mul117_CAST_add118
C3_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C3_main_mul117_CAST_add118')
C4_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C4_main_mul117_CAST_add118')
C5_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C5_main_mul117_CAST_add118')
C6_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C6_main_mul117_CAST_add118')
C7_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C7_main_mul117_CAST_add118')
C8_main_mul117_CAST_add118 = solver.IntVar(0, 1, 'C8_main_mul117_CAST_add118')
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_CAST_add118_float + (-1)*C3_main_mul117_CAST_add118<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul117_CAST_add118
solver.Add( + (1)*main_mul117_float + (1)*main_mul117_CAST_add118_fixp + (-1)*C4_main_mul117_CAST_add118<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul117_CAST_add118
solver.Add( + (1)*main_mul117_fixp + (1)*main_mul117_CAST_add118_double + (-1)*C5_main_mul117_CAST_add118<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul117_CAST_add118
solver.Add( + (1)*main_mul117_double + (1)*main_mul117_CAST_add118_fixp + (-1)*C6_main_mul117_CAST_add118<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul117_CAST_add118
solver.Add( + (1)*main_mul117_float + (1)*main_mul117_CAST_add118_double + (-1)*C7_main_mul117_CAST_add118<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul117_CAST_add118
solver.Add( + (1)*main_mul117_double + (1)*main_mul117_CAST_add118_float + (-1)*C8_main_mul117_CAST_add118<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul117_CAST_add118



#Stuff for   %add118 = fadd double %add93, %mul117, !taffo.info !58, !taffo.initweight !57
main_add118_fixbits = solver.IntVar(0, 18, 'main_add118_fixbits')
main_add118_fixp = solver.IntVar(0, 1, 'main_add118_fixp')
main_add118_float = solver.IntVar(0, 1, 'main_add118_float')
main_add118_double = solver.IntVar(0, 1, 'main_add118_double')
main_add118_enob = solver.IntVar(-10000, 10000, 'main_add118_enob')
solver.Add( + (1)*main_add118_enob + (-1)*main_add118_fixbits + (10000)*main_add118_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add118_enob + (10000)*main_add118_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add118_enob + (10000)*main_add118_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add118_fixbits + (-10000)*main_add118_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_add118_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add118_enob
solver.Add( + (1)*main_add118_fixp + (1)*main_add118_float + (1)*main_add118_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add118_fixbits + (-10000)*main_add118_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add93_CAST_add118_fixp + (-1)*main_mul117_CAST_add118_fixp==0)    #fix equality
solver.Add( + (1)*main_add93_CAST_add118_float + (-1)*main_mul117_CAST_add118_float==0)    #float equality
solver.Add( + (1)*main_add93_CAST_add118_double + (-1)*main_mul117_CAST_add118_double==0)    #double equality
solver.Add( + (1)*main_add93_CAST_add118_fixbits + (-1)*main_mul117_CAST_add118_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add93_CAST_add118_fixp + (-1)*main_add118_fixp==0)    #fix equality
solver.Add( + (1)*main_add93_CAST_add118_float + (-1)*main_add118_float==0)    #float equality
solver.Add( + (1)*main_add93_CAST_add118_double + (-1)*main_add118_double==0)    #double equality
solver.Add( + (1)*main_add93_CAST_add118_fixbits + (-1)*main_add118_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add118_fixp
mathCostObj +=  + (2.33125)*main_add118_float
mathCostObj +=  + (2.72422)*main_add118_double
solver.Add( + (1)*main_add118_enob + (-1)*main_add93_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add118_enob + (-1)*main_mul117_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp9')
solver.Add( + (1)*A_enob_memphi_main_tmp9 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_1 = solver.IntVar(0, 1, 'main_main_tmp9_enob_1')
main_main_tmp9_enob_2 = solver.IntVar(0, 1, 'main_main_tmp9_enob_2')
main_main_tmp9_enob_3 = solver.IntVar(0, 1, 'main_main_tmp9_enob_3')
solver.Add( + (1)*main_main_tmp9_enob_1 + (1)*main_main_tmp9_enob_2 + (1)*main_main_tmp9_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp9 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp9_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add125 = fadd double %add118, %tmp9, !taffo.info !8, !taffo.initweight !31
main_add118_CAST_add125_fixbits = solver.IntVar(0, 18, 'main_add118_CAST_add125_fixbits')
main_add118_CAST_add125_fixp = solver.IntVar(0, 1, 'main_add118_CAST_add125_fixp')
main_add118_CAST_add125_float = solver.IntVar(0, 1, 'main_add118_CAST_add125_float')
main_add118_CAST_add125_double = solver.IntVar(0, 1, 'main_add118_CAST_add125_double')
solver.Add( + (1)*main_add118_CAST_add125_fixp + (1)*main_add118_CAST_add125_float + (1)*main_add118_CAST_add125_double==1)    #exactly 1 type
solver.Add( + (1)*main_add118_CAST_add125_fixbits + (-10000)*main_add118_CAST_add125_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C1_main_add118_CAST_add125')
C2_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C2_main_add118_CAST_add125')
solver.Add( + (1)*main_add118_fixbits + (-1)*main_add118_CAST_add125_fixbits + (-10000)*C1_main_add118_CAST_add125<=0)    #Shift cost 1
solver.Add( + (-1)*main_add118_fixbits + (1)*main_add118_CAST_add125_fixbits + (-10000)*C2_main_add118_CAST_add125<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add118_CAST_add125
castCostObj +=  + (1)*C2_main_add118_CAST_add125
C3_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C3_main_add118_CAST_add125')
C4_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C4_main_add118_CAST_add125')
C5_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C5_main_add118_CAST_add125')
C6_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C6_main_add118_CAST_add125')
C7_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C7_main_add118_CAST_add125')
C8_main_add118_CAST_add125 = solver.IntVar(0, 1, 'C8_main_add118_CAST_add125')
solver.Add( + (1)*main_add118_fixp + (1)*main_add118_CAST_add125_float + (-1)*C3_main_add118_CAST_add125<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add118_CAST_add125
solver.Add( + (1)*main_add118_float + (1)*main_add118_CAST_add125_fixp + (-1)*C4_main_add118_CAST_add125<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add118_CAST_add125
solver.Add( + (1)*main_add118_fixp + (1)*main_add118_CAST_add125_double + (-1)*C5_main_add118_CAST_add125<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add118_CAST_add125
solver.Add( + (1)*main_add118_double + (1)*main_add118_CAST_add125_fixp + (-1)*C6_main_add118_CAST_add125<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add118_CAST_add125
solver.Add( + (1)*main_add118_float + (1)*main_add118_CAST_add125_double + (-1)*C7_main_add118_CAST_add125<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add118_CAST_add125
solver.Add( + (1)*main_add118_double + (1)*main_add118_CAST_add125_float + (-1)*C8_main_add118_CAST_add125<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add118_CAST_add125



#Constraint for cast for   %add125 = fadd double %add118, %tmp9, !taffo.info !8, !taffo.initweight !31
A_CAST_add125_fixbits = solver.IntVar(0, 16, 'A_CAST_add125_fixbits')
A_CAST_add125_fixp = solver.IntVar(0, 1, 'A_CAST_add125_fixp')
A_CAST_add125_float = solver.IntVar(0, 1, 'A_CAST_add125_float')
A_CAST_add125_double = solver.IntVar(0, 1, 'A_CAST_add125_double')
solver.Add( + (1)*A_CAST_add125_fixp + (1)*A_CAST_add125_float + (1)*A_CAST_add125_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_add125_fixbits + (-10000)*A_CAST_add125_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_add125 = solver.IntVar(0, 1, 'C1_A_CAST_add125')
C2_A_CAST_add125 = solver.IntVar(0, 1, 'C2_A_CAST_add125')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_add125_fixbits + (-10000)*C1_A_CAST_add125<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_add125_fixbits + (-10000)*C2_A_CAST_add125<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_add125
castCostObj +=  + (1)*C2_A_CAST_add125
C3_A_CAST_add125 = solver.IntVar(0, 1, 'C3_A_CAST_add125')
C4_A_CAST_add125 = solver.IntVar(0, 1, 'C4_A_CAST_add125')
C5_A_CAST_add125 = solver.IntVar(0, 1, 'C5_A_CAST_add125')
C6_A_CAST_add125 = solver.IntVar(0, 1, 'C6_A_CAST_add125')
C7_A_CAST_add125 = solver.IntVar(0, 1, 'C7_A_CAST_add125')
C8_A_CAST_add125 = solver.IntVar(0, 1, 'C8_A_CAST_add125')
solver.Add( + (1)*A_fixp + (1)*A_CAST_add125_float + (-1)*C3_A_CAST_add125<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_add125
solver.Add( + (1)*A_float + (1)*A_CAST_add125_fixp + (-1)*C4_A_CAST_add125<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_add125
solver.Add( + (1)*A_fixp + (1)*A_CAST_add125_double + (-1)*C5_A_CAST_add125<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_add125
solver.Add( + (1)*A_double + (1)*A_CAST_add125_fixp + (-1)*C6_A_CAST_add125<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_add125
solver.Add( + (1)*A_float + (1)*A_CAST_add125_double + (-1)*C7_A_CAST_add125<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_add125
solver.Add( + (1)*A_double + (1)*A_CAST_add125_float + (-1)*C8_A_CAST_add125<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_add125



#Stuff for   %add125 = fadd double %add118, %tmp9, !taffo.info !8, !taffo.initweight !31
main_add125_fixbits = solver.IntVar(0, 17, 'main_add125_fixbits')
main_add125_fixp = solver.IntVar(0, 1, 'main_add125_fixp')
main_add125_float = solver.IntVar(0, 1, 'main_add125_float')
main_add125_double = solver.IntVar(0, 1, 'main_add125_double')
main_add125_enob = solver.IntVar(-10000, 10000, 'main_add125_enob')
solver.Add( + (1)*main_add125_enob + (-1)*main_add125_fixbits + (10000)*main_add125_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add125_enob + (10000)*main_add125_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add125_enob + (10000)*main_add125_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add125_fixbits + (-10000)*main_add125_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_add125_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add125_enob
solver.Add( + (1)*main_add125_fixp + (1)*main_add125_float + (1)*main_add125_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add125_fixbits + (-10000)*main_add125_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add118_CAST_add125_fixp + (-1)*A_CAST_add125_fixp==0)    #fix equality
solver.Add( + (1)*main_add118_CAST_add125_float + (-1)*A_CAST_add125_float==0)    #float equality
solver.Add( + (1)*main_add118_CAST_add125_double + (-1)*A_CAST_add125_double==0)    #double equality
solver.Add( + (1)*main_add118_CAST_add125_fixbits + (-1)*A_CAST_add125_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add118_CAST_add125_fixp + (-1)*main_add125_fixp==0)    #fix equality
solver.Add( + (1)*main_add118_CAST_add125_float + (-1)*main_add125_float==0)    #float equality
solver.Add( + (1)*main_add118_CAST_add125_double + (-1)*main_add125_double==0)    #double equality
solver.Add( + (1)*main_add118_CAST_add125_fixbits + (-1)*main_add125_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add125_fixp
mathCostObj +=  + (2.33125)*main_add125_float
mathCostObj +=  + (2.72422)*main_add125_double
solver.Add( + (1)*main_add125_enob + (-1)*main_add118_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add125_enob + (-1)*A_enob_memphi_main_tmp9<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add125, double* %arrayidx131, align 8, !taffo.info !37, !taffo.initweight !28
main_add125_CAST_store_fixbits = solver.IntVar(0, 17, 'main_add125_CAST_store_fixbits')
main_add125_CAST_store_fixp = solver.IntVar(0, 1, 'main_add125_CAST_store_fixp')
main_add125_CAST_store_float = solver.IntVar(0, 1, 'main_add125_CAST_store_float')
main_add125_CAST_store_double = solver.IntVar(0, 1, 'main_add125_CAST_store_double')
solver.Add( + (1)*main_add125_CAST_store_fixp + (1)*main_add125_CAST_store_float + (1)*main_add125_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add125_CAST_store_fixbits + (-10000)*main_add125_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add125_CAST_store = solver.IntVar(0, 1, 'C1_main_add125_CAST_store')
C2_main_add125_CAST_store = solver.IntVar(0, 1, 'C2_main_add125_CAST_store')
solver.Add( + (1)*main_add125_fixbits + (-1)*main_add125_CAST_store_fixbits + (-10000)*C1_main_add125_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add125_fixbits + (1)*main_add125_CAST_store_fixbits + (-10000)*C2_main_add125_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add125_CAST_store
castCostObj +=  + (1)*C2_main_add125_CAST_store
C3_main_add125_CAST_store = solver.IntVar(0, 1, 'C3_main_add125_CAST_store')
C4_main_add125_CAST_store = solver.IntVar(0, 1, 'C4_main_add125_CAST_store')
C5_main_add125_CAST_store = solver.IntVar(0, 1, 'C5_main_add125_CAST_store')
C6_main_add125_CAST_store = solver.IntVar(0, 1, 'C6_main_add125_CAST_store')
C7_main_add125_CAST_store = solver.IntVar(0, 1, 'C7_main_add125_CAST_store')
C8_main_add125_CAST_store = solver.IntVar(0, 1, 'C8_main_add125_CAST_store')
solver.Add( + (1)*main_add125_fixp + (1)*main_add125_CAST_store_float + (-1)*C3_main_add125_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add125_CAST_store
solver.Add( + (1)*main_add125_float + (1)*main_add125_CAST_store_fixp + (-1)*C4_main_add125_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add125_CAST_store
solver.Add( + (1)*main_add125_fixp + (1)*main_add125_CAST_store_double + (-1)*C5_main_add125_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add125_CAST_store
solver.Add( + (1)*main_add125_double + (1)*main_add125_CAST_store_fixp + (-1)*C6_main_add125_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add125_CAST_store
solver.Add( + (1)*main_add125_float + (1)*main_add125_CAST_store_double + (-1)*C7_main_add125_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add125_CAST_store
solver.Add( + (1)*main_add125_double + (1)*main_add125_CAST_store_float + (-1)*C8_main_add125_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add125_CAST_store
solver.Add( + (1)*B_fixp + (-1)*main_add125_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B_float + (-1)*main_add125_CAST_store_float==0)    #float equality
solver.Add( + (1)*B_double + (-1)*main_add125_CAST_store_double==0)    #double equality
solver.Add( + (1)*B_fixbits + (-1)*main_add125_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
B_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'B_enob_storeENOB_storeENOB')
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_enob_storeENOB_storeENOB + (-1)*main_add125_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp2 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp3 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp4 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp5 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp7 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp8 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp9 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp10')
solver.Add( + (1)*B_enob_memphi_main_tmp10 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_1 = solver.IntVar(0, 1, 'main_main_tmp10_enob_1')
main_main_tmp10_enob_2 = solver.IntVar(0, 1, 'main_main_tmp10_enob_2')
main_main_tmp10_enob_3 = solver.IntVar(0, 1, 'main_main_tmp10_enob_3')
solver.Add( + (1)*main_main_tmp10_enob_1 + (1)*main_main_tmp10_enob_2 + (1)*main_main_tmp10_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp10 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp10_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp10 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp11')
solver.Add( + (1)*B_enob_memphi_main_tmp11 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_1 = solver.IntVar(0, 1, 'main_main_tmp11_enob_1')
main_main_tmp11_enob_2 = solver.IntVar(0, 1, 'main_main_tmp11_enob_2')
main_main_tmp11_enob_3 = solver.IntVar(0, 1, 'main_main_tmp11_enob_3')
solver.Add( + (1)*main_main_tmp11_enob_1 + (1)*main_main_tmp11_enob_2 + (1)*main_main_tmp11_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp11 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp11_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp11 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_3<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__20_fixbits = solver.IntVar(0, 30, 'ConstantValue__20_fixbits')
ConstantValue__20_fixp = solver.IntVar(0, 1, 'ConstantValue__20_fixp')
ConstantValue__20_float = solver.IntVar(0, 1, 'ConstantValue__20_float')
ConstantValue__20_double = solver.IntVar(0, 1, 'ConstantValue__20_double')
ConstantValue__20_enob = solver.IntVar(-10000, 10000, 'ConstantValue__20_enob')
solver.Add( + (1)*ConstantValue__20_enob + (-1)*ConstantValue__20_fixbits + (10000)*ConstantValue__20_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_float + (1)*ConstantValue__20_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__21_fixbits = solver.IntVar(0, 30, 'ConstantValue__21_fixbits')
ConstantValue__21_fixp = solver.IntVar(0, 1, 'ConstantValue__21_fixp')
ConstantValue__21_float = solver.IntVar(0, 1, 'ConstantValue__21_float')
ConstantValue__21_double = solver.IntVar(0, 1, 'ConstantValue__21_double')
ConstantValue__21_enob = solver.IntVar(-10000, 10000, 'ConstantValue__21_enob')
solver.Add( + (1)*ConstantValue__21_enob + (-1)*ConstantValue__21_fixbits + (10000)*ConstantValue__21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__21_fixp + (1)*ConstantValue__21_float + (1)*ConstantValue__21_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__22_fixbits = solver.IntVar(0, 30, 'ConstantValue__22_fixbits')
ConstantValue__22_fixp = solver.IntVar(0, 1, 'ConstantValue__22_fixp')
ConstantValue__22_float = solver.IntVar(0, 1, 'ConstantValue__22_float')
ConstantValue__22_double = solver.IntVar(0, 1, 'ConstantValue__22_double')
ConstantValue__22_enob = solver.IntVar(-10000, 10000, 'ConstantValue__22_enob')
solver.Add( + (1)*ConstantValue__22_enob + (-1)*ConstantValue__22_fixbits + (10000)*ConstantValue__22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_float + (1)*ConstantValue__22_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul166 = fmul double 2.000000e+00, %tmp11, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
ConstantValue__22_CAST_mul166_fixbits = solver.IntVar(0, 30, 'ConstantValue__22_CAST_mul166_fixbits')
ConstantValue__22_CAST_mul166_fixp = solver.IntVar(0, 1, 'ConstantValue__22_CAST_mul166_fixp')
ConstantValue__22_CAST_mul166_float = solver.IntVar(0, 1, 'ConstantValue__22_CAST_mul166_float')
ConstantValue__22_CAST_mul166_double = solver.IntVar(0, 1, 'ConstantValue__22_CAST_mul166_double')
solver.Add( + (1)*ConstantValue__22_CAST_mul166_fixp + (1)*ConstantValue__22_CAST_mul166_float + (1)*ConstantValue__22_CAST_mul166_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__22_CAST_mul166_fixbits + (-10000)*ConstantValue__22_CAST_mul166_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C1_ConstantValue__22_CAST_mul166')
C2_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C2_ConstantValue__22_CAST_mul166')
solver.Add( + (1)*ConstantValue__22_fixbits + (-1)*ConstantValue__22_CAST_mul166_fixbits + (-10000)*C1_ConstantValue__22_CAST_mul166<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__22_fixbits + (1)*ConstantValue__22_CAST_mul166_fixbits + (-10000)*C2_ConstantValue__22_CAST_mul166<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__22_CAST_mul166
castCostObj +=  + (1)*C2_ConstantValue__22_CAST_mul166
C3_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C3_ConstantValue__22_CAST_mul166')
C4_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C4_ConstantValue__22_CAST_mul166')
C5_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C5_ConstantValue__22_CAST_mul166')
C6_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C6_ConstantValue__22_CAST_mul166')
C7_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C7_ConstantValue__22_CAST_mul166')
C8_ConstantValue__22_CAST_mul166 = solver.IntVar(0, 1, 'C8_ConstantValue__22_CAST_mul166')
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_CAST_mul166_float + (-1)*C3_ConstantValue__22_CAST_mul166<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__22_CAST_mul166
solver.Add( + (1)*ConstantValue__22_float + (1)*ConstantValue__22_CAST_mul166_fixp + (-1)*C4_ConstantValue__22_CAST_mul166<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__22_CAST_mul166
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_CAST_mul166_double + (-1)*C5_ConstantValue__22_CAST_mul166<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__22_CAST_mul166
solver.Add( + (1)*ConstantValue__22_double + (1)*ConstantValue__22_CAST_mul166_fixp + (-1)*C6_ConstantValue__22_CAST_mul166<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__22_CAST_mul166
solver.Add( + (1)*ConstantValue__22_float + (1)*ConstantValue__22_CAST_mul166_double + (-1)*C7_ConstantValue__22_CAST_mul166<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__22_CAST_mul166
solver.Add( + (1)*ConstantValue__22_double + (1)*ConstantValue__22_CAST_mul166_float + (-1)*C8_ConstantValue__22_CAST_mul166<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__22_CAST_mul166



#Constraint for cast for   %mul166 = fmul double 2.000000e+00, %tmp11, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
B_CAST_mul166_fixbits = solver.IntVar(0, 17, 'B_CAST_mul166_fixbits')
B_CAST_mul166_fixp = solver.IntVar(0, 1, 'B_CAST_mul166_fixp')
B_CAST_mul166_float = solver.IntVar(0, 1, 'B_CAST_mul166_float')
B_CAST_mul166_double = solver.IntVar(0, 1, 'B_CAST_mul166_double')
solver.Add( + (1)*B_CAST_mul166_fixp + (1)*B_CAST_mul166_float + (1)*B_CAST_mul166_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_mul166_fixbits + (-10000)*B_CAST_mul166_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_mul166 = solver.IntVar(0, 1, 'C1_B_CAST_mul166')
C2_B_CAST_mul166 = solver.IntVar(0, 1, 'C2_B_CAST_mul166')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_mul166_fixbits + (-10000)*C1_B_CAST_mul166<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_mul166_fixbits + (-10000)*C2_B_CAST_mul166<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_mul166
castCostObj +=  + (1)*C2_B_CAST_mul166
C3_B_CAST_mul166 = solver.IntVar(0, 1, 'C3_B_CAST_mul166')
C4_B_CAST_mul166 = solver.IntVar(0, 1, 'C4_B_CAST_mul166')
C5_B_CAST_mul166 = solver.IntVar(0, 1, 'C5_B_CAST_mul166')
C6_B_CAST_mul166 = solver.IntVar(0, 1, 'C6_B_CAST_mul166')
C7_B_CAST_mul166 = solver.IntVar(0, 1, 'C7_B_CAST_mul166')
C8_B_CAST_mul166 = solver.IntVar(0, 1, 'C8_B_CAST_mul166')
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul166_float + (-1)*C3_B_CAST_mul166<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_mul166
solver.Add( + (1)*B_float + (1)*B_CAST_mul166_fixp + (-1)*C4_B_CAST_mul166<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_mul166
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul166_double + (-1)*C5_B_CAST_mul166<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_mul166
solver.Add( + (1)*B_double + (1)*B_CAST_mul166_fixp + (-1)*C6_B_CAST_mul166<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_mul166
solver.Add( + (1)*B_float + (1)*B_CAST_mul166_double + (-1)*C7_B_CAST_mul166<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_mul166
solver.Add( + (1)*B_double + (1)*B_CAST_mul166_float + (-1)*C8_B_CAST_mul166<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_mul166



#Stuff for   %mul166 = fmul double 2.000000e+00, %tmp11, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
main_mul166_fixbits = solver.IntVar(0, 16, 'main_mul166_fixbits')
main_mul166_fixp = solver.IntVar(0, 1, 'main_mul166_fixp')
main_mul166_float = solver.IntVar(0, 1, 'main_mul166_float')
main_mul166_double = solver.IntVar(0, 1, 'main_mul166_double')
main_mul166_enob = solver.IntVar(-10000, 10000, 'main_mul166_enob')
solver.Add( + (1)*main_mul166_enob + (-1)*main_mul166_fixbits + (10000)*main_mul166_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul166_enob + (10000)*main_mul166_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul166_enob + (10000)*main_mul166_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul166_fixbits + (-10000)*main_mul166_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul166_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul166_enob
solver.Add( + (1)*main_mul166_fixp + (1)*main_mul166_float + (1)*main_mul166_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul166_fixbits + (-10000)*main_mul166_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__22_CAST_mul166_fixp + (-1)*B_CAST_mul166_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__22_CAST_mul166_float + (-1)*B_CAST_mul166_float==0)    #float equality
solver.Add( + (1)*ConstantValue__22_CAST_mul166_double + (-1)*B_CAST_mul166_double==0)    #double equality
solver.Add( + (1)*ConstantValue__22_CAST_mul166_fixp + (-1)*main_mul166_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__22_CAST_mul166_float + (-1)*main_mul166_float==0)    #float equality
solver.Add( + (1)*ConstantValue__22_CAST_mul166_double + (-1)*main_mul166_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul166_fixp
mathCostObj +=  + (2.64722)*main_mul166_float
mathCostObj +=  + (4.02255)*main_mul166_double
main_main_mul166_enob_1 = solver.IntVar(0, 1, 'main_main_mul166_enob_1')
main_main_mul166_enob_2 = solver.IntVar(0, 1, 'main_main_mul166_enob_2')
solver.Add( + (1)*main_main_mul166_enob_1 + (1)*main_main_mul166_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul166_enob + (-1)*B_enob_memphi_main_tmp11 + (-10000)*main_main_mul166_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul166_enob + (-1)*ConstantValue__20_enob + (-10000)*main_main_mul166_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub167 = fsub double %tmp10, %mul166, !taffo.info !62, !taffo.initweight !31
B_CAST_sub167_fixbits = solver.IntVar(0, 17, 'B_CAST_sub167_fixbits')
B_CAST_sub167_fixp = solver.IntVar(0, 1, 'B_CAST_sub167_fixp')
B_CAST_sub167_float = solver.IntVar(0, 1, 'B_CAST_sub167_float')
B_CAST_sub167_double = solver.IntVar(0, 1, 'B_CAST_sub167_double')
solver.Add( + (1)*B_CAST_sub167_fixp + (1)*B_CAST_sub167_float + (1)*B_CAST_sub167_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_sub167_fixbits + (-10000)*B_CAST_sub167_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_sub167 = solver.IntVar(0, 1, 'C1_B_CAST_sub167')
C2_B_CAST_sub167 = solver.IntVar(0, 1, 'C2_B_CAST_sub167')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_sub167_fixbits + (-10000)*C1_B_CAST_sub167<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_sub167_fixbits + (-10000)*C2_B_CAST_sub167<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_sub167
castCostObj +=  + (1)*C2_B_CAST_sub167
C3_B_CAST_sub167 = solver.IntVar(0, 1, 'C3_B_CAST_sub167')
C4_B_CAST_sub167 = solver.IntVar(0, 1, 'C4_B_CAST_sub167')
C5_B_CAST_sub167 = solver.IntVar(0, 1, 'C5_B_CAST_sub167')
C6_B_CAST_sub167 = solver.IntVar(0, 1, 'C6_B_CAST_sub167')
C7_B_CAST_sub167 = solver.IntVar(0, 1, 'C7_B_CAST_sub167')
C8_B_CAST_sub167 = solver.IntVar(0, 1, 'C8_B_CAST_sub167')
solver.Add( + (1)*B_fixp + (1)*B_CAST_sub167_float + (-1)*C3_B_CAST_sub167<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_sub167
solver.Add( + (1)*B_float + (1)*B_CAST_sub167_fixp + (-1)*C4_B_CAST_sub167<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_sub167
solver.Add( + (1)*B_fixp + (1)*B_CAST_sub167_double + (-1)*C5_B_CAST_sub167<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_sub167
solver.Add( + (1)*B_double + (1)*B_CAST_sub167_fixp + (-1)*C6_B_CAST_sub167<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_sub167
solver.Add( + (1)*B_float + (1)*B_CAST_sub167_double + (-1)*C7_B_CAST_sub167<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_sub167
solver.Add( + (1)*B_double + (1)*B_CAST_sub167_float + (-1)*C8_B_CAST_sub167<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_sub167



#Constraint for cast for   %sub167 = fsub double %tmp10, %mul166, !taffo.info !62, !taffo.initweight !31
main_mul166_CAST_sub167_fixbits = solver.IntVar(0, 16, 'main_mul166_CAST_sub167_fixbits')
main_mul166_CAST_sub167_fixp = solver.IntVar(0, 1, 'main_mul166_CAST_sub167_fixp')
main_mul166_CAST_sub167_float = solver.IntVar(0, 1, 'main_mul166_CAST_sub167_float')
main_mul166_CAST_sub167_double = solver.IntVar(0, 1, 'main_mul166_CAST_sub167_double')
solver.Add( + (1)*main_mul166_CAST_sub167_fixp + (1)*main_mul166_CAST_sub167_float + (1)*main_mul166_CAST_sub167_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul166_CAST_sub167_fixbits + (-10000)*main_mul166_CAST_sub167_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C1_main_mul166_CAST_sub167')
C2_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C2_main_mul166_CAST_sub167')
solver.Add( + (1)*main_mul166_fixbits + (-1)*main_mul166_CAST_sub167_fixbits + (-10000)*C1_main_mul166_CAST_sub167<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul166_fixbits + (1)*main_mul166_CAST_sub167_fixbits + (-10000)*C2_main_mul166_CAST_sub167<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul166_CAST_sub167
castCostObj +=  + (1)*C2_main_mul166_CAST_sub167
C3_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C3_main_mul166_CAST_sub167')
C4_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C4_main_mul166_CAST_sub167')
C5_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C5_main_mul166_CAST_sub167')
C6_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C6_main_mul166_CAST_sub167')
C7_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C7_main_mul166_CAST_sub167')
C8_main_mul166_CAST_sub167 = solver.IntVar(0, 1, 'C8_main_mul166_CAST_sub167')
solver.Add( + (1)*main_mul166_fixp + (1)*main_mul166_CAST_sub167_float + (-1)*C3_main_mul166_CAST_sub167<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul166_CAST_sub167
solver.Add( + (1)*main_mul166_float + (1)*main_mul166_CAST_sub167_fixp + (-1)*C4_main_mul166_CAST_sub167<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul166_CAST_sub167
solver.Add( + (1)*main_mul166_fixp + (1)*main_mul166_CAST_sub167_double + (-1)*C5_main_mul166_CAST_sub167<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul166_CAST_sub167
solver.Add( + (1)*main_mul166_double + (1)*main_mul166_CAST_sub167_fixp + (-1)*C6_main_mul166_CAST_sub167<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul166_CAST_sub167
solver.Add( + (1)*main_mul166_float + (1)*main_mul166_CAST_sub167_double + (-1)*C7_main_mul166_CAST_sub167<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul166_CAST_sub167
solver.Add( + (1)*main_mul166_double + (1)*main_mul166_CAST_sub167_float + (-1)*C8_main_mul166_CAST_sub167<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul166_CAST_sub167



#Stuff for   %sub167 = fsub double %tmp10, %mul166, !taffo.info !62, !taffo.initweight !31
main_sub167_fixbits = solver.IntVar(0, 16, 'main_sub167_fixbits')
main_sub167_fixp = solver.IntVar(0, 1, 'main_sub167_fixp')
main_sub167_float = solver.IntVar(0, 1, 'main_sub167_float')
main_sub167_double = solver.IntVar(0, 1, 'main_sub167_double')
main_sub167_enob = solver.IntVar(-10000, 10000, 'main_sub167_enob')
solver.Add( + (1)*main_sub167_enob + (-1)*main_sub167_fixbits + (10000)*main_sub167_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub167_enob + (10000)*main_sub167_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub167_enob + (10000)*main_sub167_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub167_fixbits + (-10000)*main_sub167_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_sub167_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub167_enob
solver.Add( + (1)*main_sub167_fixp + (1)*main_sub167_float + (1)*main_sub167_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub167_fixbits + (-10000)*main_sub167_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*B_CAST_sub167_fixp + (-1)*main_mul166_CAST_sub167_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_sub167_float + (-1)*main_mul166_CAST_sub167_float==0)    #float equality
solver.Add( + (1)*B_CAST_sub167_double + (-1)*main_mul166_CAST_sub167_double==0)    #double equality
solver.Add( + (1)*B_CAST_sub167_fixbits + (-1)*main_mul166_CAST_sub167_fixbits==0)    #same fractional bit
solver.Add( + (1)*B_CAST_sub167_fixp + (-1)*main_sub167_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_sub167_float + (-1)*main_sub167_float==0)    #float equality
solver.Add( + (1)*B_CAST_sub167_double + (-1)*main_sub167_double==0)    #double equality
solver.Add( + (1)*B_CAST_sub167_fixbits + (-1)*main_sub167_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub167_fixp
mathCostObj +=  + (2.33125)*main_sub167_float
mathCostObj +=  + (2.72422)*main_sub167_double
solver.Add( + (1)*main_sub167_enob + (-1)*B_enob_memphi_main_tmp10<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub167_enob + (-1)*main_mul166_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp12')
solver.Add( + (1)*B_enob_memphi_main_tmp12 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp12_enob_1 = solver.IntVar(0, 1, 'main_main_tmp12_enob_1')
main_main_tmp12_enob_2 = solver.IntVar(0, 1, 'main_main_tmp12_enob_2')
main_main_tmp12_enob_3 = solver.IntVar(0, 1, 'main_main_tmp12_enob_3')
solver.Add( + (1)*main_main_tmp12_enob_1 + (1)*main_main_tmp12_enob_2 + (1)*main_main_tmp12_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp12 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp12_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp12 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add175 = fadd double %sub167, %tmp12, !taffo.info !64, !taffo.initweight !31
main_sub167_CAST_add175_fixbits = solver.IntVar(0, 16, 'main_sub167_CAST_add175_fixbits')
main_sub167_CAST_add175_fixp = solver.IntVar(0, 1, 'main_sub167_CAST_add175_fixp')
main_sub167_CAST_add175_float = solver.IntVar(0, 1, 'main_sub167_CAST_add175_float')
main_sub167_CAST_add175_double = solver.IntVar(0, 1, 'main_sub167_CAST_add175_double')
solver.Add( + (1)*main_sub167_CAST_add175_fixp + (1)*main_sub167_CAST_add175_float + (1)*main_sub167_CAST_add175_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub167_CAST_add175_fixbits + (-10000)*main_sub167_CAST_add175_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C1_main_sub167_CAST_add175')
C2_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C2_main_sub167_CAST_add175')
solver.Add( + (1)*main_sub167_fixbits + (-1)*main_sub167_CAST_add175_fixbits + (-10000)*C1_main_sub167_CAST_add175<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub167_fixbits + (1)*main_sub167_CAST_add175_fixbits + (-10000)*C2_main_sub167_CAST_add175<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub167_CAST_add175
castCostObj +=  + (1)*C2_main_sub167_CAST_add175
C3_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C3_main_sub167_CAST_add175')
C4_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C4_main_sub167_CAST_add175')
C5_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C5_main_sub167_CAST_add175')
C6_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C6_main_sub167_CAST_add175')
C7_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C7_main_sub167_CAST_add175')
C8_main_sub167_CAST_add175 = solver.IntVar(0, 1, 'C8_main_sub167_CAST_add175')
solver.Add( + (1)*main_sub167_fixp + (1)*main_sub167_CAST_add175_float + (-1)*C3_main_sub167_CAST_add175<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub167_CAST_add175
solver.Add( + (1)*main_sub167_float + (1)*main_sub167_CAST_add175_fixp + (-1)*C4_main_sub167_CAST_add175<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub167_CAST_add175
solver.Add( + (1)*main_sub167_fixp + (1)*main_sub167_CAST_add175_double + (-1)*C5_main_sub167_CAST_add175<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub167_CAST_add175
solver.Add( + (1)*main_sub167_double + (1)*main_sub167_CAST_add175_fixp + (-1)*C6_main_sub167_CAST_add175<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub167_CAST_add175
solver.Add( + (1)*main_sub167_float + (1)*main_sub167_CAST_add175_double + (-1)*C7_main_sub167_CAST_add175<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub167_CAST_add175
solver.Add( + (1)*main_sub167_double + (1)*main_sub167_CAST_add175_float + (-1)*C8_main_sub167_CAST_add175<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub167_CAST_add175



#Constraint for cast for   %add175 = fadd double %sub167, %tmp12, !taffo.info !64, !taffo.initweight !31
B_CAST_add175_fixbits = solver.IntVar(0, 17, 'B_CAST_add175_fixbits')
B_CAST_add175_fixp = solver.IntVar(0, 1, 'B_CAST_add175_fixp')
B_CAST_add175_float = solver.IntVar(0, 1, 'B_CAST_add175_float')
B_CAST_add175_double = solver.IntVar(0, 1, 'B_CAST_add175_double')
solver.Add( + (1)*B_CAST_add175_fixp + (1)*B_CAST_add175_float + (1)*B_CAST_add175_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_add175_fixbits + (-10000)*B_CAST_add175_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_add175 = solver.IntVar(0, 1, 'C1_B_CAST_add175')
C2_B_CAST_add175 = solver.IntVar(0, 1, 'C2_B_CAST_add175')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_add175_fixbits + (-10000)*C1_B_CAST_add175<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_add175_fixbits + (-10000)*C2_B_CAST_add175<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_add175
castCostObj +=  + (1)*C2_B_CAST_add175
C3_B_CAST_add175 = solver.IntVar(0, 1, 'C3_B_CAST_add175')
C4_B_CAST_add175 = solver.IntVar(0, 1, 'C4_B_CAST_add175')
C5_B_CAST_add175 = solver.IntVar(0, 1, 'C5_B_CAST_add175')
C6_B_CAST_add175 = solver.IntVar(0, 1, 'C6_B_CAST_add175')
C7_B_CAST_add175 = solver.IntVar(0, 1, 'C7_B_CAST_add175')
C8_B_CAST_add175 = solver.IntVar(0, 1, 'C8_B_CAST_add175')
solver.Add( + (1)*B_fixp + (1)*B_CAST_add175_float + (-1)*C3_B_CAST_add175<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_add175
solver.Add( + (1)*B_float + (1)*B_CAST_add175_fixp + (-1)*C4_B_CAST_add175<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_add175
solver.Add( + (1)*B_fixp + (1)*B_CAST_add175_double + (-1)*C5_B_CAST_add175<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_add175
solver.Add( + (1)*B_double + (1)*B_CAST_add175_fixp + (-1)*C6_B_CAST_add175<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_add175
solver.Add( + (1)*B_float + (1)*B_CAST_add175_double + (-1)*C7_B_CAST_add175<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_add175
solver.Add( + (1)*B_double + (1)*B_CAST_add175_float + (-1)*C8_B_CAST_add175<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_add175



#Stuff for   %add175 = fadd double %sub167, %tmp12, !taffo.info !64, !taffo.initweight !31
main_add175_fixbits = solver.IntVar(0, 15, 'main_add175_fixbits')
main_add175_fixp = solver.IntVar(0, 1, 'main_add175_fixp')
main_add175_float = solver.IntVar(0, 1, 'main_add175_float')
main_add175_double = solver.IntVar(0, 1, 'main_add175_double')
main_add175_enob = solver.IntVar(-10000, 10000, 'main_add175_enob')
solver.Add( + (1)*main_add175_enob + (-1)*main_add175_fixbits + (10000)*main_add175_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add175_enob + (10000)*main_add175_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add175_enob + (10000)*main_add175_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add175_fixbits + (-10000)*main_add175_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add175_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add175_enob
solver.Add( + (1)*main_add175_fixp + (1)*main_add175_float + (1)*main_add175_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add175_fixbits + (-10000)*main_add175_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub167_CAST_add175_fixp + (-1)*B_CAST_add175_fixp==0)    #fix equality
solver.Add( + (1)*main_sub167_CAST_add175_float + (-1)*B_CAST_add175_float==0)    #float equality
solver.Add( + (1)*main_sub167_CAST_add175_double + (-1)*B_CAST_add175_double==0)    #double equality
solver.Add( + (1)*main_sub167_CAST_add175_fixbits + (-1)*B_CAST_add175_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub167_CAST_add175_fixp + (-1)*main_add175_fixp==0)    #fix equality
solver.Add( + (1)*main_sub167_CAST_add175_float + (-1)*main_add175_float==0)    #float equality
solver.Add( + (1)*main_sub167_CAST_add175_double + (-1)*main_add175_double==0)    #double equality
solver.Add( + (1)*main_sub167_CAST_add175_fixbits + (-1)*main_add175_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add175_fixp
mathCostObj +=  + (2.33125)*main_add175_float
mathCostObj +=  + (2.72422)*main_add175_double
solver.Add( + (1)*main_add175_enob + (-1)*main_sub167_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add175_enob + (-1)*B_enob_memphi_main_tmp12<=0)    #Enob propagation in sum second addend



#Stuff for double 1.250000e-01
ConstantValue__23_fixbits = solver.IntVar(0, 31, 'ConstantValue__23_fixbits')
ConstantValue__23_fixp = solver.IntVar(0, 1, 'ConstantValue__23_fixp')
ConstantValue__23_float = solver.IntVar(0, 1, 'ConstantValue__23_float')
ConstantValue__23_double = solver.IntVar(0, 1, 'ConstantValue__23_double')
ConstantValue__23_enob = solver.IntVar(-10000, 10000, 'ConstantValue__23_enob')
solver.Add( + (1)*ConstantValue__23_enob + (-1)*ConstantValue__23_fixbits + (10000)*ConstantValue__23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_float + (1)*ConstantValue__23_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__24_fixbits = solver.IntVar(0, 31, 'ConstantValue__24_fixbits')
ConstantValue__24_fixp = solver.IntVar(0, 1, 'ConstantValue__24_fixp')
ConstantValue__24_float = solver.IntVar(0, 1, 'ConstantValue__24_float')
ConstantValue__24_double = solver.IntVar(0, 1, 'ConstantValue__24_double')
ConstantValue__24_enob = solver.IntVar(-10000, 10000, 'ConstantValue__24_enob')
solver.Add( + (1)*ConstantValue__24_enob + (-1)*ConstantValue__24_fixbits + (10000)*ConstantValue__24_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__24_fixp + (1)*ConstantValue__24_float + (1)*ConstantValue__24_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__25_fixbits = solver.IntVar(0, 31, 'ConstantValue__25_fixbits')
ConstantValue__25_fixp = solver.IntVar(0, 1, 'ConstantValue__25_fixp')
ConstantValue__25_float = solver.IntVar(0, 1, 'ConstantValue__25_float')
ConstantValue__25_double = solver.IntVar(0, 1, 'ConstantValue__25_double')
ConstantValue__25_enob = solver.IntVar(-10000, 10000, 'ConstantValue__25_enob')
solver.Add( + (1)*ConstantValue__25_enob + (-1)*ConstantValue__25_fixbits + (10000)*ConstantValue__25_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__25_enob + (10000)*ConstantValue__25_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__25_enob + (10000)*ConstantValue__25_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__25_fixbits + (-10000)*ConstantValue__25_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_float + (1)*ConstantValue__25_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__25_fixbits + (-10000)*ConstantValue__25_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul176 = fmul double 1.250000e-01, %add175, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
ConstantValue__25_CAST_mul176_fixbits = solver.IntVar(0, 31, 'ConstantValue__25_CAST_mul176_fixbits')
ConstantValue__25_CAST_mul176_fixp = solver.IntVar(0, 1, 'ConstantValue__25_CAST_mul176_fixp')
ConstantValue__25_CAST_mul176_float = solver.IntVar(0, 1, 'ConstantValue__25_CAST_mul176_float')
ConstantValue__25_CAST_mul176_double = solver.IntVar(0, 1, 'ConstantValue__25_CAST_mul176_double')
solver.Add( + (1)*ConstantValue__25_CAST_mul176_fixp + (1)*ConstantValue__25_CAST_mul176_float + (1)*ConstantValue__25_CAST_mul176_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__25_CAST_mul176_fixbits + (-10000)*ConstantValue__25_CAST_mul176_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C1_ConstantValue__25_CAST_mul176')
C2_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C2_ConstantValue__25_CAST_mul176')
solver.Add( + (1)*ConstantValue__25_fixbits + (-1)*ConstantValue__25_CAST_mul176_fixbits + (-10000)*C1_ConstantValue__25_CAST_mul176<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__25_fixbits + (1)*ConstantValue__25_CAST_mul176_fixbits + (-10000)*C2_ConstantValue__25_CAST_mul176<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__25_CAST_mul176
castCostObj +=  + (1)*C2_ConstantValue__25_CAST_mul176
C3_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C3_ConstantValue__25_CAST_mul176')
C4_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C4_ConstantValue__25_CAST_mul176')
C5_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C5_ConstantValue__25_CAST_mul176')
C6_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C6_ConstantValue__25_CAST_mul176')
C7_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C7_ConstantValue__25_CAST_mul176')
C8_ConstantValue__25_CAST_mul176 = solver.IntVar(0, 1, 'C8_ConstantValue__25_CAST_mul176')
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_CAST_mul176_float + (-1)*C3_ConstantValue__25_CAST_mul176<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__25_CAST_mul176
solver.Add( + (1)*ConstantValue__25_float + (1)*ConstantValue__25_CAST_mul176_fixp + (-1)*C4_ConstantValue__25_CAST_mul176<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__25_CAST_mul176
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_CAST_mul176_double + (-1)*C5_ConstantValue__25_CAST_mul176<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__25_CAST_mul176
solver.Add( + (1)*ConstantValue__25_double + (1)*ConstantValue__25_CAST_mul176_fixp + (-1)*C6_ConstantValue__25_CAST_mul176<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__25_CAST_mul176
solver.Add( + (1)*ConstantValue__25_float + (1)*ConstantValue__25_CAST_mul176_double + (-1)*C7_ConstantValue__25_CAST_mul176<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__25_CAST_mul176
solver.Add( + (1)*ConstantValue__25_double + (1)*ConstantValue__25_CAST_mul176_float + (-1)*C8_ConstantValue__25_CAST_mul176<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__25_CAST_mul176



#Constraint for cast for   %mul176 = fmul double 1.250000e-01, %add175, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
main_add175_CAST_mul176_fixbits = solver.IntVar(0, 15, 'main_add175_CAST_mul176_fixbits')
main_add175_CAST_mul176_fixp = solver.IntVar(0, 1, 'main_add175_CAST_mul176_fixp')
main_add175_CAST_mul176_float = solver.IntVar(0, 1, 'main_add175_CAST_mul176_float')
main_add175_CAST_mul176_double = solver.IntVar(0, 1, 'main_add175_CAST_mul176_double')
solver.Add( + (1)*main_add175_CAST_mul176_fixp + (1)*main_add175_CAST_mul176_float + (1)*main_add175_CAST_mul176_double==1)    #exactly 1 type
solver.Add( + (1)*main_add175_CAST_mul176_fixbits + (-10000)*main_add175_CAST_mul176_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C1_main_add175_CAST_mul176')
C2_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C2_main_add175_CAST_mul176')
solver.Add( + (1)*main_add175_fixbits + (-1)*main_add175_CAST_mul176_fixbits + (-10000)*C1_main_add175_CAST_mul176<=0)    #Shift cost 1
solver.Add( + (-1)*main_add175_fixbits + (1)*main_add175_CAST_mul176_fixbits + (-10000)*C2_main_add175_CAST_mul176<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add175_CAST_mul176
castCostObj +=  + (1)*C2_main_add175_CAST_mul176
C3_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C3_main_add175_CAST_mul176')
C4_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C4_main_add175_CAST_mul176')
C5_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C5_main_add175_CAST_mul176')
C6_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C6_main_add175_CAST_mul176')
C7_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C7_main_add175_CAST_mul176')
C8_main_add175_CAST_mul176 = solver.IntVar(0, 1, 'C8_main_add175_CAST_mul176')
solver.Add( + (1)*main_add175_fixp + (1)*main_add175_CAST_mul176_float + (-1)*C3_main_add175_CAST_mul176<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add175_CAST_mul176
solver.Add( + (1)*main_add175_float + (1)*main_add175_CAST_mul176_fixp + (-1)*C4_main_add175_CAST_mul176<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add175_CAST_mul176
solver.Add( + (1)*main_add175_fixp + (1)*main_add175_CAST_mul176_double + (-1)*C5_main_add175_CAST_mul176<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add175_CAST_mul176
solver.Add( + (1)*main_add175_double + (1)*main_add175_CAST_mul176_fixp + (-1)*C6_main_add175_CAST_mul176<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add175_CAST_mul176
solver.Add( + (1)*main_add175_float + (1)*main_add175_CAST_mul176_double + (-1)*C7_main_add175_CAST_mul176<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add175_CAST_mul176
solver.Add( + (1)*main_add175_double + (1)*main_add175_CAST_mul176_float + (-1)*C8_main_add175_CAST_mul176<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add175_CAST_mul176



#Stuff for   %mul176 = fmul double 1.250000e-01, %add175, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
main_mul176_fixbits = solver.IntVar(0, 18, 'main_mul176_fixbits')
main_mul176_fixp = solver.IntVar(0, 1, 'main_mul176_fixp')
main_mul176_float = solver.IntVar(0, 1, 'main_mul176_float')
main_mul176_double = solver.IntVar(0, 1, 'main_mul176_double')
main_mul176_enob = solver.IntVar(-10000, 10000, 'main_mul176_enob')
solver.Add( + (1)*main_mul176_enob + (-1)*main_mul176_fixbits + (10000)*main_mul176_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul176_enob + (10000)*main_mul176_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul176_enob + (10000)*main_mul176_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul176_fixbits + (-10000)*main_mul176_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_mul176_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul176_enob
solver.Add( + (1)*main_mul176_fixp + (1)*main_mul176_float + (1)*main_mul176_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul176_fixbits + (-10000)*main_mul176_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__25_CAST_mul176_fixp + (-1)*main_add175_CAST_mul176_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__25_CAST_mul176_float + (-1)*main_add175_CAST_mul176_float==0)    #float equality
solver.Add( + (1)*ConstantValue__25_CAST_mul176_double + (-1)*main_add175_CAST_mul176_double==0)    #double equality
solver.Add( + (1)*ConstantValue__25_CAST_mul176_fixp + (-1)*main_mul176_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__25_CAST_mul176_float + (-1)*main_mul176_float==0)    #float equality
solver.Add( + (1)*ConstantValue__25_CAST_mul176_double + (-1)*main_mul176_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul176_fixp
mathCostObj +=  + (2.64722)*main_mul176_float
mathCostObj +=  + (4.02255)*main_mul176_double
main_main_mul176_enob_1 = solver.IntVar(0, 1, 'main_main_mul176_enob_1')
main_main_mul176_enob_2 = solver.IntVar(0, 1, 'main_main_mul176_enob_2')
solver.Add( + (1)*main_main_mul176_enob_1 + (1)*main_main_mul176_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul176_enob + (-1)*main_add175_enob + (-10000)*main_main_mul176_enob_1<=3)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul176_enob + (-1)*ConstantValue__23_enob + (-10000)*main_main_mul176_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp13 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp13')
solver.Add( + (1)*B_enob_memphi_main_tmp13 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp13_enob_1 = solver.IntVar(0, 1, 'main_main_tmp13_enob_1')
main_main_tmp13_enob_2 = solver.IntVar(0, 1, 'main_main_tmp13_enob_2')
main_main_tmp13_enob_3 = solver.IntVar(0, 1, 'main_main_tmp13_enob_3')
solver.Add( + (1)*main_main_tmp13_enob_1 + (1)*main_main_tmp13_enob_2 + (1)*main_main_tmp13_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp13 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp13_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp13 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp14 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp14')
solver.Add( + (1)*B_enob_memphi_main_tmp14 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp14_enob_1 = solver.IntVar(0, 1, 'main_main_tmp14_enob_1')
main_main_tmp14_enob_2 = solver.IntVar(0, 1, 'main_main_tmp14_enob_2')
main_main_tmp14_enob_3 = solver.IntVar(0, 1, 'main_main_tmp14_enob_3')
solver.Add( + (1)*main_main_tmp14_enob_1 + (1)*main_main_tmp14_enob_2 + (1)*main_main_tmp14_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp14 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp14_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp14 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp14_enob_3<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__26_fixbits = solver.IntVar(0, 30, 'ConstantValue__26_fixbits')
ConstantValue__26_fixp = solver.IntVar(0, 1, 'ConstantValue__26_fixp')
ConstantValue__26_float = solver.IntVar(0, 1, 'ConstantValue__26_float')
ConstantValue__26_double = solver.IntVar(0, 1, 'ConstantValue__26_double')
ConstantValue__26_enob = solver.IntVar(-10000, 10000, 'ConstantValue__26_enob')
solver.Add( + (1)*ConstantValue__26_enob + (-1)*ConstantValue__26_fixbits + (10000)*ConstantValue__26_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__26_fixp + (1)*ConstantValue__26_float + (1)*ConstantValue__26_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__27_fixbits = solver.IntVar(0, 30, 'ConstantValue__27_fixbits')
ConstantValue__27_fixp = solver.IntVar(0, 1, 'ConstantValue__27_fixp')
ConstantValue__27_float = solver.IntVar(0, 1, 'ConstantValue__27_float')
ConstantValue__27_double = solver.IntVar(0, 1, 'ConstantValue__27_double')
ConstantValue__27_enob = solver.IntVar(-10000, 10000, 'ConstantValue__27_enob')
solver.Add( + (1)*ConstantValue__27_enob + (-1)*ConstantValue__27_fixbits + (10000)*ConstantValue__27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__27_fixp + (1)*ConstantValue__27_float + (1)*ConstantValue__27_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__28_fixbits = solver.IntVar(0, 30, 'ConstantValue__28_fixbits')
ConstantValue__28_fixp = solver.IntVar(0, 1, 'ConstantValue__28_fixp')
ConstantValue__28_float = solver.IntVar(0, 1, 'ConstantValue__28_float')
ConstantValue__28_double = solver.IntVar(0, 1, 'ConstantValue__28_double')
ConstantValue__28_enob = solver.IntVar(-10000, 10000, 'ConstantValue__28_enob')
solver.Add( + (1)*ConstantValue__28_enob + (-1)*ConstantValue__28_fixbits + (10000)*ConstantValue__28_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_float + (1)*ConstantValue__28_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul190 = fmul double 2.000000e+00, %tmp14, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
ConstantValue__28_CAST_mul190_fixbits = solver.IntVar(0, 30, 'ConstantValue__28_CAST_mul190_fixbits')
ConstantValue__28_CAST_mul190_fixp = solver.IntVar(0, 1, 'ConstantValue__28_CAST_mul190_fixp')
ConstantValue__28_CAST_mul190_float = solver.IntVar(0, 1, 'ConstantValue__28_CAST_mul190_float')
ConstantValue__28_CAST_mul190_double = solver.IntVar(0, 1, 'ConstantValue__28_CAST_mul190_double')
solver.Add( + (1)*ConstantValue__28_CAST_mul190_fixp + (1)*ConstantValue__28_CAST_mul190_float + (1)*ConstantValue__28_CAST_mul190_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__28_CAST_mul190_fixbits + (-10000)*ConstantValue__28_CAST_mul190_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C1_ConstantValue__28_CAST_mul190')
C2_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C2_ConstantValue__28_CAST_mul190')
solver.Add( + (1)*ConstantValue__28_fixbits + (-1)*ConstantValue__28_CAST_mul190_fixbits + (-10000)*C1_ConstantValue__28_CAST_mul190<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__28_fixbits + (1)*ConstantValue__28_CAST_mul190_fixbits + (-10000)*C2_ConstantValue__28_CAST_mul190<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__28_CAST_mul190
castCostObj +=  + (1)*C2_ConstantValue__28_CAST_mul190
C3_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C3_ConstantValue__28_CAST_mul190')
C4_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C4_ConstantValue__28_CAST_mul190')
C5_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C5_ConstantValue__28_CAST_mul190')
C6_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C6_ConstantValue__28_CAST_mul190')
C7_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C7_ConstantValue__28_CAST_mul190')
C8_ConstantValue__28_CAST_mul190 = solver.IntVar(0, 1, 'C8_ConstantValue__28_CAST_mul190')
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_CAST_mul190_float + (-1)*C3_ConstantValue__28_CAST_mul190<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__28_CAST_mul190
solver.Add( + (1)*ConstantValue__28_float + (1)*ConstantValue__28_CAST_mul190_fixp + (-1)*C4_ConstantValue__28_CAST_mul190<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__28_CAST_mul190
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_CAST_mul190_double + (-1)*C5_ConstantValue__28_CAST_mul190<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__28_CAST_mul190
solver.Add( + (1)*ConstantValue__28_double + (1)*ConstantValue__28_CAST_mul190_fixp + (-1)*C6_ConstantValue__28_CAST_mul190<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__28_CAST_mul190
solver.Add( + (1)*ConstantValue__28_float + (1)*ConstantValue__28_CAST_mul190_double + (-1)*C7_ConstantValue__28_CAST_mul190<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__28_CAST_mul190
solver.Add( + (1)*ConstantValue__28_double + (1)*ConstantValue__28_CAST_mul190_float + (-1)*C8_ConstantValue__28_CAST_mul190<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__28_CAST_mul190



#Constraint for cast for   %mul190 = fmul double 2.000000e+00, %tmp14, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
B_CAST_mul190_fixbits = solver.IntVar(0, 17, 'B_CAST_mul190_fixbits')
B_CAST_mul190_fixp = solver.IntVar(0, 1, 'B_CAST_mul190_fixp')
B_CAST_mul190_float = solver.IntVar(0, 1, 'B_CAST_mul190_float')
B_CAST_mul190_double = solver.IntVar(0, 1, 'B_CAST_mul190_double')
solver.Add( + (1)*B_CAST_mul190_fixp + (1)*B_CAST_mul190_float + (1)*B_CAST_mul190_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_mul190_fixbits + (-10000)*B_CAST_mul190_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_mul190 = solver.IntVar(0, 1, 'C1_B_CAST_mul190')
C2_B_CAST_mul190 = solver.IntVar(0, 1, 'C2_B_CAST_mul190')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_mul190_fixbits + (-10000)*C1_B_CAST_mul190<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_mul190_fixbits + (-10000)*C2_B_CAST_mul190<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_mul190
castCostObj +=  + (1)*C2_B_CAST_mul190
C3_B_CAST_mul190 = solver.IntVar(0, 1, 'C3_B_CAST_mul190')
C4_B_CAST_mul190 = solver.IntVar(0, 1, 'C4_B_CAST_mul190')
C5_B_CAST_mul190 = solver.IntVar(0, 1, 'C5_B_CAST_mul190')
C6_B_CAST_mul190 = solver.IntVar(0, 1, 'C6_B_CAST_mul190')
C7_B_CAST_mul190 = solver.IntVar(0, 1, 'C7_B_CAST_mul190')
C8_B_CAST_mul190 = solver.IntVar(0, 1, 'C8_B_CAST_mul190')
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul190_float + (-1)*C3_B_CAST_mul190<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_mul190
solver.Add( + (1)*B_float + (1)*B_CAST_mul190_fixp + (-1)*C4_B_CAST_mul190<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_mul190
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul190_double + (-1)*C5_B_CAST_mul190<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_mul190
solver.Add( + (1)*B_double + (1)*B_CAST_mul190_fixp + (-1)*C6_B_CAST_mul190<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_mul190
solver.Add( + (1)*B_float + (1)*B_CAST_mul190_double + (-1)*C7_B_CAST_mul190<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_mul190
solver.Add( + (1)*B_double + (1)*B_CAST_mul190_float + (-1)*C8_B_CAST_mul190<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_mul190



#Stuff for   %mul190 = fmul double 2.000000e+00, %tmp14, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
main_mul190_fixbits = solver.IntVar(0, 16, 'main_mul190_fixbits')
main_mul190_fixp = solver.IntVar(0, 1, 'main_mul190_fixp')
main_mul190_float = solver.IntVar(0, 1, 'main_mul190_float')
main_mul190_double = solver.IntVar(0, 1, 'main_mul190_double')
main_mul190_enob = solver.IntVar(-10000, 10000, 'main_mul190_enob')
solver.Add( + (1)*main_mul190_enob + (-1)*main_mul190_fixbits + (10000)*main_mul190_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul190_enob + (10000)*main_mul190_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul190_enob + (10000)*main_mul190_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul190_fixbits + (-10000)*main_mul190_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul190_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul190_enob
solver.Add( + (1)*main_mul190_fixp + (1)*main_mul190_float + (1)*main_mul190_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul190_fixbits + (-10000)*main_mul190_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__28_CAST_mul190_fixp + (-1)*B_CAST_mul190_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__28_CAST_mul190_float + (-1)*B_CAST_mul190_float==0)    #float equality
solver.Add( + (1)*ConstantValue__28_CAST_mul190_double + (-1)*B_CAST_mul190_double==0)    #double equality
solver.Add( + (1)*ConstantValue__28_CAST_mul190_fixp + (-1)*main_mul190_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__28_CAST_mul190_float + (-1)*main_mul190_float==0)    #float equality
solver.Add( + (1)*ConstantValue__28_CAST_mul190_double + (-1)*main_mul190_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul190_fixp
mathCostObj +=  + (2.64722)*main_mul190_float
mathCostObj +=  + (4.02255)*main_mul190_double
main_main_mul190_enob_1 = solver.IntVar(0, 1, 'main_main_mul190_enob_1')
main_main_mul190_enob_2 = solver.IntVar(0, 1, 'main_main_mul190_enob_2')
solver.Add( + (1)*main_main_mul190_enob_1 + (1)*main_main_mul190_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul190_enob + (-1)*B_enob_memphi_main_tmp14 + (-10000)*main_main_mul190_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul190_enob + (-1)*ConstantValue__26_enob + (-10000)*main_main_mul190_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub191 = fsub double %tmp13, %mul190, !taffo.info !62, !taffo.initweight !31
B_CAST_sub191_fixbits = solver.IntVar(0, 17, 'B_CAST_sub191_fixbits')
B_CAST_sub191_fixp = solver.IntVar(0, 1, 'B_CAST_sub191_fixp')
B_CAST_sub191_float = solver.IntVar(0, 1, 'B_CAST_sub191_float')
B_CAST_sub191_double = solver.IntVar(0, 1, 'B_CAST_sub191_double')
solver.Add( + (1)*B_CAST_sub191_fixp + (1)*B_CAST_sub191_float + (1)*B_CAST_sub191_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_sub191_fixbits + (-10000)*B_CAST_sub191_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_sub191 = solver.IntVar(0, 1, 'C1_B_CAST_sub191')
C2_B_CAST_sub191 = solver.IntVar(0, 1, 'C2_B_CAST_sub191')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_sub191_fixbits + (-10000)*C1_B_CAST_sub191<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_sub191_fixbits + (-10000)*C2_B_CAST_sub191<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_sub191
castCostObj +=  + (1)*C2_B_CAST_sub191
C3_B_CAST_sub191 = solver.IntVar(0, 1, 'C3_B_CAST_sub191')
C4_B_CAST_sub191 = solver.IntVar(0, 1, 'C4_B_CAST_sub191')
C5_B_CAST_sub191 = solver.IntVar(0, 1, 'C5_B_CAST_sub191')
C6_B_CAST_sub191 = solver.IntVar(0, 1, 'C6_B_CAST_sub191')
C7_B_CAST_sub191 = solver.IntVar(0, 1, 'C7_B_CAST_sub191')
C8_B_CAST_sub191 = solver.IntVar(0, 1, 'C8_B_CAST_sub191')
solver.Add( + (1)*B_fixp + (1)*B_CAST_sub191_float + (-1)*C3_B_CAST_sub191<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_sub191
solver.Add( + (1)*B_float + (1)*B_CAST_sub191_fixp + (-1)*C4_B_CAST_sub191<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_sub191
solver.Add( + (1)*B_fixp + (1)*B_CAST_sub191_double + (-1)*C5_B_CAST_sub191<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_sub191
solver.Add( + (1)*B_double + (1)*B_CAST_sub191_fixp + (-1)*C6_B_CAST_sub191<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_sub191
solver.Add( + (1)*B_float + (1)*B_CAST_sub191_double + (-1)*C7_B_CAST_sub191<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_sub191
solver.Add( + (1)*B_double + (1)*B_CAST_sub191_float + (-1)*C8_B_CAST_sub191<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_sub191



#Constraint for cast for   %sub191 = fsub double %tmp13, %mul190, !taffo.info !62, !taffo.initweight !31
main_mul190_CAST_sub191_fixbits = solver.IntVar(0, 16, 'main_mul190_CAST_sub191_fixbits')
main_mul190_CAST_sub191_fixp = solver.IntVar(0, 1, 'main_mul190_CAST_sub191_fixp')
main_mul190_CAST_sub191_float = solver.IntVar(0, 1, 'main_mul190_CAST_sub191_float')
main_mul190_CAST_sub191_double = solver.IntVar(0, 1, 'main_mul190_CAST_sub191_double')
solver.Add( + (1)*main_mul190_CAST_sub191_fixp + (1)*main_mul190_CAST_sub191_float + (1)*main_mul190_CAST_sub191_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul190_CAST_sub191_fixbits + (-10000)*main_mul190_CAST_sub191_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C1_main_mul190_CAST_sub191')
C2_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C2_main_mul190_CAST_sub191')
solver.Add( + (1)*main_mul190_fixbits + (-1)*main_mul190_CAST_sub191_fixbits + (-10000)*C1_main_mul190_CAST_sub191<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul190_fixbits + (1)*main_mul190_CAST_sub191_fixbits + (-10000)*C2_main_mul190_CAST_sub191<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul190_CAST_sub191
castCostObj +=  + (1)*C2_main_mul190_CAST_sub191
C3_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C3_main_mul190_CAST_sub191')
C4_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C4_main_mul190_CAST_sub191')
C5_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C5_main_mul190_CAST_sub191')
C6_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C6_main_mul190_CAST_sub191')
C7_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C7_main_mul190_CAST_sub191')
C8_main_mul190_CAST_sub191 = solver.IntVar(0, 1, 'C8_main_mul190_CAST_sub191')
solver.Add( + (1)*main_mul190_fixp + (1)*main_mul190_CAST_sub191_float + (-1)*C3_main_mul190_CAST_sub191<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul190_CAST_sub191
solver.Add( + (1)*main_mul190_float + (1)*main_mul190_CAST_sub191_fixp + (-1)*C4_main_mul190_CAST_sub191<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul190_CAST_sub191
solver.Add( + (1)*main_mul190_fixp + (1)*main_mul190_CAST_sub191_double + (-1)*C5_main_mul190_CAST_sub191<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul190_CAST_sub191
solver.Add( + (1)*main_mul190_double + (1)*main_mul190_CAST_sub191_fixp + (-1)*C6_main_mul190_CAST_sub191<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul190_CAST_sub191
solver.Add( + (1)*main_mul190_float + (1)*main_mul190_CAST_sub191_double + (-1)*C7_main_mul190_CAST_sub191<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul190_CAST_sub191
solver.Add( + (1)*main_mul190_double + (1)*main_mul190_CAST_sub191_float + (-1)*C8_main_mul190_CAST_sub191<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul190_CAST_sub191



#Stuff for   %sub191 = fsub double %tmp13, %mul190, !taffo.info !62, !taffo.initweight !31
main_sub191_fixbits = solver.IntVar(0, 16, 'main_sub191_fixbits')
main_sub191_fixp = solver.IntVar(0, 1, 'main_sub191_fixp')
main_sub191_float = solver.IntVar(0, 1, 'main_sub191_float')
main_sub191_double = solver.IntVar(0, 1, 'main_sub191_double')
main_sub191_enob = solver.IntVar(-10000, 10000, 'main_sub191_enob')
solver.Add( + (1)*main_sub191_enob + (-1)*main_sub191_fixbits + (10000)*main_sub191_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub191_enob + (10000)*main_sub191_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub191_enob + (10000)*main_sub191_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub191_fixbits + (-10000)*main_sub191_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_sub191_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub191_enob
solver.Add( + (1)*main_sub191_fixp + (1)*main_sub191_float + (1)*main_sub191_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub191_fixbits + (-10000)*main_sub191_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*B_CAST_sub191_fixp + (-1)*main_mul190_CAST_sub191_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_sub191_float + (-1)*main_mul190_CAST_sub191_float==0)    #float equality
solver.Add( + (1)*B_CAST_sub191_double + (-1)*main_mul190_CAST_sub191_double==0)    #double equality
solver.Add( + (1)*B_CAST_sub191_fixbits + (-1)*main_mul190_CAST_sub191_fixbits==0)    #same fractional bit
solver.Add( + (1)*B_CAST_sub191_fixp + (-1)*main_sub191_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_sub191_float + (-1)*main_sub191_float==0)    #float equality
solver.Add( + (1)*B_CAST_sub191_double + (-1)*main_sub191_double==0)    #double equality
solver.Add( + (1)*B_CAST_sub191_fixbits + (-1)*main_sub191_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub191_fixp
mathCostObj +=  + (2.33125)*main_sub191_float
mathCostObj +=  + (2.72422)*main_sub191_double
solver.Add( + (1)*main_sub191_enob + (-1)*B_enob_memphi_main_tmp13<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub191_enob + (-1)*main_mul190_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp15 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp15')
solver.Add( + (1)*B_enob_memphi_main_tmp15 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp15_enob_1 = solver.IntVar(0, 1, 'main_main_tmp15_enob_1')
main_main_tmp15_enob_2 = solver.IntVar(0, 1, 'main_main_tmp15_enob_2')
main_main_tmp15_enob_3 = solver.IntVar(0, 1, 'main_main_tmp15_enob_3')
solver.Add( + (1)*main_main_tmp15_enob_1 + (1)*main_main_tmp15_enob_2 + (1)*main_main_tmp15_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp15 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp15_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp15 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp15_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add199 = fadd double %sub191, %tmp15, !taffo.info !64, !taffo.initweight !31
main_sub191_CAST_add199_fixbits = solver.IntVar(0, 16, 'main_sub191_CAST_add199_fixbits')
main_sub191_CAST_add199_fixp = solver.IntVar(0, 1, 'main_sub191_CAST_add199_fixp')
main_sub191_CAST_add199_float = solver.IntVar(0, 1, 'main_sub191_CAST_add199_float')
main_sub191_CAST_add199_double = solver.IntVar(0, 1, 'main_sub191_CAST_add199_double')
solver.Add( + (1)*main_sub191_CAST_add199_fixp + (1)*main_sub191_CAST_add199_float + (1)*main_sub191_CAST_add199_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub191_CAST_add199_fixbits + (-10000)*main_sub191_CAST_add199_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C1_main_sub191_CAST_add199')
C2_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C2_main_sub191_CAST_add199')
solver.Add( + (1)*main_sub191_fixbits + (-1)*main_sub191_CAST_add199_fixbits + (-10000)*C1_main_sub191_CAST_add199<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub191_fixbits + (1)*main_sub191_CAST_add199_fixbits + (-10000)*C2_main_sub191_CAST_add199<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub191_CAST_add199
castCostObj +=  + (1)*C2_main_sub191_CAST_add199
C3_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C3_main_sub191_CAST_add199')
C4_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C4_main_sub191_CAST_add199')
C5_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C5_main_sub191_CAST_add199')
C6_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C6_main_sub191_CAST_add199')
C7_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C7_main_sub191_CAST_add199')
C8_main_sub191_CAST_add199 = solver.IntVar(0, 1, 'C8_main_sub191_CAST_add199')
solver.Add( + (1)*main_sub191_fixp + (1)*main_sub191_CAST_add199_float + (-1)*C3_main_sub191_CAST_add199<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub191_CAST_add199
solver.Add( + (1)*main_sub191_float + (1)*main_sub191_CAST_add199_fixp + (-1)*C4_main_sub191_CAST_add199<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub191_CAST_add199
solver.Add( + (1)*main_sub191_fixp + (1)*main_sub191_CAST_add199_double + (-1)*C5_main_sub191_CAST_add199<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub191_CAST_add199
solver.Add( + (1)*main_sub191_double + (1)*main_sub191_CAST_add199_fixp + (-1)*C6_main_sub191_CAST_add199<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub191_CAST_add199
solver.Add( + (1)*main_sub191_float + (1)*main_sub191_CAST_add199_double + (-1)*C7_main_sub191_CAST_add199<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub191_CAST_add199
solver.Add( + (1)*main_sub191_double + (1)*main_sub191_CAST_add199_float + (-1)*C8_main_sub191_CAST_add199<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub191_CAST_add199



#Constraint for cast for   %add199 = fadd double %sub191, %tmp15, !taffo.info !64, !taffo.initweight !31
B_CAST_add199_fixbits = solver.IntVar(0, 17, 'B_CAST_add199_fixbits')
B_CAST_add199_fixp = solver.IntVar(0, 1, 'B_CAST_add199_fixp')
B_CAST_add199_float = solver.IntVar(0, 1, 'B_CAST_add199_float')
B_CAST_add199_double = solver.IntVar(0, 1, 'B_CAST_add199_double')
solver.Add( + (1)*B_CAST_add199_fixp + (1)*B_CAST_add199_float + (1)*B_CAST_add199_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_add199_fixbits + (-10000)*B_CAST_add199_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_add199 = solver.IntVar(0, 1, 'C1_B_CAST_add199')
C2_B_CAST_add199 = solver.IntVar(0, 1, 'C2_B_CAST_add199')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_add199_fixbits + (-10000)*C1_B_CAST_add199<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_add199_fixbits + (-10000)*C2_B_CAST_add199<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_add199
castCostObj +=  + (1)*C2_B_CAST_add199
C3_B_CAST_add199 = solver.IntVar(0, 1, 'C3_B_CAST_add199')
C4_B_CAST_add199 = solver.IntVar(0, 1, 'C4_B_CAST_add199')
C5_B_CAST_add199 = solver.IntVar(0, 1, 'C5_B_CAST_add199')
C6_B_CAST_add199 = solver.IntVar(0, 1, 'C6_B_CAST_add199')
C7_B_CAST_add199 = solver.IntVar(0, 1, 'C7_B_CAST_add199')
C8_B_CAST_add199 = solver.IntVar(0, 1, 'C8_B_CAST_add199')
solver.Add( + (1)*B_fixp + (1)*B_CAST_add199_float + (-1)*C3_B_CAST_add199<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_add199
solver.Add( + (1)*B_float + (1)*B_CAST_add199_fixp + (-1)*C4_B_CAST_add199<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_add199
solver.Add( + (1)*B_fixp + (1)*B_CAST_add199_double + (-1)*C5_B_CAST_add199<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_add199
solver.Add( + (1)*B_double + (1)*B_CAST_add199_fixp + (-1)*C6_B_CAST_add199<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_add199
solver.Add( + (1)*B_float + (1)*B_CAST_add199_double + (-1)*C7_B_CAST_add199<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_add199
solver.Add( + (1)*B_double + (1)*B_CAST_add199_float + (-1)*C8_B_CAST_add199<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_add199



#Stuff for   %add199 = fadd double %sub191, %tmp15, !taffo.info !64, !taffo.initweight !31
main_add199_fixbits = solver.IntVar(0, 15, 'main_add199_fixbits')
main_add199_fixp = solver.IntVar(0, 1, 'main_add199_fixp')
main_add199_float = solver.IntVar(0, 1, 'main_add199_float')
main_add199_double = solver.IntVar(0, 1, 'main_add199_double')
main_add199_enob = solver.IntVar(-10000, 10000, 'main_add199_enob')
solver.Add( + (1)*main_add199_enob + (-1)*main_add199_fixbits + (10000)*main_add199_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add199_enob + (10000)*main_add199_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add199_enob + (10000)*main_add199_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add199_fixbits + (-10000)*main_add199_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add199_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add199_enob
solver.Add( + (1)*main_add199_fixp + (1)*main_add199_float + (1)*main_add199_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add199_fixbits + (-10000)*main_add199_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub191_CAST_add199_fixp + (-1)*B_CAST_add199_fixp==0)    #fix equality
solver.Add( + (1)*main_sub191_CAST_add199_float + (-1)*B_CAST_add199_float==0)    #float equality
solver.Add( + (1)*main_sub191_CAST_add199_double + (-1)*B_CAST_add199_double==0)    #double equality
solver.Add( + (1)*main_sub191_CAST_add199_fixbits + (-1)*B_CAST_add199_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub191_CAST_add199_fixp + (-1)*main_add199_fixp==0)    #fix equality
solver.Add( + (1)*main_sub191_CAST_add199_float + (-1)*main_add199_float==0)    #float equality
solver.Add( + (1)*main_sub191_CAST_add199_double + (-1)*main_add199_double==0)    #double equality
solver.Add( + (1)*main_sub191_CAST_add199_fixbits + (-1)*main_add199_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add199_fixp
mathCostObj +=  + (2.33125)*main_add199_float
mathCostObj +=  + (2.72422)*main_add199_double
solver.Add( + (1)*main_add199_enob + (-1)*main_sub191_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add199_enob + (-1)*B_enob_memphi_main_tmp15<=0)    #Enob propagation in sum second addend



#Stuff for double 1.250000e-01
ConstantValue__29_fixbits = solver.IntVar(0, 31, 'ConstantValue__29_fixbits')
ConstantValue__29_fixp = solver.IntVar(0, 1, 'ConstantValue__29_fixp')
ConstantValue__29_float = solver.IntVar(0, 1, 'ConstantValue__29_float')
ConstantValue__29_double = solver.IntVar(0, 1, 'ConstantValue__29_double')
ConstantValue__29_enob = solver.IntVar(-10000, 10000, 'ConstantValue__29_enob')
solver.Add( + (1)*ConstantValue__29_enob + (-1)*ConstantValue__29_fixbits + (10000)*ConstantValue__29_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__29_fixp + (1)*ConstantValue__29_float + (1)*ConstantValue__29_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__30_fixbits = solver.IntVar(0, 31, 'ConstantValue__30_fixbits')
ConstantValue__30_fixp = solver.IntVar(0, 1, 'ConstantValue__30_fixp')
ConstantValue__30_float = solver.IntVar(0, 1, 'ConstantValue__30_float')
ConstantValue__30_double = solver.IntVar(0, 1, 'ConstantValue__30_double')
ConstantValue__30_enob = solver.IntVar(-10000, 10000, 'ConstantValue__30_enob')
solver.Add( + (1)*ConstantValue__30_enob + (-1)*ConstantValue__30_fixbits + (10000)*ConstantValue__30_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__30_fixp + (1)*ConstantValue__30_float + (1)*ConstantValue__30_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__31_fixbits = solver.IntVar(0, 31, 'ConstantValue__31_fixbits')
ConstantValue__31_fixp = solver.IntVar(0, 1, 'ConstantValue__31_fixp')
ConstantValue__31_float = solver.IntVar(0, 1, 'ConstantValue__31_float')
ConstantValue__31_double = solver.IntVar(0, 1, 'ConstantValue__31_double')
ConstantValue__31_enob = solver.IntVar(-10000, 10000, 'ConstantValue__31_enob')
solver.Add( + (1)*ConstantValue__31_enob + (-1)*ConstantValue__31_fixbits + (10000)*ConstantValue__31_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_float + (1)*ConstantValue__31_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul200 = fmul double 1.250000e-01, %add199, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
ConstantValue__31_CAST_mul200_fixbits = solver.IntVar(0, 31, 'ConstantValue__31_CAST_mul200_fixbits')
ConstantValue__31_CAST_mul200_fixp = solver.IntVar(0, 1, 'ConstantValue__31_CAST_mul200_fixp')
ConstantValue__31_CAST_mul200_float = solver.IntVar(0, 1, 'ConstantValue__31_CAST_mul200_float')
ConstantValue__31_CAST_mul200_double = solver.IntVar(0, 1, 'ConstantValue__31_CAST_mul200_double')
solver.Add( + (1)*ConstantValue__31_CAST_mul200_fixp + (1)*ConstantValue__31_CAST_mul200_float + (1)*ConstantValue__31_CAST_mul200_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__31_CAST_mul200_fixbits + (-10000)*ConstantValue__31_CAST_mul200_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C1_ConstantValue__31_CAST_mul200')
C2_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C2_ConstantValue__31_CAST_mul200')
solver.Add( + (1)*ConstantValue__31_fixbits + (-1)*ConstantValue__31_CAST_mul200_fixbits + (-10000)*C1_ConstantValue__31_CAST_mul200<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__31_fixbits + (1)*ConstantValue__31_CAST_mul200_fixbits + (-10000)*C2_ConstantValue__31_CAST_mul200<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__31_CAST_mul200
castCostObj +=  + (1)*C2_ConstantValue__31_CAST_mul200
C3_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C3_ConstantValue__31_CAST_mul200')
C4_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C4_ConstantValue__31_CAST_mul200')
C5_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C5_ConstantValue__31_CAST_mul200')
C6_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C6_ConstantValue__31_CAST_mul200')
C7_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C7_ConstantValue__31_CAST_mul200')
C8_ConstantValue__31_CAST_mul200 = solver.IntVar(0, 1, 'C8_ConstantValue__31_CAST_mul200')
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_CAST_mul200_float + (-1)*C3_ConstantValue__31_CAST_mul200<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__31_CAST_mul200
solver.Add( + (1)*ConstantValue__31_float + (1)*ConstantValue__31_CAST_mul200_fixp + (-1)*C4_ConstantValue__31_CAST_mul200<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__31_CAST_mul200
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_CAST_mul200_double + (-1)*C5_ConstantValue__31_CAST_mul200<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__31_CAST_mul200
solver.Add( + (1)*ConstantValue__31_double + (1)*ConstantValue__31_CAST_mul200_fixp + (-1)*C6_ConstantValue__31_CAST_mul200<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__31_CAST_mul200
solver.Add( + (1)*ConstantValue__31_float + (1)*ConstantValue__31_CAST_mul200_double + (-1)*C7_ConstantValue__31_CAST_mul200<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__31_CAST_mul200
solver.Add( + (1)*ConstantValue__31_double + (1)*ConstantValue__31_CAST_mul200_float + (-1)*C8_ConstantValue__31_CAST_mul200<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__31_CAST_mul200



#Constraint for cast for   %mul200 = fmul double 1.250000e-01, %add199, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
main_add199_CAST_mul200_fixbits = solver.IntVar(0, 15, 'main_add199_CAST_mul200_fixbits')
main_add199_CAST_mul200_fixp = solver.IntVar(0, 1, 'main_add199_CAST_mul200_fixp')
main_add199_CAST_mul200_float = solver.IntVar(0, 1, 'main_add199_CAST_mul200_float')
main_add199_CAST_mul200_double = solver.IntVar(0, 1, 'main_add199_CAST_mul200_double')
solver.Add( + (1)*main_add199_CAST_mul200_fixp + (1)*main_add199_CAST_mul200_float + (1)*main_add199_CAST_mul200_double==1)    #exactly 1 type
solver.Add( + (1)*main_add199_CAST_mul200_fixbits + (-10000)*main_add199_CAST_mul200_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C1_main_add199_CAST_mul200')
C2_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C2_main_add199_CAST_mul200')
solver.Add( + (1)*main_add199_fixbits + (-1)*main_add199_CAST_mul200_fixbits + (-10000)*C1_main_add199_CAST_mul200<=0)    #Shift cost 1
solver.Add( + (-1)*main_add199_fixbits + (1)*main_add199_CAST_mul200_fixbits + (-10000)*C2_main_add199_CAST_mul200<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add199_CAST_mul200
castCostObj +=  + (1)*C2_main_add199_CAST_mul200
C3_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C3_main_add199_CAST_mul200')
C4_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C4_main_add199_CAST_mul200')
C5_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C5_main_add199_CAST_mul200')
C6_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C6_main_add199_CAST_mul200')
C7_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C7_main_add199_CAST_mul200')
C8_main_add199_CAST_mul200 = solver.IntVar(0, 1, 'C8_main_add199_CAST_mul200')
solver.Add( + (1)*main_add199_fixp + (1)*main_add199_CAST_mul200_float + (-1)*C3_main_add199_CAST_mul200<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add199_CAST_mul200
solver.Add( + (1)*main_add199_float + (1)*main_add199_CAST_mul200_fixp + (-1)*C4_main_add199_CAST_mul200<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add199_CAST_mul200
solver.Add( + (1)*main_add199_fixp + (1)*main_add199_CAST_mul200_double + (-1)*C5_main_add199_CAST_mul200<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add199_CAST_mul200
solver.Add( + (1)*main_add199_double + (1)*main_add199_CAST_mul200_fixp + (-1)*C6_main_add199_CAST_mul200<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add199_CAST_mul200
solver.Add( + (1)*main_add199_float + (1)*main_add199_CAST_mul200_double + (-1)*C7_main_add199_CAST_mul200<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add199_CAST_mul200
solver.Add( + (1)*main_add199_double + (1)*main_add199_CAST_mul200_float + (-1)*C8_main_add199_CAST_mul200<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add199_CAST_mul200



#Stuff for   %mul200 = fmul double 1.250000e-01, %add199, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
main_mul200_fixbits = solver.IntVar(0, 18, 'main_mul200_fixbits')
main_mul200_fixp = solver.IntVar(0, 1, 'main_mul200_fixp')
main_mul200_float = solver.IntVar(0, 1, 'main_mul200_float')
main_mul200_double = solver.IntVar(0, 1, 'main_mul200_double')
main_mul200_enob = solver.IntVar(-10000, 10000, 'main_mul200_enob')
solver.Add( + (1)*main_mul200_enob + (-1)*main_mul200_fixbits + (10000)*main_mul200_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul200_enob + (10000)*main_mul200_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul200_enob + (10000)*main_mul200_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul200_fixbits + (-10000)*main_mul200_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_mul200_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul200_enob
solver.Add( + (1)*main_mul200_fixp + (1)*main_mul200_float + (1)*main_mul200_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul200_fixbits + (-10000)*main_mul200_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__31_CAST_mul200_fixp + (-1)*main_add199_CAST_mul200_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__31_CAST_mul200_float + (-1)*main_add199_CAST_mul200_float==0)    #float equality
solver.Add( + (1)*ConstantValue__31_CAST_mul200_double + (-1)*main_add199_CAST_mul200_double==0)    #double equality
solver.Add( + (1)*ConstantValue__31_CAST_mul200_fixp + (-1)*main_mul200_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__31_CAST_mul200_float + (-1)*main_mul200_float==0)    #float equality
solver.Add( + (1)*ConstantValue__31_CAST_mul200_double + (-1)*main_mul200_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul200_fixp
mathCostObj +=  + (2.64722)*main_mul200_float
mathCostObj +=  + (4.02255)*main_mul200_double
main_main_mul200_enob_1 = solver.IntVar(0, 1, 'main_main_mul200_enob_1')
main_main_mul200_enob_2 = solver.IntVar(0, 1, 'main_main_mul200_enob_2')
solver.Add( + (1)*main_main_mul200_enob_1 + (1)*main_main_mul200_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul200_enob + (-1)*main_add199_enob + (-10000)*main_main_mul200_enob_1<=3)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul200_enob + (-1)*ConstantValue__29_enob + (-10000)*main_main_mul200_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add201 = fadd double %mul176, %mul200, !taffo.info !68, !taffo.initweight !57
main_mul176_CAST_add201_fixbits = solver.IntVar(0, 18, 'main_mul176_CAST_add201_fixbits')
main_mul176_CAST_add201_fixp = solver.IntVar(0, 1, 'main_mul176_CAST_add201_fixp')
main_mul176_CAST_add201_float = solver.IntVar(0, 1, 'main_mul176_CAST_add201_float')
main_mul176_CAST_add201_double = solver.IntVar(0, 1, 'main_mul176_CAST_add201_double')
solver.Add( + (1)*main_mul176_CAST_add201_fixp + (1)*main_mul176_CAST_add201_float + (1)*main_mul176_CAST_add201_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul176_CAST_add201_fixbits + (-10000)*main_mul176_CAST_add201_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C1_main_mul176_CAST_add201')
C2_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C2_main_mul176_CAST_add201')
solver.Add( + (1)*main_mul176_fixbits + (-1)*main_mul176_CAST_add201_fixbits + (-10000)*C1_main_mul176_CAST_add201<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul176_fixbits + (1)*main_mul176_CAST_add201_fixbits + (-10000)*C2_main_mul176_CAST_add201<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul176_CAST_add201
castCostObj +=  + (1)*C2_main_mul176_CAST_add201
C3_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C3_main_mul176_CAST_add201')
C4_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C4_main_mul176_CAST_add201')
C5_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C5_main_mul176_CAST_add201')
C6_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C6_main_mul176_CAST_add201')
C7_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C7_main_mul176_CAST_add201')
C8_main_mul176_CAST_add201 = solver.IntVar(0, 1, 'C8_main_mul176_CAST_add201')
solver.Add( + (1)*main_mul176_fixp + (1)*main_mul176_CAST_add201_float + (-1)*C3_main_mul176_CAST_add201<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul176_CAST_add201
solver.Add( + (1)*main_mul176_float + (1)*main_mul176_CAST_add201_fixp + (-1)*C4_main_mul176_CAST_add201<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul176_CAST_add201
solver.Add( + (1)*main_mul176_fixp + (1)*main_mul176_CAST_add201_double + (-1)*C5_main_mul176_CAST_add201<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul176_CAST_add201
solver.Add( + (1)*main_mul176_double + (1)*main_mul176_CAST_add201_fixp + (-1)*C6_main_mul176_CAST_add201<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul176_CAST_add201
solver.Add( + (1)*main_mul176_float + (1)*main_mul176_CAST_add201_double + (-1)*C7_main_mul176_CAST_add201<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul176_CAST_add201
solver.Add( + (1)*main_mul176_double + (1)*main_mul176_CAST_add201_float + (-1)*C8_main_mul176_CAST_add201<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul176_CAST_add201



#Constraint for cast for   %add201 = fadd double %mul176, %mul200, !taffo.info !68, !taffo.initweight !57
main_mul200_CAST_add201_fixbits = solver.IntVar(0, 18, 'main_mul200_CAST_add201_fixbits')
main_mul200_CAST_add201_fixp = solver.IntVar(0, 1, 'main_mul200_CAST_add201_fixp')
main_mul200_CAST_add201_float = solver.IntVar(0, 1, 'main_mul200_CAST_add201_float')
main_mul200_CAST_add201_double = solver.IntVar(0, 1, 'main_mul200_CAST_add201_double')
solver.Add( + (1)*main_mul200_CAST_add201_fixp + (1)*main_mul200_CAST_add201_float + (1)*main_mul200_CAST_add201_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul200_CAST_add201_fixbits + (-10000)*main_mul200_CAST_add201_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C1_main_mul200_CAST_add201')
C2_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C2_main_mul200_CAST_add201')
solver.Add( + (1)*main_mul200_fixbits + (-1)*main_mul200_CAST_add201_fixbits + (-10000)*C1_main_mul200_CAST_add201<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul200_fixbits + (1)*main_mul200_CAST_add201_fixbits + (-10000)*C2_main_mul200_CAST_add201<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul200_CAST_add201
castCostObj +=  + (1)*C2_main_mul200_CAST_add201
C3_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C3_main_mul200_CAST_add201')
C4_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C4_main_mul200_CAST_add201')
C5_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C5_main_mul200_CAST_add201')
C6_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C6_main_mul200_CAST_add201')
C7_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C7_main_mul200_CAST_add201')
C8_main_mul200_CAST_add201 = solver.IntVar(0, 1, 'C8_main_mul200_CAST_add201')
solver.Add( + (1)*main_mul200_fixp + (1)*main_mul200_CAST_add201_float + (-1)*C3_main_mul200_CAST_add201<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul200_CAST_add201
solver.Add( + (1)*main_mul200_float + (1)*main_mul200_CAST_add201_fixp + (-1)*C4_main_mul200_CAST_add201<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul200_CAST_add201
solver.Add( + (1)*main_mul200_fixp + (1)*main_mul200_CAST_add201_double + (-1)*C5_main_mul200_CAST_add201<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul200_CAST_add201
solver.Add( + (1)*main_mul200_double + (1)*main_mul200_CAST_add201_fixp + (-1)*C6_main_mul200_CAST_add201<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul200_CAST_add201
solver.Add( + (1)*main_mul200_float + (1)*main_mul200_CAST_add201_double + (-1)*C7_main_mul200_CAST_add201<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul200_CAST_add201
solver.Add( + (1)*main_mul200_double + (1)*main_mul200_CAST_add201_float + (-1)*C8_main_mul200_CAST_add201<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul200_CAST_add201



#Stuff for   %add201 = fadd double %mul176, %mul200, !taffo.info !68, !taffo.initweight !57
main_add201_fixbits = solver.IntVar(0, 17, 'main_add201_fixbits')
main_add201_fixp = solver.IntVar(0, 1, 'main_add201_fixp')
main_add201_float = solver.IntVar(0, 1, 'main_add201_float')
main_add201_double = solver.IntVar(0, 1, 'main_add201_double')
main_add201_enob = solver.IntVar(-10000, 10000, 'main_add201_enob')
solver.Add( + (1)*main_add201_enob + (-1)*main_add201_fixbits + (10000)*main_add201_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add201_enob + (10000)*main_add201_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add201_enob + (10000)*main_add201_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add201_fixbits + (-10000)*main_add201_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_add201_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add201_enob
solver.Add( + (1)*main_add201_fixp + (1)*main_add201_float + (1)*main_add201_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add201_fixbits + (-10000)*main_add201_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul176_CAST_add201_fixp + (-1)*main_mul200_CAST_add201_fixp==0)    #fix equality
solver.Add( + (1)*main_mul176_CAST_add201_float + (-1)*main_mul200_CAST_add201_float==0)    #float equality
solver.Add( + (1)*main_mul176_CAST_add201_double + (-1)*main_mul200_CAST_add201_double==0)    #double equality
solver.Add( + (1)*main_mul176_CAST_add201_fixbits + (-1)*main_mul200_CAST_add201_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul176_CAST_add201_fixp + (-1)*main_add201_fixp==0)    #fix equality
solver.Add( + (1)*main_mul176_CAST_add201_float + (-1)*main_add201_float==0)    #float equality
solver.Add( + (1)*main_mul176_CAST_add201_double + (-1)*main_add201_double==0)    #double equality
solver.Add( + (1)*main_mul176_CAST_add201_fixbits + (-1)*main_add201_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add201_fixp
mathCostObj +=  + (2.33125)*main_add201_float
mathCostObj +=  + (2.72422)*main_add201_double
solver.Add( + (1)*main_add201_enob + (-1)*main_mul176_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add201_enob + (-1)*main_mul200_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp16 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp16')
solver.Add( + (1)*B_enob_memphi_main_tmp16 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp16_enob_1 = solver.IntVar(0, 1, 'main_main_tmp16_enob_1')
main_main_tmp16_enob_2 = solver.IntVar(0, 1, 'main_main_tmp16_enob_2')
main_main_tmp16_enob_3 = solver.IntVar(0, 1, 'main_main_tmp16_enob_3')
solver.Add( + (1)*main_main_tmp16_enob_1 + (1)*main_main_tmp16_enob_2 + (1)*main_main_tmp16_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp16 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp16_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp16 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp17 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp17')
solver.Add( + (1)*B_enob_memphi_main_tmp17 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp17_enob_1 = solver.IntVar(0, 1, 'main_main_tmp17_enob_1')
main_main_tmp17_enob_2 = solver.IntVar(0, 1, 'main_main_tmp17_enob_2')
main_main_tmp17_enob_3 = solver.IntVar(0, 1, 'main_main_tmp17_enob_3')
solver.Add( + (1)*main_main_tmp17_enob_1 + (1)*main_main_tmp17_enob_2 + (1)*main_main_tmp17_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp17 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp17_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp17 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_3<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__32_fixbits = solver.IntVar(0, 30, 'ConstantValue__32_fixbits')
ConstantValue__32_fixp = solver.IntVar(0, 1, 'ConstantValue__32_fixp')
ConstantValue__32_float = solver.IntVar(0, 1, 'ConstantValue__32_float')
ConstantValue__32_double = solver.IntVar(0, 1, 'ConstantValue__32_double')
ConstantValue__32_enob = solver.IntVar(-10000, 10000, 'ConstantValue__32_enob')
solver.Add( + (1)*ConstantValue__32_enob + (-1)*ConstantValue__32_fixbits + (10000)*ConstantValue__32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__32_fixp + (1)*ConstantValue__32_float + (1)*ConstantValue__32_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__33_fixbits = solver.IntVar(0, 30, 'ConstantValue__33_fixbits')
ConstantValue__33_fixp = solver.IntVar(0, 1, 'ConstantValue__33_fixp')
ConstantValue__33_float = solver.IntVar(0, 1, 'ConstantValue__33_float')
ConstantValue__33_double = solver.IntVar(0, 1, 'ConstantValue__33_double')
ConstantValue__33_enob = solver.IntVar(-10000, 10000, 'ConstantValue__33_enob')
solver.Add( + (1)*ConstantValue__33_enob + (-1)*ConstantValue__33_fixbits + (10000)*ConstantValue__33_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_float + (1)*ConstantValue__33_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__34_fixbits = solver.IntVar(0, 30, 'ConstantValue__34_fixbits')
ConstantValue__34_fixp = solver.IntVar(0, 1, 'ConstantValue__34_fixp')
ConstantValue__34_float = solver.IntVar(0, 1, 'ConstantValue__34_float')
ConstantValue__34_double = solver.IntVar(0, 1, 'ConstantValue__34_double')
ConstantValue__34_enob = solver.IntVar(-10000, 10000, 'ConstantValue__34_enob')
solver.Add( + (1)*ConstantValue__34_enob + (-1)*ConstantValue__34_fixbits + (10000)*ConstantValue__34_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_float + (1)*ConstantValue__34_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul215 = fmul double 2.000000e+00, %tmp17, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
ConstantValue__34_CAST_mul215_fixbits = solver.IntVar(0, 30, 'ConstantValue__34_CAST_mul215_fixbits')
ConstantValue__34_CAST_mul215_fixp = solver.IntVar(0, 1, 'ConstantValue__34_CAST_mul215_fixp')
ConstantValue__34_CAST_mul215_float = solver.IntVar(0, 1, 'ConstantValue__34_CAST_mul215_float')
ConstantValue__34_CAST_mul215_double = solver.IntVar(0, 1, 'ConstantValue__34_CAST_mul215_double')
solver.Add( + (1)*ConstantValue__34_CAST_mul215_fixp + (1)*ConstantValue__34_CAST_mul215_float + (1)*ConstantValue__34_CAST_mul215_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__34_CAST_mul215_fixbits + (-10000)*ConstantValue__34_CAST_mul215_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C1_ConstantValue__34_CAST_mul215')
C2_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C2_ConstantValue__34_CAST_mul215')
solver.Add( + (1)*ConstantValue__34_fixbits + (-1)*ConstantValue__34_CAST_mul215_fixbits + (-10000)*C1_ConstantValue__34_CAST_mul215<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__34_fixbits + (1)*ConstantValue__34_CAST_mul215_fixbits + (-10000)*C2_ConstantValue__34_CAST_mul215<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__34_CAST_mul215
castCostObj +=  + (1)*C2_ConstantValue__34_CAST_mul215
C3_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C3_ConstantValue__34_CAST_mul215')
C4_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C4_ConstantValue__34_CAST_mul215')
C5_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C5_ConstantValue__34_CAST_mul215')
C6_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C6_ConstantValue__34_CAST_mul215')
C7_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C7_ConstantValue__34_CAST_mul215')
C8_ConstantValue__34_CAST_mul215 = solver.IntVar(0, 1, 'C8_ConstantValue__34_CAST_mul215')
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_CAST_mul215_float + (-1)*C3_ConstantValue__34_CAST_mul215<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__34_CAST_mul215
solver.Add( + (1)*ConstantValue__34_float + (1)*ConstantValue__34_CAST_mul215_fixp + (-1)*C4_ConstantValue__34_CAST_mul215<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__34_CAST_mul215
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_CAST_mul215_double + (-1)*C5_ConstantValue__34_CAST_mul215<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__34_CAST_mul215
solver.Add( + (1)*ConstantValue__34_double + (1)*ConstantValue__34_CAST_mul215_fixp + (-1)*C6_ConstantValue__34_CAST_mul215<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__34_CAST_mul215
solver.Add( + (1)*ConstantValue__34_float + (1)*ConstantValue__34_CAST_mul215_double + (-1)*C7_ConstantValue__34_CAST_mul215<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__34_CAST_mul215
solver.Add( + (1)*ConstantValue__34_double + (1)*ConstantValue__34_CAST_mul215_float + (-1)*C8_ConstantValue__34_CAST_mul215<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__34_CAST_mul215



#Constraint for cast for   %mul215 = fmul double 2.000000e+00, %tmp17, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
B_CAST_mul215_fixbits = solver.IntVar(0, 17, 'B_CAST_mul215_fixbits')
B_CAST_mul215_fixp = solver.IntVar(0, 1, 'B_CAST_mul215_fixp')
B_CAST_mul215_float = solver.IntVar(0, 1, 'B_CAST_mul215_float')
B_CAST_mul215_double = solver.IntVar(0, 1, 'B_CAST_mul215_double')
solver.Add( + (1)*B_CAST_mul215_fixp + (1)*B_CAST_mul215_float + (1)*B_CAST_mul215_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_mul215_fixbits + (-10000)*B_CAST_mul215_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_mul215 = solver.IntVar(0, 1, 'C1_B_CAST_mul215')
C2_B_CAST_mul215 = solver.IntVar(0, 1, 'C2_B_CAST_mul215')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_mul215_fixbits + (-10000)*C1_B_CAST_mul215<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_mul215_fixbits + (-10000)*C2_B_CAST_mul215<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_mul215
castCostObj +=  + (1)*C2_B_CAST_mul215
C3_B_CAST_mul215 = solver.IntVar(0, 1, 'C3_B_CAST_mul215')
C4_B_CAST_mul215 = solver.IntVar(0, 1, 'C4_B_CAST_mul215')
C5_B_CAST_mul215 = solver.IntVar(0, 1, 'C5_B_CAST_mul215')
C6_B_CAST_mul215 = solver.IntVar(0, 1, 'C6_B_CAST_mul215')
C7_B_CAST_mul215 = solver.IntVar(0, 1, 'C7_B_CAST_mul215')
C8_B_CAST_mul215 = solver.IntVar(0, 1, 'C8_B_CAST_mul215')
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul215_float + (-1)*C3_B_CAST_mul215<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_mul215
solver.Add( + (1)*B_float + (1)*B_CAST_mul215_fixp + (-1)*C4_B_CAST_mul215<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_mul215
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul215_double + (-1)*C5_B_CAST_mul215<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_mul215
solver.Add( + (1)*B_double + (1)*B_CAST_mul215_fixp + (-1)*C6_B_CAST_mul215<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_mul215
solver.Add( + (1)*B_float + (1)*B_CAST_mul215_double + (-1)*C7_B_CAST_mul215<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_mul215
solver.Add( + (1)*B_double + (1)*B_CAST_mul215_float + (-1)*C8_B_CAST_mul215<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_mul215



#Stuff for   %mul215 = fmul double 2.000000e+00, %tmp17, !taffo.info !60, !taffo.initweight !31, !taffo.constinfo !43
main_mul215_fixbits = solver.IntVar(0, 16, 'main_mul215_fixbits')
main_mul215_fixp = solver.IntVar(0, 1, 'main_mul215_fixp')
main_mul215_float = solver.IntVar(0, 1, 'main_mul215_float')
main_mul215_double = solver.IntVar(0, 1, 'main_mul215_double')
main_mul215_enob = solver.IntVar(-10000, 10000, 'main_mul215_enob')
solver.Add( + (1)*main_mul215_enob + (-1)*main_mul215_fixbits + (10000)*main_mul215_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul215_enob + (10000)*main_mul215_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul215_enob + (10000)*main_mul215_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul215_fixbits + (-10000)*main_mul215_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul215_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul215_enob
solver.Add( + (1)*main_mul215_fixp + (1)*main_mul215_float + (1)*main_mul215_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul215_fixbits + (-10000)*main_mul215_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__34_CAST_mul215_fixp + (-1)*B_CAST_mul215_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__34_CAST_mul215_float + (-1)*B_CAST_mul215_float==0)    #float equality
solver.Add( + (1)*ConstantValue__34_CAST_mul215_double + (-1)*B_CAST_mul215_double==0)    #double equality
solver.Add( + (1)*ConstantValue__34_CAST_mul215_fixp + (-1)*main_mul215_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__34_CAST_mul215_float + (-1)*main_mul215_float==0)    #float equality
solver.Add( + (1)*ConstantValue__34_CAST_mul215_double + (-1)*main_mul215_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul215_fixp
mathCostObj +=  + (2.64722)*main_mul215_float
mathCostObj +=  + (4.02255)*main_mul215_double
main_main_mul215_enob_1 = solver.IntVar(0, 1, 'main_main_mul215_enob_1')
main_main_mul215_enob_2 = solver.IntVar(0, 1, 'main_main_mul215_enob_2')
solver.Add( + (1)*main_main_mul215_enob_1 + (1)*main_main_mul215_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul215_enob + (-1)*B_enob_memphi_main_tmp17 + (-10000)*main_main_mul215_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul215_enob + (-1)*ConstantValue__32_enob + (-10000)*main_main_mul215_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub216 = fsub double %tmp16, %mul215, !taffo.info !62, !taffo.initweight !31
B_CAST_sub216_fixbits = solver.IntVar(0, 17, 'B_CAST_sub216_fixbits')
B_CAST_sub216_fixp = solver.IntVar(0, 1, 'B_CAST_sub216_fixp')
B_CAST_sub216_float = solver.IntVar(0, 1, 'B_CAST_sub216_float')
B_CAST_sub216_double = solver.IntVar(0, 1, 'B_CAST_sub216_double')
solver.Add( + (1)*B_CAST_sub216_fixp + (1)*B_CAST_sub216_float + (1)*B_CAST_sub216_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_sub216_fixbits + (-10000)*B_CAST_sub216_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_sub216 = solver.IntVar(0, 1, 'C1_B_CAST_sub216')
C2_B_CAST_sub216 = solver.IntVar(0, 1, 'C2_B_CAST_sub216')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_sub216_fixbits + (-10000)*C1_B_CAST_sub216<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_sub216_fixbits + (-10000)*C2_B_CAST_sub216<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_sub216
castCostObj +=  + (1)*C2_B_CAST_sub216
C3_B_CAST_sub216 = solver.IntVar(0, 1, 'C3_B_CAST_sub216')
C4_B_CAST_sub216 = solver.IntVar(0, 1, 'C4_B_CAST_sub216')
C5_B_CAST_sub216 = solver.IntVar(0, 1, 'C5_B_CAST_sub216')
C6_B_CAST_sub216 = solver.IntVar(0, 1, 'C6_B_CAST_sub216')
C7_B_CAST_sub216 = solver.IntVar(0, 1, 'C7_B_CAST_sub216')
C8_B_CAST_sub216 = solver.IntVar(0, 1, 'C8_B_CAST_sub216')
solver.Add( + (1)*B_fixp + (1)*B_CAST_sub216_float + (-1)*C3_B_CAST_sub216<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_sub216
solver.Add( + (1)*B_float + (1)*B_CAST_sub216_fixp + (-1)*C4_B_CAST_sub216<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_sub216
solver.Add( + (1)*B_fixp + (1)*B_CAST_sub216_double + (-1)*C5_B_CAST_sub216<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_sub216
solver.Add( + (1)*B_double + (1)*B_CAST_sub216_fixp + (-1)*C6_B_CAST_sub216<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_sub216
solver.Add( + (1)*B_float + (1)*B_CAST_sub216_double + (-1)*C7_B_CAST_sub216<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_sub216
solver.Add( + (1)*B_double + (1)*B_CAST_sub216_float + (-1)*C8_B_CAST_sub216<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_sub216



#Constraint for cast for   %sub216 = fsub double %tmp16, %mul215, !taffo.info !62, !taffo.initweight !31
main_mul215_CAST_sub216_fixbits = solver.IntVar(0, 16, 'main_mul215_CAST_sub216_fixbits')
main_mul215_CAST_sub216_fixp = solver.IntVar(0, 1, 'main_mul215_CAST_sub216_fixp')
main_mul215_CAST_sub216_float = solver.IntVar(0, 1, 'main_mul215_CAST_sub216_float')
main_mul215_CAST_sub216_double = solver.IntVar(0, 1, 'main_mul215_CAST_sub216_double')
solver.Add( + (1)*main_mul215_CAST_sub216_fixp + (1)*main_mul215_CAST_sub216_float + (1)*main_mul215_CAST_sub216_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul215_CAST_sub216_fixbits + (-10000)*main_mul215_CAST_sub216_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C1_main_mul215_CAST_sub216')
C2_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C2_main_mul215_CAST_sub216')
solver.Add( + (1)*main_mul215_fixbits + (-1)*main_mul215_CAST_sub216_fixbits + (-10000)*C1_main_mul215_CAST_sub216<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul215_fixbits + (1)*main_mul215_CAST_sub216_fixbits + (-10000)*C2_main_mul215_CAST_sub216<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul215_CAST_sub216
castCostObj +=  + (1)*C2_main_mul215_CAST_sub216
C3_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C3_main_mul215_CAST_sub216')
C4_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C4_main_mul215_CAST_sub216')
C5_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C5_main_mul215_CAST_sub216')
C6_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C6_main_mul215_CAST_sub216')
C7_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C7_main_mul215_CAST_sub216')
C8_main_mul215_CAST_sub216 = solver.IntVar(0, 1, 'C8_main_mul215_CAST_sub216')
solver.Add( + (1)*main_mul215_fixp + (1)*main_mul215_CAST_sub216_float + (-1)*C3_main_mul215_CAST_sub216<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul215_CAST_sub216
solver.Add( + (1)*main_mul215_float + (1)*main_mul215_CAST_sub216_fixp + (-1)*C4_main_mul215_CAST_sub216<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul215_CAST_sub216
solver.Add( + (1)*main_mul215_fixp + (1)*main_mul215_CAST_sub216_double + (-1)*C5_main_mul215_CAST_sub216<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul215_CAST_sub216
solver.Add( + (1)*main_mul215_double + (1)*main_mul215_CAST_sub216_fixp + (-1)*C6_main_mul215_CAST_sub216<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul215_CAST_sub216
solver.Add( + (1)*main_mul215_float + (1)*main_mul215_CAST_sub216_double + (-1)*C7_main_mul215_CAST_sub216<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul215_CAST_sub216
solver.Add( + (1)*main_mul215_double + (1)*main_mul215_CAST_sub216_float + (-1)*C8_main_mul215_CAST_sub216<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul215_CAST_sub216



#Stuff for   %sub216 = fsub double %tmp16, %mul215, !taffo.info !62, !taffo.initweight !31
main_sub216_fixbits = solver.IntVar(0, 16, 'main_sub216_fixbits')
main_sub216_fixp = solver.IntVar(0, 1, 'main_sub216_fixp')
main_sub216_float = solver.IntVar(0, 1, 'main_sub216_float')
main_sub216_double = solver.IntVar(0, 1, 'main_sub216_double')
main_sub216_enob = solver.IntVar(-10000, 10000, 'main_sub216_enob')
solver.Add( + (1)*main_sub216_enob + (-1)*main_sub216_fixbits + (10000)*main_sub216_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub216_enob + (10000)*main_sub216_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub216_enob + (10000)*main_sub216_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub216_fixbits + (-10000)*main_sub216_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_sub216_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub216_enob
solver.Add( + (1)*main_sub216_fixp + (1)*main_sub216_float + (1)*main_sub216_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub216_fixbits + (-10000)*main_sub216_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*B_CAST_sub216_fixp + (-1)*main_mul215_CAST_sub216_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_sub216_float + (-1)*main_mul215_CAST_sub216_float==0)    #float equality
solver.Add( + (1)*B_CAST_sub216_double + (-1)*main_mul215_CAST_sub216_double==0)    #double equality
solver.Add( + (1)*B_CAST_sub216_fixbits + (-1)*main_mul215_CAST_sub216_fixbits==0)    #same fractional bit
solver.Add( + (1)*B_CAST_sub216_fixp + (-1)*main_sub216_fixp==0)    #fix equality
solver.Add( + (1)*B_CAST_sub216_float + (-1)*main_sub216_float==0)    #float equality
solver.Add( + (1)*B_CAST_sub216_double + (-1)*main_sub216_double==0)    #double equality
solver.Add( + (1)*B_CAST_sub216_fixbits + (-1)*main_sub216_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub216_fixp
mathCostObj +=  + (2.33125)*main_sub216_float
mathCostObj +=  + (2.72422)*main_sub216_double
solver.Add( + (1)*main_sub216_enob + (-1)*B_enob_memphi_main_tmp16<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub216_enob + (-1)*main_mul215_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp18 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp18')
solver.Add( + (1)*B_enob_memphi_main_tmp18 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp18_enob_1 = solver.IntVar(0, 1, 'main_main_tmp18_enob_1')
main_main_tmp18_enob_2 = solver.IntVar(0, 1, 'main_main_tmp18_enob_2')
main_main_tmp18_enob_3 = solver.IntVar(0, 1, 'main_main_tmp18_enob_3')
solver.Add( + (1)*main_main_tmp18_enob_1 + (1)*main_main_tmp18_enob_2 + (1)*main_main_tmp18_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp18 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp18_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp18 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp18_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add224 = fadd double %sub216, %tmp18, !taffo.info !64, !taffo.initweight !31
main_sub216_CAST_add224_fixbits = solver.IntVar(0, 16, 'main_sub216_CAST_add224_fixbits')
main_sub216_CAST_add224_fixp = solver.IntVar(0, 1, 'main_sub216_CAST_add224_fixp')
main_sub216_CAST_add224_float = solver.IntVar(0, 1, 'main_sub216_CAST_add224_float')
main_sub216_CAST_add224_double = solver.IntVar(0, 1, 'main_sub216_CAST_add224_double')
solver.Add( + (1)*main_sub216_CAST_add224_fixp + (1)*main_sub216_CAST_add224_float + (1)*main_sub216_CAST_add224_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub216_CAST_add224_fixbits + (-10000)*main_sub216_CAST_add224_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C1_main_sub216_CAST_add224')
C2_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C2_main_sub216_CAST_add224')
solver.Add( + (1)*main_sub216_fixbits + (-1)*main_sub216_CAST_add224_fixbits + (-10000)*C1_main_sub216_CAST_add224<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub216_fixbits + (1)*main_sub216_CAST_add224_fixbits + (-10000)*C2_main_sub216_CAST_add224<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub216_CAST_add224
castCostObj +=  + (1)*C2_main_sub216_CAST_add224
C3_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C3_main_sub216_CAST_add224')
C4_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C4_main_sub216_CAST_add224')
C5_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C5_main_sub216_CAST_add224')
C6_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C6_main_sub216_CAST_add224')
C7_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C7_main_sub216_CAST_add224')
C8_main_sub216_CAST_add224 = solver.IntVar(0, 1, 'C8_main_sub216_CAST_add224')
solver.Add( + (1)*main_sub216_fixp + (1)*main_sub216_CAST_add224_float + (-1)*C3_main_sub216_CAST_add224<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub216_CAST_add224
solver.Add( + (1)*main_sub216_float + (1)*main_sub216_CAST_add224_fixp + (-1)*C4_main_sub216_CAST_add224<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub216_CAST_add224
solver.Add( + (1)*main_sub216_fixp + (1)*main_sub216_CAST_add224_double + (-1)*C5_main_sub216_CAST_add224<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub216_CAST_add224
solver.Add( + (1)*main_sub216_double + (1)*main_sub216_CAST_add224_fixp + (-1)*C6_main_sub216_CAST_add224<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub216_CAST_add224
solver.Add( + (1)*main_sub216_float + (1)*main_sub216_CAST_add224_double + (-1)*C7_main_sub216_CAST_add224<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub216_CAST_add224
solver.Add( + (1)*main_sub216_double + (1)*main_sub216_CAST_add224_float + (-1)*C8_main_sub216_CAST_add224<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub216_CAST_add224



#Constraint for cast for   %add224 = fadd double %sub216, %tmp18, !taffo.info !64, !taffo.initweight !31
B_CAST_add224_fixbits = solver.IntVar(0, 17, 'B_CAST_add224_fixbits')
B_CAST_add224_fixp = solver.IntVar(0, 1, 'B_CAST_add224_fixp')
B_CAST_add224_float = solver.IntVar(0, 1, 'B_CAST_add224_float')
B_CAST_add224_double = solver.IntVar(0, 1, 'B_CAST_add224_double')
solver.Add( + (1)*B_CAST_add224_fixp + (1)*B_CAST_add224_float + (1)*B_CAST_add224_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_add224_fixbits + (-10000)*B_CAST_add224_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_add224 = solver.IntVar(0, 1, 'C1_B_CAST_add224')
C2_B_CAST_add224 = solver.IntVar(0, 1, 'C2_B_CAST_add224')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_add224_fixbits + (-10000)*C1_B_CAST_add224<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_add224_fixbits + (-10000)*C2_B_CAST_add224<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_add224
castCostObj +=  + (1)*C2_B_CAST_add224
C3_B_CAST_add224 = solver.IntVar(0, 1, 'C3_B_CAST_add224')
C4_B_CAST_add224 = solver.IntVar(0, 1, 'C4_B_CAST_add224')
C5_B_CAST_add224 = solver.IntVar(0, 1, 'C5_B_CAST_add224')
C6_B_CAST_add224 = solver.IntVar(0, 1, 'C6_B_CAST_add224')
C7_B_CAST_add224 = solver.IntVar(0, 1, 'C7_B_CAST_add224')
C8_B_CAST_add224 = solver.IntVar(0, 1, 'C8_B_CAST_add224')
solver.Add( + (1)*B_fixp + (1)*B_CAST_add224_float + (-1)*C3_B_CAST_add224<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_add224
solver.Add( + (1)*B_float + (1)*B_CAST_add224_fixp + (-1)*C4_B_CAST_add224<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_add224
solver.Add( + (1)*B_fixp + (1)*B_CAST_add224_double + (-1)*C5_B_CAST_add224<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_add224
solver.Add( + (1)*B_double + (1)*B_CAST_add224_fixp + (-1)*C6_B_CAST_add224<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_add224
solver.Add( + (1)*B_float + (1)*B_CAST_add224_double + (-1)*C7_B_CAST_add224<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_add224
solver.Add( + (1)*B_double + (1)*B_CAST_add224_float + (-1)*C8_B_CAST_add224<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_add224



#Stuff for   %add224 = fadd double %sub216, %tmp18, !taffo.info !64, !taffo.initweight !31
main_add224_fixbits = solver.IntVar(0, 15, 'main_add224_fixbits')
main_add224_fixp = solver.IntVar(0, 1, 'main_add224_fixp')
main_add224_float = solver.IntVar(0, 1, 'main_add224_float')
main_add224_double = solver.IntVar(0, 1, 'main_add224_double')
main_add224_enob = solver.IntVar(-10000, 10000, 'main_add224_enob')
solver.Add( + (1)*main_add224_enob + (-1)*main_add224_fixbits + (10000)*main_add224_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add224_enob + (10000)*main_add224_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add224_enob + (10000)*main_add224_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add224_fixbits + (-10000)*main_add224_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add224_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add224_enob
solver.Add( + (1)*main_add224_fixp + (1)*main_add224_float + (1)*main_add224_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add224_fixbits + (-10000)*main_add224_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub216_CAST_add224_fixp + (-1)*B_CAST_add224_fixp==0)    #fix equality
solver.Add( + (1)*main_sub216_CAST_add224_float + (-1)*B_CAST_add224_float==0)    #float equality
solver.Add( + (1)*main_sub216_CAST_add224_double + (-1)*B_CAST_add224_double==0)    #double equality
solver.Add( + (1)*main_sub216_CAST_add224_fixbits + (-1)*B_CAST_add224_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub216_CAST_add224_fixp + (-1)*main_add224_fixp==0)    #fix equality
solver.Add( + (1)*main_sub216_CAST_add224_float + (-1)*main_add224_float==0)    #float equality
solver.Add( + (1)*main_sub216_CAST_add224_double + (-1)*main_add224_double==0)    #double equality
solver.Add( + (1)*main_sub216_CAST_add224_fixbits + (-1)*main_add224_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add224_fixp
mathCostObj +=  + (2.33125)*main_add224_float
mathCostObj +=  + (2.72422)*main_add224_double
solver.Add( + (1)*main_add224_enob + (-1)*main_sub216_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add224_enob + (-1)*B_enob_memphi_main_tmp18<=0)    #Enob propagation in sum second addend



#Stuff for double 1.250000e-01
ConstantValue__35_fixbits = solver.IntVar(0, 31, 'ConstantValue__35_fixbits')
ConstantValue__35_fixp = solver.IntVar(0, 1, 'ConstantValue__35_fixp')
ConstantValue__35_float = solver.IntVar(0, 1, 'ConstantValue__35_float')
ConstantValue__35_double = solver.IntVar(0, 1, 'ConstantValue__35_double')
ConstantValue__35_enob = solver.IntVar(-10000, 10000, 'ConstantValue__35_enob')
solver.Add( + (1)*ConstantValue__35_enob + (-1)*ConstantValue__35_fixbits + (10000)*ConstantValue__35_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__35_fixp + (1)*ConstantValue__35_float + (1)*ConstantValue__35_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__36_fixbits = solver.IntVar(0, 31, 'ConstantValue__36_fixbits')
ConstantValue__36_fixp = solver.IntVar(0, 1, 'ConstantValue__36_fixp')
ConstantValue__36_float = solver.IntVar(0, 1, 'ConstantValue__36_float')
ConstantValue__36_double = solver.IntVar(0, 1, 'ConstantValue__36_double')
ConstantValue__36_enob = solver.IntVar(-10000, 10000, 'ConstantValue__36_enob')
solver.Add( + (1)*ConstantValue__36_enob + (-1)*ConstantValue__36_fixbits + (10000)*ConstantValue__36_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__36_enob + (10000)*ConstantValue__36_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__36_enob + (10000)*ConstantValue__36_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__36_fixbits + (-10000)*ConstantValue__36_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__36_fixp + (1)*ConstantValue__36_float + (1)*ConstantValue__36_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__36_fixbits + (-10000)*ConstantValue__36_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e-01
ConstantValue__37_fixbits = solver.IntVar(0, 31, 'ConstantValue__37_fixbits')
ConstantValue__37_fixp = solver.IntVar(0, 1, 'ConstantValue__37_fixp')
ConstantValue__37_float = solver.IntVar(0, 1, 'ConstantValue__37_float')
ConstantValue__37_double = solver.IntVar(0, 1, 'ConstantValue__37_double')
ConstantValue__37_enob = solver.IntVar(-10000, 10000, 'ConstantValue__37_enob')
solver.Add( + (1)*ConstantValue__37_enob + (-1)*ConstantValue__37_fixbits + (10000)*ConstantValue__37_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_float + (1)*ConstantValue__37_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul225 = fmul double 1.250000e-01, %add224, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
ConstantValue__37_CAST_mul225_fixbits = solver.IntVar(0, 31, 'ConstantValue__37_CAST_mul225_fixbits')
ConstantValue__37_CAST_mul225_fixp = solver.IntVar(0, 1, 'ConstantValue__37_CAST_mul225_fixp')
ConstantValue__37_CAST_mul225_float = solver.IntVar(0, 1, 'ConstantValue__37_CAST_mul225_float')
ConstantValue__37_CAST_mul225_double = solver.IntVar(0, 1, 'ConstantValue__37_CAST_mul225_double')
solver.Add( + (1)*ConstantValue__37_CAST_mul225_fixp + (1)*ConstantValue__37_CAST_mul225_float + (1)*ConstantValue__37_CAST_mul225_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__37_CAST_mul225_fixbits + (-10000)*ConstantValue__37_CAST_mul225_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C1_ConstantValue__37_CAST_mul225')
C2_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C2_ConstantValue__37_CAST_mul225')
solver.Add( + (1)*ConstantValue__37_fixbits + (-1)*ConstantValue__37_CAST_mul225_fixbits + (-10000)*C1_ConstantValue__37_CAST_mul225<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__37_fixbits + (1)*ConstantValue__37_CAST_mul225_fixbits + (-10000)*C2_ConstantValue__37_CAST_mul225<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__37_CAST_mul225
castCostObj +=  + (1)*C2_ConstantValue__37_CAST_mul225
C3_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C3_ConstantValue__37_CAST_mul225')
C4_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C4_ConstantValue__37_CAST_mul225')
C5_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C5_ConstantValue__37_CAST_mul225')
C6_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C6_ConstantValue__37_CAST_mul225')
C7_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C7_ConstantValue__37_CAST_mul225')
C8_ConstantValue__37_CAST_mul225 = solver.IntVar(0, 1, 'C8_ConstantValue__37_CAST_mul225')
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_CAST_mul225_float + (-1)*C3_ConstantValue__37_CAST_mul225<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__37_CAST_mul225
solver.Add( + (1)*ConstantValue__37_float + (1)*ConstantValue__37_CAST_mul225_fixp + (-1)*C4_ConstantValue__37_CAST_mul225<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__37_CAST_mul225
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_CAST_mul225_double + (-1)*C5_ConstantValue__37_CAST_mul225<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__37_CAST_mul225
solver.Add( + (1)*ConstantValue__37_double + (1)*ConstantValue__37_CAST_mul225_fixp + (-1)*C6_ConstantValue__37_CAST_mul225<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__37_CAST_mul225
solver.Add( + (1)*ConstantValue__37_float + (1)*ConstantValue__37_CAST_mul225_double + (-1)*C7_ConstantValue__37_CAST_mul225<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__37_CAST_mul225
solver.Add( + (1)*ConstantValue__37_double + (1)*ConstantValue__37_CAST_mul225_float + (-1)*C8_ConstantValue__37_CAST_mul225<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__37_CAST_mul225



#Constraint for cast for   %mul225 = fmul double 1.250000e-01, %add224, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
main_add224_CAST_mul225_fixbits = solver.IntVar(0, 15, 'main_add224_CAST_mul225_fixbits')
main_add224_CAST_mul225_fixp = solver.IntVar(0, 1, 'main_add224_CAST_mul225_fixp')
main_add224_CAST_mul225_float = solver.IntVar(0, 1, 'main_add224_CAST_mul225_float')
main_add224_CAST_mul225_double = solver.IntVar(0, 1, 'main_add224_CAST_mul225_double')
solver.Add( + (1)*main_add224_CAST_mul225_fixp + (1)*main_add224_CAST_mul225_float + (1)*main_add224_CAST_mul225_double==1)    #exactly 1 type
solver.Add( + (1)*main_add224_CAST_mul225_fixbits + (-10000)*main_add224_CAST_mul225_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C1_main_add224_CAST_mul225')
C2_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C2_main_add224_CAST_mul225')
solver.Add( + (1)*main_add224_fixbits + (-1)*main_add224_CAST_mul225_fixbits + (-10000)*C1_main_add224_CAST_mul225<=0)    #Shift cost 1
solver.Add( + (-1)*main_add224_fixbits + (1)*main_add224_CAST_mul225_fixbits + (-10000)*C2_main_add224_CAST_mul225<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add224_CAST_mul225
castCostObj +=  + (1)*C2_main_add224_CAST_mul225
C3_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C3_main_add224_CAST_mul225')
C4_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C4_main_add224_CAST_mul225')
C5_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C5_main_add224_CAST_mul225')
C6_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C6_main_add224_CAST_mul225')
C7_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C7_main_add224_CAST_mul225')
C8_main_add224_CAST_mul225 = solver.IntVar(0, 1, 'C8_main_add224_CAST_mul225')
solver.Add( + (1)*main_add224_fixp + (1)*main_add224_CAST_mul225_float + (-1)*C3_main_add224_CAST_mul225<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add224_CAST_mul225
solver.Add( + (1)*main_add224_float + (1)*main_add224_CAST_mul225_fixp + (-1)*C4_main_add224_CAST_mul225<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add224_CAST_mul225
solver.Add( + (1)*main_add224_fixp + (1)*main_add224_CAST_mul225_double + (-1)*C5_main_add224_CAST_mul225<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add224_CAST_mul225
solver.Add( + (1)*main_add224_double + (1)*main_add224_CAST_mul225_fixp + (-1)*C6_main_add224_CAST_mul225<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add224_CAST_mul225
solver.Add( + (1)*main_add224_float + (1)*main_add224_CAST_mul225_double + (-1)*C7_main_add224_CAST_mul225<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add224_CAST_mul225
solver.Add( + (1)*main_add224_double + (1)*main_add224_CAST_mul225_float + (-1)*C8_main_add224_CAST_mul225<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add224_CAST_mul225



#Stuff for   %mul225 = fmul double 1.250000e-01, %add224, !taffo.info !66, !taffo.initweight !35, !taffo.constinfo !52
main_mul225_fixbits = solver.IntVar(0, 18, 'main_mul225_fixbits')
main_mul225_fixp = solver.IntVar(0, 1, 'main_mul225_fixp')
main_mul225_float = solver.IntVar(0, 1, 'main_mul225_float')
main_mul225_double = solver.IntVar(0, 1, 'main_mul225_double')
main_mul225_enob = solver.IntVar(-10000, 10000, 'main_mul225_enob')
solver.Add( + (1)*main_mul225_enob + (-1)*main_mul225_fixbits + (10000)*main_mul225_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul225_enob + (10000)*main_mul225_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul225_enob + (10000)*main_mul225_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul225_fixbits + (-10000)*main_mul225_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_mul225_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul225_enob
solver.Add( + (1)*main_mul225_fixp + (1)*main_mul225_float + (1)*main_mul225_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul225_fixbits + (-10000)*main_mul225_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__37_CAST_mul225_fixp + (-1)*main_add224_CAST_mul225_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__37_CAST_mul225_float + (-1)*main_add224_CAST_mul225_float==0)    #float equality
solver.Add( + (1)*ConstantValue__37_CAST_mul225_double + (-1)*main_add224_CAST_mul225_double==0)    #double equality
solver.Add( + (1)*ConstantValue__37_CAST_mul225_fixp + (-1)*main_mul225_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__37_CAST_mul225_float + (-1)*main_mul225_float==0)    #float equality
solver.Add( + (1)*ConstantValue__37_CAST_mul225_double + (-1)*main_mul225_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul225_fixp
mathCostObj +=  + (2.64722)*main_mul225_float
mathCostObj +=  + (4.02255)*main_mul225_double
main_main_mul225_enob_1 = solver.IntVar(0, 1, 'main_main_mul225_enob_1')
main_main_mul225_enob_2 = solver.IntVar(0, 1, 'main_main_mul225_enob_2')
solver.Add( + (1)*main_main_mul225_enob_1 + (1)*main_main_mul225_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul225_enob + (-1)*main_add224_enob + (-10000)*main_main_mul225_enob_1<=3)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul225_enob + (-1)*ConstantValue__35_enob + (-10000)*main_main_mul225_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add226 = fadd double %add201, %mul225, !taffo.info !70, !taffo.initweight !57
main_add201_CAST_add226_fixbits = solver.IntVar(0, 17, 'main_add201_CAST_add226_fixbits')
main_add201_CAST_add226_fixp = solver.IntVar(0, 1, 'main_add201_CAST_add226_fixp')
main_add201_CAST_add226_float = solver.IntVar(0, 1, 'main_add201_CAST_add226_float')
main_add201_CAST_add226_double = solver.IntVar(0, 1, 'main_add201_CAST_add226_double')
solver.Add( + (1)*main_add201_CAST_add226_fixp + (1)*main_add201_CAST_add226_float + (1)*main_add201_CAST_add226_double==1)    #exactly 1 type
solver.Add( + (1)*main_add201_CAST_add226_fixbits + (-10000)*main_add201_CAST_add226_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C1_main_add201_CAST_add226')
C2_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C2_main_add201_CAST_add226')
solver.Add( + (1)*main_add201_fixbits + (-1)*main_add201_CAST_add226_fixbits + (-10000)*C1_main_add201_CAST_add226<=0)    #Shift cost 1
solver.Add( + (-1)*main_add201_fixbits + (1)*main_add201_CAST_add226_fixbits + (-10000)*C2_main_add201_CAST_add226<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add201_CAST_add226
castCostObj +=  + (1)*C2_main_add201_CAST_add226
C3_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C3_main_add201_CAST_add226')
C4_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C4_main_add201_CAST_add226')
C5_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C5_main_add201_CAST_add226')
C6_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C6_main_add201_CAST_add226')
C7_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C7_main_add201_CAST_add226')
C8_main_add201_CAST_add226 = solver.IntVar(0, 1, 'C8_main_add201_CAST_add226')
solver.Add( + (1)*main_add201_fixp + (1)*main_add201_CAST_add226_float + (-1)*C3_main_add201_CAST_add226<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add201_CAST_add226
solver.Add( + (1)*main_add201_float + (1)*main_add201_CAST_add226_fixp + (-1)*C4_main_add201_CAST_add226<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add201_CAST_add226
solver.Add( + (1)*main_add201_fixp + (1)*main_add201_CAST_add226_double + (-1)*C5_main_add201_CAST_add226<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add201_CAST_add226
solver.Add( + (1)*main_add201_double + (1)*main_add201_CAST_add226_fixp + (-1)*C6_main_add201_CAST_add226<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add201_CAST_add226
solver.Add( + (1)*main_add201_float + (1)*main_add201_CAST_add226_double + (-1)*C7_main_add201_CAST_add226<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add201_CAST_add226
solver.Add( + (1)*main_add201_double + (1)*main_add201_CAST_add226_float + (-1)*C8_main_add201_CAST_add226<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add201_CAST_add226



#Constraint for cast for   %add226 = fadd double %add201, %mul225, !taffo.info !70, !taffo.initweight !57
main_mul225_CAST_add226_fixbits = solver.IntVar(0, 18, 'main_mul225_CAST_add226_fixbits')
main_mul225_CAST_add226_fixp = solver.IntVar(0, 1, 'main_mul225_CAST_add226_fixp')
main_mul225_CAST_add226_float = solver.IntVar(0, 1, 'main_mul225_CAST_add226_float')
main_mul225_CAST_add226_double = solver.IntVar(0, 1, 'main_mul225_CAST_add226_double')
solver.Add( + (1)*main_mul225_CAST_add226_fixp + (1)*main_mul225_CAST_add226_float + (1)*main_mul225_CAST_add226_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul225_CAST_add226_fixbits + (-10000)*main_mul225_CAST_add226_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C1_main_mul225_CAST_add226')
C2_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C2_main_mul225_CAST_add226')
solver.Add( + (1)*main_mul225_fixbits + (-1)*main_mul225_CAST_add226_fixbits + (-10000)*C1_main_mul225_CAST_add226<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul225_fixbits + (1)*main_mul225_CAST_add226_fixbits + (-10000)*C2_main_mul225_CAST_add226<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul225_CAST_add226
castCostObj +=  + (1)*C2_main_mul225_CAST_add226
C3_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C3_main_mul225_CAST_add226')
C4_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C4_main_mul225_CAST_add226')
C5_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C5_main_mul225_CAST_add226')
C6_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C6_main_mul225_CAST_add226')
C7_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C7_main_mul225_CAST_add226')
C8_main_mul225_CAST_add226 = solver.IntVar(0, 1, 'C8_main_mul225_CAST_add226')
solver.Add( + (1)*main_mul225_fixp + (1)*main_mul225_CAST_add226_float + (-1)*C3_main_mul225_CAST_add226<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul225_CAST_add226
solver.Add( + (1)*main_mul225_float + (1)*main_mul225_CAST_add226_fixp + (-1)*C4_main_mul225_CAST_add226<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul225_CAST_add226
solver.Add( + (1)*main_mul225_fixp + (1)*main_mul225_CAST_add226_double + (-1)*C5_main_mul225_CAST_add226<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul225_CAST_add226
solver.Add( + (1)*main_mul225_double + (1)*main_mul225_CAST_add226_fixp + (-1)*C6_main_mul225_CAST_add226<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul225_CAST_add226
solver.Add( + (1)*main_mul225_float + (1)*main_mul225_CAST_add226_double + (-1)*C7_main_mul225_CAST_add226<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul225_CAST_add226
solver.Add( + (1)*main_mul225_double + (1)*main_mul225_CAST_add226_float + (-1)*C8_main_mul225_CAST_add226<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul225_CAST_add226



#Stuff for   %add226 = fadd double %add201, %mul225, !taffo.info !70, !taffo.initweight !57
main_add226_fixbits = solver.IntVar(0, 17, 'main_add226_fixbits')
main_add226_fixp = solver.IntVar(0, 1, 'main_add226_fixp')
main_add226_float = solver.IntVar(0, 1, 'main_add226_float')
main_add226_double = solver.IntVar(0, 1, 'main_add226_double')
main_add226_enob = solver.IntVar(-10000, 10000, 'main_add226_enob')
solver.Add( + (1)*main_add226_enob + (-1)*main_add226_fixbits + (10000)*main_add226_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add226_enob + (10000)*main_add226_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add226_enob + (10000)*main_add226_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add226_fixbits + (-10000)*main_add226_fixp>=-9984)    #Limit the lower number of frac bits17
solver.Add( + (1)*main_add226_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add226_enob
solver.Add( + (1)*main_add226_fixp + (1)*main_add226_float + (1)*main_add226_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add226_fixbits + (-10000)*main_add226_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add201_CAST_add226_fixp + (-1)*main_mul225_CAST_add226_fixp==0)    #fix equality
solver.Add( + (1)*main_add201_CAST_add226_float + (-1)*main_mul225_CAST_add226_float==0)    #float equality
solver.Add( + (1)*main_add201_CAST_add226_double + (-1)*main_mul225_CAST_add226_double==0)    #double equality
solver.Add( + (1)*main_add201_CAST_add226_fixbits + (-1)*main_mul225_CAST_add226_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add201_CAST_add226_fixp + (-1)*main_add226_fixp==0)    #fix equality
solver.Add( + (1)*main_add201_CAST_add226_float + (-1)*main_add226_float==0)    #float equality
solver.Add( + (1)*main_add201_CAST_add226_double + (-1)*main_add226_double==0)    #double equality
solver.Add( + (1)*main_add201_CAST_add226_fixbits + (-1)*main_add226_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add226_fixp
mathCostObj +=  + (2.33125)*main_add226_float
mathCostObj +=  + (2.72422)*main_add226_double
solver.Add( + (1)*main_add226_enob + (-1)*main_add201_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add226_enob + (-1)*main_mul225_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp19 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp19')
solver.Add( + (1)*B_enob_memphi_main_tmp19 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp19_enob_1 = solver.IntVar(0, 1, 'main_main_tmp19_enob_1')
main_main_tmp19_enob_2 = solver.IntVar(0, 1, 'main_main_tmp19_enob_2')
main_main_tmp19_enob_3 = solver.IntVar(0, 1, 'main_main_tmp19_enob_3')
solver.Add( + (1)*main_main_tmp19_enob_1 + (1)*main_main_tmp19_enob_2 + (1)*main_main_tmp19_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp19 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp19_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp19 + (-1)*B_enob_storeENOB_storeENOB + (10000)*main_main_tmp19_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add233 = fadd double %add226, %tmp19, !taffo.info !12, !taffo.initweight !31
main_add226_CAST_add233_fixbits = solver.IntVar(0, 17, 'main_add226_CAST_add233_fixbits')
main_add226_CAST_add233_fixp = solver.IntVar(0, 1, 'main_add226_CAST_add233_fixp')
main_add226_CAST_add233_float = solver.IntVar(0, 1, 'main_add226_CAST_add233_float')
main_add226_CAST_add233_double = solver.IntVar(0, 1, 'main_add226_CAST_add233_double')
solver.Add( + (1)*main_add226_CAST_add233_fixp + (1)*main_add226_CAST_add233_float + (1)*main_add226_CAST_add233_double==1)    #exactly 1 type
solver.Add( + (1)*main_add226_CAST_add233_fixbits + (-10000)*main_add226_CAST_add233_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C1_main_add226_CAST_add233')
C2_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C2_main_add226_CAST_add233')
solver.Add( + (1)*main_add226_fixbits + (-1)*main_add226_CAST_add233_fixbits + (-10000)*C1_main_add226_CAST_add233<=0)    #Shift cost 1
solver.Add( + (-1)*main_add226_fixbits + (1)*main_add226_CAST_add233_fixbits + (-10000)*C2_main_add226_CAST_add233<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add226_CAST_add233
castCostObj +=  + (1)*C2_main_add226_CAST_add233
C3_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C3_main_add226_CAST_add233')
C4_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C4_main_add226_CAST_add233')
C5_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C5_main_add226_CAST_add233')
C6_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C6_main_add226_CAST_add233')
C7_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C7_main_add226_CAST_add233')
C8_main_add226_CAST_add233 = solver.IntVar(0, 1, 'C8_main_add226_CAST_add233')
solver.Add( + (1)*main_add226_fixp + (1)*main_add226_CAST_add233_float + (-1)*C3_main_add226_CAST_add233<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add226_CAST_add233
solver.Add( + (1)*main_add226_float + (1)*main_add226_CAST_add233_fixp + (-1)*C4_main_add226_CAST_add233<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add226_CAST_add233
solver.Add( + (1)*main_add226_fixp + (1)*main_add226_CAST_add233_double + (-1)*C5_main_add226_CAST_add233<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add226_CAST_add233
solver.Add( + (1)*main_add226_double + (1)*main_add226_CAST_add233_fixp + (-1)*C6_main_add226_CAST_add233<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add226_CAST_add233
solver.Add( + (1)*main_add226_float + (1)*main_add226_CAST_add233_double + (-1)*C7_main_add226_CAST_add233<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add226_CAST_add233
solver.Add( + (1)*main_add226_double + (1)*main_add226_CAST_add233_float + (-1)*C8_main_add226_CAST_add233<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add226_CAST_add233



#Constraint for cast for   %add233 = fadd double %add226, %tmp19, !taffo.info !12, !taffo.initweight !31
B_CAST_add233_fixbits = solver.IntVar(0, 17, 'B_CAST_add233_fixbits')
B_CAST_add233_fixp = solver.IntVar(0, 1, 'B_CAST_add233_fixp')
B_CAST_add233_float = solver.IntVar(0, 1, 'B_CAST_add233_float')
B_CAST_add233_double = solver.IntVar(0, 1, 'B_CAST_add233_double')
solver.Add( + (1)*B_CAST_add233_fixp + (1)*B_CAST_add233_float + (1)*B_CAST_add233_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_add233_fixbits + (-10000)*B_CAST_add233_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_add233 = solver.IntVar(0, 1, 'C1_B_CAST_add233')
C2_B_CAST_add233 = solver.IntVar(0, 1, 'C2_B_CAST_add233')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_add233_fixbits + (-10000)*C1_B_CAST_add233<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_add233_fixbits + (-10000)*C2_B_CAST_add233<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_add233
castCostObj +=  + (1)*C2_B_CAST_add233
C3_B_CAST_add233 = solver.IntVar(0, 1, 'C3_B_CAST_add233')
C4_B_CAST_add233 = solver.IntVar(0, 1, 'C4_B_CAST_add233')
C5_B_CAST_add233 = solver.IntVar(0, 1, 'C5_B_CAST_add233')
C6_B_CAST_add233 = solver.IntVar(0, 1, 'C6_B_CAST_add233')
C7_B_CAST_add233 = solver.IntVar(0, 1, 'C7_B_CAST_add233')
C8_B_CAST_add233 = solver.IntVar(0, 1, 'C8_B_CAST_add233')
solver.Add( + (1)*B_fixp + (1)*B_CAST_add233_float + (-1)*C3_B_CAST_add233<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_add233
solver.Add( + (1)*B_float + (1)*B_CAST_add233_fixp + (-1)*C4_B_CAST_add233<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_add233
solver.Add( + (1)*B_fixp + (1)*B_CAST_add233_double + (-1)*C5_B_CAST_add233<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_add233
solver.Add( + (1)*B_double + (1)*B_CAST_add233_fixp + (-1)*C6_B_CAST_add233<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_add233
solver.Add( + (1)*B_float + (1)*B_CAST_add233_double + (-1)*C7_B_CAST_add233<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_add233
solver.Add( + (1)*B_double + (1)*B_CAST_add233_float + (-1)*C8_B_CAST_add233<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_add233



#Stuff for   %add233 = fadd double %add226, %tmp19, !taffo.info !12, !taffo.initweight !31
main_add233_fixbits = solver.IntVar(0, 16, 'main_add233_fixbits')
main_add233_fixp = solver.IntVar(0, 1, 'main_add233_fixp')
main_add233_float = solver.IntVar(0, 1, 'main_add233_float')
main_add233_double = solver.IntVar(0, 1, 'main_add233_double')
main_add233_enob = solver.IntVar(-10000, 10000, 'main_add233_enob')
solver.Add( + (1)*main_add233_enob + (-1)*main_add233_fixbits + (10000)*main_add233_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add233_enob + (10000)*main_add233_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add233_enob + (10000)*main_add233_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add233_fixbits + (-10000)*main_add233_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_add233_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add233_enob
solver.Add( + (1)*main_add233_fixp + (1)*main_add233_float + (1)*main_add233_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add233_fixbits + (-10000)*main_add233_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add226_CAST_add233_fixp + (-1)*B_CAST_add233_fixp==0)    #fix equality
solver.Add( + (1)*main_add226_CAST_add233_float + (-1)*B_CAST_add233_float==0)    #float equality
solver.Add( + (1)*main_add226_CAST_add233_double + (-1)*B_CAST_add233_double==0)    #double equality
solver.Add( + (1)*main_add226_CAST_add233_fixbits + (-1)*B_CAST_add233_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add226_CAST_add233_fixp + (-1)*main_add233_fixp==0)    #fix equality
solver.Add( + (1)*main_add226_CAST_add233_float + (-1)*main_add233_float==0)    #float equality
solver.Add( + (1)*main_add226_CAST_add233_double + (-1)*main_add233_double==0)    #double equality
solver.Add( + (1)*main_add226_CAST_add233_fixbits + (-1)*main_add233_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add233_fixp
mathCostObj +=  + (2.33125)*main_add233_float
mathCostObj +=  + (2.72422)*main_add233_double
solver.Add( + (1)*main_add233_enob + (-1)*main_add226_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add233_enob + (-1)*B_enob_memphi_main_tmp19<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add233, double* %arrayidx239, align 8, !taffo.info !37, !taffo.initweight !28
main_add233_CAST_store_fixbits = solver.IntVar(0, 16, 'main_add233_CAST_store_fixbits')
main_add233_CAST_store_fixp = solver.IntVar(0, 1, 'main_add233_CAST_store_fixp')
main_add233_CAST_store_float = solver.IntVar(0, 1, 'main_add233_CAST_store_float')
main_add233_CAST_store_double = solver.IntVar(0, 1, 'main_add233_CAST_store_double')
solver.Add( + (1)*main_add233_CAST_store_fixp + (1)*main_add233_CAST_store_float + (1)*main_add233_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add233_CAST_store_fixbits + (-10000)*main_add233_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add233_CAST_store = solver.IntVar(0, 1, 'C1_main_add233_CAST_store')
C2_main_add233_CAST_store = solver.IntVar(0, 1, 'C2_main_add233_CAST_store')
solver.Add( + (1)*main_add233_fixbits + (-1)*main_add233_CAST_store_fixbits + (-10000)*C1_main_add233_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add233_fixbits + (1)*main_add233_CAST_store_fixbits + (-10000)*C2_main_add233_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add233_CAST_store
castCostObj +=  + (1)*C2_main_add233_CAST_store
C3_main_add233_CAST_store = solver.IntVar(0, 1, 'C3_main_add233_CAST_store')
C4_main_add233_CAST_store = solver.IntVar(0, 1, 'C4_main_add233_CAST_store')
C5_main_add233_CAST_store = solver.IntVar(0, 1, 'C5_main_add233_CAST_store')
C6_main_add233_CAST_store = solver.IntVar(0, 1, 'C6_main_add233_CAST_store')
C7_main_add233_CAST_store = solver.IntVar(0, 1, 'C7_main_add233_CAST_store')
C8_main_add233_CAST_store = solver.IntVar(0, 1, 'C8_main_add233_CAST_store')
solver.Add( + (1)*main_add233_fixp + (1)*main_add233_CAST_store_float + (-1)*C3_main_add233_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add233_CAST_store
solver.Add( + (1)*main_add233_float + (1)*main_add233_CAST_store_fixp + (-1)*C4_main_add233_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add233_CAST_store
solver.Add( + (1)*main_add233_fixp + (1)*main_add233_CAST_store_double + (-1)*C5_main_add233_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add233_CAST_store
solver.Add( + (1)*main_add233_double + (1)*main_add233_CAST_store_fixp + (-1)*C6_main_add233_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add233_CAST_store
solver.Add( + (1)*main_add233_float + (1)*main_add233_CAST_store_double + (-1)*C7_main_add233_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add233_CAST_store
solver.Add( + (1)*main_add233_double + (1)*main_add233_CAST_store_float + (-1)*C8_main_add233_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add233_CAST_store
solver.Add( + (1)*A_fixp + (-1)*main_add233_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*A_float + (-1)*main_add233_CAST_store_float==0)    #float equality
solver.Add( + (1)*A_double + (-1)*main_add233_CAST_store_double==0)    #double equality
solver.Add( + (1)*A_fixbits + (-1)*main_add233_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
A_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'A_enob_storeENOB_storeENOB')
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (-1)*main_add233_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp2 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp2_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp3 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp4 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp5 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp7 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp8 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp9 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp10 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp11 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp12 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp13 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp14 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp14_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp15 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp15_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp16 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp17 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp18 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp18_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp19 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp19_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp22 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp22')
solver.Add( + (1)*A_enob_memphi_main_tmp22 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call277 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp21, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.4, i32 0, i32 0), double %tmp22), !taffo.info !37, !taffo.initweight !31, !taffo.constinfo !81
A_CAST_call277_fixbits = solver.IntVar(0, 16, 'A_CAST_call277_fixbits')
A_CAST_call277_fixp = solver.IntVar(0, 1, 'A_CAST_call277_fixp')
A_CAST_call277_float = solver.IntVar(0, 1, 'A_CAST_call277_float')
A_CAST_call277_double = solver.IntVar(0, 1, 'A_CAST_call277_double')
solver.Add( + (1)*A_CAST_call277_fixp + (1)*A_CAST_call277_float + (1)*A_CAST_call277_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_call277_fixbits + (-10000)*A_CAST_call277_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_call277 = solver.IntVar(0, 1, 'C1_A_CAST_call277')
C2_A_CAST_call277 = solver.IntVar(0, 1, 'C2_A_CAST_call277')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_call277_fixbits + (-10000)*C1_A_CAST_call277<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_call277_fixbits + (-10000)*C2_A_CAST_call277<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_call277
castCostObj +=  + (1)*C2_A_CAST_call277
C3_A_CAST_call277 = solver.IntVar(0, 1, 'C3_A_CAST_call277')
C4_A_CAST_call277 = solver.IntVar(0, 1, 'C4_A_CAST_call277')
C5_A_CAST_call277 = solver.IntVar(0, 1, 'C5_A_CAST_call277')
C6_A_CAST_call277 = solver.IntVar(0, 1, 'C6_A_CAST_call277')
C7_A_CAST_call277 = solver.IntVar(0, 1, 'C7_A_CAST_call277')
C8_A_CAST_call277 = solver.IntVar(0, 1, 'C8_A_CAST_call277')
solver.Add( + (1)*A_fixp + (1)*A_CAST_call277_float + (-1)*C3_A_CAST_call277<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_call277
solver.Add( + (1)*A_float + (1)*A_CAST_call277_fixp + (-1)*C4_A_CAST_call277<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_call277
solver.Add( + (1)*A_fixp + (1)*A_CAST_call277_double + (-1)*C5_A_CAST_call277<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_call277
solver.Add( + (1)*A_double + (1)*A_CAST_call277_fixp + (-1)*C6_A_CAST_call277<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_call277
solver.Add( + (1)*A_float + (1)*A_CAST_call277_double + (-1)*C7_A_CAST_call277<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_call277
solver.Add( + (1)*A_double + (1)*A_CAST_call277_float + (-1)*C8_A_CAST_call277<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_call277
solver.Add( + (1)*A_CAST_call277_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 1372.53+ 1 * enobCostObj / 11704+ 1000 * mathCostObj / 119.656)

# Model declaration end.