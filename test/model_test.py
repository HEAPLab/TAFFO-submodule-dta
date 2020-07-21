


#Stuff for   %A = alloca [400 x [400 x double]], align 16, !taffo.info !11, !taffo.initweight !14
main_A_fixbits = solver.IntVar(0, 31, 'main_A_fixbits')
main_A_fixp = solver.IntVar(0, 1, 'main_A_fixp')
main_A_float = solver.IntVar(0, 1, 'main_A_float')
main_A_double = solver.IntVar(0, 1, 'main_A_double')
main_A_enob = solver.IntVar(-10000, 10000, 'main_A_enob')
solver.Add( + (1)*main_A_enob + (-1)*main_A_fixbits + (10000)*main_A_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_A_enob + (10000)*main_A_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_A_enob + (10000)*main_A_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_A_fixbits + (-10000)*main_A_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_A_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_A_double<=0)    #Disable double data type
enobCostObj =  + (-1)*main_A_enob
solver.Add( + (1)*main_A_fixp + (1)*main_A_float + (1)*main_A_double==1)    #Exactly one selected type
solver.Add( + (1)*main_A_fixbits + (-10000)*main_A_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %x1 = alloca [400 x double], align 16, !taffo.info !15, !taffo.initweight !14
main_x1_fixbits = solver.IntVar(0, 22, 'main_x1_fixbits')
main_x1_fixp = solver.IntVar(0, 1, 'main_x1_fixp')
main_x1_float = solver.IntVar(0, 1, 'main_x1_float')
main_x1_double = solver.IntVar(0, 1, 'main_x1_double')
main_x1_enob = solver.IntVar(-10000, 10000, 'main_x1_enob')
solver.Add( + (1)*main_x1_enob + (-1)*main_x1_fixbits + (10000)*main_x1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_x1_enob + (10000)*main_x1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_x1_enob + (10000)*main_x1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_x1_fixbits + (-10000)*main_x1_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_x1_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_x1_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_x1_enob
solver.Add( + (1)*main_x1_fixp + (1)*main_x1_float + (1)*main_x1_double==1)    #Exactly one selected type
solver.Add( + (1)*main_x1_fixbits + (-10000)*main_x1_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %x2 = alloca [400 x double], align 16, !taffo.info !15, !taffo.initweight !14
main_x2_fixbits = solver.IntVar(0, 22, 'main_x2_fixbits')
main_x2_fixp = solver.IntVar(0, 1, 'main_x2_fixp')
main_x2_float = solver.IntVar(0, 1, 'main_x2_float')
main_x2_double = solver.IntVar(0, 1, 'main_x2_double')
main_x2_enob = solver.IntVar(-10000, 10000, 'main_x2_enob')
solver.Add( + (1)*main_x2_enob + (-1)*main_x2_fixbits + (10000)*main_x2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_x2_enob + (10000)*main_x2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_x2_enob + (10000)*main_x2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_x2_fixbits + (-10000)*main_x2_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_x2_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_x2_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_x2_enob
solver.Add( + (1)*main_x2_fixp + (1)*main_x2_float + (1)*main_x2_double==1)    #Exactly one selected type
solver.Add( + (1)*main_x2_fixbits + (-10000)*main_x2_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %y_1 = alloca [400 x double], align 16, !taffo.info !11, !taffo.initweight !14
main_y_1_fixbits = solver.IntVar(0, 31, 'main_y_1_fixbits')
main_y_1_fixp = solver.IntVar(0, 1, 'main_y_1_fixp')
main_y_1_float = solver.IntVar(0, 1, 'main_y_1_float')
main_y_1_double = solver.IntVar(0, 1, 'main_y_1_double')
main_y_1_enob = solver.IntVar(-10000, 10000, 'main_y_1_enob')
solver.Add( + (1)*main_y_1_enob + (-1)*main_y_1_fixbits + (10000)*main_y_1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_y_1_enob + (10000)*main_y_1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_y_1_enob + (10000)*main_y_1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_y_1_fixbits + (-10000)*main_y_1_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_y_1_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_y_1_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_y_1_enob
solver.Add( + (1)*main_y_1_fixp + (1)*main_y_1_float + (1)*main_y_1_double==1)    #Exactly one selected type
solver.Add( + (1)*main_y_1_fixbits + (-10000)*main_y_1_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %y_2 = alloca [400 x double], align 16, !taffo.info !11, !taffo.initweight !14
main_y_2_fixbits = solver.IntVar(0, 31, 'main_y_2_fixbits')
main_y_2_fixp = solver.IntVar(0, 1, 'main_y_2_fixp')
main_y_2_float = solver.IntVar(0, 1, 'main_y_2_float')
main_y_2_double = solver.IntVar(0, 1, 'main_y_2_double')
main_y_2_enob = solver.IntVar(-10000, 10000, 'main_y_2_enob')
solver.Add( + (1)*main_y_2_enob + (-1)*main_y_2_fixbits + (10000)*main_y_2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_y_2_enob + (10000)*main_y_2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_y_2_enob + (10000)*main_y_2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_y_2_fixbits + (-10000)*main_y_2_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_y_2_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_y_2_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_y_2_enob
solver.Add( + (1)*main_y_2_fixp + (1)*main_y_2_float + (1)*main_y_2_double==1)    #Exactly one selected type
solver.Add( + (1)*main_y_2_fixbits + (-10000)*main_y_2_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
main_x1_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'main_x1_enob_memphi_main_tmp')
solver.Add( + (1)*main_x1_enob_memphi_main_tmp + (-1)*main_x1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
main_main_tmp_enob_2 = solver.IntVar(0, 1, 'main_main_tmp_enob_2')
main_main_tmp_enob_3 = solver.IntVar(0, 1, 'main_main_tmp_enob_3')
solver.Add( + (1)*main_main_tmp_enob_1 + (1)*main_main_tmp_enob_2 + (1)*main_main_tmp_enob_3==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp1')
solver.Add( + (1)*main_A_enob_memphi_main_tmp1 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
solver.Add( + (1)*main_main_tmp1_enob_1 + (1)*main_main_tmp1_enob_2==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_y_1_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'main_y_1_enob_memphi_main_tmp2')
solver.Add( + (1)*main_y_1_enob_memphi_main_tmp2 + (-1)*main_y_1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
main_main_tmp2_enob_2 = solver.IntVar(0, 1, 'main_main_tmp2_enob_2')
solver.Add( + (1)*main_main_tmp2_enob_1 + (1)*main_main_tmp2_enob_2==1)    #Enob: one selected constraint



#Constraint for cast for   %mul60 = fmul double %tmp1, %tmp2, !taffo.info !11, !taffo.initweight !22
main_A_CAST_mul60_fixbits = solver.IntVar(0, 31, 'main_A_CAST_mul60_fixbits')
main_A_CAST_mul60_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul60_fixp')
main_A_CAST_mul60_float = solver.IntVar(0, 1, 'main_A_CAST_mul60_float')
main_A_CAST_mul60_double = solver.IntVar(0, 1, 'main_A_CAST_mul60_double')
solver.Add( + (1)*main_A_CAST_mul60_fixp + (1)*main_A_CAST_mul60_float + (1)*main_A_CAST_mul60_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul60_fixbits + (-10000)*main_A_CAST_mul60_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul60')
C2_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul60')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul60_fixbits + (-10000)*C1_main_A_CAST_mul60<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul60_fixbits + (-10000)*C2_main_A_CAST_mul60<=0)    #Shift cost 2
castCostObj =  + (1)*C1_main_A_CAST_mul60
castCostObj +=  + (1)*C2_main_A_CAST_mul60
C3_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul60')
C4_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul60')
C5_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul60')
C6_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul60')
C7_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul60')
C8_main_A_CAST_mul60 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul60')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul60_float + (-1)*C3_main_A_CAST_mul60<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul60
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul60_fixp + (-1)*C4_main_A_CAST_mul60<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul60
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul60_double + (-1)*C5_main_A_CAST_mul60<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul60
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul60_fixp + (-1)*C6_main_A_CAST_mul60<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul60
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul60_double + (-1)*C7_main_A_CAST_mul60<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul60
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul60_float + (-1)*C8_main_A_CAST_mul60<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul60



#Constraint for cast for   %mul60 = fmul double %tmp1, %tmp2, !taffo.info !11, !taffo.initweight !22
main_y_1_CAST_mul60_fixbits = solver.IntVar(0, 31, 'main_y_1_CAST_mul60_fixbits')
main_y_1_CAST_mul60_fixp = solver.IntVar(0, 1, 'main_y_1_CAST_mul60_fixp')
main_y_1_CAST_mul60_float = solver.IntVar(0, 1, 'main_y_1_CAST_mul60_float')
main_y_1_CAST_mul60_double = solver.IntVar(0, 1, 'main_y_1_CAST_mul60_double')
solver.Add( + (1)*main_y_1_CAST_mul60_fixp + (1)*main_y_1_CAST_mul60_float + (1)*main_y_1_CAST_mul60_double==1)    #exactly 1 type
solver.Add( + (1)*main_y_1_CAST_mul60_fixbits + (-10000)*main_y_1_CAST_mul60_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C1_main_y_1_CAST_mul60')
C2_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C2_main_y_1_CAST_mul60')
solver.Add( + (1)*main_y_1_fixbits + (-1)*main_y_1_CAST_mul60_fixbits + (-10000)*C1_main_y_1_CAST_mul60<=0)    #Shift cost 1
solver.Add( + (-1)*main_y_1_fixbits + (1)*main_y_1_CAST_mul60_fixbits + (-10000)*C2_main_y_1_CAST_mul60<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y_1_CAST_mul60
castCostObj +=  + (1)*C2_main_y_1_CAST_mul60
C3_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C3_main_y_1_CAST_mul60')
C4_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C4_main_y_1_CAST_mul60')
C5_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C5_main_y_1_CAST_mul60')
C6_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C6_main_y_1_CAST_mul60')
C7_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C7_main_y_1_CAST_mul60')
C8_main_y_1_CAST_mul60 = solver.IntVar(0, 1, 'C8_main_y_1_CAST_mul60')
solver.Add( + (1)*main_y_1_fixp + (1)*main_y_1_CAST_mul60_float + (-1)*C3_main_y_1_CAST_mul60<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y_1_CAST_mul60
solver.Add( + (1)*main_y_1_float + (1)*main_y_1_CAST_mul60_fixp + (-1)*C4_main_y_1_CAST_mul60<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y_1_CAST_mul60
solver.Add( + (1)*main_y_1_fixp + (1)*main_y_1_CAST_mul60_double + (-1)*C5_main_y_1_CAST_mul60<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y_1_CAST_mul60
solver.Add( + (1)*main_y_1_double + (1)*main_y_1_CAST_mul60_fixp + (-1)*C6_main_y_1_CAST_mul60<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y_1_CAST_mul60
solver.Add( + (1)*main_y_1_float + (1)*main_y_1_CAST_mul60_double + (-1)*C7_main_y_1_CAST_mul60<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y_1_CAST_mul60
solver.Add( + (1)*main_y_1_double + (1)*main_y_1_CAST_mul60_float + (-1)*C8_main_y_1_CAST_mul60<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y_1_CAST_mul60



#Stuff for   %mul60 = fmul double %tmp1, %tmp2, !taffo.info !11, !taffo.initweight !22
main_mul60_fixbits = solver.IntVar(0, 31, 'main_mul60_fixbits')
main_mul60_fixp = solver.IntVar(0, 1, 'main_mul60_fixp')
main_mul60_float = solver.IntVar(0, 1, 'main_mul60_float')
main_mul60_double = solver.IntVar(0, 1, 'main_mul60_double')
main_mul60_enob = solver.IntVar(-10000, 10000, 'main_mul60_enob')
solver.Add( + (1)*main_mul60_enob + (-1)*main_mul60_fixbits + (10000)*main_mul60_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul60_enob + (10000)*main_mul60_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul60_enob + (10000)*main_mul60_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul60_fixbits + (-10000)*main_mul60_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_mul60_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul60_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul60_enob
solver.Add( + (1)*main_mul60_fixp + (1)*main_mul60_float + (1)*main_mul60_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul60_fixbits + (-10000)*main_mul60_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul60_fixp + (-1)*main_y_1_CAST_mul60_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul60_float + (-1)*main_y_1_CAST_mul60_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul60_double + (-1)*main_y_1_CAST_mul60_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul60_fixp + (-1)*main_mul60_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul60_float + (-1)*main_mul60_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul60_double + (-1)*main_mul60_double==0)    #double equality
mathCostObj =  + (1.65217)*main_mul60_fixp
mathCostObj +=  + (6)*main_mul60_float
mathCostObj +=  + (12.2551)*main_mul60_double
main_main_mul60_enob_1 = solver.IntVar(0, 1, 'main_main_mul60_enob_1')
main_main_mul60_enob_2 = solver.IntVar(0, 1, 'main_main_mul60_enob_2')
solver.Add( + (1)*main_main_mul60_enob_1 + (1)*main_main_mul60_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul60_enob + (-1)*main_y_1_enob_memphi_main_tmp2 + (-10000)*main_main_mul60_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul60_enob + (-1)*main_A_enob_memphi_main_tmp1 + (-10000)*main_main_mul60_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add61 = fadd double %tmp, %mul60, !taffo.info !40, !taffo.initweight !22
main_x1_CAST_add61_fixbits = solver.IntVar(0, 22, 'main_x1_CAST_add61_fixbits')
main_x1_CAST_add61_fixp = solver.IntVar(0, 1, 'main_x1_CAST_add61_fixp')
main_x1_CAST_add61_float = solver.IntVar(0, 1, 'main_x1_CAST_add61_float')
main_x1_CAST_add61_double = solver.IntVar(0, 1, 'main_x1_CAST_add61_double')
solver.Add( + (1)*main_x1_CAST_add61_fixp + (1)*main_x1_CAST_add61_float + (1)*main_x1_CAST_add61_double==1)    #exactly 1 type
solver.Add( + (1)*main_x1_CAST_add61_fixbits + (-10000)*main_x1_CAST_add61_fixp<=0)    #If no fix, fix frac part = 0
C1_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C1_main_x1_CAST_add61')
C2_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C2_main_x1_CAST_add61')
solver.Add( + (1)*main_x1_fixbits + (-1)*main_x1_CAST_add61_fixbits + (-10000)*C1_main_x1_CAST_add61<=0)    #Shift cost 1
solver.Add( + (-1)*main_x1_fixbits + (1)*main_x1_CAST_add61_fixbits + (-10000)*C2_main_x1_CAST_add61<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_x1_CAST_add61
castCostObj +=  + (1)*C2_main_x1_CAST_add61
C3_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C3_main_x1_CAST_add61')
C4_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C4_main_x1_CAST_add61')
C5_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C5_main_x1_CAST_add61')
C6_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C6_main_x1_CAST_add61')
C7_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C7_main_x1_CAST_add61')
C8_main_x1_CAST_add61 = solver.IntVar(0, 1, 'C8_main_x1_CAST_add61')
solver.Add( + (1)*main_x1_fixp + (1)*main_x1_CAST_add61_float + (-1)*C3_main_x1_CAST_add61<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_x1_CAST_add61
solver.Add( + (1)*main_x1_float + (1)*main_x1_CAST_add61_fixp + (-1)*C4_main_x1_CAST_add61<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_x1_CAST_add61
solver.Add( + (1)*main_x1_fixp + (1)*main_x1_CAST_add61_double + (-1)*C5_main_x1_CAST_add61<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_x1_CAST_add61
solver.Add( + (1)*main_x1_double + (1)*main_x1_CAST_add61_fixp + (-1)*C6_main_x1_CAST_add61<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_x1_CAST_add61
solver.Add( + (1)*main_x1_float + (1)*main_x1_CAST_add61_double + (-1)*C7_main_x1_CAST_add61<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_x1_CAST_add61
solver.Add( + (1)*main_x1_double + (1)*main_x1_CAST_add61_float + (-1)*C8_main_x1_CAST_add61<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_x1_CAST_add61



#Constraint for cast for   %add61 = fadd double %tmp, %mul60, !taffo.info !40, !taffo.initweight !22
main_mul60_CAST_add61_fixbits = solver.IntVar(0, 31, 'main_mul60_CAST_add61_fixbits')
main_mul60_CAST_add61_fixp = solver.IntVar(0, 1, 'main_mul60_CAST_add61_fixp')
main_mul60_CAST_add61_float = solver.IntVar(0, 1, 'main_mul60_CAST_add61_float')
main_mul60_CAST_add61_double = solver.IntVar(0, 1, 'main_mul60_CAST_add61_double')
solver.Add( + (1)*main_mul60_CAST_add61_fixp + (1)*main_mul60_CAST_add61_float + (1)*main_mul60_CAST_add61_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul60_CAST_add61_fixbits + (-10000)*main_mul60_CAST_add61_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C1_main_mul60_CAST_add61')
C2_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C2_main_mul60_CAST_add61')
solver.Add( + (1)*main_mul60_fixbits + (-1)*main_mul60_CAST_add61_fixbits + (-10000)*C1_main_mul60_CAST_add61<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul60_fixbits + (1)*main_mul60_CAST_add61_fixbits + (-10000)*C2_main_mul60_CAST_add61<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul60_CAST_add61
castCostObj +=  + (1)*C2_main_mul60_CAST_add61
C3_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C3_main_mul60_CAST_add61')
C4_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C4_main_mul60_CAST_add61')
C5_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C5_main_mul60_CAST_add61')
C6_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C6_main_mul60_CAST_add61')
C7_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C7_main_mul60_CAST_add61')
C8_main_mul60_CAST_add61 = solver.IntVar(0, 1, 'C8_main_mul60_CAST_add61')
solver.Add( + (1)*main_mul60_fixp + (1)*main_mul60_CAST_add61_float + (-1)*C3_main_mul60_CAST_add61<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul60_CAST_add61
solver.Add( + (1)*main_mul60_float + (1)*main_mul60_CAST_add61_fixp + (-1)*C4_main_mul60_CAST_add61<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul60_CAST_add61
solver.Add( + (1)*main_mul60_fixp + (1)*main_mul60_CAST_add61_double + (-1)*C5_main_mul60_CAST_add61<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul60_CAST_add61
solver.Add( + (1)*main_mul60_double + (1)*main_mul60_CAST_add61_fixp + (-1)*C6_main_mul60_CAST_add61<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul60_CAST_add61
solver.Add( + (1)*main_mul60_float + (1)*main_mul60_CAST_add61_double + (-1)*C7_main_mul60_CAST_add61<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul60_CAST_add61
solver.Add( + (1)*main_mul60_double + (1)*main_mul60_CAST_add61_float + (-1)*C8_main_mul60_CAST_add61<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul60_CAST_add61



#Stuff for   %add61 = fadd double %tmp, %mul60, !taffo.info !40, !taffo.initweight !22
main_add61_fixbits = solver.IntVar(0, 22, 'main_add61_fixbits')
main_add61_fixp = solver.IntVar(0, 1, 'main_add61_fixp')
main_add61_float = solver.IntVar(0, 1, 'main_add61_float')
main_add61_double = solver.IntVar(0, 1, 'main_add61_double')
main_add61_enob = solver.IntVar(-10000, 10000, 'main_add61_enob')
solver.Add( + (1)*main_add61_enob + (-1)*main_add61_fixbits + (10000)*main_add61_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add61_enob + (10000)*main_add61_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add61_enob + (10000)*main_add61_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add61_fixbits + (-10000)*main_add61_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_add61_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add61_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add61_enob
solver.Add( + (1)*main_add61_fixp + (1)*main_add61_float + (1)*main_add61_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add61_fixbits + (-10000)*main_add61_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_x1_CAST_add61_fixp + (-1)*main_mul60_CAST_add61_fixp==0)    #fix equality
solver.Add( + (1)*main_x1_CAST_add61_float + (-1)*main_mul60_CAST_add61_float==0)    #float equality
solver.Add( + (1)*main_x1_CAST_add61_double + (-1)*main_mul60_CAST_add61_double==0)    #double equality
solver.Add( + (1)*main_x1_CAST_add61_fixbits + (-1)*main_mul60_CAST_add61_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_x1_CAST_add61_fixp + (-1)*main_add61_fixp==0)    #fix equality
solver.Add( + (1)*main_x1_CAST_add61_float + (-1)*main_add61_float==0)    #float equality
solver.Add( + (1)*main_x1_CAST_add61_double + (-1)*main_add61_double==0)    #double equality
solver.Add( + (1)*main_x1_CAST_add61_fixbits + (-1)*main_add61_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add61_fixp
mathCostObj +=  + (3)*main_add61_float
mathCostObj +=  + (6.64928)*main_add61_double
solver.Add( + (1)*main_add61_enob + (-1)*main_x1_enob_memphi_main_tmp<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add61_enob + (-1)*main_mul60_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add61, double* %arrayidx63, align 8, !taffo.info !15, !taffo.initweight !21
main_add61_CAST_store_fixbits = solver.IntVar(0, 22, 'main_add61_CAST_store_fixbits')
main_add61_CAST_store_fixp = solver.IntVar(0, 1, 'main_add61_CAST_store_fixp')
main_add61_CAST_store_float = solver.IntVar(0, 1, 'main_add61_CAST_store_float')
main_add61_CAST_store_double = solver.IntVar(0, 1, 'main_add61_CAST_store_double')
solver.Add( + (1)*main_add61_CAST_store_fixp + (1)*main_add61_CAST_store_float + (1)*main_add61_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add61_CAST_store_fixbits + (-10000)*main_add61_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add61_CAST_store = solver.IntVar(0, 1, 'C1_main_add61_CAST_store')
C2_main_add61_CAST_store = solver.IntVar(0, 1, 'C2_main_add61_CAST_store')
solver.Add( + (1)*main_add61_fixbits + (-1)*main_add61_CAST_store_fixbits + (-10000)*C1_main_add61_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add61_fixbits + (1)*main_add61_CAST_store_fixbits + (-10000)*C2_main_add61_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add61_CAST_store
castCostObj +=  + (1)*C2_main_add61_CAST_store
C3_main_add61_CAST_store = solver.IntVar(0, 1, 'C3_main_add61_CAST_store')
C4_main_add61_CAST_store = solver.IntVar(0, 1, 'C4_main_add61_CAST_store')
C5_main_add61_CAST_store = solver.IntVar(0, 1, 'C5_main_add61_CAST_store')
C6_main_add61_CAST_store = solver.IntVar(0, 1, 'C6_main_add61_CAST_store')
C7_main_add61_CAST_store = solver.IntVar(0, 1, 'C7_main_add61_CAST_store')
C8_main_add61_CAST_store = solver.IntVar(0, 1, 'C8_main_add61_CAST_store')
solver.Add( + (1)*main_add61_fixp + (1)*main_add61_CAST_store_float + (-1)*C3_main_add61_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add61_CAST_store
solver.Add( + (1)*main_add61_float + (1)*main_add61_CAST_store_fixp + (-1)*C4_main_add61_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add61_CAST_store
solver.Add( + (1)*main_add61_fixp + (1)*main_add61_CAST_store_double + (-1)*C5_main_add61_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add61_CAST_store
solver.Add( + (1)*main_add61_double + (1)*main_add61_CAST_store_fixp + (-1)*C6_main_add61_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add61_CAST_store
solver.Add( + (1)*main_add61_float + (1)*main_add61_CAST_store_double + (-1)*C7_main_add61_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add61_CAST_store
solver.Add( + (1)*main_add61_double + (1)*main_add61_CAST_store_float + (-1)*C8_main_add61_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add61_CAST_store
solver.Add( + (1)*main_x1_fixp + (-1)*main_add61_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_x1_float + (-1)*main_add61_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_x1_double + (-1)*main_add61_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_x1_fixbits + (-1)*main_add61_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_x1_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_x1_enob_storeENOB')
solver.Add( + (1)*main_x1_enob_storeENOB + (-1)*main_x1_fixbits + (10000)*main_x1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_x1_enob_storeENOB + (10000)*main_x1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_x1_enob_storeENOB + (10000)*main_x1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_x1_enob_storeENOB + (-1)*main_add61_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_x1_enob_memphi_main_tmp + (-1)*main_x1_enob_storeENOB + (10000)*main_main_tmp_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_x2_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'main_x2_enob_memphi_main_tmp3')
solver.Add( + (1)*main_x2_enob_memphi_main_tmp3 + (-1)*main_x2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3 + (1)*main_main_tmp3_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_x2_enob_memphi_main_tmp3 + (-1)*main_x1_enob_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_A_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'main_A_enob_memphi_main_tmp4')
solver.Add( + (1)*main_A_enob_memphi_main_tmp4 + (-1)*main_A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
main_y_2_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'main_y_2_enob_memphi_main_tmp5')
solver.Add( + (1)*main_y_2_enob_memphi_main_tmp5 + (-1)*main_y_2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_2==1)    #Enob: one selected constraint



#Constraint for cast for   %mul86 = fmul double %tmp4, %tmp5, !taffo.info !11, !taffo.initweight !22
main_A_CAST_mul86_fixbits = solver.IntVar(0, 31, 'main_A_CAST_mul86_fixbits')
main_A_CAST_mul86_fixp = solver.IntVar(0, 1, 'main_A_CAST_mul86_fixp')
main_A_CAST_mul86_float = solver.IntVar(0, 1, 'main_A_CAST_mul86_float')
main_A_CAST_mul86_double = solver.IntVar(0, 1, 'main_A_CAST_mul86_double')
solver.Add( + (1)*main_A_CAST_mul86_fixp + (1)*main_A_CAST_mul86_float + (1)*main_A_CAST_mul86_double==1)    #exactly 1 type
solver.Add( + (1)*main_A_CAST_mul86_fixbits + (-10000)*main_A_CAST_mul86_fixp<=0)    #If no fix, fix frac part = 0
C1_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C1_main_A_CAST_mul86')
C2_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C2_main_A_CAST_mul86')
solver.Add( + (1)*main_A_fixbits + (-1)*main_A_CAST_mul86_fixbits + (-10000)*C1_main_A_CAST_mul86<=0)    #Shift cost 1
solver.Add( + (-1)*main_A_fixbits + (1)*main_A_CAST_mul86_fixbits + (-10000)*C2_main_A_CAST_mul86<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_A_CAST_mul86
castCostObj +=  + (1)*C2_main_A_CAST_mul86
C3_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C3_main_A_CAST_mul86')
C4_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C4_main_A_CAST_mul86')
C5_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C5_main_A_CAST_mul86')
C6_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C6_main_A_CAST_mul86')
C7_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C7_main_A_CAST_mul86')
C8_main_A_CAST_mul86 = solver.IntVar(0, 1, 'C8_main_A_CAST_mul86')
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul86_float + (-1)*C3_main_A_CAST_mul86<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_A_CAST_mul86
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul86_fixp + (-1)*C4_main_A_CAST_mul86<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_A_CAST_mul86
solver.Add( + (1)*main_A_fixp + (1)*main_A_CAST_mul86_double + (-1)*C5_main_A_CAST_mul86<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_A_CAST_mul86
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul86_fixp + (-1)*C6_main_A_CAST_mul86<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_A_CAST_mul86
solver.Add( + (1)*main_A_float + (1)*main_A_CAST_mul86_double + (-1)*C7_main_A_CAST_mul86<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_A_CAST_mul86
solver.Add( + (1)*main_A_double + (1)*main_A_CAST_mul86_float + (-1)*C8_main_A_CAST_mul86<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_A_CAST_mul86



#Constraint for cast for   %mul86 = fmul double %tmp4, %tmp5, !taffo.info !11, !taffo.initweight !22
main_y_2_CAST_mul86_fixbits = solver.IntVar(0, 31, 'main_y_2_CAST_mul86_fixbits')
main_y_2_CAST_mul86_fixp = solver.IntVar(0, 1, 'main_y_2_CAST_mul86_fixp')
main_y_2_CAST_mul86_float = solver.IntVar(0, 1, 'main_y_2_CAST_mul86_float')
main_y_2_CAST_mul86_double = solver.IntVar(0, 1, 'main_y_2_CAST_mul86_double')
solver.Add( + (1)*main_y_2_CAST_mul86_fixp + (1)*main_y_2_CAST_mul86_float + (1)*main_y_2_CAST_mul86_double==1)    #exactly 1 type
solver.Add( + (1)*main_y_2_CAST_mul86_fixbits + (-10000)*main_y_2_CAST_mul86_fixp<=0)    #If no fix, fix frac part = 0
C1_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C1_main_y_2_CAST_mul86')
C2_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C2_main_y_2_CAST_mul86')
solver.Add( + (1)*main_y_2_fixbits + (-1)*main_y_2_CAST_mul86_fixbits + (-10000)*C1_main_y_2_CAST_mul86<=0)    #Shift cost 1
solver.Add( + (-1)*main_y_2_fixbits + (1)*main_y_2_CAST_mul86_fixbits + (-10000)*C2_main_y_2_CAST_mul86<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_y_2_CAST_mul86
castCostObj +=  + (1)*C2_main_y_2_CAST_mul86
C3_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C3_main_y_2_CAST_mul86')
C4_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C4_main_y_2_CAST_mul86')
C5_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C5_main_y_2_CAST_mul86')
C6_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C6_main_y_2_CAST_mul86')
C7_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C7_main_y_2_CAST_mul86')
C8_main_y_2_CAST_mul86 = solver.IntVar(0, 1, 'C8_main_y_2_CAST_mul86')
solver.Add( + (1)*main_y_2_fixp + (1)*main_y_2_CAST_mul86_float + (-1)*C3_main_y_2_CAST_mul86<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_y_2_CAST_mul86
solver.Add( + (1)*main_y_2_float + (1)*main_y_2_CAST_mul86_fixp + (-1)*C4_main_y_2_CAST_mul86<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_y_2_CAST_mul86
solver.Add( + (1)*main_y_2_fixp + (1)*main_y_2_CAST_mul86_double + (-1)*C5_main_y_2_CAST_mul86<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_y_2_CAST_mul86
solver.Add( + (1)*main_y_2_double + (1)*main_y_2_CAST_mul86_fixp + (-1)*C6_main_y_2_CAST_mul86<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_y_2_CAST_mul86
solver.Add( + (1)*main_y_2_float + (1)*main_y_2_CAST_mul86_double + (-1)*C7_main_y_2_CAST_mul86<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_y_2_CAST_mul86
solver.Add( + (1)*main_y_2_double + (1)*main_y_2_CAST_mul86_float + (-1)*C8_main_y_2_CAST_mul86<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_y_2_CAST_mul86



#Stuff for   %mul86 = fmul double %tmp4, %tmp5, !taffo.info !11, !taffo.initweight !22
main_mul86_fixbits = solver.IntVar(0, 31, 'main_mul86_fixbits')
main_mul86_fixp = solver.IntVar(0, 1, 'main_mul86_fixp')
main_mul86_float = solver.IntVar(0, 1, 'main_mul86_float')
main_mul86_double = solver.IntVar(0, 1, 'main_mul86_double')
main_mul86_enob = solver.IntVar(-10000, 10000, 'main_mul86_enob')
solver.Add( + (1)*main_mul86_enob + (-1)*main_mul86_fixbits + (10000)*main_mul86_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul86_enob + (10000)*main_mul86_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul86_enob + (10000)*main_mul86_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul86_fixbits + (-10000)*main_mul86_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_mul86_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_mul86_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul86_enob
solver.Add( + (1)*main_mul86_fixp + (1)*main_mul86_float + (1)*main_mul86_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul86_fixbits + (-10000)*main_mul86_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_A_CAST_mul86_fixp + (-1)*main_y_2_CAST_mul86_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul86_float + (-1)*main_y_2_CAST_mul86_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul86_double + (-1)*main_y_2_CAST_mul86_double==0)    #double equality
solver.Add( + (1)*main_A_CAST_mul86_fixp + (-1)*main_mul86_fixp==0)    #fix equality
solver.Add( + (1)*main_A_CAST_mul86_float + (-1)*main_mul86_float==0)    #float equality
solver.Add( + (1)*main_A_CAST_mul86_double + (-1)*main_mul86_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul86_fixp
mathCostObj +=  + (6)*main_mul86_float
mathCostObj +=  + (12.2551)*main_mul86_double
main_main_mul86_enob_1 = solver.IntVar(0, 1, 'main_main_mul86_enob_1')
main_main_mul86_enob_2 = solver.IntVar(0, 1, 'main_main_mul86_enob_2')
solver.Add( + (1)*main_main_mul86_enob_1 + (1)*main_main_mul86_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul86_enob + (-1)*main_y_2_enob_memphi_main_tmp5 + (-10000)*main_main_mul86_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul86_enob + (-1)*main_A_enob_memphi_main_tmp4 + (-10000)*main_main_mul86_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add87 = fadd double %tmp3, %mul86, !taffo.info !40, !taffo.initweight !22
main_x2_CAST_add87_fixbits = solver.IntVar(0, 22, 'main_x2_CAST_add87_fixbits')
main_x2_CAST_add87_fixp = solver.IntVar(0, 1, 'main_x2_CAST_add87_fixp')
main_x2_CAST_add87_float = solver.IntVar(0, 1, 'main_x2_CAST_add87_float')
main_x2_CAST_add87_double = solver.IntVar(0, 1, 'main_x2_CAST_add87_double')
solver.Add( + (1)*main_x2_CAST_add87_fixp + (1)*main_x2_CAST_add87_float + (1)*main_x2_CAST_add87_double==1)    #exactly 1 type
solver.Add( + (1)*main_x2_CAST_add87_fixbits + (-10000)*main_x2_CAST_add87_fixp<=0)    #If no fix, fix frac part = 0
C1_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C1_main_x2_CAST_add87')
C2_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C2_main_x2_CAST_add87')
solver.Add( + (1)*main_x2_fixbits + (-1)*main_x2_CAST_add87_fixbits + (-10000)*C1_main_x2_CAST_add87<=0)    #Shift cost 1
solver.Add( + (-1)*main_x2_fixbits + (1)*main_x2_CAST_add87_fixbits + (-10000)*C2_main_x2_CAST_add87<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_x2_CAST_add87
castCostObj +=  + (1)*C2_main_x2_CAST_add87
C3_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C3_main_x2_CAST_add87')
C4_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C4_main_x2_CAST_add87')
C5_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C5_main_x2_CAST_add87')
C6_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C6_main_x2_CAST_add87')
C7_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C7_main_x2_CAST_add87')
C8_main_x2_CAST_add87 = solver.IntVar(0, 1, 'C8_main_x2_CAST_add87')
solver.Add( + (1)*main_x2_fixp + (1)*main_x2_CAST_add87_float + (-1)*C3_main_x2_CAST_add87<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_x2_CAST_add87
solver.Add( + (1)*main_x2_float + (1)*main_x2_CAST_add87_fixp + (-1)*C4_main_x2_CAST_add87<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_x2_CAST_add87
solver.Add( + (1)*main_x2_fixp + (1)*main_x2_CAST_add87_double + (-1)*C5_main_x2_CAST_add87<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_x2_CAST_add87
solver.Add( + (1)*main_x2_double + (1)*main_x2_CAST_add87_fixp + (-1)*C6_main_x2_CAST_add87<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_x2_CAST_add87
solver.Add( + (1)*main_x2_float + (1)*main_x2_CAST_add87_double + (-1)*C7_main_x2_CAST_add87<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_x2_CAST_add87
solver.Add( + (1)*main_x2_double + (1)*main_x2_CAST_add87_float + (-1)*C8_main_x2_CAST_add87<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_x2_CAST_add87



#Constraint for cast for   %add87 = fadd double %tmp3, %mul86, !taffo.info !40, !taffo.initweight !22
main_mul86_CAST_add87_fixbits = solver.IntVar(0, 31, 'main_mul86_CAST_add87_fixbits')
main_mul86_CAST_add87_fixp = solver.IntVar(0, 1, 'main_mul86_CAST_add87_fixp')
main_mul86_CAST_add87_float = solver.IntVar(0, 1, 'main_mul86_CAST_add87_float')
main_mul86_CAST_add87_double = solver.IntVar(0, 1, 'main_mul86_CAST_add87_double')
solver.Add( + (1)*main_mul86_CAST_add87_fixp + (1)*main_mul86_CAST_add87_float + (1)*main_mul86_CAST_add87_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul86_CAST_add87_fixbits + (-10000)*main_mul86_CAST_add87_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C1_main_mul86_CAST_add87')
C2_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C2_main_mul86_CAST_add87')
solver.Add( + (1)*main_mul86_fixbits + (-1)*main_mul86_CAST_add87_fixbits + (-10000)*C1_main_mul86_CAST_add87<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul86_fixbits + (1)*main_mul86_CAST_add87_fixbits + (-10000)*C2_main_mul86_CAST_add87<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul86_CAST_add87
castCostObj +=  + (1)*C2_main_mul86_CAST_add87
C3_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C3_main_mul86_CAST_add87')
C4_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C4_main_mul86_CAST_add87')
C5_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C5_main_mul86_CAST_add87')
C6_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C6_main_mul86_CAST_add87')
C7_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C7_main_mul86_CAST_add87')
C8_main_mul86_CAST_add87 = solver.IntVar(0, 1, 'C8_main_mul86_CAST_add87')
solver.Add( + (1)*main_mul86_fixp + (1)*main_mul86_CAST_add87_float + (-1)*C3_main_mul86_CAST_add87<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul86_CAST_add87
solver.Add( + (1)*main_mul86_float + (1)*main_mul86_CAST_add87_fixp + (-1)*C4_main_mul86_CAST_add87<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul86_CAST_add87
solver.Add( + (1)*main_mul86_fixp + (1)*main_mul86_CAST_add87_double + (-1)*C5_main_mul86_CAST_add87<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul86_CAST_add87
solver.Add( + (1)*main_mul86_double + (1)*main_mul86_CAST_add87_fixp + (-1)*C6_main_mul86_CAST_add87<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul86_CAST_add87
solver.Add( + (1)*main_mul86_float + (1)*main_mul86_CAST_add87_double + (-1)*C7_main_mul86_CAST_add87<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul86_CAST_add87
solver.Add( + (1)*main_mul86_double + (1)*main_mul86_CAST_add87_float + (-1)*C8_main_mul86_CAST_add87<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul86_CAST_add87



#Stuff for   %add87 = fadd double %tmp3, %mul86, !taffo.info !40, !taffo.initweight !22
main_add87_fixbits = solver.IntVar(0, 22, 'main_add87_fixbits')
main_add87_fixp = solver.IntVar(0, 1, 'main_add87_fixp')
main_add87_float = solver.IntVar(0, 1, 'main_add87_float')
main_add87_double = solver.IntVar(0, 1, 'main_add87_double')
main_add87_enob = solver.IntVar(-10000, 10000, 'main_add87_enob')
solver.Add( + (1)*main_add87_enob + (-1)*main_add87_fixbits + (10000)*main_add87_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add87_enob + (10000)*main_add87_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add87_enob + (10000)*main_add87_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add87_fixbits + (-10000)*main_add87_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_add87_enob<=333)    #Enob constraint for error maximal
solver.Add( + (1)*main_add87_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add87_enob
solver.Add( + (1)*main_add87_fixp + (1)*main_add87_float + (1)*main_add87_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add87_fixbits + (-10000)*main_add87_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_x2_CAST_add87_fixp + (-1)*main_mul86_CAST_add87_fixp==0)    #fix equality
solver.Add( + (1)*main_x2_CAST_add87_float + (-1)*main_mul86_CAST_add87_float==0)    #float equality
solver.Add( + (1)*main_x2_CAST_add87_double + (-1)*main_mul86_CAST_add87_double==0)    #double equality
solver.Add( + (1)*main_x2_CAST_add87_fixbits + (-1)*main_mul86_CAST_add87_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_x2_CAST_add87_fixp + (-1)*main_add87_fixp==0)    #fix equality
solver.Add( + (1)*main_x2_CAST_add87_float + (-1)*main_add87_float==0)    #float equality
solver.Add( + (1)*main_x2_CAST_add87_double + (-1)*main_add87_double==0)    #double equality
solver.Add( + (1)*main_x2_CAST_add87_fixbits + (-1)*main_add87_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add87_fixp
mathCostObj +=  + (3)*main_add87_float
mathCostObj +=  + (6.64928)*main_add87_double
solver.Add( + (1)*main_add87_enob + (-1)*main_x2_enob_memphi_main_tmp3<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add87_enob + (-1)*main_mul86_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add87, double* %arrayidx89, align 8, !taffo.info !15, !taffo.initweight !21
main_add87_CAST_store_fixbits = solver.IntVar(0, 22, 'main_add87_CAST_store_fixbits')
main_add87_CAST_store_fixp = solver.IntVar(0, 1, 'main_add87_CAST_store_fixp')
main_add87_CAST_store_float = solver.IntVar(0, 1, 'main_add87_CAST_store_float')
main_add87_CAST_store_double = solver.IntVar(0, 1, 'main_add87_CAST_store_double')
solver.Add( + (1)*main_add87_CAST_store_fixp + (1)*main_add87_CAST_store_float + (1)*main_add87_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add87_CAST_store_fixbits + (-10000)*main_add87_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add87_CAST_store = solver.IntVar(0, 1, 'C1_main_add87_CAST_store')
C2_main_add87_CAST_store = solver.IntVar(0, 1, 'C2_main_add87_CAST_store')
solver.Add( + (1)*main_add87_fixbits + (-1)*main_add87_CAST_store_fixbits + (-10000)*C1_main_add87_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add87_fixbits + (1)*main_add87_CAST_store_fixbits + (-10000)*C2_main_add87_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add87_CAST_store
castCostObj +=  + (1)*C2_main_add87_CAST_store
C3_main_add87_CAST_store = solver.IntVar(0, 1, 'C3_main_add87_CAST_store')
C4_main_add87_CAST_store = solver.IntVar(0, 1, 'C4_main_add87_CAST_store')
C5_main_add87_CAST_store = solver.IntVar(0, 1, 'C5_main_add87_CAST_store')
C6_main_add87_CAST_store = solver.IntVar(0, 1, 'C6_main_add87_CAST_store')
C7_main_add87_CAST_store = solver.IntVar(0, 1, 'C7_main_add87_CAST_store')
C8_main_add87_CAST_store = solver.IntVar(0, 1, 'C8_main_add87_CAST_store')
solver.Add( + (1)*main_add87_fixp + (1)*main_add87_CAST_store_float + (-1)*C3_main_add87_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add87_CAST_store
solver.Add( + (1)*main_add87_float + (1)*main_add87_CAST_store_fixp + (-1)*C4_main_add87_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add87_CAST_store
solver.Add( + (1)*main_add87_fixp + (1)*main_add87_CAST_store_double + (-1)*C5_main_add87_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add87_CAST_store
solver.Add( + (1)*main_add87_double + (1)*main_add87_CAST_store_fixp + (-1)*C6_main_add87_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add87_CAST_store
solver.Add( + (1)*main_add87_float + (1)*main_add87_CAST_store_double + (-1)*C7_main_add87_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add87_CAST_store
solver.Add( + (1)*main_add87_double + (1)*main_add87_CAST_store_float + (-1)*C8_main_add87_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add87_CAST_store
solver.Add( + (1)*main_x2_fixp + (-1)*main_add87_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_x2_float + (-1)*main_add87_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_x2_double + (-1)*main_add87_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_x2_fixbits + (-1)*main_add87_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_x2_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_x2_enob_storeENOB')
solver.Add( + (1)*main_x2_enob_storeENOB + (-1)*main_x2_fixbits + (10000)*main_x2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_x2_enob_storeENOB + (10000)*main_x2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_x2_enob_storeENOB + (10000)*main_x2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_x2_enob_storeENOB + (-1)*main_add87_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_x2_enob_memphi_main_tmp3 + (-1)*main_x2_enob_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_x1_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'main_x1_enob_memphi_main_tmp8')
solver.Add( + (1)*main_x1_enob_memphi_main_tmp8 + (-1)*main_x1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
main_main_tmp8_enob_2 = solver.IntVar(0, 1, 'main_main_tmp8_enob_2')
main_main_tmp8_enob_3 = solver.IntVar(0, 1, 'main_main_tmp8_enob_3')
solver.Add( + (1)*main_main_tmp8_enob_1 + (1)*main_main_tmp8_enob_2 + (1)*main_main_tmp8_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_x1_enob_memphi_main_tmp8 + (-1)*main_x1_enob_storeENOB + (10000)*main_main_tmp8_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call105 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp7, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.5, i32 0, i32 0), double %tmp8), !taffo.info !15, !taffo.initweight !22, !taffo.constinfo !45
main_x1_CAST_call105_fixbits = solver.IntVar(0, 22, 'main_x1_CAST_call105_fixbits')
main_x1_CAST_call105_fixp = solver.IntVar(0, 1, 'main_x1_CAST_call105_fixp')
main_x1_CAST_call105_float = solver.IntVar(0, 1, 'main_x1_CAST_call105_float')
main_x1_CAST_call105_double = solver.IntVar(0, 1, 'main_x1_CAST_call105_double')
solver.Add( + (1)*main_x1_CAST_call105_fixp + (1)*main_x1_CAST_call105_float + (1)*main_x1_CAST_call105_double==1)    #exactly 1 type
solver.Add( + (1)*main_x1_CAST_call105_fixbits + (-10000)*main_x1_CAST_call105_fixp<=0)    #If no fix, fix frac part = 0
C1_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C1_main_x1_CAST_call105')
C2_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C2_main_x1_CAST_call105')
solver.Add( + (1)*main_x1_fixbits + (-1)*main_x1_CAST_call105_fixbits + (-10000)*C1_main_x1_CAST_call105<=0)    #Shift cost 1
solver.Add( + (-1)*main_x1_fixbits + (1)*main_x1_CAST_call105_fixbits + (-10000)*C2_main_x1_CAST_call105<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_x1_CAST_call105
castCostObj +=  + (1)*C2_main_x1_CAST_call105
C3_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C3_main_x1_CAST_call105')
C4_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C4_main_x1_CAST_call105')
C5_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C5_main_x1_CAST_call105')
C6_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C6_main_x1_CAST_call105')
C7_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C7_main_x1_CAST_call105')
C8_main_x1_CAST_call105 = solver.IntVar(0, 1, 'C8_main_x1_CAST_call105')
solver.Add( + (1)*main_x1_fixp + (1)*main_x1_CAST_call105_float + (-1)*C3_main_x1_CAST_call105<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_x1_CAST_call105
solver.Add( + (1)*main_x1_float + (1)*main_x1_CAST_call105_fixp + (-1)*C4_main_x1_CAST_call105<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_x1_CAST_call105
solver.Add( + (1)*main_x1_fixp + (1)*main_x1_CAST_call105_double + (-1)*C5_main_x1_CAST_call105<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_x1_CAST_call105
solver.Add( + (1)*main_x1_double + (1)*main_x1_CAST_call105_fixp + (-1)*C6_main_x1_CAST_call105<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_x1_CAST_call105
solver.Add( + (1)*main_x1_float + (1)*main_x1_CAST_call105_double + (-1)*C7_main_x1_CAST_call105<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_x1_CAST_call105
solver.Add( + (1)*main_x1_double + (1)*main_x1_CAST_call105_float + (-1)*C8_main_x1_CAST_call105<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_x1_CAST_call105
solver.Add( + (1)*main_x1_CAST_call105_double==1)    #Type constraint for argument value

#Restriction for new enob [LOAD]
main_x2_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'main_x2_enob_memphi_main_tmp11')
solver.Add( + (1)*main_x2_enob_memphi_main_tmp11 + (-1)*main_x2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_1 = solver.IntVar(0, 1, 'main_main_tmp11_enob_1')
main_main_tmp11_enob_2 = solver.IntVar(0, 1, 'main_main_tmp11_enob_2')
main_main_tmp11_enob_3 = solver.IntVar(0, 1, 'main_main_tmp11_enob_3')
main_main_tmp11_enob_4 = solver.IntVar(0, 1, 'main_main_tmp11_enob_4')
solver.Add( + (1)*main_main_tmp11_enob_1 + (1)*main_main_tmp11_enob_2 + (1)*main_main_tmp11_enob_3 + (1)*main_main_tmp11_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_x2_enob_memphi_main_tmp11 + (-1)*main_x1_enob_storeENOB + (10000)*main_main_tmp11_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_x2_enob_memphi_main_tmp11 + (-1)*main_x2_enob_storeENOB + (10000)*main_main_tmp11_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call121 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp10, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.5, i32 0, i32 0), double %tmp11), !taffo.info !15, !taffo.initweight !22, !taffo.constinfo !45
main_x2_CAST_call121_fixbits = solver.IntVar(0, 22, 'main_x2_CAST_call121_fixbits')
main_x2_CAST_call121_fixp = solver.IntVar(0, 1, 'main_x2_CAST_call121_fixp')
main_x2_CAST_call121_float = solver.IntVar(0, 1, 'main_x2_CAST_call121_float')
main_x2_CAST_call121_double = solver.IntVar(0, 1, 'main_x2_CAST_call121_double')
solver.Add( + (1)*main_x2_CAST_call121_fixp + (1)*main_x2_CAST_call121_float + (1)*main_x2_CAST_call121_double==1)    #exactly 1 type
solver.Add( + (1)*main_x2_CAST_call121_fixbits + (-10000)*main_x2_CAST_call121_fixp<=0)    #If no fix, fix frac part = 0
C1_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C1_main_x2_CAST_call121')
C2_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C2_main_x2_CAST_call121')
solver.Add( + (1)*main_x2_fixbits + (-1)*main_x2_CAST_call121_fixbits + (-10000)*C1_main_x2_CAST_call121<=0)    #Shift cost 1
solver.Add( + (-1)*main_x2_fixbits + (1)*main_x2_CAST_call121_fixbits + (-10000)*C2_main_x2_CAST_call121<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_x2_CAST_call121
castCostObj +=  + (1)*C2_main_x2_CAST_call121
C3_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C3_main_x2_CAST_call121')
C4_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C4_main_x2_CAST_call121')
C5_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C5_main_x2_CAST_call121')
C6_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C6_main_x2_CAST_call121')
C7_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C7_main_x2_CAST_call121')
C8_main_x2_CAST_call121 = solver.IntVar(0, 1, 'C8_main_x2_CAST_call121')
solver.Add( + (1)*main_x2_fixp + (1)*main_x2_CAST_call121_float + (-1)*C3_main_x2_CAST_call121<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_x2_CAST_call121
solver.Add( + (1)*main_x2_float + (1)*main_x2_CAST_call121_fixp + (-1)*C4_main_x2_CAST_call121<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_x2_CAST_call121
solver.Add( + (1)*main_x2_fixp + (1)*main_x2_CAST_call121_double + (-1)*C5_main_x2_CAST_call121<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_x2_CAST_call121
solver.Add( + (1)*main_x2_double + (1)*main_x2_CAST_call121_fixp + (-1)*C6_main_x2_CAST_call121<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_x2_CAST_call121
solver.Add( + (1)*main_x2_float + (1)*main_x2_CAST_call121_double + (-1)*C7_main_x2_CAST_call121<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_x2_CAST_call121
solver.Add( + (1)*main_x2_double + (1)*main_x2_CAST_call121_float + (-1)*C8_main_x2_CAST_call121<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_x2_CAST_call121
solver.Add( + (1)*main_x2_CAST_call121_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(10000 * castCostObj / 191.061+ 1 * enobCostObj / 2997+ 10000 * mathCostObj / 37.8087)

# Model declaration end.