


#Stuff for   %A = alloca [400 x [400 x double]], align 16, !taffo.info !11, !taffo.initweight !13
main_A_fixbits = solver.IntVar(0, 29, 'main_A_fixbits')
main_A_fixp = solver.IntVar(0, 1, 'main_A_fixp')
main_A_float = solver.IntVar(0, 1, 'main_A_float')
main_A_double = solver.IntVar(0, 1, 'main_A_double')
main_A_enob = solver.IntVar(-10000, 10000, 'main_A_enob')
solver.Add( + (1)*main_A_enob + (-1)*main_A_fixbits + (10000)*main_A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_A_enob + (10000)*main_A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_A_enob + (10000)*main_A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_A_fixbits + (-10000)*main_A_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_A_double<=0)    #Disable double data type
enobCostObj =  + (-1)*main_A_enob
solver.Add( + (1)*main_A_fixp + (1)*main_A_float + (1)*main_A_double==1)    #Exactly one selected type
solver.Add( + (1)*main_A_fixbits + (-10000)*main_A_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %b = alloca [400 x double], align 16, !taffo.info !14, !taffo.initweight !13
main_b_fixbits = solver.IntVar(0, 29, 'main_b_fixbits')
main_b_fixp = solver.IntVar(0, 1, 'main_b_fixp')
main_b_float = solver.IntVar(0, 1, 'main_b_float')
main_b_double = solver.IntVar(0, 1, 'main_b_double')
main_b_enob = solver.IntVar(-10000, 10000, 'main_b_enob')
solver.Add( + (1)*main_b_enob + (-1)*main_b_fixbits + (10000)*main_b_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_b_enob + (10000)*main_b_float<=10022)    #Enob constraint for float
solver.Add( + (1)*main_b_enob + (10000)*main_b_double<=10051)    #Enob constraint for double
solver.Add( + (1)*main_b_fixbits + (-10000)*main_b_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_b_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_b_enob
solver.Add( + (1)*main_b_fixp + (1)*main_b_float + (1)*main_b_double==1)    #Exactly one selected type
solver.Add( + (1)*main_b_fixbits + (-10000)*main_b_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %x = alloca [400 x double], align 16, !taffo.info !16, !taffo.initweight !13
main_x_fixbits = solver.IntVar(0, 29, 'main_x_fixbits')
main_x_fixp = solver.IntVar(0, 1, 'main_x_fixp')
main_x_float = solver.IntVar(0, 1, 'main_x_float')
main_x_double = solver.IntVar(0, 1, 'main_x_double')
main_x_enob = solver.IntVar(-10000, 10000, 'main_x_enob')
solver.Add( + (1)*main_x_enob + (-1)*main_x_fixbits + (10000)*main_x_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_x_enob + (10000)*main_x_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_x_enob + (10000)*main_x_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_x_fixbits + (-10000)*main_x_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_x_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_x_enob
solver.Add( + (1)*main_x_fixp + (1)*main_x_float + (1)*main_x_double==1)    #Exactly one selected type
solver.Add( + (1)*main_x_fixbits + (-10000)*main_x_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %y = alloca [400 x double], align 16, !taffo.info !17, !taffo.initweight !13
main_y_fixbits = solver.IntVar(0, 28, 'main_y_fixbits')
main_y_fixp = solver.IntVar(0, 1, 'main_y_fixp')
main_y_float = solver.IntVar(0, 1, 'main_y_float')
main_y_double = solver.IntVar(0, 1, 'main_y_double')
main_y_enob = solver.IntVar(-10000, 10000, 'main_y_enob')
solver.Add( + (1)*main_y_enob + (-1)*main_y_fixbits + (10000)*main_y_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_y_enob + (10000)*main_y_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_y_enob + (10000)*main_y_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_y_fixbits + (-10000)*main_y_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_y_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_y_enob
solver.Add( + (1)*main_y_fixp + (1)*main_y_float + (1)*main_y_double==1)    #Exactly one selected type
solver.Add( + (1)*main_y_fixbits + (-10000)*main_y_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %B = alloca [400 x [400 x double]], align 16, !taffo.info !19, !taffo.initweight !13
main_B_fixbits = solver.IntVar(0, 22, 'main_B_fixbits')
main_B_fixp = solver.IntVar(0, 1, 'main_B_fixp')
main_B_float = solver.IntVar(0, 1, 'main_B_float')
main_B_double = solver.IntVar(0, 1, 'main_B_double')
main_B_enob = solver.IntVar(-10000, 10000, 'main_B_enob')
solver.Add( + (1)*main_B_enob + (-1)*main_B_fixbits + (10000)*main_B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_B_enob + (10000)*main_B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_B_enob + (10000)*main_B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_B_fixbits + (-10000)*main_B_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_B_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_B_enob
solver.Add( + (1)*main_B_fixp + (1)*main_B_float + (1)*main_B_double==1)    #Exactly one selected type
solver.Add( + (1)*main_B_fixbits + (-10000)*main_B_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 400 to double, !taffo.info !22
main_conv_fixbits = solver.IntVar(0, 23, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10015)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=10044)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_conv_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__fixbits = solver.IntVar(0, 32, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__0_fixbits = solver.IntVar(0, 32, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__0_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx, align 8, !taffo.info !29, !taffo.initweight !27, !taffo.constinfo !30
ConstantValue__0_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__0_CAST_store_fixbits')
ConstantValue__0_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_fixp')
ConstantValue__0_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_float')
ConstantValue__0_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__0_CAST_store_double')
solver.Add( + (1)*ConstantValue__0_CAST_store_fixp + (1)*ConstantValue__0_CAST_store_float + (1)*ConstantValue__0_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__0_CAST_store_fixbits + (-10000)*ConstantValue__0_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__0_CAST_store')
C2_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__0_CAST_store')
solver.Add( + (1)*ConstantValue__0_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits + (-10000)*C1_ConstantValue__0_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__0_fixbits + (1)*ConstantValue__0_CAST_store_fixbits + (-10000)*C2_ConstantValue__0_CAST_store<=0)    #Shift cost 2
castCostObj =  + (1)*C1_ConstantValue__0_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__0_CAST_store
C3_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__0_CAST_store')
C4_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__0_CAST_store')
C5_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__0_CAST_store')
C6_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__0_CAST_store')
C7_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__0_CAST_store')
C8_ConstantValue__0_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__0_CAST_store')
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_CAST_store_float + (-1)*C3_ConstantValue__0_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C4_ConstantValue__0_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_CAST_store_double + (-1)*C5_ConstantValue__0_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_fixp + (-1)*C6_ConstantValue__0_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_CAST_store_double + (-1)*C7_ConstantValue__0_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__0_CAST_store
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_CAST_store_float + (-1)*C8_ConstantValue__0_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__0_CAST_store
solver.Add( + (1)*main_x_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_x_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_x_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_x_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 0.000000e+00
ConstantValue__1_fixbits = solver.IntVar(0, 32, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__1_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



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
solver.Add( + (1)*ConstantValue__2_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx10, align 8, !taffo.info !29, !taffo.initweight !27, !taffo.constinfo !30
ConstantValue__2_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__2_CAST_store_fixbits')
ConstantValue__2_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__2_CAST_store_fixp')
ConstantValue__2_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__2_CAST_store_float')
ConstantValue__2_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__2_CAST_store_double')
solver.Add( + (1)*ConstantValue__2_CAST_store_fixp + (1)*ConstantValue__2_CAST_store_float + (1)*ConstantValue__2_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__2_CAST_store_fixbits + (-10000)*ConstantValue__2_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__2_CAST_store')
C2_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__2_CAST_store')
solver.Add( + (1)*ConstantValue__2_fixbits + (-1)*ConstantValue__2_CAST_store_fixbits + (-10000)*C1_ConstantValue__2_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__2_fixbits + (1)*ConstantValue__2_CAST_store_fixbits + (-10000)*C2_ConstantValue__2_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__2_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__2_CAST_store
C3_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__2_CAST_store')
C4_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__2_CAST_store')
C5_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__2_CAST_store')
C6_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__2_CAST_store')
C7_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__2_CAST_store')
C8_ConstantValue__2_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__2_CAST_store')
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_CAST_store_float + (-1)*C3_ConstantValue__2_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_float + (1)*ConstantValue__2_CAST_store_fixp + (-1)*C4_ConstantValue__2_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_CAST_store_double + (-1)*C5_ConstantValue__2_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_double + (1)*ConstantValue__2_CAST_store_fixp + (-1)*C6_ConstantValue__2_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_float + (1)*ConstantValue__2_CAST_store_double + (-1)*C7_ConstantValue__2_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__2_CAST_store
solver.Add( + (1)*ConstantValue__2_double + (1)*ConstantValue__2_CAST_store_float + (-1)*C8_ConstantValue__2_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__2_CAST_store
solver.Add( + (1)*main_y_fixp + (-1)*ConstantValue__2_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_y_float + (-1)*ConstantValue__2_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_y_double + (-1)*ConstantValue__2_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_y_fixbits + (-1)*ConstantValue__2_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for   %conv11 = sitofp i32 %add to double, !taffo.info !26, !taffo.initweight !28
main_conv11_fixbits = solver.IntVar(0, 22, 'main_conv11_fixbits')
main_conv11_fixp = solver.IntVar(0, 1, 'main_conv11_fixp')
main_conv11_float = solver.IntVar(0, 1, 'main_conv11_float')
main_conv11_double = solver.IntVar(0, 1, 'main_conv11_double')
main_conv11_enob = solver.IntVar(-10000, 10000, 'main_conv11_enob')
solver.Add( + (1)*main_conv11_enob + (-1)*main_conv11_fixbits + (10000)*main_conv11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv11_enob + (10000)*main_conv11_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv11_enob + (10000)*main_conv11_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv11_fixbits + (-10000)*main_conv11_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_conv11_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_conv11_enob
solver.Add( + (1)*main_conv11_fixp + (1)*main_conv11_float + (1)*main_conv11_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv11_fixbits + (-10000)*main_conv11_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double %conv11, %conv, !taffo.info !34, !taffo.initweight !27
main_conv11_CAST_div_fixbits = solver.IntVar(0, 22, 'main_conv11_CAST_div_fixbits')
main_conv11_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv11_CAST_div_fixp')
main_conv11_CAST_div_float = solver.IntVar(0, 1, 'main_conv11_CAST_div_float')
main_conv11_CAST_div_double = solver.IntVar(0, 1, 'main_conv11_CAST_div_double')
solver.Add( + (1)*main_conv11_CAST_div_fixp + (1)*main_conv11_CAST_div_float + (1)*main_conv11_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv11_CAST_div_fixbits + (-10000)*main_conv11_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv11_CAST_div = solver.IntVar(0, 1, 'C1_main_conv11_CAST_div')
C2_main_conv11_CAST_div = solver.IntVar(0, 1, 'C2_main_conv11_CAST_div')
solver.Add( + (1)*main_conv11_fixbits + (-1)*main_conv11_CAST_div_fixbits + (-10000)*C1_main_conv11_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv11_fixbits + (1)*main_conv11_CAST_div_fixbits + (-10000)*C2_main_conv11_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv11_CAST_div
castCostObj +=  + (1)*C2_main_conv11_CAST_div
C3_main_conv11_CAST_div = solver.IntVar(0, 1, 'C3_main_conv11_CAST_div')
C4_main_conv11_CAST_div = solver.IntVar(0, 1, 'C4_main_conv11_CAST_div')
C5_main_conv11_CAST_div = solver.IntVar(0, 1, 'C5_main_conv11_CAST_div')
C6_main_conv11_CAST_div = solver.IntVar(0, 1, 'C6_main_conv11_CAST_div')
C7_main_conv11_CAST_div = solver.IntVar(0, 1, 'C7_main_conv11_CAST_div')
C8_main_conv11_CAST_div = solver.IntVar(0, 1, 'C8_main_conv11_CAST_div')
solver.Add( + (1)*main_conv11_fixp + (1)*main_conv11_CAST_div_float + (-1)*C3_main_conv11_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_conv11_CAST_div
solver.Add( + (1)*main_conv11_float + (1)*main_conv11_CAST_div_fixp + (-1)*C4_main_conv11_CAST_div<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_conv11_CAST_div
solver.Add( + (1)*main_conv11_fixp + (1)*main_conv11_CAST_div_double + (-1)*C5_main_conv11_CAST_div<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_conv11_CAST_div
solver.Add( + (1)*main_conv11_double + (1)*main_conv11_CAST_div_fixp + (-1)*C6_main_conv11_CAST_div<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_conv11_CAST_div
solver.Add( + (1)*main_conv11_float + (1)*main_conv11_CAST_div_double + (-1)*C7_main_conv11_CAST_div<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_conv11_CAST_div
solver.Add( + (1)*main_conv11_double + (1)*main_conv11_CAST_div_float + (-1)*C8_main_conv11_CAST_div<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_conv11_CAST_div



#Constraint for cast for   %div = fdiv double %conv11, %conv, !taffo.info !34, !taffo.initweight !27
main_conv_CAST_div_fixbits = solver.IntVar(0, 23, 'main_conv_CAST_div_fixbits')
main_conv_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv_CAST_div_fixp')
main_conv_CAST_div_float = solver.IntVar(0, 1, 'main_conv_CAST_div_float')
main_conv_CAST_div_double = solver.IntVar(0, 1, 'main_conv_CAST_div_double')
solver.Add( + (1)*main_conv_CAST_div_fixp + (1)*main_conv_CAST_div_float + (1)*main_conv_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv_CAST_div_fixbits + (-10000)*main_conv_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv_CAST_div = solver.IntVar(0, 1, 'C1_main_conv_CAST_div')
C2_main_conv_CAST_div = solver.IntVar(0, 1, 'C2_main_conv_CAST_div')
solver.Add( + (1)*main_conv_fixbits + (-1)*main_conv_CAST_div_fixbits + (-10000)*C1_main_conv_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv_fixbits + (1)*main_conv_CAST_div_fixbits + (-10000)*C2_main_conv_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv_CAST_div
castCostObj +=  + (1)*C2_main_conv_CAST_div
C3_main_conv_CAST_div = solver.IntVar(0, 1, 'C3_main_conv_CAST_div')
C4_main_conv_CAST_div = solver.IntVar(0, 1, 'C4_main_conv_CAST_div')
C5_main_conv_CAST_div = solver.IntVar(0, 1, 'C5_main_conv_CAST_div')
C6_main_conv_CAST_div = solver.IntVar(0, 1, 'C6_main_conv_CAST_div')
C7_main_conv_CAST_div = solver.IntVar(0, 1, 'C7_main_conv_CAST_div')
C8_main_conv_CAST_div = solver.IntVar(0, 1, 'C8_main_conv_CAST_div')
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_div_float + (-1)*C3_main_conv_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_conv_CAST_div
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div_fixp + (-1)*C4_main_conv_CAST_div<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_conv_CAST_div
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_CAST_div_double + (-1)*C5_main_conv_CAST_div<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_conv_CAST_div
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div_fixp + (-1)*C6_main_conv_CAST_div<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_conv_CAST_div
solver.Add( + (1)*main_conv_float + (1)*main_conv_CAST_div_double + (-1)*C7_main_conv_CAST_div<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_conv_CAST_div
solver.Add( + (1)*main_conv_double + (1)*main_conv_CAST_div_float + (-1)*C8_main_conv_CAST_div<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_conv_CAST_div



#Stuff for   %div = fdiv double %conv11, %conv, !taffo.info !34, !taffo.initweight !27
main_div_fixbits = solver.IntVar(0, 30, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_div_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv11_CAST_div_fixp + (-1)*main_conv_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv11_CAST_div_float + (-1)*main_conv_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_conv11_CAST_div_double + (-1)*main_conv_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_conv11_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv11_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_conv11_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj =  + (1.61159)*main_div_fixp
mathCostObj +=  + (6)*main_div_float
mathCostObj +=  + (12)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*main_conv_enob + (-10000)*main_main_div_enob_1<=1042)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_conv11_enob + (-10000)*main_main_div_enob_2<=9)    #Enob: propagation in division 2



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
solver.Add( + (1)*ConstantValue__3_double<=0)    #Disable double data type
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
solver.Add( + (1)*ConstantValue__4_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div12 = fdiv double %div, 2.000000e+00, !taffo.info !36, !taffo.initweight !28, !taffo.constinfo !38
main_div_CAST_div12_fixbits = solver.IntVar(0, 30, 'main_div_CAST_div12_fixbits')
main_div_CAST_div12_fixp = solver.IntVar(0, 1, 'main_div_CAST_div12_fixp')
main_div_CAST_div12_float = solver.IntVar(0, 1, 'main_div_CAST_div12_float')
main_div_CAST_div12_double = solver.IntVar(0, 1, 'main_div_CAST_div12_double')
solver.Add( + (1)*main_div_CAST_div12_fixp + (1)*main_div_CAST_div12_float + (1)*main_div_CAST_div12_double==1)    #exactly 1 type
solver.Add( + (1)*main_div_CAST_div12_fixbits + (-10000)*main_div_CAST_div12_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div_CAST_div12 = solver.IntVar(0, 1, 'C1_main_div_CAST_div12')
C2_main_div_CAST_div12 = solver.IntVar(0, 1, 'C2_main_div_CAST_div12')
solver.Add( + (1)*main_div_fixbits + (-1)*main_div_CAST_div12_fixbits + (-10000)*C1_main_div_CAST_div12<=0)    #Shift cost 1
solver.Add( + (-1)*main_div_fixbits + (1)*main_div_CAST_div12_fixbits + (-10000)*C2_main_div_CAST_div12<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div_CAST_div12
castCostObj +=  + (1)*C2_main_div_CAST_div12
C3_main_div_CAST_div12 = solver.IntVar(0, 1, 'C3_main_div_CAST_div12')
C4_main_div_CAST_div12 = solver.IntVar(0, 1, 'C4_main_div_CAST_div12')
C5_main_div_CAST_div12 = solver.IntVar(0, 1, 'C5_main_div_CAST_div12')
C6_main_div_CAST_div12 = solver.IntVar(0, 1, 'C6_main_div_CAST_div12')
C7_main_div_CAST_div12 = solver.IntVar(0, 1, 'C7_main_div_CAST_div12')
C8_main_div_CAST_div12 = solver.IntVar(0, 1, 'C8_main_div_CAST_div12')
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_div12_float + (-1)*C3_main_div_CAST_div12<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div_CAST_div12
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_div12_fixp + (-1)*C4_main_div_CAST_div12<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div_CAST_div12
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_div12_double + (-1)*C5_main_div_CAST_div12<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div_CAST_div12
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_div12_fixp + (-1)*C6_main_div_CAST_div12<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div_CAST_div12
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_div12_double + (-1)*C7_main_div_CAST_div12<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div_CAST_div12
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_div12_float + (-1)*C8_main_div_CAST_div12<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div_CAST_div12



#Stuff for double 2.000000e+00
ConstantValue__5_fixbits = solver.IntVar(0, 30, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__5_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div12 = fdiv double %div, 2.000000e+00, !taffo.info !36, !taffo.initweight !28, !taffo.constinfo !38
ConstantValue__5_CAST_div12_fixbits = solver.IntVar(0, 30, 'ConstantValue__5_CAST_div12_fixbits')
ConstantValue__5_CAST_div12_fixp = solver.IntVar(0, 1, 'ConstantValue__5_CAST_div12_fixp')
ConstantValue__5_CAST_div12_float = solver.IntVar(0, 1, 'ConstantValue__5_CAST_div12_float')
ConstantValue__5_CAST_div12_double = solver.IntVar(0, 1, 'ConstantValue__5_CAST_div12_double')
solver.Add( + (1)*ConstantValue__5_CAST_div12_fixp + (1)*ConstantValue__5_CAST_div12_float + (1)*ConstantValue__5_CAST_div12_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__5_CAST_div12_fixbits + (-10000)*ConstantValue__5_CAST_div12_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C1_ConstantValue__5_CAST_div12')
C2_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C2_ConstantValue__5_CAST_div12')
solver.Add( + (1)*ConstantValue__5_fixbits + (-1)*ConstantValue__5_CAST_div12_fixbits + (-10000)*C1_ConstantValue__5_CAST_div12<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__5_fixbits + (1)*ConstantValue__5_CAST_div12_fixbits + (-10000)*C2_ConstantValue__5_CAST_div12<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__5_CAST_div12
castCostObj +=  + (1)*C2_ConstantValue__5_CAST_div12
C3_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C3_ConstantValue__5_CAST_div12')
C4_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C4_ConstantValue__5_CAST_div12')
C5_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C5_ConstantValue__5_CAST_div12')
C6_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C6_ConstantValue__5_CAST_div12')
C7_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C7_ConstantValue__5_CAST_div12')
C8_ConstantValue__5_CAST_div12 = solver.IntVar(0, 1, 'C8_ConstantValue__5_CAST_div12')
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_CAST_div12_float + (-1)*C3_ConstantValue__5_CAST_div12<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__5_CAST_div12
solver.Add( + (1)*ConstantValue__5_float + (1)*ConstantValue__5_CAST_div12_fixp + (-1)*C4_ConstantValue__5_CAST_div12<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__5_CAST_div12
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_CAST_div12_double + (-1)*C5_ConstantValue__5_CAST_div12<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__5_CAST_div12
solver.Add( + (1)*ConstantValue__5_double + (1)*ConstantValue__5_CAST_div12_fixp + (-1)*C6_ConstantValue__5_CAST_div12<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__5_CAST_div12
solver.Add( + (1)*ConstantValue__5_float + (1)*ConstantValue__5_CAST_div12_double + (-1)*C7_ConstantValue__5_CAST_div12<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__5_CAST_div12
solver.Add( + (1)*ConstantValue__5_double + (1)*ConstantValue__5_CAST_div12_float + (-1)*C8_ConstantValue__5_CAST_div12<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__5_CAST_div12



#Stuff for   %div12 = fdiv double %div, 2.000000e+00, !taffo.info !36, !taffo.initweight !28, !taffo.constinfo !38
main_div12_fixbits = solver.IntVar(0, 30, 'main_div12_fixbits')
main_div12_fixp = solver.IntVar(0, 1, 'main_div12_fixp')
main_div12_float = solver.IntVar(0, 1, 'main_div12_float')
main_div12_double = solver.IntVar(0, 1, 'main_div12_double')
main_div12_enob = solver.IntVar(-10000, 10000, 'main_div12_enob')
solver.Add( + (1)*main_div12_enob + (-1)*main_div12_fixbits + (10000)*main_div12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div12_enob + (10000)*main_div12_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div12_enob + (10000)*main_div12_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div12_fixbits + (-10000)*main_div12_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_div12_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div12_enob
solver.Add( + (1)*main_div12_fixp + (1)*main_div12_float + (1)*main_div12_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div12_fixbits + (-10000)*main_div12_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_div_CAST_div12_fixp + (-1)*ConstantValue__5_CAST_div12_fixp==0)    #fix equality
solver.Add( + (1)*main_div_CAST_div12_float + (-1)*ConstantValue__5_CAST_div12_float==0)    #float equality
solver.Add( + (1)*main_div_CAST_div12_double + (-1)*ConstantValue__5_CAST_div12_double==0)    #double equality
solver.Add( + (1)*main_div_CAST_div12_fixp + (-1)*main_div12_fixp==0)    #fix equality
solver.Add( + (1)*main_div_CAST_div12_float + (-1)*main_div12_float==0)    #float equality
solver.Add( + (1)*main_div_CAST_div12_double + (-1)*main_div12_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div12_fixp
mathCostObj +=  + (6)*main_div12_float
mathCostObj +=  + (12)*main_div12_double
main_main_div12_enob_1 = solver.IntVar(0, 1, 'main_main_div12_enob_1')
main_main_div12_enob_2 = solver.IntVar(0, 1, 'main_main_div12_enob_2')
solver.Add( + (1)*main_main_div12_enob_1 + (1)*main_main_div12_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div12_enob + (-1)*ConstantValue__3_enob + (-10000)*main_main_div12_enob_1<=3072)    #Enob: propagation in division 1
solver.Add( + (1)*main_div12_enob + (-1)*main_div_enob + (-10000)*main_main_div12_enob_2<=3072)    #Enob: propagation in division 2



#Stuff for double 4.000000e+00
ConstantValue__6_fixbits = solver.IntVar(0, 29, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10021)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10050)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__6_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 4.000000e+00
ConstantValue__7_fixbits = solver.IntVar(0, 29, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10021)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10050)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__7_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add13 = fadd double %div12, 4.000000e+00, !taffo.info !14, !taffo.initweight !41, !taffo.constinfo !42
main_div12_CAST_add13_fixbits = solver.IntVar(0, 30, 'main_div12_CAST_add13_fixbits')
main_div12_CAST_add13_fixp = solver.IntVar(0, 1, 'main_div12_CAST_add13_fixp')
main_div12_CAST_add13_float = solver.IntVar(0, 1, 'main_div12_CAST_add13_float')
main_div12_CAST_add13_double = solver.IntVar(0, 1, 'main_div12_CAST_add13_double')
solver.Add( + (1)*main_div12_CAST_add13_fixp + (1)*main_div12_CAST_add13_float + (1)*main_div12_CAST_add13_double==1)    #exactly 1 type
solver.Add( + (1)*main_div12_CAST_add13_fixbits + (-10000)*main_div12_CAST_add13_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C1_main_div12_CAST_add13')
C2_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C2_main_div12_CAST_add13')
solver.Add( + (1)*main_div12_fixbits + (-1)*main_div12_CAST_add13_fixbits + (-10000)*C1_main_div12_CAST_add13<=0)    #Shift cost 1
solver.Add( + (-1)*main_div12_fixbits + (1)*main_div12_CAST_add13_fixbits + (-10000)*C2_main_div12_CAST_add13<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div12_CAST_add13
castCostObj +=  + (1)*C2_main_div12_CAST_add13
C3_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C3_main_div12_CAST_add13')
C4_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C4_main_div12_CAST_add13')
C5_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C5_main_div12_CAST_add13')
C6_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C6_main_div12_CAST_add13')
C7_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C7_main_div12_CAST_add13')
C8_main_div12_CAST_add13 = solver.IntVar(0, 1, 'C8_main_div12_CAST_add13')
solver.Add( + (1)*main_div12_fixp + (1)*main_div12_CAST_add13_float + (-1)*C3_main_div12_CAST_add13<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div12_CAST_add13
solver.Add( + (1)*main_div12_float + (1)*main_div12_CAST_add13_fixp + (-1)*C4_main_div12_CAST_add13<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div12_CAST_add13
solver.Add( + (1)*main_div12_fixp + (1)*main_div12_CAST_add13_double + (-1)*C5_main_div12_CAST_add13<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div12_CAST_add13
solver.Add( + (1)*main_div12_double + (1)*main_div12_CAST_add13_fixp + (-1)*C6_main_div12_CAST_add13<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div12_CAST_add13
solver.Add( + (1)*main_div12_float + (1)*main_div12_CAST_add13_double + (-1)*C7_main_div12_CAST_add13<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div12_CAST_add13
solver.Add( + (1)*main_div12_double + (1)*main_div12_CAST_add13_float + (-1)*C8_main_div12_CAST_add13<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div12_CAST_add13



#Stuff for double 4.000000e+00
ConstantValue__8_fixbits = solver.IntVar(0, 29, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10021)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=10050)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__8_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add13 = fadd double %div12, 4.000000e+00, !taffo.info !14, !taffo.initweight !41, !taffo.constinfo !42
ConstantValue__8_CAST_add13_fixbits = solver.IntVar(0, 29, 'ConstantValue__8_CAST_add13_fixbits')
ConstantValue__8_CAST_add13_fixp = solver.IntVar(0, 1, 'ConstantValue__8_CAST_add13_fixp')
ConstantValue__8_CAST_add13_float = solver.IntVar(0, 1, 'ConstantValue__8_CAST_add13_float')
ConstantValue__8_CAST_add13_double = solver.IntVar(0, 1, 'ConstantValue__8_CAST_add13_double')
solver.Add( + (1)*ConstantValue__8_CAST_add13_fixp + (1)*ConstantValue__8_CAST_add13_float + (1)*ConstantValue__8_CAST_add13_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__8_CAST_add13_fixbits + (-10000)*ConstantValue__8_CAST_add13_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C1_ConstantValue__8_CAST_add13')
C2_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C2_ConstantValue__8_CAST_add13')
solver.Add( + (1)*ConstantValue__8_fixbits + (-1)*ConstantValue__8_CAST_add13_fixbits + (-10000)*C1_ConstantValue__8_CAST_add13<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__8_fixbits + (1)*ConstantValue__8_CAST_add13_fixbits + (-10000)*C2_ConstantValue__8_CAST_add13<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__8_CAST_add13
castCostObj +=  + (1)*C2_ConstantValue__8_CAST_add13
C3_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C3_ConstantValue__8_CAST_add13')
C4_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C4_ConstantValue__8_CAST_add13')
C5_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C5_ConstantValue__8_CAST_add13')
C6_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C6_ConstantValue__8_CAST_add13')
C7_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C7_ConstantValue__8_CAST_add13')
C8_ConstantValue__8_CAST_add13 = solver.IntVar(0, 1, 'C8_ConstantValue__8_CAST_add13')
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_add13_float + (-1)*C3_ConstantValue__8_CAST_add13<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__8_CAST_add13
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_add13_fixp + (-1)*C4_ConstantValue__8_CAST_add13<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__8_CAST_add13
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_add13_double + (-1)*C5_ConstantValue__8_CAST_add13<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__8_CAST_add13
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_add13_fixp + (-1)*C6_ConstantValue__8_CAST_add13<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__8_CAST_add13
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_add13_double + (-1)*C7_ConstantValue__8_CAST_add13<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__8_CAST_add13
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_add13_float + (-1)*C8_ConstantValue__8_CAST_add13<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__8_CAST_add13



#Stuff for   %add13 = fadd double %div12, 4.000000e+00, !taffo.info !14, !taffo.initweight !41, !taffo.constinfo !42
main_add13_fixbits = solver.IntVar(0, 29, 'main_add13_fixbits')
main_add13_fixp = solver.IntVar(0, 1, 'main_add13_fixp')
main_add13_float = solver.IntVar(0, 1, 'main_add13_float')
main_add13_double = solver.IntVar(0, 1, 'main_add13_double')
main_add13_enob = solver.IntVar(-10000, 10000, 'main_add13_enob')
solver.Add( + (1)*main_add13_enob + (-1)*main_add13_fixbits + (10000)*main_add13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add13_enob + (10000)*main_add13_float<=10022)    #Enob constraint for float
solver.Add( + (1)*main_add13_enob + (10000)*main_add13_double<=10051)    #Enob constraint for double
solver.Add( + (1)*main_add13_fixbits + (-10000)*main_add13_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_add13_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add13_enob
solver.Add( + (1)*main_add13_fixp + (1)*main_add13_float + (1)*main_add13_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add13_fixbits + (-10000)*main_add13_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_div12_CAST_add13_fixp + (-1)*ConstantValue__8_CAST_add13_fixp==0)    #fix equality
solver.Add( + (1)*main_div12_CAST_add13_float + (-1)*ConstantValue__8_CAST_add13_float==0)    #float equality
solver.Add( + (1)*main_div12_CAST_add13_double + (-1)*ConstantValue__8_CAST_add13_double==0)    #double equality
solver.Add( + (1)*main_div12_CAST_add13_fixbits + (-1)*ConstantValue__8_CAST_add13_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_div12_CAST_add13_fixp + (-1)*main_add13_fixp==0)    #fix equality
solver.Add( + (1)*main_div12_CAST_add13_float + (-1)*main_add13_float==0)    #float equality
solver.Add( + (1)*main_div12_CAST_add13_double + (-1)*main_add13_double==0)    #double equality
solver.Add( + (1)*main_div12_CAST_add13_fixbits + (-1)*main_add13_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add13_fixp
mathCostObj +=  + (3)*main_add13_float
mathCostObj +=  + (6.64928)*main_add13_double
solver.Add( + (1)*main_add13_enob + (-1)*main_div12_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add13_enob + (-1)*ConstantValue__6_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add13, double* %arrayidx15, align 8, !taffo.info !29, !taffo.initweight !27
main_add13_CAST_store_fixbits = solver.IntVar(0, 29, 'main_add13_CAST_store_fixbits')
main_add13_CAST_store_fixp = solver.IntVar(0, 1, 'main_add13_CAST_store_fixp')
main_add13_CAST_store_float = solver.IntVar(0, 1, 'main_add13_CAST_store_float')
main_add13_CAST_store_double = solver.IntVar(0, 1, 'main_add13_CAST_store_double')
solver.Add( + (1)*main_add13_CAST_store_fixp + (1)*main_add13_CAST_store_float + (1)*main_add13_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add13_CAST_store_fixbits + (-10000)*main_add13_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add13_CAST_store = solver.IntVar(0, 1, 'C1_main_add13_CAST_store')
C2_main_add13_CAST_store = solver.IntVar(0, 1, 'C2_main_add13_CAST_store')
solver.Add( + (1)*main_add13_fixbits + (-1)*main_add13_CAST_store_fixbits + (-10000)*C1_main_add13_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add13_fixbits + (1)*main_add13_CAST_store_fixbits + (-10000)*C2_main_add13_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add13_CAST_store
castCostObj +=  + (1)*C2_main_add13_CAST_store
C3_main_add13_CAST_store = solver.IntVar(0, 1, 'C3_main_add13_CAST_store')
C4_main_add13_CAST_store = solver.IntVar(0, 1, 'C4_main_add13_CAST_store')
C5_main_add13_CAST_store = solver.IntVar(0, 1, 'C5_main_add13_CAST_store')
C6_main_add13_CAST_store = solver.IntVar(0, 1, 'C6_main_add13_CAST_store')
C7_main_add13_CAST_store = solver.IntVar(0, 1, 'C7_main_add13_CAST_store')
C8_main_add13_CAST_store = solver.IntVar(0, 1, 'C8_main_add13_CAST_store')
solver.Add( + (1)*main_add13_fixp + (1)*main_add13_CAST_store_float + (-1)*C3_main_add13_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add13_CAST_store
solver.Add( + (1)*main_add13_float + (1)*main_add13_CAST_store_fixp + (-1)*C4_main_add13_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add13_CAST_store
solver.Add( + (1)*main_add13_fixp + (1)*main_add13_CAST_store_double + (-1)*C5_main_add13_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add13_CAST_store
solver.Add( + (1)*main_add13_double + (1)*main_add13_CAST_store_fixp + (-1)*C6_main_add13_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add13_CAST_store
solver.Add( + (1)*main_add13_float + (1)*main_add13_CAST_store_double + (-1)*C7_main_add13_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add13_CAST_store
solver.Add( + (1)*main_add13_double + (1)*main_add13_CAST_store_float + (-1)*C8_main_add13_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add13_CAST_store
solver.Add( + (1)*main_b_fixp + (-1)*main_add13_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_b_float + (-1)*main_add13_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_b_double + (-1)*main_add13_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_b_fixbits + (-1)*main_add13_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_b_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_b_enob_storeENOB')
solver.Add( + (1)*main_b_enob_storeENOB + (-1)*main_b_fixbits + (10000)*main_b_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_b_enob_storeENOB + (10000)*main_b_float<=10022)    #Enob constraint for float
solver.Add( + (1)*main_b_enob_storeENOB + (10000)*main_b_double<=10051)    #Enob constraint for double
solver.Add( + (1)*main_b_enob_storeENOB + (-1)*main_add13_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv24 = sitofp i32 %rem to double, !taffo.info !26, !taffo.initweight !41
main_conv24_fixbits = solver.IntVar(0, 22, 'main_conv24_fixbits')
main_conv24_fixp = solver.IntVar(0, 1, 'main_conv24_fixp')
main_conv24_float = solver.IntVar(0, 1, 'main_conv24_float')
main_conv24_double = solver.IntVar(0, 1, 'main_conv24_double')
main_conv24_enob = solver.IntVar(-10000, 10000, 'main_conv24_enob')
solver.Add( + (1)*main_conv24_enob + (-1)*main_conv24_fixbits + (10000)*main_conv24_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv24_enob + (10000)*main_conv24_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv24_enob + (10000)*main_conv24_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv24_fixbits + (-10000)*main_conv24_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_conv24_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_conv24_enob
solver.Add( + (1)*main_conv24_fixp + (1)*main_conv24_float + (1)*main_conv24_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv24_fixbits + (-10000)*main_conv24_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv25 = sitofp i32 400 to double, !taffo.info !22
main_conv25_fixbits = solver.IntVar(0, 23, 'main_conv25_fixbits')
main_conv25_fixp = solver.IntVar(0, 1, 'main_conv25_fixp')
main_conv25_float = solver.IntVar(0, 1, 'main_conv25_float')
main_conv25_double = solver.IntVar(0, 1, 'main_conv25_double')
main_conv25_enob = solver.IntVar(-10000, 10000, 'main_conv25_enob')
solver.Add( + (1)*main_conv25_enob + (-1)*main_conv25_fixbits + (10000)*main_conv25_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv25_enob + (10000)*main_conv25_float<=10015)    #Enob constraint for float
solver.Add( + (1)*main_conv25_enob + (10000)*main_conv25_double<=10044)    #Enob constraint for double
solver.Add( + (1)*main_conv25_fixbits + (-10000)*main_conv25_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_conv25_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_conv25_enob
solver.Add( + (1)*main_conv25_fixp + (1)*main_conv25_float + (1)*main_conv25_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv25_fixbits + (-10000)*main_conv25_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__9_fixbits = solver.IntVar(0, 31, 'ConstantValue__9_fixbits')
ConstantValue__9_fixp = solver.IntVar(0, 1, 'ConstantValue__9_fixp')
ConstantValue__9_float = solver.IntVar(0, 1, 'ConstantValue__9_float')
ConstantValue__9_double = solver.IntVar(0, 1, 'ConstantValue__9_double')
ConstantValue__9_enob = solver.IntVar(-10000, 10000, 'ConstantValue__9_enob')
solver.Add( + (1)*ConstantValue__9_enob + (-1)*ConstantValue__9_fixbits + (10000)*ConstantValue__9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__9_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_float + (1)*ConstantValue__9_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__10_fixbits = solver.IntVar(0, 31, 'ConstantValue__10_fixbits')
ConstantValue__10_fixp = solver.IntVar(0, 1, 'ConstantValue__10_fixp')
ConstantValue__10_float = solver.IntVar(0, 1, 'ConstantValue__10_float')
ConstantValue__10_double = solver.IntVar(0, 1, 'ConstantValue__10_double')
ConstantValue__10_enob = solver.IntVar(-10000, 10000, 'ConstantValue__10_enob')
solver.Add( + (1)*ConstantValue__10_enob + (-1)*ConstantValue__10_fixbits + (10000)*ConstantValue__10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__10_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_float + (1)*ConstantValue__10_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp<=0)    #If not fix, frac part to zero



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
solver.Add( + (1)*ConstantValue__11_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_float + (1)*ConstantValue__11_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp<=0)    #If not fix, frac part to zero



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
solver.Add( + (1)*ConstantValue__12_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx43, align 8, !taffo.info !11, !taffo.initweight !28, !taffo.constinfo !30
ConstantValue__12_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__12_CAST_store_fixbits')
ConstantValue__12_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__12_CAST_store_fixp')
ConstantValue__12_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__12_CAST_store_float')
ConstantValue__12_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__12_CAST_store_double')
solver.Add( + (1)*ConstantValue__12_CAST_store_fixp + (1)*ConstantValue__12_CAST_store_float + (1)*ConstantValue__12_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__12_CAST_store_fixbits + (-10000)*ConstantValue__12_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__12_CAST_store')
C2_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__12_CAST_store')
solver.Add( + (1)*ConstantValue__12_fixbits + (-1)*ConstantValue__12_CAST_store_fixbits + (-10000)*C1_ConstantValue__12_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__12_fixbits + (1)*ConstantValue__12_CAST_store_fixbits + (-10000)*C2_ConstantValue__12_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__12_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__12_CAST_store
C3_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__12_CAST_store')
C4_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__12_CAST_store')
C5_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__12_CAST_store')
C6_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__12_CAST_store')
C7_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__12_CAST_store')
C8_ConstantValue__12_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__12_CAST_store')
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_store_float + (-1)*C3_ConstantValue__12_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_store_fixp + (-1)*C4_ConstantValue__12_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_CAST_store_double + (-1)*C5_ConstantValue__12_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_store_fixp + (-1)*C6_ConstantValue__12_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_float + (1)*ConstantValue__12_CAST_store_double + (-1)*C7_ConstantValue__12_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__12_CAST_store
solver.Add( + (1)*ConstantValue__12_double + (1)*ConstantValue__12_CAST_store_float + (-1)*C8_ConstantValue__12_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__12_CAST_store
solver.Add( + (1)*main_A_fixp + (-1)*ConstantValue__12_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_A_float + (-1)*ConstantValue__12_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_A_double + (-1)*ConstantValue__12_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_A_fixbits + (-1)*ConstantValue__12_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 1.000000e+00
ConstantValue__13_fixbits = solver.IntVar(0, 31, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__13_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_float + (1)*ConstantValue__13_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__14_fixbits = solver.IntVar(0, 31, 'ConstantValue__14_fixbits')
ConstantValue__14_fixp = solver.IntVar(0, 1, 'ConstantValue__14_fixp')
ConstantValue__14_float = solver.IntVar(0, 1, 'ConstantValue__14_float')
ConstantValue__14_double = solver.IntVar(0, 1, 'ConstantValue__14_double')
ConstantValue__14_enob = solver.IntVar(-10000, 10000, 'ConstantValue__14_enob')
solver.Add( + (1)*ConstantValue__14_enob + (-1)*ConstantValue__14_fixbits + (10000)*ConstantValue__14_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__14_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_float + (1)*ConstantValue__14_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx50, align 8, !taffo.info !11, !taffo.initweight !28, !taffo.constinfo !55
ConstantValue__14_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__14_CAST_store_fixbits')
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
castCostObj +=  + (6.25227)*C3_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_store_fixp + (-1)*C4_ConstantValue__14_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_store_double + (-1)*C5_ConstantValue__14_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_store_fixp + (-1)*C6_ConstantValue__14_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_store_double + (-1)*C7_ConstantValue__14_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__14_CAST_store
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_store_float + (-1)*C8_ConstantValue__14_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__14_CAST_store
solver.Add( + (1)*main_A_fixp + (-1)*ConstantValue__14_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_A_float + (-1)*ConstantValue__14_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_A_double + (-1)*ConstantValue__14_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_A_fixbits + (-1)*ConstantValue__14_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



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
solver.Add( + (1)*ConstantValue__15_double<=0)    #Disable double data type
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
solver.Add( + (1)*ConstantValue__16_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx66, align 8, !taffo.info !29, !taffo.initweight !28, !taffo.constinfo !30
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
castCostObj +=  + (6.25227)*C3_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_store_fixp + (-1)*C4_ConstantValue__16_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_store_double + (-1)*C5_ConstantValue__16_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_store_fixp + (-1)*C6_ConstantValue__16_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_store_double + (-1)*C7_ConstantValue__16_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__16_CAST_store
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_store_float + (-1)*C8_ConstantValue__16_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__16_CAST_store
solver.Add( + (1)*main_B_fixp + (-1)*ConstantValue__16_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_B_float + (-1)*ConstantValue__16_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_B_double + (-1)*ConstantValue__16_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_B_fixbits + (-1)*ConstantValue__16_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp')
solver.Add( + (1)*main_A_enob_memphi_main_tmp + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
solver.Add( + (1)*main_main_tmp_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp1')
solver.Add( + (1)*main_A_enob_memphi_main_tmp1 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
solver.Add( + (1)*main_main_tmp1_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp1 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !69, !taffo.initweight !41
main_A_CAST_mul_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul_fixbits')
main_A_CAST_mul_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul_fixp')
main_A_CAST_mul_float = solver.IntVar(0, 1, 'main_A_CAST_mul_float')
main_A_CAST_mul_double = solver.IntVar(0, 1, 'main_A_CAST_mul_double')
solver.Add( + (1)*main_A_CAST_mul_fixp + (1)*main_A_CAST_mul_float + (1)*main_A_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul_fixbits + (-10000)*main_A_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul = solver.IntVar(0, 1, 'C1_main_A_CAST_mul')
C2_main_A_CAST_mul = solver.IntVar(0, 1, 'C2_main_A_CAST_mul')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul_fixbits + (-10000)*C1_main_A_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul_fixbits + (-10000)*C2_main_A_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul
castCostObj +=  + (1)*C2_main_A_CAST_mul
C3_main_A_CAST_mul = solver.IntVar(0, 1, 'C3_main_A_CAST_mul')
C4_main_A_CAST_mul = solver.IntVar(0, 1, 'C4_main_A_CAST_mul')
C5_main_A_CAST_mul = solver.IntVar(0, 1, 'C5_main_A_CAST_mul')
C6_main_A_CAST_mul = solver.IntVar(0, 1, 'C6_main_A_CAST_mul')
C7_main_A_CAST_mul = solver.IntVar(0, 1, 'C7_main_A_CAST_mul')
C8_main_A_CAST_mul = solver.IntVar(0, 1, 'C8_main_A_CAST_mul')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul_float + (-1)*C3_main_A_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul_fixp + (-1)*C4_main_A_CAST_mul<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul_double + (-1)*C5_main_A_CAST_mul<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul_fixp + (-1)*C6_main_A_CAST_mul<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul_double + (-1)*C7_main_A_CAST_mul<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul_float + (-1)*C8_main_A_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !69, !taffo.initweight !41
main_A_CAST_mul_0_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul_0_fixbits')
main_A_CAST_mul_0_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul_0_fixp')
main_A_CAST_mul_0_float = solver.IntVar(0, 1, 'main_A_CAST_mul_0_float')
main_A_CAST_mul_0_double = solver.IntVar(0, 1, 'main_A_CAST_mul_0_double')
solver.Add( + (1)*main_A_CAST_mul_0_fixp + (1)*main_A_CAST_mul_0_float + (1)*main_A_CAST_mul_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul_0_fixbits + (-10000)*main_A_CAST_mul_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul_0')
C2_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul_0')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul_0_fixbits + (-10000)*C1_main_A_CAST_mul_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul_0_fixbits + (-10000)*C2_main_A_CAST_mul_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul_0
castCostObj +=  + (1)*C2_main_A_CAST_mul_0
C3_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul_0')
C4_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul_0')
C5_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul_0')
C6_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul_0')
C7_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul_0')
C8_main_A_CAST_mul_0 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul_0')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul_0_float + (-1)*C3_main_A_CAST_mul_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul_0_fixp + (-1)*C4_main_A_CAST_mul_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul_0
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul_0_double + (-1)*C5_main_A_CAST_mul_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul_0_fixp + (-1)*C6_main_A_CAST_mul_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul_0_double + (-1)*C7_main_A_CAST_mul_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul_0_float + (-1)*C8_main_A_CAST_mul_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul_0



#Stuff for   %mul = fmul double %tmp, %tmp1, !taffo.info !69, !taffo.initweight !41
main_mul_fixbits = solver.IntVar(0, 28, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_mul_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul_enob
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul_fixp + (-1)*main_A_CAST_mul_0_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul_float + (-1)*main_A_CAST_mul_0_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul_double + (-1)*main_A_CAST_mul_0_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul_double + (-1)*main_mul_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul_fixp
mathCostObj +=  + (6)*main_mul_float
mathCostObj +=  + (12.2551)*main_mul_double
main_main_mul_enob_1 = solver.IntVar(0, 1, 'main_main_mul_enob_1')
main_main_mul_enob_2 = solver.IntVar(0, 1, 'main_main_mul_enob_2')
solver.Add( + (1)*main_main_mul_enob_1 + (1)*main_main_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul_enob + (-1)*main_A_enob_memphi_main_tmp1 + (-10000)*main_main_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul_enob + (-1)*main_A_enob_memphi_main_tmp + (-10000)*main_main_mul_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_B_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_B_enob_memphi_main_tmp2')
solver.Add( + (1)*main_B_enob_memphi_main_tmp2 + (-1)*main_B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
main_main_tmp2_enob_4 = solver.IntVar(0, 1, 'main_main_tmp2_enob_4')
solver.Add( + (1)*main_main_tmp2_enob_1 + (1)*main_main_tmp2_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp2 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add97 = fadd double %tmp2, %mul, !taffo.info !19, !taffo.initweight !41
main_B_CAST_add97_fixbits = solver.IntVar(0, 22, 'main_B_CAST_add97_fixbits')
main_B_CAST_add97_fixp = solver.IntVar(0, 1, 'main_B_CAST_add97_fixp')
main_B_CAST_add97_float = solver.IntVar(0, 1, 'main_B_CAST_add97_float')
main_B_CAST_add97_double = solver.IntVar(0, 1, 'main_B_CAST_add97_double')
solver.Add( + (1)*main_B_CAST_add97_fixp + (1)*main_B_CAST_add97_float + (1)*main_B_CAST_add97_double==1)    #exactly 1 type
solver.Add( + (1)*main_B_CAST_add97_fixbits + (-10000)*main_B_CAST_add97_fixp<=0)    #If no fix, fix frac part = 0
C1_main_B_CAST_add97 = solver.IntVar(0, 1, 'C1_main_B_CAST_add97')
C2_main_B_CAST_add97 = solver.IntVar(0, 1, 'C2_main_B_CAST_add97')
solver.Add( + (1)*main_B_fixbits + (-1)*main_B_CAST_add97_fixbits + (-10000)*C1_main_B_CAST_add97<=0)    #Shift cost 1
solver.Add( + (-1)*main_B_fixbits + (1)*main_B_CAST_add97_fixbits + (-10000)*C2_main_B_CAST_add97<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_B_CAST_add97
castCostObj +=  + (1)*C2_main_B_CAST_add97
C3_main_B_CAST_add97 = solver.IntVar(0, 1, 'C3_main_B_CAST_add97')
C4_main_B_CAST_add97 = solver.IntVar(0, 1, 'C4_main_B_CAST_add97')
C5_main_B_CAST_add97 = solver.IntVar(0, 1, 'C5_main_B_CAST_add97')
C6_main_B_CAST_add97 = solver.IntVar(0, 1, 'C6_main_B_CAST_add97')
C7_main_B_CAST_add97 = solver.IntVar(0, 1, 'C7_main_B_CAST_add97')
C8_main_B_CAST_add97 = solver.IntVar(0, 1, 'C8_main_B_CAST_add97')
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_add97_float + (-1)*C3_main_B_CAST_add97<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_B_CAST_add97
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_add97_fixp + (-1)*C4_main_B_CAST_add97<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_B_CAST_add97
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_add97_double + (-1)*C5_main_B_CAST_add97<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_B_CAST_add97
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_add97_fixp + (-1)*C6_main_B_CAST_add97<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_B_CAST_add97
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_add97_double + (-1)*C7_main_B_CAST_add97<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_B_CAST_add97
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_add97_float + (-1)*C8_main_B_CAST_add97<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_B_CAST_add97



#Constraint for cast for   %add97 = fadd double %tmp2, %mul, !taffo.info !19, !taffo.initweight !41
main_mul_CAST_add97_fixbits = solver.IntVar(0, 28, 'main_mul_CAST_add97_fixbits')
main_mul_CAST_add97_fixp = solver.IntVar(0, 1, 'main_mul_CAST_add97_fixp')
main_mul_CAST_add97_float = solver.IntVar(0, 1, 'main_mul_CAST_add97_float')
main_mul_CAST_add97_double = solver.IntVar(0, 1, 'main_mul_CAST_add97_double')
solver.Add( + (1)*main_mul_CAST_add97_fixp + (1)*main_mul_CAST_add97_float + (1)*main_mul_CAST_add97_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul_CAST_add97_fixbits + (-10000)*main_mul_CAST_add97_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C1_main_mul_CAST_add97')
C2_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C2_main_mul_CAST_add97')
solver.Add( + (1)*main_mul_fixbits + (-1)*main_mul_CAST_add97_fixbits + (-10000)*C1_main_mul_CAST_add97<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul_fixbits + (1)*main_mul_CAST_add97_fixbits + (-10000)*C2_main_mul_CAST_add97<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul_CAST_add97
castCostObj +=  + (1)*C2_main_mul_CAST_add97
C3_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C3_main_mul_CAST_add97')
C4_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C4_main_mul_CAST_add97')
C5_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C5_main_mul_CAST_add97')
C6_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C6_main_mul_CAST_add97')
C7_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C7_main_mul_CAST_add97')
C8_main_mul_CAST_add97 = solver.IntVar(0, 1, 'C8_main_mul_CAST_add97')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_add97_float + (-1)*C3_main_mul_CAST_add97<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul_CAST_add97
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_add97_fixp + (-1)*C4_main_mul_CAST_add97<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul_CAST_add97
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_add97_double + (-1)*C5_main_mul_CAST_add97<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul_CAST_add97
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_add97_fixp + (-1)*C6_main_mul_CAST_add97<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul_CAST_add97
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_add97_double + (-1)*C7_main_mul_CAST_add97<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul_CAST_add97
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_add97_float + (-1)*C8_main_mul_CAST_add97<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul_CAST_add97



#Stuff for   %add97 = fadd double %tmp2, %mul, !taffo.info !19, !taffo.initweight !41
main_add97_fixbits = solver.IntVar(0, 22, 'main_add97_fixbits')
main_add97_fixp = solver.IntVar(0, 1, 'main_add97_fixp')
main_add97_float = solver.IntVar(0, 1, 'main_add97_float')
main_add97_double = solver.IntVar(0, 1, 'main_add97_double')
main_add97_enob = solver.IntVar(-10000, 10000, 'main_add97_enob')
solver.Add( + (1)*main_add97_enob + (-1)*main_add97_fixbits + (10000)*main_add97_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add97_enob + (10000)*main_add97_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add97_enob + (10000)*main_add97_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add97_fixbits + (-10000)*main_add97_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_add97_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add97_enob
solver.Add( + (1)*main_add97_fixp + (1)*main_add97_float + (1)*main_add97_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add97_fixbits + (-10000)*main_add97_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_B_CAST_add97_fixp + (-1)*main_mul_CAST_add97_fixp==0)    #fix equality
solver.Add( + (1)*main_B_CAST_add97_float + (-1)*main_mul_CAST_add97_float==0)    #float equality
solver.Add( + (1)*main_B_CAST_add97_double + (-1)*main_mul_CAST_add97_double==0)    #double equality
solver.Add( + (1)*main_B_CAST_add97_fixbits + (-1)*main_mul_CAST_add97_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_B_CAST_add97_fixp + (-1)*main_add97_fixp==0)    #fix equality
solver.Add( + (1)*main_B_CAST_add97_float + (-1)*main_add97_float==0)    #float equality
solver.Add( + (1)*main_B_CAST_add97_double + (-1)*main_add97_double==0)    #double equality
solver.Add( + (1)*main_B_CAST_add97_fixbits + (-1)*main_add97_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add97_fixp
mathCostObj +=  + (3)*main_add97_float
mathCostObj +=  + (6.64928)*main_add97_double
solver.Add( + (1)*main_add97_enob + (-1)*main_B_enob_memphi_main_tmp2<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add97_enob + (-1)*main_mul_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add97, double* %arrayidx96, align 8, !taffo.info !29, !taffo.initweight !28
main_add97_CAST_store_fixbits = solver.IntVar(0, 22, 'main_add97_CAST_store_fixbits')
main_add97_CAST_store_fixp = solver.IntVar(0, 1, 'main_add97_CAST_store_fixp')
main_add97_CAST_store_float = solver.IntVar(0, 1, 'main_add97_CAST_store_float')
main_add97_CAST_store_double = solver.IntVar(0, 1, 'main_add97_CAST_store_double')
solver.Add( + (1)*main_add97_CAST_store_fixp + (1)*main_add97_CAST_store_float + (1)*main_add97_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add97_CAST_store_fixbits + (-10000)*main_add97_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add97_CAST_store = solver.IntVar(0, 1, 'C1_main_add97_CAST_store')
C2_main_add97_CAST_store = solver.IntVar(0, 1, 'C2_main_add97_CAST_store')
solver.Add( + (1)*main_add97_fixbits + (-1)*main_add97_CAST_store_fixbits + (-10000)*C1_main_add97_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add97_fixbits + (1)*main_add97_CAST_store_fixbits + (-10000)*C2_main_add97_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add97_CAST_store
castCostObj +=  + (1)*C2_main_add97_CAST_store
C3_main_add97_CAST_store = solver.IntVar(0, 1, 'C3_main_add97_CAST_store')
C4_main_add97_CAST_store = solver.IntVar(0, 1, 'C4_main_add97_CAST_store')
C5_main_add97_CAST_store = solver.IntVar(0, 1, 'C5_main_add97_CAST_store')
C6_main_add97_CAST_store = solver.IntVar(0, 1, 'C6_main_add97_CAST_store')
C7_main_add97_CAST_store = solver.IntVar(0, 1, 'C7_main_add97_CAST_store')
C8_main_add97_CAST_store = solver.IntVar(0, 1, 'C8_main_add97_CAST_store')
solver.Add( + (1)*main_add97_fixp + (1)*main_add97_CAST_store_float + (-1)*C3_main_add97_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add97_CAST_store
solver.Add( + (1)*main_add97_float + (1)*main_add97_CAST_store_fixp + (-1)*C4_main_add97_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add97_CAST_store
solver.Add( + (1)*main_add97_fixp + (1)*main_add97_CAST_store_double + (-1)*C5_main_add97_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add97_CAST_store
solver.Add( + (1)*main_add97_double + (1)*main_add97_CAST_store_fixp + (-1)*C6_main_add97_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add97_CAST_store
solver.Add( + (1)*main_add97_float + (1)*main_add97_CAST_store_double + (-1)*C7_main_add97_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add97_CAST_store
solver.Add( + (1)*main_add97_double + (1)*main_add97_CAST_store_float + (-1)*C8_main_add97_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add97_CAST_store
solver.Add( + (1)*main_B_fixp + (-1)*main_add97_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_B_float + (-1)*main_add97_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_B_double + (-1)*main_add97_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_B_fixbits + (-1)*main_add97_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_B_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_B_enob_storeENOB')
solver.Add( + (1)*main_B_enob_storeENOB + (-1)*main_B_fixbits + (10000)*main_B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_B_enob_storeENOB + (10000)*main_B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_B_enob_storeENOB + (10000)*main_B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_B_enob_storeENOB + (-1)*main_add97_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp2 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp2_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_B_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'main_B_enob_memphi_main_tmp3')
solver.Add( + (1)*main_B_enob_memphi_main_tmp3 + (-1)*main_B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp3 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp3_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_B_enob_memphi_main_tmp3 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp3, double* %arrayidx122, align 8, !taffo.info !11, !taffo.initweight !28
main_B_CAST_store_fixbits = solver.IntVar(0, 22, 'main_B_CAST_store_fixbits')
main_B_CAST_store_fixp = solver.IntVar(0, 1, 'main_B_CAST_store_fixp')
main_B_CAST_store_float = solver.IntVar(0, 1, 'main_B_CAST_store_float')
main_B_CAST_store_double = solver.IntVar(0, 1, 'main_B_CAST_store_double')
solver.Add( + (1)*main_B_CAST_store_fixp + (1)*main_B_CAST_store_float + (1)*main_B_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_B_CAST_store_fixbits + (-10000)*main_B_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_B_CAST_store = solver.IntVar(0, 1, 'C1_main_B_CAST_store')
C2_main_B_CAST_store = solver.IntVar(0, 1, 'C2_main_B_CAST_store')
solver.Add( + (1)*main_B_fixbits + (-1)*main_B_CAST_store_fixbits + (-10000)*C1_main_B_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_B_fixbits + (1)*main_B_CAST_store_fixbits + (-10000)*C2_main_B_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_B_CAST_store
castCostObj +=  + (1)*C2_main_B_CAST_store
C3_main_B_CAST_store = solver.IntVar(0, 1, 'C3_main_B_CAST_store')
C4_main_B_CAST_store = solver.IntVar(0, 1, 'C4_main_B_CAST_store')
C5_main_B_CAST_store = solver.IntVar(0, 1, 'C5_main_B_CAST_store')
C6_main_B_CAST_store = solver.IntVar(0, 1, 'C6_main_B_CAST_store')
C7_main_B_CAST_store = solver.IntVar(0, 1, 'C7_main_B_CAST_store')
C8_main_B_CAST_store = solver.IntVar(0, 1, 'C8_main_B_CAST_store')
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_store_float + (-1)*C3_main_B_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_B_CAST_store
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_store_fixp + (-1)*C4_main_B_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_B_CAST_store
solver.Add( + (1)*main_B_fixp + (1)*main_B_CAST_store_double + (-1)*C5_main_B_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_B_CAST_store
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_store_fixp + (-1)*C6_main_B_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_B_CAST_store
solver.Add( + (1)*main_B_float + (1)*main_B_CAST_store_double + (-1)*C7_main_B_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_B_CAST_store
solver.Add( + (1)*main_B_double + (1)*main_B_CAST_store_float + (-1)*C8_main_B_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_B_CAST_store
solver.Add( + (1)*main_A_fixp + (-1)*main_B_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_A_float + (-1)*main_B_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_A_double + (-1)*main_B_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_A_fixbits + (-1)*main_B_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_A_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_A_enob_storeENOB')
solver.Add( + (1)*main_A_enob_storeENOB + (-1)*main_A_fixbits + (10000)*main_A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_A_enob_storeENOB + (10000)*main_A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_A_enob_storeENOB + (10000)*main_A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_A_enob_storeENOB + (-1)*main_B_enob_memphi_main_tmp3<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp4')
solver.Add( + (1)*main_A_enob_memphi_main_tmp4 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_4 = solver.IntVar(0, 1, 'main_main_tmp4_enob_4')
main_main_tmp4_enob_5 = solver.IntVar(0, 1, 'main_main_tmp4_enob_5')
main_main_tmp4_enob_6 = solver.IntVar(0, 1, 'main_main_tmp4_enob_6')
main_main_tmp4_enob_7 = solver.IntVar(0, 1, 'main_main_tmp4_enob_7')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_4 + (1)*main_main_tmp4_enob_5 + (1)*main_main_tmp4_enob_6 + (1)*main_main_tmp4_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp4 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp4_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp4 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp4_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp4 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp4_enob_5<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %w.0 = phi double [ %tmp4, %for.body137 ], [ %sub155, %for.inc156 ], !taffo.info !75
main_w_0_fixbits = solver.IntVar(0, 29, 'main_w_0_fixbits')
main_w_0_fixp = solver.IntVar(0, 1, 'main_w_0_fixp')
main_w_0_float = solver.IntVar(0, 1, 'main_w_0_float')
main_w_0_double = solver.IntVar(0, 1, 'main_w_0_double')
main_w_0_enob = solver.IntVar(-10000, 10000, 'main_w_0_enob')
solver.Add( + (1)*main_w_0_enob + (-1)*main_w_0_fixbits + (10000)*main_w_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_w_0_enob + (10000)*main_w_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_w_0_enob + (10000)*main_w_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_w_0_fixbits + (-10000)*main_w_0_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_w_0_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_w_0_enob
solver.Add( + (1)*main_w_0_fixp + (1)*main_w_0_float + (1)*main_w_0_double==1)    #Exactly one selected type
solver.Add( + (1)*main_w_0_fixbits + (-10000)*main_w_0_fixp<=0)    #If not fix, frac part to zero
main_main_w_0_enob_0 = solver.IntVar(0, 1, 'main_main_w_0_enob_0')
main_main_w_0_enob_1 = solver.IntVar(0, 1, 'main_main_w_0_enob_1')
solver.Add( + (1)*main_main_w_0_enob_0 + (1)*main_main_w_0_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %w.0 = phi double [ %tmp4, %for.body137 ], [ %sub155, %for.inc156 ], !taffo.info !75
main_A_CAST_w_0_fixbits = solver.IntVar(0, 29, 'main_A_CAST_w_0_fixbits')
main_A_CAST_w_0_fixp = solver.IntVar(0, 1, 'main_A_CAST_w_0_fixp')
main_A_CAST_w_0_float = solver.IntVar(0, 1, 'main_A_CAST_w_0_float')
main_A_CAST_w_0_double = solver.IntVar(0, 1, 'main_A_CAST_w_0_double')
solver.Add( + (1)*main_A_CAST_w_0_fixp + (1)*main_A_CAST_w_0_float + (1)*main_A_CAST_w_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_w_0_fixbits + (-10000)*main_A_CAST_w_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C1_main_A_CAST_w_0')
C2_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C2_main_A_CAST_w_0')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_w_0_fixbits + (-10000)*C1_main_A_CAST_w_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_w_0_fixbits + (-10000)*C2_main_A_CAST_w_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_w_0
castCostObj +=  + (1)*C2_main_A_CAST_w_0
C3_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C3_main_A_CAST_w_0')
C4_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C4_main_A_CAST_w_0')
C5_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C5_main_A_CAST_w_0')
C6_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C6_main_A_CAST_w_0')
C7_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C7_main_A_CAST_w_0')
C8_main_A_CAST_w_0 = solver.IntVar(0, 1, 'C8_main_A_CAST_w_0')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_w_0_float + (-1)*C3_main_A_CAST_w_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_w_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_w_0_fixp + (-1)*C4_main_A_CAST_w_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_w_0
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_w_0_double + (-1)*C5_main_A_CAST_w_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_w_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_w_0_fixp + (-1)*C6_main_A_CAST_w_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_w_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_w_0_double + (-1)*C7_main_A_CAST_w_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_w_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_w_0_float + (-1)*C8_main_A_CAST_w_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_w_0
solver.Add( + (1)*main_w_0_fixp + (-1)*main_A_CAST_w_0_fixp==0)    #fix equality
solver.Add( + (1)*main_w_0_float + (-1)*main_A_CAST_w_0_float==0)    #float equality
solver.Add( + (1)*main_w_0_double + (-1)*main_A_CAST_w_0_double==0)    #double equality
solver.Add( + (1)*main_w_0_fixbits + (-1)*main_A_CAST_w_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_0_enob + (-1)*main_A_enob_memphi_main_tmp4 + (10000)*main_main_w_0_enob_0<=10000)    #Enob: forcing phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp5')
solver.Add( + (1)*main_A_enob_memphi_main_tmp5 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_4 = solver.IntVar(0, 1, 'main_main_tmp5_enob_4')
main_main_tmp5_enob_5 = solver.IntVar(0, 1, 'main_main_tmp5_enob_5')
main_main_tmp5_enob_6 = solver.IntVar(0, 1, 'main_main_tmp5_enob_6')
main_main_tmp5_enob_7 = solver.IntVar(0, 1, 'main_main_tmp5_enob_7')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_4 + (1)*main_main_tmp5_enob_5 + (1)*main_main_tmp5_enob_6 + (1)*main_main_tmp5_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp5 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp5_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp5 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp5_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp5 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp5_enob_5<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp6')
solver.Add( + (1)*main_A_enob_memphi_main_tmp6 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_4 = solver.IntVar(0, 1, 'main_main_tmp6_enob_4')
main_main_tmp6_enob_5 = solver.IntVar(0, 1, 'main_main_tmp6_enob_5')
main_main_tmp6_enob_6 = solver.IntVar(0, 1, 'main_main_tmp6_enob_6')
main_main_tmp6_enob_7 = solver.IntVar(0, 1, 'main_main_tmp6_enob_7')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_4 + (1)*main_main_tmp6_enob_5 + (1)*main_main_tmp6_enob_6 + (1)*main_main_tmp6_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp6 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp6_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp6 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp6_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp6 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp6_enob_5<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul154 = fmul double %tmp5, %tmp6, !taffo.info !69, !taffo.initweight !41
main_A_CAST_mul154_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul154_fixbits')
main_A_CAST_mul154_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul154_fixp')
main_A_CAST_mul154_float = solver.IntVar(0, 1, 'main_A_CAST_mul154_float')
main_A_CAST_mul154_double = solver.IntVar(0, 1, 'main_A_CAST_mul154_double')
solver.Add( + (1)*main_A_CAST_mul154_fixp + (1)*main_A_CAST_mul154_float + (1)*main_A_CAST_mul154_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul154_fixbits + (-10000)*main_A_CAST_mul154_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul154')
C2_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul154')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul154_fixbits + (-10000)*C1_main_A_CAST_mul154<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul154_fixbits + (-10000)*C2_main_A_CAST_mul154<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul154
castCostObj +=  + (1)*C2_main_A_CAST_mul154
C3_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul154')
C4_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul154')
C5_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul154')
C6_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul154')
C7_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul154')
C8_main_A_CAST_mul154 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul154')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul154_float + (-1)*C3_main_A_CAST_mul154<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul154
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul154_fixp + (-1)*C4_main_A_CAST_mul154<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul154
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul154_double + (-1)*C5_main_A_CAST_mul154<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul154
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul154_fixp + (-1)*C6_main_A_CAST_mul154<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul154
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul154_double + (-1)*C7_main_A_CAST_mul154<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul154
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul154_float + (-1)*C8_main_A_CAST_mul154<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul154



#Constraint for cast for   %mul154 = fmul double %tmp5, %tmp6, !taffo.info !69, !taffo.initweight !41
main_A_CAST_mul154_0_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul154_0_fixbits')
main_A_CAST_mul154_0_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul154_0_fixp')
main_A_CAST_mul154_0_float = solver.IntVar(0, 1, 'main_A_CAST_mul154_0_float')
main_A_CAST_mul154_0_double = solver.IntVar(0, 1, 'main_A_CAST_mul154_0_double')
solver.Add( + (1)*main_A_CAST_mul154_0_fixp + (1)*main_A_CAST_mul154_0_float + (1)*main_A_CAST_mul154_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul154_0_fixbits + (-10000)*main_A_CAST_mul154_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul154_0')
C2_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul154_0')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul154_0_fixbits + (-10000)*C1_main_A_CAST_mul154_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul154_0_fixbits + (-10000)*C2_main_A_CAST_mul154_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul154_0
castCostObj +=  + (1)*C2_main_A_CAST_mul154_0
C3_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul154_0')
C4_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul154_0')
C5_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul154_0')
C6_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul154_0')
C7_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul154_0')
C8_main_A_CAST_mul154_0 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul154_0')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul154_0_float + (-1)*C3_main_A_CAST_mul154_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul154_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul154_0_fixp + (-1)*C4_main_A_CAST_mul154_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul154_0
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul154_0_double + (-1)*C5_main_A_CAST_mul154_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul154_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul154_0_fixp + (-1)*C6_main_A_CAST_mul154_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul154_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul154_0_double + (-1)*C7_main_A_CAST_mul154_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul154_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul154_0_float + (-1)*C8_main_A_CAST_mul154_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul154_0



#Stuff for   %mul154 = fmul double %tmp5, %tmp6, !taffo.info !69, !taffo.initweight !41
main_mul154_fixbits = solver.IntVar(0, 28, 'main_mul154_fixbits')
main_mul154_fixp = solver.IntVar(0, 1, 'main_mul154_fixp')
main_mul154_float = solver.IntVar(0, 1, 'main_mul154_float')
main_mul154_double = solver.IntVar(0, 1, 'main_mul154_double')
main_mul154_enob = solver.IntVar(-10000, 10000, 'main_mul154_enob')
solver.Add( + (1)*main_mul154_enob + (-1)*main_mul154_fixbits + (10000)*main_mul154_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul154_enob + (10000)*main_mul154_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul154_enob + (10000)*main_mul154_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul154_fixbits + (-10000)*main_mul154_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_mul154_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul154_enob
solver.Add( + (1)*main_mul154_fixp + (1)*main_mul154_float + (1)*main_mul154_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul154_fixbits + (-10000)*main_mul154_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul154_fixp + (-1)*main_A_CAST_mul154_0_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul154_float + (-1)*main_A_CAST_mul154_0_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul154_double + (-1)*main_A_CAST_mul154_0_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul154_fixp + (-1)*main_mul154_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul154_float + (-1)*main_mul154_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul154_double + (-1)*main_mul154_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul154_fixp
mathCostObj +=  + (6)*main_mul154_float
mathCostObj +=  + (12.2551)*main_mul154_double
main_main_mul154_enob_1 = solver.IntVar(0, 1, 'main_main_mul154_enob_1')
main_main_mul154_enob_2 = solver.IntVar(0, 1, 'main_main_mul154_enob_2')
solver.Add( + (1)*main_main_mul154_enob_1 + (1)*main_main_mul154_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul154_enob + (-1)*main_A_enob_memphi_main_tmp6 + (-10000)*main_main_mul154_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul154_enob + (-1)*main_A_enob_memphi_main_tmp5 + (-10000)*main_main_mul154_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub155 = fsub double %w.0, %mul154, !taffo.info !76, !taffo.initweight !27
main_w_0_CAST_sub155_fixbits = solver.IntVar(0, 29, 'main_w_0_CAST_sub155_fixbits')
main_w_0_CAST_sub155_fixp = solver.IntVar(0, 1, 'main_w_0_CAST_sub155_fixp')
main_w_0_CAST_sub155_float = solver.IntVar(0, 1, 'main_w_0_CAST_sub155_float')
main_w_0_CAST_sub155_double = solver.IntVar(0, 1, 'main_w_0_CAST_sub155_double')
solver.Add( + (1)*main_w_0_CAST_sub155_fixp + (1)*main_w_0_CAST_sub155_float + (1)*main_w_0_CAST_sub155_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_0_CAST_sub155_fixbits + (-10000)*main_w_0_CAST_sub155_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C1_main_w_0_CAST_sub155')
C2_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C2_main_w_0_CAST_sub155')
solver.Add( + (1)*main_w_0_fixbits + (-1)*main_w_0_CAST_sub155_fixbits + (-10000)*C1_main_w_0_CAST_sub155<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_0_fixbits + (1)*main_w_0_CAST_sub155_fixbits + (-10000)*C2_main_w_0_CAST_sub155<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_0_CAST_sub155
castCostObj +=  + (1)*C2_main_w_0_CAST_sub155
C3_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C3_main_w_0_CAST_sub155')
C4_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C4_main_w_0_CAST_sub155')
C5_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C5_main_w_0_CAST_sub155')
C6_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C6_main_w_0_CAST_sub155')
C7_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C7_main_w_0_CAST_sub155')
C8_main_w_0_CAST_sub155 = solver.IntVar(0, 1, 'C8_main_w_0_CAST_sub155')
solver.Add( + (1)*main_w_0_fixp + (1)*main_w_0_CAST_sub155_float + (-1)*C3_main_w_0_CAST_sub155<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_0_CAST_sub155
solver.Add( + (1)*main_w_0_float + (1)*main_w_0_CAST_sub155_fixp + (-1)*C4_main_w_0_CAST_sub155<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_0_CAST_sub155
solver.Add( + (1)*main_w_0_fixp + (1)*main_w_0_CAST_sub155_double + (-1)*C5_main_w_0_CAST_sub155<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_0_CAST_sub155
solver.Add( + (1)*main_w_0_double + (1)*main_w_0_CAST_sub155_fixp + (-1)*C6_main_w_0_CAST_sub155<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_0_CAST_sub155
solver.Add( + (1)*main_w_0_float + (1)*main_w_0_CAST_sub155_double + (-1)*C7_main_w_0_CAST_sub155<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_0_CAST_sub155
solver.Add( + (1)*main_w_0_double + (1)*main_w_0_CAST_sub155_float + (-1)*C8_main_w_0_CAST_sub155<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_0_CAST_sub155



#Constraint for cast for   %sub155 = fsub double %w.0, %mul154, !taffo.info !76, !taffo.initweight !27
main_mul154_CAST_sub155_fixbits = solver.IntVar(0, 28, 'main_mul154_CAST_sub155_fixbits')
main_mul154_CAST_sub155_fixp = solver.IntVar(0, 1, 'main_mul154_CAST_sub155_fixp')
main_mul154_CAST_sub155_float = solver.IntVar(0, 1, 'main_mul154_CAST_sub155_float')
main_mul154_CAST_sub155_double = solver.IntVar(0, 1, 'main_mul154_CAST_sub155_double')
solver.Add( + (1)*main_mul154_CAST_sub155_fixp + (1)*main_mul154_CAST_sub155_float + (1)*main_mul154_CAST_sub155_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul154_CAST_sub155_fixbits + (-10000)*main_mul154_CAST_sub155_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C1_main_mul154_CAST_sub155')
C2_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C2_main_mul154_CAST_sub155')
solver.Add( + (1)*main_mul154_fixbits + (-1)*main_mul154_CAST_sub155_fixbits + (-10000)*C1_main_mul154_CAST_sub155<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul154_fixbits + (1)*main_mul154_CAST_sub155_fixbits + (-10000)*C2_main_mul154_CAST_sub155<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul154_CAST_sub155
castCostObj +=  + (1)*C2_main_mul154_CAST_sub155
C3_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C3_main_mul154_CAST_sub155')
C4_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C4_main_mul154_CAST_sub155')
C5_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C5_main_mul154_CAST_sub155')
C6_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C6_main_mul154_CAST_sub155')
C7_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C7_main_mul154_CAST_sub155')
C8_main_mul154_CAST_sub155 = solver.IntVar(0, 1, 'C8_main_mul154_CAST_sub155')
solver.Add( + (1)*main_mul154_fixp + (1)*main_mul154_CAST_sub155_float + (-1)*C3_main_mul154_CAST_sub155<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul154_CAST_sub155
solver.Add( + (1)*main_mul154_float + (1)*main_mul154_CAST_sub155_fixp + (-1)*C4_main_mul154_CAST_sub155<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul154_CAST_sub155
solver.Add( + (1)*main_mul154_fixp + (1)*main_mul154_CAST_sub155_double + (-1)*C5_main_mul154_CAST_sub155<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul154_CAST_sub155
solver.Add( + (1)*main_mul154_double + (1)*main_mul154_CAST_sub155_fixp + (-1)*C6_main_mul154_CAST_sub155<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul154_CAST_sub155
solver.Add( + (1)*main_mul154_float + (1)*main_mul154_CAST_sub155_double + (-1)*C7_main_mul154_CAST_sub155<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul154_CAST_sub155
solver.Add( + (1)*main_mul154_double + (1)*main_mul154_CAST_sub155_float + (-1)*C8_main_mul154_CAST_sub155<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul154_CAST_sub155



#Stuff for   %sub155 = fsub double %w.0, %mul154, !taffo.info !76, !taffo.initweight !27
main_sub155_fixbits = solver.IntVar(0, 28, 'main_sub155_fixbits')
main_sub155_fixp = solver.IntVar(0, 1, 'main_sub155_fixp')
main_sub155_float = solver.IntVar(0, 1, 'main_sub155_float')
main_sub155_double = solver.IntVar(0, 1, 'main_sub155_double')
main_sub155_enob = solver.IntVar(-10000, 10000, 'main_sub155_enob')
solver.Add( + (1)*main_sub155_enob + (-1)*main_sub155_fixbits + (10000)*main_sub155_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub155_enob + (10000)*main_sub155_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub155_enob + (10000)*main_sub155_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub155_fixbits + (-10000)*main_sub155_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_sub155_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub155_enob
solver.Add( + (1)*main_sub155_fixp + (1)*main_sub155_float + (1)*main_sub155_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub155_fixbits + (-10000)*main_sub155_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %w.0 = phi double [ %tmp4, %for.body137 ], [ %sub155, %for.inc156 ], !taffo.info !75
main_sub155_CAST_w_0_fixbits = solver.IntVar(0, 28, 'main_sub155_CAST_w_0_fixbits')
main_sub155_CAST_w_0_fixp = solver.IntVar(0, 1, 'main_sub155_CAST_w_0_fixp')
main_sub155_CAST_w_0_float = solver.IntVar(0, 1, 'main_sub155_CAST_w_0_float')
main_sub155_CAST_w_0_double = solver.IntVar(0, 1, 'main_sub155_CAST_w_0_double')
solver.Add( + (1)*main_sub155_CAST_w_0_fixp + (1)*main_sub155_CAST_w_0_float + (1)*main_sub155_CAST_w_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub155_CAST_w_0_fixbits + (-10000)*main_sub155_CAST_w_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C1_main_sub155_CAST_w_0')
C2_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C2_main_sub155_CAST_w_0')
solver.Add( + (1)*main_sub155_fixbits + (-1)*main_sub155_CAST_w_0_fixbits + (-10000)*C1_main_sub155_CAST_w_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub155_fixbits + (1)*main_sub155_CAST_w_0_fixbits + (-10000)*C2_main_sub155_CAST_w_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub155_CAST_w_0
castCostObj +=  + (1)*C2_main_sub155_CAST_w_0
C3_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C3_main_sub155_CAST_w_0')
C4_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C4_main_sub155_CAST_w_0')
C5_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C5_main_sub155_CAST_w_0')
C6_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C6_main_sub155_CAST_w_0')
C7_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C7_main_sub155_CAST_w_0')
C8_main_sub155_CAST_w_0 = solver.IntVar(0, 1, 'C8_main_sub155_CAST_w_0')
solver.Add( + (1)*main_sub155_fixp + (1)*main_sub155_CAST_w_0_float + (-1)*C3_main_sub155_CAST_w_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub155_CAST_w_0
solver.Add( + (1)*main_sub155_float + (1)*main_sub155_CAST_w_0_fixp + (-1)*C4_main_sub155_CAST_w_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub155_CAST_w_0
solver.Add( + (1)*main_sub155_fixp + (1)*main_sub155_CAST_w_0_double + (-1)*C5_main_sub155_CAST_w_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub155_CAST_w_0
solver.Add( + (1)*main_sub155_double + (1)*main_sub155_CAST_w_0_fixp + (-1)*C6_main_sub155_CAST_w_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub155_CAST_w_0
solver.Add( + (1)*main_sub155_float + (1)*main_sub155_CAST_w_0_double + (-1)*C7_main_sub155_CAST_w_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub155_CAST_w_0
solver.Add( + (1)*main_sub155_double + (1)*main_sub155_CAST_w_0_float + (-1)*C8_main_sub155_CAST_w_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub155_CAST_w_0
solver.Add( + (1)*main_w_0_fixp + (-1)*main_sub155_CAST_w_0_fixp==0)    #fix equality
solver.Add( + (1)*main_w_0_float + (-1)*main_sub155_CAST_w_0_float==0)    #float equality
solver.Add( + (1)*main_w_0_double + (-1)*main_sub155_CAST_w_0_double==0)    #double equality
solver.Add( + (1)*main_w_0_fixbits + (-1)*main_sub155_CAST_w_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_0_enob + (-1)*main_sub155_enob + (10000)*main_main_w_0_enob_1<=10000)    #Enob: forcing phi enob
solver.Add( + (1)*main_w_0_CAST_sub155_fixp + (-1)*main_mul154_CAST_sub155_fixp==0)    #fix equality
solver.Add( + (1)*main_w_0_CAST_sub155_float + (-1)*main_mul154_CAST_sub155_float==0)    #float equality
solver.Add( + (1)*main_w_0_CAST_sub155_double + (-1)*main_mul154_CAST_sub155_double==0)    #double equality
solver.Add( + (1)*main_w_0_CAST_sub155_fixbits + (-1)*main_mul154_CAST_sub155_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_0_CAST_sub155_fixp + (-1)*main_sub155_fixp==0)    #fix equality
solver.Add( + (1)*main_w_0_CAST_sub155_float + (-1)*main_sub155_float==0)    #float equality
solver.Add( + (1)*main_w_0_CAST_sub155_double + (-1)*main_sub155_double==0)    #double equality
solver.Add( + (1)*main_w_0_CAST_sub155_fixbits + (-1)*main_sub155_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub155_fixp
mathCostObj +=  + (3)*main_sub155_float
mathCostObj +=  + (6.64928)*main_sub155_double
solver.Add( + (1)*main_sub155_enob + (-1)*main_w_0_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub155_enob + (-1)*main_mul154_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp7')
solver.Add( + (1)*main_A_enob_memphi_main_tmp7 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
main_main_tmp7_enob_4 = solver.IntVar(0, 1, 'main_main_tmp7_enob_4')
main_main_tmp7_enob_5 = solver.IntVar(0, 1, 'main_main_tmp7_enob_5')
main_main_tmp7_enob_6 = solver.IntVar(0, 1, 'main_main_tmp7_enob_6')
main_main_tmp7_enob_7 = solver.IntVar(0, 1, 'main_main_tmp7_enob_7')
solver.Add( + (1)*main_main_tmp7_enob_1 + (1)*main_main_tmp7_enob_4 + (1)*main_main_tmp7_enob_5 + (1)*main_main_tmp7_enob_6 + (1)*main_main_tmp7_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp7 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp7 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp7_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp7 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp7_enob_5<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div163 = fdiv double %w.0, %tmp7, !taffo.info !11, !taffo.initweight !27
main_w_0_CAST_div163_fixbits = solver.IntVar(0, 29, 'main_w_0_CAST_div163_fixbits')
main_w_0_CAST_div163_fixp = solver.IntVar(0, 1, 'main_w_0_CAST_div163_fixp')
main_w_0_CAST_div163_float = solver.IntVar(0, 1, 'main_w_0_CAST_div163_float')
main_w_0_CAST_div163_double = solver.IntVar(0, 1, 'main_w_0_CAST_div163_double')
solver.Add( + (1)*main_w_0_CAST_div163_fixp + (1)*main_w_0_CAST_div163_float + (1)*main_w_0_CAST_div163_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_0_CAST_div163_fixbits + (-10000)*main_w_0_CAST_div163_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C1_main_w_0_CAST_div163')
C2_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C2_main_w_0_CAST_div163')
solver.Add( + (1)*main_w_0_fixbits + (-1)*main_w_0_CAST_div163_fixbits + (-10000)*C1_main_w_0_CAST_div163<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_0_fixbits + (1)*main_w_0_CAST_div163_fixbits + (-10000)*C2_main_w_0_CAST_div163<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_0_CAST_div163
castCostObj +=  + (1)*C2_main_w_0_CAST_div163
C3_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C3_main_w_0_CAST_div163')
C4_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C4_main_w_0_CAST_div163')
C5_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C5_main_w_0_CAST_div163')
C6_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C6_main_w_0_CAST_div163')
C7_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C7_main_w_0_CAST_div163')
C8_main_w_0_CAST_div163 = solver.IntVar(0, 1, 'C8_main_w_0_CAST_div163')
solver.Add( + (1)*main_w_0_fixp + (1)*main_w_0_CAST_div163_float + (-1)*C3_main_w_0_CAST_div163<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_0_CAST_div163
solver.Add( + (1)*main_w_0_float + (1)*main_w_0_CAST_div163_fixp + (-1)*C4_main_w_0_CAST_div163<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_0_CAST_div163
solver.Add( + (1)*main_w_0_fixp + (1)*main_w_0_CAST_div163_double + (-1)*C5_main_w_0_CAST_div163<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_0_CAST_div163
solver.Add( + (1)*main_w_0_double + (1)*main_w_0_CAST_div163_fixp + (-1)*C6_main_w_0_CAST_div163<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_0_CAST_div163
solver.Add( + (1)*main_w_0_float + (1)*main_w_0_CAST_div163_double + (-1)*C7_main_w_0_CAST_div163<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_0_CAST_div163
solver.Add( + (1)*main_w_0_double + (1)*main_w_0_CAST_div163_float + (-1)*C8_main_w_0_CAST_div163<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_0_CAST_div163



#Constraint for cast for   %div163 = fdiv double %w.0, %tmp7, !taffo.info !11, !taffo.initweight !27
main_A_CAST_div163_fixbits = solver.IntVar(0, 29, 'main_A_CAST_div163_fixbits')
main_A_CAST_div163_fixp = solver.IntVar(0, 1, 'main_A_CAST_div163_fixp')
main_A_CAST_div163_float = solver.IntVar(0, 1, 'main_A_CAST_div163_float')
main_A_CAST_div163_double = solver.IntVar(0, 1, 'main_A_CAST_div163_double')
solver.Add( + (1)*main_A_CAST_div163_fixp + (1)*main_A_CAST_div163_float + (1)*main_A_CAST_div163_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_div163_fixbits + (-10000)*main_A_CAST_div163_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_div163 = solver.IntVar(0, 1, 'C1_main_A_CAST_div163')
C2_main_A_CAST_div163 = solver.IntVar(0, 1, 'C2_main_A_CAST_div163')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_div163_fixbits + (-10000)*C1_main_A_CAST_div163<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_div163_fixbits + (-10000)*C2_main_A_CAST_div163<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_div163
castCostObj +=  + (1)*C2_main_A_CAST_div163
C3_main_A_CAST_div163 = solver.IntVar(0, 1, 'C3_main_A_CAST_div163')
C4_main_A_CAST_div163 = solver.IntVar(0, 1, 'C4_main_A_CAST_div163')
C5_main_A_CAST_div163 = solver.IntVar(0, 1, 'C5_main_A_CAST_div163')
C6_main_A_CAST_div163 = solver.IntVar(0, 1, 'C6_main_A_CAST_div163')
C7_main_A_CAST_div163 = solver.IntVar(0, 1, 'C7_main_A_CAST_div163')
C8_main_A_CAST_div163 = solver.IntVar(0, 1, 'C8_main_A_CAST_div163')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_div163_float + (-1)*C3_main_A_CAST_div163<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_div163
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_div163_fixp + (-1)*C4_main_A_CAST_div163<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_div163
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_div163_double + (-1)*C5_main_A_CAST_div163<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_div163
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_div163_fixp + (-1)*C6_main_A_CAST_div163<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_div163
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_div163_double + (-1)*C7_main_A_CAST_div163<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_div163
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_div163_float + (-1)*C8_main_A_CAST_div163<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_div163



#Stuff for   %div163 = fdiv double %w.0, %tmp7, !taffo.info !11, !taffo.initweight !27
main_div163_fixbits = solver.IntVar(0, 29, 'main_div163_fixbits')
main_div163_fixp = solver.IntVar(0, 1, 'main_div163_fixp')
main_div163_float = solver.IntVar(0, 1, 'main_div163_float')
main_div163_double = solver.IntVar(0, 1, 'main_div163_double')
main_div163_enob = solver.IntVar(-10000, 10000, 'main_div163_enob')
solver.Add( + (1)*main_div163_enob + (-1)*main_div163_fixbits + (10000)*main_div163_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div163_enob + (10000)*main_div163_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div163_enob + (10000)*main_div163_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div163_fixbits + (-10000)*main_div163_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_div163_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div163_enob
solver.Add( + (1)*main_div163_fixp + (1)*main_div163_float + (1)*main_div163_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div163_fixbits + (-10000)*main_div163_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_w_0_CAST_div163_fixp + (-1)*main_A_CAST_div163_fixp==0)    #fix equality
solver.Add( + (1)*main_w_0_CAST_div163_float + (-1)*main_A_CAST_div163_float==0)    #float equality
solver.Add( + (1)*main_w_0_CAST_div163_double + (-1)*main_A_CAST_div163_double==0)    #double equality
solver.Add( + (1)*main_w_0_CAST_div163_fixp + (-1)*main_div163_fixp==0)    #fix equality
solver.Add( + (1)*main_w_0_CAST_div163_float + (-1)*main_div163_float==0)    #float equality
solver.Add( + (1)*main_w_0_CAST_div163_double + (-1)*main_div163_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div163_fixp
mathCostObj +=  + (6)*main_div163_float
mathCostObj +=  + (12)*main_div163_double
main_main_div163_enob_1 = solver.IntVar(0, 1, 'main_main_div163_enob_1')
main_main_div163_enob_2 = solver.IntVar(0, 1, 'main_main_div163_enob_2')
solver.Add( + (1)*main_main_div163_enob_1 + (1)*main_main_div163_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div163_enob + (-1)*main_A_enob_memphi_main_tmp7 + (-10000)*main_main_div163_enob_1<=1026)    #Enob: propagation in division 1
solver.Add( + (1)*main_div163_enob + (-1)*main_w_0_enob + (-10000)*main_main_div163_enob_2<=1026)    #Enob: propagation in division 2



#Constraint for cast for   store double %div163, double* %arrayidx167, align 8, !taffo.info !11, !taffo.initweight !28
main_div163_CAST_store_fixbits = solver.IntVar(0, 29, 'main_div163_CAST_store_fixbits')
main_div163_CAST_store_fixp = solver.IntVar(0, 1, 'main_div163_CAST_store_fixp')
main_div163_CAST_store_float = solver.IntVar(0, 1, 'main_div163_CAST_store_float')
main_div163_CAST_store_double = solver.IntVar(0, 1, 'main_div163_CAST_store_double')
solver.Add( + (1)*main_div163_CAST_store_fixp + (1)*main_div163_CAST_store_float + (1)*main_div163_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div163_CAST_store_fixbits + (-10000)*main_div163_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div163_CAST_store = solver.IntVar(0, 1, 'C1_main_div163_CAST_store')
C2_main_div163_CAST_store = solver.IntVar(0, 1, 'C2_main_div163_CAST_store')
solver.Add( + (1)*main_div163_fixbits + (-1)*main_div163_CAST_store_fixbits + (-10000)*C1_main_div163_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div163_fixbits + (1)*main_div163_CAST_store_fixbits + (-10000)*C2_main_div163_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div163_CAST_store
castCostObj +=  + (1)*C2_main_div163_CAST_store
C3_main_div163_CAST_store = solver.IntVar(0, 1, 'C3_main_div163_CAST_store')
C4_main_div163_CAST_store = solver.IntVar(0, 1, 'C4_main_div163_CAST_store')
C5_main_div163_CAST_store = solver.IntVar(0, 1, 'C5_main_div163_CAST_store')
C6_main_div163_CAST_store = solver.IntVar(0, 1, 'C6_main_div163_CAST_store')
C7_main_div163_CAST_store = solver.IntVar(0, 1, 'C7_main_div163_CAST_store')
C8_main_div163_CAST_store = solver.IntVar(0, 1, 'C8_main_div163_CAST_store')
solver.Add( + (1)*main_div163_fixp + (1)*main_div163_CAST_store_float + (-1)*C3_main_div163_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div163_CAST_store
solver.Add( + (1)*main_div163_float + (1)*main_div163_CAST_store_fixp + (-1)*C4_main_div163_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div163_CAST_store
solver.Add( + (1)*main_div163_fixp + (1)*main_div163_CAST_store_double + (-1)*C5_main_div163_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div163_CAST_store
solver.Add( + (1)*main_div163_double + (1)*main_div163_CAST_store_fixp + (-1)*C6_main_div163_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div163_CAST_store
solver.Add( + (1)*main_div163_float + (1)*main_div163_CAST_store_double + (-1)*C7_main_div163_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div163_CAST_store
solver.Add( + (1)*main_div163_double + (1)*main_div163_CAST_store_float + (-1)*C8_main_div163_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div163_CAST_store
solver.Add( + (1)*main_A_fixp + (-1)*main_div163_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_A_float + (-1)*main_div163_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_A_double + (-1)*main_div163_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_A_fixbits + (-1)*main_div163_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_A_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_A_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB + (-1)*main_A_fixbits + (10000)*main_A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB + (10000)*main_A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB + (10000)*main_A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB + (-1)*main_div163_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp4 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp5 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp6 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp7 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_7<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp8')
solver.Add( + (1)*main_A_enob_memphi_main_tmp8 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
main_main_tmp8_enob_4 = solver.IntVar(0, 1, 'main_main_tmp8_enob_4')
main_main_tmp8_enob_5 = solver.IntVar(0, 1, 'main_main_tmp8_enob_5')
main_main_tmp8_enob_6 = solver.IntVar(0, 1, 'main_main_tmp8_enob_6')
main_main_tmp8_enob_7 = solver.IntVar(0, 1, 'main_main_tmp8_enob_7')
solver.Add( + (1)*main_main_tmp8_enob_1 + (1)*main_main_tmp8_enob_4 + (1)*main_main_tmp8_enob_5 + (1)*main_main_tmp8_enob_6 + (1)*main_main_tmp8_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp8 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp8 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp8_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp8 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp8_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp8 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_6<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %w.1 = phi double [ %tmp8, %for.body174 ], [ %sub192, %for.inc193 ], !taffo.info !75
main_w_1_fixbits = solver.IntVar(0, 29, 'main_w_1_fixbits')
main_w_1_fixp = solver.IntVar(0, 1, 'main_w_1_fixp')
main_w_1_float = solver.IntVar(0, 1, 'main_w_1_float')
main_w_1_double = solver.IntVar(0, 1, 'main_w_1_double')
main_w_1_enob = solver.IntVar(-10000, 10000, 'main_w_1_enob')
solver.Add( + (1)*main_w_1_enob + (-1)*main_w_1_fixbits + (10000)*main_w_1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_w_1_enob + (10000)*main_w_1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_w_1_enob + (10000)*main_w_1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_w_1_fixbits + (-10000)*main_w_1_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_w_1_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_w_1_enob
solver.Add( + (1)*main_w_1_fixp + (1)*main_w_1_float + (1)*main_w_1_double==1)    #Exactly one selected type
solver.Add( + (1)*main_w_1_fixbits + (-10000)*main_w_1_fixp<=0)    #If not fix, frac part to zero
main_main_w_1_enob_0 = solver.IntVar(0, 1, 'main_main_w_1_enob_0')
main_main_w_1_enob_1 = solver.IntVar(0, 1, 'main_main_w_1_enob_1')
solver.Add( + (1)*main_main_w_1_enob_0 + (1)*main_main_w_1_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %w.1 = phi double [ %tmp8, %for.body174 ], [ %sub192, %for.inc193 ], !taffo.info !75
main_A_CAST_w_1_fixbits = solver.IntVar(0, 29, 'main_A_CAST_w_1_fixbits')
main_A_CAST_w_1_fixp = solver.IntVar(0, 1, 'main_A_CAST_w_1_fixp')
main_A_CAST_w_1_float = solver.IntVar(0, 1, 'main_A_CAST_w_1_float')
main_A_CAST_w_1_double = solver.IntVar(0, 1, 'main_A_CAST_w_1_double')
solver.Add( + (1)*main_A_CAST_w_1_fixp + (1)*main_A_CAST_w_1_float + (1)*main_A_CAST_w_1_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_w_1_fixbits + (-10000)*main_A_CAST_w_1_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C1_main_A_CAST_w_1')
C2_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C2_main_A_CAST_w_1')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_w_1_fixbits + (-10000)*C1_main_A_CAST_w_1<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_w_1_fixbits + (-10000)*C2_main_A_CAST_w_1<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_w_1
castCostObj +=  + (1)*C2_main_A_CAST_w_1
C3_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C3_main_A_CAST_w_1')
C4_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C4_main_A_CAST_w_1')
C5_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C5_main_A_CAST_w_1')
C6_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C6_main_A_CAST_w_1')
C7_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C7_main_A_CAST_w_1')
C8_main_A_CAST_w_1 = solver.IntVar(0, 1, 'C8_main_A_CAST_w_1')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_w_1_float + (-1)*C3_main_A_CAST_w_1<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_w_1
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_w_1_fixp + (-1)*C4_main_A_CAST_w_1<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_w_1
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_w_1_double + (-1)*C5_main_A_CAST_w_1<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_w_1
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_w_1_fixp + (-1)*C6_main_A_CAST_w_1<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_w_1
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_w_1_double + (-1)*C7_main_A_CAST_w_1<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_w_1
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_w_1_float + (-1)*C8_main_A_CAST_w_1<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_w_1
solver.Add( + (1)*main_w_1_fixp + (-1)*main_A_CAST_w_1_fixp==0)    #fix equality
solver.Add( + (1)*main_w_1_float + (-1)*main_A_CAST_w_1_float==0)    #float equality
solver.Add( + (1)*main_w_1_double + (-1)*main_A_CAST_w_1_double==0)    #double equality
solver.Add( + (1)*main_w_1_fixbits + (-1)*main_A_CAST_w_1_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_1_enob + (-1)*main_A_enob_memphi_main_tmp8 + (10000)*main_main_w_1_enob_0<=10000)    #Enob: forcing phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp9')
solver.Add( + (1)*main_A_enob_memphi_main_tmp9 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_1 = solver.IntVar(0, 1, 'main_main_tmp9_enob_1')
main_main_tmp9_enob_4 = solver.IntVar(0, 1, 'main_main_tmp9_enob_4')
main_main_tmp9_enob_5 = solver.IntVar(0, 1, 'main_main_tmp9_enob_5')
main_main_tmp9_enob_6 = solver.IntVar(0, 1, 'main_main_tmp9_enob_6')
main_main_tmp9_enob_7 = solver.IntVar(0, 1, 'main_main_tmp9_enob_7')
solver.Add( + (1)*main_main_tmp9_enob_1 + (1)*main_main_tmp9_enob_4 + (1)*main_main_tmp9_enob_5 + (1)*main_main_tmp9_enob_6 + (1)*main_main_tmp9_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp9 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp9_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp9 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp9_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp9 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp9_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp9 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_6<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp10')
solver.Add( + (1)*main_A_enob_memphi_main_tmp10 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_1 = solver.IntVar(0, 1, 'main_main_tmp10_enob_1')
main_main_tmp10_enob_4 = solver.IntVar(0, 1, 'main_main_tmp10_enob_4')
main_main_tmp10_enob_5 = solver.IntVar(0, 1, 'main_main_tmp10_enob_5')
main_main_tmp10_enob_6 = solver.IntVar(0, 1, 'main_main_tmp10_enob_6')
main_main_tmp10_enob_7 = solver.IntVar(0, 1, 'main_main_tmp10_enob_7')
solver.Add( + (1)*main_main_tmp10_enob_1 + (1)*main_main_tmp10_enob_4 + (1)*main_main_tmp10_enob_5 + (1)*main_main_tmp10_enob_6 + (1)*main_main_tmp10_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp10 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp10_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp10 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp10_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp10 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp10_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp10 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_6<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul191 = fmul double %tmp9, %tmp10, !taffo.info !69, !taffo.initweight !41
main_A_CAST_mul191_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul191_fixbits')
main_A_CAST_mul191_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul191_fixp')
main_A_CAST_mul191_float = solver.IntVar(0, 1, 'main_A_CAST_mul191_float')
main_A_CAST_mul191_double = solver.IntVar(0, 1, 'main_A_CAST_mul191_double')
solver.Add( + (1)*main_A_CAST_mul191_fixp + (1)*main_A_CAST_mul191_float + (1)*main_A_CAST_mul191_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul191_fixbits + (-10000)*main_A_CAST_mul191_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul191')
C2_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul191')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul191_fixbits + (-10000)*C1_main_A_CAST_mul191<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul191_fixbits + (-10000)*C2_main_A_CAST_mul191<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul191
castCostObj +=  + (1)*C2_main_A_CAST_mul191
C3_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul191')
C4_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul191')
C5_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul191')
C6_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul191')
C7_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul191')
C8_main_A_CAST_mul191 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul191')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul191_float + (-1)*C3_main_A_CAST_mul191<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul191
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul191_fixp + (-1)*C4_main_A_CAST_mul191<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul191
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul191_double + (-1)*C5_main_A_CAST_mul191<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul191
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul191_fixp + (-1)*C6_main_A_CAST_mul191<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul191
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul191_double + (-1)*C7_main_A_CAST_mul191<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul191
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul191_float + (-1)*C8_main_A_CAST_mul191<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul191



#Constraint for cast for   %mul191 = fmul double %tmp9, %tmp10, !taffo.info !69, !taffo.initweight !41
main_A_CAST_mul191_0_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul191_0_fixbits')
main_A_CAST_mul191_0_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul191_0_fixp')
main_A_CAST_mul191_0_float = solver.IntVar(0, 1, 'main_A_CAST_mul191_0_float')
main_A_CAST_mul191_0_double = solver.IntVar(0, 1, 'main_A_CAST_mul191_0_double')
solver.Add( + (1)*main_A_CAST_mul191_0_fixp + (1)*main_A_CAST_mul191_0_float + (1)*main_A_CAST_mul191_0_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul191_0_fixbits + (-10000)*main_A_CAST_mul191_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul191_0')
C2_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul191_0')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul191_0_fixbits + (-10000)*C1_main_A_CAST_mul191_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul191_0_fixbits + (-10000)*C2_main_A_CAST_mul191_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul191_0
castCostObj +=  + (1)*C2_main_A_CAST_mul191_0
C3_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul191_0')
C4_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul191_0')
C5_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul191_0')
C6_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul191_0')
C7_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul191_0')
C8_main_A_CAST_mul191_0 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul191_0')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul191_0_float + (-1)*C3_main_A_CAST_mul191_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul191_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul191_0_fixp + (-1)*C4_main_A_CAST_mul191_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul191_0
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul191_0_double + (-1)*C5_main_A_CAST_mul191_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul191_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul191_0_fixp + (-1)*C6_main_A_CAST_mul191_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul191_0
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul191_0_double + (-1)*C7_main_A_CAST_mul191_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul191_0
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul191_0_float + (-1)*C8_main_A_CAST_mul191_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul191_0



#Stuff for   %mul191 = fmul double %tmp9, %tmp10, !taffo.info !69, !taffo.initweight !41
main_mul191_fixbits = solver.IntVar(0, 28, 'main_mul191_fixbits')
main_mul191_fixp = solver.IntVar(0, 1, 'main_mul191_fixp')
main_mul191_float = solver.IntVar(0, 1, 'main_mul191_float')
main_mul191_double = solver.IntVar(0, 1, 'main_mul191_double')
main_mul191_enob = solver.IntVar(-10000, 10000, 'main_mul191_enob')
solver.Add( + (1)*main_mul191_enob + (-1)*main_mul191_fixbits + (10000)*main_mul191_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul191_enob + (10000)*main_mul191_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul191_enob + (10000)*main_mul191_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul191_fixbits + (-10000)*main_mul191_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_mul191_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul191_enob
solver.Add( + (1)*main_mul191_fixp + (1)*main_mul191_float + (1)*main_mul191_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul191_fixbits + (-10000)*main_mul191_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul191_fixp + (-1)*main_A_CAST_mul191_0_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul191_float + (-1)*main_A_CAST_mul191_0_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul191_double + (-1)*main_A_CAST_mul191_0_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul191_fixp + (-1)*main_mul191_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul191_float + (-1)*main_mul191_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul191_double + (-1)*main_mul191_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul191_fixp
mathCostObj +=  + (6)*main_mul191_float
mathCostObj +=  + (12.2551)*main_mul191_double
main_main_mul191_enob_1 = solver.IntVar(0, 1, 'main_main_mul191_enob_1')
main_main_mul191_enob_2 = solver.IntVar(0, 1, 'main_main_mul191_enob_2')
solver.Add( + (1)*main_main_mul191_enob_1 + (1)*main_main_mul191_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul191_enob + (-1)*main_A_enob_memphi_main_tmp10 + (-10000)*main_main_mul191_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul191_enob + (-1)*main_A_enob_memphi_main_tmp9 + (-10000)*main_main_mul191_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub192 = fsub double %w.1, %mul191, !taffo.info !76, !taffo.initweight !27
main_w_1_CAST_sub192_fixbits = solver.IntVar(0, 29, 'main_w_1_CAST_sub192_fixbits')
main_w_1_CAST_sub192_fixp = solver.IntVar(0, 1, 'main_w_1_CAST_sub192_fixp')
main_w_1_CAST_sub192_float = solver.IntVar(0, 1, 'main_w_1_CAST_sub192_float')
main_w_1_CAST_sub192_double = solver.IntVar(0, 1, 'main_w_1_CAST_sub192_double')
solver.Add( + (1)*main_w_1_CAST_sub192_fixp + (1)*main_w_1_CAST_sub192_float + (1)*main_w_1_CAST_sub192_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_1_CAST_sub192_fixbits + (-10000)*main_w_1_CAST_sub192_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C1_main_w_1_CAST_sub192')
C2_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C2_main_w_1_CAST_sub192')
solver.Add( + (1)*main_w_1_fixbits + (-1)*main_w_1_CAST_sub192_fixbits + (-10000)*C1_main_w_1_CAST_sub192<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_1_fixbits + (1)*main_w_1_CAST_sub192_fixbits + (-10000)*C2_main_w_1_CAST_sub192<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_1_CAST_sub192
castCostObj +=  + (1)*C2_main_w_1_CAST_sub192
C3_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C3_main_w_1_CAST_sub192')
C4_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C4_main_w_1_CAST_sub192')
C5_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C5_main_w_1_CAST_sub192')
C6_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C6_main_w_1_CAST_sub192')
C7_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C7_main_w_1_CAST_sub192')
C8_main_w_1_CAST_sub192 = solver.IntVar(0, 1, 'C8_main_w_1_CAST_sub192')
solver.Add( + (1)*main_w_1_fixp + (1)*main_w_1_CAST_sub192_float + (-1)*C3_main_w_1_CAST_sub192<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_1_CAST_sub192
solver.Add( + (1)*main_w_1_float + (1)*main_w_1_CAST_sub192_fixp + (-1)*C4_main_w_1_CAST_sub192<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_1_CAST_sub192
solver.Add( + (1)*main_w_1_fixp + (1)*main_w_1_CAST_sub192_double + (-1)*C5_main_w_1_CAST_sub192<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_1_CAST_sub192
solver.Add( + (1)*main_w_1_double + (1)*main_w_1_CAST_sub192_fixp + (-1)*C6_main_w_1_CAST_sub192<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_1_CAST_sub192
solver.Add( + (1)*main_w_1_float + (1)*main_w_1_CAST_sub192_double + (-1)*C7_main_w_1_CAST_sub192<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_1_CAST_sub192
solver.Add( + (1)*main_w_1_double + (1)*main_w_1_CAST_sub192_float + (-1)*C8_main_w_1_CAST_sub192<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_1_CAST_sub192



#Constraint for cast for   %sub192 = fsub double %w.1, %mul191, !taffo.info !76, !taffo.initweight !27
main_mul191_CAST_sub192_fixbits = solver.IntVar(0, 28, 'main_mul191_CAST_sub192_fixbits')
main_mul191_CAST_sub192_fixp = solver.IntVar(0, 1, 'main_mul191_CAST_sub192_fixp')
main_mul191_CAST_sub192_float = solver.IntVar(0, 1, 'main_mul191_CAST_sub192_float')
main_mul191_CAST_sub192_double = solver.IntVar(0, 1, 'main_mul191_CAST_sub192_double')
solver.Add( + (1)*main_mul191_CAST_sub192_fixp + (1)*main_mul191_CAST_sub192_float + (1)*main_mul191_CAST_sub192_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul191_CAST_sub192_fixbits + (-10000)*main_mul191_CAST_sub192_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C1_main_mul191_CAST_sub192')
C2_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C2_main_mul191_CAST_sub192')
solver.Add( + (1)*main_mul191_fixbits + (-1)*main_mul191_CAST_sub192_fixbits + (-10000)*C1_main_mul191_CAST_sub192<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul191_fixbits + (1)*main_mul191_CAST_sub192_fixbits + (-10000)*C2_main_mul191_CAST_sub192<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul191_CAST_sub192
castCostObj +=  + (1)*C2_main_mul191_CAST_sub192
C3_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C3_main_mul191_CAST_sub192')
C4_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C4_main_mul191_CAST_sub192')
C5_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C5_main_mul191_CAST_sub192')
C6_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C6_main_mul191_CAST_sub192')
C7_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C7_main_mul191_CAST_sub192')
C8_main_mul191_CAST_sub192 = solver.IntVar(0, 1, 'C8_main_mul191_CAST_sub192')
solver.Add( + (1)*main_mul191_fixp + (1)*main_mul191_CAST_sub192_float + (-1)*C3_main_mul191_CAST_sub192<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul191_CAST_sub192
solver.Add( + (1)*main_mul191_float + (1)*main_mul191_CAST_sub192_fixp + (-1)*C4_main_mul191_CAST_sub192<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul191_CAST_sub192
solver.Add( + (1)*main_mul191_fixp + (1)*main_mul191_CAST_sub192_double + (-1)*C5_main_mul191_CAST_sub192<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul191_CAST_sub192
solver.Add( + (1)*main_mul191_double + (1)*main_mul191_CAST_sub192_fixp + (-1)*C6_main_mul191_CAST_sub192<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul191_CAST_sub192
solver.Add( + (1)*main_mul191_float + (1)*main_mul191_CAST_sub192_double + (-1)*C7_main_mul191_CAST_sub192<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul191_CAST_sub192
solver.Add( + (1)*main_mul191_double + (1)*main_mul191_CAST_sub192_float + (-1)*C8_main_mul191_CAST_sub192<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul191_CAST_sub192



#Stuff for   %sub192 = fsub double %w.1, %mul191, !taffo.info !76, !taffo.initweight !27
main_sub192_fixbits = solver.IntVar(0, 28, 'main_sub192_fixbits')
main_sub192_fixp = solver.IntVar(0, 1, 'main_sub192_fixp')
main_sub192_float = solver.IntVar(0, 1, 'main_sub192_float')
main_sub192_double = solver.IntVar(0, 1, 'main_sub192_double')
main_sub192_enob = solver.IntVar(-10000, 10000, 'main_sub192_enob')
solver.Add( + (1)*main_sub192_enob + (-1)*main_sub192_fixbits + (10000)*main_sub192_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub192_enob + (10000)*main_sub192_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub192_enob + (10000)*main_sub192_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub192_fixbits + (-10000)*main_sub192_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_sub192_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub192_enob
solver.Add( + (1)*main_sub192_fixp + (1)*main_sub192_float + (1)*main_sub192_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub192_fixbits + (-10000)*main_sub192_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %w.1 = phi double [ %tmp8, %for.body174 ], [ %sub192, %for.inc193 ], !taffo.info !75
main_sub192_CAST_w_1_fixbits = solver.IntVar(0, 28, 'main_sub192_CAST_w_1_fixbits')
main_sub192_CAST_w_1_fixp = solver.IntVar(0, 1, 'main_sub192_CAST_w_1_fixp')
main_sub192_CAST_w_1_float = solver.IntVar(0, 1, 'main_sub192_CAST_w_1_float')
main_sub192_CAST_w_1_double = solver.IntVar(0, 1, 'main_sub192_CAST_w_1_double')
solver.Add( + (1)*main_sub192_CAST_w_1_fixp + (1)*main_sub192_CAST_w_1_float + (1)*main_sub192_CAST_w_1_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub192_CAST_w_1_fixbits + (-10000)*main_sub192_CAST_w_1_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C1_main_sub192_CAST_w_1')
C2_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C2_main_sub192_CAST_w_1')
solver.Add( + (1)*main_sub192_fixbits + (-1)*main_sub192_CAST_w_1_fixbits + (-10000)*C1_main_sub192_CAST_w_1<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub192_fixbits + (1)*main_sub192_CAST_w_1_fixbits + (-10000)*C2_main_sub192_CAST_w_1<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub192_CAST_w_1
castCostObj +=  + (1)*C2_main_sub192_CAST_w_1
C3_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C3_main_sub192_CAST_w_1')
C4_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C4_main_sub192_CAST_w_1')
C5_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C5_main_sub192_CAST_w_1')
C6_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C6_main_sub192_CAST_w_1')
C7_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C7_main_sub192_CAST_w_1')
C8_main_sub192_CAST_w_1 = solver.IntVar(0, 1, 'C8_main_sub192_CAST_w_1')
solver.Add( + (1)*main_sub192_fixp + (1)*main_sub192_CAST_w_1_float + (-1)*C3_main_sub192_CAST_w_1<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub192_CAST_w_1
solver.Add( + (1)*main_sub192_float + (1)*main_sub192_CAST_w_1_fixp + (-1)*C4_main_sub192_CAST_w_1<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub192_CAST_w_1
solver.Add( + (1)*main_sub192_fixp + (1)*main_sub192_CAST_w_1_double + (-1)*C5_main_sub192_CAST_w_1<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub192_CAST_w_1
solver.Add( + (1)*main_sub192_double + (1)*main_sub192_CAST_w_1_fixp + (-1)*C6_main_sub192_CAST_w_1<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub192_CAST_w_1
solver.Add( + (1)*main_sub192_float + (1)*main_sub192_CAST_w_1_double + (-1)*C7_main_sub192_CAST_w_1<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub192_CAST_w_1
solver.Add( + (1)*main_sub192_double + (1)*main_sub192_CAST_w_1_float + (-1)*C8_main_sub192_CAST_w_1<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub192_CAST_w_1
solver.Add( + (1)*main_w_1_fixp + (-1)*main_sub192_CAST_w_1_fixp==0)    #fix equality
solver.Add( + (1)*main_w_1_float + (-1)*main_sub192_CAST_w_1_float==0)    #float equality
solver.Add( + (1)*main_w_1_double + (-1)*main_sub192_CAST_w_1_double==0)    #double equality
solver.Add( + (1)*main_w_1_fixbits + (-1)*main_sub192_CAST_w_1_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_1_enob + (-1)*main_sub192_enob + (10000)*main_main_w_1_enob_1<=10000)    #Enob: forcing phi enob
solver.Add( + (1)*main_w_1_CAST_sub192_fixp + (-1)*main_mul191_CAST_sub192_fixp==0)    #fix equality
solver.Add( + (1)*main_w_1_CAST_sub192_float + (-1)*main_mul191_CAST_sub192_float==0)    #float equality
solver.Add( + (1)*main_w_1_CAST_sub192_double + (-1)*main_mul191_CAST_sub192_double==0)    #double equality
solver.Add( + (1)*main_w_1_CAST_sub192_fixbits + (-1)*main_mul191_CAST_sub192_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_1_CAST_sub192_fixp + (-1)*main_sub192_fixp==0)    #fix equality
solver.Add( + (1)*main_w_1_CAST_sub192_float + (-1)*main_sub192_float==0)    #float equality
solver.Add( + (1)*main_w_1_CAST_sub192_double + (-1)*main_sub192_double==0)    #double equality
solver.Add( + (1)*main_w_1_CAST_sub192_fixbits + (-1)*main_sub192_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub192_fixp
mathCostObj +=  + (3)*main_sub192_float
mathCostObj +=  + (6.64928)*main_sub192_double
solver.Add( + (1)*main_sub192_enob + (-1)*main_w_1_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub192_enob + (-1)*main_mul191_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %w.1, double* %arrayidx199, align 8, !taffo.info !11, !taffo.initweight !27
main_w_1_CAST_store_fixbits = solver.IntVar(0, 29, 'main_w_1_CAST_store_fixbits')
main_w_1_CAST_store_fixp = solver.IntVar(0, 1, 'main_w_1_CAST_store_fixp')
main_w_1_CAST_store_float = solver.IntVar(0, 1, 'main_w_1_CAST_store_float')
main_w_1_CAST_store_double = solver.IntVar(0, 1, 'main_w_1_CAST_store_double')
solver.Add( + (1)*main_w_1_CAST_store_fixp + (1)*main_w_1_CAST_store_float + (1)*main_w_1_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_1_CAST_store_fixbits + (-10000)*main_w_1_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_1_CAST_store = solver.IntVar(0, 1, 'C1_main_w_1_CAST_store')
C2_main_w_1_CAST_store = solver.IntVar(0, 1, 'C2_main_w_1_CAST_store')
solver.Add( + (1)*main_w_1_fixbits + (-1)*main_w_1_CAST_store_fixbits + (-10000)*C1_main_w_1_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_1_fixbits + (1)*main_w_1_CAST_store_fixbits + (-10000)*C2_main_w_1_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_1_CAST_store
castCostObj +=  + (1)*C2_main_w_1_CAST_store
C3_main_w_1_CAST_store = solver.IntVar(0, 1, 'C3_main_w_1_CAST_store')
C4_main_w_1_CAST_store = solver.IntVar(0, 1, 'C4_main_w_1_CAST_store')
C5_main_w_1_CAST_store = solver.IntVar(0, 1, 'C5_main_w_1_CAST_store')
C6_main_w_1_CAST_store = solver.IntVar(0, 1, 'C6_main_w_1_CAST_store')
C7_main_w_1_CAST_store = solver.IntVar(0, 1, 'C7_main_w_1_CAST_store')
C8_main_w_1_CAST_store = solver.IntVar(0, 1, 'C8_main_w_1_CAST_store')
solver.Add( + (1)*main_w_1_fixp + (1)*main_w_1_CAST_store_float + (-1)*C3_main_w_1_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_1_CAST_store
solver.Add( + (1)*main_w_1_float + (1)*main_w_1_CAST_store_fixp + (-1)*C4_main_w_1_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_1_CAST_store
solver.Add( + (1)*main_w_1_fixp + (1)*main_w_1_CAST_store_double + (-1)*C5_main_w_1_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_1_CAST_store
solver.Add( + (1)*main_w_1_double + (1)*main_w_1_CAST_store_fixp + (-1)*C6_main_w_1_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_1_CAST_store
solver.Add( + (1)*main_w_1_float + (1)*main_w_1_CAST_store_double + (-1)*C7_main_w_1_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_1_CAST_store
solver.Add( + (1)*main_w_1_double + (1)*main_w_1_CAST_store_float + (-1)*C8_main_w_1_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_1_CAST_store
solver.Add( + (1)*main_A_fixp + (-1)*main_w_1_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_A_float + (-1)*main_w_1_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_A_double + (-1)*main_w_1_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_A_fixbits + (-1)*main_w_1_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_A_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_A_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB_storeENOB + (-1)*main_A_fixbits + (10000)*main_A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_A_enob_storeENOB_storeENOB_storeENOB + (-1)*main_w_1_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp4 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp5 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp6 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp7 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp7_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp8 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp8_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp9 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp10 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_7<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_b_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'main_b_enob_memphi_main_tmp11')
solver.Add( + (1)*main_b_enob_memphi_main_tmp11 + (-1)*main_b_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_1 = solver.IntVar(0, 1, 'main_main_tmp11_enob_1')
solver.Add( + (1)*main_main_tmp11_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_b_enob_memphi_main_tmp11 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp11_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %w.2 = phi double [ %tmp11, %for.body209 ], [ %sub223, %for.inc224 ], !taffo.info !80
main_w_2_fixbits = solver.IntVar(0, 28, 'main_w_2_fixbits')
main_w_2_fixp = solver.IntVar(0, 1, 'main_w_2_fixp')
main_w_2_float = solver.IntVar(0, 1, 'main_w_2_float')
main_w_2_double = solver.IntVar(0, 1, 'main_w_2_double')
main_w_2_enob = solver.IntVar(-10000, 10000, 'main_w_2_enob')
solver.Add( + (1)*main_w_2_enob + (-1)*main_w_2_fixbits + (10000)*main_w_2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_w_2_enob + (10000)*main_w_2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_w_2_enob + (10000)*main_w_2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_w_2_fixbits + (-10000)*main_w_2_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_w_2_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_w_2_enob
solver.Add( + (1)*main_w_2_fixp + (1)*main_w_2_float + (1)*main_w_2_double==1)    #Exactly one selected type
solver.Add( + (1)*main_w_2_fixbits + (-10000)*main_w_2_fixp<=0)    #If not fix, frac part to zero
main_main_w_2_enob_0 = solver.IntVar(0, 1, 'main_main_w_2_enob_0')
main_main_w_2_enob_1 = solver.IntVar(0, 1, 'main_main_w_2_enob_1')
solver.Add( + (1)*main_main_w_2_enob_0 + (1)*main_main_w_2_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %w.2 = phi double [ %tmp11, %for.body209 ], [ %sub223, %for.inc224 ], !taffo.info !80
main_b_CAST_w_2_fixbits = solver.IntVar(0, 29, 'main_b_CAST_w_2_fixbits')
main_b_CAST_w_2_fixp = solver.IntVar(0, 1, 'main_b_CAST_w_2_fixp')
main_b_CAST_w_2_float = solver.IntVar(0, 1, 'main_b_CAST_w_2_float')
main_b_CAST_w_2_double = solver.IntVar(0, 1, 'main_b_CAST_w_2_double')
solver.Add( + (1)*main_b_CAST_w_2_fixp + (1)*main_b_CAST_w_2_float + (1)*main_b_CAST_w_2_double==1)    #exactly 1 type
solver.Add( + (1)*main_b_CAST_w_2_fixbits + (-10000)*main_b_CAST_w_2_fixp<=0)    #If no fix, fix frac part = 0
C1_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C1_main_b_CAST_w_2')
C2_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C2_main_b_CAST_w_2')
solver.Add( + (1)*main_b_fixbits + (-1)*main_b_CAST_w_2_fixbits + (-10000)*C1_main_b_CAST_w_2<=0)    #Shift cost 1
solver.Add( + (-1)*main_b_fixbits + (1)*main_b_CAST_w_2_fixbits + (-10000)*C2_main_b_CAST_w_2<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_b_CAST_w_2
castCostObj +=  + (1)*C2_main_b_CAST_w_2
C3_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C3_main_b_CAST_w_2')
C4_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C4_main_b_CAST_w_2')
C5_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C5_main_b_CAST_w_2')
C6_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C6_main_b_CAST_w_2')
C7_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C7_main_b_CAST_w_2')
C8_main_b_CAST_w_2 = solver.IntVar(0, 1, 'C8_main_b_CAST_w_2')
solver.Add( + (1)*main_b_fixp + (1)*main_b_CAST_w_2_float + (-1)*C3_main_b_CAST_w_2<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_b_CAST_w_2
solver.Add( + (1)*main_b_float + (1)*main_b_CAST_w_2_fixp + (-1)*C4_main_b_CAST_w_2<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_b_CAST_w_2
solver.Add( + (1)*main_b_fixp + (1)*main_b_CAST_w_2_double + (-1)*C5_main_b_CAST_w_2<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_b_CAST_w_2
solver.Add( + (1)*main_b_double + (1)*main_b_CAST_w_2_fixp + (-1)*C6_main_b_CAST_w_2<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_b_CAST_w_2
solver.Add( + (1)*main_b_float + (1)*main_b_CAST_w_2_double + (-1)*C7_main_b_CAST_w_2<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_b_CAST_w_2
solver.Add( + (1)*main_b_double + (1)*main_b_CAST_w_2_float + (-1)*C8_main_b_CAST_w_2<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_b_CAST_w_2
solver.Add( + (1)*main_w_2_fixp + (-1)*main_b_CAST_w_2_fixp==0)    #fix equality
solver.Add( + (1)*main_w_2_float + (-1)*main_b_CAST_w_2_float==0)    #float equality
solver.Add( + (1)*main_w_2_double + (-1)*main_b_CAST_w_2_double==0)    #double equality
solver.Add( + (1)*main_w_2_fixbits + (-1)*main_b_CAST_w_2_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_2_enob + (-1)*main_b_enob_memphi_main_tmp11 + (10000)*main_main_w_2_enob_0<=10000)    #Enob: forcing phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp12')
solver.Add( + (1)*main_A_enob_memphi_main_tmp12 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp12_enob_1 = solver.IntVar(0, 1, 'main_main_tmp12_enob_1')
main_main_tmp12_enob_4 = solver.IntVar(0, 1, 'main_main_tmp12_enob_4')
main_main_tmp12_enob_5 = solver.IntVar(0, 1, 'main_main_tmp12_enob_5')
main_main_tmp12_enob_6 = solver.IntVar(0, 1, 'main_main_tmp12_enob_6')
main_main_tmp12_enob_7 = solver.IntVar(0, 1, 'main_main_tmp12_enob_7')
solver.Add( + (1)*main_main_tmp12_enob_1 + (1)*main_main_tmp12_enob_4 + (1)*main_main_tmp12_enob_5 + (1)*main_main_tmp12_enob_6 + (1)*main_main_tmp12_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp12 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp12_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp12 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp12_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp12 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp12_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp12 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp12 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_7<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_y_enob_memphi_main_tmp13 = solver.IntVar(-10000, 10000, 'main_y_enob_memphi_main_tmp13')
solver.Add( + (1)*main_y_enob_memphi_main_tmp13 + (-1)*main_y_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp13_enob_1 = solver.IntVar(0, 1, 'main_main_tmp13_enob_1')
main_main_tmp13_enob_4 = solver.IntVar(0, 1, 'main_main_tmp13_enob_4')
main_main_tmp13_enob_5 = solver.IntVar(0, 1, 'main_main_tmp13_enob_5')
main_main_tmp13_enob_6 = solver.IntVar(0, 1, 'main_main_tmp13_enob_6')
main_main_tmp13_enob_7 = solver.IntVar(0, 1, 'main_main_tmp13_enob_7')
main_main_tmp13_enob_8 = solver.IntVar(0, 1, 'main_main_tmp13_enob_8')
solver.Add( + (1)*main_main_tmp13_enob_1 + (1)*main_main_tmp13_enob_4 + (1)*main_main_tmp13_enob_5 + (1)*main_main_tmp13_enob_6 + (1)*main_main_tmp13_enob_7 + (1)*main_main_tmp13_enob_8==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp13 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp13_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp13 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp13_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp13 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp13_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp13 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp13 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_7<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul222 = fmul double %tmp12, %tmp13, !taffo.info !81, !taffo.initweight !28
main_A_CAST_mul222_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul222_fixbits')
main_A_CAST_mul222_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul222_fixp')
main_A_CAST_mul222_float = solver.IntVar(0, 1, 'main_A_CAST_mul222_float')
main_A_CAST_mul222_double = solver.IntVar(0, 1, 'main_A_CAST_mul222_double')
solver.Add( + (1)*main_A_CAST_mul222_fixp + (1)*main_A_CAST_mul222_float + (1)*main_A_CAST_mul222_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul222_fixbits + (-10000)*main_A_CAST_mul222_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul222')
C2_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul222')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul222_fixbits + (-10000)*C1_main_A_CAST_mul222<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul222_fixbits + (-10000)*C2_main_A_CAST_mul222<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul222
castCostObj +=  + (1)*C2_main_A_CAST_mul222
C3_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul222')
C4_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul222')
C5_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul222')
C6_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul222')
C7_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul222')
C8_main_A_CAST_mul222 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul222')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul222_float + (-1)*C3_main_A_CAST_mul222<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul222
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul222_fixp + (-1)*C4_main_A_CAST_mul222<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul222
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul222_double + (-1)*C5_main_A_CAST_mul222<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul222
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul222_fixp + (-1)*C6_main_A_CAST_mul222<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul222
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul222_double + (-1)*C7_main_A_CAST_mul222<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul222
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul222_float + (-1)*C8_main_A_CAST_mul222<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul222



#Constraint for cast for   %mul222 = fmul double %tmp12, %tmp13, !taffo.info !81, !taffo.initweight !28
main_y_CAST_mul222_fixbits = solver.IntVar(0, 28, 'main_y_CAST_mul222_fixbits')
main_y_CAST_mul222_fixp = solver.IntVar(0, 1, 'main_y_CAST_mul222_fixp')
main_y_CAST_mul222_float = solver.IntVar(0, 1, 'main_y_CAST_mul222_float')
main_y_CAST_mul222_double = solver.IntVar(0, 1, 'main_y_CAST_mul222_double')
solver.Add( + (1)*main_y_CAST_mul222_fixp + (1)*main_y_CAST_mul222_float + (1)*main_y_CAST_mul222_double==1)    #exactly 1 type
solver.Add( + (1)*main_y_CAST_mul222_fixbits + (-10000)*main_y_CAST_mul222_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C1_main_y_CAST_mul222')
C2_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C2_main_y_CAST_mul222')
solver.Add( + (1)*main_y_fixbits + (-1)*main_y_CAST_mul222_fixbits + (-10000)*C1_main_y_CAST_mul222<=0)    #Shift cost 1
solver.Add( + (-1)*main_y_fixbits + (1)*main_y_CAST_mul222_fixbits + (-10000)*C2_main_y_CAST_mul222<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y_CAST_mul222
castCostObj +=  + (1)*C2_main_y_CAST_mul222
C3_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C3_main_y_CAST_mul222')
C4_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C4_main_y_CAST_mul222')
C5_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C5_main_y_CAST_mul222')
C6_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C6_main_y_CAST_mul222')
C7_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C7_main_y_CAST_mul222')
C8_main_y_CAST_mul222 = solver.IntVar(0, 1, 'C8_main_y_CAST_mul222')
solver.Add( + (1)*main_y_fixp + (1)*main_y_CAST_mul222_float + (-1)*C3_main_y_CAST_mul222<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y_CAST_mul222
solver.Add( + (1)*main_y_float + (1)*main_y_CAST_mul222_fixp + (-1)*C4_main_y_CAST_mul222<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y_CAST_mul222
solver.Add( + (1)*main_y_fixp + (1)*main_y_CAST_mul222_double + (-1)*C5_main_y_CAST_mul222<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y_CAST_mul222
solver.Add( + (1)*main_y_double + (1)*main_y_CAST_mul222_fixp + (-1)*C6_main_y_CAST_mul222<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y_CAST_mul222
solver.Add( + (1)*main_y_float + (1)*main_y_CAST_mul222_double + (-1)*C7_main_y_CAST_mul222<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y_CAST_mul222
solver.Add( + (1)*main_y_double + (1)*main_y_CAST_mul222_float + (-1)*C8_main_y_CAST_mul222<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y_CAST_mul222



#Stuff for   %mul222 = fmul double %tmp12, %tmp13, !taffo.info !81, !taffo.initweight !28
main_mul222_fixbits = solver.IntVar(0, 27, 'main_mul222_fixbits')
main_mul222_fixp = solver.IntVar(0, 1, 'main_mul222_fixp')
main_mul222_float = solver.IntVar(0, 1, 'main_mul222_float')
main_mul222_double = solver.IntVar(0, 1, 'main_mul222_double')
main_mul222_enob = solver.IntVar(-10000, 10000, 'main_mul222_enob')
solver.Add( + (1)*main_mul222_enob + (-1)*main_mul222_fixbits + (10000)*main_mul222_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul222_enob + (10000)*main_mul222_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul222_enob + (10000)*main_mul222_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul222_fixbits + (-10000)*main_mul222_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_mul222_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul222_enob
solver.Add( + (1)*main_mul222_fixp + (1)*main_mul222_float + (1)*main_mul222_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul222_fixbits + (-10000)*main_mul222_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul222_fixp + (-1)*main_y_CAST_mul222_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul222_float + (-1)*main_y_CAST_mul222_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul222_double + (-1)*main_y_CAST_mul222_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul222_fixp + (-1)*main_mul222_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul222_float + (-1)*main_mul222_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul222_double + (-1)*main_mul222_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul222_fixp
mathCostObj +=  + (6)*main_mul222_float
mathCostObj +=  + (12.2551)*main_mul222_double
main_main_mul222_enob_1 = solver.IntVar(0, 1, 'main_main_mul222_enob_1')
main_main_mul222_enob_2 = solver.IntVar(0, 1, 'main_main_mul222_enob_2')
solver.Add( + (1)*main_main_mul222_enob_1 + (1)*main_main_mul222_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul222_enob + (-1)*main_y_enob_memphi_main_tmp13 + (-10000)*main_main_mul222_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul222_enob + (-1)*main_A_enob_memphi_main_tmp12 + (-10000)*main_main_mul222_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub223 = fsub double %w.2, %mul222, !taffo.info !83, !taffo.initweight !27
main_w_2_CAST_sub223_fixbits = solver.IntVar(0, 28, 'main_w_2_CAST_sub223_fixbits')
main_w_2_CAST_sub223_fixp = solver.IntVar(0, 1, 'main_w_2_CAST_sub223_fixp')
main_w_2_CAST_sub223_float = solver.IntVar(0, 1, 'main_w_2_CAST_sub223_float')
main_w_2_CAST_sub223_double = solver.IntVar(0, 1, 'main_w_2_CAST_sub223_double')
solver.Add( + (1)*main_w_2_CAST_sub223_fixp + (1)*main_w_2_CAST_sub223_float + (1)*main_w_2_CAST_sub223_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_2_CAST_sub223_fixbits + (-10000)*main_w_2_CAST_sub223_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C1_main_w_2_CAST_sub223')
C2_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C2_main_w_2_CAST_sub223')
solver.Add( + (1)*main_w_2_fixbits + (-1)*main_w_2_CAST_sub223_fixbits + (-10000)*C1_main_w_2_CAST_sub223<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_2_fixbits + (1)*main_w_2_CAST_sub223_fixbits + (-10000)*C2_main_w_2_CAST_sub223<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_2_CAST_sub223
castCostObj +=  + (1)*C2_main_w_2_CAST_sub223
C3_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C3_main_w_2_CAST_sub223')
C4_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C4_main_w_2_CAST_sub223')
C5_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C5_main_w_2_CAST_sub223')
C6_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C6_main_w_2_CAST_sub223')
C7_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C7_main_w_2_CAST_sub223')
C8_main_w_2_CAST_sub223 = solver.IntVar(0, 1, 'C8_main_w_2_CAST_sub223')
solver.Add( + (1)*main_w_2_fixp + (1)*main_w_2_CAST_sub223_float + (-1)*C3_main_w_2_CAST_sub223<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_2_CAST_sub223
solver.Add( + (1)*main_w_2_float + (1)*main_w_2_CAST_sub223_fixp + (-1)*C4_main_w_2_CAST_sub223<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_2_CAST_sub223
solver.Add( + (1)*main_w_2_fixp + (1)*main_w_2_CAST_sub223_double + (-1)*C5_main_w_2_CAST_sub223<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_2_CAST_sub223
solver.Add( + (1)*main_w_2_double + (1)*main_w_2_CAST_sub223_fixp + (-1)*C6_main_w_2_CAST_sub223<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_2_CAST_sub223
solver.Add( + (1)*main_w_2_float + (1)*main_w_2_CAST_sub223_double + (-1)*C7_main_w_2_CAST_sub223<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_2_CAST_sub223
solver.Add( + (1)*main_w_2_double + (1)*main_w_2_CAST_sub223_float + (-1)*C8_main_w_2_CAST_sub223<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_2_CAST_sub223



#Constraint for cast for   %sub223 = fsub double %w.2, %mul222, !taffo.info !83, !taffo.initweight !27
main_mul222_CAST_sub223_fixbits = solver.IntVar(0, 27, 'main_mul222_CAST_sub223_fixbits')
main_mul222_CAST_sub223_fixp = solver.IntVar(0, 1, 'main_mul222_CAST_sub223_fixp')
main_mul222_CAST_sub223_float = solver.IntVar(0, 1, 'main_mul222_CAST_sub223_float')
main_mul222_CAST_sub223_double = solver.IntVar(0, 1, 'main_mul222_CAST_sub223_double')
solver.Add( + (1)*main_mul222_CAST_sub223_fixp + (1)*main_mul222_CAST_sub223_float + (1)*main_mul222_CAST_sub223_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul222_CAST_sub223_fixbits + (-10000)*main_mul222_CAST_sub223_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C1_main_mul222_CAST_sub223')
C2_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C2_main_mul222_CAST_sub223')
solver.Add( + (1)*main_mul222_fixbits + (-1)*main_mul222_CAST_sub223_fixbits + (-10000)*C1_main_mul222_CAST_sub223<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul222_fixbits + (1)*main_mul222_CAST_sub223_fixbits + (-10000)*C2_main_mul222_CAST_sub223<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul222_CAST_sub223
castCostObj +=  + (1)*C2_main_mul222_CAST_sub223
C3_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C3_main_mul222_CAST_sub223')
C4_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C4_main_mul222_CAST_sub223')
C5_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C5_main_mul222_CAST_sub223')
C6_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C6_main_mul222_CAST_sub223')
C7_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C7_main_mul222_CAST_sub223')
C8_main_mul222_CAST_sub223 = solver.IntVar(0, 1, 'C8_main_mul222_CAST_sub223')
solver.Add( + (1)*main_mul222_fixp + (1)*main_mul222_CAST_sub223_float + (-1)*C3_main_mul222_CAST_sub223<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul222_CAST_sub223
solver.Add( + (1)*main_mul222_float + (1)*main_mul222_CAST_sub223_fixp + (-1)*C4_main_mul222_CAST_sub223<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul222_CAST_sub223
solver.Add( + (1)*main_mul222_fixp + (1)*main_mul222_CAST_sub223_double + (-1)*C5_main_mul222_CAST_sub223<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul222_CAST_sub223
solver.Add( + (1)*main_mul222_double + (1)*main_mul222_CAST_sub223_fixp + (-1)*C6_main_mul222_CAST_sub223<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul222_CAST_sub223
solver.Add( + (1)*main_mul222_float + (1)*main_mul222_CAST_sub223_double + (-1)*C7_main_mul222_CAST_sub223<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul222_CAST_sub223
solver.Add( + (1)*main_mul222_double + (1)*main_mul222_CAST_sub223_float + (-1)*C8_main_mul222_CAST_sub223<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul222_CAST_sub223



#Stuff for   %sub223 = fsub double %w.2, %mul222, !taffo.info !83, !taffo.initweight !27
main_sub223_fixbits = solver.IntVar(0, 28, 'main_sub223_fixbits')
main_sub223_fixp = solver.IntVar(0, 1, 'main_sub223_fixp')
main_sub223_float = solver.IntVar(0, 1, 'main_sub223_float')
main_sub223_double = solver.IntVar(0, 1, 'main_sub223_double')
main_sub223_enob = solver.IntVar(-10000, 10000, 'main_sub223_enob')
solver.Add( + (1)*main_sub223_enob + (-1)*main_sub223_fixbits + (10000)*main_sub223_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub223_enob + (10000)*main_sub223_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub223_enob + (10000)*main_sub223_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub223_fixbits + (-10000)*main_sub223_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_sub223_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub223_enob
solver.Add( + (1)*main_sub223_fixp + (1)*main_sub223_float + (1)*main_sub223_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub223_fixbits + (-10000)*main_sub223_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %w.2 = phi double [ %tmp11, %for.body209 ], [ %sub223, %for.inc224 ], !taffo.info !80
main_sub223_CAST_w_2_fixbits = solver.IntVar(0, 28, 'main_sub223_CAST_w_2_fixbits')
main_sub223_CAST_w_2_fixp = solver.IntVar(0, 1, 'main_sub223_CAST_w_2_fixp')
main_sub223_CAST_w_2_float = solver.IntVar(0, 1, 'main_sub223_CAST_w_2_float')
main_sub223_CAST_w_2_double = solver.IntVar(0, 1, 'main_sub223_CAST_w_2_double')
solver.Add( + (1)*main_sub223_CAST_w_2_fixp + (1)*main_sub223_CAST_w_2_float + (1)*main_sub223_CAST_w_2_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub223_CAST_w_2_fixbits + (-10000)*main_sub223_CAST_w_2_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C1_main_sub223_CAST_w_2')
C2_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C2_main_sub223_CAST_w_2')
solver.Add( + (1)*main_sub223_fixbits + (-1)*main_sub223_CAST_w_2_fixbits + (-10000)*C1_main_sub223_CAST_w_2<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub223_fixbits + (1)*main_sub223_CAST_w_2_fixbits + (-10000)*C2_main_sub223_CAST_w_2<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub223_CAST_w_2
castCostObj +=  + (1)*C2_main_sub223_CAST_w_2
C3_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C3_main_sub223_CAST_w_2')
C4_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C4_main_sub223_CAST_w_2')
C5_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C5_main_sub223_CAST_w_2')
C6_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C6_main_sub223_CAST_w_2')
C7_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C7_main_sub223_CAST_w_2')
C8_main_sub223_CAST_w_2 = solver.IntVar(0, 1, 'C8_main_sub223_CAST_w_2')
solver.Add( + (1)*main_sub223_fixp + (1)*main_sub223_CAST_w_2_float + (-1)*C3_main_sub223_CAST_w_2<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub223_CAST_w_2
solver.Add( + (1)*main_sub223_float + (1)*main_sub223_CAST_w_2_fixp + (-1)*C4_main_sub223_CAST_w_2<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub223_CAST_w_2
solver.Add( + (1)*main_sub223_fixp + (1)*main_sub223_CAST_w_2_double + (-1)*C5_main_sub223_CAST_w_2<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub223_CAST_w_2
solver.Add( + (1)*main_sub223_double + (1)*main_sub223_CAST_w_2_fixp + (-1)*C6_main_sub223_CAST_w_2<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub223_CAST_w_2
solver.Add( + (1)*main_sub223_float + (1)*main_sub223_CAST_w_2_double + (-1)*C7_main_sub223_CAST_w_2<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub223_CAST_w_2
solver.Add( + (1)*main_sub223_double + (1)*main_sub223_CAST_w_2_float + (-1)*C8_main_sub223_CAST_w_2<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub223_CAST_w_2
solver.Add( + (1)*main_w_2_fixp + (-1)*main_sub223_CAST_w_2_fixp==0)    #fix equality
solver.Add( + (1)*main_w_2_float + (-1)*main_sub223_CAST_w_2_float==0)    #float equality
solver.Add( + (1)*main_w_2_double + (-1)*main_sub223_CAST_w_2_double==0)    #double equality
solver.Add( + (1)*main_w_2_fixbits + (-1)*main_sub223_CAST_w_2_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_2_enob + (-1)*main_sub223_enob + (10000)*main_main_w_2_enob_1<=10000)    #Enob: forcing phi enob
solver.Add( + (1)*main_w_2_CAST_sub223_fixp + (-1)*main_mul222_CAST_sub223_fixp==0)    #fix equality
solver.Add( + (1)*main_w_2_CAST_sub223_float + (-1)*main_mul222_CAST_sub223_float==0)    #float equality
solver.Add( + (1)*main_w_2_CAST_sub223_double + (-1)*main_mul222_CAST_sub223_double==0)    #double equality
solver.Add( + (1)*main_w_2_CAST_sub223_fixbits + (-1)*main_mul222_CAST_sub223_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_2_CAST_sub223_fixp + (-1)*main_sub223_fixp==0)    #fix equality
solver.Add( + (1)*main_w_2_CAST_sub223_float + (-1)*main_sub223_float==0)    #float equality
solver.Add( + (1)*main_w_2_CAST_sub223_double + (-1)*main_sub223_double==0)    #double equality
solver.Add( + (1)*main_w_2_CAST_sub223_fixbits + (-1)*main_sub223_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub223_fixp
mathCostObj +=  + (3)*main_sub223_float
mathCostObj +=  + (6.64928)*main_sub223_double
solver.Add( + (1)*main_sub223_enob + (-1)*main_w_2_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub223_enob + (-1)*main_mul222_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %w.2, double* %arrayidx228, align 8, !taffo.info !29, !taffo.initweight !27
main_w_2_CAST_store_fixbits = solver.IntVar(0, 28, 'main_w_2_CAST_store_fixbits')
main_w_2_CAST_store_fixp = solver.IntVar(0, 1, 'main_w_2_CAST_store_fixp')
main_w_2_CAST_store_float = solver.IntVar(0, 1, 'main_w_2_CAST_store_float')
main_w_2_CAST_store_double = solver.IntVar(0, 1, 'main_w_2_CAST_store_double')
solver.Add( + (1)*main_w_2_CAST_store_fixp + (1)*main_w_2_CAST_store_float + (1)*main_w_2_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_2_CAST_store_fixbits + (-10000)*main_w_2_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_2_CAST_store = solver.IntVar(0, 1, 'C1_main_w_2_CAST_store')
C2_main_w_2_CAST_store = solver.IntVar(0, 1, 'C2_main_w_2_CAST_store')
solver.Add( + (1)*main_w_2_fixbits + (-1)*main_w_2_CAST_store_fixbits + (-10000)*C1_main_w_2_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_2_fixbits + (1)*main_w_2_CAST_store_fixbits + (-10000)*C2_main_w_2_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_2_CAST_store
castCostObj +=  + (1)*C2_main_w_2_CAST_store
C3_main_w_2_CAST_store = solver.IntVar(0, 1, 'C3_main_w_2_CAST_store')
C4_main_w_2_CAST_store = solver.IntVar(0, 1, 'C4_main_w_2_CAST_store')
C5_main_w_2_CAST_store = solver.IntVar(0, 1, 'C5_main_w_2_CAST_store')
C6_main_w_2_CAST_store = solver.IntVar(0, 1, 'C6_main_w_2_CAST_store')
C7_main_w_2_CAST_store = solver.IntVar(0, 1, 'C7_main_w_2_CAST_store')
C8_main_w_2_CAST_store = solver.IntVar(0, 1, 'C8_main_w_2_CAST_store')
solver.Add( + (1)*main_w_2_fixp + (1)*main_w_2_CAST_store_float + (-1)*C3_main_w_2_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_2_CAST_store
solver.Add( + (1)*main_w_2_float + (1)*main_w_2_CAST_store_fixp + (-1)*C4_main_w_2_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_2_CAST_store
solver.Add( + (1)*main_w_2_fixp + (1)*main_w_2_CAST_store_double + (-1)*C5_main_w_2_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_2_CAST_store
solver.Add( + (1)*main_w_2_double + (1)*main_w_2_CAST_store_fixp + (-1)*C6_main_w_2_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_2_CAST_store
solver.Add( + (1)*main_w_2_float + (1)*main_w_2_CAST_store_double + (-1)*C7_main_w_2_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_2_CAST_store
solver.Add( + (1)*main_w_2_double + (1)*main_w_2_CAST_store_float + (-1)*C8_main_w_2_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_2_CAST_store
solver.Add( + (1)*main_y_fixp + (-1)*main_w_2_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_y_float + (-1)*main_w_2_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_y_double + (-1)*main_w_2_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_y_fixbits + (-1)*main_w_2_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_y_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_y_enob_storeENOB')
solver.Add( + (1)*main_y_enob_storeENOB + (-1)*main_y_fixbits + (10000)*main_y_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_y_enob_storeENOB + (10000)*main_y_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_y_enob_storeENOB + (10000)*main_y_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_y_enob_storeENOB + (-1)*main_w_2_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp13 + (-1)*main_y_enob_storeENOB + (10000)*main_main_tmp13_enob_8<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_y_enob_memphi_main_tmp14 = solver.IntVar(-10000, 10000, 'main_y_enob_memphi_main_tmp14')
solver.Add( + (1)*main_y_enob_memphi_main_tmp14 + (-1)*main_y_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp14_enob_1 = solver.IntVar(0, 1, 'main_main_tmp14_enob_1')
main_main_tmp14_enob_4 = solver.IntVar(0, 1, 'main_main_tmp14_enob_4')
main_main_tmp14_enob_5 = solver.IntVar(0, 1, 'main_main_tmp14_enob_5')
main_main_tmp14_enob_6 = solver.IntVar(0, 1, 'main_main_tmp14_enob_6')
main_main_tmp14_enob_7 = solver.IntVar(0, 1, 'main_main_tmp14_enob_7')
main_main_tmp14_enob_8 = solver.IntVar(0, 1, 'main_main_tmp14_enob_8')
solver.Add( + (1)*main_main_tmp14_enob_1 + (1)*main_main_tmp14_enob_4 + (1)*main_main_tmp14_enob_5 + (1)*main_main_tmp14_enob_6 + (1)*main_main_tmp14_enob_7 + (1)*main_main_tmp14_enob_8==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp14 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp14_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp14 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp14_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp14 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp14_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp14 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp14_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp14 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp14_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_y_enob_memphi_main_tmp14 + (-1)*main_y_enob_storeENOB + (10000)*main_main_tmp14_enob_8<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %w.3 = phi double [ %tmp14, %for.body235 ], [ %sub250, %for.inc251 ], !taffo.info !80
main_w_3_fixbits = solver.IntVar(0, 28, 'main_w_3_fixbits')
main_w_3_fixp = solver.IntVar(0, 1, 'main_w_3_fixp')
main_w_3_float = solver.IntVar(0, 1, 'main_w_3_float')
main_w_3_double = solver.IntVar(0, 1, 'main_w_3_double')
main_w_3_enob = solver.IntVar(-10000, 10000, 'main_w_3_enob')
solver.Add( + (1)*main_w_3_enob + (-1)*main_w_3_fixbits + (10000)*main_w_3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_w_3_enob + (10000)*main_w_3_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_w_3_enob + (10000)*main_w_3_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_w_3_fixbits + (-10000)*main_w_3_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_w_3_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_w_3_enob
solver.Add( + (1)*main_w_3_fixp + (1)*main_w_3_float + (1)*main_w_3_double==1)    #Exactly one selected type
solver.Add( + (1)*main_w_3_fixbits + (-10000)*main_w_3_fixp<=0)    #If not fix, frac part to zero
main_main_w_3_enob_0 = solver.IntVar(0, 1, 'main_main_w_3_enob_0')
main_main_w_3_enob_1 = solver.IntVar(0, 1, 'main_main_w_3_enob_1')
solver.Add( + (1)*main_main_w_3_enob_0 + (1)*main_main_w_3_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %w.3 = phi double [ %tmp14, %for.body235 ], [ %sub250, %for.inc251 ], !taffo.info !80
main_y_CAST_w_3_fixbits = solver.IntVar(0, 28, 'main_y_CAST_w_3_fixbits')
main_y_CAST_w_3_fixp = solver.IntVar(0, 1, 'main_y_CAST_w_3_fixp')
main_y_CAST_w_3_float = solver.IntVar(0, 1, 'main_y_CAST_w_3_float')
main_y_CAST_w_3_double = solver.IntVar(0, 1, 'main_y_CAST_w_3_double')
solver.Add( + (1)*main_y_CAST_w_3_fixp + (1)*main_y_CAST_w_3_float + (1)*main_y_CAST_w_3_double==1)    #exactly 1 type
solver.Add( + (1)*main_y_CAST_w_3_fixbits + (-10000)*main_y_CAST_w_3_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C1_main_y_CAST_w_3')
C2_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C2_main_y_CAST_w_3')
solver.Add( + (1)*main_y_fixbits + (-1)*main_y_CAST_w_3_fixbits + (-10000)*C1_main_y_CAST_w_3<=0)    #Shift cost 1
solver.Add( + (-1)*main_y_fixbits + (1)*main_y_CAST_w_3_fixbits + (-10000)*C2_main_y_CAST_w_3<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y_CAST_w_3
castCostObj +=  + (1)*C2_main_y_CAST_w_3
C3_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C3_main_y_CAST_w_3')
C4_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C4_main_y_CAST_w_3')
C5_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C5_main_y_CAST_w_3')
C6_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C6_main_y_CAST_w_3')
C7_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C7_main_y_CAST_w_3')
C8_main_y_CAST_w_3 = solver.IntVar(0, 1, 'C8_main_y_CAST_w_3')
solver.Add( + (1)*main_y_fixp + (1)*main_y_CAST_w_3_float + (-1)*C3_main_y_CAST_w_3<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y_CAST_w_3
solver.Add( + (1)*main_y_float + (1)*main_y_CAST_w_3_fixp + (-1)*C4_main_y_CAST_w_3<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y_CAST_w_3
solver.Add( + (1)*main_y_fixp + (1)*main_y_CAST_w_3_double + (-1)*C5_main_y_CAST_w_3<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y_CAST_w_3
solver.Add( + (1)*main_y_double + (1)*main_y_CAST_w_3_fixp + (-1)*C6_main_y_CAST_w_3<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y_CAST_w_3
solver.Add( + (1)*main_y_float + (1)*main_y_CAST_w_3_double + (-1)*C7_main_y_CAST_w_3<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y_CAST_w_3
solver.Add( + (1)*main_y_double + (1)*main_y_CAST_w_3_float + (-1)*C8_main_y_CAST_w_3<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y_CAST_w_3
solver.Add( + (1)*main_w_3_fixp + (-1)*main_y_CAST_w_3_fixp==0)    #fix equality
solver.Add( + (1)*main_w_3_float + (-1)*main_y_CAST_w_3_float==0)    #float equality
solver.Add( + (1)*main_w_3_double + (-1)*main_y_CAST_w_3_double==0)    #double equality
solver.Add( + (1)*main_w_3_fixbits + (-1)*main_y_CAST_w_3_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_3_enob + (-1)*main_y_enob_memphi_main_tmp14 + (10000)*main_main_w_3_enob_0<=10000)    #Enob: forcing phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp15 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp15')
solver.Add( + (1)*main_A_enob_memphi_main_tmp15 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp15_enob_1 = solver.IntVar(0, 1, 'main_main_tmp15_enob_1')
main_main_tmp15_enob_4 = solver.IntVar(0, 1, 'main_main_tmp15_enob_4')
main_main_tmp15_enob_5 = solver.IntVar(0, 1, 'main_main_tmp15_enob_5')
main_main_tmp15_enob_6 = solver.IntVar(0, 1, 'main_main_tmp15_enob_6')
main_main_tmp15_enob_7 = solver.IntVar(0, 1, 'main_main_tmp15_enob_7')
solver.Add( + (1)*main_main_tmp15_enob_1 + (1)*main_main_tmp15_enob_4 + (1)*main_main_tmp15_enob_5 + (1)*main_main_tmp15_enob_6 + (1)*main_main_tmp15_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp15 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp15_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp15 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp15_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp15 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp15_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp15 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp15_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp15 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp15_enob_7<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_x_enob_memphi_main_tmp16 = solver.IntVar(-10000, 10000, 'main_x_enob_memphi_main_tmp16')
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_x_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp16_enob_1 = solver.IntVar(0, 1, 'main_main_tmp16_enob_1')
main_main_tmp16_enob_4 = solver.IntVar(0, 1, 'main_main_tmp16_enob_4')
main_main_tmp16_enob_5 = solver.IntVar(0, 1, 'main_main_tmp16_enob_5')
main_main_tmp16_enob_6 = solver.IntVar(0, 1, 'main_main_tmp16_enob_6')
main_main_tmp16_enob_7 = solver.IntVar(0, 1, 'main_main_tmp16_enob_7')
main_main_tmp16_enob_8 = solver.IntVar(0, 1, 'main_main_tmp16_enob_8')
main_main_tmp16_enob_9 = solver.IntVar(0, 1, 'main_main_tmp16_enob_9')
solver.Add( + (1)*main_main_tmp16_enob_1 + (1)*main_main_tmp16_enob_4 + (1)*main_main_tmp16_enob_5 + (1)*main_main_tmp16_enob_6 + (1)*main_main_tmp16_enob_7 + (1)*main_main_tmp16_enob_8 + (1)*main_main_tmp16_enob_9==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp16_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp16_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp16_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_y_enob_storeENOB + (10000)*main_main_tmp16_enob_8<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul249 = fmul double %tmp15, %tmp16, !taffo.info !84, !taffo.initweight !28
main_A_CAST_mul249_fixbits = solver.IntVar(0, 29, 'main_A_CAST_mul249_fixbits')
main_A_CAST_mul249_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul249_fixp')
main_A_CAST_mul249_float = solver.IntVar(0, 1, 'main_A_CAST_mul249_float')
main_A_CAST_mul249_double = solver.IntVar(0, 1, 'main_A_CAST_mul249_double')
solver.Add( + (1)*main_A_CAST_mul249_fixp + (1)*main_A_CAST_mul249_float + (1)*main_A_CAST_mul249_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul249_fixbits + (-10000)*main_A_CAST_mul249_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul249')
C2_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul249')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul249_fixbits + (-10000)*C1_main_A_CAST_mul249<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul249_fixbits + (-10000)*C2_main_A_CAST_mul249<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul249
castCostObj +=  + (1)*C2_main_A_CAST_mul249
C3_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul249')
C4_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul249')
C5_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul249')
C6_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul249')
C7_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul249')
C8_main_A_CAST_mul249 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul249')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul249_float + (-1)*C3_main_A_CAST_mul249<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul249
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul249_fixp + (-1)*C4_main_A_CAST_mul249<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul249
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul249_double + (-1)*C5_main_A_CAST_mul249<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul249
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul249_fixp + (-1)*C6_main_A_CAST_mul249<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul249
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul249_double + (-1)*C7_main_A_CAST_mul249<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul249
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul249_float + (-1)*C8_main_A_CAST_mul249<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul249



#Constraint for cast for   %mul249 = fmul double %tmp15, %tmp16, !taffo.info !84, !taffo.initweight !28
main_x_CAST_mul249_fixbits = solver.IntVar(0, 29, 'main_x_CAST_mul249_fixbits')
main_x_CAST_mul249_fixp = solver.IntVar(0, 1, 'main_x_CAST_mul249_fixp')
main_x_CAST_mul249_float = solver.IntVar(0, 1, 'main_x_CAST_mul249_float')
main_x_CAST_mul249_double = solver.IntVar(0, 1, 'main_x_CAST_mul249_double')
solver.Add( + (1)*main_x_CAST_mul249_fixp + (1)*main_x_CAST_mul249_float + (1)*main_x_CAST_mul249_double==1)    #exactly 1 type
solver.Add( + (1)*main_x_CAST_mul249_fixbits + (-10000)*main_x_CAST_mul249_fixp<=0)    #If no fix, fix frac part = 0
C1_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C1_main_x_CAST_mul249')
C2_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C2_main_x_CAST_mul249')
solver.Add( + (1)*main_x_fixbits + (-1)*main_x_CAST_mul249_fixbits + (-10000)*C1_main_x_CAST_mul249<=0)    #Shift cost 1
solver.Add( + (-1)*main_x_fixbits + (1)*main_x_CAST_mul249_fixbits + (-10000)*C2_main_x_CAST_mul249<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_x_CAST_mul249
castCostObj +=  + (1)*C2_main_x_CAST_mul249
C3_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C3_main_x_CAST_mul249')
C4_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C4_main_x_CAST_mul249')
C5_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C5_main_x_CAST_mul249')
C6_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C6_main_x_CAST_mul249')
C7_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C7_main_x_CAST_mul249')
C8_main_x_CAST_mul249 = solver.IntVar(0, 1, 'C8_main_x_CAST_mul249')
solver.Add( + (1)*main_x_fixp + (1)*main_x_CAST_mul249_float + (-1)*C3_main_x_CAST_mul249<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_x_CAST_mul249
solver.Add( + (1)*main_x_float + (1)*main_x_CAST_mul249_fixp + (-1)*C4_main_x_CAST_mul249<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_x_CAST_mul249
solver.Add( + (1)*main_x_fixp + (1)*main_x_CAST_mul249_double + (-1)*C5_main_x_CAST_mul249<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_x_CAST_mul249
solver.Add( + (1)*main_x_double + (1)*main_x_CAST_mul249_fixp + (-1)*C6_main_x_CAST_mul249<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_x_CAST_mul249
solver.Add( + (1)*main_x_float + (1)*main_x_CAST_mul249_double + (-1)*C7_main_x_CAST_mul249<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_x_CAST_mul249
solver.Add( + (1)*main_x_double + (1)*main_x_CAST_mul249_float + (-1)*C8_main_x_CAST_mul249<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_x_CAST_mul249



#Stuff for   %mul249 = fmul double %tmp15, %tmp16, !taffo.info !84, !taffo.initweight !28
main_mul249_fixbits = solver.IntVar(0, 28, 'main_mul249_fixbits')
main_mul249_fixp = solver.IntVar(0, 1, 'main_mul249_fixp')
main_mul249_float = solver.IntVar(0, 1, 'main_mul249_float')
main_mul249_double = solver.IntVar(0, 1, 'main_mul249_double')
main_mul249_enob = solver.IntVar(-10000, 10000, 'main_mul249_enob')
solver.Add( + (1)*main_mul249_enob + (-1)*main_mul249_fixbits + (10000)*main_mul249_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul249_enob + (10000)*main_mul249_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul249_enob + (10000)*main_mul249_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul249_fixbits + (-10000)*main_mul249_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_mul249_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul249_enob
solver.Add( + (1)*main_mul249_fixp + (1)*main_mul249_float + (1)*main_mul249_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul249_fixbits + (-10000)*main_mul249_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul249_fixp + (-1)*main_x_CAST_mul249_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul249_float + (-1)*main_x_CAST_mul249_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul249_double + (-1)*main_x_CAST_mul249_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul249_fixp + (-1)*main_mul249_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul249_float + (-1)*main_mul249_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul249_double + (-1)*main_mul249_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul249_fixp
mathCostObj +=  + (6)*main_mul249_float
mathCostObj +=  + (12.2551)*main_mul249_double
main_main_mul249_enob_1 = solver.IntVar(0, 1, 'main_main_mul249_enob_1')
main_main_mul249_enob_2 = solver.IntVar(0, 1, 'main_main_mul249_enob_2')
solver.Add( + (1)*main_main_mul249_enob_1 + (1)*main_main_mul249_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul249_enob + (-1)*main_x_enob_memphi_main_tmp16 + (-10000)*main_main_mul249_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul249_enob + (-1)*main_A_enob_memphi_main_tmp15 + (-10000)*main_main_mul249_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub250 = fsub double %w.3, %mul249, !taffo.info !83, !taffo.initweight !27
main_w_3_CAST_sub250_fixbits = solver.IntVar(0, 28, 'main_w_3_CAST_sub250_fixbits')
main_w_3_CAST_sub250_fixp = solver.IntVar(0, 1, 'main_w_3_CAST_sub250_fixp')
main_w_3_CAST_sub250_float = solver.IntVar(0, 1, 'main_w_3_CAST_sub250_float')
main_w_3_CAST_sub250_double = solver.IntVar(0, 1, 'main_w_3_CAST_sub250_double')
solver.Add( + (1)*main_w_3_CAST_sub250_fixp + (1)*main_w_3_CAST_sub250_float + (1)*main_w_3_CAST_sub250_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_3_CAST_sub250_fixbits + (-10000)*main_w_3_CAST_sub250_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C1_main_w_3_CAST_sub250')
C2_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C2_main_w_3_CAST_sub250')
solver.Add( + (1)*main_w_3_fixbits + (-1)*main_w_3_CAST_sub250_fixbits + (-10000)*C1_main_w_3_CAST_sub250<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_3_fixbits + (1)*main_w_3_CAST_sub250_fixbits + (-10000)*C2_main_w_3_CAST_sub250<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_3_CAST_sub250
castCostObj +=  + (1)*C2_main_w_3_CAST_sub250
C3_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C3_main_w_3_CAST_sub250')
C4_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C4_main_w_3_CAST_sub250')
C5_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C5_main_w_3_CAST_sub250')
C6_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C6_main_w_3_CAST_sub250')
C7_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C7_main_w_3_CAST_sub250')
C8_main_w_3_CAST_sub250 = solver.IntVar(0, 1, 'C8_main_w_3_CAST_sub250')
solver.Add( + (1)*main_w_3_fixp + (1)*main_w_3_CAST_sub250_float + (-1)*C3_main_w_3_CAST_sub250<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_3_CAST_sub250
solver.Add( + (1)*main_w_3_float + (1)*main_w_3_CAST_sub250_fixp + (-1)*C4_main_w_3_CAST_sub250<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_3_CAST_sub250
solver.Add( + (1)*main_w_3_fixp + (1)*main_w_3_CAST_sub250_double + (-1)*C5_main_w_3_CAST_sub250<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_3_CAST_sub250
solver.Add( + (1)*main_w_3_double + (1)*main_w_3_CAST_sub250_fixp + (-1)*C6_main_w_3_CAST_sub250<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_3_CAST_sub250
solver.Add( + (1)*main_w_3_float + (1)*main_w_3_CAST_sub250_double + (-1)*C7_main_w_3_CAST_sub250<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_3_CAST_sub250
solver.Add( + (1)*main_w_3_double + (1)*main_w_3_CAST_sub250_float + (-1)*C8_main_w_3_CAST_sub250<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_3_CAST_sub250



#Constraint for cast for   %sub250 = fsub double %w.3, %mul249, !taffo.info !83, !taffo.initweight !27
main_mul249_CAST_sub250_fixbits = solver.IntVar(0, 28, 'main_mul249_CAST_sub250_fixbits')
main_mul249_CAST_sub250_fixp = solver.IntVar(0, 1, 'main_mul249_CAST_sub250_fixp')
main_mul249_CAST_sub250_float = solver.IntVar(0, 1, 'main_mul249_CAST_sub250_float')
main_mul249_CAST_sub250_double = solver.IntVar(0, 1, 'main_mul249_CAST_sub250_double')
solver.Add( + (1)*main_mul249_CAST_sub250_fixp + (1)*main_mul249_CAST_sub250_float + (1)*main_mul249_CAST_sub250_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul249_CAST_sub250_fixbits + (-10000)*main_mul249_CAST_sub250_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C1_main_mul249_CAST_sub250')
C2_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C2_main_mul249_CAST_sub250')
solver.Add( + (1)*main_mul249_fixbits + (-1)*main_mul249_CAST_sub250_fixbits + (-10000)*C1_main_mul249_CAST_sub250<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul249_fixbits + (1)*main_mul249_CAST_sub250_fixbits + (-10000)*C2_main_mul249_CAST_sub250<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul249_CAST_sub250
castCostObj +=  + (1)*C2_main_mul249_CAST_sub250
C3_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C3_main_mul249_CAST_sub250')
C4_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C4_main_mul249_CAST_sub250')
C5_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C5_main_mul249_CAST_sub250')
C6_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C6_main_mul249_CAST_sub250')
C7_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C7_main_mul249_CAST_sub250')
C8_main_mul249_CAST_sub250 = solver.IntVar(0, 1, 'C8_main_mul249_CAST_sub250')
solver.Add( + (1)*main_mul249_fixp + (1)*main_mul249_CAST_sub250_float + (-1)*C3_main_mul249_CAST_sub250<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul249_CAST_sub250
solver.Add( + (1)*main_mul249_float + (1)*main_mul249_CAST_sub250_fixp + (-1)*C4_main_mul249_CAST_sub250<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul249_CAST_sub250
solver.Add( + (1)*main_mul249_fixp + (1)*main_mul249_CAST_sub250_double + (-1)*C5_main_mul249_CAST_sub250<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul249_CAST_sub250
solver.Add( + (1)*main_mul249_double + (1)*main_mul249_CAST_sub250_fixp + (-1)*C6_main_mul249_CAST_sub250<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul249_CAST_sub250
solver.Add( + (1)*main_mul249_float + (1)*main_mul249_CAST_sub250_double + (-1)*C7_main_mul249_CAST_sub250<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul249_CAST_sub250
solver.Add( + (1)*main_mul249_double + (1)*main_mul249_CAST_sub250_float + (-1)*C8_main_mul249_CAST_sub250<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul249_CAST_sub250



#Stuff for   %sub250 = fsub double %w.3, %mul249, !taffo.info !83, !taffo.initweight !27
main_sub250_fixbits = solver.IntVar(0, 28, 'main_sub250_fixbits')
main_sub250_fixp = solver.IntVar(0, 1, 'main_sub250_fixp')
main_sub250_float = solver.IntVar(0, 1, 'main_sub250_float')
main_sub250_double = solver.IntVar(0, 1, 'main_sub250_double')
main_sub250_enob = solver.IntVar(-10000, 10000, 'main_sub250_enob')
solver.Add( + (1)*main_sub250_enob + (-1)*main_sub250_fixbits + (10000)*main_sub250_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub250_enob + (10000)*main_sub250_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub250_enob + (10000)*main_sub250_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub250_fixbits + (-10000)*main_sub250_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_sub250_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub250_enob
solver.Add( + (1)*main_sub250_fixp + (1)*main_sub250_float + (1)*main_sub250_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub250_fixbits + (-10000)*main_sub250_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %w.3 = phi double [ %tmp14, %for.body235 ], [ %sub250, %for.inc251 ], !taffo.info !80
main_sub250_CAST_w_3_fixbits = solver.IntVar(0, 28, 'main_sub250_CAST_w_3_fixbits')
main_sub250_CAST_w_3_fixp = solver.IntVar(0, 1, 'main_sub250_CAST_w_3_fixp')
main_sub250_CAST_w_3_float = solver.IntVar(0, 1, 'main_sub250_CAST_w_3_float')
main_sub250_CAST_w_3_double = solver.IntVar(0, 1, 'main_sub250_CAST_w_3_double')
solver.Add( + (1)*main_sub250_CAST_w_3_fixp + (1)*main_sub250_CAST_w_3_float + (1)*main_sub250_CAST_w_3_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub250_CAST_w_3_fixbits + (-10000)*main_sub250_CAST_w_3_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C1_main_sub250_CAST_w_3')
C2_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C2_main_sub250_CAST_w_3')
solver.Add( + (1)*main_sub250_fixbits + (-1)*main_sub250_CAST_w_3_fixbits + (-10000)*C1_main_sub250_CAST_w_3<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub250_fixbits + (1)*main_sub250_CAST_w_3_fixbits + (-10000)*C2_main_sub250_CAST_w_3<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub250_CAST_w_3
castCostObj +=  + (1)*C2_main_sub250_CAST_w_3
C3_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C3_main_sub250_CAST_w_3')
C4_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C4_main_sub250_CAST_w_3')
C5_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C5_main_sub250_CAST_w_3')
C6_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C6_main_sub250_CAST_w_3')
C7_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C7_main_sub250_CAST_w_3')
C8_main_sub250_CAST_w_3 = solver.IntVar(0, 1, 'C8_main_sub250_CAST_w_3')
solver.Add( + (1)*main_sub250_fixp + (1)*main_sub250_CAST_w_3_float + (-1)*C3_main_sub250_CAST_w_3<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub250_CAST_w_3
solver.Add( + (1)*main_sub250_float + (1)*main_sub250_CAST_w_3_fixp + (-1)*C4_main_sub250_CAST_w_3<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub250_CAST_w_3
solver.Add( + (1)*main_sub250_fixp + (1)*main_sub250_CAST_w_3_double + (-1)*C5_main_sub250_CAST_w_3<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub250_CAST_w_3
solver.Add( + (1)*main_sub250_double + (1)*main_sub250_CAST_w_3_fixp + (-1)*C6_main_sub250_CAST_w_3<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub250_CAST_w_3
solver.Add( + (1)*main_sub250_float + (1)*main_sub250_CAST_w_3_double + (-1)*C7_main_sub250_CAST_w_3<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub250_CAST_w_3
solver.Add( + (1)*main_sub250_double + (1)*main_sub250_CAST_w_3_float + (-1)*C8_main_sub250_CAST_w_3<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub250_CAST_w_3
solver.Add( + (1)*main_w_3_fixp + (-1)*main_sub250_CAST_w_3_fixp==0)    #fix equality
solver.Add( + (1)*main_w_3_float + (-1)*main_sub250_CAST_w_3_float==0)    #float equality
solver.Add( + (1)*main_w_3_double + (-1)*main_sub250_CAST_w_3_double==0)    #double equality
solver.Add( + (1)*main_w_3_fixbits + (-1)*main_sub250_CAST_w_3_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_3_enob + (-1)*main_sub250_enob + (10000)*main_main_w_3_enob_1<=10000)    #Enob: forcing phi enob
solver.Add( + (1)*main_w_3_CAST_sub250_fixp + (-1)*main_mul249_CAST_sub250_fixp==0)    #fix equality
solver.Add( + (1)*main_w_3_CAST_sub250_float + (-1)*main_mul249_CAST_sub250_float==0)    #float equality
solver.Add( + (1)*main_w_3_CAST_sub250_double + (-1)*main_mul249_CAST_sub250_double==0)    #double equality
solver.Add( + (1)*main_w_3_CAST_sub250_fixbits + (-1)*main_mul249_CAST_sub250_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_w_3_CAST_sub250_fixp + (-1)*main_sub250_fixp==0)    #fix equality
solver.Add( + (1)*main_w_3_CAST_sub250_float + (-1)*main_sub250_float==0)    #float equality
solver.Add( + (1)*main_w_3_CAST_sub250_double + (-1)*main_sub250_double==0)    #double equality
solver.Add( + (1)*main_w_3_CAST_sub250_fixbits + (-1)*main_sub250_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub250_fixp
mathCostObj +=  + (3)*main_sub250_float
mathCostObj +=  + (6.64928)*main_sub250_double
solver.Add( + (1)*main_sub250_enob + (-1)*main_w_3_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub250_enob + (-1)*main_mul249_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp17 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp17')
solver.Add( + (1)*main_A_enob_memphi_main_tmp17 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp17_enob_1 = solver.IntVar(0, 1, 'main_main_tmp17_enob_1')
main_main_tmp17_enob_4 = solver.IntVar(0, 1, 'main_main_tmp17_enob_4')
main_main_tmp17_enob_5 = solver.IntVar(0, 1, 'main_main_tmp17_enob_5')
main_main_tmp17_enob_6 = solver.IntVar(0, 1, 'main_main_tmp17_enob_6')
main_main_tmp17_enob_7 = solver.IntVar(0, 1, 'main_main_tmp17_enob_7')
solver.Add( + (1)*main_main_tmp17_enob_1 + (1)*main_main_tmp17_enob_4 + (1)*main_main_tmp17_enob_5 + (1)*main_main_tmp17_enob_6 + (1)*main_main_tmp17_enob_7==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp17 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp17_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp17 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp17_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp17 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp17_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp17 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_A_enob_memphi_main_tmp17 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_7<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div258 = fdiv double %w.3, %tmp17, !taffo.info !85, !taffo.initweight !27
main_w_3_CAST_div258_fixbits = solver.IntVar(0, 28, 'main_w_3_CAST_div258_fixbits')
main_w_3_CAST_div258_fixp = solver.IntVar(0, 1, 'main_w_3_CAST_div258_fixp')
main_w_3_CAST_div258_float = solver.IntVar(0, 1, 'main_w_3_CAST_div258_float')
main_w_3_CAST_div258_double = solver.IntVar(0, 1, 'main_w_3_CAST_div258_double')
solver.Add( + (1)*main_w_3_CAST_div258_fixp + (1)*main_w_3_CAST_div258_float + (1)*main_w_3_CAST_div258_double==1)    #exactly 1 type
solver.Add( + (1)*main_w_3_CAST_div258_fixbits + (-10000)*main_w_3_CAST_div258_fixp<=0)    #If no fix, fix frac part = 0
C1_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C1_main_w_3_CAST_div258')
C2_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C2_main_w_3_CAST_div258')
solver.Add( + (1)*main_w_3_fixbits + (-1)*main_w_3_CAST_div258_fixbits + (-10000)*C1_main_w_3_CAST_div258<=0)    #Shift cost 1
solver.Add( + (-1)*main_w_3_fixbits + (1)*main_w_3_CAST_div258_fixbits + (-10000)*C2_main_w_3_CAST_div258<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_w_3_CAST_div258
castCostObj +=  + (1)*C2_main_w_3_CAST_div258
C3_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C3_main_w_3_CAST_div258')
C4_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C4_main_w_3_CAST_div258')
C5_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C5_main_w_3_CAST_div258')
C6_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C6_main_w_3_CAST_div258')
C7_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C7_main_w_3_CAST_div258')
C8_main_w_3_CAST_div258 = solver.IntVar(0, 1, 'C8_main_w_3_CAST_div258')
solver.Add( + (1)*main_w_3_fixp + (1)*main_w_3_CAST_div258_float + (-1)*C3_main_w_3_CAST_div258<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_w_3_CAST_div258
solver.Add( + (1)*main_w_3_float + (1)*main_w_3_CAST_div258_fixp + (-1)*C4_main_w_3_CAST_div258<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_w_3_CAST_div258
solver.Add( + (1)*main_w_3_fixp + (1)*main_w_3_CAST_div258_double + (-1)*C5_main_w_3_CAST_div258<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_w_3_CAST_div258
solver.Add( + (1)*main_w_3_double + (1)*main_w_3_CAST_div258_fixp + (-1)*C6_main_w_3_CAST_div258<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_w_3_CAST_div258
solver.Add( + (1)*main_w_3_float + (1)*main_w_3_CAST_div258_double + (-1)*C7_main_w_3_CAST_div258<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_w_3_CAST_div258
solver.Add( + (1)*main_w_3_double + (1)*main_w_3_CAST_div258_float + (-1)*C8_main_w_3_CAST_div258<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_w_3_CAST_div258



#Constraint for cast for   %div258 = fdiv double %w.3, %tmp17, !taffo.info !85, !taffo.initweight !27
main_A_CAST_div258_fixbits = solver.IntVar(0, 29, 'main_A_CAST_div258_fixbits')
main_A_CAST_div258_fixp = solver.IntVar(0, 1, 'main_A_CAST_div258_fixp')
main_A_CAST_div258_float = solver.IntVar(0, 1, 'main_A_CAST_div258_float')
main_A_CAST_div258_double = solver.IntVar(0, 1, 'main_A_CAST_div258_double')
solver.Add( + (1)*main_A_CAST_div258_fixp + (1)*main_A_CAST_div258_float + (1)*main_A_CAST_div258_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_div258_fixbits + (-10000)*main_A_CAST_div258_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_div258 = solver.IntVar(0, 1, 'C1_main_A_CAST_div258')
C2_main_A_CAST_div258 = solver.IntVar(0, 1, 'C2_main_A_CAST_div258')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_div258_fixbits + (-10000)*C1_main_A_CAST_div258<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_div258_fixbits + (-10000)*C2_main_A_CAST_div258<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_div258
castCostObj +=  + (1)*C2_main_A_CAST_div258
C3_main_A_CAST_div258 = solver.IntVar(0, 1, 'C3_main_A_CAST_div258')
C4_main_A_CAST_div258 = solver.IntVar(0, 1, 'C4_main_A_CAST_div258')
C5_main_A_CAST_div258 = solver.IntVar(0, 1, 'C5_main_A_CAST_div258')
C6_main_A_CAST_div258 = solver.IntVar(0, 1, 'C6_main_A_CAST_div258')
C7_main_A_CAST_div258 = solver.IntVar(0, 1, 'C7_main_A_CAST_div258')
C8_main_A_CAST_div258 = solver.IntVar(0, 1, 'C8_main_A_CAST_div258')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_div258_float + (-1)*C3_main_A_CAST_div258<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_div258
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_div258_fixp + (-1)*C4_main_A_CAST_div258<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_div258
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_div258_double + (-1)*C5_main_A_CAST_div258<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_div258
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_div258_fixp + (-1)*C6_main_A_CAST_div258<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_div258
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_div258_double + (-1)*C7_main_A_CAST_div258<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_div258
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_div258_float + (-1)*C8_main_A_CAST_div258<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_div258



#Stuff for   %div258 = fdiv double %w.3, %tmp17, !taffo.info !85, !taffo.initweight !27
main_div258_fixbits = solver.IntVar(0, 29, 'main_div258_fixbits')
main_div258_fixp = solver.IntVar(0, 1, 'main_div258_fixp')
main_div258_float = solver.IntVar(0, 1, 'main_div258_float')
main_div258_double = solver.IntVar(0, 1, 'main_div258_double')
main_div258_enob = solver.IntVar(-10000, 10000, 'main_div258_enob')
solver.Add( + (1)*main_div258_enob + (-1)*main_div258_fixbits + (10000)*main_div258_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div258_enob + (10000)*main_div258_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div258_enob + (10000)*main_div258_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div258_fixbits + (-10000)*main_div258_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_div258_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div258_enob
solver.Add( + (1)*main_div258_fixp + (1)*main_div258_float + (1)*main_div258_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div258_fixbits + (-10000)*main_div258_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_w_3_CAST_div258_fixp + (-1)*main_A_CAST_div258_fixp==0)    #fix equality
solver.Add( + (1)*main_w_3_CAST_div258_float + (-1)*main_A_CAST_div258_float==0)    #float equality
solver.Add( + (1)*main_w_3_CAST_div258_double + (-1)*main_A_CAST_div258_double==0)    #double equality
solver.Add( + (1)*main_w_3_CAST_div258_fixp + (-1)*main_div258_fixp==0)    #fix equality
solver.Add( + (1)*main_w_3_CAST_div258_float + (-1)*main_div258_float==0)    #float equality
solver.Add( + (1)*main_w_3_CAST_div258_double + (-1)*main_div258_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div258_fixp
mathCostObj +=  + (6)*main_div258_float
mathCostObj +=  + (12)*main_div258_double
main_main_div258_enob_1 = solver.IntVar(0, 1, 'main_main_div258_enob_1')
main_main_div258_enob_2 = solver.IntVar(0, 1, 'main_main_div258_enob_2')
solver.Add( + (1)*main_main_div258_enob_1 + (1)*main_main_div258_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div258_enob + (-1)*main_A_enob_memphi_main_tmp17 + (-10000)*main_main_div258_enob_1<=1026)    #Enob: propagation in division 1
solver.Add( + (1)*main_div258_enob + (-1)*main_w_3_enob + (-10000)*main_main_div258_enob_2<=1026)    #Enob: propagation in division 2



#Constraint for cast for   store double %div258, double* %arrayidx260, align 8, !taffo.info !29, !taffo.initweight !27
main_div258_CAST_store_fixbits = solver.IntVar(0, 29, 'main_div258_CAST_store_fixbits')
main_div258_CAST_store_fixp = solver.IntVar(0, 1, 'main_div258_CAST_store_fixp')
main_div258_CAST_store_float = solver.IntVar(0, 1, 'main_div258_CAST_store_float')
main_div258_CAST_store_double = solver.IntVar(0, 1, 'main_div258_CAST_store_double')
solver.Add( + (1)*main_div258_CAST_store_fixp + (1)*main_div258_CAST_store_float + (1)*main_div258_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div258_CAST_store_fixbits + (-10000)*main_div258_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div258_CAST_store = solver.IntVar(0, 1, 'C1_main_div258_CAST_store')
C2_main_div258_CAST_store = solver.IntVar(0, 1, 'C2_main_div258_CAST_store')
solver.Add( + (1)*main_div258_fixbits + (-1)*main_div258_CAST_store_fixbits + (-10000)*C1_main_div258_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div258_fixbits + (1)*main_div258_CAST_store_fixbits + (-10000)*C2_main_div258_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div258_CAST_store
castCostObj +=  + (1)*C2_main_div258_CAST_store
C3_main_div258_CAST_store = solver.IntVar(0, 1, 'C3_main_div258_CAST_store')
C4_main_div258_CAST_store = solver.IntVar(0, 1, 'C4_main_div258_CAST_store')
C5_main_div258_CAST_store = solver.IntVar(0, 1, 'C5_main_div258_CAST_store')
C6_main_div258_CAST_store = solver.IntVar(0, 1, 'C6_main_div258_CAST_store')
C7_main_div258_CAST_store = solver.IntVar(0, 1, 'C7_main_div258_CAST_store')
C8_main_div258_CAST_store = solver.IntVar(0, 1, 'C8_main_div258_CAST_store')
solver.Add( + (1)*main_div258_fixp + (1)*main_div258_CAST_store_float + (-1)*C3_main_div258_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div258_CAST_store
solver.Add( + (1)*main_div258_float + (1)*main_div258_CAST_store_fixp + (-1)*C4_main_div258_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div258_CAST_store
solver.Add( + (1)*main_div258_fixp + (1)*main_div258_CAST_store_double + (-1)*C5_main_div258_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div258_CAST_store
solver.Add( + (1)*main_div258_double + (1)*main_div258_CAST_store_fixp + (-1)*C6_main_div258_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div258_CAST_store
solver.Add( + (1)*main_div258_float + (1)*main_div258_CAST_store_double + (-1)*C7_main_div258_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div258_CAST_store
solver.Add( + (1)*main_div258_double + (1)*main_div258_CAST_store_float + (-1)*C8_main_div258_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div258_CAST_store
solver.Add( + (1)*main_x_fixp + (-1)*main_div258_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_x_float + (-1)*main_div258_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_x_double + (-1)*main_div258_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_x_fixbits + (-1)*main_div258_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_x_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_x_enob_storeENOB')
solver.Add( + (1)*main_x_enob_storeENOB + (-1)*main_x_fixbits + (10000)*main_x_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_x_enob_storeENOB + (10000)*main_x_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_x_enob_storeENOB + (10000)*main_x_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_x_enob_storeENOB + (-1)*main_div258_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp16 + (-1)*main_x_enob_storeENOB + (10000)*main_main_tmp16_enob_9<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_x_enob_memphi_main_tmp20 = solver.IntVar(-10000, 10000, 'main_x_enob_memphi_main_tmp20')
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_x_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp20_enob_1 = solver.IntVar(0, 1, 'main_main_tmp20_enob_1')
main_main_tmp20_enob_4 = solver.IntVar(0, 1, 'main_main_tmp20_enob_4')
main_main_tmp20_enob_5 = solver.IntVar(0, 1, 'main_main_tmp20_enob_5')
main_main_tmp20_enob_6 = solver.IntVar(0, 1, 'main_main_tmp20_enob_6')
main_main_tmp20_enob_7 = solver.IntVar(0, 1, 'main_main_tmp20_enob_7')
main_main_tmp20_enob_8 = solver.IntVar(0, 1, 'main_main_tmp20_enob_8')
main_main_tmp20_enob_9 = solver.IntVar(0, 1, 'main_main_tmp20_enob_9')
solver.Add( + (1)*main_main_tmp20_enob_1 + (1)*main_main_tmp20_enob_4 + (1)*main_main_tmp20_enob_5 + (1)*main_main_tmp20_enob_6 + (1)*main_main_tmp20_enob_7 + (1)*main_main_tmp20_enob_8 + (1)*main_main_tmp20_enob_9==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_b_enob_storeENOB + (10000)*main_main_tmp20_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_B_enob_storeENOB + (10000)*main_main_tmp20_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_A_enob_storeENOB + (10000)*main_main_tmp20_enob_5<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_A_enob_storeENOB_storeENOB + (10000)*main_main_tmp20_enob_6<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_A_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp20_enob_7<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_y_enob_storeENOB + (10000)*main_main_tmp20_enob_8<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x_enob_memphi_main_tmp20 + (-1)*main_x_enob_storeENOB + (10000)*main_main_tmp20_enob_9<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call272 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp19, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.5, i32 0, i32 0), double %tmp20), !taffo.info !29, !taffo.initweight !28, !taffo.constinfo !90
main_x_CAST_call272_fixbits = solver.IntVar(0, 29, 'main_x_CAST_call272_fixbits')
main_x_CAST_call272_fixp = solver.IntVar(0, 1, 'main_x_CAST_call272_fixp')
main_x_CAST_call272_float = solver.IntVar(0, 1, 'main_x_CAST_call272_float')
main_x_CAST_call272_double = solver.IntVar(0, 1, 'main_x_CAST_call272_double')
solver.Add( + (1)*main_x_CAST_call272_fixp + (1)*main_x_CAST_call272_float + (1)*main_x_CAST_call272_double==1)    #exactly 1 type
solver.Add( + (1)*main_x_CAST_call272_fixbits + (-10000)*main_x_CAST_call272_fixp<=0)    #If no fix, fix frac part = 0
C1_main_x_CAST_call272 = solver.IntVar(0, 1, 'C1_main_x_CAST_call272')
C2_main_x_CAST_call272 = solver.IntVar(0, 1, 'C2_main_x_CAST_call272')
solver.Add( + (1)*main_x_fixbits + (-1)*main_x_CAST_call272_fixbits + (-10000)*C1_main_x_CAST_call272<=0)    #Shift cost 1
solver.Add( + (-1)*main_x_fixbits + (1)*main_x_CAST_call272_fixbits + (-10000)*C2_main_x_CAST_call272<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_x_CAST_call272
castCostObj +=  + (1)*C2_main_x_CAST_call272
C3_main_x_CAST_call272 = solver.IntVar(0, 1, 'C3_main_x_CAST_call272')
C4_main_x_CAST_call272 = solver.IntVar(0, 1, 'C4_main_x_CAST_call272')
C5_main_x_CAST_call272 = solver.IntVar(0, 1, 'C5_main_x_CAST_call272')
C6_main_x_CAST_call272 = solver.IntVar(0, 1, 'C6_main_x_CAST_call272')
C7_main_x_CAST_call272 = solver.IntVar(0, 1, 'C7_main_x_CAST_call272')
C8_main_x_CAST_call272 = solver.IntVar(0, 1, 'C8_main_x_CAST_call272')
solver.Add( + (1)*main_x_fixp + (1)*main_x_CAST_call272_float + (-1)*C3_main_x_CAST_call272<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_x_CAST_call272
solver.Add( + (1)*main_x_float + (1)*main_x_CAST_call272_fixp + (-1)*C4_main_x_CAST_call272<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_x_CAST_call272
solver.Add( + (1)*main_x_fixp + (1)*main_x_CAST_call272_double + (-1)*C5_main_x_CAST_call272<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_x_CAST_call272
solver.Add( + (1)*main_x_double + (1)*main_x_CAST_call272_fixp + (-1)*C6_main_x_CAST_call272<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_x_CAST_call272
solver.Add( + (1)*main_x_float + (1)*main_x_CAST_call272_double + (-1)*C7_main_x_CAST_call272<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_x_CAST_call272
solver.Add( + (1)*main_x_double + (1)*main_x_CAST_call272_float + (-1)*C8_main_x_CAST_call272<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_x_CAST_call272
solver.Add( + (1)*main_x_CAST_call272_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(10000 * castCostObj / 812.009+ 1 * enobCostObj / 25966+ 10000 * mathCostObj / 149.171)

# Model declaration end.