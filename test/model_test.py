


#Stuff for @a = common dso_local global double 0.000000e+00, align 8, !taffo.initweight !0, !taffo.info !1
a_fixbits = solver.IntVar(0, 15, 'a_fixbits')
a_fixp = solver.IntVar(0, 1, 'a_fixp')
a_float = solver.IntVar(0, 1, 'a_float')
a_double = solver.IntVar(0, 1, 'a_double')
a_enob = solver.IntVar(-10000, 10000, 'a_enob')
solver.Add( + (1)*a_enob + (-1)*a_fixbits + (10000)*a_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*a_enob + (10000)*a_float<=10023)    #Enob constraint for float
solver.Add( + (1)*a_enob + (10000)*a_double<=10052)    #Enob constraint for double
solver.Add( + (1)*a_fixbits + (-10000)*a_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj =  + (-1)*a_enob
solver.Add( + (1)*a_fixp + (1)*a_float + (1)*a_double==1)    #Exactly one selected type
solver.Add( + (1)*a_fixbits + (-10000)*a_fixp<=0)    #If not fix, frac part to zero



#Stuff for @b = common dso_local global double 0.000000e+00, align 8, !taffo.initweight !0, !taffo.info !8
b_fixbits = solver.IntVar(0, 15, 'b_fixbits')
b_fixp = solver.IntVar(0, 1, 'b_fixp')
b_float = solver.IntVar(0, 1, 'b_float')
b_double = solver.IntVar(0, 1, 'b_double')
b_enob = solver.IntVar(-10000, 10000, 'b_enob')
solver.Add( + (1)*b_enob + (-1)*b_fixbits + (10000)*b_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*b_enob + (10000)*b_float<=10007)    #Enob constraint for float
solver.Add( + (1)*b_enob + (10000)*b_double<=10036)    #Enob constraint for double
solver.Add( + (1)*b_fixbits + (-10000)*b_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj +=  + (-1)*b_enob
solver.Add( + (1)*b_fixp + (1)*b_float + (1)*b_double==1)    #Exactly one selected type
solver.Add( + (1)*b_fixbits + (-10000)*b_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
b_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'b_enob_memphi_main_tmp2')
solver.Add( + (1)*b_enob_memphi_main_tmp2 + (-1)*b_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp4')
solver.Add( + (1)*a_enob_memphi_main_tmp4 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %add = fadd double %tmp4, %tmp2, !taffo.initweight !25, !taffo.info !26
a_CAST_add_fixbits = solver.IntVar(0, 15, 'a_CAST_add_fixbits')
a_CAST_add_fixp = solver.IntVar(0, 1, 'a_CAST_add_fixp')
a_CAST_add_float = solver.IntVar(0, 1, 'a_CAST_add_float')
a_CAST_add_double = solver.IntVar(0, 1, 'a_CAST_add_double')
solver.Add( + (1)*a_CAST_add_fixp + (1)*a_CAST_add_float + (1)*a_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_add_fixbits + (-10000)*a_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_add = solver.IntVar(0, 1, 'C1_a_CAST_add')
C2_a_CAST_add = solver.IntVar(0, 1, 'C2_a_CAST_add')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_add_fixbits + (-10000)*C1_a_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_add_fixbits + (-10000)*C2_a_CAST_add<=0)    #Shift cost 2
castCostObj =  + (1.13006)*C1_a_CAST_add
castCostObj +=  + (1.13006)*C2_a_CAST_add
C3_a_CAST_add = solver.IntVar(0, 1, 'C3_a_CAST_add')
C4_a_CAST_add = solver.IntVar(0, 1, 'C4_a_CAST_add')
C5_a_CAST_add = solver.IntVar(0, 1, 'C5_a_CAST_add')
C6_a_CAST_add = solver.IntVar(0, 1, 'C6_a_CAST_add')
C7_a_CAST_add = solver.IntVar(0, 1, 'C7_a_CAST_add')
C8_a_CAST_add = solver.IntVar(0, 1, 'C8_a_CAST_add')
solver.Add( + (1)*a_fixp + (1)*a_CAST_add_float + (-1)*C3_a_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_a_CAST_add
solver.Add( + (1)*a_float + (1)*a_CAST_add_fixp + (-1)*C4_a_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_a_CAST_add
solver.Add( + (1)*a_fixp + (1)*a_CAST_add_double + (-1)*C5_a_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_a_CAST_add
solver.Add( + (1)*a_double + (1)*a_CAST_add_fixp + (-1)*C6_a_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_a_CAST_add
solver.Add( + (1)*a_float + (1)*a_CAST_add_double + (-1)*C7_a_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7_a_CAST_add
solver.Add( + (1)*a_double + (1)*a_CAST_add_float + (-1)*C8_a_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_a_CAST_add



#Constraint for cast for   %add = fadd double %tmp4, %tmp2, !taffo.initweight !25, !taffo.info !26
b_CAST_add_fixbits = solver.IntVar(0, 15, 'b_CAST_add_fixbits')
b_CAST_add_fixp = solver.IntVar(0, 1, 'b_CAST_add_fixp')
b_CAST_add_float = solver.IntVar(0, 1, 'b_CAST_add_float')
b_CAST_add_double = solver.IntVar(0, 1, 'b_CAST_add_double')
solver.Add( + (1)*b_CAST_add_fixp + (1)*b_CAST_add_float + (1)*b_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*b_CAST_add_fixbits + (-10000)*b_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_b_CAST_add = solver.IntVar(0, 1, 'C1_b_CAST_add')
C2_b_CAST_add = solver.IntVar(0, 1, 'C2_b_CAST_add')
solver.Add( + (1)*b_fixbits + (-1)*b_CAST_add_fixbits + (-10000)*C1_b_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*b_fixbits + (1)*b_CAST_add_fixbits + (-10000)*C2_b_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_b_CAST_add
castCostObj +=  + (1.13006)*C2_b_CAST_add
C3_b_CAST_add = solver.IntVar(0, 1, 'C3_b_CAST_add')
C4_b_CAST_add = solver.IntVar(0, 1, 'C4_b_CAST_add')
C5_b_CAST_add = solver.IntVar(0, 1, 'C5_b_CAST_add')
C6_b_CAST_add = solver.IntVar(0, 1, 'C6_b_CAST_add')
C7_b_CAST_add = solver.IntVar(0, 1, 'C7_b_CAST_add')
C8_b_CAST_add = solver.IntVar(0, 1, 'C8_b_CAST_add')
solver.Add( + (1)*b_fixp + (1)*b_CAST_add_float + (-1)*C3_b_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_b_CAST_add
solver.Add( + (1)*b_float + (1)*b_CAST_add_fixp + (-1)*C4_b_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_b_CAST_add
solver.Add( + (1)*b_fixp + (1)*b_CAST_add_double + (-1)*C5_b_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_b_CAST_add
solver.Add( + (1)*b_double + (1)*b_CAST_add_fixp + (-1)*C6_b_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_b_CAST_add
solver.Add( + (1)*b_float + (1)*b_CAST_add_double + (-1)*C7_b_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7_b_CAST_add
solver.Add( + (1)*b_double + (1)*b_CAST_add_float + (-1)*C8_b_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_b_CAST_add



#Stuff for   %add = fadd double %tmp4, %tmp2, !taffo.initweight !25, !taffo.info !26
main_add_fixbits = solver.IntVar(0, 15, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
main_add_enob = solver.IntVar(-10000, 10000, 'main_add_enob')
solver.Add( + (1)*main_add_enob + (-1)*main_add_fixbits + (10000)*main_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add_enob + (10000)*main_add_float<=10007)    #Enob constraint for float
solver.Add( + (1)*main_add_enob + (10000)*main_add_double<=10036)    #Enob constraint for double
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj +=  + (-1)*main_add_enob
solver.Add( + (1)*main_add_fixp + (1)*main_add_float + (1)*main_add_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*a_CAST_add_fixp + (-1)*b_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_add_float + (-1)*b_CAST_add_float==0)    #float equality
solver.Add( + (1)*a_CAST_add_double + (-1)*b_CAST_add_double==0)    #double equality
solver.Add( + (1)*a_CAST_add_fixbits + (-1)*b_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*a_CAST_add_fixp + (-1)*main_add_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_add_float + (-1)*main_add_float==0)    #float equality
solver.Add( + (1)*a_CAST_add_double + (-1)*main_add_double==0)    #double equality
solver.Add( + (1)*a_CAST_add_fixbits + (-1)*main_add_fixbits==0)    #same fractional bit
mathCostObj =  + (1.30379)*main_add_fixp
mathCostObj +=  + (1.80596)*main_add_float
mathCostObj +=  + (2.15411)*main_add_double
solver.Add( + (1)*main_add_enob + (-1)*a_enob_memphi_main_tmp4<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*b_enob_memphi_main_tmp2<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add, double* %tmp3, align 8, !taffo.initweight !28, !taffo.info !8
main_add_CAST_store_fixbits = solver.IntVar(0, 15, 'main_add_CAST_store_fixbits')
main_add_CAST_store_fixp = solver.IntVar(0, 1, 'main_add_CAST_store_fixp')
main_add_CAST_store_float = solver.IntVar(0, 1, 'main_add_CAST_store_float')
main_add_CAST_store_double = solver.IntVar(0, 1, 'main_add_CAST_store_double')
solver.Add( + (1)*main_add_CAST_store_fixp + (1)*main_add_CAST_store_float + (1)*main_add_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add_CAST_store_fixbits + (-10000)*main_add_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add_CAST_store = solver.IntVar(0, 1, 'C1_main_add_CAST_store')
C2_main_add_CAST_store = solver.IntVar(0, 1, 'C2_main_add_CAST_store')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add_CAST_store_fixbits + (-10000)*C1_main_add_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add_fixbits + (1)*main_add_CAST_store_fixbits + (-10000)*C2_main_add_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_main_add_CAST_store
castCostObj +=  + (1.13006)*C2_main_add_CAST_store
C3_main_add_CAST_store = solver.IntVar(0, 1, 'C3_main_add_CAST_store')
C4_main_add_CAST_store = solver.IntVar(0, 1, 'C4_main_add_CAST_store')
C5_main_add_CAST_store = solver.IntVar(0, 1, 'C5_main_add_CAST_store')
C6_main_add_CAST_store = solver.IntVar(0, 1, 'C6_main_add_CAST_store')
C7_main_add_CAST_store = solver.IntVar(0, 1, 'C7_main_add_CAST_store')
C8_main_add_CAST_store = solver.IntVar(0, 1, 'C8_main_add_CAST_store')
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_float + (-1)*C3_main_add_CAST_store<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_fixp + (-1)*C4_main_add_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_main_add_CAST_store
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_store_double + (-1)*C5_main_add_CAST_store<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_fixp + (-1)*C6_main_add_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_main_add_CAST_store
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_store_double + (-1)*C7_main_add_CAST_store<=1)    #Float to double
castCostObj +=  + (1)*C7_main_add_CAST_store
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_store_float + (-1)*C8_main_add_CAST_store<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_main_add_CAST_store
solver.Add( + (1)*a_fixp + (-1)*main_add_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*a_float + (-1)*main_add_CAST_store_float==0)    #float equality
solver.Add( + (1)*a_double + (-1)*main_add_CAST_store_double==0)    #double equality
solver.Add( + (1)*a_fixbits + (-1)*main_add_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
a_enob_storeENOB = solver.IntVar(-10000, 10000, 'a_enob_storeENOB')
solver.Add( + (1)*a_enob_storeENOB + (-1)*a_fixbits + (10000)*a_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*a_enob_storeENOB + (10000)*a_float<=10023)    #Enob constraint for float
solver.Add( + (1)*a_enob_storeENOB + (10000)*a_double<=10052)    #Enob constraint for double
solver.Add( + (1)*a_enob_storeENOB + (-1)*main_add_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp5')
solver.Add( + (1)*a_enob_memphi_main_tmp5 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp5_enob_0 = solver.IntVar(0, 1, 'main_main_tmp5_enob_0')
solver.Add( + (1)*main_main_tmp5_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp5 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp5_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp7')
solver.Add( + (1)*a_enob_memphi_main_tmp7 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_0 = solver.IntVar(0, 1, 'main_main_tmp7_enob_0')
solver.Add( + (1)*main_main_tmp7_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp7 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp7_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([23 x i8], [23 x i8]* @.str.2, i32 0, i32 0), double %tmp5, double %tmp7), !taffo.initweight !25, !taffo.info !20, !taffo.constinfo !29
a_CAST_call2_fixbits = solver.IntVar(0, 15, 'a_CAST_call2_fixbits')
a_CAST_call2_fixp = solver.IntVar(0, 1, 'a_CAST_call2_fixp')
a_CAST_call2_float = solver.IntVar(0, 1, 'a_CAST_call2_float')
a_CAST_call2_double = solver.IntVar(0, 1, 'a_CAST_call2_double')
solver.Add( + (1)*a_CAST_call2_fixp + (1)*a_CAST_call2_float + (1)*a_CAST_call2_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_call2_fixbits + (-10000)*a_CAST_call2_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_call2 = solver.IntVar(0, 1, 'C1_a_CAST_call2')
C2_a_CAST_call2 = solver.IntVar(0, 1, 'C2_a_CAST_call2')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_call2_fixbits + (-10000)*C1_a_CAST_call2<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_call2_fixbits + (-10000)*C2_a_CAST_call2<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_a_CAST_call2
castCostObj +=  + (1.13006)*C2_a_CAST_call2
C3_a_CAST_call2 = solver.IntVar(0, 1, 'C3_a_CAST_call2')
C4_a_CAST_call2 = solver.IntVar(0, 1, 'C4_a_CAST_call2')
C5_a_CAST_call2 = solver.IntVar(0, 1, 'C5_a_CAST_call2')
C6_a_CAST_call2 = solver.IntVar(0, 1, 'C6_a_CAST_call2')
C7_a_CAST_call2 = solver.IntVar(0, 1, 'C7_a_CAST_call2')
C8_a_CAST_call2 = solver.IntVar(0, 1, 'C8_a_CAST_call2')
solver.Add( + (1)*a_fixp + (1)*a_CAST_call2_float + (-1)*C3_a_CAST_call2<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_a_CAST_call2
solver.Add( + (1)*a_float + (1)*a_CAST_call2_fixp + (-1)*C4_a_CAST_call2<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_a_CAST_call2
solver.Add( + (1)*a_fixp + (1)*a_CAST_call2_double + (-1)*C5_a_CAST_call2<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_a_CAST_call2
solver.Add( + (1)*a_double + (1)*a_CAST_call2_fixp + (-1)*C6_a_CAST_call2<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_a_CAST_call2
solver.Add( + (1)*a_float + (1)*a_CAST_call2_double + (-1)*C7_a_CAST_call2<=1)    #Float to double
castCostObj +=  + (1)*C7_a_CAST_call2
solver.Add( + (1)*a_double + (1)*a_CAST_call2_float + (-1)*C8_a_CAST_call2<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_a_CAST_call2
solver.Add( + (1)*a_CAST_call2_double==1)    #Type constraint for argument value



#Constraint for cast for   %call2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([23 x i8], [23 x i8]* @.str.2, i32 0, i32 0), double %tmp5, double %tmp7), !taffo.initweight !25, !taffo.info !20, !taffo.constinfo !29
a_CAST_call2_0_fixbits = solver.IntVar(0, 15, 'a_CAST_call2_0_fixbits')
a_CAST_call2_0_fixp = solver.IntVar(0, 1, 'a_CAST_call2_0_fixp')
a_CAST_call2_0_float = solver.IntVar(0, 1, 'a_CAST_call2_0_float')
a_CAST_call2_0_double = solver.IntVar(0, 1, 'a_CAST_call2_0_double')
solver.Add( + (1)*a_CAST_call2_0_fixp + (1)*a_CAST_call2_0_float + (1)*a_CAST_call2_0_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_call2_0_fixbits + (-10000)*a_CAST_call2_0_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_call2_0 = solver.IntVar(0, 1, 'C1_a_CAST_call2_0')
C2_a_CAST_call2_0 = solver.IntVar(0, 1, 'C2_a_CAST_call2_0')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_call2_0_fixbits + (-10000)*C1_a_CAST_call2_0<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_call2_0_fixbits + (-10000)*C2_a_CAST_call2_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_a_CAST_call2_0
castCostObj +=  + (1.13006)*C2_a_CAST_call2_0
C3_a_CAST_call2_0 = solver.IntVar(0, 1, 'C3_a_CAST_call2_0')
C4_a_CAST_call2_0 = solver.IntVar(0, 1, 'C4_a_CAST_call2_0')
C5_a_CAST_call2_0 = solver.IntVar(0, 1, 'C5_a_CAST_call2_0')
C6_a_CAST_call2_0 = solver.IntVar(0, 1, 'C6_a_CAST_call2_0')
C7_a_CAST_call2_0 = solver.IntVar(0, 1, 'C7_a_CAST_call2_0')
C8_a_CAST_call2_0 = solver.IntVar(0, 1, 'C8_a_CAST_call2_0')
solver.Add( + (1)*a_fixp + (1)*a_CAST_call2_0_float + (-1)*C3_a_CAST_call2_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_a_CAST_call2_0
solver.Add( + (1)*a_float + (1)*a_CAST_call2_0_fixp + (-1)*C4_a_CAST_call2_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_a_CAST_call2_0
solver.Add( + (1)*a_fixp + (1)*a_CAST_call2_0_double + (-1)*C5_a_CAST_call2_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_a_CAST_call2_0
solver.Add( + (1)*a_double + (1)*a_CAST_call2_0_fixp + (-1)*C6_a_CAST_call2_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_a_CAST_call2_0
solver.Add( + (1)*a_float + (1)*a_CAST_call2_0_double + (-1)*C7_a_CAST_call2_0<=1)    #Float to double
castCostObj +=  + (1)*C7_a_CAST_call2_0
solver.Add( + (1)*a_double + (1)*a_CAST_call2_0_float + (-1)*C8_a_CAST_call2_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_a_CAST_call2_0
solver.Add( + (1)*a_CAST_call2_0_double==1)    #Type constraint for argument value



#Stuff for   %call3 = call double @resolvePointer.1(double* %tmp8), !taffo.initweight !0, !taffo.info !1, !taffo.constinfo !22, !taffo.originalCall !30
main_call3_fixbits = solver.IntVar(0, 15, 'main_call3_fixbits')
main_call3_fixp = solver.IntVar(0, 1, 'main_call3_fixp')
main_call3_float = solver.IntVar(0, 1, 'main_call3_float')
main_call3_double = solver.IntVar(0, 1, 'main_call3_double')
main_call3_enob = solver.IntVar(-10000, 10000, 'main_call3_enob')
solver.Add( + (1)*main_call3_enob + (-1)*main_call3_fixbits + (10000)*main_call3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call3_enob + (10000)*main_call3_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_call3_enob + (10000)*main_call3_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_call3_fixbits + (-10000)*main_call3_fixp>=-9986)    #Limit the lower number of frac bits15
enobCostObj +=  + (-1)*main_call3_enob
solver.Add( + (1)*main_call3_fixp + (1)*main_call3_float + (1)*main_call3_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call3_fixbits + (-10000)*main_call3_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
a_enob_memphi_resolvePointer_1_tmp = solver.IntVar(-10000, 10000, 'a_enob_memphi_resolvePointer_1_tmp')
solver.Add( + (1)*a_enob_memphi_resolvePointer_1_tmp + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   ret double %tmp
a_CAST_ret_fixbits = solver.IntVar(0, 15, 'a_CAST_ret_fixbits')
a_CAST_ret_fixp = solver.IntVar(0, 1, 'a_CAST_ret_fixp')
a_CAST_ret_float = solver.IntVar(0, 1, 'a_CAST_ret_float')
a_CAST_ret_double = solver.IntVar(0, 1, 'a_CAST_ret_double')
solver.Add( + (1)*a_CAST_ret_fixp + (1)*a_CAST_ret_float + (1)*a_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_ret_fixbits + (-10000)*a_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_ret = solver.IntVar(0, 1, 'C1_a_CAST_ret')
C2_a_CAST_ret = solver.IntVar(0, 1, 'C2_a_CAST_ret')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_ret_fixbits + (-10000)*C1_a_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_ret_fixbits + (-10000)*C2_a_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_a_CAST_ret
castCostObj +=  + (1.13006)*C2_a_CAST_ret
C3_a_CAST_ret = solver.IntVar(0, 1, 'C3_a_CAST_ret')
C4_a_CAST_ret = solver.IntVar(0, 1, 'C4_a_CAST_ret')
C5_a_CAST_ret = solver.IntVar(0, 1, 'C5_a_CAST_ret')
C6_a_CAST_ret = solver.IntVar(0, 1, 'C6_a_CAST_ret')
C7_a_CAST_ret = solver.IntVar(0, 1, 'C7_a_CAST_ret')
C8_a_CAST_ret = solver.IntVar(0, 1, 'C8_a_CAST_ret')
solver.Add( + (1)*a_fixp + (1)*a_CAST_ret_float + (-1)*C3_a_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_a_CAST_ret
solver.Add( + (1)*a_float + (1)*a_CAST_ret_fixp + (-1)*C4_a_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_a_CAST_ret
solver.Add( + (1)*a_fixp + (1)*a_CAST_ret_double + (-1)*C5_a_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_a_CAST_ret
solver.Add( + (1)*a_double + (1)*a_CAST_ret_fixp + (-1)*C6_a_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_a_CAST_ret
solver.Add( + (1)*a_float + (1)*a_CAST_ret_double + (-1)*C7_a_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7_a_CAST_ret
solver.Add( + (1)*a_double + (1)*a_CAST_ret_float + (-1)*C8_a_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_a_CAST_ret
solver.Add( + (1)*main_call3_fixp + (-1)*a_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*main_call3_float + (-1)*a_CAST_ret_float==0)    #float equality
solver.Add( + (1)*main_call3_double + (-1)*a_CAST_ret_double==0)    #double equality
solver.Add( + (1)*main_call3_fixbits + (-1)*a_CAST_ret_fixbits==0)    #same fractional bit





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 35.4355+ 1 * enobCostObj / 176+ 1000 * mathCostObj / 2.15411)

# Model declaration end.