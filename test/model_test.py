


#Stuff for @A = common dso_local global [20 x [30 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !10
A_fixbits = solver.IntVar(0, 21, 'A_fixbits')
A_fixp = solver.IntVar(0, 1, 'A_fixp')
A_float = solver.IntVar(0, 1, 'A_float')
A_double = solver.IntVar(0, 1, 'A_double')
A_enob = solver.IntVar(-10000, 10000, 'A_enob')
solver.Add( + (1)*A_enob + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_fixbits + (-10000)*A_fixp>=-9980)    #Limit the lower number of frac bits21
enobCostObj =  + (-1)*A_enob
solver.Add( + (1)*A_fixp + (1)*A_float + (1)*A_double==1)    #Exactly one selected type
solver.Add( + (1)*A_fixbits + (-10000)*A_fixp<=0)    #If not fix, frac part to zero



#Stuff for @Q = common dso_local global [20 x [30 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !10
Q_fixbits = solver.IntVar(0, 21, 'Q_fixbits')
Q_fixp = solver.IntVar(0, 1, 'Q_fixp')
Q_float = solver.IntVar(0, 1, 'Q_float')
Q_double = solver.IntVar(0, 1, 'Q_double')
Q_enob = solver.IntVar(-10000, 10000, 'Q_enob')
solver.Add( + (1)*Q_enob + (-1)*Q_fixbits + (10000)*Q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*Q_enob + (10000)*Q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*Q_enob + (10000)*Q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*Q_fixbits + (-10000)*Q_fixp>=-9980)    #Limit the lower number of frac bits21
enobCostObj +=  + (-1)*Q_enob
solver.Add( + (1)*Q_fixp + (1)*Q_float + (1)*Q_double==1)    #Exactly one selected type
solver.Add( + (1)*Q_fixbits + (-10000)*Q_fixp<=0)    #If not fix, frac part to zero



#Stuff for @R = common dso_local global [30 x [30 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !10
R_fixbits = solver.IntVar(0, 21, 'R_fixbits')
R_fixp = solver.IntVar(0, 1, 'R_fixp')
R_float = solver.IntVar(0, 1, 'R_float')
R_double = solver.IntVar(0, 1, 'R_double')
R_enob = solver.IntVar(-10000, 10000, 'R_enob')
solver.Add( + (1)*R_enob + (-1)*R_fixbits + (10000)*R_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*R_enob + (10000)*R_float<=10149)    #Enob constraint for float
solver.Add( + (1)*R_enob + (10000)*R_double<=11074)    #Enob constraint for double
solver.Add( + (1)*R_fixbits + (-10000)*R_fixp>=-9980)    #Limit the lower number of frac bits21
enobCostObj +=  + (-1)*R_enob
solver.Add( + (1)*R_fixp + (1)*R_float + (1)*R_double==1)    #Exactly one selected type
solver.Add( + (1)*R_fixbits + (-10000)*R_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %rem to double, !taffo.info !22, !taffo.initweight !25
main_conv_fixbits = solver.IntVar(0, 26, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9975)    #Limit the lower number of frac bits26
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv6 = sitofp i32 20 to double, !taffo.info !26
main_conv6_fixbits = solver.IntVar(0, 27, 'main_conv6_fixbits')
main_conv6_fixp = solver.IntVar(0, 1, 'main_conv6_fixp')
main_conv6_float = solver.IntVar(0, 1, 'main_conv6_float')
main_conv6_double = solver.IntVar(0, 1, 'main_conv6_double')
main_conv6_enob = solver.IntVar(-10000, 10000, 'main_conv6_enob')
solver.Add( + (1)*main_conv6_enob + (-1)*main_conv6_fixbits + (10000)*main_conv6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv6_enob + (10000)*main_conv6_float<=10019)    #Enob constraint for float
solver.Add( + (1)*main_conv6_enob + (10000)*main_conv6_double<=10048)    #Enob constraint for double
solver.Add( + (1)*main_conv6_fixbits + (-10000)*main_conv6_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv6_enob
solver.Add( + (1)*main_conv6_fixp + (1)*main_conv6_float + (1)*main_conv6_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv6_fixbits + (-10000)*main_conv6_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv6_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div = fdiv double %conv, %conv6, !taffo.info !28, !taffo.initweight !30
main_conv_CAST_div_fixbits = solver.IntVar(0, 26, 'main_conv_CAST_div_fixbits')
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
castCostObj +=  + (6.62652)*C3_main_conv_CAST_div
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div_fixp + (-1)*C4_main_conv_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv_CAST_div
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_div_double + (-1)*C5_main_conv_CAST_div<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv_CAST_div
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div_fixp + (-1)*C6_main_conv_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv_CAST_div
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div_double + (-1)*C7_main_conv_CAST_div<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv_CAST_div
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div_float + (-1)*C8_main_conv_CAST_div<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv_CAST_div



#Constraint for cast for   %div = fdiv double %conv, %conv6, !taffo.info !28, !taffo.initweight !30
main_conv6_CAST_div_fixbits = solver.IntVar(0, 27, 'main_conv6_CAST_div_fixbits')
main_conv6_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv6_CAST_div_fixp')
main_conv6_CAST_div_float = solver.IntVar(0, 1, 'main_conv6_CAST_div_float')
main_conv6_CAST_div_double = solver.IntVar(0, 1, 'main_conv6_CAST_div_double')
solver.Add( + (1)*main_conv6_CAST_div_fixp + (1)*main_conv6_CAST_div_float + (1)*main_conv6_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv6_CAST_div_fixbits + (-10000)*main_conv6_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv6_CAST_div = solver.IntVar(0, 1, 'C1_main_conv6_CAST_div')
C2_main_conv6_CAST_div = solver.IntVar(0, 1, 'C2_main_conv6_CAST_div')
solver.Add( + (1)*main_conv6_fixbits + (-1)*main_conv6_CAST_div_fixbits + (-10000)*C1_main_conv6_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv6_fixbits + (1)*main_conv6_CAST_div_fixbits + (-10000)*C2_main_conv6_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv6_CAST_div
castCostObj +=  + (1)*C2_main_conv6_CAST_div
C3_main_conv6_CAST_div = solver.IntVar(0, 1, 'C3_main_conv6_CAST_div')
C4_main_conv6_CAST_div = solver.IntVar(0, 1, 'C4_main_conv6_CAST_div')
C5_main_conv6_CAST_div = solver.IntVar(0, 1, 'C5_main_conv6_CAST_div')
C6_main_conv6_CAST_div = solver.IntVar(0, 1, 'C6_main_conv6_CAST_div')
C7_main_conv6_CAST_div = solver.IntVar(0, 1, 'C7_main_conv6_CAST_div')
C8_main_conv6_CAST_div = solver.IntVar(0, 1, 'C8_main_conv6_CAST_div')
solver.Add( + (1)*main_conv6_fixp + (1)*main_conv6_CAST_div_float + (-1)*C3_main_conv6_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv6_CAST_div
solver.Add( + (1)*main_conv6_float + (1)*main_conv6_CAST_div_fixp + (-1)*C4_main_conv6_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv6_CAST_div
solver.Add( + (1)*main_conv6_fixp + (1)*main_conv6_CAST_div_double + (-1)*C5_main_conv6_CAST_div<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv6_CAST_div
solver.Add( + (1)*main_conv6_double + (1)*main_conv6_CAST_div_fixp + (-1)*C6_main_conv6_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv6_CAST_div
solver.Add( + (1)*main_conv6_float + (1)*main_conv6_CAST_div_double + (-1)*C7_main_conv6_CAST_div<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv6_CAST_div
solver.Add( + (1)*main_conv6_double + (1)*main_conv6_CAST_div_float + (-1)*C8_main_conv6_CAST_div<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv6_CAST_div



#Stuff for   %div = fdiv double %conv, %conv6, !taffo.info !28, !taffo.initweight !30
main_div_fixbits = solver.IntVar(0, 30, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_conv6_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_conv6_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_conv6_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj =  + (5.29598)*main_div_fixp
mathCostObj +=  + (5.60026)*main_div_float
mathCostObj +=  + (18.3266)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*main_conv6_enob + (-10000)*main_main_div_enob_1<=1032)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_conv_enob + (-10000)*main_main_div_enob_2<=4)    #Enob: propagation in division 2



#Stuff for double 1.000000e+02
ConstantValue__fixbits = solver.IntVar(0, 25, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+02
ConstantValue__0_fixbits = solver.IntVar(0, 25, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul7 = fmul double %div, 1.000000e+02, !taffo.info !31, !taffo.initweight !33, !taffo.constinfo !34
main_div_CAST_mul7_fixbits = solver.IntVar(0, 30, 'main_div_CAST_mul7_fixbits')
main_div_CAST_mul7_fixp = solver.IntVar(0, 1, 'main_div_CAST_mul7_fixp')
main_div_CAST_mul7_float = solver.IntVar(0, 1, 'main_div_CAST_mul7_float')
main_div_CAST_mul7_double = solver.IntVar(0, 1, 'main_div_CAST_mul7_double')
solver.Add( + (1)*main_div_CAST_mul7_fixp + (1)*main_div_CAST_mul7_float + (1)*main_div_CAST_mul7_double==1)    #exactly 1 type
solver.Add( + (1)*main_div_CAST_mul7_fixbits + (-10000)*main_div_CAST_mul7_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C1_main_div_CAST_mul7')
C2_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C2_main_div_CAST_mul7')
solver.Add( + (1)*main_div_fixbits + (-1)*main_div_CAST_mul7_fixbits + (-10000)*C1_main_div_CAST_mul7<=0)    #Shift cost 1
solver.Add( + (-1)*main_div_fixbits + (1)*main_div_CAST_mul7_fixbits + (-10000)*C2_main_div_CAST_mul7<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div_CAST_mul7
castCostObj +=  + (1)*C2_main_div_CAST_mul7
C3_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C3_main_div_CAST_mul7')
C4_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C4_main_div_CAST_mul7')
C5_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C5_main_div_CAST_mul7')
C6_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C6_main_div_CAST_mul7')
C7_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C7_main_div_CAST_mul7')
C8_main_div_CAST_mul7 = solver.IntVar(0, 1, 'C8_main_div_CAST_mul7')
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_mul7_float + (-1)*C3_main_div_CAST_mul7<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div_CAST_mul7
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_mul7_fixp + (-1)*C4_main_div_CAST_mul7<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div_CAST_mul7
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_mul7_double + (-1)*C5_main_div_CAST_mul7<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div_CAST_mul7
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_mul7_fixp + (-1)*C6_main_div_CAST_mul7<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div_CAST_mul7
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_mul7_double + (-1)*C7_main_div_CAST_mul7<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div_CAST_mul7
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_mul7_float + (-1)*C8_main_div_CAST_mul7<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div_CAST_mul7



#Stuff for double 1.000000e+02
ConstantValue__1_fixbits = solver.IntVar(0, 25, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul7 = fmul double %div, 1.000000e+02, !taffo.info !31, !taffo.initweight !33, !taffo.constinfo !34
ConstantValue__1_CAST_mul7_fixbits = solver.IntVar(0, 25, 'ConstantValue__1_CAST_mul7_fixbits')
ConstantValue__1_CAST_mul7_fixp = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul7_fixp')
ConstantValue__1_CAST_mul7_float = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul7_float')
ConstantValue__1_CAST_mul7_double = solver.IntVar(0, 1, 'ConstantValue__1_CAST_mul7_double')
solver.Add( + (1)*ConstantValue__1_CAST_mul7_fixp + (1)*ConstantValue__1_CAST_mul7_float + (1)*ConstantValue__1_CAST_mul7_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__1_CAST_mul7_fixbits + (-10000)*ConstantValue__1_CAST_mul7_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C1_ConstantValue__1_CAST_mul7')
C2_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C2_ConstantValue__1_CAST_mul7')
solver.Add( + (1)*ConstantValue__1_fixbits + (-1)*ConstantValue__1_CAST_mul7_fixbits + (-10000)*C1_ConstantValue__1_CAST_mul7<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__1_fixbits + (1)*ConstantValue__1_CAST_mul7_fixbits + (-10000)*C2_ConstantValue__1_CAST_mul7<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__1_CAST_mul7
castCostObj +=  + (1)*C2_ConstantValue__1_CAST_mul7
C3_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C3_ConstantValue__1_CAST_mul7')
C4_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C4_ConstantValue__1_CAST_mul7')
C5_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C5_ConstantValue__1_CAST_mul7')
C6_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C6_ConstantValue__1_CAST_mul7')
C7_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C7_ConstantValue__1_CAST_mul7')
C8_ConstantValue__1_CAST_mul7 = solver.IntVar(0, 1, 'C8_ConstantValue__1_CAST_mul7')
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_mul7_float + (-1)*C3_ConstantValue__1_CAST_mul7<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__1_CAST_mul7
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_mul7_fixp + (-1)*C4_ConstantValue__1_CAST_mul7<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__1_CAST_mul7
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_mul7_double + (-1)*C5_ConstantValue__1_CAST_mul7<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__1_CAST_mul7
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_mul7_fixp + (-1)*C6_ConstantValue__1_CAST_mul7<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__1_CAST_mul7
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_mul7_double + (-1)*C7_ConstantValue__1_CAST_mul7<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__1_CAST_mul7
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_mul7_float + (-1)*C8_ConstantValue__1_CAST_mul7<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__1_CAST_mul7



#Stuff for   %mul7 = fmul double %div, 1.000000e+02, !taffo.info !31, !taffo.initweight !33, !taffo.constinfo !34
main_mul7_fixbits = solver.IntVar(0, 24, 'main_mul7_fixbits')
main_mul7_fixp = solver.IntVar(0, 1, 'main_mul7_fixp')
main_mul7_float = solver.IntVar(0, 1, 'main_mul7_float')
main_mul7_double = solver.IntVar(0, 1, 'main_mul7_double')
main_mul7_enob = solver.IntVar(-10000, 10000, 'main_mul7_enob')
solver.Add( + (1)*main_mul7_enob + (-1)*main_mul7_fixbits + (10000)*main_mul7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul7_enob + (10000)*main_mul7_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul7_enob + (10000)*main_mul7_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul7_fixbits + (-10000)*main_mul7_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*main_mul7_enob
solver.Add( + (1)*main_mul7_fixp + (1)*main_mul7_float + (1)*main_mul7_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul7_fixbits + (-10000)*main_mul7_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_div_CAST_mul7_fixp + (-1)*ConstantValue__1_CAST_mul7_fixp==0)    #fix equality
solver.Add( + (1)*main_div_CAST_mul7_float + (-1)*ConstantValue__1_CAST_mul7_float==0)    #float equality
solver.Add( + (1)*main_div_CAST_mul7_double + (-1)*ConstantValue__1_CAST_mul7_double==0)    #double equality
solver.Add( + (1)*main_div_CAST_mul7_fixp + (-1)*main_mul7_fixp==0)    #fix equality
solver.Add( + (1)*main_div_CAST_mul7_float + (-1)*main_mul7_float==0)    #float equality
solver.Add( + (1)*main_div_CAST_mul7_double + (-1)*main_mul7_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul7_fixp
mathCostObj +=  + (2.64722)*main_mul7_float
mathCostObj +=  + (4.02255)*main_mul7_double
main_main_mul7_enob_1 = solver.IntVar(0, 1, 'main_main_mul7_enob_1')
main_main_mul7_enob_2 = solver.IntVar(0, 1, 'main_main_mul7_enob_2')
solver.Add( + (1)*main_main_mul7_enob_1 + (1)*main_main_mul7_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul7_enob + (-1)*ConstantValue__enob + (-10000)*main_main_mul7_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul7_enob + (-1)*main_div_enob + (-10000)*main_main_mul7_enob_2<=-7)    #Enob: propagation in product 2



#Stuff for double 1.000000e+01
ConstantValue__2_fixbits = solver.IntVar(0, 28, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10020)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10049)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+01
ConstantValue__3_fixbits = solver.IntVar(0, 28, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10020)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10049)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add = fadd double %mul7, 1.000000e+01, !taffo.info !37, !taffo.initweight !39, !taffo.constinfo !40
main_mul7_CAST_add_fixbits = solver.IntVar(0, 24, 'main_mul7_CAST_add_fixbits')
main_mul7_CAST_add_fixp = solver.IntVar(0, 1, 'main_mul7_CAST_add_fixp')
main_mul7_CAST_add_float = solver.IntVar(0, 1, 'main_mul7_CAST_add_float')
main_mul7_CAST_add_double = solver.IntVar(0, 1, 'main_mul7_CAST_add_double')
solver.Add( + (1)*main_mul7_CAST_add_fixp + (1)*main_mul7_CAST_add_float + (1)*main_mul7_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul7_CAST_add_fixbits + (-10000)*main_mul7_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul7_CAST_add = solver.IntVar(0, 1, 'C1_main_mul7_CAST_add')
C2_main_mul7_CAST_add = solver.IntVar(0, 1, 'C2_main_mul7_CAST_add')
solver.Add( + (1)*main_mul7_fixbits + (-1)*main_mul7_CAST_add_fixbits + (-10000)*C1_main_mul7_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul7_fixbits + (1)*main_mul7_CAST_add_fixbits + (-10000)*C2_main_mul7_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul7_CAST_add
castCostObj +=  + (1)*C2_main_mul7_CAST_add
C3_main_mul7_CAST_add = solver.IntVar(0, 1, 'C3_main_mul7_CAST_add')
C4_main_mul7_CAST_add = solver.IntVar(0, 1, 'C4_main_mul7_CAST_add')
C5_main_mul7_CAST_add = solver.IntVar(0, 1, 'C5_main_mul7_CAST_add')
C6_main_mul7_CAST_add = solver.IntVar(0, 1, 'C6_main_mul7_CAST_add')
C7_main_mul7_CAST_add = solver.IntVar(0, 1, 'C7_main_mul7_CAST_add')
C8_main_mul7_CAST_add = solver.IntVar(0, 1, 'C8_main_mul7_CAST_add')
solver.Add( + (1)*main_mul7_fixp + (1)*main_mul7_CAST_add_float + (-1)*C3_main_mul7_CAST_add<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul7_CAST_add
solver.Add( + (1)*main_mul7_float + (1)*main_mul7_CAST_add_fixp + (-1)*C4_main_mul7_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul7_CAST_add
solver.Add( + (1)*main_mul7_fixp + (1)*main_mul7_CAST_add_double + (-1)*C5_main_mul7_CAST_add<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul7_CAST_add
solver.Add( + (1)*main_mul7_double + (1)*main_mul7_CAST_add_fixp + (-1)*C6_main_mul7_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul7_CAST_add
solver.Add( + (1)*main_mul7_float + (1)*main_mul7_CAST_add_double + (-1)*C7_main_mul7_CAST_add<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul7_CAST_add
solver.Add( + (1)*main_mul7_double + (1)*main_mul7_CAST_add_float + (-1)*C8_main_mul7_CAST_add<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul7_CAST_add



#Stuff for double 1.000000e+01
ConstantValue__4_fixbits = solver.IntVar(0, 28, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10020)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10049)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add = fadd double %mul7, 1.000000e+01, !taffo.info !37, !taffo.initweight !39, !taffo.constinfo !40
ConstantValue__4_CAST_add_fixbits = solver.IntVar(0, 28, 'ConstantValue__4_CAST_add_fixbits')
ConstantValue__4_CAST_add_fixp = solver.IntVar(0, 1, 'ConstantValue__4_CAST_add_fixp')
ConstantValue__4_CAST_add_float = solver.IntVar(0, 1, 'ConstantValue__4_CAST_add_float')
ConstantValue__4_CAST_add_double = solver.IntVar(0, 1, 'ConstantValue__4_CAST_add_double')
solver.Add( + (1)*ConstantValue__4_CAST_add_fixp + (1)*ConstantValue__4_CAST_add_float + (1)*ConstantValue__4_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__4_CAST_add_fixbits + (-10000)*ConstantValue__4_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C1_ConstantValue__4_CAST_add')
C2_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C2_ConstantValue__4_CAST_add')
solver.Add( + (1)*ConstantValue__4_fixbits + (-1)*ConstantValue__4_CAST_add_fixbits + (-10000)*C1_ConstantValue__4_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__4_fixbits + (1)*ConstantValue__4_CAST_add_fixbits + (-10000)*C2_ConstantValue__4_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__4_CAST_add
castCostObj +=  + (1)*C2_ConstantValue__4_CAST_add
C3_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_add')
C4_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_add')
C5_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_add')
C6_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_add')
C7_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_add')
C8_ConstantValue__4_CAST_add = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_add')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_add_float + (-1)*C3_ConstantValue__4_CAST_add<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__4_CAST_add
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_add_fixp + (-1)*C4_ConstantValue__4_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__4_CAST_add
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_add_double + (-1)*C5_ConstantValue__4_CAST_add<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__4_CAST_add
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_add_fixp + (-1)*C6_ConstantValue__4_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__4_CAST_add
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_add_double + (-1)*C7_ConstantValue__4_CAST_add<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__4_CAST_add
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_add_float + (-1)*C8_ConstantValue__4_CAST_add<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__4_CAST_add



#Stuff for   %add = fadd double %mul7, 1.000000e+01, !taffo.info !37, !taffo.initweight !39, !taffo.constinfo !40
main_add_fixbits = solver.IntVar(0, 24, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
main_add_enob = solver.IntVar(-10000, 10000, 'main_add_enob')
solver.Add( + (1)*main_add_enob + (-1)*main_add_fixbits + (10000)*main_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add_enob + (10000)*main_add_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add_enob + (10000)*main_add_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*main_add_enob
solver.Add( + (1)*main_add_fixp + (1)*main_add_float + (1)*main_add_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul7_CAST_add_fixp + (-1)*ConstantValue__4_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*main_mul7_CAST_add_float + (-1)*ConstantValue__4_CAST_add_float==0)    #float equality
solver.Add( + (1)*main_mul7_CAST_add_double + (-1)*ConstantValue__4_CAST_add_double==0)    #double equality
solver.Add( + (1)*main_mul7_CAST_add_fixbits + (-1)*ConstantValue__4_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul7_CAST_add_fixp + (-1)*main_add_fixp==0)    #fix equality
solver.Add( + (1)*main_mul7_CAST_add_float + (-1)*main_add_float==0)    #float equality
solver.Add( + (1)*main_mul7_CAST_add_double + (-1)*main_add_double==0)    #double equality
solver.Add( + (1)*main_mul7_CAST_add_fixbits + (-1)*main_add_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add_fixp
mathCostObj +=  + (2.33125)*main_add_float
mathCostObj +=  + (2.72422)*main_add_double
solver.Add( + (1)*main_add_enob + (-1)*main_mul7_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*ConstantValue__2_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add, double* %arrayidx9, align 8, !taffo.info !8, !taffo.initweight !21
main_add_CAST_store_fixbits = solver.IntVar(0, 24, 'main_add_CAST_store_fixbits')
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
castCostObj +=  + (6.62652)*C3_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_fixp + (-1)*C4_main_add_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add_CAST_store
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_double + (-1)*C5_main_add_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_fixp + (-1)*C6_main_add_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_double + (-1)*C7_main_add_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_float + (-1)*C8_main_add_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add_CAST_store
solver.Add( + (1)*A_fixp + (-1)*main_add_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*A_float + (-1)*main_add_CAST_store_float==0)    #float equality
solver.Add( + (1)*A_double + (-1)*main_add_CAST_store_double==0)    #double equality
solver.Add( + (1)*A_fixbits + (-1)*main_add_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
A_enob_storeENOB = solver.IntVar(-10000, 10000, 'A_enob_storeENOB')
solver.Add( + (1)*A_enob_storeENOB + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob_storeENOB + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob_storeENOB + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_enob_storeENOB + (-1)*main_add_enob<=0)    #Enob constraint ENOB propagation in load/store



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



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx13, align 8, !taffo.info !8, !taffo.initweight !21, !taffo.constinfo !44
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
castCostObj +=  + (1)*C1_ConstantValue__6_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__6_CAST_store
C3_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__6_CAST_store')
C4_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__6_CAST_store')
C5_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__6_CAST_store')
C6_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__6_CAST_store')
C7_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__6_CAST_store')
C8_ConstantValue__6_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__6_CAST_store')
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_store_float + (-1)*C3_ConstantValue__6_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_store_fixp + (-1)*C4_ConstantValue__6_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_store_double + (-1)*C5_ConstantValue__6_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_store_fixp + (-1)*C6_ConstantValue__6_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_store_double + (-1)*C7_ConstantValue__6_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_store_float + (-1)*C8_ConstantValue__6_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__6_CAST_store
solver.Add( + (1)*Q_fixp + (-1)*ConstantValue__6_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*Q_float + (-1)*ConstantValue__6_CAST_store_float==0)    #float equality
solver.Add( + (1)*Q_double + (-1)*ConstantValue__6_CAST_store_double==0)    #double equality
solver.Add( + (1)*Q_fixbits + (-1)*ConstantValue__6_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 0.000000e+00
ConstantValue__7_fixbits = solver.IntVar(0, 32, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__8_fixbits = solver.IntVar(0, 32, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx28, align 8, !taffo.info !8, !taffo.initweight !21, !taffo.constinfo !44
ConstantValue__8_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__8_CAST_store_fixbits')
ConstantValue__8_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__8_CAST_store_fixp')
ConstantValue__8_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__8_CAST_store_float')
ConstantValue__8_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__8_CAST_store_double')
solver.Add( + (1)*ConstantValue__8_CAST_store_fixp + (1)*ConstantValue__8_CAST_store_float + (1)*ConstantValue__8_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__8_CAST_store_fixbits + (-10000)*ConstantValue__8_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__8_CAST_store')
C2_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__8_CAST_store')
solver.Add( + (1)*ConstantValue__8_fixbits + (-1)*ConstantValue__8_CAST_store_fixbits + (-10000)*C1_ConstantValue__8_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__8_fixbits + (1)*ConstantValue__8_CAST_store_fixbits + (-10000)*C2_ConstantValue__8_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__8_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__8_CAST_store
C3_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__8_CAST_store')
C4_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__8_CAST_store')
C5_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__8_CAST_store')
C6_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__8_CAST_store')
C7_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__8_CAST_store')
C8_ConstantValue__8_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__8_CAST_store')
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_store_float + (-1)*C3_ConstantValue__8_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_store_fixp + (-1)*C4_ConstantValue__8_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_store_double + (-1)*C5_ConstantValue__8_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_store_fixp + (-1)*C6_ConstantValue__8_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_store_double + (-1)*C7_ConstantValue__8_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_store_float + (-1)*C8_ConstantValue__8_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__8_CAST_store
solver.Add( + (1)*R_fixp + (-1)*ConstantValue__8_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*R_float + (-1)*ConstantValue__8_CAST_store_float==0)    #float equality
solver.Add( + (1)*R_double + (-1)*ConstantValue__8_CAST_store_double==0)    #double equality
solver.Add( + (1)*R_fixbits + (-1)*ConstantValue__8_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for   %nrm.0 = phi double [ 0.000000e+00, %for.body39 ], [ %add53, %for.inc54 ], !taffo.info !49
main_nrm_0_fixbits = solver.IntVar(0, 21, 'main_nrm_0_fixbits')
main_nrm_0_fixp = solver.IntVar(0, 1, 'main_nrm_0_fixp')
main_nrm_0_float = solver.IntVar(0, 1, 'main_nrm_0_float')
main_nrm_0_double = solver.IntVar(0, 1, 'main_nrm_0_double')
main_nrm_0_enob = solver.IntVar(-10000, 10000, 'main_nrm_0_enob')
solver.Add( + (1)*main_nrm_0_enob + (-1)*main_nrm_0_fixbits + (10000)*main_nrm_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_nrm_0_enob + (10000)*main_nrm_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_nrm_0_enob + (10000)*main_nrm_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_nrm_0_fixbits + (-10000)*main_nrm_0_fixp>=-9980)    #Limit the lower number of frac bits21
enobCostObj +=  + (-1)*main_nrm_0_enob
solver.Add( + (1)*main_nrm_0_fixp + (1)*main_nrm_0_float + (1)*main_nrm_0_double==1)    #Exactly one selected type
solver.Add( + (1)*main_nrm_0_fixbits + (-10000)*main_nrm_0_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__9_fixbits = solver.IntVar(0, 32, 'ConstantValue__9_fixbits')
ConstantValue__9_fixp = solver.IntVar(0, 1, 'ConstantValue__9_fixp')
ConstantValue__9_float = solver.IntVar(0, 1, 'ConstantValue__9_float')
ConstantValue__9_double = solver.IntVar(0, 1, 'ConstantValue__9_double')
ConstantValue__9_enob = solver.IntVar(-10000, 10000, 'ConstantValue__9_enob')
solver.Add( + (1)*ConstantValue__9_enob + (-1)*ConstantValue__9_fixbits + (10000)*ConstantValue__9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_float + (1)*ConstantValue__9_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp<=0)    #If not fix, frac part to zero
main_main_nrm_0_enob_1 = solver.IntVar(0, 1, 'main_main_nrm_0_enob_1')
solver.Add( + (1)*main_main_nrm_0_enob_1==1)    #Enob: one selected constraint



#Stuff for double 0.000000e+00
ConstantValue__10_fixbits = solver.IntVar(0, 32, 'ConstantValue__10_fixbits')
ConstantValue__10_fixp = solver.IntVar(0, 1, 'ConstantValue__10_fixp')
ConstantValue__10_float = solver.IntVar(0, 1, 'ConstantValue__10_float')
ConstantValue__10_double = solver.IntVar(0, 1, 'ConstantValue__10_double')
ConstantValue__10_enob = solver.IntVar(-10000, 10000, 'ConstantValue__10_enob')
solver.Add( + (1)*ConstantValue__10_enob + (-1)*ConstantValue__10_fixbits + (10000)*ConstantValue__10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_float + (1)*ConstantValue__10_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp')
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_3 = solver.IntVar(0, 1, 'main_main_tmp_enob_3')
main_main_tmp_enob_4 = solver.IntVar(0, 1, 'main_main_tmp_enob_4')
main_main_tmp_enob_5 = solver.IntVar(0, 1, 'main_main_tmp_enob_5')
main_main_tmp_enob_6 = solver.IntVar(0, 1, 'main_main_tmp_enob_6')
main_main_tmp_enob_7 = solver.IntVar(0, 1, 'main_main_tmp_enob_7')
main_main_tmp_enob_8 = solver.IntVar(0, 1, 'main_main_tmp_enob_8')
solver.Add( + (1)*main_main_tmp_enob_3 + (1)*main_main_tmp_enob_4 + (1)*main_main_tmp_enob_5 + (1)*main_main_tmp_enob_6 + (1)*main_main_tmp_enob_7 + (1)*main_main_tmp_enob_8==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp1')
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_3 = solver.IntVar(0, 1, 'main_main_tmp1_enob_3')
main_main_tmp1_enob_4 = solver.IntVar(0, 1, 'main_main_tmp1_enob_4')
main_main_tmp1_enob_5 = solver.IntVar(0, 1, 'main_main_tmp1_enob_5')
main_main_tmp1_enob_6 = solver.IntVar(0, 1, 'main_main_tmp1_enob_6')
main_main_tmp1_enob_7 = solver.IntVar(0, 1, 'main_main_tmp1_enob_7')
main_main_tmp1_enob_8 = solver.IntVar(0, 1, 'main_main_tmp1_enob_8')
solver.Add( + (1)*main_main_tmp1_enob_3 + (1)*main_main_tmp1_enob_4 + (1)*main_main_tmp1_enob_5 + (1)*main_main_tmp1_enob_6 + (1)*main_main_tmp1_enob_7 + (1)*main_main_tmp1_enob_8==1)    #Enob: one selected constraint



#Constraint for cast for   %mul52 = fmul double %tmp, %tmp1, !taffo.info !52, !taffo.initweight !25
A_CAST_mul52_fixbits = solver.IntVar(0, 21, 'A_CAST_mul52_fixbits')
A_CAST_mul52_fixp = solver.IntVar(0, 1, 'A_CAST_mul52_fixp')
A_CAST_mul52_float = solver.IntVar(0, 1, 'A_CAST_mul52_float')
A_CAST_mul52_double = solver.IntVar(0, 1, 'A_CAST_mul52_double')
solver.Add( + (1)*A_CAST_mul52_fixp + (1)*A_CAST_mul52_float + (1)*A_CAST_mul52_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_mul52_fixbits + (-10000)*A_CAST_mul52_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_mul52 = solver.IntVar(0, 1, 'C1_A_CAST_mul52')
C2_A_CAST_mul52 = solver.IntVar(0, 1, 'C2_A_CAST_mul52')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_mul52_fixbits + (-10000)*C1_A_CAST_mul52<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_mul52_fixbits + (-10000)*C2_A_CAST_mul52<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_mul52
castCostObj +=  + (1)*C2_A_CAST_mul52
C3_A_CAST_mul52 = solver.IntVar(0, 1, 'C3_A_CAST_mul52')
C4_A_CAST_mul52 = solver.IntVar(0, 1, 'C4_A_CAST_mul52')
C5_A_CAST_mul52 = solver.IntVar(0, 1, 'C5_A_CAST_mul52')
C6_A_CAST_mul52 = solver.IntVar(0, 1, 'C6_A_CAST_mul52')
C7_A_CAST_mul52 = solver.IntVar(0, 1, 'C7_A_CAST_mul52')
C8_A_CAST_mul52 = solver.IntVar(0, 1, 'C8_A_CAST_mul52')
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul52_float + (-1)*C3_A_CAST_mul52<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_mul52
solver.Add( + (1)*A_float + (1)*A_CAST_mul52_fixp + (-1)*C4_A_CAST_mul52<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_mul52
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul52_double + (-1)*C5_A_CAST_mul52<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_mul52
solver.Add( + (1)*A_double + (1)*A_CAST_mul52_fixp + (-1)*C6_A_CAST_mul52<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_mul52
solver.Add( + (1)*A_float + (1)*A_CAST_mul52_double + (-1)*C7_A_CAST_mul52<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_mul52
solver.Add( + (1)*A_double + (1)*A_CAST_mul52_float + (-1)*C8_A_CAST_mul52<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_mul52



#Constraint for cast for   %mul52 = fmul double %tmp, %tmp1, !taffo.info !52, !taffo.initweight !25
A_CAST_mul52_0_fixbits = solver.IntVar(0, 21, 'A_CAST_mul52_0_fixbits')
A_CAST_mul52_0_fixp = solver.IntVar(0, 1, 'A_CAST_mul52_0_fixp')
A_CAST_mul52_0_float = solver.IntVar(0, 1, 'A_CAST_mul52_0_float')
A_CAST_mul52_0_double = solver.IntVar(0, 1, 'A_CAST_mul52_0_double')
solver.Add( + (1)*A_CAST_mul52_0_fixp + (1)*A_CAST_mul52_0_float + (1)*A_CAST_mul52_0_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_mul52_0_fixbits + (-10000)*A_CAST_mul52_0_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C1_A_CAST_mul52_0')
C2_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C2_A_CAST_mul52_0')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_mul52_0_fixbits + (-10000)*C1_A_CAST_mul52_0<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_mul52_0_fixbits + (-10000)*C2_A_CAST_mul52_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_mul52_0
castCostObj +=  + (1)*C2_A_CAST_mul52_0
C3_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C3_A_CAST_mul52_0')
C4_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C4_A_CAST_mul52_0')
C5_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C5_A_CAST_mul52_0')
C6_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C6_A_CAST_mul52_0')
C7_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C7_A_CAST_mul52_0')
C8_A_CAST_mul52_0 = solver.IntVar(0, 1, 'C8_A_CAST_mul52_0')
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul52_0_float + (-1)*C3_A_CAST_mul52_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_mul52_0
solver.Add( + (1)*A_float + (1)*A_CAST_mul52_0_fixp + (-1)*C4_A_CAST_mul52_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_mul52_0
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul52_0_double + (-1)*C5_A_CAST_mul52_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_mul52_0
solver.Add( + (1)*A_double + (1)*A_CAST_mul52_0_fixp + (-1)*C6_A_CAST_mul52_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_mul52_0
solver.Add( + (1)*A_float + (1)*A_CAST_mul52_0_double + (-1)*C7_A_CAST_mul52_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_mul52_0
solver.Add( + (1)*A_double + (1)*A_CAST_mul52_0_float + (-1)*C8_A_CAST_mul52_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_mul52_0



#Stuff for   %mul52 = fmul double %tmp, %tmp1, !taffo.info !52, !taffo.initweight !25
main_mul52_fixbits = solver.IntVar(0, 11, 'main_mul52_fixbits')
main_mul52_fixp = solver.IntVar(0, 1, 'main_mul52_fixp')
main_mul52_float = solver.IntVar(0, 1, 'main_mul52_float')
main_mul52_double = solver.IntVar(0, 1, 'main_mul52_double')
main_mul52_enob = solver.IntVar(-10000, 10000, 'main_mul52_enob')
solver.Add( + (1)*main_mul52_enob + (-1)*main_mul52_fixbits + (10000)*main_mul52_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul52_enob + (10000)*main_mul52_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul52_enob + (10000)*main_mul52_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul52_fixbits + (-10000)*main_mul52_fixp>=-9990)    #Limit the lower number of frac bits11
enobCostObj +=  + (-1)*main_mul52_enob
solver.Add( + (1)*main_mul52_fixp + (1)*main_mul52_float + (1)*main_mul52_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul52_fixbits + (-10000)*main_mul52_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*A_CAST_mul52_fixp + (-1)*A_CAST_mul52_0_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_mul52_float + (-1)*A_CAST_mul52_0_float==0)    #float equality
solver.Add( + (1)*A_CAST_mul52_double + (-1)*A_CAST_mul52_0_double==0)    #double equality
solver.Add( + (1)*A_CAST_mul52_fixp + (-1)*main_mul52_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_mul52_float + (-1)*main_mul52_float==0)    #float equality
solver.Add( + (1)*A_CAST_mul52_double + (-1)*main_mul52_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul52_fixp
mathCostObj +=  + (2.64722)*main_mul52_float
mathCostObj +=  + (4.02255)*main_mul52_double
main_main_mul52_enob_1 = solver.IntVar(0, 1, 'main_main_mul52_enob_1')
main_main_mul52_enob_2 = solver.IntVar(0, 1, 'main_main_mul52_enob_2')
solver.Add( + (1)*main_main_mul52_enob_1 + (1)*main_main_mul52_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul52_enob + (-1)*A_enob_memphi_main_tmp1 + (-10000)*main_main_mul52_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul52_enob + (-1)*A_enob_memphi_main_tmp + (-10000)*main_main_mul52_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add53 = fadd double %nrm.0, %mul52, !taffo.info !52, !taffo.initweight !20
main_nrm_0_CAST_add53_fixbits = solver.IntVar(0, 21, 'main_nrm_0_CAST_add53_fixbits')
main_nrm_0_CAST_add53_fixp = solver.IntVar(0, 1, 'main_nrm_0_CAST_add53_fixp')
main_nrm_0_CAST_add53_float = solver.IntVar(0, 1, 'main_nrm_0_CAST_add53_float')
main_nrm_0_CAST_add53_double = solver.IntVar(0, 1, 'main_nrm_0_CAST_add53_double')
solver.Add( + (1)*main_nrm_0_CAST_add53_fixp + (1)*main_nrm_0_CAST_add53_float + (1)*main_nrm_0_CAST_add53_double==1)    #exactly 1 type
solver.Add( + (1)*main_nrm_0_CAST_add53_fixbits + (-10000)*main_nrm_0_CAST_add53_fixp<=0)    #If no fix, fix frac part = 0
C1_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C1_main_nrm_0_CAST_add53')
C2_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C2_main_nrm_0_CAST_add53')
solver.Add( + (1)*main_nrm_0_fixbits + (-1)*main_nrm_0_CAST_add53_fixbits + (-10000)*C1_main_nrm_0_CAST_add53<=0)    #Shift cost 1
solver.Add( + (-1)*main_nrm_0_fixbits + (1)*main_nrm_0_CAST_add53_fixbits + (-10000)*C2_main_nrm_0_CAST_add53<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_nrm_0_CAST_add53
castCostObj +=  + (1)*C2_main_nrm_0_CAST_add53
C3_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C3_main_nrm_0_CAST_add53')
C4_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C4_main_nrm_0_CAST_add53')
C5_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C5_main_nrm_0_CAST_add53')
C6_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C6_main_nrm_0_CAST_add53')
C7_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C7_main_nrm_0_CAST_add53')
C8_main_nrm_0_CAST_add53 = solver.IntVar(0, 1, 'C8_main_nrm_0_CAST_add53')
solver.Add( + (1)*main_nrm_0_fixp + (1)*main_nrm_0_CAST_add53_float + (-1)*C3_main_nrm_0_CAST_add53<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_nrm_0_CAST_add53
solver.Add( + (1)*main_nrm_0_float + (1)*main_nrm_0_CAST_add53_fixp + (-1)*C4_main_nrm_0_CAST_add53<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_nrm_0_CAST_add53
solver.Add( + (1)*main_nrm_0_fixp + (1)*main_nrm_0_CAST_add53_double + (-1)*C5_main_nrm_0_CAST_add53<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_nrm_0_CAST_add53
solver.Add( + (1)*main_nrm_0_double + (1)*main_nrm_0_CAST_add53_fixp + (-1)*C6_main_nrm_0_CAST_add53<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_nrm_0_CAST_add53
solver.Add( + (1)*main_nrm_0_float + (1)*main_nrm_0_CAST_add53_double + (-1)*C7_main_nrm_0_CAST_add53<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_nrm_0_CAST_add53
solver.Add( + (1)*main_nrm_0_double + (1)*main_nrm_0_CAST_add53_float + (-1)*C8_main_nrm_0_CAST_add53<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_nrm_0_CAST_add53



#Constraint for cast for   %add53 = fadd double %nrm.0, %mul52, !taffo.info !52, !taffo.initweight !20
main_mul52_CAST_add53_fixbits = solver.IntVar(0, 11, 'main_mul52_CAST_add53_fixbits')
main_mul52_CAST_add53_fixp = solver.IntVar(0, 1, 'main_mul52_CAST_add53_fixp')
main_mul52_CAST_add53_float = solver.IntVar(0, 1, 'main_mul52_CAST_add53_float')
main_mul52_CAST_add53_double = solver.IntVar(0, 1, 'main_mul52_CAST_add53_double')
solver.Add( + (1)*main_mul52_CAST_add53_fixp + (1)*main_mul52_CAST_add53_float + (1)*main_mul52_CAST_add53_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul52_CAST_add53_fixbits + (-10000)*main_mul52_CAST_add53_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C1_main_mul52_CAST_add53')
C2_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C2_main_mul52_CAST_add53')
solver.Add( + (1)*main_mul52_fixbits + (-1)*main_mul52_CAST_add53_fixbits + (-10000)*C1_main_mul52_CAST_add53<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul52_fixbits + (1)*main_mul52_CAST_add53_fixbits + (-10000)*C2_main_mul52_CAST_add53<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul52_CAST_add53
castCostObj +=  + (1)*C2_main_mul52_CAST_add53
C3_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C3_main_mul52_CAST_add53')
C4_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C4_main_mul52_CAST_add53')
C5_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C5_main_mul52_CAST_add53')
C6_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C6_main_mul52_CAST_add53')
C7_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C7_main_mul52_CAST_add53')
C8_main_mul52_CAST_add53 = solver.IntVar(0, 1, 'C8_main_mul52_CAST_add53')
solver.Add( + (1)*main_mul52_fixp + (1)*main_mul52_CAST_add53_float + (-1)*C3_main_mul52_CAST_add53<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul52_CAST_add53
solver.Add( + (1)*main_mul52_float + (1)*main_mul52_CAST_add53_fixp + (-1)*C4_main_mul52_CAST_add53<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul52_CAST_add53
solver.Add( + (1)*main_mul52_fixp + (1)*main_mul52_CAST_add53_double + (-1)*C5_main_mul52_CAST_add53<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul52_CAST_add53
solver.Add( + (1)*main_mul52_double + (1)*main_mul52_CAST_add53_fixp + (-1)*C6_main_mul52_CAST_add53<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul52_CAST_add53
solver.Add( + (1)*main_mul52_float + (1)*main_mul52_CAST_add53_double + (-1)*C7_main_mul52_CAST_add53<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul52_CAST_add53
solver.Add( + (1)*main_mul52_double + (1)*main_mul52_CAST_add53_float + (-1)*C8_main_mul52_CAST_add53<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul52_CAST_add53



#Stuff for   %add53 = fadd double %nrm.0, %mul52, !taffo.info !52, !taffo.initweight !20
main_add53_fixbits = solver.IntVar(0, 11, 'main_add53_fixbits')
main_add53_fixp = solver.IntVar(0, 1, 'main_add53_fixp')
main_add53_float = solver.IntVar(0, 1, 'main_add53_float')
main_add53_double = solver.IntVar(0, 1, 'main_add53_double')
main_add53_enob = solver.IntVar(-10000, 10000, 'main_add53_enob')
solver.Add( + (1)*main_add53_enob + (-1)*main_add53_fixbits + (10000)*main_add53_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add53_enob + (10000)*main_add53_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add53_enob + (10000)*main_add53_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add53_fixbits + (-10000)*main_add53_fixp>=-9990)    #Limit the lower number of frac bits11
enobCostObj +=  + (-1)*main_add53_enob
solver.Add( + (1)*main_add53_fixp + (1)*main_add53_float + (1)*main_add53_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add53_fixbits + (-10000)*main_add53_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %nrm.0 = phi double [ 0.000000e+00, %for.body39 ], [ %add53, %for.inc54 ], !taffo.info !49
main_add53_CAST_nrm_0_fixbits = solver.IntVar(0, 11, 'main_add53_CAST_nrm_0_fixbits')
main_add53_CAST_nrm_0_fixp = solver.IntVar(0, 1, 'main_add53_CAST_nrm_0_fixp')
main_add53_CAST_nrm_0_float = solver.IntVar(0, 1, 'main_add53_CAST_nrm_0_float')
main_add53_CAST_nrm_0_double = solver.IntVar(0, 1, 'main_add53_CAST_nrm_0_double')
solver.Add( + (1)*main_add53_CAST_nrm_0_fixp + (1)*main_add53_CAST_nrm_0_float + (1)*main_add53_CAST_nrm_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_add53_CAST_nrm_0_fixbits + (-10000)*main_add53_CAST_nrm_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C1_main_add53_CAST_nrm_0')
C2_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C2_main_add53_CAST_nrm_0')
solver.Add( + (1)*main_add53_fixbits + (-1)*main_add53_CAST_nrm_0_fixbits + (-10000)*C1_main_add53_CAST_nrm_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_add53_fixbits + (1)*main_add53_CAST_nrm_0_fixbits + (-10000)*C2_main_add53_CAST_nrm_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add53_CAST_nrm_0
castCostObj +=  + (1)*C2_main_add53_CAST_nrm_0
C3_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C3_main_add53_CAST_nrm_0')
C4_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C4_main_add53_CAST_nrm_0')
C5_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C5_main_add53_CAST_nrm_0')
C6_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C6_main_add53_CAST_nrm_0')
C7_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C7_main_add53_CAST_nrm_0')
C8_main_add53_CAST_nrm_0 = solver.IntVar(0, 1, 'C8_main_add53_CAST_nrm_0')
solver.Add( + (1)*main_add53_fixp + (1)*main_add53_CAST_nrm_0_float + (-1)*C3_main_add53_CAST_nrm_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add53_CAST_nrm_0
solver.Add( + (1)*main_add53_float + (1)*main_add53_CAST_nrm_0_fixp + (-1)*C4_main_add53_CAST_nrm_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add53_CAST_nrm_0
solver.Add( + (1)*main_add53_fixp + (1)*main_add53_CAST_nrm_0_double + (-1)*C5_main_add53_CAST_nrm_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add53_CAST_nrm_0
solver.Add( + (1)*main_add53_double + (1)*main_add53_CAST_nrm_0_fixp + (-1)*C6_main_add53_CAST_nrm_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add53_CAST_nrm_0
solver.Add( + (1)*main_add53_float + (1)*main_add53_CAST_nrm_0_double + (-1)*C7_main_add53_CAST_nrm_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add53_CAST_nrm_0
solver.Add( + (1)*main_add53_double + (1)*main_add53_CAST_nrm_0_float + (-1)*C8_main_add53_CAST_nrm_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add53_CAST_nrm_0
solver.Add( + (1)*main_nrm_0_fixp + (-1)*main_add53_CAST_nrm_0_fixp==0)    #fix equality
solver.Add( + (1)*main_nrm_0_float + (-1)*main_add53_CAST_nrm_0_float==0)    #float equality
solver.Add( + (1)*main_nrm_0_double + (-1)*main_add53_CAST_nrm_0_double==0)    #double equality
solver.Add( + (1)*main_nrm_0_fixbits + (-1)*main_add53_CAST_nrm_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_nrm_0_enob + (-1)*main_add53_enob + (10000)*main_main_nrm_0_enob_1<=10000)    #Enob: forcing phi enob
solver.Add( + (1)*main_nrm_0_CAST_add53_fixp + (-1)*main_mul52_CAST_add53_fixp==0)    #fix equality
solver.Add( + (1)*main_nrm_0_CAST_add53_float + (-1)*main_mul52_CAST_add53_float==0)    #float equality
solver.Add( + (1)*main_nrm_0_CAST_add53_double + (-1)*main_mul52_CAST_add53_double==0)    #double equality
solver.Add( + (1)*main_nrm_0_CAST_add53_fixbits + (-1)*main_mul52_CAST_add53_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_nrm_0_CAST_add53_fixp + (-1)*main_add53_fixp==0)    #fix equality
solver.Add( + (1)*main_nrm_0_CAST_add53_float + (-1)*main_add53_float==0)    #float equality
solver.Add( + (1)*main_nrm_0_CAST_add53_double + (-1)*main_add53_double==0)    #double equality
solver.Add( + (1)*main_nrm_0_CAST_add53_fixbits + (-1)*main_add53_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add53_fixp
mathCostObj +=  + (2.33125)*main_add53_float
mathCostObj +=  + (2.72422)*main_add53_double
solver.Add( + (1)*main_add53_enob + (-1)*main_nrm_0_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add53_enob + (-1)*main_mul52_enob<=0)    #Enob propagation in sum second addend



#Stuff for   %call = call double @sqrt(double %nrm.0) #3, !taffo.info !8, !taffo.initweight !20, !taffo.constinfo !24
main_call_fixbits = solver.IntVar(0, 21, 'main_call_fixbits')
main_call_fixp = solver.IntVar(0, 1, 'main_call_fixp')
main_call_float = solver.IntVar(0, 1, 'main_call_float')
main_call_double = solver.IntVar(0, 1, 'main_call_double')
main_call_enob = solver.IntVar(-10000, 10000, 'main_call_enob')
solver.Add( + (1)*main_call_enob + (-1)*main_call_fixbits + (10000)*main_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call_enob + (10000)*main_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_call_enob + (10000)*main_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp>=-9980)    #Limit the lower number of frac bits21
enobCostObj +=  + (-1)*main_call_enob
solver.Add( + (1)*main_call_fixp + (1)*main_call_float + (1)*main_call_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call_double==1)    #Type constraint for return value



#Constraint for cast for   %call = call double @sqrt(double %nrm.0) #3, !taffo.info !8, !taffo.initweight !20, !taffo.constinfo !24
main_nrm_0_CAST_call_fixbits = solver.IntVar(0, 21, 'main_nrm_0_CAST_call_fixbits')
main_nrm_0_CAST_call_fixp = solver.IntVar(0, 1, 'main_nrm_0_CAST_call_fixp')
main_nrm_0_CAST_call_float = solver.IntVar(0, 1, 'main_nrm_0_CAST_call_float')
main_nrm_0_CAST_call_double = solver.IntVar(0, 1, 'main_nrm_0_CAST_call_double')
solver.Add( + (1)*main_nrm_0_CAST_call_fixp + (1)*main_nrm_0_CAST_call_float + (1)*main_nrm_0_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*main_nrm_0_CAST_call_fixbits + (-10000)*main_nrm_0_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C1_main_nrm_0_CAST_call')
C2_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C2_main_nrm_0_CAST_call')
solver.Add( + (1)*main_nrm_0_fixbits + (-1)*main_nrm_0_CAST_call_fixbits + (-10000)*C1_main_nrm_0_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*main_nrm_0_fixbits + (1)*main_nrm_0_CAST_call_fixbits + (-10000)*C2_main_nrm_0_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_nrm_0_CAST_call
castCostObj +=  + (1)*C2_main_nrm_0_CAST_call
C3_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C3_main_nrm_0_CAST_call')
C4_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C4_main_nrm_0_CAST_call')
C5_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C5_main_nrm_0_CAST_call')
C6_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C6_main_nrm_0_CAST_call')
C7_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C7_main_nrm_0_CAST_call')
C8_main_nrm_0_CAST_call = solver.IntVar(0, 1, 'C8_main_nrm_0_CAST_call')
solver.Add( + (1)*main_nrm_0_fixp + (1)*main_nrm_0_CAST_call_float + (-1)*C3_main_nrm_0_CAST_call<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_nrm_0_CAST_call
solver.Add( + (1)*main_nrm_0_float + (1)*main_nrm_0_CAST_call_fixp + (-1)*C4_main_nrm_0_CAST_call<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_nrm_0_CAST_call
solver.Add( + (1)*main_nrm_0_fixp + (1)*main_nrm_0_CAST_call_double + (-1)*C5_main_nrm_0_CAST_call<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_nrm_0_CAST_call
solver.Add( + (1)*main_nrm_0_double + (1)*main_nrm_0_CAST_call_fixp + (-1)*C6_main_nrm_0_CAST_call<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_nrm_0_CAST_call
solver.Add( + (1)*main_nrm_0_float + (1)*main_nrm_0_CAST_call_double + (-1)*C7_main_nrm_0_CAST_call<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_nrm_0_CAST_call
solver.Add( + (1)*main_nrm_0_double + (1)*main_nrm_0_CAST_call_float + (-1)*C8_main_nrm_0_CAST_call<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_nrm_0_CAST_call
solver.Add( + (1)*main_nrm_0_CAST_call_double==1)    #Type constraint for argument value



#Constraint for cast for   store double %call, double* %arrayidx60, align 8, !taffo.info !8, !taffo.initweight !21
main_call_CAST_store_fixbits = solver.IntVar(0, 21, 'main_call_CAST_store_fixbits')
main_call_CAST_store_fixp = solver.IntVar(0, 1, 'main_call_CAST_store_fixp')
main_call_CAST_store_float = solver.IntVar(0, 1, 'main_call_CAST_store_float')
main_call_CAST_store_double = solver.IntVar(0, 1, 'main_call_CAST_store_double')
solver.Add( + (1)*main_call_CAST_store_fixp + (1)*main_call_CAST_store_float + (1)*main_call_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_call_CAST_store_fixbits + (-10000)*main_call_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_call_CAST_store = solver.IntVar(0, 1, 'C1_main_call_CAST_store')
C2_main_call_CAST_store = solver.IntVar(0, 1, 'C2_main_call_CAST_store')
solver.Add( + (1)*main_call_fixbits + (-1)*main_call_CAST_store_fixbits + (-10000)*C1_main_call_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_call_fixbits + (1)*main_call_CAST_store_fixbits + (-10000)*C2_main_call_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_call_CAST_store
castCostObj +=  + (1)*C2_main_call_CAST_store
C3_main_call_CAST_store = solver.IntVar(0, 1, 'C3_main_call_CAST_store')
C4_main_call_CAST_store = solver.IntVar(0, 1, 'C4_main_call_CAST_store')
C5_main_call_CAST_store = solver.IntVar(0, 1, 'C5_main_call_CAST_store')
C6_main_call_CAST_store = solver.IntVar(0, 1, 'C6_main_call_CAST_store')
C7_main_call_CAST_store = solver.IntVar(0, 1, 'C7_main_call_CAST_store')
C8_main_call_CAST_store = solver.IntVar(0, 1, 'C8_main_call_CAST_store')
solver.Add( + (1)*main_call_fixp + (1)*main_call_CAST_store_float + (-1)*C3_main_call_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_call_CAST_store
solver.Add( + (1)*main_call_float + (1)*main_call_CAST_store_fixp + (-1)*C4_main_call_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_call_CAST_store
solver.Add( + (1)*main_call_fixp + (1)*main_call_CAST_store_double + (-1)*C5_main_call_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_call_CAST_store
solver.Add( + (1)*main_call_double + (1)*main_call_CAST_store_fixp + (-1)*C6_main_call_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_call_CAST_store
solver.Add( + (1)*main_call_float + (1)*main_call_CAST_store_double + (-1)*C7_main_call_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_call_CAST_store
solver.Add( + (1)*main_call_double + (1)*main_call_CAST_store_float + (-1)*C8_main_call_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_call_CAST_store
solver.Add( + (1)*R_fixp + (-1)*main_call_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*R_float + (-1)*main_call_CAST_store_float==0)    #float equality
solver.Add( + (1)*R_double + (-1)*main_call_CAST_store_double==0)    #double equality
solver.Add( + (1)*R_fixbits + (-1)*main_call_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
R_enob_storeENOB = solver.IntVar(-10000, 10000, 'R_enob_storeENOB')
solver.Add( + (1)*R_enob_storeENOB + (-1)*R_fixbits + (10000)*R_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*R_enob_storeENOB + (10000)*R_float<=10149)    #Enob constraint for float
solver.Add( + (1)*R_enob_storeENOB + (10000)*R_double<=11074)    #Enob constraint for double
solver.Add( + (1)*R_enob_storeENOB + (-1)*main_call_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*R_enob_storeENOB + (10000)*main_main_tmp_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*R_enob_storeENOB + (10000)*main_main_tmp1_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
R_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'R_enob_memphi_main_tmp2')
solver.Add( + (1)*R_enob_memphi_main_tmp2 + (-1)*R_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_0 = solver.IntVar(0, 1, 'main_main_tmp2_enob_0')
solver.Add( + (1)*main_main_tmp2_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*R_enob_memphi_main_tmp2 + (-1)*R_enob_storeENOB + (10000)*main_main_tmp2_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 0.000000e+00
ConstantValue__11_fixbits = solver.IntVar(0, 32, 'ConstantValue__11_fixbits')
ConstantValue__11_fixp = solver.IntVar(0, 1, 'ConstantValue__11_fixp')
ConstantValue__11_float = solver.IntVar(0, 1, 'ConstantValue__11_float')
ConstantValue__11_double = solver.IntVar(0, 1, 'ConstantValue__11_double')
ConstantValue__11_enob = solver.IntVar(-10000, 10000, 'ConstantValue__11_enob')
solver.Add( + (1)*ConstantValue__11_enob + (-1)*ConstantValue__11_fixbits + (10000)*ConstantValue__11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_float + (1)*ConstantValue__11_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cmp69 = fcmp une double %tmp2, 0.000000e+00, !taffo.info !54, !taffo.initweight !25
R_CAST_cmp69_fixbits = solver.IntVar(0, 21, 'R_CAST_cmp69_fixbits')
R_CAST_cmp69_fixp = solver.IntVar(0, 1, 'R_CAST_cmp69_fixp')
R_CAST_cmp69_float = solver.IntVar(0, 1, 'R_CAST_cmp69_float')
R_CAST_cmp69_double = solver.IntVar(0, 1, 'R_CAST_cmp69_double')
solver.Add( + (1)*R_CAST_cmp69_fixp + (1)*R_CAST_cmp69_float + (1)*R_CAST_cmp69_double==1)    #exactly 1 type
solver.Add( + (1)*R_CAST_cmp69_fixbits + (-10000)*R_CAST_cmp69_fixp<=0)    #If no fix, fix frac part = 0
C1_R_CAST_cmp69 = solver.IntVar(0, 1, 'C1_R_CAST_cmp69')
C2_R_CAST_cmp69 = solver.IntVar(0, 1, 'C2_R_CAST_cmp69')
solver.Add( + (1)*R_fixbits + (-1)*R_CAST_cmp69_fixbits + (-10000)*C1_R_CAST_cmp69<=0)    #Shift cost 1
solver.Add( + (-1)*R_fixbits + (1)*R_CAST_cmp69_fixbits + (-10000)*C2_R_CAST_cmp69<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_R_CAST_cmp69
castCostObj +=  + (1)*C2_R_CAST_cmp69
C3_R_CAST_cmp69 = solver.IntVar(0, 1, 'C3_R_CAST_cmp69')
C4_R_CAST_cmp69 = solver.IntVar(0, 1, 'C4_R_CAST_cmp69')
C5_R_CAST_cmp69 = solver.IntVar(0, 1, 'C5_R_CAST_cmp69')
C6_R_CAST_cmp69 = solver.IntVar(0, 1, 'C6_R_CAST_cmp69')
C7_R_CAST_cmp69 = solver.IntVar(0, 1, 'C7_R_CAST_cmp69')
C8_R_CAST_cmp69 = solver.IntVar(0, 1, 'C8_R_CAST_cmp69')
solver.Add( + (1)*R_fixp + (1)*R_CAST_cmp69_float + (-1)*C3_R_CAST_cmp69<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_R_CAST_cmp69
solver.Add( + (1)*R_float + (1)*R_CAST_cmp69_fixp + (-1)*C4_R_CAST_cmp69<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_R_CAST_cmp69
solver.Add( + (1)*R_fixp + (1)*R_CAST_cmp69_double + (-1)*C5_R_CAST_cmp69<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_R_CAST_cmp69
solver.Add( + (1)*R_double + (1)*R_CAST_cmp69_fixp + (-1)*C6_R_CAST_cmp69<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_R_CAST_cmp69
solver.Add( + (1)*R_float + (1)*R_CAST_cmp69_double + (-1)*C7_R_CAST_cmp69<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_R_CAST_cmp69
solver.Add( + (1)*R_double + (1)*R_CAST_cmp69_float + (-1)*C8_R_CAST_cmp69<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_R_CAST_cmp69



#Stuff for double 0.000000e+00
ConstantValue__12_fixbits = solver.IntVar(0, 32, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cmp69 = fcmp une double %tmp2, 0.000000e+00, !taffo.info !54, !taffo.initweight !25
ConstantValue__12_CAST_cmp69_fixbits = solver.IntVar(0, 32, 'ConstantValue__12_CAST_cmp69_fixbits')
ConstantValue__12_CAST_cmp69_fixp = solver.IntVar(0, 1, 'ConstantValue__12_CAST_cmp69_fixp')
ConstantValue__12_CAST_cmp69_float = solver.IntVar(0, 1, 'ConstantValue__12_CAST_cmp69_float')
ConstantValue__12_CAST_cmp69_double = solver.IntVar(0, 1, 'ConstantValue__12_CAST_cmp69_double')
solver.Add( + (1)*ConstantValue__12_CAST_cmp69_fixp + (1)*ConstantValue__12_CAST_cmp69_float + (1)*ConstantValue__12_CAST_cmp69_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__12_CAST_cmp69_fixbits + (-10000)*ConstantValue__12_CAST_cmp69_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C1_ConstantValue__12_CAST_cmp69')
C2_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C2_ConstantValue__12_CAST_cmp69')
solver.Add( + (1)*ConstantValue__12_fixbits + (-1)*ConstantValue__12_CAST_cmp69_fixbits + (-10000)*C1_ConstantValue__12_CAST_cmp69<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__12_fixbits + (1)*ConstantValue__12_CAST_cmp69_fixbits + (-10000)*C2_ConstantValue__12_CAST_cmp69<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__12_CAST_cmp69
castCostObj +=  + (1)*C2_ConstantValue__12_CAST_cmp69
C3_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C3_ConstantValue__12_CAST_cmp69')
C4_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C4_ConstantValue__12_CAST_cmp69')
C5_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C5_ConstantValue__12_CAST_cmp69')
C6_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C6_ConstantValue__12_CAST_cmp69')
C7_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C7_ConstantValue__12_CAST_cmp69')
C8_ConstantValue__12_CAST_cmp69 = solver.IntVar(0, 1, 'C8_ConstantValue__12_CAST_cmp69')
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_cmp69_float + (-1)*C3_ConstantValue__12_CAST_cmp69<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__12_CAST_cmp69
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_cmp69_fixp + (-1)*C4_ConstantValue__12_CAST_cmp69<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__12_CAST_cmp69
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_cmp69_double + (-1)*C5_ConstantValue__12_CAST_cmp69<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__12_CAST_cmp69
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_cmp69_fixp + (-1)*C6_ConstantValue__12_CAST_cmp69<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__12_CAST_cmp69
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_cmp69_double + (-1)*C7_ConstantValue__12_CAST_cmp69<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__12_CAST_cmp69
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_cmp69_float + (-1)*C8_ConstantValue__12_CAST_cmp69<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__12_CAST_cmp69
solver.Add( + (1)*R_CAST_cmp69_fixp + (-1)*ConstantValue__12_CAST_cmp69_fixp==0)    #fix equality
solver.Add( + (1)*R_CAST_cmp69_float + (-1)*ConstantValue__12_CAST_cmp69_float==0)    #float equality
solver.Add( + (1)*R_CAST_cmp69_double + (-1)*ConstantValue__12_CAST_cmp69_double==0)    #double equality
solver.Add( + (1)*R_CAST_cmp69_fixbits + (-1)*ConstantValue__12_CAST_cmp69_fixbits==0)    #same fractional bit

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp3')
solver.Add( + (1)*A_enob_memphi_main_tmp3 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob [LOAD]
R_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'R_enob_memphi_main_tmp4')
solver.Add( + (1)*R_enob_memphi_main_tmp4 + (-1)*R_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_0 = solver.IntVar(0, 1, 'main_main_tmp4_enob_0')
solver.Add( + (1)*main_main_tmp4_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*R_enob_memphi_main_tmp4 + (-1)*R_enob_storeENOB + (10000)*main_main_tmp4_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div79 = fdiv double %tmp3, %tmp4, !taffo.info !28, !taffo.initweight !25
A_CAST_div79_fixbits = solver.IntVar(0, 21, 'A_CAST_div79_fixbits')
A_CAST_div79_fixp = solver.IntVar(0, 1, 'A_CAST_div79_fixp')
A_CAST_div79_float = solver.IntVar(0, 1, 'A_CAST_div79_float')
A_CAST_div79_double = solver.IntVar(0, 1, 'A_CAST_div79_double')
solver.Add( + (1)*A_CAST_div79_fixp + (1)*A_CAST_div79_float + (1)*A_CAST_div79_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_div79_fixbits + (-10000)*A_CAST_div79_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_div79 = solver.IntVar(0, 1, 'C1_A_CAST_div79')
C2_A_CAST_div79 = solver.IntVar(0, 1, 'C2_A_CAST_div79')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_div79_fixbits + (-10000)*C1_A_CAST_div79<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_div79_fixbits + (-10000)*C2_A_CAST_div79<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_div79
castCostObj +=  + (1)*C2_A_CAST_div79
C3_A_CAST_div79 = solver.IntVar(0, 1, 'C3_A_CAST_div79')
C4_A_CAST_div79 = solver.IntVar(0, 1, 'C4_A_CAST_div79')
C5_A_CAST_div79 = solver.IntVar(0, 1, 'C5_A_CAST_div79')
C6_A_CAST_div79 = solver.IntVar(0, 1, 'C6_A_CAST_div79')
C7_A_CAST_div79 = solver.IntVar(0, 1, 'C7_A_CAST_div79')
C8_A_CAST_div79 = solver.IntVar(0, 1, 'C8_A_CAST_div79')
solver.Add( + (1)*A_fixp + (1)*A_CAST_div79_float + (-1)*C3_A_CAST_div79<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_div79
solver.Add( + (1)*A_float + (1)*A_CAST_div79_fixp + (-1)*C4_A_CAST_div79<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_div79
solver.Add( + (1)*A_fixp + (1)*A_CAST_div79_double + (-1)*C5_A_CAST_div79<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_div79
solver.Add( + (1)*A_double + (1)*A_CAST_div79_fixp + (-1)*C6_A_CAST_div79<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_div79
solver.Add( + (1)*A_float + (1)*A_CAST_div79_double + (-1)*C7_A_CAST_div79<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_div79
solver.Add( + (1)*A_double + (1)*A_CAST_div79_float + (-1)*C8_A_CAST_div79<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_div79



#Constraint for cast for   %div79 = fdiv double %tmp3, %tmp4, !taffo.info !28, !taffo.initweight !25
R_CAST_div79_fixbits = solver.IntVar(0, 21, 'R_CAST_div79_fixbits')
R_CAST_div79_fixp = solver.IntVar(0, 1, 'R_CAST_div79_fixp')
R_CAST_div79_float = solver.IntVar(0, 1, 'R_CAST_div79_float')
R_CAST_div79_double = solver.IntVar(0, 1, 'R_CAST_div79_double')
solver.Add( + (1)*R_CAST_div79_fixp + (1)*R_CAST_div79_float + (1)*R_CAST_div79_double==1)    #exactly 1 type
solver.Add( + (1)*R_CAST_div79_fixbits + (-10000)*R_CAST_div79_fixp<=0)    #If no fix, fix frac part = 0
C1_R_CAST_div79 = solver.IntVar(0, 1, 'C1_R_CAST_div79')
C2_R_CAST_div79 = solver.IntVar(0, 1, 'C2_R_CAST_div79')
solver.Add( + (1)*R_fixbits + (-1)*R_CAST_div79_fixbits + (-10000)*C1_R_CAST_div79<=0)    #Shift cost 1
solver.Add( + (-1)*R_fixbits + (1)*R_CAST_div79_fixbits + (-10000)*C2_R_CAST_div79<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_R_CAST_div79
castCostObj +=  + (1)*C2_R_CAST_div79
C3_R_CAST_div79 = solver.IntVar(0, 1, 'C3_R_CAST_div79')
C4_R_CAST_div79 = solver.IntVar(0, 1, 'C4_R_CAST_div79')
C5_R_CAST_div79 = solver.IntVar(0, 1, 'C5_R_CAST_div79')
C6_R_CAST_div79 = solver.IntVar(0, 1, 'C6_R_CAST_div79')
C7_R_CAST_div79 = solver.IntVar(0, 1, 'C7_R_CAST_div79')
C8_R_CAST_div79 = solver.IntVar(0, 1, 'C8_R_CAST_div79')
solver.Add( + (1)*R_fixp + (1)*R_CAST_div79_float + (-1)*C3_R_CAST_div79<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_R_CAST_div79
solver.Add( + (1)*R_float + (1)*R_CAST_div79_fixp + (-1)*C4_R_CAST_div79<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_R_CAST_div79
solver.Add( + (1)*R_fixp + (1)*R_CAST_div79_double + (-1)*C5_R_CAST_div79<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_R_CAST_div79
solver.Add( + (1)*R_double + (1)*R_CAST_div79_fixp + (-1)*C6_R_CAST_div79<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_R_CAST_div79
solver.Add( + (1)*R_float + (1)*R_CAST_div79_double + (-1)*C7_R_CAST_div79<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_R_CAST_div79
solver.Add( + (1)*R_double + (1)*R_CAST_div79_float + (-1)*C8_R_CAST_div79<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_R_CAST_div79



#Stuff for   %div79 = fdiv double %tmp3, %tmp4, !taffo.info !28, !taffo.initweight !25
main_div79_fixbits = solver.IntVar(0, 30, 'main_div79_fixbits')
main_div79_fixp = solver.IntVar(0, 1, 'main_div79_fixp')
main_div79_float = solver.IntVar(0, 1, 'main_div79_float')
main_div79_double = solver.IntVar(0, 1, 'main_div79_double')
main_div79_enob = solver.IntVar(-10000, 10000, 'main_div79_enob')
solver.Add( + (1)*main_div79_enob + (-1)*main_div79_fixbits + (10000)*main_div79_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div79_enob + (10000)*main_div79_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div79_enob + (10000)*main_div79_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div79_fixbits + (-10000)*main_div79_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*main_div79_enob
solver.Add( + (1)*main_div79_fixp + (1)*main_div79_float + (1)*main_div79_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div79_fixbits + (-10000)*main_div79_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*A_CAST_div79_fixp + (-1)*R_CAST_div79_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_div79_float + (-1)*R_CAST_div79_float==0)    #float equality
solver.Add( + (1)*A_CAST_div79_double + (-1)*R_CAST_div79_double==0)    #double equality
solver.Add( + (1)*A_CAST_div79_fixp + (-1)*main_div79_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_div79_float + (-1)*main_div79_float==0)    #float equality
solver.Add( + (1)*A_CAST_div79_double + (-1)*main_div79_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div79_fixp
mathCostObj +=  + (5.60026)*main_div79_float
mathCostObj +=  + (18.3266)*main_div79_double
main_main_div79_enob_1 = solver.IntVar(0, 1, 'main_main_div79_enob_1')
main_main_div79_enob_2 = solver.IntVar(0, 1, 'main_main_div79_enob_2')
solver.Add( + (1)*main_main_div79_enob_1 + (1)*main_main_div79_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div79_enob + (-1)*R_enob_memphi_main_tmp4 + (-10000)*main_main_div79_enob_1<=1044)    #Enob: propagation in division 1
solver.Add( + (1)*main_div79_enob + (-1)*A_enob_memphi_main_tmp3 + (-10000)*main_main_div79_enob_2<=1044)    #Enob: propagation in division 2



#Constraint for cast for   store double %div79, double* %arrayidx83, align 8, !taffo.info !8, !taffo.initweight !21
main_div79_CAST_store_fixbits = solver.IntVar(0, 30, 'main_div79_CAST_store_fixbits')
main_div79_CAST_store_fixp = solver.IntVar(0, 1, 'main_div79_CAST_store_fixp')
main_div79_CAST_store_float = solver.IntVar(0, 1, 'main_div79_CAST_store_float')
main_div79_CAST_store_double = solver.IntVar(0, 1, 'main_div79_CAST_store_double')
solver.Add( + (1)*main_div79_CAST_store_fixp + (1)*main_div79_CAST_store_float + (1)*main_div79_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div79_CAST_store_fixbits + (-10000)*main_div79_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div79_CAST_store = solver.IntVar(0, 1, 'C1_main_div79_CAST_store')
C2_main_div79_CAST_store = solver.IntVar(0, 1, 'C2_main_div79_CAST_store')
solver.Add( + (1)*main_div79_fixbits + (-1)*main_div79_CAST_store_fixbits + (-10000)*C1_main_div79_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div79_fixbits + (1)*main_div79_CAST_store_fixbits + (-10000)*C2_main_div79_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div79_CAST_store
castCostObj +=  + (1)*C2_main_div79_CAST_store
C3_main_div79_CAST_store = solver.IntVar(0, 1, 'C3_main_div79_CAST_store')
C4_main_div79_CAST_store = solver.IntVar(0, 1, 'C4_main_div79_CAST_store')
C5_main_div79_CAST_store = solver.IntVar(0, 1, 'C5_main_div79_CAST_store')
C6_main_div79_CAST_store = solver.IntVar(0, 1, 'C6_main_div79_CAST_store')
C7_main_div79_CAST_store = solver.IntVar(0, 1, 'C7_main_div79_CAST_store')
C8_main_div79_CAST_store = solver.IntVar(0, 1, 'C8_main_div79_CAST_store')
solver.Add( + (1)*main_div79_fixp + (1)*main_div79_CAST_store_float + (-1)*C3_main_div79_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div79_CAST_store
solver.Add( + (1)*main_div79_float + (1)*main_div79_CAST_store_fixp + (-1)*C4_main_div79_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div79_CAST_store
solver.Add( + (1)*main_div79_fixp + (1)*main_div79_CAST_store_double + (-1)*C5_main_div79_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div79_CAST_store
solver.Add( + (1)*main_div79_double + (1)*main_div79_CAST_store_fixp + (-1)*C6_main_div79_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div79_CAST_store
solver.Add( + (1)*main_div79_float + (1)*main_div79_CAST_store_double + (-1)*C7_main_div79_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div79_CAST_store
solver.Add( + (1)*main_div79_double + (1)*main_div79_CAST_store_float + (-1)*C8_main_div79_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div79_CAST_store
solver.Add( + (1)*Q_fixp + (-1)*main_div79_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*Q_float + (-1)*main_div79_CAST_store_float==0)    #float equality
solver.Add( + (1)*Q_double + (-1)*main_div79_CAST_store_double==0)    #double equality
solver.Add( + (1)*Q_fixbits + (-1)*main_div79_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
Q_enob_storeENOB = solver.IntVar(-10000, 10000, 'Q_enob_storeENOB')
solver.Add( + (1)*Q_enob_storeENOB + (-1)*Q_fixbits + (10000)*Q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*Q_enob_storeENOB + (10000)*Q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*Q_enob_storeENOB + (10000)*Q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*Q_enob_storeENOB + (-1)*main_div79_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*Q_enob_storeENOB + (10000)*main_main_tmp_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*Q_enob_storeENOB + (10000)*main_main_tmp1_enob_4<=10000)    #Enob: forcing MEM phi enob



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



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx87, align 8, !taffo.info !8, !taffo.initweight !21, !taffo.constinfo !44
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
castCostObj +=  + (1)*C1_ConstantValue__14_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__14_CAST_store
C3_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__14_CAST_store')
C4_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__14_CAST_store')
C5_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__14_CAST_store')
C6_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__14_CAST_store')
C7_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__14_CAST_store')
C8_ConstantValue__14_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__14_CAST_store')
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_store_float + (-1)*C3_ConstantValue__14_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_store_fixp + (-1)*C4_ConstantValue__14_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_store_double + (-1)*C5_ConstantValue__14_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_store_fixp + (-1)*C6_ConstantValue__14_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_store_double + (-1)*C7_ConstantValue__14_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_store_float + (-1)*C8_ConstantValue__14_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__14_CAST_store
solver.Add( + (1)*Q_fixp + (-1)*ConstantValue__14_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*Q_float + (-1)*ConstantValue__14_CAST_store_float==0)    #float equality
solver.Add( + (1)*Q_double + (-1)*ConstantValue__14_CAST_store_double==0)    #double equality
solver.Add( + (1)*Q_fixbits + (-1)*ConstantValue__14_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*Q_enob_storeENOB + (10000)*main_main_tmp_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*Q_enob_storeENOB + (10000)*main_main_tmp1_enob_5<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 0.000000e+00
ConstantValue__15_fixbits = solver.IntVar(0, 32, 'ConstantValue__15_fixbits')
ConstantValue__15_fixp = solver.IntVar(0, 1, 'ConstantValue__15_fixp')
ConstantValue__15_float = solver.IntVar(0, 1, 'ConstantValue__15_float')
ConstantValue__15_double = solver.IntVar(0, 1, 'ConstantValue__15_double')
ConstantValue__15_enob = solver.IntVar(-10000, 10000, 'ConstantValue__15_enob')
solver.Add( + (1)*ConstantValue__15_enob + (-1)*ConstantValue__15_fixbits + (10000)*ConstantValue__15_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__15_fixp + (1)*ConstantValue__15_float + (1)*ConstantValue__15_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__16_fixbits = solver.IntVar(0, 32, 'ConstantValue__16_fixbits')
ConstantValue__16_fixp = solver.IntVar(0, 1, 'ConstantValue__16_fixp')
ConstantValue__16_float = solver.IntVar(0, 1, 'ConstantValue__16_float')
ConstantValue__16_double = solver.IntVar(0, 1, 'ConstantValue__16_double')
ConstantValue__16_enob = solver.IntVar(-10000, 10000, 'ConstantValue__16_enob')
solver.Add( + (1)*ConstantValue__16_enob + (-1)*ConstantValue__16_fixbits + (10000)*ConstantValue__16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx99, align 8, !taffo.info !8, !taffo.initweight !21, !taffo.constinfo !44
ConstantValue__16_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__16_CAST_store_fixbits')
ConstantValue__16_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__16_CAST_store_fixp')
ConstantValue__16_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__16_CAST_store_float')
ConstantValue__16_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__16_CAST_store_double')
solver.Add( + (1)*ConstantValue__16_CAST_store_fixp + (1)*ConstantValue__16_CAST_store_float + (1)*ConstantValue__16_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__16_CAST_store_fixbits + (-10000)*ConstantValue__16_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__16_CAST_store')
C2_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__16_CAST_store')
solver.Add( + (1)*ConstantValue__16_fixbits + (-1)*ConstantValue__16_CAST_store_fixbits + (-10000)*C1_ConstantValue__16_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__16_fixbits + (1)*ConstantValue__16_CAST_store_fixbits + (-10000)*C2_ConstantValue__16_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__16_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__16_CAST_store
C3_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__16_CAST_store')
C4_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__16_CAST_store')
C5_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__16_CAST_store')
C6_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__16_CAST_store')
C7_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__16_CAST_store')
C8_ConstantValue__16_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__16_CAST_store')
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_store_float + (-1)*C3_ConstantValue__16_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_store_fixp + (-1)*C4_ConstantValue__16_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_store_double + (-1)*C5_ConstantValue__16_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_store_fixp + (-1)*C6_ConstantValue__16_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_store_double + (-1)*C7_ConstantValue__16_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_store_float + (-1)*C8_ConstantValue__16_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__16_CAST_store
solver.Add( + (1)*R_fixp + (-1)*ConstantValue__16_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*R_float + (-1)*ConstantValue__16_CAST_store_float==0)    #float equality
solver.Add( + (1)*R_double + (-1)*ConstantValue__16_CAST_store_double==0)    #double equality
solver.Add( + (1)*R_fixbits + (-1)*ConstantValue__16_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*R_enob_storeENOB + (10000)*main_main_tmp_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*R_enob_storeENOB + (10000)*main_main_tmp1_enob_6<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
Q_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'Q_enob_memphi_main_tmp5')
solver.Add( + (1)*Q_enob_memphi_main_tmp5 + (-1)*Q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_0 = solver.IntVar(0, 1, 'main_main_tmp5_enob_0')
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
solver.Add( + (1)*main_main_tmp5_enob_0 + (1)*main_main_tmp5_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*Q_enob_memphi_main_tmp5 + (-1)*R_enob_storeENOB + (10000)*main_main_tmp5_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*Q_enob_memphi_main_tmp5 + (-1)*Q_enob_storeENOB + (10000)*main_main_tmp5_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp6')
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_0 = solver.IntVar(0, 1, 'main_main_tmp6_enob_0')
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_4 = solver.IntVar(0, 1, 'main_main_tmp6_enob_4')
main_main_tmp6_enob_5 = solver.IntVar(0, 1, 'main_main_tmp6_enob_5')
solver.Add( + (1)*main_main_tmp6_enob_0 + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_4 + (1)*main_main_tmp6_enob_5==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*R_enob_storeENOB + (10000)*main_main_tmp6_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*Q_enob_storeENOB + (10000)*main_main_tmp6_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul112 = fmul double %tmp5, %tmp6, !taffo.info !52, !taffo.initweight !25
Q_CAST_mul112_fixbits = solver.IntVar(0, 21, 'Q_CAST_mul112_fixbits')
Q_CAST_mul112_fixp = solver.IntVar(0, 1, 'Q_CAST_mul112_fixp')
Q_CAST_mul112_float = solver.IntVar(0, 1, 'Q_CAST_mul112_float')
Q_CAST_mul112_double = solver.IntVar(0, 1, 'Q_CAST_mul112_double')
solver.Add( + (1)*Q_CAST_mul112_fixp + (1)*Q_CAST_mul112_float + (1)*Q_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*Q_CAST_mul112_fixbits + (-10000)*Q_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_Q_CAST_mul112 = solver.IntVar(0, 1, 'C1_Q_CAST_mul112')
C2_Q_CAST_mul112 = solver.IntVar(0, 1, 'C2_Q_CAST_mul112')
solver.Add( + (1)*Q_fixbits + (-1)*Q_CAST_mul112_fixbits + (-10000)*C1_Q_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*Q_fixbits + (1)*Q_CAST_mul112_fixbits + (-10000)*C2_Q_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_Q_CAST_mul112
castCostObj +=  + (1)*C2_Q_CAST_mul112
C3_Q_CAST_mul112 = solver.IntVar(0, 1, 'C3_Q_CAST_mul112')
C4_Q_CAST_mul112 = solver.IntVar(0, 1, 'C4_Q_CAST_mul112')
C5_Q_CAST_mul112 = solver.IntVar(0, 1, 'C5_Q_CAST_mul112')
C6_Q_CAST_mul112 = solver.IntVar(0, 1, 'C6_Q_CAST_mul112')
C7_Q_CAST_mul112 = solver.IntVar(0, 1, 'C7_Q_CAST_mul112')
C8_Q_CAST_mul112 = solver.IntVar(0, 1, 'C8_Q_CAST_mul112')
solver.Add( + (1)*Q_fixp + (1)*Q_CAST_mul112_float + (-1)*C3_Q_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_Q_CAST_mul112
solver.Add( + (1)*Q_float + (1)*Q_CAST_mul112_fixp + (-1)*C4_Q_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_Q_CAST_mul112
solver.Add( + (1)*Q_fixp + (1)*Q_CAST_mul112_double + (-1)*C5_Q_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_Q_CAST_mul112
solver.Add( + (1)*Q_double + (1)*Q_CAST_mul112_fixp + (-1)*C6_Q_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_Q_CAST_mul112
solver.Add( + (1)*Q_float + (1)*Q_CAST_mul112_double + (-1)*C7_Q_CAST_mul112<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_Q_CAST_mul112
solver.Add( + (1)*Q_double + (1)*Q_CAST_mul112_float + (-1)*C8_Q_CAST_mul112<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_Q_CAST_mul112



#Constraint for cast for   %mul112 = fmul double %tmp5, %tmp6, !taffo.info !52, !taffo.initweight !25
A_CAST_mul112_fixbits = solver.IntVar(0, 21, 'A_CAST_mul112_fixbits')
A_CAST_mul112_fixp = solver.IntVar(0, 1, 'A_CAST_mul112_fixp')
A_CAST_mul112_float = solver.IntVar(0, 1, 'A_CAST_mul112_float')
A_CAST_mul112_double = solver.IntVar(0, 1, 'A_CAST_mul112_double')
solver.Add( + (1)*A_CAST_mul112_fixp + (1)*A_CAST_mul112_float + (1)*A_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_mul112_fixbits + (-10000)*A_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_mul112 = solver.IntVar(0, 1, 'C1_A_CAST_mul112')
C2_A_CAST_mul112 = solver.IntVar(0, 1, 'C2_A_CAST_mul112')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_mul112_fixbits + (-10000)*C1_A_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_mul112_fixbits + (-10000)*C2_A_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_mul112
castCostObj +=  + (1)*C2_A_CAST_mul112
C3_A_CAST_mul112 = solver.IntVar(0, 1, 'C3_A_CAST_mul112')
C4_A_CAST_mul112 = solver.IntVar(0, 1, 'C4_A_CAST_mul112')
C5_A_CAST_mul112 = solver.IntVar(0, 1, 'C5_A_CAST_mul112')
C6_A_CAST_mul112 = solver.IntVar(0, 1, 'C6_A_CAST_mul112')
C7_A_CAST_mul112 = solver.IntVar(0, 1, 'C7_A_CAST_mul112')
C8_A_CAST_mul112 = solver.IntVar(0, 1, 'C8_A_CAST_mul112')
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul112_float + (-1)*C3_A_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_mul112
solver.Add( + (1)*A_float + (1)*A_CAST_mul112_fixp + (-1)*C4_A_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_mul112
solver.Add( + (1)*A_fixp + (1)*A_CAST_mul112_double + (-1)*C5_A_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_mul112
solver.Add( + (1)*A_double + (1)*A_CAST_mul112_fixp + (-1)*C6_A_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_mul112
solver.Add( + (1)*A_float + (1)*A_CAST_mul112_double + (-1)*C7_A_CAST_mul112<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_mul112
solver.Add( + (1)*A_double + (1)*A_CAST_mul112_float + (-1)*C8_A_CAST_mul112<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_mul112



#Stuff for   %mul112 = fmul double %tmp5, %tmp6, !taffo.info !52, !taffo.initweight !25
main_mul112_fixbits = solver.IntVar(0, 11, 'main_mul112_fixbits')
main_mul112_fixp = solver.IntVar(0, 1, 'main_mul112_fixp')
main_mul112_float = solver.IntVar(0, 1, 'main_mul112_float')
main_mul112_double = solver.IntVar(0, 1, 'main_mul112_double')
main_mul112_enob = solver.IntVar(-10000, 10000, 'main_mul112_enob')
solver.Add( + (1)*main_mul112_enob + (-1)*main_mul112_fixbits + (10000)*main_mul112_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp>=-9990)    #Limit the lower number of frac bits11
enobCostObj +=  + (-1)*main_mul112_enob
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_float + (1)*main_mul112_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*Q_CAST_mul112_fixp + (-1)*A_CAST_mul112_fixp==0)    #fix equality
solver.Add( + (1)*Q_CAST_mul112_float + (-1)*A_CAST_mul112_float==0)    #float equality
solver.Add( + (1)*Q_CAST_mul112_double + (-1)*A_CAST_mul112_double==0)    #double equality
solver.Add( + (1)*Q_CAST_mul112_fixp + (-1)*main_mul112_fixp==0)    #fix equality
solver.Add( + (1)*Q_CAST_mul112_float + (-1)*main_mul112_float==0)    #float equality
solver.Add( + (1)*Q_CAST_mul112_double + (-1)*main_mul112_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul112_fixp
mathCostObj +=  + (2.64722)*main_mul112_float
mathCostObj +=  + (4.02255)*main_mul112_double
main_main_mul112_enob_1 = solver.IntVar(0, 1, 'main_main_mul112_enob_1')
main_main_mul112_enob_2 = solver.IntVar(0, 1, 'main_main_mul112_enob_2')
solver.Add( + (1)*main_main_mul112_enob_1 + (1)*main_main_mul112_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul112_enob + (-1)*A_enob_memphi_main_tmp6 + (-10000)*main_main_mul112_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul112_enob + (-1)*Q_enob_memphi_main_tmp5 + (-10000)*main_main_mul112_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
R_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'R_enob_memphi_main_tmp7')
solver.Add( + (1)*R_enob_memphi_main_tmp7 + (-1)*R_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
solver.Add( + (1)*main_main_tmp7_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add117 = fadd double %tmp7, %mul112, !taffo.info !57, !taffo.initweight !25
R_CAST_add117_fixbits = solver.IntVar(0, 21, 'R_CAST_add117_fixbits')
R_CAST_add117_fixp = solver.IntVar(0, 1, 'R_CAST_add117_fixp')
R_CAST_add117_float = solver.IntVar(0, 1, 'R_CAST_add117_float')
R_CAST_add117_double = solver.IntVar(0, 1, 'R_CAST_add117_double')
solver.Add( + (1)*R_CAST_add117_fixp + (1)*R_CAST_add117_float + (1)*R_CAST_add117_double==1)    #exactly 1 type
solver.Add( + (1)*R_CAST_add117_fixbits + (-10000)*R_CAST_add117_fixp<=0)    #If no fix, fix frac part = 0
C1_R_CAST_add117 = solver.IntVar(0, 1, 'C1_R_CAST_add117')
C2_R_CAST_add117 = solver.IntVar(0, 1, 'C2_R_CAST_add117')
solver.Add( + (1)*R_fixbits + (-1)*R_CAST_add117_fixbits + (-10000)*C1_R_CAST_add117<=0)    #Shift cost 1
solver.Add( + (-1)*R_fixbits + (1)*R_CAST_add117_fixbits + (-10000)*C2_R_CAST_add117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_R_CAST_add117
castCostObj +=  + (1)*C2_R_CAST_add117
C3_R_CAST_add117 = solver.IntVar(0, 1, 'C3_R_CAST_add117')
C4_R_CAST_add117 = solver.IntVar(0, 1, 'C4_R_CAST_add117')
C5_R_CAST_add117 = solver.IntVar(0, 1, 'C5_R_CAST_add117')
C6_R_CAST_add117 = solver.IntVar(0, 1, 'C6_R_CAST_add117')
C7_R_CAST_add117 = solver.IntVar(0, 1, 'C7_R_CAST_add117')
C8_R_CAST_add117 = solver.IntVar(0, 1, 'C8_R_CAST_add117')
solver.Add( + (1)*R_fixp + (1)*R_CAST_add117_float + (-1)*C3_R_CAST_add117<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_R_CAST_add117
solver.Add( + (1)*R_float + (1)*R_CAST_add117_fixp + (-1)*C4_R_CAST_add117<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_R_CAST_add117
solver.Add( + (1)*R_fixp + (1)*R_CAST_add117_double + (-1)*C5_R_CAST_add117<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_R_CAST_add117
solver.Add( + (1)*R_double + (1)*R_CAST_add117_fixp + (-1)*C6_R_CAST_add117<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_R_CAST_add117
solver.Add( + (1)*R_float + (1)*R_CAST_add117_double + (-1)*C7_R_CAST_add117<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_R_CAST_add117
solver.Add( + (1)*R_double + (1)*R_CAST_add117_float + (-1)*C8_R_CAST_add117<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_R_CAST_add117



#Constraint for cast for   %add117 = fadd double %tmp7, %mul112, !taffo.info !57, !taffo.initweight !25
main_mul112_CAST_add117_fixbits = solver.IntVar(0, 11, 'main_mul112_CAST_add117_fixbits')
main_mul112_CAST_add117_fixp = solver.IntVar(0, 1, 'main_mul112_CAST_add117_fixp')
main_mul112_CAST_add117_float = solver.IntVar(0, 1, 'main_mul112_CAST_add117_float')
main_mul112_CAST_add117_double = solver.IntVar(0, 1, 'main_mul112_CAST_add117_double')
solver.Add( + (1)*main_mul112_CAST_add117_fixp + (1)*main_mul112_CAST_add117_float + (1)*main_mul112_CAST_add117_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul112_CAST_add117_fixbits + (-10000)*main_mul112_CAST_add117_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C1_main_mul112_CAST_add117')
C2_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C2_main_mul112_CAST_add117')
solver.Add( + (1)*main_mul112_fixbits + (-1)*main_mul112_CAST_add117_fixbits + (-10000)*C1_main_mul112_CAST_add117<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul112_fixbits + (1)*main_mul112_CAST_add117_fixbits + (-10000)*C2_main_mul112_CAST_add117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul112_CAST_add117
castCostObj +=  + (1)*C2_main_mul112_CAST_add117
C3_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C3_main_mul112_CAST_add117')
C4_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C4_main_mul112_CAST_add117')
C5_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C5_main_mul112_CAST_add117')
C6_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C6_main_mul112_CAST_add117')
C7_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C7_main_mul112_CAST_add117')
C8_main_mul112_CAST_add117 = solver.IntVar(0, 1, 'C8_main_mul112_CAST_add117')
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_CAST_add117_float + (-1)*C3_main_mul112_CAST_add117<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul112_CAST_add117
solver.Add( + (1)*main_mul112_float + (1)*main_mul112_CAST_add117_fixp + (-1)*C4_main_mul112_CAST_add117<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul112_CAST_add117
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_CAST_add117_double + (-1)*C5_main_mul112_CAST_add117<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul112_CAST_add117
solver.Add( + (1)*main_mul112_double + (1)*main_mul112_CAST_add117_fixp + (-1)*C6_main_mul112_CAST_add117<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul112_CAST_add117
solver.Add( + (1)*main_mul112_float + (1)*main_mul112_CAST_add117_double + (-1)*C7_main_mul112_CAST_add117<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul112_CAST_add117
solver.Add( + (1)*main_mul112_double + (1)*main_mul112_CAST_add117_float + (-1)*C8_main_mul112_CAST_add117<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul112_CAST_add117



#Stuff for   %add117 = fadd double %tmp7, %mul112, !taffo.info !57, !taffo.initweight !25
main_add117_fixbits = solver.IntVar(0, 11, 'main_add117_fixbits')
main_add117_fixp = solver.IntVar(0, 1, 'main_add117_fixp')
main_add117_float = solver.IntVar(0, 1, 'main_add117_float')
main_add117_double = solver.IntVar(0, 1, 'main_add117_double')
main_add117_enob = solver.IntVar(-10000, 10000, 'main_add117_enob')
solver.Add( + (1)*main_add117_enob + (-1)*main_add117_fixbits + (10000)*main_add117_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add117_enob + (10000)*main_add117_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add117_enob + (10000)*main_add117_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add117_fixbits + (-10000)*main_add117_fixp>=-9990)    #Limit the lower number of frac bits11
enobCostObj +=  + (-1)*main_add117_enob
solver.Add( + (1)*main_add117_fixp + (1)*main_add117_float + (1)*main_add117_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add117_fixbits + (-10000)*main_add117_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*R_CAST_add117_fixp + (-1)*main_mul112_CAST_add117_fixp==0)    #fix equality
solver.Add( + (1)*R_CAST_add117_float + (-1)*main_mul112_CAST_add117_float==0)    #float equality
solver.Add( + (1)*R_CAST_add117_double + (-1)*main_mul112_CAST_add117_double==0)    #double equality
solver.Add( + (1)*R_CAST_add117_fixbits + (-1)*main_mul112_CAST_add117_fixbits==0)    #same fractional bit
solver.Add( + (1)*R_CAST_add117_fixp + (-1)*main_add117_fixp==0)    #fix equality
solver.Add( + (1)*R_CAST_add117_float + (-1)*main_add117_float==0)    #float equality
solver.Add( + (1)*R_CAST_add117_double + (-1)*main_add117_double==0)    #double equality
solver.Add( + (1)*R_CAST_add117_fixbits + (-1)*main_add117_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add117_fixp
mathCostObj +=  + (2.33125)*main_add117_float
mathCostObj +=  + (2.72422)*main_add117_double
solver.Add( + (1)*main_add117_enob + (-1)*R_enob_memphi_main_tmp7<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add117_enob + (-1)*main_mul112_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add117, double* %arrayidx116, align 8, !taffo.info !8, !taffo.initweight !21
main_add117_CAST_store_fixbits = solver.IntVar(0, 11, 'main_add117_CAST_store_fixbits')
main_add117_CAST_store_fixp = solver.IntVar(0, 1, 'main_add117_CAST_store_fixp')
main_add117_CAST_store_float = solver.IntVar(0, 1, 'main_add117_CAST_store_float')
main_add117_CAST_store_double = solver.IntVar(0, 1, 'main_add117_CAST_store_double')
solver.Add( + (1)*main_add117_CAST_store_fixp + (1)*main_add117_CAST_store_float + (1)*main_add117_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add117_CAST_store_fixbits + (-10000)*main_add117_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add117_CAST_store = solver.IntVar(0, 1, 'C1_main_add117_CAST_store')
C2_main_add117_CAST_store = solver.IntVar(0, 1, 'C2_main_add117_CAST_store')
solver.Add( + (1)*main_add117_fixbits + (-1)*main_add117_CAST_store_fixbits + (-10000)*C1_main_add117_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add117_fixbits + (1)*main_add117_CAST_store_fixbits + (-10000)*C2_main_add117_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add117_CAST_store
castCostObj +=  + (1)*C2_main_add117_CAST_store
C3_main_add117_CAST_store = solver.IntVar(0, 1, 'C3_main_add117_CAST_store')
C4_main_add117_CAST_store = solver.IntVar(0, 1, 'C4_main_add117_CAST_store')
C5_main_add117_CAST_store = solver.IntVar(0, 1, 'C5_main_add117_CAST_store')
C6_main_add117_CAST_store = solver.IntVar(0, 1, 'C6_main_add117_CAST_store')
C7_main_add117_CAST_store = solver.IntVar(0, 1, 'C7_main_add117_CAST_store')
C8_main_add117_CAST_store = solver.IntVar(0, 1, 'C8_main_add117_CAST_store')
solver.Add( + (1)*main_add117_fixp + (1)*main_add117_CAST_store_float + (-1)*C3_main_add117_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add117_CAST_store
solver.Add( + (1)*main_add117_float + (1)*main_add117_CAST_store_fixp + (-1)*C4_main_add117_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add117_CAST_store
solver.Add( + (1)*main_add117_fixp + (1)*main_add117_CAST_store_double + (-1)*C5_main_add117_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add117_CAST_store
solver.Add( + (1)*main_add117_double + (1)*main_add117_CAST_store_fixp + (-1)*C6_main_add117_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add117_CAST_store
solver.Add( + (1)*main_add117_float + (1)*main_add117_CAST_store_double + (-1)*C7_main_add117_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add117_CAST_store
solver.Add( + (1)*main_add117_double + (1)*main_add117_CAST_store_float + (-1)*C8_main_add117_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add117_CAST_store
solver.Add( + (1)*R_fixp + (-1)*main_add117_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*R_float + (-1)*main_add117_CAST_store_float==0)    #float equality
solver.Add( + (1)*R_double + (-1)*main_add117_CAST_store_double==0)    #double equality
solver.Add( + (1)*R_fixbits + (-1)*main_add117_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
R_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'R_enob_storeENOB_storeENOB')
solver.Add( + (1)*R_enob_storeENOB_storeENOB + (-1)*R_fixbits + (10000)*R_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*R_enob_storeENOB_storeENOB + (10000)*R_float<=10149)    #Enob constraint for float
solver.Add( + (1)*R_enob_storeENOB_storeENOB + (10000)*R_double<=11074)    #Enob constraint for double
solver.Add( + (1)*R_enob_storeENOB_storeENOB + (-1)*main_add117_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*R_enob_storeENOB_storeENOB + (10000)*main_main_tmp_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*R_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*R_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*R_enob_memphi_main_tmp7 + (-1)*R_enob_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp8')
solver.Add( + (1)*A_enob_memphi_main_tmp8 + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
main_main_tmp8_enob_2 = solver.IntVar(0, 1, 'main_main_tmp8_enob_2')
solver.Add( + (1)*main_main_tmp8_enob_1 + (1)*main_main_tmp8_enob_2==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp8 + (-1)*R_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
Q_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'Q_enob_memphi_main_tmp9')
solver.Add( + (1)*Q_enob_memphi_main_tmp9 + (-1)*Q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
main_main_tmp9_enob_1 = solver.IntVar(0, 1, 'main_main_tmp9_enob_1')
solver.Add( + (1)*main_main_tmp9_enob_0 + (1)*main_main_tmp9_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*Q_enob_memphi_main_tmp9 + (-1)*R_enob_storeENOB + (10000)*main_main_tmp9_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*Q_enob_memphi_main_tmp9 + (-1)*Q_enob_storeENOB + (10000)*main_main_tmp9_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
R_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'R_enob_memphi_main_tmp10')
solver.Add( + (1)*R_enob_memphi_main_tmp10 + (-1)*R_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_1 = solver.IntVar(0, 1, 'main_main_tmp10_enob_1')
solver.Add( + (1)*main_main_tmp10_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*R_enob_memphi_main_tmp10 + (-1)*R_enob_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul137 = fmul double %tmp9, %tmp10, !taffo.info !52, !taffo.initweight !25
Q_CAST_mul137_fixbits = solver.IntVar(0, 21, 'Q_CAST_mul137_fixbits')
Q_CAST_mul137_fixp = solver.IntVar(0, 1, 'Q_CAST_mul137_fixp')
Q_CAST_mul137_float = solver.IntVar(0, 1, 'Q_CAST_mul137_float')
Q_CAST_mul137_double = solver.IntVar(0, 1, 'Q_CAST_mul137_double')
solver.Add( + (1)*Q_CAST_mul137_fixp + (1)*Q_CAST_mul137_float + (1)*Q_CAST_mul137_double==1)    #exactly 1 type
solver.Add( + (1)*Q_CAST_mul137_fixbits + (-10000)*Q_CAST_mul137_fixp<=0)    #If no fix, fix frac part = 0
C1_Q_CAST_mul137 = solver.IntVar(0, 1, 'C1_Q_CAST_mul137')
C2_Q_CAST_mul137 = solver.IntVar(0, 1, 'C2_Q_CAST_mul137')
solver.Add( + (1)*Q_fixbits + (-1)*Q_CAST_mul137_fixbits + (-10000)*C1_Q_CAST_mul137<=0)    #Shift cost 1
solver.Add( + (-1)*Q_fixbits + (1)*Q_CAST_mul137_fixbits + (-10000)*C2_Q_CAST_mul137<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_Q_CAST_mul137
castCostObj +=  + (1)*C2_Q_CAST_mul137
C3_Q_CAST_mul137 = solver.IntVar(0, 1, 'C3_Q_CAST_mul137')
C4_Q_CAST_mul137 = solver.IntVar(0, 1, 'C4_Q_CAST_mul137')
C5_Q_CAST_mul137 = solver.IntVar(0, 1, 'C5_Q_CAST_mul137')
C6_Q_CAST_mul137 = solver.IntVar(0, 1, 'C6_Q_CAST_mul137')
C7_Q_CAST_mul137 = solver.IntVar(0, 1, 'C7_Q_CAST_mul137')
C8_Q_CAST_mul137 = solver.IntVar(0, 1, 'C8_Q_CAST_mul137')
solver.Add( + (1)*Q_fixp + (1)*Q_CAST_mul137_float + (-1)*C3_Q_CAST_mul137<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_Q_CAST_mul137
solver.Add( + (1)*Q_float + (1)*Q_CAST_mul137_fixp + (-1)*C4_Q_CAST_mul137<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_Q_CAST_mul137
solver.Add( + (1)*Q_fixp + (1)*Q_CAST_mul137_double + (-1)*C5_Q_CAST_mul137<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_Q_CAST_mul137
solver.Add( + (1)*Q_double + (1)*Q_CAST_mul137_fixp + (-1)*C6_Q_CAST_mul137<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_Q_CAST_mul137
solver.Add( + (1)*Q_float + (1)*Q_CAST_mul137_double + (-1)*C7_Q_CAST_mul137<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_Q_CAST_mul137
solver.Add( + (1)*Q_double + (1)*Q_CAST_mul137_float + (-1)*C8_Q_CAST_mul137<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_Q_CAST_mul137



#Constraint for cast for   %mul137 = fmul double %tmp9, %tmp10, !taffo.info !52, !taffo.initweight !25
R_CAST_mul137_fixbits = solver.IntVar(0, 21, 'R_CAST_mul137_fixbits')
R_CAST_mul137_fixp = solver.IntVar(0, 1, 'R_CAST_mul137_fixp')
R_CAST_mul137_float = solver.IntVar(0, 1, 'R_CAST_mul137_float')
R_CAST_mul137_double = solver.IntVar(0, 1, 'R_CAST_mul137_double')
solver.Add( + (1)*R_CAST_mul137_fixp + (1)*R_CAST_mul137_float + (1)*R_CAST_mul137_double==1)    #exactly 1 type
solver.Add( + (1)*R_CAST_mul137_fixbits + (-10000)*R_CAST_mul137_fixp<=0)    #If no fix, fix frac part = 0
C1_R_CAST_mul137 = solver.IntVar(0, 1, 'C1_R_CAST_mul137')
C2_R_CAST_mul137 = solver.IntVar(0, 1, 'C2_R_CAST_mul137')
solver.Add( + (1)*R_fixbits + (-1)*R_CAST_mul137_fixbits + (-10000)*C1_R_CAST_mul137<=0)    #Shift cost 1
solver.Add( + (-1)*R_fixbits + (1)*R_CAST_mul137_fixbits + (-10000)*C2_R_CAST_mul137<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_R_CAST_mul137
castCostObj +=  + (1)*C2_R_CAST_mul137
C3_R_CAST_mul137 = solver.IntVar(0, 1, 'C3_R_CAST_mul137')
C4_R_CAST_mul137 = solver.IntVar(0, 1, 'C4_R_CAST_mul137')
C5_R_CAST_mul137 = solver.IntVar(0, 1, 'C5_R_CAST_mul137')
C6_R_CAST_mul137 = solver.IntVar(0, 1, 'C6_R_CAST_mul137')
C7_R_CAST_mul137 = solver.IntVar(0, 1, 'C7_R_CAST_mul137')
C8_R_CAST_mul137 = solver.IntVar(0, 1, 'C8_R_CAST_mul137')
solver.Add( + (1)*R_fixp + (1)*R_CAST_mul137_float + (-1)*C3_R_CAST_mul137<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_R_CAST_mul137
solver.Add( + (1)*R_float + (1)*R_CAST_mul137_fixp + (-1)*C4_R_CAST_mul137<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_R_CAST_mul137
solver.Add( + (1)*R_fixp + (1)*R_CAST_mul137_double + (-1)*C5_R_CAST_mul137<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_R_CAST_mul137
solver.Add( + (1)*R_double + (1)*R_CAST_mul137_fixp + (-1)*C6_R_CAST_mul137<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_R_CAST_mul137
solver.Add( + (1)*R_float + (1)*R_CAST_mul137_double + (-1)*C7_R_CAST_mul137<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_R_CAST_mul137
solver.Add( + (1)*R_double + (1)*R_CAST_mul137_float + (-1)*C8_R_CAST_mul137<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_R_CAST_mul137



#Stuff for   %mul137 = fmul double %tmp9, %tmp10, !taffo.info !52, !taffo.initweight !25
main_mul137_fixbits = solver.IntVar(0, 11, 'main_mul137_fixbits')
main_mul137_fixp = solver.IntVar(0, 1, 'main_mul137_fixp')
main_mul137_float = solver.IntVar(0, 1, 'main_mul137_float')
main_mul137_double = solver.IntVar(0, 1, 'main_mul137_double')
main_mul137_enob = solver.IntVar(-10000, 10000, 'main_mul137_enob')
solver.Add( + (1)*main_mul137_enob + (-1)*main_mul137_fixbits + (10000)*main_mul137_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul137_enob + (10000)*main_mul137_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul137_enob + (10000)*main_mul137_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul137_fixbits + (-10000)*main_mul137_fixp>=-9990)    #Limit the lower number of frac bits11
enobCostObj +=  + (-1)*main_mul137_enob
solver.Add( + (1)*main_mul137_fixp + (1)*main_mul137_float + (1)*main_mul137_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul137_fixbits + (-10000)*main_mul137_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*Q_CAST_mul137_fixp + (-1)*R_CAST_mul137_fixp==0)    #fix equality
solver.Add( + (1)*Q_CAST_mul137_float + (-1)*R_CAST_mul137_float==0)    #float equality
solver.Add( + (1)*Q_CAST_mul137_double + (-1)*R_CAST_mul137_double==0)    #double equality
solver.Add( + (1)*Q_CAST_mul137_fixp + (-1)*main_mul137_fixp==0)    #fix equality
solver.Add( + (1)*Q_CAST_mul137_float + (-1)*main_mul137_float==0)    #float equality
solver.Add( + (1)*Q_CAST_mul137_double + (-1)*main_mul137_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul137_fixp
mathCostObj +=  + (2.64722)*main_mul137_float
mathCostObj +=  + (4.02255)*main_mul137_double
main_main_mul137_enob_1 = solver.IntVar(0, 1, 'main_main_mul137_enob_1')
main_main_mul137_enob_2 = solver.IntVar(0, 1, 'main_main_mul137_enob_2')
solver.Add( + (1)*main_main_mul137_enob_1 + (1)*main_main_mul137_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul137_enob + (-1)*R_enob_memphi_main_tmp10 + (-10000)*main_main_mul137_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul137_enob + (-1)*Q_enob_memphi_main_tmp9 + (-10000)*main_main_mul137_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub = fsub double %tmp8, %mul137, !taffo.info !57, !taffo.initweight !25
A_CAST_sub_fixbits = solver.IntVar(0, 21, 'A_CAST_sub_fixbits')
A_CAST_sub_fixp = solver.IntVar(0, 1, 'A_CAST_sub_fixp')
A_CAST_sub_float = solver.IntVar(0, 1, 'A_CAST_sub_float')
A_CAST_sub_double = solver.IntVar(0, 1, 'A_CAST_sub_double')
solver.Add( + (1)*A_CAST_sub_fixp + (1)*A_CAST_sub_float + (1)*A_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*A_CAST_sub_fixbits + (-10000)*A_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_A_CAST_sub = solver.IntVar(0, 1, 'C1_A_CAST_sub')
C2_A_CAST_sub = solver.IntVar(0, 1, 'C2_A_CAST_sub')
solver.Add( + (1)*A_fixbits + (-1)*A_CAST_sub_fixbits + (-10000)*C1_A_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*A_fixbits + (1)*A_CAST_sub_fixbits + (-10000)*C2_A_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_A_CAST_sub
castCostObj +=  + (1)*C2_A_CAST_sub
C3_A_CAST_sub = solver.IntVar(0, 1, 'C3_A_CAST_sub')
C4_A_CAST_sub = solver.IntVar(0, 1, 'C4_A_CAST_sub')
C5_A_CAST_sub = solver.IntVar(0, 1, 'C5_A_CAST_sub')
C6_A_CAST_sub = solver.IntVar(0, 1, 'C6_A_CAST_sub')
C7_A_CAST_sub = solver.IntVar(0, 1, 'C7_A_CAST_sub')
C8_A_CAST_sub = solver.IntVar(0, 1, 'C8_A_CAST_sub')
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub_float + (-1)*C3_A_CAST_sub<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_A_CAST_sub
solver.Add( + (1)*A_float + (1)*A_CAST_sub_fixp + (-1)*C4_A_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_A_CAST_sub
solver.Add( + (1)*A_fixp + (1)*A_CAST_sub_double + (-1)*C5_A_CAST_sub<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_A_CAST_sub
solver.Add( + (1)*A_double + (1)*A_CAST_sub_fixp + (-1)*C6_A_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_A_CAST_sub
solver.Add( + (1)*A_float + (1)*A_CAST_sub_double + (-1)*C7_A_CAST_sub<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_A_CAST_sub
solver.Add( + (1)*A_double + (1)*A_CAST_sub_float + (-1)*C8_A_CAST_sub<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_A_CAST_sub



#Constraint for cast for   %sub = fsub double %tmp8, %mul137, !taffo.info !57, !taffo.initweight !25
main_mul137_CAST_sub_fixbits = solver.IntVar(0, 11, 'main_mul137_CAST_sub_fixbits')
main_mul137_CAST_sub_fixp = solver.IntVar(0, 1, 'main_mul137_CAST_sub_fixp')
main_mul137_CAST_sub_float = solver.IntVar(0, 1, 'main_mul137_CAST_sub_float')
main_mul137_CAST_sub_double = solver.IntVar(0, 1, 'main_mul137_CAST_sub_double')
solver.Add( + (1)*main_mul137_CAST_sub_fixp + (1)*main_mul137_CAST_sub_float + (1)*main_mul137_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul137_CAST_sub_fixbits + (-10000)*main_mul137_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C1_main_mul137_CAST_sub')
C2_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C2_main_mul137_CAST_sub')
solver.Add( + (1)*main_mul137_fixbits + (-1)*main_mul137_CAST_sub_fixbits + (-10000)*C1_main_mul137_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul137_fixbits + (1)*main_mul137_CAST_sub_fixbits + (-10000)*C2_main_mul137_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul137_CAST_sub
castCostObj +=  + (1)*C2_main_mul137_CAST_sub
C3_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C3_main_mul137_CAST_sub')
C4_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C4_main_mul137_CAST_sub')
C5_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C5_main_mul137_CAST_sub')
C6_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C6_main_mul137_CAST_sub')
C7_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C7_main_mul137_CAST_sub')
C8_main_mul137_CAST_sub = solver.IntVar(0, 1, 'C8_main_mul137_CAST_sub')
solver.Add( + (1)*main_mul137_fixp + (1)*main_mul137_CAST_sub_float + (-1)*C3_main_mul137_CAST_sub<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul137_CAST_sub
solver.Add( + (1)*main_mul137_float + (1)*main_mul137_CAST_sub_fixp + (-1)*C4_main_mul137_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul137_CAST_sub
solver.Add( + (1)*main_mul137_fixp + (1)*main_mul137_CAST_sub_double + (-1)*C5_main_mul137_CAST_sub<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul137_CAST_sub
solver.Add( + (1)*main_mul137_double + (1)*main_mul137_CAST_sub_fixp + (-1)*C6_main_mul137_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul137_CAST_sub
solver.Add( + (1)*main_mul137_float + (1)*main_mul137_CAST_sub_double + (-1)*C7_main_mul137_CAST_sub<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul137_CAST_sub
solver.Add( + (1)*main_mul137_double + (1)*main_mul137_CAST_sub_float + (-1)*C8_main_mul137_CAST_sub<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul137_CAST_sub



#Stuff for   %sub = fsub double %tmp8, %mul137, !taffo.info !57, !taffo.initweight !25
main_sub_fixbits = solver.IntVar(0, 11, 'main_sub_fixbits')
main_sub_fixp = solver.IntVar(0, 1, 'main_sub_fixp')
main_sub_float = solver.IntVar(0, 1, 'main_sub_float')
main_sub_double = solver.IntVar(0, 1, 'main_sub_double')
main_sub_enob = solver.IntVar(-10000, 10000, 'main_sub_enob')
solver.Add( + (1)*main_sub_enob + (-1)*main_sub_fixbits + (10000)*main_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp>=-9990)    #Limit the lower number of frac bits11
enobCostObj +=  + (-1)*main_sub_enob
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_float + (1)*main_sub_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*A_CAST_sub_fixp + (-1)*main_mul137_CAST_sub_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub_float + (-1)*main_mul137_CAST_sub_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub_double + (-1)*main_mul137_CAST_sub_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub_fixbits + (-1)*main_mul137_CAST_sub_fixbits==0)    #same fractional bit
solver.Add( + (1)*A_CAST_sub_fixp + (-1)*main_sub_fixp==0)    #fix equality
solver.Add( + (1)*A_CAST_sub_float + (-1)*main_sub_float==0)    #float equality
solver.Add( + (1)*A_CAST_sub_double + (-1)*main_sub_double==0)    #double equality
solver.Add( + (1)*A_CAST_sub_fixbits + (-1)*main_sub_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub_fixp
mathCostObj +=  + (2.33125)*main_sub_float
mathCostObj +=  + (2.72422)*main_sub_double
solver.Add( + (1)*main_sub_enob + (-1)*A_enob_memphi_main_tmp8<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub_enob + (-1)*main_mul137_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub, double* %arrayidx141, align 8, !taffo.info !8, !taffo.initweight !21
main_sub_CAST_store_fixbits = solver.IntVar(0, 11, 'main_sub_CAST_store_fixbits')
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
castCostObj +=  + (6.62652)*C3_main_sub_CAST_store
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_store_fixp + (-1)*C4_main_sub_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub_CAST_store
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_store_double + (-1)*C5_main_sub_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub_CAST_store
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_store_fixp + (-1)*C6_main_sub_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub_CAST_store
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_store_double + (-1)*C7_main_sub_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub_CAST_store
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_store_float + (-1)*C8_main_sub_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub_CAST_store
solver.Add( + (1)*A_fixp + (-1)*main_sub_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*A_float + (-1)*main_sub_CAST_store_float==0)    #float equality
solver.Add( + (1)*A_double + (-1)*main_sub_CAST_store_double==0)    #double equality
solver.Add( + (1)*A_fixbits + (-1)*main_sub_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
A_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'A_enob_storeENOB_storeENOB')
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (-1)*A_fixbits + (10000)*A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (10000)*A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (10000)*A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*A_enob_storeENOB_storeENOB + (-1)*main_sub_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp_enob_8<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp1 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp1_enob_8<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp6 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp8 + (-1)*A_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
R_enob_memphi_main_tmp13 = solver.IntVar(-10000, 10000, 'R_enob_memphi_main_tmp13')
solver.Add( + (1)*R_enob_memphi_main_tmp13 + (-1)*R_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call171 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp12, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.5, i32 0, i32 0), double %tmp13), !taffo.info !8, !taffo.initweight !25, !taffo.constinfo !60
R_CAST_call171_fixbits = solver.IntVar(0, 21, 'R_CAST_call171_fixbits')
R_CAST_call171_fixp = solver.IntVar(0, 1, 'R_CAST_call171_fixp')
R_CAST_call171_float = solver.IntVar(0, 1, 'R_CAST_call171_float')
R_CAST_call171_double = solver.IntVar(0, 1, 'R_CAST_call171_double')
solver.Add( + (1)*R_CAST_call171_fixp + (1)*R_CAST_call171_float + (1)*R_CAST_call171_double==1)    #exactly 1 type
solver.Add( + (1)*R_CAST_call171_fixbits + (-10000)*R_CAST_call171_fixp<=0)    #If no fix, fix frac part = 0
C1_R_CAST_call171 = solver.IntVar(0, 1, 'C1_R_CAST_call171')
C2_R_CAST_call171 = solver.IntVar(0, 1, 'C2_R_CAST_call171')
solver.Add( + (1)*R_fixbits + (-1)*R_CAST_call171_fixbits + (-10000)*C1_R_CAST_call171<=0)    #Shift cost 1
solver.Add( + (-1)*R_fixbits + (1)*R_CAST_call171_fixbits + (-10000)*C2_R_CAST_call171<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_R_CAST_call171
castCostObj +=  + (1)*C2_R_CAST_call171
C3_R_CAST_call171 = solver.IntVar(0, 1, 'C3_R_CAST_call171')
C4_R_CAST_call171 = solver.IntVar(0, 1, 'C4_R_CAST_call171')
C5_R_CAST_call171 = solver.IntVar(0, 1, 'C5_R_CAST_call171')
C6_R_CAST_call171 = solver.IntVar(0, 1, 'C6_R_CAST_call171')
C7_R_CAST_call171 = solver.IntVar(0, 1, 'C7_R_CAST_call171')
C8_R_CAST_call171 = solver.IntVar(0, 1, 'C8_R_CAST_call171')
solver.Add( + (1)*R_fixp + (1)*R_CAST_call171_float + (-1)*C3_R_CAST_call171<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_R_CAST_call171
solver.Add( + (1)*R_float + (1)*R_CAST_call171_fixp + (-1)*C4_R_CAST_call171<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_R_CAST_call171
solver.Add( + (1)*R_fixp + (1)*R_CAST_call171_double + (-1)*C5_R_CAST_call171<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_R_CAST_call171
solver.Add( + (1)*R_double + (1)*R_CAST_call171_fixp + (-1)*C6_R_CAST_call171<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_R_CAST_call171
solver.Add( + (1)*R_float + (1)*R_CAST_call171_double + (-1)*C7_R_CAST_call171<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_R_CAST_call171
solver.Add( + (1)*R_double + (1)*R_CAST_call171_float + (-1)*C8_R_CAST_call171<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_R_CAST_call171
solver.Add( + (1)*R_CAST_call171_double==1)    #Type constraint for argument value

#Restriction for new enob [LOAD]
Q_enob_memphi_main_tmp16 = solver.IntVar(-10000, 10000, 'Q_enob_memphi_main_tmp16')
solver.Add( + (1)*Q_enob_memphi_main_tmp16 + (-1)*Q_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call198 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp15, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.5, i32 0, i32 0), double %tmp16), !taffo.info !8, !taffo.initweight !25, !taffo.constinfo !60
Q_CAST_call198_fixbits = solver.IntVar(0, 21, 'Q_CAST_call198_fixbits')
Q_CAST_call198_fixp = solver.IntVar(0, 1, 'Q_CAST_call198_fixp')
Q_CAST_call198_float = solver.IntVar(0, 1, 'Q_CAST_call198_float')
Q_CAST_call198_double = solver.IntVar(0, 1, 'Q_CAST_call198_double')
solver.Add( + (1)*Q_CAST_call198_fixp + (1)*Q_CAST_call198_float + (1)*Q_CAST_call198_double==1)    #exactly 1 type
solver.Add( + (1)*Q_CAST_call198_fixbits + (-10000)*Q_CAST_call198_fixp<=0)    #If no fix, fix frac part = 0
C1_Q_CAST_call198 = solver.IntVar(0, 1, 'C1_Q_CAST_call198')
C2_Q_CAST_call198 = solver.IntVar(0, 1, 'C2_Q_CAST_call198')
solver.Add( + (1)*Q_fixbits + (-1)*Q_CAST_call198_fixbits + (-10000)*C1_Q_CAST_call198<=0)    #Shift cost 1
solver.Add( + (-1)*Q_fixbits + (1)*Q_CAST_call198_fixbits + (-10000)*C2_Q_CAST_call198<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_Q_CAST_call198
castCostObj +=  + (1)*C2_Q_CAST_call198
C3_Q_CAST_call198 = solver.IntVar(0, 1, 'C3_Q_CAST_call198')
C4_Q_CAST_call198 = solver.IntVar(0, 1, 'C4_Q_CAST_call198')
C5_Q_CAST_call198 = solver.IntVar(0, 1, 'C5_Q_CAST_call198')
C6_Q_CAST_call198 = solver.IntVar(0, 1, 'C6_Q_CAST_call198')
C7_Q_CAST_call198 = solver.IntVar(0, 1, 'C7_Q_CAST_call198')
C8_Q_CAST_call198 = solver.IntVar(0, 1, 'C8_Q_CAST_call198')
solver.Add( + (1)*Q_fixp + (1)*Q_CAST_call198_float + (-1)*C3_Q_CAST_call198<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_Q_CAST_call198
solver.Add( + (1)*Q_float + (1)*Q_CAST_call198_fixp + (-1)*C4_Q_CAST_call198<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_Q_CAST_call198
solver.Add( + (1)*Q_fixp + (1)*Q_CAST_call198_double + (-1)*C5_Q_CAST_call198<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_Q_CAST_call198
solver.Add( + (1)*Q_double + (1)*Q_CAST_call198_fixp + (-1)*C6_Q_CAST_call198<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_Q_CAST_call198
solver.Add( + (1)*Q_float + (1)*Q_CAST_call198_double + (-1)*C7_Q_CAST_call198<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_Q_CAST_call198
solver.Add( + (1)*Q_double + (1)*Q_CAST_call198_float + (-1)*C8_Q_CAST_call198<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_Q_CAST_call198
solver.Add( + (1)*Q_CAST_call198_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1 * castCostObj / 696.211+ 100000 * enobCostObj / 17232+ 1 * mathCostObj / 63.6403)

# Model declaration end.