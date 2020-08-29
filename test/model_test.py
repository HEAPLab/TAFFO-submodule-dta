


#Stuff for @data = common dso_local global [32 x [28 x double]] zeroinitializer, align 16, !taffo.info !8, !taffo.initweight !11
data_fixbits = solver.IntVar(0, 27, 'data_fixbits')
data_fixp = solver.IntVar(0, 1, 'data_fixp')
data_float = solver.IntVar(0, 1, 'data_float')
data_double = solver.IntVar(0, 1, 'data_double')
data_enob = solver.IntVar(-10000, 10000, 'data_enob')
solver.Add( + (1)*data_enob + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_fixbits + (-10000)*data_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*data_enob<=333)    #Enob constraint for error maximal
enobCostObj =  + (-1)*data_enob
solver.Add( + (1)*data_fixp + (1)*data_float + (1)*data_double==1)    #Exactly one selected type
solver.Add( + (1)*data_fixbits + (-10000)*data_fixp<=0)    #If not fix, frac part to zero



#Stuff for @mean = common dso_local global [28 x double] zeroinitializer, align 16, !taffo.info !12, !taffo.initweight !11
mean_fixbits = solver.IntVar(0, 15, 'mean_fixbits')
mean_fixp = solver.IntVar(0, 1, 'mean_fixp')
mean_float = solver.IntVar(0, 1, 'mean_float')
mean_double = solver.IntVar(0, 1, 'mean_double')
mean_enob = solver.IntVar(-10000, 10000, 'mean_enob')
solver.Add( + (1)*mean_enob + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_fixbits + (-10000)*mean_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*mean_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*mean_enob
solver.Add( + (1)*mean_fixp + (1)*mean_float + (1)*mean_double==1)    #Exactly one selected type
solver.Add( + (1)*mean_fixbits + (-10000)*mean_fixp<=0)    #If not fix, frac part to zero



#Stuff for @stddev = common dso_local global [28 x double] zeroinitializer, align 16, !taffo.info !14, !taffo.initweight !11
stddev_fixbits = solver.IntVar(0, 18, 'stddev_fixbits')
stddev_fixp = solver.IntVar(0, 1, 'stddev_fixp')
stddev_float = solver.IntVar(0, 1, 'stddev_float')
stddev_double = solver.IntVar(0, 1, 'stddev_double')
stddev_enob = solver.IntVar(-10000, 10000, 'stddev_enob')
solver.Add( + (1)*stddev_enob + (-1)*stddev_fixbits + (10000)*stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*stddev_enob + (10000)*stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*stddev_enob + (10000)*stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*stddev_fixbits + (-10000)*stddev_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*stddev_enob<=4)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*stddev_enob
solver.Add( + (1)*stddev_fixp + (1)*stddev_float + (1)*stddev_double==1)    #Exactly one selected type
solver.Add( + (1)*stddev_fixbits + (-10000)*stddev_fixp<=0)    #If not fix, frac part to zero



#Stuff for @corr = common dso_local global [28 x [28 x double]] zeroinitializer, align 16, !taffo.info !17, !taffo.initweight !11
corr_fixbits = solver.IntVar(0, 29, 'corr_fixbits')
corr_fixp = solver.IntVar(0, 1, 'corr_fixp')
corr_float = solver.IntVar(0, 1, 'corr_float')
corr_double = solver.IntVar(0, 1, 'corr_double')
corr_enob = solver.IntVar(-10000, 10000, 'corr_enob')
solver.Add( + (1)*corr_enob + (-1)*corr_fixbits + (10000)*corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*corr_enob + (10000)*corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*corr_enob + (10000)*corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*corr_fixbits + (-10000)*corr_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*corr_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*corr_enob
solver.Add( + (1)*corr_fixp + (1)*corr_float + (1)*corr_double==1)    #Exactly one selected type
solver.Add( + (1)*corr_fixbits + (-10000)*corr_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %mul to double, !taffo.info !27, !taffo.initweight !29
main_conv_fixbits = solver.IntVar(0, 24, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_enob<=1)    #Limiting Enob for integer to float conversion



#Stuff for double 2.800000e+01
ConstantValue__fixbits = solver.IntVar(0, 27, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.800000e+01
ConstantValue__0_fixbits = solver.IntVar(0, 27, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double %conv, 2.800000e+01, !taffo.info !33, !taffo.initweight !35, !taffo.constinfo !36
main_conv_CAST_div_fixbits = solver.IntVar(0, 24, 'main_conv_CAST_div_fixbits')
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



#Stuff for double 2.800000e+01
ConstantValue__1_fixbits = solver.IntVar(0, 27, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10019)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10048)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9974)    #Limit the lower number of frac bits27
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div = fdiv double %conv, 2.800000e+01, !taffo.info !33, !taffo.initweight !35, !taffo.constinfo !36
ConstantValue__1_CAST_div_fixbits = solver.IntVar(0, 27, 'ConstantValue__1_CAST_div_fixbits')
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
castCostObj +=  + (6.62652)*C3_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_div_fixp + (-1)*C4_ConstantValue__1_CAST_div<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_CAST_div_double + (-1)*C5_ConstantValue__1_CAST_div<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_div_fixp + (-1)*C6_ConstantValue__1_CAST_div<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_float + (1)*ConstantValue__1_CAST_div_double + (-1)*C7_ConstantValue__1_CAST_div<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__1_CAST_div
solver.Add( + (1)*ConstantValue__1_double + (1)*ConstantValue__1_CAST_div_float + (-1)*C8_ConstantValue__1_CAST_div<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__1_CAST_div



#Stuff for   %div = fdiv double %conv, 2.800000e+01, !taffo.info !33, !taffo.initweight !35, !taffo.constinfo !36
main_div_fixbits = solver.IntVar(0, 28, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
main_div_enob = solver.IntVar(-10000, 10000, 'main_div_enob')
solver.Add( + (1)*main_div_enob + (-1)*main_div_fixbits + (10000)*main_div_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div_enob + (10000)*main_div_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div_enob + (10000)*main_div_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp>=-9973)    #Limit the lower number of frac bits28
enobCostObj +=  + (-1)*main_div_enob
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*ConstantValue__1_CAST_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*ConstantValue__1_CAST_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*ConstantValue__1_CAST_div_double==0)    #double equality
solver.Add( + (1)*main_conv_CAST_div_fixp + (-1)*main_div_fixp==0)    #fix equality
solver.Add( + (1)*main_conv_CAST_div_float + (-1)*main_div_float==0)    #float equality
solver.Add( + (1)*main_conv_CAST_div_double + (-1)*main_div_double==0)    #double equality
mathCostObj =  + (5.29598)*main_div_fixp
mathCostObj +=  + (5.60026)*main_div_float
mathCostObj +=  + (18.3266)*main_div_double
main_main_div_enob_1 = solver.IntVar(0, 1, 'main_main_div_enob_1')
main_main_div_enob_2 = solver.IntVar(0, 1, 'main_main_div_enob_2')
solver.Add( + (1)*main_main_div_enob_1 + (1)*main_main_div_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div_enob + (-1)*ConstantValue__enob + (-10000)*main_main_div_enob_1<=1034)    #Enob: propagation in division 1
solver.Add( + (1)*main_div_enob + (-1)*main_conv_enob + (-10000)*main_main_div_enob_2<=5)    #Enob: propagation in division 2



#Stuff for   %conv8 = sitofp i32 %i.0 to double, !taffo.info !27, !taffo.initweight !28
main_conv8_fixbits = solver.IntVar(0, 24, 'main_conv8_fixbits')
main_conv8_fixp = solver.IntVar(0, 1, 'main_conv8_fixp')
main_conv8_float = solver.IntVar(0, 1, 'main_conv8_float')
main_conv8_double = solver.IntVar(0, 1, 'main_conv8_double')
main_conv8_enob = solver.IntVar(-10000, 10000, 'main_conv8_enob')
solver.Add( + (1)*main_conv8_enob + (-1)*main_conv8_fixbits + (10000)*main_conv8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv8_enob + (10000)*main_conv8_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv8_enob + (10000)*main_conv8_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv8_fixbits + (-10000)*main_conv8_fixp>=-9977)    #Limit the lower number of frac bits24
enobCostObj +=  + (-1)*main_conv8_enob
solver.Add( + (1)*main_conv8_fixp + (1)*main_conv8_float + (1)*main_conv8_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv8_fixbits + (-10000)*main_conv8_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_conv8_enob<=1)    #Limiting Enob for integer to float conversion



#Constraint for cast for   %add = fadd double %div, %conv8, !taffo.info !39, !taffo.initweight !29
main_div_CAST_add_fixbits = solver.IntVar(0, 28, 'main_div_CAST_add_fixbits')
main_div_CAST_add_fixp = solver.IntVar(0, 1, 'main_div_CAST_add_fixp')
main_div_CAST_add_float = solver.IntVar(0, 1, 'main_div_CAST_add_float')
main_div_CAST_add_double = solver.IntVar(0, 1, 'main_div_CAST_add_double')
solver.Add( + (1)*main_div_CAST_add_fixp + (1)*main_div_CAST_add_float + (1)*main_div_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*main_div_CAST_add_fixbits + (-10000)*main_div_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div_CAST_add = solver.IntVar(0, 1, 'C1_main_div_CAST_add')
C2_main_div_CAST_add = solver.IntVar(0, 1, 'C2_main_div_CAST_add')
solver.Add( + (1)*main_div_fixbits + (-1)*main_div_CAST_add_fixbits + (-10000)*C1_main_div_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*main_div_fixbits + (1)*main_div_CAST_add_fixbits + (-10000)*C2_main_div_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div_CAST_add
castCostObj +=  + (1)*C2_main_div_CAST_add
C3_main_div_CAST_add = solver.IntVar(0, 1, 'C3_main_div_CAST_add')
C4_main_div_CAST_add = solver.IntVar(0, 1, 'C4_main_div_CAST_add')
C5_main_div_CAST_add = solver.IntVar(0, 1, 'C5_main_div_CAST_add')
C6_main_div_CAST_add = solver.IntVar(0, 1, 'C6_main_div_CAST_add')
C7_main_div_CAST_add = solver.IntVar(0, 1, 'C7_main_div_CAST_add')
C8_main_div_CAST_add = solver.IntVar(0, 1, 'C8_main_div_CAST_add')
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_add_float + (-1)*C3_main_div_CAST_add<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div_CAST_add
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_add_fixp + (-1)*C4_main_div_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div_CAST_add
solver.Add( + (1)*main_div_fixp + (1)*main_div_CAST_add_double + (-1)*C5_main_div_CAST_add<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div_CAST_add
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_add_fixp + (-1)*C6_main_div_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div_CAST_add
solver.Add( + (1)*main_div_float + (1)*main_div_CAST_add_double + (-1)*C7_main_div_CAST_add<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div_CAST_add
solver.Add( + (1)*main_div_double + (1)*main_div_CAST_add_float + (-1)*C8_main_div_CAST_add<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div_CAST_add



#Constraint for cast for   %add = fadd double %div, %conv8, !taffo.info !39, !taffo.initweight !29
main_conv8_CAST_add_fixbits = solver.IntVar(0, 24, 'main_conv8_CAST_add_fixbits')
main_conv8_CAST_add_fixp = solver.IntVar(0, 1, 'main_conv8_CAST_add_fixp')
main_conv8_CAST_add_float = solver.IntVar(0, 1, 'main_conv8_CAST_add_float')
main_conv8_CAST_add_double = solver.IntVar(0, 1, 'main_conv8_CAST_add_double')
solver.Add( + (1)*main_conv8_CAST_add_fixp + (1)*main_conv8_CAST_add_float + (1)*main_conv8_CAST_add_double==1)    #exactly 1 type
solver.Add( + (1)*main_conv8_CAST_add_fixbits + (-10000)*main_conv8_CAST_add_fixp<=0)    #If no fix, fix frac part = 0
C1_main_conv8_CAST_add = solver.IntVar(0, 1, 'C1_main_conv8_CAST_add')
C2_main_conv8_CAST_add = solver.IntVar(0, 1, 'C2_main_conv8_CAST_add')
solver.Add( + (1)*main_conv8_fixbits + (-1)*main_conv8_CAST_add_fixbits + (-10000)*C1_main_conv8_CAST_add<=0)    #Shift cost 1
solver.Add( + (-1)*main_conv8_fixbits + (1)*main_conv8_CAST_add_fixbits + (-10000)*C2_main_conv8_CAST_add<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_conv8_CAST_add
castCostObj +=  + (1)*C2_main_conv8_CAST_add
C3_main_conv8_CAST_add = solver.IntVar(0, 1, 'C3_main_conv8_CAST_add')
C4_main_conv8_CAST_add = solver.IntVar(0, 1, 'C4_main_conv8_CAST_add')
C5_main_conv8_CAST_add = solver.IntVar(0, 1, 'C5_main_conv8_CAST_add')
C6_main_conv8_CAST_add = solver.IntVar(0, 1, 'C6_main_conv8_CAST_add')
C7_main_conv8_CAST_add = solver.IntVar(0, 1, 'C7_main_conv8_CAST_add')
C8_main_conv8_CAST_add = solver.IntVar(0, 1, 'C8_main_conv8_CAST_add')
solver.Add( + (1)*main_conv8_fixp + (1)*main_conv8_CAST_add_float + (-1)*C3_main_conv8_CAST_add<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_conv8_CAST_add
solver.Add( + (1)*main_conv8_float + (1)*main_conv8_CAST_add_fixp + (-1)*C4_main_conv8_CAST_add<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_conv8_CAST_add
solver.Add( + (1)*main_conv8_fixp + (1)*main_conv8_CAST_add_double + (-1)*C5_main_conv8_CAST_add<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_conv8_CAST_add
solver.Add( + (1)*main_conv8_double + (1)*main_conv8_CAST_add_fixp + (-1)*C6_main_conv8_CAST_add<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_conv8_CAST_add
solver.Add( + (1)*main_conv8_float + (1)*main_conv8_CAST_add_double + (-1)*C7_main_conv8_CAST_add<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_conv8_CAST_add
solver.Add( + (1)*main_conv8_double + (1)*main_conv8_CAST_add_float + (-1)*C8_main_conv8_CAST_add<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_conv8_CAST_add



#Stuff for   %add = fadd double %div, %conv8, !taffo.info !39, !taffo.initweight !29
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
solver.Add( + (1)*main_div_CAST_add_fixp + (-1)*main_conv8_CAST_add_fixp==0)    #fix equality
solver.Add( + (1)*main_div_CAST_add_float + (-1)*main_conv8_CAST_add_float==0)    #float equality
solver.Add( + (1)*main_div_CAST_add_double + (-1)*main_conv8_CAST_add_double==0)    #double equality
solver.Add( + (1)*main_div_CAST_add_fixbits + (-1)*main_conv8_CAST_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_div_CAST_add_fixp + (-1)*main_add_fixp==0)    #fix equality
solver.Add( + (1)*main_div_CAST_add_float + (-1)*main_add_float==0)    #float equality
solver.Add( + (1)*main_div_CAST_add_double + (-1)*main_add_double==0)    #double equality
solver.Add( + (1)*main_div_CAST_add_fixbits + (-1)*main_add_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add_fixp
mathCostObj +=  + (2.33125)*main_add_float
mathCostObj +=  + (2.72422)*main_add_double
solver.Add( + (1)*main_add_enob + (-1)*main_div_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*main_conv8_enob<=0)    #Enob propagation in sum second addend



#Stuff for double 3.200000e+01
ConstantValue__2_fixbits = solver.IntVar(0, 26, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 3.200000e+01
ConstantValue__3_fixbits = solver.IntVar(0, 26, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div9 = fdiv double %add, 3.200000e+01, !taffo.info !41, !taffo.initweight !35, !taffo.constinfo !43
main_add_CAST_div9_fixbits = solver.IntVar(0, 24, 'main_add_CAST_div9_fixbits')
main_add_CAST_div9_fixp = solver.IntVar(0, 1, 'main_add_CAST_div9_fixp')
main_add_CAST_div9_float = solver.IntVar(0, 1, 'main_add_CAST_div9_float')
main_add_CAST_div9_double = solver.IntVar(0, 1, 'main_add_CAST_div9_double')
solver.Add( + (1)*main_add_CAST_div9_fixp + (1)*main_add_CAST_div9_float + (1)*main_add_CAST_div9_double==1)    #exactly 1 type
solver.Add( + (1)*main_add_CAST_div9_fixbits + (-10000)*main_add_CAST_div9_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add_CAST_div9 = solver.IntVar(0, 1, 'C1_main_add_CAST_div9')
C2_main_add_CAST_div9 = solver.IntVar(0, 1, 'C2_main_add_CAST_div9')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add_CAST_div9_fixbits + (-10000)*C1_main_add_CAST_div9<=0)    #Shift cost 1
solver.Add( + (-1)*main_add_fixbits + (1)*main_add_CAST_div9_fixbits + (-10000)*C2_main_add_CAST_div9<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add_CAST_div9
castCostObj +=  + (1)*C2_main_add_CAST_div9
C3_main_add_CAST_div9 = solver.IntVar(0, 1, 'C3_main_add_CAST_div9')
C4_main_add_CAST_div9 = solver.IntVar(0, 1, 'C4_main_add_CAST_div9')
C5_main_add_CAST_div9 = solver.IntVar(0, 1, 'C5_main_add_CAST_div9')
C6_main_add_CAST_div9 = solver.IntVar(0, 1, 'C6_main_add_CAST_div9')
C7_main_add_CAST_div9 = solver.IntVar(0, 1, 'C7_main_add_CAST_div9')
C8_main_add_CAST_div9 = solver.IntVar(0, 1, 'C8_main_add_CAST_div9')
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_div9_float + (-1)*C3_main_add_CAST_div9<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add_CAST_div9
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_div9_fixp + (-1)*C4_main_add_CAST_div9<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add_CAST_div9
solver.Add( + (1)*main_add_fixp + (1)*main_add_CAST_div9_double + (-1)*C5_main_add_CAST_div9<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add_CAST_div9
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_div9_fixp + (-1)*C6_main_add_CAST_div9<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add_CAST_div9
solver.Add( + (1)*main_add_float + (1)*main_add_CAST_div9_double + (-1)*C7_main_add_CAST_div9<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add_CAST_div9
solver.Add( + (1)*main_add_double + (1)*main_add_CAST_div9_float + (-1)*C8_main_add_CAST_div9<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add_CAST_div9



#Stuff for double 3.200000e+01
ConstantValue__4_fixbits = solver.IntVar(0, 26, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div9 = fdiv double %add, 3.200000e+01, !taffo.info !41, !taffo.initweight !35, !taffo.constinfo !43
ConstantValue__4_CAST_div9_fixbits = solver.IntVar(0, 26, 'ConstantValue__4_CAST_div9_fixbits')
ConstantValue__4_CAST_div9_fixp = solver.IntVar(0, 1, 'ConstantValue__4_CAST_div9_fixp')
ConstantValue__4_CAST_div9_float = solver.IntVar(0, 1, 'ConstantValue__4_CAST_div9_float')
ConstantValue__4_CAST_div9_double = solver.IntVar(0, 1, 'ConstantValue__4_CAST_div9_double')
solver.Add( + (1)*ConstantValue__4_CAST_div9_fixp + (1)*ConstantValue__4_CAST_div9_float + (1)*ConstantValue__4_CAST_div9_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__4_CAST_div9_fixbits + (-10000)*ConstantValue__4_CAST_div9_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C1_ConstantValue__4_CAST_div9')
C2_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C2_ConstantValue__4_CAST_div9')
solver.Add( + (1)*ConstantValue__4_fixbits + (-1)*ConstantValue__4_CAST_div9_fixbits + (-10000)*C1_ConstantValue__4_CAST_div9<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__4_fixbits + (1)*ConstantValue__4_CAST_div9_fixbits + (-10000)*C2_ConstantValue__4_CAST_div9<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__4_CAST_div9
castCostObj +=  + (1)*C2_ConstantValue__4_CAST_div9
C3_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_div9')
C4_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_div9')
C5_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_div9')
C6_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_div9')
C7_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_div9')
C8_ConstantValue__4_CAST_div9 = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_div9')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_div9_float + (-1)*C3_ConstantValue__4_CAST_div9<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__4_CAST_div9
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_div9_fixp + (-1)*C4_ConstantValue__4_CAST_div9<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__4_CAST_div9
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_div9_double + (-1)*C5_ConstantValue__4_CAST_div9<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__4_CAST_div9
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_div9_fixp + (-1)*C6_ConstantValue__4_CAST_div9<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__4_CAST_div9
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_div9_double + (-1)*C7_ConstantValue__4_CAST_div9<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__4_CAST_div9
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_div9_float + (-1)*C8_ConstantValue__4_CAST_div9<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__4_CAST_div9



#Stuff for   %div9 = fdiv double %add, 3.200000e+01, !taffo.info !41, !taffo.initweight !35, !taffo.constinfo !43
main_div9_fixbits = solver.IntVar(0, 28, 'main_div9_fixbits')
main_div9_fixp = solver.IntVar(0, 1, 'main_div9_fixp')
main_div9_float = solver.IntVar(0, 1, 'main_div9_float')
main_div9_double = solver.IntVar(0, 1, 'main_div9_double')
main_div9_enob = solver.IntVar(-10000, 10000, 'main_div9_enob')
solver.Add( + (1)*main_div9_enob + (-1)*main_div9_fixbits + (10000)*main_div9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div9_enob + (10000)*main_div9_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div9_enob + (10000)*main_div9_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div9_fixbits + (-10000)*main_div9_fixp>=-9973)    #Limit the lower number of frac bits28
enobCostObj +=  + (-1)*main_div9_enob
solver.Add( + (1)*main_div9_fixp + (1)*main_div9_float + (1)*main_div9_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div9_fixbits + (-10000)*main_div9_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add_CAST_div9_fixp + (-1)*ConstantValue__4_CAST_div9_fixp==0)    #fix equality
solver.Add( + (1)*main_add_CAST_div9_float + (-1)*ConstantValue__4_CAST_div9_float==0)    #float equality
solver.Add( + (1)*main_add_CAST_div9_double + (-1)*ConstantValue__4_CAST_div9_double==0)    #double equality
solver.Add( + (1)*main_add_CAST_div9_fixp + (-1)*main_div9_fixp==0)    #fix equality
solver.Add( + (1)*main_add_CAST_div9_float + (-1)*main_div9_float==0)    #float equality
solver.Add( + (1)*main_add_CAST_div9_double + (-1)*main_div9_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div9_fixp
mathCostObj +=  + (5.60026)*main_div9_float
mathCostObj +=  + (18.3266)*main_div9_double
main_main_div9_enob_1 = solver.IntVar(0, 1, 'main_main_div9_enob_1')
main_main_div9_enob_2 = solver.IntVar(0, 1, 'main_main_div9_enob_2')
solver.Add( + (1)*main_main_div9_enob_1 + (1)*main_main_div9_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div9_enob + (-1)*ConstantValue__2_enob + (-10000)*main_main_div9_enob_1<=1034)    #Enob: propagation in division 1
solver.Add( + (1)*main_div9_enob + (-1)*main_add_enob + (-10000)*main_main_div9_enob_2<=5)    #Enob: propagation in division 2



#Constraint for cast for   store double %div9, double* %arrayidx11, align 8, !taffo.info !8, !taffo.initweight !29
main_div9_CAST_store_fixbits = solver.IntVar(0, 28, 'main_div9_CAST_store_fixbits')
main_div9_CAST_store_fixp = solver.IntVar(0, 1, 'main_div9_CAST_store_fixp')
main_div9_CAST_store_float = solver.IntVar(0, 1, 'main_div9_CAST_store_float')
main_div9_CAST_store_double = solver.IntVar(0, 1, 'main_div9_CAST_store_double')
solver.Add( + (1)*main_div9_CAST_store_fixp + (1)*main_div9_CAST_store_float + (1)*main_div9_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div9_CAST_store_fixbits + (-10000)*main_div9_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div9_CAST_store = solver.IntVar(0, 1, 'C1_main_div9_CAST_store')
C2_main_div9_CAST_store = solver.IntVar(0, 1, 'C2_main_div9_CAST_store')
solver.Add( + (1)*main_div9_fixbits + (-1)*main_div9_CAST_store_fixbits + (-10000)*C1_main_div9_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div9_fixbits + (1)*main_div9_CAST_store_fixbits + (-10000)*C2_main_div9_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div9_CAST_store
castCostObj +=  + (1)*C2_main_div9_CAST_store
C3_main_div9_CAST_store = solver.IntVar(0, 1, 'C3_main_div9_CAST_store')
C4_main_div9_CAST_store = solver.IntVar(0, 1, 'C4_main_div9_CAST_store')
C5_main_div9_CAST_store = solver.IntVar(0, 1, 'C5_main_div9_CAST_store')
C6_main_div9_CAST_store = solver.IntVar(0, 1, 'C6_main_div9_CAST_store')
C7_main_div9_CAST_store = solver.IntVar(0, 1, 'C7_main_div9_CAST_store')
C8_main_div9_CAST_store = solver.IntVar(0, 1, 'C8_main_div9_CAST_store')
solver.Add( + (1)*main_div9_fixp + (1)*main_div9_CAST_store_float + (-1)*C3_main_div9_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div9_CAST_store
solver.Add( + (1)*main_div9_float + (1)*main_div9_CAST_store_fixp + (-1)*C4_main_div9_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div9_CAST_store
solver.Add( + (1)*main_div9_fixp + (1)*main_div9_CAST_store_double + (-1)*C5_main_div9_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div9_CAST_store
solver.Add( + (1)*main_div9_double + (1)*main_div9_CAST_store_fixp + (-1)*C6_main_div9_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div9_CAST_store
solver.Add( + (1)*main_div9_float + (1)*main_div9_CAST_store_double + (-1)*C7_main_div9_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div9_CAST_store
solver.Add( + (1)*main_div9_double + (1)*main_div9_CAST_store_float + (-1)*C8_main_div9_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div9_CAST_store
solver.Add( + (1)*data_fixp + (-1)*main_div9_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*data_float + (-1)*main_div9_CAST_store_float==0)    #float equality
solver.Add( + (1)*data_double + (-1)*main_div9_CAST_store_double==0)    #double equality
solver.Add( + (1)*data_fixbits + (-1)*main_div9_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
data_enob_storeENOB = solver.IntVar(-10000, 10000, 'data_enob_storeENOB')
solver.Add( + (1)*data_enob_storeENOB + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob_storeENOB + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob_storeENOB + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_enob_storeENOB + (-1)*main_div9_enob<=0)    #Enob constraint ENOB propagation in load/store



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



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx21, align 8, !taffo.info !12, !taffo.initweight !28, !taffo.constinfo !48
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
solver.Add( + (1)*mean_fixp + (-1)*ConstantValue__6_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*ConstantValue__6_CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*ConstantValue__6_CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*ConstantValue__6_CAST_store_fixbits==0)    #same fractional bit

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



#Constraint for cast for   %add32 = fadd double %tmp1, %tmp, !taffo.info !49, !taffo.initweight !29
mean_CAST_add32_fixbits = solver.IntVar(0, 15, 'mean_CAST_add32_fixbits')
mean_CAST_add32_fixp = solver.IntVar(0, 1, 'mean_CAST_add32_fixp')
mean_CAST_add32_float = solver.IntVar(0, 1, 'mean_CAST_add32_float')
mean_CAST_add32_double = solver.IntVar(0, 1, 'mean_CAST_add32_double')
solver.Add( + (1)*mean_CAST_add32_fixp + (1)*mean_CAST_add32_float + (1)*mean_CAST_add32_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_add32_fixbits + (-10000)*mean_CAST_add32_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_add32 = solver.IntVar(0, 1, 'C1_mean_CAST_add32')
C2_mean_CAST_add32 = solver.IntVar(0, 1, 'C2_mean_CAST_add32')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_add32_fixbits + (-10000)*C1_mean_CAST_add32<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_add32_fixbits + (-10000)*C2_mean_CAST_add32<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mean_CAST_add32
castCostObj +=  + (1)*C2_mean_CAST_add32
C3_mean_CAST_add32 = solver.IntVar(0, 1, 'C3_mean_CAST_add32')
C4_mean_CAST_add32 = solver.IntVar(0, 1, 'C4_mean_CAST_add32')
C5_mean_CAST_add32 = solver.IntVar(0, 1, 'C5_mean_CAST_add32')
C6_mean_CAST_add32 = solver.IntVar(0, 1, 'C6_mean_CAST_add32')
C7_mean_CAST_add32 = solver.IntVar(0, 1, 'C7_mean_CAST_add32')
C8_mean_CAST_add32 = solver.IntVar(0, 1, 'C8_mean_CAST_add32')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_add32_float + (-1)*C3_mean_CAST_add32<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_mean_CAST_add32
solver.Add( + (1)*mean_float + (1)*mean_CAST_add32_fixp + (-1)*C4_mean_CAST_add32<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_mean_CAST_add32
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_add32_double + (-1)*C5_mean_CAST_add32<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_mean_CAST_add32
solver.Add( + (1)*mean_double + (1)*mean_CAST_add32_fixp + (-1)*C6_mean_CAST_add32<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_mean_CAST_add32
solver.Add( + (1)*mean_float + (1)*mean_CAST_add32_double + (-1)*C7_mean_CAST_add32<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_mean_CAST_add32
solver.Add( + (1)*mean_double + (1)*mean_CAST_add32_float + (-1)*C8_mean_CAST_add32<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_mean_CAST_add32



#Constraint for cast for   %add32 = fadd double %tmp1, %tmp, !taffo.info !49, !taffo.initweight !29
data_CAST_add32_fixbits = solver.IntVar(0, 27, 'data_CAST_add32_fixbits')
data_CAST_add32_fixp = solver.IntVar(0, 1, 'data_CAST_add32_fixp')
data_CAST_add32_float = solver.IntVar(0, 1, 'data_CAST_add32_float')
data_CAST_add32_double = solver.IntVar(0, 1, 'data_CAST_add32_double')
solver.Add( + (1)*data_CAST_add32_fixp + (1)*data_CAST_add32_float + (1)*data_CAST_add32_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_add32_fixbits + (-10000)*data_CAST_add32_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_add32 = solver.IntVar(0, 1, 'C1_data_CAST_add32')
C2_data_CAST_add32 = solver.IntVar(0, 1, 'C2_data_CAST_add32')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_add32_fixbits + (-10000)*C1_data_CAST_add32<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_add32_fixbits + (-10000)*C2_data_CAST_add32<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_add32
castCostObj +=  + (1)*C2_data_CAST_add32
C3_data_CAST_add32 = solver.IntVar(0, 1, 'C3_data_CAST_add32')
C4_data_CAST_add32 = solver.IntVar(0, 1, 'C4_data_CAST_add32')
C5_data_CAST_add32 = solver.IntVar(0, 1, 'C5_data_CAST_add32')
C6_data_CAST_add32 = solver.IntVar(0, 1, 'C6_data_CAST_add32')
C7_data_CAST_add32 = solver.IntVar(0, 1, 'C7_data_CAST_add32')
C8_data_CAST_add32 = solver.IntVar(0, 1, 'C8_data_CAST_add32')
solver.Add( + (1)*data_fixp + (1)*data_CAST_add32_float + (-1)*C3_data_CAST_add32<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_data_CAST_add32
solver.Add( + (1)*data_float + (1)*data_CAST_add32_fixp + (-1)*C4_data_CAST_add32<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_data_CAST_add32
solver.Add( + (1)*data_fixp + (1)*data_CAST_add32_double + (-1)*C5_data_CAST_add32<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_data_CAST_add32
solver.Add( + (1)*data_double + (1)*data_CAST_add32_fixp + (-1)*C6_data_CAST_add32<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_data_CAST_add32
solver.Add( + (1)*data_float + (1)*data_CAST_add32_double + (-1)*C7_data_CAST_add32<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_data_CAST_add32
solver.Add( + (1)*data_double + (1)*data_CAST_add32_float + (-1)*C8_data_CAST_add32<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_data_CAST_add32



#Stuff for   %add32 = fadd double %tmp1, %tmp, !taffo.info !49, !taffo.initweight !29
main_add32_fixbits = solver.IntVar(0, 15, 'main_add32_fixbits')
main_add32_fixp = solver.IntVar(0, 1, 'main_add32_fixp')
main_add32_float = solver.IntVar(0, 1, 'main_add32_float')
main_add32_double = solver.IntVar(0, 1, 'main_add32_double')
main_add32_enob = solver.IntVar(-10000, 10000, 'main_add32_enob')
solver.Add( + (1)*main_add32_enob + (-1)*main_add32_fixbits + (10000)*main_add32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add32_enob + (10000)*main_add32_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add32_enob + (10000)*main_add32_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add32_fixbits + (-10000)*main_add32_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_add32_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add32_enob
solver.Add( + (1)*main_add32_fixp + (1)*main_add32_float + (1)*main_add32_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add32_fixbits + (-10000)*main_add32_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*mean_CAST_add32_fixp + (-1)*data_CAST_add32_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_add32_float + (-1)*data_CAST_add32_float==0)    #float equality
solver.Add( + (1)*mean_CAST_add32_double + (-1)*data_CAST_add32_double==0)    #double equality
solver.Add( + (1)*mean_CAST_add32_fixbits + (-1)*data_CAST_add32_fixbits==0)    #same fractional bit
solver.Add( + (1)*mean_CAST_add32_fixp + (-1)*main_add32_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_add32_float + (-1)*main_add32_float==0)    #float equality
solver.Add( + (1)*mean_CAST_add32_double + (-1)*main_add32_double==0)    #double equality
solver.Add( + (1)*mean_CAST_add32_fixbits + (-1)*main_add32_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add32_fixp
mathCostObj +=  + (2.33125)*main_add32_float
mathCostObj +=  + (2.72422)*main_add32_double
solver.Add( + (1)*main_add32_enob + (-1)*mean_enob_memphi_main_tmp1<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add32_enob + (-1)*data_enob_memphi_main_tmp<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add32, double* %arrayidx31, align 8, !taffo.info !12, !taffo.initweight !28
main_add32_CAST_store_fixbits = solver.IntVar(0, 15, 'main_add32_CAST_store_fixbits')
main_add32_CAST_store_fixp = solver.IntVar(0, 1, 'main_add32_CAST_store_fixp')
main_add32_CAST_store_float = solver.IntVar(0, 1, 'main_add32_CAST_store_float')
main_add32_CAST_store_double = solver.IntVar(0, 1, 'main_add32_CAST_store_double')
solver.Add( + (1)*main_add32_CAST_store_fixp + (1)*main_add32_CAST_store_float + (1)*main_add32_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add32_CAST_store_fixbits + (-10000)*main_add32_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add32_CAST_store = solver.IntVar(0, 1, 'C1_main_add32_CAST_store')
C2_main_add32_CAST_store = solver.IntVar(0, 1, 'C2_main_add32_CAST_store')
solver.Add( + (1)*main_add32_fixbits + (-1)*main_add32_CAST_store_fixbits + (-10000)*C1_main_add32_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add32_fixbits + (1)*main_add32_CAST_store_fixbits + (-10000)*C2_main_add32_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add32_CAST_store
castCostObj +=  + (1)*C2_main_add32_CAST_store
C3_main_add32_CAST_store = solver.IntVar(0, 1, 'C3_main_add32_CAST_store')
C4_main_add32_CAST_store = solver.IntVar(0, 1, 'C4_main_add32_CAST_store')
C5_main_add32_CAST_store = solver.IntVar(0, 1, 'C5_main_add32_CAST_store')
C6_main_add32_CAST_store = solver.IntVar(0, 1, 'C6_main_add32_CAST_store')
C7_main_add32_CAST_store = solver.IntVar(0, 1, 'C7_main_add32_CAST_store')
C8_main_add32_CAST_store = solver.IntVar(0, 1, 'C8_main_add32_CAST_store')
solver.Add( + (1)*main_add32_fixp + (1)*main_add32_CAST_store_float + (-1)*C3_main_add32_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add32_CAST_store
solver.Add( + (1)*main_add32_float + (1)*main_add32_CAST_store_fixp + (-1)*C4_main_add32_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add32_CAST_store
solver.Add( + (1)*main_add32_fixp + (1)*main_add32_CAST_store_double + (-1)*C5_main_add32_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add32_CAST_store
solver.Add( + (1)*main_add32_double + (1)*main_add32_CAST_store_fixp + (-1)*C6_main_add32_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add32_CAST_store
solver.Add( + (1)*main_add32_float + (1)*main_add32_CAST_store_double + (-1)*C7_main_add32_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add32_CAST_store
solver.Add( + (1)*main_add32_double + (1)*main_add32_CAST_store_float + (-1)*C8_main_add32_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add32_CAST_store
solver.Add( + (1)*mean_fixp + (-1)*main_add32_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mean_float + (-1)*main_add32_CAST_store_float==0)    #float equality
solver.Add( + (1)*mean_double + (-1)*main_add32_CAST_store_double==0)    #double equality
solver.Add( + (1)*mean_fixbits + (-1)*main_add32_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
mean_enob_storeENOB = solver.IntVar(-10000, 10000, 'mean_enob_storeENOB')
solver.Add( + (1)*mean_enob_storeENOB + (-1)*mean_fixbits + (10000)*mean_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mean_enob_storeENOB + (10000)*mean_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mean_enob_storeENOB + (10000)*mean_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mean_enob_storeENOB + (-1)*main_add32_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp1 + (-1)*mean_enob_storeENOB + (10000)*main_main_tmp1_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
mean_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp2')
solver.Add( + (1)*mean_enob_memphi_main_tmp2 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp2_enob_1 = solver.IntVar(0, 1, 'main_main_tmp2_enob_1')
solver.Add( + (1)*main_main_tmp2_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp2 + (-1)*mean_enob_storeENOB + (10000)*main_main_tmp2_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 3.200000e+01
ConstantValue__7_fixbits = solver.IntVar(0, 26, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 3.200000e+01
ConstantValue__8_fixbits = solver.IntVar(0, 26, 'ConstantValue__8_fixbits')
ConstantValue__8_fixp = solver.IntVar(0, 1, 'ConstantValue__8_fixp')
ConstantValue__8_float = solver.IntVar(0, 1, 'ConstantValue__8_float')
ConstantValue__8_double = solver.IntVar(0, 1, 'ConstantValue__8_double')
ConstantValue__8_enob = solver.IntVar(-10000, 10000, 'ConstantValue__8_enob')
solver.Add( + (1)*ConstantValue__8_enob + (-1)*ConstantValue__8_fixbits + (10000)*ConstantValue__8_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__8_enob + (10000)*ConstantValue__8_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_float + (1)*ConstantValue__8_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__8_fixbits + (-10000)*ConstantValue__8_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div38 = fdiv double %tmp2, 3.200000e+01, !taffo.info !51, !taffo.initweight !28, !taffo.constinfo !43
mean_CAST_div38_fixbits = solver.IntVar(0, 15, 'mean_CAST_div38_fixbits')
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
castCostObj +=  + (6.62652)*C3_mean_CAST_div38
solver.Add( + (1)*mean_float + (1)*mean_CAST_div38_fixp + (-1)*C4_mean_CAST_div38<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_mean_CAST_div38
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_div38_double + (-1)*C5_mean_CAST_div38<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_mean_CAST_div38
solver.Add( + (1)*mean_double + (1)*mean_CAST_div38_fixp + (-1)*C6_mean_CAST_div38<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_mean_CAST_div38
solver.Add( + (1)*mean_float + (1)*mean_CAST_div38_double + (-1)*C7_mean_CAST_div38<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_mean_CAST_div38
solver.Add( + (1)*mean_double + (1)*mean_CAST_div38_float + (-1)*C8_mean_CAST_div38<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_mean_CAST_div38



#Stuff for double 3.200000e+01
ConstantValue__9_fixbits = solver.IntVar(0, 26, 'ConstantValue__9_fixbits')
ConstantValue__9_fixp = solver.IntVar(0, 1, 'ConstantValue__9_fixp')
ConstantValue__9_float = solver.IntVar(0, 1, 'ConstantValue__9_float')
ConstantValue__9_double = solver.IntVar(0, 1, 'ConstantValue__9_double')
ConstantValue__9_enob = solver.IntVar(-10000, 10000, 'ConstantValue__9_enob')
solver.Add( + (1)*ConstantValue__9_enob + (-1)*ConstantValue__9_fixbits + (10000)*ConstantValue__9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_float + (1)*ConstantValue__9_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div38 = fdiv double %tmp2, 3.200000e+01, !taffo.info !51, !taffo.initweight !28, !taffo.constinfo !43
ConstantValue__9_CAST_div38_fixbits = solver.IntVar(0, 26, 'ConstantValue__9_CAST_div38_fixbits')
ConstantValue__9_CAST_div38_fixp = solver.IntVar(0, 1, 'ConstantValue__9_CAST_div38_fixp')
ConstantValue__9_CAST_div38_float = solver.IntVar(0, 1, 'ConstantValue__9_CAST_div38_float')
ConstantValue__9_CAST_div38_double = solver.IntVar(0, 1, 'ConstantValue__9_CAST_div38_double')
solver.Add( + (1)*ConstantValue__9_CAST_div38_fixp + (1)*ConstantValue__9_CAST_div38_float + (1)*ConstantValue__9_CAST_div38_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__9_CAST_div38_fixbits + (-10000)*ConstantValue__9_CAST_div38_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C1_ConstantValue__9_CAST_div38')
C2_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C2_ConstantValue__9_CAST_div38')
solver.Add( + (1)*ConstantValue__9_fixbits + (-1)*ConstantValue__9_CAST_div38_fixbits + (-10000)*C1_ConstantValue__9_CAST_div38<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__9_fixbits + (1)*ConstantValue__9_CAST_div38_fixbits + (-10000)*C2_ConstantValue__9_CAST_div38<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__9_CAST_div38
castCostObj +=  + (1)*C2_ConstantValue__9_CAST_div38
C3_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C3_ConstantValue__9_CAST_div38')
C4_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C4_ConstantValue__9_CAST_div38')
C5_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C5_ConstantValue__9_CAST_div38')
C6_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C6_ConstantValue__9_CAST_div38')
C7_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C7_ConstantValue__9_CAST_div38')
C8_ConstantValue__9_CAST_div38 = solver.IntVar(0, 1, 'C8_ConstantValue__9_CAST_div38')
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_CAST_div38_float + (-1)*C3_ConstantValue__9_CAST_div38<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__9_CAST_div38
solver.Add( + (1)*ConstantValue__9_float + (1)*ConstantValue__9_CAST_div38_fixp + (-1)*C4_ConstantValue__9_CAST_div38<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__9_CAST_div38
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_CAST_div38_double + (-1)*C5_ConstantValue__9_CAST_div38<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__9_CAST_div38
solver.Add( + (1)*ConstantValue__9_double + (1)*ConstantValue__9_CAST_div38_fixp + (-1)*C6_ConstantValue__9_CAST_div38<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__9_CAST_div38
solver.Add( + (1)*ConstantValue__9_float + (1)*ConstantValue__9_CAST_div38_double + (-1)*C7_ConstantValue__9_CAST_div38<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__9_CAST_div38
solver.Add( + (1)*ConstantValue__9_double + (1)*ConstantValue__9_CAST_div38_float + (-1)*C8_ConstantValue__9_CAST_div38<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__9_CAST_div38



#Stuff for   %div38 = fdiv double %tmp2, 3.200000e+01, !taffo.info !51, !taffo.initweight !28, !taffo.constinfo !43
main_div38_fixbits = solver.IntVar(0, 20, 'main_div38_fixbits')
main_div38_fixp = solver.IntVar(0, 1, 'main_div38_fixp')
main_div38_float = solver.IntVar(0, 1, 'main_div38_float')
main_div38_double = solver.IntVar(0, 1, 'main_div38_double')
main_div38_enob = solver.IntVar(-10000, 10000, 'main_div38_enob')
solver.Add( + (1)*main_div38_enob + (-1)*main_div38_fixbits + (10000)*main_div38_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div38_enob + (10000)*main_div38_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div38_enob + (10000)*main_div38_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div38_fixbits + (-10000)*main_div38_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_div38_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_div38_enob
solver.Add( + (1)*main_div38_fixp + (1)*main_div38_float + (1)*main_div38_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div38_fixbits + (-10000)*main_div38_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*mean_CAST_div38_fixp + (-1)*ConstantValue__9_CAST_div38_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_div38_float + (-1)*ConstantValue__9_CAST_div38_float==0)    #float equality
solver.Add( + (1)*mean_CAST_div38_double + (-1)*ConstantValue__9_CAST_div38_double==0)    #double equality
solver.Add( + (1)*mean_CAST_div38_fixp + (-1)*main_div38_fixp==0)    #fix equality
solver.Add( + (1)*mean_CAST_div38_float + (-1)*main_div38_float==0)    #float equality
solver.Add( + (1)*mean_CAST_div38_double + (-1)*main_div38_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div38_fixp
mathCostObj +=  + (5.60026)*main_div38_float
mathCostObj +=  + (18.3266)*main_div38_double
main_main_div38_enob_1 = solver.IntVar(0, 1, 'main_main_div38_enob_1')
main_main_div38_enob_2 = solver.IntVar(0, 1, 'main_main_div38_enob_2')
solver.Add( + (1)*main_main_div38_enob_1 + (1)*main_main_div38_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div38_enob + (-1)*ConstantValue__7_enob + (-10000)*main_main_div38_enob_1<=1034)    #Enob: propagation in division 1
solver.Add( + (1)*main_div38_enob + (-1)*mean_enob_memphi_main_tmp2 + (-10000)*main_main_div38_enob_2<=5)    #Enob: propagation in division 2



#Constraint for cast for   store double %div38, double* %arrayidx37, align 8, !taffo.info !12, !taffo.initweight !28
main_div38_CAST_store_fixbits = solver.IntVar(0, 20, 'main_div38_CAST_store_fixbits')
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
castCostObj +=  + (6.62652)*C3_main_div38_CAST_store
solver.Add( + (1)*main_div38_float + (1)*main_div38_CAST_store_fixp + (-1)*C4_main_div38_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div38_CAST_store
solver.Add( + (1)*main_div38_fixp + (1)*main_div38_CAST_store_double + (-1)*C5_main_div38_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div38_CAST_store
solver.Add( + (1)*main_div38_double + (1)*main_div38_CAST_store_fixp + (-1)*C6_main_div38_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div38_CAST_store
solver.Add( + (1)*main_div38_float + (1)*main_div38_CAST_store_double + (-1)*C7_main_div38_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div38_CAST_store
solver.Add( + (1)*main_div38_double + (1)*main_div38_CAST_store_float + (-1)*C8_main_div38_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div38_CAST_store
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



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx47, align 8, !taffo.info !14, !taffo.initweight !28, !taffo.constinfo !48
ConstantValue__11_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__11_CAST_store_fixbits')
ConstantValue__11_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__11_CAST_store_fixp')
ConstantValue__11_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__11_CAST_store_float')
ConstantValue__11_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__11_CAST_store_double')
solver.Add( + (1)*ConstantValue__11_CAST_store_fixp + (1)*ConstantValue__11_CAST_store_float + (1)*ConstantValue__11_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__11_CAST_store_fixbits + (-10000)*ConstantValue__11_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__11_CAST_store')
C2_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__11_CAST_store')
solver.Add( + (1)*ConstantValue__11_fixbits + (-1)*ConstantValue__11_CAST_store_fixbits + (-10000)*C1_ConstantValue__11_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__11_fixbits + (1)*ConstantValue__11_CAST_store_fixbits + (-10000)*C2_ConstantValue__11_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__11_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__11_CAST_store
C3_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__11_CAST_store')
C4_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__11_CAST_store')
C5_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__11_CAST_store')
C6_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__11_CAST_store')
C7_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__11_CAST_store')
C8_ConstantValue__11_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__11_CAST_store')
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_CAST_store_float + (-1)*C3_ConstantValue__11_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__11_CAST_store
solver.Add( + (1)*ConstantValue__11_float + (1)*ConstantValue__11_CAST_store_fixp + (-1)*C4_ConstantValue__11_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__11_CAST_store
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_CAST_store_double + (-1)*C5_ConstantValue__11_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__11_CAST_store
solver.Add( + (1)*ConstantValue__11_double + (1)*ConstantValue__11_CAST_store_fixp + (-1)*C6_ConstantValue__11_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__11_CAST_store
solver.Add( + (1)*ConstantValue__11_float + (1)*ConstantValue__11_CAST_store_double + (-1)*C7_ConstantValue__11_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__11_CAST_store
solver.Add( + (1)*ConstantValue__11_double + (1)*ConstantValue__11_CAST_store_float + (-1)*C8_ConstantValue__11_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__11_CAST_store
solver.Add( + (1)*stddev_fixp + (-1)*ConstantValue__11_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*stddev_float + (-1)*ConstantValue__11_CAST_store_float==0)    #float equality
solver.Add( + (1)*stddev_double + (-1)*ConstantValue__11_CAST_store_double==0)    #double equality
solver.Add( + (1)*stddev_fixbits + (-1)*ConstantValue__11_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp3')
solver.Add( + (1)*data_enob_memphi_main_tmp3 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp3_enob_1 = solver.IntVar(0, 1, 'main_main_tmp3_enob_1')
main_main_tmp3_enob_2 = solver.IntVar(0, 1, 'main_main_tmp3_enob_2')
main_main_tmp3_enob_3 = solver.IntVar(0, 1, 'main_main_tmp3_enob_3')
solver.Add( + (1)*main_main_tmp3_enob_1 + (1)*main_main_tmp3_enob_2 + (1)*main_main_tmp3_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp3 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp3_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp3 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
mean_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp4')
solver.Add( + (1)*mean_enob_memphi_main_tmp4 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp4_enob_1 = solver.IntVar(0, 1, 'main_main_tmp4_enob_1')
main_main_tmp4_enob_2 = solver.IntVar(0, 1, 'main_main_tmp4_enob_2')
main_main_tmp4_enob_3 = solver.IntVar(0, 1, 'main_main_tmp4_enob_3')
solver.Add( + (1)*main_main_tmp4_enob_1 + (1)*main_main_tmp4_enob_2 + (1)*main_main_tmp4_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp4 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp4_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp4 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub = fsub double %tmp3, %tmp4, !taffo.info !49, !taffo.initweight !29
data_CAST_sub_fixbits = solver.IntVar(0, 27, 'data_CAST_sub_fixbits')
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
castCostObj +=  + (6.62652)*C3_data_CAST_sub
solver.Add( + (1)*data_float + (1)*data_CAST_sub_fixp + (-1)*C4_data_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_data_CAST_sub
solver.Add( + (1)*data_fixp + (1)*data_CAST_sub_double + (-1)*C5_data_CAST_sub<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_data_CAST_sub
solver.Add( + (1)*data_double + (1)*data_CAST_sub_fixp + (-1)*C6_data_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_data_CAST_sub
solver.Add( + (1)*data_float + (1)*data_CAST_sub_double + (-1)*C7_data_CAST_sub<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_data_CAST_sub
solver.Add( + (1)*data_double + (1)*data_CAST_sub_float + (-1)*C8_data_CAST_sub<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_data_CAST_sub



#Constraint for cast for   %sub = fsub double %tmp3, %tmp4, !taffo.info !49, !taffo.initweight !29
mean_CAST_sub_fixbits = solver.IntVar(0, 15, 'mean_CAST_sub_fixbits')
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
castCostObj +=  + (6.62652)*C3_mean_CAST_sub
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub_fixp + (-1)*C4_mean_CAST_sub<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_mean_CAST_sub
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_sub_double + (-1)*C5_mean_CAST_sub<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_mean_CAST_sub
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub_fixp + (-1)*C6_mean_CAST_sub<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_mean_CAST_sub
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub_double + (-1)*C7_mean_CAST_sub<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_mean_CAST_sub
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub_float + (-1)*C8_mean_CAST_sub<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_mean_CAST_sub



#Stuff for   %sub = fsub double %tmp3, %tmp4, !taffo.info !49, !taffo.initweight !29
main_sub_fixbits = solver.IntVar(0, 15, 'main_sub_fixbits')
main_sub_fixp = solver.IntVar(0, 1, 'main_sub_fixp')
main_sub_float = solver.IntVar(0, 1, 'main_sub_float')
main_sub_double = solver.IntVar(0, 1, 'main_sub_double')
main_sub_enob = solver.IntVar(-10000, 10000, 'main_sub_enob')
solver.Add( + (1)*main_sub_enob + (-1)*main_sub_fixbits + (10000)*main_sub_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub_enob + (10000)*main_sub_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub_fixbits + (-10000)*main_sub_fixp>=-9986)    #Limit the lower number of frac bits15
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
mathCostObj +=  + (1.24179)*main_sub_fixp
mathCostObj +=  + (2.33125)*main_sub_float
mathCostObj +=  + (2.72422)*main_sub_double
solver.Add( + (1)*main_sub_enob + (-1)*data_enob_memphi_main_tmp3<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub_enob + (-1)*mean_enob_memphi_main_tmp4<=0)    #Enob propagation in sub second addend

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

#Restriction for new enob [LOAD]
mean_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp6')
solver.Add( + (1)*mean_enob_memphi_main_tmp6 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp6_enob_1 = solver.IntVar(0, 1, 'main_main_tmp6_enob_1')
main_main_tmp6_enob_2 = solver.IntVar(0, 1, 'main_main_tmp6_enob_2')
main_main_tmp6_enob_3 = solver.IntVar(0, 1, 'main_main_tmp6_enob_3')
solver.Add( + (1)*main_main_tmp6_enob_1 + (1)*main_main_tmp6_enob_2 + (1)*main_main_tmp6_enob_3==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp6 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp6_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp6 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_2<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub64 = fsub double %tmp5, %tmp6, !taffo.info !49, !taffo.initweight !29
data_CAST_sub64_fixbits = solver.IntVar(0, 27, 'data_CAST_sub64_fixbits')
data_CAST_sub64_fixp = solver.IntVar(0, 1, 'data_CAST_sub64_fixp')
data_CAST_sub64_float = solver.IntVar(0, 1, 'data_CAST_sub64_float')
data_CAST_sub64_double = solver.IntVar(0, 1, 'data_CAST_sub64_double')
solver.Add( + (1)*data_CAST_sub64_fixp + (1)*data_CAST_sub64_float + (1)*data_CAST_sub64_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_sub64_fixbits + (-10000)*data_CAST_sub64_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_sub64 = solver.IntVar(0, 1, 'C1_data_CAST_sub64')
C2_data_CAST_sub64 = solver.IntVar(0, 1, 'C2_data_CAST_sub64')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_sub64_fixbits + (-10000)*C1_data_CAST_sub64<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_sub64_fixbits + (-10000)*C2_data_CAST_sub64<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_sub64
castCostObj +=  + (1)*C2_data_CAST_sub64
C3_data_CAST_sub64 = solver.IntVar(0, 1, 'C3_data_CAST_sub64')
C4_data_CAST_sub64 = solver.IntVar(0, 1, 'C4_data_CAST_sub64')
C5_data_CAST_sub64 = solver.IntVar(0, 1, 'C5_data_CAST_sub64')
C6_data_CAST_sub64 = solver.IntVar(0, 1, 'C6_data_CAST_sub64')
C7_data_CAST_sub64 = solver.IntVar(0, 1, 'C7_data_CAST_sub64')
C8_data_CAST_sub64 = solver.IntVar(0, 1, 'C8_data_CAST_sub64')
solver.Add( + (1)*data_fixp + (1)*data_CAST_sub64_float + (-1)*C3_data_CAST_sub64<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_data_CAST_sub64
solver.Add( + (1)*data_float + (1)*data_CAST_sub64_fixp + (-1)*C4_data_CAST_sub64<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_data_CAST_sub64
solver.Add( + (1)*data_fixp + (1)*data_CAST_sub64_double + (-1)*C5_data_CAST_sub64<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_data_CAST_sub64
solver.Add( + (1)*data_double + (1)*data_CAST_sub64_fixp + (-1)*C6_data_CAST_sub64<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_data_CAST_sub64
solver.Add( + (1)*data_float + (1)*data_CAST_sub64_double + (-1)*C7_data_CAST_sub64<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_data_CAST_sub64
solver.Add( + (1)*data_double + (1)*data_CAST_sub64_float + (-1)*C8_data_CAST_sub64<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_data_CAST_sub64



#Constraint for cast for   %sub64 = fsub double %tmp5, %tmp6, !taffo.info !49, !taffo.initweight !29
mean_CAST_sub64_fixbits = solver.IntVar(0, 15, 'mean_CAST_sub64_fixbits')
mean_CAST_sub64_fixp = solver.IntVar(0, 1, 'mean_CAST_sub64_fixp')
mean_CAST_sub64_float = solver.IntVar(0, 1, 'mean_CAST_sub64_float')
mean_CAST_sub64_double = solver.IntVar(0, 1, 'mean_CAST_sub64_double')
solver.Add( + (1)*mean_CAST_sub64_fixp + (1)*mean_CAST_sub64_float + (1)*mean_CAST_sub64_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_sub64_fixbits + (-10000)*mean_CAST_sub64_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_sub64 = solver.IntVar(0, 1, 'C1_mean_CAST_sub64')
C2_mean_CAST_sub64 = solver.IntVar(0, 1, 'C2_mean_CAST_sub64')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_sub64_fixbits + (-10000)*C1_mean_CAST_sub64<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_sub64_fixbits + (-10000)*C2_mean_CAST_sub64<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mean_CAST_sub64
castCostObj +=  + (1)*C2_mean_CAST_sub64
C3_mean_CAST_sub64 = solver.IntVar(0, 1, 'C3_mean_CAST_sub64')
C4_mean_CAST_sub64 = solver.IntVar(0, 1, 'C4_mean_CAST_sub64')
C5_mean_CAST_sub64 = solver.IntVar(0, 1, 'C5_mean_CAST_sub64')
C6_mean_CAST_sub64 = solver.IntVar(0, 1, 'C6_mean_CAST_sub64')
C7_mean_CAST_sub64 = solver.IntVar(0, 1, 'C7_mean_CAST_sub64')
C8_mean_CAST_sub64 = solver.IntVar(0, 1, 'C8_mean_CAST_sub64')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_sub64_float + (-1)*C3_mean_CAST_sub64<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_mean_CAST_sub64
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub64_fixp + (-1)*C4_mean_CAST_sub64<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_mean_CAST_sub64
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_sub64_double + (-1)*C5_mean_CAST_sub64<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_mean_CAST_sub64
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub64_fixp + (-1)*C6_mean_CAST_sub64<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_mean_CAST_sub64
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub64_double + (-1)*C7_mean_CAST_sub64<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_mean_CAST_sub64
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub64_float + (-1)*C8_mean_CAST_sub64<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_mean_CAST_sub64



#Stuff for   %sub64 = fsub double %tmp5, %tmp6, !taffo.info !49, !taffo.initweight !29
main_sub64_fixbits = solver.IntVar(0, 15, 'main_sub64_fixbits')
main_sub64_fixp = solver.IntVar(0, 1, 'main_sub64_fixp')
main_sub64_float = solver.IntVar(0, 1, 'main_sub64_float')
main_sub64_double = solver.IntVar(0, 1, 'main_sub64_double')
main_sub64_enob = solver.IntVar(-10000, 10000, 'main_sub64_enob')
solver.Add( + (1)*main_sub64_enob + (-1)*main_sub64_fixbits + (10000)*main_sub64_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub64_enob + (10000)*main_sub64_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub64_enob + (10000)*main_sub64_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub64_fixbits + (-10000)*main_sub64_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub64_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub64_enob
solver.Add( + (1)*main_sub64_fixp + (1)*main_sub64_float + (1)*main_sub64_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub64_fixbits + (-10000)*main_sub64_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*data_CAST_sub64_fixp + (-1)*mean_CAST_sub64_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_sub64_float + (-1)*mean_CAST_sub64_float==0)    #float equality
solver.Add( + (1)*data_CAST_sub64_double + (-1)*mean_CAST_sub64_double==0)    #double equality
solver.Add( + (1)*data_CAST_sub64_fixbits + (-1)*mean_CAST_sub64_fixbits==0)    #same fractional bit
solver.Add( + (1)*data_CAST_sub64_fixp + (-1)*main_sub64_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_sub64_float + (-1)*main_sub64_float==0)    #float equality
solver.Add( + (1)*data_CAST_sub64_double + (-1)*main_sub64_double==0)    #double equality
solver.Add( + (1)*data_CAST_sub64_fixbits + (-1)*main_sub64_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub64_fixp
mathCostObj +=  + (2.33125)*main_sub64_float
mathCostObj +=  + (2.72422)*main_sub64_double
solver.Add( + (1)*main_sub64_enob + (-1)*data_enob_memphi_main_tmp5<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub64_enob + (-1)*mean_enob_memphi_main_tmp6<=0)    #Enob propagation in sub second addend



#Constraint for cast for   %mul65 = fmul double %sub, %sub64, !taffo.info !53, !taffo.initweight !35
main_sub_CAST_mul65_fixbits = solver.IntVar(0, 15, 'main_sub_CAST_mul65_fixbits')
main_sub_CAST_mul65_fixp = solver.IntVar(0, 1, 'main_sub_CAST_mul65_fixp')
main_sub_CAST_mul65_float = solver.IntVar(0, 1, 'main_sub_CAST_mul65_float')
main_sub_CAST_mul65_double = solver.IntVar(0, 1, 'main_sub_CAST_mul65_double')
solver.Add( + (1)*main_sub_CAST_mul65_fixp + (1)*main_sub_CAST_mul65_float + (1)*main_sub_CAST_mul65_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub_CAST_mul65_fixbits + (-10000)*main_sub_CAST_mul65_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C1_main_sub_CAST_mul65')
C2_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C2_main_sub_CAST_mul65')
solver.Add( + (1)*main_sub_fixbits + (-1)*main_sub_CAST_mul65_fixbits + (-10000)*C1_main_sub_CAST_mul65<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub_fixbits + (1)*main_sub_CAST_mul65_fixbits + (-10000)*C2_main_sub_CAST_mul65<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub_CAST_mul65
castCostObj +=  + (1)*C2_main_sub_CAST_mul65
C3_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C3_main_sub_CAST_mul65')
C4_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C4_main_sub_CAST_mul65')
C5_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C5_main_sub_CAST_mul65')
C6_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C6_main_sub_CAST_mul65')
C7_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C7_main_sub_CAST_mul65')
C8_main_sub_CAST_mul65 = solver.IntVar(0, 1, 'C8_main_sub_CAST_mul65')
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_mul65_float + (-1)*C3_main_sub_CAST_mul65<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub_CAST_mul65
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_mul65_fixp + (-1)*C4_main_sub_CAST_mul65<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub_CAST_mul65
solver.Add( + (1)*main_sub_fixp + (1)*main_sub_CAST_mul65_double + (-1)*C5_main_sub_CAST_mul65<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub_CAST_mul65
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_mul65_fixp + (-1)*C6_main_sub_CAST_mul65<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub_CAST_mul65
solver.Add( + (1)*main_sub_float + (1)*main_sub_CAST_mul65_double + (-1)*C7_main_sub_CAST_mul65<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub_CAST_mul65
solver.Add( + (1)*main_sub_double + (1)*main_sub_CAST_mul65_float + (-1)*C8_main_sub_CAST_mul65<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub_CAST_mul65



#Constraint for cast for   %mul65 = fmul double %sub, %sub64, !taffo.info !53, !taffo.initweight !35
main_sub64_CAST_mul65_fixbits = solver.IntVar(0, 15, 'main_sub64_CAST_mul65_fixbits')
main_sub64_CAST_mul65_fixp = solver.IntVar(0, 1, 'main_sub64_CAST_mul65_fixp')
main_sub64_CAST_mul65_float = solver.IntVar(0, 1, 'main_sub64_CAST_mul65_float')
main_sub64_CAST_mul65_double = solver.IntVar(0, 1, 'main_sub64_CAST_mul65_double')
solver.Add( + (1)*main_sub64_CAST_mul65_fixp + (1)*main_sub64_CAST_mul65_float + (1)*main_sub64_CAST_mul65_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub64_CAST_mul65_fixbits + (-10000)*main_sub64_CAST_mul65_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C1_main_sub64_CAST_mul65')
C2_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C2_main_sub64_CAST_mul65')
solver.Add( + (1)*main_sub64_fixbits + (-1)*main_sub64_CAST_mul65_fixbits + (-10000)*C1_main_sub64_CAST_mul65<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub64_fixbits + (1)*main_sub64_CAST_mul65_fixbits + (-10000)*C2_main_sub64_CAST_mul65<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub64_CAST_mul65
castCostObj +=  + (1)*C2_main_sub64_CAST_mul65
C3_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C3_main_sub64_CAST_mul65')
C4_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C4_main_sub64_CAST_mul65')
C5_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C5_main_sub64_CAST_mul65')
C6_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C6_main_sub64_CAST_mul65')
C7_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C7_main_sub64_CAST_mul65')
C8_main_sub64_CAST_mul65 = solver.IntVar(0, 1, 'C8_main_sub64_CAST_mul65')
solver.Add( + (1)*main_sub64_fixp + (1)*main_sub64_CAST_mul65_float + (-1)*C3_main_sub64_CAST_mul65<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub64_CAST_mul65
solver.Add( + (1)*main_sub64_float + (1)*main_sub64_CAST_mul65_fixp + (-1)*C4_main_sub64_CAST_mul65<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub64_CAST_mul65
solver.Add( + (1)*main_sub64_fixp + (1)*main_sub64_CAST_mul65_double + (-1)*C5_main_sub64_CAST_mul65<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub64_CAST_mul65
solver.Add( + (1)*main_sub64_double + (1)*main_sub64_CAST_mul65_fixp + (-1)*C6_main_sub64_CAST_mul65<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub64_CAST_mul65
solver.Add( + (1)*main_sub64_float + (1)*main_sub64_CAST_mul65_double + (-1)*C7_main_sub64_CAST_mul65<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub64_CAST_mul65
solver.Add( + (1)*main_sub64_double + (1)*main_sub64_CAST_mul65_float + (-1)*C8_main_sub64_CAST_mul65<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub64_CAST_mul65



#Stuff for   %mul65 = fmul double %sub, %sub64, !taffo.info !53, !taffo.initweight !35
main_mul65_fixbits = solver.IntVar(0, 31, 'main_mul65_fixbits')
main_mul65_fixp = solver.IntVar(0, 1, 'main_mul65_fixp')
main_mul65_float = solver.IntVar(0, 1, 'main_mul65_float')
main_mul65_double = solver.IntVar(0, 1, 'main_mul65_double')
main_mul65_enob = solver.IntVar(-10000, 10000, 'main_mul65_enob')
solver.Add( + (1)*main_mul65_enob + (-1)*main_mul65_fixbits + (10000)*main_mul65_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul65_enob + (10000)*main_mul65_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul65_enob + (10000)*main_mul65_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul65_fixbits + (-10000)*main_mul65_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_mul65_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul65_enob
solver.Add( + (1)*main_mul65_fixp + (1)*main_mul65_float + (1)*main_mul65_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul65_fixbits + (-10000)*main_mul65_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub_CAST_mul65_fixp + (-1)*main_sub64_CAST_mul65_fixp==0)    #fix equality
solver.Add( + (1)*main_sub_CAST_mul65_float + (-1)*main_sub64_CAST_mul65_float==0)    #float equality
solver.Add( + (1)*main_sub_CAST_mul65_double + (-1)*main_sub64_CAST_mul65_double==0)    #double equality
solver.Add( + (1)*main_sub_CAST_mul65_fixp + (-1)*main_mul65_fixp==0)    #fix equality
solver.Add( + (1)*main_sub_CAST_mul65_float + (-1)*main_mul65_float==0)    #float equality
solver.Add( + (1)*main_sub_CAST_mul65_double + (-1)*main_mul65_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul65_fixp
mathCostObj +=  + (2.64722)*main_mul65_float
mathCostObj +=  + (4.02255)*main_mul65_double
main_main_mul65_enob_1 = solver.IntVar(0, 1, 'main_main_mul65_enob_1')
main_main_mul65_enob_2 = solver.IntVar(0, 1, 'main_main_mul65_enob_2')
solver.Add( + (1)*main_main_mul65_enob_1 + (1)*main_main_mul65_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul65_enob + (-1)*main_sub64_enob + (-10000)*main_main_mul65_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul65_enob + (-1)*main_sub_enob + (-10000)*main_main_mul65_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
stddev_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'stddev_enob_memphi_main_tmp7')
solver.Add( + (1)*stddev_enob_memphi_main_tmp7 + (-1)*stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp7_enob_1 = solver.IntVar(0, 1, 'main_main_tmp7_enob_1')
solver.Add( + (1)*main_main_tmp7_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add68 = fadd double %tmp7, %mul65, !taffo.info !55, !taffo.initweight !29
stddev_CAST_add68_fixbits = solver.IntVar(0, 18, 'stddev_CAST_add68_fixbits')
stddev_CAST_add68_fixp = solver.IntVar(0, 1, 'stddev_CAST_add68_fixp')
stddev_CAST_add68_float = solver.IntVar(0, 1, 'stddev_CAST_add68_float')
stddev_CAST_add68_double = solver.IntVar(0, 1, 'stddev_CAST_add68_double')
solver.Add( + (1)*stddev_CAST_add68_fixp + (1)*stddev_CAST_add68_float + (1)*stddev_CAST_add68_double==1)    #exactly 1 type
solver.Add( + (1)*stddev_CAST_add68_fixbits + (-10000)*stddev_CAST_add68_fixp<=0)    #If no fix, fix frac part = 0
C1_stddev_CAST_add68 = solver.IntVar(0, 1, 'C1_stddev_CAST_add68')
C2_stddev_CAST_add68 = solver.IntVar(0, 1, 'C2_stddev_CAST_add68')
solver.Add( + (1)*stddev_fixbits + (-1)*stddev_CAST_add68_fixbits + (-10000)*C1_stddev_CAST_add68<=0)    #Shift cost 1
solver.Add( + (-1)*stddev_fixbits + (1)*stddev_CAST_add68_fixbits + (-10000)*C2_stddev_CAST_add68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_stddev_CAST_add68
castCostObj +=  + (1)*C2_stddev_CAST_add68
C3_stddev_CAST_add68 = solver.IntVar(0, 1, 'C3_stddev_CAST_add68')
C4_stddev_CAST_add68 = solver.IntVar(0, 1, 'C4_stddev_CAST_add68')
C5_stddev_CAST_add68 = solver.IntVar(0, 1, 'C5_stddev_CAST_add68')
C6_stddev_CAST_add68 = solver.IntVar(0, 1, 'C6_stddev_CAST_add68')
C7_stddev_CAST_add68 = solver.IntVar(0, 1, 'C7_stddev_CAST_add68')
C8_stddev_CAST_add68 = solver.IntVar(0, 1, 'C8_stddev_CAST_add68')
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_add68_float + (-1)*C3_stddev_CAST_add68<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_stddev_CAST_add68
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_add68_fixp + (-1)*C4_stddev_CAST_add68<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_stddev_CAST_add68
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_add68_double + (-1)*C5_stddev_CAST_add68<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_stddev_CAST_add68
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_add68_fixp + (-1)*C6_stddev_CAST_add68<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_stddev_CAST_add68
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_add68_double + (-1)*C7_stddev_CAST_add68<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_stddev_CAST_add68
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_add68_float + (-1)*C8_stddev_CAST_add68<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_stddev_CAST_add68



#Constraint for cast for   %add68 = fadd double %tmp7, %mul65, !taffo.info !55, !taffo.initweight !29
main_mul65_CAST_add68_fixbits = solver.IntVar(0, 31, 'main_mul65_CAST_add68_fixbits')
main_mul65_CAST_add68_fixp = solver.IntVar(0, 1, 'main_mul65_CAST_add68_fixp')
main_mul65_CAST_add68_float = solver.IntVar(0, 1, 'main_mul65_CAST_add68_float')
main_mul65_CAST_add68_double = solver.IntVar(0, 1, 'main_mul65_CAST_add68_double')
solver.Add( + (1)*main_mul65_CAST_add68_fixp + (1)*main_mul65_CAST_add68_float + (1)*main_mul65_CAST_add68_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul65_CAST_add68_fixbits + (-10000)*main_mul65_CAST_add68_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C1_main_mul65_CAST_add68')
C2_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C2_main_mul65_CAST_add68')
solver.Add( + (1)*main_mul65_fixbits + (-1)*main_mul65_CAST_add68_fixbits + (-10000)*C1_main_mul65_CAST_add68<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul65_fixbits + (1)*main_mul65_CAST_add68_fixbits + (-10000)*C2_main_mul65_CAST_add68<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul65_CAST_add68
castCostObj +=  + (1)*C2_main_mul65_CAST_add68
C3_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C3_main_mul65_CAST_add68')
C4_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C4_main_mul65_CAST_add68')
C5_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C5_main_mul65_CAST_add68')
C6_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C6_main_mul65_CAST_add68')
C7_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C7_main_mul65_CAST_add68')
C8_main_mul65_CAST_add68 = solver.IntVar(0, 1, 'C8_main_mul65_CAST_add68')
solver.Add( + (1)*main_mul65_fixp + (1)*main_mul65_CAST_add68_float + (-1)*C3_main_mul65_CAST_add68<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul65_CAST_add68
solver.Add( + (1)*main_mul65_float + (1)*main_mul65_CAST_add68_fixp + (-1)*C4_main_mul65_CAST_add68<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul65_CAST_add68
solver.Add( + (1)*main_mul65_fixp + (1)*main_mul65_CAST_add68_double + (-1)*C5_main_mul65_CAST_add68<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul65_CAST_add68
solver.Add( + (1)*main_mul65_double + (1)*main_mul65_CAST_add68_fixp + (-1)*C6_main_mul65_CAST_add68<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul65_CAST_add68
solver.Add( + (1)*main_mul65_float + (1)*main_mul65_CAST_add68_double + (-1)*C7_main_mul65_CAST_add68<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul65_CAST_add68
solver.Add( + (1)*main_mul65_double + (1)*main_mul65_CAST_add68_float + (-1)*C8_main_mul65_CAST_add68<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul65_CAST_add68



#Stuff for   %add68 = fadd double %tmp7, %mul65, !taffo.info !55, !taffo.initweight !29
main_add68_fixbits = solver.IntVar(0, 31, 'main_add68_fixbits')
main_add68_fixp = solver.IntVar(0, 1, 'main_add68_fixp')
main_add68_float = solver.IntVar(0, 1, 'main_add68_float')
main_add68_double = solver.IntVar(0, 1, 'main_add68_double')
main_add68_enob = solver.IntVar(-10000, 10000, 'main_add68_enob')
solver.Add( + (1)*main_add68_enob + (-1)*main_add68_fixbits + (10000)*main_add68_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add68_enob + (10000)*main_add68_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add68_enob + (10000)*main_add68_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add68_fixbits + (-10000)*main_add68_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_add68_enob<=4)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add68_enob
solver.Add( + (1)*main_add68_fixp + (1)*main_add68_float + (1)*main_add68_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add68_fixbits + (-10000)*main_add68_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*stddev_CAST_add68_fixp + (-1)*main_mul65_CAST_add68_fixp==0)    #fix equality
solver.Add( + (1)*stddev_CAST_add68_float + (-1)*main_mul65_CAST_add68_float==0)    #float equality
solver.Add( + (1)*stddev_CAST_add68_double + (-1)*main_mul65_CAST_add68_double==0)    #double equality
solver.Add( + (1)*stddev_CAST_add68_fixbits + (-1)*main_mul65_CAST_add68_fixbits==0)    #same fractional bit
solver.Add( + (1)*stddev_CAST_add68_fixp + (-1)*main_add68_fixp==0)    #fix equality
solver.Add( + (1)*stddev_CAST_add68_float + (-1)*main_add68_float==0)    #float equality
solver.Add( + (1)*stddev_CAST_add68_double + (-1)*main_add68_double==0)    #double equality
solver.Add( + (1)*stddev_CAST_add68_fixbits + (-1)*main_add68_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add68_fixp
mathCostObj +=  + (2.33125)*main_add68_float
mathCostObj +=  + (2.72422)*main_add68_double
solver.Add( + (1)*main_add68_enob + (-1)*stddev_enob_memphi_main_tmp7<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add68_enob + (-1)*main_mul65_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add68, double* %arrayidx67, align 8, !taffo.info !14, !taffo.initweight !28
main_add68_CAST_store_fixbits = solver.IntVar(0, 31, 'main_add68_CAST_store_fixbits')
main_add68_CAST_store_fixp = solver.IntVar(0, 1, 'main_add68_CAST_store_fixp')
main_add68_CAST_store_float = solver.IntVar(0, 1, 'main_add68_CAST_store_float')
main_add68_CAST_store_double = solver.IntVar(0, 1, 'main_add68_CAST_store_double')
solver.Add( + (1)*main_add68_CAST_store_fixp + (1)*main_add68_CAST_store_float + (1)*main_add68_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add68_CAST_store_fixbits + (-10000)*main_add68_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add68_CAST_store = solver.IntVar(0, 1, 'C1_main_add68_CAST_store')
C2_main_add68_CAST_store = solver.IntVar(0, 1, 'C2_main_add68_CAST_store')
solver.Add( + (1)*main_add68_fixbits + (-1)*main_add68_CAST_store_fixbits + (-10000)*C1_main_add68_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add68_fixbits + (1)*main_add68_CAST_store_fixbits + (-10000)*C2_main_add68_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add68_CAST_store
castCostObj +=  + (1)*C2_main_add68_CAST_store
C3_main_add68_CAST_store = solver.IntVar(0, 1, 'C3_main_add68_CAST_store')
C4_main_add68_CAST_store = solver.IntVar(0, 1, 'C4_main_add68_CAST_store')
C5_main_add68_CAST_store = solver.IntVar(0, 1, 'C5_main_add68_CAST_store')
C6_main_add68_CAST_store = solver.IntVar(0, 1, 'C6_main_add68_CAST_store')
C7_main_add68_CAST_store = solver.IntVar(0, 1, 'C7_main_add68_CAST_store')
C8_main_add68_CAST_store = solver.IntVar(0, 1, 'C8_main_add68_CAST_store')
solver.Add( + (1)*main_add68_fixp + (1)*main_add68_CAST_store_float + (-1)*C3_main_add68_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add68_CAST_store
solver.Add( + (1)*main_add68_float + (1)*main_add68_CAST_store_fixp + (-1)*C4_main_add68_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add68_CAST_store
solver.Add( + (1)*main_add68_fixp + (1)*main_add68_CAST_store_double + (-1)*C5_main_add68_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add68_CAST_store
solver.Add( + (1)*main_add68_double + (1)*main_add68_CAST_store_fixp + (-1)*C6_main_add68_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add68_CAST_store
solver.Add( + (1)*main_add68_float + (1)*main_add68_CAST_store_double + (-1)*C7_main_add68_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add68_CAST_store
solver.Add( + (1)*main_add68_double + (1)*main_add68_CAST_store_float + (-1)*C8_main_add68_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add68_CAST_store
solver.Add( + (1)*stddev_fixp + (-1)*main_add68_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*stddev_float + (-1)*main_add68_CAST_store_float==0)    #float equality
solver.Add( + (1)*stddev_double + (-1)*main_add68_CAST_store_double==0)    #double equality
solver.Add( + (1)*stddev_fixbits + (-1)*main_add68_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
stddev_enob_storeENOB = solver.IntVar(-10000, 10000, 'stddev_enob_storeENOB')
solver.Add( + (1)*stddev_enob_storeENOB + (-1)*stddev_fixbits + (10000)*stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*stddev_enob_storeENOB + (10000)*stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*stddev_enob_storeENOB + (10000)*stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*stddev_enob_storeENOB + (-1)*main_add68_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*stddev_enob_memphi_main_tmp7 + (-1)*stddev_enob_storeENOB + (10000)*main_main_tmp7_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
stddev_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'stddev_enob_memphi_main_tmp8')
solver.Add( + (1)*stddev_enob_memphi_main_tmp8 + (-1)*stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_1 = solver.IntVar(0, 1, 'main_main_tmp8_enob_1')
solver.Add( + (1)*main_main_tmp8_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*stddev_enob_memphi_main_tmp8 + (-1)*stddev_enob_storeENOB + (10000)*main_main_tmp8_enob_1<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 3.200000e+01
ConstantValue__12_fixbits = solver.IntVar(0, 26, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 3.200000e+01
ConstantValue__13_fixbits = solver.IntVar(0, 26, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_float + (1)*ConstantValue__13_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div74 = fdiv double %tmp8, 3.200000e+01, !taffo.info !57, !taffo.initweight !28, !taffo.constinfo !43
stddev_CAST_div74_fixbits = solver.IntVar(0, 18, 'stddev_CAST_div74_fixbits')
stddev_CAST_div74_fixp = solver.IntVar(0, 1, 'stddev_CAST_div74_fixp')
stddev_CAST_div74_float = solver.IntVar(0, 1, 'stddev_CAST_div74_float')
stddev_CAST_div74_double = solver.IntVar(0, 1, 'stddev_CAST_div74_double')
solver.Add( + (1)*stddev_CAST_div74_fixp + (1)*stddev_CAST_div74_float + (1)*stddev_CAST_div74_double==1)    #exactly 1 type
solver.Add( + (1)*stddev_CAST_div74_fixbits + (-10000)*stddev_CAST_div74_fixp<=0)    #If no fix, fix frac part = 0
C1_stddev_CAST_div74 = solver.IntVar(0, 1, 'C1_stddev_CAST_div74')
C2_stddev_CAST_div74 = solver.IntVar(0, 1, 'C2_stddev_CAST_div74')
solver.Add( + (1)*stddev_fixbits + (-1)*stddev_CAST_div74_fixbits + (-10000)*C1_stddev_CAST_div74<=0)    #Shift cost 1
solver.Add( + (-1)*stddev_fixbits + (1)*stddev_CAST_div74_fixbits + (-10000)*C2_stddev_CAST_div74<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_stddev_CAST_div74
castCostObj +=  + (1)*C2_stddev_CAST_div74
C3_stddev_CAST_div74 = solver.IntVar(0, 1, 'C3_stddev_CAST_div74')
C4_stddev_CAST_div74 = solver.IntVar(0, 1, 'C4_stddev_CAST_div74')
C5_stddev_CAST_div74 = solver.IntVar(0, 1, 'C5_stddev_CAST_div74')
C6_stddev_CAST_div74 = solver.IntVar(0, 1, 'C6_stddev_CAST_div74')
C7_stddev_CAST_div74 = solver.IntVar(0, 1, 'C7_stddev_CAST_div74')
C8_stddev_CAST_div74 = solver.IntVar(0, 1, 'C8_stddev_CAST_div74')
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_div74_float + (-1)*C3_stddev_CAST_div74<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_stddev_CAST_div74
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_div74_fixp + (-1)*C4_stddev_CAST_div74<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_stddev_CAST_div74
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_div74_double + (-1)*C5_stddev_CAST_div74<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_stddev_CAST_div74
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_div74_fixp + (-1)*C6_stddev_CAST_div74<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_stddev_CAST_div74
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_div74_double + (-1)*C7_stddev_CAST_div74<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_stddev_CAST_div74
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_div74_float + (-1)*C8_stddev_CAST_div74<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_stddev_CAST_div74



#Stuff for double 3.200000e+01
ConstantValue__14_fixbits = solver.IntVar(0, 26, 'ConstantValue__14_fixbits')
ConstantValue__14_fixp = solver.IntVar(0, 1, 'ConstantValue__14_fixp')
ConstantValue__14_float = solver.IntVar(0, 1, 'ConstantValue__14_float')
ConstantValue__14_double = solver.IntVar(0, 1, 'ConstantValue__14_double')
ConstantValue__14_enob = solver.IntVar(-10000, 10000, 'ConstantValue__14_enob')
solver.Add( + (1)*ConstantValue__14_enob + (-1)*ConstantValue__14_fixbits + (10000)*ConstantValue__14_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__14_enob + (10000)*ConstantValue__14_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_float + (1)*ConstantValue__14_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div74 = fdiv double %tmp8, 3.200000e+01, !taffo.info !57, !taffo.initweight !28, !taffo.constinfo !43
ConstantValue__14_CAST_div74_fixbits = solver.IntVar(0, 26, 'ConstantValue__14_CAST_div74_fixbits')
ConstantValue__14_CAST_div74_fixp = solver.IntVar(0, 1, 'ConstantValue__14_CAST_div74_fixp')
ConstantValue__14_CAST_div74_float = solver.IntVar(0, 1, 'ConstantValue__14_CAST_div74_float')
ConstantValue__14_CAST_div74_double = solver.IntVar(0, 1, 'ConstantValue__14_CAST_div74_double')
solver.Add( + (1)*ConstantValue__14_CAST_div74_fixp + (1)*ConstantValue__14_CAST_div74_float + (1)*ConstantValue__14_CAST_div74_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__14_CAST_div74_fixbits + (-10000)*ConstantValue__14_CAST_div74_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C1_ConstantValue__14_CAST_div74')
C2_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C2_ConstantValue__14_CAST_div74')
solver.Add( + (1)*ConstantValue__14_fixbits + (-1)*ConstantValue__14_CAST_div74_fixbits + (-10000)*C1_ConstantValue__14_CAST_div74<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__14_fixbits + (1)*ConstantValue__14_CAST_div74_fixbits + (-10000)*C2_ConstantValue__14_CAST_div74<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__14_CAST_div74
castCostObj +=  + (1)*C2_ConstantValue__14_CAST_div74
C3_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C3_ConstantValue__14_CAST_div74')
C4_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C4_ConstantValue__14_CAST_div74')
C5_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C5_ConstantValue__14_CAST_div74')
C6_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C6_ConstantValue__14_CAST_div74')
C7_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C7_ConstantValue__14_CAST_div74')
C8_ConstantValue__14_CAST_div74 = solver.IntVar(0, 1, 'C8_ConstantValue__14_CAST_div74')
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_div74_float + (-1)*C3_ConstantValue__14_CAST_div74<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__14_CAST_div74
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_div74_fixp + (-1)*C4_ConstantValue__14_CAST_div74<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__14_CAST_div74
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_div74_double + (-1)*C5_ConstantValue__14_CAST_div74<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__14_CAST_div74
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_div74_fixp + (-1)*C6_ConstantValue__14_CAST_div74<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__14_CAST_div74
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_div74_double + (-1)*C7_ConstantValue__14_CAST_div74<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__14_CAST_div74
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_div74_float + (-1)*C8_ConstantValue__14_CAST_div74<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__14_CAST_div74



#Stuff for   %div74 = fdiv double %tmp8, 3.200000e+01, !taffo.info !57, !taffo.initweight !28, !taffo.constinfo !43
main_div74_fixbits = solver.IntVar(0, 23, 'main_div74_fixbits')
main_div74_fixp = solver.IntVar(0, 1, 'main_div74_fixp')
main_div74_float = solver.IntVar(0, 1, 'main_div74_float')
main_div74_double = solver.IntVar(0, 1, 'main_div74_double')
main_div74_enob = solver.IntVar(-10000, 10000, 'main_div74_enob')
solver.Add( + (1)*main_div74_enob + (-1)*main_div74_fixbits + (10000)*main_div74_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div74_enob + (10000)*main_div74_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div74_enob + (10000)*main_div74_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div74_fixbits + (-10000)*main_div74_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_div74_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_div74_enob
solver.Add( + (1)*main_div74_fixp + (1)*main_div74_float + (1)*main_div74_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div74_fixbits + (-10000)*main_div74_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*stddev_CAST_div74_fixp + (-1)*ConstantValue__14_CAST_div74_fixp==0)    #fix equality
solver.Add( + (1)*stddev_CAST_div74_float + (-1)*ConstantValue__14_CAST_div74_float==0)    #float equality
solver.Add( + (1)*stddev_CAST_div74_double + (-1)*ConstantValue__14_CAST_div74_double==0)    #double equality
solver.Add( + (1)*stddev_CAST_div74_fixp + (-1)*main_div74_fixp==0)    #fix equality
solver.Add( + (1)*stddev_CAST_div74_float + (-1)*main_div74_float==0)    #float equality
solver.Add( + (1)*stddev_CAST_div74_double + (-1)*main_div74_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div74_fixp
mathCostObj +=  + (5.60026)*main_div74_float
mathCostObj +=  + (18.3266)*main_div74_double
main_main_div74_enob_1 = solver.IntVar(0, 1, 'main_main_div74_enob_1')
main_main_div74_enob_2 = solver.IntVar(0, 1, 'main_main_div74_enob_2')
solver.Add( + (1)*main_main_div74_enob_1 + (1)*main_main_div74_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div74_enob + (-1)*ConstantValue__12_enob + (-10000)*main_main_div74_enob_1<=1034)    #Enob: propagation in division 1
solver.Add( + (1)*main_div74_enob + (-1)*stddev_enob_memphi_main_tmp8 + (-10000)*main_main_div74_enob_2<=5)    #Enob: propagation in division 2



#Constraint for cast for   store double %div74, double* %arrayidx73, align 8, !taffo.info !14, !taffo.initweight !28
main_div74_CAST_store_fixbits = solver.IntVar(0, 23, 'main_div74_CAST_store_fixbits')
main_div74_CAST_store_fixp = solver.IntVar(0, 1, 'main_div74_CAST_store_fixp')
main_div74_CAST_store_float = solver.IntVar(0, 1, 'main_div74_CAST_store_float')
main_div74_CAST_store_double = solver.IntVar(0, 1, 'main_div74_CAST_store_double')
solver.Add( + (1)*main_div74_CAST_store_fixp + (1)*main_div74_CAST_store_float + (1)*main_div74_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div74_CAST_store_fixbits + (-10000)*main_div74_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div74_CAST_store = solver.IntVar(0, 1, 'C1_main_div74_CAST_store')
C2_main_div74_CAST_store = solver.IntVar(0, 1, 'C2_main_div74_CAST_store')
solver.Add( + (1)*main_div74_fixbits + (-1)*main_div74_CAST_store_fixbits + (-10000)*C1_main_div74_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div74_fixbits + (1)*main_div74_CAST_store_fixbits + (-10000)*C2_main_div74_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div74_CAST_store
castCostObj +=  + (1)*C2_main_div74_CAST_store
C3_main_div74_CAST_store = solver.IntVar(0, 1, 'C3_main_div74_CAST_store')
C4_main_div74_CAST_store = solver.IntVar(0, 1, 'C4_main_div74_CAST_store')
C5_main_div74_CAST_store = solver.IntVar(0, 1, 'C5_main_div74_CAST_store')
C6_main_div74_CAST_store = solver.IntVar(0, 1, 'C6_main_div74_CAST_store')
C7_main_div74_CAST_store = solver.IntVar(0, 1, 'C7_main_div74_CAST_store')
C8_main_div74_CAST_store = solver.IntVar(0, 1, 'C8_main_div74_CAST_store')
solver.Add( + (1)*main_div74_fixp + (1)*main_div74_CAST_store_float + (-1)*C3_main_div74_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div74_CAST_store
solver.Add( + (1)*main_div74_float + (1)*main_div74_CAST_store_fixp + (-1)*C4_main_div74_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div74_CAST_store
solver.Add( + (1)*main_div74_fixp + (1)*main_div74_CAST_store_double + (-1)*C5_main_div74_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div74_CAST_store
solver.Add( + (1)*main_div74_double + (1)*main_div74_CAST_store_fixp + (-1)*C6_main_div74_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div74_CAST_store
solver.Add( + (1)*main_div74_float + (1)*main_div74_CAST_store_double + (-1)*C7_main_div74_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div74_CAST_store
solver.Add( + (1)*main_div74_double + (1)*main_div74_CAST_store_float + (-1)*C8_main_div74_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div74_CAST_store
solver.Add( + (1)*stddev_fixp + (-1)*main_div74_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*stddev_float + (-1)*main_div74_CAST_store_float==0)    #float equality
solver.Add( + (1)*stddev_double + (-1)*main_div74_CAST_store_double==0)    #double equality
solver.Add( + (1)*stddev_fixbits + (-1)*main_div74_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
stddev_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'stddev_enob_storeENOB_storeENOB')
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB + (-1)*stddev_fixbits + (10000)*stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB + (10000)*stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB + (10000)*stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB + (-1)*main_div74_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
stddev_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'stddev_enob_memphi_main_tmp9')
solver.Add( + (1)*stddev_enob_memphi_main_tmp9 + (-1)*stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
solver.Add( + (1)*main_main_tmp9_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*stddev_enob_memphi_main_tmp9 + (-1)*stddev_enob_storeENOB_storeENOB + (10000)*main_main_tmp9_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %call = call double @sqrt(double %tmp9) #3, !taffo.info !59, !taffo.initweight !29, !taffo.constinfo !47
main_call_fixbits = solver.IntVar(0, 25, 'main_call_fixbits')
main_call_fixp = solver.IntVar(0, 1, 'main_call_fixp')
main_call_float = solver.IntVar(0, 1, 'main_call_float')
main_call_double = solver.IntVar(0, 1, 'main_call_double')
main_call_enob = solver.IntVar(-10000, 10000, 'main_call_enob')
solver.Add( + (1)*main_call_enob + (-1)*main_call_fixbits + (10000)*main_call_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call_enob + (10000)*main_call_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_call_enob + (10000)*main_call_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp>=-9976)    #Limit the lower number of frac bits25
solver.Add( + (1)*main_call_enob<=4)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_call_enob
solver.Add( + (1)*main_call_fixp + (1)*main_call_float + (1)*main_call_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call_fixbits + (-10000)*main_call_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call_double==1)    #Type constraint for return value



#Constraint for cast for   %call = call double @sqrt(double %tmp9) #3, !taffo.info !59, !taffo.initweight !29, !taffo.constinfo !47
stddev_CAST_call_fixbits = solver.IntVar(0, 18, 'stddev_CAST_call_fixbits')
stddev_CAST_call_fixp = solver.IntVar(0, 1, 'stddev_CAST_call_fixp')
stddev_CAST_call_float = solver.IntVar(0, 1, 'stddev_CAST_call_float')
stddev_CAST_call_double = solver.IntVar(0, 1, 'stddev_CAST_call_double')
solver.Add( + (1)*stddev_CAST_call_fixp + (1)*stddev_CAST_call_float + (1)*stddev_CAST_call_double==1)    #exactly 1 type
solver.Add( + (1)*stddev_CAST_call_fixbits + (-10000)*stddev_CAST_call_fixp<=0)    #If no fix, fix frac part = 0
C1_stddev_CAST_call = solver.IntVar(0, 1, 'C1_stddev_CAST_call')
C2_stddev_CAST_call = solver.IntVar(0, 1, 'C2_stddev_CAST_call')
solver.Add( + (1)*stddev_fixbits + (-1)*stddev_CAST_call_fixbits + (-10000)*C1_stddev_CAST_call<=0)    #Shift cost 1
solver.Add( + (-1)*stddev_fixbits + (1)*stddev_CAST_call_fixbits + (-10000)*C2_stddev_CAST_call<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_stddev_CAST_call
castCostObj +=  + (1)*C2_stddev_CAST_call
C3_stddev_CAST_call = solver.IntVar(0, 1, 'C3_stddev_CAST_call')
C4_stddev_CAST_call = solver.IntVar(0, 1, 'C4_stddev_CAST_call')
C5_stddev_CAST_call = solver.IntVar(0, 1, 'C5_stddev_CAST_call')
C6_stddev_CAST_call = solver.IntVar(0, 1, 'C6_stddev_CAST_call')
C7_stddev_CAST_call = solver.IntVar(0, 1, 'C7_stddev_CAST_call')
C8_stddev_CAST_call = solver.IntVar(0, 1, 'C8_stddev_CAST_call')
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_call_float + (-1)*C3_stddev_CAST_call<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_stddev_CAST_call
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_call_fixp + (-1)*C4_stddev_CAST_call<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_stddev_CAST_call
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_call_double + (-1)*C5_stddev_CAST_call<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_stddev_CAST_call
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_call_fixp + (-1)*C6_stddev_CAST_call<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_stddev_CAST_call
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_call_double + (-1)*C7_stddev_CAST_call<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_stddev_CAST_call
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_call_float + (-1)*C8_stddev_CAST_call<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_stddev_CAST_call
solver.Add( + (1)*stddev_CAST_call_double==1)    #Type constraint for argument value



#Constraint for cast for   store double %call, double* %arrayidx78, align 8, !taffo.info !14, !taffo.initweight !28
main_call_CAST_store_fixbits = solver.IntVar(0, 25, 'main_call_CAST_store_fixbits')
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
solver.Add( + (1)*stddev_fixp + (-1)*main_call_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*stddev_float + (-1)*main_call_CAST_store_float==0)    #float equality
solver.Add( + (1)*stddev_double + (-1)*main_call_CAST_store_double==0)    #double equality
solver.Add( + (1)*stddev_fixbits + (-1)*main_call_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
stddev_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'stddev_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB + (-1)*stddev_fixbits + (10000)*stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB + (-1)*main_call_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
stddev_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'stddev_enob_memphi_main_tmp10')
solver.Add( + (1)*stddev_enob_memphi_main_tmp10 + (-1)*stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_0 = solver.IntVar(0, 1, 'main_main_tmp10_enob_0')
solver.Add( + (1)*main_main_tmp10_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*stddev_enob_memphi_main_tmp10 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp10_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 1.000000e-01
ConstantValue__15_fixbits = solver.IntVar(0, 31, 'ConstantValue__15_fixbits')
ConstantValue__15_fixp = solver.IntVar(0, 1, 'ConstantValue__15_fixp')
ConstantValue__15_float = solver.IntVar(0, 1, 'ConstantValue__15_float')
ConstantValue__15_double = solver.IntVar(0, 1, 'ConstantValue__15_double')
ConstantValue__15_enob = solver.IntVar(-10000, 10000, 'ConstantValue__15_enob')
solver.Add( + (1)*ConstantValue__15_enob + (-1)*ConstantValue__15_fixbits + (10000)*ConstantValue__15_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_float<=10027)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__15_enob + (10000)*ConstantValue__15_double<=10056)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__15_fixp + (1)*ConstantValue__15_float + (1)*ConstantValue__15_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__15_fixbits + (-10000)*ConstantValue__15_fixp<=0)    #If not fix, frac part to zero

#Restriction for new enob [LOAD]
stddev_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'stddev_enob_memphi_main_tmp11')
solver.Add( + (1)*stddev_enob_memphi_main_tmp11 + (-1)*stddev_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_0 = solver.IntVar(0, 1, 'main_main_tmp11_enob_0')
solver.Add( + (1)*main_main_tmp11_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*stddev_enob_memphi_main_tmp11 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp11_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !14, !taffo.initweight !29
main_cond_fixbits = solver.IntVar(0, 18, 'main_cond_fixbits')
main_cond_fixp = solver.IntVar(0, 1, 'main_cond_fixp')
main_cond_float = solver.IntVar(0, 1, 'main_cond_float')
main_cond_double = solver.IntVar(0, 1, 'main_cond_double')
main_cond_enob = solver.IntVar(-10000, 10000, 'main_cond_enob')
solver.Add( + (1)*main_cond_enob + (-1)*main_cond_fixbits + (10000)*main_cond_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_cond_enob + (10000)*main_cond_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_cond_enob + (10000)*main_cond_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_cond_fixbits + (-10000)*main_cond_fixp>=-9983)    #Limit the lower number of frac bits18
solver.Add( + (1)*main_cond_enob<=4)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_cond_enob
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_float + (1)*main_cond_double==1)    #Exactly one selected type
solver.Add( + (1)*main_cond_fixbits + (-10000)*main_cond_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__16_fixbits = solver.IntVar(0, 31, 'ConstantValue__16_fixbits')
ConstantValue__16_fixp = solver.IntVar(0, 1, 'ConstantValue__16_fixp')
ConstantValue__16_float = solver.IntVar(0, 1, 'ConstantValue__16_float')
ConstantValue__16_double = solver.IntVar(0, 1, 'ConstantValue__16_double')
ConstantValue__16_enob = solver.IntVar(-10000, 10000, 'ConstantValue__16_enob')
solver.Add( + (1)*ConstantValue__16_enob + (-1)*ConstantValue__16_fixbits + (10000)*ConstantValue__16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__16_enob + (10000)*ConstantValue__16_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero
main_main_cond_enob_1 = solver.IntVar(0, 1, 'main_main_cond_enob_1')
solver.Add( + (1)*main_main_cond_enob_1==1)    #Enob: one selected constraint



#Stuff for double 1.000000e+00
ConstantValue__17_fixbits = solver.IntVar(0, 31, 'ConstantValue__17_fixbits')
ConstantValue__17_fixp = solver.IntVar(0, 1, 'ConstantValue__17_fixp')
ConstantValue__17_float = solver.IntVar(0, 1, 'ConstantValue__17_float')
ConstantValue__17_double = solver.IntVar(0, 1, 'ConstantValue__17_double')
ConstantValue__17_enob = solver.IntVar(-10000, 10000, 'ConstantValue__17_enob')
solver.Add( + (1)*ConstantValue__17_enob + (-1)*ConstantValue__17_fixbits + (10000)*ConstantValue__17_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__17_enob + (10000)*ConstantValue__17_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_float + (1)*ConstantValue__17_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %cond = phi double [ 1.000000e+00, %cond.true ], [ %tmp11, %cond.false ], !taffo.info !14, !taffo.initweight !29
stddev_CAST_cond_fixbits = solver.IntVar(0, 18, 'stddev_CAST_cond_fixbits')
stddev_CAST_cond_fixp = solver.IntVar(0, 1, 'stddev_CAST_cond_fixp')
stddev_CAST_cond_float = solver.IntVar(0, 1, 'stddev_CAST_cond_float')
stddev_CAST_cond_double = solver.IntVar(0, 1, 'stddev_CAST_cond_double')
solver.Add( + (1)*stddev_CAST_cond_fixp + (1)*stddev_CAST_cond_float + (1)*stddev_CAST_cond_double==1)    #exactly 1 type
solver.Add( + (1)*stddev_CAST_cond_fixbits + (-10000)*stddev_CAST_cond_fixp<=0)    #If no fix, fix frac part = 0
C1_stddev_CAST_cond = solver.IntVar(0, 1, 'C1_stddev_CAST_cond')
C2_stddev_CAST_cond = solver.IntVar(0, 1, 'C2_stddev_CAST_cond')
solver.Add( + (1)*stddev_fixbits + (-1)*stddev_CAST_cond_fixbits + (-10000)*C1_stddev_CAST_cond<=0)    #Shift cost 1
solver.Add( + (-1)*stddev_fixbits + (1)*stddev_CAST_cond_fixbits + (-10000)*C2_stddev_CAST_cond<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_stddev_CAST_cond
castCostObj +=  + (1)*C2_stddev_CAST_cond
C3_stddev_CAST_cond = solver.IntVar(0, 1, 'C3_stddev_CAST_cond')
C4_stddev_CAST_cond = solver.IntVar(0, 1, 'C4_stddev_CAST_cond')
C5_stddev_CAST_cond = solver.IntVar(0, 1, 'C5_stddev_CAST_cond')
C6_stddev_CAST_cond = solver.IntVar(0, 1, 'C6_stddev_CAST_cond')
C7_stddev_CAST_cond = solver.IntVar(0, 1, 'C7_stddev_CAST_cond')
C8_stddev_CAST_cond = solver.IntVar(0, 1, 'C8_stddev_CAST_cond')
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_cond_float + (-1)*C3_stddev_CAST_cond<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_stddev_CAST_cond
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_cond_fixp + (-1)*C4_stddev_CAST_cond<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_stddev_CAST_cond
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_cond_double + (-1)*C5_stddev_CAST_cond<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_stddev_CAST_cond
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_cond_fixp + (-1)*C6_stddev_CAST_cond<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_stddev_CAST_cond
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_cond_double + (-1)*C7_stddev_CAST_cond<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_stddev_CAST_cond
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_cond_float + (-1)*C8_stddev_CAST_cond<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_stddev_CAST_cond
solver.Add( + (1)*main_cond_fixp + (-1)*stddev_CAST_cond_fixp==0)    #fix equality
solver.Add( + (1)*main_cond_float + (-1)*stddev_CAST_cond_float==0)    #float equality
solver.Add( + (1)*main_cond_double + (-1)*stddev_CAST_cond_double==0)    #double equality
solver.Add( + (1)*main_cond_fixbits + (-1)*stddev_CAST_cond_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_cond_enob + (-1)*stddev_enob_memphi_main_tmp11 + (10000)*main_main_cond_enob_1<=10000)    #Enob: forcing phi enob



#Constraint for cast for   store double %cond, double* %arrayidx86, align 8, !taffo.info !14, !taffo.initweight !28
main_cond_CAST_store_fixbits = solver.IntVar(0, 18, 'main_cond_CAST_store_fixbits')
main_cond_CAST_store_fixp = solver.IntVar(0, 1, 'main_cond_CAST_store_fixp')
main_cond_CAST_store_float = solver.IntVar(0, 1, 'main_cond_CAST_store_float')
main_cond_CAST_store_double = solver.IntVar(0, 1, 'main_cond_CAST_store_double')
solver.Add( + (1)*main_cond_CAST_store_fixp + (1)*main_cond_CAST_store_float + (1)*main_cond_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_cond_CAST_store_fixbits + (-10000)*main_cond_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_cond_CAST_store = solver.IntVar(0, 1, 'C1_main_cond_CAST_store')
C2_main_cond_CAST_store = solver.IntVar(0, 1, 'C2_main_cond_CAST_store')
solver.Add( + (1)*main_cond_fixbits + (-1)*main_cond_CAST_store_fixbits + (-10000)*C1_main_cond_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_cond_fixbits + (1)*main_cond_CAST_store_fixbits + (-10000)*C2_main_cond_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_cond_CAST_store
castCostObj +=  + (1)*C2_main_cond_CAST_store
C3_main_cond_CAST_store = solver.IntVar(0, 1, 'C3_main_cond_CAST_store')
C4_main_cond_CAST_store = solver.IntVar(0, 1, 'C4_main_cond_CAST_store')
C5_main_cond_CAST_store = solver.IntVar(0, 1, 'C5_main_cond_CAST_store')
C6_main_cond_CAST_store = solver.IntVar(0, 1, 'C6_main_cond_CAST_store')
C7_main_cond_CAST_store = solver.IntVar(0, 1, 'C7_main_cond_CAST_store')
C8_main_cond_CAST_store = solver.IntVar(0, 1, 'C8_main_cond_CAST_store')
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_CAST_store_float + (-1)*C3_main_cond_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_cond_CAST_store
solver.Add( + (1)*main_cond_float + (1)*main_cond_CAST_store_fixp + (-1)*C4_main_cond_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_cond_CAST_store
solver.Add( + (1)*main_cond_fixp + (1)*main_cond_CAST_store_double + (-1)*C5_main_cond_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_cond_CAST_store
solver.Add( + (1)*main_cond_double + (1)*main_cond_CAST_store_fixp + (-1)*C6_main_cond_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_cond_CAST_store
solver.Add( + (1)*main_cond_float + (1)*main_cond_CAST_store_double + (-1)*C7_main_cond_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_cond_CAST_store
solver.Add( + (1)*main_cond_double + (1)*main_cond_CAST_store_float + (-1)*C8_main_cond_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_cond_CAST_store
solver.Add( + (1)*stddev_fixp + (-1)*main_cond_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*stddev_float + (-1)*main_cond_CAST_store_float==0)    #float equality
solver.Add( + (1)*stddev_double + (-1)*main_cond_CAST_store_double==0)    #double equality
solver.Add( + (1)*stddev_fixbits + (-1)*main_cond_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*stddev_fixbits + (10000)*stddev_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*stddev_float<=10149)    #Enob constraint for float
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*stddev_double<=11074)    #Enob constraint for double
solver.Add( + (1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_cond_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp3 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp3_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp4 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp4_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp5 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp5_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp6 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp6_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
mean_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'mean_enob_memphi_main_tmp12')
solver.Add( + (1)*mean_enob_memphi_main_tmp12 + (-1)*mean_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp12_enob_1 = solver.IntVar(0, 1, 'main_main_tmp12_enob_1')
main_main_tmp12_enob_2 = solver.IntVar(0, 1, 'main_main_tmp12_enob_2')
main_main_tmp12_enob_3 = solver.IntVar(0, 1, 'main_main_tmp12_enob_3')
main_main_tmp12_enob_4 = solver.IntVar(0, 1, 'main_main_tmp12_enob_4')
solver.Add( + (1)*main_main_tmp12_enob_1 + (1)*main_main_tmp12_enob_2 + (1)*main_main_tmp12_enob_3 + (1)*main_main_tmp12_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp12 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp12_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp12 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp12 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_3<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp13 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp13')
solver.Add( + (1)*data_enob_memphi_main_tmp13 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp13_enob_1 = solver.IntVar(0, 1, 'main_main_tmp13_enob_1')
main_main_tmp13_enob_2 = solver.IntVar(0, 1, 'main_main_tmp13_enob_2')
main_main_tmp13_enob_3 = solver.IntVar(0, 1, 'main_main_tmp13_enob_3')
main_main_tmp13_enob_4 = solver.IntVar(0, 1, 'main_main_tmp13_enob_4')
solver.Add( + (1)*main_main_tmp13_enob_1 + (1)*main_main_tmp13_enob_2 + (1)*main_main_tmp13_enob_3 + (1)*main_main_tmp13_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp13 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp13_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp13 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp13 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_3<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %sub104 = fsub double %tmp13, %tmp12, !taffo.info !49, !taffo.initweight !29
data_CAST_sub104_fixbits = solver.IntVar(0, 27, 'data_CAST_sub104_fixbits')
data_CAST_sub104_fixp = solver.IntVar(0, 1, 'data_CAST_sub104_fixp')
data_CAST_sub104_float = solver.IntVar(0, 1, 'data_CAST_sub104_float')
data_CAST_sub104_double = solver.IntVar(0, 1, 'data_CAST_sub104_double')
solver.Add( + (1)*data_CAST_sub104_fixp + (1)*data_CAST_sub104_float + (1)*data_CAST_sub104_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_sub104_fixbits + (-10000)*data_CAST_sub104_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_sub104 = solver.IntVar(0, 1, 'C1_data_CAST_sub104')
C2_data_CAST_sub104 = solver.IntVar(0, 1, 'C2_data_CAST_sub104')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_sub104_fixbits + (-10000)*C1_data_CAST_sub104<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_sub104_fixbits + (-10000)*C2_data_CAST_sub104<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_sub104
castCostObj +=  + (1)*C2_data_CAST_sub104
C3_data_CAST_sub104 = solver.IntVar(0, 1, 'C3_data_CAST_sub104')
C4_data_CAST_sub104 = solver.IntVar(0, 1, 'C4_data_CAST_sub104')
C5_data_CAST_sub104 = solver.IntVar(0, 1, 'C5_data_CAST_sub104')
C6_data_CAST_sub104 = solver.IntVar(0, 1, 'C6_data_CAST_sub104')
C7_data_CAST_sub104 = solver.IntVar(0, 1, 'C7_data_CAST_sub104')
C8_data_CAST_sub104 = solver.IntVar(0, 1, 'C8_data_CAST_sub104')
solver.Add( + (1)*data_fixp + (1)*data_CAST_sub104_float + (-1)*C3_data_CAST_sub104<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_data_CAST_sub104
solver.Add( + (1)*data_float + (1)*data_CAST_sub104_fixp + (-1)*C4_data_CAST_sub104<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_data_CAST_sub104
solver.Add( + (1)*data_fixp + (1)*data_CAST_sub104_double + (-1)*C5_data_CAST_sub104<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_data_CAST_sub104
solver.Add( + (1)*data_double + (1)*data_CAST_sub104_fixp + (-1)*C6_data_CAST_sub104<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_data_CAST_sub104
solver.Add( + (1)*data_float + (1)*data_CAST_sub104_double + (-1)*C7_data_CAST_sub104<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_data_CAST_sub104
solver.Add( + (1)*data_double + (1)*data_CAST_sub104_float + (-1)*C8_data_CAST_sub104<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_data_CAST_sub104



#Constraint for cast for   %sub104 = fsub double %tmp13, %tmp12, !taffo.info !49, !taffo.initweight !29
mean_CAST_sub104_fixbits = solver.IntVar(0, 15, 'mean_CAST_sub104_fixbits')
mean_CAST_sub104_fixp = solver.IntVar(0, 1, 'mean_CAST_sub104_fixp')
mean_CAST_sub104_float = solver.IntVar(0, 1, 'mean_CAST_sub104_float')
mean_CAST_sub104_double = solver.IntVar(0, 1, 'mean_CAST_sub104_double')
solver.Add( + (1)*mean_CAST_sub104_fixp + (1)*mean_CAST_sub104_float + (1)*mean_CAST_sub104_double==1)    #exactly 1 type
solver.Add( + (1)*mean_CAST_sub104_fixbits + (-10000)*mean_CAST_sub104_fixp<=0)    #If no fix, fix frac part = 0
C1_mean_CAST_sub104 = solver.IntVar(0, 1, 'C1_mean_CAST_sub104')
C2_mean_CAST_sub104 = solver.IntVar(0, 1, 'C2_mean_CAST_sub104')
solver.Add( + (1)*mean_fixbits + (-1)*mean_CAST_sub104_fixbits + (-10000)*C1_mean_CAST_sub104<=0)    #Shift cost 1
solver.Add( + (-1)*mean_fixbits + (1)*mean_CAST_sub104_fixbits + (-10000)*C2_mean_CAST_sub104<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mean_CAST_sub104
castCostObj +=  + (1)*C2_mean_CAST_sub104
C3_mean_CAST_sub104 = solver.IntVar(0, 1, 'C3_mean_CAST_sub104')
C4_mean_CAST_sub104 = solver.IntVar(0, 1, 'C4_mean_CAST_sub104')
C5_mean_CAST_sub104 = solver.IntVar(0, 1, 'C5_mean_CAST_sub104')
C6_mean_CAST_sub104 = solver.IntVar(0, 1, 'C6_mean_CAST_sub104')
C7_mean_CAST_sub104 = solver.IntVar(0, 1, 'C7_mean_CAST_sub104')
C8_mean_CAST_sub104 = solver.IntVar(0, 1, 'C8_mean_CAST_sub104')
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_sub104_float + (-1)*C3_mean_CAST_sub104<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_mean_CAST_sub104
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub104_fixp + (-1)*C4_mean_CAST_sub104<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_mean_CAST_sub104
solver.Add( + (1)*mean_fixp + (1)*mean_CAST_sub104_double + (-1)*C5_mean_CAST_sub104<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_mean_CAST_sub104
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub104_fixp + (-1)*C6_mean_CAST_sub104<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_mean_CAST_sub104
solver.Add( + (1)*mean_float + (1)*mean_CAST_sub104_double + (-1)*C7_mean_CAST_sub104<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_mean_CAST_sub104
solver.Add( + (1)*mean_double + (1)*mean_CAST_sub104_float + (-1)*C8_mean_CAST_sub104<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_mean_CAST_sub104



#Stuff for   %sub104 = fsub double %tmp13, %tmp12, !taffo.info !49, !taffo.initweight !29
main_sub104_fixbits = solver.IntVar(0, 15, 'main_sub104_fixbits')
main_sub104_fixp = solver.IntVar(0, 1, 'main_sub104_fixp')
main_sub104_float = solver.IntVar(0, 1, 'main_sub104_float')
main_sub104_double = solver.IntVar(0, 1, 'main_sub104_double')
main_sub104_enob = solver.IntVar(-10000, 10000, 'main_sub104_enob')
solver.Add( + (1)*main_sub104_enob + (-1)*main_sub104_fixbits + (10000)*main_sub104_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub104_enob + (10000)*main_sub104_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub104_enob + (10000)*main_sub104_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub104_fixbits + (-10000)*main_sub104_fixp>=-9986)    #Limit the lower number of frac bits15
solver.Add( + (1)*main_sub104_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_sub104_enob
solver.Add( + (1)*main_sub104_fixp + (1)*main_sub104_float + (1)*main_sub104_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub104_fixbits + (-10000)*main_sub104_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*data_CAST_sub104_fixp + (-1)*mean_CAST_sub104_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_sub104_float + (-1)*mean_CAST_sub104_float==0)    #float equality
solver.Add( + (1)*data_CAST_sub104_double + (-1)*mean_CAST_sub104_double==0)    #double equality
solver.Add( + (1)*data_CAST_sub104_fixbits + (-1)*mean_CAST_sub104_fixbits==0)    #same fractional bit
solver.Add( + (1)*data_CAST_sub104_fixp + (-1)*main_sub104_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_sub104_float + (-1)*main_sub104_float==0)    #float equality
solver.Add( + (1)*data_CAST_sub104_double + (-1)*main_sub104_double==0)    #double equality
solver.Add( + (1)*data_CAST_sub104_fixbits + (-1)*main_sub104_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_sub104_fixp
mathCostObj +=  + (2.33125)*main_sub104_float
mathCostObj +=  + (2.72422)*main_sub104_double
solver.Add( + (1)*main_sub104_enob + (-1)*data_enob_memphi_main_tmp13<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub104_enob + (-1)*mean_enob_memphi_main_tmp12<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub104, double* %arrayidx103, align 8, !taffo.info !8, !taffo.initweight !29
main_sub104_CAST_store_fixbits = solver.IntVar(0, 15, 'main_sub104_CAST_store_fixbits')
main_sub104_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub104_CAST_store_fixp')
main_sub104_CAST_store_float = solver.IntVar(0, 1, 'main_sub104_CAST_store_float')
main_sub104_CAST_store_double = solver.IntVar(0, 1, 'main_sub104_CAST_store_double')
solver.Add( + (1)*main_sub104_CAST_store_fixp + (1)*main_sub104_CAST_store_float + (1)*main_sub104_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub104_CAST_store_fixbits + (-10000)*main_sub104_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub104_CAST_store = solver.IntVar(0, 1, 'C1_main_sub104_CAST_store')
C2_main_sub104_CAST_store = solver.IntVar(0, 1, 'C2_main_sub104_CAST_store')
solver.Add( + (1)*main_sub104_fixbits + (-1)*main_sub104_CAST_store_fixbits + (-10000)*C1_main_sub104_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub104_fixbits + (1)*main_sub104_CAST_store_fixbits + (-10000)*C2_main_sub104_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub104_CAST_store
castCostObj +=  + (1)*C2_main_sub104_CAST_store
C3_main_sub104_CAST_store = solver.IntVar(0, 1, 'C3_main_sub104_CAST_store')
C4_main_sub104_CAST_store = solver.IntVar(0, 1, 'C4_main_sub104_CAST_store')
C5_main_sub104_CAST_store = solver.IntVar(0, 1, 'C5_main_sub104_CAST_store')
C6_main_sub104_CAST_store = solver.IntVar(0, 1, 'C6_main_sub104_CAST_store')
C7_main_sub104_CAST_store = solver.IntVar(0, 1, 'C7_main_sub104_CAST_store')
C8_main_sub104_CAST_store = solver.IntVar(0, 1, 'C8_main_sub104_CAST_store')
solver.Add( + (1)*main_sub104_fixp + (1)*main_sub104_CAST_store_float + (-1)*C3_main_sub104_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_sub104_CAST_store
solver.Add( + (1)*main_sub104_float + (1)*main_sub104_CAST_store_fixp + (-1)*C4_main_sub104_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_sub104_CAST_store
solver.Add( + (1)*main_sub104_fixp + (1)*main_sub104_CAST_store_double + (-1)*C5_main_sub104_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_sub104_CAST_store
solver.Add( + (1)*main_sub104_double + (1)*main_sub104_CAST_store_fixp + (-1)*C6_main_sub104_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_sub104_CAST_store
solver.Add( + (1)*main_sub104_float + (1)*main_sub104_CAST_store_double + (-1)*C7_main_sub104_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_sub104_CAST_store
solver.Add( + (1)*main_sub104_double + (1)*main_sub104_CAST_store_float + (-1)*C8_main_sub104_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_sub104_CAST_store
solver.Add( + (1)*data_fixp + (-1)*main_sub104_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*data_float + (-1)*main_sub104_CAST_store_float==0)    #float equality
solver.Add( + (1)*data_double + (-1)*main_sub104_CAST_store_double==0)    #double equality
solver.Add( + (1)*data_fixbits + (-1)*main_sub104_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
data_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'data_enob_storeENOB_storeENOB')
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_enob_storeENOB_storeENOB + (-1)*main_sub104_enob<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for   %call105 = call double @sqrt(double 3.200000e+01) #3, !taffo.info !64, !taffo.initweight !28, !taffo.constinfo !66
main_call105_fixbits = solver.IntVar(0, 29, 'main_call105_fixbits')
main_call105_fixp = solver.IntVar(0, 1, 'main_call105_fixp')
main_call105_float = solver.IntVar(0, 1, 'main_call105_float')
main_call105_double = solver.IntVar(0, 1, 'main_call105_double')
main_call105_enob = solver.IntVar(-10000, 10000, 'main_call105_enob')
solver.Add( + (1)*main_call105_enob + (-1)*main_call105_fixbits + (10000)*main_call105_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_call105_enob + (10000)*main_call105_float<=10021)    #Enob constraint for float
solver.Add( + (1)*main_call105_enob + (10000)*main_call105_double<=10050)    #Enob constraint for double
solver.Add( + (1)*main_call105_fixbits + (-10000)*main_call105_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_call105_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_call105_enob
solver.Add( + (1)*main_call105_fixp + (1)*main_call105_float + (1)*main_call105_double==1)    #Exactly one selected type
solver.Add( + (1)*main_call105_fixbits + (-10000)*main_call105_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call105_double==1)    #Type constraint for return value



#Stuff for double 3.200000e+01
ConstantValue__18_fixbits = solver.IntVar(0, 26, 'ConstantValue__18_fixbits')
ConstantValue__18_fixp = solver.IntVar(0, 1, 'ConstantValue__18_fixp')
ConstantValue__18_float = solver.IntVar(0, 1, 'ConstantValue__18_float')
ConstantValue__18_double = solver.IntVar(0, 1, 'ConstantValue__18_double')
ConstantValue__18_enob = solver.IntVar(-10000, 10000, 'ConstantValue__18_enob')
solver.Add( + (1)*ConstantValue__18_enob + (-1)*ConstantValue__18_fixbits + (10000)*ConstantValue__18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__18_fixp + (1)*ConstantValue__18_float + (1)*ConstantValue__18_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 3.200000e+01
ConstantValue__19_fixbits = solver.IntVar(0, 26, 'ConstantValue__19_fixbits')
ConstantValue__19_fixp = solver.IntVar(0, 1, 'ConstantValue__19_fixp')
ConstantValue__19_float = solver.IntVar(0, 1, 'ConstantValue__19_float')
ConstantValue__19_double = solver.IntVar(0, 1, 'ConstantValue__19_double')
ConstantValue__19_enob = solver.IntVar(-10000, 10000, 'ConstantValue__19_enob')
solver.Add( + (1)*ConstantValue__19_enob + (-1)*ConstantValue__19_fixbits + (10000)*ConstantValue__19_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp>=-9975)    #Limit the lower number of frac bits26
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_float + (1)*ConstantValue__19_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %call105 = call double @sqrt(double 3.200000e+01) #3, !taffo.info !64, !taffo.initweight !28, !taffo.constinfo !66
ConstantValue__19_CAST_call105_fixbits = solver.IntVar(0, 26, 'ConstantValue__19_CAST_call105_fixbits')
ConstantValue__19_CAST_call105_fixp = solver.IntVar(0, 1, 'ConstantValue__19_CAST_call105_fixp')
ConstantValue__19_CAST_call105_float = solver.IntVar(0, 1, 'ConstantValue__19_CAST_call105_float')
ConstantValue__19_CAST_call105_double = solver.IntVar(0, 1, 'ConstantValue__19_CAST_call105_double')
solver.Add( + (1)*ConstantValue__19_CAST_call105_fixp + (1)*ConstantValue__19_CAST_call105_float + (1)*ConstantValue__19_CAST_call105_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__19_CAST_call105_fixbits + (-10000)*ConstantValue__19_CAST_call105_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C1_ConstantValue__19_CAST_call105')
C2_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C2_ConstantValue__19_CAST_call105')
solver.Add( + (1)*ConstantValue__19_fixbits + (-1)*ConstantValue__19_CAST_call105_fixbits + (-10000)*C1_ConstantValue__19_CAST_call105<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__19_fixbits + (1)*ConstantValue__19_CAST_call105_fixbits + (-10000)*C2_ConstantValue__19_CAST_call105<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__19_CAST_call105
castCostObj +=  + (1)*C2_ConstantValue__19_CAST_call105
C3_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C3_ConstantValue__19_CAST_call105')
C4_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C4_ConstantValue__19_CAST_call105')
C5_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C5_ConstantValue__19_CAST_call105')
C6_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C6_ConstantValue__19_CAST_call105')
C7_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C7_ConstantValue__19_CAST_call105')
C8_ConstantValue__19_CAST_call105 = solver.IntVar(0, 1, 'C8_ConstantValue__19_CAST_call105')
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_call105_float + (-1)*C3_ConstantValue__19_CAST_call105<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__19_CAST_call105
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_call105_fixp + (-1)*C4_ConstantValue__19_CAST_call105<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__19_CAST_call105
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_CAST_call105_double + (-1)*C5_ConstantValue__19_CAST_call105<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__19_CAST_call105
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_call105_fixp + (-1)*C6_ConstantValue__19_CAST_call105<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__19_CAST_call105
solver.Add( + (1)*ConstantValue__19_float + (1)*ConstantValue__19_CAST_call105_double + (-1)*C7_ConstantValue__19_CAST_call105<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__19_CAST_call105
solver.Add( + (1)*ConstantValue__19_double + (1)*ConstantValue__19_CAST_call105_float + (-1)*C8_ConstantValue__19_CAST_call105<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__19_CAST_call105
solver.Add( + (1)*ConstantValue__19_CAST_call105_double==1)    #Type constraint for argument value

#Restriction for new enob [LOAD]
stddev_enob_memphi_main_tmp14 = solver.IntVar(-10000, 10000, 'stddev_enob_memphi_main_tmp14')
solver.Add( + (1)*stddev_enob_memphi_main_tmp14 + (-1)*stddev_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul108 = fmul double %call105, %tmp14, !taffo.info !67, !taffo.initweight !29
main_call105_CAST_mul108_fixbits = solver.IntVar(0, 29, 'main_call105_CAST_mul108_fixbits')
main_call105_CAST_mul108_fixp = solver.IntVar(0, 1, 'main_call105_CAST_mul108_fixp')
main_call105_CAST_mul108_float = solver.IntVar(0, 1, 'main_call105_CAST_mul108_float')
main_call105_CAST_mul108_double = solver.IntVar(0, 1, 'main_call105_CAST_mul108_double')
solver.Add( + (1)*main_call105_CAST_mul108_fixp + (1)*main_call105_CAST_mul108_float + (1)*main_call105_CAST_mul108_double==1)    #exactly 1 type
solver.Add( + (1)*main_call105_CAST_mul108_fixbits + (-10000)*main_call105_CAST_mul108_fixp<=0)    #If no fix, fix frac part = 0
C1_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C1_main_call105_CAST_mul108')
C2_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C2_main_call105_CAST_mul108')
solver.Add( + (1)*main_call105_fixbits + (-1)*main_call105_CAST_mul108_fixbits + (-10000)*C1_main_call105_CAST_mul108<=0)    #Shift cost 1
solver.Add( + (-1)*main_call105_fixbits + (1)*main_call105_CAST_mul108_fixbits + (-10000)*C2_main_call105_CAST_mul108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_call105_CAST_mul108
castCostObj +=  + (1)*C2_main_call105_CAST_mul108
C3_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C3_main_call105_CAST_mul108')
C4_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C4_main_call105_CAST_mul108')
C5_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C5_main_call105_CAST_mul108')
C6_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C6_main_call105_CAST_mul108')
C7_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C7_main_call105_CAST_mul108')
C8_main_call105_CAST_mul108 = solver.IntVar(0, 1, 'C8_main_call105_CAST_mul108')
solver.Add( + (1)*main_call105_fixp + (1)*main_call105_CAST_mul108_float + (-1)*C3_main_call105_CAST_mul108<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_call105_CAST_mul108
solver.Add( + (1)*main_call105_float + (1)*main_call105_CAST_mul108_fixp + (-1)*C4_main_call105_CAST_mul108<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_call105_CAST_mul108
solver.Add( + (1)*main_call105_fixp + (1)*main_call105_CAST_mul108_double + (-1)*C5_main_call105_CAST_mul108<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_call105_CAST_mul108
solver.Add( + (1)*main_call105_double + (1)*main_call105_CAST_mul108_fixp + (-1)*C6_main_call105_CAST_mul108<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_call105_CAST_mul108
solver.Add( + (1)*main_call105_float + (1)*main_call105_CAST_mul108_double + (-1)*C7_main_call105_CAST_mul108<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_call105_CAST_mul108
solver.Add( + (1)*main_call105_double + (1)*main_call105_CAST_mul108_float + (-1)*C8_main_call105_CAST_mul108<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_call105_CAST_mul108



#Constraint for cast for   %mul108 = fmul double %call105, %tmp14, !taffo.info !67, !taffo.initweight !29
stddev_CAST_mul108_fixbits = solver.IntVar(0, 18, 'stddev_CAST_mul108_fixbits')
stddev_CAST_mul108_fixp = solver.IntVar(0, 1, 'stddev_CAST_mul108_fixp')
stddev_CAST_mul108_float = solver.IntVar(0, 1, 'stddev_CAST_mul108_float')
stddev_CAST_mul108_double = solver.IntVar(0, 1, 'stddev_CAST_mul108_double')
solver.Add( + (1)*stddev_CAST_mul108_fixp + (1)*stddev_CAST_mul108_float + (1)*stddev_CAST_mul108_double==1)    #exactly 1 type
solver.Add( + (1)*stddev_CAST_mul108_fixbits + (-10000)*stddev_CAST_mul108_fixp<=0)    #If no fix, fix frac part = 0
C1_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C1_stddev_CAST_mul108')
C2_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C2_stddev_CAST_mul108')
solver.Add( + (1)*stddev_fixbits + (-1)*stddev_CAST_mul108_fixbits + (-10000)*C1_stddev_CAST_mul108<=0)    #Shift cost 1
solver.Add( + (-1)*stddev_fixbits + (1)*stddev_CAST_mul108_fixbits + (-10000)*C2_stddev_CAST_mul108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_stddev_CAST_mul108
castCostObj +=  + (1)*C2_stddev_CAST_mul108
C3_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C3_stddev_CAST_mul108')
C4_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C4_stddev_CAST_mul108')
C5_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C5_stddev_CAST_mul108')
C6_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C6_stddev_CAST_mul108')
C7_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C7_stddev_CAST_mul108')
C8_stddev_CAST_mul108 = solver.IntVar(0, 1, 'C8_stddev_CAST_mul108')
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_mul108_float + (-1)*C3_stddev_CAST_mul108<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_stddev_CAST_mul108
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_mul108_fixp + (-1)*C4_stddev_CAST_mul108<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_stddev_CAST_mul108
solver.Add( + (1)*stddev_fixp + (1)*stddev_CAST_mul108_double + (-1)*C5_stddev_CAST_mul108<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_stddev_CAST_mul108
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_mul108_fixp + (-1)*C6_stddev_CAST_mul108<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_stddev_CAST_mul108
solver.Add( + (1)*stddev_float + (1)*stddev_CAST_mul108_double + (-1)*C7_stddev_CAST_mul108<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_stddev_CAST_mul108
solver.Add( + (1)*stddev_double + (1)*stddev_CAST_mul108_float + (-1)*C8_stddev_CAST_mul108<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_stddev_CAST_mul108



#Stuff for   %mul108 = fmul double %call105, %tmp14, !taffo.info !67, !taffo.initweight !29
main_mul108_fixbits = solver.IntVar(0, 16, 'main_mul108_fixbits')
main_mul108_fixp = solver.IntVar(0, 1, 'main_mul108_fixp')
main_mul108_float = solver.IntVar(0, 1, 'main_mul108_float')
main_mul108_double = solver.IntVar(0, 1, 'main_mul108_double')
main_mul108_enob = solver.IntVar(-10000, 10000, 'main_mul108_enob')
solver.Add( + (1)*main_mul108_enob + (-1)*main_mul108_fixbits + (10000)*main_mul108_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul108_enob + (10000)*main_mul108_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul108_enob + (10000)*main_mul108_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul108_fixbits + (-10000)*main_mul108_fixp>=-9985)    #Limit the lower number of frac bits16
solver.Add( + (1)*main_mul108_enob<=4)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul108_enob
solver.Add( + (1)*main_mul108_fixp + (1)*main_mul108_float + (1)*main_mul108_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul108_fixbits + (-10000)*main_mul108_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_call105_CAST_mul108_fixp + (-1)*stddev_CAST_mul108_fixp==0)    #fix equality
solver.Add( + (1)*main_call105_CAST_mul108_float + (-1)*stddev_CAST_mul108_float==0)    #float equality
solver.Add( + (1)*main_call105_CAST_mul108_double + (-1)*stddev_CAST_mul108_double==0)    #double equality
solver.Add( + (1)*main_call105_CAST_mul108_fixp + (-1)*main_mul108_fixp==0)    #fix equality
solver.Add( + (1)*main_call105_CAST_mul108_float + (-1)*main_mul108_float==0)    #float equality
solver.Add( + (1)*main_call105_CAST_mul108_double + (-1)*main_mul108_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul108_fixp
mathCostObj +=  + (2.64722)*main_mul108_float
mathCostObj +=  + (4.02255)*main_mul108_double
main_main_mul108_enob_1 = solver.IntVar(0, 1, 'main_main_mul108_enob_1')
main_main_mul108_enob_2 = solver.IntVar(0, 1, 'main_main_mul108_enob_2')
solver.Add( + (1)*main_main_mul108_enob_1 + (1)*main_main_mul108_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul108_enob + (-1)*stddev_enob_memphi_main_tmp14 + (-10000)*main_main_mul108_enob_1<=-3)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul108_enob + (-1)*main_call105_enob + (-10000)*main_main_mul108_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp15 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp15')
solver.Add( + (1)*data_enob_memphi_main_tmp15 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %div113 = fdiv double %tmp15, %mul108, !taffo.info !69, !taffo.initweight !35
data_CAST_div113_fixbits = solver.IntVar(0, 27, 'data_CAST_div113_fixbits')
data_CAST_div113_fixp = solver.IntVar(0, 1, 'data_CAST_div113_fixp')
data_CAST_div113_float = solver.IntVar(0, 1, 'data_CAST_div113_float')
data_CAST_div113_double = solver.IntVar(0, 1, 'data_CAST_div113_double')
solver.Add( + (1)*data_CAST_div113_fixp + (1)*data_CAST_div113_float + (1)*data_CAST_div113_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_div113_fixbits + (-10000)*data_CAST_div113_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_div113 = solver.IntVar(0, 1, 'C1_data_CAST_div113')
C2_data_CAST_div113 = solver.IntVar(0, 1, 'C2_data_CAST_div113')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_div113_fixbits + (-10000)*C1_data_CAST_div113<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_div113_fixbits + (-10000)*C2_data_CAST_div113<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_div113
castCostObj +=  + (1)*C2_data_CAST_div113
C3_data_CAST_div113 = solver.IntVar(0, 1, 'C3_data_CAST_div113')
C4_data_CAST_div113 = solver.IntVar(0, 1, 'C4_data_CAST_div113')
C5_data_CAST_div113 = solver.IntVar(0, 1, 'C5_data_CAST_div113')
C6_data_CAST_div113 = solver.IntVar(0, 1, 'C6_data_CAST_div113')
C7_data_CAST_div113 = solver.IntVar(0, 1, 'C7_data_CAST_div113')
C8_data_CAST_div113 = solver.IntVar(0, 1, 'C8_data_CAST_div113')
solver.Add( + (1)*data_fixp + (1)*data_CAST_div113_float + (-1)*C3_data_CAST_div113<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_data_CAST_div113
solver.Add( + (1)*data_float + (1)*data_CAST_div113_fixp + (-1)*C4_data_CAST_div113<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_data_CAST_div113
solver.Add( + (1)*data_fixp + (1)*data_CAST_div113_double + (-1)*C5_data_CAST_div113<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_data_CAST_div113
solver.Add( + (1)*data_double + (1)*data_CAST_div113_fixp + (-1)*C6_data_CAST_div113<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_data_CAST_div113
solver.Add( + (1)*data_float + (1)*data_CAST_div113_double + (-1)*C7_data_CAST_div113<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_data_CAST_div113
solver.Add( + (1)*data_double + (1)*data_CAST_div113_float + (-1)*C8_data_CAST_div113<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_data_CAST_div113



#Constraint for cast for   %div113 = fdiv double %tmp15, %mul108, !taffo.info !69, !taffo.initweight !35
main_mul108_CAST_div113_fixbits = solver.IntVar(0, 16, 'main_mul108_CAST_div113_fixbits')
main_mul108_CAST_div113_fixp = solver.IntVar(0, 1, 'main_mul108_CAST_div113_fixp')
main_mul108_CAST_div113_float = solver.IntVar(0, 1, 'main_mul108_CAST_div113_float')
main_mul108_CAST_div113_double = solver.IntVar(0, 1, 'main_mul108_CAST_div113_double')
solver.Add( + (1)*main_mul108_CAST_div113_fixp + (1)*main_mul108_CAST_div113_float + (1)*main_mul108_CAST_div113_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul108_CAST_div113_fixbits + (-10000)*main_mul108_CAST_div113_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C1_main_mul108_CAST_div113')
C2_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C2_main_mul108_CAST_div113')
solver.Add( + (1)*main_mul108_fixbits + (-1)*main_mul108_CAST_div113_fixbits + (-10000)*C1_main_mul108_CAST_div113<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul108_fixbits + (1)*main_mul108_CAST_div113_fixbits + (-10000)*C2_main_mul108_CAST_div113<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul108_CAST_div113
castCostObj +=  + (1)*C2_main_mul108_CAST_div113
C3_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C3_main_mul108_CAST_div113')
C4_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C4_main_mul108_CAST_div113')
C5_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C5_main_mul108_CAST_div113')
C6_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C6_main_mul108_CAST_div113')
C7_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C7_main_mul108_CAST_div113')
C8_main_mul108_CAST_div113 = solver.IntVar(0, 1, 'C8_main_mul108_CAST_div113')
solver.Add( + (1)*main_mul108_fixp + (1)*main_mul108_CAST_div113_float + (-1)*C3_main_mul108_CAST_div113<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul108_CAST_div113
solver.Add( + (1)*main_mul108_float + (1)*main_mul108_CAST_div113_fixp + (-1)*C4_main_mul108_CAST_div113<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul108_CAST_div113
solver.Add( + (1)*main_mul108_fixp + (1)*main_mul108_CAST_div113_double + (-1)*C5_main_mul108_CAST_div113<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul108_CAST_div113
solver.Add( + (1)*main_mul108_double + (1)*main_mul108_CAST_div113_fixp + (-1)*C6_main_mul108_CAST_div113<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul108_CAST_div113
solver.Add( + (1)*main_mul108_float + (1)*main_mul108_CAST_div113_double + (-1)*C7_main_mul108_CAST_div113<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul108_CAST_div113
solver.Add( + (1)*main_mul108_double + (1)*main_mul108_CAST_div113_float + (-1)*C8_main_mul108_CAST_div113<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul108_CAST_div113



#Stuff for   %div113 = fdiv double %tmp15, %mul108, !taffo.info !69, !taffo.initweight !35
main_div113_fixbits = solver.IntVar(0, 30, 'main_div113_fixbits')
main_div113_fixp = solver.IntVar(0, 1, 'main_div113_fixp')
main_div113_float = solver.IntVar(0, 1, 'main_div113_float')
main_div113_double = solver.IntVar(0, 1, 'main_div113_double')
main_div113_enob = solver.IntVar(-10000, 10000, 'main_div113_enob')
solver.Add( + (1)*main_div113_enob + (-1)*main_div113_fixbits + (10000)*main_div113_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div113_enob + (10000)*main_div113_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div113_enob + (10000)*main_div113_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div113_fixbits + (-10000)*main_div113_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_div113_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_div113_enob
solver.Add( + (1)*main_div113_fixp + (1)*main_div113_float + (1)*main_div113_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div113_fixbits + (-10000)*main_div113_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*data_CAST_div113_fixp + (-1)*main_mul108_CAST_div113_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_div113_float + (-1)*main_mul108_CAST_div113_float==0)    #float equality
solver.Add( + (1)*data_CAST_div113_double + (-1)*main_mul108_CAST_div113_double==0)    #double equality
solver.Add( + (1)*data_CAST_div113_fixp + (-1)*main_div113_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_div113_float + (-1)*main_div113_float==0)    #float equality
solver.Add( + (1)*data_CAST_div113_double + (-1)*main_div113_double==0)    #double equality
mathCostObj +=  + (5.29598)*main_div113_fixp
mathCostObj +=  + (5.60026)*main_div113_float
mathCostObj +=  + (18.3266)*main_div113_double
main_main_div113_enob_1 = solver.IntVar(0, 1, 'main_main_div113_enob_1')
main_main_div113_enob_2 = solver.IntVar(0, 1, 'main_main_div113_enob_2')
solver.Add( + (1)*main_main_div113_enob_1 + (1)*main_main_div113_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div113_enob + (-1)*main_mul108_enob + (-10000)*main_main_div113_enob_1<=1054)    #Enob: propagation in division 1
solver.Add( + (1)*main_div113_enob + (-1)*data_enob_memphi_main_tmp15 + (-10000)*main_main_div113_enob_2<=1054)    #Enob: propagation in division 2



#Constraint for cast for   store double %div113, double* %arrayidx112, align 8, !taffo.info !8, !taffo.initweight !29
main_div113_CAST_store_fixbits = solver.IntVar(0, 30, 'main_div113_CAST_store_fixbits')
main_div113_CAST_store_fixp = solver.IntVar(0, 1, 'main_div113_CAST_store_fixp')
main_div113_CAST_store_float = solver.IntVar(0, 1, 'main_div113_CAST_store_float')
main_div113_CAST_store_double = solver.IntVar(0, 1, 'main_div113_CAST_store_double')
solver.Add( + (1)*main_div113_CAST_store_fixp + (1)*main_div113_CAST_store_float + (1)*main_div113_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div113_CAST_store_fixbits + (-10000)*main_div113_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div113_CAST_store = solver.IntVar(0, 1, 'C1_main_div113_CAST_store')
C2_main_div113_CAST_store = solver.IntVar(0, 1, 'C2_main_div113_CAST_store')
solver.Add( + (1)*main_div113_fixbits + (-1)*main_div113_CAST_store_fixbits + (-10000)*C1_main_div113_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div113_fixbits + (1)*main_div113_CAST_store_fixbits + (-10000)*C2_main_div113_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div113_CAST_store
castCostObj +=  + (1)*C2_main_div113_CAST_store
C3_main_div113_CAST_store = solver.IntVar(0, 1, 'C3_main_div113_CAST_store')
C4_main_div113_CAST_store = solver.IntVar(0, 1, 'C4_main_div113_CAST_store')
C5_main_div113_CAST_store = solver.IntVar(0, 1, 'C5_main_div113_CAST_store')
C6_main_div113_CAST_store = solver.IntVar(0, 1, 'C6_main_div113_CAST_store')
C7_main_div113_CAST_store = solver.IntVar(0, 1, 'C7_main_div113_CAST_store')
C8_main_div113_CAST_store = solver.IntVar(0, 1, 'C8_main_div113_CAST_store')
solver.Add( + (1)*main_div113_fixp + (1)*main_div113_CAST_store_float + (-1)*C3_main_div113_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_div113_CAST_store
solver.Add( + (1)*main_div113_float + (1)*main_div113_CAST_store_fixp + (-1)*C4_main_div113_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_div113_CAST_store
solver.Add( + (1)*main_div113_fixp + (1)*main_div113_CAST_store_double + (-1)*C5_main_div113_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_div113_CAST_store
solver.Add( + (1)*main_div113_double + (1)*main_div113_CAST_store_fixp + (-1)*C6_main_div113_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_div113_CAST_store
solver.Add( + (1)*main_div113_float + (1)*main_div113_CAST_store_double + (-1)*C7_main_div113_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_div113_CAST_store
solver.Add( + (1)*main_div113_double + (1)*main_div113_CAST_store_float + (-1)*C8_main_div113_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_div113_CAST_store
solver.Add( + (1)*data_fixp + (-1)*main_div113_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*data_float + (-1)*main_div113_CAST_store_float==0)    #float equality
solver.Add( + (1)*data_double + (-1)*main_div113_CAST_store_double==0)    #double equality
solver.Add( + (1)*data_fixbits + (-1)*main_div113_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
data_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'data_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*data_enob_storeENOB_storeENOB_storeENOB + (-1)*data_fixbits + (10000)*data_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*data_enob_storeENOB_storeENOB_storeENOB + (10000)*data_float<=10149)    #Enob constraint for float
solver.Add( + (1)*data_enob_storeENOB_storeENOB_storeENOB + (10000)*data_double<=11074)    #Enob constraint for double
solver.Add( + (1)*data_enob_storeENOB_storeENOB_storeENOB + (-1)*main_div113_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*mean_enob_memphi_main_tmp12 + (-1)*data_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp12_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp13 + (-1)*data_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp13_enob_4<=10000)    #Enob: forcing MEM phi enob



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



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx127, align 8, !taffo.info !17, !taffo.initweight !29, !taffo.constinfo !71
ConstantValue__21_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__21_CAST_store_fixbits')
ConstantValue__21_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__21_CAST_store_fixp')
ConstantValue__21_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__21_CAST_store_float')
ConstantValue__21_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__21_CAST_store_double')
solver.Add( + (1)*ConstantValue__21_CAST_store_fixp + (1)*ConstantValue__21_CAST_store_float + (1)*ConstantValue__21_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__21_CAST_store_fixbits + (-10000)*ConstantValue__21_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__21_CAST_store')
C2_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__21_CAST_store')
solver.Add( + (1)*ConstantValue__21_fixbits + (-1)*ConstantValue__21_CAST_store_fixbits + (-10000)*C1_ConstantValue__21_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__21_fixbits + (1)*ConstantValue__21_CAST_store_fixbits + (-10000)*C2_ConstantValue__21_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__21_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__21_CAST_store
C3_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__21_CAST_store')
C4_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__21_CAST_store')
C5_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__21_CAST_store')
C6_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__21_CAST_store')
C7_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__21_CAST_store')
C8_ConstantValue__21_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__21_CAST_store')
solver.Add( + (1)*ConstantValue__21_fixp + (1)*ConstantValue__21_CAST_store_float + (-1)*C3_ConstantValue__21_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__21_CAST_store
solver.Add( + (1)*ConstantValue__21_float + (1)*ConstantValue__21_CAST_store_fixp + (-1)*C4_ConstantValue__21_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__21_CAST_store
solver.Add( + (1)*ConstantValue__21_fixp + (1)*ConstantValue__21_CAST_store_double + (-1)*C5_ConstantValue__21_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__21_CAST_store
solver.Add( + (1)*ConstantValue__21_double + (1)*ConstantValue__21_CAST_store_fixp + (-1)*C6_ConstantValue__21_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__21_CAST_store
solver.Add( + (1)*ConstantValue__21_float + (1)*ConstantValue__21_CAST_store_double + (-1)*C7_ConstantValue__21_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__21_CAST_store
solver.Add( + (1)*ConstantValue__21_double + (1)*ConstantValue__21_CAST_store_float + (-1)*C8_ConstantValue__21_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__21_CAST_store
solver.Add( + (1)*corr_fixp + (-1)*ConstantValue__21_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*corr_float + (-1)*ConstantValue__21_CAST_store_float==0)    #float equality
solver.Add( + (1)*corr_double + (-1)*ConstantValue__21_CAST_store_double==0)    #double equality
solver.Add( + (1)*corr_fixbits + (-1)*ConstantValue__21_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 0.000000e+00
ConstantValue__22_fixbits = solver.IntVar(0, 32, 'ConstantValue__22_fixbits')
ConstantValue__22_fixp = solver.IntVar(0, 1, 'ConstantValue__22_fixp')
ConstantValue__22_float = solver.IntVar(0, 1, 'ConstantValue__22_float')
ConstantValue__22_double = solver.IntVar(0, 1, 'ConstantValue__22_double')
ConstantValue__22_enob = solver.IntVar(-10000, 10000, 'ConstantValue__22_enob')
solver.Add( + (1)*ConstantValue__22_enob + (-1)*ConstantValue__22_fixbits + (10000)*ConstantValue__22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__22_enob + (10000)*ConstantValue__22_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_float + (1)*ConstantValue__22_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__23_fixbits = solver.IntVar(0, 32, 'ConstantValue__23_fixbits')
ConstantValue__23_fixp = solver.IntVar(0, 1, 'ConstantValue__23_fixp')
ConstantValue__23_float = solver.IntVar(0, 1, 'ConstantValue__23_float')
ConstantValue__23_double = solver.IntVar(0, 1, 'ConstantValue__23_double')
ConstantValue__23_enob = solver.IntVar(-10000, 10000, 'ConstantValue__23_enob')
solver.Add( + (1)*ConstantValue__23_enob + (-1)*ConstantValue__23_fixbits + (10000)*ConstantValue__23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_float + (1)*ConstantValue__23_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx136, align 8, !taffo.info !17, !taffo.initweight !29, !taffo.constinfo !48
ConstantValue__23_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__23_CAST_store_fixbits')
ConstantValue__23_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__23_CAST_store_fixp')
ConstantValue__23_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__23_CAST_store_float')
ConstantValue__23_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__23_CAST_store_double')
solver.Add( + (1)*ConstantValue__23_CAST_store_fixp + (1)*ConstantValue__23_CAST_store_float + (1)*ConstantValue__23_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__23_CAST_store_fixbits + (-10000)*ConstantValue__23_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__23_CAST_store')
C2_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__23_CAST_store')
solver.Add( + (1)*ConstantValue__23_fixbits + (-1)*ConstantValue__23_CAST_store_fixbits + (-10000)*C1_ConstantValue__23_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__23_fixbits + (1)*ConstantValue__23_CAST_store_fixbits + (-10000)*C2_ConstantValue__23_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__23_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__23_CAST_store
C3_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__23_CAST_store')
C4_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__23_CAST_store')
C5_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__23_CAST_store')
C6_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__23_CAST_store')
C7_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__23_CAST_store')
C8_ConstantValue__23_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__23_CAST_store')
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_CAST_store_float + (-1)*C3_ConstantValue__23_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__23_CAST_store
solver.Add( + (1)*ConstantValue__23_float + (1)*ConstantValue__23_CAST_store_fixp + (-1)*C4_ConstantValue__23_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__23_CAST_store
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_CAST_store_double + (-1)*C5_ConstantValue__23_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__23_CAST_store
solver.Add( + (1)*ConstantValue__23_double + (1)*ConstantValue__23_CAST_store_fixp + (-1)*C6_ConstantValue__23_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__23_CAST_store
solver.Add( + (1)*ConstantValue__23_float + (1)*ConstantValue__23_CAST_store_double + (-1)*C7_ConstantValue__23_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__23_CAST_store
solver.Add( + (1)*ConstantValue__23_double + (1)*ConstantValue__23_CAST_store_float + (-1)*C8_ConstantValue__23_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__23_CAST_store
solver.Add( + (1)*corr_fixp + (-1)*ConstantValue__23_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*corr_float + (-1)*ConstantValue__23_CAST_store_float==0)    #float equality
solver.Add( + (1)*corr_double + (-1)*ConstantValue__23_CAST_store_double==0)    #double equality
solver.Add( + (1)*corr_fixbits + (-1)*ConstantValue__23_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp16 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp16')
solver.Add( + (1)*data_enob_memphi_main_tmp16 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp16_enob_1 = solver.IntVar(0, 1, 'main_main_tmp16_enob_1')
main_main_tmp16_enob_2 = solver.IntVar(0, 1, 'main_main_tmp16_enob_2')
main_main_tmp16_enob_3 = solver.IntVar(0, 1, 'main_main_tmp16_enob_3')
main_main_tmp16_enob_4 = solver.IntVar(0, 1, 'main_main_tmp16_enob_4')
solver.Add( + (1)*main_main_tmp16_enob_1 + (1)*main_main_tmp16_enob_2 + (1)*main_main_tmp16_enob_3 + (1)*main_main_tmp16_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp16 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp16_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp16 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp16 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp16 + (-1)*data_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp16_enob_4<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
data_enob_memphi_main_tmp17 = solver.IntVar(-10000, 10000, 'data_enob_memphi_main_tmp17')
solver.Add( + (1)*data_enob_memphi_main_tmp17 + (-1)*data_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp17_enob_1 = solver.IntVar(0, 1, 'main_main_tmp17_enob_1')
main_main_tmp17_enob_2 = solver.IntVar(0, 1, 'main_main_tmp17_enob_2')
main_main_tmp17_enob_3 = solver.IntVar(0, 1, 'main_main_tmp17_enob_3')
main_main_tmp17_enob_4 = solver.IntVar(0, 1, 'main_main_tmp17_enob_4')
solver.Add( + (1)*main_main_tmp17_enob_1 + (1)*main_main_tmp17_enob_2 + (1)*main_main_tmp17_enob_3 + (1)*main_main_tmp17_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp17 + (-1)*data_enob_storeENOB + (10000)*main_main_tmp17_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp17 + (-1)*mean_enob_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp17 + (-1)*stddev_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*data_enob_memphi_main_tmp17 + (-1)*data_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp17_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul149 = fmul double %tmp16, %tmp17, !taffo.info !74, !taffo.initweight !35
data_CAST_mul149_fixbits = solver.IntVar(0, 27, 'data_CAST_mul149_fixbits')
data_CAST_mul149_fixp = solver.IntVar(0, 1, 'data_CAST_mul149_fixp')
data_CAST_mul149_float = solver.IntVar(0, 1, 'data_CAST_mul149_float')
data_CAST_mul149_double = solver.IntVar(0, 1, 'data_CAST_mul149_double')
solver.Add( + (1)*data_CAST_mul149_fixp + (1)*data_CAST_mul149_float + (1)*data_CAST_mul149_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_mul149_fixbits + (-10000)*data_CAST_mul149_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_mul149 = solver.IntVar(0, 1, 'C1_data_CAST_mul149')
C2_data_CAST_mul149 = solver.IntVar(0, 1, 'C2_data_CAST_mul149')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_mul149_fixbits + (-10000)*C1_data_CAST_mul149<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_mul149_fixbits + (-10000)*C2_data_CAST_mul149<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_mul149
castCostObj +=  + (1)*C2_data_CAST_mul149
C3_data_CAST_mul149 = solver.IntVar(0, 1, 'C3_data_CAST_mul149')
C4_data_CAST_mul149 = solver.IntVar(0, 1, 'C4_data_CAST_mul149')
C5_data_CAST_mul149 = solver.IntVar(0, 1, 'C5_data_CAST_mul149')
C6_data_CAST_mul149 = solver.IntVar(0, 1, 'C6_data_CAST_mul149')
C7_data_CAST_mul149 = solver.IntVar(0, 1, 'C7_data_CAST_mul149')
C8_data_CAST_mul149 = solver.IntVar(0, 1, 'C8_data_CAST_mul149')
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul149_float + (-1)*C3_data_CAST_mul149<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_data_CAST_mul149
solver.Add( + (1)*data_float + (1)*data_CAST_mul149_fixp + (-1)*C4_data_CAST_mul149<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_data_CAST_mul149
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul149_double + (-1)*C5_data_CAST_mul149<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_data_CAST_mul149
solver.Add( + (1)*data_double + (1)*data_CAST_mul149_fixp + (-1)*C6_data_CAST_mul149<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_data_CAST_mul149
solver.Add( + (1)*data_float + (1)*data_CAST_mul149_double + (-1)*C7_data_CAST_mul149<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_data_CAST_mul149
solver.Add( + (1)*data_double + (1)*data_CAST_mul149_float + (-1)*C8_data_CAST_mul149<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_data_CAST_mul149



#Constraint for cast for   %mul149 = fmul double %tmp16, %tmp17, !taffo.info !74, !taffo.initweight !35
data_CAST_mul149_0_fixbits = solver.IntVar(0, 27, 'data_CAST_mul149_0_fixbits')
data_CAST_mul149_0_fixp = solver.IntVar(0, 1, 'data_CAST_mul149_0_fixp')
data_CAST_mul149_0_float = solver.IntVar(0, 1, 'data_CAST_mul149_0_float')
data_CAST_mul149_0_double = solver.IntVar(0, 1, 'data_CAST_mul149_0_double')
solver.Add( + (1)*data_CAST_mul149_0_fixp + (1)*data_CAST_mul149_0_float + (1)*data_CAST_mul149_0_double==1)    #exactly 1 type
solver.Add( + (1)*data_CAST_mul149_0_fixbits + (-10000)*data_CAST_mul149_0_fixp<=0)    #If no fix, fix frac part = 0
C1_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C1_data_CAST_mul149_0')
C2_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C2_data_CAST_mul149_0')
solver.Add( + (1)*data_fixbits + (-1)*data_CAST_mul149_0_fixbits + (-10000)*C1_data_CAST_mul149_0<=0)    #Shift cost 1
solver.Add( + (-1)*data_fixbits + (1)*data_CAST_mul149_0_fixbits + (-10000)*C2_data_CAST_mul149_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_data_CAST_mul149_0
castCostObj +=  + (1)*C2_data_CAST_mul149_0
C3_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C3_data_CAST_mul149_0')
C4_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C4_data_CAST_mul149_0')
C5_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C5_data_CAST_mul149_0')
C6_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C6_data_CAST_mul149_0')
C7_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C7_data_CAST_mul149_0')
C8_data_CAST_mul149_0 = solver.IntVar(0, 1, 'C8_data_CAST_mul149_0')
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul149_0_float + (-1)*C3_data_CAST_mul149_0<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_data_CAST_mul149_0
solver.Add( + (1)*data_float + (1)*data_CAST_mul149_0_fixp + (-1)*C4_data_CAST_mul149_0<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_data_CAST_mul149_0
solver.Add( + (1)*data_fixp + (1)*data_CAST_mul149_0_double + (-1)*C5_data_CAST_mul149_0<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_data_CAST_mul149_0
solver.Add( + (1)*data_double + (1)*data_CAST_mul149_0_fixp + (-1)*C6_data_CAST_mul149_0<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_data_CAST_mul149_0
solver.Add( + (1)*data_float + (1)*data_CAST_mul149_0_double + (-1)*C7_data_CAST_mul149_0<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_data_CAST_mul149_0
solver.Add( + (1)*data_double + (1)*data_CAST_mul149_0_float + (-1)*C8_data_CAST_mul149_0<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_data_CAST_mul149_0



#Stuff for   %mul149 = fmul double %tmp16, %tmp17, !taffo.info !74, !taffo.initweight !35
main_mul149_fixbits = solver.IntVar(0, 24, 'main_mul149_fixbits')
main_mul149_fixp = solver.IntVar(0, 1, 'main_mul149_fixp')
main_mul149_float = solver.IntVar(0, 1, 'main_mul149_float')
main_mul149_double = solver.IntVar(0, 1, 'main_mul149_double')
main_mul149_enob = solver.IntVar(-10000, 10000, 'main_mul149_enob')
solver.Add( + (1)*main_mul149_enob + (-1)*main_mul149_fixbits + (10000)*main_mul149_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul149_enob + (10000)*main_mul149_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul149_enob + (10000)*main_mul149_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul149_fixbits + (-10000)*main_mul149_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*main_mul149_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_mul149_enob
solver.Add( + (1)*main_mul149_fixp + (1)*main_mul149_float + (1)*main_mul149_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul149_fixbits + (-10000)*main_mul149_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*data_CAST_mul149_fixp + (-1)*data_CAST_mul149_0_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_mul149_float + (-1)*data_CAST_mul149_0_float==0)    #float equality
solver.Add( + (1)*data_CAST_mul149_double + (-1)*data_CAST_mul149_0_double==0)    #double equality
solver.Add( + (1)*data_CAST_mul149_fixp + (-1)*main_mul149_fixp==0)    #fix equality
solver.Add( + (1)*data_CAST_mul149_float + (-1)*main_mul149_float==0)    #float equality
solver.Add( + (1)*data_CAST_mul149_double + (-1)*main_mul149_double==0)    #double equality
mathCostObj +=  + (1.62391)*main_mul149_fixp
mathCostObj +=  + (2.64722)*main_mul149_float
mathCostObj +=  + (4.02255)*main_mul149_double
main_main_mul149_enob_1 = solver.IntVar(0, 1, 'main_main_mul149_enob_1')
main_main_mul149_enob_2 = solver.IntVar(0, 1, 'main_main_mul149_enob_2')
solver.Add( + (1)*main_main_mul149_enob_1 + (1)*main_main_mul149_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul149_enob + (-1)*data_enob_memphi_main_tmp17 + (-10000)*main_main_mul149_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul149_enob + (-1)*data_enob_memphi_main_tmp16 + (-10000)*main_main_mul149_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
corr_enob_memphi_main_tmp18 = solver.IntVar(-10000, 10000, 'corr_enob_memphi_main_tmp18')
solver.Add( + (1)*corr_enob_memphi_main_tmp18 + (-1)*corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp18_enob_1 = solver.IntVar(0, 1, 'main_main_tmp18_enob_1')
solver.Add( + (1)*main_main_tmp18_enob_1==1)    #Enob: one selected constraint



#Constraint for cast for   %add154 = fadd double %tmp18, %mul149, !taffo.info !76, !taffo.initweight !35
corr_CAST_add154_fixbits = solver.IntVar(0, 29, 'corr_CAST_add154_fixbits')
corr_CAST_add154_fixp = solver.IntVar(0, 1, 'corr_CAST_add154_fixp')
corr_CAST_add154_float = solver.IntVar(0, 1, 'corr_CAST_add154_float')
corr_CAST_add154_double = solver.IntVar(0, 1, 'corr_CAST_add154_double')
solver.Add( + (1)*corr_CAST_add154_fixp + (1)*corr_CAST_add154_float + (1)*corr_CAST_add154_double==1)    #exactly 1 type
solver.Add( + (1)*corr_CAST_add154_fixbits + (-10000)*corr_CAST_add154_fixp<=0)    #If no fix, fix frac part = 0
C1_corr_CAST_add154 = solver.IntVar(0, 1, 'C1_corr_CAST_add154')
C2_corr_CAST_add154 = solver.IntVar(0, 1, 'C2_corr_CAST_add154')
solver.Add( + (1)*corr_fixbits + (-1)*corr_CAST_add154_fixbits + (-10000)*C1_corr_CAST_add154<=0)    #Shift cost 1
solver.Add( + (-1)*corr_fixbits + (1)*corr_CAST_add154_fixbits + (-10000)*C2_corr_CAST_add154<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_corr_CAST_add154
castCostObj +=  + (1)*C2_corr_CAST_add154
C3_corr_CAST_add154 = solver.IntVar(0, 1, 'C3_corr_CAST_add154')
C4_corr_CAST_add154 = solver.IntVar(0, 1, 'C4_corr_CAST_add154')
C5_corr_CAST_add154 = solver.IntVar(0, 1, 'C5_corr_CAST_add154')
C6_corr_CAST_add154 = solver.IntVar(0, 1, 'C6_corr_CAST_add154')
C7_corr_CAST_add154 = solver.IntVar(0, 1, 'C7_corr_CAST_add154')
C8_corr_CAST_add154 = solver.IntVar(0, 1, 'C8_corr_CAST_add154')
solver.Add( + (1)*corr_fixp + (1)*corr_CAST_add154_float + (-1)*C3_corr_CAST_add154<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_corr_CAST_add154
solver.Add( + (1)*corr_float + (1)*corr_CAST_add154_fixp + (-1)*C4_corr_CAST_add154<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_corr_CAST_add154
solver.Add( + (1)*corr_fixp + (1)*corr_CAST_add154_double + (-1)*C5_corr_CAST_add154<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_corr_CAST_add154
solver.Add( + (1)*corr_double + (1)*corr_CAST_add154_fixp + (-1)*C6_corr_CAST_add154<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_corr_CAST_add154
solver.Add( + (1)*corr_float + (1)*corr_CAST_add154_double + (-1)*C7_corr_CAST_add154<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_corr_CAST_add154
solver.Add( + (1)*corr_double + (1)*corr_CAST_add154_float + (-1)*C8_corr_CAST_add154<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_corr_CAST_add154



#Constraint for cast for   %add154 = fadd double %tmp18, %mul149, !taffo.info !76, !taffo.initweight !35
main_mul149_CAST_add154_fixbits = solver.IntVar(0, 24, 'main_mul149_CAST_add154_fixbits')
main_mul149_CAST_add154_fixp = solver.IntVar(0, 1, 'main_mul149_CAST_add154_fixp')
main_mul149_CAST_add154_float = solver.IntVar(0, 1, 'main_mul149_CAST_add154_float')
main_mul149_CAST_add154_double = solver.IntVar(0, 1, 'main_mul149_CAST_add154_double')
solver.Add( + (1)*main_mul149_CAST_add154_fixp + (1)*main_mul149_CAST_add154_float + (1)*main_mul149_CAST_add154_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul149_CAST_add154_fixbits + (-10000)*main_mul149_CAST_add154_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C1_main_mul149_CAST_add154')
C2_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C2_main_mul149_CAST_add154')
solver.Add( + (1)*main_mul149_fixbits + (-1)*main_mul149_CAST_add154_fixbits + (-10000)*C1_main_mul149_CAST_add154<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul149_fixbits + (1)*main_mul149_CAST_add154_fixbits + (-10000)*C2_main_mul149_CAST_add154<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul149_CAST_add154
castCostObj +=  + (1)*C2_main_mul149_CAST_add154
C3_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C3_main_mul149_CAST_add154')
C4_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C4_main_mul149_CAST_add154')
C5_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C5_main_mul149_CAST_add154')
C6_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C6_main_mul149_CAST_add154')
C7_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C7_main_mul149_CAST_add154')
C8_main_mul149_CAST_add154 = solver.IntVar(0, 1, 'C8_main_mul149_CAST_add154')
solver.Add( + (1)*main_mul149_fixp + (1)*main_mul149_CAST_add154_float + (-1)*C3_main_mul149_CAST_add154<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_mul149_CAST_add154
solver.Add( + (1)*main_mul149_float + (1)*main_mul149_CAST_add154_fixp + (-1)*C4_main_mul149_CAST_add154<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_mul149_CAST_add154
solver.Add( + (1)*main_mul149_fixp + (1)*main_mul149_CAST_add154_double + (-1)*C5_main_mul149_CAST_add154<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_mul149_CAST_add154
solver.Add( + (1)*main_mul149_double + (1)*main_mul149_CAST_add154_fixp + (-1)*C6_main_mul149_CAST_add154<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_mul149_CAST_add154
solver.Add( + (1)*main_mul149_float + (1)*main_mul149_CAST_add154_double + (-1)*C7_main_mul149_CAST_add154<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_mul149_CAST_add154
solver.Add( + (1)*main_mul149_double + (1)*main_mul149_CAST_add154_float + (-1)*C8_main_mul149_CAST_add154<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_mul149_CAST_add154



#Stuff for   %add154 = fadd double %tmp18, %mul149, !taffo.info !76, !taffo.initweight !35
main_add154_fixbits = solver.IntVar(0, 24, 'main_add154_fixbits')
main_add154_fixp = solver.IntVar(0, 1, 'main_add154_fixp')
main_add154_float = solver.IntVar(0, 1, 'main_add154_float')
main_add154_double = solver.IntVar(0, 1, 'main_add154_double')
main_add154_enob = solver.IntVar(-10000, 10000, 'main_add154_enob')
solver.Add( + (1)*main_add154_enob + (-1)*main_add154_fixbits + (10000)*main_add154_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add154_enob + (10000)*main_add154_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add154_enob + (10000)*main_add154_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add154_fixbits + (-10000)*main_add154_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*main_add154_enob<=333)    #Enob constraint for error maximal
enobCostObj +=  + (-1)*main_add154_enob
solver.Add( + (1)*main_add154_fixp + (1)*main_add154_float + (1)*main_add154_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add154_fixbits + (-10000)*main_add154_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*corr_CAST_add154_fixp + (-1)*main_mul149_CAST_add154_fixp==0)    #fix equality
solver.Add( + (1)*corr_CAST_add154_float + (-1)*main_mul149_CAST_add154_float==0)    #float equality
solver.Add( + (1)*corr_CAST_add154_double + (-1)*main_mul149_CAST_add154_double==0)    #double equality
solver.Add( + (1)*corr_CAST_add154_fixbits + (-1)*main_mul149_CAST_add154_fixbits==0)    #same fractional bit
solver.Add( + (1)*corr_CAST_add154_fixp + (-1)*main_add154_fixp==0)    #fix equality
solver.Add( + (1)*corr_CAST_add154_float + (-1)*main_add154_float==0)    #float equality
solver.Add( + (1)*corr_CAST_add154_double + (-1)*main_add154_double==0)    #double equality
solver.Add( + (1)*corr_CAST_add154_fixbits + (-1)*main_add154_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.24179)*main_add154_fixp
mathCostObj +=  + (2.33125)*main_add154_float
mathCostObj +=  + (2.72422)*main_add154_double
solver.Add( + (1)*main_add154_enob + (-1)*corr_enob_memphi_main_tmp18<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add154_enob + (-1)*main_mul149_enob<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add154, double* %arrayidx153, align 8, !taffo.info !17, !taffo.initweight !29
main_add154_CAST_store_fixbits = solver.IntVar(0, 24, 'main_add154_CAST_store_fixbits')
main_add154_CAST_store_fixp = solver.IntVar(0, 1, 'main_add154_CAST_store_fixp')
main_add154_CAST_store_float = solver.IntVar(0, 1, 'main_add154_CAST_store_float')
main_add154_CAST_store_double = solver.IntVar(0, 1, 'main_add154_CAST_store_double')
solver.Add( + (1)*main_add154_CAST_store_fixp + (1)*main_add154_CAST_store_float + (1)*main_add154_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add154_CAST_store_fixbits + (-10000)*main_add154_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add154_CAST_store = solver.IntVar(0, 1, 'C1_main_add154_CAST_store')
C2_main_add154_CAST_store = solver.IntVar(0, 1, 'C2_main_add154_CAST_store')
solver.Add( + (1)*main_add154_fixbits + (-1)*main_add154_CAST_store_fixbits + (-10000)*C1_main_add154_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add154_fixbits + (1)*main_add154_CAST_store_fixbits + (-10000)*C2_main_add154_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add154_CAST_store
castCostObj +=  + (1)*C2_main_add154_CAST_store
C3_main_add154_CAST_store = solver.IntVar(0, 1, 'C3_main_add154_CAST_store')
C4_main_add154_CAST_store = solver.IntVar(0, 1, 'C4_main_add154_CAST_store')
C5_main_add154_CAST_store = solver.IntVar(0, 1, 'C5_main_add154_CAST_store')
C6_main_add154_CAST_store = solver.IntVar(0, 1, 'C6_main_add154_CAST_store')
C7_main_add154_CAST_store = solver.IntVar(0, 1, 'C7_main_add154_CAST_store')
C8_main_add154_CAST_store = solver.IntVar(0, 1, 'C8_main_add154_CAST_store')
solver.Add( + (1)*main_add154_fixp + (1)*main_add154_CAST_store_float + (-1)*C3_main_add154_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_main_add154_CAST_store
solver.Add( + (1)*main_add154_float + (1)*main_add154_CAST_store_fixp + (-1)*C4_main_add154_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_main_add154_CAST_store
solver.Add( + (1)*main_add154_fixp + (1)*main_add154_CAST_store_double + (-1)*C5_main_add154_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_main_add154_CAST_store
solver.Add( + (1)*main_add154_double + (1)*main_add154_CAST_store_fixp + (-1)*C6_main_add154_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_main_add154_CAST_store
solver.Add( + (1)*main_add154_float + (1)*main_add154_CAST_store_double + (-1)*C7_main_add154_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_main_add154_CAST_store
solver.Add( + (1)*main_add154_double + (1)*main_add154_CAST_store_float + (-1)*C8_main_add154_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_main_add154_CAST_store
solver.Add( + (1)*corr_fixp + (-1)*main_add154_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*corr_float + (-1)*main_add154_CAST_store_float==0)    #float equality
solver.Add( + (1)*corr_double + (-1)*main_add154_CAST_store_double==0)    #double equality
solver.Add( + (1)*corr_fixbits + (-1)*main_add154_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
corr_enob_storeENOB = solver.IntVar(-10000, 10000, 'corr_enob_storeENOB')
solver.Add( + (1)*corr_enob_storeENOB + (-1)*corr_fixbits + (10000)*corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*corr_enob_storeENOB + (10000)*corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*corr_enob_storeENOB + (10000)*corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*corr_enob_storeENOB + (-1)*main_add154_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*corr_enob_memphi_main_tmp18 + (-1)*corr_enob_storeENOB + (10000)*main_main_tmp18_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
corr_enob_memphi_main_tmp19 = solver.IntVar(-10000, 10000, 'corr_enob_memphi_main_tmp19')
solver.Add( + (1)*corr_enob_memphi_main_tmp19 + (-1)*corr_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp19_enob_1 = solver.IntVar(0, 1, 'main_main_tmp19_enob_1')
solver.Add( + (1)*main_main_tmp19_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*corr_enob_memphi_main_tmp19 + (-1)*corr_enob_storeENOB + (10000)*main_main_tmp19_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp19, double* %arrayidx165, align 8, !taffo.info !17, !taffo.initweight !29
corr_CAST_store_fixbits = solver.IntVar(0, 29, 'corr_CAST_store_fixbits')
corr_CAST_store_fixp = solver.IntVar(0, 1, 'corr_CAST_store_fixp')
corr_CAST_store_float = solver.IntVar(0, 1, 'corr_CAST_store_float')
corr_CAST_store_double = solver.IntVar(0, 1, 'corr_CAST_store_double')
solver.Add( + (1)*corr_CAST_store_fixp + (1)*corr_CAST_store_float + (1)*corr_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*corr_CAST_store_fixbits + (-10000)*corr_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_corr_CAST_store = solver.IntVar(0, 1, 'C1_corr_CAST_store')
C2_corr_CAST_store = solver.IntVar(0, 1, 'C2_corr_CAST_store')
solver.Add( + (1)*corr_fixbits + (-1)*corr_CAST_store_fixbits + (-10000)*C1_corr_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*corr_fixbits + (1)*corr_CAST_store_fixbits + (-10000)*C2_corr_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_corr_CAST_store
castCostObj +=  + (1)*C2_corr_CAST_store
C3_corr_CAST_store = solver.IntVar(0, 1, 'C3_corr_CAST_store')
C4_corr_CAST_store = solver.IntVar(0, 1, 'C4_corr_CAST_store')
C5_corr_CAST_store = solver.IntVar(0, 1, 'C5_corr_CAST_store')
C6_corr_CAST_store = solver.IntVar(0, 1, 'C6_corr_CAST_store')
C7_corr_CAST_store = solver.IntVar(0, 1, 'C7_corr_CAST_store')
C8_corr_CAST_store = solver.IntVar(0, 1, 'C8_corr_CAST_store')
solver.Add( + (1)*corr_fixp + (1)*corr_CAST_store_float + (-1)*C3_corr_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_corr_CAST_store
solver.Add( + (1)*corr_float + (1)*corr_CAST_store_fixp + (-1)*C4_corr_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_corr_CAST_store
solver.Add( + (1)*corr_fixp + (1)*corr_CAST_store_double + (-1)*C5_corr_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_corr_CAST_store
solver.Add( + (1)*corr_double + (1)*corr_CAST_store_fixp + (-1)*C6_corr_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_corr_CAST_store
solver.Add( + (1)*corr_float + (1)*corr_CAST_store_double + (-1)*C7_corr_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_corr_CAST_store
solver.Add( + (1)*corr_double + (1)*corr_CAST_store_float + (-1)*C8_corr_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_corr_CAST_store
solver.Add( + (1)*corr_fixp + (-1)*corr_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*corr_float + (-1)*corr_CAST_store_float==0)    #float equality
solver.Add( + (1)*corr_double + (-1)*corr_CAST_store_double==0)    #double equality
solver.Add( + (1)*corr_fixbits + (-1)*corr_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
corr_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'corr_enob_storeENOB_storeENOB')
solver.Add( + (1)*corr_enob_storeENOB_storeENOB + (-1)*corr_fixbits + (10000)*corr_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*corr_enob_storeENOB_storeENOB + (10000)*corr_float<=10149)    #Enob constraint for float
solver.Add( + (1)*corr_enob_storeENOB_storeENOB + (10000)*corr_double<=11074)    #Enob constraint for double
solver.Add( + (1)*corr_enob_storeENOB_storeENOB + (-1)*corr_enob_memphi_main_tmp19<=0)    #Enob constraint ENOB propagation in load/store



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



#Constraint for cast for   store double 1.000000e+00, double* getelementptr inbounds ([28 x [28 x double]], [28 x [28 x double]]* @corr, i64 0, i64 27, i64 27), align 8, !taffo.info !17, !taffo.initweight !28, !taffo.constinfo !71
ConstantValue__25_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__25_CAST_store_fixbits')
ConstantValue__25_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__25_CAST_store_fixp')
ConstantValue__25_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__25_CAST_store_float')
ConstantValue__25_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__25_CAST_store_double')
solver.Add( + (1)*ConstantValue__25_CAST_store_fixp + (1)*ConstantValue__25_CAST_store_float + (1)*ConstantValue__25_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__25_CAST_store_fixbits + (-10000)*ConstantValue__25_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__25_CAST_store')
C2_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__25_CAST_store')
solver.Add( + (1)*ConstantValue__25_fixbits + (-1)*ConstantValue__25_CAST_store_fixbits + (-10000)*C1_ConstantValue__25_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__25_fixbits + (1)*ConstantValue__25_CAST_store_fixbits + (-10000)*C2_ConstantValue__25_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__25_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__25_CAST_store
C3_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__25_CAST_store')
C4_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__25_CAST_store')
C5_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__25_CAST_store')
C6_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__25_CAST_store')
C7_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__25_CAST_store')
C8_ConstantValue__25_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__25_CAST_store')
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_CAST_store_float + (-1)*C3_ConstantValue__25_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_ConstantValue__25_CAST_store
solver.Add( + (1)*ConstantValue__25_float + (1)*ConstantValue__25_CAST_store_fixp + (-1)*C4_ConstantValue__25_CAST_store<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_ConstantValue__25_CAST_store
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_CAST_store_double + (-1)*C5_ConstantValue__25_CAST_store<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_ConstantValue__25_CAST_store
solver.Add( + (1)*ConstantValue__25_double + (1)*ConstantValue__25_CAST_store_fixp + (-1)*C6_ConstantValue__25_CAST_store<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_ConstantValue__25_CAST_store
solver.Add( + (1)*ConstantValue__25_float + (1)*ConstantValue__25_CAST_store_double + (-1)*C7_ConstantValue__25_CAST_store<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_ConstantValue__25_CAST_store
solver.Add( + (1)*ConstantValue__25_double + (1)*ConstantValue__25_CAST_store_float + (-1)*C8_ConstantValue__25_CAST_store<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_ConstantValue__25_CAST_store
solver.Add( + (1)*corr_fixp + (-1)*ConstantValue__25_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*corr_float + (-1)*ConstantValue__25_CAST_store_float==0)    #float equality
solver.Add( + (1)*corr_double + (-1)*ConstantValue__25_CAST_store_double==0)    #double equality
solver.Add( + (1)*corr_fixbits + (-1)*ConstantValue__25_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
corr_enob_memphi_main_tmp20 = solver.IntVar(-10000, 10000, 'corr_enob_memphi_main_tmp20')
solver.Add( + (1)*corr_enob_memphi_main_tmp20 + (-1)*corr_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %call184 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.6, i32 0, i32 0), double %tmp20), !taffo.info !17, !taffo.initweight !35, !taffo.constinfo !78
corr_CAST_call184_fixbits = solver.IntVar(0, 29, 'corr_CAST_call184_fixbits')
corr_CAST_call184_fixp = solver.IntVar(0, 1, 'corr_CAST_call184_fixp')
corr_CAST_call184_float = solver.IntVar(0, 1, 'corr_CAST_call184_float')
corr_CAST_call184_double = solver.IntVar(0, 1, 'corr_CAST_call184_double')
solver.Add( + (1)*corr_CAST_call184_fixp + (1)*corr_CAST_call184_float + (1)*corr_CAST_call184_double==1)    #exactly 1 type
solver.Add( + (1)*corr_CAST_call184_fixbits + (-10000)*corr_CAST_call184_fixp<=0)    #If no fix, fix frac part = 0
C1_corr_CAST_call184 = solver.IntVar(0, 1, 'C1_corr_CAST_call184')
C2_corr_CAST_call184 = solver.IntVar(0, 1, 'C2_corr_CAST_call184')
solver.Add( + (1)*corr_fixbits + (-1)*corr_CAST_call184_fixbits + (-10000)*C1_corr_CAST_call184<=0)    #Shift cost 1
solver.Add( + (-1)*corr_fixbits + (1)*corr_CAST_call184_fixbits + (-10000)*C2_corr_CAST_call184<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_corr_CAST_call184
castCostObj +=  + (1)*C2_corr_CAST_call184
C3_corr_CAST_call184 = solver.IntVar(0, 1, 'C3_corr_CAST_call184')
C4_corr_CAST_call184 = solver.IntVar(0, 1, 'C4_corr_CAST_call184')
C5_corr_CAST_call184 = solver.IntVar(0, 1, 'C5_corr_CAST_call184')
C6_corr_CAST_call184 = solver.IntVar(0, 1, 'C6_corr_CAST_call184')
C7_corr_CAST_call184 = solver.IntVar(0, 1, 'C7_corr_CAST_call184')
C8_corr_CAST_call184 = solver.IntVar(0, 1, 'C8_corr_CAST_call184')
solver.Add( + (1)*corr_fixp + (1)*corr_CAST_call184_float + (-1)*C3_corr_CAST_call184<=1)    #Fix to float
castCostObj +=  + (6.62652)*C3_corr_CAST_call184
solver.Add( + (1)*corr_float + (1)*corr_CAST_call184_fixp + (-1)*C4_corr_CAST_call184<=1)    #Float to fix
castCostObj +=  + (3.2755)*C4_corr_CAST_call184
solver.Add( + (1)*corr_fixp + (1)*corr_CAST_call184_double + (-1)*C5_corr_CAST_call184<=1)    #Fix to double
castCostObj +=  + (19.8918)*C5_corr_CAST_call184
solver.Add( + (1)*corr_double + (1)*corr_CAST_call184_fixp + (-1)*C6_corr_CAST_call184<=1)    #Double to fix
castCostObj +=  + (4.64839)*C6_corr_CAST_call184
solver.Add( + (1)*corr_float + (1)*corr_CAST_call184_double + (-1)*C7_corr_CAST_call184<=1)    #Float to double
castCostObj +=  + (1.62799)*C7_corr_CAST_call184
solver.Add( + (1)*corr_double + (1)*corr_CAST_call184_float + (-1)*C8_corr_CAST_call184<=1)    #Double to float
castCostObj +=  + (1.79206)*C8_corr_CAST_call184
solver.Add( + (1)*corr_CAST_call184_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(1000 * castCostObj / 994.588+ 1 * enobCostObj / 9769+ 1000 * mathCostObj / 122.77)

# Model declaration end.