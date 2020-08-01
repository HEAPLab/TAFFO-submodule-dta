


#Stuff for @A = common dso_local global [16 x [22 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
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



#Stuff for @B = common dso_local global [22 x [18 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
B_fixbits = solver.IntVar(0, 31, 'B_fixbits')
B_fixp = solver.IntVar(0, 1, 'B_fixp')
B_float = solver.IntVar(0, 1, 'B_float')
B_double = solver.IntVar(0, 1, 'B_double')
B_enob = solver.IntVar(-10000, 10000, 'B_enob')
solver.Add( + (1)*B_enob + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_fixbits + (-10000)*B_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*B_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*B_enob
solver.Add( + (1)*B_fixp + (1)*B_float + (1)*B_double==1)    #Exactly one selected type
solver.Add( + (1)*B_fixbits + (-10000)*B_fixp<=0)    #If not fix, frac part to zero



#Stuff for @C = common dso_local global [18 x [24 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
C_fixbits = solver.IntVar(0, 31, 'C_fixbits')
C_fixp = solver.IntVar(0, 1, 'C_fixp')
C_float = solver.IntVar(0, 1, 'C_float')
C_double = solver.IntVar(0, 1, 'C_double')
C_enob = solver.IntVar(-10000, 10000, 'C_enob')
solver.Add( + (1)*C_enob + (-1)*C_fixbits + (10000)*C_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*C_enob + (10000)*C_float<=10149)    #Enob constraint for float
solver.Add( + (1)*C_enob + (10000)*C_double<=11074)    #Enob constraint for double
solver.Add( + (1)*C_fixbits + (-10000)*C_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*C_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*C_enob
solver.Add( + (1)*C_fixp + (1)*C_float + (1)*C_double==1)    #Exactly one selected type
solver.Add( + (1)*C_fixbits + (-10000)*C_fixp<=0)    #If not fix, frac part to zero



#Stuff for @D = common dso_local global [16 x [24 x double]] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
D_fixbits = solver.IntVar(0, 16, 'D_fixbits')
D_fixp = solver.IntVar(0, 1, 'D_fixp')
D_float = solver.IntVar(0, 1, 'D_float')
D_double = solver.IntVar(0, 1, 'D_double')
D_enob = solver.IntVar(-10000, 10000, 'D_enob')
solver.Add( + (1)*D_enob + (-1)*D_fixbits + (10000)*D_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*D_enob + (10000)*D_float<=10149)    #Enob constraint for float
solver.Add( + (1)*D_enob + (10000)*D_double<=11074)    #Enob constraint for double
solver.Add( + (1)*D_fixbits + (-10000)*D_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*D_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*D_enob
solver.Add( + (1)*D_fixp + (1)*D_float + (1)*D_double==1)    #Exactly one selected type
solver.Add( + (1)*D_fixbits + (-10000)*D_fixp<=0)    #If not fix, frac part to zero



#Stuff for @tmp = common dso_local global [16 x [18 x double]] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
tmp_fixbits = solver.IntVar(0, 16, 'tmp_fixbits')
tmp_fixp = solver.IntVar(0, 1, 'tmp_fixp')
tmp_float = solver.IntVar(0, 1, 'tmp_float')
tmp_double = solver.IntVar(0, 1, 'tmp_double')
tmp_enob = solver.IntVar(-10000, 10000, 'tmp_enob')
solver.Add( + (1)*tmp_enob + (-1)*tmp_fixbits + (10000)*tmp_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*tmp_enob + (10000)*tmp_float<=10149)    #Enob constraint for float
solver.Add( + (1)*tmp_enob + (10000)*tmp_double<=11074)    #Enob constraint for double
solver.Add( + (1)*tmp_fixbits + (-10000)*tmp_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*tmp_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*tmp_enob
solver.Add( + (1)*tmp_fixp + (1)*tmp_float + (1)*tmp_double==1)    #Exactly one selected type
solver.Add( + (1)*tmp_fixbits + (-10000)*tmp_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %rem to double, !taffo.info !31, !taffo.initweight !34
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



#Stuff for   %conv8 = sitofp i32 16 to double, !taffo.info !35
main_conv8_fixbits = solver.IntVar(0, 27, 'main_conv8_fixbits')
main_conv8_fixp = solver.IntVar(0, 1, 'main_conv8_fixp')
main_conv8_float = solver.IntVar(0, 1, 'main_conv8_float')
main_conv8_double = solver.IntVar(0, 1, 'main_conv8_double')
main_conv8_enob = solver.IntVar(-10000, 10000, 'main_conv8_enob')
solver.Add( + (1)*main_conv8_enob + (-1)*main_conv8_fixbits + (10000)*main_conv8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv8_enob + (10000)*main_conv8_float<=10019)    #Enob constraint for float
solver.Add( + (1)*main_conv8_enob + (10000)*main_conv8_double<=10048)    #Enob constraint for double
solver.Add( + (1)*main_conv8_fixbits + (-10000)*main_conv8_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv8_enob
solver.Add( + (1)*main_conv8_fixp + (1)*main_conv8_float + (1)*main_conv8_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv8_fixbits + (-10000)*main_conv8_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv8_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div = fdiv double %conv, %conv8, !taffo.info !37, !taffo.initweight !38
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



#Constraint for cast for   %div = fdiv double %conv, %conv8, !taffo.info !37, !taffo.initweight !38
main_conv8_CAST_div_fixbits = solver.IntVar(0, 27, 'main_conv8_CAST_div_fixbits')
main_conv8_CAST_div_fixp = solver.IntVar(0, 1, 'main_conv8_CAST_div_fixp')
main_conv8_CAST_div_float = solver.IntVar(0, 1, 'main_conv8_CAST_div_float')
main_conv8_CAST_div_double = solver.IntVar(0, 1, 'main_conv8_CAST_div_double')
solver.Add( + (1)*main_conv8_CAST_div_fixp + (1)*main_conv8_CAST_div_float + (1)*main_conv8_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv8_CAST_div_fixbits + (-10000)*main_conv8_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv8_CAST_div = solver.IntVar(0, 1, 'C1_main_conv8_CAST_div')
C2_main_conv8_CAST_div = solver.IntVar(0, 1, 'C2_main_conv8_CAST_div')
solver.Add( + (1)*main_conv8_fixbits + (-1)*main_conv8_CAST_div_fixbits + (-10000)*C1_main_conv8_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv8_fixbits + (1)*main_conv8_CAST_div_fixbits + (-10000)*C2_main_conv8_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv8_CAST_div
castCostObj +=  + (1)*C2_main_conv8_CAST_div
C3_main_conv8_CAST_div = solver.IntVar(0, 1, 'C3_main_conv8_CAST_div')
C4_main_conv8_CAST_div = solver.IntVar(0, 1, 'C4_main_conv8_CAST_div')
C5_main_conv8_CAST_div = solver.IntVar(0, 1, 'C5_main_conv8_CAST_div')
C6_main_conv8_CAST_div = solver.IntVar(0, 1, 'C6_main_conv8_CAST_div')
C7_main_conv8_CAST_div = solver.IntVar(0, 1, 'C7_main_conv8_CAST_div')
C8_main_conv8_CAST_div = solver.IntVar(0, 1, 'C8_main_conv8_CAST_div')
solver.Add( + (1)*main_conv8_fixp + (1)*main_conv8_CAST_div_float + (-1)*C3_main_conv8_CAST_div<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv8_CAST_div
solver.Add( + (1)*main_conv8_float + (1)*main_conv8_CAST_div_fixp + (-1)*C4_main_conv8_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv8_CAST_div
solver.Add( + (1)*main_conv8_fixp + (1)*main_conv8_CAST_div_double + (-1)*C5_main_conv8_CAST_div<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv8_CAST_div
solver.Add( + (1)*main_conv8_double + (1)*main_conv8_CAST_div_fixp + (-1)*C6_main_conv8_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv8_CAST_div
solver.Add( + (1)*main_conv8_float + (1)*main_conv8_CAST_div_double + (-1)*C7_main_conv8_CAST_div<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv8_CAST_div
solver.Add( + (1)*main_conv8_double + (1)*main_conv8_CAST_div_float + (-1)*C8_main_conv8_CAST_div<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv8_CAST_div



#Stuff for   %div = fdiv double %conv, %conv8, !taffo.info !37, !taffo.initweight !38
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
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_conv8_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_conv8_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_conv8_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj =  + (5.29598)*main_div_fixp
mathCostObj +=  + (5.60026)*main_div_float
mathCostObj +=  + (18.3266)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*main_conv8_enob + (-10000)*main_main_div_enob_1<=1032)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_conv_enob + (-10000)*main_main_div_enob_2<=4)    #Enob: propagation in division 2



#Constraint for cast for   store double %div, double* %arrayidx10, align 8, !taffo.info !40, !taffo.initweight !24
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



#Stuff for   %conv25 = sitofp i32 %rem24 to double, !taffo.info !41, !taffo.initweight !33
main_conv25_fixbits = solver.IntVar(0, 27, 'main_conv25_fixbits')
main_conv25_fixp = solver.IntVar(0, 1, 'main_conv25_fixp')
main_conv25_float = solver.IntVar(0, 1, 'main_conv25_float')
main_conv25_double = solver.IntVar(0, 1, 'main_conv25_double')
main_conv25_enob = solver.IntVar(-10000, 10000, 'main_conv25_enob')
solver.Add( + (1)*main_conv25_enob + (-1)*main_conv25_fixbits + (10000)*main_conv25_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv25_enob + (10000)*main_conv25_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv25_enob + (10000)*main_conv25_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv25_fixbits + (-10000)*main_conv25_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv25_enob
solver.Add( + (1)*main_conv25_fixp + (1)*main_conv25_float + (1)*main_conv25_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv25_fixbits + (-10000)*main_conv25_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv25_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv26 = sitofp i32 18 to double, !taffo.info !43
main_conv26_fixbits = solver.IntVar(0, 27, 'main_conv26_fixbits')
main_conv26_fixp = solver.IntVar(0, 1, 'main_conv26_fixp')
main_conv26_float = solver.IntVar(0, 1, 'main_conv26_float')
main_conv26_double = solver.IntVar(0, 1, 'main_conv26_double')
main_conv26_enob = solver.IntVar(-10000, 10000, 'main_conv26_enob')
solver.Add( + (1)*main_conv26_enob + (-1)*main_conv26_fixbits + (10000)*main_conv26_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv26_enob + (10000)*main_conv26_float<=10019)    #Enob constraint for float
solver.Add( + (1)*main_conv26_enob + (10000)*main_conv26_double<=10048)    #Enob constraint for double
solver.Add( + (1)*main_conv26_fixbits + (-10000)*main_conv26_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv26_enob
solver.Add( + (1)*main_conv26_fixp + (1)*main_conv26_float + (1)*main_conv26_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv26_fixbits + (-10000)*main_conv26_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv26_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div27 = fdiv double %conv25, %conv26, !taffo.info !37, !taffo.initweight !34
main_conv25_CAST_div27_fixbits = solver.IntVar(0, 27, 'main_conv25_CAST_div27_fixbits')
main_conv25_CAST_div27_fixp = solver.IntVar(0, 1, 'main_conv25_CAST_div27_fixp')
main_conv25_CAST_div27_float = solver.IntVar(0, 1, 'main_conv25_CAST_div27_float')
main_conv25_CAST_div27_double = solver.IntVar(0, 1, 'main_conv25_CAST_div27_double')
solver.Add( + (1)*main_conv25_CAST_div27_fixp + (1)*main_conv25_CAST_div27_float + (1)*main_conv25_CAST_div27_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv25_CAST_div27_fixbits + (-10000)*main_conv25_CAST_div27_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C1_main_conv25_CAST_div27')
C2_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C2_main_conv25_CAST_div27')
solver.Add( + (1)*main_conv25_fixbits + (-1)*main_conv25_CAST_div27_fixbits + (-10000)*C1_main_conv25_CAST_div27<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv25_fixbits + (1)*main_conv25_CAST_div27_fixbits + (-10000)*C2_main_conv25_CAST_div27<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv25_CAST_div27
castCostObj +=  + (1)*C2_main_conv25_CAST_div27
C3_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C3_main_conv25_CAST_div27')
C4_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C4_main_conv25_CAST_div27')
C5_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C5_main_conv25_CAST_div27')
C6_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C6_main_conv25_CAST_div27')
C7_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C7_main_conv25_CAST_div27')
C8_main_conv25_CAST_div27 = solver.IntVar(0, 1, 'C8_main_conv25_CAST_div27')
solver.Add( + (1)*main_conv25_fixp + (1)*main_conv25_CAST_div27_float + (-1)*C3_main_conv25_CAST_div27<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv25_CAST_div27
solver.Add( + (1)*main_conv25_float + (1)*main_conv25_CAST_div27_fixp + (-1)*C4_main_conv25_CAST_div27<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv25_CAST_div27
solver.Add( + (1)*main_conv25_fixp + (1)*main_conv25_CAST_div27_double + (-1)*C5_main_conv25_CAST_div27<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv25_CAST_div27
solver.Add( + (1)*main_conv25_double + (1)*main_conv25_CAST_div27_fixp + (-1)*C6_main_conv25_CAST_div27<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv25_CAST_div27
solver.Add( + (1)*main_conv25_float + (1)*main_conv25_CAST_div27_double + (-1)*C7_main_conv25_CAST_div27<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv25_CAST_div27
solver.Add( + (1)*main_conv25_double + (1)*main_conv25_CAST_div27_float + (-1)*C8_main_conv25_CAST_div27<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv25_CAST_div27



#Constraint for cast for   %div27 = fdiv double %conv25, %conv26, !taffo.info !37, !taffo.initweight !34
main_conv26_CAST_div27_fixbits = solver.IntVar(0, 27, 'main_conv26_CAST_div27_fixbits')
main_conv26_CAST_div27_fixp = solver.IntVar(0, 1, 'main_conv26_CAST_div27_fixp')
main_conv26_CAST_div27_float = solver.IntVar(0, 1, 'main_conv26_CAST_div27_float')
main_conv26_CAST_div27_double = solver.IntVar(0, 1, 'main_conv26_CAST_div27_double')
solver.Add( + (1)*main_conv26_CAST_div27_fixp + (1)*main_conv26_CAST_div27_float + (1)*main_conv26_CAST_div27_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv26_CAST_div27_fixbits + (-10000)*main_conv26_CAST_div27_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C1_main_conv26_CAST_div27')
C2_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C2_main_conv26_CAST_div27')
solver.Add( + (1)*main_conv26_fixbits + (-1)*main_conv26_CAST_div27_fixbits + (-10000)*C1_main_conv26_CAST_div27<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv26_fixbits + (1)*main_conv26_CAST_div27_fixbits + (-10000)*C2_main_conv26_CAST_div27<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv26_CAST_div27
castCostObj +=  + (1)*C2_main_conv26_CAST_div27
C3_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C3_main_conv26_CAST_div27')
C4_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C4_main_conv26_CAST_div27')
C5_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C5_main_conv26_CAST_div27')
C6_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C6_main_conv26_CAST_div27')
C7_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C7_main_conv26_CAST_div27')
C8_main_conv26_CAST_div27 = solver.IntVar(0, 1, 'C8_main_conv26_CAST_div27')
solver.Add( + (1)*main_conv26_fixp + (1)*main_conv26_CAST_div27_float + (-1)*C3_main_conv26_CAST_div27<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv26_CAST_div27
solver.Add( + (1)*main_conv26_float + (1)*main_conv26_CAST_div27_fixp + (-1)*C4_main_conv26_CAST_div27<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv26_CAST_div27
solver.Add( + (1)*main_conv26_fixp + (1)*main_conv26_CAST_div27_double + (-1)*C5_main_conv26_CAST_div27<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv26_CAST_div27
solver.Add( + (1)*main_conv26_double + (1)*main_conv26_CAST_div27_fixp + (-1)*C6_main_conv26_CAST_div27<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv26_CAST_div27
solver.Add( + (1)*main_conv26_float + (1)*main_conv26_CAST_div27_double + (-1)*C7_main_conv26_CAST_div27<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv26_CAST_div27
solver.Add( + (1)*main_conv26_double + (1)*main_conv26_CAST_div27_float + (-1)*C8_main_conv26_CAST_div27<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv26_CAST_div27



#Stuff for   %div27 = fdiv double %conv25, %conv26, !taffo.info !37, !taffo.initweight !34
main_div27_fixbits = solver.IntVar(0, 31, 'main_div27_fixbits')
main_div27_fixp = solver.IntVar(0, 1, 'main_div27_fixp')
main_div27_float = solver.IntVar(0, 1, 'main_div27_float')
main_div27_double = solver.IntVar(0, 1, 'main_div27_double')
main_div27_enob = solver.IntVar(-10000, 10000, 'main_div27_enob')
solver.Add( + (1)*main_div27_enob + (-1)*main_div27_fixbits + (10000)*main_div27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div27_enob + (10000)*main_div27_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div27_enob + (10000)*main_div27_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div27_fixbits + (-10000)*main_div27_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*main_div27_enob
solver.Add( + (1)*main_div27_fixp + (1)*main_div27_float + (1)*main_div27_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div27_fixbits + (-10000)*main_div27_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv25_CAST_div27_fixp + (-1)*main_conv26_CAST_div27_fixp==0)    #fix equality
solver.Add( + (1)*main_conv25_CAST_div27_float + (-1)*main_conv26_CAST_div27_float==0)    #float equality
solver.Add( + (1)*main_conv25_CAST_div27_double + (-1)*main_conv26_CAST_div27_double==0)    #double equality
solver.Add( + (1)*main_conv25_CAST_div27_fixp + (-1)*main_div27_fixp==0)    #fix equality
solver.Add( + (1)*main_conv25_CAST_div27_float + (-1)*main_div27_float==0)    #float equality
solver.Add( + (1)*main_conv25_CAST_div27_double + (-1)*main_div27_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div27_fixp
mathCostObj +=  + (5.60026)*main_div27_float
mathCostObj +=  + (18.3266)*main_div27_double
main_main_div27_enob_1 = solver.IntVar(0, 1, 'main_main_div27_enob_1')
main_main_div27_enob_2 = solver.IntVar(0, 1, 'main_main_div27_enob_2')
solver.Add( + (1)*main_main_div27_enob_1 + (1)*main_main_div27_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div27_enob + (-1)*main_conv26_enob + (-10000)*main_main_div27_enob_1<=1032)    #Enob: propagation in division 1
solver.Add( + (1)*main_div27_enob + (-1)*main_conv25_enob + (-10000)*main_main_div27_enob_2<=4)    #Enob: propagation in division 2



#Constraint for cast for   store double %div27, double* %arrayidx31, align 8, !taffo.info !40, !taffo.initweight !24
main_div27_CAST_store_fixbits = solver.IntVar(0, 31, 'main_div27_CAST_store_fixbits')
main_div27_CAST_store_fixp = solver.IntVar(0, 1, 'main_div27_CAST_store_fixp')
main_div27_CAST_store_float = solver.IntVar(0, 1, 'main_div27_CAST_store_float')
main_div27_CAST_store_double = solver.IntVar(0, 1, 'main_div27_CAST_store_double')
solver.Add( + (1)*main_div27_CAST_store_fixp + (1)*main_div27_CAST_store_float + (1)*main_div27_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div27_CAST_store_fixbits + (-10000)*main_div27_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div27_CAST_store = solver.IntVar(0, 1, 'C1_main_div27_CAST_store')
C2_main_div27_CAST_store = solver.IntVar(0, 1, 'C2_main_div27_CAST_store')
solver.Add( + (1)*main_div27_fixbits + (-1)*main_div27_CAST_store_fixbits + (-10000)*C1_main_div27_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div27_fixbits + (1)*main_div27_CAST_store_fixbits + (-10000)*C2_main_div27_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div27_CAST_store
castCostObj +=  + (1)*C2_main_div27_CAST_store
C3_main_div27_CAST_store = solver.IntVar(0, 1, 'C3_main_div27_CAST_store')
C4_main_div27_CAST_store = solver.IntVar(0, 1, 'C4_main_div27_CAST_store')
C5_main_div27_CAST_store = solver.IntVar(0, 1, 'C5_main_div27_CAST_store')
C6_main_div27_CAST_store = solver.IntVar(0, 1, 'C6_main_div27_CAST_store')
C7_main_div27_CAST_store = solver.IntVar(0, 1, 'C7_main_div27_CAST_store')
C8_main_div27_CAST_store = solver.IntVar(0, 1, 'C8_main_div27_CAST_store')
solver.Add( + (1)*main_div27_fixp + (1)*main_div27_CAST_store_float + (-1)*C3_main_div27_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div27_CAST_store
solver.Add( + (1)*main_div27_float + (1)*main_div27_CAST_store_fixp + (-1)*C4_main_div27_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div27_CAST_store
solver.Add( + (1)*main_div27_fixp + (1)*main_div27_CAST_store_double + (-1)*C5_main_div27_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div27_CAST_store
solver.Add( + (1)*main_div27_double + (1)*main_div27_CAST_store_fixp + (-1)*C6_main_div27_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div27_CAST_store
solver.Add( + (1)*main_div27_float + (1)*main_div27_CAST_store_double + (-1)*C7_main_div27_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div27_CAST_store
solver.Add( + (1)*main_div27_double + (1)*main_div27_CAST_store_float + (-1)*C8_main_div27_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div27_CAST_store
solver.Add( + (1)*B_fixp + (-1)*main_div27_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B_float + (-1)*main_div27_CAST_store_float==0)    #float equality
solver.Add( + (1)*B_double + (-1)*main_div27_CAST_store_double==0)    #double equality
solver.Add( + (1)*B_fixbits + (-1)*main_div27_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
B_enob_storeENOB = solver.IntVar(-10000, 10000, 'B_enob_storeENOB')
solver.Add( + (1)*B_enob_storeENOB + (-1)*B_fixbits + (10000)*B_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B_enob_storeENOB + (10000)*B_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B_enob_storeENOB + (10000)*B_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B_enob_storeENOB + (-1)*main_div27_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv50 = sitofp i32 %rem49 to double, !taffo.info !45, !taffo.initweight !34
main_conv50_fixbits = solver.IntVar(0, 27, 'main_conv50_fixbits')
main_conv50_fixp = solver.IntVar(0, 1, 'main_conv50_fixp')
main_conv50_float = solver.IntVar(0, 1, 'main_conv50_float')
main_conv50_double = solver.IntVar(0, 1, 'main_conv50_double')
main_conv50_enob = solver.IntVar(-10000, 10000, 'main_conv50_enob')
solver.Add( + (1)*main_conv50_enob + (-1)*main_conv50_fixbits + (10000)*main_conv50_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv50_enob + (10000)*main_conv50_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv50_enob + (10000)*main_conv50_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv50_fixbits + (-10000)*main_conv50_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv50_enob
solver.Add( + (1)*main_conv50_fixp + (1)*main_conv50_float + (1)*main_conv50_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv50_fixbits + (-10000)*main_conv50_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv50_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv51 = sitofp i32 24 to double, !taffo.info !47
main_conv51_fixbits = solver.IntVar(0, 27, 'main_conv51_fixbits')
main_conv51_fixp = solver.IntVar(0, 1, 'main_conv51_fixp')
main_conv51_float = solver.IntVar(0, 1, 'main_conv51_float')
main_conv51_double = solver.IntVar(0, 1, 'main_conv51_double')
main_conv51_enob = solver.IntVar(-10000, 10000, 'main_conv51_enob')
solver.Add( + (1)*main_conv51_enob + (-1)*main_conv51_fixbits + (10000)*main_conv51_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv51_enob + (10000)*main_conv51_float<=10019)    #Enob constraint for float
solver.Add( + (1)*main_conv51_enob + (10000)*main_conv51_double<=10048)    #Enob constraint for double
solver.Add( + (1)*main_conv51_fixbits + (-10000)*main_conv51_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv51_enob
solver.Add( + (1)*main_conv51_fixp + (1)*main_conv51_float + (1)*main_conv51_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv51_fixbits + (-10000)*main_conv51_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv51_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div52 = fdiv double %conv50, %conv51, !taffo.info !37, !taffo.initweight !38
main_conv50_CAST_div52_fixbits = solver.IntVar(0, 27, 'main_conv50_CAST_div52_fixbits')
main_conv50_CAST_div52_fixp = solver.IntVar(0, 1, 'main_conv50_CAST_div52_fixp')
main_conv50_CAST_div52_float = solver.IntVar(0, 1, 'main_conv50_CAST_div52_float')
main_conv50_CAST_div52_double = solver.IntVar(0, 1, 'main_conv50_CAST_div52_double')
solver.Add( + (1)*main_conv50_CAST_div52_fixp + (1)*main_conv50_CAST_div52_float + (1)*main_conv50_CAST_div52_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv50_CAST_div52_fixbits + (-10000)*main_conv50_CAST_div52_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C1_main_conv50_CAST_div52')
C2_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C2_main_conv50_CAST_div52')
solver.Add( + (1)*main_conv50_fixbits + (-1)*main_conv50_CAST_div52_fixbits + (-10000)*C1_main_conv50_CAST_div52<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv50_fixbits + (1)*main_conv50_CAST_div52_fixbits + (-10000)*C2_main_conv50_CAST_div52<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv50_CAST_div52
castCostObj +=  + (1)*C2_main_conv50_CAST_div52
C3_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C3_main_conv50_CAST_div52')
C4_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C4_main_conv50_CAST_div52')
C5_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C5_main_conv50_CAST_div52')
C6_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C6_main_conv50_CAST_div52')
C7_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C7_main_conv50_CAST_div52')
C8_main_conv50_CAST_div52 = solver.IntVar(0, 1, 'C8_main_conv50_CAST_div52')
solver.Add( + (1)*main_conv50_fixp + (1)*main_conv50_CAST_div52_float + (-1)*C3_main_conv50_CAST_div52<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv50_CAST_div52
solver.Add( + (1)*main_conv50_float + (1)*main_conv50_CAST_div52_fixp + (-1)*C4_main_conv50_CAST_div52<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv50_CAST_div52
solver.Add( + (1)*main_conv50_fixp + (1)*main_conv50_CAST_div52_double + (-1)*C5_main_conv50_CAST_div52<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv50_CAST_div52
solver.Add( + (1)*main_conv50_double + (1)*main_conv50_CAST_div52_fixp + (-1)*C6_main_conv50_CAST_div52<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv50_CAST_div52
solver.Add( + (1)*main_conv50_float + (1)*main_conv50_CAST_div52_double + (-1)*C7_main_conv50_CAST_div52<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv50_CAST_div52
solver.Add( + (1)*main_conv50_double + (1)*main_conv50_CAST_div52_float + (-1)*C8_main_conv50_CAST_div52<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv50_CAST_div52



#Constraint for cast for   %div52 = fdiv double %conv50, %conv51, !taffo.info !37, !taffo.initweight !38
main_conv51_CAST_div52_fixbits = solver.IntVar(0, 27, 'main_conv51_CAST_div52_fixbits')
main_conv51_CAST_div52_fixp = solver.IntVar(0, 1, 'main_conv51_CAST_div52_fixp')
main_conv51_CAST_div52_float = solver.IntVar(0, 1, 'main_conv51_CAST_div52_float')
main_conv51_CAST_div52_double = solver.IntVar(0, 1, 'main_conv51_CAST_div52_double')
solver.Add( + (1)*main_conv51_CAST_div52_fixp + (1)*main_conv51_CAST_div52_float + (1)*main_conv51_CAST_div52_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv51_CAST_div52_fixbits + (-10000)*main_conv51_CAST_div52_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C1_main_conv51_CAST_div52')
C2_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C2_main_conv51_CAST_div52')
solver.Add( + (1)*main_conv51_fixbits + (-1)*main_conv51_CAST_div52_fixbits + (-10000)*C1_main_conv51_CAST_div52<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv51_fixbits + (1)*main_conv51_CAST_div52_fixbits + (-10000)*C2_main_conv51_CAST_div52<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv51_CAST_div52
castCostObj +=  + (1)*C2_main_conv51_CAST_div52
C3_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C3_main_conv51_CAST_div52')
C4_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C4_main_conv51_CAST_div52')
C5_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C5_main_conv51_CAST_div52')
C6_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C6_main_conv51_CAST_div52')
C7_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C7_main_conv51_CAST_div52')
C8_main_conv51_CAST_div52 = solver.IntVar(0, 1, 'C8_main_conv51_CAST_div52')
solver.Add( + (1)*main_conv51_fixp + (1)*main_conv51_CAST_div52_float + (-1)*C3_main_conv51_CAST_div52<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv51_CAST_div52
solver.Add( + (1)*main_conv51_float + (1)*main_conv51_CAST_div52_fixp + (-1)*C4_main_conv51_CAST_div52<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv51_CAST_div52
solver.Add( + (1)*main_conv51_fixp + (1)*main_conv51_CAST_div52_double + (-1)*C5_main_conv51_CAST_div52<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv51_CAST_div52
solver.Add( + (1)*main_conv51_double + (1)*main_conv51_CAST_div52_fixp + (-1)*C6_main_conv51_CAST_div52<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv51_CAST_div52
solver.Add( + (1)*main_conv51_float + (1)*main_conv51_CAST_div52_double + (-1)*C7_main_conv51_CAST_div52<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv51_CAST_div52
solver.Add( + (1)*main_conv51_double + (1)*main_conv51_CAST_div52_float + (-1)*C8_main_conv51_CAST_div52<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv51_CAST_div52



#Stuff for   %div52 = fdiv double %conv50, %conv51, !taffo.info !37, !taffo.initweight !38
main_div52_fixbits = solver.IntVar(0, 31, 'main_div52_fixbits')
main_div52_fixp = solver.IntVar(0, 1, 'main_div52_fixp')
main_div52_float = solver.IntVar(0, 1, 'main_div52_float')
main_div52_double = solver.IntVar(0, 1, 'main_div52_double')
main_div52_enob = solver.IntVar(-10000, 10000, 'main_div52_enob')
solver.Add( + (1)*main_div52_enob + (-1)*main_div52_fixbits + (10000)*main_div52_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div52_enob + (10000)*main_div52_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div52_enob + (10000)*main_div52_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div52_fixbits + (-10000)*main_div52_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*main_div52_enob
solver.Add( + (1)*main_div52_fixp + (1)*main_div52_float + (1)*main_div52_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div52_fixbits + (-10000)*main_div52_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv50_CAST_div52_fixp + (-1)*main_conv51_CAST_div52_fixp==0)    #fix equality
solver.Add( + (1)*main_conv50_CAST_div52_float + (-1)*main_conv51_CAST_div52_float==0)    #float equality
solver.Add( + (1)*main_conv50_CAST_div52_double + (-1)*main_conv51_CAST_div52_double==0)    #double equality
solver.Add( + (1)*main_conv50_CAST_div52_fixp + (-1)*main_div52_fixp==0)    #fix equality
solver.Add( + (1)*main_conv50_CAST_div52_float + (-1)*main_div52_float==0)    #float equality
solver.Add( + (1)*main_conv50_CAST_div52_double + (-1)*main_div52_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div52_fixp
mathCostObj +=  + (5.60026)*main_div52_float
mathCostObj +=  + (18.3266)*main_div52_double
main_main_div52_enob_1 = solver.IntVar(0, 1, 'main_main_div52_enob_1')
main_main_div52_enob_2 = solver.IntVar(0, 1, 'main_main_div52_enob_2')
solver.Add( + (1)*main_main_div52_enob_1 + (1)*main_main_div52_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div52_enob + (-1)*main_conv51_enob + (-10000)*main_main_div52_enob_1<=1034)    #Enob: propagation in division 1
solver.Add( + (1)*main_div52_enob + (-1)*main_conv50_enob + (-10000)*main_main_div52_enob_2<=5)    #Enob: propagation in division 2



#Constraint for cast for   store double %div52, double* %arrayidx56, align 8, !taffo.info !40, !taffo.initweight !24
main_div52_CAST_store_fixbits = solver.IntVar(0, 31, 'main_div52_CAST_store_fixbits')
main_div52_CAST_store_fixp = solver.IntVar(0, 1, 'main_div52_CAST_store_fixp')
main_div52_CAST_store_float = solver.IntVar(0, 1, 'main_div52_CAST_store_float')
main_div52_CAST_store_double = solver.IntVar(0, 1, 'main_div52_CAST_store_double')
solver.Add( + (1)*main_div52_CAST_store_fixp + (1)*main_div52_CAST_store_float + (1)*main_div52_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div52_CAST_store_fixbits + (-10000)*main_div52_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div52_CAST_store = solver.IntVar(0, 1, 'C1_main_div52_CAST_store')
C2_main_div52_CAST_store = solver.IntVar(0, 1, 'C2_main_div52_CAST_store')
solver.Add( + (1)*main_div52_fixbits + (-1)*main_div52_CAST_store_fixbits + (-10000)*C1_main_div52_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div52_fixbits + (1)*main_div52_CAST_store_fixbits + (-10000)*C2_main_div52_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div52_CAST_store
castCostObj +=  + (1)*C2_main_div52_CAST_store
C3_main_div52_CAST_store = solver.IntVar(0, 1, 'C3_main_div52_CAST_store')
C4_main_div52_CAST_store = solver.IntVar(0, 1, 'C4_main_div52_CAST_store')
C5_main_div52_CAST_store = solver.IntVar(0, 1, 'C5_main_div52_CAST_store')
C6_main_div52_CAST_store = solver.IntVar(0, 1, 'C6_main_div52_CAST_store')
C7_main_div52_CAST_store = solver.IntVar(0, 1, 'C7_main_div52_CAST_store')
C8_main_div52_CAST_store = solver.IntVar(0, 1, 'C8_main_div52_CAST_store')
solver.Add( + (1)*main_div52_fixp + (1)*main_div52_CAST_store_float + (-1)*C3_main_div52_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div52_CAST_store
solver.Add( + (1)*main_div52_float + (1)*main_div52_CAST_store_fixp + (-1)*C4_main_div52_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div52_CAST_store
solver.Add( + (1)*main_div52_fixp + (1)*main_div52_CAST_store_double + (-1)*C5_main_div52_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div52_CAST_store
solver.Add( + (1)*main_div52_double + (1)*main_div52_CAST_store_fixp + (-1)*C6_main_div52_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div52_CAST_store
solver.Add( + (1)*main_div52_float + (1)*main_div52_CAST_store_double + (-1)*C7_main_div52_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div52_CAST_store
solver.Add( + (1)*main_div52_double + (1)*main_div52_CAST_store_float + (-1)*C8_main_div52_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div52_CAST_store
solver.Add( + (1)*C_fixp + (-1)*main_div52_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*C_float + (-1)*main_div52_CAST_store_float==0)    #float equality
solver.Add( + (1)*C_double + (-1)*main_div52_CAST_store_double==0)    #double equality
solver.Add( + (1)*C_fixbits + (-1)*main_div52_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
C_enob_storeENOB = solver.IntVar(-10000, 10000, 'C_enob_storeENOB')
solver.Add( + (1)*C_enob_storeENOB + (-1)*C_fixbits + (10000)*C_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*C_enob_storeENOB + (10000)*C_float<=10149)    #Enob constraint for float
solver.Add( + (1)*C_enob_storeENOB + (10000)*C_double<=11074)    #Enob constraint for double
solver.Add( + (1)*C_enob_storeENOB + (-1)*main_div52_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %conv74 = sitofp i32 %rem73 to double, !taffo.info !49, !taffo.initweight !33
main_conv74_fixbits = solver.IntVar(0, 27, 'main_conv74_fixbits')
main_conv74_fixp = solver.IntVar(0, 1, 'main_conv74_fixp')
main_conv74_float = solver.IntVar(0, 1, 'main_conv74_float')
main_conv74_double = solver.IntVar(0, 1, 'main_conv74_double')
main_conv74_enob = solver.IntVar(-10000, 10000, 'main_conv74_enob')
solver.Add( + (1)*main_conv74_enob + (-1)*main_conv74_fixbits + (10000)*main_conv74_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv74_enob + (10000)*main_conv74_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv74_enob + (10000)*main_conv74_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv74_fixbits + (-10000)*main_conv74_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv74_enob
solver.Add( + (1)*main_conv74_fixp + (1)*main_conv74_float + (1)*main_conv74_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv74_fixbits + (-10000)*main_conv74_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv74_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for   %conv75 = sitofp i32 22 to double, !taffo.info !51
main_conv75_fixbits = solver.IntVar(0, 27, 'main_conv75_fixbits')
main_conv75_fixp = solver.IntVar(0, 1, 'main_conv75_fixp')
main_conv75_float = solver.IntVar(0, 1, 'main_conv75_float')
main_conv75_double = solver.IntVar(0, 1, 'main_conv75_double')
main_conv75_enob = solver.IntVar(-10000, 10000, 'main_conv75_enob')
solver.Add( + (1)*main_conv75_enob + (-1)*main_conv75_fixbits + (10000)*main_conv75_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv75_enob + (10000)*main_conv75_float<=10019)    #Enob constraint for float
solver.Add( + (1)*main_conv75_enob + (10000)*main_conv75_double<=10048)    #Enob constraint for double
solver.Add( + (1)*main_conv75_fixbits + (-10000)*main_conv75_fixp>=-9974)    #Limit the lower number of frac bits27
enobCostObj +=  + (-1)*main_conv75_enob
solver.Add( + (1)*main_conv75_fixp + (1)*main_conv75_float + (1)*main_conv75_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv75_fixbits + (-10000)*main_conv75_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv75_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %div76 = fdiv double %conv74, %conv75, !taffo.info !37, !taffo.initweight !34
main_conv74_CAST_div76_fixbits = solver.IntVar(0, 27, 'main_conv74_CAST_div76_fixbits')
main_conv74_CAST_div76_fixp = solver.IntVar(0, 1, 'main_conv74_CAST_div76_fixp')
main_conv74_CAST_div76_float = solver.IntVar(0, 1, 'main_conv74_CAST_div76_float')
main_conv74_CAST_div76_double = solver.IntVar(0, 1, 'main_conv74_CAST_div76_double')
solver.Add( + (1)*main_conv74_CAST_div76_fixp + (1)*main_conv74_CAST_div76_float + (1)*main_conv74_CAST_div76_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv74_CAST_div76_fixbits + (-10000)*main_conv74_CAST_div76_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C1_main_conv74_CAST_div76')
C2_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C2_main_conv74_CAST_div76')
solver.Add( + (1)*main_conv74_fixbits + (-1)*main_conv74_CAST_div76_fixbits + (-10000)*C1_main_conv74_CAST_div76<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv74_fixbits + (1)*main_conv74_CAST_div76_fixbits + (-10000)*C2_main_conv74_CAST_div76<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv74_CAST_div76
castCostObj +=  + (1)*C2_main_conv74_CAST_div76
C3_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C3_main_conv74_CAST_div76')
C4_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C4_main_conv74_CAST_div76')
C5_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C5_main_conv74_CAST_div76')
C6_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C6_main_conv74_CAST_div76')
C7_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C7_main_conv74_CAST_div76')
C8_main_conv74_CAST_div76 = solver.IntVar(0, 1, 'C8_main_conv74_CAST_div76')
solver.Add( + (1)*main_conv74_fixp + (1)*main_conv74_CAST_div76_float + (-1)*C3_main_conv74_CAST_div76<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv74_CAST_div76
solver.Add( + (1)*main_conv74_float + (1)*main_conv74_CAST_div76_fixp + (-1)*C4_main_conv74_CAST_div76<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv74_CAST_div76
solver.Add( + (1)*main_conv74_fixp + (1)*main_conv74_CAST_div76_double + (-1)*C5_main_conv74_CAST_div76<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv74_CAST_div76
solver.Add( + (1)*main_conv74_double + (1)*main_conv74_CAST_div76_fixp + (-1)*C6_main_conv74_CAST_div76<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv74_CAST_div76
solver.Add( + (1)*main_conv74_float + (1)*main_conv74_CAST_div76_double + (-1)*C7_main_conv74_CAST_div76<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv74_CAST_div76
solver.Add( + (1)*main_conv74_double + (1)*main_conv74_CAST_div76_float + (-1)*C8_main_conv74_CAST_div76<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv74_CAST_div76



#Constraint for cast for   %div76 = fdiv double %conv74, %conv75, !taffo.info !37, !taffo.initweight !34
main_conv75_CAST_div76_fixbits = solver.IntVar(0, 27, 'main_conv75_CAST_div76_fixbits')
main_conv75_CAST_div76_fixp = solver.IntVar(0, 1, 'main_conv75_CAST_div76_fixp')
main_conv75_CAST_div76_float = solver.IntVar(0, 1, 'main_conv75_CAST_div76_float')
main_conv75_CAST_div76_double = solver.IntVar(0, 1, 'main_conv75_CAST_div76_double')
solver.Add( + (1)*main_conv75_CAST_div76_fixp + (1)*main_conv75_CAST_div76_float + (1)*main_conv75_CAST_div76_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv75_CAST_div76_fixbits + (-10000)*main_conv75_CAST_div76_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C1_main_conv75_CAST_div76')
C2_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C2_main_conv75_CAST_div76')
solver.Add( + (1)*main_conv75_fixbits + (-1)*main_conv75_CAST_div76_fixbits + (-10000)*C1_main_conv75_CAST_div76<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv75_fixbits + (1)*main_conv75_CAST_div76_fixbits + (-10000)*C2_main_conv75_CAST_div76<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv75_CAST_div76
castCostObj +=  + (1)*C2_main_conv75_CAST_div76
C3_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C3_main_conv75_CAST_div76')
C4_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C4_main_conv75_CAST_div76')
C5_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C5_main_conv75_CAST_div76')
C6_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C6_main_conv75_CAST_div76')
C7_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C7_main_conv75_CAST_div76')
C8_main_conv75_CAST_div76 = solver.IntVar(0, 1, 'C8_main_conv75_CAST_div76')
solver.Add( + (1)*main_conv75_fixp + (1)*main_conv75_CAST_div76_float + (-1)*C3_main_conv75_CAST_div76<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv75_CAST_div76
solver.Add( + (1)*main_conv75_float + (1)*main_conv75_CAST_div76_fixp + (-1)*C4_main_conv75_CAST_div76<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv75_CAST_div76
solver.Add( + (1)*main_conv75_fixp + (1)*main_conv75_CAST_div76_double + (-1)*C5_main_conv75_CAST_div76<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv75_CAST_div76
solver.Add( + (1)*main_conv75_double + (1)*main_conv75_CAST_div76_fixp + (-1)*C6_main_conv75_CAST_div76<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv75_CAST_div76
solver.Add( + (1)*main_conv75_float + (1)*main_conv75_CAST_div76_double + (-1)*C7_main_conv75_CAST_div76<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv75_CAST_div76
solver.Add( + (1)*main_conv75_double + (1)*main_conv75_CAST_div76_float + (-1)*C8_main_conv75_CAST_div76<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv75_CAST_div76



#Stuff for   %div76 = fdiv double %conv74, %conv75, !taffo.info !37, !taffo.initweight !34
main_div76_fixbits = solver.IntVar(0, 31, 'main_div76_fixbits')
main_div76_fixp = solver.IntVar(0, 1, 'main_div76_fixp')
main_div76_float = solver.IntVar(0, 1, 'main_div76_float')
main_div76_double = solver.IntVar(0, 1, 'main_div76_double')
main_div76_enob = solver.IntVar(-10000, 10000, 'main_div76_enob')
solver.Add( + (1)*main_div76_enob + (-1)*main_div76_fixbits + (10000)*main_div76_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div76_enob + (10000)*main_div76_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div76_enob + (10000)*main_div76_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div76_fixbits + (-10000)*main_div76_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*main_div76_enob
solver.Add( + (1)*main_div76_fixp + (1)*main_div76_float + (1)*main_div76_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div76_fixbits + (-10000)*main_div76_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv74_CAST_div76_fixp + (-1)*main_conv75_CAST_div76_fixp==0)    #fix equality
solver.Add( + (1)*main_conv74_CAST_div76_float + (-1)*main_conv75_CAST_div76_float==0)    #float equality
solver.Add( + (1)*main_conv74_CAST_div76_double + (-1)*main_conv75_CAST_div76_double==0)    #double equality
solver.Add( + (1)*main_conv74_CAST_div76_fixp + (-1)*main_div76_fixp==0)    #fix equality
solver.Add( + (1)*main_conv74_CAST_div76_float + (-1)*main_div76_float==0)    #float equality
solver.Add( + (1)*main_conv74_CAST_div76_double + (-1)*main_div76_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div76_fixp
mathCostObj +=  + (5.60026)*main_div76_float
mathCostObj +=  + (18.3266)*main_div76_double
main_main_div76_enob_1 = solver.IntVar(0, 1, 'main_main_div76_enob_1')
main_main_div76_enob_2 = solver.IntVar(0, 1, 'main_main_div76_enob_2')
solver.Add( + (1)*main_main_div76_enob_1 + (1)*main_main_div76_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div76_enob + (-1)*main_conv75_enob + (-10000)*main_main_div76_enob_1<=1032)    #Enob: propagation in division 1
solver.Add( + (1)*main_div76_enob + (-1)*main_conv74_enob + (-10000)*main_main_div76_enob_2<=4)    #Enob: propagation in division 2



#Constraint for cast for   store double %div76, double* %arrayidx80, align 8, !taffo.info !12, !taffo.initweight !24
main_div76_CAST_store_fixbits = solver.IntVar(0, 31, 'main_div76_CAST_store_fixbits')
main_div76_CAST_store_fixp = solver.IntVar(0, 1, 'main_div76_CAST_store_fixp')
main_div76_CAST_store_float = solver.IntVar(0, 1, 'main_div76_CAST_store_float')
main_div76_CAST_store_double = solver.IntVar(0, 1, 'main_div76_CAST_store_double')
solver.Add( + (1)*main_div76_CAST_store_fixp + (1)*main_div76_CAST_store_float + (1)*main_div76_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div76_CAST_store_fixbits + (-10000)*main_div76_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div76_CAST_store = solver.IntVar(0, 1, 'C1_main_div76_CAST_store')
C2_main_div76_CAST_store = solver.IntVar(0, 1, 'C2_main_div76_CAST_store')
solver.Add( + (1)*main_div76_fixbits + (-1)*main_div76_CAST_store_fixbits + (-10000)*C1_main_div76_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div76_fixbits + (1)*main_div76_CAST_store_fixbits + (-10000)*C2_main_div76_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div76_CAST_store
castCostObj +=  + (1)*C2_main_div76_CAST_store
C3_main_div76_CAST_store = solver.IntVar(0, 1, 'C3_main_div76_CAST_store')
C4_main_div76_CAST_store = solver.IntVar(0, 1, 'C4_main_div76_CAST_store')
C5_main_div76_CAST_store = solver.IntVar(0, 1, 'C5_main_div76_CAST_store')
C6_main_div76_CAST_store = solver.IntVar(0, 1, 'C6_main_div76_CAST_store')
C7_main_div76_CAST_store = solver.IntVar(0, 1, 'C7_main_div76_CAST_store')
C8_main_div76_CAST_store = solver.IntVar(0, 1, 'C8_main_div76_CAST_store')
solver.Add( + (1)*main_div76_fixp + (1)*main_div76_CAST_store_float + (-1)*C3_main_div76_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div76_CAST_store
solver.Add( + (1)*main_div76_float + (1)*main_div76_CAST_store_fixp + (-1)*C4_main_div76_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div76_CAST_store
solver.Add( + (1)*main_div76_fixp + (1)*main_div76_CAST_store_double + (-1)*C5_main_div76_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div76_CAST_store
solver.Add( + (1)*main_div76_double + (1)*main_div76_CAST_store_fixp + (-1)*C6_main_div76_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div76_CAST_store
solver.Add( + (1)*main_div76_float + (1)*main_div76_CAST_store_double + (-1)*C7_main_div76_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div76_CAST_store
solver.Add( + (1)*main_div76_double + (1)*main_div76_CAST_store_float + (-1)*C8_main_div76_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div76_CAST_store
solver.Add( + (1)*D_fixp + (-1)*main_div76_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*D_float + (-1)*main_div76_CAST_store_float==0)    #float equality
solver.Add( + (1)*D_double + (-1)*main_div76_CAST_store_double==0)    #double equality
solver.Add( + (1)*D_fixbits + (-1)*main_div76_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
D_enob_storeENOB = solver.IntVar(-10000, 10000, 'D_enob_storeENOB')
solver.Add( + (1)*D_enob_storeENOB + (-1)*D_fixbits + (10000)*D_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*D_enob_storeENOB + (10000)*D_float<=10149)    #Enob constraint for float
solver.Add( + (1)*D_enob_storeENOB + (10000)*D_double<=11074)    #Enob constraint for double
solver.Add( + (1)*D_enob_storeENOB + (-1)*main_div76_enob<=0)    #Enob constraint ENOB propagation in load/store



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
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx98, align 8, !taffo.info !12, !taffo.initweight !24, !taffo.constinfo !53
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
solver.Add( + (1)*tmp_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*tmp_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*tmp_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*tmp_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
A_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'A_enob_memphi_main_tmp')
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp_enob_1 = solver.IntVar(0, 1, 'main_main_tmp_enob_1')
solver.Add( + (1)*main_main_tmp_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*A_enob_memphi_main_tmp + (-1)*A_enob_storeENOB + (10000)*main_main_tmp_enob_1<=10000)    #Enob: forcing MEM phi enob



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



#Constraint for cast for   %mul107 = fmul double 1.500000e+00, %tmp, !taffo.info !58, !taffo.initweight !23, !taffo.constinfo !60
ConstantValue__3_CAST_mul107_fixbits = solver.IntVar(0, 30, 'ConstantValue__3_CAST_mul107_fixbits')
ConstantValue__3_CAST_mul107_fixp = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul107_fixp')
ConstantValue__3_CAST_mul107_float = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul107_float')
ConstantValue__3_CAST_mul107_double = solver.IntVar(0, 1, 'ConstantValue__3_CAST_mul107_double')
solver.Add( + (1)*ConstantValue__3_CAST_mul107_fixp + (1)*ConstantValue__3_CAST_mul107_float + (1)*ConstantValue__3_CAST_mul107_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__3_CAST_mul107_fixbits + (-10000)*ConstantValue__3_CAST_mul107_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C1_ConstantValue__3_CAST_mul107')
C2_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C2_ConstantValue__3_CAST_mul107')
solver.Add( + (1)*ConstantValue__3_fixbits + (-1)*ConstantValue__3_CAST_mul107_fixbits + (-10000)*C1_ConstantValue__3_CAST_mul107<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__3_fixbits + (1)*ConstantValue__3_CAST_mul107_fixbits + (-10000)*C2_ConstantValue__3_CAST_mul107<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__3_CAST_mul107
castCostObj +=  + (1)*C2_ConstantValue__3_CAST_mul107
C3_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C3_ConstantValue__3_CAST_mul107')
C4_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C4_ConstantValue__3_CAST_mul107')
C5_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C5_ConstantValue__3_CAST_mul107')
C6_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C6_ConstantValue__3_CAST_mul107')
C7_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C7_ConstantValue__3_CAST_mul107')
C8_ConstantValue__3_CAST_mul107 = solver.IntVar(0, 1, 'C8_ConstantValue__3_CAST_mul107')
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul107_float + (-1)*C3_ConstantValue__3_CAST_mul107<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__3_CAST_mul107
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul107_fixp + (-1)*C4_ConstantValue__3_CAST_mul107<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__3_CAST_mul107
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_CAST_mul107_double + (-1)*C5_ConstantValue__3_CAST_mul107<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__3_CAST_mul107
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul107_fixp + (-1)*C6_ConstantValue__3_CAST_mul107<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__3_CAST_mul107
solver.Add( + (1)*ConstantValue__3_float + (1)*ConstantValue__3_CAST_mul107_double + (-1)*C7_ConstantValue__3_CAST_mul107<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__3_CAST_mul107
solver.Add( + (1)*ConstantValue__3_double + (1)*ConstantValue__3_CAST_mul107_float + (-1)*C8_ConstantValue__3_CAST_mul107<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__3_CAST_mul107



#Constraint for cast for   %mul107 = fmul double 1.500000e+00, %tmp, !taffo.info !58, !taffo.initweight !23, !taffo.constinfo !60
A_CAST_mul107_fixbits = solver.IntVar(0, 31, 'A_CAST_mul107_fixbits')
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



#Stuff for   %mul107 = fmul double 1.500000e+00, %tmp, !taffo.info !58, !taffo.initweight !23, !taffo.constinfo !60
main_mul107_fixbits = solver.IntVar(0, 30, 'main_mul107_fixbits')
main_mul107_fixp = solver.IntVar(0, 1, 'main_mul107_fixp')
main_mul107_float = solver.IntVar(0, 1, 'main_mul107_float')
main_mul107_double = solver.IntVar(0, 1, 'main_mul107_double')
main_mul107_enob = solver.IntVar(-10000, 10000, 'main_mul107_enob')
solver.Add( + (1)*main_mul107_enob + (-1)*main_mul107_fixbits + (10000)*main_mul107_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul107_enob + (10000)*main_mul107_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul107_enob + (10000)*main_mul107_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul107_fixbits + (-10000)*main_mul107_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_mul107_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul107_enob
solver.Add( + (1)*main_mul107_fixp + (1)*main_mul107_float + (1)*main_mul107_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul107_fixbits + (-10000)*main_mul107_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__3_CAST_mul107_fixp + (-1)*A_CAST_mul107_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul107_float + (-1)*A_CAST_mul107_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul107_double + (-1)*A_CAST_mul107_double==0)    #double equality
solver.Add( + (1)*ConstantValue__3_CAST_mul107_fixp + (-1)*main_mul107_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__3_CAST_mul107_float + (-1)*main_mul107_float==0)    #float equality
solver.Add( + (1)*ConstantValue__3_CAST_mul107_double + (-1)*main_mul107_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul107_fixp
mathCostObj +=  + (2.64722)*main_mul107_float
mathCostObj +=  + (4.02255)*main_mul107_double
main_main_mul107_enob_1 = solver.IntVar(0, 1, 'main_main_mul107_enob_1')
main_main_mul107_enob_2 = solver.IntVar(0, 1, 'main_main_mul107_enob_2')
solver.Add( + (1)*main_main_mul107_enob_1 + (1)*main_main_mul107_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul107_enob + (-1)*A_enob_memphi_main_tmp + (-10000)*main_main_mul107_enob_1<=-1)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul107_enob + (-1)*ConstantValue__1_enob + (-10000)*main_main_mul107_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
B_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'B_enob_memphi_main_tmp1')
solver.Add( + (1)*B_enob_memphi_main_tmp1 + (-1)*B_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp1_enob_1 = solver.IntVar(0, 1, 'main_main_tmp1_enob_1')
main_main_tmp1_enob_2 = solver.IntVar(0, 1, 'main_main_tmp1_enob_2')
solver.Add( + (1)*main_main_tmp1_enob_1 + (1)*main_main_tmp1_enob_2==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp1 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*B_enob_memphi_main_tmp1 + (-1)*B_enob_storeENOB + (10000)*main_main_tmp1_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul112 = fmul double %mul107, %tmp1, !taffo.info !58, !taffo.initweight !24
main_mul107_CAST_mul112_fixbits = solver.IntVar(0, 30, 'main_mul107_CAST_mul112_fixbits')
main_mul107_CAST_mul112_fixp = solver.IntVar(0, 1, 'main_mul107_CAST_mul112_fixp')
main_mul107_CAST_mul112_float = solver.IntVar(0, 1, 'main_mul107_CAST_mul112_float')
main_mul107_CAST_mul112_double = solver.IntVar(0, 1, 'main_mul107_CAST_mul112_double')
solver.Add( + (1)*main_mul107_CAST_mul112_fixp + (1)*main_mul107_CAST_mul112_float + (1)*main_mul107_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul107_CAST_mul112_fixbits + (-10000)*main_mul107_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C1_main_mul107_CAST_mul112')
C2_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C2_main_mul107_CAST_mul112')
solver.Add( + (1)*main_mul107_fixbits + (-1)*main_mul107_CAST_mul112_fixbits + (-10000)*C1_main_mul107_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul107_fixbits + (1)*main_mul107_CAST_mul112_fixbits + (-10000)*C2_main_mul107_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul107_CAST_mul112
castCostObj +=  + (1)*C2_main_mul107_CAST_mul112
C3_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C3_main_mul107_CAST_mul112')
C4_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C4_main_mul107_CAST_mul112')
C5_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C5_main_mul107_CAST_mul112')
C6_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C6_main_mul107_CAST_mul112')
C7_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C7_main_mul107_CAST_mul112')
C8_main_mul107_CAST_mul112 = solver.IntVar(0, 1, 'C8_main_mul107_CAST_mul112')
solver.Add( + (1)*main_mul107_fixp + (1)*main_mul107_CAST_mul112_float + (-1)*C3_main_mul107_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul107_CAST_mul112
solver.Add( + (1)*main_mul107_float + (1)*main_mul107_CAST_mul112_fixp + (-1)*C4_main_mul107_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul107_CAST_mul112
solver.Add( + (1)*main_mul107_fixp + (1)*main_mul107_CAST_mul112_double + (-1)*C5_main_mul107_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul107_CAST_mul112
solver.Add( + (1)*main_mul107_double + (1)*main_mul107_CAST_mul112_fixp + (-1)*C6_main_mul107_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul107_CAST_mul112
solver.Add( + (1)*main_mul107_float + (1)*main_mul107_CAST_mul112_double + (-1)*C7_main_mul107_CAST_mul112<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul107_CAST_mul112
solver.Add( + (1)*main_mul107_double + (1)*main_mul107_CAST_mul112_float + (-1)*C8_main_mul107_CAST_mul112<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul107_CAST_mul112



#Constraint for cast for   %mul112 = fmul double %mul107, %tmp1, !taffo.info !58, !taffo.initweight !24
B_CAST_mul112_fixbits = solver.IntVar(0, 31, 'B_CAST_mul112_fixbits')
B_CAST_mul112_fixp = solver.IntVar(0, 1, 'B_CAST_mul112_fixp')
B_CAST_mul112_float = solver.IntVar(0, 1, 'B_CAST_mul112_float')
B_CAST_mul112_double = solver.IntVar(0, 1, 'B_CAST_mul112_double')
solver.Add( + (1)*B_CAST_mul112_fixp + (1)*B_CAST_mul112_float + (1)*B_CAST_mul112_double==1)    #exactly 1 type
solver.Add( + (1)*B_CAST_mul112_fixbits + (-10000)*B_CAST_mul112_fixp<=0)    #If no fix, fix frac part = 0
C1_B_CAST_mul112 = solver.IntVar(0, 1, 'C1_B_CAST_mul112')
C2_B_CAST_mul112 = solver.IntVar(0, 1, 'C2_B_CAST_mul112')
solver.Add( + (1)*B_fixbits + (-1)*B_CAST_mul112_fixbits + (-10000)*C1_B_CAST_mul112<=0)    #Shift cost 1
solver.Add( + (-1)*B_fixbits + (1)*B_CAST_mul112_fixbits + (-10000)*C2_B_CAST_mul112<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B_CAST_mul112
castCostObj +=  + (1)*C2_B_CAST_mul112
C3_B_CAST_mul112 = solver.IntVar(0, 1, 'C3_B_CAST_mul112')
C4_B_CAST_mul112 = solver.IntVar(0, 1, 'C4_B_CAST_mul112')
C5_B_CAST_mul112 = solver.IntVar(0, 1, 'C5_B_CAST_mul112')
C6_B_CAST_mul112 = solver.IntVar(0, 1, 'C6_B_CAST_mul112')
C7_B_CAST_mul112 = solver.IntVar(0, 1, 'C7_B_CAST_mul112')
C8_B_CAST_mul112 = solver.IntVar(0, 1, 'C8_B_CAST_mul112')
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul112_float + (-1)*C3_B_CAST_mul112<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_B_CAST_mul112
solver.Add( + (1)*B_float + (1)*B_CAST_mul112_fixp + (-1)*C4_B_CAST_mul112<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_B_CAST_mul112
solver.Add( + (1)*B_fixp + (1)*B_CAST_mul112_double + (-1)*C5_B_CAST_mul112<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_B_CAST_mul112
solver.Add( + (1)*B_double + (1)*B_CAST_mul112_fixp + (-1)*C6_B_CAST_mul112<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_B_CAST_mul112
solver.Add( + (1)*B_float + (1)*B_CAST_mul112_double + (-1)*C7_B_CAST_mul112<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_B_CAST_mul112
solver.Add( + (1)*B_double + (1)*B_CAST_mul112_float + (-1)*C8_B_CAST_mul112<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_B_CAST_mul112



#Stuff for   %mul112 = fmul double %mul107, %tmp1, !taffo.info !58, !taffo.initweight !24
main_mul112_fixbits = solver.IntVar(0, 30, 'main_mul112_fixbits')
main_mul112_fixp = solver.IntVar(0, 1, 'main_mul112_fixp')
main_mul112_float = solver.IntVar(0, 1, 'main_mul112_float')
main_mul112_double = solver.IntVar(0, 1, 'main_mul112_double')
main_mul112_enob = solver.IntVar(-10000, 10000, 'main_mul112_enob')
solver.Add( + (1)*main_mul112_enob + (-1)*main_mul112_fixbits + (10000)*main_mul112_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul112_enob + (10000)*main_mul112_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_mul112_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul112_enob
solver.Add( + (1)*main_mul112_fixp + (1)*main_mul112_float + (1)*main_mul112_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul112_fixbits + (-10000)*main_mul112_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul107_CAST_mul112_fixp + (-1)*B_CAST_mul112_fixp==0)    #fix equality
solver.Add( + (1)*main_mul107_CAST_mul112_float + (-1)*B_CAST_mul112_float==0)    #float equality
solver.Add( + (1)*main_mul107_CAST_mul112_double + (-1)*B_CAST_mul112_double==0)    #double equality
solver.Add( + (1)*main_mul107_CAST_mul112_fixp + (-1)*main_mul112_fixp==0)    #fix equality
solver.Add( + (1)*main_mul107_CAST_mul112_float + (-1)*main_mul112_float==0)    #float equality
solver.Add( + (1)*main_mul107_CAST_mul112_double + (-1)*main_mul112_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul112_fixp
mathCostObj +=  + (2.64722)*main_mul112_float
mathCostObj +=  + (4.02255)*main_mul112_double
main_main_mul112_enob_1 = solver.IntVar(0, 1, 'main_main_mul112_enob_1')
main_main_mul112_enob_2 = solver.IntVar(0, 1, 'main_main_mul112_enob_2')
solver.Add( + (1)*main_main_mul112_enob_1 + (1)*main_main_mul112_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul112_enob + (-1)*B_enob_memphi_main_tmp1 + (-10000)*main_main_mul112_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul112_enob + (-1)*main_mul107_enob + (-10000)*main_main_mul112_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
tmp_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'tmp_enob_memphi_main_tmp2')
solver.Add( + (1)*tmp_enob_memphi_main_tmp2 + (-1)*tmp_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
solver.Add( + (1)*main_main_tmp2_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add117 = fadd double %tmp2, %mul112, !taffo.info !63, !taffo.initweight !33
tmp_CAST_add117_fixbits = solver.IntVar(0, 16, 'tmp_CAST_add117_fixbits')
tmp_CAST_add117_fixp = solver.IntVar(0, 1, 'tmp_CAST_add117_fixp')
tmp_CAST_add117_float = solver.IntVar(0, 1, 'tmp_CAST_add117_float')
tmp_CAST_add117_double = solver.IntVar(0, 1, 'tmp_CAST_add117_double')
solver.Add( + (1)*tmp_CAST_add117_fixp + (1)*tmp_CAST_add117_float + (1)*tmp_CAST_add117_double==1)    #exactly 1 type
solver.Add( + (1)*tmp_CAST_add117_fixbits + (-10000)*tmp_CAST_add117_fixp<=0)    #If no fix, fix frac part = 0
C1_tmp_CAST_add117 = solver.IntVar(0, 1, 'C1_tmp_CAST_add117')
C2_tmp_CAST_add117 = solver.IntVar(0, 1, 'C2_tmp_CAST_add117')
solver.Add( + (1)*tmp_fixbits + (-1)*tmp_CAST_add117_fixbits + (-10000)*C1_tmp_CAST_add117<=0)    #Shift cost 1
solver.Add( + (-1)*tmp_fixbits + (1)*tmp_CAST_add117_fixbits + (-10000)*C2_tmp_CAST_add117<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_tmp_CAST_add117
castCostObj +=  + (1)*C2_tmp_CAST_add117
C3_tmp_CAST_add117 = solver.IntVar(0, 1, 'C3_tmp_CAST_add117')
C4_tmp_CAST_add117 = solver.IntVar(0, 1, 'C4_tmp_CAST_add117')
C5_tmp_CAST_add117 = solver.IntVar(0, 1, 'C5_tmp_CAST_add117')
C6_tmp_CAST_add117 = solver.IntVar(0, 1, 'C6_tmp_CAST_add117')
C7_tmp_CAST_add117 = solver.IntVar(0, 1, 'C7_tmp_CAST_add117')
C8_tmp_CAST_add117 = solver.IntVar(0, 1, 'C8_tmp_CAST_add117')
solver.Add( + (1)*tmp_fixp + (1)*tmp_CAST_add117_float + (-1)*C3_tmp_CAST_add117<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_tmp_CAST_add117
solver.Add( + (1)*tmp_float + (1)*tmp_CAST_add117_fixp + (-1)*C4_tmp_CAST_add117<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_tmp_CAST_add117
solver.Add( + (1)*tmp_fixp + (1)*tmp_CAST_add117_double + (-1)*C5_tmp_CAST_add117<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_tmp_CAST_add117
solver.Add( + (1)*tmp_double + (1)*tmp_CAST_add117_fixp + (-1)*C6_tmp_CAST_add117<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_tmp_CAST_add117
solver.Add( + (1)*tmp_float + (1)*tmp_CAST_add117_double + (-1)*C7_tmp_CAST_add117<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_tmp_CAST_add117
solver.Add( + (1)*tmp_double + (1)*tmp_CAST_add117_float + (-1)*C8_tmp_CAST_add117<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_tmp_CAST_add117



#Constraint for cast for   %add117 = fadd double %tmp2, %mul112, !taffo.info !63, !taffo.initweight !33
main_mul112_CAST_add117_fixbits = solver.IntVar(0, 30, 'main_mul112_CAST_add117_fixbits')
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



#Stuff for   %add117 = fadd double %tmp2, %mul112, !taffo.info !63, !taffo.initweight !33
main_add117_fixbits = solver.IntVar(0, 16, 'main_add117_fixbits')
main_add117_fixp = solver.IntVar(0, 1, 'main_add117_fixp')
main_add117_float = solver.IntVar(0, 1, 'main_add117_float')
main_add117_double = solver.IntVar(0, 1, 'main_add117_double')
main_add117_enob = solver.IntVar(-10000, 10000, 'main_add117_enob')
solver.Add( + (1)*main_add117_enob + (-1)*main_add117_fixbits + (10000)*main_add117_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add117_enob + (10000)*main_add117_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add117_enob + (10000)*main_add117_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add117_fixbits + (-10000)*main_add117_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_add117_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add117_enob
solver.Add( + (1)*main_add117_fixp + (1)*main_add117_float + (1)*main_add117_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add117_fixbits + (-10000)*main_add117_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*tmp_CAST_add117_fixp + (-1)*main_mul112_CAST_add117_fixp==0)    #fix equality
solver.Add( + (1)*tmp_CAST_add117_float + (-1)*main_mul112_CAST_add117_float==0)    #float equality
solver.Add( + (1)*tmp_CAST_add117_double + (-1)*main_mul112_CAST_add117_double==0)    #double equality
solver.Add( + (1)*tmp_CAST_add117_fixbits + (-1)*main_mul112_CAST_add117_fixbits==0)    #same fractional bit
solver.Add( + (1)*tmp_CAST_add117_fixp + (-1)*main_add117_fixp==0)    #fix equality
solver.Add( + (1)*tmp_CAST_add117_float + (-1)*main_add117_float==0)    #float equality
solver.Add( + (1)*tmp_CAST_add117_double + (-1)*main_add117_double==0)    #double equality
solver.Add( + (1)*tmp_CAST_add117_fixbits + (-1)*main_add117_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add117_fixp
mathCostObj +=  + (2.33125)*main_add117_float
mathCostObj +=  + (2.72422)*main_add117_double
solver.Add( + (1)*main_add117_enob + (-1)*tmp_enob_memphi_main_tmp2<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add117_enob + (-1)*main_mul112_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add117, double* %arrayidx116, align 8, !taffo.info !12, !taffo.initweight !24
main_add117_CAST_store_fixbits = solver.IntVar(0, 16, 'main_add117_CAST_store_fixbits')
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
solver.Add( + (1)*tmp_fixp + (-1)*main_add117_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*tmp_float + (-1)*main_add117_CAST_store_float==0)    #float equality
solver.Add( + (1)*tmp_double + (-1)*main_add117_CAST_store_double==0)    #double equality
solver.Add( + (1)*tmp_fixbits + (-1)*main_add117_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
tmp_enob_storeENOB = solver.IntVar(-10000, 10000, 'tmp_enob_storeENOB')
solver.Add( + (1)*tmp_enob_storeENOB + (-1)*tmp_fixbits + (10000)*tmp_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*tmp_enob_storeENOB + (10000)*tmp_float<=10149)    #Enob constraint for float
solver.Add( + (1)*tmp_enob_storeENOB + (10000)*tmp_double<=11074)    #Enob constraint for double
solver.Add( + (1)*tmp_enob_storeENOB + (-1)*main_add117_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*tmp_enob_memphi_main_tmp2 + (-1)*tmp_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
D_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'D_enob_memphi_main_tmp3')
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*D_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
main_main_tmp3_enob_4 = solver.IntVar(0, 1, 'main_main_tmp3_enob_4')
main_main_tmp3_enob_6 = solver.IntVar(0, 1, 'main_main_tmp3_enob_6')
main_main_tmp3_enob_7 = solver.IntVar(0, 1, 'main_main_tmp3_enob_7')
main_main_tmp3_enob_8 = solver.IntVar(0, 1, 'main_main_tmp3_enob_8')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3 + (1)*main_main_tmp3_enob_4 + (1)*main_main_tmp3_enob_6 + (1)*main_main_tmp3_enob_7 + (1)*main_main_tmp3_enob_8==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp3_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*B_enob_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*C_enob_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*D_enob_storeENOB + (10000)*main_main_tmp3_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*tmp_enob_storeENOB + (10000)*main_main_tmp3_enob_6<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.200000e+00
ConstantValue__4_fixbits = solver.IntVar(0, 30, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.200000e+00
ConstantValue__5_fixbits = solver.IntVar(0, 30, 'ConstantValue__5_fixbits')
ConstantValue__5_fixp = solver.IntVar(0, 1, 'ConstantValue__5_fixp')
ConstantValue__5_float = solver.IntVar(0, 1, 'ConstantValue__5_float')
ConstantValue__5_double = solver.IntVar(0, 1, 'ConstantValue__5_double')
ConstantValue__5_enob = solver.IntVar(-10000, 10000, 'ConstantValue__5_enob')
solver.Add( + (1)*ConstantValue__5_enob + (-1)*ConstantValue__5_fixbits + (10000)*ConstantValue__5_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__5_enob + (10000)*ConstantValue__5_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__5_fixp + (1)*ConstantValue__5_float + (1)*ConstantValue__5_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__5_fixbits + (-10000)*ConstantValue__5_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul139 = fmul double %tmp3, 1.200000e+00, !taffo.info !67, !taffo.initweight !23, !taffo.constinfo !69
D_CAST_mul139_fixbits = solver.IntVar(0, 16, 'D_CAST_mul139_fixbits')
D_CAST_mul139_fixp = solver.IntVar(0, 1, 'D_CAST_mul139_fixp')
D_CAST_mul139_float = solver.IntVar(0, 1, 'D_CAST_mul139_float')
D_CAST_mul139_double = solver.IntVar(0, 1, 'D_CAST_mul139_double')
solver.Add( + (1)*D_CAST_mul139_fixp + (1)*D_CAST_mul139_float + (1)*D_CAST_mul139_double==1)    #exactly 1 type
solver.Add( + (1)*D_CAST_mul139_fixbits + (-10000)*D_CAST_mul139_fixp<=0)    #If no fix, fix frac part = 0
C1_D_CAST_mul139 = solver.IntVar(0, 1, 'C1_D_CAST_mul139')
C2_D_CAST_mul139 = solver.IntVar(0, 1, 'C2_D_CAST_mul139')
solver.Add( + (1)*D_fixbits + (-1)*D_CAST_mul139_fixbits + (-10000)*C1_D_CAST_mul139<=0)    #Shift cost 1
solver.Add( + (-1)*D_fixbits + (1)*D_CAST_mul139_fixbits + (-10000)*C2_D_CAST_mul139<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_D_CAST_mul139
castCostObj +=  + (1)*C2_D_CAST_mul139
C3_D_CAST_mul139 = solver.IntVar(0, 1, 'C3_D_CAST_mul139')
C4_D_CAST_mul139 = solver.IntVar(0, 1, 'C4_D_CAST_mul139')
C5_D_CAST_mul139 = solver.IntVar(0, 1, 'C5_D_CAST_mul139')
C6_D_CAST_mul139 = solver.IntVar(0, 1, 'C6_D_CAST_mul139')
C7_D_CAST_mul139 = solver.IntVar(0, 1, 'C7_D_CAST_mul139')
C8_D_CAST_mul139 = solver.IntVar(0, 1, 'C8_D_CAST_mul139')
solver.Add( + (1)*D_fixp + (1)*D_CAST_mul139_float + (-1)*C3_D_CAST_mul139<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_D_CAST_mul139
solver.Add( + (1)*D_float + (1)*D_CAST_mul139_fixp + (-1)*C4_D_CAST_mul139<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_D_CAST_mul139
solver.Add( + (1)*D_fixp + (1)*D_CAST_mul139_double + (-1)*C5_D_CAST_mul139<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_D_CAST_mul139
solver.Add( + (1)*D_double + (1)*D_CAST_mul139_fixp + (-1)*C6_D_CAST_mul139<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_D_CAST_mul139
solver.Add( + (1)*D_float + (1)*D_CAST_mul139_double + (-1)*C7_D_CAST_mul139<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_D_CAST_mul139
solver.Add( + (1)*D_double + (1)*D_CAST_mul139_float + (-1)*C8_D_CAST_mul139<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_D_CAST_mul139



#Stuff for double 1.200000e+00
ConstantValue__6_fixbits = solver.IntVar(0, 30, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul139 = fmul double %tmp3, 1.200000e+00, !taffo.info !67, !taffo.initweight !23, !taffo.constinfo !69
ConstantValue__6_CAST_mul139_fixbits = solver.IntVar(0, 30, 'ConstantValue__6_CAST_mul139_fixbits')
ConstantValue__6_CAST_mul139_fixp = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul139_fixp')
ConstantValue__6_CAST_mul139_float = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul139_float')
ConstantValue__6_CAST_mul139_double = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul139_double')
solver.Add( + (1)*ConstantValue__6_CAST_mul139_fixp + (1)*ConstantValue__6_CAST_mul139_float + (1)*ConstantValue__6_CAST_mul139_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__6_CAST_mul139_fixbits + (-10000)*ConstantValue__6_CAST_mul139_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C1_ConstantValue__6_CAST_mul139')
C2_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C2_ConstantValue__6_CAST_mul139')
solver.Add( + (1)*ConstantValue__6_fixbits + (-1)*ConstantValue__6_CAST_mul139_fixbits + (-10000)*C1_ConstantValue__6_CAST_mul139<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__6_fixbits + (1)*ConstantValue__6_CAST_mul139_fixbits + (-10000)*C2_ConstantValue__6_CAST_mul139<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__6_CAST_mul139
castCostObj +=  + (1)*C2_ConstantValue__6_CAST_mul139
C3_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C3_ConstantValue__6_CAST_mul139')
C4_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C4_ConstantValue__6_CAST_mul139')
C5_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C5_ConstantValue__6_CAST_mul139')
C6_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C6_ConstantValue__6_CAST_mul139')
C7_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C7_ConstantValue__6_CAST_mul139')
C8_ConstantValue__6_CAST_mul139 = solver.IntVar(0, 1, 'C8_ConstantValue__6_CAST_mul139')
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_mul139_float + (-1)*C3_ConstantValue__6_CAST_mul139<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__6_CAST_mul139
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_mul139_fixp + (-1)*C4_ConstantValue__6_CAST_mul139<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__6_CAST_mul139
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_mul139_double + (-1)*C5_ConstantValue__6_CAST_mul139<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__6_CAST_mul139
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_mul139_fixp + (-1)*C6_ConstantValue__6_CAST_mul139<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__6_CAST_mul139
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_mul139_double + (-1)*C7_ConstantValue__6_CAST_mul139<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__6_CAST_mul139
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_mul139_float + (-1)*C8_ConstantValue__6_CAST_mul139<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__6_CAST_mul139



#Stuff for   %mul139 = fmul double %tmp3, 1.200000e+00, !taffo.info !67, !taffo.initweight !23, !taffo.constinfo !69
main_mul139_fixbits = solver.IntVar(0, 16, 'main_mul139_fixbits')
main_mul139_fixp = solver.IntVar(0, 1, 'main_mul139_fixp')
main_mul139_float = solver.IntVar(0, 1, 'main_mul139_float')
main_mul139_double = solver.IntVar(0, 1, 'main_mul139_double')
main_mul139_enob = solver.IntVar(-10000, 10000, 'main_mul139_enob')
solver.Add( + (1)*main_mul139_enob + (-1)*main_mul139_fixbits + (10000)*main_mul139_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul139_enob + (10000)*main_mul139_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul139_enob + (10000)*main_mul139_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul139_fixbits + (-10000)*main_mul139_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul139_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul139_enob
solver.Add( + (1)*main_mul139_fixp + (1)*main_mul139_float + (1)*main_mul139_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul139_fixbits + (-10000)*main_mul139_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*D_CAST_mul139_fixp + (-1)*ConstantValue__6_CAST_mul139_fixp==0)    #fix equality
solver.Add( + (1)*D_CAST_mul139_float + (-1)*ConstantValue__6_CAST_mul139_float==0)    #float equality
solver.Add( + (1)*D_CAST_mul139_double + (-1)*ConstantValue__6_CAST_mul139_double==0)    #double equality
solver.Add( + (1)*D_CAST_mul139_fixp + (-1)*main_mul139_fixp==0)    #fix equality
solver.Add( + (1)*D_CAST_mul139_float + (-1)*main_mul139_float==0)    #float equality
solver.Add( + (1)*D_CAST_mul139_double + (-1)*main_mul139_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul139_fixp
mathCostObj +=  + (2.64722)*main_mul139_float
mathCostObj +=  + (4.02255)*main_mul139_double
main_main_mul139_enob_1 = solver.IntVar(0, 1, 'main_main_mul139_enob_1')
main_main_mul139_enob_2 = solver.IntVar(0, 1, 'main_main_mul139_enob_2')
solver.Add( + (1)*main_main_mul139_enob_1 + (1)*main_main_mul139_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul139_enob + (-1)*ConstantValue__4_enob + (-10000)*main_main_mul139_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul139_enob + (-1)*D_enob_memphi_main_tmp3 + (-10000)*main_main_mul139_enob_2<=0)    #Enob: propagation in product 2



#Constraint for cast for   store double %mul139, double* %arrayidx138, align 8, !taffo.info !12, !taffo.initweight !24
main_mul139_CAST_store_fixbits = solver.IntVar(0, 16, 'main_mul139_CAST_store_fixbits')
main_mul139_CAST_store_fixp = solver.IntVar(0, 1, 'main_mul139_CAST_store_fixp')
main_mul139_CAST_store_float = solver.IntVar(0, 1, 'main_mul139_CAST_store_float')
main_mul139_CAST_store_double = solver.IntVar(0, 1, 'main_mul139_CAST_store_double')
solver.Add( + (1)*main_mul139_CAST_store_fixp + (1)*main_mul139_CAST_store_float + (1)*main_mul139_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul139_CAST_store_fixbits + (-10000)*main_mul139_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul139_CAST_store = solver.IntVar(0, 1, 'C1_main_mul139_CAST_store')
C2_main_mul139_CAST_store = solver.IntVar(0, 1, 'C2_main_mul139_CAST_store')
solver.Add( + (1)*main_mul139_fixbits + (-1)*main_mul139_CAST_store_fixbits + (-10000)*C1_main_mul139_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul139_fixbits + (1)*main_mul139_CAST_store_fixbits + (-10000)*C2_main_mul139_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul139_CAST_store
castCostObj +=  + (1)*C2_main_mul139_CAST_store
C3_main_mul139_CAST_store = solver.IntVar(0, 1, 'C3_main_mul139_CAST_store')
C4_main_mul139_CAST_store = solver.IntVar(0, 1, 'C4_main_mul139_CAST_store')
C5_main_mul139_CAST_store = solver.IntVar(0, 1, 'C5_main_mul139_CAST_store')
C6_main_mul139_CAST_store = solver.IntVar(0, 1, 'C6_main_mul139_CAST_store')
C7_main_mul139_CAST_store = solver.IntVar(0, 1, 'C7_main_mul139_CAST_store')
C8_main_mul139_CAST_store = solver.IntVar(0, 1, 'C8_main_mul139_CAST_store')
solver.Add( + (1)*main_mul139_fixp + (1)*main_mul139_CAST_store_float + (-1)*C3_main_mul139_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul139_CAST_store
solver.Add( + (1)*main_mul139_float + (1)*main_mul139_CAST_store_fixp + (-1)*C4_main_mul139_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul139_CAST_store
solver.Add( + (1)*main_mul139_fixp + (1)*main_mul139_CAST_store_double + (-1)*C5_main_mul139_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul139_CAST_store
solver.Add( + (1)*main_mul139_double + (1)*main_mul139_CAST_store_fixp + (-1)*C6_main_mul139_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul139_CAST_store
solver.Add( + (1)*main_mul139_float + (1)*main_mul139_CAST_store_double + (-1)*C7_main_mul139_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul139_CAST_store
solver.Add( + (1)*main_mul139_double + (1)*main_mul139_CAST_store_float + (-1)*C8_main_mul139_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul139_CAST_store
solver.Add( + (1)*D_fixp + (-1)*main_mul139_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*D_float + (-1)*main_mul139_CAST_store_float==0)    #float equality
solver.Add( + (1)*D_double + (-1)*main_mul139_CAST_store_double==0)    #double equality
solver.Add( + (1)*D_fixbits + (-1)*main_mul139_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
D_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'D_enob_storeENOB_storeENOB')
solver.Add( + (1)*D_enob_storeENOB_storeENOB + (-1)*D_fixbits + (10000)*D_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*D_enob_storeENOB_storeENOB + (10000)*D_float<=10149)    #Enob constraint for float
solver.Add( + (1)*D_enob_storeENOB_storeENOB + (10000)*D_double<=11074)    #Enob constraint for double
solver.Add( + (1)*D_enob_storeENOB_storeENOB + (-1)*main_mul139_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*D_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_7<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
tmp_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'tmp_enob_memphi_main_tmp4')
solver.Add( + (1)*tmp_enob_memphi_main_tmp4 + (-1)*tmp_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
main_main_tmp4_enob_4 = solver.IntVar(0, 1, 'main_main_tmp4_enob_4')
main_main_tmp4_enob_6 = solver.IntVar(0, 1, 'main_main_tmp4_enob_6')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3 + (1)*main_main_tmp4_enob_4 + (1)*main_main_tmp4_enob_6==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*tmp_enob_memphi_main_tmp4 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp4_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*tmp_enob_memphi_main_tmp4 + (-1)*B_enob_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*tmp_enob_memphi_main_tmp4 + (-1)*C_enob_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*tmp_enob_memphi_main_tmp4 + (-1)*D_enob_storeENOB + (10000)*main_main_tmp4_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*tmp_enob_memphi_main_tmp4 + (-1)*tmp_enob_storeENOB + (10000)*main_main_tmp4_enob_6<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
C_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'C_enob_memphi_main_tmp5')
solver.Add( + (1)*C_enob_memphi_main_tmp5 + (-1)*C_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_1 = solver.IntVar(0, 1, 'main_main_tmp5_enob_1')
main_main_tmp5_enob_2 = solver.IntVar(0, 1, 'main_main_tmp5_enob_2')
main_main_tmp5_enob_3 = solver.IntVar(0, 1, 'main_main_tmp5_enob_3')
solver.Add( + (1)*main_main_tmp5_enob_1 + (1)*main_main_tmp5_enob_2 + (1)*main_main_tmp5_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*C_enob_memphi_main_tmp5 + (-1)*A_enob_storeENOB + (10000)*main_main_tmp5_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*C_enob_memphi_main_tmp5 + (-1)*B_enob_storeENOB + (10000)*main_main_tmp5_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*C_enob_memphi_main_tmp5 + (-1)*C_enob_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul152 = fmul double %tmp4, %tmp5, !taffo.info !12, !taffo.initweight !33
tmp_CAST_mul152_fixbits = solver.IntVar(0, 16, 'tmp_CAST_mul152_fixbits')
tmp_CAST_mul152_fixp = solver.IntVar(0, 1, 'tmp_CAST_mul152_fixp')
tmp_CAST_mul152_float = solver.IntVar(0, 1, 'tmp_CAST_mul152_float')
tmp_CAST_mul152_double = solver.IntVar(0, 1, 'tmp_CAST_mul152_double')
solver.Add( + (1)*tmp_CAST_mul152_fixp + (1)*tmp_CAST_mul152_float + (1)*tmp_CAST_mul152_double==1)    #exactly 1 type
solver.Add( + (1)*tmp_CAST_mul152_fixbits + (-10000)*tmp_CAST_mul152_fixp<=0)    #If no fix, fix frac part = 0
C1_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C1_tmp_CAST_mul152')
C2_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C2_tmp_CAST_mul152')
solver.Add( + (1)*tmp_fixbits + (-1)*tmp_CAST_mul152_fixbits + (-10000)*C1_tmp_CAST_mul152<=0)    #Shift cost 1
solver.Add( + (-1)*tmp_fixbits + (1)*tmp_CAST_mul152_fixbits + (-10000)*C2_tmp_CAST_mul152<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_tmp_CAST_mul152
castCostObj +=  + (1)*C2_tmp_CAST_mul152
C3_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C3_tmp_CAST_mul152')
C4_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C4_tmp_CAST_mul152')
C5_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C5_tmp_CAST_mul152')
C6_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C6_tmp_CAST_mul152')
C7_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C7_tmp_CAST_mul152')
C8_tmp_CAST_mul152 = solver.IntVar(0, 1, 'C8_tmp_CAST_mul152')
solver.Add( + (1)*tmp_fixp + (1)*tmp_CAST_mul152_float + (-1)*C3_tmp_CAST_mul152<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_tmp_CAST_mul152
solver.Add( + (1)*tmp_float + (1)*tmp_CAST_mul152_fixp + (-1)*C4_tmp_CAST_mul152<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_tmp_CAST_mul152
solver.Add( + (1)*tmp_fixp + (1)*tmp_CAST_mul152_double + (-1)*C5_tmp_CAST_mul152<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_tmp_CAST_mul152
solver.Add( + (1)*tmp_double + (1)*tmp_CAST_mul152_fixp + (-1)*C6_tmp_CAST_mul152<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_tmp_CAST_mul152
solver.Add( + (1)*tmp_float + (1)*tmp_CAST_mul152_double + (-1)*C7_tmp_CAST_mul152<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_tmp_CAST_mul152
solver.Add( + (1)*tmp_double + (1)*tmp_CAST_mul152_float + (-1)*C8_tmp_CAST_mul152<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_tmp_CAST_mul152



#Constraint for cast for   %mul152 = fmul double %tmp4, %tmp5, !taffo.info !12, !taffo.initweight !33
C_CAST_mul152_fixbits = solver.IntVar(0, 31, 'C_CAST_mul152_fixbits')
C_CAST_mul152_fixp = solver.IntVar(0, 1, 'C_CAST_mul152_fixp')
C_CAST_mul152_float = solver.IntVar(0, 1, 'C_CAST_mul152_float')
C_CAST_mul152_double = solver.IntVar(0, 1, 'C_CAST_mul152_double')
solver.Add( + (1)*C_CAST_mul152_fixp + (1)*C_CAST_mul152_float + (1)*C_CAST_mul152_double==1)    #exactly 1 type
solver.Add( + (1)*C_CAST_mul152_fixbits + (-10000)*C_CAST_mul152_fixp<=0)    #If no fix, fix frac part = 0
C1_C_CAST_mul152 = solver.IntVar(0, 1, 'C1_C_CAST_mul152')
C2_C_CAST_mul152 = solver.IntVar(0, 1, 'C2_C_CAST_mul152')
solver.Add( + (1)*C_fixbits + (-1)*C_CAST_mul152_fixbits + (-10000)*C1_C_CAST_mul152<=0)    #Shift cost 1
solver.Add( + (-1)*C_fixbits + (1)*C_CAST_mul152_fixbits + (-10000)*C2_C_CAST_mul152<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_C_CAST_mul152
castCostObj +=  + (1)*C2_C_CAST_mul152
C3_C_CAST_mul152 = solver.IntVar(0, 1, 'C3_C_CAST_mul152')
C4_C_CAST_mul152 = solver.IntVar(0, 1, 'C4_C_CAST_mul152')
C5_C_CAST_mul152 = solver.IntVar(0, 1, 'C5_C_CAST_mul152')
C6_C_CAST_mul152 = solver.IntVar(0, 1, 'C6_C_CAST_mul152')
C7_C_CAST_mul152 = solver.IntVar(0, 1, 'C7_C_CAST_mul152')
C8_C_CAST_mul152 = solver.IntVar(0, 1, 'C8_C_CAST_mul152')
solver.Add( + (1)*C_fixp + (1)*C_CAST_mul152_float + (-1)*C3_C_CAST_mul152<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_C_CAST_mul152
solver.Add( + (1)*C_float + (1)*C_CAST_mul152_fixp + (-1)*C4_C_CAST_mul152<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_C_CAST_mul152
solver.Add( + (1)*C_fixp + (1)*C_CAST_mul152_double + (-1)*C5_C_CAST_mul152<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_C_CAST_mul152
solver.Add( + (1)*C_double + (1)*C_CAST_mul152_fixp + (-1)*C6_C_CAST_mul152<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_C_CAST_mul152
solver.Add( + (1)*C_float + (1)*C_CAST_mul152_double + (-1)*C7_C_CAST_mul152<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_C_CAST_mul152
solver.Add( + (1)*C_double + (1)*C_CAST_mul152_float + (-1)*C8_C_CAST_mul152<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_C_CAST_mul152



#Stuff for   %mul152 = fmul double %tmp4, %tmp5, !taffo.info !12, !taffo.initweight !33
main_mul152_fixbits = solver.IntVar(0, 16, 'main_mul152_fixbits')
main_mul152_fixp = solver.IntVar(0, 1, 'main_mul152_fixp')
main_mul152_float = solver.IntVar(0, 1, 'main_mul152_float')
main_mul152_double = solver.IntVar(0, 1, 'main_mul152_double')
main_mul152_enob = solver.IntVar(-10000, 10000, 'main_mul152_enob')
solver.Add( + (1)*main_mul152_enob + (-1)*main_mul152_fixbits + (10000)*main_mul152_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul152_enob + (10000)*main_mul152_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul152_enob + (10000)*main_mul152_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul152_fixbits + (-10000)*main_mul152_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul152_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul152_enob
solver.Add( + (1)*main_mul152_fixp + (1)*main_mul152_float + (1)*main_mul152_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul152_fixbits + (-10000)*main_mul152_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*tmp_CAST_mul152_fixp + (-1)*C_CAST_mul152_fixp==0)    #fix equality
solver.Add( + (1)*tmp_CAST_mul152_float + (-1)*C_CAST_mul152_float==0)    #float equality
solver.Add( + (1)*tmp_CAST_mul152_double + (-1)*C_CAST_mul152_double==0)    #double equality
solver.Add( + (1)*tmp_CAST_mul152_fixp + (-1)*main_mul152_fixp==0)    #fix equality
solver.Add( + (1)*tmp_CAST_mul152_float + (-1)*main_mul152_float==0)    #float equality
solver.Add( + (1)*tmp_CAST_mul152_double + (-1)*main_mul152_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul152_fixp
mathCostObj +=  + (2.64722)*main_mul152_float
mathCostObj +=  + (4.02255)*main_mul152_double
main_main_mul152_enob_1 = solver.IntVar(0, 1, 'main_main_mul152_enob_1')
main_main_mul152_enob_2 = solver.IntVar(0, 1, 'main_main_mul152_enob_2')
solver.Add( + (1)*main_main_mul152_enob_1 + (1)*main_main_mul152_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul152_enob + (-1)*C_enob_memphi_main_tmp5 + (-10000)*main_main_mul152_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul152_enob + (-1)*tmp_enob_memphi_main_tmp4 + (-10000)*main_main_mul152_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
D_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'D_enob_memphi_main_tmp6')
solver.Add( + (1)*D_enob_memphi_main_tmp6 + (-1)*D_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_0 = solver.IntVar(0, 1, 'main_main_tmp6_enob_0')
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
solver.Add( + (1)*main_main_tmp6_enob_0 + (1)*main_main_tmp6_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp6 + (-1)*D_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add157 = fadd double %tmp6, %mul152, !taffo.info !72, !taffo.initweight !33
D_CAST_add157_fixbits = solver.IntVar(0, 16, 'D_CAST_add157_fixbits')
D_CAST_add157_fixp = solver.IntVar(0, 1, 'D_CAST_add157_fixp')
D_CAST_add157_float = solver.IntVar(0, 1, 'D_CAST_add157_float')
D_CAST_add157_double = solver.IntVar(0, 1, 'D_CAST_add157_double')
solver.Add( + (1)*D_CAST_add157_fixp + (1)*D_CAST_add157_float + (1)*D_CAST_add157_double==1)    #exactly 1 type
solver.Add( + (1)*D_CAST_add157_fixbits + (-10000)*D_CAST_add157_fixp<=0)    #If no fix, fix frac part = 0
C1_D_CAST_add157 = solver.IntVar(0, 1, 'C1_D_CAST_add157')
C2_D_CAST_add157 = solver.IntVar(0, 1, 'C2_D_CAST_add157')
solver.Add( + (1)*D_fixbits + (-1)*D_CAST_add157_fixbits + (-10000)*C1_D_CAST_add157<=0)    #Shift cost 1
solver.Add( + (-1)*D_fixbits + (1)*D_CAST_add157_fixbits + (-10000)*C2_D_CAST_add157<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_D_CAST_add157
castCostObj +=  + (1)*C2_D_CAST_add157
C3_D_CAST_add157 = solver.IntVar(0, 1, 'C3_D_CAST_add157')
C4_D_CAST_add157 = solver.IntVar(0, 1, 'C4_D_CAST_add157')
C5_D_CAST_add157 = solver.IntVar(0, 1, 'C5_D_CAST_add157')
C6_D_CAST_add157 = solver.IntVar(0, 1, 'C6_D_CAST_add157')
C7_D_CAST_add157 = solver.IntVar(0, 1, 'C7_D_CAST_add157')
C8_D_CAST_add157 = solver.IntVar(0, 1, 'C8_D_CAST_add157')
solver.Add( + (1)*D_fixp + (1)*D_CAST_add157_float + (-1)*C3_D_CAST_add157<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_D_CAST_add157
solver.Add( + (1)*D_float + (1)*D_CAST_add157_fixp + (-1)*C4_D_CAST_add157<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_D_CAST_add157
solver.Add( + (1)*D_fixp + (1)*D_CAST_add157_double + (-1)*C5_D_CAST_add157<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_D_CAST_add157
solver.Add( + (1)*D_double + (1)*D_CAST_add157_fixp + (-1)*C6_D_CAST_add157<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_D_CAST_add157
solver.Add( + (1)*D_float + (1)*D_CAST_add157_double + (-1)*C7_D_CAST_add157<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_D_CAST_add157
solver.Add( + (1)*D_double + (1)*D_CAST_add157_float + (-1)*C8_D_CAST_add157<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_D_CAST_add157



#Constraint for cast for   %add157 = fadd double %tmp6, %mul152, !taffo.info !72, !taffo.initweight !33
main_mul152_CAST_add157_fixbits = solver.IntVar(0, 16, 'main_mul152_CAST_add157_fixbits')
main_mul152_CAST_add157_fixp = solver.IntVar(0, 1, 'main_mul152_CAST_add157_fixp')
main_mul152_CAST_add157_float = solver.IntVar(0, 1, 'main_mul152_CAST_add157_float')
main_mul152_CAST_add157_double = solver.IntVar(0, 1, 'main_mul152_CAST_add157_double')
solver.Add( + (1)*main_mul152_CAST_add157_fixp + (1)*main_mul152_CAST_add157_float + (1)*main_mul152_CAST_add157_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul152_CAST_add157_fixbits + (-10000)*main_mul152_CAST_add157_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C1_main_mul152_CAST_add157')
C2_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C2_main_mul152_CAST_add157')
solver.Add( + (1)*main_mul152_fixbits + (-1)*main_mul152_CAST_add157_fixbits + (-10000)*C1_main_mul152_CAST_add157<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul152_fixbits + (1)*main_mul152_CAST_add157_fixbits + (-10000)*C2_main_mul152_CAST_add157<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul152_CAST_add157
castCostObj +=  + (1)*C2_main_mul152_CAST_add157
C3_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C3_main_mul152_CAST_add157')
C4_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C4_main_mul152_CAST_add157')
C5_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C5_main_mul152_CAST_add157')
C6_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C6_main_mul152_CAST_add157')
C7_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C7_main_mul152_CAST_add157')
C8_main_mul152_CAST_add157 = solver.IntVar(0, 1, 'C8_main_mul152_CAST_add157')
solver.Add( + (1)*main_mul152_fixp + (1)*main_mul152_CAST_add157_float + (-1)*C3_main_mul152_CAST_add157<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul152_CAST_add157
solver.Add( + (1)*main_mul152_float + (1)*main_mul152_CAST_add157_fixp + (-1)*C4_main_mul152_CAST_add157<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul152_CAST_add157
solver.Add( + (1)*main_mul152_fixp + (1)*main_mul152_CAST_add157_double + (-1)*C5_main_mul152_CAST_add157<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul152_CAST_add157
solver.Add( + (1)*main_mul152_double + (1)*main_mul152_CAST_add157_fixp + (-1)*C6_main_mul152_CAST_add157<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul152_CAST_add157
solver.Add( + (1)*main_mul152_float + (1)*main_mul152_CAST_add157_double + (-1)*C7_main_mul152_CAST_add157<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul152_CAST_add157
solver.Add( + (1)*main_mul152_double + (1)*main_mul152_CAST_add157_float + (-1)*C8_main_mul152_CAST_add157<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul152_CAST_add157



#Stuff for   %add157 = fadd double %tmp6, %mul152, !taffo.info !72, !taffo.initweight !33
main_add157_fixbits = solver.IntVar(0, 15, 'main_add157_fixbits')
main_add157_fixp = solver.IntVar(0, 1, 'main_add157_fixp')
main_add157_float = solver.IntVar(0, 1, 'main_add157_float')
main_add157_double = solver.IntVar(0, 1, 'main_add157_double')
main_add157_enob = solver.IntVar(-10000, 10000, 'main_add157_enob')
solver.Add( + (1)*main_add157_enob + (-1)*main_add157_fixbits + (10000)*main_add157_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add157_enob + (10000)*main_add157_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add157_enob + (10000)*main_add157_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add157_fixbits + (-10000)*main_add157_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add157_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add157_enob
solver.Add( + (1)*main_add157_fixp + (1)*main_add157_float + (1)*main_add157_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add157_fixbits + (-10000)*main_add157_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*D_CAST_add157_fixp + (-1)*main_mul152_CAST_add157_fixp==0)    #fix equality
solver.Add( + (1)*D_CAST_add157_float + (-1)*main_mul152_CAST_add157_float==0)    #float equality
solver.Add( + (1)*D_CAST_add157_double + (-1)*main_mul152_CAST_add157_double==0)    #double equality
solver.Add( + (1)*D_CAST_add157_fixbits + (-1)*main_mul152_CAST_add157_fixbits==0)    #same fractional bit
solver.Add( + (1)*D_CAST_add157_fixp + (-1)*main_add157_fixp==0)    #fix equality
solver.Add( + (1)*D_CAST_add157_float + (-1)*main_add157_float==0)    #float equality
solver.Add( + (1)*D_CAST_add157_double + (-1)*main_add157_double==0)    #double equality
solver.Add( + (1)*D_CAST_add157_fixbits + (-1)*main_add157_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add157_fixp
mathCostObj +=  + (2.33125)*main_add157_float
mathCostObj +=  + (2.72422)*main_add157_double
solver.Add( + (1)*main_add157_enob + (-1)*D_enob_memphi_main_tmp6<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add157_enob + (-1)*main_mul152_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add157, double* %arrayidx156, align 8, !taffo.info !12, !taffo.initweight !24
main_add157_CAST_store_fixbits = solver.IntVar(0, 15, 'main_add157_CAST_store_fixbits')
main_add157_CAST_store_fixp = solver.IntVar(0, 1, 'main_add157_CAST_store_fixp')
main_add157_CAST_store_float = solver.IntVar(0, 1, 'main_add157_CAST_store_float')
main_add157_CAST_store_double = solver.IntVar(0, 1, 'main_add157_CAST_store_double')
solver.Add( + (1)*main_add157_CAST_store_fixp + (1)*main_add157_CAST_store_float + (1)*main_add157_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add157_CAST_store_fixbits + (-10000)*main_add157_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add157_CAST_store = solver.IntVar(0, 1, 'C1_main_add157_CAST_store')
C2_main_add157_CAST_store = solver.IntVar(0, 1, 'C2_main_add157_CAST_store')
solver.Add( + (1)*main_add157_fixbits + (-1)*main_add157_CAST_store_fixbits + (-10000)*C1_main_add157_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add157_fixbits + (1)*main_add157_CAST_store_fixbits + (-10000)*C2_main_add157_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add157_CAST_store
castCostObj +=  + (1)*C2_main_add157_CAST_store
C3_main_add157_CAST_store = solver.IntVar(0, 1, 'C3_main_add157_CAST_store')
C4_main_add157_CAST_store = solver.IntVar(0, 1, 'C4_main_add157_CAST_store')
C5_main_add157_CAST_store = solver.IntVar(0, 1, 'C5_main_add157_CAST_store')
C6_main_add157_CAST_store = solver.IntVar(0, 1, 'C6_main_add157_CAST_store')
C7_main_add157_CAST_store = solver.IntVar(0, 1, 'C7_main_add157_CAST_store')
C8_main_add157_CAST_store = solver.IntVar(0, 1, 'C8_main_add157_CAST_store')
solver.Add( + (1)*main_add157_fixp + (1)*main_add157_CAST_store_float + (-1)*C3_main_add157_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add157_CAST_store
solver.Add( + (1)*main_add157_float + (1)*main_add157_CAST_store_fixp + (-1)*C4_main_add157_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add157_CAST_store
solver.Add( + (1)*main_add157_fixp + (1)*main_add157_CAST_store_double + (-1)*C5_main_add157_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add157_CAST_store
solver.Add( + (1)*main_add157_double + (1)*main_add157_CAST_store_fixp + (-1)*C6_main_add157_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add157_CAST_store
solver.Add( + (1)*main_add157_float + (1)*main_add157_CAST_store_double + (-1)*C7_main_add157_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add157_CAST_store
solver.Add( + (1)*main_add157_double + (1)*main_add157_CAST_store_float + (-1)*C8_main_add157_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add157_CAST_store
solver.Add( + (1)*D_fixp + (-1)*main_add157_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*D_float + (-1)*main_add157_CAST_store_float==0)    #float equality
solver.Add( + (1)*D_double + (-1)*main_add157_CAST_store_double==0)    #double equality
solver.Add( + (1)*D_fixbits + (-1)*main_add157_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
D_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'D_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*D_enob_storeENOB_storeENOB_storeENOB + (-1)*D_fixbits + (10000)*D_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*D_enob_storeENOB_storeENOB_storeENOB + (10000)*D_float<=10149)    #Enob constraint for float
solver.Add( + (1)*D_enob_storeENOB_storeENOB_storeENOB + (10000)*D_double<=11074)    #Enob constraint for double
solver.Add( + (1)*D_enob_storeENOB_storeENOB_storeENOB + (-1)*main_add157_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp3 + (-1)*D_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_8<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*D_enob_memphi_main_tmp6 + (-1)*D_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
D_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'D_enob_memphi_main_tmp9')
solver.Add( + (1)*D_enob_memphi_main_tmp9 + (-1)*D_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call184 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp8, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.6, i32 0, i32 0), double %tmp9), !taffo.info !12, !taffo.initweight !33, !taffo.constinfo !77
D_CAST_call184_fixbits = solver.IntVar(0, 16, 'D_CAST_call184_fixbits')
D_CAST_call184_fixp = solver.IntVar(0, 1, 'D_CAST_call184_fixp')
D_CAST_call184_float = solver.IntVar(0, 1, 'D_CAST_call184_float')
D_CAST_call184_double = solver.IntVar(0, 1, 'D_CAST_call184_double')
solver.Add( + (1)*D_CAST_call184_fixp + (1)*D_CAST_call184_float + (1)*D_CAST_call184_double==1)    #exactly 1 type
solver.Add( + (1)*D_CAST_call184_fixbits + (-10000)*D_CAST_call184_fixp<=0)    #If no fix, fix frac part = 0
C1_D_CAST_call184 = solver.IntVar(0, 1, 'C1_D_CAST_call184')
C2_D_CAST_call184 = solver.IntVar(0, 1, 'C2_D_CAST_call184')
solver.Add( + (1)*D_fixbits + (-1)*D_CAST_call184_fixbits + (-10000)*C1_D_CAST_call184<=0)    #Shift cost 1
solver.Add( + (-1)*D_fixbits + (1)*D_CAST_call184_fixbits + (-10000)*C2_D_CAST_call184<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_D_CAST_call184
castCostObj +=  + (1)*C2_D_CAST_call184
C3_D_CAST_call184 = solver.IntVar(0, 1, 'C3_D_CAST_call184')
C4_D_CAST_call184 = solver.IntVar(0, 1, 'C4_D_CAST_call184')
C5_D_CAST_call184 = solver.IntVar(0, 1, 'C5_D_CAST_call184')
C6_D_CAST_call184 = solver.IntVar(0, 1, 'C6_D_CAST_call184')
C7_D_CAST_call184 = solver.IntVar(0, 1, 'C7_D_CAST_call184')
C8_D_CAST_call184 = solver.IntVar(0, 1, 'C8_D_CAST_call184')
solver.Add( + (1)*D_fixp + (1)*D_CAST_call184_float + (-1)*C3_D_CAST_call184<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_D_CAST_call184
solver.Add( + (1)*D_float + (1)*D_CAST_call184_fixp + (-1)*C4_D_CAST_call184<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_D_CAST_call184
solver.Add( + (1)*D_fixp + (1)*D_CAST_call184_double + (-1)*C5_D_CAST_call184<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_D_CAST_call184
solver.Add( + (1)*D_double + (1)*D_CAST_call184_fixp + (-1)*C6_D_CAST_call184<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_D_CAST_call184
solver.Add( + (1)*D_float + (1)*D_CAST_call184_double + (-1)*C7_D_CAST_call184<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_D_CAST_call184
solver.Add( + (1)*D_double + (1)*D_CAST_call184_float + (-1)*C8_D_CAST_call184<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_D_CAST_call184
solver.Add( + (1)*D_CAST_call184_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 576.861+ 1 * enobCostObj / 12447+ 1000 * mathCostObj / 94.8451)

# Model declaration end.