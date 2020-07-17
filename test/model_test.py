


#Stuff for   %imgIn = alloca [192 x [128 x double]], align 16, !taffo.info !11, !taffo.initweight !13
main_imgIn_fixbits = solver.IntVar(0, 27, 'main_imgIn_fixbits')
main_imgIn_fixp = solver.IntVar(0, 1, 'main_imgIn_fixp')
main_imgIn_float = solver.IntVar(0, 1, 'main_imgIn_float')
main_imgIn_double = solver.IntVar(0, 1, 'main_imgIn_double')
main_imgIn_enob = solver.IntVar(-10000, 10000, 'main_imgIn_enob')
solver.Add( + (1)*main_imgIn_enob + (-1)*main_imgIn_fixbits + (10000)*main_imgIn_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_imgIn_enob + (10000)*main_imgIn_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_imgIn_enob + (10000)*main_imgIn_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_imgIn_fixbits + (-10000)*main_imgIn_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_imgIn_double<=0)    #Disable double data type
enobCostObj =  + (-1)*main_imgIn_enob
solver.Add( + (1)*main_imgIn_fixp + (1)*main_imgIn_float + (1)*main_imgIn_double==1)    #Exactly one selected type
solver.Add( + (1)*main_imgIn_fixbits + (-10000)*main_imgIn_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %imgOut = alloca [192 x [128 x double]], align 16, !taffo.info !11, !taffo.initweight !13
main_imgOut_fixbits = solver.IntVar(0, 27, 'main_imgOut_fixbits')
main_imgOut_fixp = solver.IntVar(0, 1, 'main_imgOut_fixp')
main_imgOut_float = solver.IntVar(0, 1, 'main_imgOut_float')
main_imgOut_double = solver.IntVar(0, 1, 'main_imgOut_double')
main_imgOut_enob = solver.IntVar(-10000, 10000, 'main_imgOut_enob')
solver.Add( + (1)*main_imgOut_enob + (-1)*main_imgOut_fixbits + (10000)*main_imgOut_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_imgOut_enob + (10000)*main_imgOut_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_imgOut_enob + (10000)*main_imgOut_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_imgOut_fixbits + (-10000)*main_imgOut_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_imgOut_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_imgOut_enob
solver.Add( + (1)*main_imgOut_fixp + (1)*main_imgOut_float + (1)*main_imgOut_double==1)    #Exactly one selected type
solver.Add( + (1)*main_imgOut_fixbits + (-10000)*main_imgOut_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %y1 = alloca [192 x [128 x double]], align 16, !taffo.info !11, !taffo.initweight !13
main_y1_fixbits = solver.IntVar(0, 27, 'main_y1_fixbits')
main_y1_fixp = solver.IntVar(0, 1, 'main_y1_fixp')
main_y1_float = solver.IntVar(0, 1, 'main_y1_float')
main_y1_double = solver.IntVar(0, 1, 'main_y1_double')
main_y1_enob = solver.IntVar(-10000, 10000, 'main_y1_enob')
solver.Add( + (1)*main_y1_enob + (-1)*main_y1_fixbits + (10000)*main_y1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_y1_enob + (10000)*main_y1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_y1_enob + (10000)*main_y1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_y1_fixbits + (-10000)*main_y1_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_y1_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_y1_enob
solver.Add( + (1)*main_y1_fixp + (1)*main_y1_float + (1)*main_y1_double==1)    #Exactly one selected type
solver.Add( + (1)*main_y1_fixbits + (-10000)*main_y1_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %y2 = alloca [192 x [128 x double]], align 16, !taffo.info !11, !taffo.initweight !13
main_y2_fixbits = solver.IntVar(0, 27, 'main_y2_fixbits')
main_y2_fixp = solver.IntVar(0, 1, 'main_y2_fixp')
main_y2_float = solver.IntVar(0, 1, 'main_y2_float')
main_y2_double = solver.IntVar(0, 1, 'main_y2_double')
main_y2_enob = solver.IntVar(-10000, 10000, 'main_y2_enob')
solver.Add( + (1)*main_y2_enob + (-1)*main_y2_fixbits + (10000)*main_y2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_y2_enob + (10000)*main_y2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_y2_enob + (10000)*main_y2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_y2_fixbits + (-10000)*main_y2_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_y2_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_y2_enob
solver.Add( + (1)*main_y2_fixp + (1)*main_y2_float + (1)*main_y2_double==1)    #Exactly one selected type
solver.Add( + (1)*main_y2_fixbits + (-10000)*main_y2_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %rem to double, !taffo.info !15, !taffo.initweight !21
main_conv_fixbits = solver.IntVar(0, 22, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_conv_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 6.553500e+04
ConstantValue__fixbits = solver.IntVar(0, 16, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10008)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10037)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 6.553500e+04
ConstantValue__0_fixbits = solver.IntVar(0, 16, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10008)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10037)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*ConstantValue__0_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double %conv, 6.553500e+04, !taffo.info !15, !taffo.initweight !22, !taffo.constinfo !23
main_conv_CAST_div_fixbits = solver.IntVar(0, 22, 'main_conv_CAST_div_fixbits')
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



#Stuff for double 6.553500e+04
ConstantValue__1_fixbits = solver.IntVar(0, 16, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10008)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10037)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*ConstantValue__1_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double %conv, 6.553500e+04, !taffo.info !15, !taffo.initweight !22, !taffo.constinfo !23
ConstantValue__1_CAST_div_fixbits = solver.IntVar(0, 16, 'ConstantValue__1_CAST_div_fixbits')
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
castCostObj +=  + (6.25227)*C3_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_div_fixp + (-1)*C4_ConstantValue__1_CAST_div<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_div_double + (-1)*C5_ConstantValue__1_CAST_div<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_div_fixp + (-1)*C6_ConstantValue__1_CAST_div<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_div_double + (-1)*C7_ConstantValue__1_CAST_div<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_div_float + (-1)*C8_ConstantValue__1_CAST_div<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__1_CAST_div



#Stuff for   %div = fdiv double %conv, 6.553500e+04, !taffo.info !15, !taffo.initweight !22, !taffo.constinfo !23
main_div_fixbits = solver.IntVar(0, 22, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_div_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*ConstantValue__1_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*ConstantValue__1_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*ConstantValue__1_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj =  + (1.61159)*main_div_fixp
mathCostObj +=  + (6)*main_div_float
mathCostObj +=  + (12)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*ConstantValue__enob + (-10000)*main_main_div_enob_1<=3072)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_conv_enob + (-10000)*main_main_div_enob_2<=3072)    #Enob: propagation in division 2



#Constraint for cast for   store double %div, double* %arrayidx13, align 8, !taffo.info !11, !taffo.initweight !18
main_div_CAST_store_fixbits = solver.IntVar(0, 22, 'main_div_CAST_store_fixbits')
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
castCostObj +=  + (6.25227)*C3_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_fixp + (-1)*C4_main_div_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div_CAST_store
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_store_double + (-1)*C5_main_div_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_fixp + (-1)*C6_main_div_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div_CAST_store
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_store_double + (-1)*C7_main_div_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div_CAST_store
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_store_float + (-1)*C8_main_div_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div_CAST_store
solver.Add( + (1)*main_imgIn_fixp + (-1)*main_div_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_imgIn_float + (-1)*main_div_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_imgIn_double + (-1)*main_div_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_imgIn_fixbits + (-1)*main_div_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_imgIn_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_imgIn_enob_storeENOB')
solver.Add( + (1)*main_imgIn_enob_storeENOB + (-1)*main_imgIn_fixbits + (10000)*main_imgIn_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_imgIn_enob_storeENOB + (10000)*main_imgIn_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_imgIn_enob_storeENOB + (10000)*main_imgIn_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_imgIn_enob_storeENOB + (-1)*main_div_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for double -2.500000e-01
ConstantValue__2_fixbits = solver.IntVar(0, 30, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__2_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__3_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__3_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call = call double @exp(double -2.500000e-01) #1, !taffo.constinfo !26
ConstantValue__3_CAST_call_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_CAST_call_fixbits')
ConstantValue__3_CAST_call_fixp = solver.IntVar(0, 1, 'ConstantValue__3_CAST_call_fixp')
ConstantValue__3_CAST_call_float = solver.IntVar(0, 1, 'ConstantValue__3_CAST_call_float')
ConstantValue__3_CAST_call_double = solver.IntVar(0, 1, 'ConstantValue__3_CAST_call_double')
solver.Add( + (1)*ConstantValue__3_CAST_call_fixp + (1)*ConstantValue__3_CAST_call_float + (1)*ConstantValue__3_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__3_CAST_call_fixbits + (-10000)*ConstantValue__3_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C1_ConstantValue__3_CAST_call')
C2_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C2_ConstantValue__3_CAST_call')
solver.Add( + (1)*ConstantValue__3_fixbits + (-1)*ConstantValue__3_CAST_call_fixbits + (-10000)*C1_ConstantValue__3_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__3_fixbits + (1)*ConstantValue__3_CAST_call_fixbits + (-10000)*C2_ConstantValue__3_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__3_CAST_call
castCostObj +=  + (1)*C2_ConstantValue__3_CAST_call
C3_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C3_ConstantValue__3_CAST_call')
C4_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C4_ConstantValue__3_CAST_call')
C5_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C5_ConstantValue__3_CAST_call')
C6_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C6_ConstantValue__3_CAST_call')
C7_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C7_ConstantValue__3_CAST_call')
C8_ConstantValue__3_CAST_call = solver.IntVar(0, 1, 'C8_ConstantValue__3_CAST_call')
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_call_float + (-1)*C3_ConstantValue__3_CAST_call<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__3_CAST_call
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_call_fixp + (-1)*C4_ConstantValue__3_CAST_call<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__3_CAST_call
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_call_double + (-1)*C5_ConstantValue__3_CAST_call<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__3_CAST_call
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_call_fixp + (-1)*C6_ConstantValue__3_CAST_call<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__3_CAST_call
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_call_double + (-1)*C7_ConstantValue__3_CAST_call<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__3_CAST_call
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_call_float + (-1)*C8_ConstantValue__3_CAST_call<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__3_CAST_call
solver.Add( + (1)*ConstantValue__3_CAST_call_double==1)    #Type constraint for argument value



#Stuff for double 1.000000e+00
ConstantValue__4_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__4_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__5_fixbits = solver.IntVar(0, 31, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__5_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__6_fixbits = solver.IntVar(0, 30, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__6_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__7_fixbits = solver.IntVar(0, 30, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__7_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call40 = call double @exp(double -2.500000e-01) #1, !taffo.constinfo !26
ConstantValue__7_CAST_call40_fixbits = solver.IntVar(0, 30, 'ConstantValue__7_CAST_call40_fixbits')
ConstantValue__7_CAST_call40_fixp = solver.IntVar(0, 1, 'ConstantValue__7_CAST_call40_fixp')
ConstantValue__7_CAST_call40_float = solver.IntVar(0, 1, 'ConstantValue__7_CAST_call40_float')
ConstantValue__7_CAST_call40_double = solver.IntVar(0, 1, 'ConstantValue__7_CAST_call40_double')
solver.Add( + (1)*ConstantValue__7_CAST_call40_fixp + (1)*ConstantValue__7_CAST_call40_float + (1)*ConstantValue__7_CAST_call40_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__7_CAST_call40_fixbits + (-10000)*ConstantValue__7_CAST_call40_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C1_ConstantValue__7_CAST_call40')
C2_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C2_ConstantValue__7_CAST_call40')
solver.Add( + (1)*ConstantValue__7_fixbits + (-1)*ConstantValue__7_CAST_call40_fixbits + (-10000)*C1_ConstantValue__7_CAST_call40<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__7_fixbits + (1)*ConstantValue__7_CAST_call40_fixbits + (-10000)*C2_ConstantValue__7_CAST_call40<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__7_CAST_call40
castCostObj +=  + (1)*C2_ConstantValue__7_CAST_call40
C3_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C3_ConstantValue__7_CAST_call40')
C4_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C4_ConstantValue__7_CAST_call40')
C5_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C5_ConstantValue__7_CAST_call40')
C6_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C6_ConstantValue__7_CAST_call40')
C7_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C7_ConstantValue__7_CAST_call40')
C8_ConstantValue__7_CAST_call40 = solver.IntVar(0, 1, 'C8_ConstantValue__7_CAST_call40')
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_call40_float + (-1)*C3_ConstantValue__7_CAST_call40<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__7_CAST_call40
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_call40_fixp + (-1)*C4_ConstantValue__7_CAST_call40<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__7_CAST_call40
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_CAST_call40_double + (-1)*C5_ConstantValue__7_CAST_call40<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__7_CAST_call40
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_call40_fixp + (-1)*C6_ConstantValue__7_CAST_call40<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__7_CAST_call40
solver.Add( + (1)*ConstantValue__7_float + (1)*ConstantValue__7_CAST_call40_double + (-1)*C7_ConstantValue__7_CAST_call40<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__7_CAST_call40
solver.Add( + (1)*ConstantValue__7_double + (1)*ConstantValue__7_CAST_call40_float + (-1)*C8_ConstantValue__7_CAST_call40<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__7_CAST_call40
solver.Add( + (1)*ConstantValue__7_CAST_call40_double==1)    #Type constraint for argument value



#Stuff for double 1.000000e+00
ConstantValue__8_fixbits = solver.IntVar(0, 31, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__8_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



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



#Stuff for double -2.500000e-01
ConstantValue__10_fixbits = solver.IntVar(0, 30, 'ConstantValue__10_fixbits')
ConstantValue__10_fixp = solver.IntVar(0, 1, 'ConstantValue__10_fixp')
ConstantValue__10_float = solver.IntVar(0, 1, 'ConstantValue__10_float')
ConstantValue__10_double = solver.IntVar(0, 1, 'ConstantValue__10_double')
ConstantValue__10_enob = solver.IntVar(-10000, 10000, 'ConstantValue__10_enob')
solver.Add( + (1)*ConstantValue__10_enob + (-1)*ConstantValue__10_fixbits + (10000)*ConstantValue__10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__10_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_float + (1)*ConstantValue__10_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__11_fixbits = solver.IntVar(0, 30, 'ConstantValue__11_fixbits')
ConstantValue__11_fixp = solver.IntVar(0, 1, 'ConstantValue__11_fixp')
ConstantValue__11_float = solver.IntVar(0, 1, 'ConstantValue__11_float')
ConstantValue__11_double = solver.IntVar(0, 1, 'ConstantValue__11_double')
ConstantValue__11_enob = solver.IntVar(-10000, 10000, 'ConstantValue__11_enob')
solver.Add( + (1)*ConstantValue__11_enob + (-1)*ConstantValue__11_fixbits + (10000)*ConstantValue__11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__11_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_float + (1)*ConstantValue__11_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call43 = call double @exp(double -2.500000e-01) #1, !taffo.constinfo !26
ConstantValue__11_CAST_call43_fixbits = solver.IntVar(0, 30, 'ConstantValue__11_CAST_call43_fixbits')
ConstantValue__11_CAST_call43_fixp = solver.IntVar(0, 1, 'ConstantValue__11_CAST_call43_fixp')
ConstantValue__11_CAST_call43_float = solver.IntVar(0, 1, 'ConstantValue__11_CAST_call43_float')
ConstantValue__11_CAST_call43_double = solver.IntVar(0, 1, 'ConstantValue__11_CAST_call43_double')
solver.Add( + (1)*ConstantValue__11_CAST_call43_fixp + (1)*ConstantValue__11_CAST_call43_float + (1)*ConstantValue__11_CAST_call43_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__11_CAST_call43_fixbits + (-10000)*ConstantValue__11_CAST_call43_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C1_ConstantValue__11_CAST_call43')
C2_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C2_ConstantValue__11_CAST_call43')
solver.Add( + (1)*ConstantValue__11_fixbits + (-1)*ConstantValue__11_CAST_call43_fixbits + (-10000)*C1_ConstantValue__11_CAST_call43<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__11_fixbits + (1)*ConstantValue__11_CAST_call43_fixbits + (-10000)*C2_ConstantValue__11_CAST_call43<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__11_CAST_call43
castCostObj +=  + (1)*C2_ConstantValue__11_CAST_call43
C3_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C3_ConstantValue__11_CAST_call43')
C4_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C4_ConstantValue__11_CAST_call43')
C5_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C5_ConstantValue__11_CAST_call43')
C6_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C6_ConstantValue__11_CAST_call43')
C7_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C7_ConstantValue__11_CAST_call43')
C8_ConstantValue__11_CAST_call43 = solver.IntVar(0, 1, 'C8_ConstantValue__11_CAST_call43')
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_CAST_call43_float + (-1)*C3_ConstantValue__11_CAST_call43<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__11_CAST_call43
solver.Add( + (1)*ConstantValue__11_float + (1)*ConstantValue__11_CAST_call43_fixp + (-1)*C4_ConstantValue__11_CAST_call43<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__11_CAST_call43
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_CAST_call43_double + (-1)*C5_ConstantValue__11_CAST_call43<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__11_CAST_call43
solver.Add( + (1)*ConstantValue__11_double + (1)*ConstantValue__11_CAST_call43_fixp + (-1)*C6_ConstantValue__11_CAST_call43<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__11_CAST_call43
solver.Add( + (1)*ConstantValue__11_float + (1)*ConstantValue__11_CAST_call43_double + (-1)*C7_ConstantValue__11_CAST_call43<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__11_CAST_call43
solver.Add( + (1)*ConstantValue__11_double + (1)*ConstantValue__11_CAST_call43_float + (-1)*C8_ConstantValue__11_CAST_call43<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__11_CAST_call43
solver.Add( + (1)*ConstantValue__11_CAST_call43_double==1)    #Type constraint for argument value



#Stuff for double 5.000000e-01
ConstantValue__12_fixbits = solver.IntVar(0, 31, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__12_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-01
ConstantValue__13_fixbits = solver.IntVar(0, 31, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=10053)    #Enob constraint for double
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



#Stuff for double 1.000000e+00
ConstantValue__15_fixbits = solver.IntVar(0, 31, 'ConstantValue__15_fixbits')
ConstantValue__15_fixp = solver.IntVar(0, 1, 'ConstantValue__15_fixp')
ConstantValue__15_float = solver.IntVar(0, 1, 'ConstantValue__15_float')
ConstantValue__15_double = solver.IntVar(0, 1, 'ConstantValue__15_double')
ConstantValue__15_enob = solver.IntVar(-10000, 10000, 'ConstantValue__15_enob')
solver.Add( + (1)*ConstantValue__15_enob + (-1)*ConstantValue__15_fixbits + (10000)*ConstantValue__15_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__15_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__15_fixp + (1)*ConstantValue__15_float + (1)*ConstantValue__15_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-01
ConstantValue__16_fixbits = solver.IntVar(0, 31, 'ConstantValue__16_fixbits')
ConstantValue__16_fixp = solver.IntVar(0, 1, 'ConstantValue__16_fixp')
ConstantValue__16_float = solver.IntVar(0, 1, 'ConstantValue__16_float')
ConstantValue__16_double = solver.IntVar(0, 1, 'ConstantValue__16_double')
ConstantValue__16_enob = solver.IntVar(-10000, 10000, 'ConstantValue__16_enob')
solver.Add( + (1)*ConstantValue__16_enob + (-1)*ConstantValue__16_fixbits + (10000)*ConstantValue__16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__16_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-01
ConstantValue__17_fixbits = solver.IntVar(0, 31, 'ConstantValue__17_fixbits')
ConstantValue__17_fixp = solver.IntVar(0, 1, 'ConstantValue__17_fixp')
ConstantValue__17_float = solver.IntVar(0, 1, 'ConstantValue__17_float')
ConstantValue__17_double = solver.IntVar(0, 1, 'ConstantValue__17_double')
ConstantValue__17_enob = solver.IntVar(-10000, 10000, 'ConstantValue__17_enob')
solver.Add( + (1)*ConstantValue__17_enob + (-1)*ConstantValue__17_fixbits + (10000)*ConstantValue__17_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__17_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_float + (1)*ConstantValue__17_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call46 = call double @exp(double 5.000000e-01) #1, !taffo.constinfo !32
ConstantValue__17_CAST_call46_fixbits = solver.IntVar(0, 31, 'ConstantValue__17_CAST_call46_fixbits')
ConstantValue__17_CAST_call46_fixp = solver.IntVar(0, 1, 'ConstantValue__17_CAST_call46_fixp')
ConstantValue__17_CAST_call46_float = solver.IntVar(0, 1, 'ConstantValue__17_CAST_call46_float')
ConstantValue__17_CAST_call46_double = solver.IntVar(0, 1, 'ConstantValue__17_CAST_call46_double')
solver.Add( + (1)*ConstantValue__17_CAST_call46_fixp + (1)*ConstantValue__17_CAST_call46_float + (1)*ConstantValue__17_CAST_call46_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__17_CAST_call46_fixbits + (-10000)*ConstantValue__17_CAST_call46_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C1_ConstantValue__17_CAST_call46')
C2_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C2_ConstantValue__17_CAST_call46')
solver.Add( + (1)*ConstantValue__17_fixbits + (-1)*ConstantValue__17_CAST_call46_fixbits + (-10000)*C1_ConstantValue__17_CAST_call46<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__17_fixbits + (1)*ConstantValue__17_CAST_call46_fixbits + (-10000)*C2_ConstantValue__17_CAST_call46<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__17_CAST_call46
castCostObj +=  + (1)*C2_ConstantValue__17_CAST_call46
C3_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C3_ConstantValue__17_CAST_call46')
C4_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C4_ConstantValue__17_CAST_call46')
C5_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C5_ConstantValue__17_CAST_call46')
C6_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C6_ConstantValue__17_CAST_call46')
C7_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C7_ConstantValue__17_CAST_call46')
C8_ConstantValue__17_CAST_call46 = solver.IntVar(0, 1, 'C8_ConstantValue__17_CAST_call46')
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_CAST_call46_float + (-1)*C3_ConstantValue__17_CAST_call46<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__17_CAST_call46
solver.Add( + (1)*ConstantValue__17_float + (1)*ConstantValue__17_CAST_call46_fixp + (-1)*C4_ConstantValue__17_CAST_call46<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__17_CAST_call46
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_CAST_call46_double + (-1)*C5_ConstantValue__17_CAST_call46<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__17_CAST_call46
solver.Add( + (1)*ConstantValue__17_double + (1)*ConstantValue__17_CAST_call46_fixp + (-1)*C6_ConstantValue__17_CAST_call46<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__17_CAST_call46
solver.Add( + (1)*ConstantValue__17_float + (1)*ConstantValue__17_CAST_call46_double + (-1)*C7_ConstantValue__17_CAST_call46<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__17_CAST_call46
solver.Add( + (1)*ConstantValue__17_double + (1)*ConstantValue__17_CAST_call46_float + (-1)*C8_ConstantValue__17_CAST_call46<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__17_CAST_call46
solver.Add( + (1)*ConstantValue__17_CAST_call46_double==1)    #Type constraint for argument value



#Stuff for double -2.500000e-01
ConstantValue__18_fixbits = solver.IntVar(0, 30, 'ConstantValue__18_fixbits')
ConstantValue__18_fixp = solver.IntVar(0, 1, 'ConstantValue__18_fixp')
ConstantValue__18_float = solver.IntVar(0, 1, 'ConstantValue__18_float')
ConstantValue__18_double = solver.IntVar(0, 1, 'ConstantValue__18_double')
ConstantValue__18_enob = solver.IntVar(-10000, 10000, 'ConstantValue__18_enob')
solver.Add( + (1)*ConstantValue__18_enob + (-1)*ConstantValue__18_fixbits + (10000)*ConstantValue__18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__18_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__18_fixp + (1)*ConstantValue__18_float + (1)*ConstantValue__18_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__19_fixbits = solver.IntVar(0, 30, 'ConstantValue__19_fixbits')
ConstantValue__19_fixp = solver.IntVar(0, 1, 'ConstantValue__19_fixp')
ConstantValue__19_float = solver.IntVar(0, 1, 'ConstantValue__19_float')
ConstantValue__19_double = solver.IntVar(0, 1, 'ConstantValue__19_double')
ConstantValue__19_enob = solver.IntVar(-10000, 10000, 'ConstantValue__19_enob')
solver.Add( + (1)*ConstantValue__19_enob + (-1)*ConstantValue__19_fixbits + (10000)*ConstantValue__19_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__19_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_float + (1)*ConstantValue__19_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call49 = call double @exp(double -2.500000e-01) #1, !taffo.constinfo !26
ConstantValue__19_CAST_call49_fixbits = solver.IntVar(0, 30, 'ConstantValue__19_CAST_call49_fixbits')
ConstantValue__19_CAST_call49_fixp = solver.IntVar(0, 1, 'ConstantValue__19_CAST_call49_fixp')
ConstantValue__19_CAST_call49_float = solver.IntVar(0, 1, 'ConstantValue__19_CAST_call49_float')
ConstantValue__19_CAST_call49_double = solver.IntVar(0, 1, 'ConstantValue__19_CAST_call49_double')
solver.Add( + (1)*ConstantValue__19_CAST_call49_fixp + (1)*ConstantValue__19_CAST_call49_float + (1)*ConstantValue__19_CAST_call49_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__19_CAST_call49_fixbits + (-10000)*ConstantValue__19_CAST_call49_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C1_ConstantValue__19_CAST_call49')
C2_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C2_ConstantValue__19_CAST_call49')
solver.Add( + (1)*ConstantValue__19_fixbits + (-1)*ConstantValue__19_CAST_call49_fixbits + (-10000)*C1_ConstantValue__19_CAST_call49<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__19_fixbits + (1)*ConstantValue__19_CAST_call49_fixbits + (-10000)*C2_ConstantValue__19_CAST_call49<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__19_CAST_call49
castCostObj +=  + (1)*C2_ConstantValue__19_CAST_call49
C3_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C3_ConstantValue__19_CAST_call49')
C4_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C4_ConstantValue__19_CAST_call49')
C5_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C5_ConstantValue__19_CAST_call49')
C6_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C6_ConstantValue__19_CAST_call49')
C7_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C7_ConstantValue__19_CAST_call49')
C8_ConstantValue__19_CAST_call49 = solver.IntVar(0, 1, 'C8_ConstantValue__19_CAST_call49')
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_call49_float + (-1)*C3_ConstantValue__19_CAST_call49<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__19_CAST_call49
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_call49_fixp + (-1)*C4_ConstantValue__19_CAST_call49<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__19_CAST_call49
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_call49_double + (-1)*C5_ConstantValue__19_CAST_call49<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__19_CAST_call49
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_call49_fixp + (-1)*C6_ConstantValue__19_CAST_call49<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__19_CAST_call49
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_call49_double + (-1)*C7_ConstantValue__19_CAST_call49<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__19_CAST_call49
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_call49_float + (-1)*C8_ConstantValue__19_CAST_call49<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__19_CAST_call49
solver.Add( + (1)*ConstantValue__19_CAST_call49_double==1)    #Type constraint for argument value



#Stuff for double -7.500000e-01
ConstantValue__20_fixbits = solver.IntVar(0, 30, 'ConstantValue__20_fixbits')
ConstantValue__20_fixp = solver.IntVar(0, 1, 'ConstantValue__20_fixp')
ConstantValue__20_float = solver.IntVar(0, 1, 'ConstantValue__20_float')
ConstantValue__20_double = solver.IntVar(0, 1, 'ConstantValue__20_double')
ConstantValue__20_enob = solver.IntVar(-10000, 10000, 'ConstantValue__20_enob')
solver.Add( + (1)*ConstantValue__20_enob + (-1)*ConstantValue__20_fixbits + (10000)*ConstantValue__20_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__20_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_float + (1)*ConstantValue__20_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -7.500000e-01
ConstantValue__21_fixbits = solver.IntVar(0, 30, 'ConstantValue__21_fixbits')
ConstantValue__21_fixp = solver.IntVar(0, 1, 'ConstantValue__21_fixp')
ConstantValue__21_float = solver.IntVar(0, 1, 'ConstantValue__21_float')
ConstantValue__21_double = solver.IntVar(0, 1, 'ConstantValue__21_double')
ConstantValue__21_enob = solver.IntVar(-10000, 10000, 'ConstantValue__21_enob')
solver.Add( + (1)*ConstantValue__21_enob + (-1)*ConstantValue__21_fixbits + (10000)*ConstantValue__21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__21_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__21_fixp + (1)*ConstantValue__21_float + (1)*ConstantValue__21_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__22_fixbits = solver.IntVar(0, 30, 'ConstantValue__22_fixbits')
ConstantValue__22_fixp = solver.IntVar(0, 1, 'ConstantValue__22_fixp')
ConstantValue__22_float = solver.IntVar(0, 1, 'ConstantValue__22_float')
ConstantValue__22_double = solver.IntVar(0, 1, 'ConstantValue__22_double')
ConstantValue__22_enob = solver.IntVar(-10000, 10000, 'ConstantValue__22_enob')
solver.Add( + (1)*ConstantValue__22_enob + (-1)*ConstantValue__22_fixbits + (10000)*ConstantValue__22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__22_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_float + (1)*ConstantValue__22_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__23_fixbits = solver.IntVar(0, 30, 'ConstantValue__23_fixbits')
ConstantValue__23_fixp = solver.IntVar(0, 1, 'ConstantValue__23_fixp')
ConstantValue__23_float = solver.IntVar(0, 1, 'ConstantValue__23_float')
ConstantValue__23_double = solver.IntVar(0, 1, 'ConstantValue__23_double')
ConstantValue__23_enob = solver.IntVar(-10000, 10000, 'ConstantValue__23_enob')
solver.Add( + (1)*ConstantValue__23_enob + (-1)*ConstantValue__23_fixbits + (10000)*ConstantValue__23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__23_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_float + (1)*ConstantValue__23_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call52 = call double @exp(double -2.500000e-01) #1, !taffo.constinfo !26
ConstantValue__23_CAST_call52_fixbits = solver.IntVar(0, 30, 'ConstantValue__23_CAST_call52_fixbits')
ConstantValue__23_CAST_call52_fixp = solver.IntVar(0, 1, 'ConstantValue__23_CAST_call52_fixp')
ConstantValue__23_CAST_call52_float = solver.IntVar(0, 1, 'ConstantValue__23_CAST_call52_float')
ConstantValue__23_CAST_call52_double = solver.IntVar(0, 1, 'ConstantValue__23_CAST_call52_double')
solver.Add( + (1)*ConstantValue__23_CAST_call52_fixp + (1)*ConstantValue__23_CAST_call52_float + (1)*ConstantValue__23_CAST_call52_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__23_CAST_call52_fixbits + (-10000)*ConstantValue__23_CAST_call52_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C1_ConstantValue__23_CAST_call52')
C2_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C2_ConstantValue__23_CAST_call52')
solver.Add( + (1)*ConstantValue__23_fixbits + (-1)*ConstantValue__23_CAST_call52_fixbits + (-10000)*C1_ConstantValue__23_CAST_call52<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__23_fixbits + (1)*ConstantValue__23_CAST_call52_fixbits + (-10000)*C2_ConstantValue__23_CAST_call52<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__23_CAST_call52
castCostObj +=  + (1)*C2_ConstantValue__23_CAST_call52
C3_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C3_ConstantValue__23_CAST_call52')
C4_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C4_ConstantValue__23_CAST_call52')
C5_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C5_ConstantValue__23_CAST_call52')
C6_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C6_ConstantValue__23_CAST_call52')
C7_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C7_ConstantValue__23_CAST_call52')
C8_ConstantValue__23_CAST_call52 = solver.IntVar(0, 1, 'C8_ConstantValue__23_CAST_call52')
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_CAST_call52_float + (-1)*C3_ConstantValue__23_CAST_call52<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__23_CAST_call52
solver.Add( + (1)*ConstantValue__23_float + (1)*ConstantValue__23_CAST_call52_fixp + (-1)*C4_ConstantValue__23_CAST_call52<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__23_CAST_call52
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_CAST_call52_double + (-1)*C5_ConstantValue__23_CAST_call52<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__23_CAST_call52
solver.Add( + (1)*ConstantValue__23_double + (1)*ConstantValue__23_CAST_call52_fixp + (-1)*C6_ConstantValue__23_CAST_call52<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__23_CAST_call52
solver.Add( + (1)*ConstantValue__23_float + (1)*ConstantValue__23_CAST_call52_double + (-1)*C7_ConstantValue__23_CAST_call52<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__23_CAST_call52
solver.Add( + (1)*ConstantValue__23_double + (1)*ConstantValue__23_CAST_call52_float + (-1)*C8_ConstantValue__23_CAST_call52<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__23_CAST_call52
solver.Add( + (1)*ConstantValue__23_CAST_call52_double==1)    #Type constraint for argument value



#Stuff for double 1.250000e+00
ConstantValue__24_fixbits = solver.IntVar(0, 30, 'ConstantValue__24_fixbits')
ConstantValue__24_fixp = solver.IntVar(0, 1, 'ConstantValue__24_fixp')
ConstantValue__24_float = solver.IntVar(0, 1, 'ConstantValue__24_float')
ConstantValue__24_double = solver.IntVar(0, 1, 'ConstantValue__24_double')
ConstantValue__24_enob = solver.IntVar(-10000, 10000, 'ConstantValue__24_enob')
solver.Add( + (1)*ConstantValue__24_enob + (-1)*ConstantValue__24_fixbits + (10000)*ConstantValue__24_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__24_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__24_fixp + (1)*ConstantValue__24_float + (1)*ConstantValue__24_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.250000e+00
ConstantValue__25_fixbits = solver.IntVar(0, 30, 'ConstantValue__25_fixbits')
ConstantValue__25_fixp = solver.IntVar(0, 1, 'ConstantValue__25_fixp')
ConstantValue__25_float = solver.IntVar(0, 1, 'ConstantValue__25_float')
ConstantValue__25_double = solver.IntVar(0, 1, 'ConstantValue__25_double')
ConstantValue__25_enob = solver.IntVar(-10000, 10000, 'ConstantValue__25_enob')
solver.Add( + (1)*ConstantValue__25_enob + (-1)*ConstantValue__25_fixbits + (10000)*ConstantValue__25_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__25_enob + (10000)*ConstantValue__25_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__25_enob + (10000)*ConstantValue__25_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__25_fixbits + (-10000)*ConstantValue__25_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__25_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_float + (1)*ConstantValue__25_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__25_fixbits + (-10000)*ConstantValue__25_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__26_fixbits = solver.IntVar(0, 32, 'ConstantValue__26_fixbits')
ConstantValue__26_fixp = solver.IntVar(0, 1, 'ConstantValue__26_fixp')
ConstantValue__26_float = solver.IntVar(0, 1, 'ConstantValue__26_float')
ConstantValue__26_double = solver.IntVar(0, 1, 'ConstantValue__26_double')
ConstantValue__26_enob = solver.IntVar(-10000, 10000, 'ConstantValue__26_enob')
solver.Add( + (1)*ConstantValue__26_enob + (-1)*ConstantValue__26_fixbits + (10000)*ConstantValue__26_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__26_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__26_fixp + (1)*ConstantValue__26_float + (1)*ConstantValue__26_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__27_fixbits = solver.IntVar(0, 32, 'ConstantValue__27_fixbits')
ConstantValue__27_fixp = solver.IntVar(0, 1, 'ConstantValue__27_fixp')
ConstantValue__27_float = solver.IntVar(0, 1, 'ConstantValue__27_float')
ConstantValue__27_double = solver.IntVar(0, 1, 'ConstantValue__27_double')
ConstantValue__27_enob = solver.IntVar(-10000, 10000, 'ConstantValue__27_enob')
solver.Add( + (1)*ConstantValue__27_enob + (-1)*ConstantValue__27_fixbits + (10000)*ConstantValue__27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__27_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__27_fixp + (1)*ConstantValue__27_float + (1)*ConstantValue__27_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -5.000000e-01
ConstantValue__28_fixbits = solver.IntVar(0, 30, 'ConstantValue__28_fixbits')
ConstantValue__28_fixp = solver.IntVar(0, 1, 'ConstantValue__28_fixp')
ConstantValue__28_float = solver.IntVar(0, 1, 'ConstantValue__28_float')
ConstantValue__28_double = solver.IntVar(0, 1, 'ConstantValue__28_double')
ConstantValue__28_enob = solver.IntVar(-10000, 10000, 'ConstantValue__28_enob')
solver.Add( + (1)*ConstantValue__28_enob + (-1)*ConstantValue__28_fixbits + (10000)*ConstantValue__28_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__28_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_float + (1)*ConstantValue__28_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -5.000000e-01
ConstantValue__29_fixbits = solver.IntVar(0, 30, 'ConstantValue__29_fixbits')
ConstantValue__29_fixp = solver.IntVar(0, 1, 'ConstantValue__29_fixp')
ConstantValue__29_float = solver.IntVar(0, 1, 'ConstantValue__29_float')
ConstantValue__29_double = solver.IntVar(0, 1, 'ConstantValue__29_double')
ConstantValue__29_enob = solver.IntVar(-10000, 10000, 'ConstantValue__29_enob')
solver.Add( + (1)*ConstantValue__29_enob + (-1)*ConstantValue__29_fixbits + (10000)*ConstantValue__29_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__29_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__29_fixp + (1)*ConstantValue__29_float + (1)*ConstantValue__29_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call56 = call double @exp(double -5.000000e-01) #1, !taffo.constinfo !46
ConstantValue__29_CAST_call56_fixbits = solver.IntVar(0, 30, 'ConstantValue__29_CAST_call56_fixbits')
ConstantValue__29_CAST_call56_fixp = solver.IntVar(0, 1, 'ConstantValue__29_CAST_call56_fixp')
ConstantValue__29_CAST_call56_float = solver.IntVar(0, 1, 'ConstantValue__29_CAST_call56_float')
ConstantValue__29_CAST_call56_double = solver.IntVar(0, 1, 'ConstantValue__29_CAST_call56_double')
solver.Add( + (1)*ConstantValue__29_CAST_call56_fixp + (1)*ConstantValue__29_CAST_call56_float + (1)*ConstantValue__29_CAST_call56_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__29_CAST_call56_fixbits + (-10000)*ConstantValue__29_CAST_call56_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C1_ConstantValue__29_CAST_call56')
C2_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C2_ConstantValue__29_CAST_call56')
solver.Add( + (1)*ConstantValue__29_fixbits + (-1)*ConstantValue__29_CAST_call56_fixbits + (-10000)*C1_ConstantValue__29_CAST_call56<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__29_fixbits + (1)*ConstantValue__29_CAST_call56_fixbits + (-10000)*C2_ConstantValue__29_CAST_call56<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__29_CAST_call56
castCostObj +=  + (1)*C2_ConstantValue__29_CAST_call56
C3_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C3_ConstantValue__29_CAST_call56')
C4_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C4_ConstantValue__29_CAST_call56')
C5_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C5_ConstantValue__29_CAST_call56')
C6_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C6_ConstantValue__29_CAST_call56')
C7_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C7_ConstantValue__29_CAST_call56')
C8_ConstantValue__29_CAST_call56 = solver.IntVar(0, 1, 'C8_ConstantValue__29_CAST_call56')
solver.Add( + (1)*ConstantValue__29_fixp + (1)*ConstantValue__29_CAST_call56_float + (-1)*C3_ConstantValue__29_CAST_call56<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__29_CAST_call56
solver.Add( + (1)*ConstantValue__29_float + (1)*ConstantValue__29_CAST_call56_fixp + (-1)*C4_ConstantValue__29_CAST_call56<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__29_CAST_call56
solver.Add( + (1)*ConstantValue__29_fixp + (1)*ConstantValue__29_CAST_call56_double + (-1)*C5_ConstantValue__29_CAST_call56<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__29_CAST_call56
solver.Add( + (1)*ConstantValue__29_double + (1)*ConstantValue__29_CAST_call56_fixp + (-1)*C6_ConstantValue__29_CAST_call56<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__29_CAST_call56
solver.Add( + (1)*ConstantValue__29_float + (1)*ConstantValue__29_CAST_call56_double + (-1)*C7_ConstantValue__29_CAST_call56<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__29_CAST_call56
solver.Add( + (1)*ConstantValue__29_double + (1)*ConstantValue__29_CAST_call56_float + (-1)*C8_ConstantValue__29_CAST_call56<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__29_CAST_call56
solver.Add( + (1)*ConstantValue__29_CAST_call56_double==1)    #Type constraint for argument value



#Stuff for double 2.000000e+00
ConstantValue__30_fixbits = solver.IntVar(0, 30, 'ConstantValue__30_fixbits')
ConstantValue__30_fixp = solver.IntVar(0, 1, 'ConstantValue__30_fixp')
ConstantValue__30_float = solver.IntVar(0, 1, 'ConstantValue__30_float')
ConstantValue__30_double = solver.IntVar(0, 1, 'ConstantValue__30_double')
ConstantValue__30_enob = solver.IntVar(-10000, 10000, 'ConstantValue__30_enob')
solver.Add( + (1)*ConstantValue__30_enob + (-1)*ConstantValue__30_fixbits + (10000)*ConstantValue__30_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__30_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__30_fixp + (1)*ConstantValue__30_float + (1)*ConstantValue__30_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__31_fixbits = solver.IntVar(0, 30, 'ConstantValue__31_fixbits')
ConstantValue__31_fixp = solver.IntVar(0, 1, 'ConstantValue__31_fixp')
ConstantValue__31_float = solver.IntVar(0, 1, 'ConstantValue__31_float')
ConstantValue__31_double = solver.IntVar(0, 1, 'ConstantValue__31_double')
ConstantValue__31_enob = solver.IntVar(-10000, 10000, 'ConstantValue__31_enob')
solver.Add( + (1)*ConstantValue__31_enob + (-1)*ConstantValue__31_fixbits + (10000)*ConstantValue__31_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__31_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_float + (1)*ConstantValue__31_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call58 = call double @pow(double 2.000000e+00, double -2.500000e-01) #1, !taffo.constinfo !49
ConstantValue__31_CAST_call58_fixbits = solver.IntVar(0, 30, 'ConstantValue__31_CAST_call58_fixbits')
ConstantValue__31_CAST_call58_fixp = solver.IntVar(0, 1, 'ConstantValue__31_CAST_call58_fixp')
ConstantValue__31_CAST_call58_float = solver.IntVar(0, 1, 'ConstantValue__31_CAST_call58_float')
ConstantValue__31_CAST_call58_double = solver.IntVar(0, 1, 'ConstantValue__31_CAST_call58_double')
solver.Add( + (1)*ConstantValue__31_CAST_call58_fixp + (1)*ConstantValue__31_CAST_call58_float + (1)*ConstantValue__31_CAST_call58_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__31_CAST_call58_fixbits + (-10000)*ConstantValue__31_CAST_call58_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C1_ConstantValue__31_CAST_call58')
C2_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C2_ConstantValue__31_CAST_call58')
solver.Add( + (1)*ConstantValue__31_fixbits + (-1)*ConstantValue__31_CAST_call58_fixbits + (-10000)*C1_ConstantValue__31_CAST_call58<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__31_fixbits + (1)*ConstantValue__31_CAST_call58_fixbits + (-10000)*C2_ConstantValue__31_CAST_call58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__31_CAST_call58
castCostObj +=  + (1)*C2_ConstantValue__31_CAST_call58
C3_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C3_ConstantValue__31_CAST_call58')
C4_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C4_ConstantValue__31_CAST_call58')
C5_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C5_ConstantValue__31_CAST_call58')
C6_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C6_ConstantValue__31_CAST_call58')
C7_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C7_ConstantValue__31_CAST_call58')
C8_ConstantValue__31_CAST_call58 = solver.IntVar(0, 1, 'C8_ConstantValue__31_CAST_call58')
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_CAST_call58_float + (-1)*C3_ConstantValue__31_CAST_call58<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__31_CAST_call58
solver.Add( + (1)*ConstantValue__31_float + (1)*ConstantValue__31_CAST_call58_fixp + (-1)*C4_ConstantValue__31_CAST_call58<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__31_CAST_call58
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_CAST_call58_double + (-1)*C5_ConstantValue__31_CAST_call58<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__31_CAST_call58
solver.Add( + (1)*ConstantValue__31_double + (1)*ConstantValue__31_CAST_call58_fixp + (-1)*C6_ConstantValue__31_CAST_call58<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__31_CAST_call58
solver.Add( + (1)*ConstantValue__31_float + (1)*ConstantValue__31_CAST_call58_double + (-1)*C7_ConstantValue__31_CAST_call58<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__31_CAST_call58
solver.Add( + (1)*ConstantValue__31_double + (1)*ConstantValue__31_CAST_call58_float + (-1)*C8_ConstantValue__31_CAST_call58<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__31_CAST_call58
solver.Add( + (1)*ConstantValue__31_CAST_call58_double==1)    #Type constraint for argument value



#Stuff for double -2.500000e-01
ConstantValue__32_fixbits = solver.IntVar(0, 30, 'ConstantValue__32_fixbits')
ConstantValue__32_fixp = solver.IntVar(0, 1, 'ConstantValue__32_fixp')
ConstantValue__32_float = solver.IntVar(0, 1, 'ConstantValue__32_float')
ConstantValue__32_double = solver.IntVar(0, 1, 'ConstantValue__32_double')
ConstantValue__32_enob = solver.IntVar(-10000, 10000, 'ConstantValue__32_enob')
solver.Add( + (1)*ConstantValue__32_enob + (-1)*ConstantValue__32_fixbits + (10000)*ConstantValue__32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__32_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__32_fixp + (1)*ConstantValue__32_float + (1)*ConstantValue__32_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -2.500000e-01
ConstantValue__33_fixbits = solver.IntVar(0, 30, 'ConstantValue__33_fixbits')
ConstantValue__33_fixp = solver.IntVar(0, 1, 'ConstantValue__33_fixp')
ConstantValue__33_float = solver.IntVar(0, 1, 'ConstantValue__33_float')
ConstantValue__33_double = solver.IntVar(0, 1, 'ConstantValue__33_double')
ConstantValue__33_enob = solver.IntVar(-10000, 10000, 'ConstantValue__33_enob')
solver.Add( + (1)*ConstantValue__33_enob + (-1)*ConstantValue__33_fixbits + (10000)*ConstantValue__33_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__33_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_float + (1)*ConstantValue__33_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call58 = call double @pow(double 2.000000e+00, double -2.500000e-01) #1, !taffo.constinfo !49
ConstantValue__33_CAST_call58_fixbits = solver.IntVar(0, 30, 'ConstantValue__33_CAST_call58_fixbits')
ConstantValue__33_CAST_call58_fixp = solver.IntVar(0, 1, 'ConstantValue__33_CAST_call58_fixp')
ConstantValue__33_CAST_call58_float = solver.IntVar(0, 1, 'ConstantValue__33_CAST_call58_float')
ConstantValue__33_CAST_call58_double = solver.IntVar(0, 1, 'ConstantValue__33_CAST_call58_double')
solver.Add( + (1)*ConstantValue__33_CAST_call58_fixp + (1)*ConstantValue__33_CAST_call58_float + (1)*ConstantValue__33_CAST_call58_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__33_CAST_call58_fixbits + (-10000)*ConstantValue__33_CAST_call58_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C1_ConstantValue__33_CAST_call58')
C2_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C2_ConstantValue__33_CAST_call58')
solver.Add( + (1)*ConstantValue__33_fixbits + (-1)*ConstantValue__33_CAST_call58_fixbits + (-10000)*C1_ConstantValue__33_CAST_call58<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__33_fixbits + (1)*ConstantValue__33_CAST_call58_fixbits + (-10000)*C2_ConstantValue__33_CAST_call58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__33_CAST_call58
castCostObj +=  + (1)*C2_ConstantValue__33_CAST_call58
C3_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C3_ConstantValue__33_CAST_call58')
C4_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C4_ConstantValue__33_CAST_call58')
C5_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C5_ConstantValue__33_CAST_call58')
C6_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C6_ConstantValue__33_CAST_call58')
C7_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C7_ConstantValue__33_CAST_call58')
C8_ConstantValue__33_CAST_call58 = solver.IntVar(0, 1, 'C8_ConstantValue__33_CAST_call58')
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_CAST_call58_float + (-1)*C3_ConstantValue__33_CAST_call58<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__33_CAST_call58
solver.Add( + (1)*ConstantValue__33_float + (1)*ConstantValue__33_CAST_call58_fixp + (-1)*C4_ConstantValue__33_CAST_call58<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__33_CAST_call58
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_CAST_call58_double + (-1)*C5_ConstantValue__33_CAST_call58<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__33_CAST_call58
solver.Add( + (1)*ConstantValue__33_double + (1)*ConstantValue__33_CAST_call58_fixp + (-1)*C6_ConstantValue__33_CAST_call58<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__33_CAST_call58
solver.Add( + (1)*ConstantValue__33_float + (1)*ConstantValue__33_CAST_call58_double + (-1)*C7_ConstantValue__33_CAST_call58<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__33_CAST_call58
solver.Add( + (1)*ConstantValue__33_double + (1)*ConstantValue__33_CAST_call58_float + (-1)*C8_ConstantValue__33_CAST_call58<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__33_CAST_call58
solver.Add( + (1)*ConstantValue__33_CAST_call58_double==1)    #Type constraint for argument value



#Stuff for double -5.000000e-01
ConstantValue__34_fixbits = solver.IntVar(0, 30, 'ConstantValue__34_fixbits')
ConstantValue__34_fixp = solver.IntVar(0, 1, 'ConstantValue__34_fixp')
ConstantValue__34_float = solver.IntVar(0, 1, 'ConstantValue__34_float')
ConstantValue__34_double = solver.IntVar(0, 1, 'ConstantValue__34_double')
ConstantValue__34_enob = solver.IntVar(-10000, 10000, 'ConstantValue__34_enob')
solver.Add( + (1)*ConstantValue__34_enob + (-1)*ConstantValue__34_fixbits + (10000)*ConstantValue__34_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__34_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_float + (1)*ConstantValue__34_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -5.000000e-01
ConstantValue__35_fixbits = solver.IntVar(0, 30, 'ConstantValue__35_fixbits')
ConstantValue__35_fixp = solver.IntVar(0, 1, 'ConstantValue__35_fixp')
ConstantValue__35_float = solver.IntVar(0, 1, 'ConstantValue__35_float')
ConstantValue__35_double = solver.IntVar(0, 1, 'ConstantValue__35_double')
ConstantValue__35_enob = solver.IntVar(-10000, 10000, 'ConstantValue__35_enob')
solver.Add( + (1)*ConstantValue__35_enob + (-1)*ConstantValue__35_fixbits + (10000)*ConstantValue__35_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__35_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__35_fixp + (1)*ConstantValue__35_float + (1)*ConstantValue__35_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call59 = call double @exp(double -5.000000e-01) #1, !taffo.constinfo !46
ConstantValue__35_CAST_call59_fixbits = solver.IntVar(0, 30, 'ConstantValue__35_CAST_call59_fixbits')
ConstantValue__35_CAST_call59_fixp = solver.IntVar(0, 1, 'ConstantValue__35_CAST_call59_fixp')
ConstantValue__35_CAST_call59_float = solver.IntVar(0, 1, 'ConstantValue__35_CAST_call59_float')
ConstantValue__35_CAST_call59_double = solver.IntVar(0, 1, 'ConstantValue__35_CAST_call59_double')
solver.Add( + (1)*ConstantValue__35_CAST_call59_fixp + (1)*ConstantValue__35_CAST_call59_float + (1)*ConstantValue__35_CAST_call59_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__35_CAST_call59_fixbits + (-10000)*ConstantValue__35_CAST_call59_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C1_ConstantValue__35_CAST_call59')
C2_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C2_ConstantValue__35_CAST_call59')
solver.Add( + (1)*ConstantValue__35_fixbits + (-1)*ConstantValue__35_CAST_call59_fixbits + (-10000)*C1_ConstantValue__35_CAST_call59<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__35_fixbits + (1)*ConstantValue__35_CAST_call59_fixbits + (-10000)*C2_ConstantValue__35_CAST_call59<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__35_CAST_call59
castCostObj +=  + (1)*C2_ConstantValue__35_CAST_call59
C3_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C3_ConstantValue__35_CAST_call59')
C4_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C4_ConstantValue__35_CAST_call59')
C5_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C5_ConstantValue__35_CAST_call59')
C6_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C6_ConstantValue__35_CAST_call59')
C7_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C7_ConstantValue__35_CAST_call59')
C8_ConstantValue__35_CAST_call59 = solver.IntVar(0, 1, 'C8_ConstantValue__35_CAST_call59')
solver.Add( + (1)*ConstantValue__35_fixp + (1)*ConstantValue__35_CAST_call59_float + (-1)*C3_ConstantValue__35_CAST_call59<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__35_CAST_call59
solver.Add( + (1)*ConstantValue__35_float + (1)*ConstantValue__35_CAST_call59_fixp + (-1)*C4_ConstantValue__35_CAST_call59<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__35_CAST_call59
solver.Add( + (1)*ConstantValue__35_fixp + (1)*ConstantValue__35_CAST_call59_double + (-1)*C5_ConstantValue__35_CAST_call59<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__35_CAST_call59
solver.Add( + (1)*ConstantValue__35_double + (1)*ConstantValue__35_CAST_call59_fixp + (-1)*C6_ConstantValue__35_CAST_call59<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__35_CAST_call59
solver.Add( + (1)*ConstantValue__35_float + (1)*ConstantValue__35_CAST_call59_double + (-1)*C7_ConstantValue__35_CAST_call59<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__35_CAST_call59
solver.Add( + (1)*ConstantValue__35_double + (1)*ConstantValue__35_CAST_call59_float + (-1)*C8_ConstantValue__35_CAST_call59<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__35_CAST_call59
solver.Add( + (1)*ConstantValue__35_CAST_call59_double==1)    #Type constraint for argument value



#Stuff for double -0.000000e+00
ConstantValue__36_fixbits = solver.IntVar(0, 32, 'ConstantValue__36_fixbits')
ConstantValue__36_fixp = solver.IntVar(0, 1, 'ConstantValue__36_fixp')
ConstantValue__36_float = solver.IntVar(0, 1, 'ConstantValue__36_float')
ConstantValue__36_double = solver.IntVar(0, 1, 'ConstantValue__36_double')
ConstantValue__36_enob = solver.IntVar(-10000, 10000, 'ConstantValue__36_enob')
solver.Add( + (1)*ConstantValue__36_enob + (-1)*ConstantValue__36_fixbits + (10000)*ConstantValue__36_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__36_enob + (10000)*ConstantValue__36_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__36_enob + (10000)*ConstantValue__36_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__36_fixbits + (-10000)*ConstantValue__36_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__36_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__36_fixp + (1)*ConstantValue__36_float + (1)*ConstantValue__36_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__36_fixbits + (-10000)*ConstantValue__36_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__37_fixbits = solver.IntVar(0, 32, 'ConstantValue__37_fixbits')
ConstantValue__37_fixp = solver.IntVar(0, 1, 'ConstantValue__37_fixp')
ConstantValue__37_float = solver.IntVar(0, 1, 'ConstantValue__37_float')
ConstantValue__37_double = solver.IntVar(0, 1, 'ConstantValue__37_double')
ConstantValue__37_enob = solver.IntVar(-10000, 10000, 'ConstantValue__37_enob')
solver.Add( + (1)*ConstantValue__37_enob + (-1)*ConstantValue__37_fixbits + (10000)*ConstantValue__37_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__37_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_float + (1)*ConstantValue__37_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
main_imgIn_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'main_imgIn_enob_memphi_main_tmp')
solver.Add( + (1)*main_imgIn_enob_memphi_main_tmp + (-1)*main_imgIn_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
solver.Add( + (1)*main_main_tmp_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_imgIn_enob_memphi_main_tmp + (-1)*main_imgIn_enob_storeENOB + (10000)*main_main_tmp_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_imgIn_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'main_imgIn_enob_memphi_main_tmp1')
solver.Add( + (1)*main_imgIn_enob_memphi_main_tmp1 + (-1)*main_imgIn_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
solver.Add( + (1)*main_main_tmp1_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_imgIn_enob_memphi_main_tmp1 + (-1)*main_imgIn_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_y1_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_y1_enob_memphi_main_tmp2')
solver.Add( + (1)*main_y1_enob_memphi_main_tmp2 + (-1)*main_y1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_0 = solver.IntVar(0, 1, 'main_main_tmp2_enob_0')
solver.Add( + (1)*main_main_tmp2_enob_0==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_imgIn_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'main_imgIn_enob_memphi_main_tmp3')
solver.Add( + (1)*main_imgIn_enob_memphi_main_tmp3 + (-1)*main_imgIn_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
solver.Add( + (1)*main_main_tmp3_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_imgIn_enob_memphi_main_tmp3 + (-1)*main_imgIn_enob_storeENOB + (10000)*main_main_tmp3_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_y2_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'main_y2_enob_memphi_main_tmp4')
solver.Add( + (1)*main_y2_enob_memphi_main_tmp4 + (-1)*main_y2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_0 = solver.IntVar(0, 1, 'main_main_tmp4_enob_0')
solver.Add( + (1)*main_main_tmp4_enob_0==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_y1_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'main_y1_enob_memphi_main_tmp5')
solver.Add( + (1)*main_y1_enob_memphi_main_tmp5 + (-1)*main_y1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
solver.Add( + (1)*main_main_tmp5_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_y2_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'main_y2_enob_memphi_main_tmp6')
solver.Add( + (1)*main_y2_enob_memphi_main_tmp6 + (-1)*main_y2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2==1)    #Enob: one selected constraint



#Constraint for cast for   %add146 = fadd double %tmp5, %tmp6, !taffo.info !11, !taffo.initweight !20
main_y1_CAST_add146_fixbits = solver.IntVar(0, 27, 'main_y1_CAST_add146_fixbits')
main_y1_CAST_add146_fixp = solver.IntVar(0, 1, 'main_y1_CAST_add146_fixp')
main_y1_CAST_add146_float = solver.IntVar(0, 1, 'main_y1_CAST_add146_float')
main_y1_CAST_add146_double = solver.IntVar(0, 1, 'main_y1_CAST_add146_double')
solver.Add( + (1)*main_y1_CAST_add146_fixp + (1)*main_y1_CAST_add146_float + (1)*main_y1_CAST_add146_double==1)    #exactly 1 type
solver.Add( + (1)*main_y1_CAST_add146_fixbits + (-10000)*main_y1_CAST_add146_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C1_main_y1_CAST_add146')
C2_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C2_main_y1_CAST_add146')
solver.Add( + (1)*main_y1_fixbits + (-1)*main_y1_CAST_add146_fixbits + (-10000)*C1_main_y1_CAST_add146<=0)    #Shift cost 1
solver.Add( + (-1)*main_y1_fixbits + (1)*main_y1_CAST_add146_fixbits + (-10000)*C2_main_y1_CAST_add146<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y1_CAST_add146
castCostObj +=  + (1)*C2_main_y1_CAST_add146
C3_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C3_main_y1_CAST_add146')
C4_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C4_main_y1_CAST_add146')
C5_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C5_main_y1_CAST_add146')
C6_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C6_main_y1_CAST_add146')
C7_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C7_main_y1_CAST_add146')
C8_main_y1_CAST_add146 = solver.IntVar(0, 1, 'C8_main_y1_CAST_add146')
solver.Add( + (1)*main_y1_fixp + (1)*main_y1_CAST_add146_float + (-1)*C3_main_y1_CAST_add146<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y1_CAST_add146
solver.Add( + (1)*main_y1_float + (1)*main_y1_CAST_add146_fixp + (-1)*C4_main_y1_CAST_add146<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y1_CAST_add146
solver.Add( + (1)*main_y1_fixp + (1)*main_y1_CAST_add146_double + (-1)*C5_main_y1_CAST_add146<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y1_CAST_add146
solver.Add( + (1)*main_y1_double + (1)*main_y1_CAST_add146_fixp + (-1)*C6_main_y1_CAST_add146<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y1_CAST_add146
solver.Add( + (1)*main_y1_float + (1)*main_y1_CAST_add146_double + (-1)*C7_main_y1_CAST_add146<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y1_CAST_add146
solver.Add( + (1)*main_y1_double + (1)*main_y1_CAST_add146_float + (-1)*C8_main_y1_CAST_add146<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y1_CAST_add146



#Constraint for cast for   %add146 = fadd double %tmp5, %tmp6, !taffo.info !11, !taffo.initweight !20
main_y2_CAST_add146_fixbits = solver.IntVar(0, 27, 'main_y2_CAST_add146_fixbits')
main_y2_CAST_add146_fixp = solver.IntVar(0, 1, 'main_y2_CAST_add146_fixp')
main_y2_CAST_add146_float = solver.IntVar(0, 1, 'main_y2_CAST_add146_float')
main_y2_CAST_add146_double = solver.IntVar(0, 1, 'main_y2_CAST_add146_double')
solver.Add( + (1)*main_y2_CAST_add146_fixp + (1)*main_y2_CAST_add146_float + (1)*main_y2_CAST_add146_double==1)    #exactly 1 type
solver.Add( + (1)*main_y2_CAST_add146_fixbits + (-10000)*main_y2_CAST_add146_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C1_main_y2_CAST_add146')
C2_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C2_main_y2_CAST_add146')
solver.Add( + (1)*main_y2_fixbits + (-1)*main_y2_CAST_add146_fixbits + (-10000)*C1_main_y2_CAST_add146<=0)    #Shift cost 1
solver.Add( + (-1)*main_y2_fixbits + (1)*main_y2_CAST_add146_fixbits + (-10000)*C2_main_y2_CAST_add146<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y2_CAST_add146
castCostObj +=  + (1)*C2_main_y2_CAST_add146
C3_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C3_main_y2_CAST_add146')
C4_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C4_main_y2_CAST_add146')
C5_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C5_main_y2_CAST_add146')
C6_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C6_main_y2_CAST_add146')
C7_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C7_main_y2_CAST_add146')
C8_main_y2_CAST_add146 = solver.IntVar(0, 1, 'C8_main_y2_CAST_add146')
solver.Add( + (1)*main_y2_fixp + (1)*main_y2_CAST_add146_float + (-1)*C3_main_y2_CAST_add146<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y2_CAST_add146
solver.Add( + (1)*main_y2_float + (1)*main_y2_CAST_add146_fixp + (-1)*C4_main_y2_CAST_add146<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y2_CAST_add146
solver.Add( + (1)*main_y2_fixp + (1)*main_y2_CAST_add146_double + (-1)*C5_main_y2_CAST_add146<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y2_CAST_add146
solver.Add( + (1)*main_y2_double + (1)*main_y2_CAST_add146_fixp + (-1)*C6_main_y2_CAST_add146<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y2_CAST_add146
solver.Add( + (1)*main_y2_float + (1)*main_y2_CAST_add146_double + (-1)*C7_main_y2_CAST_add146<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y2_CAST_add146
solver.Add( + (1)*main_y2_double + (1)*main_y2_CAST_add146_float + (-1)*C8_main_y2_CAST_add146<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y2_CAST_add146



#Stuff for   %add146 = fadd double %tmp5, %tmp6, !taffo.info !11, !taffo.initweight !20
main_add146_fixbits = solver.IntVar(0, 27, 'main_add146_fixbits')
main_add146_fixp = solver.IntVar(0, 1, 'main_add146_fixp')
main_add146_float = solver.IntVar(0, 1, 'main_add146_float')
main_add146_double = solver.IntVar(0, 1, 'main_add146_double')
main_add146_enob = solver.IntVar(-10000, 10000, 'main_add146_enob')
solver.Add( + (1)*main_add146_enob + (-1)*main_add146_fixbits + (10000)*main_add146_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add146_enob + (10000)*main_add146_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add146_enob + (10000)*main_add146_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add146_fixbits + (-10000)*main_add146_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_add146_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add146_enob
solver.Add( + (1)*main_add146_fixp + (1)*main_add146_float + (1)*main_add146_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add146_fixbits + (-10000)*main_add146_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_y1_CAST_add146_fixp + (-1)*main_y2_CAST_add146_fixp==0)    #fix equality
solver.Add( + (1)*main_y1_CAST_add146_float + (-1)*main_y2_CAST_add146_float==0)    #float equality
solver.Add( + (1)*main_y1_CAST_add146_double + (-1)*main_y2_CAST_add146_double==0)    #double equality
solver.Add( + (1)*main_y1_CAST_add146_fixbits + (-1)*main_y2_CAST_add146_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_y1_CAST_add146_fixp + (-1)*main_add146_fixp==0)    #fix equality
solver.Add( + (1)*main_y1_CAST_add146_float + (-1)*main_add146_float==0)    #float equality
solver.Add( + (1)*main_y1_CAST_add146_double + (-1)*main_add146_double==0)    #double equality
solver.Add( + (1)*main_y1_CAST_add146_fixbits + (-1)*main_add146_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add146_fixp
mathCostObj +=  + (3)*main_add146_float
mathCostObj +=  + (6.64928)*main_add146_double
solver.Add( + (1)*main_add146_enob + (-1)*main_y1_enob_memphi_main_tmp5<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add146_enob + (-1)*main_y2_enob_memphi_main_tmp6<=0)    #Enob propagation in sum second addend



#Stuff for double 1.000000e+00
ConstantValue__38_fixbits = solver.IntVar(0, 31, 'ConstantValue__38_fixbits')
ConstantValue__38_fixp = solver.IntVar(0, 1, 'ConstantValue__38_fixp')
ConstantValue__38_float = solver.IntVar(0, 1, 'ConstantValue__38_float')
ConstantValue__38_double = solver.IntVar(0, 1, 'ConstantValue__38_double')
ConstantValue__38_enob = solver.IntVar(-10000, 10000, 'ConstantValue__38_enob')
solver.Add( + (1)*ConstantValue__38_enob + (-1)*ConstantValue__38_fixbits + (10000)*ConstantValue__38_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__38_enob + (10000)*ConstantValue__38_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__38_enob + (10000)*ConstantValue__38_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__38_fixbits + (-10000)*ConstantValue__38_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__38_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__38_fixp + (1)*ConstantValue__38_float + (1)*ConstantValue__38_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__38_fixbits + (-10000)*ConstantValue__38_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__39_fixbits = solver.IntVar(0, 31, 'ConstantValue__39_fixbits')
ConstantValue__39_fixp = solver.IntVar(0, 1, 'ConstantValue__39_fixp')
ConstantValue__39_float = solver.IntVar(0, 1, 'ConstantValue__39_float')
ConstantValue__39_double = solver.IntVar(0, 1, 'ConstantValue__39_double')
ConstantValue__39_enob = solver.IntVar(-10000, 10000, 'ConstantValue__39_enob')
solver.Add( + (1)*ConstantValue__39_enob + (-1)*ConstantValue__39_fixbits + (10000)*ConstantValue__39_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__39_enob + (10000)*ConstantValue__39_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__39_enob + (10000)*ConstantValue__39_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__39_fixbits + (-10000)*ConstantValue__39_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__39_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__39_fixp + (1)*ConstantValue__39_float + (1)*ConstantValue__39_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__39_fixbits + (-10000)*ConstantValue__39_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__40_fixbits = solver.IntVar(0, 31, 'ConstantValue__40_fixbits')
ConstantValue__40_fixp = solver.IntVar(0, 1, 'ConstantValue__40_fixp')
ConstantValue__40_float = solver.IntVar(0, 1, 'ConstantValue__40_float')
ConstantValue__40_double = solver.IntVar(0, 1, 'ConstantValue__40_double')
ConstantValue__40_enob = solver.IntVar(-10000, 10000, 'ConstantValue__40_enob')
solver.Add( + (1)*ConstantValue__40_enob + (-1)*ConstantValue__40_fixbits + (10000)*ConstantValue__40_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__40_enob + (10000)*ConstantValue__40_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__40_enob + (10000)*ConstantValue__40_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__40_fixbits + (-10000)*ConstantValue__40_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__40_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__40_fixp + (1)*ConstantValue__40_float + (1)*ConstantValue__40_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__40_fixbits + (-10000)*ConstantValue__40_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul147 = fmul double 1.000000e+00, %add146, !taffo.info !35, !taffo.initweight !17, !taffo.constinfo !29
ConstantValue__40_CAST_mul147_fixbits = solver.IntVar(0, 31, 'ConstantValue__40_CAST_mul147_fixbits')
ConstantValue__40_CAST_mul147_fixp = solver.IntVar(0, 1, 'ConstantValue__40_CAST_mul147_fixp')
ConstantValue__40_CAST_mul147_float = solver.IntVar(0, 1, 'ConstantValue__40_CAST_mul147_float')
ConstantValue__40_CAST_mul147_double = solver.IntVar(0, 1, 'ConstantValue__40_CAST_mul147_double')
solver.Add( + (1)*ConstantValue__40_CAST_mul147_fixp + (1)*ConstantValue__40_CAST_mul147_float + (1)*ConstantValue__40_CAST_mul147_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__40_CAST_mul147_fixbits + (-10000)*ConstantValue__40_CAST_mul147_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C1_ConstantValue__40_CAST_mul147')
C2_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C2_ConstantValue__40_CAST_mul147')
solver.Add( + (1)*ConstantValue__40_fixbits + (-1)*ConstantValue__40_CAST_mul147_fixbits + (-10000)*C1_ConstantValue__40_CAST_mul147<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__40_fixbits + (1)*ConstantValue__40_CAST_mul147_fixbits + (-10000)*C2_ConstantValue__40_CAST_mul147<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__40_CAST_mul147
castCostObj +=  + (1)*C2_ConstantValue__40_CAST_mul147
C3_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C3_ConstantValue__40_CAST_mul147')
C4_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C4_ConstantValue__40_CAST_mul147')
C5_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C5_ConstantValue__40_CAST_mul147')
C6_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C6_ConstantValue__40_CAST_mul147')
C7_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C7_ConstantValue__40_CAST_mul147')
C8_ConstantValue__40_CAST_mul147 = solver.IntVar(0, 1, 'C8_ConstantValue__40_CAST_mul147')
solver.Add( + (1)*ConstantValue__40_fixp + (1)*ConstantValue__40_CAST_mul147_float + (-1)*C3_ConstantValue__40_CAST_mul147<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__40_CAST_mul147
solver.Add( + (1)*ConstantValue__40_float + (1)*ConstantValue__40_CAST_mul147_fixp + (-1)*C4_ConstantValue__40_CAST_mul147<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__40_CAST_mul147
solver.Add( + (1)*ConstantValue__40_fixp + (1)*ConstantValue__40_CAST_mul147_double + (-1)*C5_ConstantValue__40_CAST_mul147<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__40_CAST_mul147
solver.Add( + (1)*ConstantValue__40_double + (1)*ConstantValue__40_CAST_mul147_fixp + (-1)*C6_ConstantValue__40_CAST_mul147<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__40_CAST_mul147
solver.Add( + (1)*ConstantValue__40_float + (1)*ConstantValue__40_CAST_mul147_double + (-1)*C7_ConstantValue__40_CAST_mul147<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__40_CAST_mul147
solver.Add( + (1)*ConstantValue__40_double + (1)*ConstantValue__40_CAST_mul147_float + (-1)*C8_ConstantValue__40_CAST_mul147<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__40_CAST_mul147



#Constraint for cast for   %mul147 = fmul double 1.000000e+00, %add146, !taffo.info !35, !taffo.initweight !17, !taffo.constinfo !29
main_add146_CAST_mul147_fixbits = solver.IntVar(0, 27, 'main_add146_CAST_mul147_fixbits')
main_add146_CAST_mul147_fixp = solver.IntVar(0, 1, 'main_add146_CAST_mul147_fixp')
main_add146_CAST_mul147_float = solver.IntVar(0, 1, 'main_add146_CAST_mul147_float')
main_add146_CAST_mul147_double = solver.IntVar(0, 1, 'main_add146_CAST_mul147_double')
solver.Add( + (1)*main_add146_CAST_mul147_fixp + (1)*main_add146_CAST_mul147_float + (1)*main_add146_CAST_mul147_double==1)    #exactly 1 type
solver.Add( + (1)*main_add146_CAST_mul147_fixbits + (-10000)*main_add146_CAST_mul147_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C1_main_add146_CAST_mul147')
C2_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C2_main_add146_CAST_mul147')
solver.Add( + (1)*main_add146_fixbits + (-1)*main_add146_CAST_mul147_fixbits + (-10000)*C1_main_add146_CAST_mul147<=0)    #Shift cost 1
solver.Add( + (-1)*main_add146_fixbits + (1)*main_add146_CAST_mul147_fixbits + (-10000)*C2_main_add146_CAST_mul147<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add146_CAST_mul147
castCostObj +=  + (1)*C2_main_add146_CAST_mul147
C3_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C3_main_add146_CAST_mul147')
C4_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C4_main_add146_CAST_mul147')
C5_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C5_main_add146_CAST_mul147')
C6_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C6_main_add146_CAST_mul147')
C7_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C7_main_add146_CAST_mul147')
C8_main_add146_CAST_mul147 = solver.IntVar(0, 1, 'C8_main_add146_CAST_mul147')
solver.Add( + (1)*main_add146_fixp + (1)*main_add146_CAST_mul147_float + (-1)*C3_main_add146_CAST_mul147<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add146_CAST_mul147
solver.Add( + (1)*main_add146_float + (1)*main_add146_CAST_mul147_fixp + (-1)*C4_main_add146_CAST_mul147<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add146_CAST_mul147
solver.Add( + (1)*main_add146_fixp + (1)*main_add146_CAST_mul147_double + (-1)*C5_main_add146_CAST_mul147<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add146_CAST_mul147
solver.Add( + (1)*main_add146_double + (1)*main_add146_CAST_mul147_fixp + (-1)*C6_main_add146_CAST_mul147<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add146_CAST_mul147
solver.Add( + (1)*main_add146_float + (1)*main_add146_CAST_mul147_double + (-1)*C7_main_add146_CAST_mul147<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add146_CAST_mul147
solver.Add( + (1)*main_add146_double + (1)*main_add146_CAST_mul147_float + (-1)*C8_main_add146_CAST_mul147<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add146_CAST_mul147



#Stuff for   %mul147 = fmul double 1.000000e+00, %add146, !taffo.info !35, !taffo.initweight !17, !taffo.constinfo !29
main_mul147_fixbits = solver.IntVar(0, 26, 'main_mul147_fixbits')
main_mul147_fixp = solver.IntVar(0, 1, 'main_mul147_fixp')
main_mul147_float = solver.IntVar(0, 1, 'main_mul147_float')
main_mul147_double = solver.IntVar(0, 1, 'main_mul147_double')
main_mul147_enob = solver.IntVar(-10000, 10000, 'main_mul147_enob')
solver.Add( + (1)*main_mul147_enob + (-1)*main_mul147_fixbits + (10000)*main_mul147_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul147_enob + (10000)*main_mul147_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul147_enob + (10000)*main_mul147_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul147_fixbits + (-10000)*main_mul147_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*main_mul147_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul147_enob
solver.Add( + (1)*main_mul147_fixp + (1)*main_mul147_float + (1)*main_mul147_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul147_fixbits + (-10000)*main_mul147_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__40_CAST_mul147_fixp + (-1)*main_add146_CAST_mul147_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__40_CAST_mul147_float + (-1)*main_add146_CAST_mul147_float==0)    #float equality
solver.Add( + (1)*ConstantValue__40_CAST_mul147_double + (-1)*main_add146_CAST_mul147_double==0)    #double equality
solver.Add( + (1)*ConstantValue__40_CAST_mul147_fixp + (-1)*main_mul147_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__40_CAST_mul147_float + (-1)*main_mul147_float==0)    #float equality
solver.Add( + (1)*ConstantValue__40_CAST_mul147_double + (-1)*main_mul147_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul147_fixp
mathCostObj +=  + (6)*main_mul147_float
mathCostObj +=  + (12.2551)*main_mul147_double
main_main_mul147_enob_1 = solver.IntVar(0, 1, 'main_main_mul147_enob_1')
main_main_mul147_enob_2 = solver.IntVar(0, 1, 'main_main_mul147_enob_2')
solver.Add( + (1)*main_main_mul147_enob_1 + (1)*main_main_mul147_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul147_enob + (-1)*main_add146_enob + (-10000)*main_main_mul147_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul147_enob + (-1)*ConstantValue__38_enob + (-10000)*main_main_mul147_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   store double %mul147, double* %arrayidx151, align 8, !taffo.info !11, !taffo.initweight !18
main_mul147_CAST_store_fixbits = solver.IntVar(0, 26, 'main_mul147_CAST_store_fixbits')
main_mul147_CAST_store_fixp = solver.IntVar(0, 1, 'main_mul147_CAST_store_fixp')
main_mul147_CAST_store_float = solver.IntVar(0, 1, 'main_mul147_CAST_store_float')
main_mul147_CAST_store_double = solver.IntVar(0, 1, 'main_mul147_CAST_store_double')
solver.Add( + (1)*main_mul147_CAST_store_fixp + (1)*main_mul147_CAST_store_float + (1)*main_mul147_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul147_CAST_store_fixbits + (-10000)*main_mul147_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul147_CAST_store = solver.IntVar(0, 1, 'C1_main_mul147_CAST_store')
C2_main_mul147_CAST_store = solver.IntVar(0, 1, 'C2_main_mul147_CAST_store')
solver.Add( + (1)*main_mul147_fixbits + (-1)*main_mul147_CAST_store_fixbits + (-10000)*C1_main_mul147_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul147_fixbits + (1)*main_mul147_CAST_store_fixbits + (-10000)*C2_main_mul147_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul147_CAST_store
castCostObj +=  + (1)*C2_main_mul147_CAST_store
C3_main_mul147_CAST_store = solver.IntVar(0, 1, 'C3_main_mul147_CAST_store')
C4_main_mul147_CAST_store = solver.IntVar(0, 1, 'C4_main_mul147_CAST_store')
C5_main_mul147_CAST_store = solver.IntVar(0, 1, 'C5_main_mul147_CAST_store')
C6_main_mul147_CAST_store = solver.IntVar(0, 1, 'C6_main_mul147_CAST_store')
C7_main_mul147_CAST_store = solver.IntVar(0, 1, 'C7_main_mul147_CAST_store')
C8_main_mul147_CAST_store = solver.IntVar(0, 1, 'C8_main_mul147_CAST_store')
solver.Add( + (1)*main_mul147_fixp + (1)*main_mul147_CAST_store_float + (-1)*C3_main_mul147_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul147_CAST_store
solver.Add( + (1)*main_mul147_float + (1)*main_mul147_CAST_store_fixp + (-1)*C4_main_mul147_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul147_CAST_store
solver.Add( + (1)*main_mul147_fixp + (1)*main_mul147_CAST_store_double + (-1)*C5_main_mul147_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul147_CAST_store
solver.Add( + (1)*main_mul147_double + (1)*main_mul147_CAST_store_fixp + (-1)*C6_main_mul147_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul147_CAST_store
solver.Add( + (1)*main_mul147_float + (1)*main_mul147_CAST_store_double + (-1)*C7_main_mul147_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul147_CAST_store
solver.Add( + (1)*main_mul147_double + (1)*main_mul147_CAST_store_float + (-1)*C8_main_mul147_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul147_CAST_store
solver.Add( + (1)*main_imgOut_fixp + (-1)*main_mul147_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_imgOut_float + (-1)*main_mul147_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_imgOut_double + (-1)*main_mul147_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_imgOut_fixbits + (-1)*main_mul147_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_imgOut_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_imgOut_enob_storeENOB')
solver.Add( + (1)*main_imgOut_enob_storeENOB + (-1)*main_imgOut_fixbits + (10000)*main_imgOut_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_imgOut_enob_storeENOB + (10000)*main_imgOut_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_imgOut_enob_storeENOB + (10000)*main_imgOut_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_imgOut_enob_storeENOB + (-1)*main_mul147_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_imgOut_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'main_imgOut_enob_memphi_main_tmp7')
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp7 + (-1)*main_imgOut_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
main_main_tmp7_enob_2 = solver.IntVar(0, 1, 'main_main_tmp7_enob_2')
main_main_tmp7_enob_3 = solver.IntVar(0, 1, 'main_main_tmp7_enob_3')
solver.Add( + (1)*main_main_tmp7_enob_1 + (1)*main_main_tmp7_enob_2 + (1)*main_main_tmp7_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp7 + (-1)*main_imgOut_enob_storeENOB + (10000)*main_main_tmp7_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_imgOut_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_imgOut_enob_memphi_main_tmp8')
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp8 + (-1)*main_imgOut_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
main_main_tmp8_enob_2 = solver.IntVar(0, 1, 'main_main_tmp8_enob_2')
main_main_tmp8_enob_3 = solver.IntVar(0, 1, 'main_main_tmp8_enob_3')
solver.Add( + (1)*main_main_tmp8_enob_1 + (1)*main_main_tmp8_enob_2 + (1)*main_main_tmp8_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp8 + (-1)*main_imgOut_enob_storeENOB + (10000)*main_main_tmp8_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_y1_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'main_y1_enob_memphi_main_tmp9')
solver.Add( + (1)*main_y1_enob_memphi_main_tmp9 + (-1)*main_y1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
solver.Add( + (1)*main_main_tmp9_enob_0==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_imgOut_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'main_imgOut_enob_memphi_main_tmp10')
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp10 + (-1)*main_imgOut_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_1 = solver.IntVar(0, 1, 'main_main_tmp10_enob_1')
main_main_tmp10_enob_2 = solver.IntVar(0, 1, 'main_main_tmp10_enob_2')
main_main_tmp10_enob_3 = solver.IntVar(0, 1, 'main_main_tmp10_enob_3')
solver.Add( + (1)*main_main_tmp10_enob_1 + (1)*main_main_tmp10_enob_2 + (1)*main_main_tmp10_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp10 + (-1)*main_imgOut_enob_storeENOB + (10000)*main_main_tmp10_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_y2_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'main_y2_enob_memphi_main_tmp11')
solver.Add( + (1)*main_y2_enob_memphi_main_tmp11 + (-1)*main_y2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_0 = solver.IntVar(0, 1, 'main_main_tmp11_enob_0')
solver.Add( + (1)*main_main_tmp11_enob_0==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_y1_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'main_y1_enob_memphi_main_tmp12')
solver.Add( + (1)*main_y1_enob_memphi_main_tmp12 + (-1)*main_y1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp12_enob_1 = solver.IntVar(0, 1, 'main_main_tmp12_enob_1')
main_main_tmp12_enob_2 = solver.IntVar(0, 1, 'main_main_tmp12_enob_2')
main_main_tmp12_enob_3 = solver.IntVar(0, 1, 'main_main_tmp12_enob_3')
main_main_tmp12_enob_4 = solver.IntVar(0, 1, 'main_main_tmp12_enob_4')
solver.Add( + (1)*main_main_tmp12_enob_1 + (1)*main_main_tmp12_enob_2 + (1)*main_main_tmp12_enob_3 + (1)*main_main_tmp12_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_y1_enob_memphi_main_tmp12 + (-1)*main_imgOut_enob_storeENOB + (10000)*main_main_tmp12_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_y2_enob_memphi_main_tmp13 = solver.IntVar(-10000, 10000, 'main_y2_enob_memphi_main_tmp13')
solver.Add( + (1)*main_y2_enob_memphi_main_tmp13 + (-1)*main_y2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp13_enob_1 = solver.IntVar(0, 1, 'main_main_tmp13_enob_1')
main_main_tmp13_enob_2 = solver.IntVar(0, 1, 'main_main_tmp13_enob_2')
main_main_tmp13_enob_3 = solver.IntVar(0, 1, 'main_main_tmp13_enob_3')
main_main_tmp13_enob_4 = solver.IntVar(0, 1, 'main_main_tmp13_enob_4')
main_main_tmp13_enob_5 = solver.IntVar(0, 1, 'main_main_tmp13_enob_5')
solver.Add( + (1)*main_main_tmp13_enob_1 + (1)*main_main_tmp13_enob_2 + (1)*main_main_tmp13_enob_3 + (1)*main_main_tmp13_enob_4 + (1)*main_main_tmp13_enob_5==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_y2_enob_memphi_main_tmp13 + (-1)*main_imgOut_enob_storeENOB + (10000)*main_main_tmp13_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add244 = fadd double %tmp12, %tmp13, !taffo.info !11, !taffo.initweight !20
main_y1_CAST_add244_fixbits = solver.IntVar(0, 27, 'main_y1_CAST_add244_fixbits')
main_y1_CAST_add244_fixp = solver.IntVar(0, 1, 'main_y1_CAST_add244_fixp')
main_y1_CAST_add244_float = solver.IntVar(0, 1, 'main_y1_CAST_add244_float')
main_y1_CAST_add244_double = solver.IntVar(0, 1, 'main_y1_CAST_add244_double')
solver.Add( + (1)*main_y1_CAST_add244_fixp + (1)*main_y1_CAST_add244_float + (1)*main_y1_CAST_add244_double==1)    #exactly 1 type
solver.Add( + (1)*main_y1_CAST_add244_fixbits + (-10000)*main_y1_CAST_add244_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C1_main_y1_CAST_add244')
C2_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C2_main_y1_CAST_add244')
solver.Add( + (1)*main_y1_fixbits + (-1)*main_y1_CAST_add244_fixbits + (-10000)*C1_main_y1_CAST_add244<=0)    #Shift cost 1
solver.Add( + (-1)*main_y1_fixbits + (1)*main_y1_CAST_add244_fixbits + (-10000)*C2_main_y1_CAST_add244<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y1_CAST_add244
castCostObj +=  + (1)*C2_main_y1_CAST_add244
C3_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C3_main_y1_CAST_add244')
C4_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C4_main_y1_CAST_add244')
C5_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C5_main_y1_CAST_add244')
C6_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C6_main_y1_CAST_add244')
C7_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C7_main_y1_CAST_add244')
C8_main_y1_CAST_add244 = solver.IntVar(0, 1, 'C8_main_y1_CAST_add244')
solver.Add( + (1)*main_y1_fixp + (1)*main_y1_CAST_add244_float + (-1)*C3_main_y1_CAST_add244<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y1_CAST_add244
solver.Add( + (1)*main_y1_float + (1)*main_y1_CAST_add244_fixp + (-1)*C4_main_y1_CAST_add244<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y1_CAST_add244
solver.Add( + (1)*main_y1_fixp + (1)*main_y1_CAST_add244_double + (-1)*C5_main_y1_CAST_add244<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y1_CAST_add244
solver.Add( + (1)*main_y1_double + (1)*main_y1_CAST_add244_fixp + (-1)*C6_main_y1_CAST_add244<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y1_CAST_add244
solver.Add( + (1)*main_y1_float + (1)*main_y1_CAST_add244_double + (-1)*C7_main_y1_CAST_add244<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y1_CAST_add244
solver.Add( + (1)*main_y1_double + (1)*main_y1_CAST_add244_float + (-1)*C8_main_y1_CAST_add244<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y1_CAST_add244



#Constraint for cast for   %add244 = fadd double %tmp12, %tmp13, !taffo.info !11, !taffo.initweight !20
main_y2_CAST_add244_fixbits = solver.IntVar(0, 27, 'main_y2_CAST_add244_fixbits')
main_y2_CAST_add244_fixp = solver.IntVar(0, 1, 'main_y2_CAST_add244_fixp')
main_y2_CAST_add244_float = solver.IntVar(0, 1, 'main_y2_CAST_add244_float')
main_y2_CAST_add244_double = solver.IntVar(0, 1, 'main_y2_CAST_add244_double')
solver.Add( + (1)*main_y2_CAST_add244_fixp + (1)*main_y2_CAST_add244_float + (1)*main_y2_CAST_add244_double==1)    #exactly 1 type
solver.Add( + (1)*main_y2_CAST_add244_fixbits + (-10000)*main_y2_CAST_add244_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C1_main_y2_CAST_add244')
C2_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C2_main_y2_CAST_add244')
solver.Add( + (1)*main_y2_fixbits + (-1)*main_y2_CAST_add244_fixbits + (-10000)*C1_main_y2_CAST_add244<=0)    #Shift cost 1
solver.Add( + (-1)*main_y2_fixbits + (1)*main_y2_CAST_add244_fixbits + (-10000)*C2_main_y2_CAST_add244<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y2_CAST_add244
castCostObj +=  + (1)*C2_main_y2_CAST_add244
C3_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C3_main_y2_CAST_add244')
C4_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C4_main_y2_CAST_add244')
C5_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C5_main_y2_CAST_add244')
C6_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C6_main_y2_CAST_add244')
C7_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C7_main_y2_CAST_add244')
C8_main_y2_CAST_add244 = solver.IntVar(0, 1, 'C8_main_y2_CAST_add244')
solver.Add( + (1)*main_y2_fixp + (1)*main_y2_CAST_add244_float + (-1)*C3_main_y2_CAST_add244<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y2_CAST_add244
solver.Add( + (1)*main_y2_float + (1)*main_y2_CAST_add244_fixp + (-1)*C4_main_y2_CAST_add244<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y2_CAST_add244
solver.Add( + (1)*main_y2_fixp + (1)*main_y2_CAST_add244_double + (-1)*C5_main_y2_CAST_add244<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y2_CAST_add244
solver.Add( + (1)*main_y2_double + (1)*main_y2_CAST_add244_fixp + (-1)*C6_main_y2_CAST_add244<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y2_CAST_add244
solver.Add( + (1)*main_y2_float + (1)*main_y2_CAST_add244_double + (-1)*C7_main_y2_CAST_add244<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y2_CAST_add244
solver.Add( + (1)*main_y2_double + (1)*main_y2_CAST_add244_float + (-1)*C8_main_y2_CAST_add244<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y2_CAST_add244



#Stuff for   %add244 = fadd double %tmp12, %tmp13, !taffo.info !11, !taffo.initweight !20
main_add244_fixbits = solver.IntVar(0, 27, 'main_add244_fixbits')
main_add244_fixp = solver.IntVar(0, 1, 'main_add244_fixp')
main_add244_float = solver.IntVar(0, 1, 'main_add244_float')
main_add244_double = solver.IntVar(0, 1, 'main_add244_double')
main_add244_enob = solver.IntVar(-10000, 10000, 'main_add244_enob')
solver.Add( + (1)*main_add244_enob + (-1)*main_add244_fixbits + (10000)*main_add244_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add244_enob + (10000)*main_add244_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add244_enob + (10000)*main_add244_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add244_fixbits + (-10000)*main_add244_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*main_add244_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add244_enob
solver.Add( + (1)*main_add244_fixp + (1)*main_add244_float + (1)*main_add244_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add244_fixbits + (-10000)*main_add244_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_y1_CAST_add244_fixp + (-1)*main_y2_CAST_add244_fixp==0)    #fix equality
solver.Add( + (1)*main_y1_CAST_add244_float + (-1)*main_y2_CAST_add244_float==0)    #float equality
solver.Add( + (1)*main_y1_CAST_add244_double + (-1)*main_y2_CAST_add244_double==0)    #double equality
solver.Add( + (1)*main_y1_CAST_add244_fixbits + (-1)*main_y2_CAST_add244_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_y1_CAST_add244_fixp + (-1)*main_add244_fixp==0)    #fix equality
solver.Add( + (1)*main_y1_CAST_add244_float + (-1)*main_add244_float==0)    #float equality
solver.Add( + (1)*main_y1_CAST_add244_double + (-1)*main_add244_double==0)    #double equality
solver.Add( + (1)*main_y1_CAST_add244_fixbits + (-1)*main_add244_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add244_fixp
mathCostObj +=  + (3)*main_add244_float
mathCostObj +=  + (6.64928)*main_add244_double
solver.Add( + (1)*main_add244_enob + (-1)*main_y1_enob_memphi_main_tmp12<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add244_enob + (-1)*main_y2_enob_memphi_main_tmp13<=0)    #Enob propagation in sum second addend



#Stuff for double 1.000000e+00
ConstantValue__41_fixbits = solver.IntVar(0, 31, 'ConstantValue__41_fixbits')
ConstantValue__41_fixp = solver.IntVar(0, 1, 'ConstantValue__41_fixp')
ConstantValue__41_float = solver.IntVar(0, 1, 'ConstantValue__41_float')
ConstantValue__41_double = solver.IntVar(0, 1, 'ConstantValue__41_double')
ConstantValue__41_enob = solver.IntVar(-10000, 10000, 'ConstantValue__41_enob')
solver.Add( + (1)*ConstantValue__41_enob + (-1)*ConstantValue__41_fixbits + (10000)*ConstantValue__41_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__41_enob + (10000)*ConstantValue__41_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__41_enob + (10000)*ConstantValue__41_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__41_fixbits + (-10000)*ConstantValue__41_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__41_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__41_fixp + (1)*ConstantValue__41_float + (1)*ConstantValue__41_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__41_fixbits + (-10000)*ConstantValue__41_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__42_fixbits = solver.IntVar(0, 31, 'ConstantValue__42_fixbits')
ConstantValue__42_fixp = solver.IntVar(0, 1, 'ConstantValue__42_fixp')
ConstantValue__42_float = solver.IntVar(0, 1, 'ConstantValue__42_float')
ConstantValue__42_double = solver.IntVar(0, 1, 'ConstantValue__42_double')
ConstantValue__42_enob = solver.IntVar(-10000, 10000, 'ConstantValue__42_enob')
solver.Add( + (1)*ConstantValue__42_enob + (-1)*ConstantValue__42_fixbits + (10000)*ConstantValue__42_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__42_enob + (10000)*ConstantValue__42_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__42_enob + (10000)*ConstantValue__42_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__42_fixbits + (-10000)*ConstantValue__42_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__42_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__42_fixp + (1)*ConstantValue__42_float + (1)*ConstantValue__42_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__42_fixbits + (-10000)*ConstantValue__42_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__43_fixbits = solver.IntVar(0, 31, 'ConstantValue__43_fixbits')
ConstantValue__43_fixp = solver.IntVar(0, 1, 'ConstantValue__43_fixp')
ConstantValue__43_float = solver.IntVar(0, 1, 'ConstantValue__43_float')
ConstantValue__43_double = solver.IntVar(0, 1, 'ConstantValue__43_double')
ConstantValue__43_enob = solver.IntVar(-10000, 10000, 'ConstantValue__43_enob')
solver.Add( + (1)*ConstantValue__43_enob + (-1)*ConstantValue__43_fixbits + (10000)*ConstantValue__43_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__43_enob + (10000)*ConstantValue__43_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__43_enob + (10000)*ConstantValue__43_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__43_fixbits + (-10000)*ConstantValue__43_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__43_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__43_fixp + (1)*ConstantValue__43_float + (1)*ConstantValue__43_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__43_fixbits + (-10000)*ConstantValue__43_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul245 = fmul double 1.000000e+00, %add244, !taffo.info !35, !taffo.initweight !17, !taffo.constinfo !29
ConstantValue__43_CAST_mul245_fixbits = solver.IntVar(0, 31, 'ConstantValue__43_CAST_mul245_fixbits')
ConstantValue__43_CAST_mul245_fixp = solver.IntVar(0, 1, 'ConstantValue__43_CAST_mul245_fixp')
ConstantValue__43_CAST_mul245_float = solver.IntVar(0, 1, 'ConstantValue__43_CAST_mul245_float')
ConstantValue__43_CAST_mul245_double = solver.IntVar(0, 1, 'ConstantValue__43_CAST_mul245_double')
solver.Add( + (1)*ConstantValue__43_CAST_mul245_fixp + (1)*ConstantValue__43_CAST_mul245_float + (1)*ConstantValue__43_CAST_mul245_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__43_CAST_mul245_fixbits + (-10000)*ConstantValue__43_CAST_mul245_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C1_ConstantValue__43_CAST_mul245')
C2_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C2_ConstantValue__43_CAST_mul245')
solver.Add( + (1)*ConstantValue__43_fixbits + (-1)*ConstantValue__43_CAST_mul245_fixbits + (-10000)*C1_ConstantValue__43_CAST_mul245<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__43_fixbits + (1)*ConstantValue__43_CAST_mul245_fixbits + (-10000)*C2_ConstantValue__43_CAST_mul245<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__43_CAST_mul245
castCostObj +=  + (1)*C2_ConstantValue__43_CAST_mul245
C3_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C3_ConstantValue__43_CAST_mul245')
C4_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C4_ConstantValue__43_CAST_mul245')
C5_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C5_ConstantValue__43_CAST_mul245')
C6_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C6_ConstantValue__43_CAST_mul245')
C7_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C7_ConstantValue__43_CAST_mul245')
C8_ConstantValue__43_CAST_mul245 = solver.IntVar(0, 1, 'C8_ConstantValue__43_CAST_mul245')
solver.Add( + (1)*ConstantValue__43_fixp + (1)*ConstantValue__43_CAST_mul245_float + (-1)*C3_ConstantValue__43_CAST_mul245<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__43_CAST_mul245
solver.Add( + (1)*ConstantValue__43_float + (1)*ConstantValue__43_CAST_mul245_fixp + (-1)*C4_ConstantValue__43_CAST_mul245<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__43_CAST_mul245
solver.Add( + (1)*ConstantValue__43_fixp + (1)*ConstantValue__43_CAST_mul245_double + (-1)*C5_ConstantValue__43_CAST_mul245<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__43_CAST_mul245
solver.Add( + (1)*ConstantValue__43_double + (1)*ConstantValue__43_CAST_mul245_fixp + (-1)*C6_ConstantValue__43_CAST_mul245<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__43_CAST_mul245
solver.Add( + (1)*ConstantValue__43_float + (1)*ConstantValue__43_CAST_mul245_double + (-1)*C7_ConstantValue__43_CAST_mul245<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__43_CAST_mul245
solver.Add( + (1)*ConstantValue__43_double + (1)*ConstantValue__43_CAST_mul245_float + (-1)*C8_ConstantValue__43_CAST_mul245<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__43_CAST_mul245



#Constraint for cast for   %mul245 = fmul double 1.000000e+00, %add244, !taffo.info !35, !taffo.initweight !17, !taffo.constinfo !29
main_add244_CAST_mul245_fixbits = solver.IntVar(0, 27, 'main_add244_CAST_mul245_fixbits')
main_add244_CAST_mul245_fixp = solver.IntVar(0, 1, 'main_add244_CAST_mul245_fixp')
main_add244_CAST_mul245_float = solver.IntVar(0, 1, 'main_add244_CAST_mul245_float')
main_add244_CAST_mul245_double = solver.IntVar(0, 1, 'main_add244_CAST_mul245_double')
solver.Add( + (1)*main_add244_CAST_mul245_fixp + (1)*main_add244_CAST_mul245_float + (1)*main_add244_CAST_mul245_double==1)    #exactly 1 type
solver.Add( + (1)*main_add244_CAST_mul245_fixbits + (-10000)*main_add244_CAST_mul245_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C1_main_add244_CAST_mul245')
C2_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C2_main_add244_CAST_mul245')
solver.Add( + (1)*main_add244_fixbits + (-1)*main_add244_CAST_mul245_fixbits + (-10000)*C1_main_add244_CAST_mul245<=0)    #Shift cost 1
solver.Add( + (-1)*main_add244_fixbits + (1)*main_add244_CAST_mul245_fixbits + (-10000)*C2_main_add244_CAST_mul245<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add244_CAST_mul245
castCostObj +=  + (1)*C2_main_add244_CAST_mul245
C3_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C3_main_add244_CAST_mul245')
C4_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C4_main_add244_CAST_mul245')
C5_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C5_main_add244_CAST_mul245')
C6_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C6_main_add244_CAST_mul245')
C7_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C7_main_add244_CAST_mul245')
C8_main_add244_CAST_mul245 = solver.IntVar(0, 1, 'C8_main_add244_CAST_mul245')
solver.Add( + (1)*main_add244_fixp + (1)*main_add244_CAST_mul245_float + (-1)*C3_main_add244_CAST_mul245<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add244_CAST_mul245
solver.Add( + (1)*main_add244_float + (1)*main_add244_CAST_mul245_fixp + (-1)*C4_main_add244_CAST_mul245<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add244_CAST_mul245
solver.Add( + (1)*main_add244_fixp + (1)*main_add244_CAST_mul245_double + (-1)*C5_main_add244_CAST_mul245<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add244_CAST_mul245
solver.Add( + (1)*main_add244_double + (1)*main_add244_CAST_mul245_fixp + (-1)*C6_main_add244_CAST_mul245<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add244_CAST_mul245
solver.Add( + (1)*main_add244_float + (1)*main_add244_CAST_mul245_double + (-1)*C7_main_add244_CAST_mul245<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add244_CAST_mul245
solver.Add( + (1)*main_add244_double + (1)*main_add244_CAST_mul245_float + (-1)*C8_main_add244_CAST_mul245<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add244_CAST_mul245



#Stuff for   %mul245 = fmul double 1.000000e+00, %add244, !taffo.info !35, !taffo.initweight !17, !taffo.constinfo !29
main_mul245_fixbits = solver.IntVar(0, 26, 'main_mul245_fixbits')
main_mul245_fixp = solver.IntVar(0, 1, 'main_mul245_fixp')
main_mul245_float = solver.IntVar(0, 1, 'main_mul245_float')
main_mul245_double = solver.IntVar(0, 1, 'main_mul245_double')
main_mul245_enob = solver.IntVar(-10000, 10000, 'main_mul245_enob')
solver.Add( + (1)*main_mul245_enob + (-1)*main_mul245_fixbits + (10000)*main_mul245_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul245_enob + (10000)*main_mul245_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul245_enob + (10000)*main_mul245_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul245_fixbits + (-10000)*main_mul245_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*main_mul245_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul245_enob
solver.Add( + (1)*main_mul245_fixp + (1)*main_mul245_float + (1)*main_mul245_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul245_fixbits + (-10000)*main_mul245_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__43_CAST_mul245_fixp + (-1)*main_add244_CAST_mul245_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__43_CAST_mul245_float + (-1)*main_add244_CAST_mul245_float==0)    #float equality
solver.Add( + (1)*ConstantValue__43_CAST_mul245_double + (-1)*main_add244_CAST_mul245_double==0)    #double equality
solver.Add( + (1)*ConstantValue__43_CAST_mul245_fixp + (-1)*main_mul245_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__43_CAST_mul245_float + (-1)*main_mul245_float==0)    #float equality
solver.Add( + (1)*ConstantValue__43_CAST_mul245_double + (-1)*main_mul245_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul245_fixp
mathCostObj +=  + (6)*main_mul245_float
mathCostObj +=  + (12.2551)*main_mul245_double
main_main_mul245_enob_1 = solver.IntVar(0, 1, 'main_main_mul245_enob_1')
main_main_mul245_enob_2 = solver.IntVar(0, 1, 'main_main_mul245_enob_2')
solver.Add( + (1)*main_main_mul245_enob_1 + (1)*main_main_mul245_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul245_enob + (-1)*main_add244_enob + (-10000)*main_main_mul245_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul245_enob + (-1)*ConstantValue__41_enob + (-10000)*main_main_mul245_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   store double %mul245, double* %arrayidx249, align 8, !taffo.info !11, !taffo.initweight !18
main_mul245_CAST_store_fixbits = solver.IntVar(0, 26, 'main_mul245_CAST_store_fixbits')
main_mul245_CAST_store_fixp = solver.IntVar(0, 1, 'main_mul245_CAST_store_fixp')
main_mul245_CAST_store_float = solver.IntVar(0, 1, 'main_mul245_CAST_store_float')
main_mul245_CAST_store_double = solver.IntVar(0, 1, 'main_mul245_CAST_store_double')
solver.Add( + (1)*main_mul245_CAST_store_fixp + (1)*main_mul245_CAST_store_float + (1)*main_mul245_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul245_CAST_store_fixbits + (-10000)*main_mul245_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul245_CAST_store = solver.IntVar(0, 1, 'C1_main_mul245_CAST_store')
C2_main_mul245_CAST_store = solver.IntVar(0, 1, 'C2_main_mul245_CAST_store')
solver.Add( + (1)*main_mul245_fixbits + (-1)*main_mul245_CAST_store_fixbits + (-10000)*C1_main_mul245_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul245_fixbits + (1)*main_mul245_CAST_store_fixbits + (-10000)*C2_main_mul245_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul245_CAST_store
castCostObj +=  + (1)*C2_main_mul245_CAST_store
C3_main_mul245_CAST_store = solver.IntVar(0, 1, 'C3_main_mul245_CAST_store')
C4_main_mul245_CAST_store = solver.IntVar(0, 1, 'C4_main_mul245_CAST_store')
C5_main_mul245_CAST_store = solver.IntVar(0, 1, 'C5_main_mul245_CAST_store')
C6_main_mul245_CAST_store = solver.IntVar(0, 1, 'C6_main_mul245_CAST_store')
C7_main_mul245_CAST_store = solver.IntVar(0, 1, 'C7_main_mul245_CAST_store')
C8_main_mul245_CAST_store = solver.IntVar(0, 1, 'C8_main_mul245_CAST_store')
solver.Add( + (1)*main_mul245_fixp + (1)*main_mul245_CAST_store_float + (-1)*C3_main_mul245_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul245_CAST_store
solver.Add( + (1)*main_mul245_float + (1)*main_mul245_CAST_store_fixp + (-1)*C4_main_mul245_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul245_CAST_store
solver.Add( + (1)*main_mul245_fixp + (1)*main_mul245_CAST_store_double + (-1)*C5_main_mul245_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul245_CAST_store
solver.Add( + (1)*main_mul245_double + (1)*main_mul245_CAST_store_fixp + (-1)*C6_main_mul245_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul245_CAST_store
solver.Add( + (1)*main_mul245_float + (1)*main_mul245_CAST_store_double + (-1)*C7_main_mul245_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul245_CAST_store
solver.Add( + (1)*main_mul245_double + (1)*main_mul245_CAST_store_float + (-1)*C8_main_mul245_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul245_CAST_store
solver.Add( + (1)*main_imgOut_fixp + (-1)*main_mul245_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_imgOut_float + (-1)*main_mul245_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_imgOut_double + (-1)*main_mul245_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_imgOut_fixbits + (-1)*main_mul245_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_imgOut_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_imgOut_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_imgOut_enob_storeENOB_storeENOB + (-1)*main_imgOut_fixbits + (10000)*main_imgOut_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_imgOut_enob_storeENOB_storeENOB + (10000)*main_imgOut_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_imgOut_enob_storeENOB_storeENOB + (10000)*main_imgOut_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_imgOut_enob_storeENOB_storeENOB + (-1)*main_mul245_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
main_imgOut_enob_memphi_main_tmp16 = solver.IntVar(-10000, 10000, 'main_imgOut_enob_memphi_main_tmp16')
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp16 + (-1)*main_imgOut_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp16_enob_1 = solver.IntVar(0, 1, 'main_main_tmp16_enob_1')
main_main_tmp16_enob_2 = solver.IntVar(0, 1, 'main_main_tmp16_enob_2')
main_main_tmp16_enob_3 = solver.IntVar(0, 1, 'main_main_tmp16_enob_3')
main_main_tmp16_enob_4 = solver.IntVar(0, 1, 'main_main_tmp16_enob_4')
main_main_tmp16_enob_5 = solver.IntVar(0, 1, 'main_main_tmp16_enob_5')
main_main_tmp16_enob_6 = solver.IntVar(0, 1, 'main_main_tmp16_enob_6')
solver.Add( + (1)*main_main_tmp16_enob_1 + (1)*main_main_tmp16_enob_2 + (1)*main_main_tmp16_enob_3 + (1)*main_main_tmp16_enob_4 + (1)*main_main_tmp16_enob_5 + (1)*main_main_tmp16_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp16 + (-1)*main_imgOut_enob_storeENOB + (10000)*main_main_tmp16_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_imgOut_enob_memphi_main_tmp16 + (-1)*main_imgOut_enob_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_6<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call274 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp15, i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.7, i32 0, i32 0), double %tmp16), !taffo.info !11, !taffo.initweight !20, !taffo.constinfo !57
main_imgOut_CAST_call274_fixbits = solver.IntVar(0, 27, 'main_imgOut_CAST_call274_fixbits')
main_imgOut_CAST_call274_fixp = solver.IntVar(0, 1, 'main_imgOut_CAST_call274_fixp')
main_imgOut_CAST_call274_float = solver.IntVar(0, 1, 'main_imgOut_CAST_call274_float')
main_imgOut_CAST_call274_double = solver.IntVar(0, 1, 'main_imgOut_CAST_call274_double')
solver.Add( + (1)*main_imgOut_CAST_call274_fixp + (1)*main_imgOut_CAST_call274_float + (1)*main_imgOut_CAST_call274_double==1)    #exactly 1 type
solver.Add( + (1)*main_imgOut_CAST_call274_fixbits + (-10000)*main_imgOut_CAST_call274_fixp<=0)    #If no fix, fix frac part = 0
C1_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C1_main_imgOut_CAST_call274')
C2_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C2_main_imgOut_CAST_call274')
solver.Add( + (1)*main_imgOut_fixbits + (-1)*main_imgOut_CAST_call274_fixbits + (-10000)*C1_main_imgOut_CAST_call274<=0)    #Shift cost 1
solver.Add( + (-1)*main_imgOut_fixbits + (1)*main_imgOut_CAST_call274_fixbits + (-10000)*C2_main_imgOut_CAST_call274<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_imgOut_CAST_call274
castCostObj +=  + (1)*C2_main_imgOut_CAST_call274
C3_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C3_main_imgOut_CAST_call274')
C4_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C4_main_imgOut_CAST_call274')
C5_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C5_main_imgOut_CAST_call274')
C6_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C6_main_imgOut_CAST_call274')
C7_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C7_main_imgOut_CAST_call274')
C8_main_imgOut_CAST_call274 = solver.IntVar(0, 1, 'C8_main_imgOut_CAST_call274')
solver.Add( + (1)*main_imgOut_fixp + (1)*main_imgOut_CAST_call274_float + (-1)*C3_main_imgOut_CAST_call274<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_imgOut_CAST_call274
solver.Add( + (1)*main_imgOut_float + (1)*main_imgOut_CAST_call274_fixp + (-1)*C4_main_imgOut_CAST_call274<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_imgOut_CAST_call274
solver.Add( + (1)*main_imgOut_fixp + (1)*main_imgOut_CAST_call274_double + (-1)*C5_main_imgOut_CAST_call274<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_imgOut_CAST_call274
solver.Add( + (1)*main_imgOut_double + (1)*main_imgOut_CAST_call274_fixp + (-1)*C6_main_imgOut_CAST_call274<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_imgOut_CAST_call274
solver.Add( + (1)*main_imgOut_float + (1)*main_imgOut_CAST_call274_double + (-1)*C7_main_imgOut_CAST_call274<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_imgOut_CAST_call274
solver.Add( + (1)*main_imgOut_double + (1)*main_imgOut_CAST_call274_float + (-1)*C8_main_imgOut_CAST_call274<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_imgOut_CAST_call274
solver.Add( + (1)*main_imgOut_CAST_call274_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(10000 * castCostObj / 382.122+ 1 * enobCostObj / 10740+ 10000 * mathCostObj / 49.8087)

# Model declaration end.