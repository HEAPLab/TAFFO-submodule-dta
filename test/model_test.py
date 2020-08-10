


#Stuff for @sptprice = dso_local global float* null, align 8, !taffo.info !3, !taffo.initweight !6
sptprice_fixbits = solver.IntVar(0, 31, 'sptprice_fixbits')
sptprice_fixp = solver.IntVar(0, 1, 'sptprice_fixp')
sptprice_float = solver.IntVar(0, 1, 'sptprice_float')
sptprice_double = solver.IntVar(0, 1, 'sptprice_double')
sptprice_enob = solver.IntVar(-10000, 10000, 'sptprice_enob')
solver.Add( + (1)*sptprice_enob + (-1)*sptprice_fixbits + (10000)*sptprice_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*sptprice_enob + (10000)*sptprice_float<=10025)    #Enob constraint for float
solver.Add( + (1)*sptprice_enob + (10000)*sptprice_double<=10054)    #Enob constraint for double
solver.Add( + (1)*sptprice_fixbits + (-10000)*sptprice_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*sptprice_enob<=27)    #Enob constraint for error maximal
enobCostObj =  + (-1)*sptprice_enob
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_float + (1)*sptprice_double==1)    #Exactly one selected type
solver.Add( + (1)*sptprice_fixbits + (-10000)*sptprice_fixp<=0)    #If not fix, frac part to zero



#Stuff for @strike = dso_local global float* null, align 8, !taffo.info !3, !taffo.initweight !6
strike_fixbits = solver.IntVar(0, 31, 'strike_fixbits')
strike_fixp = solver.IntVar(0, 1, 'strike_fixp')
strike_float = solver.IntVar(0, 1, 'strike_float')
strike_double = solver.IntVar(0, 1, 'strike_double')
strike_enob = solver.IntVar(-10000, 10000, 'strike_enob')
solver.Add( + (1)*strike_enob + (-1)*strike_fixbits + (10000)*strike_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*strike_enob + (10000)*strike_float<=10025)    #Enob constraint for float
solver.Add( + (1)*strike_enob + (10000)*strike_double<=10054)    #Enob constraint for double
solver.Add( + (1)*strike_fixbits + (-10000)*strike_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*strike_enob<=27)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*strike_enob
solver.Add( + (1)*strike_fixp + (1)*strike_float + (1)*strike_double==1)    #Exactly one selected type
solver.Add( + (1)*strike_fixbits + (-10000)*strike_fixp<=0)    #If not fix, frac part to zero



#Stuff for @rate = dso_local global float* null, align 8, !taffo.info !3, !taffo.initweight !6
rate_fixbits = solver.IntVar(0, 31, 'rate_fixbits')
rate_fixp = solver.IntVar(0, 1, 'rate_fixp')
rate_float = solver.IntVar(0, 1, 'rate_float')
rate_double = solver.IntVar(0, 1, 'rate_double')
rate_enob = solver.IntVar(-10000, 10000, 'rate_enob')
solver.Add( + (1)*rate_enob + (-1)*rate_fixbits + (10000)*rate_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*rate_enob + (10000)*rate_float<=10025)    #Enob constraint for float
solver.Add( + (1)*rate_enob + (10000)*rate_double<=10054)    #Enob constraint for double
solver.Add( + (1)*rate_fixbits + (-10000)*rate_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*rate_enob<=27)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*rate_enob
solver.Add( + (1)*rate_fixp + (1)*rate_float + (1)*rate_double==1)    #Exactly one selected type
solver.Add( + (1)*rate_fixbits + (-10000)*rate_fixp<=0)    #If not fix, frac part to zero



#Stuff for @volatility = dso_local global float* null, align 8, !taffo.info !3, !taffo.initweight !6
volatility_fixbits = solver.IntVar(0, 31, 'volatility_fixbits')
volatility_fixp = solver.IntVar(0, 1, 'volatility_fixp')
volatility_float = solver.IntVar(0, 1, 'volatility_float')
volatility_double = solver.IntVar(0, 1, 'volatility_double')
volatility_enob = solver.IntVar(-10000, 10000, 'volatility_enob')
solver.Add( + (1)*volatility_enob + (-1)*volatility_fixbits + (10000)*volatility_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*volatility_enob + (10000)*volatility_float<=10025)    #Enob constraint for float
solver.Add( + (1)*volatility_enob + (10000)*volatility_double<=10054)    #Enob constraint for double
solver.Add( + (1)*volatility_fixbits + (-10000)*volatility_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*volatility_enob<=27)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*volatility_enob
solver.Add( + (1)*volatility_fixp + (1)*volatility_float + (1)*volatility_double==1)    #Exactly one selected type
solver.Add( + (1)*volatility_fixbits + (-10000)*volatility_fixp<=0)    #If not fix, frac part to zero



#Stuff for @otime = dso_local global float* null, align 8, !taffo.info !3, !taffo.initweight !6
otime_fixbits = solver.IntVar(0, 31, 'otime_fixbits')
otime_fixp = solver.IntVar(0, 1, 'otime_fixp')
otime_float = solver.IntVar(0, 1, 'otime_float')
otime_double = solver.IntVar(0, 1, 'otime_double')
otime_enob = solver.IntVar(-10000, 10000, 'otime_enob')
solver.Add( + (1)*otime_enob + (-1)*otime_fixbits + (10000)*otime_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*otime_enob + (10000)*otime_float<=10025)    #Enob constraint for float
solver.Add( + (1)*otime_enob + (10000)*otime_double<=10054)    #Enob constraint for double
solver.Add( + (1)*otime_fixbits + (-10000)*otime_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*otime_enob<=27)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*otime_enob
solver.Add( + (1)*otime_fixp + (1)*otime_float + (1)*otime_double==1)    #Exactly one selected type
solver.Add( + (1)*otime_fixbits + (-10000)*otime_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.200000e+02
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



#Stuff for double 1.200000e+02
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



#Stuff for double 1.200000e+02
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



#Stuff for double 1.200000e+02
ConstantValue__2_fixbits = solver.IntVar(0, 25, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10017)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10046)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %N1 = alloca float, align 4, !taffo.info !26, !taffo.initweight !6
_Z9bs_threadPv_N1_fixbits = solver.IntVar(0, 29, '_Z9bs_threadPv_N1_fixbits')
_Z9bs_threadPv_N1_fixp = solver.IntVar(0, 1, '_Z9bs_threadPv_N1_fixp')
_Z9bs_threadPv_N1_float = solver.IntVar(0, 1, '_Z9bs_threadPv_N1_float')
_Z9bs_threadPv_N1_double = solver.IntVar(0, 1, '_Z9bs_threadPv_N1_double')
_Z9bs_threadPv_N1_enob = solver.IntVar(-10000, 10000, '_Z9bs_threadPv_N1_enob')
solver.Add( + (1)*_Z9bs_threadPv_N1_enob + (-1)*_Z9bs_threadPv_N1_fixbits + (10000)*_Z9bs_threadPv_N1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z9bs_threadPv_N1_enob + (10000)*_Z9bs_threadPv_N1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z9bs_threadPv_N1_enob + (10000)*_Z9bs_threadPv_N1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z9bs_threadPv_N1_fixbits + (-10000)*_Z9bs_threadPv_N1_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z9bs_threadPv_N1_enob
solver.Add( + (1)*_Z9bs_threadPv_N1_fixp + (1)*_Z9bs_threadPv_N1_float + (1)*_Z9bs_threadPv_N1_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z9bs_threadPv_N1_fixbits + (-10000)*_Z9bs_threadPv_N1_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %N2 = alloca float, align 4, !taffo.info !26, !taffo.initweight !6
_Z9bs_threadPv_N2_fixbits = solver.IntVar(0, 29, '_Z9bs_threadPv_N2_fixbits')
_Z9bs_threadPv_N2_fixp = solver.IntVar(0, 1, '_Z9bs_threadPv_N2_fixp')
_Z9bs_threadPv_N2_float = solver.IntVar(0, 1, '_Z9bs_threadPv_N2_float')
_Z9bs_threadPv_N2_double = solver.IntVar(0, 1, '_Z9bs_threadPv_N2_double')
_Z9bs_threadPv_N2_enob = solver.IntVar(-10000, 10000, '_Z9bs_threadPv_N2_enob')
solver.Add( + (1)*_Z9bs_threadPv_N2_enob + (-1)*_Z9bs_threadPv_N2_fixbits + (10000)*_Z9bs_threadPv_N2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z9bs_threadPv_N2_enob + (10000)*_Z9bs_threadPv_N2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z9bs_threadPv_N2_enob + (10000)*_Z9bs_threadPv_N2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z9bs_threadPv_N2_fixbits + (-10000)*_Z9bs_threadPv_N2_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z9bs_threadPv_N2_enob
solver.Add( + (1)*_Z9bs_threadPv_N2_fixp + (1)*_Z9bs_threadPv_N2_float + (1)*_Z9bs_threadPv_N2_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z9bs_threadPv_N2_fixbits + (-10000)*_Z9bs_threadPv_N2_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
sptprice_enob_memphi__Z9bs_threadPv_tmp5 = solver.IntVar(-10000, 10000, 'sptprice_enob_memphi__Z9bs_threadPv_tmp5')
solver.Add( + (1)*sptprice_enob_memphi__Z9bs_threadPv_tmp5 + (-1)*sptprice_enob<=0)    #Enob constraint, new enob at most original variable enob
_Z9bs_threadPv__Z9bs_threadPv_tmp5_enob_1 = solver.IntVar(0, 1, '_Z9bs_threadPv__Z9bs_threadPv_tmp5_enob_1')
solver.Add( + (1)*_Z9bs_threadPv__Z9bs_threadPv_tmp5_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
sptprice_enob_memphi__Z9bs_threadPv_tmp7 = solver.IntVar(-10000, 10000, 'sptprice_enob_memphi__Z9bs_threadPv_tmp7')
solver.Add( + (1)*sptprice_enob_memphi__Z9bs_threadPv_tmp7 + (-1)*sptprice_enob<=0)    #Enob constraint, new enob at most original variable enob
_Z9bs_threadPv__Z9bs_threadPv_tmp7_enob_1 = solver.IntVar(0, 1, '_Z9bs_threadPv__Z9bs_threadPv_tmp7_enob_1')
solver.Add( + (1)*_Z9bs_threadPv__Z9bs_threadPv_tmp7_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
sptprice_enob_memphi__Z9bs_threadPv_tmp9 = solver.IntVar(-10000, 10000, 'sptprice_enob_memphi__Z9bs_threadPv_tmp9')
solver.Add( + (1)*sptprice_enob_memphi__Z9bs_threadPv_tmp9 + (-1)*sptprice_enob<=0)    #Enob constraint, new enob at most original variable enob
_Z9bs_threadPv__Z9bs_threadPv_tmp9_enob_1 = solver.IntVar(0, 1, '_Z9bs_threadPv__Z9bs_threadPv_tmp9_enob_1')
solver.Add( + (1)*_Z9bs_threadPv__Z9bs_threadPv_tmp9_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
sptprice_enob_memphi__Z9bs_threadPv_tmp11 = solver.IntVar(-10000, 10000, 'sptprice_enob_memphi__Z9bs_threadPv_tmp11')
solver.Add( + (1)*sptprice_enob_memphi__Z9bs_threadPv_tmp11 + (-1)*sptprice_enob<=0)    #Enob constraint, new enob at most original variable enob
_Z9bs_threadPv__Z9bs_threadPv_tmp11_enob_1 = solver.IntVar(0, 1, '_Z9bs_threadPv__Z9bs_threadPv_tmp11_enob_1')
solver.Add( + (1)*_Z9bs_threadPv__Z9bs_threadPv_tmp11_enob_1==1)    #Enob: one selected constraint

#Restriction for new enob [LOAD]
sptprice_enob_memphi__Z9bs_threadPv_tmp13 = solver.IntVar(-10000, 10000, 'sptprice_enob_memphi__Z9bs_threadPv_tmp13')
solver.Add( + (1)*sptprice_enob_memphi__Z9bs_threadPv_tmp13 + (-1)*sptprice_enob<=0)    #Enob constraint, new enob at most original variable enob
_Z9bs_threadPv__Z9bs_threadPv_tmp13_enob_1 = solver.IntVar(0, 1, '_Z9bs_threadPv__Z9bs_threadPv_tmp13_enob_1')
solver.Add( + (1)*_Z9bs_threadPv__Z9bs_threadPv_tmp13_enob_1==1)    #Enob: one selected constraint



#Stuff for float 0.000000e+00
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



#Stuff for   %call = call float @_Z19BlkSchlsEqEuroNoDivfffffifPfS_.5(float %tmp5, float %tmp7, float %tmp9, float %tmp11, float %tmp13, i32 %tmp15, float 0.000000e+00, float* %N1, float* %N2), !taffo.info !47, !taffo.initweight !32, !taffo.constinfo !49, !taffo.originalCall !50
_Z9bs_threadPv_call_fixbits = solver.IntVar(0, 30, '_Z9bs_threadPv_call_fixbits')
_Z9bs_threadPv_call_fixp = solver.IntVar(0, 1, '_Z9bs_threadPv_call_fixp')
_Z9bs_threadPv_call_float = solver.IntVar(0, 1, '_Z9bs_threadPv_call_float')
_Z9bs_threadPv_call_double = solver.IntVar(0, 1, '_Z9bs_threadPv_call_double')
_Z9bs_threadPv_call_enob = solver.IntVar(-10000, 10000, '_Z9bs_threadPv_call_enob')
solver.Add( + (1)*_Z9bs_threadPv_call_enob + (-1)*_Z9bs_threadPv_call_fixbits + (10000)*_Z9bs_threadPv_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z9bs_threadPv_call_enob + (10000)*_Z9bs_threadPv_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z9bs_threadPv_call_enob + (10000)*_Z9bs_threadPv_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z9bs_threadPv_call_fixbits + (-10000)*_Z9bs_threadPv_call_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z9bs_threadPv_call_enob
solver.Add( + (1)*_Z9bs_threadPv_call_fixp + (1)*_Z9bs_threadPv_call_float + (1)*_Z9bs_threadPv_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z9bs_threadPv_call_fixbits + (-10000)*_Z9bs_threadPv_call_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call = call float @_ZSt4sqrtf.1.12(float %time), !taffo.info !37, !taffo.initweight !39, !taffo.constinfo !40, !taffo.originalCall !41
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_float<=10026)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_double<=10055)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call = call float @sqrtf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_ZSt4sqrtf_1_12_call_fixbits = solver.IntVar(0, 31, '_ZSt4sqrtf_1_12_call_fixbits')
_ZSt4sqrtf_1_12_call_fixp = solver.IntVar(0, 1, '_ZSt4sqrtf_1_12_call_fixp')
_ZSt4sqrtf_1_12_call_float = solver.IntVar(0, 1, '_ZSt4sqrtf_1_12_call_float')
_ZSt4sqrtf_1_12_call_double = solver.IntVar(0, 1, '_ZSt4sqrtf_1_12_call_double')
_ZSt4sqrtf_1_12_call_enob = solver.IntVar(-10000, 10000, '_ZSt4sqrtf_1_12_call_enob')
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_enob + (-1)*_ZSt4sqrtf_1_12_call_fixbits + (10000)*_ZSt4sqrtf_1_12_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_enob + (10000)*_ZSt4sqrtf_1_12_call_float<=10026)    #Enob constraint for float
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_enob + (10000)*_ZSt4sqrtf_1_12_call_double<=10055)    #Enob constraint for double
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_fixbits + (-10000)*_ZSt4sqrtf_1_12_call_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_ZSt4sqrtf_1_12_call_enob
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_fixp + (1)*_ZSt4sqrtf_1_12_call_float + (1)*_ZSt4sqrtf_1_12_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_fixbits + (-10000)*_ZSt4sqrtf_1_12_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_float==1)    #Type constraint for return value



#Constraint for cast for   %call = call float @sqrtf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
sptprice_CAST_call_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_call_fixbits')
sptprice_CAST_call_fixp = solver.IntVar(0, 1, 'sptprice_CAST_call_fixp')
sptprice_CAST_call_float = solver.IntVar(0, 1, 'sptprice_CAST_call_float')
sptprice_CAST_call_double = solver.IntVar(0, 1, 'sptprice_CAST_call_double')
solver.Add( + (1)*sptprice_CAST_call_fixp + (1)*sptprice_CAST_call_float + (1)*sptprice_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_call_fixbits + (-10000)*sptprice_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_call = solver.IntVar(0, 1, 'C1_sptprice_CAST_call')
C2_sptprice_CAST_call = solver.IntVar(0, 1, 'C2_sptprice_CAST_call')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_call_fixbits + (-10000)*C1_sptprice_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_call_fixbits + (-10000)*C2_sptprice_CAST_call<=0)    #Shift cost 2
castCostObj =  + (1.13006)*C1_sptprice_CAST_call
castCostObj +=  + (1.13006)*C2_sptprice_CAST_call
C3_sptprice_CAST_call = solver.IntVar(0, 1, 'C3_sptprice_CAST_call')
C4_sptprice_CAST_call = solver.IntVar(0, 1, 'C4_sptprice_CAST_call')
C5_sptprice_CAST_call = solver.IntVar(0, 1, 'C5_sptprice_CAST_call')
C6_sptprice_CAST_call = solver.IntVar(0, 1, 'C6_sptprice_CAST_call')
C7_sptprice_CAST_call = solver.IntVar(0, 1, 'C7_sptprice_CAST_call')
C8_sptprice_CAST_call = solver.IntVar(0, 1, 'C8_sptprice_CAST_call')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_call_float + (-1)*C3_sptprice_CAST_call<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_call
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_call_fixp + (-1)*C4_sptprice_CAST_call<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_call
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_call_double + (-1)*C5_sptprice_CAST_call<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_call
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_call_fixp + (-1)*C6_sptprice_CAST_call<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_call
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_call_double + (-1)*C7_sptprice_CAST_call<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_call
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_call_float + (-1)*C8_sptprice_CAST_call<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_call
solver.Add( + (1)*sptprice_CAST_call_float==1)    #Type constraint for argument value



#Constraint for cast for   ret float %call, !taffo.info !32, !taffo.initweight !33
_ZSt4sqrtf_1_12_call_CAST_ret_fixbits = solver.IntVar(0, 31, '_ZSt4sqrtf_1_12_call_CAST_ret_fixbits')
_ZSt4sqrtf_1_12_call_CAST_ret_fixp = solver.IntVar(0, 1, '_ZSt4sqrtf_1_12_call_CAST_ret_fixp')
_ZSt4sqrtf_1_12_call_CAST_ret_float = solver.IntVar(0, 1, '_ZSt4sqrtf_1_12_call_CAST_ret_float')
_ZSt4sqrtf_1_12_call_CAST_ret_double = solver.IntVar(0, 1, '_ZSt4sqrtf_1_12_call_CAST_ret_double')
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixp + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_float + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixbits + (-10000)*_ZSt4sqrtf_1_12_call_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C1__ZSt4sqrtf_1_12_call_CAST_ret')
C2__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C2__ZSt4sqrtf_1_12_call_CAST_ret')
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_fixbits + (-1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixbits + (-10000)*C1__ZSt4sqrtf_1_12_call_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_ZSt4sqrtf_1_12_call_fixbits + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixbits + (-10000)*C2__ZSt4sqrtf_1_12_call_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__ZSt4sqrtf_1_12_call_CAST_ret
castCostObj +=  + (1.13006)*C2__ZSt4sqrtf_1_12_call_CAST_ret
C3__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C3__ZSt4sqrtf_1_12_call_CAST_ret')
C4__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C4__ZSt4sqrtf_1_12_call_CAST_ret')
C5__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C5__ZSt4sqrtf_1_12_call_CAST_ret')
C6__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C6__ZSt4sqrtf_1_12_call_CAST_ret')
C7__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C7__ZSt4sqrtf_1_12_call_CAST_ret')
C8__ZSt4sqrtf_1_12_call_CAST_ret = solver.IntVar(0, 1, 'C8__ZSt4sqrtf_1_12_call_CAST_ret')
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_fixp + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_float + (-1)*C3__ZSt4sqrtf_1_12_call_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__ZSt4sqrtf_1_12_call_CAST_ret
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_float + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixp + (-1)*C4__ZSt4sqrtf_1_12_call_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__ZSt4sqrtf_1_12_call_CAST_ret
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_fixp + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_double + (-1)*C5__ZSt4sqrtf_1_12_call_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__ZSt4sqrtf_1_12_call_CAST_ret
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_double + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixp + (-1)*C6__ZSt4sqrtf_1_12_call_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__ZSt4sqrtf_1_12_call_CAST_ret
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_float + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_double + (-1)*C7__ZSt4sqrtf_1_12_call_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__ZSt4sqrtf_1_12_call_CAST_ret
solver.Add( + (1)*_ZSt4sqrtf_1_12_call_double + (1)*_ZSt4sqrtf_1_12_call_CAST_ret_float + (-1)*C8__ZSt4sqrtf_1_12_call_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__ZSt4sqrtf_1_12_call_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp + (-1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_float + (-1)*_ZSt4sqrtf_1_12_call_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_double + (-1)*_ZSt4sqrtf_1_12_call_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits + (-1)*_ZSt4sqrtf_1_12_call_CAST_ret_fixbits==0)    #same fractional bit



#Constraint for cast for   %div = fdiv float %sptprice, %strike, !taffo.info !42, !taffo.initweight !39
sptprice_CAST_div_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_div_fixbits')
sptprice_CAST_div_fixp = solver.IntVar(0, 1, 'sptprice_CAST_div_fixp')
sptprice_CAST_div_float = solver.IntVar(0, 1, 'sptprice_CAST_div_float')
sptprice_CAST_div_double = solver.IntVar(0, 1, 'sptprice_CAST_div_double')
solver.Add( + (1)*sptprice_CAST_div_fixp + (1)*sptprice_CAST_div_float + (1)*sptprice_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_div_fixbits + (-10000)*sptprice_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_div = solver.IntVar(0, 1, 'C1_sptprice_CAST_div')
C2_sptprice_CAST_div = solver.IntVar(0, 1, 'C2_sptprice_CAST_div')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_div_fixbits + (-10000)*C1_sptprice_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_div_fixbits + (-10000)*C2_sptprice_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_div
castCostObj +=  + (1.13006)*C2_sptprice_CAST_div
C3_sptprice_CAST_div = solver.IntVar(0, 1, 'C3_sptprice_CAST_div')
C4_sptprice_CAST_div = solver.IntVar(0, 1, 'C4_sptprice_CAST_div')
C5_sptprice_CAST_div = solver.IntVar(0, 1, 'C5_sptprice_CAST_div')
C6_sptprice_CAST_div = solver.IntVar(0, 1, 'C6_sptprice_CAST_div')
C7_sptprice_CAST_div = solver.IntVar(0, 1, 'C7_sptprice_CAST_div')
C8_sptprice_CAST_div = solver.IntVar(0, 1, 'C8_sptprice_CAST_div')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_div_float + (-1)*C3_sptprice_CAST_div<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_div
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_div_fixp + (-1)*C4_sptprice_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_div
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_div_double + (-1)*C5_sptprice_CAST_div<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_div
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_div_fixp + (-1)*C6_sptprice_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_div
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_div_double + (-1)*C7_sptprice_CAST_div<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_div
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_div_float + (-1)*C8_sptprice_CAST_div<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_div



#Constraint for cast for   %div = fdiv float %sptprice, %strike, !taffo.info !42, !taffo.initweight !39
sptprice_CAST_div_0_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_div_0_fixbits')
sptprice_CAST_div_0_fixp = solver.IntVar(0, 1, 'sptprice_CAST_div_0_fixp')
sptprice_CAST_div_0_float = solver.IntVar(0, 1, 'sptprice_CAST_div_0_float')
sptprice_CAST_div_0_double = solver.IntVar(0, 1, 'sptprice_CAST_div_0_double')
solver.Add( + (1)*sptprice_CAST_div_0_fixp + (1)*sptprice_CAST_div_0_float + (1)*sptprice_CAST_div_0_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_div_0_fixbits + (-10000)*sptprice_CAST_div_0_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C1_sptprice_CAST_div_0')
C2_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C2_sptprice_CAST_div_0')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_div_0_fixbits + (-10000)*C1_sptprice_CAST_div_0<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_div_0_fixbits + (-10000)*C2_sptprice_CAST_div_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_div_0
castCostObj +=  + (1.13006)*C2_sptprice_CAST_div_0
C3_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C3_sptprice_CAST_div_0')
C4_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C4_sptprice_CAST_div_0')
C5_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C5_sptprice_CAST_div_0')
C6_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C6_sptprice_CAST_div_0')
C7_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C7_sptprice_CAST_div_0')
C8_sptprice_CAST_div_0 = solver.IntVar(0, 1, 'C8_sptprice_CAST_div_0')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_div_0_float + (-1)*C3_sptprice_CAST_div_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_div_0
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_div_0_fixp + (-1)*C4_sptprice_CAST_div_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_div_0
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_div_0_double + (-1)*C5_sptprice_CAST_div_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_div_0
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_div_0_fixp + (-1)*C6_sptprice_CAST_div_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_div_0
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_div_0_double + (-1)*C7_sptprice_CAST_div_0<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_div_0
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_div_0_float + (-1)*C8_sptprice_CAST_div_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_div_0



#Stuff for   %div = fdiv float %sptprice, %strike, !taffo.info !42, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float<=10025)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double<=10054)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*sptprice_CAST_div_fixp + (-1)*sptprice_CAST_div_0_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_div_float + (-1)*sptprice_CAST_div_0_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_div_double + (-1)*sptprice_CAST_div_0_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_div_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_div_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_div_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double==0)    #double equality
mathCostObj =  + (3.45438)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp
mathCostObj +=  + (4.13283)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float
mathCostObj +=  + (5.68177)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp7 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_1<=2)    #Enob: propagation in division 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp5 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_enob_2<=2)    #Enob: propagation in division 2



#Stuff for   %call27 = call float @_ZSt3logf.4.10(float %div), !taffo.info !44, !taffo.initweight !46, !taffo.constinfo !40, !taffo.originalCall !47
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call = call float @logf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_ZSt3logf_4_10_call_fixbits = solver.IntVar(0, 30, '_ZSt3logf_4_10_call_fixbits')
_ZSt3logf_4_10_call_fixp = solver.IntVar(0, 1, '_ZSt3logf_4_10_call_fixp')
_ZSt3logf_4_10_call_float = solver.IntVar(0, 1, '_ZSt3logf_4_10_call_float')
_ZSt3logf_4_10_call_double = solver.IntVar(0, 1, '_ZSt3logf_4_10_call_double')
_ZSt3logf_4_10_call_enob = solver.IntVar(-10000, 10000, '_ZSt3logf_4_10_call_enob')
solver.Add( + (1)*_ZSt3logf_4_10_call_enob + (-1)*_ZSt3logf_4_10_call_fixbits + (10000)*_ZSt3logf_4_10_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_ZSt3logf_4_10_call_enob + (10000)*_ZSt3logf_4_10_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_ZSt3logf_4_10_call_enob + (10000)*_ZSt3logf_4_10_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_ZSt3logf_4_10_call_fixbits + (-10000)*_ZSt3logf_4_10_call_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_ZSt3logf_4_10_call_enob
solver.Add( + (1)*_ZSt3logf_4_10_call_fixp + (1)*_ZSt3logf_4_10_call_float + (1)*_ZSt3logf_4_10_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_ZSt3logf_4_10_call_fixbits + (-10000)*_ZSt3logf_4_10_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_ZSt3logf_4_10_call_float==1)    #Type constraint for return value



#Constraint for cast for   %call = call float @logf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div_CAST_call_float==1)    #Type constraint for argument value



#Constraint for cast for   ret float %call, !taffo.info !32, !taffo.initweight !33
_ZSt3logf_4_10_call_CAST_ret_fixbits = solver.IntVar(0, 30, '_ZSt3logf_4_10_call_CAST_ret_fixbits')
_ZSt3logf_4_10_call_CAST_ret_fixp = solver.IntVar(0, 1, '_ZSt3logf_4_10_call_CAST_ret_fixp')
_ZSt3logf_4_10_call_CAST_ret_float = solver.IntVar(0, 1, '_ZSt3logf_4_10_call_CAST_ret_float')
_ZSt3logf_4_10_call_CAST_ret_double = solver.IntVar(0, 1, '_ZSt3logf_4_10_call_CAST_ret_double')
solver.Add( + (1)*_ZSt3logf_4_10_call_CAST_ret_fixp + (1)*_ZSt3logf_4_10_call_CAST_ret_float + (1)*_ZSt3logf_4_10_call_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_ZSt3logf_4_10_call_CAST_ret_fixbits + (-10000)*_ZSt3logf_4_10_call_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C1__ZSt3logf_4_10_call_CAST_ret')
C2__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C2__ZSt3logf_4_10_call_CAST_ret')
solver.Add( + (1)*_ZSt3logf_4_10_call_fixbits + (-1)*_ZSt3logf_4_10_call_CAST_ret_fixbits + (-10000)*C1__ZSt3logf_4_10_call_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_ZSt3logf_4_10_call_fixbits + (1)*_ZSt3logf_4_10_call_CAST_ret_fixbits + (-10000)*C2__ZSt3logf_4_10_call_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__ZSt3logf_4_10_call_CAST_ret
castCostObj +=  + (1.13006)*C2__ZSt3logf_4_10_call_CAST_ret
C3__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C3__ZSt3logf_4_10_call_CAST_ret')
C4__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C4__ZSt3logf_4_10_call_CAST_ret')
C5__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C5__ZSt3logf_4_10_call_CAST_ret')
C6__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C6__ZSt3logf_4_10_call_CAST_ret')
C7__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C7__ZSt3logf_4_10_call_CAST_ret')
C8__ZSt3logf_4_10_call_CAST_ret = solver.IntVar(0, 1, 'C8__ZSt3logf_4_10_call_CAST_ret')
solver.Add( + (1)*_ZSt3logf_4_10_call_fixp + (1)*_ZSt3logf_4_10_call_CAST_ret_float + (-1)*C3__ZSt3logf_4_10_call_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__ZSt3logf_4_10_call_CAST_ret
solver.Add( + (1)*_ZSt3logf_4_10_call_float + (1)*_ZSt3logf_4_10_call_CAST_ret_fixp + (-1)*C4__ZSt3logf_4_10_call_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__ZSt3logf_4_10_call_CAST_ret
solver.Add( + (1)*_ZSt3logf_4_10_call_fixp + (1)*_ZSt3logf_4_10_call_CAST_ret_double + (-1)*C5__ZSt3logf_4_10_call_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__ZSt3logf_4_10_call_CAST_ret
solver.Add( + (1)*_ZSt3logf_4_10_call_double + (1)*_ZSt3logf_4_10_call_CAST_ret_fixp + (-1)*C6__ZSt3logf_4_10_call_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__ZSt3logf_4_10_call_CAST_ret
solver.Add( + (1)*_ZSt3logf_4_10_call_float + (1)*_ZSt3logf_4_10_call_CAST_ret_double + (-1)*C7__ZSt3logf_4_10_call_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__ZSt3logf_4_10_call_CAST_ret
solver.Add( + (1)*_ZSt3logf_4_10_call_double + (1)*_ZSt3logf_4_10_call_CAST_ret_float + (-1)*C8__ZSt3logf_4_10_call_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__ZSt3logf_4_10_call_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp + (-1)*_ZSt3logf_4_10_call_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_float + (-1)*_ZSt3logf_4_10_call_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_double + (-1)*_ZSt3logf_4_10_call_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits + (-1)*_ZSt3logf_4_10_call_CAST_ret_fixbits==0)    #same fractional bit



#Constraint for cast for   %mul = fmul float %volatility, %volatility, !taffo.info !48, !taffo.initweight !39
sptprice_CAST_mul_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul_fixbits')
sptprice_CAST_mul_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul_fixp')
sptprice_CAST_mul_float = solver.IntVar(0, 1, 'sptprice_CAST_mul_float')
sptprice_CAST_mul_double = solver.IntVar(0, 1, 'sptprice_CAST_mul_double')
solver.Add( + (1)*sptprice_CAST_mul_fixp + (1)*sptprice_CAST_mul_float + (1)*sptprice_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul_fixbits + (-10000)*sptprice_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul')
C2_sptprice_CAST_mul = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul_fixbits + (-10000)*C1_sptprice_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul_fixbits + (-10000)*C2_sptprice_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul
C3_sptprice_CAST_mul = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul')
C4_sptprice_CAST_mul = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul')
C5_sptprice_CAST_mul = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul')
C6_sptprice_CAST_mul = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul')
C7_sptprice_CAST_mul = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul')
C8_sptprice_CAST_mul = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul_float + (-1)*C3_sptprice_CAST_mul<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul_fixp + (-1)*C4_sptprice_CAST_mul<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul_double + (-1)*C5_sptprice_CAST_mul<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul_fixp + (-1)*C6_sptprice_CAST_mul<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul_double + (-1)*C7_sptprice_CAST_mul<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul_float + (-1)*C8_sptprice_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul



#Constraint for cast for   %mul = fmul float %volatility, %volatility, !taffo.info !48, !taffo.initweight !39
sptprice_CAST_mul_0_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul_0_fixbits')
sptprice_CAST_mul_0_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul_0_fixp')
sptprice_CAST_mul_0_float = solver.IntVar(0, 1, 'sptprice_CAST_mul_0_float')
sptprice_CAST_mul_0_double = solver.IntVar(0, 1, 'sptprice_CAST_mul_0_double')
solver.Add( + (1)*sptprice_CAST_mul_0_fixp + (1)*sptprice_CAST_mul_0_float + (1)*sptprice_CAST_mul_0_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul_0_fixbits + (-10000)*sptprice_CAST_mul_0_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul_0')
C2_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul_0')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul_0_fixbits + (-10000)*C1_sptprice_CAST_mul_0<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul_0_fixbits + (-10000)*C2_sptprice_CAST_mul_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul_0
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul_0
C3_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul_0')
C4_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul_0')
C5_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul_0')
C6_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul_0')
C7_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul_0')
C8_sptprice_CAST_mul_0 = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul_0')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul_0_float + (-1)*C3_sptprice_CAST_mul_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul_0
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul_0_fixp + (-1)*C4_sptprice_CAST_mul_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul_0
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul_0_double + (-1)*C5_sptprice_CAST_mul_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul_0
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul_0_fixp + (-1)*C6_sptprice_CAST_mul_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul_0
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul_0_double + (-1)*C7_sptprice_CAST_mul_0<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul_0
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul_0_float + (-1)*C8_sptprice_CAST_mul_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul_0



#Stuff for   %mul = fmul float %volatility, %volatility, !taffo.info !48, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float<=10032)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double<=10061)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*sptprice_CAST_mul_fixp + (-1)*sptprice_CAST_mul_0_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul_float + (-1)*sptprice_CAST_mul_0_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul_double + (-1)*sptprice_CAST_mul_0_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_mul_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp11 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_1<=4)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp11 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob_2<=4)    #Enob: propagation in product 2



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



#Stuff for double 5.000000e-01
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



#Constraint for cast for   %mul28 = fmul double %conv, 5.000000e-01, !taffo.info !50, !taffo.initweight !46, !taffo.constinfo !52
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28



#Stuff for double 5.000000e-01
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



#Constraint for cast for   %mul28 = fmul double %conv, 5.000000e-01, !taffo.info !50, !taffo.initweight !46, !taffo.constinfo !52
ConstantValue__6_CAST_mul28_fixbits = solver.IntVar(0, 31, 'ConstantValue__6_CAST_mul28_fixbits')
ConstantValue__6_CAST_mul28_fixp = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul28_fixp')
ConstantValue__6_CAST_mul28_float = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul28_float')
ConstantValue__6_CAST_mul28_double = solver.IntVar(0, 1, 'ConstantValue__6_CAST_mul28_double')
solver.Add( + (1)*ConstantValue__6_CAST_mul28_fixp + (1)*ConstantValue__6_CAST_mul28_float + (1)*ConstantValue__6_CAST_mul28_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__6_CAST_mul28_fixbits + (-10000)*ConstantValue__6_CAST_mul28_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C1_ConstantValue__6_CAST_mul28')
C2_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C2_ConstantValue__6_CAST_mul28')
solver.Add( + (1)*ConstantValue__6_fixbits + (-1)*ConstantValue__6_CAST_mul28_fixbits + (-10000)*C1_ConstantValue__6_CAST_mul28<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__6_fixbits + (1)*ConstantValue__6_CAST_mul28_fixbits + (-10000)*C2_ConstantValue__6_CAST_mul28<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__6_CAST_mul28
castCostObj +=  + (1.13006)*C2_ConstantValue__6_CAST_mul28
C3_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C3_ConstantValue__6_CAST_mul28')
C4_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C4_ConstantValue__6_CAST_mul28')
C5_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C5_ConstantValue__6_CAST_mul28')
C6_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C6_ConstantValue__6_CAST_mul28')
C7_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C7_ConstantValue__6_CAST_mul28')
C8_ConstantValue__6_CAST_mul28 = solver.IntVar(0, 1, 'C8_ConstantValue__6_CAST_mul28')
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_mul28_float + (-1)*C3_ConstantValue__6_CAST_mul28<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__6_CAST_mul28
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_mul28_fixp + (-1)*C4_ConstantValue__6_CAST_mul28<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__6_CAST_mul28
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_mul28_double + (-1)*C5_ConstantValue__6_CAST_mul28<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__6_CAST_mul28
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_mul28_fixp + (-1)*C6_ConstantValue__6_CAST_mul28<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__6_CAST_mul28
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_mul28_double + (-1)*C7_ConstantValue__6_CAST_mul28<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__6_CAST_mul28
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_mul28_float + (-1)*C8_ConstantValue__6_CAST_mul28<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__6_CAST_mul28



#Stuff for   %mul28 = fmul double %conv, 5.000000e-01, !taffo.info !50, !taffo.initweight !46, !taffo.constinfo !52
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float<=10033)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double<=10062)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp + (-1)*ConstantValue__6_CAST_mul28_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_float + (-1)*ConstantValue__6_CAST_mul28_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_double + (-1)*ConstantValue__6_CAST_mul28_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_CAST_mul28_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob + (-1)*ConstantValue__4_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_1<=9)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob_2<=1)    #Enob: propagation in product 2



#Constraint for cast for   %add = fadd float %rate, %conv29, !taffo.info !58, !taffo.initweight !39
sptprice_CAST_add_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_add_fixbits')
sptprice_CAST_add_fixp = solver.IntVar(0, 1, 'sptprice_CAST_add_fixp')
sptprice_CAST_add_float = solver.IntVar(0, 1, 'sptprice_CAST_add_float')
sptprice_CAST_add_double = solver.IntVar(0, 1, 'sptprice_CAST_add_double')
solver.Add( + (1)*sptprice_CAST_add_fixp + (1)*sptprice_CAST_add_float + (1)*sptprice_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_add_fixbits + (-10000)*sptprice_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_add = solver.IntVar(0, 1, 'C1_sptprice_CAST_add')
C2_sptprice_CAST_add = solver.IntVar(0, 1, 'C2_sptprice_CAST_add')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_add_fixbits + (-10000)*C1_sptprice_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_add_fixbits + (-10000)*C2_sptprice_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_add
castCostObj +=  + (1.13006)*C2_sptprice_CAST_add
C3_sptprice_CAST_add = solver.IntVar(0, 1, 'C3_sptprice_CAST_add')
C4_sptprice_CAST_add = solver.IntVar(0, 1, 'C4_sptprice_CAST_add')
C5_sptprice_CAST_add = solver.IntVar(0, 1, 'C5_sptprice_CAST_add')
C6_sptprice_CAST_add = solver.IntVar(0, 1, 'C6_sptprice_CAST_add')
C7_sptprice_CAST_add = solver.IntVar(0, 1, 'C7_sptprice_CAST_add')
C8_sptprice_CAST_add = solver.IntVar(0, 1, 'C8_sptprice_CAST_add')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_add_float + (-1)*C3_sptprice_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_add
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_add_fixp + (-1)*C4_sptprice_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_add
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_add_double + (-1)*C5_sptprice_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_add
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_add_fixp + (-1)*C6_sptprice_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_add
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_add_double + (-1)*C7_sptprice_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_add
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_add_float + (-1)*C8_sptprice_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_add



#Constraint for cast for   %add = fadd float %rate, %conv29, !taffo.info !58, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add



#Stuff for   %add = fadd float %rate, %conv29, !taffo.info !58, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float<=10029)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double<=10058)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*sptprice_CAST_add_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_add_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_add_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_add_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*sptprice_CAST_add_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_add_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_add_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_add_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp9<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul28_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %mul30 = fmul float %add, %time, !taffo.info !60, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30



#Constraint for cast for   %mul30 = fmul float %add, %time, !taffo.info !60, !taffo.initweight !39
sptprice_CAST_mul30_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul30_fixbits')
sptprice_CAST_mul30_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul30_fixp')
sptprice_CAST_mul30_float = solver.IntVar(0, 1, 'sptprice_CAST_mul30_float')
sptprice_CAST_mul30_double = solver.IntVar(0, 1, 'sptprice_CAST_mul30_double')
solver.Add( + (1)*sptprice_CAST_mul30_fixp + (1)*sptprice_CAST_mul30_float + (1)*sptprice_CAST_mul30_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul30_fixbits + (-10000)*sptprice_CAST_mul30_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul30')
C2_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul30')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul30_fixbits + (-10000)*C1_sptprice_CAST_mul30<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul30_fixbits + (-10000)*C2_sptprice_CAST_mul30<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul30
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul30
C3_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul30')
C4_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul30')
C5_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul30')
C6_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul30')
C7_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul30')
C8_sptprice_CAST_mul30 = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul30')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul30_float + (-1)*C3_sptprice_CAST_mul30<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul30
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul30_fixp + (-1)*C4_sptprice_CAST_mul30<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul30
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul30_double + (-1)*C5_sptprice_CAST_mul30<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul30
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul30_fixp + (-1)*C6_sptprice_CAST_mul30<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul30
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul30_double + (-1)*C7_sptprice_CAST_mul30<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul30
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul30_float + (-1)*C8_sptprice_CAST_mul30<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul30



#Stuff for   %mul30 = fmul float %add, %time, !taffo.info !60, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float<=10033)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double<=10062)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp + (-1)*sptprice_CAST_mul30_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_float + (-1)*sptprice_CAST_mul30_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_double + (-1)*sptprice_CAST_mul30_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_CAST_mul30_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp13 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_1<=5)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob_2<=4)    #Enob: propagation in product 2



#Constraint for cast for   %add31 = fadd float %mul30, %call27, !taffo.info !62, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31



#Constraint for cast for   %add31 = fadd float %mul30, %call27, !taffo.info !62, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31



#Stuff for   %add31 = fadd float %mul30, %call27, !taffo.info !62, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_CAST_add31_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_CAST_add31_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul30_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call27_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %mul32 = fmul float %volatility, %call, !taffo.info !64, !taffo.initweight !39
sptprice_CAST_mul32_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul32_fixbits')
sptprice_CAST_mul32_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul32_fixp')
sptprice_CAST_mul32_float = solver.IntVar(0, 1, 'sptprice_CAST_mul32_float')
sptprice_CAST_mul32_double = solver.IntVar(0, 1, 'sptprice_CAST_mul32_double')
solver.Add( + (1)*sptprice_CAST_mul32_fixp + (1)*sptprice_CAST_mul32_float + (1)*sptprice_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul32_fixbits + (-10000)*sptprice_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul32')
C2_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul32')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul32_fixbits + (-10000)*C1_sptprice_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul32_fixbits + (-10000)*C2_sptprice_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul32
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul32
C3_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul32')
C4_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul32')
C5_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul32')
C6_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul32')
C7_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul32')
C8_sptprice_CAST_mul32 = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul32')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul32_float + (-1)*C3_sptprice_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul32
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul32_fixp + (-1)*C4_sptprice_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul32
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul32_double + (-1)*C5_sptprice_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul32
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul32_fixp + (-1)*C6_sptprice_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul32
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul32_double + (-1)*C7_sptprice_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul32
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul32_float + (-1)*C8_sptprice_CAST_mul32<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul32



#Constraint for cast for   %mul32 = fmul float %volatility, %call, !taffo.info !64, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32



#Stuff for   %mul32 = fmul float %volatility, %call, !taffo.info !64, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float<=10030)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double<=10059)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*sptprice_CAST_mul32_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul32_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul32_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_CAST_mul32_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_mul32_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul32_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul32_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_1<=4)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp11 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob_2<=2)    #Enob: propagation in product 2



#Constraint for cast for   %div33 = fdiv float %add31, %mul32, !taffo.info !66, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33



#Constraint for cast for   %div33 = fdiv float %add31, %mul32, !taffo.info !66, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33



#Stuff for   %div33 = fdiv float %add31, %mul32, !taffo.info !66, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits = solver.IntVar(0, 24, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_div33_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_CAST_div33_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double==0)    #double equality
mathCostObj +=  + (3.45438)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp
mathCostObj +=  + (4.13283)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float
mathCostObj +=  + (5.68177)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_1<=1022)    #Enob: propagation in division 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_add31_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob_2<=4)    #Enob: propagation in division 2



#Constraint for cast for   %sub = fsub float %div33, %mul32, !taffo.info !68, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixbits = solver.IntVar(0, 24, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub



#Constraint for cast for   %sub = fsub float %div33, %mul32, !taffo.info !68, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub



#Stuff for   %sub = fsub float %div33, %mul32, !taffo.info !68, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits = solver.IntVar(0, 24, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_CAST_sub_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul32_enob<=0)    #Enob propagation in sub second addend



#Stuff for   %call34 = call float @_Z4CNDFf.2.13(float %div33), !taffo.info !34, !taffo.initweight !39, !taffo.constinfo !40, !taffo.originalCall !70
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp<=0)    #If not fix, frac part to zero



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



#Stuff for float -0.000000e+00
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



#Stuff for float -0.000000e+00
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



#Stuff for float -0.000000e+00
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



#Constraint for cast for   %sub = fsub float -0.000000e+00, %InputX, !taffo.info !33, !taffo.initweight !23, !taffo.constinfo !35
ConstantValue__10_CAST_sub_fixbits = solver.IntVar(0, 32, 'ConstantValue__10_CAST_sub_fixbits')
ConstantValue__10_CAST_sub_fixp = solver.IntVar(0, 1, 'ConstantValue__10_CAST_sub_fixp')
ConstantValue__10_CAST_sub_float = solver.IntVar(0, 1, 'ConstantValue__10_CAST_sub_float')
ConstantValue__10_CAST_sub_double = solver.IntVar(0, 1, 'ConstantValue__10_CAST_sub_double')
solver.Add( + (1)*ConstantValue__10_CAST_sub_fixp + (1)*ConstantValue__10_CAST_sub_float + (1)*ConstantValue__10_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__10_CAST_sub_fixbits + (-10000)*ConstantValue__10_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C1_ConstantValue__10_CAST_sub')
C2_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C2_ConstantValue__10_CAST_sub')
solver.Add( + (1)*ConstantValue__10_fixbits + (-1)*ConstantValue__10_CAST_sub_fixbits + (-10000)*C1_ConstantValue__10_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__10_fixbits + (1)*ConstantValue__10_CAST_sub_fixbits + (-10000)*C2_ConstantValue__10_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__10_CAST_sub
castCostObj +=  + (1.13006)*C2_ConstantValue__10_CAST_sub
C3_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C3_ConstantValue__10_CAST_sub')
C4_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C4_ConstantValue__10_CAST_sub')
C5_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C5_ConstantValue__10_CAST_sub')
C6_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C6_ConstantValue__10_CAST_sub')
C7_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C7_ConstantValue__10_CAST_sub')
C8_ConstantValue__10_CAST_sub = solver.IntVar(0, 1, 'C8_ConstantValue__10_CAST_sub')
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_CAST_sub_float + (-1)*C3_ConstantValue__10_CAST_sub<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__10_CAST_sub
solver.Add( + (1)*ConstantValue__10_float + (1)*ConstantValue__10_CAST_sub_fixp + (-1)*C4_ConstantValue__10_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__10_CAST_sub
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_CAST_sub_double + (-1)*C5_ConstantValue__10_CAST_sub<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__10_CAST_sub
solver.Add( + (1)*ConstantValue__10_double + (1)*ConstantValue__10_CAST_sub_fixp + (-1)*C6_ConstantValue__10_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__10_CAST_sub
solver.Add( + (1)*ConstantValue__10_float + (1)*ConstantValue__10_CAST_sub_double + (-1)*C7_ConstantValue__10_CAST_sub<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__10_CAST_sub
solver.Add( + (1)*ConstantValue__10_double + (1)*ConstantValue__10_CAST_sub_float + (-1)*C8_ConstantValue__10_CAST_sub<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__10_CAST_sub



#Constraint for cast for   %sub = fsub float -0.000000e+00, %InputX, !taffo.info !33, !taffo.initweight !23, !taffo.constinfo !35
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixbits = solver.IntVar(0, 24, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0



#Stuff for   %sub = fsub float -0.000000e+00, %InputX, !taffo.info !33, !taffo.initweight !23, !taffo.constinfo !35
_Z4CNDFf_2_13_sub_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_2_13_sub_fixbits')
_Z4CNDFf_2_13_sub_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub_fixp')
_Z4CNDFf_2_13_sub_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub_float')
_Z4CNDFf_2_13_sub_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub_double')
_Z4CNDFf_2_13_sub_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_sub_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_sub_enob + (-1)*_Z4CNDFf_2_13_sub_fixbits + (10000)*_Z4CNDFf_2_13_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_sub_enob + (10000)*_Z4CNDFf_2_13_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_sub_enob + (10000)*_Z4CNDFf_2_13_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_sub_fixbits + (-10000)*_Z4CNDFf_2_13_sub_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_sub_enob
solver.Add( + (1)*_Z4CNDFf_2_13_sub_fixp + (1)*_Z4CNDFf_2_13_sub_float + (1)*_Z4CNDFf_2_13_sub_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_sub_fixbits + (-10000)*_Z4CNDFf_2_13_sub_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__10_CAST_sub_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__10_CAST_sub_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_float==0)    #float equality
solver.Add( + (1)*ConstantValue__10_CAST_sub_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_double==0)    #double equality
solver.Add( + (1)*ConstantValue__10_CAST_sub_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_sub_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__10_CAST_sub_fixp + (-1)*_Z4CNDFf_2_13_sub_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__10_CAST_sub_float + (-1)*_Z4CNDFf_2_13_sub_float==0)    #float equality
solver.Add( + (1)*ConstantValue__10_CAST_sub_double + (-1)*_Z4CNDFf_2_13_sub_double==0)    #double equality
solver.Add( + (1)*ConstantValue__10_CAST_sub_fixbits + (-1)*_Z4CNDFf_2_13_sub_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_sub_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_sub_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_sub_double
solver.Add( + (1)*_Z4CNDFf_2_13_sub_enob + (-1)*ConstantValue__8_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z4CNDFf_2_13_sub_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob<=0)    #Enob propagation in sub second addend



#Stuff for   %InputX.addr.0 = phi float [ %sub, %if.then ], [ %InputX, %if.else ], !taffo.info !39
_Z4CNDFf_2_13_InputX_addr_0_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_2_13_InputX_addr_0_fixbits')
_Z4CNDFf_2_13_InputX_addr_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_fixp')
_Z4CNDFf_2_13_InputX_addr_0_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_float')
_Z4CNDFf_2_13_InputX_addr_0_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_double')
_Z4CNDFf_2_13_InputX_addr_0_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_InputX_addr_0_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (-1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (10000)*_Z4CNDFf_2_13_InputX_addr_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (10000)*_Z4CNDFf_2_13_InputX_addr_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (10000)*_Z4CNDFf_2_13_InputX_addr_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (-10000)*_Z4CNDFf_2_13_InputX_addr_0_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_InputX_addr_0_enob
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (-10000)*_Z4CNDFf_2_13_InputX_addr_0_fixp<=0)    #If not fix, frac part to zero
_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_0 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_0')
_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_1')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_0 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %InputX.addr.0 = phi float [ %sub, %if.then ], [ %InputX, %if.else ], !taffo.info !39
_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixbits')
_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixp')
_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_float')
_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_double')
solver.Add( + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixbits + (-10000)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
C2__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
solver.Add( + (1)*_Z4CNDFf_2_13_sub_fixbits + (-1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixbits + (-10000)*C1__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_sub_fixbits + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixbits + (-10000)*C2__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
C3__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
C4__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
C5__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
C6__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
C7__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
C8__Z4CNDFf_2_13_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_sub_CAST_InputX_addr_0')
solver.Add( + (1)*_Z4CNDFf_2_13_sub_fixp + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_float + (-1)*C3__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub_float + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixp + (-1)*C4__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub_fixp + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_double + (-1)*C5__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub_double + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixp + (-1)*C6__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub_float + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_double + (-1)*C7__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub_double + (1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_float + (-1)*C8__Z4CNDFf_2_13_sub_CAST_InputX_addr_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (-1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (-1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (-1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_2_13_sub_CAST_InputX_addr_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (-1)*_Z4CNDFf_2_13_sub_enob + (10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_0<=10000)    #Enob: forcing phi enob



#Constraint for cast for   %InputX.addr.0 = phi float [ %sub, %if.then ], [ %InputX, %if.else ], !taffo.info !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixbits = solver.IntVar(0, 24, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_CAST_InputX_addr_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_div33_enob + (10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_InputX_addr_0_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   %mul = fmul float %InputX.addr.0, %InputX.addr.0, !taffo.info !41, !taffo.initweight !23
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixbits')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_float')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_double')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixbits + (-10000)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixbits + (-10000)*C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixbits + (-10000)*C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul
C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_float + (-1)*C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp + (-1)*C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_double + (-1)*C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp + (-1)*C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_double + (-1)*C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_float + (-1)*C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul



#Constraint for cast for   %mul = fmul float %InputX.addr.0, %InputX.addr.0, !taffo.info !41, !taffo.initweight !23
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixbits')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixp')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_float')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_double')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixbits + (-10000)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixbits + (-10000)*C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixbits + (-10000)*C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0
C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_float + (-1)*C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixp + (-1)*C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_double + (-1)*C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixp + (-1)*C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_double + (-1)*C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_float + (-1)*C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0



#Stuff for   %mul = fmul float %InputX.addr.0, %InputX.addr.0, !taffo.info !41, !taffo.initweight !23
_Z4CNDFf_2_13_mul_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_2_13_mul_fixbits')
_Z4CNDFf_2_13_mul_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul_fixp')
_Z4CNDFf_2_13_mul_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul_float')
_Z4CNDFf_2_13_mul_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul_double')
_Z4CNDFf_2_13_mul_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul_enob + (-1)*_Z4CNDFf_2_13_mul_fixbits + (10000)*_Z4CNDFf_2_13_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul_enob + (10000)*_Z4CNDFf_2_13_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul_enob + (10000)*_Z4CNDFf_2_13_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul_fixbits + (-10000)*_Z4CNDFf_2_13_mul_fixp>=-9983)    #Limit the lower number of frac bits18
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul_fixp + (1)*_Z4CNDFf_2_13_mul_float + (1)*_Z4CNDFf_2_13_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul_fixbits + (-10000)*_Z4CNDFf_2_13_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_float + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_double + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_fixp + (-1)*_Z4CNDFf_2_13_mul_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_float + (-1)*_Z4CNDFf_2_13_mul_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul_double + (-1)*_Z4CNDFf_2_13_mul_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul_enob + (-1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul_enob + (-1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for float -5.000000e-01
ConstantValue__11_fixbits = solver.IntVar(0, 30, 'ConstantValue__11_fixbits')
ConstantValue__11_fixp = solver.IntVar(0, 1, 'ConstantValue__11_fixp')
ConstantValue__11_float = solver.IntVar(0, 1, 'ConstantValue__11_float')
ConstantValue__11_double = solver.IntVar(0, 1, 'ConstantValue__11_double')
ConstantValue__11_enob = solver.IntVar(-10000, 10000, 'ConstantValue__11_enob')
solver.Add( + (1)*ConstantValue__11_enob + (-1)*ConstantValue__11_fixbits + (10000)*ConstantValue__11_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__11_enob + (10000)*ConstantValue__11_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_float + (1)*ConstantValue__11_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__11_fixbits + (-10000)*ConstantValue__11_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -5.000000e-01
ConstantValue__12_fixbits = solver.IntVar(0, 30, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -5.000000e-01
ConstantValue__13_fixbits = solver.IntVar(0, 30, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_float + (1)*ConstantValue__13_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul16 = fmul float -5.000000e-01, %mul, !taffo.info !43, !taffo.initweight !30, !taffo.constinfo !45
ConstantValue__13_CAST_mul16_fixbits = solver.IntVar(0, 30, 'ConstantValue__13_CAST_mul16_fixbits')
ConstantValue__13_CAST_mul16_fixp = solver.IntVar(0, 1, 'ConstantValue__13_CAST_mul16_fixp')
ConstantValue__13_CAST_mul16_float = solver.IntVar(0, 1, 'ConstantValue__13_CAST_mul16_float')
ConstantValue__13_CAST_mul16_double = solver.IntVar(0, 1, 'ConstantValue__13_CAST_mul16_double')
solver.Add( + (1)*ConstantValue__13_CAST_mul16_fixp + (1)*ConstantValue__13_CAST_mul16_float + (1)*ConstantValue__13_CAST_mul16_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__13_CAST_mul16_fixbits + (-10000)*ConstantValue__13_CAST_mul16_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C1_ConstantValue__13_CAST_mul16')
C2_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C2_ConstantValue__13_CAST_mul16')
solver.Add( + (1)*ConstantValue__13_fixbits + (-1)*ConstantValue__13_CAST_mul16_fixbits + (-10000)*C1_ConstantValue__13_CAST_mul16<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__13_fixbits + (1)*ConstantValue__13_CAST_mul16_fixbits + (-10000)*C2_ConstantValue__13_CAST_mul16<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__13_CAST_mul16
castCostObj +=  + (1.13006)*C2_ConstantValue__13_CAST_mul16
C3_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C3_ConstantValue__13_CAST_mul16')
C4_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C4_ConstantValue__13_CAST_mul16')
C5_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C5_ConstantValue__13_CAST_mul16')
C6_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C6_ConstantValue__13_CAST_mul16')
C7_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C7_ConstantValue__13_CAST_mul16')
C8_ConstantValue__13_CAST_mul16 = solver.IntVar(0, 1, 'C8_ConstantValue__13_CAST_mul16')
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_CAST_mul16_float + (-1)*C3_ConstantValue__13_CAST_mul16<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__13_CAST_mul16
solver.Add( + (1)*ConstantValue__13_float + (1)*ConstantValue__13_CAST_mul16_fixp + (-1)*C4_ConstantValue__13_CAST_mul16<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__13_CAST_mul16
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_CAST_mul16_double + (-1)*C5_ConstantValue__13_CAST_mul16<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__13_CAST_mul16
solver.Add( + (1)*ConstantValue__13_double + (1)*ConstantValue__13_CAST_mul16_fixp + (-1)*C6_ConstantValue__13_CAST_mul16<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__13_CAST_mul16
solver.Add( + (1)*ConstantValue__13_float + (1)*ConstantValue__13_CAST_mul16_double + (-1)*C7_ConstantValue__13_CAST_mul16<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__13_CAST_mul16
solver.Add( + (1)*ConstantValue__13_double + (1)*ConstantValue__13_CAST_mul16_float + (-1)*C8_ConstantValue__13_CAST_mul16<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__13_CAST_mul16



#Constraint for cast for   %mul16 = fmul float -5.000000e-01, %mul, !taffo.info !43, !taffo.initweight !30, !taffo.constinfo !45
_Z4CNDFf_2_13_mul_CAST_mul16_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_2_13_mul_CAST_mul16_fixbits')
_Z4CNDFf_2_13_mul_CAST_mul16_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul_CAST_mul16_fixp')
_Z4CNDFf_2_13_mul_CAST_mul16_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul_CAST_mul16_float')
_Z4CNDFf_2_13_mul_CAST_mul16_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul_CAST_mul16_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_fixp + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_float + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_fixbits + (-10000)*_Z4CNDFf_2_13_mul_CAST_mul16_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul_CAST_mul16')
C2__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul_CAST_mul16')
solver.Add( + (1)*_Z4CNDFf_2_13_mul_fixbits + (-1)*_Z4CNDFf_2_13_mul_CAST_mul16_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul_CAST_mul16<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul_fixbits + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul_CAST_mul16<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul_CAST_mul16
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul_CAST_mul16
C3__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul_CAST_mul16')
C4__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul_CAST_mul16')
C5__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul_CAST_mul16')
C6__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul_CAST_mul16')
C7__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul_CAST_mul16')
C8__Z4CNDFf_2_13_mul_CAST_mul16 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul_CAST_mul16')
solver.Add( + (1)*_Z4CNDFf_2_13_mul_fixp + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_float + (-1)*C3__Z4CNDFf_2_13_mul_CAST_mul16<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_2_13_mul_float + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_fixp + (-1)*C4__Z4CNDFf_2_13_mul_CAST_mul16<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_2_13_mul_fixp + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_double + (-1)*C5__Z4CNDFf_2_13_mul_CAST_mul16<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_2_13_mul_double + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_fixp + (-1)*C6__Z4CNDFf_2_13_mul_CAST_mul16<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_2_13_mul_float + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_double + (-1)*C7__Z4CNDFf_2_13_mul_CAST_mul16<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_2_13_mul_double + (1)*_Z4CNDFf_2_13_mul_CAST_mul16_float + (-1)*C8__Z4CNDFf_2_13_mul_CAST_mul16<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul_CAST_mul16



#Stuff for   %mul16 = fmul float -5.000000e-01, %mul, !taffo.info !43, !taffo.initweight !30, !taffo.constinfo !45
_Z4CNDFf_2_13_mul16_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_2_13_mul16_fixbits')
_Z4CNDFf_2_13_mul16_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul16_fixp')
_Z4CNDFf_2_13_mul16_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul16_float')
_Z4CNDFf_2_13_mul16_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul16_double')
_Z4CNDFf_2_13_mul16_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul16_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_enob + (-1)*_Z4CNDFf_2_13_mul16_fixbits + (10000)*_Z4CNDFf_2_13_mul16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_enob + (10000)*_Z4CNDFf_2_13_mul16_float<=10020)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_enob + (10000)*_Z4CNDFf_2_13_mul16_double<=10049)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_fixbits + (-10000)*_Z4CNDFf_2_13_mul16_fixp>=-9983)    #Limit the lower number of frac bits18
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul16_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_fixp + (1)*_Z4CNDFf_2_13_mul16_float + (1)*_Z4CNDFf_2_13_mul16_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_fixbits + (-10000)*_Z4CNDFf_2_13_mul16_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__13_CAST_mul16_fixp + (-1)*_Z4CNDFf_2_13_mul_CAST_mul16_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__13_CAST_mul16_float + (-1)*_Z4CNDFf_2_13_mul_CAST_mul16_float==0)    #float equality
solver.Add( + (1)*ConstantValue__13_CAST_mul16_double + (-1)*_Z4CNDFf_2_13_mul_CAST_mul16_double==0)    #double equality
solver.Add( + (1)*ConstantValue__13_CAST_mul16_fixp + (-1)*_Z4CNDFf_2_13_mul16_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__13_CAST_mul16_float + (-1)*_Z4CNDFf_2_13_mul16_float==0)    #float equality
solver.Add( + (1)*ConstantValue__13_CAST_mul16_double + (-1)*_Z4CNDFf_2_13_mul16_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul16_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul16_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul16_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_enob + (-1)*_Z4CNDFf_2_13_mul_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_1<=1)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_enob + (-1)*ConstantValue__11_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul16_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for   %call = call float @_ZSt3expf.8.15(float %mul16), !taffo.info !48, !taffo.initweight !32, !taffo.constinfo !50, !taffo.originalCall !51
_Z4CNDFf_2_13_call_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_2_13_call_fixbits')
_Z4CNDFf_2_13_call_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_call_fixp')
_Z4CNDFf_2_13_call_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_call_float')
_Z4CNDFf_2_13_call_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_call_double')
_Z4CNDFf_2_13_call_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_call_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_call_enob + (-1)*_Z4CNDFf_2_13_call_fixbits + (10000)*_Z4CNDFf_2_13_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_call_enob + (10000)*_Z4CNDFf_2_13_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_call_enob + (10000)*_Z4CNDFf_2_13_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixbits + (-10000)*_Z4CNDFf_2_13_call_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_call_enob
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixp + (1)*_Z4CNDFf_2_13_call_float + (1)*_Z4CNDFf_2_13_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixbits + (-10000)*_Z4CNDFf_2_13_call_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call = call float @expf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_ZSt3expf_8_15_call_fixbits = solver.IntVar(0, 31, '_ZSt3expf_8_15_call_fixbits')
_ZSt3expf_8_15_call_fixp = solver.IntVar(0, 1, '_ZSt3expf_8_15_call_fixp')
_ZSt3expf_8_15_call_float = solver.IntVar(0, 1, '_ZSt3expf_8_15_call_float')
_ZSt3expf_8_15_call_double = solver.IntVar(0, 1, '_ZSt3expf_8_15_call_double')
_ZSt3expf_8_15_call_enob = solver.IntVar(-10000, 10000, '_ZSt3expf_8_15_call_enob')
solver.Add( + (1)*_ZSt3expf_8_15_call_enob + (-1)*_ZSt3expf_8_15_call_fixbits + (10000)*_ZSt3expf_8_15_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_ZSt3expf_8_15_call_enob + (10000)*_ZSt3expf_8_15_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_ZSt3expf_8_15_call_enob + (10000)*_ZSt3expf_8_15_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_ZSt3expf_8_15_call_fixbits + (-10000)*_ZSt3expf_8_15_call_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_ZSt3expf_8_15_call_enob
solver.Add( + (1)*_ZSt3expf_8_15_call_fixp + (1)*_ZSt3expf_8_15_call_float + (1)*_ZSt3expf_8_15_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_ZSt3expf_8_15_call_fixbits + (-10000)*_ZSt3expf_8_15_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_ZSt3expf_8_15_call_float==1)    #Type constraint for return value



#Constraint for cast for   %call = call float @expf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_Z4CNDFf_2_13_mul16_CAST_call_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_2_13_mul16_CAST_call_fixbits')
_Z4CNDFf_2_13_mul16_CAST_call_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul16_CAST_call_fixp')
_Z4CNDFf_2_13_mul16_CAST_call_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul16_CAST_call_float')
_Z4CNDFf_2_13_mul16_CAST_call_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul16_CAST_call_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_CAST_call_fixp + (1)*_Z4CNDFf_2_13_mul16_CAST_call_float + (1)*_Z4CNDFf_2_13_mul16_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_CAST_call_fixbits + (-10000)*_Z4CNDFf_2_13_mul16_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul16_CAST_call')
C2__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul16_CAST_call')
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_fixbits + (-1)*_Z4CNDFf_2_13_mul16_CAST_call_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul16_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul16_fixbits + (1)*_Z4CNDFf_2_13_mul16_CAST_call_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul16_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul16_CAST_call
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul16_CAST_call
C3__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul16_CAST_call')
C4__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul16_CAST_call')
C5__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul16_CAST_call')
C6__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul16_CAST_call')
C7__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul16_CAST_call')
C8__Z4CNDFf_2_13_mul16_CAST_call = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul16_CAST_call')
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_fixp + (1)*_Z4CNDFf_2_13_mul16_CAST_call_float + (-1)*C3__Z4CNDFf_2_13_mul16_CAST_call<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_float + (1)*_Z4CNDFf_2_13_mul16_CAST_call_fixp + (-1)*C4__Z4CNDFf_2_13_mul16_CAST_call<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_fixp + (1)*_Z4CNDFf_2_13_mul16_CAST_call_double + (-1)*C5__Z4CNDFf_2_13_mul16_CAST_call<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_double + (1)*_Z4CNDFf_2_13_mul16_CAST_call_fixp + (-1)*C6__Z4CNDFf_2_13_mul16_CAST_call<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_float + (1)*_Z4CNDFf_2_13_mul16_CAST_call_double + (-1)*C7__Z4CNDFf_2_13_mul16_CAST_call<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_double + (1)*_Z4CNDFf_2_13_mul16_CAST_call_float + (-1)*C8__Z4CNDFf_2_13_mul16_CAST_call<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_2_13_mul16_CAST_call_float==1)    #Type constraint for argument value



#Constraint for cast for   ret float %call, !taffo.info !32, !taffo.initweight !34
_ZSt3expf_8_15_call_CAST_ret_fixbits = solver.IntVar(0, 31, '_ZSt3expf_8_15_call_CAST_ret_fixbits')
_ZSt3expf_8_15_call_CAST_ret_fixp = solver.IntVar(0, 1, '_ZSt3expf_8_15_call_CAST_ret_fixp')
_ZSt3expf_8_15_call_CAST_ret_float = solver.IntVar(0, 1, '_ZSt3expf_8_15_call_CAST_ret_float')
_ZSt3expf_8_15_call_CAST_ret_double = solver.IntVar(0, 1, '_ZSt3expf_8_15_call_CAST_ret_double')
solver.Add( + (1)*_ZSt3expf_8_15_call_CAST_ret_fixp + (1)*_ZSt3expf_8_15_call_CAST_ret_float + (1)*_ZSt3expf_8_15_call_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_ZSt3expf_8_15_call_CAST_ret_fixbits + (-10000)*_ZSt3expf_8_15_call_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C1__ZSt3expf_8_15_call_CAST_ret')
C2__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C2__ZSt3expf_8_15_call_CAST_ret')
solver.Add( + (1)*_ZSt3expf_8_15_call_fixbits + (-1)*_ZSt3expf_8_15_call_CAST_ret_fixbits + (-10000)*C1__ZSt3expf_8_15_call_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_ZSt3expf_8_15_call_fixbits + (1)*_ZSt3expf_8_15_call_CAST_ret_fixbits + (-10000)*C2__ZSt3expf_8_15_call_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__ZSt3expf_8_15_call_CAST_ret
castCostObj +=  + (1.13006)*C2__ZSt3expf_8_15_call_CAST_ret
C3__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C3__ZSt3expf_8_15_call_CAST_ret')
C4__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C4__ZSt3expf_8_15_call_CAST_ret')
C5__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C5__ZSt3expf_8_15_call_CAST_ret')
C6__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C6__ZSt3expf_8_15_call_CAST_ret')
C7__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C7__ZSt3expf_8_15_call_CAST_ret')
C8__ZSt3expf_8_15_call_CAST_ret = solver.IntVar(0, 1, 'C8__ZSt3expf_8_15_call_CAST_ret')
solver.Add( + (1)*_ZSt3expf_8_15_call_fixp + (1)*_ZSt3expf_8_15_call_CAST_ret_float + (-1)*C3__ZSt3expf_8_15_call_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__ZSt3expf_8_15_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_8_15_call_float + (1)*_ZSt3expf_8_15_call_CAST_ret_fixp + (-1)*C4__ZSt3expf_8_15_call_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__ZSt3expf_8_15_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_8_15_call_fixp + (1)*_ZSt3expf_8_15_call_CAST_ret_double + (-1)*C5__ZSt3expf_8_15_call_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__ZSt3expf_8_15_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_8_15_call_double + (1)*_ZSt3expf_8_15_call_CAST_ret_fixp + (-1)*C6__ZSt3expf_8_15_call_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__ZSt3expf_8_15_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_8_15_call_float + (1)*_ZSt3expf_8_15_call_CAST_ret_double + (-1)*C7__ZSt3expf_8_15_call_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__ZSt3expf_8_15_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_8_15_call_double + (1)*_ZSt3expf_8_15_call_CAST_ret_float + (-1)*C8__ZSt3expf_8_15_call_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__ZSt3expf_8_15_call_CAST_ret
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixp + (-1)*_ZSt3expf_8_15_call_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_float + (-1)*_ZSt3expf_8_15_call_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_double + (-1)*_ZSt3expf_8_15_call_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixbits + (-1)*_ZSt3expf_8_15_call_CAST_ret_fixbits==0)    #same fractional bit



#Stuff for double 0x3FD9884533D43651
ConstantValue__14_fixbits = solver.IntVar(0, 31, 'ConstantValue__14_fixbits')
ConstantValue__14_fixp = solver.IntVar(0, 1, 'ConstantValue__14_fixp')
ConstantValue__14_float = solver.IntVar(0, 1, 'ConstantValue__14_float')
ConstantValue__14_double = solver.IntVar(0, 1, 'ConstantValue__14_double')
ConstantValue__14_enob = solver.IntVar(-10000, 10000, 'ConstantValue__14_enob')
solver.Add( + (1)*ConstantValue__14_enob + (-1)*ConstantValue__14_fixbits + (10000)*ConstantValue__14_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_float + (1)*ConstantValue__14_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FD9884533D43651
ConstantValue__15_fixbits = solver.IntVar(0, 31, 'ConstantValue__15_fixbits')
ConstantValue__15_fixp = solver.IntVar(0, 1, 'ConstantValue__15_fixp')
ConstantValue__15_float = solver.IntVar(0, 1, 'ConstantValue__15_float')
ConstantValue__15_double = solver.IntVar(0, 1, 'ConstantValue__15_double')
ConstantValue__15_enob = solver.IntVar(-10000, 10000, 'ConstantValue__15_enob')
solver.Add( + (1)*ConstantValue__15_enob + (-1)*ConstantValue__15_fixbits + (10000)*ConstantValue__15_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__15_fixp + (1)*ConstantValue__15_float + (1)*ConstantValue__15_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul18 = fmul double %conv17, 0x3FD9884533D43651, !taffo.info !53, !taffo.initweight !30, !taffo.constinfo !55
_Z4CNDFf_2_13_call_CAST_mul18_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_2_13_call_CAST_mul18_fixbits')
_Z4CNDFf_2_13_call_CAST_mul18_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_call_CAST_mul18_fixp')
_Z4CNDFf_2_13_call_CAST_mul18_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_call_CAST_mul18_float')
_Z4CNDFf_2_13_call_CAST_mul18_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_call_CAST_mul18_double')
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_fixp + (1)*_Z4CNDFf_2_13_call_CAST_mul18_float + (1)*_Z4CNDFf_2_13_call_CAST_mul18_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_fixbits + (-10000)*_Z4CNDFf_2_13_call_CAST_mul18_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_call_CAST_mul18')
C2__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_call_CAST_mul18')
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixbits + (-1)*_Z4CNDFf_2_13_call_CAST_mul18_fixbits + (-10000)*C1__Z4CNDFf_2_13_call_CAST_mul18<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_call_fixbits + (1)*_Z4CNDFf_2_13_call_CAST_mul18_fixbits + (-10000)*C2__Z4CNDFf_2_13_call_CAST_mul18<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_call_CAST_mul18
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_call_CAST_mul18
C3__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_call_CAST_mul18')
C4__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_call_CAST_mul18')
C5__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_call_CAST_mul18')
C6__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_call_CAST_mul18')
C7__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_call_CAST_mul18')
C8__Z4CNDFf_2_13_call_CAST_mul18 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_call_CAST_mul18')
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixp + (1)*_Z4CNDFf_2_13_call_CAST_mul18_float + (-1)*C3__Z4CNDFf_2_13_call_CAST_mul18<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_2_13_call_float + (1)*_Z4CNDFf_2_13_call_CAST_mul18_fixp + (-1)*C4__Z4CNDFf_2_13_call_CAST_mul18<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_2_13_call_fixp + (1)*_Z4CNDFf_2_13_call_CAST_mul18_double + (-1)*C5__Z4CNDFf_2_13_call_CAST_mul18<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_2_13_call_double + (1)*_Z4CNDFf_2_13_call_CAST_mul18_fixp + (-1)*C6__Z4CNDFf_2_13_call_CAST_mul18<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_2_13_call_float + (1)*_Z4CNDFf_2_13_call_CAST_mul18_double + (-1)*C7__Z4CNDFf_2_13_call_CAST_mul18<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_2_13_call_double + (1)*_Z4CNDFf_2_13_call_CAST_mul18_float + (-1)*C8__Z4CNDFf_2_13_call_CAST_mul18<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_call_CAST_mul18



#Stuff for double 0x3FD9884533D43651
ConstantValue__16_fixbits = solver.IntVar(0, 31, 'ConstantValue__16_fixbits')
ConstantValue__16_fixp = solver.IntVar(0, 1, 'ConstantValue__16_fixp')
ConstantValue__16_float = solver.IntVar(0, 1, 'ConstantValue__16_float')
ConstantValue__16_double = solver.IntVar(0, 1, 'ConstantValue__16_double')
ConstantValue__16_enob = solver.IntVar(-10000, 10000, 'ConstantValue__16_enob')
solver.Add( + (1)*ConstantValue__16_enob + (-1)*ConstantValue__16_fixbits + (10000)*ConstantValue__16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul18 = fmul double %conv17, 0x3FD9884533D43651, !taffo.info !53, !taffo.initweight !30, !taffo.constinfo !55
ConstantValue__16_CAST_mul18_fixbits = solver.IntVar(0, 31, 'ConstantValue__16_CAST_mul18_fixbits')
ConstantValue__16_CAST_mul18_fixp = solver.IntVar(0, 1, 'ConstantValue__16_CAST_mul18_fixp')
ConstantValue__16_CAST_mul18_float = solver.IntVar(0, 1, 'ConstantValue__16_CAST_mul18_float')
ConstantValue__16_CAST_mul18_double = solver.IntVar(0, 1, 'ConstantValue__16_CAST_mul18_double')
solver.Add( + (1)*ConstantValue__16_CAST_mul18_fixp + (1)*ConstantValue__16_CAST_mul18_float + (1)*ConstantValue__16_CAST_mul18_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__16_CAST_mul18_fixbits + (-10000)*ConstantValue__16_CAST_mul18_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C1_ConstantValue__16_CAST_mul18')
C2_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C2_ConstantValue__16_CAST_mul18')
solver.Add( + (1)*ConstantValue__16_fixbits + (-1)*ConstantValue__16_CAST_mul18_fixbits + (-10000)*C1_ConstantValue__16_CAST_mul18<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__16_fixbits + (1)*ConstantValue__16_CAST_mul18_fixbits + (-10000)*C2_ConstantValue__16_CAST_mul18<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__16_CAST_mul18
castCostObj +=  + (1.13006)*C2_ConstantValue__16_CAST_mul18
C3_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C3_ConstantValue__16_CAST_mul18')
C4_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C4_ConstantValue__16_CAST_mul18')
C5_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C5_ConstantValue__16_CAST_mul18')
C6_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C6_ConstantValue__16_CAST_mul18')
C7_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C7_ConstantValue__16_CAST_mul18')
C8_ConstantValue__16_CAST_mul18 = solver.IntVar(0, 1, 'C8_ConstantValue__16_CAST_mul18')
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_mul18_float + (-1)*C3_ConstantValue__16_CAST_mul18<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__16_CAST_mul18
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_mul18_fixp + (-1)*C4_ConstantValue__16_CAST_mul18<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__16_CAST_mul18
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_CAST_mul18_double + (-1)*C5_ConstantValue__16_CAST_mul18<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__16_CAST_mul18
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_mul18_fixp + (-1)*C6_ConstantValue__16_CAST_mul18<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__16_CAST_mul18
solver.Add( + (1)*ConstantValue__16_float + (1)*ConstantValue__16_CAST_mul18_double + (-1)*C7_ConstantValue__16_CAST_mul18<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__16_CAST_mul18
solver.Add( + (1)*ConstantValue__16_double + (1)*ConstantValue__16_CAST_mul18_float + (-1)*C8_ConstantValue__16_CAST_mul18<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__16_CAST_mul18



#Stuff for   %mul18 = fmul double %conv17, 0x3FD9884533D43651, !taffo.info !53, !taffo.initweight !30, !taffo.constinfo !55
_Z4CNDFf_2_13_mul18_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_2_13_mul18_fixbits')
_Z4CNDFf_2_13_mul18_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul18_fixp')
_Z4CNDFf_2_13_mul18_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul18_float')
_Z4CNDFf_2_13_mul18_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul18_double')
_Z4CNDFf_2_13_mul18_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul18_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_enob + (-1)*_Z4CNDFf_2_13_mul18_fixbits + (10000)*_Z4CNDFf_2_13_mul18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_enob + (10000)*_Z4CNDFf_2_13_mul18_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_enob + (10000)*_Z4CNDFf_2_13_mul18_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_fixbits + (-10000)*_Z4CNDFf_2_13_mul18_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul18_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_fixp + (1)*_Z4CNDFf_2_13_mul18_float + (1)*_Z4CNDFf_2_13_mul18_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_fixbits + (-10000)*_Z4CNDFf_2_13_mul18_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_fixp + (-1)*ConstantValue__16_CAST_mul18_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_float + (-1)*ConstantValue__16_CAST_mul18_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_double + (-1)*ConstantValue__16_CAST_mul18_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_fixp + (-1)*_Z4CNDFf_2_13_mul18_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_float + (-1)*_Z4CNDFf_2_13_mul18_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_call_CAST_mul18_double + (-1)*_Z4CNDFf_2_13_mul18_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul18_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul18_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul18_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_enob + (-1)*ConstantValue__14_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_enob + (-1)*_Z4CNDFf_2_13_call_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul18_enob_2<=1)    #Enob: propagation in product 2



#Stuff for double 0x3FCDA6711871100E
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



#Stuff for double 0x3FCDA6711871100E
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



#Stuff for double 0x3FCDA6711871100E
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



#Constraint for cast for   %mul21 = fmul double 0x3FCDA6711871100E, %conv20, !taffo.info !61, !taffo.initweight !30, !taffo.constinfo !63
ConstantValue__19_CAST_mul21_fixbits = solver.IntVar(0, 31, 'ConstantValue__19_CAST_mul21_fixbits')
ConstantValue__19_CAST_mul21_fixp = solver.IntVar(0, 1, 'ConstantValue__19_CAST_mul21_fixp')
ConstantValue__19_CAST_mul21_float = solver.IntVar(0, 1, 'ConstantValue__19_CAST_mul21_float')
ConstantValue__19_CAST_mul21_double = solver.IntVar(0, 1, 'ConstantValue__19_CAST_mul21_double')
solver.Add( + (1)*ConstantValue__19_CAST_mul21_fixp + (1)*ConstantValue__19_CAST_mul21_float + (1)*ConstantValue__19_CAST_mul21_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__19_CAST_mul21_fixbits + (-10000)*ConstantValue__19_CAST_mul21_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C1_ConstantValue__19_CAST_mul21')
C2_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C2_ConstantValue__19_CAST_mul21')
solver.Add( + (1)*ConstantValue__19_fixbits + (-1)*ConstantValue__19_CAST_mul21_fixbits + (-10000)*C1_ConstantValue__19_CAST_mul21<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__19_fixbits + (1)*ConstantValue__19_CAST_mul21_fixbits + (-10000)*C2_ConstantValue__19_CAST_mul21<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__19_CAST_mul21
castCostObj +=  + (1.13006)*C2_ConstantValue__19_CAST_mul21
C3_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C3_ConstantValue__19_CAST_mul21')
C4_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C4_ConstantValue__19_CAST_mul21')
C5_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C5_ConstantValue__19_CAST_mul21')
C6_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C6_ConstantValue__19_CAST_mul21')
C7_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C7_ConstantValue__19_CAST_mul21')
C8_ConstantValue__19_CAST_mul21 = solver.IntVar(0, 1, 'C8_ConstantValue__19_CAST_mul21')
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_mul21_float + (-1)*C3_ConstantValue__19_CAST_mul21<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__19_CAST_mul21
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_mul21_fixp + (-1)*C4_ConstantValue__19_CAST_mul21<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__19_CAST_mul21
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_mul21_double + (-1)*C5_ConstantValue__19_CAST_mul21<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__19_CAST_mul21
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_mul21_fixp + (-1)*C6_ConstantValue__19_CAST_mul21<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__19_CAST_mul21
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_mul21_double + (-1)*C7_ConstantValue__19_CAST_mul21<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__19_CAST_mul21
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_mul21_float + (-1)*C8_ConstantValue__19_CAST_mul21<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__19_CAST_mul21



#Constraint for cast for   %mul21 = fmul double 0x3FCDA6711871100E, %conv20, !taffo.info !61, !taffo.initweight !30, !taffo.constinfo !63
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixbits')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixp')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_float')
_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_double')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixbits + (-10000)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixbits + (-10000)*C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_InputX_addr_0_fixbits + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixbits + (-10000)*C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21
C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21')
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_float + (-1)*C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixp + (-1)*C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_fixp + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_double + (-1)*C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixp + (-1)*C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_float + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_double + (-1)*C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_2_13_InputX_addr_0_double + (1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_float + (-1)*C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_InputX_addr_0_CAST_mul21



#Stuff for   %mul21 = fmul double 0x3FCDA6711871100E, %conv20, !taffo.info !61, !taffo.initweight !30, !taffo.constinfo !63
_Z4CNDFf_2_13_mul21_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_2_13_mul21_fixbits')
_Z4CNDFf_2_13_mul21_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul21_fixp')
_Z4CNDFf_2_13_mul21_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul21_float')
_Z4CNDFf_2_13_mul21_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul21_double')
_Z4CNDFf_2_13_mul21_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul21_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_enob + (-1)*_Z4CNDFf_2_13_mul21_fixbits + (10000)*_Z4CNDFf_2_13_mul21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_enob + (10000)*_Z4CNDFf_2_13_mul21_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_enob + (10000)*_Z4CNDFf_2_13_mul21_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_fixbits + (-10000)*_Z4CNDFf_2_13_mul21_fixp>=-9975)    #Limit the lower number of frac bits26
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul21_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_fixp + (1)*_Z4CNDFf_2_13_mul21_float + (1)*_Z4CNDFf_2_13_mul21_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_fixbits + (-10000)*_Z4CNDFf_2_13_mul21_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__19_CAST_mul21_fixp + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__19_CAST_mul21_float + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_float==0)    #float equality
solver.Add( + (1)*ConstantValue__19_CAST_mul21_double + (-1)*_Z4CNDFf_2_13_InputX_addr_0_CAST_mul21_double==0)    #double equality
solver.Add( + (1)*ConstantValue__19_CAST_mul21_fixp + (-1)*_Z4CNDFf_2_13_mul21_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__19_CAST_mul21_float + (-1)*_Z4CNDFf_2_13_mul21_float==0)    #float equality
solver.Add( + (1)*ConstantValue__19_CAST_mul21_double + (-1)*_Z4CNDFf_2_13_mul21_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul21_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul21_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul21_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_enob + (-1)*_Z4CNDFf_2_13_InputX_addr_0_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_1<=2)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_enob + (-1)*ConstantValue__17_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul21_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for double 1.000000e+00
ConstantValue__20_fixbits = solver.IntVar(0, 31, 'ConstantValue__20_fixbits')
ConstantValue__20_fixp = solver.IntVar(0, 1, 'ConstantValue__20_fixp')
ConstantValue__20_float = solver.IntVar(0, 1, 'ConstantValue__20_float')
ConstantValue__20_double = solver.IntVar(0, 1, 'ConstantValue__20_double')
ConstantValue__20_enob = solver.IntVar(-10000, 10000, 'ConstantValue__20_enob')
solver.Add( + (1)*ConstantValue__20_enob + (-1)*ConstantValue__20_fixbits + (10000)*ConstantValue__20_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_float + (1)*ConstantValue__20_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__21_fixbits = solver.IntVar(0, 31, 'ConstantValue__21_fixbits')
ConstantValue__21_fixp = solver.IntVar(0, 1, 'ConstantValue__21_fixp')
ConstantValue__21_float = solver.IntVar(0, 1, 'ConstantValue__21_float')
ConstantValue__21_double = solver.IntVar(0, 1, 'ConstantValue__21_double')
ConstantValue__21_enob = solver.IntVar(-10000, 10000, 'ConstantValue__21_enob')
solver.Add( + (1)*ConstantValue__21_enob + (-1)*ConstantValue__21_fixbits + (10000)*ConstantValue__21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__21_enob + (10000)*ConstantValue__21_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__21_fixp + (1)*ConstantValue__21_float + (1)*ConstantValue__21_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__21_fixbits + (-10000)*ConstantValue__21_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__22_fixbits = solver.IntVar(0, 31, 'ConstantValue__22_fixbits')
ConstantValue__22_fixp = solver.IntVar(0, 1, 'ConstantValue__22_fixp')
ConstantValue__22_float = solver.IntVar(0, 1, 'ConstantValue__22_float')
ConstantValue__22_double = solver.IntVar(0, 1, 'ConstantValue__22_double')
ConstantValue__22_enob = solver.IntVar(-10000, 10000, 'ConstantValue__22_enob')
solver.Add( + (1)*ConstantValue__22_enob + (-1)*ConstantValue__22_fixbits + (10000)*ConstantValue__22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_float + (1)*ConstantValue__22_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add = fadd double 1.000000e+00, %conv23, !taffo.info !68, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__22_CAST_add_fixbits = solver.IntVar(0, 31, 'ConstantValue__22_CAST_add_fixbits')
ConstantValue__22_CAST_add_fixp = solver.IntVar(0, 1, 'ConstantValue__22_CAST_add_fixp')
ConstantValue__22_CAST_add_float = solver.IntVar(0, 1, 'ConstantValue__22_CAST_add_float')
ConstantValue__22_CAST_add_double = solver.IntVar(0, 1, 'ConstantValue__22_CAST_add_double')
solver.Add( + (1)*ConstantValue__22_CAST_add_fixp + (1)*ConstantValue__22_CAST_add_float + (1)*ConstantValue__22_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__22_CAST_add_fixbits + (-10000)*ConstantValue__22_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C1_ConstantValue__22_CAST_add')
C2_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C2_ConstantValue__22_CAST_add')
solver.Add( + (1)*ConstantValue__22_fixbits + (-1)*ConstantValue__22_CAST_add_fixbits + (-10000)*C1_ConstantValue__22_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__22_fixbits + (1)*ConstantValue__22_CAST_add_fixbits + (-10000)*C2_ConstantValue__22_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__22_CAST_add
castCostObj +=  + (1.13006)*C2_ConstantValue__22_CAST_add
C3_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C3_ConstantValue__22_CAST_add')
C4_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C4_ConstantValue__22_CAST_add')
C5_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C5_ConstantValue__22_CAST_add')
C6_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C6_ConstantValue__22_CAST_add')
C7_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C7_ConstantValue__22_CAST_add')
C8_ConstantValue__22_CAST_add = solver.IntVar(0, 1, 'C8_ConstantValue__22_CAST_add')
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_CAST_add_float + (-1)*C3_ConstantValue__22_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__22_CAST_add
solver.Add( + (1)*ConstantValue__22_float + (1)*ConstantValue__22_CAST_add_fixp + (-1)*C4_ConstantValue__22_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__22_CAST_add
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_CAST_add_double + (-1)*C5_ConstantValue__22_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__22_CAST_add
solver.Add( + (1)*ConstantValue__22_double + (1)*ConstantValue__22_CAST_add_fixp + (-1)*C6_ConstantValue__22_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__22_CAST_add
solver.Add( + (1)*ConstantValue__22_float + (1)*ConstantValue__22_CAST_add_double + (-1)*C7_ConstantValue__22_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__22_CAST_add
solver.Add( + (1)*ConstantValue__22_double + (1)*ConstantValue__22_CAST_add_float + (-1)*C8_ConstantValue__22_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__22_CAST_add



#Constraint for cast for   %add = fadd double 1.000000e+00, %conv23, !taffo.info !68, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_mul21_CAST_add_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_2_13_mul21_CAST_add_fixbits')
_Z4CNDFf_2_13_mul21_CAST_add_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul21_CAST_add_fixp')
_Z4CNDFf_2_13_mul21_CAST_add_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul21_CAST_add_float')
_Z4CNDFf_2_13_mul21_CAST_add_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul21_CAST_add_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_CAST_add_fixp + (1)*_Z4CNDFf_2_13_mul21_CAST_add_float + (1)*_Z4CNDFf_2_13_mul21_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_CAST_add_fixbits + (-10000)*_Z4CNDFf_2_13_mul21_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul21_CAST_add')
C2__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul21_CAST_add')
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_fixbits + (-1)*_Z4CNDFf_2_13_mul21_CAST_add_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul21_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul21_fixbits + (1)*_Z4CNDFf_2_13_mul21_CAST_add_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul21_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul21_CAST_add
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul21_CAST_add
C3__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul21_CAST_add')
C4__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul21_CAST_add')
C5__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul21_CAST_add')
C6__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul21_CAST_add')
C7__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul21_CAST_add')
C8__Z4CNDFf_2_13_mul21_CAST_add = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul21_CAST_add')
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_fixp + (1)*_Z4CNDFf_2_13_mul21_CAST_add_float + (-1)*C3__Z4CNDFf_2_13_mul21_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_float + (1)*_Z4CNDFf_2_13_mul21_CAST_add_fixp + (-1)*C4__Z4CNDFf_2_13_mul21_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_fixp + (1)*_Z4CNDFf_2_13_mul21_CAST_add_double + (-1)*C5__Z4CNDFf_2_13_mul21_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_double + (1)*_Z4CNDFf_2_13_mul21_CAST_add_fixp + (-1)*C6__Z4CNDFf_2_13_mul21_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_float + (1)*_Z4CNDFf_2_13_mul21_CAST_add_double + (-1)*C7__Z4CNDFf_2_13_mul21_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_2_13_mul21_double + (1)*_Z4CNDFf_2_13_mul21_CAST_add_float + (-1)*C8__Z4CNDFf_2_13_mul21_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul21_CAST_add



#Stuff for   %add = fadd double 1.000000e+00, %conv23, !taffo.info !68, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_add_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_2_13_add_fixbits')
_Z4CNDFf_2_13_add_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add_fixp')
_Z4CNDFf_2_13_add_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add_float')
_Z4CNDFf_2_13_add_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add_double')
_Z4CNDFf_2_13_add_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_add_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_add_enob + (-1)*_Z4CNDFf_2_13_add_fixbits + (10000)*_Z4CNDFf_2_13_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_add_enob + (10000)*_Z4CNDFf_2_13_add_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_add_enob + (10000)*_Z4CNDFf_2_13_add_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_add_fixbits + (-10000)*_Z4CNDFf_2_13_add_fixp>=-9975)    #Limit the lower number of frac bits26
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_add_enob
solver.Add( + (1)*_Z4CNDFf_2_13_add_fixp + (1)*_Z4CNDFf_2_13_add_float + (1)*_Z4CNDFf_2_13_add_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_add_fixbits + (-10000)*_Z4CNDFf_2_13_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__22_CAST_add_fixp + (-1)*_Z4CNDFf_2_13_mul21_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__22_CAST_add_float + (-1)*_Z4CNDFf_2_13_mul21_CAST_add_float==0)    #float equality
solver.Add( + (1)*ConstantValue__22_CAST_add_double + (-1)*_Z4CNDFf_2_13_mul21_CAST_add_double==0)    #double equality
solver.Add( + (1)*ConstantValue__22_CAST_add_fixbits + (-1)*_Z4CNDFf_2_13_mul21_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__22_CAST_add_fixp + (-1)*_Z4CNDFf_2_13_add_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__22_CAST_add_float + (-1)*_Z4CNDFf_2_13_add_float==0)    #float equality
solver.Add( + (1)*ConstantValue__22_CAST_add_double + (-1)*_Z4CNDFf_2_13_add_double==0)    #double equality
solver.Add( + (1)*ConstantValue__22_CAST_add_fixbits + (-1)*_Z4CNDFf_2_13_add_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_add_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_add_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_add_double
solver.Add( + (1)*_Z4CNDFf_2_13_add_enob + (-1)*ConstantValue__20_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_2_13_add_enob + (-1)*_Z4CNDFf_2_13_mul21_enob<=0)    #Enob propagation in sum second addend



#Stuff for double 1.000000e+00
ConstantValue__23_fixbits = solver.IntVar(0, 31, 'ConstantValue__23_fixbits')
ConstantValue__23_fixp = solver.IntVar(0, 1, 'ConstantValue__23_fixp')
ConstantValue__23_float = solver.IntVar(0, 1, 'ConstantValue__23_float')
ConstantValue__23_double = solver.IntVar(0, 1, 'ConstantValue__23_double')
ConstantValue__23_enob = solver.IntVar(-10000, 10000, 'ConstantValue__23_enob')
solver.Add( + (1)*ConstantValue__23_enob + (-1)*ConstantValue__23_fixbits + (10000)*ConstantValue__23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_float + (1)*ConstantValue__23_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__24_fixbits = solver.IntVar(0, 31, 'ConstantValue__24_fixbits')
ConstantValue__24_fixp = solver.IntVar(0, 1, 'ConstantValue__24_fixp')
ConstantValue__24_float = solver.IntVar(0, 1, 'ConstantValue__24_float')
ConstantValue__24_double = solver.IntVar(0, 1, 'ConstantValue__24_double')
ConstantValue__24_enob = solver.IntVar(-10000, 10000, 'ConstantValue__24_enob')
solver.Add( + (1)*ConstantValue__24_enob + (-1)*ConstantValue__24_fixbits + (10000)*ConstantValue__24_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__24_enob + (10000)*ConstantValue__24_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__24_fixp + (1)*ConstantValue__24_float + (1)*ConstantValue__24_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__24_fixbits + (-10000)*ConstantValue__24_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__25_fixbits = solver.IntVar(0, 31, 'ConstantValue__25_fixbits')
ConstantValue__25_fixp = solver.IntVar(0, 1, 'ConstantValue__25_fixp')
ConstantValue__25_float = solver.IntVar(0, 1, 'ConstantValue__25_float')
ConstantValue__25_double = solver.IntVar(0, 1, 'ConstantValue__25_double')
ConstantValue__25_enob = solver.IntVar(-10000, 10000, 'ConstantValue__25_enob')
solver.Add( + (1)*ConstantValue__25_enob + (-1)*ConstantValue__25_fixbits + (10000)*ConstantValue__25_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__25_enob + (10000)*ConstantValue__25_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__25_enob + (10000)*ConstantValue__25_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__25_fixbits + (-10000)*ConstantValue__25_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_float + (1)*ConstantValue__25_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__25_fixbits + (-10000)*ConstantValue__25_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double 1.000000e+00, %conv25, !taffo.info !73, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__25_CAST_div_fixbits = solver.IntVar(0, 31, 'ConstantValue__25_CAST_div_fixbits')
ConstantValue__25_CAST_div_fixp = solver.IntVar(0, 1, 'ConstantValue__25_CAST_div_fixp')
ConstantValue__25_CAST_div_float = solver.IntVar(0, 1, 'ConstantValue__25_CAST_div_float')
ConstantValue__25_CAST_div_double = solver.IntVar(0, 1, 'ConstantValue__25_CAST_div_double')
solver.Add( + (1)*ConstantValue__25_CAST_div_fixp + (1)*ConstantValue__25_CAST_div_float + (1)*ConstantValue__25_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__25_CAST_div_fixbits + (-10000)*ConstantValue__25_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C1_ConstantValue__25_CAST_div')
C2_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C2_ConstantValue__25_CAST_div')
solver.Add( + (1)*ConstantValue__25_fixbits + (-1)*ConstantValue__25_CAST_div_fixbits + (-10000)*C1_ConstantValue__25_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__25_fixbits + (1)*ConstantValue__25_CAST_div_fixbits + (-10000)*C2_ConstantValue__25_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__25_CAST_div
castCostObj +=  + (1.13006)*C2_ConstantValue__25_CAST_div
C3_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C3_ConstantValue__25_CAST_div')
C4_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C4_ConstantValue__25_CAST_div')
C5_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C5_ConstantValue__25_CAST_div')
C6_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C6_ConstantValue__25_CAST_div')
C7_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C7_ConstantValue__25_CAST_div')
C8_ConstantValue__25_CAST_div = solver.IntVar(0, 1, 'C8_ConstantValue__25_CAST_div')
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_CAST_div_float + (-1)*C3_ConstantValue__25_CAST_div<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__25_CAST_div
solver.Add( + (1)*ConstantValue__25_float + (1)*ConstantValue__25_CAST_div_fixp + (-1)*C4_ConstantValue__25_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__25_CAST_div
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_CAST_div_double + (-1)*C5_ConstantValue__25_CAST_div<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__25_CAST_div
solver.Add( + (1)*ConstantValue__25_double + (1)*ConstantValue__25_CAST_div_fixp + (-1)*C6_ConstantValue__25_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__25_CAST_div
solver.Add( + (1)*ConstantValue__25_float + (1)*ConstantValue__25_CAST_div_double + (-1)*C7_ConstantValue__25_CAST_div<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__25_CAST_div
solver.Add( + (1)*ConstantValue__25_double + (1)*ConstantValue__25_CAST_div_float + (-1)*C8_ConstantValue__25_CAST_div<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__25_CAST_div



#Constraint for cast for   %div = fdiv double 1.000000e+00, %conv25, !taffo.info !73, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_add_CAST_div_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_2_13_add_CAST_div_fixbits')
_Z4CNDFf_2_13_add_CAST_div_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add_CAST_div_fixp')
_Z4CNDFf_2_13_add_CAST_div_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add_CAST_div_float')
_Z4CNDFf_2_13_add_CAST_div_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add_CAST_div_double')
solver.Add( + (1)*_Z4CNDFf_2_13_add_CAST_div_fixp + (1)*_Z4CNDFf_2_13_add_CAST_div_float + (1)*_Z4CNDFf_2_13_add_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_add_CAST_div_fixbits + (-10000)*_Z4CNDFf_2_13_add_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_add_CAST_div')
C2__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_add_CAST_div')
solver.Add( + (1)*_Z4CNDFf_2_13_add_fixbits + (-1)*_Z4CNDFf_2_13_add_CAST_div_fixbits + (-10000)*C1__Z4CNDFf_2_13_add_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_add_fixbits + (1)*_Z4CNDFf_2_13_add_CAST_div_fixbits + (-10000)*C2__Z4CNDFf_2_13_add_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_add_CAST_div
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_add_CAST_div
C3__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_add_CAST_div')
C4__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_add_CAST_div')
C5__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_add_CAST_div')
C6__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_add_CAST_div')
C7__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_add_CAST_div')
C8__Z4CNDFf_2_13_add_CAST_div = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_add_CAST_div')
solver.Add( + (1)*_Z4CNDFf_2_13_add_fixp + (1)*_Z4CNDFf_2_13_add_CAST_div_float + (-1)*C3__Z4CNDFf_2_13_add_CAST_div<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_2_13_add_float + (1)*_Z4CNDFf_2_13_add_CAST_div_fixp + (-1)*C4__Z4CNDFf_2_13_add_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_2_13_add_fixp + (1)*_Z4CNDFf_2_13_add_CAST_div_double + (-1)*C5__Z4CNDFf_2_13_add_CAST_div<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_2_13_add_double + (1)*_Z4CNDFf_2_13_add_CAST_div_fixp + (-1)*C6__Z4CNDFf_2_13_add_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_2_13_add_float + (1)*_Z4CNDFf_2_13_add_CAST_div_double + (-1)*C7__Z4CNDFf_2_13_add_CAST_div<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_2_13_add_double + (1)*_Z4CNDFf_2_13_add_CAST_div_float + (-1)*C8__Z4CNDFf_2_13_add_CAST_div<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_add_CAST_div



#Stuff for   %div = fdiv double 1.000000e+00, %conv25, !taffo.info !73, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_div_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_div_fixbits')
_Z4CNDFf_2_13_div_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_fixp')
_Z4CNDFf_2_13_div_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_float')
_Z4CNDFf_2_13_div_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_double')
_Z4CNDFf_2_13_div_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_div_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_div_enob + (-1)*_Z4CNDFf_2_13_div_fixbits + (10000)*_Z4CNDFf_2_13_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_div_enob + (10000)*_Z4CNDFf_2_13_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_div_enob + (10000)*_Z4CNDFf_2_13_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-10000)*_Z4CNDFf_2_13_div_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_div_enob
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-10000)*_Z4CNDFf_2_13_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__25_CAST_div_fixp + (-1)*_Z4CNDFf_2_13_add_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__25_CAST_div_float + (-1)*_Z4CNDFf_2_13_add_CAST_div_float==0)    #float equality
solver.Add( + (1)*ConstantValue__25_CAST_div_double + (-1)*_Z4CNDFf_2_13_add_CAST_div_double==0)    #double equality
solver.Add( + (1)*ConstantValue__25_CAST_div_fixp + (-1)*_Z4CNDFf_2_13_div_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__25_CAST_div_float + (-1)*_Z4CNDFf_2_13_div_float==0)    #float equality
solver.Add( + (1)*ConstantValue__25_CAST_div_double + (-1)*_Z4CNDFf_2_13_div_double==0)    #double equality
mathCostObj +=  + (3.45438)*_Z4CNDFf_2_13_div_fixp
mathCostObj +=  + (4.13283)*_Z4CNDFf_2_13_div_float
mathCostObj +=  + (5.68177)*_Z4CNDFf_2_13_div_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_div_enob + (-1)*_Z4CNDFf_2_13_add_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_1<=10)    #Enob: propagation in division 1
solver.Add( + (1)*_Z4CNDFf_2_13_div_enob + (-1)*ConstantValue__23_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_div_enob_2<=1034)    #Enob: propagation in division 2



#Constraint for cast for   %mul27 = fmul float %conv26, %conv26, !taffo.info !77, !taffo.initweight !23
_Z4CNDFf_2_13_div_CAST_mul27_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_div_CAST_mul27_fixbits')
_Z4CNDFf_2_13_div_CAST_mul27_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul27_fixp')
_Z4CNDFf_2_13_div_CAST_mul27_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul27_float')
_Z4CNDFf_2_13_div_CAST_mul27_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul27_double')
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul27_float + (1)*_Z4CNDFf_2_13_div_CAST_mul27_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_fixbits + (-10000)*_Z4CNDFf_2_13_div_CAST_mul27_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_div_CAST_mul27')
C2__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_div_CAST_mul27')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-1)*_Z4CNDFf_2_13_div_CAST_mul27_fixbits + (-10000)*C1__Z4CNDFf_2_13_div_CAST_mul27<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_div_fixbits + (1)*_Z4CNDFf_2_13_div_CAST_mul27_fixbits + (-10000)*C2__Z4CNDFf_2_13_div_CAST_mul27<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_div_CAST_mul27
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_div_CAST_mul27
C3__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_div_CAST_mul27')
C4__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_div_CAST_mul27')
C5__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_div_CAST_mul27')
C6__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_div_CAST_mul27')
C7__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_div_CAST_mul27')
C8__Z4CNDFf_2_13_div_CAST_mul27 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_div_CAST_mul27')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul27_float + (-1)*C3__Z4CNDFf_2_13_div_CAST_mul27<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul27_fixp + (-1)*C4__Z4CNDFf_2_13_div_CAST_mul27<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul27_double + (-1)*C5__Z4CNDFf_2_13_div_CAST_mul27<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul27_fixp + (-1)*C6__Z4CNDFf_2_13_div_CAST_mul27<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul27_double + (-1)*C7__Z4CNDFf_2_13_div_CAST_mul27<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul27_float + (-1)*C8__Z4CNDFf_2_13_div_CAST_mul27<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_div_CAST_mul27



#Constraint for cast for   %mul27 = fmul float %conv26, %conv26, !taffo.info !77, !taffo.initweight !23
_Z4CNDFf_2_13_div_CAST_mul27_0_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_div_CAST_mul27_0_fixbits')
_Z4CNDFf_2_13_div_CAST_mul27_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul27_0_fixp')
_Z4CNDFf_2_13_div_CAST_mul27_0_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul27_0_float')
_Z4CNDFf_2_13_div_CAST_mul27_0_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul27_0_double')
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_float + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixbits + (-10000)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_div_CAST_mul27_0')
C2__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_div_CAST_mul27_0')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-1)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixbits + (-10000)*C1__Z4CNDFf_2_13_div_CAST_mul27_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_div_fixbits + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixbits + (-10000)*C2__Z4CNDFf_2_13_div_CAST_mul27_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_div_CAST_mul27_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_div_CAST_mul27_0
C3__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_div_CAST_mul27_0')
C4__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_div_CAST_mul27_0')
C5__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_div_CAST_mul27_0')
C6__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_div_CAST_mul27_0')
C7__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_div_CAST_mul27_0')
C8__Z4CNDFf_2_13_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_div_CAST_mul27_0')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_float + (-1)*C3__Z4CNDFf_2_13_div_CAST_mul27_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixp + (-1)*C4__Z4CNDFf_2_13_div_CAST_mul27_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_double + (-1)*C5__Z4CNDFf_2_13_div_CAST_mul27_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixp + (-1)*C6__Z4CNDFf_2_13_div_CAST_mul27_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_double + (-1)*C7__Z4CNDFf_2_13_div_CAST_mul27_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul27_0_float + (-1)*C8__Z4CNDFf_2_13_div_CAST_mul27_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_div_CAST_mul27_0



#Stuff for   %mul27 = fmul float %conv26, %conv26, !taffo.info !77, !taffo.initweight !23
_Z4CNDFf_2_13_mul27_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_2_13_mul27_fixbits')
_Z4CNDFf_2_13_mul27_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_fixp')
_Z4CNDFf_2_13_mul27_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_float')
_Z4CNDFf_2_13_mul27_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_double')
_Z4CNDFf_2_13_mul27_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul27_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_enob + (-1)*_Z4CNDFf_2_13_mul27_fixbits + (10000)*_Z4CNDFf_2_13_mul27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_enob + (10000)*_Z4CNDFf_2_13_mul27_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_enob + (10000)*_Z4CNDFf_2_13_mul27_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixbits + (-10000)*_Z4CNDFf_2_13_mul27_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul27_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixp + (1)*_Z4CNDFf_2_13_mul27_float + (1)*_Z4CNDFf_2_13_mul27_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixbits + (-10000)*_Z4CNDFf_2_13_mul27_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_fixp + (-1)*_Z4CNDFf_2_13_div_CAST_mul27_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_float + (-1)*_Z4CNDFf_2_13_div_CAST_mul27_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_double + (-1)*_Z4CNDFf_2_13_div_CAST_mul27_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_fixp + (-1)*_Z4CNDFf_2_13_mul27_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_float + (-1)*_Z4CNDFf_2_13_mul27_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul27_double + (-1)*_Z4CNDFf_2_13_mul27_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul27_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul27_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul27_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_enob + (-1)*_Z4CNDFf_2_13_div_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_enob + (-1)*_Z4CNDFf_2_13_div_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul27_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul28 = fmul float %mul27, %conv26, !taffo.info !79, !taffo.initweight !23
_Z4CNDFf_2_13_mul27_CAST_mul28_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_2_13_mul27_CAST_mul28_fixbits')
_Z4CNDFf_2_13_mul27_CAST_mul28_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_CAST_mul28_fixp')
_Z4CNDFf_2_13_mul27_CAST_mul28_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_CAST_mul28_float')
_Z4CNDFf_2_13_mul27_CAST_mul28_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_CAST_mul28_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixp + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_float + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixbits + (-10000)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul27_CAST_mul28')
C2__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul27_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixbits + (-1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul27_CAST_mul28<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul27_fixbits + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul27_CAST_mul28<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul27_CAST_mul28
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul27_CAST_mul28
C3__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul27_CAST_mul28')
C4__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul27_CAST_mul28')
C5__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul27_CAST_mul28')
C6__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul27_CAST_mul28')
C7__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul27_CAST_mul28')
C8__Z4CNDFf_2_13_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul27_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixp + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_float + (-1)*C3__Z4CNDFf_2_13_mul27_CAST_mul28<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_float + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixp + (-1)*C4__Z4CNDFf_2_13_mul27_CAST_mul28<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixp + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_double + (-1)*C5__Z4CNDFf_2_13_mul27_CAST_mul28<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_double + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixp + (-1)*C6__Z4CNDFf_2_13_mul27_CAST_mul28<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_float + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_double + (-1)*C7__Z4CNDFf_2_13_mul27_CAST_mul28<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_double + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_float + (-1)*C8__Z4CNDFf_2_13_mul27_CAST_mul28<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul27_CAST_mul28



#Constraint for cast for   %mul28 = fmul float %mul27, %conv26, !taffo.info !79, !taffo.initweight !23
_Z4CNDFf_2_13_div_CAST_mul28_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_div_CAST_mul28_fixbits')
_Z4CNDFf_2_13_div_CAST_mul28_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul28_fixp')
_Z4CNDFf_2_13_div_CAST_mul28_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul28_float')
_Z4CNDFf_2_13_div_CAST_mul28_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul28_double')
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul28_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul28_float + (1)*_Z4CNDFf_2_13_div_CAST_mul28_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul28_fixbits + (-10000)*_Z4CNDFf_2_13_div_CAST_mul28_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_div_CAST_mul28')
C2__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_div_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-1)*_Z4CNDFf_2_13_div_CAST_mul28_fixbits + (-10000)*C1__Z4CNDFf_2_13_div_CAST_mul28<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_div_fixbits + (1)*_Z4CNDFf_2_13_div_CAST_mul28_fixbits + (-10000)*C2__Z4CNDFf_2_13_div_CAST_mul28<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_div_CAST_mul28
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_div_CAST_mul28
C3__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_div_CAST_mul28')
C4__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_div_CAST_mul28')
C5__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_div_CAST_mul28')
C6__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_div_CAST_mul28')
C7__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_div_CAST_mul28')
C8__Z4CNDFf_2_13_div_CAST_mul28 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_div_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul28_float + (-1)*C3__Z4CNDFf_2_13_div_CAST_mul28<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul28_fixp + (-1)*C4__Z4CNDFf_2_13_div_CAST_mul28<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul28_double + (-1)*C5__Z4CNDFf_2_13_div_CAST_mul28<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul28_fixp + (-1)*C6__Z4CNDFf_2_13_div_CAST_mul28<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul28_double + (-1)*C7__Z4CNDFf_2_13_div_CAST_mul28<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul28_float + (-1)*C8__Z4CNDFf_2_13_div_CAST_mul28<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_div_CAST_mul28



#Stuff for   %mul28 = fmul float %mul27, %conv26, !taffo.info !79, !taffo.initweight !23
_Z4CNDFf_2_13_mul28_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul28_fixbits')
_Z4CNDFf_2_13_mul28_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_fixp')
_Z4CNDFf_2_13_mul28_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_float')
_Z4CNDFf_2_13_mul28_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_double')
_Z4CNDFf_2_13_mul28_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul28_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_enob + (-1)*_Z4CNDFf_2_13_mul28_fixbits + (10000)*_Z4CNDFf_2_13_mul28_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_enob + (10000)*_Z4CNDFf_2_13_mul28_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_enob + (10000)*_Z4CNDFf_2_13_mul28_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixbits + (-10000)*_Z4CNDFf_2_13_mul28_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul28_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixp + (1)*_Z4CNDFf_2_13_mul28_float + (1)*_Z4CNDFf_2_13_mul28_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixbits + (-10000)*_Z4CNDFf_2_13_mul28_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixp + (-1)*_Z4CNDFf_2_13_div_CAST_mul28_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_float + (-1)*_Z4CNDFf_2_13_div_CAST_mul28_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_double + (-1)*_Z4CNDFf_2_13_div_CAST_mul28_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_fixp + (-1)*_Z4CNDFf_2_13_mul28_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_float + (-1)*_Z4CNDFf_2_13_mul28_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul28_double + (-1)*_Z4CNDFf_2_13_mul28_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul28_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul28_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul28_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_enob + (-1)*_Z4CNDFf_2_13_div_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_enob + (-1)*_Z4CNDFf_2_13_mul27_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul28_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul29 = fmul float %mul28, %conv26, !taffo.info !81, !taffo.initweight !23
_Z4CNDFf_2_13_mul28_CAST_mul29_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul28_CAST_mul29_fixbits')
_Z4CNDFf_2_13_mul28_CAST_mul29_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_CAST_mul29_fixp')
_Z4CNDFf_2_13_mul28_CAST_mul29_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_CAST_mul29_float')
_Z4CNDFf_2_13_mul28_CAST_mul29_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_CAST_mul29_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixp + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_float + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixbits + (-10000)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul28_CAST_mul29')
C2__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul28_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixbits + (-1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul28_CAST_mul29<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul28_fixbits + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul28_CAST_mul29<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul28_CAST_mul29
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul28_CAST_mul29
C3__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul28_CAST_mul29')
C4__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul28_CAST_mul29')
C5__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul28_CAST_mul29')
C6__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul28_CAST_mul29')
C7__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul28_CAST_mul29')
C8__Z4CNDFf_2_13_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul28_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixp + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_float + (-1)*C3__Z4CNDFf_2_13_mul28_CAST_mul29<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_float + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixp + (-1)*C4__Z4CNDFf_2_13_mul28_CAST_mul29<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixp + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_double + (-1)*C5__Z4CNDFf_2_13_mul28_CAST_mul29<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_double + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixp + (-1)*C6__Z4CNDFf_2_13_mul28_CAST_mul29<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_float + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_double + (-1)*C7__Z4CNDFf_2_13_mul28_CAST_mul29<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_double + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_float + (-1)*C8__Z4CNDFf_2_13_mul28_CAST_mul29<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul28_CAST_mul29



#Constraint for cast for   %mul29 = fmul float %mul28, %conv26, !taffo.info !81, !taffo.initweight !23
_Z4CNDFf_2_13_div_CAST_mul29_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_div_CAST_mul29_fixbits')
_Z4CNDFf_2_13_div_CAST_mul29_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul29_fixp')
_Z4CNDFf_2_13_div_CAST_mul29_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul29_float')
_Z4CNDFf_2_13_div_CAST_mul29_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul29_double')
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul29_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul29_float + (1)*_Z4CNDFf_2_13_div_CAST_mul29_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul29_fixbits + (-10000)*_Z4CNDFf_2_13_div_CAST_mul29_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_div_CAST_mul29')
C2__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_div_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-1)*_Z4CNDFf_2_13_div_CAST_mul29_fixbits + (-10000)*C1__Z4CNDFf_2_13_div_CAST_mul29<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_div_fixbits + (1)*_Z4CNDFf_2_13_div_CAST_mul29_fixbits + (-10000)*C2__Z4CNDFf_2_13_div_CAST_mul29<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_div_CAST_mul29
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_div_CAST_mul29
C3__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_div_CAST_mul29')
C4__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_div_CAST_mul29')
C5__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_div_CAST_mul29')
C6__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_div_CAST_mul29')
C7__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_div_CAST_mul29')
C8__Z4CNDFf_2_13_div_CAST_mul29 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_div_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul29_float + (-1)*C3__Z4CNDFf_2_13_div_CAST_mul29<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul29_fixp + (-1)*C4__Z4CNDFf_2_13_div_CAST_mul29<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul29_double + (-1)*C5__Z4CNDFf_2_13_div_CAST_mul29<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul29_fixp + (-1)*C6__Z4CNDFf_2_13_div_CAST_mul29<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul29_double + (-1)*C7__Z4CNDFf_2_13_div_CAST_mul29<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul29_float + (-1)*C8__Z4CNDFf_2_13_div_CAST_mul29<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_div_CAST_mul29



#Stuff for   %mul29 = fmul float %mul28, %conv26, !taffo.info !81, !taffo.initweight !23
_Z4CNDFf_2_13_mul29_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul29_fixbits')
_Z4CNDFf_2_13_mul29_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_fixp')
_Z4CNDFf_2_13_mul29_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_float')
_Z4CNDFf_2_13_mul29_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_double')
_Z4CNDFf_2_13_mul29_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul29_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_enob + (-1)*_Z4CNDFf_2_13_mul29_fixbits + (10000)*_Z4CNDFf_2_13_mul29_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_enob + (10000)*_Z4CNDFf_2_13_mul29_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_enob + (10000)*_Z4CNDFf_2_13_mul29_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixbits + (-10000)*_Z4CNDFf_2_13_mul29_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul29_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixp + (1)*_Z4CNDFf_2_13_mul29_float + (1)*_Z4CNDFf_2_13_mul29_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixbits + (-10000)*_Z4CNDFf_2_13_mul29_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixp + (-1)*_Z4CNDFf_2_13_div_CAST_mul29_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_float + (-1)*_Z4CNDFf_2_13_div_CAST_mul29_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_double + (-1)*_Z4CNDFf_2_13_div_CAST_mul29_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_fixp + (-1)*_Z4CNDFf_2_13_mul29_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_float + (-1)*_Z4CNDFf_2_13_mul29_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul29_double + (-1)*_Z4CNDFf_2_13_mul29_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul29_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul29_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul29_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_enob + (-1)*_Z4CNDFf_2_13_div_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_enob + (-1)*_Z4CNDFf_2_13_mul28_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul29_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul30 = fmul float %mul29, %conv26, !taffo.info !83, !taffo.initweight !23
_Z4CNDFf_2_13_mul29_CAST_mul30_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul29_CAST_mul30_fixbits')
_Z4CNDFf_2_13_mul29_CAST_mul30_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_CAST_mul30_fixp')
_Z4CNDFf_2_13_mul29_CAST_mul30_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_CAST_mul30_float')
_Z4CNDFf_2_13_mul29_CAST_mul30_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_CAST_mul30_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixp + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_float + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixbits + (-10000)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul29_CAST_mul30')
C2__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul29_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixbits + (-1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul29_CAST_mul30<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul29_fixbits + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul29_CAST_mul30<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul29_CAST_mul30
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul29_CAST_mul30
C3__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul29_CAST_mul30')
C4__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul29_CAST_mul30')
C5__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul29_CAST_mul30')
C6__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul29_CAST_mul30')
C7__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul29_CAST_mul30')
C8__Z4CNDFf_2_13_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul29_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixp + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_float + (-1)*C3__Z4CNDFf_2_13_mul29_CAST_mul30<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_float + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixp + (-1)*C4__Z4CNDFf_2_13_mul29_CAST_mul30<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixp + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_double + (-1)*C5__Z4CNDFf_2_13_mul29_CAST_mul30<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_double + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixp + (-1)*C6__Z4CNDFf_2_13_mul29_CAST_mul30<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_float + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_double + (-1)*C7__Z4CNDFf_2_13_mul29_CAST_mul30<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_double + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_float + (-1)*C8__Z4CNDFf_2_13_mul29_CAST_mul30<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul29_CAST_mul30



#Constraint for cast for   %mul30 = fmul float %mul29, %conv26, !taffo.info !83, !taffo.initweight !23
_Z4CNDFf_2_13_div_CAST_mul30_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_div_CAST_mul30_fixbits')
_Z4CNDFf_2_13_div_CAST_mul30_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul30_fixp')
_Z4CNDFf_2_13_div_CAST_mul30_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul30_float')
_Z4CNDFf_2_13_div_CAST_mul30_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul30_double')
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul30_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul30_float + (1)*_Z4CNDFf_2_13_div_CAST_mul30_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul30_fixbits + (-10000)*_Z4CNDFf_2_13_div_CAST_mul30_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_div_CAST_mul30')
C2__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_div_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-1)*_Z4CNDFf_2_13_div_CAST_mul30_fixbits + (-10000)*C1__Z4CNDFf_2_13_div_CAST_mul30<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_div_fixbits + (1)*_Z4CNDFf_2_13_div_CAST_mul30_fixbits + (-10000)*C2__Z4CNDFf_2_13_div_CAST_mul30<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_div_CAST_mul30
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_div_CAST_mul30
C3__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_div_CAST_mul30')
C4__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_div_CAST_mul30')
C5__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_div_CAST_mul30')
C6__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_div_CAST_mul30')
C7__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_div_CAST_mul30')
C8__Z4CNDFf_2_13_div_CAST_mul30 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_div_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul30_float + (-1)*C3__Z4CNDFf_2_13_div_CAST_mul30<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul30_fixp + (-1)*C4__Z4CNDFf_2_13_div_CAST_mul30<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul30_double + (-1)*C5__Z4CNDFf_2_13_div_CAST_mul30<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul30_fixp + (-1)*C6__Z4CNDFf_2_13_div_CAST_mul30<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul30_double + (-1)*C7__Z4CNDFf_2_13_div_CAST_mul30<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul30_float + (-1)*C8__Z4CNDFf_2_13_div_CAST_mul30<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_div_CAST_mul30



#Stuff for   %mul30 = fmul float %mul29, %conv26, !taffo.info !83, !taffo.initweight !23
_Z4CNDFf_2_13_mul30_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul30_fixbits')
_Z4CNDFf_2_13_mul30_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul30_fixp')
_Z4CNDFf_2_13_mul30_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul30_float')
_Z4CNDFf_2_13_mul30_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul30_double')
_Z4CNDFf_2_13_mul30_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul30_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_enob + (-1)*_Z4CNDFf_2_13_mul30_fixbits + (10000)*_Z4CNDFf_2_13_mul30_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_enob + (10000)*_Z4CNDFf_2_13_mul30_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_enob + (10000)*_Z4CNDFf_2_13_mul30_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_fixbits + (-10000)*_Z4CNDFf_2_13_mul30_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul30_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_fixp + (1)*_Z4CNDFf_2_13_mul30_float + (1)*_Z4CNDFf_2_13_mul30_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_fixbits + (-10000)*_Z4CNDFf_2_13_mul30_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixp + (-1)*_Z4CNDFf_2_13_div_CAST_mul30_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_float + (-1)*_Z4CNDFf_2_13_div_CAST_mul30_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_double + (-1)*_Z4CNDFf_2_13_div_CAST_mul30_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_fixp + (-1)*_Z4CNDFf_2_13_mul30_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_float + (-1)*_Z4CNDFf_2_13_mul30_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul30_double + (-1)*_Z4CNDFf_2_13_mul30_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul30_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul30_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul30_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_enob + (-1)*_Z4CNDFf_2_13_div_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_enob + (-1)*_Z4CNDFf_2_13_mul29_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul30_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for double 0x3FD470BF3A92F8EC
ConstantValue__26_fixbits = solver.IntVar(0, 31, 'ConstantValue__26_fixbits')
ConstantValue__26_fixp = solver.IntVar(0, 1, 'ConstantValue__26_fixp')
ConstantValue__26_float = solver.IntVar(0, 1, 'ConstantValue__26_float')
ConstantValue__26_double = solver.IntVar(0, 1, 'ConstantValue__26_double')
ConstantValue__26_enob = solver.IntVar(-10000, 10000, 'ConstantValue__26_enob')
solver.Add( + (1)*ConstantValue__26_enob + (-1)*ConstantValue__26_fixbits + (10000)*ConstantValue__26_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__26_fixp + (1)*ConstantValue__26_float + (1)*ConstantValue__26_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FD470BF3A92F8EC
ConstantValue__27_fixbits = solver.IntVar(0, 31, 'ConstantValue__27_fixbits')
ConstantValue__27_fixp = solver.IntVar(0, 1, 'ConstantValue__27_fixp')
ConstantValue__27_float = solver.IntVar(0, 1, 'ConstantValue__27_float')
ConstantValue__27_double = solver.IntVar(0, 1, 'ConstantValue__27_double')
ConstantValue__27_enob = solver.IntVar(-10000, 10000, 'ConstantValue__27_enob')
solver.Add( + (1)*ConstantValue__27_enob + (-1)*ConstantValue__27_fixbits + (10000)*ConstantValue__27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__27_fixp + (1)*ConstantValue__27_float + (1)*ConstantValue__27_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul32 = fmul double %conv31, 0x3FD470BF3A92F8EC, !taffo.info !85, !taffo.initweight !30, !taffo.constinfo !87
_Z4CNDFf_2_13_div_CAST_mul32_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_div_CAST_mul32_fixbits')
_Z4CNDFf_2_13_div_CAST_mul32_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul32_fixp')
_Z4CNDFf_2_13_div_CAST_mul32_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul32_float')
_Z4CNDFf_2_13_div_CAST_mul32_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_div_CAST_mul32_double')
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul32_float + (1)*_Z4CNDFf_2_13_div_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_fixbits + (-10000)*_Z4CNDFf_2_13_div_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_div_CAST_mul32')
C2__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_div_CAST_mul32')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixbits + (-1)*_Z4CNDFf_2_13_div_CAST_mul32_fixbits + (-10000)*C1__Z4CNDFf_2_13_div_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_div_fixbits + (1)*_Z4CNDFf_2_13_div_CAST_mul32_fixbits + (-10000)*C2__Z4CNDFf_2_13_div_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_div_CAST_mul32
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_div_CAST_mul32
C3__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_div_CAST_mul32')
C4__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_div_CAST_mul32')
C5__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_div_CAST_mul32')
C6__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_div_CAST_mul32')
C7__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_div_CAST_mul32')
C8__Z4CNDFf_2_13_div_CAST_mul32 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_div_CAST_mul32')
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul32_float + (-1)*C3__Z4CNDFf_2_13_div_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul32_fixp + (-1)*C4__Z4CNDFf_2_13_div_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_2_13_div_fixp + (1)*_Z4CNDFf_2_13_div_CAST_mul32_double + (-1)*C5__Z4CNDFf_2_13_div_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul32_fixp + (-1)*C6__Z4CNDFf_2_13_div_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_2_13_div_float + (1)*_Z4CNDFf_2_13_div_CAST_mul32_double + (-1)*C7__Z4CNDFf_2_13_div_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_2_13_div_double + (1)*_Z4CNDFf_2_13_div_CAST_mul32_float + (-1)*C8__Z4CNDFf_2_13_div_CAST_mul32<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_div_CAST_mul32



#Stuff for double 0x3FD470BF3A92F8EC
ConstantValue__28_fixbits = solver.IntVar(0, 31, 'ConstantValue__28_fixbits')
ConstantValue__28_fixp = solver.IntVar(0, 1, 'ConstantValue__28_fixp')
ConstantValue__28_float = solver.IntVar(0, 1, 'ConstantValue__28_float')
ConstantValue__28_double = solver.IntVar(0, 1, 'ConstantValue__28_double')
ConstantValue__28_enob = solver.IntVar(-10000, 10000, 'ConstantValue__28_enob')
solver.Add( + (1)*ConstantValue__28_enob + (-1)*ConstantValue__28_fixbits + (10000)*ConstantValue__28_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_float + (1)*ConstantValue__28_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul32 = fmul double %conv31, 0x3FD470BF3A92F8EC, !taffo.info !85, !taffo.initweight !30, !taffo.constinfo !87
ConstantValue__28_CAST_mul32_fixbits = solver.IntVar(0, 31, 'ConstantValue__28_CAST_mul32_fixbits')
ConstantValue__28_CAST_mul32_fixp = solver.IntVar(0, 1, 'ConstantValue__28_CAST_mul32_fixp')
ConstantValue__28_CAST_mul32_float = solver.IntVar(0, 1, 'ConstantValue__28_CAST_mul32_float')
ConstantValue__28_CAST_mul32_double = solver.IntVar(0, 1, 'ConstantValue__28_CAST_mul32_double')
solver.Add( + (1)*ConstantValue__28_CAST_mul32_fixp + (1)*ConstantValue__28_CAST_mul32_float + (1)*ConstantValue__28_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__28_CAST_mul32_fixbits + (-10000)*ConstantValue__28_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C1_ConstantValue__28_CAST_mul32')
C2_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C2_ConstantValue__28_CAST_mul32')
solver.Add( + (1)*ConstantValue__28_fixbits + (-1)*ConstantValue__28_CAST_mul32_fixbits + (-10000)*C1_ConstantValue__28_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__28_fixbits + (1)*ConstantValue__28_CAST_mul32_fixbits + (-10000)*C2_ConstantValue__28_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__28_CAST_mul32
castCostObj +=  + (1.13006)*C2_ConstantValue__28_CAST_mul32
C3_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C3_ConstantValue__28_CAST_mul32')
C4_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C4_ConstantValue__28_CAST_mul32')
C5_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C5_ConstantValue__28_CAST_mul32')
C6_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C6_ConstantValue__28_CAST_mul32')
C7_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C7_ConstantValue__28_CAST_mul32')
C8_ConstantValue__28_CAST_mul32 = solver.IntVar(0, 1, 'C8_ConstantValue__28_CAST_mul32')
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_CAST_mul32_float + (-1)*C3_ConstantValue__28_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__28_CAST_mul32
solver.Add( + (1)*ConstantValue__28_float + (1)*ConstantValue__28_CAST_mul32_fixp + (-1)*C4_ConstantValue__28_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__28_CAST_mul32
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_CAST_mul32_double + (-1)*C5_ConstantValue__28_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__28_CAST_mul32
solver.Add( + (1)*ConstantValue__28_double + (1)*ConstantValue__28_CAST_mul32_fixp + (-1)*C6_ConstantValue__28_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__28_CAST_mul32
solver.Add( + (1)*ConstantValue__28_float + (1)*ConstantValue__28_CAST_mul32_double + (-1)*C7_ConstantValue__28_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__28_CAST_mul32
solver.Add( + (1)*ConstantValue__28_double + (1)*ConstantValue__28_CAST_mul32_float + (-1)*C8_ConstantValue__28_CAST_mul32<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__28_CAST_mul32



#Stuff for   %mul32 = fmul double %conv31, 0x3FD470BF3A92F8EC, !taffo.info !85, !taffo.initweight !30, !taffo.constinfo !87
_Z4CNDFf_2_13_mul32_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul32_fixbits')
_Z4CNDFf_2_13_mul32_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul32_fixp')
_Z4CNDFf_2_13_mul32_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul32_float')
_Z4CNDFf_2_13_mul32_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul32_double')
_Z4CNDFf_2_13_mul32_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul32_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_enob + (-1)*_Z4CNDFf_2_13_mul32_fixbits + (10000)*_Z4CNDFf_2_13_mul32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_enob + (10000)*_Z4CNDFf_2_13_mul32_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_enob + (10000)*_Z4CNDFf_2_13_mul32_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_fixbits + (-10000)*_Z4CNDFf_2_13_mul32_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul32_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_fixp + (1)*_Z4CNDFf_2_13_mul32_float + (1)*_Z4CNDFf_2_13_mul32_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_fixbits + (-10000)*_Z4CNDFf_2_13_mul32_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_fixp + (-1)*ConstantValue__28_CAST_mul32_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_float + (-1)*ConstantValue__28_CAST_mul32_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_double + (-1)*ConstantValue__28_CAST_mul32_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_fixp + (-1)*_Z4CNDFf_2_13_mul32_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_float + (-1)*_Z4CNDFf_2_13_mul32_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_div_CAST_mul32_double + (-1)*_Z4CNDFf_2_13_mul32_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul32_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul32_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul32_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_enob + (-1)*ConstantValue__26_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_enob + (-1)*_Z4CNDFf_2_13_div_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul32_enob_2<=2)    #Enob: propagation in product 2



#Stuff for double 0xBFD6D1F0E5A8325B
ConstantValue__29_fixbits = solver.IntVar(0, 30, 'ConstantValue__29_fixbits')
ConstantValue__29_fixp = solver.IntVar(0, 1, 'ConstantValue__29_fixp')
ConstantValue__29_float = solver.IntVar(0, 1, 'ConstantValue__29_float')
ConstantValue__29_double = solver.IntVar(0, 1, 'ConstantValue__29_double')
ConstantValue__29_enob = solver.IntVar(-10000, 10000, 'ConstantValue__29_enob')
solver.Add( + (1)*ConstantValue__29_enob + (-1)*ConstantValue__29_fixbits + (10000)*ConstantValue__29_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__29_fixp + (1)*ConstantValue__29_float + (1)*ConstantValue__29_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0xBFD6D1F0E5A8325B
ConstantValue__30_fixbits = solver.IntVar(0, 30, 'ConstantValue__30_fixbits')
ConstantValue__30_fixp = solver.IntVar(0, 1, 'ConstantValue__30_fixp')
ConstantValue__30_float = solver.IntVar(0, 1, 'ConstantValue__30_float')
ConstantValue__30_double = solver.IntVar(0, 1, 'ConstantValue__30_double')
ConstantValue__30_enob = solver.IntVar(-10000, 10000, 'ConstantValue__30_enob')
solver.Add( + (1)*ConstantValue__30_enob + (-1)*ConstantValue__30_fixbits + (10000)*ConstantValue__30_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__30_fixp + (1)*ConstantValue__30_float + (1)*ConstantValue__30_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul35 = fmul double %conv34, 0xBFD6D1F0E5A8325B, !taffo.info !92, !taffo.initweight !30, !taffo.constinfo !94
_Z4CNDFf_2_13_mul27_CAST_mul35_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_2_13_mul27_CAST_mul35_fixbits')
_Z4CNDFf_2_13_mul27_CAST_mul35_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_CAST_mul35_fixp')
_Z4CNDFf_2_13_mul27_CAST_mul35_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_CAST_mul35_float')
_Z4CNDFf_2_13_mul27_CAST_mul35_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul27_CAST_mul35_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixp + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_float + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixbits + (-10000)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul27_CAST_mul35')
C2__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul27_CAST_mul35')
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixbits + (-1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul27_CAST_mul35<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul27_fixbits + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul27_CAST_mul35<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul27_CAST_mul35
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul27_CAST_mul35
C3__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul27_CAST_mul35')
C4__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul27_CAST_mul35')
C5__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul27_CAST_mul35')
C6__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul27_CAST_mul35')
C7__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul27_CAST_mul35')
C8__Z4CNDFf_2_13_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul27_CAST_mul35')
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixp + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_float + (-1)*C3__Z4CNDFf_2_13_mul27_CAST_mul35<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_float + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixp + (-1)*C4__Z4CNDFf_2_13_mul27_CAST_mul35<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_fixp + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_double + (-1)*C5__Z4CNDFf_2_13_mul27_CAST_mul35<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_double + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixp + (-1)*C6__Z4CNDFf_2_13_mul27_CAST_mul35<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_float + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_double + (-1)*C7__Z4CNDFf_2_13_mul27_CAST_mul35<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_double + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_float + (-1)*C8__Z4CNDFf_2_13_mul27_CAST_mul35<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul27_CAST_mul35



#Stuff for double 0xBFD6D1F0E5A8325B
ConstantValue__31_fixbits = solver.IntVar(0, 30, 'ConstantValue__31_fixbits')
ConstantValue__31_fixp = solver.IntVar(0, 1, 'ConstantValue__31_fixp')
ConstantValue__31_float = solver.IntVar(0, 1, 'ConstantValue__31_float')
ConstantValue__31_double = solver.IntVar(0, 1, 'ConstantValue__31_double')
ConstantValue__31_enob = solver.IntVar(-10000, 10000, 'ConstantValue__31_enob')
solver.Add( + (1)*ConstantValue__31_enob + (-1)*ConstantValue__31_fixbits + (10000)*ConstantValue__31_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_float + (1)*ConstantValue__31_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul35 = fmul double %conv34, 0xBFD6D1F0E5A8325B, !taffo.info !92, !taffo.initweight !30, !taffo.constinfo !94
ConstantValue__31_CAST_mul35_fixbits = solver.IntVar(0, 30, 'ConstantValue__31_CAST_mul35_fixbits')
ConstantValue__31_CAST_mul35_fixp = solver.IntVar(0, 1, 'ConstantValue__31_CAST_mul35_fixp')
ConstantValue__31_CAST_mul35_float = solver.IntVar(0, 1, 'ConstantValue__31_CAST_mul35_float')
ConstantValue__31_CAST_mul35_double = solver.IntVar(0, 1, 'ConstantValue__31_CAST_mul35_double')
solver.Add( + (1)*ConstantValue__31_CAST_mul35_fixp + (1)*ConstantValue__31_CAST_mul35_float + (1)*ConstantValue__31_CAST_mul35_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__31_CAST_mul35_fixbits + (-10000)*ConstantValue__31_CAST_mul35_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C1_ConstantValue__31_CAST_mul35')
C2_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C2_ConstantValue__31_CAST_mul35')
solver.Add( + (1)*ConstantValue__31_fixbits + (-1)*ConstantValue__31_CAST_mul35_fixbits + (-10000)*C1_ConstantValue__31_CAST_mul35<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__31_fixbits + (1)*ConstantValue__31_CAST_mul35_fixbits + (-10000)*C2_ConstantValue__31_CAST_mul35<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__31_CAST_mul35
castCostObj +=  + (1.13006)*C2_ConstantValue__31_CAST_mul35
C3_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C3_ConstantValue__31_CAST_mul35')
C4_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C4_ConstantValue__31_CAST_mul35')
C5_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C5_ConstantValue__31_CAST_mul35')
C6_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C6_ConstantValue__31_CAST_mul35')
C7_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C7_ConstantValue__31_CAST_mul35')
C8_ConstantValue__31_CAST_mul35 = solver.IntVar(0, 1, 'C8_ConstantValue__31_CAST_mul35')
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_CAST_mul35_float + (-1)*C3_ConstantValue__31_CAST_mul35<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__31_CAST_mul35
solver.Add( + (1)*ConstantValue__31_float + (1)*ConstantValue__31_CAST_mul35_fixp + (-1)*C4_ConstantValue__31_CAST_mul35<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__31_CAST_mul35
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_CAST_mul35_double + (-1)*C5_ConstantValue__31_CAST_mul35<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__31_CAST_mul35
solver.Add( + (1)*ConstantValue__31_double + (1)*ConstantValue__31_CAST_mul35_fixp + (-1)*C6_ConstantValue__31_CAST_mul35<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__31_CAST_mul35
solver.Add( + (1)*ConstantValue__31_float + (1)*ConstantValue__31_CAST_mul35_double + (-1)*C7_ConstantValue__31_CAST_mul35<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__31_CAST_mul35
solver.Add( + (1)*ConstantValue__31_double + (1)*ConstantValue__31_CAST_mul35_float + (-1)*C8_ConstantValue__31_CAST_mul35<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__31_CAST_mul35



#Stuff for   %mul35 = fmul double %conv34, 0xBFD6D1F0E5A8325B, !taffo.info !92, !taffo.initweight !30, !taffo.constinfo !94
_Z4CNDFf_2_13_mul35_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul35_fixbits')
_Z4CNDFf_2_13_mul35_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul35_fixp')
_Z4CNDFf_2_13_mul35_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul35_float')
_Z4CNDFf_2_13_mul35_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul35_double')
_Z4CNDFf_2_13_mul35_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul35_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_enob + (-1)*_Z4CNDFf_2_13_mul35_fixbits + (10000)*_Z4CNDFf_2_13_mul35_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_enob + (10000)*_Z4CNDFf_2_13_mul35_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_enob + (10000)*_Z4CNDFf_2_13_mul35_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_fixbits + (-10000)*_Z4CNDFf_2_13_mul35_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul35_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_fixp + (1)*_Z4CNDFf_2_13_mul35_float + (1)*_Z4CNDFf_2_13_mul35_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_fixbits + (-10000)*_Z4CNDFf_2_13_mul35_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixp + (-1)*ConstantValue__31_CAST_mul35_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_float + (-1)*ConstantValue__31_CAST_mul35_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_double + (-1)*ConstantValue__31_CAST_mul35_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_fixp + (-1)*_Z4CNDFf_2_13_mul35_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_float + (-1)*_Z4CNDFf_2_13_mul35_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul27_CAST_mul35_double + (-1)*_Z4CNDFf_2_13_mul35_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul35_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul35_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul35_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_enob + (-1)*ConstantValue__29_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_enob + (-1)*_Z4CNDFf_2_13_mul27_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul35_enob_2<=1)    #Enob: propagation in product 2



#Stuff for double 0x3FFC80EF025F5E68
ConstantValue__32_fixbits = solver.IntVar(0, 30, 'ConstantValue__32_fixbits')
ConstantValue__32_fixp = solver.IntVar(0, 1, 'ConstantValue__32_fixp')
ConstantValue__32_float = solver.IntVar(0, 1, 'ConstantValue__32_float')
ConstantValue__32_double = solver.IntVar(0, 1, 'ConstantValue__32_double')
ConstantValue__32_enob = solver.IntVar(-10000, 10000, 'ConstantValue__32_enob')
solver.Add( + (1)*ConstantValue__32_enob + (-1)*ConstantValue__32_fixbits + (10000)*ConstantValue__32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__32_fixp + (1)*ConstantValue__32_float + (1)*ConstantValue__32_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FFC80EF025F5E68
ConstantValue__33_fixbits = solver.IntVar(0, 30, 'ConstantValue__33_fixbits')
ConstantValue__33_fixp = solver.IntVar(0, 1, 'ConstantValue__33_fixp')
ConstantValue__33_float = solver.IntVar(0, 1, 'ConstantValue__33_float')
ConstantValue__33_double = solver.IntVar(0, 1, 'ConstantValue__33_double')
ConstantValue__33_enob = solver.IntVar(-10000, 10000, 'ConstantValue__33_enob')
solver.Add( + (1)*ConstantValue__33_enob + (-1)*ConstantValue__33_fixbits + (10000)*ConstantValue__33_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_float + (1)*ConstantValue__33_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul38 = fmul double %conv37, 0x3FFC80EF025F5E68, !taffo.info !99, !taffo.initweight !30, !taffo.constinfo !101
_Z4CNDFf_2_13_mul28_CAST_mul38_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul28_CAST_mul38_fixbits')
_Z4CNDFf_2_13_mul28_CAST_mul38_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_CAST_mul38_fixp')
_Z4CNDFf_2_13_mul28_CAST_mul38_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_CAST_mul38_float')
_Z4CNDFf_2_13_mul28_CAST_mul38_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul28_CAST_mul38_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixp + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_float + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixbits + (-10000)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul28_CAST_mul38')
C2__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul28_CAST_mul38')
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixbits + (-1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul28_CAST_mul38<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul28_fixbits + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul28_CAST_mul38<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul28_CAST_mul38
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul28_CAST_mul38
C3__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul28_CAST_mul38')
C4__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul28_CAST_mul38')
C5__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul28_CAST_mul38')
C6__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul28_CAST_mul38')
C7__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul28_CAST_mul38')
C8__Z4CNDFf_2_13_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul28_CAST_mul38')
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixp + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_float + (-1)*C3__Z4CNDFf_2_13_mul28_CAST_mul38<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_float + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixp + (-1)*C4__Z4CNDFf_2_13_mul28_CAST_mul38<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_fixp + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_double + (-1)*C5__Z4CNDFf_2_13_mul28_CAST_mul38<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_double + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixp + (-1)*C6__Z4CNDFf_2_13_mul28_CAST_mul38<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_float + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_double + (-1)*C7__Z4CNDFf_2_13_mul28_CAST_mul38<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_double + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_float + (-1)*C8__Z4CNDFf_2_13_mul28_CAST_mul38<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul28_CAST_mul38



#Stuff for double 0x3FFC80EF025F5E68
ConstantValue__34_fixbits = solver.IntVar(0, 30, 'ConstantValue__34_fixbits')
ConstantValue__34_fixp = solver.IntVar(0, 1, 'ConstantValue__34_fixp')
ConstantValue__34_float = solver.IntVar(0, 1, 'ConstantValue__34_float')
ConstantValue__34_double = solver.IntVar(0, 1, 'ConstantValue__34_double')
ConstantValue__34_enob = solver.IntVar(-10000, 10000, 'ConstantValue__34_enob')
solver.Add( + (1)*ConstantValue__34_enob + (-1)*ConstantValue__34_fixbits + (10000)*ConstantValue__34_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_float + (1)*ConstantValue__34_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul38 = fmul double %conv37, 0x3FFC80EF025F5E68, !taffo.info !99, !taffo.initweight !30, !taffo.constinfo !101
ConstantValue__34_CAST_mul38_fixbits = solver.IntVar(0, 30, 'ConstantValue__34_CAST_mul38_fixbits')
ConstantValue__34_CAST_mul38_fixp = solver.IntVar(0, 1, 'ConstantValue__34_CAST_mul38_fixp')
ConstantValue__34_CAST_mul38_float = solver.IntVar(0, 1, 'ConstantValue__34_CAST_mul38_float')
ConstantValue__34_CAST_mul38_double = solver.IntVar(0, 1, 'ConstantValue__34_CAST_mul38_double')
solver.Add( + (1)*ConstantValue__34_CAST_mul38_fixp + (1)*ConstantValue__34_CAST_mul38_float + (1)*ConstantValue__34_CAST_mul38_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__34_CAST_mul38_fixbits + (-10000)*ConstantValue__34_CAST_mul38_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C1_ConstantValue__34_CAST_mul38')
C2_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C2_ConstantValue__34_CAST_mul38')
solver.Add( + (1)*ConstantValue__34_fixbits + (-1)*ConstantValue__34_CAST_mul38_fixbits + (-10000)*C1_ConstantValue__34_CAST_mul38<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__34_fixbits + (1)*ConstantValue__34_CAST_mul38_fixbits + (-10000)*C2_ConstantValue__34_CAST_mul38<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__34_CAST_mul38
castCostObj +=  + (1.13006)*C2_ConstantValue__34_CAST_mul38
C3_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C3_ConstantValue__34_CAST_mul38')
C4_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C4_ConstantValue__34_CAST_mul38')
C5_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C5_ConstantValue__34_CAST_mul38')
C6_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C6_ConstantValue__34_CAST_mul38')
C7_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C7_ConstantValue__34_CAST_mul38')
C8_ConstantValue__34_CAST_mul38 = solver.IntVar(0, 1, 'C8_ConstantValue__34_CAST_mul38')
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_CAST_mul38_float + (-1)*C3_ConstantValue__34_CAST_mul38<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__34_CAST_mul38
solver.Add( + (1)*ConstantValue__34_float + (1)*ConstantValue__34_CAST_mul38_fixp + (-1)*C4_ConstantValue__34_CAST_mul38<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__34_CAST_mul38
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_CAST_mul38_double + (-1)*C5_ConstantValue__34_CAST_mul38<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__34_CAST_mul38
solver.Add( + (1)*ConstantValue__34_double + (1)*ConstantValue__34_CAST_mul38_fixp + (-1)*C6_ConstantValue__34_CAST_mul38<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__34_CAST_mul38
solver.Add( + (1)*ConstantValue__34_float + (1)*ConstantValue__34_CAST_mul38_double + (-1)*C7_ConstantValue__34_CAST_mul38<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__34_CAST_mul38
solver.Add( + (1)*ConstantValue__34_double + (1)*ConstantValue__34_CAST_mul38_float + (-1)*C8_ConstantValue__34_CAST_mul38<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__34_CAST_mul38



#Stuff for   %mul38 = fmul double %conv37, 0x3FFC80EF025F5E68, !taffo.info !99, !taffo.initweight !30, !taffo.constinfo !101
_Z4CNDFf_2_13_mul38_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul38_fixbits')
_Z4CNDFf_2_13_mul38_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul38_fixp')
_Z4CNDFf_2_13_mul38_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul38_float')
_Z4CNDFf_2_13_mul38_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul38_double')
_Z4CNDFf_2_13_mul38_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul38_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_enob + (-1)*_Z4CNDFf_2_13_mul38_fixbits + (10000)*_Z4CNDFf_2_13_mul38_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_enob + (10000)*_Z4CNDFf_2_13_mul38_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_enob + (10000)*_Z4CNDFf_2_13_mul38_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_fixbits + (-10000)*_Z4CNDFf_2_13_mul38_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul38_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_fixp + (1)*_Z4CNDFf_2_13_mul38_float + (1)*_Z4CNDFf_2_13_mul38_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_fixbits + (-10000)*_Z4CNDFf_2_13_mul38_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixp + (-1)*ConstantValue__34_CAST_mul38_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_float + (-1)*ConstantValue__34_CAST_mul38_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_double + (-1)*ConstantValue__34_CAST_mul38_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_fixp + (-1)*_Z4CNDFf_2_13_mul38_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_float + (-1)*_Z4CNDFf_2_13_mul38_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul28_CAST_mul38_double + (-1)*_Z4CNDFf_2_13_mul38_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul38_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul38_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul38_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_enob + (-1)*ConstantValue__32_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_enob + (-1)*_Z4CNDFf_2_13_mul28_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul38_enob_2<=-1)    #Enob: propagation in product 2



#Constraint for cast for   %add40 = fadd float %conv36, %conv39, !taffo.info !106, !taffo.initweight !23
_Z4CNDFf_2_13_mul35_CAST_add40_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul35_CAST_add40_fixbits')
_Z4CNDFf_2_13_mul35_CAST_add40_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul35_CAST_add40_fixp')
_Z4CNDFf_2_13_mul35_CAST_add40_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul35_CAST_add40_float')
_Z4CNDFf_2_13_mul35_CAST_add40_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul35_CAST_add40_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixp + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_float + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixbits + (-10000)*_Z4CNDFf_2_13_mul35_CAST_add40_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul35_CAST_add40')
C2__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul35_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_fixbits + (-1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul35_CAST_add40<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul35_fixbits + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul35_CAST_add40<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul35_CAST_add40
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul35_CAST_add40
C3__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul35_CAST_add40')
C4__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul35_CAST_add40')
C5__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul35_CAST_add40')
C6__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul35_CAST_add40')
C7__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul35_CAST_add40')
C8__Z4CNDFf_2_13_mul35_CAST_add40 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul35_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_fixp + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_float + (-1)*C3__Z4CNDFf_2_13_mul35_CAST_add40<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_float + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixp + (-1)*C4__Z4CNDFf_2_13_mul35_CAST_add40<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_fixp + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_double + (-1)*C5__Z4CNDFf_2_13_mul35_CAST_add40<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_double + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixp + (-1)*C6__Z4CNDFf_2_13_mul35_CAST_add40<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_float + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_double + (-1)*C7__Z4CNDFf_2_13_mul35_CAST_add40<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_double + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_float + (-1)*C8__Z4CNDFf_2_13_mul35_CAST_add40<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul35_CAST_add40



#Constraint for cast for   %add40 = fadd float %conv36, %conv39, !taffo.info !106, !taffo.initweight !23
_Z4CNDFf_2_13_mul38_CAST_add40_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul38_CAST_add40_fixbits')
_Z4CNDFf_2_13_mul38_CAST_add40_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul38_CAST_add40_fixp')
_Z4CNDFf_2_13_mul38_CAST_add40_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul38_CAST_add40_float')
_Z4CNDFf_2_13_mul38_CAST_add40_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul38_CAST_add40_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixp + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_float + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixbits + (-10000)*_Z4CNDFf_2_13_mul38_CAST_add40_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul38_CAST_add40')
C2__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul38_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_fixbits + (-1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul38_CAST_add40<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul38_fixbits + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul38_CAST_add40<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul38_CAST_add40
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul38_CAST_add40
C3__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul38_CAST_add40')
C4__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul38_CAST_add40')
C5__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul38_CAST_add40')
C6__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul38_CAST_add40')
C7__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul38_CAST_add40')
C8__Z4CNDFf_2_13_mul38_CAST_add40 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul38_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_fixp + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_float + (-1)*C3__Z4CNDFf_2_13_mul38_CAST_add40<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_float + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixp + (-1)*C4__Z4CNDFf_2_13_mul38_CAST_add40<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_fixp + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_double + (-1)*C5__Z4CNDFf_2_13_mul38_CAST_add40<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_double + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixp + (-1)*C6__Z4CNDFf_2_13_mul38_CAST_add40<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_float + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_double + (-1)*C7__Z4CNDFf_2_13_mul38_CAST_add40<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_2_13_mul38_double + (1)*_Z4CNDFf_2_13_mul38_CAST_add40_float + (-1)*C8__Z4CNDFf_2_13_mul38_CAST_add40<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul38_CAST_add40



#Stuff for   %add40 = fadd float %conv36, %conv39, !taffo.info !106, !taffo.initweight !23
_Z4CNDFf_2_13_add40_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add40_fixbits')
_Z4CNDFf_2_13_add40_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add40_fixp')
_Z4CNDFf_2_13_add40_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add40_float')
_Z4CNDFf_2_13_add40_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add40_double')
_Z4CNDFf_2_13_add40_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_add40_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_add40_enob + (-1)*_Z4CNDFf_2_13_add40_fixbits + (10000)*_Z4CNDFf_2_13_add40_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_add40_enob + (10000)*_Z4CNDFf_2_13_add40_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_add40_enob + (10000)*_Z4CNDFf_2_13_add40_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_add40_fixbits + (-10000)*_Z4CNDFf_2_13_add40_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_add40_enob
solver.Add( + (1)*_Z4CNDFf_2_13_add40_fixp + (1)*_Z4CNDFf_2_13_add40_float + (1)*_Z4CNDFf_2_13_add40_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_add40_fixbits + (-10000)*_Z4CNDFf_2_13_add40_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixp + (-1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_float + (-1)*_Z4CNDFf_2_13_mul38_CAST_add40_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_double + (-1)*_Z4CNDFf_2_13_mul38_CAST_add40_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixbits + (-1)*_Z4CNDFf_2_13_mul38_CAST_add40_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixp + (-1)*_Z4CNDFf_2_13_add40_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_float + (-1)*_Z4CNDFf_2_13_add40_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_double + (-1)*_Z4CNDFf_2_13_add40_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul35_CAST_add40_fixbits + (-1)*_Z4CNDFf_2_13_add40_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_add40_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_add40_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_add40_double
solver.Add( + (1)*_Z4CNDFf_2_13_add40_enob + (-1)*_Z4CNDFf_2_13_mul35_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_2_13_add40_enob + (-1)*_Z4CNDFf_2_13_mul38_enob<=0)    #Enob propagation in sum second addend



#Stuff for double 0xBFFD23DD4EF278D0
ConstantValue__35_fixbits = solver.IntVar(0, 29, 'ConstantValue__35_fixbits')
ConstantValue__35_fixp = solver.IntVar(0, 1, 'ConstantValue__35_fixp')
ConstantValue__35_float = solver.IntVar(0, 1, 'ConstantValue__35_float')
ConstantValue__35_double = solver.IntVar(0, 1, 'ConstantValue__35_double')
ConstantValue__35_enob = solver.IntVar(-10000, 10000, 'ConstantValue__35_enob')
solver.Add( + (1)*ConstantValue__35_enob + (-1)*ConstantValue__35_fixbits + (10000)*ConstantValue__35_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__35_fixp + (1)*ConstantValue__35_float + (1)*ConstantValue__35_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0xBFFD23DD4EF278D0
ConstantValue__36_fixbits = solver.IntVar(0, 29, 'ConstantValue__36_fixbits')
ConstantValue__36_fixp = solver.IntVar(0, 1, 'ConstantValue__36_fixp')
ConstantValue__36_float = solver.IntVar(0, 1, 'ConstantValue__36_float')
ConstantValue__36_double = solver.IntVar(0, 1, 'ConstantValue__36_double')
ConstantValue__36_enob = solver.IntVar(-10000, 10000, 'ConstantValue__36_enob')
solver.Add( + (1)*ConstantValue__36_enob + (-1)*ConstantValue__36_fixbits + (10000)*ConstantValue__36_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__36_enob + (10000)*ConstantValue__36_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__36_enob + (10000)*ConstantValue__36_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__36_fixbits + (-10000)*ConstantValue__36_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__36_fixp + (1)*ConstantValue__36_float + (1)*ConstantValue__36_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__36_fixbits + (-10000)*ConstantValue__36_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul42 = fmul double %conv41, 0xBFFD23DD4EF278D0, !taffo.info !108, !taffo.initweight !30, !taffo.constinfo !110
_Z4CNDFf_2_13_mul29_CAST_mul42_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul29_CAST_mul42_fixbits')
_Z4CNDFf_2_13_mul29_CAST_mul42_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_CAST_mul42_fixp')
_Z4CNDFf_2_13_mul29_CAST_mul42_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_CAST_mul42_float')
_Z4CNDFf_2_13_mul29_CAST_mul42_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul29_CAST_mul42_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixp + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_float + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixbits + (-10000)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul29_CAST_mul42')
C2__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul29_CAST_mul42')
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixbits + (-1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul29_CAST_mul42<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul29_fixbits + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul29_CAST_mul42<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul29_CAST_mul42
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul29_CAST_mul42
C3__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul29_CAST_mul42')
C4__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul29_CAST_mul42')
C5__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul29_CAST_mul42')
C6__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul29_CAST_mul42')
C7__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul29_CAST_mul42')
C8__Z4CNDFf_2_13_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul29_CAST_mul42')
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixp + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_float + (-1)*C3__Z4CNDFf_2_13_mul29_CAST_mul42<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_float + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixp + (-1)*C4__Z4CNDFf_2_13_mul29_CAST_mul42<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_fixp + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_double + (-1)*C5__Z4CNDFf_2_13_mul29_CAST_mul42<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_double + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixp + (-1)*C6__Z4CNDFf_2_13_mul29_CAST_mul42<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_float + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_double + (-1)*C7__Z4CNDFf_2_13_mul29_CAST_mul42<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_double + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_float + (-1)*C8__Z4CNDFf_2_13_mul29_CAST_mul42<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul29_CAST_mul42



#Stuff for double 0xBFFD23DD4EF278D0
ConstantValue__37_fixbits = solver.IntVar(0, 29, 'ConstantValue__37_fixbits')
ConstantValue__37_fixp = solver.IntVar(0, 1, 'ConstantValue__37_fixp')
ConstantValue__37_float = solver.IntVar(0, 1, 'ConstantValue__37_float')
ConstantValue__37_double = solver.IntVar(0, 1, 'ConstantValue__37_double')
ConstantValue__37_enob = solver.IntVar(-10000, 10000, 'ConstantValue__37_enob')
solver.Add( + (1)*ConstantValue__37_enob + (-1)*ConstantValue__37_fixbits + (10000)*ConstantValue__37_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_float + (1)*ConstantValue__37_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul42 = fmul double %conv41, 0xBFFD23DD4EF278D0, !taffo.info !108, !taffo.initweight !30, !taffo.constinfo !110
ConstantValue__37_CAST_mul42_fixbits = solver.IntVar(0, 29, 'ConstantValue__37_CAST_mul42_fixbits')
ConstantValue__37_CAST_mul42_fixp = solver.IntVar(0, 1, 'ConstantValue__37_CAST_mul42_fixp')
ConstantValue__37_CAST_mul42_float = solver.IntVar(0, 1, 'ConstantValue__37_CAST_mul42_float')
ConstantValue__37_CAST_mul42_double = solver.IntVar(0, 1, 'ConstantValue__37_CAST_mul42_double')
solver.Add( + (1)*ConstantValue__37_CAST_mul42_fixp + (1)*ConstantValue__37_CAST_mul42_float + (1)*ConstantValue__37_CAST_mul42_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__37_CAST_mul42_fixbits + (-10000)*ConstantValue__37_CAST_mul42_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C1_ConstantValue__37_CAST_mul42')
C2_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C2_ConstantValue__37_CAST_mul42')
solver.Add( + (1)*ConstantValue__37_fixbits + (-1)*ConstantValue__37_CAST_mul42_fixbits + (-10000)*C1_ConstantValue__37_CAST_mul42<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__37_fixbits + (1)*ConstantValue__37_CAST_mul42_fixbits + (-10000)*C2_ConstantValue__37_CAST_mul42<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__37_CAST_mul42
castCostObj +=  + (1.13006)*C2_ConstantValue__37_CAST_mul42
C3_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C3_ConstantValue__37_CAST_mul42')
C4_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C4_ConstantValue__37_CAST_mul42')
C5_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C5_ConstantValue__37_CAST_mul42')
C6_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C6_ConstantValue__37_CAST_mul42')
C7_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C7_ConstantValue__37_CAST_mul42')
C8_ConstantValue__37_CAST_mul42 = solver.IntVar(0, 1, 'C8_ConstantValue__37_CAST_mul42')
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_CAST_mul42_float + (-1)*C3_ConstantValue__37_CAST_mul42<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__37_CAST_mul42
solver.Add( + (1)*ConstantValue__37_float + (1)*ConstantValue__37_CAST_mul42_fixp + (-1)*C4_ConstantValue__37_CAST_mul42<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__37_CAST_mul42
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_CAST_mul42_double + (-1)*C5_ConstantValue__37_CAST_mul42<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__37_CAST_mul42
solver.Add( + (1)*ConstantValue__37_double + (1)*ConstantValue__37_CAST_mul42_fixp + (-1)*C6_ConstantValue__37_CAST_mul42<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__37_CAST_mul42
solver.Add( + (1)*ConstantValue__37_float + (1)*ConstantValue__37_CAST_mul42_double + (-1)*C7_ConstantValue__37_CAST_mul42<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__37_CAST_mul42
solver.Add( + (1)*ConstantValue__37_double + (1)*ConstantValue__37_CAST_mul42_float + (-1)*C8_ConstantValue__37_CAST_mul42<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__37_CAST_mul42



#Stuff for   %mul42 = fmul double %conv41, 0xBFFD23DD4EF278D0, !taffo.info !108, !taffo.initweight !30, !taffo.constinfo !110
_Z4CNDFf_2_13_mul42_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul42_fixbits')
_Z4CNDFf_2_13_mul42_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul42_fixp')
_Z4CNDFf_2_13_mul42_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul42_float')
_Z4CNDFf_2_13_mul42_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul42_double')
_Z4CNDFf_2_13_mul42_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul42_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_enob + (-1)*_Z4CNDFf_2_13_mul42_fixbits + (10000)*_Z4CNDFf_2_13_mul42_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_enob + (10000)*_Z4CNDFf_2_13_mul42_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_enob + (10000)*_Z4CNDFf_2_13_mul42_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_fixbits + (-10000)*_Z4CNDFf_2_13_mul42_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul42_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_fixp + (1)*_Z4CNDFf_2_13_mul42_float + (1)*_Z4CNDFf_2_13_mul42_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_fixbits + (-10000)*_Z4CNDFf_2_13_mul42_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixp + (-1)*ConstantValue__37_CAST_mul42_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_float + (-1)*ConstantValue__37_CAST_mul42_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_double + (-1)*ConstantValue__37_CAST_mul42_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_fixp + (-1)*_Z4CNDFf_2_13_mul42_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_float + (-1)*_Z4CNDFf_2_13_mul42_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul29_CAST_mul42_double + (-1)*_Z4CNDFf_2_13_mul42_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul42_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul42_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul42_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_enob + (-1)*ConstantValue__35_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_enob + (-1)*_Z4CNDFf_2_13_mul29_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul42_enob_2<=-1)    #Enob: propagation in product 2



#Constraint for cast for   %add44 = fadd float %add40, %conv43, !taffo.info !115, !taffo.initweight !23
_Z4CNDFf_2_13_add40_CAST_add44_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add40_CAST_add44_fixbits')
_Z4CNDFf_2_13_add40_CAST_add44_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add40_CAST_add44_fixp')
_Z4CNDFf_2_13_add40_CAST_add44_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add40_CAST_add44_float')
_Z4CNDFf_2_13_add40_CAST_add44_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add40_CAST_add44_double')
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixp + (1)*_Z4CNDFf_2_13_add40_CAST_add44_float + (1)*_Z4CNDFf_2_13_add40_CAST_add44_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixbits + (-10000)*_Z4CNDFf_2_13_add40_CAST_add44_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_add40_CAST_add44')
C2__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_add40_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_2_13_add40_fixbits + (-1)*_Z4CNDFf_2_13_add40_CAST_add44_fixbits + (-10000)*C1__Z4CNDFf_2_13_add40_CAST_add44<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_add40_fixbits + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixbits + (-10000)*C2__Z4CNDFf_2_13_add40_CAST_add44<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_add40_CAST_add44
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_add40_CAST_add44
C3__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_add40_CAST_add44')
C4__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_add40_CAST_add44')
C5__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_add40_CAST_add44')
C6__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_add40_CAST_add44')
C7__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_add40_CAST_add44')
C8__Z4CNDFf_2_13_add40_CAST_add44 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_add40_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_2_13_add40_fixp + (1)*_Z4CNDFf_2_13_add40_CAST_add44_float + (-1)*C3__Z4CNDFf_2_13_add40_CAST_add44<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_add40_float + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixp + (-1)*C4__Z4CNDFf_2_13_add40_CAST_add44<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_add40_fixp + (1)*_Z4CNDFf_2_13_add40_CAST_add44_double + (-1)*C5__Z4CNDFf_2_13_add40_CAST_add44<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_add40_double + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixp + (-1)*C6__Z4CNDFf_2_13_add40_CAST_add44<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_add40_float + (1)*_Z4CNDFf_2_13_add40_CAST_add44_double + (-1)*C7__Z4CNDFf_2_13_add40_CAST_add44<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_add40_double + (1)*_Z4CNDFf_2_13_add40_CAST_add44_float + (-1)*C8__Z4CNDFf_2_13_add40_CAST_add44<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_add40_CAST_add44



#Constraint for cast for   %add44 = fadd float %add40, %conv43, !taffo.info !115, !taffo.initweight !23
_Z4CNDFf_2_13_mul42_CAST_add44_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul42_CAST_add44_fixbits')
_Z4CNDFf_2_13_mul42_CAST_add44_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul42_CAST_add44_fixp')
_Z4CNDFf_2_13_mul42_CAST_add44_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul42_CAST_add44_float')
_Z4CNDFf_2_13_mul42_CAST_add44_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul42_CAST_add44_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixp + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_float + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixbits + (-10000)*_Z4CNDFf_2_13_mul42_CAST_add44_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul42_CAST_add44')
C2__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul42_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_fixbits + (-1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul42_CAST_add44<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul42_fixbits + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul42_CAST_add44<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul42_CAST_add44
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul42_CAST_add44
C3__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul42_CAST_add44')
C4__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul42_CAST_add44')
C5__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul42_CAST_add44')
C6__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul42_CAST_add44')
C7__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul42_CAST_add44')
C8__Z4CNDFf_2_13_mul42_CAST_add44 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul42_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_fixp + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_float + (-1)*C3__Z4CNDFf_2_13_mul42_CAST_add44<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_float + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixp + (-1)*C4__Z4CNDFf_2_13_mul42_CAST_add44<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_fixp + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_double + (-1)*C5__Z4CNDFf_2_13_mul42_CAST_add44<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_double + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixp + (-1)*C6__Z4CNDFf_2_13_mul42_CAST_add44<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_float + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_double + (-1)*C7__Z4CNDFf_2_13_mul42_CAST_add44<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_2_13_mul42_double + (1)*_Z4CNDFf_2_13_mul42_CAST_add44_float + (-1)*C8__Z4CNDFf_2_13_mul42_CAST_add44<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul42_CAST_add44



#Stuff for   %add44 = fadd float %add40, %conv43, !taffo.info !115, !taffo.initweight !23
_Z4CNDFf_2_13_add44_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add44_fixbits')
_Z4CNDFf_2_13_add44_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add44_fixp')
_Z4CNDFf_2_13_add44_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add44_float')
_Z4CNDFf_2_13_add44_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add44_double')
_Z4CNDFf_2_13_add44_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_add44_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_add44_enob + (-1)*_Z4CNDFf_2_13_add44_fixbits + (10000)*_Z4CNDFf_2_13_add44_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_add44_enob + (10000)*_Z4CNDFf_2_13_add44_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_add44_enob + (10000)*_Z4CNDFf_2_13_add44_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_add44_fixbits + (-10000)*_Z4CNDFf_2_13_add44_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_add44_enob
solver.Add( + (1)*_Z4CNDFf_2_13_add44_fixp + (1)*_Z4CNDFf_2_13_add44_float + (1)*_Z4CNDFf_2_13_add44_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_add44_fixbits + (-10000)*_Z4CNDFf_2_13_add44_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixp + (-1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_float + (-1)*_Z4CNDFf_2_13_mul42_CAST_add44_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_double + (-1)*_Z4CNDFf_2_13_mul42_CAST_add44_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixbits + (-1)*_Z4CNDFf_2_13_mul42_CAST_add44_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixp + (-1)*_Z4CNDFf_2_13_add44_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_float + (-1)*_Z4CNDFf_2_13_add44_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_double + (-1)*_Z4CNDFf_2_13_add44_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_add40_CAST_add44_fixbits + (-1)*_Z4CNDFf_2_13_add44_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_add44_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_add44_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_add44_double
solver.Add( + (1)*_Z4CNDFf_2_13_add44_enob + (-1)*_Z4CNDFf_2_13_add40_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_2_13_add44_enob + (-1)*_Z4CNDFf_2_13_mul42_enob<=0)    #Enob propagation in sum second addend



#Stuff for double 0x3FF548CDD6F42943
ConstantValue__38_fixbits = solver.IntVar(0, 30, 'ConstantValue__38_fixbits')
ConstantValue__38_fixp = solver.IntVar(0, 1, 'ConstantValue__38_fixp')
ConstantValue__38_float = solver.IntVar(0, 1, 'ConstantValue__38_float')
ConstantValue__38_double = solver.IntVar(0, 1, 'ConstantValue__38_double')
ConstantValue__38_enob = solver.IntVar(-10000, 10000, 'ConstantValue__38_enob')
solver.Add( + (1)*ConstantValue__38_enob + (-1)*ConstantValue__38_fixbits + (10000)*ConstantValue__38_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__38_enob + (10000)*ConstantValue__38_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__38_enob + (10000)*ConstantValue__38_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__38_fixbits + (-10000)*ConstantValue__38_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__38_fixp + (1)*ConstantValue__38_float + (1)*ConstantValue__38_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__38_fixbits + (-10000)*ConstantValue__38_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FF548CDD6F42943
ConstantValue__39_fixbits = solver.IntVar(0, 30, 'ConstantValue__39_fixbits')
ConstantValue__39_fixp = solver.IntVar(0, 1, 'ConstantValue__39_fixp')
ConstantValue__39_float = solver.IntVar(0, 1, 'ConstantValue__39_float')
ConstantValue__39_double = solver.IntVar(0, 1, 'ConstantValue__39_double')
ConstantValue__39_enob = solver.IntVar(-10000, 10000, 'ConstantValue__39_enob')
solver.Add( + (1)*ConstantValue__39_enob + (-1)*ConstantValue__39_fixbits + (10000)*ConstantValue__39_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__39_enob + (10000)*ConstantValue__39_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__39_enob + (10000)*ConstantValue__39_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__39_fixbits + (-10000)*ConstantValue__39_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__39_fixp + (1)*ConstantValue__39_float + (1)*ConstantValue__39_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__39_fixbits + (-10000)*ConstantValue__39_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul46 = fmul double %conv45, 0x3FF548CDD6F42943, !taffo.info !117, !taffo.initweight !30, !taffo.constinfo !119
_Z4CNDFf_2_13_mul30_CAST_mul46_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul30_CAST_mul46_fixbits')
_Z4CNDFf_2_13_mul30_CAST_mul46_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul30_CAST_mul46_fixp')
_Z4CNDFf_2_13_mul30_CAST_mul46_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul30_CAST_mul46_float')
_Z4CNDFf_2_13_mul30_CAST_mul46_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul30_CAST_mul46_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixp + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_float + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixbits + (-10000)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul30_CAST_mul46')
C2__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul30_CAST_mul46')
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_fixbits + (-1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul30_CAST_mul46<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul30_fixbits + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul30_CAST_mul46<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul30_CAST_mul46
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul30_CAST_mul46
C3__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul30_CAST_mul46')
C4__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul30_CAST_mul46')
C5__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul30_CAST_mul46')
C6__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul30_CAST_mul46')
C7__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul30_CAST_mul46')
C8__Z4CNDFf_2_13_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul30_CAST_mul46')
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_fixp + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_float + (-1)*C3__Z4CNDFf_2_13_mul30_CAST_mul46<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_float + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixp + (-1)*C4__Z4CNDFf_2_13_mul30_CAST_mul46<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_fixp + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_double + (-1)*C5__Z4CNDFf_2_13_mul30_CAST_mul46<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_double + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixp + (-1)*C6__Z4CNDFf_2_13_mul30_CAST_mul46<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_float + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_double + (-1)*C7__Z4CNDFf_2_13_mul30_CAST_mul46<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_double + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_float + (-1)*C8__Z4CNDFf_2_13_mul30_CAST_mul46<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul30_CAST_mul46



#Stuff for double 0x3FF548CDD6F42943
ConstantValue__40_fixbits = solver.IntVar(0, 30, 'ConstantValue__40_fixbits')
ConstantValue__40_fixp = solver.IntVar(0, 1, 'ConstantValue__40_fixp')
ConstantValue__40_float = solver.IntVar(0, 1, 'ConstantValue__40_float')
ConstantValue__40_double = solver.IntVar(0, 1, 'ConstantValue__40_double')
ConstantValue__40_enob = solver.IntVar(-10000, 10000, 'ConstantValue__40_enob')
solver.Add( + (1)*ConstantValue__40_enob + (-1)*ConstantValue__40_fixbits + (10000)*ConstantValue__40_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__40_enob + (10000)*ConstantValue__40_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__40_enob + (10000)*ConstantValue__40_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__40_fixbits + (-10000)*ConstantValue__40_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__40_fixp + (1)*ConstantValue__40_float + (1)*ConstantValue__40_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__40_fixbits + (-10000)*ConstantValue__40_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul46 = fmul double %conv45, 0x3FF548CDD6F42943, !taffo.info !117, !taffo.initweight !30, !taffo.constinfo !119
ConstantValue__40_CAST_mul46_fixbits = solver.IntVar(0, 30, 'ConstantValue__40_CAST_mul46_fixbits')
ConstantValue__40_CAST_mul46_fixp = solver.IntVar(0, 1, 'ConstantValue__40_CAST_mul46_fixp')
ConstantValue__40_CAST_mul46_float = solver.IntVar(0, 1, 'ConstantValue__40_CAST_mul46_float')
ConstantValue__40_CAST_mul46_double = solver.IntVar(0, 1, 'ConstantValue__40_CAST_mul46_double')
solver.Add( + (1)*ConstantValue__40_CAST_mul46_fixp + (1)*ConstantValue__40_CAST_mul46_float + (1)*ConstantValue__40_CAST_mul46_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__40_CAST_mul46_fixbits + (-10000)*ConstantValue__40_CAST_mul46_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C1_ConstantValue__40_CAST_mul46')
C2_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C2_ConstantValue__40_CAST_mul46')
solver.Add( + (1)*ConstantValue__40_fixbits + (-1)*ConstantValue__40_CAST_mul46_fixbits + (-10000)*C1_ConstantValue__40_CAST_mul46<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__40_fixbits + (1)*ConstantValue__40_CAST_mul46_fixbits + (-10000)*C2_ConstantValue__40_CAST_mul46<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__40_CAST_mul46
castCostObj +=  + (1.13006)*C2_ConstantValue__40_CAST_mul46
C3_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C3_ConstantValue__40_CAST_mul46')
C4_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C4_ConstantValue__40_CAST_mul46')
C5_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C5_ConstantValue__40_CAST_mul46')
C6_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C6_ConstantValue__40_CAST_mul46')
C7_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C7_ConstantValue__40_CAST_mul46')
C8_ConstantValue__40_CAST_mul46 = solver.IntVar(0, 1, 'C8_ConstantValue__40_CAST_mul46')
solver.Add( + (1)*ConstantValue__40_fixp + (1)*ConstantValue__40_CAST_mul46_float + (-1)*C3_ConstantValue__40_CAST_mul46<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__40_CAST_mul46
solver.Add( + (1)*ConstantValue__40_float + (1)*ConstantValue__40_CAST_mul46_fixp + (-1)*C4_ConstantValue__40_CAST_mul46<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__40_CAST_mul46
solver.Add( + (1)*ConstantValue__40_fixp + (1)*ConstantValue__40_CAST_mul46_double + (-1)*C5_ConstantValue__40_CAST_mul46<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__40_CAST_mul46
solver.Add( + (1)*ConstantValue__40_double + (1)*ConstantValue__40_CAST_mul46_fixp + (-1)*C6_ConstantValue__40_CAST_mul46<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__40_CAST_mul46
solver.Add( + (1)*ConstantValue__40_float + (1)*ConstantValue__40_CAST_mul46_double + (-1)*C7_ConstantValue__40_CAST_mul46<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__40_CAST_mul46
solver.Add( + (1)*ConstantValue__40_double + (1)*ConstantValue__40_CAST_mul46_float + (-1)*C8_ConstantValue__40_CAST_mul46<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__40_CAST_mul46



#Stuff for   %mul46 = fmul double %conv45, 0x3FF548CDD6F42943, !taffo.info !117, !taffo.initweight !30, !taffo.constinfo !119
_Z4CNDFf_2_13_mul46_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul46_fixbits')
_Z4CNDFf_2_13_mul46_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul46_fixp')
_Z4CNDFf_2_13_mul46_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul46_float')
_Z4CNDFf_2_13_mul46_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul46_double')
_Z4CNDFf_2_13_mul46_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul46_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_enob + (-1)*_Z4CNDFf_2_13_mul46_fixbits + (10000)*_Z4CNDFf_2_13_mul46_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_enob + (10000)*_Z4CNDFf_2_13_mul46_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_enob + (10000)*_Z4CNDFf_2_13_mul46_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_fixbits + (-10000)*_Z4CNDFf_2_13_mul46_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul46_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_fixp + (1)*_Z4CNDFf_2_13_mul46_float + (1)*_Z4CNDFf_2_13_mul46_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_fixbits + (-10000)*_Z4CNDFf_2_13_mul46_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixp + (-1)*ConstantValue__40_CAST_mul46_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_float + (-1)*ConstantValue__40_CAST_mul46_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_double + (-1)*ConstantValue__40_CAST_mul46_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_fixp + (-1)*_Z4CNDFf_2_13_mul46_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_float + (-1)*_Z4CNDFf_2_13_mul46_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_mul30_CAST_mul46_double + (-1)*_Z4CNDFf_2_13_mul46_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul46_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul46_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul46_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_enob + (-1)*ConstantValue__38_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_enob + (-1)*_Z4CNDFf_2_13_mul30_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul46_enob_2<=0)    #Enob: propagation in product 2



#Constraint for cast for   %add48 = fadd float %add44, %conv47, !taffo.info !124, !taffo.initweight !23
_Z4CNDFf_2_13_add44_CAST_add48_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add44_CAST_add48_fixbits')
_Z4CNDFf_2_13_add44_CAST_add48_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add44_CAST_add48_fixp')
_Z4CNDFf_2_13_add44_CAST_add48_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add44_CAST_add48_float')
_Z4CNDFf_2_13_add44_CAST_add48_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add44_CAST_add48_double')
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixp + (1)*_Z4CNDFf_2_13_add44_CAST_add48_float + (1)*_Z4CNDFf_2_13_add44_CAST_add48_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixbits + (-10000)*_Z4CNDFf_2_13_add44_CAST_add48_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_add44_CAST_add48')
C2__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_add44_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_2_13_add44_fixbits + (-1)*_Z4CNDFf_2_13_add44_CAST_add48_fixbits + (-10000)*C1__Z4CNDFf_2_13_add44_CAST_add48<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_add44_fixbits + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixbits + (-10000)*C2__Z4CNDFf_2_13_add44_CAST_add48<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_add44_CAST_add48
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_add44_CAST_add48
C3__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_add44_CAST_add48')
C4__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_add44_CAST_add48')
C5__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_add44_CAST_add48')
C6__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_add44_CAST_add48')
C7__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_add44_CAST_add48')
C8__Z4CNDFf_2_13_add44_CAST_add48 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_add44_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_2_13_add44_fixp + (1)*_Z4CNDFf_2_13_add44_CAST_add48_float + (-1)*C3__Z4CNDFf_2_13_add44_CAST_add48<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_add44_float + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixp + (-1)*C4__Z4CNDFf_2_13_add44_CAST_add48<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_add44_fixp + (1)*_Z4CNDFf_2_13_add44_CAST_add48_double + (-1)*C5__Z4CNDFf_2_13_add44_CAST_add48<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_add44_double + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixp + (-1)*C6__Z4CNDFf_2_13_add44_CAST_add48<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_add44_float + (1)*_Z4CNDFf_2_13_add44_CAST_add48_double + (-1)*C7__Z4CNDFf_2_13_add44_CAST_add48<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_add44_double + (1)*_Z4CNDFf_2_13_add44_CAST_add48_float + (-1)*C8__Z4CNDFf_2_13_add44_CAST_add48<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_add44_CAST_add48



#Constraint for cast for   %add48 = fadd float %add44, %conv47, !taffo.info !124, !taffo.initweight !23
_Z4CNDFf_2_13_mul46_CAST_add48_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul46_CAST_add48_fixbits')
_Z4CNDFf_2_13_mul46_CAST_add48_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul46_CAST_add48_fixp')
_Z4CNDFf_2_13_mul46_CAST_add48_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul46_CAST_add48_float')
_Z4CNDFf_2_13_mul46_CAST_add48_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul46_CAST_add48_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixp + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_float + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixbits + (-10000)*_Z4CNDFf_2_13_mul46_CAST_add48_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul46_CAST_add48')
C2__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul46_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_fixbits + (-1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul46_CAST_add48<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul46_fixbits + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul46_CAST_add48<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul46_CAST_add48
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul46_CAST_add48
C3__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul46_CAST_add48')
C4__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul46_CAST_add48')
C5__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul46_CAST_add48')
C6__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul46_CAST_add48')
C7__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul46_CAST_add48')
C8__Z4CNDFf_2_13_mul46_CAST_add48 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul46_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_fixp + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_float + (-1)*C3__Z4CNDFf_2_13_mul46_CAST_add48<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_float + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixp + (-1)*C4__Z4CNDFf_2_13_mul46_CAST_add48<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_fixp + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_double + (-1)*C5__Z4CNDFf_2_13_mul46_CAST_add48<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_double + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixp + (-1)*C6__Z4CNDFf_2_13_mul46_CAST_add48<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_float + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_double + (-1)*C7__Z4CNDFf_2_13_mul46_CAST_add48<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_2_13_mul46_double + (1)*_Z4CNDFf_2_13_mul46_CAST_add48_float + (-1)*C8__Z4CNDFf_2_13_mul46_CAST_add48<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul46_CAST_add48



#Stuff for   %add48 = fadd float %add44, %conv47, !taffo.info !124, !taffo.initweight !23
_Z4CNDFf_2_13_add48_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add48_fixbits')
_Z4CNDFf_2_13_add48_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add48_fixp')
_Z4CNDFf_2_13_add48_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add48_float')
_Z4CNDFf_2_13_add48_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add48_double')
_Z4CNDFf_2_13_add48_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_add48_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_add48_enob + (-1)*_Z4CNDFf_2_13_add48_fixbits + (10000)*_Z4CNDFf_2_13_add48_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_add48_enob + (10000)*_Z4CNDFf_2_13_add48_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_add48_enob + (10000)*_Z4CNDFf_2_13_add48_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_add48_fixbits + (-10000)*_Z4CNDFf_2_13_add48_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_add48_enob
solver.Add( + (1)*_Z4CNDFf_2_13_add48_fixp + (1)*_Z4CNDFf_2_13_add48_float + (1)*_Z4CNDFf_2_13_add48_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_add48_fixbits + (-10000)*_Z4CNDFf_2_13_add48_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixp + (-1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_float + (-1)*_Z4CNDFf_2_13_mul46_CAST_add48_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_double + (-1)*_Z4CNDFf_2_13_mul46_CAST_add48_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixbits + (-1)*_Z4CNDFf_2_13_mul46_CAST_add48_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixp + (-1)*_Z4CNDFf_2_13_add48_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_float + (-1)*_Z4CNDFf_2_13_add48_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_double + (-1)*_Z4CNDFf_2_13_add48_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_add44_CAST_add48_fixbits + (-1)*_Z4CNDFf_2_13_add48_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_add48_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_add48_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_add48_double
solver.Add( + (1)*_Z4CNDFf_2_13_add48_enob + (-1)*_Z4CNDFf_2_13_add44_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_2_13_add48_enob + (-1)*_Z4CNDFf_2_13_mul46_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %add49 = fadd float %add48, %conv33, !taffo.info !126, !taffo.initweight !23
_Z4CNDFf_2_13_add48_CAST_add49_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add48_CAST_add49_fixbits')
_Z4CNDFf_2_13_add48_CAST_add49_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add48_CAST_add49_fixp')
_Z4CNDFf_2_13_add48_CAST_add49_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add48_CAST_add49_float')
_Z4CNDFf_2_13_add48_CAST_add49_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add48_CAST_add49_double')
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixp + (1)*_Z4CNDFf_2_13_add48_CAST_add49_float + (1)*_Z4CNDFf_2_13_add48_CAST_add49_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixbits + (-10000)*_Z4CNDFf_2_13_add48_CAST_add49_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_add48_CAST_add49')
C2__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_add48_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_2_13_add48_fixbits + (-1)*_Z4CNDFf_2_13_add48_CAST_add49_fixbits + (-10000)*C1__Z4CNDFf_2_13_add48_CAST_add49<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_add48_fixbits + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixbits + (-10000)*C2__Z4CNDFf_2_13_add48_CAST_add49<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_add48_CAST_add49
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_add48_CAST_add49
C3__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_add48_CAST_add49')
C4__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_add48_CAST_add49')
C5__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_add48_CAST_add49')
C6__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_add48_CAST_add49')
C7__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_add48_CAST_add49')
C8__Z4CNDFf_2_13_add48_CAST_add49 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_add48_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_2_13_add48_fixp + (1)*_Z4CNDFf_2_13_add48_CAST_add49_float + (-1)*C3__Z4CNDFf_2_13_add48_CAST_add49<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_add48_float + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixp + (-1)*C4__Z4CNDFf_2_13_add48_CAST_add49<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_add48_fixp + (1)*_Z4CNDFf_2_13_add48_CAST_add49_double + (-1)*C5__Z4CNDFf_2_13_add48_CAST_add49<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_add48_double + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixp + (-1)*C6__Z4CNDFf_2_13_add48_CAST_add49<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_add48_float + (1)*_Z4CNDFf_2_13_add48_CAST_add49_double + (-1)*C7__Z4CNDFf_2_13_add48_CAST_add49<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_add48_double + (1)*_Z4CNDFf_2_13_add48_CAST_add49_float + (-1)*C8__Z4CNDFf_2_13_add48_CAST_add49<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_add48_CAST_add49



#Constraint for cast for   %add49 = fadd float %add48, %conv33, !taffo.info !126, !taffo.initweight !23
_Z4CNDFf_2_13_mul32_CAST_add49_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul32_CAST_add49_fixbits')
_Z4CNDFf_2_13_mul32_CAST_add49_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul32_CAST_add49_fixp')
_Z4CNDFf_2_13_mul32_CAST_add49_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul32_CAST_add49_float')
_Z4CNDFf_2_13_mul32_CAST_add49_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul32_CAST_add49_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixp + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_float + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixbits + (-10000)*_Z4CNDFf_2_13_mul32_CAST_add49_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul32_CAST_add49')
C2__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul32_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_fixbits + (-1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul32_CAST_add49<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul32_fixbits + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul32_CAST_add49<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul32_CAST_add49
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul32_CAST_add49
C3__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul32_CAST_add49')
C4__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul32_CAST_add49')
C5__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul32_CAST_add49')
C6__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul32_CAST_add49')
C7__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul32_CAST_add49')
C8__Z4CNDFf_2_13_mul32_CAST_add49 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul32_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_fixp + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_float + (-1)*C3__Z4CNDFf_2_13_mul32_CAST_add49<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_float + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixp + (-1)*C4__Z4CNDFf_2_13_mul32_CAST_add49<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_fixp + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_double + (-1)*C5__Z4CNDFf_2_13_mul32_CAST_add49<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_double + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixp + (-1)*C6__Z4CNDFf_2_13_mul32_CAST_add49<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_float + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_double + (-1)*C7__Z4CNDFf_2_13_mul32_CAST_add49<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_2_13_mul32_double + (1)*_Z4CNDFf_2_13_mul32_CAST_add49_float + (-1)*C8__Z4CNDFf_2_13_mul32_CAST_add49<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul32_CAST_add49



#Stuff for   %add49 = fadd float %add48, %conv33, !taffo.info !126, !taffo.initweight !23
_Z4CNDFf_2_13_add49_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add49_fixbits')
_Z4CNDFf_2_13_add49_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add49_fixp')
_Z4CNDFf_2_13_add49_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add49_float')
_Z4CNDFf_2_13_add49_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add49_double')
_Z4CNDFf_2_13_add49_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_add49_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_add49_enob + (-1)*_Z4CNDFf_2_13_add49_fixbits + (10000)*_Z4CNDFf_2_13_add49_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_add49_enob + (10000)*_Z4CNDFf_2_13_add49_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_add49_enob + (10000)*_Z4CNDFf_2_13_add49_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_add49_fixbits + (-10000)*_Z4CNDFf_2_13_add49_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_add49_enob
solver.Add( + (1)*_Z4CNDFf_2_13_add49_fixp + (1)*_Z4CNDFf_2_13_add49_float + (1)*_Z4CNDFf_2_13_add49_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_add49_fixbits + (-10000)*_Z4CNDFf_2_13_add49_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixp + (-1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_float + (-1)*_Z4CNDFf_2_13_mul32_CAST_add49_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_double + (-1)*_Z4CNDFf_2_13_mul32_CAST_add49_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixbits + (-1)*_Z4CNDFf_2_13_mul32_CAST_add49_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixp + (-1)*_Z4CNDFf_2_13_add49_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_float + (-1)*_Z4CNDFf_2_13_add49_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_double + (-1)*_Z4CNDFf_2_13_add49_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_add48_CAST_add49_fixbits + (-1)*_Z4CNDFf_2_13_add49_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_add49_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_add49_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_add49_double
solver.Add( + (1)*_Z4CNDFf_2_13_add49_enob + (-1)*_Z4CNDFf_2_13_add48_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_2_13_add49_enob + (-1)*_Z4CNDFf_2_13_mul32_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %mul50 = fmul float %add49, %conv19, !taffo.info !128, !taffo.initweight !23
_Z4CNDFf_2_13_add49_CAST_mul50_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_add49_CAST_mul50_fixbits')
_Z4CNDFf_2_13_add49_CAST_mul50_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add49_CAST_mul50_fixp')
_Z4CNDFf_2_13_add49_CAST_mul50_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add49_CAST_mul50_float')
_Z4CNDFf_2_13_add49_CAST_mul50_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_add49_CAST_mul50_double')
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixp + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_float + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixbits + (-10000)*_Z4CNDFf_2_13_add49_CAST_mul50_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_add49_CAST_mul50')
C2__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_add49_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_2_13_add49_fixbits + (-1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixbits + (-10000)*C1__Z4CNDFf_2_13_add49_CAST_mul50<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_add49_fixbits + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixbits + (-10000)*C2__Z4CNDFf_2_13_add49_CAST_mul50<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_add49_CAST_mul50
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_add49_CAST_mul50
C3__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_add49_CAST_mul50')
C4__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_add49_CAST_mul50')
C5__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_add49_CAST_mul50')
C6__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_add49_CAST_mul50')
C7__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_add49_CAST_mul50')
C8__Z4CNDFf_2_13_add49_CAST_mul50 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_add49_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_2_13_add49_fixp + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_float + (-1)*C3__Z4CNDFf_2_13_add49_CAST_mul50<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_add49_float + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixp + (-1)*C4__Z4CNDFf_2_13_add49_CAST_mul50<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_add49_fixp + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_double + (-1)*C5__Z4CNDFf_2_13_add49_CAST_mul50<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_add49_double + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixp + (-1)*C6__Z4CNDFf_2_13_add49_CAST_mul50<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_add49_float + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_double + (-1)*C7__Z4CNDFf_2_13_add49_CAST_mul50<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_add49_double + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_float + (-1)*C8__Z4CNDFf_2_13_add49_CAST_mul50<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_add49_CAST_mul50



#Constraint for cast for   %mul50 = fmul float %add49, %conv19, !taffo.info !128, !taffo.initweight !23
_Z4CNDFf_2_13_mul18_CAST_mul50_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_2_13_mul18_CAST_mul50_fixbits')
_Z4CNDFf_2_13_mul18_CAST_mul50_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul18_CAST_mul50_fixp')
_Z4CNDFf_2_13_mul18_CAST_mul50_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul18_CAST_mul50_float')
_Z4CNDFf_2_13_mul18_CAST_mul50_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul18_CAST_mul50_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixp + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_float + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixbits + (-10000)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul18_CAST_mul50')
C2__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul18_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_fixbits + (-1)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul18_CAST_mul50<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul18_fixbits + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul18_CAST_mul50<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul18_CAST_mul50
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul18_CAST_mul50
C3__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul18_CAST_mul50')
C4__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul18_CAST_mul50')
C5__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul18_CAST_mul50')
C6__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul18_CAST_mul50')
C7__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul18_CAST_mul50')
C8__Z4CNDFf_2_13_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul18_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_fixp + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_float + (-1)*C3__Z4CNDFf_2_13_mul18_CAST_mul50<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_float + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixp + (-1)*C4__Z4CNDFf_2_13_mul18_CAST_mul50<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_fixp + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_double + (-1)*C5__Z4CNDFf_2_13_mul18_CAST_mul50<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_double + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixp + (-1)*C6__Z4CNDFf_2_13_mul18_CAST_mul50<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_float + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_double + (-1)*C7__Z4CNDFf_2_13_mul18_CAST_mul50<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_2_13_mul18_double + (1)*_Z4CNDFf_2_13_mul18_CAST_mul50_float + (-1)*C8__Z4CNDFf_2_13_mul18_CAST_mul50<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul18_CAST_mul50



#Stuff for   %mul50 = fmul float %add49, %conv19, !taffo.info !128, !taffo.initweight !23
_Z4CNDFf_2_13_mul50_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul50_fixbits')
_Z4CNDFf_2_13_mul50_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul50_fixp')
_Z4CNDFf_2_13_mul50_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul50_float')
_Z4CNDFf_2_13_mul50_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul50_double')
_Z4CNDFf_2_13_mul50_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_mul50_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_enob + (-1)*_Z4CNDFf_2_13_mul50_fixbits + (10000)*_Z4CNDFf_2_13_mul50_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_enob + (10000)*_Z4CNDFf_2_13_mul50_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_enob + (10000)*_Z4CNDFf_2_13_mul50_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_fixbits + (-10000)*_Z4CNDFf_2_13_mul50_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_mul50_enob
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_fixp + (1)*_Z4CNDFf_2_13_mul50_float + (1)*_Z4CNDFf_2_13_mul50_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_fixbits + (-10000)*_Z4CNDFf_2_13_mul50_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixp + (-1)*_Z4CNDFf_2_13_mul18_CAST_mul50_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_float + (-1)*_Z4CNDFf_2_13_mul18_CAST_mul50_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_double + (-1)*_Z4CNDFf_2_13_mul18_CAST_mul50_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_fixp + (-1)*_Z4CNDFf_2_13_mul50_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_float + (-1)*_Z4CNDFf_2_13_mul50_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_add49_CAST_mul50_double + (-1)*_Z4CNDFf_2_13_mul50_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_2_13_mul50_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_2_13_mul50_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_2_13_mul50_double
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_1')
_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_2')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_1 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_enob + (-1)*_Z4CNDFf_2_13_mul18_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_enob + (-1)*_Z4CNDFf_2_13_add49_enob + (-10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_mul50_enob_2<=1024)    #Enob: propagation in product 2



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
solver.Add( + (1)*ConstantValue__43_fixp + (1)*ConstantValue__43_float + (1)*ConstantValue__43_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__43_fixbits + (-10000)*ConstantValue__43_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub52 = fsub double 1.000000e+00, %conv51, !taffo.info !130, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__43_CAST_sub52_fixbits = solver.IntVar(0, 31, 'ConstantValue__43_CAST_sub52_fixbits')
ConstantValue__43_CAST_sub52_fixp = solver.IntVar(0, 1, 'ConstantValue__43_CAST_sub52_fixp')
ConstantValue__43_CAST_sub52_float = solver.IntVar(0, 1, 'ConstantValue__43_CAST_sub52_float')
ConstantValue__43_CAST_sub52_double = solver.IntVar(0, 1, 'ConstantValue__43_CAST_sub52_double')
solver.Add( + (1)*ConstantValue__43_CAST_sub52_fixp + (1)*ConstantValue__43_CAST_sub52_float + (1)*ConstantValue__43_CAST_sub52_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__43_CAST_sub52_fixbits + (-10000)*ConstantValue__43_CAST_sub52_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C1_ConstantValue__43_CAST_sub52')
C2_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C2_ConstantValue__43_CAST_sub52')
solver.Add( + (1)*ConstantValue__43_fixbits + (-1)*ConstantValue__43_CAST_sub52_fixbits + (-10000)*C1_ConstantValue__43_CAST_sub52<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__43_fixbits + (1)*ConstantValue__43_CAST_sub52_fixbits + (-10000)*C2_ConstantValue__43_CAST_sub52<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__43_CAST_sub52
castCostObj +=  + (1.13006)*C2_ConstantValue__43_CAST_sub52
C3_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C3_ConstantValue__43_CAST_sub52')
C4_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C4_ConstantValue__43_CAST_sub52')
C5_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C5_ConstantValue__43_CAST_sub52')
C6_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C6_ConstantValue__43_CAST_sub52')
C7_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C7_ConstantValue__43_CAST_sub52')
C8_ConstantValue__43_CAST_sub52 = solver.IntVar(0, 1, 'C8_ConstantValue__43_CAST_sub52')
solver.Add( + (1)*ConstantValue__43_fixp + (1)*ConstantValue__43_CAST_sub52_float + (-1)*C3_ConstantValue__43_CAST_sub52<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__43_CAST_sub52
solver.Add( + (1)*ConstantValue__43_float + (1)*ConstantValue__43_CAST_sub52_fixp + (-1)*C4_ConstantValue__43_CAST_sub52<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__43_CAST_sub52
solver.Add( + (1)*ConstantValue__43_fixp + (1)*ConstantValue__43_CAST_sub52_double + (-1)*C5_ConstantValue__43_CAST_sub52<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__43_CAST_sub52
solver.Add( + (1)*ConstantValue__43_double + (1)*ConstantValue__43_CAST_sub52_fixp + (-1)*C6_ConstantValue__43_CAST_sub52<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__43_CAST_sub52
solver.Add( + (1)*ConstantValue__43_float + (1)*ConstantValue__43_CAST_sub52_double + (-1)*C7_ConstantValue__43_CAST_sub52<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__43_CAST_sub52
solver.Add( + (1)*ConstantValue__43_double + (1)*ConstantValue__43_CAST_sub52_float + (-1)*C8_ConstantValue__43_CAST_sub52<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__43_CAST_sub52



#Constraint for cast for   %sub52 = fsub double 1.000000e+00, %conv51, !taffo.info !130, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_mul50_CAST_sub52_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_mul50_CAST_sub52_fixbits')
_Z4CNDFf_2_13_mul50_CAST_sub52_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul50_CAST_sub52_fixp')
_Z4CNDFf_2_13_mul50_CAST_sub52_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul50_CAST_sub52_float')
_Z4CNDFf_2_13_mul50_CAST_sub52_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_mul50_CAST_sub52_double')
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixp + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_float + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixbits + (-10000)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_mul50_CAST_sub52')
C2__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_mul50_CAST_sub52')
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_fixbits + (-1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixbits + (-10000)*C1__Z4CNDFf_2_13_mul50_CAST_sub52<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_mul50_fixbits + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixbits + (-10000)*C2__Z4CNDFf_2_13_mul50_CAST_sub52<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_mul50_CAST_sub52
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_mul50_CAST_sub52
C3__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_mul50_CAST_sub52')
C4__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_mul50_CAST_sub52')
C5__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_mul50_CAST_sub52')
C6__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_mul50_CAST_sub52')
C7__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_mul50_CAST_sub52')
C8__Z4CNDFf_2_13_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_mul50_CAST_sub52')
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_fixp + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_float + (-1)*C3__Z4CNDFf_2_13_mul50_CAST_sub52<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_float + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixp + (-1)*C4__Z4CNDFf_2_13_mul50_CAST_sub52<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_fixp + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_double + (-1)*C5__Z4CNDFf_2_13_mul50_CAST_sub52<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_double + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixp + (-1)*C6__Z4CNDFf_2_13_mul50_CAST_sub52<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_float + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_double + (-1)*C7__Z4CNDFf_2_13_mul50_CAST_sub52<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_2_13_mul50_double + (1)*_Z4CNDFf_2_13_mul50_CAST_sub52_float + (-1)*C8__Z4CNDFf_2_13_mul50_CAST_sub52<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_mul50_CAST_sub52



#Stuff for   %sub52 = fsub double 1.000000e+00, %conv51, !taffo.info !130, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_sub52_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_sub52_fixbits')
_Z4CNDFf_2_13_sub52_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_fixp')
_Z4CNDFf_2_13_sub52_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_float')
_Z4CNDFf_2_13_sub52_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_double')
_Z4CNDFf_2_13_sub52_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_sub52_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_enob + (-1)*_Z4CNDFf_2_13_sub52_fixbits + (10000)*_Z4CNDFf_2_13_sub52_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_enob + (10000)*_Z4CNDFf_2_13_sub52_float<=10024)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_enob + (10000)*_Z4CNDFf_2_13_sub52_double<=10053)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixbits + (-10000)*_Z4CNDFf_2_13_sub52_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_sub52_enob
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixp + (1)*_Z4CNDFf_2_13_sub52_float + (1)*_Z4CNDFf_2_13_sub52_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixbits + (-10000)*_Z4CNDFf_2_13_sub52_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__43_CAST_sub52_fixp + (-1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__43_CAST_sub52_float + (-1)*_Z4CNDFf_2_13_mul50_CAST_sub52_float==0)    #float equality
solver.Add( + (1)*ConstantValue__43_CAST_sub52_double + (-1)*_Z4CNDFf_2_13_mul50_CAST_sub52_double==0)    #double equality
solver.Add( + (1)*ConstantValue__43_CAST_sub52_fixbits + (-1)*_Z4CNDFf_2_13_mul50_CAST_sub52_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__43_CAST_sub52_fixp + (-1)*_Z4CNDFf_2_13_sub52_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__43_CAST_sub52_float + (-1)*_Z4CNDFf_2_13_sub52_float==0)    #float equality
solver.Add( + (1)*ConstantValue__43_CAST_sub52_double + (-1)*_Z4CNDFf_2_13_sub52_double==0)    #double equality
solver.Add( + (1)*ConstantValue__43_CAST_sub52_fixbits + (-1)*_Z4CNDFf_2_13_sub52_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_sub52_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_sub52_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_sub52_double
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_enob + (-1)*ConstantValue__41_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_enob + (-1)*_Z4CNDFf_2_13_mul50_enob<=0)    #Enob propagation in sub second addend



#Stuff for double 1.000000e+00
ConstantValue__44_fixbits = solver.IntVar(0, 31, 'ConstantValue__44_fixbits')
ConstantValue__44_fixp = solver.IntVar(0, 1, 'ConstantValue__44_fixp')
ConstantValue__44_float = solver.IntVar(0, 1, 'ConstantValue__44_float')
ConstantValue__44_double = solver.IntVar(0, 1, 'ConstantValue__44_double')
ConstantValue__44_enob = solver.IntVar(-10000, 10000, 'ConstantValue__44_enob')
solver.Add( + (1)*ConstantValue__44_enob + (-1)*ConstantValue__44_fixbits + (10000)*ConstantValue__44_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__44_enob + (10000)*ConstantValue__44_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__44_enob + (10000)*ConstantValue__44_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__44_fixbits + (-10000)*ConstantValue__44_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__44_fixp + (1)*ConstantValue__44_float + (1)*ConstantValue__44_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__44_fixbits + (-10000)*ConstantValue__44_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__45_fixbits = solver.IntVar(0, 31, 'ConstantValue__45_fixbits')
ConstantValue__45_fixp = solver.IntVar(0, 1, 'ConstantValue__45_fixp')
ConstantValue__45_float = solver.IntVar(0, 1, 'ConstantValue__45_float')
ConstantValue__45_double = solver.IntVar(0, 1, 'ConstantValue__45_double')
ConstantValue__45_enob = solver.IntVar(-10000, 10000, 'ConstantValue__45_enob')
solver.Add( + (1)*ConstantValue__45_enob + (-1)*ConstantValue__45_fixbits + (10000)*ConstantValue__45_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__45_enob + (10000)*ConstantValue__45_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__45_enob + (10000)*ConstantValue__45_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__45_fixbits + (-10000)*ConstantValue__45_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__45_fixp + (1)*ConstantValue__45_float + (1)*ConstantValue__45_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__45_fixbits + (-10000)*ConstantValue__45_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__46_fixbits = solver.IntVar(0, 31, 'ConstantValue__46_fixbits')
ConstantValue__46_fixp = solver.IntVar(0, 1, 'ConstantValue__46_fixp')
ConstantValue__46_float = solver.IntVar(0, 1, 'ConstantValue__46_float')
ConstantValue__46_double = solver.IntVar(0, 1, 'ConstantValue__46_double')
ConstantValue__46_enob = solver.IntVar(-10000, 10000, 'ConstantValue__46_enob')
solver.Add( + (1)*ConstantValue__46_enob + (-1)*ConstantValue__46_fixbits + (10000)*ConstantValue__46_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__46_enob + (10000)*ConstantValue__46_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__46_enob + (10000)*ConstantValue__46_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__46_fixbits + (-10000)*ConstantValue__46_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__46_fixp + (1)*ConstantValue__46_float + (1)*ConstantValue__46_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__46_fixbits + (-10000)*ConstantValue__46_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub56 = fsub double 1.000000e+00, %conv55, !taffo.info !134, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__46_CAST_sub56_fixbits = solver.IntVar(0, 31, 'ConstantValue__46_CAST_sub56_fixbits')
ConstantValue__46_CAST_sub56_fixp = solver.IntVar(0, 1, 'ConstantValue__46_CAST_sub56_fixp')
ConstantValue__46_CAST_sub56_float = solver.IntVar(0, 1, 'ConstantValue__46_CAST_sub56_float')
ConstantValue__46_CAST_sub56_double = solver.IntVar(0, 1, 'ConstantValue__46_CAST_sub56_double')
solver.Add( + (1)*ConstantValue__46_CAST_sub56_fixp + (1)*ConstantValue__46_CAST_sub56_float + (1)*ConstantValue__46_CAST_sub56_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__46_CAST_sub56_fixbits + (-10000)*ConstantValue__46_CAST_sub56_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C1_ConstantValue__46_CAST_sub56')
C2_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C2_ConstantValue__46_CAST_sub56')
solver.Add( + (1)*ConstantValue__46_fixbits + (-1)*ConstantValue__46_CAST_sub56_fixbits + (-10000)*C1_ConstantValue__46_CAST_sub56<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__46_fixbits + (1)*ConstantValue__46_CAST_sub56_fixbits + (-10000)*C2_ConstantValue__46_CAST_sub56<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__46_CAST_sub56
castCostObj +=  + (1.13006)*C2_ConstantValue__46_CAST_sub56
C3_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C3_ConstantValue__46_CAST_sub56')
C4_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C4_ConstantValue__46_CAST_sub56')
C5_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C5_ConstantValue__46_CAST_sub56')
C6_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C6_ConstantValue__46_CAST_sub56')
C7_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C7_ConstantValue__46_CAST_sub56')
C8_ConstantValue__46_CAST_sub56 = solver.IntVar(0, 1, 'C8_ConstantValue__46_CAST_sub56')
solver.Add( + (1)*ConstantValue__46_fixp + (1)*ConstantValue__46_CAST_sub56_float + (-1)*C3_ConstantValue__46_CAST_sub56<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__46_CAST_sub56
solver.Add( + (1)*ConstantValue__46_float + (1)*ConstantValue__46_CAST_sub56_fixp + (-1)*C4_ConstantValue__46_CAST_sub56<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__46_CAST_sub56
solver.Add( + (1)*ConstantValue__46_fixp + (1)*ConstantValue__46_CAST_sub56_double + (-1)*C5_ConstantValue__46_CAST_sub56<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__46_CAST_sub56
solver.Add( + (1)*ConstantValue__46_double + (1)*ConstantValue__46_CAST_sub56_fixp + (-1)*C6_ConstantValue__46_CAST_sub56<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__46_CAST_sub56
solver.Add( + (1)*ConstantValue__46_float + (1)*ConstantValue__46_CAST_sub56_double + (-1)*C7_ConstantValue__46_CAST_sub56<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__46_CAST_sub56
solver.Add( + (1)*ConstantValue__46_double + (1)*ConstantValue__46_CAST_sub56_float + (-1)*C8_ConstantValue__46_CAST_sub56<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__46_CAST_sub56



#Constraint for cast for   %sub56 = fsub double 1.000000e+00, %conv55, !taffo.info !134, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_sub52_CAST_sub56_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_sub52_CAST_sub56_fixbits')
_Z4CNDFf_2_13_sub52_CAST_sub56_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_CAST_sub56_fixp')
_Z4CNDFf_2_13_sub52_CAST_sub56_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_CAST_sub56_float')
_Z4CNDFf_2_13_sub52_CAST_sub56_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_CAST_sub56_double')
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixp + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_float + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixbits + (-10000)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_sub52_CAST_sub56')
C2__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_sub52_CAST_sub56')
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixbits + (-1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixbits + (-10000)*C1__Z4CNDFf_2_13_sub52_CAST_sub56<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_sub52_fixbits + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixbits + (-10000)*C2__Z4CNDFf_2_13_sub52_CAST_sub56<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_sub52_CAST_sub56
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_sub52_CAST_sub56
C3__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_sub52_CAST_sub56')
C4__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_sub52_CAST_sub56')
C5__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_sub52_CAST_sub56')
C6__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_sub52_CAST_sub56')
C7__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_sub52_CAST_sub56')
C8__Z4CNDFf_2_13_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_sub52_CAST_sub56')
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixp + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_float + (-1)*C3__Z4CNDFf_2_13_sub52_CAST_sub56<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_float + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixp + (-1)*C4__Z4CNDFf_2_13_sub52_CAST_sub56<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixp + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_double + (-1)*C5__Z4CNDFf_2_13_sub52_CAST_sub56<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_double + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixp + (-1)*C6__Z4CNDFf_2_13_sub52_CAST_sub56<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_float + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_double + (-1)*C7__Z4CNDFf_2_13_sub52_CAST_sub56<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_double + (1)*_Z4CNDFf_2_13_sub52_CAST_sub56_float + (-1)*C8__Z4CNDFf_2_13_sub52_CAST_sub56<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_sub52_CAST_sub56



#Stuff for   %sub56 = fsub double 1.000000e+00, %conv55, !taffo.info !134, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_2_13_sub56_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_sub56_fixbits')
_Z4CNDFf_2_13_sub56_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub56_fixp')
_Z4CNDFf_2_13_sub56_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub56_float')
_Z4CNDFf_2_13_sub56_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub56_double')
_Z4CNDFf_2_13_sub56_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_sub56_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_enob + (-1)*_Z4CNDFf_2_13_sub56_fixbits + (10000)*_Z4CNDFf_2_13_sub56_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_enob + (10000)*_Z4CNDFf_2_13_sub56_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_enob + (10000)*_Z4CNDFf_2_13_sub56_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_fixbits + (-10000)*_Z4CNDFf_2_13_sub56_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_sub56_enob
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_fixp + (1)*_Z4CNDFf_2_13_sub56_float + (1)*_Z4CNDFf_2_13_sub56_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_fixbits + (-10000)*_Z4CNDFf_2_13_sub56_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__46_CAST_sub56_fixp + (-1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__46_CAST_sub56_float + (-1)*_Z4CNDFf_2_13_sub52_CAST_sub56_float==0)    #float equality
solver.Add( + (1)*ConstantValue__46_CAST_sub56_double + (-1)*_Z4CNDFf_2_13_sub52_CAST_sub56_double==0)    #double equality
solver.Add( + (1)*ConstantValue__46_CAST_sub56_fixbits + (-1)*_Z4CNDFf_2_13_sub52_CAST_sub56_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__46_CAST_sub56_fixp + (-1)*_Z4CNDFf_2_13_sub56_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__46_CAST_sub56_float + (-1)*_Z4CNDFf_2_13_sub56_float==0)    #float equality
solver.Add( + (1)*ConstantValue__46_CAST_sub56_double + (-1)*_Z4CNDFf_2_13_sub56_double==0)    #double equality
solver.Add( + (1)*ConstantValue__46_CAST_sub56_fixbits + (-1)*_Z4CNDFf_2_13_sub56_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_2_13_sub56_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_2_13_sub56_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_2_13_sub56_double
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_enob + (-1)*ConstantValue__44_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_enob + (-1)*_Z4CNDFf_2_13_sub52_enob<=0)    #Enob propagation in sub second addend



#Stuff for   %OutputX.0 = phi float [ %conv57, %if.then54 ], [ %conv53, %if.end ], !taffo.info !136
_Z4CNDFf_2_13_OutputX_0_fixbits = solver.IntVar(0, 29, '_Z4CNDFf_2_13_OutputX_0_fixbits')
_Z4CNDFf_2_13_OutputX_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_OutputX_0_fixp')
_Z4CNDFf_2_13_OutputX_0_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_OutputX_0_float')
_Z4CNDFf_2_13_OutputX_0_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_OutputX_0_double')
_Z4CNDFf_2_13_OutputX_0_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_2_13_OutputX_0_enob')
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_enob + (-1)*_Z4CNDFf_2_13_OutputX_0_fixbits + (10000)*_Z4CNDFf_2_13_OutputX_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_enob + (10000)*_Z4CNDFf_2_13_OutputX_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_enob + (10000)*_Z4CNDFf_2_13_OutputX_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixbits + (-10000)*_Z4CNDFf_2_13_OutputX_0_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z4CNDFf_2_13_OutputX_0_enob
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixp + (1)*_Z4CNDFf_2_13_OutputX_0_float + (1)*_Z4CNDFf_2_13_OutputX_0_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixbits + (-10000)*_Z4CNDFf_2_13_OutputX_0_fixp<=0)    #If not fix, frac part to zero
_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_0 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_0')
_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_1')
solver.Add( + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_0 + (1)*_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %OutputX.0 = phi float [ %conv57, %if.then54 ], [ %conv53, %if.end ], !taffo.info !136
_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixbits')
_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixp')
_Z4CNDFf_2_13_sub56_CAST_OutputX_0_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub56_CAST_OutputX_0_float')
_Z4CNDFf_2_13_sub56_CAST_OutputX_0_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub56_CAST_OutputX_0_double')
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixp + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_float + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixbits + (-10000)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
C2__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_fixbits + (-1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixbits + (-10000)*C1__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_sub56_fixbits + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixbits + (-10000)*C2__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_sub56_CAST_OutputX_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_sub56_CAST_OutputX_0
C3__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
C4__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
C5__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
C6__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
C7__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
C8__Z4CNDFf_2_13_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_sub56_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_fixp + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_float + (-1)*C3__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_float + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixp + (-1)*C4__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_fixp + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_double + (-1)*C5__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_double + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixp + (-1)*C6__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_float + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_double + (-1)*C7__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub56_double + (1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_float + (-1)*C8__Z4CNDFf_2_13_sub56_CAST_OutputX_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixp + (-1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_float + (-1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_double + (-1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixbits + (-1)*_Z4CNDFf_2_13_sub56_CAST_OutputX_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_enob + (-1)*_Z4CNDFf_2_13_sub56_enob + (10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_0<=10000)    #Enob: forcing phi enob



#Constraint for cast for   %OutputX.0 = phi float [ %conv57, %if.then54 ], [ %conv53, %if.end ], !taffo.info !136
_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixbits')
_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixp')
_Z4CNDFf_2_13_sub52_CAST_OutputX_0_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_CAST_OutputX_0_float')
_Z4CNDFf_2_13_sub52_CAST_OutputX_0_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_sub52_CAST_OutputX_0_double')
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixp + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_float + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixbits + (-10000)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
C2__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixbits + (-1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixbits + (-10000)*C1__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_sub52_fixbits + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixbits + (-10000)*C2__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_sub52_CAST_OutputX_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_sub52_CAST_OutputX_0
C3__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
C4__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
C5__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
C6__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
C7__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
C8__Z4CNDFf_2_13_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_sub52_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixp + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_float + (-1)*C3__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_float + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixp + (-1)*C4__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_fixp + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_double + (-1)*C5__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_double + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixp + (-1)*C6__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_float + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_double + (-1)*C7__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_sub52_double + (1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_float + (-1)*C8__Z4CNDFf_2_13_sub52_CAST_OutputX_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixp + (-1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_float + (-1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_double + (-1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixbits + (-1)*_Z4CNDFf_2_13_sub52_CAST_OutputX_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_enob + (-1)*_Z4CNDFf_2_13_sub52_enob + (10000)*_Z4CNDFf_2_13__Z4CNDFf_2_13_OutputX_0_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   ret float %OutputX.0, !taffo.info !31, !taffo.initweight !23
_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixbits = solver.IntVar(0, 29, '_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixbits')
_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixp = solver.IntVar(0, 1, '_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixp')
_Z4CNDFf_2_13_OutputX_0_CAST_ret_float = solver.IntVar(0, 1, '_Z4CNDFf_2_13_OutputX_0_CAST_ret_float')
_Z4CNDFf_2_13_OutputX_0_CAST_ret_double = solver.IntVar(0, 1, '_Z4CNDFf_2_13_OutputX_0_CAST_ret_double')
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixp + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_float + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixbits + (-10000)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C1__Z4CNDFf_2_13_OutputX_0_CAST_ret')
C2__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C2__Z4CNDFf_2_13_OutputX_0_CAST_ret')
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixbits + (-1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixbits + (-10000)*C1__Z4CNDFf_2_13_OutputX_0_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_2_13_OutputX_0_fixbits + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixbits + (-10000)*C2__Z4CNDFf_2_13_OutputX_0_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_2_13_OutputX_0_CAST_ret
castCostObj +=  + (1.13006)*C2__Z4CNDFf_2_13_OutputX_0_CAST_ret
C3__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C3__Z4CNDFf_2_13_OutputX_0_CAST_ret')
C4__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C4__Z4CNDFf_2_13_OutputX_0_CAST_ret')
C5__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C5__Z4CNDFf_2_13_OutputX_0_CAST_ret')
C6__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C6__Z4CNDFf_2_13_OutputX_0_CAST_ret')
C7__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C7__Z4CNDFf_2_13_OutputX_0_CAST_ret')
C8__Z4CNDFf_2_13_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C8__Z4CNDFf_2_13_OutputX_0_CAST_ret')
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixp + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_float + (-1)*C3__Z4CNDFf_2_13_OutputX_0_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_2_13_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_float + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixp + (-1)*C4__Z4CNDFf_2_13_OutputX_0_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_2_13_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_fixp + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_double + (-1)*C5__Z4CNDFf_2_13_OutputX_0_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_2_13_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_double + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixp + (-1)*C6__Z4CNDFf_2_13_OutputX_0_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_2_13_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_float + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_double + (-1)*C7__Z4CNDFf_2_13_OutputX_0_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_2_13_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_2_13_OutputX_0_double + (1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_float + (-1)*C8__Z4CNDFf_2_13_OutputX_0_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_2_13_OutputX_0_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (-1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (-1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double + (-1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (-1)*_Z4CNDFf_2_13_OutputX_0_CAST_ret_fixbits==0)    #same fractional bit



#Stuff for double 1.000000e+00
ConstantValue__47_fixbits = solver.IntVar(0, 31, 'ConstantValue__47_fixbits')
ConstantValue__47_fixp = solver.IntVar(0, 1, 'ConstantValue__47_fixp')
ConstantValue__47_float = solver.IntVar(0, 1, 'ConstantValue__47_float')
ConstantValue__47_double = solver.IntVar(0, 1, 'ConstantValue__47_double')
ConstantValue__47_enob = solver.IntVar(-10000, 10000, 'ConstantValue__47_enob')
solver.Add( + (1)*ConstantValue__47_enob + (-1)*ConstantValue__47_fixbits + (10000)*ConstantValue__47_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__47_enob + (10000)*ConstantValue__47_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__47_enob + (10000)*ConstantValue__47_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__47_fixbits + (-10000)*ConstantValue__47_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__47_fixp + (1)*ConstantValue__47_float + (1)*ConstantValue__47_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__47_fixbits + (-10000)*ConstantValue__47_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call36 = call float @_Z4CNDFf.3.14(float %sub), !taffo.info !34, !taffo.initweight !39, !taffo.constinfo !40, !taffo.originalCall !74
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__48_fixbits = solver.IntVar(0, 32, 'ConstantValue__48_fixbits')
ConstantValue__48_fixp = solver.IntVar(0, 1, 'ConstantValue__48_fixp')
ConstantValue__48_float = solver.IntVar(0, 1, 'ConstantValue__48_float')
ConstantValue__48_double = solver.IntVar(0, 1, 'ConstantValue__48_double')
ConstantValue__48_enob = solver.IntVar(-10000, 10000, 'ConstantValue__48_enob')
solver.Add( + (1)*ConstantValue__48_enob + (-1)*ConstantValue__48_fixbits + (10000)*ConstantValue__48_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__48_enob + (10000)*ConstantValue__48_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__48_enob + (10000)*ConstantValue__48_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__48_fixbits + (-10000)*ConstantValue__48_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__48_fixp + (1)*ConstantValue__48_float + (1)*ConstantValue__48_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__48_fixbits + (-10000)*ConstantValue__48_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -0.000000e+00
ConstantValue__49_fixbits = solver.IntVar(0, 32, 'ConstantValue__49_fixbits')
ConstantValue__49_fixp = solver.IntVar(0, 1, 'ConstantValue__49_fixp')
ConstantValue__49_float = solver.IntVar(0, 1, 'ConstantValue__49_float')
ConstantValue__49_double = solver.IntVar(0, 1, 'ConstantValue__49_double')
ConstantValue__49_enob = solver.IntVar(-10000, 10000, 'ConstantValue__49_enob')
solver.Add( + (1)*ConstantValue__49_enob + (-1)*ConstantValue__49_fixbits + (10000)*ConstantValue__49_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__49_enob + (10000)*ConstantValue__49_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__49_enob + (10000)*ConstantValue__49_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__49_fixbits + (-10000)*ConstantValue__49_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__49_fixp + (1)*ConstantValue__49_float + (1)*ConstantValue__49_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__49_fixbits + (-10000)*ConstantValue__49_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -0.000000e+00
ConstantValue__50_fixbits = solver.IntVar(0, 32, 'ConstantValue__50_fixbits')
ConstantValue__50_fixp = solver.IntVar(0, 1, 'ConstantValue__50_fixp')
ConstantValue__50_float = solver.IntVar(0, 1, 'ConstantValue__50_float')
ConstantValue__50_double = solver.IntVar(0, 1, 'ConstantValue__50_double')
ConstantValue__50_enob = solver.IntVar(-10000, 10000, 'ConstantValue__50_enob')
solver.Add( + (1)*ConstantValue__50_enob + (-1)*ConstantValue__50_fixbits + (10000)*ConstantValue__50_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__50_enob + (10000)*ConstantValue__50_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__50_enob + (10000)*ConstantValue__50_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__50_fixbits + (-10000)*ConstantValue__50_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__50_fixp + (1)*ConstantValue__50_float + (1)*ConstantValue__50_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__50_fixbits + (-10000)*ConstantValue__50_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -0.000000e+00
ConstantValue__51_fixbits = solver.IntVar(0, 32, 'ConstantValue__51_fixbits')
ConstantValue__51_fixp = solver.IntVar(0, 1, 'ConstantValue__51_fixp')
ConstantValue__51_float = solver.IntVar(0, 1, 'ConstantValue__51_float')
ConstantValue__51_double = solver.IntVar(0, 1, 'ConstantValue__51_double')
ConstantValue__51_enob = solver.IntVar(-10000, 10000, 'ConstantValue__51_enob')
solver.Add( + (1)*ConstantValue__51_enob + (-1)*ConstantValue__51_fixbits + (10000)*ConstantValue__51_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__51_enob + (10000)*ConstantValue__51_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__51_enob + (10000)*ConstantValue__51_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__51_fixbits + (-10000)*ConstantValue__51_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__51_fixp + (1)*ConstantValue__51_float + (1)*ConstantValue__51_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__51_fixbits + (-10000)*ConstantValue__51_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub = fsub float -0.000000e+00, %InputX, !taffo.info !33, !taffo.initweight !23, !taffo.constinfo !35
ConstantValue__51_CAST_sub_fixbits = solver.IntVar(0, 32, 'ConstantValue__51_CAST_sub_fixbits')
ConstantValue__51_CAST_sub_fixp = solver.IntVar(0, 1, 'ConstantValue__51_CAST_sub_fixp')
ConstantValue__51_CAST_sub_float = solver.IntVar(0, 1, 'ConstantValue__51_CAST_sub_float')
ConstantValue__51_CAST_sub_double = solver.IntVar(0, 1, 'ConstantValue__51_CAST_sub_double')
solver.Add( + (1)*ConstantValue__51_CAST_sub_fixp + (1)*ConstantValue__51_CAST_sub_float + (1)*ConstantValue__51_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__51_CAST_sub_fixbits + (-10000)*ConstantValue__51_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C1_ConstantValue__51_CAST_sub')
C2_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C2_ConstantValue__51_CAST_sub')
solver.Add( + (1)*ConstantValue__51_fixbits + (-1)*ConstantValue__51_CAST_sub_fixbits + (-10000)*C1_ConstantValue__51_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__51_fixbits + (1)*ConstantValue__51_CAST_sub_fixbits + (-10000)*C2_ConstantValue__51_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__51_CAST_sub
castCostObj +=  + (1.13006)*C2_ConstantValue__51_CAST_sub
C3_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C3_ConstantValue__51_CAST_sub')
C4_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C4_ConstantValue__51_CAST_sub')
C5_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C5_ConstantValue__51_CAST_sub')
C6_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C6_ConstantValue__51_CAST_sub')
C7_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C7_ConstantValue__51_CAST_sub')
C8_ConstantValue__51_CAST_sub = solver.IntVar(0, 1, 'C8_ConstantValue__51_CAST_sub')
solver.Add( + (1)*ConstantValue__51_fixp + (1)*ConstantValue__51_CAST_sub_float + (-1)*C3_ConstantValue__51_CAST_sub<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__51_CAST_sub
solver.Add( + (1)*ConstantValue__51_float + (1)*ConstantValue__51_CAST_sub_fixp + (-1)*C4_ConstantValue__51_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__51_CAST_sub
solver.Add( + (1)*ConstantValue__51_fixp + (1)*ConstantValue__51_CAST_sub_double + (-1)*C5_ConstantValue__51_CAST_sub<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__51_CAST_sub
solver.Add( + (1)*ConstantValue__51_double + (1)*ConstantValue__51_CAST_sub_fixp + (-1)*C6_ConstantValue__51_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__51_CAST_sub
solver.Add( + (1)*ConstantValue__51_float + (1)*ConstantValue__51_CAST_sub_double + (-1)*C7_ConstantValue__51_CAST_sub<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__51_CAST_sub
solver.Add( + (1)*ConstantValue__51_double + (1)*ConstantValue__51_CAST_sub_float + (-1)*C8_ConstantValue__51_CAST_sub<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__51_CAST_sub



#Constraint for cast for   %sub = fsub float -0.000000e+00, %InputX, !taffo.info !33, !taffo.initweight !23, !taffo.constinfo !35
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixbits = solver.IntVar(0, 24, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub



#Stuff for   %sub = fsub float -0.000000e+00, %InputX, !taffo.info !33, !taffo.initweight !23, !taffo.constinfo !35
_Z4CNDFf_3_14_sub_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_3_14_sub_fixbits')
_Z4CNDFf_3_14_sub_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub_fixp')
_Z4CNDFf_3_14_sub_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub_float')
_Z4CNDFf_3_14_sub_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub_double')
_Z4CNDFf_3_14_sub_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_sub_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_sub_enob + (-1)*_Z4CNDFf_3_14_sub_fixbits + (10000)*_Z4CNDFf_3_14_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_sub_enob + (10000)*_Z4CNDFf_3_14_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_sub_enob + (10000)*_Z4CNDFf_3_14_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_sub_fixbits + (-10000)*_Z4CNDFf_3_14_sub_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_sub_enob
solver.Add( + (1)*_Z4CNDFf_3_14_sub_fixp + (1)*_Z4CNDFf_3_14_sub_float + (1)*_Z4CNDFf_3_14_sub_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_sub_fixbits + (-10000)*_Z4CNDFf_3_14_sub_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__51_CAST_sub_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__51_CAST_sub_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_float==0)    #float equality
solver.Add( + (1)*ConstantValue__51_CAST_sub_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_double==0)    #double equality
solver.Add( + (1)*ConstantValue__51_CAST_sub_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_sub_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__51_CAST_sub_fixp + (-1)*_Z4CNDFf_3_14_sub_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__51_CAST_sub_float + (-1)*_Z4CNDFf_3_14_sub_float==0)    #float equality
solver.Add( + (1)*ConstantValue__51_CAST_sub_double + (-1)*_Z4CNDFf_3_14_sub_double==0)    #double equality
solver.Add( + (1)*ConstantValue__51_CAST_sub_fixbits + (-1)*_Z4CNDFf_3_14_sub_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_sub_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_sub_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_sub_double
solver.Add( + (1)*_Z4CNDFf_3_14_sub_enob + (-1)*ConstantValue__49_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z4CNDFf_3_14_sub_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob<=0)    #Enob propagation in sub second addend



#Stuff for   %InputX.addr.0 = phi float [ %sub, %if.then ], [ %InputX, %if.else ], !taffo.info !39
_Z4CNDFf_3_14_InputX_addr_0_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_3_14_InputX_addr_0_fixbits')
_Z4CNDFf_3_14_InputX_addr_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_fixp')
_Z4CNDFf_3_14_InputX_addr_0_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_float')
_Z4CNDFf_3_14_InputX_addr_0_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_double')
_Z4CNDFf_3_14_InputX_addr_0_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_InputX_addr_0_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (-1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (10000)*_Z4CNDFf_3_14_InputX_addr_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (10000)*_Z4CNDFf_3_14_InputX_addr_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (10000)*_Z4CNDFf_3_14_InputX_addr_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (-10000)*_Z4CNDFf_3_14_InputX_addr_0_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_InputX_addr_0_enob
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (-10000)*_Z4CNDFf_3_14_InputX_addr_0_fixp<=0)    #If not fix, frac part to zero
_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_0 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_0')
_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_1')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_0 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %InputX.addr.0 = phi float [ %sub, %if.then ], [ %InputX, %if.else ], !taffo.info !39
_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixbits')
_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixp')
_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_float')
_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_double')
solver.Add( + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixbits + (-10000)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
C2__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
solver.Add( + (1)*_Z4CNDFf_3_14_sub_fixbits + (-1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixbits + (-10000)*C1__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_sub_fixbits + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixbits + (-10000)*C2__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
C3__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
C4__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
C5__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
C6__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
C7__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
C8__Z4CNDFf_3_14_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_sub_CAST_InputX_addr_0')
solver.Add( + (1)*_Z4CNDFf_3_14_sub_fixp + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_float + (-1)*C3__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub_float + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixp + (-1)*C4__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub_fixp + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_double + (-1)*C5__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub_double + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixp + (-1)*C6__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub_float + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_double + (-1)*C7__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub_double + (1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_float + (-1)*C8__Z4CNDFf_3_14_sub_CAST_InputX_addr_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (-1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (-1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (-1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_3_14_sub_CAST_InputX_addr_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (-1)*_Z4CNDFf_3_14_sub_enob + (10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_0<=10000)    #Enob: forcing phi enob



#Constraint for cast for   %InputX.addr.0 = phi float [ %sub, %if.then ], [ %InputX, %if.else ], !taffo.info !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixbits = solver.IntVar(0, 24, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_CAST_InputX_addr_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub_enob + (10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_InputX_addr_0_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   %mul = fmul float %InputX.addr.0, %InputX.addr.0, !taffo.info !41, !taffo.initweight !23
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixbits')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_float')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_double')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixbits + (-10000)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixbits + (-10000)*C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixbits + (-10000)*C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul
C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_float + (-1)*C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp + (-1)*C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_double + (-1)*C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp + (-1)*C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_double + (-1)*C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_float + (-1)*C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul



#Constraint for cast for   %mul = fmul float %InputX.addr.0, %InputX.addr.0, !taffo.info !41, !taffo.initweight !23
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixbits')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixp')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_float')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_double')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixbits + (-10000)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixbits + (-10000)*C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixbits + (-10000)*C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0
C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_float + (-1)*C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixp + (-1)*C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_double + (-1)*C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixp + (-1)*C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_double + (-1)*C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_float + (-1)*C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0



#Stuff for   %mul = fmul float %InputX.addr.0, %InputX.addr.0, !taffo.info !41, !taffo.initweight !23
_Z4CNDFf_3_14_mul_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_3_14_mul_fixbits')
_Z4CNDFf_3_14_mul_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul_fixp')
_Z4CNDFf_3_14_mul_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul_float')
_Z4CNDFf_3_14_mul_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul_double')
_Z4CNDFf_3_14_mul_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul_enob + (-1)*_Z4CNDFf_3_14_mul_fixbits + (10000)*_Z4CNDFf_3_14_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul_enob + (10000)*_Z4CNDFf_3_14_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul_enob + (10000)*_Z4CNDFf_3_14_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul_fixbits + (-10000)*_Z4CNDFf_3_14_mul_fixp>=-9983)    #Limit the lower number of frac bits18
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul_fixp + (1)*_Z4CNDFf_3_14_mul_float + (1)*_Z4CNDFf_3_14_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul_fixbits + (-10000)*_Z4CNDFf_3_14_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_float + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_double + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_fixp + (-1)*_Z4CNDFf_3_14_mul_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_float + (-1)*_Z4CNDFf_3_14_mul_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul_double + (-1)*_Z4CNDFf_3_14_mul_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul_enob + (-1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul_enob + (-1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for float -5.000000e-01
ConstantValue__52_fixbits = solver.IntVar(0, 30, 'ConstantValue__52_fixbits')
ConstantValue__52_fixp = solver.IntVar(0, 1, 'ConstantValue__52_fixp')
ConstantValue__52_float = solver.IntVar(0, 1, 'ConstantValue__52_float')
ConstantValue__52_double = solver.IntVar(0, 1, 'ConstantValue__52_double')
ConstantValue__52_enob = solver.IntVar(-10000, 10000, 'ConstantValue__52_enob')
solver.Add( + (1)*ConstantValue__52_enob + (-1)*ConstantValue__52_fixbits + (10000)*ConstantValue__52_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__52_enob + (10000)*ConstantValue__52_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__52_enob + (10000)*ConstantValue__52_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__52_fixbits + (-10000)*ConstantValue__52_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__52_fixp + (1)*ConstantValue__52_float + (1)*ConstantValue__52_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__52_fixbits + (-10000)*ConstantValue__52_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -5.000000e-01
ConstantValue__53_fixbits = solver.IntVar(0, 30, 'ConstantValue__53_fixbits')
ConstantValue__53_fixp = solver.IntVar(0, 1, 'ConstantValue__53_fixp')
ConstantValue__53_float = solver.IntVar(0, 1, 'ConstantValue__53_float')
ConstantValue__53_double = solver.IntVar(0, 1, 'ConstantValue__53_double')
ConstantValue__53_enob = solver.IntVar(-10000, 10000, 'ConstantValue__53_enob')
solver.Add( + (1)*ConstantValue__53_enob + (-1)*ConstantValue__53_fixbits + (10000)*ConstantValue__53_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__53_enob + (10000)*ConstantValue__53_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__53_enob + (10000)*ConstantValue__53_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__53_fixbits + (-10000)*ConstantValue__53_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__53_fixp + (1)*ConstantValue__53_float + (1)*ConstantValue__53_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__53_fixbits + (-10000)*ConstantValue__53_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -5.000000e-01
ConstantValue__54_fixbits = solver.IntVar(0, 30, 'ConstantValue__54_fixbits')
ConstantValue__54_fixp = solver.IntVar(0, 1, 'ConstantValue__54_fixp')
ConstantValue__54_float = solver.IntVar(0, 1, 'ConstantValue__54_float')
ConstantValue__54_double = solver.IntVar(0, 1, 'ConstantValue__54_double')
ConstantValue__54_enob = solver.IntVar(-10000, 10000, 'ConstantValue__54_enob')
solver.Add( + (1)*ConstantValue__54_enob + (-1)*ConstantValue__54_fixbits + (10000)*ConstantValue__54_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__54_enob + (10000)*ConstantValue__54_float<=10024)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__54_enob + (10000)*ConstantValue__54_double<=10053)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__54_fixbits + (-10000)*ConstantValue__54_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__54_fixp + (1)*ConstantValue__54_float + (1)*ConstantValue__54_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__54_fixbits + (-10000)*ConstantValue__54_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul16 = fmul float -5.000000e-01, %mul, !taffo.info !43, !taffo.initweight !30, !taffo.constinfo !45
ConstantValue__54_CAST_mul16_fixbits = solver.IntVar(0, 30, 'ConstantValue__54_CAST_mul16_fixbits')
ConstantValue__54_CAST_mul16_fixp = solver.IntVar(0, 1, 'ConstantValue__54_CAST_mul16_fixp')
ConstantValue__54_CAST_mul16_float = solver.IntVar(0, 1, 'ConstantValue__54_CAST_mul16_float')
ConstantValue__54_CAST_mul16_double = solver.IntVar(0, 1, 'ConstantValue__54_CAST_mul16_double')
solver.Add( + (1)*ConstantValue__54_CAST_mul16_fixp + (1)*ConstantValue__54_CAST_mul16_float + (1)*ConstantValue__54_CAST_mul16_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__54_CAST_mul16_fixbits + (-10000)*ConstantValue__54_CAST_mul16_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C1_ConstantValue__54_CAST_mul16')
C2_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C2_ConstantValue__54_CAST_mul16')
solver.Add( + (1)*ConstantValue__54_fixbits + (-1)*ConstantValue__54_CAST_mul16_fixbits + (-10000)*C1_ConstantValue__54_CAST_mul16<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__54_fixbits + (1)*ConstantValue__54_CAST_mul16_fixbits + (-10000)*C2_ConstantValue__54_CAST_mul16<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__54_CAST_mul16
castCostObj +=  + (1.13006)*C2_ConstantValue__54_CAST_mul16
C3_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C3_ConstantValue__54_CAST_mul16')
C4_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C4_ConstantValue__54_CAST_mul16')
C5_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C5_ConstantValue__54_CAST_mul16')
C6_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C6_ConstantValue__54_CAST_mul16')
C7_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C7_ConstantValue__54_CAST_mul16')
C8_ConstantValue__54_CAST_mul16 = solver.IntVar(0, 1, 'C8_ConstantValue__54_CAST_mul16')
solver.Add( + (1)*ConstantValue__54_fixp + (1)*ConstantValue__54_CAST_mul16_float + (-1)*C3_ConstantValue__54_CAST_mul16<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__54_CAST_mul16
solver.Add( + (1)*ConstantValue__54_float + (1)*ConstantValue__54_CAST_mul16_fixp + (-1)*C4_ConstantValue__54_CAST_mul16<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__54_CAST_mul16
solver.Add( + (1)*ConstantValue__54_fixp + (1)*ConstantValue__54_CAST_mul16_double + (-1)*C5_ConstantValue__54_CAST_mul16<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__54_CAST_mul16
solver.Add( + (1)*ConstantValue__54_double + (1)*ConstantValue__54_CAST_mul16_fixp + (-1)*C6_ConstantValue__54_CAST_mul16<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__54_CAST_mul16
solver.Add( + (1)*ConstantValue__54_float + (1)*ConstantValue__54_CAST_mul16_double + (-1)*C7_ConstantValue__54_CAST_mul16<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__54_CAST_mul16
solver.Add( + (1)*ConstantValue__54_double + (1)*ConstantValue__54_CAST_mul16_float + (-1)*C8_ConstantValue__54_CAST_mul16<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__54_CAST_mul16



#Constraint for cast for   %mul16 = fmul float -5.000000e-01, %mul, !taffo.info !43, !taffo.initweight !30, !taffo.constinfo !45
_Z4CNDFf_3_14_mul_CAST_mul16_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_3_14_mul_CAST_mul16_fixbits')
_Z4CNDFf_3_14_mul_CAST_mul16_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul_CAST_mul16_fixp')
_Z4CNDFf_3_14_mul_CAST_mul16_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul_CAST_mul16_float')
_Z4CNDFf_3_14_mul_CAST_mul16_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul_CAST_mul16_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_fixp + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_float + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_fixbits + (-10000)*_Z4CNDFf_3_14_mul_CAST_mul16_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul_CAST_mul16')
C2__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul_CAST_mul16')
solver.Add( + (1)*_Z4CNDFf_3_14_mul_fixbits + (-1)*_Z4CNDFf_3_14_mul_CAST_mul16_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul_CAST_mul16<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul_fixbits + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul_CAST_mul16<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul_CAST_mul16
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul_CAST_mul16
C3__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul_CAST_mul16')
C4__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul_CAST_mul16')
C5__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul_CAST_mul16')
C6__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul_CAST_mul16')
C7__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul_CAST_mul16')
C8__Z4CNDFf_3_14_mul_CAST_mul16 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul_CAST_mul16')
solver.Add( + (1)*_Z4CNDFf_3_14_mul_fixp + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_float + (-1)*C3__Z4CNDFf_3_14_mul_CAST_mul16<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_3_14_mul_float + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_fixp + (-1)*C4__Z4CNDFf_3_14_mul_CAST_mul16<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_3_14_mul_fixp + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_double + (-1)*C5__Z4CNDFf_3_14_mul_CAST_mul16<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_3_14_mul_double + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_fixp + (-1)*C6__Z4CNDFf_3_14_mul_CAST_mul16<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_3_14_mul_float + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_double + (-1)*C7__Z4CNDFf_3_14_mul_CAST_mul16<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul_CAST_mul16
solver.Add( + (1)*_Z4CNDFf_3_14_mul_double + (1)*_Z4CNDFf_3_14_mul_CAST_mul16_float + (-1)*C8__Z4CNDFf_3_14_mul_CAST_mul16<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul_CAST_mul16



#Stuff for   %mul16 = fmul float -5.000000e-01, %mul, !taffo.info !43, !taffo.initweight !30, !taffo.constinfo !45
_Z4CNDFf_3_14_mul16_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_3_14_mul16_fixbits')
_Z4CNDFf_3_14_mul16_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul16_fixp')
_Z4CNDFf_3_14_mul16_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul16_float')
_Z4CNDFf_3_14_mul16_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul16_double')
_Z4CNDFf_3_14_mul16_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul16_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_enob + (-1)*_Z4CNDFf_3_14_mul16_fixbits + (10000)*_Z4CNDFf_3_14_mul16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_enob + (10000)*_Z4CNDFf_3_14_mul16_float<=10020)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_enob + (10000)*_Z4CNDFf_3_14_mul16_double<=10049)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_fixbits + (-10000)*_Z4CNDFf_3_14_mul16_fixp>=-9983)    #Limit the lower number of frac bits18
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul16_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_fixp + (1)*_Z4CNDFf_3_14_mul16_float + (1)*_Z4CNDFf_3_14_mul16_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_fixbits + (-10000)*_Z4CNDFf_3_14_mul16_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__54_CAST_mul16_fixp + (-1)*_Z4CNDFf_3_14_mul_CAST_mul16_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__54_CAST_mul16_float + (-1)*_Z4CNDFf_3_14_mul_CAST_mul16_float==0)    #float equality
solver.Add( + (1)*ConstantValue__54_CAST_mul16_double + (-1)*_Z4CNDFf_3_14_mul_CAST_mul16_double==0)    #double equality
solver.Add( + (1)*ConstantValue__54_CAST_mul16_fixp + (-1)*_Z4CNDFf_3_14_mul16_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__54_CAST_mul16_float + (-1)*_Z4CNDFf_3_14_mul16_float==0)    #float equality
solver.Add( + (1)*ConstantValue__54_CAST_mul16_double + (-1)*_Z4CNDFf_3_14_mul16_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul16_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul16_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul16_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_enob + (-1)*_Z4CNDFf_3_14_mul_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_1<=1)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_enob + (-1)*ConstantValue__52_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul16_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for   %call = call float @_ZSt3expf.9.16(float %mul16), !taffo.info !48, !taffo.initweight !32, !taffo.constinfo !50, !taffo.originalCall !51
_Z4CNDFf_3_14_call_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_3_14_call_fixbits')
_Z4CNDFf_3_14_call_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_call_fixp')
_Z4CNDFf_3_14_call_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_call_float')
_Z4CNDFf_3_14_call_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_call_double')
_Z4CNDFf_3_14_call_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_call_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_call_enob + (-1)*_Z4CNDFf_3_14_call_fixbits + (10000)*_Z4CNDFf_3_14_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_call_enob + (10000)*_Z4CNDFf_3_14_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_call_enob + (10000)*_Z4CNDFf_3_14_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixbits + (-10000)*_Z4CNDFf_3_14_call_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_call_enob
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixp + (1)*_Z4CNDFf_3_14_call_float + (1)*_Z4CNDFf_3_14_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixbits + (-10000)*_Z4CNDFf_3_14_call_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call = call float @expf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_ZSt3expf_9_16_call_fixbits = solver.IntVar(0, 31, '_ZSt3expf_9_16_call_fixbits')
_ZSt3expf_9_16_call_fixp = solver.IntVar(0, 1, '_ZSt3expf_9_16_call_fixp')
_ZSt3expf_9_16_call_float = solver.IntVar(0, 1, '_ZSt3expf_9_16_call_float')
_ZSt3expf_9_16_call_double = solver.IntVar(0, 1, '_ZSt3expf_9_16_call_double')
_ZSt3expf_9_16_call_enob = solver.IntVar(-10000, 10000, '_ZSt3expf_9_16_call_enob')
solver.Add( + (1)*_ZSt3expf_9_16_call_enob + (-1)*_ZSt3expf_9_16_call_fixbits + (10000)*_ZSt3expf_9_16_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_ZSt3expf_9_16_call_enob + (10000)*_ZSt3expf_9_16_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_ZSt3expf_9_16_call_enob + (10000)*_ZSt3expf_9_16_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_ZSt3expf_9_16_call_fixbits + (-10000)*_ZSt3expf_9_16_call_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_ZSt3expf_9_16_call_enob
solver.Add( + (1)*_ZSt3expf_9_16_call_fixp + (1)*_ZSt3expf_9_16_call_float + (1)*_ZSt3expf_9_16_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_ZSt3expf_9_16_call_fixbits + (-10000)*_ZSt3expf_9_16_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_ZSt3expf_9_16_call_float==1)    #Type constraint for return value



#Constraint for cast for   %call = call float @expf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_Z4CNDFf_3_14_mul16_CAST_call_fixbits = solver.IntVar(0, 18, '_Z4CNDFf_3_14_mul16_CAST_call_fixbits')
_Z4CNDFf_3_14_mul16_CAST_call_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul16_CAST_call_fixp')
_Z4CNDFf_3_14_mul16_CAST_call_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul16_CAST_call_float')
_Z4CNDFf_3_14_mul16_CAST_call_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul16_CAST_call_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_CAST_call_fixp + (1)*_Z4CNDFf_3_14_mul16_CAST_call_float + (1)*_Z4CNDFf_3_14_mul16_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_CAST_call_fixbits + (-10000)*_Z4CNDFf_3_14_mul16_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul16_CAST_call')
C2__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul16_CAST_call')
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_fixbits + (-1)*_Z4CNDFf_3_14_mul16_CAST_call_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul16_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul16_fixbits + (1)*_Z4CNDFf_3_14_mul16_CAST_call_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul16_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul16_CAST_call
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul16_CAST_call
C3__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul16_CAST_call')
C4__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul16_CAST_call')
C5__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul16_CAST_call')
C6__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul16_CAST_call')
C7__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul16_CAST_call')
C8__Z4CNDFf_3_14_mul16_CAST_call = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul16_CAST_call')
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_fixp + (1)*_Z4CNDFf_3_14_mul16_CAST_call_float + (-1)*C3__Z4CNDFf_3_14_mul16_CAST_call<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_float + (1)*_Z4CNDFf_3_14_mul16_CAST_call_fixp + (-1)*C4__Z4CNDFf_3_14_mul16_CAST_call<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_fixp + (1)*_Z4CNDFf_3_14_mul16_CAST_call_double + (-1)*C5__Z4CNDFf_3_14_mul16_CAST_call<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_double + (1)*_Z4CNDFf_3_14_mul16_CAST_call_fixp + (-1)*C6__Z4CNDFf_3_14_mul16_CAST_call<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_float + (1)*_Z4CNDFf_3_14_mul16_CAST_call_double + (-1)*C7__Z4CNDFf_3_14_mul16_CAST_call<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_double + (1)*_Z4CNDFf_3_14_mul16_CAST_call_float + (-1)*C8__Z4CNDFf_3_14_mul16_CAST_call<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul16_CAST_call
solver.Add( + (1)*_Z4CNDFf_3_14_mul16_CAST_call_float==1)    #Type constraint for argument value



#Constraint for cast for   ret float %call, !taffo.info !32, !taffo.initweight !34
_ZSt3expf_9_16_call_CAST_ret_fixbits = solver.IntVar(0, 31, '_ZSt3expf_9_16_call_CAST_ret_fixbits')
_ZSt3expf_9_16_call_CAST_ret_fixp = solver.IntVar(0, 1, '_ZSt3expf_9_16_call_CAST_ret_fixp')
_ZSt3expf_9_16_call_CAST_ret_float = solver.IntVar(0, 1, '_ZSt3expf_9_16_call_CAST_ret_float')
_ZSt3expf_9_16_call_CAST_ret_double = solver.IntVar(0, 1, '_ZSt3expf_9_16_call_CAST_ret_double')
solver.Add( + (1)*_ZSt3expf_9_16_call_CAST_ret_fixp + (1)*_ZSt3expf_9_16_call_CAST_ret_float + (1)*_ZSt3expf_9_16_call_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_ZSt3expf_9_16_call_CAST_ret_fixbits + (-10000)*_ZSt3expf_9_16_call_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C1__ZSt3expf_9_16_call_CAST_ret')
C2__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C2__ZSt3expf_9_16_call_CAST_ret')
solver.Add( + (1)*_ZSt3expf_9_16_call_fixbits + (-1)*_ZSt3expf_9_16_call_CAST_ret_fixbits + (-10000)*C1__ZSt3expf_9_16_call_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_ZSt3expf_9_16_call_fixbits + (1)*_ZSt3expf_9_16_call_CAST_ret_fixbits + (-10000)*C2__ZSt3expf_9_16_call_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__ZSt3expf_9_16_call_CAST_ret
castCostObj +=  + (1.13006)*C2__ZSt3expf_9_16_call_CAST_ret
C3__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C3__ZSt3expf_9_16_call_CAST_ret')
C4__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C4__ZSt3expf_9_16_call_CAST_ret')
C5__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C5__ZSt3expf_9_16_call_CAST_ret')
C6__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C6__ZSt3expf_9_16_call_CAST_ret')
C7__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C7__ZSt3expf_9_16_call_CAST_ret')
C8__ZSt3expf_9_16_call_CAST_ret = solver.IntVar(0, 1, 'C8__ZSt3expf_9_16_call_CAST_ret')
solver.Add( + (1)*_ZSt3expf_9_16_call_fixp + (1)*_ZSt3expf_9_16_call_CAST_ret_float + (-1)*C3__ZSt3expf_9_16_call_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__ZSt3expf_9_16_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_9_16_call_float + (1)*_ZSt3expf_9_16_call_CAST_ret_fixp + (-1)*C4__ZSt3expf_9_16_call_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__ZSt3expf_9_16_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_9_16_call_fixp + (1)*_ZSt3expf_9_16_call_CAST_ret_double + (-1)*C5__ZSt3expf_9_16_call_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__ZSt3expf_9_16_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_9_16_call_double + (1)*_ZSt3expf_9_16_call_CAST_ret_fixp + (-1)*C6__ZSt3expf_9_16_call_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__ZSt3expf_9_16_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_9_16_call_float + (1)*_ZSt3expf_9_16_call_CAST_ret_double + (-1)*C7__ZSt3expf_9_16_call_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__ZSt3expf_9_16_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_9_16_call_double + (1)*_ZSt3expf_9_16_call_CAST_ret_float + (-1)*C8__ZSt3expf_9_16_call_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__ZSt3expf_9_16_call_CAST_ret
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixp + (-1)*_ZSt3expf_9_16_call_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_float + (-1)*_ZSt3expf_9_16_call_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_double + (-1)*_ZSt3expf_9_16_call_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixbits + (-1)*_ZSt3expf_9_16_call_CAST_ret_fixbits==0)    #same fractional bit



#Stuff for double 0x3FD9884533D43651
ConstantValue__55_fixbits = solver.IntVar(0, 31, 'ConstantValue__55_fixbits')
ConstantValue__55_fixp = solver.IntVar(0, 1, 'ConstantValue__55_fixp')
ConstantValue__55_float = solver.IntVar(0, 1, 'ConstantValue__55_float')
ConstantValue__55_double = solver.IntVar(0, 1, 'ConstantValue__55_double')
ConstantValue__55_enob = solver.IntVar(-10000, 10000, 'ConstantValue__55_enob')
solver.Add( + (1)*ConstantValue__55_enob + (-1)*ConstantValue__55_fixbits + (10000)*ConstantValue__55_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__55_enob + (10000)*ConstantValue__55_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__55_enob + (10000)*ConstantValue__55_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__55_fixbits + (-10000)*ConstantValue__55_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__55_fixp + (1)*ConstantValue__55_float + (1)*ConstantValue__55_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__55_fixbits + (-10000)*ConstantValue__55_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FD9884533D43651
ConstantValue__56_fixbits = solver.IntVar(0, 31, 'ConstantValue__56_fixbits')
ConstantValue__56_fixp = solver.IntVar(0, 1, 'ConstantValue__56_fixp')
ConstantValue__56_float = solver.IntVar(0, 1, 'ConstantValue__56_float')
ConstantValue__56_double = solver.IntVar(0, 1, 'ConstantValue__56_double')
ConstantValue__56_enob = solver.IntVar(-10000, 10000, 'ConstantValue__56_enob')
solver.Add( + (1)*ConstantValue__56_enob + (-1)*ConstantValue__56_fixbits + (10000)*ConstantValue__56_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__56_enob + (10000)*ConstantValue__56_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__56_enob + (10000)*ConstantValue__56_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__56_fixbits + (-10000)*ConstantValue__56_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__56_fixp + (1)*ConstantValue__56_float + (1)*ConstantValue__56_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__56_fixbits + (-10000)*ConstantValue__56_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul18 = fmul double %conv17, 0x3FD9884533D43651, !taffo.info !53, !taffo.initweight !30, !taffo.constinfo !55
_Z4CNDFf_3_14_call_CAST_mul18_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_3_14_call_CAST_mul18_fixbits')
_Z4CNDFf_3_14_call_CAST_mul18_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_call_CAST_mul18_fixp')
_Z4CNDFf_3_14_call_CAST_mul18_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_call_CAST_mul18_float')
_Z4CNDFf_3_14_call_CAST_mul18_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_call_CAST_mul18_double')
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_fixp + (1)*_Z4CNDFf_3_14_call_CAST_mul18_float + (1)*_Z4CNDFf_3_14_call_CAST_mul18_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_fixbits + (-10000)*_Z4CNDFf_3_14_call_CAST_mul18_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_call_CAST_mul18')
C2__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_call_CAST_mul18')
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixbits + (-1)*_Z4CNDFf_3_14_call_CAST_mul18_fixbits + (-10000)*C1__Z4CNDFf_3_14_call_CAST_mul18<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_call_fixbits + (1)*_Z4CNDFf_3_14_call_CAST_mul18_fixbits + (-10000)*C2__Z4CNDFf_3_14_call_CAST_mul18<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_call_CAST_mul18
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_call_CAST_mul18
C3__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_call_CAST_mul18')
C4__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_call_CAST_mul18')
C5__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_call_CAST_mul18')
C6__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_call_CAST_mul18')
C7__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_call_CAST_mul18')
C8__Z4CNDFf_3_14_call_CAST_mul18 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_call_CAST_mul18')
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixp + (1)*_Z4CNDFf_3_14_call_CAST_mul18_float + (-1)*C3__Z4CNDFf_3_14_call_CAST_mul18<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_3_14_call_float + (1)*_Z4CNDFf_3_14_call_CAST_mul18_fixp + (-1)*C4__Z4CNDFf_3_14_call_CAST_mul18<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_3_14_call_fixp + (1)*_Z4CNDFf_3_14_call_CAST_mul18_double + (-1)*C5__Z4CNDFf_3_14_call_CAST_mul18<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_3_14_call_double + (1)*_Z4CNDFf_3_14_call_CAST_mul18_fixp + (-1)*C6__Z4CNDFf_3_14_call_CAST_mul18<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_3_14_call_float + (1)*_Z4CNDFf_3_14_call_CAST_mul18_double + (-1)*C7__Z4CNDFf_3_14_call_CAST_mul18<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_call_CAST_mul18
solver.Add( + (1)*_Z4CNDFf_3_14_call_double + (1)*_Z4CNDFf_3_14_call_CAST_mul18_float + (-1)*C8__Z4CNDFf_3_14_call_CAST_mul18<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_call_CAST_mul18



#Stuff for double 0x3FD9884533D43651
ConstantValue__57_fixbits = solver.IntVar(0, 31, 'ConstantValue__57_fixbits')
ConstantValue__57_fixp = solver.IntVar(0, 1, 'ConstantValue__57_fixp')
ConstantValue__57_float = solver.IntVar(0, 1, 'ConstantValue__57_float')
ConstantValue__57_double = solver.IntVar(0, 1, 'ConstantValue__57_double')
ConstantValue__57_enob = solver.IntVar(-10000, 10000, 'ConstantValue__57_enob')
solver.Add( + (1)*ConstantValue__57_enob + (-1)*ConstantValue__57_fixbits + (10000)*ConstantValue__57_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__57_enob + (10000)*ConstantValue__57_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__57_enob + (10000)*ConstantValue__57_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__57_fixbits + (-10000)*ConstantValue__57_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__57_fixp + (1)*ConstantValue__57_float + (1)*ConstantValue__57_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__57_fixbits + (-10000)*ConstantValue__57_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul18 = fmul double %conv17, 0x3FD9884533D43651, !taffo.info !53, !taffo.initweight !30, !taffo.constinfo !55
ConstantValue__57_CAST_mul18_fixbits = solver.IntVar(0, 31, 'ConstantValue__57_CAST_mul18_fixbits')
ConstantValue__57_CAST_mul18_fixp = solver.IntVar(0, 1, 'ConstantValue__57_CAST_mul18_fixp')
ConstantValue__57_CAST_mul18_float = solver.IntVar(0, 1, 'ConstantValue__57_CAST_mul18_float')
ConstantValue__57_CAST_mul18_double = solver.IntVar(0, 1, 'ConstantValue__57_CAST_mul18_double')
solver.Add( + (1)*ConstantValue__57_CAST_mul18_fixp + (1)*ConstantValue__57_CAST_mul18_float + (1)*ConstantValue__57_CAST_mul18_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__57_CAST_mul18_fixbits + (-10000)*ConstantValue__57_CAST_mul18_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C1_ConstantValue__57_CAST_mul18')
C2_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C2_ConstantValue__57_CAST_mul18')
solver.Add( + (1)*ConstantValue__57_fixbits + (-1)*ConstantValue__57_CAST_mul18_fixbits + (-10000)*C1_ConstantValue__57_CAST_mul18<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__57_fixbits + (1)*ConstantValue__57_CAST_mul18_fixbits + (-10000)*C2_ConstantValue__57_CAST_mul18<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__57_CAST_mul18
castCostObj +=  + (1.13006)*C2_ConstantValue__57_CAST_mul18
C3_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C3_ConstantValue__57_CAST_mul18')
C4_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C4_ConstantValue__57_CAST_mul18')
C5_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C5_ConstantValue__57_CAST_mul18')
C6_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C6_ConstantValue__57_CAST_mul18')
C7_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C7_ConstantValue__57_CAST_mul18')
C8_ConstantValue__57_CAST_mul18 = solver.IntVar(0, 1, 'C8_ConstantValue__57_CAST_mul18')
solver.Add( + (1)*ConstantValue__57_fixp + (1)*ConstantValue__57_CAST_mul18_float + (-1)*C3_ConstantValue__57_CAST_mul18<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__57_CAST_mul18
solver.Add( + (1)*ConstantValue__57_float + (1)*ConstantValue__57_CAST_mul18_fixp + (-1)*C4_ConstantValue__57_CAST_mul18<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__57_CAST_mul18
solver.Add( + (1)*ConstantValue__57_fixp + (1)*ConstantValue__57_CAST_mul18_double + (-1)*C5_ConstantValue__57_CAST_mul18<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__57_CAST_mul18
solver.Add( + (1)*ConstantValue__57_double + (1)*ConstantValue__57_CAST_mul18_fixp + (-1)*C6_ConstantValue__57_CAST_mul18<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__57_CAST_mul18
solver.Add( + (1)*ConstantValue__57_float + (1)*ConstantValue__57_CAST_mul18_double + (-1)*C7_ConstantValue__57_CAST_mul18<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__57_CAST_mul18
solver.Add( + (1)*ConstantValue__57_double + (1)*ConstantValue__57_CAST_mul18_float + (-1)*C8_ConstantValue__57_CAST_mul18<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__57_CAST_mul18



#Stuff for   %mul18 = fmul double %conv17, 0x3FD9884533D43651, !taffo.info !53, !taffo.initweight !30, !taffo.constinfo !55
_Z4CNDFf_3_14_mul18_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_3_14_mul18_fixbits')
_Z4CNDFf_3_14_mul18_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul18_fixp')
_Z4CNDFf_3_14_mul18_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul18_float')
_Z4CNDFf_3_14_mul18_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul18_double')
_Z4CNDFf_3_14_mul18_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul18_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_enob + (-1)*_Z4CNDFf_3_14_mul18_fixbits + (10000)*_Z4CNDFf_3_14_mul18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_enob + (10000)*_Z4CNDFf_3_14_mul18_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_enob + (10000)*_Z4CNDFf_3_14_mul18_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_fixbits + (-10000)*_Z4CNDFf_3_14_mul18_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul18_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_fixp + (1)*_Z4CNDFf_3_14_mul18_float + (1)*_Z4CNDFf_3_14_mul18_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_fixbits + (-10000)*_Z4CNDFf_3_14_mul18_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_fixp + (-1)*ConstantValue__57_CAST_mul18_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_float + (-1)*ConstantValue__57_CAST_mul18_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_double + (-1)*ConstantValue__57_CAST_mul18_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_fixp + (-1)*_Z4CNDFf_3_14_mul18_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_float + (-1)*_Z4CNDFf_3_14_mul18_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_call_CAST_mul18_double + (-1)*_Z4CNDFf_3_14_mul18_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul18_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul18_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul18_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_enob + (-1)*ConstantValue__55_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_enob + (-1)*_Z4CNDFf_3_14_call_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul18_enob_2<=1)    #Enob: propagation in product 2



#Stuff for double 0x3FCDA6711871100E
ConstantValue__58_fixbits = solver.IntVar(0, 31, 'ConstantValue__58_fixbits')
ConstantValue__58_fixp = solver.IntVar(0, 1, 'ConstantValue__58_fixp')
ConstantValue__58_float = solver.IntVar(0, 1, 'ConstantValue__58_float')
ConstantValue__58_double = solver.IntVar(0, 1, 'ConstantValue__58_double')
ConstantValue__58_enob = solver.IntVar(-10000, 10000, 'ConstantValue__58_enob')
solver.Add( + (1)*ConstantValue__58_enob + (-1)*ConstantValue__58_fixbits + (10000)*ConstantValue__58_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__58_enob + (10000)*ConstantValue__58_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__58_enob + (10000)*ConstantValue__58_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__58_fixbits + (-10000)*ConstantValue__58_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__58_fixp + (1)*ConstantValue__58_float + (1)*ConstantValue__58_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__58_fixbits + (-10000)*ConstantValue__58_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FCDA6711871100E
ConstantValue__59_fixbits = solver.IntVar(0, 31, 'ConstantValue__59_fixbits')
ConstantValue__59_fixp = solver.IntVar(0, 1, 'ConstantValue__59_fixp')
ConstantValue__59_float = solver.IntVar(0, 1, 'ConstantValue__59_float')
ConstantValue__59_double = solver.IntVar(0, 1, 'ConstantValue__59_double')
ConstantValue__59_enob = solver.IntVar(-10000, 10000, 'ConstantValue__59_enob')
solver.Add( + (1)*ConstantValue__59_enob + (-1)*ConstantValue__59_fixbits + (10000)*ConstantValue__59_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__59_enob + (10000)*ConstantValue__59_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__59_enob + (10000)*ConstantValue__59_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__59_fixbits + (-10000)*ConstantValue__59_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__59_fixp + (1)*ConstantValue__59_float + (1)*ConstantValue__59_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__59_fixbits + (-10000)*ConstantValue__59_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FCDA6711871100E
ConstantValue__60_fixbits = solver.IntVar(0, 31, 'ConstantValue__60_fixbits')
ConstantValue__60_fixp = solver.IntVar(0, 1, 'ConstantValue__60_fixp')
ConstantValue__60_float = solver.IntVar(0, 1, 'ConstantValue__60_float')
ConstantValue__60_double = solver.IntVar(0, 1, 'ConstantValue__60_double')
ConstantValue__60_enob = solver.IntVar(-10000, 10000, 'ConstantValue__60_enob')
solver.Add( + (1)*ConstantValue__60_enob + (-1)*ConstantValue__60_fixbits + (10000)*ConstantValue__60_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__60_enob + (10000)*ConstantValue__60_float<=10026)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__60_enob + (10000)*ConstantValue__60_double<=10055)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__60_fixbits + (-10000)*ConstantValue__60_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__60_fixp + (1)*ConstantValue__60_float + (1)*ConstantValue__60_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__60_fixbits + (-10000)*ConstantValue__60_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul21 = fmul double 0x3FCDA6711871100E, %conv20, !taffo.info !61, !taffo.initweight !30, !taffo.constinfo !63
ConstantValue__60_CAST_mul21_fixbits = solver.IntVar(0, 31, 'ConstantValue__60_CAST_mul21_fixbits')
ConstantValue__60_CAST_mul21_fixp = solver.IntVar(0, 1, 'ConstantValue__60_CAST_mul21_fixp')
ConstantValue__60_CAST_mul21_float = solver.IntVar(0, 1, 'ConstantValue__60_CAST_mul21_float')
ConstantValue__60_CAST_mul21_double = solver.IntVar(0, 1, 'ConstantValue__60_CAST_mul21_double')
solver.Add( + (1)*ConstantValue__60_CAST_mul21_fixp + (1)*ConstantValue__60_CAST_mul21_float + (1)*ConstantValue__60_CAST_mul21_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__60_CAST_mul21_fixbits + (-10000)*ConstantValue__60_CAST_mul21_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C1_ConstantValue__60_CAST_mul21')
C2_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C2_ConstantValue__60_CAST_mul21')
solver.Add( + (1)*ConstantValue__60_fixbits + (-1)*ConstantValue__60_CAST_mul21_fixbits + (-10000)*C1_ConstantValue__60_CAST_mul21<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__60_fixbits + (1)*ConstantValue__60_CAST_mul21_fixbits + (-10000)*C2_ConstantValue__60_CAST_mul21<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__60_CAST_mul21
castCostObj +=  + (1.13006)*C2_ConstantValue__60_CAST_mul21
C3_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C3_ConstantValue__60_CAST_mul21')
C4_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C4_ConstantValue__60_CAST_mul21')
C5_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C5_ConstantValue__60_CAST_mul21')
C6_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C6_ConstantValue__60_CAST_mul21')
C7_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C7_ConstantValue__60_CAST_mul21')
C8_ConstantValue__60_CAST_mul21 = solver.IntVar(0, 1, 'C8_ConstantValue__60_CAST_mul21')
solver.Add( + (1)*ConstantValue__60_fixp + (1)*ConstantValue__60_CAST_mul21_float + (-1)*C3_ConstantValue__60_CAST_mul21<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__60_CAST_mul21
solver.Add( + (1)*ConstantValue__60_float + (1)*ConstantValue__60_CAST_mul21_fixp + (-1)*C4_ConstantValue__60_CAST_mul21<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__60_CAST_mul21
solver.Add( + (1)*ConstantValue__60_fixp + (1)*ConstantValue__60_CAST_mul21_double + (-1)*C5_ConstantValue__60_CAST_mul21<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__60_CAST_mul21
solver.Add( + (1)*ConstantValue__60_double + (1)*ConstantValue__60_CAST_mul21_fixp + (-1)*C6_ConstantValue__60_CAST_mul21<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__60_CAST_mul21
solver.Add( + (1)*ConstantValue__60_float + (1)*ConstantValue__60_CAST_mul21_double + (-1)*C7_ConstantValue__60_CAST_mul21<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__60_CAST_mul21
solver.Add( + (1)*ConstantValue__60_double + (1)*ConstantValue__60_CAST_mul21_float + (-1)*C8_ConstantValue__60_CAST_mul21<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__60_CAST_mul21



#Constraint for cast for   %mul21 = fmul double 0x3FCDA6711871100E, %conv20, !taffo.info !61, !taffo.initweight !30, !taffo.constinfo !63
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixbits = solver.IntVar(0, 24, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixbits')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixp')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_float')
_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_double')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixbits + (-10000)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixbits + (-10000)*C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_InputX_addr_0_fixbits + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixbits + (-10000)*C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21
C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21')
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_float + (-1)*C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixp + (-1)*C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_fixp + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_double + (-1)*C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixp + (-1)*C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_float + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_double + (-1)*C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21
solver.Add( + (1)*_Z4CNDFf_3_14_InputX_addr_0_double + (1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_float + (-1)*C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_InputX_addr_0_CAST_mul21



#Stuff for   %mul21 = fmul double 0x3FCDA6711871100E, %conv20, !taffo.info !61, !taffo.initweight !30, !taffo.constinfo !63
_Z4CNDFf_3_14_mul21_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_3_14_mul21_fixbits')
_Z4CNDFf_3_14_mul21_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul21_fixp')
_Z4CNDFf_3_14_mul21_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul21_float')
_Z4CNDFf_3_14_mul21_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul21_double')
_Z4CNDFf_3_14_mul21_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul21_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_enob + (-1)*_Z4CNDFf_3_14_mul21_fixbits + (10000)*_Z4CNDFf_3_14_mul21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_enob + (10000)*_Z4CNDFf_3_14_mul21_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_enob + (10000)*_Z4CNDFf_3_14_mul21_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_fixbits + (-10000)*_Z4CNDFf_3_14_mul21_fixp>=-9975)    #Limit the lower number of frac bits26
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul21_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_fixp + (1)*_Z4CNDFf_3_14_mul21_float + (1)*_Z4CNDFf_3_14_mul21_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_fixbits + (-10000)*_Z4CNDFf_3_14_mul21_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__60_CAST_mul21_fixp + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__60_CAST_mul21_float + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_float==0)    #float equality
solver.Add( + (1)*ConstantValue__60_CAST_mul21_double + (-1)*_Z4CNDFf_3_14_InputX_addr_0_CAST_mul21_double==0)    #double equality
solver.Add( + (1)*ConstantValue__60_CAST_mul21_fixp + (-1)*_Z4CNDFf_3_14_mul21_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__60_CAST_mul21_float + (-1)*_Z4CNDFf_3_14_mul21_float==0)    #float equality
solver.Add( + (1)*ConstantValue__60_CAST_mul21_double + (-1)*_Z4CNDFf_3_14_mul21_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul21_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul21_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul21_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_enob + (-1)*_Z4CNDFf_3_14_InputX_addr_0_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_1<=2)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_enob + (-1)*ConstantValue__58_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul21_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for double 1.000000e+00
ConstantValue__61_fixbits = solver.IntVar(0, 31, 'ConstantValue__61_fixbits')
ConstantValue__61_fixp = solver.IntVar(0, 1, 'ConstantValue__61_fixp')
ConstantValue__61_float = solver.IntVar(0, 1, 'ConstantValue__61_float')
ConstantValue__61_double = solver.IntVar(0, 1, 'ConstantValue__61_double')
ConstantValue__61_enob = solver.IntVar(-10000, 10000, 'ConstantValue__61_enob')
solver.Add( + (1)*ConstantValue__61_enob + (-1)*ConstantValue__61_fixbits + (10000)*ConstantValue__61_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__61_enob + (10000)*ConstantValue__61_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__61_enob + (10000)*ConstantValue__61_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__61_fixbits + (-10000)*ConstantValue__61_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__61_fixp + (1)*ConstantValue__61_float + (1)*ConstantValue__61_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__61_fixbits + (-10000)*ConstantValue__61_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__62_fixbits = solver.IntVar(0, 31, 'ConstantValue__62_fixbits')
ConstantValue__62_fixp = solver.IntVar(0, 1, 'ConstantValue__62_fixp')
ConstantValue__62_float = solver.IntVar(0, 1, 'ConstantValue__62_float')
ConstantValue__62_double = solver.IntVar(0, 1, 'ConstantValue__62_double')
ConstantValue__62_enob = solver.IntVar(-10000, 10000, 'ConstantValue__62_enob')
solver.Add( + (1)*ConstantValue__62_enob + (-1)*ConstantValue__62_fixbits + (10000)*ConstantValue__62_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__62_enob + (10000)*ConstantValue__62_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__62_enob + (10000)*ConstantValue__62_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__62_fixbits + (-10000)*ConstantValue__62_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__62_fixp + (1)*ConstantValue__62_float + (1)*ConstantValue__62_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__62_fixbits + (-10000)*ConstantValue__62_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__63_fixbits = solver.IntVar(0, 31, 'ConstantValue__63_fixbits')
ConstantValue__63_fixp = solver.IntVar(0, 1, 'ConstantValue__63_fixp')
ConstantValue__63_float = solver.IntVar(0, 1, 'ConstantValue__63_float')
ConstantValue__63_double = solver.IntVar(0, 1, 'ConstantValue__63_double')
ConstantValue__63_enob = solver.IntVar(-10000, 10000, 'ConstantValue__63_enob')
solver.Add( + (1)*ConstantValue__63_enob + (-1)*ConstantValue__63_fixbits + (10000)*ConstantValue__63_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__63_enob + (10000)*ConstantValue__63_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__63_enob + (10000)*ConstantValue__63_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__63_fixbits + (-10000)*ConstantValue__63_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__63_fixp + (1)*ConstantValue__63_float + (1)*ConstantValue__63_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__63_fixbits + (-10000)*ConstantValue__63_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add = fadd double 1.000000e+00, %conv23, !taffo.info !68, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__63_CAST_add_fixbits = solver.IntVar(0, 31, 'ConstantValue__63_CAST_add_fixbits')
ConstantValue__63_CAST_add_fixp = solver.IntVar(0, 1, 'ConstantValue__63_CAST_add_fixp')
ConstantValue__63_CAST_add_float = solver.IntVar(0, 1, 'ConstantValue__63_CAST_add_float')
ConstantValue__63_CAST_add_double = solver.IntVar(0, 1, 'ConstantValue__63_CAST_add_double')
solver.Add( + (1)*ConstantValue__63_CAST_add_fixp + (1)*ConstantValue__63_CAST_add_float + (1)*ConstantValue__63_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__63_CAST_add_fixbits + (-10000)*ConstantValue__63_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C1_ConstantValue__63_CAST_add')
C2_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C2_ConstantValue__63_CAST_add')
solver.Add( + (1)*ConstantValue__63_fixbits + (-1)*ConstantValue__63_CAST_add_fixbits + (-10000)*C1_ConstantValue__63_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__63_fixbits + (1)*ConstantValue__63_CAST_add_fixbits + (-10000)*C2_ConstantValue__63_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__63_CAST_add
castCostObj +=  + (1.13006)*C2_ConstantValue__63_CAST_add
C3_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C3_ConstantValue__63_CAST_add')
C4_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C4_ConstantValue__63_CAST_add')
C5_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C5_ConstantValue__63_CAST_add')
C6_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C6_ConstantValue__63_CAST_add')
C7_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C7_ConstantValue__63_CAST_add')
C8_ConstantValue__63_CAST_add = solver.IntVar(0, 1, 'C8_ConstantValue__63_CAST_add')
solver.Add( + (1)*ConstantValue__63_fixp + (1)*ConstantValue__63_CAST_add_float + (-1)*C3_ConstantValue__63_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__63_CAST_add
solver.Add( + (1)*ConstantValue__63_float + (1)*ConstantValue__63_CAST_add_fixp + (-1)*C4_ConstantValue__63_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__63_CAST_add
solver.Add( + (1)*ConstantValue__63_fixp + (1)*ConstantValue__63_CAST_add_double + (-1)*C5_ConstantValue__63_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__63_CAST_add
solver.Add( + (1)*ConstantValue__63_double + (1)*ConstantValue__63_CAST_add_fixp + (-1)*C6_ConstantValue__63_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__63_CAST_add
solver.Add( + (1)*ConstantValue__63_float + (1)*ConstantValue__63_CAST_add_double + (-1)*C7_ConstantValue__63_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__63_CAST_add
solver.Add( + (1)*ConstantValue__63_double + (1)*ConstantValue__63_CAST_add_float + (-1)*C8_ConstantValue__63_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__63_CAST_add



#Constraint for cast for   %add = fadd double 1.000000e+00, %conv23, !taffo.info !68, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_mul21_CAST_add_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_3_14_mul21_CAST_add_fixbits')
_Z4CNDFf_3_14_mul21_CAST_add_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul21_CAST_add_fixp')
_Z4CNDFf_3_14_mul21_CAST_add_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul21_CAST_add_float')
_Z4CNDFf_3_14_mul21_CAST_add_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul21_CAST_add_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_CAST_add_fixp + (1)*_Z4CNDFf_3_14_mul21_CAST_add_float + (1)*_Z4CNDFf_3_14_mul21_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_CAST_add_fixbits + (-10000)*_Z4CNDFf_3_14_mul21_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul21_CAST_add')
C2__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul21_CAST_add')
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_fixbits + (-1)*_Z4CNDFf_3_14_mul21_CAST_add_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul21_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul21_fixbits + (1)*_Z4CNDFf_3_14_mul21_CAST_add_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul21_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul21_CAST_add
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul21_CAST_add
C3__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul21_CAST_add')
C4__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul21_CAST_add')
C5__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul21_CAST_add')
C6__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul21_CAST_add')
C7__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul21_CAST_add')
C8__Z4CNDFf_3_14_mul21_CAST_add = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul21_CAST_add')
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_fixp + (1)*_Z4CNDFf_3_14_mul21_CAST_add_float + (-1)*C3__Z4CNDFf_3_14_mul21_CAST_add<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_float + (1)*_Z4CNDFf_3_14_mul21_CAST_add_fixp + (-1)*C4__Z4CNDFf_3_14_mul21_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_fixp + (1)*_Z4CNDFf_3_14_mul21_CAST_add_double + (-1)*C5__Z4CNDFf_3_14_mul21_CAST_add<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_double + (1)*_Z4CNDFf_3_14_mul21_CAST_add_fixp + (-1)*C6__Z4CNDFf_3_14_mul21_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_float + (1)*_Z4CNDFf_3_14_mul21_CAST_add_double + (-1)*C7__Z4CNDFf_3_14_mul21_CAST_add<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul21_CAST_add
solver.Add( + (1)*_Z4CNDFf_3_14_mul21_double + (1)*_Z4CNDFf_3_14_mul21_CAST_add_float + (-1)*C8__Z4CNDFf_3_14_mul21_CAST_add<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul21_CAST_add



#Stuff for   %add = fadd double 1.000000e+00, %conv23, !taffo.info !68, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_add_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_3_14_add_fixbits')
_Z4CNDFf_3_14_add_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add_fixp')
_Z4CNDFf_3_14_add_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add_float')
_Z4CNDFf_3_14_add_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add_double')
_Z4CNDFf_3_14_add_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_add_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_add_enob + (-1)*_Z4CNDFf_3_14_add_fixbits + (10000)*_Z4CNDFf_3_14_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_add_enob + (10000)*_Z4CNDFf_3_14_add_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_add_enob + (10000)*_Z4CNDFf_3_14_add_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_add_fixbits + (-10000)*_Z4CNDFf_3_14_add_fixp>=-9975)    #Limit the lower number of frac bits26
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_add_enob
solver.Add( + (1)*_Z4CNDFf_3_14_add_fixp + (1)*_Z4CNDFf_3_14_add_float + (1)*_Z4CNDFf_3_14_add_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_add_fixbits + (-10000)*_Z4CNDFf_3_14_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__63_CAST_add_fixp + (-1)*_Z4CNDFf_3_14_mul21_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__63_CAST_add_float + (-1)*_Z4CNDFf_3_14_mul21_CAST_add_float==0)    #float equality
solver.Add( + (1)*ConstantValue__63_CAST_add_double + (-1)*_Z4CNDFf_3_14_mul21_CAST_add_double==0)    #double equality
solver.Add( + (1)*ConstantValue__63_CAST_add_fixbits + (-1)*_Z4CNDFf_3_14_mul21_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__63_CAST_add_fixp + (-1)*_Z4CNDFf_3_14_add_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__63_CAST_add_float + (-1)*_Z4CNDFf_3_14_add_float==0)    #float equality
solver.Add( + (1)*ConstantValue__63_CAST_add_double + (-1)*_Z4CNDFf_3_14_add_double==0)    #double equality
solver.Add( + (1)*ConstantValue__63_CAST_add_fixbits + (-1)*_Z4CNDFf_3_14_add_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_add_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_add_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_add_double
solver.Add( + (1)*_Z4CNDFf_3_14_add_enob + (-1)*ConstantValue__61_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_3_14_add_enob + (-1)*_Z4CNDFf_3_14_mul21_enob<=0)    #Enob propagation in sum second addend



#Stuff for double 1.000000e+00
ConstantValue__64_fixbits = solver.IntVar(0, 31, 'ConstantValue__64_fixbits')
ConstantValue__64_fixp = solver.IntVar(0, 1, 'ConstantValue__64_fixp')
ConstantValue__64_float = solver.IntVar(0, 1, 'ConstantValue__64_float')
ConstantValue__64_double = solver.IntVar(0, 1, 'ConstantValue__64_double')
ConstantValue__64_enob = solver.IntVar(-10000, 10000, 'ConstantValue__64_enob')
solver.Add( + (1)*ConstantValue__64_enob + (-1)*ConstantValue__64_fixbits + (10000)*ConstantValue__64_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__64_enob + (10000)*ConstantValue__64_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__64_enob + (10000)*ConstantValue__64_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__64_fixbits + (-10000)*ConstantValue__64_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__64_fixp + (1)*ConstantValue__64_float + (1)*ConstantValue__64_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__64_fixbits + (-10000)*ConstantValue__64_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__65_fixbits = solver.IntVar(0, 31, 'ConstantValue__65_fixbits')
ConstantValue__65_fixp = solver.IntVar(0, 1, 'ConstantValue__65_fixp')
ConstantValue__65_float = solver.IntVar(0, 1, 'ConstantValue__65_float')
ConstantValue__65_double = solver.IntVar(0, 1, 'ConstantValue__65_double')
ConstantValue__65_enob = solver.IntVar(-10000, 10000, 'ConstantValue__65_enob')
solver.Add( + (1)*ConstantValue__65_enob + (-1)*ConstantValue__65_fixbits + (10000)*ConstantValue__65_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__65_enob + (10000)*ConstantValue__65_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__65_enob + (10000)*ConstantValue__65_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__65_fixbits + (-10000)*ConstantValue__65_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__65_fixp + (1)*ConstantValue__65_float + (1)*ConstantValue__65_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__65_fixbits + (-10000)*ConstantValue__65_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__66_fixbits = solver.IntVar(0, 31, 'ConstantValue__66_fixbits')
ConstantValue__66_fixp = solver.IntVar(0, 1, 'ConstantValue__66_fixp')
ConstantValue__66_float = solver.IntVar(0, 1, 'ConstantValue__66_float')
ConstantValue__66_double = solver.IntVar(0, 1, 'ConstantValue__66_double')
ConstantValue__66_enob = solver.IntVar(-10000, 10000, 'ConstantValue__66_enob')
solver.Add( + (1)*ConstantValue__66_enob + (-1)*ConstantValue__66_fixbits + (10000)*ConstantValue__66_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__66_enob + (10000)*ConstantValue__66_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__66_enob + (10000)*ConstantValue__66_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__66_fixbits + (-10000)*ConstantValue__66_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__66_fixp + (1)*ConstantValue__66_float + (1)*ConstantValue__66_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__66_fixbits + (-10000)*ConstantValue__66_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double 1.000000e+00, %conv25, !taffo.info !73, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__66_CAST_div_fixbits = solver.IntVar(0, 31, 'ConstantValue__66_CAST_div_fixbits')
ConstantValue__66_CAST_div_fixp = solver.IntVar(0, 1, 'ConstantValue__66_CAST_div_fixp')
ConstantValue__66_CAST_div_float = solver.IntVar(0, 1, 'ConstantValue__66_CAST_div_float')
ConstantValue__66_CAST_div_double = solver.IntVar(0, 1, 'ConstantValue__66_CAST_div_double')
solver.Add( + (1)*ConstantValue__66_CAST_div_fixp + (1)*ConstantValue__66_CAST_div_float + (1)*ConstantValue__66_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__66_CAST_div_fixbits + (-10000)*ConstantValue__66_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C1_ConstantValue__66_CAST_div')
C2_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C2_ConstantValue__66_CAST_div')
solver.Add( + (1)*ConstantValue__66_fixbits + (-1)*ConstantValue__66_CAST_div_fixbits + (-10000)*C1_ConstantValue__66_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__66_fixbits + (1)*ConstantValue__66_CAST_div_fixbits + (-10000)*C2_ConstantValue__66_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__66_CAST_div
castCostObj +=  + (1.13006)*C2_ConstantValue__66_CAST_div
C3_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C3_ConstantValue__66_CAST_div')
C4_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C4_ConstantValue__66_CAST_div')
C5_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C5_ConstantValue__66_CAST_div')
C6_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C6_ConstantValue__66_CAST_div')
C7_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C7_ConstantValue__66_CAST_div')
C8_ConstantValue__66_CAST_div = solver.IntVar(0, 1, 'C8_ConstantValue__66_CAST_div')
solver.Add( + (1)*ConstantValue__66_fixp + (1)*ConstantValue__66_CAST_div_float + (-1)*C3_ConstantValue__66_CAST_div<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__66_CAST_div
solver.Add( + (1)*ConstantValue__66_float + (1)*ConstantValue__66_CAST_div_fixp + (-1)*C4_ConstantValue__66_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__66_CAST_div
solver.Add( + (1)*ConstantValue__66_fixp + (1)*ConstantValue__66_CAST_div_double + (-1)*C5_ConstantValue__66_CAST_div<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__66_CAST_div
solver.Add( + (1)*ConstantValue__66_double + (1)*ConstantValue__66_CAST_div_fixp + (-1)*C6_ConstantValue__66_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__66_CAST_div
solver.Add( + (1)*ConstantValue__66_float + (1)*ConstantValue__66_CAST_div_double + (-1)*C7_ConstantValue__66_CAST_div<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__66_CAST_div
solver.Add( + (1)*ConstantValue__66_double + (1)*ConstantValue__66_CAST_div_float + (-1)*C8_ConstantValue__66_CAST_div<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__66_CAST_div



#Constraint for cast for   %div = fdiv double 1.000000e+00, %conv25, !taffo.info !73, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_add_CAST_div_fixbits = solver.IntVar(0, 26, '_Z4CNDFf_3_14_add_CAST_div_fixbits')
_Z4CNDFf_3_14_add_CAST_div_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add_CAST_div_fixp')
_Z4CNDFf_3_14_add_CAST_div_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add_CAST_div_float')
_Z4CNDFf_3_14_add_CAST_div_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add_CAST_div_double')
solver.Add( + (1)*_Z4CNDFf_3_14_add_CAST_div_fixp + (1)*_Z4CNDFf_3_14_add_CAST_div_float + (1)*_Z4CNDFf_3_14_add_CAST_div_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_add_CAST_div_fixbits + (-10000)*_Z4CNDFf_3_14_add_CAST_div_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_add_CAST_div')
C2__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_add_CAST_div')
solver.Add( + (1)*_Z4CNDFf_3_14_add_fixbits + (-1)*_Z4CNDFf_3_14_add_CAST_div_fixbits + (-10000)*C1__Z4CNDFf_3_14_add_CAST_div<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_add_fixbits + (1)*_Z4CNDFf_3_14_add_CAST_div_fixbits + (-10000)*C2__Z4CNDFf_3_14_add_CAST_div<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_add_CAST_div
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_add_CAST_div
C3__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_add_CAST_div')
C4__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_add_CAST_div')
C5__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_add_CAST_div')
C6__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_add_CAST_div')
C7__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_add_CAST_div')
C8__Z4CNDFf_3_14_add_CAST_div = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_add_CAST_div')
solver.Add( + (1)*_Z4CNDFf_3_14_add_fixp + (1)*_Z4CNDFf_3_14_add_CAST_div_float + (-1)*C3__Z4CNDFf_3_14_add_CAST_div<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_3_14_add_float + (1)*_Z4CNDFf_3_14_add_CAST_div_fixp + (-1)*C4__Z4CNDFf_3_14_add_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_3_14_add_fixp + (1)*_Z4CNDFf_3_14_add_CAST_div_double + (-1)*C5__Z4CNDFf_3_14_add_CAST_div<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_3_14_add_double + (1)*_Z4CNDFf_3_14_add_CAST_div_fixp + (-1)*C6__Z4CNDFf_3_14_add_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_3_14_add_float + (1)*_Z4CNDFf_3_14_add_CAST_div_double + (-1)*C7__Z4CNDFf_3_14_add_CAST_div<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_add_CAST_div
solver.Add( + (1)*_Z4CNDFf_3_14_add_double + (1)*_Z4CNDFf_3_14_add_CAST_div_float + (-1)*C8__Z4CNDFf_3_14_add_CAST_div<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_add_CAST_div



#Stuff for   %div = fdiv double 1.000000e+00, %conv25, !taffo.info !73, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_div_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_div_fixbits')
_Z4CNDFf_3_14_div_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_fixp')
_Z4CNDFf_3_14_div_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_float')
_Z4CNDFf_3_14_div_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_double')
_Z4CNDFf_3_14_div_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_div_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_div_enob + (-1)*_Z4CNDFf_3_14_div_fixbits + (10000)*_Z4CNDFf_3_14_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_div_enob + (10000)*_Z4CNDFf_3_14_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_div_enob + (10000)*_Z4CNDFf_3_14_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-10000)*_Z4CNDFf_3_14_div_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_div_enob
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-10000)*_Z4CNDFf_3_14_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__66_CAST_div_fixp + (-1)*_Z4CNDFf_3_14_add_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__66_CAST_div_float + (-1)*_Z4CNDFf_3_14_add_CAST_div_float==0)    #float equality
solver.Add( + (1)*ConstantValue__66_CAST_div_double + (-1)*_Z4CNDFf_3_14_add_CAST_div_double==0)    #double equality
solver.Add( + (1)*ConstantValue__66_CAST_div_fixp + (-1)*_Z4CNDFf_3_14_div_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__66_CAST_div_float + (-1)*_Z4CNDFf_3_14_div_float==0)    #float equality
solver.Add( + (1)*ConstantValue__66_CAST_div_double + (-1)*_Z4CNDFf_3_14_div_double==0)    #double equality
mathCostObj +=  + (3.45438)*_Z4CNDFf_3_14_div_fixp
mathCostObj +=  + (4.13283)*_Z4CNDFf_3_14_div_float
mathCostObj +=  + (5.68177)*_Z4CNDFf_3_14_div_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_div_enob + (-1)*_Z4CNDFf_3_14_add_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_1<=10)    #Enob: propagation in division 1
solver.Add( + (1)*_Z4CNDFf_3_14_div_enob + (-1)*ConstantValue__64_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_div_enob_2<=1034)    #Enob: propagation in division 2



#Constraint for cast for   %mul27 = fmul float %conv26, %conv26, !taffo.info !77, !taffo.initweight !23
_Z4CNDFf_3_14_div_CAST_mul27_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_div_CAST_mul27_fixbits')
_Z4CNDFf_3_14_div_CAST_mul27_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul27_fixp')
_Z4CNDFf_3_14_div_CAST_mul27_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul27_float')
_Z4CNDFf_3_14_div_CAST_mul27_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul27_double')
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul27_float + (1)*_Z4CNDFf_3_14_div_CAST_mul27_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_fixbits + (-10000)*_Z4CNDFf_3_14_div_CAST_mul27_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_div_CAST_mul27')
C2__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_div_CAST_mul27')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-1)*_Z4CNDFf_3_14_div_CAST_mul27_fixbits + (-10000)*C1__Z4CNDFf_3_14_div_CAST_mul27<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_div_fixbits + (1)*_Z4CNDFf_3_14_div_CAST_mul27_fixbits + (-10000)*C2__Z4CNDFf_3_14_div_CAST_mul27<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_div_CAST_mul27
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_div_CAST_mul27
C3__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_div_CAST_mul27')
C4__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_div_CAST_mul27')
C5__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_div_CAST_mul27')
C6__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_div_CAST_mul27')
C7__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_div_CAST_mul27')
C8__Z4CNDFf_3_14_div_CAST_mul27 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_div_CAST_mul27')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul27_float + (-1)*C3__Z4CNDFf_3_14_div_CAST_mul27<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul27_fixp + (-1)*C4__Z4CNDFf_3_14_div_CAST_mul27<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul27_double + (-1)*C5__Z4CNDFf_3_14_div_CAST_mul27<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul27_fixp + (-1)*C6__Z4CNDFf_3_14_div_CAST_mul27<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul27_double + (-1)*C7__Z4CNDFf_3_14_div_CAST_mul27<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_div_CAST_mul27
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul27_float + (-1)*C8__Z4CNDFf_3_14_div_CAST_mul27<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_div_CAST_mul27



#Constraint for cast for   %mul27 = fmul float %conv26, %conv26, !taffo.info !77, !taffo.initweight !23
_Z4CNDFf_3_14_div_CAST_mul27_0_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_div_CAST_mul27_0_fixbits')
_Z4CNDFf_3_14_div_CAST_mul27_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul27_0_fixp')
_Z4CNDFf_3_14_div_CAST_mul27_0_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul27_0_float')
_Z4CNDFf_3_14_div_CAST_mul27_0_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul27_0_double')
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_float + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixbits + (-10000)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_div_CAST_mul27_0')
C2__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_div_CAST_mul27_0')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-1)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixbits + (-10000)*C1__Z4CNDFf_3_14_div_CAST_mul27_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_div_fixbits + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixbits + (-10000)*C2__Z4CNDFf_3_14_div_CAST_mul27_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_div_CAST_mul27_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_div_CAST_mul27_0
C3__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_div_CAST_mul27_0')
C4__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_div_CAST_mul27_0')
C5__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_div_CAST_mul27_0')
C6__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_div_CAST_mul27_0')
C7__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_div_CAST_mul27_0')
C8__Z4CNDFf_3_14_div_CAST_mul27_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_div_CAST_mul27_0')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_float + (-1)*C3__Z4CNDFf_3_14_div_CAST_mul27_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixp + (-1)*C4__Z4CNDFf_3_14_div_CAST_mul27_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_double + (-1)*C5__Z4CNDFf_3_14_div_CAST_mul27_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixp + (-1)*C6__Z4CNDFf_3_14_div_CAST_mul27_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_double + (-1)*C7__Z4CNDFf_3_14_div_CAST_mul27_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_div_CAST_mul27_0
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul27_0_float + (-1)*C8__Z4CNDFf_3_14_div_CAST_mul27_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_div_CAST_mul27_0



#Stuff for   %mul27 = fmul float %conv26, %conv26, !taffo.info !77, !taffo.initweight !23
_Z4CNDFf_3_14_mul27_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_3_14_mul27_fixbits')
_Z4CNDFf_3_14_mul27_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_fixp')
_Z4CNDFf_3_14_mul27_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_float')
_Z4CNDFf_3_14_mul27_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_double')
_Z4CNDFf_3_14_mul27_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul27_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_enob + (-1)*_Z4CNDFf_3_14_mul27_fixbits + (10000)*_Z4CNDFf_3_14_mul27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_enob + (10000)*_Z4CNDFf_3_14_mul27_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_enob + (10000)*_Z4CNDFf_3_14_mul27_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixbits + (-10000)*_Z4CNDFf_3_14_mul27_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul27_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixp + (1)*_Z4CNDFf_3_14_mul27_float + (1)*_Z4CNDFf_3_14_mul27_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixbits + (-10000)*_Z4CNDFf_3_14_mul27_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_fixp + (-1)*_Z4CNDFf_3_14_div_CAST_mul27_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_float + (-1)*_Z4CNDFf_3_14_div_CAST_mul27_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_double + (-1)*_Z4CNDFf_3_14_div_CAST_mul27_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_fixp + (-1)*_Z4CNDFf_3_14_mul27_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_float + (-1)*_Z4CNDFf_3_14_mul27_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul27_double + (-1)*_Z4CNDFf_3_14_mul27_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul27_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul27_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul27_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_enob + (-1)*_Z4CNDFf_3_14_div_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_enob + (-1)*_Z4CNDFf_3_14_div_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul27_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul28 = fmul float %mul27, %conv26, !taffo.info !79, !taffo.initweight !23
_Z4CNDFf_3_14_mul27_CAST_mul28_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_3_14_mul27_CAST_mul28_fixbits')
_Z4CNDFf_3_14_mul27_CAST_mul28_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_CAST_mul28_fixp')
_Z4CNDFf_3_14_mul27_CAST_mul28_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_CAST_mul28_float')
_Z4CNDFf_3_14_mul27_CAST_mul28_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_CAST_mul28_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixp + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_float + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixbits + (-10000)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul27_CAST_mul28')
C2__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul27_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixbits + (-1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul27_CAST_mul28<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul27_fixbits + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul27_CAST_mul28<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul27_CAST_mul28
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul27_CAST_mul28
C3__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul27_CAST_mul28')
C4__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul27_CAST_mul28')
C5__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul27_CAST_mul28')
C6__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul27_CAST_mul28')
C7__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul27_CAST_mul28')
C8__Z4CNDFf_3_14_mul27_CAST_mul28 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul27_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixp + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_float + (-1)*C3__Z4CNDFf_3_14_mul27_CAST_mul28<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_float + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixp + (-1)*C4__Z4CNDFf_3_14_mul27_CAST_mul28<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixp + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_double + (-1)*C5__Z4CNDFf_3_14_mul27_CAST_mul28<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_double + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixp + (-1)*C6__Z4CNDFf_3_14_mul27_CAST_mul28<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_float + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_double + (-1)*C7__Z4CNDFf_3_14_mul27_CAST_mul28<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul27_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_double + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_float + (-1)*C8__Z4CNDFf_3_14_mul27_CAST_mul28<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul27_CAST_mul28



#Constraint for cast for   %mul28 = fmul float %mul27, %conv26, !taffo.info !79, !taffo.initweight !23
_Z4CNDFf_3_14_div_CAST_mul28_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_div_CAST_mul28_fixbits')
_Z4CNDFf_3_14_div_CAST_mul28_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul28_fixp')
_Z4CNDFf_3_14_div_CAST_mul28_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul28_float')
_Z4CNDFf_3_14_div_CAST_mul28_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul28_double')
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul28_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul28_float + (1)*_Z4CNDFf_3_14_div_CAST_mul28_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul28_fixbits + (-10000)*_Z4CNDFf_3_14_div_CAST_mul28_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_div_CAST_mul28')
C2__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_div_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-1)*_Z4CNDFf_3_14_div_CAST_mul28_fixbits + (-10000)*C1__Z4CNDFf_3_14_div_CAST_mul28<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_div_fixbits + (1)*_Z4CNDFf_3_14_div_CAST_mul28_fixbits + (-10000)*C2__Z4CNDFf_3_14_div_CAST_mul28<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_div_CAST_mul28
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_div_CAST_mul28
C3__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_div_CAST_mul28')
C4__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_div_CAST_mul28')
C5__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_div_CAST_mul28')
C6__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_div_CAST_mul28')
C7__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_div_CAST_mul28')
C8__Z4CNDFf_3_14_div_CAST_mul28 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_div_CAST_mul28')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul28_float + (-1)*C3__Z4CNDFf_3_14_div_CAST_mul28<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul28_fixp + (-1)*C4__Z4CNDFf_3_14_div_CAST_mul28<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul28_double + (-1)*C5__Z4CNDFf_3_14_div_CAST_mul28<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul28_fixp + (-1)*C6__Z4CNDFf_3_14_div_CAST_mul28<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul28_double + (-1)*C7__Z4CNDFf_3_14_div_CAST_mul28<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_div_CAST_mul28
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul28_float + (-1)*C8__Z4CNDFf_3_14_div_CAST_mul28<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_div_CAST_mul28



#Stuff for   %mul28 = fmul float %mul27, %conv26, !taffo.info !79, !taffo.initweight !23
_Z4CNDFf_3_14_mul28_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul28_fixbits')
_Z4CNDFf_3_14_mul28_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_fixp')
_Z4CNDFf_3_14_mul28_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_float')
_Z4CNDFf_3_14_mul28_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_double')
_Z4CNDFf_3_14_mul28_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul28_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_enob + (-1)*_Z4CNDFf_3_14_mul28_fixbits + (10000)*_Z4CNDFf_3_14_mul28_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_enob + (10000)*_Z4CNDFf_3_14_mul28_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_enob + (10000)*_Z4CNDFf_3_14_mul28_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixbits + (-10000)*_Z4CNDFf_3_14_mul28_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul28_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixp + (1)*_Z4CNDFf_3_14_mul28_float + (1)*_Z4CNDFf_3_14_mul28_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixbits + (-10000)*_Z4CNDFf_3_14_mul28_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixp + (-1)*_Z4CNDFf_3_14_div_CAST_mul28_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_float + (-1)*_Z4CNDFf_3_14_div_CAST_mul28_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_double + (-1)*_Z4CNDFf_3_14_div_CAST_mul28_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_fixp + (-1)*_Z4CNDFf_3_14_mul28_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_float + (-1)*_Z4CNDFf_3_14_mul28_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul28_double + (-1)*_Z4CNDFf_3_14_mul28_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul28_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul28_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul28_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_enob + (-1)*_Z4CNDFf_3_14_div_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_enob + (-1)*_Z4CNDFf_3_14_mul27_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul28_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul29 = fmul float %mul28, %conv26, !taffo.info !81, !taffo.initweight !23
_Z4CNDFf_3_14_mul28_CAST_mul29_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul28_CAST_mul29_fixbits')
_Z4CNDFf_3_14_mul28_CAST_mul29_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_CAST_mul29_fixp')
_Z4CNDFf_3_14_mul28_CAST_mul29_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_CAST_mul29_float')
_Z4CNDFf_3_14_mul28_CAST_mul29_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_CAST_mul29_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixp + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_float + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixbits + (-10000)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul28_CAST_mul29')
C2__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul28_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixbits + (-1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul28_CAST_mul29<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul28_fixbits + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul28_CAST_mul29<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul28_CAST_mul29
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul28_CAST_mul29
C3__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul28_CAST_mul29')
C4__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul28_CAST_mul29')
C5__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul28_CAST_mul29')
C6__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul28_CAST_mul29')
C7__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul28_CAST_mul29')
C8__Z4CNDFf_3_14_mul28_CAST_mul29 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul28_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixp + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_float + (-1)*C3__Z4CNDFf_3_14_mul28_CAST_mul29<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_float + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixp + (-1)*C4__Z4CNDFf_3_14_mul28_CAST_mul29<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixp + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_double + (-1)*C5__Z4CNDFf_3_14_mul28_CAST_mul29<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_double + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixp + (-1)*C6__Z4CNDFf_3_14_mul28_CAST_mul29<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_float + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_double + (-1)*C7__Z4CNDFf_3_14_mul28_CAST_mul29<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul28_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_double + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_float + (-1)*C8__Z4CNDFf_3_14_mul28_CAST_mul29<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul28_CAST_mul29



#Constraint for cast for   %mul29 = fmul float %mul28, %conv26, !taffo.info !81, !taffo.initweight !23
_Z4CNDFf_3_14_div_CAST_mul29_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_div_CAST_mul29_fixbits')
_Z4CNDFf_3_14_div_CAST_mul29_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul29_fixp')
_Z4CNDFf_3_14_div_CAST_mul29_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul29_float')
_Z4CNDFf_3_14_div_CAST_mul29_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul29_double')
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul29_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul29_float + (1)*_Z4CNDFf_3_14_div_CAST_mul29_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul29_fixbits + (-10000)*_Z4CNDFf_3_14_div_CAST_mul29_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_div_CAST_mul29')
C2__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_div_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-1)*_Z4CNDFf_3_14_div_CAST_mul29_fixbits + (-10000)*C1__Z4CNDFf_3_14_div_CAST_mul29<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_div_fixbits + (1)*_Z4CNDFf_3_14_div_CAST_mul29_fixbits + (-10000)*C2__Z4CNDFf_3_14_div_CAST_mul29<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_div_CAST_mul29
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_div_CAST_mul29
C3__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_div_CAST_mul29')
C4__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_div_CAST_mul29')
C5__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_div_CAST_mul29')
C6__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_div_CAST_mul29')
C7__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_div_CAST_mul29')
C8__Z4CNDFf_3_14_div_CAST_mul29 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_div_CAST_mul29')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul29_float + (-1)*C3__Z4CNDFf_3_14_div_CAST_mul29<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul29_fixp + (-1)*C4__Z4CNDFf_3_14_div_CAST_mul29<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul29_double + (-1)*C5__Z4CNDFf_3_14_div_CAST_mul29<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul29_fixp + (-1)*C6__Z4CNDFf_3_14_div_CAST_mul29<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul29_double + (-1)*C7__Z4CNDFf_3_14_div_CAST_mul29<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_div_CAST_mul29
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul29_float + (-1)*C8__Z4CNDFf_3_14_div_CAST_mul29<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_div_CAST_mul29



#Stuff for   %mul29 = fmul float %mul28, %conv26, !taffo.info !81, !taffo.initweight !23
_Z4CNDFf_3_14_mul29_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul29_fixbits')
_Z4CNDFf_3_14_mul29_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_fixp')
_Z4CNDFf_3_14_mul29_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_float')
_Z4CNDFf_3_14_mul29_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_double')
_Z4CNDFf_3_14_mul29_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul29_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_enob + (-1)*_Z4CNDFf_3_14_mul29_fixbits + (10000)*_Z4CNDFf_3_14_mul29_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_enob + (10000)*_Z4CNDFf_3_14_mul29_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_enob + (10000)*_Z4CNDFf_3_14_mul29_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixbits + (-10000)*_Z4CNDFf_3_14_mul29_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul29_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixp + (1)*_Z4CNDFf_3_14_mul29_float + (1)*_Z4CNDFf_3_14_mul29_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixbits + (-10000)*_Z4CNDFf_3_14_mul29_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixp + (-1)*_Z4CNDFf_3_14_div_CAST_mul29_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_float + (-1)*_Z4CNDFf_3_14_div_CAST_mul29_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_double + (-1)*_Z4CNDFf_3_14_div_CAST_mul29_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_fixp + (-1)*_Z4CNDFf_3_14_mul29_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_float + (-1)*_Z4CNDFf_3_14_mul29_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul29_double + (-1)*_Z4CNDFf_3_14_mul29_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul29_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul29_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul29_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_enob + (-1)*_Z4CNDFf_3_14_div_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_enob + (-1)*_Z4CNDFf_3_14_mul28_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul29_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul30 = fmul float %mul29, %conv26, !taffo.info !83, !taffo.initweight !23
_Z4CNDFf_3_14_mul29_CAST_mul30_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul29_CAST_mul30_fixbits')
_Z4CNDFf_3_14_mul29_CAST_mul30_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_CAST_mul30_fixp')
_Z4CNDFf_3_14_mul29_CAST_mul30_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_CAST_mul30_float')
_Z4CNDFf_3_14_mul29_CAST_mul30_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_CAST_mul30_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixp + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_float + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixbits + (-10000)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul29_CAST_mul30')
C2__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul29_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixbits + (-1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul29_CAST_mul30<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul29_fixbits + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul29_CAST_mul30<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul29_CAST_mul30
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul29_CAST_mul30
C3__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul29_CAST_mul30')
C4__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul29_CAST_mul30')
C5__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul29_CAST_mul30')
C6__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul29_CAST_mul30')
C7__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul29_CAST_mul30')
C8__Z4CNDFf_3_14_mul29_CAST_mul30 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul29_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixp + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_float + (-1)*C3__Z4CNDFf_3_14_mul29_CAST_mul30<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_float + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixp + (-1)*C4__Z4CNDFf_3_14_mul29_CAST_mul30<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixp + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_double + (-1)*C5__Z4CNDFf_3_14_mul29_CAST_mul30<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_double + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixp + (-1)*C6__Z4CNDFf_3_14_mul29_CAST_mul30<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_float + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_double + (-1)*C7__Z4CNDFf_3_14_mul29_CAST_mul30<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul29_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_double + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_float + (-1)*C8__Z4CNDFf_3_14_mul29_CAST_mul30<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul29_CAST_mul30



#Constraint for cast for   %mul30 = fmul float %mul29, %conv26, !taffo.info !83, !taffo.initweight !23
_Z4CNDFf_3_14_div_CAST_mul30_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_div_CAST_mul30_fixbits')
_Z4CNDFf_3_14_div_CAST_mul30_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul30_fixp')
_Z4CNDFf_3_14_div_CAST_mul30_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul30_float')
_Z4CNDFf_3_14_div_CAST_mul30_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul30_double')
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul30_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul30_float + (1)*_Z4CNDFf_3_14_div_CAST_mul30_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul30_fixbits + (-10000)*_Z4CNDFf_3_14_div_CAST_mul30_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_div_CAST_mul30')
C2__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_div_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-1)*_Z4CNDFf_3_14_div_CAST_mul30_fixbits + (-10000)*C1__Z4CNDFf_3_14_div_CAST_mul30<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_div_fixbits + (1)*_Z4CNDFf_3_14_div_CAST_mul30_fixbits + (-10000)*C2__Z4CNDFf_3_14_div_CAST_mul30<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_div_CAST_mul30
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_div_CAST_mul30
C3__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_div_CAST_mul30')
C4__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_div_CAST_mul30')
C5__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_div_CAST_mul30')
C6__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_div_CAST_mul30')
C7__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_div_CAST_mul30')
C8__Z4CNDFf_3_14_div_CAST_mul30 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_div_CAST_mul30')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul30_float + (-1)*C3__Z4CNDFf_3_14_div_CAST_mul30<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul30_fixp + (-1)*C4__Z4CNDFf_3_14_div_CAST_mul30<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul30_double + (-1)*C5__Z4CNDFf_3_14_div_CAST_mul30<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul30_fixp + (-1)*C6__Z4CNDFf_3_14_div_CAST_mul30<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul30_double + (-1)*C7__Z4CNDFf_3_14_div_CAST_mul30<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_div_CAST_mul30
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul30_float + (-1)*C8__Z4CNDFf_3_14_div_CAST_mul30<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_div_CAST_mul30



#Stuff for   %mul30 = fmul float %mul29, %conv26, !taffo.info !83, !taffo.initweight !23
_Z4CNDFf_3_14_mul30_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul30_fixbits')
_Z4CNDFf_3_14_mul30_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul30_fixp')
_Z4CNDFf_3_14_mul30_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul30_float')
_Z4CNDFf_3_14_mul30_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul30_double')
_Z4CNDFf_3_14_mul30_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul30_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_enob + (-1)*_Z4CNDFf_3_14_mul30_fixbits + (10000)*_Z4CNDFf_3_14_mul30_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_enob + (10000)*_Z4CNDFf_3_14_mul30_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_enob + (10000)*_Z4CNDFf_3_14_mul30_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_fixbits + (-10000)*_Z4CNDFf_3_14_mul30_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul30_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_fixp + (1)*_Z4CNDFf_3_14_mul30_float + (1)*_Z4CNDFf_3_14_mul30_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_fixbits + (-10000)*_Z4CNDFf_3_14_mul30_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixp + (-1)*_Z4CNDFf_3_14_div_CAST_mul30_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_float + (-1)*_Z4CNDFf_3_14_div_CAST_mul30_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_double + (-1)*_Z4CNDFf_3_14_div_CAST_mul30_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_fixp + (-1)*_Z4CNDFf_3_14_mul30_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_float + (-1)*_Z4CNDFf_3_14_mul30_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul30_double + (-1)*_Z4CNDFf_3_14_mul30_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul30_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul30_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul30_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_enob + (-1)*_Z4CNDFf_3_14_div_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_enob + (-1)*_Z4CNDFf_3_14_mul29_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul30_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for double 0x3FD470BF3A92F8EC
ConstantValue__67_fixbits = solver.IntVar(0, 31, 'ConstantValue__67_fixbits')
ConstantValue__67_fixp = solver.IntVar(0, 1, 'ConstantValue__67_fixp')
ConstantValue__67_float = solver.IntVar(0, 1, 'ConstantValue__67_float')
ConstantValue__67_double = solver.IntVar(0, 1, 'ConstantValue__67_double')
ConstantValue__67_enob = solver.IntVar(-10000, 10000, 'ConstantValue__67_enob')
solver.Add( + (1)*ConstantValue__67_enob + (-1)*ConstantValue__67_fixbits + (10000)*ConstantValue__67_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__67_enob + (10000)*ConstantValue__67_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__67_enob + (10000)*ConstantValue__67_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__67_fixbits + (-10000)*ConstantValue__67_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__67_fixp + (1)*ConstantValue__67_float + (1)*ConstantValue__67_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__67_fixbits + (-10000)*ConstantValue__67_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FD470BF3A92F8EC
ConstantValue__68_fixbits = solver.IntVar(0, 31, 'ConstantValue__68_fixbits')
ConstantValue__68_fixp = solver.IntVar(0, 1, 'ConstantValue__68_fixp')
ConstantValue__68_float = solver.IntVar(0, 1, 'ConstantValue__68_float')
ConstantValue__68_double = solver.IntVar(0, 1, 'ConstantValue__68_double')
ConstantValue__68_enob = solver.IntVar(-10000, 10000, 'ConstantValue__68_enob')
solver.Add( + (1)*ConstantValue__68_enob + (-1)*ConstantValue__68_fixbits + (10000)*ConstantValue__68_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__68_enob + (10000)*ConstantValue__68_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__68_enob + (10000)*ConstantValue__68_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__68_fixbits + (-10000)*ConstantValue__68_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__68_fixp + (1)*ConstantValue__68_float + (1)*ConstantValue__68_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__68_fixbits + (-10000)*ConstantValue__68_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul32 = fmul double %conv31, 0x3FD470BF3A92F8EC, !taffo.info !85, !taffo.initweight !30, !taffo.constinfo !87
_Z4CNDFf_3_14_div_CAST_mul32_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_div_CAST_mul32_fixbits')
_Z4CNDFf_3_14_div_CAST_mul32_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul32_fixp')
_Z4CNDFf_3_14_div_CAST_mul32_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul32_float')
_Z4CNDFf_3_14_div_CAST_mul32_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_div_CAST_mul32_double')
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul32_float + (1)*_Z4CNDFf_3_14_div_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_fixbits + (-10000)*_Z4CNDFf_3_14_div_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_div_CAST_mul32')
C2__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_div_CAST_mul32')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixbits + (-1)*_Z4CNDFf_3_14_div_CAST_mul32_fixbits + (-10000)*C1__Z4CNDFf_3_14_div_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_div_fixbits + (1)*_Z4CNDFf_3_14_div_CAST_mul32_fixbits + (-10000)*C2__Z4CNDFf_3_14_div_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_div_CAST_mul32
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_div_CAST_mul32
C3__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_div_CAST_mul32')
C4__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_div_CAST_mul32')
C5__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_div_CAST_mul32')
C6__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_div_CAST_mul32')
C7__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_div_CAST_mul32')
C8__Z4CNDFf_3_14_div_CAST_mul32 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_div_CAST_mul32')
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul32_float + (-1)*C3__Z4CNDFf_3_14_div_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul32_fixp + (-1)*C4__Z4CNDFf_3_14_div_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_3_14_div_fixp + (1)*_Z4CNDFf_3_14_div_CAST_mul32_double + (-1)*C5__Z4CNDFf_3_14_div_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul32_fixp + (-1)*C6__Z4CNDFf_3_14_div_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_3_14_div_float + (1)*_Z4CNDFf_3_14_div_CAST_mul32_double + (-1)*C7__Z4CNDFf_3_14_div_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_div_CAST_mul32
solver.Add( + (1)*_Z4CNDFf_3_14_div_double + (1)*_Z4CNDFf_3_14_div_CAST_mul32_float + (-1)*C8__Z4CNDFf_3_14_div_CAST_mul32<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_div_CAST_mul32



#Stuff for double 0x3FD470BF3A92F8EC
ConstantValue__69_fixbits = solver.IntVar(0, 31, 'ConstantValue__69_fixbits')
ConstantValue__69_fixp = solver.IntVar(0, 1, 'ConstantValue__69_fixp')
ConstantValue__69_float = solver.IntVar(0, 1, 'ConstantValue__69_float')
ConstantValue__69_double = solver.IntVar(0, 1, 'ConstantValue__69_double')
ConstantValue__69_enob = solver.IntVar(-10000, 10000, 'ConstantValue__69_enob')
solver.Add( + (1)*ConstantValue__69_enob + (-1)*ConstantValue__69_fixbits + (10000)*ConstantValue__69_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__69_enob + (10000)*ConstantValue__69_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__69_enob + (10000)*ConstantValue__69_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__69_fixbits + (-10000)*ConstantValue__69_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__69_fixp + (1)*ConstantValue__69_float + (1)*ConstantValue__69_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__69_fixbits + (-10000)*ConstantValue__69_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul32 = fmul double %conv31, 0x3FD470BF3A92F8EC, !taffo.info !85, !taffo.initweight !30, !taffo.constinfo !87
ConstantValue__69_CAST_mul32_fixbits = solver.IntVar(0, 31, 'ConstantValue__69_CAST_mul32_fixbits')
ConstantValue__69_CAST_mul32_fixp = solver.IntVar(0, 1, 'ConstantValue__69_CAST_mul32_fixp')
ConstantValue__69_CAST_mul32_float = solver.IntVar(0, 1, 'ConstantValue__69_CAST_mul32_float')
ConstantValue__69_CAST_mul32_double = solver.IntVar(0, 1, 'ConstantValue__69_CAST_mul32_double')
solver.Add( + (1)*ConstantValue__69_CAST_mul32_fixp + (1)*ConstantValue__69_CAST_mul32_float + (1)*ConstantValue__69_CAST_mul32_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__69_CAST_mul32_fixbits + (-10000)*ConstantValue__69_CAST_mul32_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C1_ConstantValue__69_CAST_mul32')
C2_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C2_ConstantValue__69_CAST_mul32')
solver.Add( + (1)*ConstantValue__69_fixbits + (-1)*ConstantValue__69_CAST_mul32_fixbits + (-10000)*C1_ConstantValue__69_CAST_mul32<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__69_fixbits + (1)*ConstantValue__69_CAST_mul32_fixbits + (-10000)*C2_ConstantValue__69_CAST_mul32<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__69_CAST_mul32
castCostObj +=  + (1.13006)*C2_ConstantValue__69_CAST_mul32
C3_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C3_ConstantValue__69_CAST_mul32')
C4_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C4_ConstantValue__69_CAST_mul32')
C5_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C5_ConstantValue__69_CAST_mul32')
C6_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C6_ConstantValue__69_CAST_mul32')
C7_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C7_ConstantValue__69_CAST_mul32')
C8_ConstantValue__69_CAST_mul32 = solver.IntVar(0, 1, 'C8_ConstantValue__69_CAST_mul32')
solver.Add( + (1)*ConstantValue__69_fixp + (1)*ConstantValue__69_CAST_mul32_float + (-1)*C3_ConstantValue__69_CAST_mul32<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__69_CAST_mul32
solver.Add( + (1)*ConstantValue__69_float + (1)*ConstantValue__69_CAST_mul32_fixp + (-1)*C4_ConstantValue__69_CAST_mul32<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__69_CAST_mul32
solver.Add( + (1)*ConstantValue__69_fixp + (1)*ConstantValue__69_CAST_mul32_double + (-1)*C5_ConstantValue__69_CAST_mul32<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__69_CAST_mul32
solver.Add( + (1)*ConstantValue__69_double + (1)*ConstantValue__69_CAST_mul32_fixp + (-1)*C6_ConstantValue__69_CAST_mul32<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__69_CAST_mul32
solver.Add( + (1)*ConstantValue__69_float + (1)*ConstantValue__69_CAST_mul32_double + (-1)*C7_ConstantValue__69_CAST_mul32<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__69_CAST_mul32
solver.Add( + (1)*ConstantValue__69_double + (1)*ConstantValue__69_CAST_mul32_float + (-1)*C8_ConstantValue__69_CAST_mul32<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__69_CAST_mul32



#Stuff for   %mul32 = fmul double %conv31, 0x3FD470BF3A92F8EC, !taffo.info !85, !taffo.initweight !30, !taffo.constinfo !87
_Z4CNDFf_3_14_mul32_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul32_fixbits')
_Z4CNDFf_3_14_mul32_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul32_fixp')
_Z4CNDFf_3_14_mul32_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul32_float')
_Z4CNDFf_3_14_mul32_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul32_double')
_Z4CNDFf_3_14_mul32_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul32_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_enob + (-1)*_Z4CNDFf_3_14_mul32_fixbits + (10000)*_Z4CNDFf_3_14_mul32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_enob + (10000)*_Z4CNDFf_3_14_mul32_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_enob + (10000)*_Z4CNDFf_3_14_mul32_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_fixbits + (-10000)*_Z4CNDFf_3_14_mul32_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul32_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_fixp + (1)*_Z4CNDFf_3_14_mul32_float + (1)*_Z4CNDFf_3_14_mul32_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_fixbits + (-10000)*_Z4CNDFf_3_14_mul32_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_fixp + (-1)*ConstantValue__69_CAST_mul32_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_float + (-1)*ConstantValue__69_CAST_mul32_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_double + (-1)*ConstantValue__69_CAST_mul32_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_fixp + (-1)*_Z4CNDFf_3_14_mul32_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_float + (-1)*_Z4CNDFf_3_14_mul32_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_div_CAST_mul32_double + (-1)*_Z4CNDFf_3_14_mul32_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul32_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul32_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul32_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_enob + (-1)*ConstantValue__67_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_enob + (-1)*_Z4CNDFf_3_14_div_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul32_enob_2<=2)    #Enob: propagation in product 2



#Stuff for double 0xBFD6D1F0E5A8325B
ConstantValue__70_fixbits = solver.IntVar(0, 30, 'ConstantValue__70_fixbits')
ConstantValue__70_fixp = solver.IntVar(0, 1, 'ConstantValue__70_fixp')
ConstantValue__70_float = solver.IntVar(0, 1, 'ConstantValue__70_float')
ConstantValue__70_double = solver.IntVar(0, 1, 'ConstantValue__70_double')
ConstantValue__70_enob = solver.IntVar(-10000, 10000, 'ConstantValue__70_enob')
solver.Add( + (1)*ConstantValue__70_enob + (-1)*ConstantValue__70_fixbits + (10000)*ConstantValue__70_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__70_enob + (10000)*ConstantValue__70_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__70_enob + (10000)*ConstantValue__70_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__70_fixbits + (-10000)*ConstantValue__70_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__70_fixp + (1)*ConstantValue__70_float + (1)*ConstantValue__70_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__70_fixbits + (-10000)*ConstantValue__70_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0xBFD6D1F0E5A8325B
ConstantValue__71_fixbits = solver.IntVar(0, 30, 'ConstantValue__71_fixbits')
ConstantValue__71_fixp = solver.IntVar(0, 1, 'ConstantValue__71_fixp')
ConstantValue__71_float = solver.IntVar(0, 1, 'ConstantValue__71_float')
ConstantValue__71_double = solver.IntVar(0, 1, 'ConstantValue__71_double')
ConstantValue__71_enob = solver.IntVar(-10000, 10000, 'ConstantValue__71_enob')
solver.Add( + (1)*ConstantValue__71_enob + (-1)*ConstantValue__71_fixbits + (10000)*ConstantValue__71_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__71_enob + (10000)*ConstantValue__71_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__71_enob + (10000)*ConstantValue__71_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__71_fixbits + (-10000)*ConstantValue__71_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__71_fixp + (1)*ConstantValue__71_float + (1)*ConstantValue__71_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__71_fixbits + (-10000)*ConstantValue__71_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul35 = fmul double %conv34, 0xBFD6D1F0E5A8325B, !taffo.info !92, !taffo.initweight !30, !taffo.constinfo !94
_Z4CNDFf_3_14_mul27_CAST_mul35_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_3_14_mul27_CAST_mul35_fixbits')
_Z4CNDFf_3_14_mul27_CAST_mul35_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_CAST_mul35_fixp')
_Z4CNDFf_3_14_mul27_CAST_mul35_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_CAST_mul35_float')
_Z4CNDFf_3_14_mul27_CAST_mul35_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul27_CAST_mul35_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixp + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_float + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixbits + (-10000)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul27_CAST_mul35')
C2__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul27_CAST_mul35')
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixbits + (-1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul27_CAST_mul35<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul27_fixbits + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul27_CAST_mul35<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul27_CAST_mul35
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul27_CAST_mul35
C3__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul27_CAST_mul35')
C4__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul27_CAST_mul35')
C5__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul27_CAST_mul35')
C6__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul27_CAST_mul35')
C7__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul27_CAST_mul35')
C8__Z4CNDFf_3_14_mul27_CAST_mul35 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul27_CAST_mul35')
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixp + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_float + (-1)*C3__Z4CNDFf_3_14_mul27_CAST_mul35<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_float + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixp + (-1)*C4__Z4CNDFf_3_14_mul27_CAST_mul35<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_fixp + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_double + (-1)*C5__Z4CNDFf_3_14_mul27_CAST_mul35<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_double + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixp + (-1)*C6__Z4CNDFf_3_14_mul27_CAST_mul35<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_float + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_double + (-1)*C7__Z4CNDFf_3_14_mul27_CAST_mul35<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul27_CAST_mul35
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_double + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_float + (-1)*C8__Z4CNDFf_3_14_mul27_CAST_mul35<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul27_CAST_mul35



#Stuff for double 0xBFD6D1F0E5A8325B
ConstantValue__72_fixbits = solver.IntVar(0, 30, 'ConstantValue__72_fixbits')
ConstantValue__72_fixp = solver.IntVar(0, 1, 'ConstantValue__72_fixp')
ConstantValue__72_float = solver.IntVar(0, 1, 'ConstantValue__72_float')
ConstantValue__72_double = solver.IntVar(0, 1, 'ConstantValue__72_double')
ConstantValue__72_enob = solver.IntVar(-10000, 10000, 'ConstantValue__72_enob')
solver.Add( + (1)*ConstantValue__72_enob + (-1)*ConstantValue__72_fixbits + (10000)*ConstantValue__72_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__72_enob + (10000)*ConstantValue__72_float<=10025)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__72_enob + (10000)*ConstantValue__72_double<=10054)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__72_fixbits + (-10000)*ConstantValue__72_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__72_fixp + (1)*ConstantValue__72_float + (1)*ConstantValue__72_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__72_fixbits + (-10000)*ConstantValue__72_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul35 = fmul double %conv34, 0xBFD6D1F0E5A8325B, !taffo.info !92, !taffo.initweight !30, !taffo.constinfo !94
ConstantValue__72_CAST_mul35_fixbits = solver.IntVar(0, 30, 'ConstantValue__72_CAST_mul35_fixbits')
ConstantValue__72_CAST_mul35_fixp = solver.IntVar(0, 1, 'ConstantValue__72_CAST_mul35_fixp')
ConstantValue__72_CAST_mul35_float = solver.IntVar(0, 1, 'ConstantValue__72_CAST_mul35_float')
ConstantValue__72_CAST_mul35_double = solver.IntVar(0, 1, 'ConstantValue__72_CAST_mul35_double')
solver.Add( + (1)*ConstantValue__72_CAST_mul35_fixp + (1)*ConstantValue__72_CAST_mul35_float + (1)*ConstantValue__72_CAST_mul35_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__72_CAST_mul35_fixbits + (-10000)*ConstantValue__72_CAST_mul35_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C1_ConstantValue__72_CAST_mul35')
C2_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C2_ConstantValue__72_CAST_mul35')
solver.Add( + (1)*ConstantValue__72_fixbits + (-1)*ConstantValue__72_CAST_mul35_fixbits + (-10000)*C1_ConstantValue__72_CAST_mul35<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__72_fixbits + (1)*ConstantValue__72_CAST_mul35_fixbits + (-10000)*C2_ConstantValue__72_CAST_mul35<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__72_CAST_mul35
castCostObj +=  + (1.13006)*C2_ConstantValue__72_CAST_mul35
C3_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C3_ConstantValue__72_CAST_mul35')
C4_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C4_ConstantValue__72_CAST_mul35')
C5_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C5_ConstantValue__72_CAST_mul35')
C6_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C6_ConstantValue__72_CAST_mul35')
C7_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C7_ConstantValue__72_CAST_mul35')
C8_ConstantValue__72_CAST_mul35 = solver.IntVar(0, 1, 'C8_ConstantValue__72_CAST_mul35')
solver.Add( + (1)*ConstantValue__72_fixp + (1)*ConstantValue__72_CAST_mul35_float + (-1)*C3_ConstantValue__72_CAST_mul35<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__72_CAST_mul35
solver.Add( + (1)*ConstantValue__72_float + (1)*ConstantValue__72_CAST_mul35_fixp + (-1)*C4_ConstantValue__72_CAST_mul35<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__72_CAST_mul35
solver.Add( + (1)*ConstantValue__72_fixp + (1)*ConstantValue__72_CAST_mul35_double + (-1)*C5_ConstantValue__72_CAST_mul35<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__72_CAST_mul35
solver.Add( + (1)*ConstantValue__72_double + (1)*ConstantValue__72_CAST_mul35_fixp + (-1)*C6_ConstantValue__72_CAST_mul35<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__72_CAST_mul35
solver.Add( + (1)*ConstantValue__72_float + (1)*ConstantValue__72_CAST_mul35_double + (-1)*C7_ConstantValue__72_CAST_mul35<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__72_CAST_mul35
solver.Add( + (1)*ConstantValue__72_double + (1)*ConstantValue__72_CAST_mul35_float + (-1)*C8_ConstantValue__72_CAST_mul35<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__72_CAST_mul35



#Stuff for   %mul35 = fmul double %conv34, 0xBFD6D1F0E5A8325B, !taffo.info !92, !taffo.initweight !30, !taffo.constinfo !94
_Z4CNDFf_3_14_mul35_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul35_fixbits')
_Z4CNDFf_3_14_mul35_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul35_fixp')
_Z4CNDFf_3_14_mul35_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul35_float')
_Z4CNDFf_3_14_mul35_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul35_double')
_Z4CNDFf_3_14_mul35_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul35_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_enob + (-1)*_Z4CNDFf_3_14_mul35_fixbits + (10000)*_Z4CNDFf_3_14_mul35_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_enob + (10000)*_Z4CNDFf_3_14_mul35_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_enob + (10000)*_Z4CNDFf_3_14_mul35_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_fixbits + (-10000)*_Z4CNDFf_3_14_mul35_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul35_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_fixp + (1)*_Z4CNDFf_3_14_mul35_float + (1)*_Z4CNDFf_3_14_mul35_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_fixbits + (-10000)*_Z4CNDFf_3_14_mul35_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixp + (-1)*ConstantValue__72_CAST_mul35_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_float + (-1)*ConstantValue__72_CAST_mul35_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_double + (-1)*ConstantValue__72_CAST_mul35_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_fixp + (-1)*_Z4CNDFf_3_14_mul35_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_float + (-1)*_Z4CNDFf_3_14_mul35_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul27_CAST_mul35_double + (-1)*_Z4CNDFf_3_14_mul35_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul35_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul35_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul35_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_enob + (-1)*ConstantValue__70_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_enob + (-1)*_Z4CNDFf_3_14_mul27_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul35_enob_2<=1)    #Enob: propagation in product 2



#Stuff for double 0x3FFC80EF025F5E68
ConstantValue__73_fixbits = solver.IntVar(0, 30, 'ConstantValue__73_fixbits')
ConstantValue__73_fixp = solver.IntVar(0, 1, 'ConstantValue__73_fixp')
ConstantValue__73_float = solver.IntVar(0, 1, 'ConstantValue__73_float')
ConstantValue__73_double = solver.IntVar(0, 1, 'ConstantValue__73_double')
ConstantValue__73_enob = solver.IntVar(-10000, 10000, 'ConstantValue__73_enob')
solver.Add( + (1)*ConstantValue__73_enob + (-1)*ConstantValue__73_fixbits + (10000)*ConstantValue__73_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__73_enob + (10000)*ConstantValue__73_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__73_enob + (10000)*ConstantValue__73_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__73_fixbits + (-10000)*ConstantValue__73_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__73_fixp + (1)*ConstantValue__73_float + (1)*ConstantValue__73_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__73_fixbits + (-10000)*ConstantValue__73_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FFC80EF025F5E68
ConstantValue__74_fixbits = solver.IntVar(0, 30, 'ConstantValue__74_fixbits')
ConstantValue__74_fixp = solver.IntVar(0, 1, 'ConstantValue__74_fixp')
ConstantValue__74_float = solver.IntVar(0, 1, 'ConstantValue__74_float')
ConstantValue__74_double = solver.IntVar(0, 1, 'ConstantValue__74_double')
ConstantValue__74_enob = solver.IntVar(-10000, 10000, 'ConstantValue__74_enob')
solver.Add( + (1)*ConstantValue__74_enob + (-1)*ConstantValue__74_fixbits + (10000)*ConstantValue__74_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__74_enob + (10000)*ConstantValue__74_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__74_enob + (10000)*ConstantValue__74_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__74_fixbits + (-10000)*ConstantValue__74_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__74_fixp + (1)*ConstantValue__74_float + (1)*ConstantValue__74_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__74_fixbits + (-10000)*ConstantValue__74_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul38 = fmul double %conv37, 0x3FFC80EF025F5E68, !taffo.info !99, !taffo.initweight !30, !taffo.constinfo !101
_Z4CNDFf_3_14_mul28_CAST_mul38_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul28_CAST_mul38_fixbits')
_Z4CNDFf_3_14_mul28_CAST_mul38_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_CAST_mul38_fixp')
_Z4CNDFf_3_14_mul28_CAST_mul38_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_CAST_mul38_float')
_Z4CNDFf_3_14_mul28_CAST_mul38_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul28_CAST_mul38_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixp + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_float + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixbits + (-10000)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul28_CAST_mul38')
C2__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul28_CAST_mul38')
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixbits + (-1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul28_CAST_mul38<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul28_fixbits + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul28_CAST_mul38<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul28_CAST_mul38
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul28_CAST_mul38
C3__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul28_CAST_mul38')
C4__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul28_CAST_mul38')
C5__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul28_CAST_mul38')
C6__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul28_CAST_mul38')
C7__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul28_CAST_mul38')
C8__Z4CNDFf_3_14_mul28_CAST_mul38 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul28_CAST_mul38')
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixp + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_float + (-1)*C3__Z4CNDFf_3_14_mul28_CAST_mul38<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_float + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixp + (-1)*C4__Z4CNDFf_3_14_mul28_CAST_mul38<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_fixp + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_double + (-1)*C5__Z4CNDFf_3_14_mul28_CAST_mul38<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_double + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixp + (-1)*C6__Z4CNDFf_3_14_mul28_CAST_mul38<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_float + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_double + (-1)*C7__Z4CNDFf_3_14_mul28_CAST_mul38<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul28_CAST_mul38
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_double + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_float + (-1)*C8__Z4CNDFf_3_14_mul28_CAST_mul38<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul28_CAST_mul38



#Stuff for double 0x3FFC80EF025F5E68
ConstantValue__75_fixbits = solver.IntVar(0, 30, 'ConstantValue__75_fixbits')
ConstantValue__75_fixp = solver.IntVar(0, 1, 'ConstantValue__75_fixp')
ConstantValue__75_float = solver.IntVar(0, 1, 'ConstantValue__75_float')
ConstantValue__75_double = solver.IntVar(0, 1, 'ConstantValue__75_double')
ConstantValue__75_enob = solver.IntVar(-10000, 10000, 'ConstantValue__75_enob')
solver.Add( + (1)*ConstantValue__75_enob + (-1)*ConstantValue__75_fixbits + (10000)*ConstantValue__75_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__75_enob + (10000)*ConstantValue__75_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__75_enob + (10000)*ConstantValue__75_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__75_fixbits + (-10000)*ConstantValue__75_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__75_fixp + (1)*ConstantValue__75_float + (1)*ConstantValue__75_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__75_fixbits + (-10000)*ConstantValue__75_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul38 = fmul double %conv37, 0x3FFC80EF025F5E68, !taffo.info !99, !taffo.initweight !30, !taffo.constinfo !101
ConstantValue__75_CAST_mul38_fixbits = solver.IntVar(0, 30, 'ConstantValue__75_CAST_mul38_fixbits')
ConstantValue__75_CAST_mul38_fixp = solver.IntVar(0, 1, 'ConstantValue__75_CAST_mul38_fixp')
ConstantValue__75_CAST_mul38_float = solver.IntVar(0, 1, 'ConstantValue__75_CAST_mul38_float')
ConstantValue__75_CAST_mul38_double = solver.IntVar(0, 1, 'ConstantValue__75_CAST_mul38_double')
solver.Add( + (1)*ConstantValue__75_CAST_mul38_fixp + (1)*ConstantValue__75_CAST_mul38_float + (1)*ConstantValue__75_CAST_mul38_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__75_CAST_mul38_fixbits + (-10000)*ConstantValue__75_CAST_mul38_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C1_ConstantValue__75_CAST_mul38')
C2_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C2_ConstantValue__75_CAST_mul38')
solver.Add( + (1)*ConstantValue__75_fixbits + (-1)*ConstantValue__75_CAST_mul38_fixbits + (-10000)*C1_ConstantValue__75_CAST_mul38<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__75_fixbits + (1)*ConstantValue__75_CAST_mul38_fixbits + (-10000)*C2_ConstantValue__75_CAST_mul38<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__75_CAST_mul38
castCostObj +=  + (1.13006)*C2_ConstantValue__75_CAST_mul38
C3_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C3_ConstantValue__75_CAST_mul38')
C4_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C4_ConstantValue__75_CAST_mul38')
C5_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C5_ConstantValue__75_CAST_mul38')
C6_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C6_ConstantValue__75_CAST_mul38')
C7_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C7_ConstantValue__75_CAST_mul38')
C8_ConstantValue__75_CAST_mul38 = solver.IntVar(0, 1, 'C8_ConstantValue__75_CAST_mul38')
solver.Add( + (1)*ConstantValue__75_fixp + (1)*ConstantValue__75_CAST_mul38_float + (-1)*C3_ConstantValue__75_CAST_mul38<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__75_CAST_mul38
solver.Add( + (1)*ConstantValue__75_float + (1)*ConstantValue__75_CAST_mul38_fixp + (-1)*C4_ConstantValue__75_CAST_mul38<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__75_CAST_mul38
solver.Add( + (1)*ConstantValue__75_fixp + (1)*ConstantValue__75_CAST_mul38_double + (-1)*C5_ConstantValue__75_CAST_mul38<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__75_CAST_mul38
solver.Add( + (1)*ConstantValue__75_double + (1)*ConstantValue__75_CAST_mul38_fixp + (-1)*C6_ConstantValue__75_CAST_mul38<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__75_CAST_mul38
solver.Add( + (1)*ConstantValue__75_float + (1)*ConstantValue__75_CAST_mul38_double + (-1)*C7_ConstantValue__75_CAST_mul38<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__75_CAST_mul38
solver.Add( + (1)*ConstantValue__75_double + (1)*ConstantValue__75_CAST_mul38_float + (-1)*C8_ConstantValue__75_CAST_mul38<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__75_CAST_mul38



#Stuff for   %mul38 = fmul double %conv37, 0x3FFC80EF025F5E68, !taffo.info !99, !taffo.initweight !30, !taffo.constinfo !101
_Z4CNDFf_3_14_mul38_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul38_fixbits')
_Z4CNDFf_3_14_mul38_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul38_fixp')
_Z4CNDFf_3_14_mul38_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul38_float')
_Z4CNDFf_3_14_mul38_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul38_double')
_Z4CNDFf_3_14_mul38_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul38_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_enob + (-1)*_Z4CNDFf_3_14_mul38_fixbits + (10000)*_Z4CNDFf_3_14_mul38_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_enob + (10000)*_Z4CNDFf_3_14_mul38_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_enob + (10000)*_Z4CNDFf_3_14_mul38_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_fixbits + (-10000)*_Z4CNDFf_3_14_mul38_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul38_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_fixp + (1)*_Z4CNDFf_3_14_mul38_float + (1)*_Z4CNDFf_3_14_mul38_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_fixbits + (-10000)*_Z4CNDFf_3_14_mul38_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixp + (-1)*ConstantValue__75_CAST_mul38_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_float + (-1)*ConstantValue__75_CAST_mul38_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_double + (-1)*ConstantValue__75_CAST_mul38_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_fixp + (-1)*_Z4CNDFf_3_14_mul38_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_float + (-1)*_Z4CNDFf_3_14_mul38_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul28_CAST_mul38_double + (-1)*_Z4CNDFf_3_14_mul38_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul38_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul38_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul38_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_enob + (-1)*ConstantValue__73_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_enob + (-1)*_Z4CNDFf_3_14_mul28_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul38_enob_2<=-1)    #Enob: propagation in product 2



#Constraint for cast for   %add40 = fadd float %conv36, %conv39, !taffo.info !106, !taffo.initweight !23
_Z4CNDFf_3_14_mul35_CAST_add40_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul35_CAST_add40_fixbits')
_Z4CNDFf_3_14_mul35_CAST_add40_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul35_CAST_add40_fixp')
_Z4CNDFf_3_14_mul35_CAST_add40_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul35_CAST_add40_float')
_Z4CNDFf_3_14_mul35_CAST_add40_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul35_CAST_add40_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixp + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_float + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixbits + (-10000)*_Z4CNDFf_3_14_mul35_CAST_add40_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul35_CAST_add40')
C2__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul35_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_fixbits + (-1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul35_CAST_add40<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul35_fixbits + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul35_CAST_add40<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul35_CAST_add40
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul35_CAST_add40
C3__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul35_CAST_add40')
C4__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul35_CAST_add40')
C5__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul35_CAST_add40')
C6__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul35_CAST_add40')
C7__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul35_CAST_add40')
C8__Z4CNDFf_3_14_mul35_CAST_add40 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul35_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_fixp + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_float + (-1)*C3__Z4CNDFf_3_14_mul35_CAST_add40<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_float + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixp + (-1)*C4__Z4CNDFf_3_14_mul35_CAST_add40<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_fixp + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_double + (-1)*C5__Z4CNDFf_3_14_mul35_CAST_add40<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_double + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixp + (-1)*C6__Z4CNDFf_3_14_mul35_CAST_add40<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_float + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_double + (-1)*C7__Z4CNDFf_3_14_mul35_CAST_add40<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul35_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_double + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_float + (-1)*C8__Z4CNDFf_3_14_mul35_CAST_add40<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul35_CAST_add40



#Constraint for cast for   %add40 = fadd float %conv36, %conv39, !taffo.info !106, !taffo.initweight !23
_Z4CNDFf_3_14_mul38_CAST_add40_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul38_CAST_add40_fixbits')
_Z4CNDFf_3_14_mul38_CAST_add40_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul38_CAST_add40_fixp')
_Z4CNDFf_3_14_mul38_CAST_add40_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul38_CAST_add40_float')
_Z4CNDFf_3_14_mul38_CAST_add40_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul38_CAST_add40_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixp + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_float + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixbits + (-10000)*_Z4CNDFf_3_14_mul38_CAST_add40_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul38_CAST_add40')
C2__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul38_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_fixbits + (-1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul38_CAST_add40<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul38_fixbits + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul38_CAST_add40<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul38_CAST_add40
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul38_CAST_add40
C3__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul38_CAST_add40')
C4__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul38_CAST_add40')
C5__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul38_CAST_add40')
C6__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul38_CAST_add40')
C7__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul38_CAST_add40')
C8__Z4CNDFf_3_14_mul38_CAST_add40 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul38_CAST_add40')
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_fixp + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_float + (-1)*C3__Z4CNDFf_3_14_mul38_CAST_add40<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_float + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixp + (-1)*C4__Z4CNDFf_3_14_mul38_CAST_add40<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_fixp + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_double + (-1)*C5__Z4CNDFf_3_14_mul38_CAST_add40<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_double + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixp + (-1)*C6__Z4CNDFf_3_14_mul38_CAST_add40<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_float + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_double + (-1)*C7__Z4CNDFf_3_14_mul38_CAST_add40<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul38_CAST_add40
solver.Add( + (1)*_Z4CNDFf_3_14_mul38_double + (1)*_Z4CNDFf_3_14_mul38_CAST_add40_float + (-1)*C8__Z4CNDFf_3_14_mul38_CAST_add40<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul38_CAST_add40



#Stuff for   %add40 = fadd float %conv36, %conv39, !taffo.info !106, !taffo.initweight !23
_Z4CNDFf_3_14_add40_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add40_fixbits')
_Z4CNDFf_3_14_add40_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add40_fixp')
_Z4CNDFf_3_14_add40_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add40_float')
_Z4CNDFf_3_14_add40_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add40_double')
_Z4CNDFf_3_14_add40_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_add40_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_add40_enob + (-1)*_Z4CNDFf_3_14_add40_fixbits + (10000)*_Z4CNDFf_3_14_add40_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_add40_enob + (10000)*_Z4CNDFf_3_14_add40_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_add40_enob + (10000)*_Z4CNDFf_3_14_add40_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_add40_fixbits + (-10000)*_Z4CNDFf_3_14_add40_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_add40_enob
solver.Add( + (1)*_Z4CNDFf_3_14_add40_fixp + (1)*_Z4CNDFf_3_14_add40_float + (1)*_Z4CNDFf_3_14_add40_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_add40_fixbits + (-10000)*_Z4CNDFf_3_14_add40_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixp + (-1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_float + (-1)*_Z4CNDFf_3_14_mul38_CAST_add40_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_double + (-1)*_Z4CNDFf_3_14_mul38_CAST_add40_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixbits + (-1)*_Z4CNDFf_3_14_mul38_CAST_add40_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixp + (-1)*_Z4CNDFf_3_14_add40_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_float + (-1)*_Z4CNDFf_3_14_add40_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_double + (-1)*_Z4CNDFf_3_14_add40_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul35_CAST_add40_fixbits + (-1)*_Z4CNDFf_3_14_add40_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_add40_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_add40_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_add40_double
solver.Add( + (1)*_Z4CNDFf_3_14_add40_enob + (-1)*_Z4CNDFf_3_14_mul35_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_3_14_add40_enob + (-1)*_Z4CNDFf_3_14_mul38_enob<=0)    #Enob propagation in sum second addend



#Stuff for double 0xBFFD23DD4EF278D0
ConstantValue__76_fixbits = solver.IntVar(0, 29, 'ConstantValue__76_fixbits')
ConstantValue__76_fixp = solver.IntVar(0, 1, 'ConstantValue__76_fixp')
ConstantValue__76_float = solver.IntVar(0, 1, 'ConstantValue__76_float')
ConstantValue__76_double = solver.IntVar(0, 1, 'ConstantValue__76_double')
ConstantValue__76_enob = solver.IntVar(-10000, 10000, 'ConstantValue__76_enob')
solver.Add( + (1)*ConstantValue__76_enob + (-1)*ConstantValue__76_fixbits + (10000)*ConstantValue__76_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__76_enob + (10000)*ConstantValue__76_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__76_enob + (10000)*ConstantValue__76_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__76_fixbits + (-10000)*ConstantValue__76_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__76_fixp + (1)*ConstantValue__76_float + (1)*ConstantValue__76_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__76_fixbits + (-10000)*ConstantValue__76_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0xBFFD23DD4EF278D0
ConstantValue__77_fixbits = solver.IntVar(0, 29, 'ConstantValue__77_fixbits')
ConstantValue__77_fixp = solver.IntVar(0, 1, 'ConstantValue__77_fixp')
ConstantValue__77_float = solver.IntVar(0, 1, 'ConstantValue__77_float')
ConstantValue__77_double = solver.IntVar(0, 1, 'ConstantValue__77_double')
ConstantValue__77_enob = solver.IntVar(-10000, 10000, 'ConstantValue__77_enob')
solver.Add( + (1)*ConstantValue__77_enob + (-1)*ConstantValue__77_fixbits + (10000)*ConstantValue__77_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__77_enob + (10000)*ConstantValue__77_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__77_enob + (10000)*ConstantValue__77_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__77_fixbits + (-10000)*ConstantValue__77_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__77_fixp + (1)*ConstantValue__77_float + (1)*ConstantValue__77_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__77_fixbits + (-10000)*ConstantValue__77_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul42 = fmul double %conv41, 0xBFFD23DD4EF278D0, !taffo.info !108, !taffo.initweight !30, !taffo.constinfo !110
_Z4CNDFf_3_14_mul29_CAST_mul42_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul29_CAST_mul42_fixbits')
_Z4CNDFf_3_14_mul29_CAST_mul42_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_CAST_mul42_fixp')
_Z4CNDFf_3_14_mul29_CAST_mul42_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_CAST_mul42_float')
_Z4CNDFf_3_14_mul29_CAST_mul42_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul29_CAST_mul42_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixp + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_float + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixbits + (-10000)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul29_CAST_mul42')
C2__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul29_CAST_mul42')
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixbits + (-1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul29_CAST_mul42<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul29_fixbits + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul29_CAST_mul42<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul29_CAST_mul42
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul29_CAST_mul42
C3__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul29_CAST_mul42')
C4__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul29_CAST_mul42')
C5__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul29_CAST_mul42')
C6__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul29_CAST_mul42')
C7__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul29_CAST_mul42')
C8__Z4CNDFf_3_14_mul29_CAST_mul42 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul29_CAST_mul42')
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixp + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_float + (-1)*C3__Z4CNDFf_3_14_mul29_CAST_mul42<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_float + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixp + (-1)*C4__Z4CNDFf_3_14_mul29_CAST_mul42<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_fixp + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_double + (-1)*C5__Z4CNDFf_3_14_mul29_CAST_mul42<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_double + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixp + (-1)*C6__Z4CNDFf_3_14_mul29_CAST_mul42<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_float + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_double + (-1)*C7__Z4CNDFf_3_14_mul29_CAST_mul42<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul29_CAST_mul42
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_double + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_float + (-1)*C8__Z4CNDFf_3_14_mul29_CAST_mul42<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul29_CAST_mul42



#Stuff for double 0xBFFD23DD4EF278D0
ConstantValue__78_fixbits = solver.IntVar(0, 29, 'ConstantValue__78_fixbits')
ConstantValue__78_fixp = solver.IntVar(0, 1, 'ConstantValue__78_fixp')
ConstantValue__78_float = solver.IntVar(0, 1, 'ConstantValue__78_float')
ConstantValue__78_double = solver.IntVar(0, 1, 'ConstantValue__78_double')
ConstantValue__78_enob = solver.IntVar(-10000, 10000, 'ConstantValue__78_enob')
solver.Add( + (1)*ConstantValue__78_enob + (-1)*ConstantValue__78_fixbits + (10000)*ConstantValue__78_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__78_enob + (10000)*ConstantValue__78_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__78_enob + (10000)*ConstantValue__78_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__78_fixbits + (-10000)*ConstantValue__78_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*ConstantValue__78_fixp + (1)*ConstantValue__78_float + (1)*ConstantValue__78_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__78_fixbits + (-10000)*ConstantValue__78_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul42 = fmul double %conv41, 0xBFFD23DD4EF278D0, !taffo.info !108, !taffo.initweight !30, !taffo.constinfo !110
ConstantValue__78_CAST_mul42_fixbits = solver.IntVar(0, 29, 'ConstantValue__78_CAST_mul42_fixbits')
ConstantValue__78_CAST_mul42_fixp = solver.IntVar(0, 1, 'ConstantValue__78_CAST_mul42_fixp')
ConstantValue__78_CAST_mul42_float = solver.IntVar(0, 1, 'ConstantValue__78_CAST_mul42_float')
ConstantValue__78_CAST_mul42_double = solver.IntVar(0, 1, 'ConstantValue__78_CAST_mul42_double')
solver.Add( + (1)*ConstantValue__78_CAST_mul42_fixp + (1)*ConstantValue__78_CAST_mul42_float + (1)*ConstantValue__78_CAST_mul42_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__78_CAST_mul42_fixbits + (-10000)*ConstantValue__78_CAST_mul42_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C1_ConstantValue__78_CAST_mul42')
C2_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C2_ConstantValue__78_CAST_mul42')
solver.Add( + (1)*ConstantValue__78_fixbits + (-1)*ConstantValue__78_CAST_mul42_fixbits + (-10000)*C1_ConstantValue__78_CAST_mul42<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__78_fixbits + (1)*ConstantValue__78_CAST_mul42_fixbits + (-10000)*C2_ConstantValue__78_CAST_mul42<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__78_CAST_mul42
castCostObj +=  + (1.13006)*C2_ConstantValue__78_CAST_mul42
C3_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C3_ConstantValue__78_CAST_mul42')
C4_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C4_ConstantValue__78_CAST_mul42')
C5_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C5_ConstantValue__78_CAST_mul42')
C6_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C6_ConstantValue__78_CAST_mul42')
C7_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C7_ConstantValue__78_CAST_mul42')
C8_ConstantValue__78_CAST_mul42 = solver.IntVar(0, 1, 'C8_ConstantValue__78_CAST_mul42')
solver.Add( + (1)*ConstantValue__78_fixp + (1)*ConstantValue__78_CAST_mul42_float + (-1)*C3_ConstantValue__78_CAST_mul42<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__78_CAST_mul42
solver.Add( + (1)*ConstantValue__78_float + (1)*ConstantValue__78_CAST_mul42_fixp + (-1)*C4_ConstantValue__78_CAST_mul42<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__78_CAST_mul42
solver.Add( + (1)*ConstantValue__78_fixp + (1)*ConstantValue__78_CAST_mul42_double + (-1)*C5_ConstantValue__78_CAST_mul42<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__78_CAST_mul42
solver.Add( + (1)*ConstantValue__78_double + (1)*ConstantValue__78_CAST_mul42_fixp + (-1)*C6_ConstantValue__78_CAST_mul42<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__78_CAST_mul42
solver.Add( + (1)*ConstantValue__78_float + (1)*ConstantValue__78_CAST_mul42_double + (-1)*C7_ConstantValue__78_CAST_mul42<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__78_CAST_mul42
solver.Add( + (1)*ConstantValue__78_double + (1)*ConstantValue__78_CAST_mul42_float + (-1)*C8_ConstantValue__78_CAST_mul42<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__78_CAST_mul42



#Stuff for   %mul42 = fmul double %conv41, 0xBFFD23DD4EF278D0, !taffo.info !108, !taffo.initweight !30, !taffo.constinfo !110
_Z4CNDFf_3_14_mul42_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul42_fixbits')
_Z4CNDFf_3_14_mul42_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul42_fixp')
_Z4CNDFf_3_14_mul42_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul42_float')
_Z4CNDFf_3_14_mul42_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul42_double')
_Z4CNDFf_3_14_mul42_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul42_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_enob + (-1)*_Z4CNDFf_3_14_mul42_fixbits + (10000)*_Z4CNDFf_3_14_mul42_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_enob + (10000)*_Z4CNDFf_3_14_mul42_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_enob + (10000)*_Z4CNDFf_3_14_mul42_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_fixbits + (-10000)*_Z4CNDFf_3_14_mul42_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul42_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_fixp + (1)*_Z4CNDFf_3_14_mul42_float + (1)*_Z4CNDFf_3_14_mul42_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_fixbits + (-10000)*_Z4CNDFf_3_14_mul42_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixp + (-1)*ConstantValue__78_CAST_mul42_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_float + (-1)*ConstantValue__78_CAST_mul42_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_double + (-1)*ConstantValue__78_CAST_mul42_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_fixp + (-1)*_Z4CNDFf_3_14_mul42_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_float + (-1)*_Z4CNDFf_3_14_mul42_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul29_CAST_mul42_double + (-1)*_Z4CNDFf_3_14_mul42_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul42_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul42_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul42_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_enob + (-1)*ConstantValue__76_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_enob + (-1)*_Z4CNDFf_3_14_mul29_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul42_enob_2<=-1)    #Enob: propagation in product 2



#Constraint for cast for   %add44 = fadd float %add40, %conv43, !taffo.info !115, !taffo.initweight !23
_Z4CNDFf_3_14_add40_CAST_add44_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add40_CAST_add44_fixbits')
_Z4CNDFf_3_14_add40_CAST_add44_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add40_CAST_add44_fixp')
_Z4CNDFf_3_14_add40_CAST_add44_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add40_CAST_add44_float')
_Z4CNDFf_3_14_add40_CAST_add44_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add40_CAST_add44_double')
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixp + (1)*_Z4CNDFf_3_14_add40_CAST_add44_float + (1)*_Z4CNDFf_3_14_add40_CAST_add44_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixbits + (-10000)*_Z4CNDFf_3_14_add40_CAST_add44_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_add40_CAST_add44')
C2__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_add40_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_3_14_add40_fixbits + (-1)*_Z4CNDFf_3_14_add40_CAST_add44_fixbits + (-10000)*C1__Z4CNDFf_3_14_add40_CAST_add44<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_add40_fixbits + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixbits + (-10000)*C2__Z4CNDFf_3_14_add40_CAST_add44<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_add40_CAST_add44
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_add40_CAST_add44
C3__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_add40_CAST_add44')
C4__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_add40_CAST_add44')
C5__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_add40_CAST_add44')
C6__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_add40_CAST_add44')
C7__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_add40_CAST_add44')
C8__Z4CNDFf_3_14_add40_CAST_add44 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_add40_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_3_14_add40_fixp + (1)*_Z4CNDFf_3_14_add40_CAST_add44_float + (-1)*C3__Z4CNDFf_3_14_add40_CAST_add44<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_add40_float + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixp + (-1)*C4__Z4CNDFf_3_14_add40_CAST_add44<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_add40_fixp + (1)*_Z4CNDFf_3_14_add40_CAST_add44_double + (-1)*C5__Z4CNDFf_3_14_add40_CAST_add44<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_add40_double + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixp + (-1)*C6__Z4CNDFf_3_14_add40_CAST_add44<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_add40_float + (1)*_Z4CNDFf_3_14_add40_CAST_add44_double + (-1)*C7__Z4CNDFf_3_14_add40_CAST_add44<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_add40_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_add40_double + (1)*_Z4CNDFf_3_14_add40_CAST_add44_float + (-1)*C8__Z4CNDFf_3_14_add40_CAST_add44<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_add40_CAST_add44



#Constraint for cast for   %add44 = fadd float %add40, %conv43, !taffo.info !115, !taffo.initweight !23
_Z4CNDFf_3_14_mul42_CAST_add44_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul42_CAST_add44_fixbits')
_Z4CNDFf_3_14_mul42_CAST_add44_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul42_CAST_add44_fixp')
_Z4CNDFf_3_14_mul42_CAST_add44_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul42_CAST_add44_float')
_Z4CNDFf_3_14_mul42_CAST_add44_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul42_CAST_add44_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixp + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_float + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixbits + (-10000)*_Z4CNDFf_3_14_mul42_CAST_add44_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul42_CAST_add44')
C2__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul42_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_fixbits + (-1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul42_CAST_add44<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul42_fixbits + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul42_CAST_add44<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul42_CAST_add44
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul42_CAST_add44
C3__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul42_CAST_add44')
C4__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul42_CAST_add44')
C5__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul42_CAST_add44')
C6__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul42_CAST_add44')
C7__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul42_CAST_add44')
C8__Z4CNDFf_3_14_mul42_CAST_add44 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul42_CAST_add44')
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_fixp + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_float + (-1)*C3__Z4CNDFf_3_14_mul42_CAST_add44<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_float + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixp + (-1)*C4__Z4CNDFf_3_14_mul42_CAST_add44<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_fixp + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_double + (-1)*C5__Z4CNDFf_3_14_mul42_CAST_add44<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_double + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixp + (-1)*C6__Z4CNDFf_3_14_mul42_CAST_add44<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_float + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_double + (-1)*C7__Z4CNDFf_3_14_mul42_CAST_add44<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul42_CAST_add44
solver.Add( + (1)*_Z4CNDFf_3_14_mul42_double + (1)*_Z4CNDFf_3_14_mul42_CAST_add44_float + (-1)*C8__Z4CNDFf_3_14_mul42_CAST_add44<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul42_CAST_add44



#Stuff for   %add44 = fadd float %add40, %conv43, !taffo.info !115, !taffo.initweight !23
_Z4CNDFf_3_14_add44_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add44_fixbits')
_Z4CNDFf_3_14_add44_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add44_fixp')
_Z4CNDFf_3_14_add44_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add44_float')
_Z4CNDFf_3_14_add44_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add44_double')
_Z4CNDFf_3_14_add44_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_add44_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_add44_enob + (-1)*_Z4CNDFf_3_14_add44_fixbits + (10000)*_Z4CNDFf_3_14_add44_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_add44_enob + (10000)*_Z4CNDFf_3_14_add44_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_add44_enob + (10000)*_Z4CNDFf_3_14_add44_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_add44_fixbits + (-10000)*_Z4CNDFf_3_14_add44_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_add44_enob
solver.Add( + (1)*_Z4CNDFf_3_14_add44_fixp + (1)*_Z4CNDFf_3_14_add44_float + (1)*_Z4CNDFf_3_14_add44_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_add44_fixbits + (-10000)*_Z4CNDFf_3_14_add44_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixp + (-1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_float + (-1)*_Z4CNDFf_3_14_mul42_CAST_add44_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_double + (-1)*_Z4CNDFf_3_14_mul42_CAST_add44_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixbits + (-1)*_Z4CNDFf_3_14_mul42_CAST_add44_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixp + (-1)*_Z4CNDFf_3_14_add44_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_float + (-1)*_Z4CNDFf_3_14_add44_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_double + (-1)*_Z4CNDFf_3_14_add44_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_add40_CAST_add44_fixbits + (-1)*_Z4CNDFf_3_14_add44_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_add44_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_add44_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_add44_double
solver.Add( + (1)*_Z4CNDFf_3_14_add44_enob + (-1)*_Z4CNDFf_3_14_add40_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_3_14_add44_enob + (-1)*_Z4CNDFf_3_14_mul42_enob<=0)    #Enob propagation in sum second addend



#Stuff for double 0x3FF548CDD6F42943
ConstantValue__79_fixbits = solver.IntVar(0, 30, 'ConstantValue__79_fixbits')
ConstantValue__79_fixp = solver.IntVar(0, 1, 'ConstantValue__79_fixp')
ConstantValue__79_float = solver.IntVar(0, 1, 'ConstantValue__79_float')
ConstantValue__79_double = solver.IntVar(0, 1, 'ConstantValue__79_double')
ConstantValue__79_enob = solver.IntVar(-10000, 10000, 'ConstantValue__79_enob')
solver.Add( + (1)*ConstantValue__79_enob + (-1)*ConstantValue__79_fixbits + (10000)*ConstantValue__79_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__79_enob + (10000)*ConstantValue__79_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__79_enob + (10000)*ConstantValue__79_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__79_fixbits + (-10000)*ConstantValue__79_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__79_fixp + (1)*ConstantValue__79_float + (1)*ConstantValue__79_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__79_fixbits + (-10000)*ConstantValue__79_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0x3FF548CDD6F42943
ConstantValue__80_fixbits = solver.IntVar(0, 30, 'ConstantValue__80_fixbits')
ConstantValue__80_fixp = solver.IntVar(0, 1, 'ConstantValue__80_fixp')
ConstantValue__80_float = solver.IntVar(0, 1, 'ConstantValue__80_float')
ConstantValue__80_double = solver.IntVar(0, 1, 'ConstantValue__80_double')
ConstantValue__80_enob = solver.IntVar(-10000, 10000, 'ConstantValue__80_enob')
solver.Add( + (1)*ConstantValue__80_enob + (-1)*ConstantValue__80_fixbits + (10000)*ConstantValue__80_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__80_enob + (10000)*ConstantValue__80_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__80_enob + (10000)*ConstantValue__80_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__80_fixbits + (-10000)*ConstantValue__80_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__80_fixp + (1)*ConstantValue__80_float + (1)*ConstantValue__80_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__80_fixbits + (-10000)*ConstantValue__80_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul46 = fmul double %conv45, 0x3FF548CDD6F42943, !taffo.info !117, !taffo.initweight !30, !taffo.constinfo !119
_Z4CNDFf_3_14_mul30_CAST_mul46_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul30_CAST_mul46_fixbits')
_Z4CNDFf_3_14_mul30_CAST_mul46_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul30_CAST_mul46_fixp')
_Z4CNDFf_3_14_mul30_CAST_mul46_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul30_CAST_mul46_float')
_Z4CNDFf_3_14_mul30_CAST_mul46_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul30_CAST_mul46_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixp + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_float + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixbits + (-10000)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul30_CAST_mul46')
C2__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul30_CAST_mul46')
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_fixbits + (-1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul30_CAST_mul46<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul30_fixbits + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul30_CAST_mul46<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul30_CAST_mul46
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul30_CAST_mul46
C3__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul30_CAST_mul46')
C4__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul30_CAST_mul46')
C5__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul30_CAST_mul46')
C6__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul30_CAST_mul46')
C7__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul30_CAST_mul46')
C8__Z4CNDFf_3_14_mul30_CAST_mul46 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul30_CAST_mul46')
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_fixp + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_float + (-1)*C3__Z4CNDFf_3_14_mul30_CAST_mul46<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_float + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixp + (-1)*C4__Z4CNDFf_3_14_mul30_CAST_mul46<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_fixp + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_double + (-1)*C5__Z4CNDFf_3_14_mul30_CAST_mul46<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_double + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixp + (-1)*C6__Z4CNDFf_3_14_mul30_CAST_mul46<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_float + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_double + (-1)*C7__Z4CNDFf_3_14_mul30_CAST_mul46<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul30_CAST_mul46
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_double + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_float + (-1)*C8__Z4CNDFf_3_14_mul30_CAST_mul46<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul30_CAST_mul46



#Stuff for double 0x3FF548CDD6F42943
ConstantValue__81_fixbits = solver.IntVar(0, 30, 'ConstantValue__81_fixbits')
ConstantValue__81_fixp = solver.IntVar(0, 1, 'ConstantValue__81_fixp')
ConstantValue__81_float = solver.IntVar(0, 1, 'ConstantValue__81_float')
ConstantValue__81_double = solver.IntVar(0, 1, 'ConstantValue__81_double')
ConstantValue__81_enob = solver.IntVar(-10000, 10000, 'ConstantValue__81_enob')
solver.Add( + (1)*ConstantValue__81_enob + (-1)*ConstantValue__81_fixbits + (10000)*ConstantValue__81_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__81_enob + (10000)*ConstantValue__81_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__81_enob + (10000)*ConstantValue__81_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__81_fixbits + (-10000)*ConstantValue__81_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__81_fixp + (1)*ConstantValue__81_float + (1)*ConstantValue__81_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__81_fixbits + (-10000)*ConstantValue__81_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul46 = fmul double %conv45, 0x3FF548CDD6F42943, !taffo.info !117, !taffo.initweight !30, !taffo.constinfo !119
ConstantValue__81_CAST_mul46_fixbits = solver.IntVar(0, 30, 'ConstantValue__81_CAST_mul46_fixbits')
ConstantValue__81_CAST_mul46_fixp = solver.IntVar(0, 1, 'ConstantValue__81_CAST_mul46_fixp')
ConstantValue__81_CAST_mul46_float = solver.IntVar(0, 1, 'ConstantValue__81_CAST_mul46_float')
ConstantValue__81_CAST_mul46_double = solver.IntVar(0, 1, 'ConstantValue__81_CAST_mul46_double')
solver.Add( + (1)*ConstantValue__81_CAST_mul46_fixp + (1)*ConstantValue__81_CAST_mul46_float + (1)*ConstantValue__81_CAST_mul46_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__81_CAST_mul46_fixbits + (-10000)*ConstantValue__81_CAST_mul46_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C1_ConstantValue__81_CAST_mul46')
C2_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C2_ConstantValue__81_CAST_mul46')
solver.Add( + (1)*ConstantValue__81_fixbits + (-1)*ConstantValue__81_CAST_mul46_fixbits + (-10000)*C1_ConstantValue__81_CAST_mul46<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__81_fixbits + (1)*ConstantValue__81_CAST_mul46_fixbits + (-10000)*C2_ConstantValue__81_CAST_mul46<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__81_CAST_mul46
castCostObj +=  + (1.13006)*C2_ConstantValue__81_CAST_mul46
C3_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C3_ConstantValue__81_CAST_mul46')
C4_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C4_ConstantValue__81_CAST_mul46')
C5_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C5_ConstantValue__81_CAST_mul46')
C6_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C6_ConstantValue__81_CAST_mul46')
C7_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C7_ConstantValue__81_CAST_mul46')
C8_ConstantValue__81_CAST_mul46 = solver.IntVar(0, 1, 'C8_ConstantValue__81_CAST_mul46')
solver.Add( + (1)*ConstantValue__81_fixp + (1)*ConstantValue__81_CAST_mul46_float + (-1)*C3_ConstantValue__81_CAST_mul46<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__81_CAST_mul46
solver.Add( + (1)*ConstantValue__81_float + (1)*ConstantValue__81_CAST_mul46_fixp + (-1)*C4_ConstantValue__81_CAST_mul46<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__81_CAST_mul46
solver.Add( + (1)*ConstantValue__81_fixp + (1)*ConstantValue__81_CAST_mul46_double + (-1)*C5_ConstantValue__81_CAST_mul46<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__81_CAST_mul46
solver.Add( + (1)*ConstantValue__81_double + (1)*ConstantValue__81_CAST_mul46_fixp + (-1)*C6_ConstantValue__81_CAST_mul46<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__81_CAST_mul46
solver.Add( + (1)*ConstantValue__81_float + (1)*ConstantValue__81_CAST_mul46_double + (-1)*C7_ConstantValue__81_CAST_mul46<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__81_CAST_mul46
solver.Add( + (1)*ConstantValue__81_double + (1)*ConstantValue__81_CAST_mul46_float + (-1)*C8_ConstantValue__81_CAST_mul46<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__81_CAST_mul46



#Stuff for   %mul46 = fmul double %conv45, 0x3FF548CDD6F42943, !taffo.info !117, !taffo.initweight !30, !taffo.constinfo !119
_Z4CNDFf_3_14_mul46_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul46_fixbits')
_Z4CNDFf_3_14_mul46_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul46_fixp')
_Z4CNDFf_3_14_mul46_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul46_float')
_Z4CNDFf_3_14_mul46_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul46_double')
_Z4CNDFf_3_14_mul46_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul46_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_enob + (-1)*_Z4CNDFf_3_14_mul46_fixbits + (10000)*_Z4CNDFf_3_14_mul46_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_enob + (10000)*_Z4CNDFf_3_14_mul46_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_enob + (10000)*_Z4CNDFf_3_14_mul46_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_fixbits + (-10000)*_Z4CNDFf_3_14_mul46_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul46_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_fixp + (1)*_Z4CNDFf_3_14_mul46_float + (1)*_Z4CNDFf_3_14_mul46_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_fixbits + (-10000)*_Z4CNDFf_3_14_mul46_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixp + (-1)*ConstantValue__81_CAST_mul46_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_float + (-1)*ConstantValue__81_CAST_mul46_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_double + (-1)*ConstantValue__81_CAST_mul46_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_fixp + (-1)*_Z4CNDFf_3_14_mul46_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_float + (-1)*_Z4CNDFf_3_14_mul46_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_mul30_CAST_mul46_double + (-1)*_Z4CNDFf_3_14_mul46_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul46_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul46_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul46_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_enob + (-1)*ConstantValue__79_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_enob + (-1)*_Z4CNDFf_3_14_mul30_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul46_enob_2<=0)    #Enob: propagation in product 2



#Constraint for cast for   %add48 = fadd float %add44, %conv47, !taffo.info !124, !taffo.initweight !23
_Z4CNDFf_3_14_add44_CAST_add48_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add44_CAST_add48_fixbits')
_Z4CNDFf_3_14_add44_CAST_add48_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add44_CAST_add48_fixp')
_Z4CNDFf_3_14_add44_CAST_add48_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add44_CAST_add48_float')
_Z4CNDFf_3_14_add44_CAST_add48_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add44_CAST_add48_double')
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixp + (1)*_Z4CNDFf_3_14_add44_CAST_add48_float + (1)*_Z4CNDFf_3_14_add44_CAST_add48_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixbits + (-10000)*_Z4CNDFf_3_14_add44_CAST_add48_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_add44_CAST_add48')
C2__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_add44_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_3_14_add44_fixbits + (-1)*_Z4CNDFf_3_14_add44_CAST_add48_fixbits + (-10000)*C1__Z4CNDFf_3_14_add44_CAST_add48<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_add44_fixbits + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixbits + (-10000)*C2__Z4CNDFf_3_14_add44_CAST_add48<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_add44_CAST_add48
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_add44_CAST_add48
C3__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_add44_CAST_add48')
C4__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_add44_CAST_add48')
C5__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_add44_CAST_add48')
C6__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_add44_CAST_add48')
C7__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_add44_CAST_add48')
C8__Z4CNDFf_3_14_add44_CAST_add48 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_add44_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_3_14_add44_fixp + (1)*_Z4CNDFf_3_14_add44_CAST_add48_float + (-1)*C3__Z4CNDFf_3_14_add44_CAST_add48<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_add44_float + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixp + (-1)*C4__Z4CNDFf_3_14_add44_CAST_add48<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_add44_fixp + (1)*_Z4CNDFf_3_14_add44_CAST_add48_double + (-1)*C5__Z4CNDFf_3_14_add44_CAST_add48<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_add44_double + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixp + (-1)*C6__Z4CNDFf_3_14_add44_CAST_add48<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_add44_float + (1)*_Z4CNDFf_3_14_add44_CAST_add48_double + (-1)*C7__Z4CNDFf_3_14_add44_CAST_add48<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_add44_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_add44_double + (1)*_Z4CNDFf_3_14_add44_CAST_add48_float + (-1)*C8__Z4CNDFf_3_14_add44_CAST_add48<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_add44_CAST_add48



#Constraint for cast for   %add48 = fadd float %add44, %conv47, !taffo.info !124, !taffo.initweight !23
_Z4CNDFf_3_14_mul46_CAST_add48_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul46_CAST_add48_fixbits')
_Z4CNDFf_3_14_mul46_CAST_add48_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul46_CAST_add48_fixp')
_Z4CNDFf_3_14_mul46_CAST_add48_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul46_CAST_add48_float')
_Z4CNDFf_3_14_mul46_CAST_add48_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul46_CAST_add48_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixp + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_float + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixbits + (-10000)*_Z4CNDFf_3_14_mul46_CAST_add48_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul46_CAST_add48')
C2__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul46_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_fixbits + (-1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul46_CAST_add48<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul46_fixbits + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul46_CAST_add48<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul46_CAST_add48
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul46_CAST_add48
C3__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul46_CAST_add48')
C4__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul46_CAST_add48')
C5__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul46_CAST_add48')
C6__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul46_CAST_add48')
C7__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul46_CAST_add48')
C8__Z4CNDFf_3_14_mul46_CAST_add48 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul46_CAST_add48')
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_fixp + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_float + (-1)*C3__Z4CNDFf_3_14_mul46_CAST_add48<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_float + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixp + (-1)*C4__Z4CNDFf_3_14_mul46_CAST_add48<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_fixp + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_double + (-1)*C5__Z4CNDFf_3_14_mul46_CAST_add48<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_double + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixp + (-1)*C6__Z4CNDFf_3_14_mul46_CAST_add48<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_float + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_double + (-1)*C7__Z4CNDFf_3_14_mul46_CAST_add48<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul46_CAST_add48
solver.Add( + (1)*_Z4CNDFf_3_14_mul46_double + (1)*_Z4CNDFf_3_14_mul46_CAST_add48_float + (-1)*C8__Z4CNDFf_3_14_mul46_CAST_add48<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul46_CAST_add48



#Stuff for   %add48 = fadd float %add44, %conv47, !taffo.info !124, !taffo.initweight !23
_Z4CNDFf_3_14_add48_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add48_fixbits')
_Z4CNDFf_3_14_add48_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add48_fixp')
_Z4CNDFf_3_14_add48_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add48_float')
_Z4CNDFf_3_14_add48_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add48_double')
_Z4CNDFf_3_14_add48_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_add48_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_add48_enob + (-1)*_Z4CNDFf_3_14_add48_fixbits + (10000)*_Z4CNDFf_3_14_add48_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_add48_enob + (10000)*_Z4CNDFf_3_14_add48_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_add48_enob + (10000)*_Z4CNDFf_3_14_add48_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_add48_fixbits + (-10000)*_Z4CNDFf_3_14_add48_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_add48_enob
solver.Add( + (1)*_Z4CNDFf_3_14_add48_fixp + (1)*_Z4CNDFf_3_14_add48_float + (1)*_Z4CNDFf_3_14_add48_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_add48_fixbits + (-10000)*_Z4CNDFf_3_14_add48_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixp + (-1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_float + (-1)*_Z4CNDFf_3_14_mul46_CAST_add48_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_double + (-1)*_Z4CNDFf_3_14_mul46_CAST_add48_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixbits + (-1)*_Z4CNDFf_3_14_mul46_CAST_add48_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixp + (-1)*_Z4CNDFf_3_14_add48_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_float + (-1)*_Z4CNDFf_3_14_add48_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_double + (-1)*_Z4CNDFf_3_14_add48_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_add44_CAST_add48_fixbits + (-1)*_Z4CNDFf_3_14_add48_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_add48_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_add48_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_add48_double
solver.Add( + (1)*_Z4CNDFf_3_14_add48_enob + (-1)*_Z4CNDFf_3_14_add44_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_3_14_add48_enob + (-1)*_Z4CNDFf_3_14_mul46_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %add49 = fadd float %add48, %conv33, !taffo.info !126, !taffo.initweight !23
_Z4CNDFf_3_14_add48_CAST_add49_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add48_CAST_add49_fixbits')
_Z4CNDFf_3_14_add48_CAST_add49_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add48_CAST_add49_fixp')
_Z4CNDFf_3_14_add48_CAST_add49_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add48_CAST_add49_float')
_Z4CNDFf_3_14_add48_CAST_add49_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add48_CAST_add49_double')
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixp + (1)*_Z4CNDFf_3_14_add48_CAST_add49_float + (1)*_Z4CNDFf_3_14_add48_CAST_add49_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixbits + (-10000)*_Z4CNDFf_3_14_add48_CAST_add49_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_add48_CAST_add49')
C2__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_add48_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_3_14_add48_fixbits + (-1)*_Z4CNDFf_3_14_add48_CAST_add49_fixbits + (-10000)*C1__Z4CNDFf_3_14_add48_CAST_add49<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_add48_fixbits + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixbits + (-10000)*C2__Z4CNDFf_3_14_add48_CAST_add49<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_add48_CAST_add49
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_add48_CAST_add49
C3__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_add48_CAST_add49')
C4__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_add48_CAST_add49')
C5__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_add48_CAST_add49')
C6__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_add48_CAST_add49')
C7__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_add48_CAST_add49')
C8__Z4CNDFf_3_14_add48_CAST_add49 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_add48_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_3_14_add48_fixp + (1)*_Z4CNDFf_3_14_add48_CAST_add49_float + (-1)*C3__Z4CNDFf_3_14_add48_CAST_add49<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_add48_float + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixp + (-1)*C4__Z4CNDFf_3_14_add48_CAST_add49<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_add48_fixp + (1)*_Z4CNDFf_3_14_add48_CAST_add49_double + (-1)*C5__Z4CNDFf_3_14_add48_CAST_add49<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_add48_double + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixp + (-1)*C6__Z4CNDFf_3_14_add48_CAST_add49<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_add48_float + (1)*_Z4CNDFf_3_14_add48_CAST_add49_double + (-1)*C7__Z4CNDFf_3_14_add48_CAST_add49<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_add48_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_add48_double + (1)*_Z4CNDFf_3_14_add48_CAST_add49_float + (-1)*C8__Z4CNDFf_3_14_add48_CAST_add49<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_add48_CAST_add49



#Constraint for cast for   %add49 = fadd float %add48, %conv33, !taffo.info !126, !taffo.initweight !23
_Z4CNDFf_3_14_mul32_CAST_add49_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul32_CAST_add49_fixbits')
_Z4CNDFf_3_14_mul32_CAST_add49_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul32_CAST_add49_fixp')
_Z4CNDFf_3_14_mul32_CAST_add49_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul32_CAST_add49_float')
_Z4CNDFf_3_14_mul32_CAST_add49_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul32_CAST_add49_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixp + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_float + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixbits + (-10000)*_Z4CNDFf_3_14_mul32_CAST_add49_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul32_CAST_add49')
C2__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul32_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_fixbits + (-1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul32_CAST_add49<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul32_fixbits + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul32_CAST_add49<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul32_CAST_add49
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul32_CAST_add49
C3__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul32_CAST_add49')
C4__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul32_CAST_add49')
C5__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul32_CAST_add49')
C6__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul32_CAST_add49')
C7__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul32_CAST_add49')
C8__Z4CNDFf_3_14_mul32_CAST_add49 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul32_CAST_add49')
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_fixp + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_float + (-1)*C3__Z4CNDFf_3_14_mul32_CAST_add49<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_float + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixp + (-1)*C4__Z4CNDFf_3_14_mul32_CAST_add49<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_fixp + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_double + (-1)*C5__Z4CNDFf_3_14_mul32_CAST_add49<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_double + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixp + (-1)*C6__Z4CNDFf_3_14_mul32_CAST_add49<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_float + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_double + (-1)*C7__Z4CNDFf_3_14_mul32_CAST_add49<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul32_CAST_add49
solver.Add( + (1)*_Z4CNDFf_3_14_mul32_double + (1)*_Z4CNDFf_3_14_mul32_CAST_add49_float + (-1)*C8__Z4CNDFf_3_14_mul32_CAST_add49<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul32_CAST_add49



#Stuff for   %add49 = fadd float %add48, %conv33, !taffo.info !126, !taffo.initweight !23
_Z4CNDFf_3_14_add49_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add49_fixbits')
_Z4CNDFf_3_14_add49_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add49_fixp')
_Z4CNDFf_3_14_add49_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add49_float')
_Z4CNDFf_3_14_add49_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add49_double')
_Z4CNDFf_3_14_add49_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_add49_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_add49_enob + (-1)*_Z4CNDFf_3_14_add49_fixbits + (10000)*_Z4CNDFf_3_14_add49_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_add49_enob + (10000)*_Z4CNDFf_3_14_add49_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_add49_enob + (10000)*_Z4CNDFf_3_14_add49_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_add49_fixbits + (-10000)*_Z4CNDFf_3_14_add49_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_add49_enob
solver.Add( + (1)*_Z4CNDFf_3_14_add49_fixp + (1)*_Z4CNDFf_3_14_add49_float + (1)*_Z4CNDFf_3_14_add49_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_add49_fixbits + (-10000)*_Z4CNDFf_3_14_add49_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixp + (-1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_float + (-1)*_Z4CNDFf_3_14_mul32_CAST_add49_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_double + (-1)*_Z4CNDFf_3_14_mul32_CAST_add49_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixbits + (-1)*_Z4CNDFf_3_14_mul32_CAST_add49_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixp + (-1)*_Z4CNDFf_3_14_add49_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_float + (-1)*_Z4CNDFf_3_14_add49_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_double + (-1)*_Z4CNDFf_3_14_add49_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_add48_CAST_add49_fixbits + (-1)*_Z4CNDFf_3_14_add49_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_add49_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_add49_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_add49_double
solver.Add( + (1)*_Z4CNDFf_3_14_add49_enob + (-1)*_Z4CNDFf_3_14_add48_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*_Z4CNDFf_3_14_add49_enob + (-1)*_Z4CNDFf_3_14_mul32_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %mul50 = fmul float %add49, %conv19, !taffo.info !128, !taffo.initweight !23
_Z4CNDFf_3_14_add49_CAST_mul50_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_add49_CAST_mul50_fixbits')
_Z4CNDFf_3_14_add49_CAST_mul50_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add49_CAST_mul50_fixp')
_Z4CNDFf_3_14_add49_CAST_mul50_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add49_CAST_mul50_float')
_Z4CNDFf_3_14_add49_CAST_mul50_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_add49_CAST_mul50_double')
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixp + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_float + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixbits + (-10000)*_Z4CNDFf_3_14_add49_CAST_mul50_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_add49_CAST_mul50')
C2__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_add49_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_3_14_add49_fixbits + (-1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixbits + (-10000)*C1__Z4CNDFf_3_14_add49_CAST_mul50<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_add49_fixbits + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixbits + (-10000)*C2__Z4CNDFf_3_14_add49_CAST_mul50<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_add49_CAST_mul50
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_add49_CAST_mul50
C3__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_add49_CAST_mul50')
C4__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_add49_CAST_mul50')
C5__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_add49_CAST_mul50')
C6__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_add49_CAST_mul50')
C7__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_add49_CAST_mul50')
C8__Z4CNDFf_3_14_add49_CAST_mul50 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_add49_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_3_14_add49_fixp + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_float + (-1)*C3__Z4CNDFf_3_14_add49_CAST_mul50<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_add49_float + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixp + (-1)*C4__Z4CNDFf_3_14_add49_CAST_mul50<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_add49_fixp + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_double + (-1)*C5__Z4CNDFf_3_14_add49_CAST_mul50<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_add49_double + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixp + (-1)*C6__Z4CNDFf_3_14_add49_CAST_mul50<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_add49_float + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_double + (-1)*C7__Z4CNDFf_3_14_add49_CAST_mul50<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_add49_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_add49_double + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_float + (-1)*C8__Z4CNDFf_3_14_add49_CAST_mul50<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_add49_CAST_mul50



#Constraint for cast for   %mul50 = fmul float %add49, %conv19, !taffo.info !128, !taffo.initweight !23
_Z4CNDFf_3_14_mul18_CAST_mul50_fixbits = solver.IntVar(0, 31, '_Z4CNDFf_3_14_mul18_CAST_mul50_fixbits')
_Z4CNDFf_3_14_mul18_CAST_mul50_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul18_CAST_mul50_fixp')
_Z4CNDFf_3_14_mul18_CAST_mul50_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul18_CAST_mul50_float')
_Z4CNDFf_3_14_mul18_CAST_mul50_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul18_CAST_mul50_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixp + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_float + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixbits + (-10000)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul18_CAST_mul50')
C2__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul18_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_fixbits + (-1)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul18_CAST_mul50<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul18_fixbits + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul18_CAST_mul50<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul18_CAST_mul50
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul18_CAST_mul50
C3__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul18_CAST_mul50')
C4__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul18_CAST_mul50')
C5__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul18_CAST_mul50')
C6__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul18_CAST_mul50')
C7__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul18_CAST_mul50')
C8__Z4CNDFf_3_14_mul18_CAST_mul50 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul18_CAST_mul50')
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_fixp + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_float + (-1)*C3__Z4CNDFf_3_14_mul18_CAST_mul50<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_float + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixp + (-1)*C4__Z4CNDFf_3_14_mul18_CAST_mul50<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_fixp + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_double + (-1)*C5__Z4CNDFf_3_14_mul18_CAST_mul50<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_double + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixp + (-1)*C6__Z4CNDFf_3_14_mul18_CAST_mul50<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_float + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_double + (-1)*C7__Z4CNDFf_3_14_mul18_CAST_mul50<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul18_CAST_mul50
solver.Add( + (1)*_Z4CNDFf_3_14_mul18_double + (1)*_Z4CNDFf_3_14_mul18_CAST_mul50_float + (-1)*C8__Z4CNDFf_3_14_mul18_CAST_mul50<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul18_CAST_mul50



#Stuff for   %mul50 = fmul float %add49, %conv19, !taffo.info !128, !taffo.initweight !23
_Z4CNDFf_3_14_mul50_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul50_fixbits')
_Z4CNDFf_3_14_mul50_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul50_fixp')
_Z4CNDFf_3_14_mul50_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul50_float')
_Z4CNDFf_3_14_mul50_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul50_double')
_Z4CNDFf_3_14_mul50_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_mul50_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_enob + (-1)*_Z4CNDFf_3_14_mul50_fixbits + (10000)*_Z4CNDFf_3_14_mul50_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_enob + (10000)*_Z4CNDFf_3_14_mul50_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_enob + (10000)*_Z4CNDFf_3_14_mul50_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_fixbits + (-10000)*_Z4CNDFf_3_14_mul50_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_mul50_enob
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_fixp + (1)*_Z4CNDFf_3_14_mul50_float + (1)*_Z4CNDFf_3_14_mul50_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_fixbits + (-10000)*_Z4CNDFf_3_14_mul50_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixp + (-1)*_Z4CNDFf_3_14_mul18_CAST_mul50_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_float + (-1)*_Z4CNDFf_3_14_mul18_CAST_mul50_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_double + (-1)*_Z4CNDFf_3_14_mul18_CAST_mul50_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_fixp + (-1)*_Z4CNDFf_3_14_mul50_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_float + (-1)*_Z4CNDFf_3_14_mul50_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_add49_CAST_mul50_double + (-1)*_Z4CNDFf_3_14_mul50_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z4CNDFf_3_14_mul50_fixp
mathCostObj +=  + (3.34669)*_Z4CNDFf_3_14_mul50_float
mathCostObj +=  + (4.14035)*_Z4CNDFf_3_14_mul50_double
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_1')
_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_2 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_2')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_1 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_enob + (-1)*_Z4CNDFf_3_14_mul18_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_enob + (-1)*_Z4CNDFf_3_14_add49_enob + (-10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_mul50_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for double 1.000000e+00
ConstantValue__82_fixbits = solver.IntVar(0, 31, 'ConstantValue__82_fixbits')
ConstantValue__82_fixp = solver.IntVar(0, 1, 'ConstantValue__82_fixp')
ConstantValue__82_float = solver.IntVar(0, 1, 'ConstantValue__82_float')
ConstantValue__82_double = solver.IntVar(0, 1, 'ConstantValue__82_double')
ConstantValue__82_enob = solver.IntVar(-10000, 10000, 'ConstantValue__82_enob')
solver.Add( + (1)*ConstantValue__82_enob + (-1)*ConstantValue__82_fixbits + (10000)*ConstantValue__82_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__82_enob + (10000)*ConstantValue__82_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__82_enob + (10000)*ConstantValue__82_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__82_fixbits + (-10000)*ConstantValue__82_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__82_fixp + (1)*ConstantValue__82_float + (1)*ConstantValue__82_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__82_fixbits + (-10000)*ConstantValue__82_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__83_fixbits = solver.IntVar(0, 31, 'ConstantValue__83_fixbits')
ConstantValue__83_fixp = solver.IntVar(0, 1, 'ConstantValue__83_fixp')
ConstantValue__83_float = solver.IntVar(0, 1, 'ConstantValue__83_float')
ConstantValue__83_double = solver.IntVar(0, 1, 'ConstantValue__83_double')
ConstantValue__83_enob = solver.IntVar(-10000, 10000, 'ConstantValue__83_enob')
solver.Add( + (1)*ConstantValue__83_enob + (-1)*ConstantValue__83_fixbits + (10000)*ConstantValue__83_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__83_enob + (10000)*ConstantValue__83_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__83_enob + (10000)*ConstantValue__83_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__83_fixbits + (-10000)*ConstantValue__83_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__83_fixp + (1)*ConstantValue__83_float + (1)*ConstantValue__83_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__83_fixbits + (-10000)*ConstantValue__83_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__84_fixbits = solver.IntVar(0, 31, 'ConstantValue__84_fixbits')
ConstantValue__84_fixp = solver.IntVar(0, 1, 'ConstantValue__84_fixp')
ConstantValue__84_float = solver.IntVar(0, 1, 'ConstantValue__84_float')
ConstantValue__84_double = solver.IntVar(0, 1, 'ConstantValue__84_double')
ConstantValue__84_enob = solver.IntVar(-10000, 10000, 'ConstantValue__84_enob')
solver.Add( + (1)*ConstantValue__84_enob + (-1)*ConstantValue__84_fixbits + (10000)*ConstantValue__84_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__84_enob + (10000)*ConstantValue__84_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__84_enob + (10000)*ConstantValue__84_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__84_fixbits + (-10000)*ConstantValue__84_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__84_fixp + (1)*ConstantValue__84_float + (1)*ConstantValue__84_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__84_fixbits + (-10000)*ConstantValue__84_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub52 = fsub double 1.000000e+00, %conv51, !taffo.info !130, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__84_CAST_sub52_fixbits = solver.IntVar(0, 31, 'ConstantValue__84_CAST_sub52_fixbits')
ConstantValue__84_CAST_sub52_fixp = solver.IntVar(0, 1, 'ConstantValue__84_CAST_sub52_fixp')
ConstantValue__84_CAST_sub52_float = solver.IntVar(0, 1, 'ConstantValue__84_CAST_sub52_float')
ConstantValue__84_CAST_sub52_double = solver.IntVar(0, 1, 'ConstantValue__84_CAST_sub52_double')
solver.Add( + (1)*ConstantValue__84_CAST_sub52_fixp + (1)*ConstantValue__84_CAST_sub52_float + (1)*ConstantValue__84_CAST_sub52_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__84_CAST_sub52_fixbits + (-10000)*ConstantValue__84_CAST_sub52_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C1_ConstantValue__84_CAST_sub52')
C2_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C2_ConstantValue__84_CAST_sub52')
solver.Add( + (1)*ConstantValue__84_fixbits + (-1)*ConstantValue__84_CAST_sub52_fixbits + (-10000)*C1_ConstantValue__84_CAST_sub52<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__84_fixbits + (1)*ConstantValue__84_CAST_sub52_fixbits + (-10000)*C2_ConstantValue__84_CAST_sub52<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__84_CAST_sub52
castCostObj +=  + (1.13006)*C2_ConstantValue__84_CAST_sub52
C3_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C3_ConstantValue__84_CAST_sub52')
C4_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C4_ConstantValue__84_CAST_sub52')
C5_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C5_ConstantValue__84_CAST_sub52')
C6_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C6_ConstantValue__84_CAST_sub52')
C7_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C7_ConstantValue__84_CAST_sub52')
C8_ConstantValue__84_CAST_sub52 = solver.IntVar(0, 1, 'C8_ConstantValue__84_CAST_sub52')
solver.Add( + (1)*ConstantValue__84_fixp + (1)*ConstantValue__84_CAST_sub52_float + (-1)*C3_ConstantValue__84_CAST_sub52<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__84_CAST_sub52
solver.Add( + (1)*ConstantValue__84_float + (1)*ConstantValue__84_CAST_sub52_fixp + (-1)*C4_ConstantValue__84_CAST_sub52<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__84_CAST_sub52
solver.Add( + (1)*ConstantValue__84_fixp + (1)*ConstantValue__84_CAST_sub52_double + (-1)*C5_ConstantValue__84_CAST_sub52<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__84_CAST_sub52
solver.Add( + (1)*ConstantValue__84_double + (1)*ConstantValue__84_CAST_sub52_fixp + (-1)*C6_ConstantValue__84_CAST_sub52<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__84_CAST_sub52
solver.Add( + (1)*ConstantValue__84_float + (1)*ConstantValue__84_CAST_sub52_double + (-1)*C7_ConstantValue__84_CAST_sub52<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__84_CAST_sub52
solver.Add( + (1)*ConstantValue__84_double + (1)*ConstantValue__84_CAST_sub52_float + (-1)*C8_ConstantValue__84_CAST_sub52<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__84_CAST_sub52



#Constraint for cast for   %sub52 = fsub double 1.000000e+00, %conv51, !taffo.info !130, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_mul50_CAST_sub52_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_mul50_CAST_sub52_fixbits')
_Z4CNDFf_3_14_mul50_CAST_sub52_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul50_CAST_sub52_fixp')
_Z4CNDFf_3_14_mul50_CAST_sub52_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul50_CAST_sub52_float')
_Z4CNDFf_3_14_mul50_CAST_sub52_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_mul50_CAST_sub52_double')
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixp + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_float + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixbits + (-10000)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_mul50_CAST_sub52')
C2__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_mul50_CAST_sub52')
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_fixbits + (-1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixbits + (-10000)*C1__Z4CNDFf_3_14_mul50_CAST_sub52<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_mul50_fixbits + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixbits + (-10000)*C2__Z4CNDFf_3_14_mul50_CAST_sub52<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_mul50_CAST_sub52
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_mul50_CAST_sub52
C3__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_mul50_CAST_sub52')
C4__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_mul50_CAST_sub52')
C5__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_mul50_CAST_sub52')
C6__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_mul50_CAST_sub52')
C7__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_mul50_CAST_sub52')
C8__Z4CNDFf_3_14_mul50_CAST_sub52 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_mul50_CAST_sub52')
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_fixp + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_float + (-1)*C3__Z4CNDFf_3_14_mul50_CAST_sub52<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_float + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixp + (-1)*C4__Z4CNDFf_3_14_mul50_CAST_sub52<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_fixp + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_double + (-1)*C5__Z4CNDFf_3_14_mul50_CAST_sub52<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_double + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixp + (-1)*C6__Z4CNDFf_3_14_mul50_CAST_sub52<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_float + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_double + (-1)*C7__Z4CNDFf_3_14_mul50_CAST_sub52<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_mul50_CAST_sub52
solver.Add( + (1)*_Z4CNDFf_3_14_mul50_double + (1)*_Z4CNDFf_3_14_mul50_CAST_sub52_float + (-1)*C8__Z4CNDFf_3_14_mul50_CAST_sub52<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_mul50_CAST_sub52



#Stuff for   %sub52 = fsub double 1.000000e+00, %conv51, !taffo.info !130, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_sub52_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_sub52_fixbits')
_Z4CNDFf_3_14_sub52_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_fixp')
_Z4CNDFf_3_14_sub52_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_float')
_Z4CNDFf_3_14_sub52_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_double')
_Z4CNDFf_3_14_sub52_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_sub52_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_enob + (-1)*_Z4CNDFf_3_14_sub52_fixbits + (10000)*_Z4CNDFf_3_14_sub52_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_enob + (10000)*_Z4CNDFf_3_14_sub52_float<=10024)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_enob + (10000)*_Z4CNDFf_3_14_sub52_double<=10053)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixbits + (-10000)*_Z4CNDFf_3_14_sub52_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_sub52_enob
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixp + (1)*_Z4CNDFf_3_14_sub52_float + (1)*_Z4CNDFf_3_14_sub52_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixbits + (-10000)*_Z4CNDFf_3_14_sub52_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__84_CAST_sub52_fixp + (-1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__84_CAST_sub52_float + (-1)*_Z4CNDFf_3_14_mul50_CAST_sub52_float==0)    #float equality
solver.Add( + (1)*ConstantValue__84_CAST_sub52_double + (-1)*_Z4CNDFf_3_14_mul50_CAST_sub52_double==0)    #double equality
solver.Add( + (1)*ConstantValue__84_CAST_sub52_fixbits + (-1)*_Z4CNDFf_3_14_mul50_CAST_sub52_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__84_CAST_sub52_fixp + (-1)*_Z4CNDFf_3_14_sub52_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__84_CAST_sub52_float + (-1)*_Z4CNDFf_3_14_sub52_float==0)    #float equality
solver.Add( + (1)*ConstantValue__84_CAST_sub52_double + (-1)*_Z4CNDFf_3_14_sub52_double==0)    #double equality
solver.Add( + (1)*ConstantValue__84_CAST_sub52_fixbits + (-1)*_Z4CNDFf_3_14_sub52_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_sub52_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_sub52_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_sub52_double
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_enob + (-1)*ConstantValue__82_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_enob + (-1)*_Z4CNDFf_3_14_mul50_enob<=0)    #Enob propagation in sub second addend



#Stuff for double 1.000000e+00
ConstantValue__85_fixbits = solver.IntVar(0, 31, 'ConstantValue__85_fixbits')
ConstantValue__85_fixp = solver.IntVar(0, 1, 'ConstantValue__85_fixp')
ConstantValue__85_float = solver.IntVar(0, 1, 'ConstantValue__85_float')
ConstantValue__85_double = solver.IntVar(0, 1, 'ConstantValue__85_double')
ConstantValue__85_enob = solver.IntVar(-10000, 10000, 'ConstantValue__85_enob')
solver.Add( + (1)*ConstantValue__85_enob + (-1)*ConstantValue__85_fixbits + (10000)*ConstantValue__85_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__85_enob + (10000)*ConstantValue__85_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__85_enob + (10000)*ConstantValue__85_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__85_fixbits + (-10000)*ConstantValue__85_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__85_fixp + (1)*ConstantValue__85_float + (1)*ConstantValue__85_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__85_fixbits + (-10000)*ConstantValue__85_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__86_fixbits = solver.IntVar(0, 31, 'ConstantValue__86_fixbits')
ConstantValue__86_fixp = solver.IntVar(0, 1, 'ConstantValue__86_fixp')
ConstantValue__86_float = solver.IntVar(0, 1, 'ConstantValue__86_float')
ConstantValue__86_double = solver.IntVar(0, 1, 'ConstantValue__86_double')
ConstantValue__86_enob = solver.IntVar(-10000, 10000, 'ConstantValue__86_enob')
solver.Add( + (1)*ConstantValue__86_enob + (-1)*ConstantValue__86_fixbits + (10000)*ConstantValue__86_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__86_enob + (10000)*ConstantValue__86_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__86_enob + (10000)*ConstantValue__86_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__86_fixbits + (-10000)*ConstantValue__86_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__86_fixp + (1)*ConstantValue__86_float + (1)*ConstantValue__86_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__86_fixbits + (-10000)*ConstantValue__86_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__87_fixbits = solver.IntVar(0, 31, 'ConstantValue__87_fixbits')
ConstantValue__87_fixp = solver.IntVar(0, 1, 'ConstantValue__87_fixp')
ConstantValue__87_float = solver.IntVar(0, 1, 'ConstantValue__87_float')
ConstantValue__87_double = solver.IntVar(0, 1, 'ConstantValue__87_double')
ConstantValue__87_enob = solver.IntVar(-10000, 10000, 'ConstantValue__87_enob')
solver.Add( + (1)*ConstantValue__87_enob + (-1)*ConstantValue__87_fixbits + (10000)*ConstantValue__87_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__87_enob + (10000)*ConstantValue__87_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__87_enob + (10000)*ConstantValue__87_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__87_fixbits + (-10000)*ConstantValue__87_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__87_fixp + (1)*ConstantValue__87_float + (1)*ConstantValue__87_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__87_fixbits + (-10000)*ConstantValue__87_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub56 = fsub double 1.000000e+00, %conv55, !taffo.info !134, !taffo.initweight !30, !taffo.constinfo !70
ConstantValue__87_CAST_sub56_fixbits = solver.IntVar(0, 31, 'ConstantValue__87_CAST_sub56_fixbits')
ConstantValue__87_CAST_sub56_fixp = solver.IntVar(0, 1, 'ConstantValue__87_CAST_sub56_fixp')
ConstantValue__87_CAST_sub56_float = solver.IntVar(0, 1, 'ConstantValue__87_CAST_sub56_float')
ConstantValue__87_CAST_sub56_double = solver.IntVar(0, 1, 'ConstantValue__87_CAST_sub56_double')
solver.Add( + (1)*ConstantValue__87_CAST_sub56_fixp + (1)*ConstantValue__87_CAST_sub56_float + (1)*ConstantValue__87_CAST_sub56_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__87_CAST_sub56_fixbits + (-10000)*ConstantValue__87_CAST_sub56_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C1_ConstantValue__87_CAST_sub56')
C2_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C2_ConstantValue__87_CAST_sub56')
solver.Add( + (1)*ConstantValue__87_fixbits + (-1)*ConstantValue__87_CAST_sub56_fixbits + (-10000)*C1_ConstantValue__87_CAST_sub56<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__87_fixbits + (1)*ConstantValue__87_CAST_sub56_fixbits + (-10000)*C2_ConstantValue__87_CAST_sub56<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__87_CAST_sub56
castCostObj +=  + (1.13006)*C2_ConstantValue__87_CAST_sub56
C3_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C3_ConstantValue__87_CAST_sub56')
C4_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C4_ConstantValue__87_CAST_sub56')
C5_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C5_ConstantValue__87_CAST_sub56')
C6_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C6_ConstantValue__87_CAST_sub56')
C7_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C7_ConstantValue__87_CAST_sub56')
C8_ConstantValue__87_CAST_sub56 = solver.IntVar(0, 1, 'C8_ConstantValue__87_CAST_sub56')
solver.Add( + (1)*ConstantValue__87_fixp + (1)*ConstantValue__87_CAST_sub56_float + (-1)*C3_ConstantValue__87_CAST_sub56<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__87_CAST_sub56
solver.Add( + (1)*ConstantValue__87_float + (1)*ConstantValue__87_CAST_sub56_fixp + (-1)*C4_ConstantValue__87_CAST_sub56<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__87_CAST_sub56
solver.Add( + (1)*ConstantValue__87_fixp + (1)*ConstantValue__87_CAST_sub56_double + (-1)*C5_ConstantValue__87_CAST_sub56<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__87_CAST_sub56
solver.Add( + (1)*ConstantValue__87_double + (1)*ConstantValue__87_CAST_sub56_fixp + (-1)*C6_ConstantValue__87_CAST_sub56<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__87_CAST_sub56
solver.Add( + (1)*ConstantValue__87_float + (1)*ConstantValue__87_CAST_sub56_double + (-1)*C7_ConstantValue__87_CAST_sub56<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__87_CAST_sub56
solver.Add( + (1)*ConstantValue__87_double + (1)*ConstantValue__87_CAST_sub56_float + (-1)*C8_ConstantValue__87_CAST_sub56<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__87_CAST_sub56



#Constraint for cast for   %sub56 = fsub double 1.000000e+00, %conv55, !taffo.info !134, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_sub52_CAST_sub56_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_sub52_CAST_sub56_fixbits')
_Z4CNDFf_3_14_sub52_CAST_sub56_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_CAST_sub56_fixp')
_Z4CNDFf_3_14_sub52_CAST_sub56_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_CAST_sub56_float')
_Z4CNDFf_3_14_sub52_CAST_sub56_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_CAST_sub56_double')
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixp + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_float + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixbits + (-10000)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_sub52_CAST_sub56')
C2__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_sub52_CAST_sub56')
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixbits + (-1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixbits + (-10000)*C1__Z4CNDFf_3_14_sub52_CAST_sub56<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_sub52_fixbits + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixbits + (-10000)*C2__Z4CNDFf_3_14_sub52_CAST_sub56<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_sub52_CAST_sub56
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_sub52_CAST_sub56
C3__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_sub52_CAST_sub56')
C4__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_sub52_CAST_sub56')
C5__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_sub52_CAST_sub56')
C6__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_sub52_CAST_sub56')
C7__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_sub52_CAST_sub56')
C8__Z4CNDFf_3_14_sub52_CAST_sub56 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_sub52_CAST_sub56')
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixp + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_float + (-1)*C3__Z4CNDFf_3_14_sub52_CAST_sub56<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_float + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixp + (-1)*C4__Z4CNDFf_3_14_sub52_CAST_sub56<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixp + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_double + (-1)*C5__Z4CNDFf_3_14_sub52_CAST_sub56<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_double + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixp + (-1)*C6__Z4CNDFf_3_14_sub52_CAST_sub56<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_float + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_double + (-1)*C7__Z4CNDFf_3_14_sub52_CAST_sub56<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_sub52_CAST_sub56
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_double + (1)*_Z4CNDFf_3_14_sub52_CAST_sub56_float + (-1)*C8__Z4CNDFf_3_14_sub52_CAST_sub56<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_sub52_CAST_sub56



#Stuff for   %sub56 = fsub double 1.000000e+00, %conv55, !taffo.info !134, !taffo.initweight !30, !taffo.constinfo !70
_Z4CNDFf_3_14_sub56_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_sub56_fixbits')
_Z4CNDFf_3_14_sub56_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub56_fixp')
_Z4CNDFf_3_14_sub56_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub56_float')
_Z4CNDFf_3_14_sub56_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub56_double')
_Z4CNDFf_3_14_sub56_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_sub56_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_enob + (-1)*_Z4CNDFf_3_14_sub56_fixbits + (10000)*_Z4CNDFf_3_14_sub56_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_enob + (10000)*_Z4CNDFf_3_14_sub56_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_enob + (10000)*_Z4CNDFf_3_14_sub56_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_fixbits + (-10000)*_Z4CNDFf_3_14_sub56_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_sub56_enob
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_fixp + (1)*_Z4CNDFf_3_14_sub56_float + (1)*_Z4CNDFf_3_14_sub56_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_fixbits + (-10000)*_Z4CNDFf_3_14_sub56_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__87_CAST_sub56_fixp + (-1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__87_CAST_sub56_float + (-1)*_Z4CNDFf_3_14_sub52_CAST_sub56_float==0)    #float equality
solver.Add( + (1)*ConstantValue__87_CAST_sub56_double + (-1)*_Z4CNDFf_3_14_sub52_CAST_sub56_double==0)    #double equality
solver.Add( + (1)*ConstantValue__87_CAST_sub56_fixbits + (-1)*_Z4CNDFf_3_14_sub52_CAST_sub56_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__87_CAST_sub56_fixp + (-1)*_Z4CNDFf_3_14_sub56_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__87_CAST_sub56_float + (-1)*_Z4CNDFf_3_14_sub56_float==0)    #float equality
solver.Add( + (1)*ConstantValue__87_CAST_sub56_double + (-1)*_Z4CNDFf_3_14_sub56_double==0)    #double equality
solver.Add( + (1)*ConstantValue__87_CAST_sub56_fixbits + (-1)*_Z4CNDFf_3_14_sub56_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z4CNDFf_3_14_sub56_fixp
mathCostObj +=  + (1.80596)*_Z4CNDFf_3_14_sub56_float
mathCostObj +=  + (2.15411)*_Z4CNDFf_3_14_sub56_double
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_enob + (-1)*ConstantValue__85_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_enob + (-1)*_Z4CNDFf_3_14_sub52_enob<=0)    #Enob propagation in sub second addend



#Stuff for   %OutputX.0 = phi float [ %conv57, %if.then54 ], [ %conv53, %if.end ], !taffo.info !136
_Z4CNDFf_3_14_OutputX_0_fixbits = solver.IntVar(0, 29, '_Z4CNDFf_3_14_OutputX_0_fixbits')
_Z4CNDFf_3_14_OutputX_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_OutputX_0_fixp')
_Z4CNDFf_3_14_OutputX_0_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_OutputX_0_float')
_Z4CNDFf_3_14_OutputX_0_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_OutputX_0_double')
_Z4CNDFf_3_14_OutputX_0_enob = solver.IntVar(-10000, 10000, '_Z4CNDFf_3_14_OutputX_0_enob')
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_enob + (-1)*_Z4CNDFf_3_14_OutputX_0_fixbits + (10000)*_Z4CNDFf_3_14_OutputX_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_enob + (10000)*_Z4CNDFf_3_14_OutputX_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_enob + (10000)*_Z4CNDFf_3_14_OutputX_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixbits + (-10000)*_Z4CNDFf_3_14_OutputX_0_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z4CNDFf_3_14_OutputX_0_enob
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixp + (1)*_Z4CNDFf_3_14_OutputX_0_float + (1)*_Z4CNDFf_3_14_OutputX_0_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixbits + (-10000)*_Z4CNDFf_3_14_OutputX_0_fixp<=0)    #If not fix, frac part to zero
_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_0 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_0')
_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_1 = solver.IntVar(0, 1, '_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_1')
solver.Add( + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_0 + (1)*_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %OutputX.0 = phi float [ %conv57, %if.then54 ], [ %conv53, %if.end ], !taffo.info !136
_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixbits')
_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixp')
_Z4CNDFf_3_14_sub56_CAST_OutputX_0_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub56_CAST_OutputX_0_float')
_Z4CNDFf_3_14_sub56_CAST_OutputX_0_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub56_CAST_OutputX_0_double')
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixp + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_float + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixbits + (-10000)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
C2__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_fixbits + (-1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixbits + (-10000)*C1__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_sub56_fixbits + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixbits + (-10000)*C2__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_sub56_CAST_OutputX_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_sub56_CAST_OutputX_0
C3__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
C4__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
C5__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
C6__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
C7__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
C8__Z4CNDFf_3_14_sub56_CAST_OutputX_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_sub56_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_fixp + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_float + (-1)*C3__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_float + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixp + (-1)*C4__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_fixp + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_double + (-1)*C5__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_double + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixp + (-1)*C6__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_float + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_double + (-1)*C7__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub56_double + (1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_float + (-1)*C8__Z4CNDFf_3_14_sub56_CAST_OutputX_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_sub56_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixp + (-1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_float + (-1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_double + (-1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixbits + (-1)*_Z4CNDFf_3_14_sub56_CAST_OutputX_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_enob + (-1)*_Z4CNDFf_3_14_sub56_enob + (10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_0<=10000)    #Enob: forcing phi enob



#Constraint for cast for   %OutputX.0 = phi float [ %conv57, %if.then54 ], [ %conv53, %if.end ], !taffo.info !136
_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixbits = solver.IntVar(0, 30, '_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixbits')
_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixp')
_Z4CNDFf_3_14_sub52_CAST_OutputX_0_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_CAST_OutputX_0_float')
_Z4CNDFf_3_14_sub52_CAST_OutputX_0_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_sub52_CAST_OutputX_0_double')
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixp + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_float + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixbits + (-10000)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
C2__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixbits + (-1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixbits + (-10000)*C1__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_sub52_fixbits + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixbits + (-10000)*C2__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_sub52_CAST_OutputX_0
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_sub52_CAST_OutputX_0
C3__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
C4__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
C5__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
C6__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
C7__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
C8__Z4CNDFf_3_14_sub52_CAST_OutputX_0 = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_sub52_CAST_OutputX_0')
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixp + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_float + (-1)*C3__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_float + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixp + (-1)*C4__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_fixp + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_double + (-1)*C5__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_double + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixp + (-1)*C6__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_float + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_double + (-1)*C7__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_sub52_double + (1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_float + (-1)*C8__Z4CNDFf_3_14_sub52_CAST_OutputX_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_sub52_CAST_OutputX_0
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixp + (-1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_float + (-1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_float==0)    #float equality
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_double + (-1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_double==0)    #double equality
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixbits + (-1)*_Z4CNDFf_3_14_sub52_CAST_OutputX_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_enob + (-1)*_Z4CNDFf_3_14_sub52_enob + (10000)*_Z4CNDFf_3_14__Z4CNDFf_3_14_OutputX_0_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   ret float %OutputX.0, !taffo.info !31, !taffo.initweight !23
_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixbits = solver.IntVar(0, 29, '_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixbits')
_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixp = solver.IntVar(0, 1, '_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixp')
_Z4CNDFf_3_14_OutputX_0_CAST_ret_float = solver.IntVar(0, 1, '_Z4CNDFf_3_14_OutputX_0_CAST_ret_float')
_Z4CNDFf_3_14_OutputX_0_CAST_ret_double = solver.IntVar(0, 1, '_Z4CNDFf_3_14_OutputX_0_CAST_ret_double')
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixp + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_float + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixbits + (-10000)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C1__Z4CNDFf_3_14_OutputX_0_CAST_ret')
C2__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C2__Z4CNDFf_3_14_OutputX_0_CAST_ret')
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixbits + (-1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixbits + (-10000)*C1__Z4CNDFf_3_14_OutputX_0_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_Z4CNDFf_3_14_OutputX_0_fixbits + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixbits + (-10000)*C2__Z4CNDFf_3_14_OutputX_0_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z4CNDFf_3_14_OutputX_0_CAST_ret
castCostObj +=  + (1.13006)*C2__Z4CNDFf_3_14_OutputX_0_CAST_ret
C3__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C3__Z4CNDFf_3_14_OutputX_0_CAST_ret')
C4__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C4__Z4CNDFf_3_14_OutputX_0_CAST_ret')
C5__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C5__Z4CNDFf_3_14_OutputX_0_CAST_ret')
C6__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C6__Z4CNDFf_3_14_OutputX_0_CAST_ret')
C7__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C7__Z4CNDFf_3_14_OutputX_0_CAST_ret')
C8__Z4CNDFf_3_14_OutputX_0_CAST_ret = solver.IntVar(0, 1, 'C8__Z4CNDFf_3_14_OutputX_0_CAST_ret')
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixp + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_float + (-1)*C3__Z4CNDFf_3_14_OutputX_0_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z4CNDFf_3_14_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_float + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixp + (-1)*C4__Z4CNDFf_3_14_OutputX_0_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z4CNDFf_3_14_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_fixp + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_double + (-1)*C5__Z4CNDFf_3_14_OutputX_0_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z4CNDFf_3_14_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_double + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixp + (-1)*C6__Z4CNDFf_3_14_OutputX_0_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z4CNDFf_3_14_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_float + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_double + (-1)*C7__Z4CNDFf_3_14_OutputX_0_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__Z4CNDFf_3_14_OutputX_0_CAST_ret
solver.Add( + (1)*_Z4CNDFf_3_14_OutputX_0_double + (1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_float + (-1)*C8__Z4CNDFf_3_14_OutputX_0_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z4CNDFf_3_14_OutputX_0_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (-1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (-1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double + (-1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (-1)*_Z4CNDFf_3_14_OutputX_0_CAST_ret_fixbits==0)    #same fractional bit



#Stuff for double 1.000000e+00
ConstantValue__88_fixbits = solver.IntVar(0, 31, 'ConstantValue__88_fixbits')
ConstantValue__88_fixp = solver.IntVar(0, 1, 'ConstantValue__88_fixp')
ConstantValue__88_float = solver.IntVar(0, 1, 'ConstantValue__88_float')
ConstantValue__88_double = solver.IntVar(0, 1, 'ConstantValue__88_double')
ConstantValue__88_enob = solver.IntVar(-10000, 10000, 'ConstantValue__88_enob')
solver.Add( + (1)*ConstantValue__88_enob + (-1)*ConstantValue__88_fixbits + (10000)*ConstantValue__88_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__88_enob + (10000)*ConstantValue__88_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__88_enob + (10000)*ConstantValue__88_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__88_fixbits + (-10000)*ConstantValue__88_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__88_fixp + (1)*ConstantValue__88_float + (1)*ConstantValue__88_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__88_fixbits + (-10000)*ConstantValue__88_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store float %call34, float* %N1, align 4, !taffo.info !73, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store
solver.Add( + (1)*_Z9bs_threadPv_N1_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*_Z9bs_threadPv_N1_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_float==0)    #float equality
solver.Add( + (1)*_Z9bs_threadPv_N1_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_double==0)    #double equality
solver.Add( + (1)*_Z9bs_threadPv_N1_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
_Z9bs_threadPv_N1_enob_storeENOB = solver.IntVar(-10000, 10000, '_Z9bs_threadPv_N1_enob_storeENOB')
solver.Add( + (1)*_Z9bs_threadPv_N1_enob_storeENOB + (-1)*_Z9bs_threadPv_N1_fixbits + (10000)*_Z9bs_threadPv_N1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z9bs_threadPv_N1_enob_storeENOB + (10000)*_Z9bs_threadPv_N1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z9bs_threadPv_N1_enob_storeENOB + (10000)*_Z9bs_threadPv_N1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z9bs_threadPv_N1_enob_storeENOB + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob<=0)    #Enob constraint ENOB propagation in load/store



#Constraint for cast for   store float %call36, float* %N2, align 4, !taffo.info !73, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store
solver.Add( + (1)*_Z9bs_threadPv_N2_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*_Z9bs_threadPv_N2_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_float==0)    #float equality
solver.Add( + (1)*_Z9bs_threadPv_N2_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_double==0)    #double equality
solver.Add( + (1)*_Z9bs_threadPv_N2_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
_Z9bs_threadPv_N2_enob_storeENOB = solver.IntVar(-10000, 10000, '_Z9bs_threadPv_N2_enob_storeENOB')
solver.Add( + (1)*_Z9bs_threadPv_N2_enob_storeENOB + (-1)*_Z9bs_threadPv_N2_fixbits + (10000)*_Z9bs_threadPv_N2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z9bs_threadPv_N2_enob_storeENOB + (10000)*_Z9bs_threadPv_N2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z9bs_threadPv_N2_enob_storeENOB + (10000)*_Z9bs_threadPv_N2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z9bs_threadPv_N2_enob_storeENOB + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for float -0.000000e+00
ConstantValue__89_fixbits = solver.IntVar(0, 32, 'ConstantValue__89_fixbits')
ConstantValue__89_fixp = solver.IntVar(0, 1, 'ConstantValue__89_fixp')
ConstantValue__89_float = solver.IntVar(0, 1, 'ConstantValue__89_float')
ConstantValue__89_double = solver.IntVar(0, 1, 'ConstantValue__89_double')
ConstantValue__89_enob = solver.IntVar(-10000, 10000, 'ConstantValue__89_enob')
solver.Add( + (1)*ConstantValue__89_enob + (-1)*ConstantValue__89_fixbits + (10000)*ConstantValue__89_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__89_enob + (10000)*ConstantValue__89_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__89_enob + (10000)*ConstantValue__89_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__89_fixbits + (-10000)*ConstantValue__89_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__89_fixp + (1)*ConstantValue__89_float + (1)*ConstantValue__89_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__89_fixbits + (-10000)*ConstantValue__89_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -0.000000e+00
ConstantValue__90_fixbits = solver.IntVar(0, 32, 'ConstantValue__90_fixbits')
ConstantValue__90_fixp = solver.IntVar(0, 1, 'ConstantValue__90_fixp')
ConstantValue__90_float = solver.IntVar(0, 1, 'ConstantValue__90_float')
ConstantValue__90_double = solver.IntVar(0, 1, 'ConstantValue__90_double')
ConstantValue__90_enob = solver.IntVar(-10000, 10000, 'ConstantValue__90_enob')
solver.Add( + (1)*ConstantValue__90_enob + (-1)*ConstantValue__90_fixbits + (10000)*ConstantValue__90_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__90_enob + (10000)*ConstantValue__90_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__90_enob + (10000)*ConstantValue__90_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__90_fixbits + (-10000)*ConstantValue__90_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__90_fixp + (1)*ConstantValue__90_float + (1)*ConstantValue__90_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__90_fixbits + (-10000)*ConstantValue__90_fixp<=0)    #If not fix, frac part to zero



#Stuff for float -0.000000e+00
ConstantValue__91_fixbits = solver.IntVar(0, 32, 'ConstantValue__91_fixbits')
ConstantValue__91_fixp = solver.IntVar(0, 1, 'ConstantValue__91_fixp')
ConstantValue__91_float = solver.IntVar(0, 1, 'ConstantValue__91_float')
ConstantValue__91_double = solver.IntVar(0, 1, 'ConstantValue__91_double')
ConstantValue__91_enob = solver.IntVar(-10000, 10000, 'ConstantValue__91_enob')
solver.Add( + (1)*ConstantValue__91_enob + (-1)*ConstantValue__91_fixbits + (10000)*ConstantValue__91_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__91_enob + (10000)*ConstantValue__91_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__91_enob + (10000)*ConstantValue__91_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__91_fixbits + (-10000)*ConstantValue__91_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__91_fixp + (1)*ConstantValue__91_float + (1)*ConstantValue__91_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__91_fixbits + (-10000)*ConstantValue__91_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub41 = fsub float -0.000000e+00, %rate, !taffo.info !75, !taffo.initweight !39, !taffo.constinfo !77
ConstantValue__91_CAST_sub41_fixbits = solver.IntVar(0, 32, 'ConstantValue__91_CAST_sub41_fixbits')
ConstantValue__91_CAST_sub41_fixp = solver.IntVar(0, 1, 'ConstantValue__91_CAST_sub41_fixp')
ConstantValue__91_CAST_sub41_float = solver.IntVar(0, 1, 'ConstantValue__91_CAST_sub41_float')
ConstantValue__91_CAST_sub41_double = solver.IntVar(0, 1, 'ConstantValue__91_CAST_sub41_double')
solver.Add( + (1)*ConstantValue__91_CAST_sub41_fixp + (1)*ConstantValue__91_CAST_sub41_float + (1)*ConstantValue__91_CAST_sub41_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__91_CAST_sub41_fixbits + (-10000)*ConstantValue__91_CAST_sub41_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C1_ConstantValue__91_CAST_sub41')
C2_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C2_ConstantValue__91_CAST_sub41')
solver.Add( + (1)*ConstantValue__91_fixbits + (-1)*ConstantValue__91_CAST_sub41_fixbits + (-10000)*C1_ConstantValue__91_CAST_sub41<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__91_fixbits + (1)*ConstantValue__91_CAST_sub41_fixbits + (-10000)*C2_ConstantValue__91_CAST_sub41<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__91_CAST_sub41
castCostObj +=  + (1.13006)*C2_ConstantValue__91_CAST_sub41
C3_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C3_ConstantValue__91_CAST_sub41')
C4_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C4_ConstantValue__91_CAST_sub41')
C5_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C5_ConstantValue__91_CAST_sub41')
C6_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C6_ConstantValue__91_CAST_sub41')
C7_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C7_ConstantValue__91_CAST_sub41')
C8_ConstantValue__91_CAST_sub41 = solver.IntVar(0, 1, 'C8_ConstantValue__91_CAST_sub41')
solver.Add( + (1)*ConstantValue__91_fixp + (1)*ConstantValue__91_CAST_sub41_float + (-1)*C3_ConstantValue__91_CAST_sub41<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__91_CAST_sub41
solver.Add( + (1)*ConstantValue__91_float + (1)*ConstantValue__91_CAST_sub41_fixp + (-1)*C4_ConstantValue__91_CAST_sub41<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__91_CAST_sub41
solver.Add( + (1)*ConstantValue__91_fixp + (1)*ConstantValue__91_CAST_sub41_double + (-1)*C5_ConstantValue__91_CAST_sub41<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__91_CAST_sub41
solver.Add( + (1)*ConstantValue__91_double + (1)*ConstantValue__91_CAST_sub41_fixp + (-1)*C6_ConstantValue__91_CAST_sub41<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__91_CAST_sub41
solver.Add( + (1)*ConstantValue__91_float + (1)*ConstantValue__91_CAST_sub41_double + (-1)*C7_ConstantValue__91_CAST_sub41<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__91_CAST_sub41
solver.Add( + (1)*ConstantValue__91_double + (1)*ConstantValue__91_CAST_sub41_float + (-1)*C8_ConstantValue__91_CAST_sub41<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__91_CAST_sub41



#Constraint for cast for   %sub41 = fsub float -0.000000e+00, %rate, !taffo.info !75, !taffo.initweight !39, !taffo.constinfo !77
sptprice_CAST_sub41_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_sub41_fixbits')
sptprice_CAST_sub41_fixp = solver.IntVar(0, 1, 'sptprice_CAST_sub41_fixp')
sptprice_CAST_sub41_float = solver.IntVar(0, 1, 'sptprice_CAST_sub41_float')
sptprice_CAST_sub41_double = solver.IntVar(0, 1, 'sptprice_CAST_sub41_double')
solver.Add( + (1)*sptprice_CAST_sub41_fixp + (1)*sptprice_CAST_sub41_float + (1)*sptprice_CAST_sub41_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_sub41_fixbits + (-10000)*sptprice_CAST_sub41_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C1_sptprice_CAST_sub41')
C2_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C2_sptprice_CAST_sub41')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_sub41_fixbits + (-10000)*C1_sptprice_CAST_sub41<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_sub41_fixbits + (-10000)*C2_sptprice_CAST_sub41<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_sub41
castCostObj +=  + (1.13006)*C2_sptprice_CAST_sub41
C3_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C3_sptprice_CAST_sub41')
C4_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C4_sptprice_CAST_sub41')
C5_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C5_sptprice_CAST_sub41')
C6_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C6_sptprice_CAST_sub41')
C7_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C7_sptprice_CAST_sub41')
C8_sptprice_CAST_sub41 = solver.IntVar(0, 1, 'C8_sptprice_CAST_sub41')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_sub41_float + (-1)*C3_sptprice_CAST_sub41<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_sub41
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_sub41_fixp + (-1)*C4_sptprice_CAST_sub41<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_sub41
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_sub41_double + (-1)*C5_sptprice_CAST_sub41<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_sub41
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_sub41_fixp + (-1)*C6_sptprice_CAST_sub41<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_sub41
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_sub41_double + (-1)*C7_sptprice_CAST_sub41<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_sub41
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_sub41_float + (-1)*C8_sptprice_CAST_sub41<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_sub41



#Stuff for   %sub41 = fsub float -0.000000e+00, %rate, !taffo.info !75, !taffo.initweight !39, !taffo.constinfo !77
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float<=10029)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double<=10058)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__91_CAST_sub41_fixp + (-1)*sptprice_CAST_sub41_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__91_CAST_sub41_float + (-1)*sptprice_CAST_sub41_float==0)    #float equality
solver.Add( + (1)*ConstantValue__91_CAST_sub41_double + (-1)*sptprice_CAST_sub41_double==0)    #double equality
solver.Add( + (1)*ConstantValue__91_CAST_sub41_fixbits + (-1)*sptprice_CAST_sub41_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__91_CAST_sub41_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__91_CAST_sub41_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float==0)    #float equality
solver.Add( + (1)*ConstantValue__91_CAST_sub41_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double==0)    #double equality
solver.Add( + (1)*ConstantValue__91_CAST_sub41_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob + (-1)*ConstantValue__89_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp9<=0)    #Enob propagation in sub second addend



#Constraint for cast for   %mul42 = fmul float %sub41, %time, !taffo.info !80, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42



#Constraint for cast for   %mul42 = fmul float %sub41, %time, !taffo.info !80, !taffo.initweight !39
sptprice_CAST_mul42_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul42_fixbits')
sptprice_CAST_mul42_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul42_fixp')
sptprice_CAST_mul42_float = solver.IntVar(0, 1, 'sptprice_CAST_mul42_float')
sptprice_CAST_mul42_double = solver.IntVar(0, 1, 'sptprice_CAST_mul42_double')
solver.Add( + (1)*sptprice_CAST_mul42_fixp + (1)*sptprice_CAST_mul42_float + (1)*sptprice_CAST_mul42_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul42_fixbits + (-10000)*sptprice_CAST_mul42_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul42')
C2_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul42')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul42_fixbits + (-10000)*C1_sptprice_CAST_mul42<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul42_fixbits + (-10000)*C2_sptprice_CAST_mul42<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul42
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul42
C3_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul42')
C4_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul42')
C5_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul42')
C6_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul42')
C7_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul42')
C8_sptprice_CAST_mul42 = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul42')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul42_float + (-1)*C3_sptprice_CAST_mul42<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul42
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul42_fixp + (-1)*C4_sptprice_CAST_mul42<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul42
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul42_double + (-1)*C5_sptprice_CAST_mul42<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul42
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul42_fixp + (-1)*C6_sptprice_CAST_mul42<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul42
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul42_double + (-1)*C7_sptprice_CAST_mul42<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul42
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul42_float + (-1)*C8_sptprice_CAST_mul42<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul42



#Stuff for   %mul42 = fmul float %sub41, %time, !taffo.info !80, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float<=10033)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double<=10062)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp + (-1)*sptprice_CAST_mul42_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_float + (-1)*sptprice_CAST_mul42_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_double + (-1)*sptprice_CAST_mul42_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_CAST_mul42_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp13 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_1<=5)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub41_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_enob_2<=4)    #Enob: propagation in product 2



#Stuff for   %call43 = call float @_ZSt3expf.11(float %mul42), !taffo.info !82, !taffo.initweight !46, !taffo.constinfo !40, !taffo.originalCall !84
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_float<=10024)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_double<=10053)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %call = call float @expf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_ZSt3expf_11_call_fixbits = solver.IntVar(0, 31, '_ZSt3expf_11_call_fixbits')
_ZSt3expf_11_call_fixp = solver.IntVar(0, 1, '_ZSt3expf_11_call_fixp')
_ZSt3expf_11_call_float = solver.IntVar(0, 1, '_ZSt3expf_11_call_float')
_ZSt3expf_11_call_double = solver.IntVar(0, 1, '_ZSt3expf_11_call_double')
_ZSt3expf_11_call_enob = solver.IntVar(-10000, 10000, '_ZSt3expf_11_call_enob')
solver.Add( + (1)*_ZSt3expf_11_call_enob + (-1)*_ZSt3expf_11_call_fixbits + (10000)*_ZSt3expf_11_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_ZSt3expf_11_call_enob + (10000)*_ZSt3expf_11_call_float<=10024)    #Enob constraint for float
solver.Add( + (1)*_ZSt3expf_11_call_enob + (10000)*_ZSt3expf_11_call_double<=10053)    #Enob constraint for double
solver.Add( + (1)*_ZSt3expf_11_call_fixbits + (-10000)*_ZSt3expf_11_call_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_ZSt3expf_11_call_enob
solver.Add( + (1)*_ZSt3expf_11_call_fixp + (1)*_ZSt3expf_11_call_float + (1)*_ZSt3expf_11_call_double==1)    #Exactly one selected type
solver.Add( + (1)*_ZSt3expf_11_call_fixbits + (-10000)*_ZSt3expf_11_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_ZSt3expf_11_call_float==1)    #Type constraint for return value



#Constraint for cast for   %call = call float @expf(float %__x) #3, !taffo.info !28, !taffo.initweight !30, !taffo.constinfo !31
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul42_CAST_call_float==1)    #Type constraint for argument value



#Constraint for cast for   ret float %call, !taffo.info !32, !taffo.initweight !33
_ZSt3expf_11_call_CAST_ret_fixbits = solver.IntVar(0, 31, '_ZSt3expf_11_call_CAST_ret_fixbits')
_ZSt3expf_11_call_CAST_ret_fixp = solver.IntVar(0, 1, '_ZSt3expf_11_call_CAST_ret_fixp')
_ZSt3expf_11_call_CAST_ret_float = solver.IntVar(0, 1, '_ZSt3expf_11_call_CAST_ret_float')
_ZSt3expf_11_call_CAST_ret_double = solver.IntVar(0, 1, '_ZSt3expf_11_call_CAST_ret_double')
solver.Add( + (1)*_ZSt3expf_11_call_CAST_ret_fixp + (1)*_ZSt3expf_11_call_CAST_ret_float + (1)*_ZSt3expf_11_call_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_ZSt3expf_11_call_CAST_ret_fixbits + (-10000)*_ZSt3expf_11_call_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C1__ZSt3expf_11_call_CAST_ret')
C2__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C2__ZSt3expf_11_call_CAST_ret')
solver.Add( + (1)*_ZSt3expf_11_call_fixbits + (-1)*_ZSt3expf_11_call_CAST_ret_fixbits + (-10000)*C1__ZSt3expf_11_call_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_ZSt3expf_11_call_fixbits + (1)*_ZSt3expf_11_call_CAST_ret_fixbits + (-10000)*C2__ZSt3expf_11_call_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__ZSt3expf_11_call_CAST_ret
castCostObj +=  + (1.13006)*C2__ZSt3expf_11_call_CAST_ret
C3__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C3__ZSt3expf_11_call_CAST_ret')
C4__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C4__ZSt3expf_11_call_CAST_ret')
C5__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C5__ZSt3expf_11_call_CAST_ret')
C6__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C6__ZSt3expf_11_call_CAST_ret')
C7__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C7__ZSt3expf_11_call_CAST_ret')
C8__ZSt3expf_11_call_CAST_ret = solver.IntVar(0, 1, 'C8__ZSt3expf_11_call_CAST_ret')
solver.Add( + (1)*_ZSt3expf_11_call_fixp + (1)*_ZSt3expf_11_call_CAST_ret_float + (-1)*C3__ZSt3expf_11_call_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__ZSt3expf_11_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_11_call_float + (1)*_ZSt3expf_11_call_CAST_ret_fixp + (-1)*C4__ZSt3expf_11_call_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__ZSt3expf_11_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_11_call_fixp + (1)*_ZSt3expf_11_call_CAST_ret_double + (-1)*C5__ZSt3expf_11_call_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__ZSt3expf_11_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_11_call_double + (1)*_ZSt3expf_11_call_CAST_ret_fixp + (-1)*C6__ZSt3expf_11_call_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__ZSt3expf_11_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_11_call_float + (1)*_ZSt3expf_11_call_CAST_ret_double + (-1)*C7__ZSt3expf_11_call_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__ZSt3expf_11_call_CAST_ret
solver.Add( + (1)*_ZSt3expf_11_call_double + (1)*_ZSt3expf_11_call_CAST_ret_float + (-1)*C8__ZSt3expf_11_call_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__ZSt3expf_11_call_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp + (-1)*_ZSt3expf_11_call_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_float + (-1)*_ZSt3expf_11_call_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_double + (-1)*_ZSt3expf_11_call_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits + (-1)*_ZSt3expf_11_call_CAST_ret_fixbits==0)    #same fractional bit



#Constraint for cast for   %mul44 = fmul float %strike, %call43, !taffo.info !85, !taffo.initweight !39
sptprice_CAST_mul44_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul44_fixbits')
sptprice_CAST_mul44_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul44_fixp')
sptprice_CAST_mul44_float = solver.IntVar(0, 1, 'sptprice_CAST_mul44_float')
sptprice_CAST_mul44_double = solver.IntVar(0, 1, 'sptprice_CAST_mul44_double')
solver.Add( + (1)*sptprice_CAST_mul44_fixp + (1)*sptprice_CAST_mul44_float + (1)*sptprice_CAST_mul44_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul44_fixbits + (-10000)*sptprice_CAST_mul44_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul44')
C2_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul44')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul44_fixbits + (-10000)*C1_sptprice_CAST_mul44<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul44_fixbits + (-10000)*C2_sptprice_CAST_mul44<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul44
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul44
C3_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul44')
C4_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul44')
C5_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul44')
C6_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul44')
C7_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul44')
C8_sptprice_CAST_mul44 = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul44')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul44_float + (-1)*C3_sptprice_CAST_mul44<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul44
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul44_fixp + (-1)*C4_sptprice_CAST_mul44<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul44
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul44_double + (-1)*C5_sptprice_CAST_mul44<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul44
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul44_fixp + (-1)*C6_sptprice_CAST_mul44<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul44
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul44_double + (-1)*C7_sptprice_CAST_mul44<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul44
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul44_float + (-1)*C8_sptprice_CAST_mul44<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul44



#Constraint for cast for   %mul44 = fmul float %strike, %call43, !taffo.info !85, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44



#Stuff for   %mul44 = fmul float %strike, %call43, !taffo.info !85, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float<=10025)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double<=10054)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp>=-9970)    #Limit the lower number of frac bits31
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*sptprice_CAST_mul44_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul44_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul44_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_CAST_mul44_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_mul44_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul44_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul44_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call43_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_1<=2)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp7 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob_2<=0)    #Enob: propagation in product 2



#Constraint for cast for   %mul47 = fmul float %sptprice, %call34, !taffo.info !88, !taffo.initweight !39
sptprice_CAST_mul47_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul47_fixbits')
sptprice_CAST_mul47_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul47_fixp')
sptprice_CAST_mul47_float = solver.IntVar(0, 1, 'sptprice_CAST_mul47_float')
sptprice_CAST_mul47_double = solver.IntVar(0, 1, 'sptprice_CAST_mul47_double')
solver.Add( + (1)*sptprice_CAST_mul47_fixp + (1)*sptprice_CAST_mul47_float + (1)*sptprice_CAST_mul47_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul47_fixbits + (-10000)*sptprice_CAST_mul47_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul47')
C2_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul47')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul47_fixbits + (-10000)*C1_sptprice_CAST_mul47<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul47_fixbits + (-10000)*C2_sptprice_CAST_mul47<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul47
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul47
C3_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul47')
C4_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul47')
C5_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul47')
C6_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul47')
C7_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul47')
C8_sptprice_CAST_mul47 = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul47')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul47_float + (-1)*C3_sptprice_CAST_mul47<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul47
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul47_fixp + (-1)*C4_sptprice_CAST_mul47<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul47
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul47_double + (-1)*C5_sptprice_CAST_mul47<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul47
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul47_fixp + (-1)*C6_sptprice_CAST_mul47<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul47
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul47_double + (-1)*C7_sptprice_CAST_mul47<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul47
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul47_float + (-1)*C8_sptprice_CAST_mul47<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul47



#Constraint for cast for   %mul47 = fmul float %sptprice, %call34, !taffo.info !88, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47



#Stuff for   %mul47 = fmul float %sptprice, %call34, !taffo.info !88, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*sptprice_CAST_mul47_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul47_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul47_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_mul47_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_mul47_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul47_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul47_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_1<=2)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp5 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul48 = fmul float %mul44, %call36, !taffo.info !90, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48



#Constraint for cast for   %mul48 = fmul float %mul44, %call36, !taffo.info !90, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48



#Stuff for   %mul48 = fmul float %mul44, %call36, !taffo.info !90, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_mul48_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul48_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_1<=2)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub49 = fsub float %mul47, %mul48, !taffo.info !92, !taffo.initweight !46
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49



#Constraint for cast for   %sub49 = fsub float %mul47, %mul48, !taffo.info !92, !taffo.initweight !46
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49



#Stuff for   %sub49 = fsub float %mul47, %mul48, !taffo.info !92, !taffo.initweight !46
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_CAST_sub49_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_CAST_sub49_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul47_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul48_enob<=0)    #Enob propagation in sub second addend



#Stuff for double 1.000000e+00
ConstantValue__92_fixbits = solver.IntVar(0, 31, 'ConstantValue__92_fixbits')
ConstantValue__92_fixp = solver.IntVar(0, 1, 'ConstantValue__92_fixp')
ConstantValue__92_float = solver.IntVar(0, 1, 'ConstantValue__92_float')
ConstantValue__92_double = solver.IntVar(0, 1, 'ConstantValue__92_double')
ConstantValue__92_enob = solver.IntVar(-10000, 10000, 'ConstantValue__92_enob')
solver.Add( + (1)*ConstantValue__92_enob + (-1)*ConstantValue__92_fixbits + (10000)*ConstantValue__92_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__92_enob + (10000)*ConstantValue__92_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__92_enob + (10000)*ConstantValue__92_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__92_fixbits + (-10000)*ConstantValue__92_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__92_fixp + (1)*ConstantValue__92_float + (1)*ConstantValue__92_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__92_fixbits + (-10000)*ConstantValue__92_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__93_fixbits = solver.IntVar(0, 31, 'ConstantValue__93_fixbits')
ConstantValue__93_fixp = solver.IntVar(0, 1, 'ConstantValue__93_fixp')
ConstantValue__93_float = solver.IntVar(0, 1, 'ConstantValue__93_float')
ConstantValue__93_double = solver.IntVar(0, 1, 'ConstantValue__93_double')
ConstantValue__93_enob = solver.IntVar(-10000, 10000, 'ConstantValue__93_enob')
solver.Add( + (1)*ConstantValue__93_enob + (-1)*ConstantValue__93_fixbits + (10000)*ConstantValue__93_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__93_enob + (10000)*ConstantValue__93_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__93_enob + (10000)*ConstantValue__93_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__93_fixbits + (-10000)*ConstantValue__93_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__93_fixp + (1)*ConstantValue__93_float + (1)*ConstantValue__93_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__93_fixbits + (-10000)*ConstantValue__93_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__94_fixbits = solver.IntVar(0, 31, 'ConstantValue__94_fixbits')
ConstantValue__94_fixp = solver.IntVar(0, 1, 'ConstantValue__94_fixp')
ConstantValue__94_float = solver.IntVar(0, 1, 'ConstantValue__94_float')
ConstantValue__94_double = solver.IntVar(0, 1, 'ConstantValue__94_double')
ConstantValue__94_enob = solver.IntVar(-10000, 10000, 'ConstantValue__94_enob')
solver.Add( + (1)*ConstantValue__94_enob + (-1)*ConstantValue__94_fixbits + (10000)*ConstantValue__94_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__94_enob + (10000)*ConstantValue__94_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__94_enob + (10000)*ConstantValue__94_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__94_fixbits + (-10000)*ConstantValue__94_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__94_fixp + (1)*ConstantValue__94_float + (1)*ConstantValue__94_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__94_fixbits + (-10000)*ConstantValue__94_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub51 = fsub double 1.000000e+00, %conv50, !taffo.info !34, !taffo.initweight !46, !taffo.constinfo !94
ConstantValue__94_CAST_sub51_fixbits = solver.IntVar(0, 31, 'ConstantValue__94_CAST_sub51_fixbits')
ConstantValue__94_CAST_sub51_fixp = solver.IntVar(0, 1, 'ConstantValue__94_CAST_sub51_fixp')
ConstantValue__94_CAST_sub51_float = solver.IntVar(0, 1, 'ConstantValue__94_CAST_sub51_float')
ConstantValue__94_CAST_sub51_double = solver.IntVar(0, 1, 'ConstantValue__94_CAST_sub51_double')
solver.Add( + (1)*ConstantValue__94_CAST_sub51_fixp + (1)*ConstantValue__94_CAST_sub51_float + (1)*ConstantValue__94_CAST_sub51_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__94_CAST_sub51_fixbits + (-10000)*ConstantValue__94_CAST_sub51_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C1_ConstantValue__94_CAST_sub51')
C2_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C2_ConstantValue__94_CAST_sub51')
solver.Add( + (1)*ConstantValue__94_fixbits + (-1)*ConstantValue__94_CAST_sub51_fixbits + (-10000)*C1_ConstantValue__94_CAST_sub51<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__94_fixbits + (1)*ConstantValue__94_CAST_sub51_fixbits + (-10000)*C2_ConstantValue__94_CAST_sub51<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__94_CAST_sub51
castCostObj +=  + (1.13006)*C2_ConstantValue__94_CAST_sub51
C3_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C3_ConstantValue__94_CAST_sub51')
C4_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C4_ConstantValue__94_CAST_sub51')
C5_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C5_ConstantValue__94_CAST_sub51')
C6_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C6_ConstantValue__94_CAST_sub51')
C7_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C7_ConstantValue__94_CAST_sub51')
C8_ConstantValue__94_CAST_sub51 = solver.IntVar(0, 1, 'C8_ConstantValue__94_CAST_sub51')
solver.Add( + (1)*ConstantValue__94_fixp + (1)*ConstantValue__94_CAST_sub51_float + (-1)*C3_ConstantValue__94_CAST_sub51<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__94_CAST_sub51
solver.Add( + (1)*ConstantValue__94_float + (1)*ConstantValue__94_CAST_sub51_fixp + (-1)*C4_ConstantValue__94_CAST_sub51<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__94_CAST_sub51
solver.Add( + (1)*ConstantValue__94_fixp + (1)*ConstantValue__94_CAST_sub51_double + (-1)*C5_ConstantValue__94_CAST_sub51<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__94_CAST_sub51
solver.Add( + (1)*ConstantValue__94_double + (1)*ConstantValue__94_CAST_sub51_fixp + (-1)*C6_ConstantValue__94_CAST_sub51<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__94_CAST_sub51
solver.Add( + (1)*ConstantValue__94_float + (1)*ConstantValue__94_CAST_sub51_double + (-1)*C7_ConstantValue__94_CAST_sub51<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__94_CAST_sub51
solver.Add( + (1)*ConstantValue__94_double + (1)*ConstantValue__94_CAST_sub51_float + (-1)*C8_ConstantValue__94_CAST_sub51<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__94_CAST_sub51



#Constraint for cast for   %sub51 = fsub double 1.000000e+00, %conv50, !taffo.info !34, !taffo.initweight !46, !taffo.constinfo !94
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51



#Stuff for   %sub51 = fsub double 1.000000e+00, %conv50, !taffo.info !34, !taffo.initweight !46, !taffo.constinfo !94
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__94_CAST_sub51_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__94_CAST_sub51_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_float==0)    #float equality
solver.Add( + (1)*ConstantValue__94_CAST_sub51_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_double==0)    #double equality
solver.Add( + (1)*ConstantValue__94_CAST_sub51_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_CAST_sub51_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__94_CAST_sub51_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__94_CAST_sub51_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float==0)    #float equality
solver.Add( + (1)*ConstantValue__94_CAST_sub51_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double==0)    #double equality
solver.Add( + (1)*ConstantValue__94_CAST_sub51_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob + (-1)*ConstantValue__92_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call34_enob<=0)    #Enob propagation in sub second addend



#Stuff for double 1.000000e+00
ConstantValue__95_fixbits = solver.IntVar(0, 31, 'ConstantValue__95_fixbits')
ConstantValue__95_fixp = solver.IntVar(0, 1, 'ConstantValue__95_fixp')
ConstantValue__95_float = solver.IntVar(0, 1, 'ConstantValue__95_float')
ConstantValue__95_double = solver.IntVar(0, 1, 'ConstantValue__95_double')
ConstantValue__95_enob = solver.IntVar(-10000, 10000, 'ConstantValue__95_enob')
solver.Add( + (1)*ConstantValue__95_enob + (-1)*ConstantValue__95_fixbits + (10000)*ConstantValue__95_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__95_enob + (10000)*ConstantValue__95_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__95_enob + (10000)*ConstantValue__95_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__95_fixbits + (-10000)*ConstantValue__95_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__95_fixp + (1)*ConstantValue__95_float + (1)*ConstantValue__95_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__95_fixbits + (-10000)*ConstantValue__95_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__96_fixbits = solver.IntVar(0, 31, 'ConstantValue__96_fixbits')
ConstantValue__96_fixp = solver.IntVar(0, 1, 'ConstantValue__96_fixp')
ConstantValue__96_float = solver.IntVar(0, 1, 'ConstantValue__96_float')
ConstantValue__96_double = solver.IntVar(0, 1, 'ConstantValue__96_double')
ConstantValue__96_enob = solver.IntVar(-10000, 10000, 'ConstantValue__96_enob')
solver.Add( + (1)*ConstantValue__96_enob + (-1)*ConstantValue__96_fixbits + (10000)*ConstantValue__96_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__96_enob + (10000)*ConstantValue__96_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__96_enob + (10000)*ConstantValue__96_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__96_fixbits + (-10000)*ConstantValue__96_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__96_fixp + (1)*ConstantValue__96_float + (1)*ConstantValue__96_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__96_fixbits + (-10000)*ConstantValue__96_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__97_fixbits = solver.IntVar(0, 31, 'ConstantValue__97_fixbits')
ConstantValue__97_fixp = solver.IntVar(0, 1, 'ConstantValue__97_fixp')
ConstantValue__97_float = solver.IntVar(0, 1, 'ConstantValue__97_float')
ConstantValue__97_double = solver.IntVar(0, 1, 'ConstantValue__97_double')
ConstantValue__97_enob = solver.IntVar(-10000, 10000, 'ConstantValue__97_enob')
solver.Add( + (1)*ConstantValue__97_enob + (-1)*ConstantValue__97_fixbits + (10000)*ConstantValue__97_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__97_enob + (10000)*ConstantValue__97_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__97_enob + (10000)*ConstantValue__97_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__97_fixbits + (-10000)*ConstantValue__97_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__97_fixp + (1)*ConstantValue__97_float + (1)*ConstantValue__97_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__97_fixbits + (-10000)*ConstantValue__97_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub54 = fsub double 1.000000e+00, %conv53, !taffo.info !34, !taffo.initweight !46, !taffo.constinfo !94
ConstantValue__97_CAST_sub54_fixbits = solver.IntVar(0, 31, 'ConstantValue__97_CAST_sub54_fixbits')
ConstantValue__97_CAST_sub54_fixp = solver.IntVar(0, 1, 'ConstantValue__97_CAST_sub54_fixp')
ConstantValue__97_CAST_sub54_float = solver.IntVar(0, 1, 'ConstantValue__97_CAST_sub54_float')
ConstantValue__97_CAST_sub54_double = solver.IntVar(0, 1, 'ConstantValue__97_CAST_sub54_double')
solver.Add( + (1)*ConstantValue__97_CAST_sub54_fixp + (1)*ConstantValue__97_CAST_sub54_float + (1)*ConstantValue__97_CAST_sub54_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__97_CAST_sub54_fixbits + (-10000)*ConstantValue__97_CAST_sub54_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C1_ConstantValue__97_CAST_sub54')
C2_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C2_ConstantValue__97_CAST_sub54')
solver.Add( + (1)*ConstantValue__97_fixbits + (-1)*ConstantValue__97_CAST_sub54_fixbits + (-10000)*C1_ConstantValue__97_CAST_sub54<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__97_fixbits + (1)*ConstantValue__97_CAST_sub54_fixbits + (-10000)*C2_ConstantValue__97_CAST_sub54<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_ConstantValue__97_CAST_sub54
castCostObj +=  + (1.13006)*C2_ConstantValue__97_CAST_sub54
C3_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C3_ConstantValue__97_CAST_sub54')
C4_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C4_ConstantValue__97_CAST_sub54')
C5_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C5_ConstantValue__97_CAST_sub54')
C6_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C6_ConstantValue__97_CAST_sub54')
C7_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C7_ConstantValue__97_CAST_sub54')
C8_ConstantValue__97_CAST_sub54 = solver.IntVar(0, 1, 'C8_ConstantValue__97_CAST_sub54')
solver.Add( + (1)*ConstantValue__97_fixp + (1)*ConstantValue__97_CAST_sub54_float + (-1)*C3_ConstantValue__97_CAST_sub54<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_ConstantValue__97_CAST_sub54
solver.Add( + (1)*ConstantValue__97_float + (1)*ConstantValue__97_CAST_sub54_fixp + (-1)*C4_ConstantValue__97_CAST_sub54<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_ConstantValue__97_CAST_sub54
solver.Add( + (1)*ConstantValue__97_fixp + (1)*ConstantValue__97_CAST_sub54_double + (-1)*C5_ConstantValue__97_CAST_sub54<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_ConstantValue__97_CAST_sub54
solver.Add( + (1)*ConstantValue__97_double + (1)*ConstantValue__97_CAST_sub54_fixp + (-1)*C6_ConstantValue__97_CAST_sub54<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_ConstantValue__97_CAST_sub54
solver.Add( + (1)*ConstantValue__97_float + (1)*ConstantValue__97_CAST_sub54_double + (-1)*C7_ConstantValue__97_CAST_sub54<=1)    #Float to double
castCostObj +=  + (1)*C7_ConstantValue__97_CAST_sub54
solver.Add( + (1)*ConstantValue__97_double + (1)*ConstantValue__97_CAST_sub54_float + (-1)*C8_ConstantValue__97_CAST_sub54<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_ConstantValue__97_CAST_sub54



#Constraint for cast for   %sub54 = fsub double 1.000000e+00, %conv53, !taffo.info !34, !taffo.initweight !46, !taffo.constinfo !94
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54



#Stuff for   %sub54 = fsub double 1.000000e+00, %conv53, !taffo.info !34, !taffo.initweight !46, !taffo.constinfo !94
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp>=-9972)    #Limit the lower number of frac bits29
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__97_CAST_sub54_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__97_CAST_sub54_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_float==0)    #float equality
solver.Add( + (1)*ConstantValue__97_CAST_sub54_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_double==0)    #double equality
solver.Add( + (1)*ConstantValue__97_CAST_sub54_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_CAST_sub54_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__97_CAST_sub54_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__97_CAST_sub54_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float==0)    #float equality
solver.Add( + (1)*ConstantValue__97_CAST_sub54_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double==0)    #double equality
solver.Add( + (1)*ConstantValue__97_CAST_sub54_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob + (-1)*ConstantValue__95_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_call36_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   %mul56 = fmul float %mul44, %conv55, !taffo.info !90, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixbits = solver.IntVar(0, 31, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56



#Constraint for cast for   %mul56 = fmul float %mul44, %conv55, !taffo.info !90, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56



#Stuff for   %mul56 = fmul float %mul44, %conv55, !taffo.info !90, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_CAST_mul56_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_CAST_mul56_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub54_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_1<=2)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul44_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %mul57 = fmul float %sptprice, %conv52, !taffo.info !88, !taffo.initweight !39
sptprice_CAST_mul57_fixbits = solver.IntVar(0, 31, 'sptprice_CAST_mul57_fixbits')
sptprice_CAST_mul57_fixp = solver.IntVar(0, 1, 'sptprice_CAST_mul57_fixp')
sptprice_CAST_mul57_float = solver.IntVar(0, 1, 'sptprice_CAST_mul57_float')
sptprice_CAST_mul57_double = solver.IntVar(0, 1, 'sptprice_CAST_mul57_double')
solver.Add( + (1)*sptprice_CAST_mul57_fixp + (1)*sptprice_CAST_mul57_float + (1)*sptprice_CAST_mul57_double==1)    #exactly 1 type
solver.Add( + (1)*sptprice_CAST_mul57_fixbits + (-10000)*sptprice_CAST_mul57_fixp<=0)    #If no fix, fix frac part = 0
C1_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C1_sptprice_CAST_mul57')
C2_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C2_sptprice_CAST_mul57')
solver.Add( + (1)*sptprice_fixbits + (-1)*sptprice_CAST_mul57_fixbits + (-10000)*C1_sptprice_CAST_mul57<=0)    #Shift cost 1
solver.Add( + (-1)*sptprice_fixbits + (1)*sptprice_CAST_mul57_fixbits + (-10000)*C2_sptprice_CAST_mul57<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1_sptprice_CAST_mul57
castCostObj +=  + (1.13006)*C2_sptprice_CAST_mul57
C3_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C3_sptprice_CAST_mul57')
C4_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C4_sptprice_CAST_mul57')
C5_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C5_sptprice_CAST_mul57')
C6_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C6_sptprice_CAST_mul57')
C7_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C7_sptprice_CAST_mul57')
C8_sptprice_CAST_mul57 = solver.IntVar(0, 1, 'C8_sptprice_CAST_mul57')
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul57_float + (-1)*C3_sptprice_CAST_mul57<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3_sptprice_CAST_mul57
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul57_fixp + (-1)*C4_sptprice_CAST_mul57<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4_sptprice_CAST_mul57
solver.Add( + (1)*sptprice_fixp + (1)*sptprice_CAST_mul57_double + (-1)*C5_sptprice_CAST_mul57<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5_sptprice_CAST_mul57
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul57_fixp + (-1)*C6_sptprice_CAST_mul57<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6_sptprice_CAST_mul57
solver.Add( + (1)*sptprice_float + (1)*sptprice_CAST_mul57_double + (-1)*C7_sptprice_CAST_mul57<=1)    #Float to double
castCostObj +=  + (1)*C7_sptprice_CAST_mul57
solver.Add( + (1)*sptprice_double + (1)*sptprice_CAST_mul57_float + (-1)*C8_sptprice_CAST_mul57<=1)    #Double to float
castCostObj +=  + (5.90592)*C8_sptprice_CAST_mul57



#Constraint for cast for   %mul57 = fmul float %sptprice, %conv52, !taffo.info !88, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixbits = solver.IntVar(0, 29, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57



#Stuff for   %mul57 = fmul float %sptprice, %conv52, !taffo.info !88, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*sptprice_CAST_mul57_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul57_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul57_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_CAST_mul57_double==0)    #double equality
solver.Add( + (1)*sptprice_CAST_mul57_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp==0)    #fix equality
solver.Add( + (1)*sptprice_CAST_mul57_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float==0)    #float equality
solver.Add( + (1)*sptprice_CAST_mul57_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double==0)    #double equality
mathCostObj +=  + (2.04123)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp
mathCostObj +=  + (3.34669)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float
mathCostObj +=  + (4.14035)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_1')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_2 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_2')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_1 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub51_enob + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_1<=2)    #Enob: propagation in product 1
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob + (-1)*sptprice_enob_memphi__Z9bs_threadPv_tmp5 + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub58 = fsub float %mul56, %mul57, !taffo.info !97, !taffo.initweight !46
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58



#Constraint for cast for   %sub58 = fsub float %mul56, %mul57, !taffo.info !97, !taffo.initweight !46
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58



#Stuff for   %sub58 = fsub float %mul56, %mul57, !taffo.info !97, !taffo.initweight !46
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_CAST_sub58_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_CAST_sub58_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.30379)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp
mathCostObj +=  + (1.80596)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float
mathCostObj +=  + (2.15411)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul56_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_mul57_enob<=0)    #Enob propagation in sub second addend



#Stuff for   %OptionPrice.0 = phi float [ %sub49, %if.then46 ], [ %sub58, %if.else ], !taffo.info !99
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob = solver.IntVar(-10000, 10000, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp>=-9971)    #Limit the lower number of frac bits30
enobCostObj +=  + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double==1)    #Exactly one selected type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp<=0)    #If not fix, frac part to zero
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_0 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_0')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_1 = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_1')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_0 + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %OptionPrice.0 = phi float [ %sub49, %if.then46 ], [ %sub58, %if.else ], !taffo.info !99
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_CAST_OptionPrice_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub49_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_0<=10000)    #Enob: forcing phi enob



#Constraint for cast for   %OptionPrice.0 = phi float [ %sub49, %if.then46 ], [ %sub58, %if.else ], !taffo.info !99
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0 = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixp==0)    #fix equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_float==0)    #float equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_double==0)    #double equality
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_CAST_OptionPrice_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_sub58_enob + (10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   ret float %OptionPrice.0, !taffo.info !73, !taffo.initweight !39
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixbits = solver.IntVar(0, 30, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixbits')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixp = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixp')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_float = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_float')
_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_double = solver.IntVar(0, 1, '_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_double')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_double==1)    #exactly 1 type
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixbits + (-10000)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixp<=0)    #If no fix, fix frac part = 0
C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixbits + (-10000)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=0)    #Shift cost 1
solver.Add( + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixbits + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixbits + (-10000)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=0)    #Shift cost 2
castCostObj +=  + (1.13006)*C1__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
castCostObj +=  + (1.13006)*C2__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret = solver.IntVar(0, 1, 'C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret')
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_float + (-1)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=1)    #Fix to float
castCostObj +=  + (4.12075)*C3__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixp + (-1)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=1)    #Float to fix
castCostObj +=  + (3.33505)*C4__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_fixp + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_double + (-1)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=1)    #Fix to double
castCostObj +=  + (5.63733)*C5__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixp + (-1)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=1)    #Double to fix
castCostObj +=  + (4.40388)*C6__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_float + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_double + (-1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=1)    #Float to double
castCostObj +=  + (1)*C7__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
solver.Add( + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_double + (1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_float + (-1)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret<=1)    #Double to float
castCostObj +=  + (5.90592)*C8__Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret
solver.Add( + (1)*_Z9bs_threadPv_call_fixp + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixp==0)    #fix equality
solver.Add( + (1)*_Z9bs_threadPv_call_float + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_float==0)    #float equality
solver.Add( + (1)*_Z9bs_threadPv_call_double + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_double==0)    #double equality
solver.Add( + (1)*_Z9bs_threadPv_call_fixbits + (-1)*_Z19BlkSchlsEqEuroNoDivfffffifPfS__5_OptionPrice_0_CAST_ret_fixbits==0)    #same fractional bit



#Stuff for double 1.000000e+09
ConstantValue__98_fixbits = solver.IntVar(0, 34, 'ConstantValue__98_fixbits')
ConstantValue__98_fixp = solver.IntVar(0, 1, 'ConstantValue__98_fixp')
ConstantValue__98_float = solver.IntVar(0, 1, 'ConstantValue__98_float')
ConstantValue__98_double = solver.IntVar(0, 1, 'ConstantValue__98_double')
ConstantValue__98_enob = solver.IntVar(-10000, 10000, 'ConstantValue__98_enob')
solver.Add( + (1)*ConstantValue__98_enob + (-1)*ConstantValue__98_fixbits + (10000)*ConstantValue__98_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__98_enob + (10000)*ConstantValue__98_float<=9994)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__98_enob + (10000)*ConstantValue__98_double<=10023)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__98_fixbits + (-10000)*ConstantValue__98_fixp>=-9967)    #Limit the lower number of frac bits34
solver.Add( + (1)*ConstantValue__98_fixp + (1)*ConstantValue__98_float + (1)*ConstantValue__98_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__98_fixbits + (-10000)*ConstantValue__98_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+09
ConstantValue__99_fixbits = solver.IntVar(0, 34, 'ConstantValue__99_fixbits')
ConstantValue__99_fixp = solver.IntVar(0, 1, 'ConstantValue__99_fixp')
ConstantValue__99_float = solver.IntVar(0, 1, 'ConstantValue__99_float')
ConstantValue__99_double = solver.IntVar(0, 1, 'ConstantValue__99_double')
ConstantValue__99_enob = solver.IntVar(-10000, 10000, 'ConstantValue__99_enob')
solver.Add( + (1)*ConstantValue__99_enob + (-1)*ConstantValue__99_fixbits + (10000)*ConstantValue__99_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__99_enob + (10000)*ConstantValue__99_float<=9994)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__99_enob + (10000)*ConstantValue__99_double<=10023)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__99_fixbits + (-10000)*ConstantValue__99_fixp>=-9967)    #Limit the lower number of frac bits34
solver.Add( + (1)*ConstantValue__99_fixp + (1)*ConstantValue__99_float + (1)*ConstantValue__99_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__99_fixbits + (-10000)*ConstantValue__99_fixp<=0)    #If not fix, frac part to zero





#All the model has been generated, lets solve it!
solver.Minimize(1 * castCostObj / 927.229+ 1 * enobCostObj / 75191+ 1000 * mathCostObj / 231.759)

# Model declaration end.