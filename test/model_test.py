


#Stuff for @DX = common dso_local global double 0.000000e+00, align 8, !taffo.info !4, !taffo.initweight !6
DX_fixbits = solver.IntVar(0, 31, 'DX_fixbits')
DX_fixp = solver.IntVar(0, 1, 'DX_fixp')
DX_float = solver.IntVar(0, 1, 'DX_float')
DX_double = solver.IntVar(0, 1, 'DX_double')
DX_enob = solver.IntVar(-10000, 10000, 'DX_enob')
solver.Add( + (1)*DX_enob + (-1)*DX_fixbits + (10000)*DX_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*DX_enob + (10000)*DX_float<=10149)    #Enob constraint for float
solver.Add( + (1)*DX_enob + (10000)*DX_double<=11074)    #Enob constraint for double
solver.Add( + (1)*DX_fixbits + (-10000)*DX_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*DX_double<=0)    #Disable double data type
enobCostObj =  + (-1)*DX_enob
solver.Add( + (1)*DX_fixp + (1)*DX_float + (1)*DX_double==1)    #Exactly one selected type
solver.Add( + (1)*DX_fixbits + (-10000)*DX_fixp<=0)    #If not fix, frac part to zero



#Stuff for @DY = common dso_local global double 0.000000e+00, align 8, !taffo.info !4, !taffo.initweight !6
DY_fixbits = solver.IntVar(0, 31, 'DY_fixbits')
DY_fixp = solver.IntVar(0, 1, 'DY_fixp')
DY_float = solver.IntVar(0, 1, 'DY_float')
DY_double = solver.IntVar(0, 1, 'DY_double')
DY_enob = solver.IntVar(-10000, 10000, 'DY_enob')
solver.Add( + (1)*DY_enob + (-1)*DY_fixbits + (10000)*DY_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*DY_enob + (10000)*DY_float<=10149)    #Enob constraint for float
solver.Add( + (1)*DY_enob + (10000)*DY_double<=11074)    #Enob constraint for double
solver.Add( + (1)*DY_fixbits + (-10000)*DY_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*DY_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*DY_enob
solver.Add( + (1)*DY_fixp + (1)*DY_float + (1)*DY_double==1)    #Exactly one selected type
solver.Add( + (1)*DY_fixbits + (-10000)*DY_fixp<=0)    #If not fix, frac part to zero



#Stuff for @DT = common dso_local global double 0.000000e+00, align 8, !taffo.info !7, !taffo.initweight !6
DT_fixbits = solver.IntVar(0, 31, 'DT_fixbits')
DT_fixp = solver.IntVar(0, 1, 'DT_fixp')
DT_float = solver.IntVar(0, 1, 'DT_float')
DT_double = solver.IntVar(0, 1, 'DT_double')
DT_enob = solver.IntVar(-10000, 10000, 'DT_enob')
solver.Add( + (1)*DT_enob + (-1)*DT_fixbits + (10000)*DT_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*DT_enob + (10000)*DT_float<=10149)    #Enob constraint for float
solver.Add( + (1)*DT_enob + (10000)*DT_double<=11074)    #Enob constraint for double
solver.Add( + (1)*DT_fixbits + (-10000)*DT_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*DT_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*DT_enob
solver.Add( + (1)*DT_fixp + (1)*DT_float + (1)*DT_double==1)    #Exactly one selected type
solver.Add( + (1)*DT_fixbits + (-10000)*DT_fixp<=0)    #If not fix, frac part to zero



#Stuff for @B1 = common dso_local global double 0.000000e+00, align 8, !taffo.info !9, !taffo.initweight !6
B1_fixbits = solver.IntVar(0, 30, 'B1_fixbits')
B1_fixp = solver.IntVar(0, 1, 'B1_fixp')
B1_float = solver.IntVar(0, 1, 'B1_float')
B1_double = solver.IntVar(0, 1, 'B1_double')
B1_enob = solver.IntVar(-10000, 10000, 'B1_enob')
solver.Add( + (1)*B1_enob + (-1)*B1_fixbits + (10000)*B1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B1_enob + (10000)*B1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B1_enob + (10000)*B1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B1_fixbits + (-10000)*B1_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*B1_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*B1_enob
solver.Add( + (1)*B1_fixp + (1)*B1_float + (1)*B1_double==1)    #Exactly one selected type
solver.Add( + (1)*B1_fixbits + (-10000)*B1_fixp<=0)    #If not fix, frac part to zero



#Stuff for @B2 = common dso_local global double 0.000000e+00, align 8, !taffo.info !11, !taffo.initweight !6
B2_fixbits = solver.IntVar(0, 31, 'B2_fixbits')
B2_fixp = solver.IntVar(0, 1, 'B2_fixp')
B2_float = solver.IntVar(0, 1, 'B2_float')
B2_double = solver.IntVar(0, 1, 'B2_double')
B2_enob = solver.IntVar(-10000, 10000, 'B2_enob')
solver.Add( + (1)*B2_enob + (-1)*B2_fixbits + (10000)*B2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*B2_enob + (10000)*B2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*B2_enob + (10000)*B2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*B2_fixbits + (-10000)*B2_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*B2_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*B2_enob
solver.Add( + (1)*B2_fixp + (1)*B2_float + (1)*B2_double==1)    #Exactly one selected type
solver.Add( + (1)*B2_fixbits + (-10000)*B2_fixp<=0)    #If not fix, frac part to zero



#Stuff for @mul1 = common dso_local global double 0.000000e+00, align 8, !taffo.info !13, !taffo.initweight !6
mul1_fixbits = solver.IntVar(0, 22, 'mul1_fixbits')
mul1_fixp = solver.IntVar(0, 1, 'mul1_fixp')
mul1_float = solver.IntVar(0, 1, 'mul1_float')
mul1_double = solver.IntVar(0, 1, 'mul1_double')
mul1_enob = solver.IntVar(-10000, 10000, 'mul1_enob')
solver.Add( + (1)*mul1_enob + (-1)*mul1_fixbits + (10000)*mul1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mul1_enob + (10000)*mul1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mul1_enob + (10000)*mul1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mul1_fixbits + (-10000)*mul1_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*mul1_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*mul1_enob
solver.Add( + (1)*mul1_fixp + (1)*mul1_float + (1)*mul1_double==1)    #Exactly one selected type
solver.Add( + (1)*mul1_fixbits + (-10000)*mul1_fixp<=0)    #If not fix, frac part to zero



#Stuff for @mul2 = common dso_local global double 0.000000e+00, align 8, !taffo.info !15, !taffo.initweight !6
mul2_fixbits = solver.IntVar(0, 23, 'mul2_fixbits')
mul2_fixp = solver.IntVar(0, 1, 'mul2_fixp')
mul2_float = solver.IntVar(0, 1, 'mul2_float')
mul2_double = solver.IntVar(0, 1, 'mul2_double')
mul2_enob = solver.IntVar(-10000, 10000, 'mul2_enob')
solver.Add( + (1)*mul2_enob + (-1)*mul2_fixbits + (10000)*mul2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mul2_enob + (10000)*mul2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mul2_enob + (10000)*mul2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mul2_fixbits + (-10000)*mul2_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*mul2_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*mul2_enob
solver.Add( + (1)*mul2_fixp + (1)*mul2_float + (1)*mul2_double==1)    #Exactly one selected type
solver.Add( + (1)*mul2_fixbits + (-10000)*mul2_fixp<=0)    #If not fix, frac part to zero



#Stuff for @a = common dso_local global double 0.000000e+00, align 8, !taffo.info !17, !taffo.initweight !6
a_fixbits = solver.IntVar(0, 22, 'a_fixbits')
a_fixp = solver.IntVar(0, 1, 'a_fixp')
a_float = solver.IntVar(0, 1, 'a_float')
a_double = solver.IntVar(0, 1, 'a_double')
a_enob = solver.IntVar(-10000, 10000, 'a_enob')
solver.Add( + (1)*a_enob + (-1)*a_fixbits + (10000)*a_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*a_enob + (10000)*a_float<=10149)    #Enob constraint for float
solver.Add( + (1)*a_enob + (10000)*a_double<=11074)    #Enob constraint for double
solver.Add( + (1)*a_fixbits + (-10000)*a_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*a_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*a_enob
solver.Add( + (1)*a_fixp + (1)*a_float + (1)*a_double==1)    #Exactly one selected type
solver.Add( + (1)*a_fixbits + (-10000)*a_fixp<=0)    #If not fix, frac part to zero



#Stuff for @b = common dso_local global double 0.000000e+00, align 8, !taffo.info !19, !taffo.initweight !6
b_fixbits = solver.IntVar(0, 22, 'b_fixbits')
b_fixp = solver.IntVar(0, 1, 'b_fixp')
b_float = solver.IntVar(0, 1, 'b_float')
b_double = solver.IntVar(0, 1, 'b_double')
b_enob = solver.IntVar(-10000, 10000, 'b_enob')
solver.Add( + (1)*b_enob + (-1)*b_fixbits + (10000)*b_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*b_enob + (10000)*b_float<=10149)    #Enob constraint for float
solver.Add( + (1)*b_enob + (10000)*b_double<=11074)    #Enob constraint for double
solver.Add( + (1)*b_fixbits + (-10000)*b_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*b_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*b_enob
solver.Add( + (1)*b_fixp + (1)*b_float + (1)*b_double==1)    #Exactly one selected type
solver.Add( + (1)*b_fixbits + (-10000)*b_fixp<=0)    #If not fix, frac part to zero



#Stuff for @c = common dso_local global double 0.000000e+00, align 8, !taffo.info !17, !taffo.initweight !6
c_fixbits = solver.IntVar(0, 22, 'c_fixbits')
c_fixp = solver.IntVar(0, 1, 'c_fixp')
c_float = solver.IntVar(0, 1, 'c_float')
c_double = solver.IntVar(0, 1, 'c_double')
c_enob = solver.IntVar(-10000, 10000, 'c_enob')
solver.Add( + (1)*c_enob + (-1)*c_fixbits + (10000)*c_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*c_enob + (10000)*c_float<=10149)    #Enob constraint for float
solver.Add( + (1)*c_enob + (10000)*c_double<=11074)    #Enob constraint for double
solver.Add( + (1)*c_fixbits + (-10000)*c_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*c_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*c_enob
solver.Add( + (1)*c_fixp + (1)*c_float + (1)*c_double==1)    #Exactly one selected type
solver.Add( + (1)*c_fixbits + (-10000)*c_fixp<=0)    #If not fix, frac part to zero



#Stuff for @d = common dso_local global double 0.000000e+00, align 8, !taffo.info !21, !taffo.initweight !6
d_fixbits = solver.IntVar(0, 23, 'd_fixbits')
d_fixp = solver.IntVar(0, 1, 'd_fixp')
d_float = solver.IntVar(0, 1, 'd_float')
d_double = solver.IntVar(0, 1, 'd_double')
d_enob = solver.IntVar(-10000, 10000, 'd_enob')
solver.Add( + (1)*d_enob + (-1)*d_fixbits + (10000)*d_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*d_enob + (10000)*d_float<=10149)    #Enob constraint for float
solver.Add( + (1)*d_enob + (10000)*d_double<=11074)    #Enob constraint for double
solver.Add( + (1)*d_fixbits + (-10000)*d_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*d_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*d_enob
solver.Add( + (1)*d_fixp + (1)*d_float + (1)*d_double==1)    #Exactly one selected type
solver.Add( + (1)*d_fixbits + (-10000)*d_fixp<=0)    #If not fix, frac part to zero



#Stuff for @e = common dso_local global double 0.000000e+00, align 8, !taffo.info !23, !taffo.initweight !6
e_fixbits = solver.IntVar(0, 23, 'e_fixbits')
e_fixp = solver.IntVar(0, 1, 'e_fixp')
e_float = solver.IntVar(0, 1, 'e_float')
e_double = solver.IntVar(0, 1, 'e_double')
e_enob = solver.IntVar(-10000, 10000, 'e_enob')
solver.Add( + (1)*e_enob + (-1)*e_fixbits + (10000)*e_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*e_enob + (10000)*e_float<=10149)    #Enob constraint for float
solver.Add( + (1)*e_enob + (10000)*e_double<=11074)    #Enob constraint for double
solver.Add( + (1)*e_fixbits + (-10000)*e_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*e_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*e_enob
solver.Add( + (1)*e_fixp + (1)*e_float + (1)*e_double==1)    #Exactly one selected type
solver.Add( + (1)*e_fixbits + (-10000)*e_fixp<=0)    #If not fix, frac part to zero



#Stuff for @f = common dso_local global double 0.000000e+00, align 8, !taffo.info !21, !taffo.initweight !6
f_fixbits = solver.IntVar(0, 23, 'f_fixbits')
f_fixp = solver.IntVar(0, 1, 'f_fixp')
f_float = solver.IntVar(0, 1, 'f_float')
f_double = solver.IntVar(0, 1, 'f_double')
f_enob = solver.IntVar(-10000, 10000, 'f_enob')
solver.Add( + (1)*f_enob + (-1)*f_fixbits + (10000)*f_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*f_enob + (10000)*f_float<=10149)    #Enob constraint for float
solver.Add( + (1)*f_enob + (10000)*f_double<=11074)    #Enob constraint for double
solver.Add( + (1)*f_fixbits + (-10000)*f_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*f_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*f_enob
solver.Add( + (1)*f_fixp + (1)*f_float + (1)*f_double==1)    #Exactly one selected type
solver.Add( + (1)*f_fixbits + (-10000)*f_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %u = alloca [200 x [200 x double]], align 16, !taffo.info !33, !taffo.initweight !6
main_u_fixbits = solver.IntVar(0, 28, 'main_u_fixbits')
main_u_fixp = solver.IntVar(0, 1, 'main_u_fixp')
main_u_float = solver.IntVar(0, 1, 'main_u_float')
main_u_double = solver.IntVar(0, 1, 'main_u_double')
main_u_enob = solver.IntVar(-10000, 10000, 'main_u_enob')
solver.Add( + (1)*main_u_enob + (-1)*main_u_fixbits + (10000)*main_u_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_u_enob + (10000)*main_u_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_u_enob + (10000)*main_u_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_u_fixbits + (-10000)*main_u_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_u_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_u_enob
solver.Add( + (1)*main_u_fixp + (1)*main_u_float + (1)*main_u_double==1)    #Exactly one selected type
solver.Add( + (1)*main_u_fixbits + (-10000)*main_u_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %v = alloca [200 x [200 x double]], align 16, !taffo.info !35, !taffo.initweight !6
main_v_fixbits = solver.IntVar(0, 29, 'main_v_fixbits')
main_v_fixp = solver.IntVar(0, 1, 'main_v_fixp')
main_v_float = solver.IntVar(0, 1, 'main_v_float')
main_v_double = solver.IntVar(0, 1, 'main_v_double')
main_v_enob = solver.IntVar(-10000, 10000, 'main_v_enob')
solver.Add( + (1)*main_v_enob + (-1)*main_v_fixbits + (10000)*main_v_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_v_enob + (10000)*main_v_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_v_enob + (10000)*main_v_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_v_fixbits + (-10000)*main_v_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_v_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_v_enob
solver.Add( + (1)*main_v_fixp + (1)*main_v_float + (1)*main_v_double==1)    #Exactly one selected type
solver.Add( + (1)*main_v_fixbits + (-10000)*main_v_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %p = alloca [200 x [200 x double]], align 16, !taffo.info !37, !taffo.initweight !6
main_p_fixbits = solver.IntVar(0, 30, 'main_p_fixbits')
main_p_fixp = solver.IntVar(0, 1, 'main_p_fixp')
main_p_float = solver.IntVar(0, 1, 'main_p_float')
main_p_double = solver.IntVar(0, 1, 'main_p_double')
main_p_enob = solver.IntVar(-10000, 10000, 'main_p_enob')
solver.Add( + (1)*main_p_enob + (-1)*main_p_fixbits + (10000)*main_p_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_p_enob + (10000)*main_p_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_p_enob + (10000)*main_p_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_p_fixbits + (-10000)*main_p_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_p_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_p_enob
solver.Add( + (1)*main_p_fixp + (1)*main_p_float + (1)*main_p_double==1)    #Exactly one selected type
solver.Add( + (1)*main_p_fixbits + (-10000)*main_p_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %q = alloca [200 x [200 x double]], align 16, !taffo.info !39, !taffo.initweight !6
main_q_fixbits = solver.IntVar(0, 22, 'main_q_fixbits')
main_q_fixp = solver.IntVar(0, 1, 'main_q_fixp')
main_q_float = solver.IntVar(0, 1, 'main_q_float')
main_q_double = solver.IntVar(0, 1, 'main_q_double')
main_q_enob = solver.IntVar(-10000, 10000, 'main_q_enob')
solver.Add( + (1)*main_q_enob + (-1)*main_q_fixbits + (10000)*main_q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_q_enob + (10000)*main_q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_q_enob + (10000)*main_q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_q_fixbits + (-10000)*main_q_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_q_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_q_enob
solver.Add( + (1)*main_q_fixp + (1)*main_q_float + (1)*main_q_double==1)    #Exactly one selected type
solver.Add( + (1)*main_q_fixbits + (-10000)*main_q_fixp<=0)    #If not fix, frac part to zero



#Stuff for   %conv = sitofp i32 %sub to double, !taffo.info !43, !taffo.initweight !45
main_conv_fixbits = solver.IntVar(0, 23, 'main_conv_fixbits')
main_conv_fixp = solver.IntVar(0, 1, 'main_conv_fixp')
main_conv_float = solver.IntVar(0, 1, 'main_conv_float')
main_conv_double = solver.IntVar(0, 1, 'main_conv_double')
main_conv_enob = solver.IntVar(-10000, 10000, 'main_conv_enob')
solver.Add( + (1)*main_conv_enob + (-1)*main_conv_fixbits + (10000)*main_conv_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_conv_enob + (10000)*main_conv_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_conv_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_conv_enob
solver.Add( + (1)*main_conv_fixp + (1)*main_conv_float + (1)*main_conv_double==1)    #Exactly one selected type
solver.Add( + (1)*main_conv_fixbits + (-10000)*main_conv_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-03
ConstantValue__fixbits = solver.IntVar(0, 31, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10031)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10060)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-03
ConstantValue__0_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10031)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10060)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__0_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 5.000000e-03, double* @DX, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !57
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
solver.Add( + (1)*DX_fixp + (-1)*ConstantValue__0_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*DX_float + (-1)*ConstantValue__0_CAST_store_float==0)    #float equality
solver.Add( + (1)*DX_double + (-1)*ConstantValue__0_CAST_store_double==0)    #double equality
solver.Add( + (1)*DX_fixbits + (-1)*ConstantValue__0_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 5.000000e-03
ConstantValue__1_fixbits = solver.IntVar(0, 31, 'ConstantValue__1_fixbits')
ConstantValue__1_fixp = solver.IntVar(0, 1, 'ConstantValue__1_fixp')
ConstantValue__1_float = solver.IntVar(0, 1, 'ConstantValue__1_float')
ConstantValue__1_double = solver.IntVar(0, 1, 'ConstantValue__1_double')
ConstantValue__1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__1_enob')
solver.Add( + (1)*ConstantValue__1_enob + (-1)*ConstantValue__1_fixbits + (10000)*ConstantValue__1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_float<=10031)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__1_enob + (10000)*ConstantValue__1_double<=10060)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__1_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__1_fixp + (1)*ConstantValue__1_float + (1)*ConstantValue__1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__1_fixbits + (-10000)*ConstantValue__1_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 5.000000e-03
ConstantValue__2_fixbits = solver.IntVar(0, 31, 'ConstantValue__2_fixbits')
ConstantValue__2_fixp = solver.IntVar(0, 1, 'ConstantValue__2_fixp')
ConstantValue__2_float = solver.IntVar(0, 1, 'ConstantValue__2_float')
ConstantValue__2_double = solver.IntVar(0, 1, 'ConstantValue__2_double')
ConstantValue__2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__2_enob')
solver.Add( + (1)*ConstantValue__2_enob + (-1)*ConstantValue__2_fixbits + (10000)*ConstantValue__2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_float<=10031)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__2_enob + (10000)*ConstantValue__2_double<=10060)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__2_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__2_fixp + (1)*ConstantValue__2_float + (1)*ConstantValue__2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__2_fixbits + (-10000)*ConstantValue__2_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 5.000000e-03, double* @DY, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !57
ConstantValue__2_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__2_CAST_store_fixbits')
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
solver.Add( + (1)*DY_fixp + (-1)*ConstantValue__2_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*DY_float + (-1)*ConstantValue__2_CAST_store_float==0)    #float equality
solver.Add( + (1)*DY_double + (-1)*ConstantValue__2_CAST_store_double==0)    #double equality
solver.Add( + (1)*DY_fixbits + (-1)*ConstantValue__2_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 1.000000e-02
ConstantValue__3_fixbits = solver.IntVar(0, 31, 'ConstantValue__3_fixbits')
ConstantValue__3_fixp = solver.IntVar(0, 1, 'ConstantValue__3_fixp')
ConstantValue__3_float = solver.IntVar(0, 1, 'ConstantValue__3_float')
ConstantValue__3_double = solver.IntVar(0, 1, 'ConstantValue__3_double')
ConstantValue__3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__3_enob')
solver.Add( + (1)*ConstantValue__3_enob + (-1)*ConstantValue__3_fixbits + (10000)*ConstantValue__3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_float<=10030)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__3_enob + (10000)*ConstantValue__3_double<=10059)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__3_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__3_fixp + (1)*ConstantValue__3_float + (1)*ConstantValue__3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__3_fixbits + (-10000)*ConstantValue__3_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e-02
ConstantValue__4_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_fixbits')
ConstantValue__4_fixp = solver.IntVar(0, 1, 'ConstantValue__4_fixp')
ConstantValue__4_float = solver.IntVar(0, 1, 'ConstantValue__4_float')
ConstantValue__4_double = solver.IntVar(0, 1, 'ConstantValue__4_double')
ConstantValue__4_enob = solver.IntVar(-10000, 10000, 'ConstantValue__4_enob')
solver.Add( + (1)*ConstantValue__4_enob + (-1)*ConstantValue__4_fixbits + (10000)*ConstantValue__4_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_float<=10030)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__4_enob + (10000)*ConstantValue__4_double<=10059)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__4_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_float + (1)*ConstantValue__4_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__4_fixbits + (-10000)*ConstantValue__4_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e-02, double* @DT, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !60
ConstantValue__4_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__4_CAST_store_fixbits')
ConstantValue__4_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_fixp')
ConstantValue__4_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_float')
ConstantValue__4_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__4_CAST_store_double')
solver.Add( + (1)*ConstantValue__4_CAST_store_fixp + (1)*ConstantValue__4_CAST_store_float + (1)*ConstantValue__4_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__4_CAST_store_fixbits + (-10000)*ConstantValue__4_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__4_CAST_store')
C2_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__4_CAST_store')
solver.Add( + (1)*ConstantValue__4_fixbits + (-1)*ConstantValue__4_CAST_store_fixbits + (-10000)*C1_ConstantValue__4_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__4_fixbits + (1)*ConstantValue__4_CAST_store_fixbits + (-10000)*C2_ConstantValue__4_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__4_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__4_CAST_store
C3_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__4_CAST_store')
C4_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__4_CAST_store')
C5_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__4_CAST_store')
C6_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__4_CAST_store')
C7_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__4_CAST_store')
C8_ConstantValue__4_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__4_CAST_store')
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_float + (-1)*C3_ConstantValue__4_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_fixp + (-1)*C4_ConstantValue__4_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_fixp + (1)*ConstantValue__4_CAST_store_double + (-1)*C5_ConstantValue__4_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_fixp + (-1)*C6_ConstantValue__4_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_float + (1)*ConstantValue__4_CAST_store_double + (-1)*C7_ConstantValue__4_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__4_CAST_store
solver.Add( + (1)*ConstantValue__4_double + (1)*ConstantValue__4_CAST_store_float + (-1)*C8_ConstantValue__4_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__4_CAST_store
solver.Add( + (1)*DT_fixp + (-1)*ConstantValue__4_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*DT_float + (-1)*ConstantValue__4_CAST_store_float==0)    #float equality
solver.Add( + (1)*DT_double + (-1)*ConstantValue__4_CAST_store_double==0)    #double equality
solver.Add( + (1)*DT_fixbits + (-1)*ConstantValue__4_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



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



#Stuff for double 2.000000e+00
ConstantValue__6_fixbits = solver.IntVar(0, 30, 'ConstantValue__6_fixbits')
ConstantValue__6_fixp = solver.IntVar(0, 1, 'ConstantValue__6_fixp')
ConstantValue__6_float = solver.IntVar(0, 1, 'ConstantValue__6_float')
ConstantValue__6_double = solver.IntVar(0, 1, 'ConstantValue__6_double')
ConstantValue__6_enob = solver.IntVar(-10000, 10000, 'ConstantValue__6_enob')
solver.Add( + (1)*ConstantValue__6_enob + (-1)*ConstantValue__6_fixbits + (10000)*ConstantValue__6_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__6_enob + (10000)*ConstantValue__6_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__6_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_float + (1)*ConstantValue__6_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__6_fixbits + (-10000)*ConstantValue__6_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 2.000000e+00, double* @B1, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !63
ConstantValue__6_CAST_store_fixbits = solver.IntVar(0, 30, 'ConstantValue__6_CAST_store_fixbits')
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
castCostObj +=  + (6.25227)*C3_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_store_fixp + (-1)*C4_ConstantValue__6_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_fixp + (1)*ConstantValue__6_CAST_store_double + (-1)*C5_ConstantValue__6_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_store_fixp + (-1)*C6_ConstantValue__6_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_float + (1)*ConstantValue__6_CAST_store_double + (-1)*C7_ConstantValue__6_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__6_CAST_store
solver.Add( + (1)*ConstantValue__6_double + (1)*ConstantValue__6_CAST_store_float + (-1)*C8_ConstantValue__6_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__6_CAST_store
solver.Add( + (1)*B1_fixp + (-1)*ConstantValue__6_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B1_float + (-1)*ConstantValue__6_CAST_store_float==0)    #float equality
solver.Add( + (1)*B1_double + (-1)*ConstantValue__6_CAST_store_double==0)    #double equality
solver.Add( + (1)*B1_fixbits + (-1)*ConstantValue__6_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 1.000000e+00
ConstantValue__7_fixbits = solver.IntVar(0, 31, 'ConstantValue__7_fixbits')
ConstantValue__7_fixp = solver.IntVar(0, 1, 'ConstantValue__7_fixp')
ConstantValue__7_float = solver.IntVar(0, 1, 'ConstantValue__7_float')
ConstantValue__7_double = solver.IntVar(0, 1, 'ConstantValue__7_double')
ConstantValue__7_enob = solver.IntVar(-10000, 10000, 'ConstantValue__7_enob')
solver.Add( + (1)*ConstantValue__7_enob + (-1)*ConstantValue__7_fixbits + (10000)*ConstantValue__7_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__7_enob + (10000)*ConstantValue__7_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__7_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__7_fixp + (1)*ConstantValue__7_float + (1)*ConstantValue__7_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__7_fixbits + (-10000)*ConstantValue__7_fixp<=0)    #If not fix, frac part to zero



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



#Constraint for cast for   store double 1.000000e+00, double* @B2, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !66
ConstantValue__8_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__8_CAST_store_fixbits')
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
castCostObj +=  + (6.25227)*C3_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_store_fixp + (-1)*C4_ConstantValue__8_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_fixp + (1)*ConstantValue__8_CAST_store_double + (-1)*C5_ConstantValue__8_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_store_fixp + (-1)*C6_ConstantValue__8_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_float + (1)*ConstantValue__8_CAST_store_double + (-1)*C7_ConstantValue__8_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__8_CAST_store
solver.Add( + (1)*ConstantValue__8_double + (1)*ConstantValue__8_CAST_store_float + (-1)*C8_ConstantValue__8_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__8_CAST_store
solver.Add( + (1)*B2_fixp + (-1)*ConstantValue__8_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*B2_float + (-1)*ConstantValue__8_CAST_store_float==0)    #float equality
solver.Add( + (1)*B2_double + (-1)*ConstantValue__8_CAST_store_double==0)    #double equality
solver.Add( + (1)*B2_fixbits + (-1)*ConstantValue__8_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
B1_enob_memphi_main_tmp = solver.IntVar(-10000, 10000, 'B1_enob_memphi_main_tmp')
solver.Add( + (1)*B1_enob_memphi_main_tmp + (-1)*B1_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob [LOAD]
DT_enob_memphi_main_tmp1 = solver.IntVar(-10000, 10000, 'DT_enob_memphi_main_tmp1')
solver.Add( + (1)*DT_enob_memphi_main_tmp1 + (-1)*DT_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !68, !taffo.initweight !44
B1_CAST_mul_fixbits = solver.IntVar(0, 30, 'B1_CAST_mul_fixbits')
B1_CAST_mul_fixp = solver.IntVar(0, 1, 'B1_CAST_mul_fixp')
B1_CAST_mul_float = solver.IntVar(0, 1, 'B1_CAST_mul_float')
B1_CAST_mul_double = solver.IntVar(0, 1, 'B1_CAST_mul_double')
solver.Add( + (1)*B1_CAST_mul_fixp + (1)*B1_CAST_mul_float + (1)*B1_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*B1_CAST_mul_fixbits + (-10000)*B1_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_B1_CAST_mul = solver.IntVar(0, 1, 'C1_B1_CAST_mul')
C2_B1_CAST_mul = solver.IntVar(0, 1, 'C2_B1_CAST_mul')
solver.Add( + (1)*B1_fixbits + (-1)*B1_CAST_mul_fixbits + (-10000)*C1_B1_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*B1_fixbits + (1)*B1_CAST_mul_fixbits + (-10000)*C2_B1_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B1_CAST_mul
castCostObj +=  + (1)*C2_B1_CAST_mul
C3_B1_CAST_mul = solver.IntVar(0, 1, 'C3_B1_CAST_mul')
C4_B1_CAST_mul = solver.IntVar(0, 1, 'C4_B1_CAST_mul')
C5_B1_CAST_mul = solver.IntVar(0, 1, 'C5_B1_CAST_mul')
C6_B1_CAST_mul = solver.IntVar(0, 1, 'C6_B1_CAST_mul')
C7_B1_CAST_mul = solver.IntVar(0, 1, 'C7_B1_CAST_mul')
C8_B1_CAST_mul = solver.IntVar(0, 1, 'C8_B1_CAST_mul')
solver.Add( + (1)*B1_fixp + (1)*B1_CAST_mul_float + (-1)*C3_B1_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_B1_CAST_mul
solver.Add( + (1)*B1_float + (1)*B1_CAST_mul_fixp + (-1)*C4_B1_CAST_mul<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_B1_CAST_mul
solver.Add( + (1)*B1_fixp + (1)*B1_CAST_mul_double + (-1)*C5_B1_CAST_mul<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_B1_CAST_mul
solver.Add( + (1)*B1_double + (1)*B1_CAST_mul_fixp + (-1)*C6_B1_CAST_mul<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_B1_CAST_mul
solver.Add( + (1)*B1_float + (1)*B1_CAST_mul_double + (-1)*C7_B1_CAST_mul<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_B1_CAST_mul
solver.Add( + (1)*B1_double + (1)*B1_CAST_mul_float + (-1)*C8_B1_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_B1_CAST_mul



#Constraint for cast for   %mul = fmul double %tmp, %tmp1, !taffo.info !68, !taffo.initweight !44
DT_CAST_mul_fixbits = solver.IntVar(0, 31, 'DT_CAST_mul_fixbits')
DT_CAST_mul_fixp = solver.IntVar(0, 1, 'DT_CAST_mul_fixp')
DT_CAST_mul_float = solver.IntVar(0, 1, 'DT_CAST_mul_float')
DT_CAST_mul_double = solver.IntVar(0, 1, 'DT_CAST_mul_double')
solver.Add( + (1)*DT_CAST_mul_fixp + (1)*DT_CAST_mul_float + (1)*DT_CAST_mul_double==1)    #exactly 1 type
solver.Add( + (1)*DT_CAST_mul_fixbits + (-10000)*DT_CAST_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_DT_CAST_mul = solver.IntVar(0, 1, 'C1_DT_CAST_mul')
C2_DT_CAST_mul = solver.IntVar(0, 1, 'C2_DT_CAST_mul')
solver.Add( + (1)*DT_fixbits + (-1)*DT_CAST_mul_fixbits + (-10000)*C1_DT_CAST_mul<=0)    #Shift cost 1
solver.Add( + (-1)*DT_fixbits + (1)*DT_CAST_mul_fixbits + (-10000)*C2_DT_CAST_mul<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_DT_CAST_mul
castCostObj +=  + (1)*C2_DT_CAST_mul
C3_DT_CAST_mul = solver.IntVar(0, 1, 'C3_DT_CAST_mul')
C4_DT_CAST_mul = solver.IntVar(0, 1, 'C4_DT_CAST_mul')
C5_DT_CAST_mul = solver.IntVar(0, 1, 'C5_DT_CAST_mul')
C6_DT_CAST_mul = solver.IntVar(0, 1, 'C6_DT_CAST_mul')
C7_DT_CAST_mul = solver.IntVar(0, 1, 'C7_DT_CAST_mul')
C8_DT_CAST_mul = solver.IntVar(0, 1, 'C8_DT_CAST_mul')
solver.Add( + (1)*DT_fixp + (1)*DT_CAST_mul_float + (-1)*C3_DT_CAST_mul<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_DT_CAST_mul
solver.Add( + (1)*DT_float + (1)*DT_CAST_mul_fixp + (-1)*C4_DT_CAST_mul<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_DT_CAST_mul
solver.Add( + (1)*DT_fixp + (1)*DT_CAST_mul_double + (-1)*C5_DT_CAST_mul<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_DT_CAST_mul
solver.Add( + (1)*DT_double + (1)*DT_CAST_mul_fixp + (-1)*C6_DT_CAST_mul<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_DT_CAST_mul
solver.Add( + (1)*DT_float + (1)*DT_CAST_mul_double + (-1)*C7_DT_CAST_mul<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_DT_CAST_mul
solver.Add( + (1)*DT_double + (1)*DT_CAST_mul_float + (-1)*C8_DT_CAST_mul<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_DT_CAST_mul



#Stuff for   %mul = fmul double %tmp, %tmp1, !taffo.info !68, !taffo.initweight !44
main_mul_fixbits = solver.IntVar(0, 31, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_mul_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul_enob
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*B1_CAST_mul_fixp + (-1)*DT_CAST_mul_fixp==0)    #fix equality
solver.Add( + (1)*B1_CAST_mul_float + (-1)*DT_CAST_mul_float==0)    #float equality
solver.Add( + (1)*B1_CAST_mul_double + (-1)*DT_CAST_mul_double==0)    #double equality
solver.Add( + (1)*B1_CAST_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*B1_CAST_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*B1_CAST_mul_double + (-1)*main_mul_double==0)    #double equality
mathCostObj =  + (1.65217)*main_mul_fixp
mathCostObj +=  + (6)*main_mul_float
mathCostObj +=  + (12.2551)*main_mul_double
main_main_mul_enob_1 = solver.IntVar(0, 1, 'main_main_mul_enob_1')
main_main_mul_enob_2 = solver.IntVar(0, 1, 'main_main_mul_enob_2')
solver.Add( + (1)*main_main_mul_enob_1 + (1)*main_main_mul_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul_enob + (-1)*DT_enob_memphi_main_tmp1 + (-10000)*main_main_mul_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul_enob + (-1)*B1_enob_memphi_main_tmp + (-10000)*main_main_mul_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
DX_enob_memphi_main_tmp2 = solver.IntVar(-10000, 10000, 'DX_enob_memphi_main_tmp2')
solver.Add( + (1)*DX_enob_memphi_main_tmp2 + (-1)*DX_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob [LOAD]
DX_enob_memphi_main_tmp3 = solver.IntVar(-10000, 10000, 'DX_enob_memphi_main_tmp3')
solver.Add( + (1)*DX_enob_memphi_main_tmp3 + (-1)*DX_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul16 = fmul double %tmp2, %tmp3, !taffo.info !70, !taffo.initweight !44
DX_CAST_mul16_fixbits = solver.IntVar(0, 31, 'DX_CAST_mul16_fixbits')
DX_CAST_mul16_fixp = solver.IntVar(0, 1, 'DX_CAST_mul16_fixp')
DX_CAST_mul16_float = solver.IntVar(0, 1, 'DX_CAST_mul16_float')
DX_CAST_mul16_double = solver.IntVar(0, 1, 'DX_CAST_mul16_double')
solver.Add( + (1)*DX_CAST_mul16_fixp + (1)*DX_CAST_mul16_float + (1)*DX_CAST_mul16_double==1)    #exactly 1 type
solver.Add( + (1)*DX_CAST_mul16_fixbits + (-10000)*DX_CAST_mul16_fixp<=0)    #If no fix, fix frac part = 0
C1_DX_CAST_mul16 = solver.IntVar(0, 1, 'C1_DX_CAST_mul16')
C2_DX_CAST_mul16 = solver.IntVar(0, 1, 'C2_DX_CAST_mul16')
solver.Add( + (1)*DX_fixbits + (-1)*DX_CAST_mul16_fixbits + (-10000)*C1_DX_CAST_mul16<=0)    #Shift cost 1
solver.Add( + (-1)*DX_fixbits + (1)*DX_CAST_mul16_fixbits + (-10000)*C2_DX_CAST_mul16<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_DX_CAST_mul16
castCostObj +=  + (1)*C2_DX_CAST_mul16
C3_DX_CAST_mul16 = solver.IntVar(0, 1, 'C3_DX_CAST_mul16')
C4_DX_CAST_mul16 = solver.IntVar(0, 1, 'C4_DX_CAST_mul16')
C5_DX_CAST_mul16 = solver.IntVar(0, 1, 'C5_DX_CAST_mul16')
C6_DX_CAST_mul16 = solver.IntVar(0, 1, 'C6_DX_CAST_mul16')
C7_DX_CAST_mul16 = solver.IntVar(0, 1, 'C7_DX_CAST_mul16')
C8_DX_CAST_mul16 = solver.IntVar(0, 1, 'C8_DX_CAST_mul16')
solver.Add( + (1)*DX_fixp + (1)*DX_CAST_mul16_float + (-1)*C3_DX_CAST_mul16<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_DX_CAST_mul16
solver.Add( + (1)*DX_float + (1)*DX_CAST_mul16_fixp + (-1)*C4_DX_CAST_mul16<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_DX_CAST_mul16
solver.Add( + (1)*DX_fixp + (1)*DX_CAST_mul16_double + (-1)*C5_DX_CAST_mul16<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_DX_CAST_mul16
solver.Add( + (1)*DX_double + (1)*DX_CAST_mul16_fixp + (-1)*C6_DX_CAST_mul16<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_DX_CAST_mul16
solver.Add( + (1)*DX_float + (1)*DX_CAST_mul16_double + (-1)*C7_DX_CAST_mul16<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_DX_CAST_mul16
solver.Add( + (1)*DX_double + (1)*DX_CAST_mul16_float + (-1)*C8_DX_CAST_mul16<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_DX_CAST_mul16



#Constraint for cast for   %mul16 = fmul double %tmp2, %tmp3, !taffo.info !70, !taffo.initweight !44
DX_CAST_mul16_0_fixbits = solver.IntVar(0, 31, 'DX_CAST_mul16_0_fixbits')
DX_CAST_mul16_0_fixp = solver.IntVar(0, 1, 'DX_CAST_mul16_0_fixp')
DX_CAST_mul16_0_float = solver.IntVar(0, 1, 'DX_CAST_mul16_0_float')
DX_CAST_mul16_0_double = solver.IntVar(0, 1, 'DX_CAST_mul16_0_double')
solver.Add( + (1)*DX_CAST_mul16_0_fixp + (1)*DX_CAST_mul16_0_float + (1)*DX_CAST_mul16_0_double==1)    #exactly 1 type
solver.Add( + (1)*DX_CAST_mul16_0_fixbits + (-10000)*DX_CAST_mul16_0_fixp<=0)    #If no fix, fix frac part = 0
C1_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C1_DX_CAST_mul16_0')
C2_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C2_DX_CAST_mul16_0')
solver.Add( + (1)*DX_fixbits + (-1)*DX_CAST_mul16_0_fixbits + (-10000)*C1_DX_CAST_mul16_0<=0)    #Shift cost 1
solver.Add( + (-1)*DX_fixbits + (1)*DX_CAST_mul16_0_fixbits + (-10000)*C2_DX_CAST_mul16_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_DX_CAST_mul16_0
castCostObj +=  + (1)*C2_DX_CAST_mul16_0
C3_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C3_DX_CAST_mul16_0')
C4_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C4_DX_CAST_mul16_0')
C5_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C5_DX_CAST_mul16_0')
C6_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C6_DX_CAST_mul16_0')
C7_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C7_DX_CAST_mul16_0')
C8_DX_CAST_mul16_0 = solver.IntVar(0, 1, 'C8_DX_CAST_mul16_0')
solver.Add( + (1)*DX_fixp + (1)*DX_CAST_mul16_0_float + (-1)*C3_DX_CAST_mul16_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_DX_CAST_mul16_0
solver.Add( + (1)*DX_float + (1)*DX_CAST_mul16_0_fixp + (-1)*C4_DX_CAST_mul16_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_DX_CAST_mul16_0
solver.Add( + (1)*DX_fixp + (1)*DX_CAST_mul16_0_double + (-1)*C5_DX_CAST_mul16_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_DX_CAST_mul16_0
solver.Add( + (1)*DX_double + (1)*DX_CAST_mul16_0_fixp + (-1)*C6_DX_CAST_mul16_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_DX_CAST_mul16_0
solver.Add( + (1)*DX_float + (1)*DX_CAST_mul16_0_double + (-1)*C7_DX_CAST_mul16_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_DX_CAST_mul16_0
solver.Add( + (1)*DX_double + (1)*DX_CAST_mul16_0_float + (-1)*C8_DX_CAST_mul16_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_DX_CAST_mul16_0



#Stuff for   %mul16 = fmul double %tmp2, %tmp3, !taffo.info !70, !taffo.initweight !44
main_mul16_fixbits = solver.IntVar(0, 31, 'main_mul16_fixbits')
main_mul16_fixp = solver.IntVar(0, 1, 'main_mul16_fixp')
main_mul16_float = solver.IntVar(0, 1, 'main_mul16_float')
main_mul16_double = solver.IntVar(0, 1, 'main_mul16_double')
main_mul16_enob = solver.IntVar(-10000, 10000, 'main_mul16_enob')
solver.Add( + (1)*main_mul16_enob + (-1)*main_mul16_fixbits + (10000)*main_mul16_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul16_enob + (10000)*main_mul16_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul16_enob + (10000)*main_mul16_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul16_fixbits + (-10000)*main_mul16_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_mul16_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul16_enob
solver.Add( + (1)*main_mul16_fixp + (1)*main_mul16_float + (1)*main_mul16_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul16_fixbits + (-10000)*main_mul16_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*DX_CAST_mul16_fixp + (-1)*DX_CAST_mul16_0_fixp==0)    #fix equality
solver.Add( + (1)*DX_CAST_mul16_float + (-1)*DX_CAST_mul16_0_float==0)    #float equality
solver.Add( + (1)*DX_CAST_mul16_double + (-1)*DX_CAST_mul16_0_double==0)    #double equality
solver.Add( + (1)*DX_CAST_mul16_fixp + (-1)*main_mul16_fixp==0)    #fix equality
solver.Add( + (1)*DX_CAST_mul16_float + (-1)*main_mul16_float==0)    #float equality
solver.Add( + (1)*DX_CAST_mul16_double + (-1)*main_mul16_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul16_fixp
mathCostObj +=  + (6)*main_mul16_float
mathCostObj +=  + (12.2551)*main_mul16_double
main_main_mul16_enob_1 = solver.IntVar(0, 1, 'main_main_mul16_enob_1')
main_main_mul16_enob_2 = solver.IntVar(0, 1, 'main_main_mul16_enob_2')
solver.Add( + (1)*main_main_mul16_enob_1 + (1)*main_main_mul16_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul16_enob + (-1)*DX_enob_memphi_main_tmp3 + (-10000)*main_main_mul16_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul16_enob + (-1)*DX_enob_memphi_main_tmp2 + (-10000)*main_main_mul16_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %div17 = fdiv double %mul, %mul16, !taffo.info !13, !taffo.initweight !45
main_mul_CAST_div17_fixbits = solver.IntVar(0, 31, 'main_mul_CAST_div17_fixbits')
main_mul_CAST_div17_fixp = solver.IntVar(0, 1, 'main_mul_CAST_div17_fixp')
main_mul_CAST_div17_float = solver.IntVar(0, 1, 'main_mul_CAST_div17_float')
main_mul_CAST_div17_double = solver.IntVar(0, 1, 'main_mul_CAST_div17_double')
solver.Add( + (1)*main_mul_CAST_div17_fixp + (1)*main_mul_CAST_div17_float + (1)*main_mul_CAST_div17_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul_CAST_div17_fixbits + (-10000)*main_mul_CAST_div17_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C1_main_mul_CAST_div17')
C2_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C2_main_mul_CAST_div17')
solver.Add( + (1)*main_mul_fixbits + (-1)*main_mul_CAST_div17_fixbits + (-10000)*C1_main_mul_CAST_div17<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul_fixbits + (1)*main_mul_CAST_div17_fixbits + (-10000)*C2_main_mul_CAST_div17<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul_CAST_div17
castCostObj +=  + (1)*C2_main_mul_CAST_div17
C3_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C3_main_mul_CAST_div17')
C4_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C4_main_mul_CAST_div17')
C5_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C5_main_mul_CAST_div17')
C6_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C6_main_mul_CAST_div17')
C7_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C7_main_mul_CAST_div17')
C8_main_mul_CAST_div17 = solver.IntVar(0, 1, 'C8_main_mul_CAST_div17')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_div17_float + (-1)*C3_main_mul_CAST_div17<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul_CAST_div17
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_div17_fixp + (-1)*C4_main_mul_CAST_div17<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul_CAST_div17
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_CAST_div17_double + (-1)*C5_main_mul_CAST_div17<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul_CAST_div17
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_div17_fixp + (-1)*C6_main_mul_CAST_div17<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul_CAST_div17
solver.Add( + (1)*main_mul_float + (1)*main_mul_CAST_div17_double + (-1)*C7_main_mul_CAST_div17<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul_CAST_div17
solver.Add( + (1)*main_mul_double + (1)*main_mul_CAST_div17_float + (-1)*C8_main_mul_CAST_div17<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul_CAST_div17



#Constraint for cast for   %div17 = fdiv double %mul, %mul16, !taffo.info !13, !taffo.initweight !45
main_mul16_CAST_div17_fixbits = solver.IntVar(0, 31, 'main_mul16_CAST_div17_fixbits')
main_mul16_CAST_div17_fixp = solver.IntVar(0, 1, 'main_mul16_CAST_div17_fixp')
main_mul16_CAST_div17_float = solver.IntVar(0, 1, 'main_mul16_CAST_div17_float')
main_mul16_CAST_div17_double = solver.IntVar(0, 1, 'main_mul16_CAST_div17_double')
solver.Add( + (1)*main_mul16_CAST_div17_fixp + (1)*main_mul16_CAST_div17_float + (1)*main_mul16_CAST_div17_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul16_CAST_div17_fixbits + (-10000)*main_mul16_CAST_div17_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C1_main_mul16_CAST_div17')
C2_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C2_main_mul16_CAST_div17')
solver.Add( + (1)*main_mul16_fixbits + (-1)*main_mul16_CAST_div17_fixbits + (-10000)*C1_main_mul16_CAST_div17<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul16_fixbits + (1)*main_mul16_CAST_div17_fixbits + (-10000)*C2_main_mul16_CAST_div17<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul16_CAST_div17
castCostObj +=  + (1)*C2_main_mul16_CAST_div17
C3_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C3_main_mul16_CAST_div17')
C4_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C4_main_mul16_CAST_div17')
C5_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C5_main_mul16_CAST_div17')
C6_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C6_main_mul16_CAST_div17')
C7_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C7_main_mul16_CAST_div17')
C8_main_mul16_CAST_div17 = solver.IntVar(0, 1, 'C8_main_mul16_CAST_div17')
solver.Add( + (1)*main_mul16_fixp + (1)*main_mul16_CAST_div17_float + (-1)*C3_main_mul16_CAST_div17<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul16_CAST_div17
solver.Add( + (1)*main_mul16_float + (1)*main_mul16_CAST_div17_fixp + (-1)*C4_main_mul16_CAST_div17<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul16_CAST_div17
solver.Add( + (1)*main_mul16_fixp + (1)*main_mul16_CAST_div17_double + (-1)*C5_main_mul16_CAST_div17<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul16_CAST_div17
solver.Add( + (1)*main_mul16_double + (1)*main_mul16_CAST_div17_fixp + (-1)*C6_main_mul16_CAST_div17<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul16_CAST_div17
solver.Add( + (1)*main_mul16_float + (1)*main_mul16_CAST_div17_double + (-1)*C7_main_mul16_CAST_div17<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul16_CAST_div17
solver.Add( + (1)*main_mul16_double + (1)*main_mul16_CAST_div17_float + (-1)*C8_main_mul16_CAST_div17<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul16_CAST_div17



#Stuff for   %div17 = fdiv double %mul, %mul16, !taffo.info !13, !taffo.initweight !45
main_div17_fixbits = solver.IntVar(0, 22, 'main_div17_fixbits')
main_div17_fixp = solver.IntVar(0, 1, 'main_div17_fixp')
main_div17_float = solver.IntVar(0, 1, 'main_div17_float')
main_div17_double = solver.IntVar(0, 1, 'main_div17_double')
main_div17_enob = solver.IntVar(-10000, 10000, 'main_div17_enob')
solver.Add( + (1)*main_div17_enob + (-1)*main_div17_fixbits + (10000)*main_div17_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div17_enob + (10000)*main_div17_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div17_enob + (10000)*main_div17_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div17_fixbits + (-10000)*main_div17_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_div17_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div17_enob
solver.Add( + (1)*main_div17_fixp + (1)*main_div17_float + (1)*main_div17_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div17_fixbits + (-10000)*main_div17_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul_CAST_div17_fixp + (-1)*main_mul16_CAST_div17_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div17_float + (-1)*main_mul16_CAST_div17_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div17_double + (-1)*main_mul16_CAST_div17_double==0)    #double equality
solver.Add( + (1)*main_mul_CAST_div17_fixp + (-1)*main_div17_fixp==0)    #fix equality
solver.Add( + (1)*main_mul_CAST_div17_float + (-1)*main_div17_float==0)    #float equality
solver.Add( + (1)*main_mul_CAST_div17_double + (-1)*main_div17_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div17_fixp
mathCostObj +=  + (6)*main_div17_float
mathCostObj +=  + (12)*main_div17_double
main_main_div17_enob_1 = solver.IntVar(0, 1, 'main_main_div17_enob_1')
main_main_div17_enob_2 = solver.IntVar(0, 1, 'main_main_div17_enob_2')
solver.Add( + (1)*main_main_div17_enob_1 + (1)*main_main_div17_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div17_enob + (-1)*main_mul16_enob + (-10000)*main_main_div17_enob_1<=994)    #Enob: propagation in division 1
solver.Add( + (1)*main_div17_enob + (-1)*main_mul_enob + (-10000)*main_main_div17_enob_2<=994)    #Enob: propagation in division 2



#Constraint for cast for   store double %div17, double* @mul1, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
main_div17_CAST_store_fixbits = solver.IntVar(0, 22, 'main_div17_CAST_store_fixbits')
main_div17_CAST_store_fixp = solver.IntVar(0, 1, 'main_div17_CAST_store_fixp')
main_div17_CAST_store_float = solver.IntVar(0, 1, 'main_div17_CAST_store_float')
main_div17_CAST_store_double = solver.IntVar(0, 1, 'main_div17_CAST_store_double')
solver.Add( + (1)*main_div17_CAST_store_fixp + (1)*main_div17_CAST_store_float + (1)*main_div17_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div17_CAST_store_fixbits + (-10000)*main_div17_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div17_CAST_store = solver.IntVar(0, 1, 'C1_main_div17_CAST_store')
C2_main_div17_CAST_store = solver.IntVar(0, 1, 'C2_main_div17_CAST_store')
solver.Add( + (1)*main_div17_fixbits + (-1)*main_div17_CAST_store_fixbits + (-10000)*C1_main_div17_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div17_fixbits + (1)*main_div17_CAST_store_fixbits + (-10000)*C2_main_div17_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div17_CAST_store
castCostObj +=  + (1)*C2_main_div17_CAST_store
C3_main_div17_CAST_store = solver.IntVar(0, 1, 'C3_main_div17_CAST_store')
C4_main_div17_CAST_store = solver.IntVar(0, 1, 'C4_main_div17_CAST_store')
C5_main_div17_CAST_store = solver.IntVar(0, 1, 'C5_main_div17_CAST_store')
C6_main_div17_CAST_store = solver.IntVar(0, 1, 'C6_main_div17_CAST_store')
C7_main_div17_CAST_store = solver.IntVar(0, 1, 'C7_main_div17_CAST_store')
C8_main_div17_CAST_store = solver.IntVar(0, 1, 'C8_main_div17_CAST_store')
solver.Add( + (1)*main_div17_fixp + (1)*main_div17_CAST_store_float + (-1)*C3_main_div17_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div17_CAST_store
solver.Add( + (1)*main_div17_float + (1)*main_div17_CAST_store_fixp + (-1)*C4_main_div17_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div17_CAST_store
solver.Add( + (1)*main_div17_fixp + (1)*main_div17_CAST_store_double + (-1)*C5_main_div17_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div17_CAST_store
solver.Add( + (1)*main_div17_double + (1)*main_div17_CAST_store_fixp + (-1)*C6_main_div17_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div17_CAST_store
solver.Add( + (1)*main_div17_float + (1)*main_div17_CAST_store_double + (-1)*C7_main_div17_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div17_CAST_store
solver.Add( + (1)*main_div17_double + (1)*main_div17_CAST_store_float + (-1)*C8_main_div17_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div17_CAST_store
solver.Add( + (1)*mul1_fixp + (-1)*main_div17_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mul1_float + (-1)*main_div17_CAST_store_float==0)    #float equality
solver.Add( + (1)*mul1_double + (-1)*main_div17_CAST_store_double==0)    #double equality
solver.Add( + (1)*mul1_fixbits + (-1)*main_div17_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
mul1_enob_storeENOB = solver.IntVar(-10000, 10000, 'mul1_enob_storeENOB')
solver.Add( + (1)*mul1_enob_storeENOB + (-1)*mul1_fixbits + (10000)*mul1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mul1_enob_storeENOB + (10000)*mul1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mul1_enob_storeENOB + (10000)*mul1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mul1_enob_storeENOB + (-1)*main_div17_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
B2_enob_memphi_main_tmp4 = solver.IntVar(-10000, 10000, 'B2_enob_memphi_main_tmp4')
solver.Add( + (1)*B2_enob_memphi_main_tmp4 + (-1)*B2_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob [LOAD]
DT_enob_memphi_main_tmp5 = solver.IntVar(-10000, 10000, 'DT_enob_memphi_main_tmp5')
solver.Add( + (1)*DT_enob_memphi_main_tmp5 + (-1)*DT_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul18 = fmul double %tmp4, %tmp5, !taffo.info !7, !taffo.initweight !44
B2_CAST_mul18_fixbits = solver.IntVar(0, 31, 'B2_CAST_mul18_fixbits')
B2_CAST_mul18_fixp = solver.IntVar(0, 1, 'B2_CAST_mul18_fixp')
B2_CAST_mul18_float = solver.IntVar(0, 1, 'B2_CAST_mul18_float')
B2_CAST_mul18_double = solver.IntVar(0, 1, 'B2_CAST_mul18_double')
solver.Add( + (1)*B2_CAST_mul18_fixp + (1)*B2_CAST_mul18_float + (1)*B2_CAST_mul18_double==1)    #exactly 1 type
solver.Add( + (1)*B2_CAST_mul18_fixbits + (-10000)*B2_CAST_mul18_fixp<=0)    #If no fix, fix frac part = 0
C1_B2_CAST_mul18 = solver.IntVar(0, 1, 'C1_B2_CAST_mul18')
C2_B2_CAST_mul18 = solver.IntVar(0, 1, 'C2_B2_CAST_mul18')
solver.Add( + (1)*B2_fixbits + (-1)*B2_CAST_mul18_fixbits + (-10000)*C1_B2_CAST_mul18<=0)    #Shift cost 1
solver.Add( + (-1)*B2_fixbits + (1)*B2_CAST_mul18_fixbits + (-10000)*C2_B2_CAST_mul18<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_B2_CAST_mul18
castCostObj +=  + (1)*C2_B2_CAST_mul18
C3_B2_CAST_mul18 = solver.IntVar(0, 1, 'C3_B2_CAST_mul18')
C4_B2_CAST_mul18 = solver.IntVar(0, 1, 'C4_B2_CAST_mul18')
C5_B2_CAST_mul18 = solver.IntVar(0, 1, 'C5_B2_CAST_mul18')
C6_B2_CAST_mul18 = solver.IntVar(0, 1, 'C6_B2_CAST_mul18')
C7_B2_CAST_mul18 = solver.IntVar(0, 1, 'C7_B2_CAST_mul18')
C8_B2_CAST_mul18 = solver.IntVar(0, 1, 'C8_B2_CAST_mul18')
solver.Add( + (1)*B2_fixp + (1)*B2_CAST_mul18_float + (-1)*C3_B2_CAST_mul18<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_B2_CAST_mul18
solver.Add( + (1)*B2_float + (1)*B2_CAST_mul18_fixp + (-1)*C4_B2_CAST_mul18<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_B2_CAST_mul18
solver.Add( + (1)*B2_fixp + (1)*B2_CAST_mul18_double + (-1)*C5_B2_CAST_mul18<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_B2_CAST_mul18
solver.Add( + (1)*B2_double + (1)*B2_CAST_mul18_fixp + (-1)*C6_B2_CAST_mul18<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_B2_CAST_mul18
solver.Add( + (1)*B2_float + (1)*B2_CAST_mul18_double + (-1)*C7_B2_CAST_mul18<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_B2_CAST_mul18
solver.Add( + (1)*B2_double + (1)*B2_CAST_mul18_float + (-1)*C8_B2_CAST_mul18<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_B2_CAST_mul18



#Constraint for cast for   %mul18 = fmul double %tmp4, %tmp5, !taffo.info !7, !taffo.initweight !44
DT_CAST_mul18_fixbits = solver.IntVar(0, 31, 'DT_CAST_mul18_fixbits')
DT_CAST_mul18_fixp = solver.IntVar(0, 1, 'DT_CAST_mul18_fixp')
DT_CAST_mul18_float = solver.IntVar(0, 1, 'DT_CAST_mul18_float')
DT_CAST_mul18_double = solver.IntVar(0, 1, 'DT_CAST_mul18_double')
solver.Add( + (1)*DT_CAST_mul18_fixp + (1)*DT_CAST_mul18_float + (1)*DT_CAST_mul18_double==1)    #exactly 1 type
solver.Add( + (1)*DT_CAST_mul18_fixbits + (-10000)*DT_CAST_mul18_fixp<=0)    #If no fix, fix frac part = 0
C1_DT_CAST_mul18 = solver.IntVar(0, 1, 'C1_DT_CAST_mul18')
C2_DT_CAST_mul18 = solver.IntVar(0, 1, 'C2_DT_CAST_mul18')
solver.Add( + (1)*DT_fixbits + (-1)*DT_CAST_mul18_fixbits + (-10000)*C1_DT_CAST_mul18<=0)    #Shift cost 1
solver.Add( + (-1)*DT_fixbits + (1)*DT_CAST_mul18_fixbits + (-10000)*C2_DT_CAST_mul18<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_DT_CAST_mul18
castCostObj +=  + (1)*C2_DT_CAST_mul18
C3_DT_CAST_mul18 = solver.IntVar(0, 1, 'C3_DT_CAST_mul18')
C4_DT_CAST_mul18 = solver.IntVar(0, 1, 'C4_DT_CAST_mul18')
C5_DT_CAST_mul18 = solver.IntVar(0, 1, 'C5_DT_CAST_mul18')
C6_DT_CAST_mul18 = solver.IntVar(0, 1, 'C6_DT_CAST_mul18')
C7_DT_CAST_mul18 = solver.IntVar(0, 1, 'C7_DT_CAST_mul18')
C8_DT_CAST_mul18 = solver.IntVar(0, 1, 'C8_DT_CAST_mul18')
solver.Add( + (1)*DT_fixp + (1)*DT_CAST_mul18_float + (-1)*C3_DT_CAST_mul18<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_DT_CAST_mul18
solver.Add( + (1)*DT_float + (1)*DT_CAST_mul18_fixp + (-1)*C4_DT_CAST_mul18<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_DT_CAST_mul18
solver.Add( + (1)*DT_fixp + (1)*DT_CAST_mul18_double + (-1)*C5_DT_CAST_mul18<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_DT_CAST_mul18
solver.Add( + (1)*DT_double + (1)*DT_CAST_mul18_fixp + (-1)*C6_DT_CAST_mul18<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_DT_CAST_mul18
solver.Add( + (1)*DT_float + (1)*DT_CAST_mul18_double + (-1)*C7_DT_CAST_mul18<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_DT_CAST_mul18
solver.Add( + (1)*DT_double + (1)*DT_CAST_mul18_float + (-1)*C8_DT_CAST_mul18<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_DT_CAST_mul18



#Stuff for   %mul18 = fmul double %tmp4, %tmp5, !taffo.info !7, !taffo.initweight !44
main_mul18_fixbits = solver.IntVar(0, 31, 'main_mul18_fixbits')
main_mul18_fixp = solver.IntVar(0, 1, 'main_mul18_fixp')
main_mul18_float = solver.IntVar(0, 1, 'main_mul18_float')
main_mul18_double = solver.IntVar(0, 1, 'main_mul18_double')
main_mul18_enob = solver.IntVar(-10000, 10000, 'main_mul18_enob')
solver.Add( + (1)*main_mul18_enob + (-1)*main_mul18_fixbits + (10000)*main_mul18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul18_enob + (10000)*main_mul18_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul18_enob + (10000)*main_mul18_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul18_fixbits + (-10000)*main_mul18_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_mul18_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul18_enob
solver.Add( + (1)*main_mul18_fixp + (1)*main_mul18_float + (1)*main_mul18_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul18_fixbits + (-10000)*main_mul18_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*B2_CAST_mul18_fixp + (-1)*DT_CAST_mul18_fixp==0)    #fix equality
solver.Add( + (1)*B2_CAST_mul18_float + (-1)*DT_CAST_mul18_float==0)    #float equality
solver.Add( + (1)*B2_CAST_mul18_double + (-1)*DT_CAST_mul18_double==0)    #double equality
solver.Add( + (1)*B2_CAST_mul18_fixp + (-1)*main_mul18_fixp==0)    #fix equality
solver.Add( + (1)*B2_CAST_mul18_float + (-1)*main_mul18_float==0)    #float equality
solver.Add( + (1)*B2_CAST_mul18_double + (-1)*main_mul18_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul18_fixp
mathCostObj +=  + (6)*main_mul18_float
mathCostObj +=  + (12.2551)*main_mul18_double
main_main_mul18_enob_1 = solver.IntVar(0, 1, 'main_main_mul18_enob_1')
main_main_mul18_enob_2 = solver.IntVar(0, 1, 'main_main_mul18_enob_2')
solver.Add( + (1)*main_main_mul18_enob_1 + (1)*main_main_mul18_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul18_enob + (-1)*DT_enob_memphi_main_tmp5 + (-10000)*main_main_mul18_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul18_enob + (-1)*B2_enob_memphi_main_tmp4 + (-10000)*main_main_mul18_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
DY_enob_memphi_main_tmp6 = solver.IntVar(-10000, 10000, 'DY_enob_memphi_main_tmp6')
solver.Add( + (1)*DY_enob_memphi_main_tmp6 + (-1)*DY_enob<=0)    #Enob constraint, new enob at most original variable enob

#Restriction for new enob [LOAD]
DY_enob_memphi_main_tmp7 = solver.IntVar(-10000, 10000, 'DY_enob_memphi_main_tmp7')
solver.Add( + (1)*DY_enob_memphi_main_tmp7 + (-1)*DY_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul19 = fmul double %tmp6, %tmp7, !taffo.info !70, !taffo.initweight !44
DY_CAST_mul19_fixbits = solver.IntVar(0, 31, 'DY_CAST_mul19_fixbits')
DY_CAST_mul19_fixp = solver.IntVar(0, 1, 'DY_CAST_mul19_fixp')
DY_CAST_mul19_float = solver.IntVar(0, 1, 'DY_CAST_mul19_float')
DY_CAST_mul19_double = solver.IntVar(0, 1, 'DY_CAST_mul19_double')
solver.Add( + (1)*DY_CAST_mul19_fixp + (1)*DY_CAST_mul19_float + (1)*DY_CAST_mul19_double==1)    #exactly 1 type
solver.Add( + (1)*DY_CAST_mul19_fixbits + (-10000)*DY_CAST_mul19_fixp<=0)    #If no fix, fix frac part = 0
C1_DY_CAST_mul19 = solver.IntVar(0, 1, 'C1_DY_CAST_mul19')
C2_DY_CAST_mul19 = solver.IntVar(0, 1, 'C2_DY_CAST_mul19')
solver.Add( + (1)*DY_fixbits + (-1)*DY_CAST_mul19_fixbits + (-10000)*C1_DY_CAST_mul19<=0)    #Shift cost 1
solver.Add( + (-1)*DY_fixbits + (1)*DY_CAST_mul19_fixbits + (-10000)*C2_DY_CAST_mul19<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_DY_CAST_mul19
castCostObj +=  + (1)*C2_DY_CAST_mul19
C3_DY_CAST_mul19 = solver.IntVar(0, 1, 'C3_DY_CAST_mul19')
C4_DY_CAST_mul19 = solver.IntVar(0, 1, 'C4_DY_CAST_mul19')
C5_DY_CAST_mul19 = solver.IntVar(0, 1, 'C5_DY_CAST_mul19')
C6_DY_CAST_mul19 = solver.IntVar(0, 1, 'C6_DY_CAST_mul19')
C7_DY_CAST_mul19 = solver.IntVar(0, 1, 'C7_DY_CAST_mul19')
C8_DY_CAST_mul19 = solver.IntVar(0, 1, 'C8_DY_CAST_mul19')
solver.Add( + (1)*DY_fixp + (1)*DY_CAST_mul19_float + (-1)*C3_DY_CAST_mul19<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_DY_CAST_mul19
solver.Add( + (1)*DY_float + (1)*DY_CAST_mul19_fixp + (-1)*C4_DY_CAST_mul19<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_DY_CAST_mul19
solver.Add( + (1)*DY_fixp + (1)*DY_CAST_mul19_double + (-1)*C5_DY_CAST_mul19<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_DY_CAST_mul19
solver.Add( + (1)*DY_double + (1)*DY_CAST_mul19_fixp + (-1)*C6_DY_CAST_mul19<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_DY_CAST_mul19
solver.Add( + (1)*DY_float + (1)*DY_CAST_mul19_double + (-1)*C7_DY_CAST_mul19<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_DY_CAST_mul19
solver.Add( + (1)*DY_double + (1)*DY_CAST_mul19_float + (-1)*C8_DY_CAST_mul19<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_DY_CAST_mul19



#Constraint for cast for   %mul19 = fmul double %tmp6, %tmp7, !taffo.info !70, !taffo.initweight !44
DY_CAST_mul19_0_fixbits = solver.IntVar(0, 31, 'DY_CAST_mul19_0_fixbits')
DY_CAST_mul19_0_fixp = solver.IntVar(0, 1, 'DY_CAST_mul19_0_fixp')
DY_CAST_mul19_0_float = solver.IntVar(0, 1, 'DY_CAST_mul19_0_float')
DY_CAST_mul19_0_double = solver.IntVar(0, 1, 'DY_CAST_mul19_0_double')
solver.Add( + (1)*DY_CAST_mul19_0_fixp + (1)*DY_CAST_mul19_0_float + (1)*DY_CAST_mul19_0_double==1)    #exactly 1 type
solver.Add( + (1)*DY_CAST_mul19_0_fixbits + (-10000)*DY_CAST_mul19_0_fixp<=0)    #If no fix, fix frac part = 0
C1_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C1_DY_CAST_mul19_0')
C2_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C2_DY_CAST_mul19_0')
solver.Add( + (1)*DY_fixbits + (-1)*DY_CAST_mul19_0_fixbits + (-10000)*C1_DY_CAST_mul19_0<=0)    #Shift cost 1
solver.Add( + (-1)*DY_fixbits + (1)*DY_CAST_mul19_0_fixbits + (-10000)*C2_DY_CAST_mul19_0<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_DY_CAST_mul19_0
castCostObj +=  + (1)*C2_DY_CAST_mul19_0
C3_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C3_DY_CAST_mul19_0')
C4_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C4_DY_CAST_mul19_0')
C5_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C5_DY_CAST_mul19_0')
C6_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C6_DY_CAST_mul19_0')
C7_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C7_DY_CAST_mul19_0')
C8_DY_CAST_mul19_0 = solver.IntVar(0, 1, 'C8_DY_CAST_mul19_0')
solver.Add( + (1)*DY_fixp + (1)*DY_CAST_mul19_0_float + (-1)*C3_DY_CAST_mul19_0<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_DY_CAST_mul19_0
solver.Add( + (1)*DY_float + (1)*DY_CAST_mul19_0_fixp + (-1)*C4_DY_CAST_mul19_0<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_DY_CAST_mul19_0
solver.Add( + (1)*DY_fixp + (1)*DY_CAST_mul19_0_double + (-1)*C5_DY_CAST_mul19_0<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_DY_CAST_mul19_0
solver.Add( + (1)*DY_double + (1)*DY_CAST_mul19_0_fixp + (-1)*C6_DY_CAST_mul19_0<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_DY_CAST_mul19_0
solver.Add( + (1)*DY_float + (1)*DY_CAST_mul19_0_double + (-1)*C7_DY_CAST_mul19_0<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_DY_CAST_mul19_0
solver.Add( + (1)*DY_double + (1)*DY_CAST_mul19_0_float + (-1)*C8_DY_CAST_mul19_0<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_DY_CAST_mul19_0



#Stuff for   %mul19 = fmul double %tmp6, %tmp7, !taffo.info !70, !taffo.initweight !44
main_mul19_fixbits = solver.IntVar(0, 31, 'main_mul19_fixbits')
main_mul19_fixp = solver.IntVar(0, 1, 'main_mul19_fixp')
main_mul19_float = solver.IntVar(0, 1, 'main_mul19_float')
main_mul19_double = solver.IntVar(0, 1, 'main_mul19_double')
main_mul19_enob = solver.IntVar(-10000, 10000, 'main_mul19_enob')
solver.Add( + (1)*main_mul19_enob + (-1)*main_mul19_fixbits + (10000)*main_mul19_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul19_enob + (10000)*main_mul19_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul19_enob + (10000)*main_mul19_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul19_fixbits + (-10000)*main_mul19_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*main_mul19_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul19_enob
solver.Add( + (1)*main_mul19_fixp + (1)*main_mul19_float + (1)*main_mul19_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul19_fixbits + (-10000)*main_mul19_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*DY_CAST_mul19_fixp + (-1)*DY_CAST_mul19_0_fixp==0)    #fix equality
solver.Add( + (1)*DY_CAST_mul19_float + (-1)*DY_CAST_mul19_0_float==0)    #float equality
solver.Add( + (1)*DY_CAST_mul19_double + (-1)*DY_CAST_mul19_0_double==0)    #double equality
solver.Add( + (1)*DY_CAST_mul19_fixp + (-1)*main_mul19_fixp==0)    #fix equality
solver.Add( + (1)*DY_CAST_mul19_float + (-1)*main_mul19_float==0)    #float equality
solver.Add( + (1)*DY_CAST_mul19_double + (-1)*main_mul19_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul19_fixp
mathCostObj +=  + (6)*main_mul19_float
mathCostObj +=  + (12.2551)*main_mul19_double
main_main_mul19_enob_1 = solver.IntVar(0, 1, 'main_main_mul19_enob_1')
main_main_mul19_enob_2 = solver.IntVar(0, 1, 'main_main_mul19_enob_2')
solver.Add( + (1)*main_main_mul19_enob_1 + (1)*main_main_mul19_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul19_enob + (-1)*DY_enob_memphi_main_tmp7 + (-10000)*main_main_mul19_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul19_enob + (-1)*DY_enob_memphi_main_tmp6 + (-10000)*main_main_mul19_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %div20 = fdiv double %mul18, %mul19, !taffo.info !15, !taffo.initweight !45
main_mul18_CAST_div20_fixbits = solver.IntVar(0, 31, 'main_mul18_CAST_div20_fixbits')
main_mul18_CAST_div20_fixp = solver.IntVar(0, 1, 'main_mul18_CAST_div20_fixp')
main_mul18_CAST_div20_float = solver.IntVar(0, 1, 'main_mul18_CAST_div20_float')
main_mul18_CAST_div20_double = solver.IntVar(0, 1, 'main_mul18_CAST_div20_double')
solver.Add( + (1)*main_mul18_CAST_div20_fixp + (1)*main_mul18_CAST_div20_float + (1)*main_mul18_CAST_div20_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul18_CAST_div20_fixbits + (-10000)*main_mul18_CAST_div20_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C1_main_mul18_CAST_div20')
C2_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C2_main_mul18_CAST_div20')
solver.Add( + (1)*main_mul18_fixbits + (-1)*main_mul18_CAST_div20_fixbits + (-10000)*C1_main_mul18_CAST_div20<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul18_fixbits + (1)*main_mul18_CAST_div20_fixbits + (-10000)*C2_main_mul18_CAST_div20<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul18_CAST_div20
castCostObj +=  + (1)*C2_main_mul18_CAST_div20
C3_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C3_main_mul18_CAST_div20')
C4_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C4_main_mul18_CAST_div20')
C5_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C5_main_mul18_CAST_div20')
C6_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C6_main_mul18_CAST_div20')
C7_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C7_main_mul18_CAST_div20')
C8_main_mul18_CAST_div20 = solver.IntVar(0, 1, 'C8_main_mul18_CAST_div20')
solver.Add( + (1)*main_mul18_fixp + (1)*main_mul18_CAST_div20_float + (-1)*C3_main_mul18_CAST_div20<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul18_CAST_div20
solver.Add( + (1)*main_mul18_float + (1)*main_mul18_CAST_div20_fixp + (-1)*C4_main_mul18_CAST_div20<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul18_CAST_div20
solver.Add( + (1)*main_mul18_fixp + (1)*main_mul18_CAST_div20_double + (-1)*C5_main_mul18_CAST_div20<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul18_CAST_div20
solver.Add( + (1)*main_mul18_double + (1)*main_mul18_CAST_div20_fixp + (-1)*C6_main_mul18_CAST_div20<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul18_CAST_div20
solver.Add( + (1)*main_mul18_float + (1)*main_mul18_CAST_div20_double + (-1)*C7_main_mul18_CAST_div20<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul18_CAST_div20
solver.Add( + (1)*main_mul18_double + (1)*main_mul18_CAST_div20_float + (-1)*C8_main_mul18_CAST_div20<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul18_CAST_div20



#Constraint for cast for   %div20 = fdiv double %mul18, %mul19, !taffo.info !15, !taffo.initweight !45
main_mul19_CAST_div20_fixbits = solver.IntVar(0, 31, 'main_mul19_CAST_div20_fixbits')
main_mul19_CAST_div20_fixp = solver.IntVar(0, 1, 'main_mul19_CAST_div20_fixp')
main_mul19_CAST_div20_float = solver.IntVar(0, 1, 'main_mul19_CAST_div20_float')
main_mul19_CAST_div20_double = solver.IntVar(0, 1, 'main_mul19_CAST_div20_double')
solver.Add( + (1)*main_mul19_CAST_div20_fixp + (1)*main_mul19_CAST_div20_float + (1)*main_mul19_CAST_div20_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul19_CAST_div20_fixbits + (-10000)*main_mul19_CAST_div20_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C1_main_mul19_CAST_div20')
C2_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C2_main_mul19_CAST_div20')
solver.Add( + (1)*main_mul19_fixbits + (-1)*main_mul19_CAST_div20_fixbits + (-10000)*C1_main_mul19_CAST_div20<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul19_fixbits + (1)*main_mul19_CAST_div20_fixbits + (-10000)*C2_main_mul19_CAST_div20<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul19_CAST_div20
castCostObj +=  + (1)*C2_main_mul19_CAST_div20
C3_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C3_main_mul19_CAST_div20')
C4_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C4_main_mul19_CAST_div20')
C5_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C5_main_mul19_CAST_div20')
C6_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C6_main_mul19_CAST_div20')
C7_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C7_main_mul19_CAST_div20')
C8_main_mul19_CAST_div20 = solver.IntVar(0, 1, 'C8_main_mul19_CAST_div20')
solver.Add( + (1)*main_mul19_fixp + (1)*main_mul19_CAST_div20_float + (-1)*C3_main_mul19_CAST_div20<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul19_CAST_div20
solver.Add( + (1)*main_mul19_float + (1)*main_mul19_CAST_div20_fixp + (-1)*C4_main_mul19_CAST_div20<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul19_CAST_div20
solver.Add( + (1)*main_mul19_fixp + (1)*main_mul19_CAST_div20_double + (-1)*C5_main_mul19_CAST_div20<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul19_CAST_div20
solver.Add( + (1)*main_mul19_double + (1)*main_mul19_CAST_div20_fixp + (-1)*C6_main_mul19_CAST_div20<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul19_CAST_div20
solver.Add( + (1)*main_mul19_float + (1)*main_mul19_CAST_div20_double + (-1)*C7_main_mul19_CAST_div20<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul19_CAST_div20
solver.Add( + (1)*main_mul19_double + (1)*main_mul19_CAST_div20_float + (-1)*C8_main_mul19_CAST_div20<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul19_CAST_div20



#Stuff for   %div20 = fdiv double %mul18, %mul19, !taffo.info !15, !taffo.initweight !45
main_div20_fixbits = solver.IntVar(0, 23, 'main_div20_fixbits')
main_div20_fixp = solver.IntVar(0, 1, 'main_div20_fixp')
main_div20_float = solver.IntVar(0, 1, 'main_div20_float')
main_div20_double = solver.IntVar(0, 1, 'main_div20_double')
main_div20_enob = solver.IntVar(-10000, 10000, 'main_div20_enob')
solver.Add( + (1)*main_div20_enob + (-1)*main_div20_fixbits + (10000)*main_div20_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div20_enob + (10000)*main_div20_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div20_enob + (10000)*main_div20_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div20_fixbits + (-10000)*main_div20_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_div20_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div20_enob
solver.Add( + (1)*main_div20_fixp + (1)*main_div20_float + (1)*main_div20_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div20_fixbits + (-10000)*main_div20_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul18_CAST_div20_fixp + (-1)*main_mul19_CAST_div20_fixp==0)    #fix equality
solver.Add( + (1)*main_mul18_CAST_div20_float + (-1)*main_mul19_CAST_div20_float==0)    #float equality
solver.Add( + (1)*main_mul18_CAST_div20_double + (-1)*main_mul19_CAST_div20_double==0)    #double equality
solver.Add( + (1)*main_mul18_CAST_div20_fixp + (-1)*main_div20_fixp==0)    #fix equality
solver.Add( + (1)*main_mul18_CAST_div20_float + (-1)*main_div20_float==0)    #float equality
solver.Add( + (1)*main_mul18_CAST_div20_double + (-1)*main_div20_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div20_fixp
mathCostObj +=  + (6)*main_div20_float
mathCostObj +=  + (12)*main_div20_double
main_main_div20_enob_1 = solver.IntVar(0, 1, 'main_main_div20_enob_1')
main_main_div20_enob_2 = solver.IntVar(0, 1, 'main_main_div20_enob_2')
solver.Add( + (1)*main_main_div20_enob_1 + (1)*main_main_div20_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div20_enob + (-1)*main_mul19_enob + (-10000)*main_main_div20_enob_1<=994)    #Enob: propagation in division 1
solver.Add( + (1)*main_div20_enob + (-1)*main_mul18_enob + (-10000)*main_main_div20_enob_2<=994)    #Enob: propagation in division 2



#Constraint for cast for   store double %div20, double* @mul2, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
main_div20_CAST_store_fixbits = solver.IntVar(0, 23, 'main_div20_CAST_store_fixbits')
main_div20_CAST_store_fixp = solver.IntVar(0, 1, 'main_div20_CAST_store_fixp')
main_div20_CAST_store_float = solver.IntVar(0, 1, 'main_div20_CAST_store_float')
main_div20_CAST_store_double = solver.IntVar(0, 1, 'main_div20_CAST_store_double')
solver.Add( + (1)*main_div20_CAST_store_fixp + (1)*main_div20_CAST_store_float + (1)*main_div20_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div20_CAST_store_fixbits + (-10000)*main_div20_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div20_CAST_store = solver.IntVar(0, 1, 'C1_main_div20_CAST_store')
C2_main_div20_CAST_store = solver.IntVar(0, 1, 'C2_main_div20_CAST_store')
solver.Add( + (1)*main_div20_fixbits + (-1)*main_div20_CAST_store_fixbits + (-10000)*C1_main_div20_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div20_fixbits + (1)*main_div20_CAST_store_fixbits + (-10000)*C2_main_div20_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div20_CAST_store
castCostObj +=  + (1)*C2_main_div20_CAST_store
C3_main_div20_CAST_store = solver.IntVar(0, 1, 'C3_main_div20_CAST_store')
C4_main_div20_CAST_store = solver.IntVar(0, 1, 'C4_main_div20_CAST_store')
C5_main_div20_CAST_store = solver.IntVar(0, 1, 'C5_main_div20_CAST_store')
C6_main_div20_CAST_store = solver.IntVar(0, 1, 'C6_main_div20_CAST_store')
C7_main_div20_CAST_store = solver.IntVar(0, 1, 'C7_main_div20_CAST_store')
C8_main_div20_CAST_store = solver.IntVar(0, 1, 'C8_main_div20_CAST_store')
solver.Add( + (1)*main_div20_fixp + (1)*main_div20_CAST_store_float + (-1)*C3_main_div20_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div20_CAST_store
solver.Add( + (1)*main_div20_float + (1)*main_div20_CAST_store_fixp + (-1)*C4_main_div20_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div20_CAST_store
solver.Add( + (1)*main_div20_fixp + (1)*main_div20_CAST_store_double + (-1)*C5_main_div20_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div20_CAST_store
solver.Add( + (1)*main_div20_double + (1)*main_div20_CAST_store_fixp + (-1)*C6_main_div20_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div20_CAST_store
solver.Add( + (1)*main_div20_float + (1)*main_div20_CAST_store_double + (-1)*C7_main_div20_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div20_CAST_store
solver.Add( + (1)*main_div20_double + (1)*main_div20_CAST_store_float + (-1)*C8_main_div20_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div20_CAST_store
solver.Add( + (1)*mul2_fixp + (-1)*main_div20_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*mul2_float + (-1)*main_div20_CAST_store_float==0)    #float equality
solver.Add( + (1)*mul2_double + (-1)*main_div20_CAST_store_double==0)    #double equality
solver.Add( + (1)*mul2_fixbits + (-1)*main_div20_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
mul2_enob_storeENOB = solver.IntVar(-10000, 10000, 'mul2_enob_storeENOB')
solver.Add( + (1)*mul2_enob_storeENOB + (-1)*mul2_fixbits + (10000)*mul2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*mul2_enob_storeENOB + (10000)*mul2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*mul2_enob_storeENOB + (10000)*mul2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*mul2_enob_storeENOB + (-1)*main_div20_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
mul1_enob_memphi_main_tmp8 = solver.IntVar(-10000, 10000, 'mul1_enob_memphi_main_tmp8')
solver.Add( + (1)*mul1_enob_memphi_main_tmp8 + (-1)*mul1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp8_enob_0 = solver.IntVar(0, 1, 'main_main_tmp8_enob_0')
solver.Add( + (1)*main_main_tmp8_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mul1_enob_memphi_main_tmp8 + (-1)*mul1_enob_storeENOB + (10000)*main_main_tmp8_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double -0.000000e+00
ConstantValue__9_fixbits = solver.IntVar(0, 32, 'ConstantValue__9_fixbits')
ConstantValue__9_fixp = solver.IntVar(0, 1, 'ConstantValue__9_fixp')
ConstantValue__9_float = solver.IntVar(0, 1, 'ConstantValue__9_float')
ConstantValue__9_double = solver.IntVar(0, 1, 'ConstantValue__9_double')
ConstantValue__9_enob = solver.IntVar(-10000, 10000, 'ConstantValue__9_enob')
solver.Add( + (1)*ConstantValue__9_enob + (-1)*ConstantValue__9_fixbits + (10000)*ConstantValue__9_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__9_enob + (10000)*ConstantValue__9_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__9_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__9_fixp + (1)*ConstantValue__9_float + (1)*ConstantValue__9_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__9_fixbits + (-10000)*ConstantValue__9_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__10_fixbits = solver.IntVar(0, 32, 'ConstantValue__10_fixbits')
ConstantValue__10_fixp = solver.IntVar(0, 1, 'ConstantValue__10_fixp')
ConstantValue__10_float = solver.IntVar(0, 1, 'ConstantValue__10_float')
ConstantValue__10_double = solver.IntVar(0, 1, 'ConstantValue__10_double')
ConstantValue__10_enob = solver.IntVar(-10000, 10000, 'ConstantValue__10_enob')
solver.Add( + (1)*ConstantValue__10_enob + (-1)*ConstantValue__10_fixbits + (10000)*ConstantValue__10_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__10_enob + (10000)*ConstantValue__10_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__10_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__10_fixp + (1)*ConstantValue__10_float + (1)*ConstantValue__10_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__10_fixbits + (-10000)*ConstantValue__10_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
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



#Constraint for cast for   %sub21 = fsub double -0.000000e+00, %tmp8, !taffo.info !72, !taffo.initweight !44, !taffo.constinfo !74
ConstantValue__11_CAST_sub21_fixbits = solver.IntVar(0, 32, 'ConstantValue__11_CAST_sub21_fixbits')
ConstantValue__11_CAST_sub21_fixp = solver.IntVar(0, 1, 'ConstantValue__11_CAST_sub21_fixp')
ConstantValue__11_CAST_sub21_float = solver.IntVar(0, 1, 'ConstantValue__11_CAST_sub21_float')
ConstantValue__11_CAST_sub21_double = solver.IntVar(0, 1, 'ConstantValue__11_CAST_sub21_double')
solver.Add( + (1)*ConstantValue__11_CAST_sub21_fixp + (1)*ConstantValue__11_CAST_sub21_float + (1)*ConstantValue__11_CAST_sub21_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__11_CAST_sub21_fixbits + (-10000)*ConstantValue__11_CAST_sub21_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C1_ConstantValue__11_CAST_sub21')
C2_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C2_ConstantValue__11_CAST_sub21')
solver.Add( + (1)*ConstantValue__11_fixbits + (-1)*ConstantValue__11_CAST_sub21_fixbits + (-10000)*C1_ConstantValue__11_CAST_sub21<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__11_fixbits + (1)*ConstantValue__11_CAST_sub21_fixbits + (-10000)*C2_ConstantValue__11_CAST_sub21<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__11_CAST_sub21
castCostObj +=  + (1)*C2_ConstantValue__11_CAST_sub21
C3_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C3_ConstantValue__11_CAST_sub21')
C4_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C4_ConstantValue__11_CAST_sub21')
C5_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C5_ConstantValue__11_CAST_sub21')
C6_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C6_ConstantValue__11_CAST_sub21')
C7_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C7_ConstantValue__11_CAST_sub21')
C8_ConstantValue__11_CAST_sub21 = solver.IntVar(0, 1, 'C8_ConstantValue__11_CAST_sub21')
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_CAST_sub21_float + (-1)*C3_ConstantValue__11_CAST_sub21<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__11_CAST_sub21
solver.Add( + (1)*ConstantValue__11_float + (1)*ConstantValue__11_CAST_sub21_fixp + (-1)*C4_ConstantValue__11_CAST_sub21<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__11_CAST_sub21
solver.Add( + (1)*ConstantValue__11_fixp + (1)*ConstantValue__11_CAST_sub21_double + (-1)*C5_ConstantValue__11_CAST_sub21<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__11_CAST_sub21
solver.Add( + (1)*ConstantValue__11_double + (1)*ConstantValue__11_CAST_sub21_fixp + (-1)*C6_ConstantValue__11_CAST_sub21<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__11_CAST_sub21
solver.Add( + (1)*ConstantValue__11_float + (1)*ConstantValue__11_CAST_sub21_double + (-1)*C7_ConstantValue__11_CAST_sub21<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__11_CAST_sub21
solver.Add( + (1)*ConstantValue__11_double + (1)*ConstantValue__11_CAST_sub21_float + (-1)*C8_ConstantValue__11_CAST_sub21<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__11_CAST_sub21



#Constraint for cast for   %sub21 = fsub double -0.000000e+00, %tmp8, !taffo.info !72, !taffo.initweight !44, !taffo.constinfo !74
mul1_CAST_sub21_fixbits = solver.IntVar(0, 22, 'mul1_CAST_sub21_fixbits')
mul1_CAST_sub21_fixp = solver.IntVar(0, 1, 'mul1_CAST_sub21_fixp')
mul1_CAST_sub21_float = solver.IntVar(0, 1, 'mul1_CAST_sub21_float')
mul1_CAST_sub21_double = solver.IntVar(0, 1, 'mul1_CAST_sub21_double')
solver.Add( + (1)*mul1_CAST_sub21_fixp + (1)*mul1_CAST_sub21_float + (1)*mul1_CAST_sub21_double==1)    #exactly 1 type
solver.Add( + (1)*mul1_CAST_sub21_fixbits + (-10000)*mul1_CAST_sub21_fixp<=0)    #If no fix, fix frac part = 0
C1_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C1_mul1_CAST_sub21')
C2_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C2_mul1_CAST_sub21')
solver.Add( + (1)*mul1_fixbits + (-1)*mul1_CAST_sub21_fixbits + (-10000)*C1_mul1_CAST_sub21<=0)    #Shift cost 1
solver.Add( + (-1)*mul1_fixbits + (1)*mul1_CAST_sub21_fixbits + (-10000)*C2_mul1_CAST_sub21<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mul1_CAST_sub21
castCostObj +=  + (1)*C2_mul1_CAST_sub21
C3_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C3_mul1_CAST_sub21')
C4_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C4_mul1_CAST_sub21')
C5_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C5_mul1_CAST_sub21')
C6_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C6_mul1_CAST_sub21')
C7_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C7_mul1_CAST_sub21')
C8_mul1_CAST_sub21 = solver.IntVar(0, 1, 'C8_mul1_CAST_sub21')
solver.Add( + (1)*mul1_fixp + (1)*mul1_CAST_sub21_float + (-1)*C3_mul1_CAST_sub21<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_mul1_CAST_sub21
solver.Add( + (1)*mul1_float + (1)*mul1_CAST_sub21_fixp + (-1)*C4_mul1_CAST_sub21<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_mul1_CAST_sub21
solver.Add( + (1)*mul1_fixp + (1)*mul1_CAST_sub21_double + (-1)*C5_mul1_CAST_sub21<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_mul1_CAST_sub21
solver.Add( + (1)*mul1_double + (1)*mul1_CAST_sub21_fixp + (-1)*C6_mul1_CAST_sub21<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_mul1_CAST_sub21
solver.Add( + (1)*mul1_float + (1)*mul1_CAST_sub21_double + (-1)*C7_mul1_CAST_sub21<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_mul1_CAST_sub21
solver.Add( + (1)*mul1_double + (1)*mul1_CAST_sub21_float + (-1)*C8_mul1_CAST_sub21<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_mul1_CAST_sub21



#Stuff for   %sub21 = fsub double -0.000000e+00, %tmp8, !taffo.info !72, !taffo.initweight !44, !taffo.constinfo !74
main_sub21_fixbits = solver.IntVar(0, 21, 'main_sub21_fixbits')
main_sub21_fixp = solver.IntVar(0, 1, 'main_sub21_fixp')
main_sub21_float = solver.IntVar(0, 1, 'main_sub21_float')
main_sub21_double = solver.IntVar(0, 1, 'main_sub21_double')
main_sub21_enob = solver.IntVar(-10000, 10000, 'main_sub21_enob')
solver.Add( + (1)*main_sub21_enob + (-1)*main_sub21_fixbits + (10000)*main_sub21_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub21_enob + (10000)*main_sub21_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub21_enob + (10000)*main_sub21_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub21_fixbits + (-10000)*main_sub21_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_sub21_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub21_enob
solver.Add( + (1)*main_sub21_fixp + (1)*main_sub21_float + (1)*main_sub21_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub21_fixbits + (-10000)*main_sub21_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__11_CAST_sub21_fixp + (-1)*mul1_CAST_sub21_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__11_CAST_sub21_float + (-1)*mul1_CAST_sub21_float==0)    #float equality
solver.Add( + (1)*ConstantValue__11_CAST_sub21_double + (-1)*mul1_CAST_sub21_double==0)    #double equality
solver.Add( + (1)*ConstantValue__11_CAST_sub21_fixbits + (-1)*mul1_CAST_sub21_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__11_CAST_sub21_fixp + (-1)*main_sub21_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__11_CAST_sub21_float + (-1)*main_sub21_float==0)    #float equality
solver.Add( + (1)*ConstantValue__11_CAST_sub21_double + (-1)*main_sub21_double==0)    #double equality
solver.Add( + (1)*ConstantValue__11_CAST_sub21_fixbits + (-1)*main_sub21_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub21_fixp
mathCostObj +=  + (3)*main_sub21_float
mathCostObj +=  + (6.64928)*main_sub21_double
solver.Add( + (1)*main_sub21_enob + (-1)*ConstantValue__9_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub21_enob + (-1)*mul1_enob_memphi_main_tmp8<=0)    #Enob propagation in sub second addend



#Stuff for double 2.000000e+00
ConstantValue__12_fixbits = solver.IntVar(0, 30, 'ConstantValue__12_fixbits')
ConstantValue__12_fixp = solver.IntVar(0, 1, 'ConstantValue__12_fixp')
ConstantValue__12_float = solver.IntVar(0, 1, 'ConstantValue__12_float')
ConstantValue__12_double = solver.IntVar(0, 1, 'ConstantValue__12_double')
ConstantValue__12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__12_enob')
solver.Add( + (1)*ConstantValue__12_enob + (-1)*ConstantValue__12_fixbits + (10000)*ConstantValue__12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__12_enob + (10000)*ConstantValue__12_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__12_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__12_fixp + (1)*ConstantValue__12_float + (1)*ConstantValue__12_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__12_fixbits + (-10000)*ConstantValue__12_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__13_fixbits = solver.IntVar(0, 30, 'ConstantValue__13_fixbits')
ConstantValue__13_fixp = solver.IntVar(0, 1, 'ConstantValue__13_fixp')
ConstantValue__13_float = solver.IntVar(0, 1, 'ConstantValue__13_float')
ConstantValue__13_double = solver.IntVar(0, 1, 'ConstantValue__13_double')
ConstantValue__13_enob = solver.IntVar(-10000, 10000, 'ConstantValue__13_enob')
solver.Add( + (1)*ConstantValue__13_enob + (-1)*ConstantValue__13_fixbits + (10000)*ConstantValue__13_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__13_enob + (10000)*ConstantValue__13_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__13_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__13_fixp + (1)*ConstantValue__13_float + (1)*ConstantValue__13_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__13_fixbits + (-10000)*ConstantValue__13_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div22 = fdiv double %sub21, 2.000000e+00, !taffo.info !77, !taffo.initweight !45, !taffo.constinfo !79
main_sub21_CAST_div22_fixbits = solver.IntVar(0, 21, 'main_sub21_CAST_div22_fixbits')
main_sub21_CAST_div22_fixp = solver.IntVar(0, 1, 'main_sub21_CAST_div22_fixp')
main_sub21_CAST_div22_float = solver.IntVar(0, 1, 'main_sub21_CAST_div22_float')
main_sub21_CAST_div22_double = solver.IntVar(0, 1, 'main_sub21_CAST_div22_double')
solver.Add( + (1)*main_sub21_CAST_div22_fixp + (1)*main_sub21_CAST_div22_float + (1)*main_sub21_CAST_div22_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub21_CAST_div22_fixbits + (-10000)*main_sub21_CAST_div22_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C1_main_sub21_CAST_div22')
C2_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C2_main_sub21_CAST_div22')
solver.Add( + (1)*main_sub21_fixbits + (-1)*main_sub21_CAST_div22_fixbits + (-10000)*C1_main_sub21_CAST_div22<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub21_fixbits + (1)*main_sub21_CAST_div22_fixbits + (-10000)*C2_main_sub21_CAST_div22<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub21_CAST_div22
castCostObj +=  + (1)*C2_main_sub21_CAST_div22
C3_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C3_main_sub21_CAST_div22')
C4_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C4_main_sub21_CAST_div22')
C5_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C5_main_sub21_CAST_div22')
C6_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C6_main_sub21_CAST_div22')
C7_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C7_main_sub21_CAST_div22')
C8_main_sub21_CAST_div22 = solver.IntVar(0, 1, 'C8_main_sub21_CAST_div22')
solver.Add( + (1)*main_sub21_fixp + (1)*main_sub21_CAST_div22_float + (-1)*C3_main_sub21_CAST_div22<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub21_CAST_div22
solver.Add( + (1)*main_sub21_float + (1)*main_sub21_CAST_div22_fixp + (-1)*C4_main_sub21_CAST_div22<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub21_CAST_div22
solver.Add( + (1)*main_sub21_fixp + (1)*main_sub21_CAST_div22_double + (-1)*C5_main_sub21_CAST_div22<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub21_CAST_div22
solver.Add( + (1)*main_sub21_double + (1)*main_sub21_CAST_div22_fixp + (-1)*C6_main_sub21_CAST_div22<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub21_CAST_div22
solver.Add( + (1)*main_sub21_float + (1)*main_sub21_CAST_div22_double + (-1)*C7_main_sub21_CAST_div22<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub21_CAST_div22
solver.Add( + (1)*main_sub21_double + (1)*main_sub21_CAST_div22_float + (-1)*C8_main_sub21_CAST_div22<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub21_CAST_div22



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
solver.Add( + (1)*ConstantValue__14_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_float + (1)*ConstantValue__14_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__14_fixbits + (-10000)*ConstantValue__14_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div22 = fdiv double %sub21, 2.000000e+00, !taffo.info !77, !taffo.initweight !45, !taffo.constinfo !79
ConstantValue__14_CAST_div22_fixbits = solver.IntVar(0, 30, 'ConstantValue__14_CAST_div22_fixbits')
ConstantValue__14_CAST_div22_fixp = solver.IntVar(0, 1, 'ConstantValue__14_CAST_div22_fixp')
ConstantValue__14_CAST_div22_float = solver.IntVar(0, 1, 'ConstantValue__14_CAST_div22_float')
ConstantValue__14_CAST_div22_double = solver.IntVar(0, 1, 'ConstantValue__14_CAST_div22_double')
solver.Add( + (1)*ConstantValue__14_CAST_div22_fixp + (1)*ConstantValue__14_CAST_div22_float + (1)*ConstantValue__14_CAST_div22_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__14_CAST_div22_fixbits + (-10000)*ConstantValue__14_CAST_div22_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C1_ConstantValue__14_CAST_div22')
C2_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C2_ConstantValue__14_CAST_div22')
solver.Add( + (1)*ConstantValue__14_fixbits + (-1)*ConstantValue__14_CAST_div22_fixbits + (-10000)*C1_ConstantValue__14_CAST_div22<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__14_fixbits + (1)*ConstantValue__14_CAST_div22_fixbits + (-10000)*C2_ConstantValue__14_CAST_div22<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__14_CAST_div22
castCostObj +=  + (1)*C2_ConstantValue__14_CAST_div22
C3_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C3_ConstantValue__14_CAST_div22')
C4_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C4_ConstantValue__14_CAST_div22')
C5_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C5_ConstantValue__14_CAST_div22')
C6_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C6_ConstantValue__14_CAST_div22')
C7_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C7_ConstantValue__14_CAST_div22')
C8_ConstantValue__14_CAST_div22 = solver.IntVar(0, 1, 'C8_ConstantValue__14_CAST_div22')
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_div22_float + (-1)*C3_ConstantValue__14_CAST_div22<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__14_CAST_div22
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_div22_fixp + (-1)*C4_ConstantValue__14_CAST_div22<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__14_CAST_div22
solver.Add( + (1)*ConstantValue__14_fixp + (1)*ConstantValue__14_CAST_div22_double + (-1)*C5_ConstantValue__14_CAST_div22<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__14_CAST_div22
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_div22_fixp + (-1)*C6_ConstantValue__14_CAST_div22<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__14_CAST_div22
solver.Add( + (1)*ConstantValue__14_float + (1)*ConstantValue__14_CAST_div22_double + (-1)*C7_ConstantValue__14_CAST_div22<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__14_CAST_div22
solver.Add( + (1)*ConstantValue__14_double + (1)*ConstantValue__14_CAST_div22_float + (-1)*C8_ConstantValue__14_CAST_div22<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__14_CAST_div22



#Stuff for   %div22 = fdiv double %sub21, 2.000000e+00, !taffo.info !77, !taffo.initweight !45, !taffo.constinfo !79
main_div22_fixbits = solver.IntVar(0, 22, 'main_div22_fixbits')
main_div22_fixp = solver.IntVar(0, 1, 'main_div22_fixp')
main_div22_float = solver.IntVar(0, 1, 'main_div22_float')
main_div22_double = solver.IntVar(0, 1, 'main_div22_double')
main_div22_enob = solver.IntVar(-10000, 10000, 'main_div22_enob')
solver.Add( + (1)*main_div22_enob + (-1)*main_div22_fixbits + (10000)*main_div22_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div22_enob + (10000)*main_div22_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div22_enob + (10000)*main_div22_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div22_fixbits + (-10000)*main_div22_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_div22_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div22_enob
solver.Add( + (1)*main_div22_fixp + (1)*main_div22_float + (1)*main_div22_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div22_fixbits + (-10000)*main_div22_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub21_CAST_div22_fixp + (-1)*ConstantValue__14_CAST_div22_fixp==0)    #fix equality
solver.Add( + (1)*main_sub21_CAST_div22_float + (-1)*ConstantValue__14_CAST_div22_float==0)    #float equality
solver.Add( + (1)*main_sub21_CAST_div22_double + (-1)*ConstantValue__14_CAST_div22_double==0)    #double equality
solver.Add( + (1)*main_sub21_CAST_div22_fixp + (-1)*main_div22_fixp==0)    #fix equality
solver.Add( + (1)*main_sub21_CAST_div22_float + (-1)*main_div22_float==0)    #float equality
solver.Add( + (1)*main_sub21_CAST_div22_double + (-1)*main_div22_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div22_fixp
mathCostObj +=  + (6)*main_div22_float
mathCostObj +=  + (12)*main_div22_double
main_main_div22_enob_1 = solver.IntVar(0, 1, 'main_main_div22_enob_1')
main_main_div22_enob_2 = solver.IntVar(0, 1, 'main_main_div22_enob_2')
solver.Add( + (1)*main_main_div22_enob_1 + (1)*main_main_div22_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div22_enob + (-1)*ConstantValue__12_enob + (-10000)*main_main_div22_enob_1<=3072)    #Enob: propagation in division 1
solver.Add( + (1)*main_div22_enob + (-1)*main_sub21_enob + (-10000)*main_main_div22_enob_2<=3072)    #Enob: propagation in division 2



#Constraint for cast for   store double %div22, double* @a, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
main_div22_CAST_store_fixbits = solver.IntVar(0, 22, 'main_div22_CAST_store_fixbits')
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
castCostObj +=  + (6.25227)*C3_main_div22_CAST_store
solver.Add( + (1)*main_div22_float + (1)*main_div22_CAST_store_fixp + (-1)*C4_main_div22_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div22_CAST_store
solver.Add( + (1)*main_div22_fixp + (1)*main_div22_CAST_store_double + (-1)*C5_main_div22_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div22_CAST_store
solver.Add( + (1)*main_div22_double + (1)*main_div22_CAST_store_fixp + (-1)*C6_main_div22_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div22_CAST_store
solver.Add( + (1)*main_div22_float + (1)*main_div22_CAST_store_double + (-1)*C7_main_div22_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div22_CAST_store
solver.Add( + (1)*main_div22_double + (1)*main_div22_CAST_store_float + (-1)*C8_main_div22_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div22_CAST_store
solver.Add( + (1)*a_fixp + (-1)*main_div22_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*a_float + (-1)*main_div22_CAST_store_float==0)    #float equality
solver.Add( + (1)*a_double + (-1)*main_div22_CAST_store_double==0)    #double equality
solver.Add( + (1)*a_fixbits + (-1)*main_div22_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
a_enob_storeENOB = solver.IntVar(-10000, 10000, 'a_enob_storeENOB')
solver.Add( + (1)*a_enob_storeENOB + (-1)*a_fixbits + (10000)*a_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*a_enob_storeENOB + (10000)*a_float<=10149)    #Enob constraint for float
solver.Add( + (1)*a_enob_storeENOB + (10000)*a_double<=11074)    #Enob constraint for double
solver.Add( + (1)*a_enob_storeENOB + (-1)*main_div22_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
mul1_enob_memphi_main_tmp9 = solver.IntVar(-10000, 10000, 'mul1_enob_memphi_main_tmp9')
solver.Add( + (1)*mul1_enob_memphi_main_tmp9 + (-1)*mul1_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp9_enob_0 = solver.IntVar(0, 1, 'main_main_tmp9_enob_0')
solver.Add( + (1)*main_main_tmp9_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mul1_enob_memphi_main_tmp9 + (-1)*mul1_enob_storeENOB + (10000)*main_main_tmp9_enob_0<=10000)    #Enob: forcing MEM phi enob



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
solver.Add( + (1)*ConstantValue__16_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__16_fixp + (1)*ConstantValue__16_float + (1)*ConstantValue__16_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__16_fixbits + (-10000)*ConstantValue__16_fixp<=0)    #If not fix, frac part to zero



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
solver.Add( + (1)*ConstantValue__17_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_float + (1)*ConstantValue__17_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__17_fixbits + (-10000)*ConstantValue__17_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add23 = fadd double 1.000000e+00, %tmp9, !taffo.info !80, !taffo.initweight !44, !taffo.constinfo !66
ConstantValue__17_CAST_add23_fixbits = solver.IntVar(0, 31, 'ConstantValue__17_CAST_add23_fixbits')
ConstantValue__17_CAST_add23_fixp = solver.IntVar(0, 1, 'ConstantValue__17_CAST_add23_fixp')
ConstantValue__17_CAST_add23_float = solver.IntVar(0, 1, 'ConstantValue__17_CAST_add23_float')
ConstantValue__17_CAST_add23_double = solver.IntVar(0, 1, 'ConstantValue__17_CAST_add23_double')
solver.Add( + (1)*ConstantValue__17_CAST_add23_fixp + (1)*ConstantValue__17_CAST_add23_float + (1)*ConstantValue__17_CAST_add23_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__17_CAST_add23_fixbits + (-10000)*ConstantValue__17_CAST_add23_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C1_ConstantValue__17_CAST_add23')
C2_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C2_ConstantValue__17_CAST_add23')
solver.Add( + (1)*ConstantValue__17_fixbits + (-1)*ConstantValue__17_CAST_add23_fixbits + (-10000)*C1_ConstantValue__17_CAST_add23<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__17_fixbits + (1)*ConstantValue__17_CAST_add23_fixbits + (-10000)*C2_ConstantValue__17_CAST_add23<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__17_CAST_add23
castCostObj +=  + (1)*C2_ConstantValue__17_CAST_add23
C3_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C3_ConstantValue__17_CAST_add23')
C4_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C4_ConstantValue__17_CAST_add23')
C5_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C5_ConstantValue__17_CAST_add23')
C6_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C6_ConstantValue__17_CAST_add23')
C7_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C7_ConstantValue__17_CAST_add23')
C8_ConstantValue__17_CAST_add23 = solver.IntVar(0, 1, 'C8_ConstantValue__17_CAST_add23')
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_CAST_add23_float + (-1)*C3_ConstantValue__17_CAST_add23<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__17_CAST_add23
solver.Add( + (1)*ConstantValue__17_float + (1)*ConstantValue__17_CAST_add23_fixp + (-1)*C4_ConstantValue__17_CAST_add23<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__17_CAST_add23
solver.Add( + (1)*ConstantValue__17_fixp + (1)*ConstantValue__17_CAST_add23_double + (-1)*C5_ConstantValue__17_CAST_add23<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__17_CAST_add23
solver.Add( + (1)*ConstantValue__17_double + (1)*ConstantValue__17_CAST_add23_fixp + (-1)*C6_ConstantValue__17_CAST_add23<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__17_CAST_add23
solver.Add( + (1)*ConstantValue__17_float + (1)*ConstantValue__17_CAST_add23_double + (-1)*C7_ConstantValue__17_CAST_add23<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__17_CAST_add23
solver.Add( + (1)*ConstantValue__17_double + (1)*ConstantValue__17_CAST_add23_float + (-1)*C8_ConstantValue__17_CAST_add23<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__17_CAST_add23



#Constraint for cast for   %add23 = fadd double 1.000000e+00, %tmp9, !taffo.info !80, !taffo.initweight !44, !taffo.constinfo !66
mul1_CAST_add23_fixbits = solver.IntVar(0, 22, 'mul1_CAST_add23_fixbits')
mul1_CAST_add23_fixp = solver.IntVar(0, 1, 'mul1_CAST_add23_fixp')
mul1_CAST_add23_float = solver.IntVar(0, 1, 'mul1_CAST_add23_float')
mul1_CAST_add23_double = solver.IntVar(0, 1, 'mul1_CAST_add23_double')
solver.Add( + (1)*mul1_CAST_add23_fixp + (1)*mul1_CAST_add23_float + (1)*mul1_CAST_add23_double==1)    #exactly 1 type
solver.Add( + (1)*mul1_CAST_add23_fixbits + (-10000)*mul1_CAST_add23_fixp<=0)    #If no fix, fix frac part = 0
C1_mul1_CAST_add23 = solver.IntVar(0, 1, 'C1_mul1_CAST_add23')
C2_mul1_CAST_add23 = solver.IntVar(0, 1, 'C2_mul1_CAST_add23')
solver.Add( + (1)*mul1_fixbits + (-1)*mul1_CAST_add23_fixbits + (-10000)*C1_mul1_CAST_add23<=0)    #Shift cost 1
solver.Add( + (-1)*mul1_fixbits + (1)*mul1_CAST_add23_fixbits + (-10000)*C2_mul1_CAST_add23<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mul1_CAST_add23
castCostObj +=  + (1)*C2_mul1_CAST_add23
C3_mul1_CAST_add23 = solver.IntVar(0, 1, 'C3_mul1_CAST_add23')
C4_mul1_CAST_add23 = solver.IntVar(0, 1, 'C4_mul1_CAST_add23')
C5_mul1_CAST_add23 = solver.IntVar(0, 1, 'C5_mul1_CAST_add23')
C6_mul1_CAST_add23 = solver.IntVar(0, 1, 'C6_mul1_CAST_add23')
C7_mul1_CAST_add23 = solver.IntVar(0, 1, 'C7_mul1_CAST_add23')
C8_mul1_CAST_add23 = solver.IntVar(0, 1, 'C8_mul1_CAST_add23')
solver.Add( + (1)*mul1_fixp + (1)*mul1_CAST_add23_float + (-1)*C3_mul1_CAST_add23<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_mul1_CAST_add23
solver.Add( + (1)*mul1_float + (1)*mul1_CAST_add23_fixp + (-1)*C4_mul1_CAST_add23<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_mul1_CAST_add23
solver.Add( + (1)*mul1_fixp + (1)*mul1_CAST_add23_double + (-1)*C5_mul1_CAST_add23<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_mul1_CAST_add23
solver.Add( + (1)*mul1_double + (1)*mul1_CAST_add23_fixp + (-1)*C6_mul1_CAST_add23<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_mul1_CAST_add23
solver.Add( + (1)*mul1_float + (1)*mul1_CAST_add23_double + (-1)*C7_mul1_CAST_add23<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_mul1_CAST_add23
solver.Add( + (1)*mul1_double + (1)*mul1_CAST_add23_float + (-1)*C8_mul1_CAST_add23<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_mul1_CAST_add23



#Stuff for   %add23 = fadd double 1.000000e+00, %tmp9, !taffo.info !80, !taffo.initweight !44, !taffo.constinfo !66
main_add23_fixbits = solver.IntVar(0, 22, 'main_add23_fixbits')
main_add23_fixp = solver.IntVar(0, 1, 'main_add23_fixp')
main_add23_float = solver.IntVar(0, 1, 'main_add23_float')
main_add23_double = solver.IntVar(0, 1, 'main_add23_double')
main_add23_enob = solver.IntVar(-10000, 10000, 'main_add23_enob')
solver.Add( + (1)*main_add23_enob + (-1)*main_add23_fixbits + (10000)*main_add23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add23_enob + (10000)*main_add23_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_add23_enob + (10000)*main_add23_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_add23_fixbits + (-10000)*main_add23_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_add23_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add23_enob
solver.Add( + (1)*main_add23_fixp + (1)*main_add23_float + (1)*main_add23_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add23_fixbits + (-10000)*main_add23_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__17_CAST_add23_fixp + (-1)*mul1_CAST_add23_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__17_CAST_add23_float + (-1)*mul1_CAST_add23_float==0)    #float equality
solver.Add( + (1)*ConstantValue__17_CAST_add23_double + (-1)*mul1_CAST_add23_double==0)    #double equality
solver.Add( + (1)*ConstantValue__17_CAST_add23_fixbits + (-1)*mul1_CAST_add23_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__17_CAST_add23_fixp + (-1)*main_add23_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__17_CAST_add23_float + (-1)*main_add23_float==0)    #float equality
solver.Add( + (1)*ConstantValue__17_CAST_add23_double + (-1)*main_add23_double==0)    #double equality
solver.Add( + (1)*ConstantValue__17_CAST_add23_fixbits + (-1)*main_add23_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add23_fixp
mathCostObj +=  + (3)*main_add23_float
mathCostObj +=  + (6.64928)*main_add23_double
solver.Add( + (1)*main_add23_enob + (-1)*ConstantValue__15_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add23_enob + (-1)*mul1_enob_memphi_main_tmp9<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add23, double* @b, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
main_add23_CAST_store_fixbits = solver.IntVar(0, 22, 'main_add23_CAST_store_fixbits')
main_add23_CAST_store_fixp = solver.IntVar(0, 1, 'main_add23_CAST_store_fixp')
main_add23_CAST_store_float = solver.IntVar(0, 1, 'main_add23_CAST_store_float')
main_add23_CAST_store_double = solver.IntVar(0, 1, 'main_add23_CAST_store_double')
solver.Add( + (1)*main_add23_CAST_store_fixp + (1)*main_add23_CAST_store_float + (1)*main_add23_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add23_CAST_store_fixbits + (-10000)*main_add23_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add23_CAST_store = solver.IntVar(0, 1, 'C1_main_add23_CAST_store')
C2_main_add23_CAST_store = solver.IntVar(0, 1, 'C2_main_add23_CAST_store')
solver.Add( + (1)*main_add23_fixbits + (-1)*main_add23_CAST_store_fixbits + (-10000)*C1_main_add23_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add23_fixbits + (1)*main_add23_CAST_store_fixbits + (-10000)*C2_main_add23_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add23_CAST_store
castCostObj +=  + (1)*C2_main_add23_CAST_store
C3_main_add23_CAST_store = solver.IntVar(0, 1, 'C3_main_add23_CAST_store')
C4_main_add23_CAST_store = solver.IntVar(0, 1, 'C4_main_add23_CAST_store')
C5_main_add23_CAST_store = solver.IntVar(0, 1, 'C5_main_add23_CAST_store')
C6_main_add23_CAST_store = solver.IntVar(0, 1, 'C6_main_add23_CAST_store')
C7_main_add23_CAST_store = solver.IntVar(0, 1, 'C7_main_add23_CAST_store')
C8_main_add23_CAST_store = solver.IntVar(0, 1, 'C8_main_add23_CAST_store')
solver.Add( + (1)*main_add23_fixp + (1)*main_add23_CAST_store_float + (-1)*C3_main_add23_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add23_CAST_store
solver.Add( + (1)*main_add23_float + (1)*main_add23_CAST_store_fixp + (-1)*C4_main_add23_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add23_CAST_store
solver.Add( + (1)*main_add23_fixp + (1)*main_add23_CAST_store_double + (-1)*C5_main_add23_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add23_CAST_store
solver.Add( + (1)*main_add23_double + (1)*main_add23_CAST_store_fixp + (-1)*C6_main_add23_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add23_CAST_store
solver.Add( + (1)*main_add23_float + (1)*main_add23_CAST_store_double + (-1)*C7_main_add23_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add23_CAST_store
solver.Add( + (1)*main_add23_double + (1)*main_add23_CAST_store_float + (-1)*C8_main_add23_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add23_CAST_store
solver.Add( + (1)*b_fixp + (-1)*main_add23_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*b_float + (-1)*main_add23_CAST_store_float==0)    #float equality
solver.Add( + (1)*b_double + (-1)*main_add23_CAST_store_double==0)    #double equality
solver.Add( + (1)*b_fixbits + (-1)*main_add23_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
b_enob_storeENOB = solver.IntVar(-10000, 10000, 'b_enob_storeENOB')
solver.Add( + (1)*b_enob_storeENOB + (-1)*b_fixbits + (10000)*b_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*b_enob_storeENOB + (10000)*b_float<=10149)    #Enob constraint for float
solver.Add( + (1)*b_enob_storeENOB + (10000)*b_double<=11074)    #Enob constraint for double
solver.Add( + (1)*b_enob_storeENOB + (-1)*main_add23_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp10 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp10')
solver.Add( + (1)*a_enob_memphi_main_tmp10 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp10_enob_0 = solver.IntVar(0, 1, 'main_main_tmp10_enob_0')
solver.Add( + (1)*main_main_tmp10_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp10 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp10_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp10, double* @c, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
a_CAST_store_fixbits = solver.IntVar(0, 22, 'a_CAST_store_fixbits')
a_CAST_store_fixp = solver.IntVar(0, 1, 'a_CAST_store_fixp')
a_CAST_store_float = solver.IntVar(0, 1, 'a_CAST_store_float')
a_CAST_store_double = solver.IntVar(0, 1, 'a_CAST_store_double')
solver.Add( + (1)*a_CAST_store_fixp + (1)*a_CAST_store_float + (1)*a_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_store_fixbits + (-10000)*a_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_store = solver.IntVar(0, 1, 'C1_a_CAST_store')
C2_a_CAST_store = solver.IntVar(0, 1, 'C2_a_CAST_store')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_store_fixbits + (-10000)*C1_a_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_store_fixbits + (-10000)*C2_a_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_a_CAST_store
castCostObj +=  + (1)*C2_a_CAST_store
C3_a_CAST_store = solver.IntVar(0, 1, 'C3_a_CAST_store')
C4_a_CAST_store = solver.IntVar(0, 1, 'C4_a_CAST_store')
C5_a_CAST_store = solver.IntVar(0, 1, 'C5_a_CAST_store')
C6_a_CAST_store = solver.IntVar(0, 1, 'C6_a_CAST_store')
C7_a_CAST_store = solver.IntVar(0, 1, 'C7_a_CAST_store')
C8_a_CAST_store = solver.IntVar(0, 1, 'C8_a_CAST_store')
solver.Add( + (1)*a_fixp + (1)*a_CAST_store_float + (-1)*C3_a_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_a_CAST_store
solver.Add( + (1)*a_float + (1)*a_CAST_store_fixp + (-1)*C4_a_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_a_CAST_store
solver.Add( + (1)*a_fixp + (1)*a_CAST_store_double + (-1)*C5_a_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_a_CAST_store
solver.Add( + (1)*a_double + (1)*a_CAST_store_fixp + (-1)*C6_a_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_a_CAST_store
solver.Add( + (1)*a_float + (1)*a_CAST_store_double + (-1)*C7_a_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_a_CAST_store
solver.Add( + (1)*a_double + (1)*a_CAST_store_float + (-1)*C8_a_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_a_CAST_store
solver.Add( + (1)*c_fixp + (-1)*a_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*c_float + (-1)*a_CAST_store_float==0)    #float equality
solver.Add( + (1)*c_double + (-1)*a_CAST_store_double==0)    #double equality
solver.Add( + (1)*c_fixbits + (-1)*a_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
c_enob_storeENOB = solver.IntVar(-10000, 10000, 'c_enob_storeENOB')
solver.Add( + (1)*c_enob_storeENOB + (-1)*c_fixbits + (10000)*c_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*c_enob_storeENOB + (10000)*c_float<=10149)    #Enob constraint for float
solver.Add( + (1)*c_enob_storeENOB + (10000)*c_double<=11074)    #Enob constraint for double
solver.Add( + (1)*c_enob_storeENOB + (-1)*a_enob_memphi_main_tmp10<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
mul2_enob_memphi_main_tmp11 = solver.IntVar(-10000, 10000, 'mul2_enob_memphi_main_tmp11')
solver.Add( + (1)*mul2_enob_memphi_main_tmp11 + (-1)*mul2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp11_enob_0 = solver.IntVar(0, 1, 'main_main_tmp11_enob_0')
solver.Add( + (1)*main_main_tmp11_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mul2_enob_memphi_main_tmp11 + (-1)*mul2_enob_storeENOB + (10000)*main_main_tmp11_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double -0.000000e+00
ConstantValue__18_fixbits = solver.IntVar(0, 32, 'ConstantValue__18_fixbits')
ConstantValue__18_fixp = solver.IntVar(0, 1, 'ConstantValue__18_fixp')
ConstantValue__18_float = solver.IntVar(0, 1, 'ConstantValue__18_float')
ConstantValue__18_double = solver.IntVar(0, 1, 'ConstantValue__18_double')
ConstantValue__18_enob = solver.IntVar(-10000, 10000, 'ConstantValue__18_enob')
solver.Add( + (1)*ConstantValue__18_enob + (-1)*ConstantValue__18_fixbits + (10000)*ConstantValue__18_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__18_enob + (10000)*ConstantValue__18_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__18_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__18_fixp + (1)*ConstantValue__18_float + (1)*ConstantValue__18_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__18_fixbits + (-10000)*ConstantValue__18_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__19_fixbits = solver.IntVar(0, 32, 'ConstantValue__19_fixbits')
ConstantValue__19_fixp = solver.IntVar(0, 1, 'ConstantValue__19_fixp')
ConstantValue__19_float = solver.IntVar(0, 1, 'ConstantValue__19_float')
ConstantValue__19_double = solver.IntVar(0, 1, 'ConstantValue__19_double')
ConstantValue__19_enob = solver.IntVar(-10000, 10000, 'ConstantValue__19_enob')
solver.Add( + (1)*ConstantValue__19_enob + (-1)*ConstantValue__19_fixbits + (10000)*ConstantValue__19_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__19_enob + (10000)*ConstantValue__19_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__19_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__19_fixp + (1)*ConstantValue__19_float + (1)*ConstantValue__19_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__19_fixbits + (-10000)*ConstantValue__19_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__20_fixbits = solver.IntVar(0, 32, 'ConstantValue__20_fixbits')
ConstantValue__20_fixp = solver.IntVar(0, 1, 'ConstantValue__20_fixp')
ConstantValue__20_float = solver.IntVar(0, 1, 'ConstantValue__20_float')
ConstantValue__20_double = solver.IntVar(0, 1, 'ConstantValue__20_double')
ConstantValue__20_enob = solver.IntVar(-10000, 10000, 'ConstantValue__20_enob')
solver.Add( + (1)*ConstantValue__20_enob + (-1)*ConstantValue__20_fixbits + (10000)*ConstantValue__20_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__20_enob + (10000)*ConstantValue__20_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__20_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_float + (1)*ConstantValue__20_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__20_fixbits + (-10000)*ConstantValue__20_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub24 = fsub double -0.000000e+00, %tmp11, !taffo.info !77, !taffo.initweight !44, !taffo.constinfo !74
ConstantValue__20_CAST_sub24_fixbits = solver.IntVar(0, 32, 'ConstantValue__20_CAST_sub24_fixbits')
ConstantValue__20_CAST_sub24_fixp = solver.IntVar(0, 1, 'ConstantValue__20_CAST_sub24_fixp')
ConstantValue__20_CAST_sub24_float = solver.IntVar(0, 1, 'ConstantValue__20_CAST_sub24_float')
ConstantValue__20_CAST_sub24_double = solver.IntVar(0, 1, 'ConstantValue__20_CAST_sub24_double')
solver.Add( + (1)*ConstantValue__20_CAST_sub24_fixp + (1)*ConstantValue__20_CAST_sub24_float + (1)*ConstantValue__20_CAST_sub24_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__20_CAST_sub24_fixbits + (-10000)*ConstantValue__20_CAST_sub24_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C1_ConstantValue__20_CAST_sub24')
C2_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C2_ConstantValue__20_CAST_sub24')
solver.Add( + (1)*ConstantValue__20_fixbits + (-1)*ConstantValue__20_CAST_sub24_fixbits + (-10000)*C1_ConstantValue__20_CAST_sub24<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__20_fixbits + (1)*ConstantValue__20_CAST_sub24_fixbits + (-10000)*C2_ConstantValue__20_CAST_sub24<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__20_CAST_sub24
castCostObj +=  + (1)*C2_ConstantValue__20_CAST_sub24
C3_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C3_ConstantValue__20_CAST_sub24')
C4_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C4_ConstantValue__20_CAST_sub24')
C5_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C5_ConstantValue__20_CAST_sub24')
C6_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C6_ConstantValue__20_CAST_sub24')
C7_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C7_ConstantValue__20_CAST_sub24')
C8_ConstantValue__20_CAST_sub24 = solver.IntVar(0, 1, 'C8_ConstantValue__20_CAST_sub24')
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_CAST_sub24_float + (-1)*C3_ConstantValue__20_CAST_sub24<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__20_CAST_sub24
solver.Add( + (1)*ConstantValue__20_float + (1)*ConstantValue__20_CAST_sub24_fixp + (-1)*C4_ConstantValue__20_CAST_sub24<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__20_CAST_sub24
solver.Add( + (1)*ConstantValue__20_fixp + (1)*ConstantValue__20_CAST_sub24_double + (-1)*C5_ConstantValue__20_CAST_sub24<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__20_CAST_sub24
solver.Add( + (1)*ConstantValue__20_double + (1)*ConstantValue__20_CAST_sub24_fixp + (-1)*C6_ConstantValue__20_CAST_sub24<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__20_CAST_sub24
solver.Add( + (1)*ConstantValue__20_float + (1)*ConstantValue__20_CAST_sub24_double + (-1)*C7_ConstantValue__20_CAST_sub24<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__20_CAST_sub24
solver.Add( + (1)*ConstantValue__20_double + (1)*ConstantValue__20_CAST_sub24_float + (-1)*C8_ConstantValue__20_CAST_sub24<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__20_CAST_sub24



#Constraint for cast for   %sub24 = fsub double -0.000000e+00, %tmp11, !taffo.info !77, !taffo.initweight !44, !taffo.constinfo !74
mul2_CAST_sub24_fixbits = solver.IntVar(0, 23, 'mul2_CAST_sub24_fixbits')
mul2_CAST_sub24_fixp = solver.IntVar(0, 1, 'mul2_CAST_sub24_fixp')
mul2_CAST_sub24_float = solver.IntVar(0, 1, 'mul2_CAST_sub24_float')
mul2_CAST_sub24_double = solver.IntVar(0, 1, 'mul2_CAST_sub24_double')
solver.Add( + (1)*mul2_CAST_sub24_fixp + (1)*mul2_CAST_sub24_float + (1)*mul2_CAST_sub24_double==1)    #exactly 1 type
solver.Add( + (1)*mul2_CAST_sub24_fixbits + (-10000)*mul2_CAST_sub24_fixp<=0)    #If no fix, fix frac part = 0
C1_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C1_mul2_CAST_sub24')
C2_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C2_mul2_CAST_sub24')
solver.Add( + (1)*mul2_fixbits + (-1)*mul2_CAST_sub24_fixbits + (-10000)*C1_mul2_CAST_sub24<=0)    #Shift cost 1
solver.Add( + (-1)*mul2_fixbits + (1)*mul2_CAST_sub24_fixbits + (-10000)*C2_mul2_CAST_sub24<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mul2_CAST_sub24
castCostObj +=  + (1)*C2_mul2_CAST_sub24
C3_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C3_mul2_CAST_sub24')
C4_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C4_mul2_CAST_sub24')
C5_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C5_mul2_CAST_sub24')
C6_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C6_mul2_CAST_sub24')
C7_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C7_mul2_CAST_sub24')
C8_mul2_CAST_sub24 = solver.IntVar(0, 1, 'C8_mul2_CAST_sub24')
solver.Add( + (1)*mul2_fixp + (1)*mul2_CAST_sub24_float + (-1)*C3_mul2_CAST_sub24<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_mul2_CAST_sub24
solver.Add( + (1)*mul2_float + (1)*mul2_CAST_sub24_fixp + (-1)*C4_mul2_CAST_sub24<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_mul2_CAST_sub24
solver.Add( + (1)*mul2_fixp + (1)*mul2_CAST_sub24_double + (-1)*C5_mul2_CAST_sub24<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_mul2_CAST_sub24
solver.Add( + (1)*mul2_double + (1)*mul2_CAST_sub24_fixp + (-1)*C6_mul2_CAST_sub24<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_mul2_CAST_sub24
solver.Add( + (1)*mul2_float + (1)*mul2_CAST_sub24_double + (-1)*C7_mul2_CAST_sub24<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_mul2_CAST_sub24
solver.Add( + (1)*mul2_double + (1)*mul2_CAST_sub24_float + (-1)*C8_mul2_CAST_sub24<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_mul2_CAST_sub24



#Stuff for   %sub24 = fsub double -0.000000e+00, %tmp11, !taffo.info !77, !taffo.initweight !44, !taffo.constinfo !74
main_sub24_fixbits = solver.IntVar(0, 22, 'main_sub24_fixbits')
main_sub24_fixp = solver.IntVar(0, 1, 'main_sub24_fixp')
main_sub24_float = solver.IntVar(0, 1, 'main_sub24_float')
main_sub24_double = solver.IntVar(0, 1, 'main_sub24_double')
main_sub24_enob = solver.IntVar(-10000, 10000, 'main_sub24_enob')
solver.Add( + (1)*main_sub24_enob + (-1)*main_sub24_fixbits + (10000)*main_sub24_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub24_enob + (10000)*main_sub24_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub24_enob + (10000)*main_sub24_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub24_fixbits + (-10000)*main_sub24_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_sub24_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub24_enob
solver.Add( + (1)*main_sub24_fixp + (1)*main_sub24_float + (1)*main_sub24_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub24_fixbits + (-10000)*main_sub24_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__20_CAST_sub24_fixp + (-1)*mul2_CAST_sub24_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__20_CAST_sub24_float + (-1)*mul2_CAST_sub24_float==0)    #float equality
solver.Add( + (1)*ConstantValue__20_CAST_sub24_double + (-1)*mul2_CAST_sub24_double==0)    #double equality
solver.Add( + (1)*ConstantValue__20_CAST_sub24_fixbits + (-1)*mul2_CAST_sub24_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__20_CAST_sub24_fixp + (-1)*main_sub24_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__20_CAST_sub24_float + (-1)*main_sub24_float==0)    #float equality
solver.Add( + (1)*ConstantValue__20_CAST_sub24_double + (-1)*main_sub24_double==0)    #double equality
solver.Add( + (1)*ConstantValue__20_CAST_sub24_fixbits + (-1)*main_sub24_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub24_fixp
mathCostObj +=  + (3)*main_sub24_float
mathCostObj +=  + (6.64928)*main_sub24_double
solver.Add( + (1)*main_sub24_enob + (-1)*ConstantValue__18_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub24_enob + (-1)*mul2_enob_memphi_main_tmp11<=0)    #Enob propagation in sub second addend



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
solver.Add( + (1)*ConstantValue__21_double<=0)    #Disable double data type
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
solver.Add( + (1)*ConstantValue__22_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__22_fixp + (1)*ConstantValue__22_float + (1)*ConstantValue__22_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__22_fixbits + (-10000)*ConstantValue__22_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div25 = fdiv double %sub24, 2.000000e+00, !taffo.info !82, !taffo.initweight !45, !taffo.constinfo !79
main_sub24_CAST_div25_fixbits = solver.IntVar(0, 22, 'main_sub24_CAST_div25_fixbits')
main_sub24_CAST_div25_fixp = solver.IntVar(0, 1, 'main_sub24_CAST_div25_fixp')
main_sub24_CAST_div25_float = solver.IntVar(0, 1, 'main_sub24_CAST_div25_float')
main_sub24_CAST_div25_double = solver.IntVar(0, 1, 'main_sub24_CAST_div25_double')
solver.Add( + (1)*main_sub24_CAST_div25_fixp + (1)*main_sub24_CAST_div25_float + (1)*main_sub24_CAST_div25_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub24_CAST_div25_fixbits + (-10000)*main_sub24_CAST_div25_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C1_main_sub24_CAST_div25')
C2_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C2_main_sub24_CAST_div25')
solver.Add( + (1)*main_sub24_fixbits + (-1)*main_sub24_CAST_div25_fixbits + (-10000)*C1_main_sub24_CAST_div25<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub24_fixbits + (1)*main_sub24_CAST_div25_fixbits + (-10000)*C2_main_sub24_CAST_div25<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub24_CAST_div25
castCostObj +=  + (1)*C2_main_sub24_CAST_div25
C3_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C3_main_sub24_CAST_div25')
C4_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C4_main_sub24_CAST_div25')
C5_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C5_main_sub24_CAST_div25')
C6_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C6_main_sub24_CAST_div25')
C7_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C7_main_sub24_CAST_div25')
C8_main_sub24_CAST_div25 = solver.IntVar(0, 1, 'C8_main_sub24_CAST_div25')
solver.Add( + (1)*main_sub24_fixp + (1)*main_sub24_CAST_div25_float + (-1)*C3_main_sub24_CAST_div25<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub24_CAST_div25
solver.Add( + (1)*main_sub24_float + (1)*main_sub24_CAST_div25_fixp + (-1)*C4_main_sub24_CAST_div25<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub24_CAST_div25
solver.Add( + (1)*main_sub24_fixp + (1)*main_sub24_CAST_div25_double + (-1)*C5_main_sub24_CAST_div25<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub24_CAST_div25
solver.Add( + (1)*main_sub24_double + (1)*main_sub24_CAST_div25_fixp + (-1)*C6_main_sub24_CAST_div25<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub24_CAST_div25
solver.Add( + (1)*main_sub24_float + (1)*main_sub24_CAST_div25_double + (-1)*C7_main_sub24_CAST_div25<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub24_CAST_div25
solver.Add( + (1)*main_sub24_double + (1)*main_sub24_CAST_div25_float + (-1)*C8_main_sub24_CAST_div25<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub24_CAST_div25



#Stuff for double 2.000000e+00
ConstantValue__23_fixbits = solver.IntVar(0, 30, 'ConstantValue__23_fixbits')
ConstantValue__23_fixp = solver.IntVar(0, 1, 'ConstantValue__23_fixp')
ConstantValue__23_float = solver.IntVar(0, 1, 'ConstantValue__23_float')
ConstantValue__23_double = solver.IntVar(0, 1, 'ConstantValue__23_double')
ConstantValue__23_enob = solver.IntVar(-10000, 10000, 'ConstantValue__23_enob')
solver.Add( + (1)*ConstantValue__23_enob + (-1)*ConstantValue__23_fixbits + (10000)*ConstantValue__23_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__23_enob + (10000)*ConstantValue__23_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__23_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_float + (1)*ConstantValue__23_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__23_fixbits + (-10000)*ConstantValue__23_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %div25 = fdiv double %sub24, 2.000000e+00, !taffo.info !82, !taffo.initweight !45, !taffo.constinfo !79
ConstantValue__23_CAST_div25_fixbits = solver.IntVar(0, 30, 'ConstantValue__23_CAST_div25_fixbits')
ConstantValue__23_CAST_div25_fixp = solver.IntVar(0, 1, 'ConstantValue__23_CAST_div25_fixp')
ConstantValue__23_CAST_div25_float = solver.IntVar(0, 1, 'ConstantValue__23_CAST_div25_float')
ConstantValue__23_CAST_div25_double = solver.IntVar(0, 1, 'ConstantValue__23_CAST_div25_double')
solver.Add( + (1)*ConstantValue__23_CAST_div25_fixp + (1)*ConstantValue__23_CAST_div25_float + (1)*ConstantValue__23_CAST_div25_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__23_CAST_div25_fixbits + (-10000)*ConstantValue__23_CAST_div25_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C1_ConstantValue__23_CAST_div25')
C2_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C2_ConstantValue__23_CAST_div25')
solver.Add( + (1)*ConstantValue__23_fixbits + (-1)*ConstantValue__23_CAST_div25_fixbits + (-10000)*C1_ConstantValue__23_CAST_div25<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__23_fixbits + (1)*ConstantValue__23_CAST_div25_fixbits + (-10000)*C2_ConstantValue__23_CAST_div25<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__23_CAST_div25
castCostObj +=  + (1)*C2_ConstantValue__23_CAST_div25
C3_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C3_ConstantValue__23_CAST_div25')
C4_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C4_ConstantValue__23_CAST_div25')
C5_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C5_ConstantValue__23_CAST_div25')
C6_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C6_ConstantValue__23_CAST_div25')
C7_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C7_ConstantValue__23_CAST_div25')
C8_ConstantValue__23_CAST_div25 = solver.IntVar(0, 1, 'C8_ConstantValue__23_CAST_div25')
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_CAST_div25_float + (-1)*C3_ConstantValue__23_CAST_div25<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__23_CAST_div25
solver.Add( + (1)*ConstantValue__23_float + (1)*ConstantValue__23_CAST_div25_fixp + (-1)*C4_ConstantValue__23_CAST_div25<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__23_CAST_div25
solver.Add( + (1)*ConstantValue__23_fixp + (1)*ConstantValue__23_CAST_div25_double + (-1)*C5_ConstantValue__23_CAST_div25<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__23_CAST_div25
solver.Add( + (1)*ConstantValue__23_double + (1)*ConstantValue__23_CAST_div25_fixp + (-1)*C6_ConstantValue__23_CAST_div25<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__23_CAST_div25
solver.Add( + (1)*ConstantValue__23_float + (1)*ConstantValue__23_CAST_div25_double + (-1)*C7_ConstantValue__23_CAST_div25<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__23_CAST_div25
solver.Add( + (1)*ConstantValue__23_double + (1)*ConstantValue__23_CAST_div25_float + (-1)*C8_ConstantValue__23_CAST_div25<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__23_CAST_div25



#Stuff for   %div25 = fdiv double %sub24, 2.000000e+00, !taffo.info !82, !taffo.initweight !45, !taffo.constinfo !79
main_div25_fixbits = solver.IntVar(0, 23, 'main_div25_fixbits')
main_div25_fixp = solver.IntVar(0, 1, 'main_div25_fixp')
main_div25_float = solver.IntVar(0, 1, 'main_div25_float')
main_div25_double = solver.IntVar(0, 1, 'main_div25_double')
main_div25_enob = solver.IntVar(-10000, 10000, 'main_div25_enob')
solver.Add( + (1)*main_div25_enob + (-1)*main_div25_fixbits + (10000)*main_div25_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div25_enob + (10000)*main_div25_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div25_enob + (10000)*main_div25_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div25_fixbits + (-10000)*main_div25_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_div25_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div25_enob
solver.Add( + (1)*main_div25_fixp + (1)*main_div25_float + (1)*main_div25_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div25_fixbits + (-10000)*main_div25_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub24_CAST_div25_fixp + (-1)*ConstantValue__23_CAST_div25_fixp==0)    #fix equality
solver.Add( + (1)*main_sub24_CAST_div25_float + (-1)*ConstantValue__23_CAST_div25_float==0)    #float equality
solver.Add( + (1)*main_sub24_CAST_div25_double + (-1)*ConstantValue__23_CAST_div25_double==0)    #double equality
solver.Add( + (1)*main_sub24_CAST_div25_fixp + (-1)*main_div25_fixp==0)    #fix equality
solver.Add( + (1)*main_sub24_CAST_div25_float + (-1)*main_div25_float==0)    #float equality
solver.Add( + (1)*main_sub24_CAST_div25_double + (-1)*main_div25_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div25_fixp
mathCostObj +=  + (6)*main_div25_float
mathCostObj +=  + (12)*main_div25_double
main_main_div25_enob_1 = solver.IntVar(0, 1, 'main_main_div25_enob_1')
main_main_div25_enob_2 = solver.IntVar(0, 1, 'main_main_div25_enob_2')
solver.Add( + (1)*main_main_div25_enob_1 + (1)*main_main_div25_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div25_enob + (-1)*ConstantValue__21_enob + (-10000)*main_main_div25_enob_1<=3072)    #Enob: propagation in division 1
solver.Add( + (1)*main_div25_enob + (-1)*main_sub24_enob + (-10000)*main_main_div25_enob_2<=3072)    #Enob: propagation in division 2



#Constraint for cast for   store double %div25, double* @d, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
main_div25_CAST_store_fixbits = solver.IntVar(0, 23, 'main_div25_CAST_store_fixbits')
main_div25_CAST_store_fixp = solver.IntVar(0, 1, 'main_div25_CAST_store_fixp')
main_div25_CAST_store_float = solver.IntVar(0, 1, 'main_div25_CAST_store_float')
main_div25_CAST_store_double = solver.IntVar(0, 1, 'main_div25_CAST_store_double')
solver.Add( + (1)*main_div25_CAST_store_fixp + (1)*main_div25_CAST_store_float + (1)*main_div25_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div25_CAST_store_fixbits + (-10000)*main_div25_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div25_CAST_store = solver.IntVar(0, 1, 'C1_main_div25_CAST_store')
C2_main_div25_CAST_store = solver.IntVar(0, 1, 'C2_main_div25_CAST_store')
solver.Add( + (1)*main_div25_fixbits + (-1)*main_div25_CAST_store_fixbits + (-10000)*C1_main_div25_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div25_fixbits + (1)*main_div25_CAST_store_fixbits + (-10000)*C2_main_div25_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div25_CAST_store
castCostObj +=  + (1)*C2_main_div25_CAST_store
C3_main_div25_CAST_store = solver.IntVar(0, 1, 'C3_main_div25_CAST_store')
C4_main_div25_CAST_store = solver.IntVar(0, 1, 'C4_main_div25_CAST_store')
C5_main_div25_CAST_store = solver.IntVar(0, 1, 'C5_main_div25_CAST_store')
C6_main_div25_CAST_store = solver.IntVar(0, 1, 'C6_main_div25_CAST_store')
C7_main_div25_CAST_store = solver.IntVar(0, 1, 'C7_main_div25_CAST_store')
C8_main_div25_CAST_store = solver.IntVar(0, 1, 'C8_main_div25_CAST_store')
solver.Add( + (1)*main_div25_fixp + (1)*main_div25_CAST_store_float + (-1)*C3_main_div25_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div25_CAST_store
solver.Add( + (1)*main_div25_float + (1)*main_div25_CAST_store_fixp + (-1)*C4_main_div25_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div25_CAST_store
solver.Add( + (1)*main_div25_fixp + (1)*main_div25_CAST_store_double + (-1)*C5_main_div25_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div25_CAST_store
solver.Add( + (1)*main_div25_double + (1)*main_div25_CAST_store_fixp + (-1)*C6_main_div25_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div25_CAST_store
solver.Add( + (1)*main_div25_float + (1)*main_div25_CAST_store_double + (-1)*C7_main_div25_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div25_CAST_store
solver.Add( + (1)*main_div25_double + (1)*main_div25_CAST_store_float + (-1)*C8_main_div25_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div25_CAST_store
solver.Add( + (1)*d_fixp + (-1)*main_div25_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*d_float + (-1)*main_div25_CAST_store_float==0)    #float equality
solver.Add( + (1)*d_double + (-1)*main_div25_CAST_store_double==0)    #double equality
solver.Add( + (1)*d_fixbits + (-1)*main_div25_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
d_enob_storeENOB = solver.IntVar(-10000, 10000, 'd_enob_storeENOB')
solver.Add( + (1)*d_enob_storeENOB + (-1)*d_fixbits + (10000)*d_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*d_enob_storeENOB + (10000)*d_float<=10149)    #Enob constraint for float
solver.Add( + (1)*d_enob_storeENOB + (10000)*d_double<=11074)    #Enob constraint for double
solver.Add( + (1)*d_enob_storeENOB + (-1)*main_div25_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
mul2_enob_memphi_main_tmp12 = solver.IntVar(-10000, 10000, 'mul2_enob_memphi_main_tmp12')
solver.Add( + (1)*mul2_enob_memphi_main_tmp12 + (-1)*mul2_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp12_enob_0 = solver.IntVar(0, 1, 'main_main_tmp12_enob_0')
solver.Add( + (1)*main_main_tmp12_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*mul2_enob_memphi_main_tmp12 + (-1)*mul2_enob_storeENOB + (10000)*main_main_tmp12_enob_0<=10000)    #Enob: forcing MEM phi enob



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
solver.Add( + (1)*ConstantValue__24_double<=0)    #Disable double data type
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
solver.Add( + (1)*ConstantValue__25_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__25_fixp + (1)*ConstantValue__25_float + (1)*ConstantValue__25_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__25_fixbits + (-10000)*ConstantValue__25_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__26_fixbits = solver.IntVar(0, 31, 'ConstantValue__26_fixbits')
ConstantValue__26_fixp = solver.IntVar(0, 1, 'ConstantValue__26_fixp')
ConstantValue__26_float = solver.IntVar(0, 1, 'ConstantValue__26_float')
ConstantValue__26_double = solver.IntVar(0, 1, 'ConstantValue__26_double')
ConstantValue__26_enob = solver.IntVar(-10000, 10000, 'ConstantValue__26_enob')
solver.Add( + (1)*ConstantValue__26_enob + (-1)*ConstantValue__26_fixbits + (10000)*ConstantValue__26_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__26_enob + (10000)*ConstantValue__26_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__26_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__26_fixp + (1)*ConstantValue__26_float + (1)*ConstantValue__26_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__26_fixbits + (-10000)*ConstantValue__26_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add26 = fadd double 1.000000e+00, %tmp12, !taffo.info !84, !taffo.initweight !44, !taffo.constinfo !66
ConstantValue__26_CAST_add26_fixbits = solver.IntVar(0, 31, 'ConstantValue__26_CAST_add26_fixbits')
ConstantValue__26_CAST_add26_fixp = solver.IntVar(0, 1, 'ConstantValue__26_CAST_add26_fixp')
ConstantValue__26_CAST_add26_float = solver.IntVar(0, 1, 'ConstantValue__26_CAST_add26_float')
ConstantValue__26_CAST_add26_double = solver.IntVar(0, 1, 'ConstantValue__26_CAST_add26_double')
solver.Add( + (1)*ConstantValue__26_CAST_add26_fixp + (1)*ConstantValue__26_CAST_add26_float + (1)*ConstantValue__26_CAST_add26_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__26_CAST_add26_fixbits + (-10000)*ConstantValue__26_CAST_add26_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C1_ConstantValue__26_CAST_add26')
C2_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C2_ConstantValue__26_CAST_add26')
solver.Add( + (1)*ConstantValue__26_fixbits + (-1)*ConstantValue__26_CAST_add26_fixbits + (-10000)*C1_ConstantValue__26_CAST_add26<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__26_fixbits + (1)*ConstantValue__26_CAST_add26_fixbits + (-10000)*C2_ConstantValue__26_CAST_add26<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__26_CAST_add26
castCostObj +=  + (1)*C2_ConstantValue__26_CAST_add26
C3_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C3_ConstantValue__26_CAST_add26')
C4_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C4_ConstantValue__26_CAST_add26')
C5_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C5_ConstantValue__26_CAST_add26')
C6_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C6_ConstantValue__26_CAST_add26')
C7_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C7_ConstantValue__26_CAST_add26')
C8_ConstantValue__26_CAST_add26 = solver.IntVar(0, 1, 'C8_ConstantValue__26_CAST_add26')
solver.Add( + (1)*ConstantValue__26_fixp + (1)*ConstantValue__26_CAST_add26_float + (-1)*C3_ConstantValue__26_CAST_add26<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__26_CAST_add26
solver.Add( + (1)*ConstantValue__26_float + (1)*ConstantValue__26_CAST_add26_fixp + (-1)*C4_ConstantValue__26_CAST_add26<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__26_CAST_add26
solver.Add( + (1)*ConstantValue__26_fixp + (1)*ConstantValue__26_CAST_add26_double + (-1)*C5_ConstantValue__26_CAST_add26<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__26_CAST_add26
solver.Add( + (1)*ConstantValue__26_double + (1)*ConstantValue__26_CAST_add26_fixp + (-1)*C6_ConstantValue__26_CAST_add26<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__26_CAST_add26
solver.Add( + (1)*ConstantValue__26_float + (1)*ConstantValue__26_CAST_add26_double + (-1)*C7_ConstantValue__26_CAST_add26<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__26_CAST_add26
solver.Add( + (1)*ConstantValue__26_double + (1)*ConstantValue__26_CAST_add26_float + (-1)*C8_ConstantValue__26_CAST_add26<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__26_CAST_add26



#Constraint for cast for   %add26 = fadd double 1.000000e+00, %tmp12, !taffo.info !84, !taffo.initweight !44, !taffo.constinfo !66
mul2_CAST_add26_fixbits = solver.IntVar(0, 23, 'mul2_CAST_add26_fixbits')
mul2_CAST_add26_fixp = solver.IntVar(0, 1, 'mul2_CAST_add26_fixp')
mul2_CAST_add26_float = solver.IntVar(0, 1, 'mul2_CAST_add26_float')
mul2_CAST_add26_double = solver.IntVar(0, 1, 'mul2_CAST_add26_double')
solver.Add( + (1)*mul2_CAST_add26_fixp + (1)*mul2_CAST_add26_float + (1)*mul2_CAST_add26_double==1)    #exactly 1 type
solver.Add( + (1)*mul2_CAST_add26_fixbits + (-10000)*mul2_CAST_add26_fixp<=0)    #If no fix, fix frac part = 0
C1_mul2_CAST_add26 = solver.IntVar(0, 1, 'C1_mul2_CAST_add26')
C2_mul2_CAST_add26 = solver.IntVar(0, 1, 'C2_mul2_CAST_add26')
solver.Add( + (1)*mul2_fixbits + (-1)*mul2_CAST_add26_fixbits + (-10000)*C1_mul2_CAST_add26<=0)    #Shift cost 1
solver.Add( + (-1)*mul2_fixbits + (1)*mul2_CAST_add26_fixbits + (-10000)*C2_mul2_CAST_add26<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_mul2_CAST_add26
castCostObj +=  + (1)*C2_mul2_CAST_add26
C3_mul2_CAST_add26 = solver.IntVar(0, 1, 'C3_mul2_CAST_add26')
C4_mul2_CAST_add26 = solver.IntVar(0, 1, 'C4_mul2_CAST_add26')
C5_mul2_CAST_add26 = solver.IntVar(0, 1, 'C5_mul2_CAST_add26')
C6_mul2_CAST_add26 = solver.IntVar(0, 1, 'C6_mul2_CAST_add26')
C7_mul2_CAST_add26 = solver.IntVar(0, 1, 'C7_mul2_CAST_add26')
C8_mul2_CAST_add26 = solver.IntVar(0, 1, 'C8_mul2_CAST_add26')
solver.Add( + (1)*mul2_fixp + (1)*mul2_CAST_add26_float + (-1)*C3_mul2_CAST_add26<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_mul2_CAST_add26
solver.Add( + (1)*mul2_float + (1)*mul2_CAST_add26_fixp + (-1)*C4_mul2_CAST_add26<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_mul2_CAST_add26
solver.Add( + (1)*mul2_fixp + (1)*mul2_CAST_add26_double + (-1)*C5_mul2_CAST_add26<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_mul2_CAST_add26
solver.Add( + (1)*mul2_double + (1)*mul2_CAST_add26_fixp + (-1)*C6_mul2_CAST_add26<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_mul2_CAST_add26
solver.Add( + (1)*mul2_float + (1)*mul2_CAST_add26_double + (-1)*C7_mul2_CAST_add26<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_mul2_CAST_add26
solver.Add( + (1)*mul2_double + (1)*mul2_CAST_add26_float + (-1)*C8_mul2_CAST_add26<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_mul2_CAST_add26



#Stuff for   %add26 = fadd double 1.000000e+00, %tmp12, !taffo.info !84, !taffo.initweight !44, !taffo.constinfo !66
main_add26_fixbits = solver.IntVar(0, 23, 'main_add26_fixbits')
main_add26_fixp = solver.IntVar(0, 1, 'main_add26_fixp')
main_add26_float = solver.IntVar(0, 1, 'main_add26_float')
main_add26_double = solver.IntVar(0, 1, 'main_add26_double')
main_add26_enob = solver.IntVar(-10000, 10000, 'main_add26_enob')
solver.Add( + (1)*main_add26_enob + (-1)*main_add26_fixbits + (10000)*main_add26_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add26_enob + (10000)*main_add26_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_add26_enob + (10000)*main_add26_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_add26_fixbits + (-10000)*main_add26_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_add26_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add26_enob
solver.Add( + (1)*main_add26_fixp + (1)*main_add26_float + (1)*main_add26_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add26_fixbits + (-10000)*main_add26_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__26_CAST_add26_fixp + (-1)*mul2_CAST_add26_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__26_CAST_add26_float + (-1)*mul2_CAST_add26_float==0)    #float equality
solver.Add( + (1)*ConstantValue__26_CAST_add26_double + (-1)*mul2_CAST_add26_double==0)    #double equality
solver.Add( + (1)*ConstantValue__26_CAST_add26_fixbits + (-1)*mul2_CAST_add26_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__26_CAST_add26_fixp + (-1)*main_add26_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__26_CAST_add26_float + (-1)*main_add26_float==0)    #float equality
solver.Add( + (1)*ConstantValue__26_CAST_add26_double + (-1)*main_add26_double==0)    #double equality
solver.Add( + (1)*ConstantValue__26_CAST_add26_fixbits + (-1)*main_add26_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add26_fixp
mathCostObj +=  + (3)*main_add26_float
mathCostObj +=  + (6.64928)*main_add26_double
solver.Add( + (1)*main_add26_enob + (-1)*ConstantValue__24_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add26_enob + (-1)*mul2_enob_memphi_main_tmp12<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add26, double* @e, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
main_add26_CAST_store_fixbits = solver.IntVar(0, 23, 'main_add26_CAST_store_fixbits')
main_add26_CAST_store_fixp = solver.IntVar(0, 1, 'main_add26_CAST_store_fixp')
main_add26_CAST_store_float = solver.IntVar(0, 1, 'main_add26_CAST_store_float')
main_add26_CAST_store_double = solver.IntVar(0, 1, 'main_add26_CAST_store_double')
solver.Add( + (1)*main_add26_CAST_store_fixp + (1)*main_add26_CAST_store_float + (1)*main_add26_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add26_CAST_store_fixbits + (-10000)*main_add26_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add26_CAST_store = solver.IntVar(0, 1, 'C1_main_add26_CAST_store')
C2_main_add26_CAST_store = solver.IntVar(0, 1, 'C2_main_add26_CAST_store')
solver.Add( + (1)*main_add26_fixbits + (-1)*main_add26_CAST_store_fixbits + (-10000)*C1_main_add26_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add26_fixbits + (1)*main_add26_CAST_store_fixbits + (-10000)*C2_main_add26_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add26_CAST_store
castCostObj +=  + (1)*C2_main_add26_CAST_store
C3_main_add26_CAST_store = solver.IntVar(0, 1, 'C3_main_add26_CAST_store')
C4_main_add26_CAST_store = solver.IntVar(0, 1, 'C4_main_add26_CAST_store')
C5_main_add26_CAST_store = solver.IntVar(0, 1, 'C5_main_add26_CAST_store')
C6_main_add26_CAST_store = solver.IntVar(0, 1, 'C6_main_add26_CAST_store')
C7_main_add26_CAST_store = solver.IntVar(0, 1, 'C7_main_add26_CAST_store')
C8_main_add26_CAST_store = solver.IntVar(0, 1, 'C8_main_add26_CAST_store')
solver.Add( + (1)*main_add26_fixp + (1)*main_add26_CAST_store_float + (-1)*C3_main_add26_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add26_CAST_store
solver.Add( + (1)*main_add26_float + (1)*main_add26_CAST_store_fixp + (-1)*C4_main_add26_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add26_CAST_store
solver.Add( + (1)*main_add26_fixp + (1)*main_add26_CAST_store_double + (-1)*C5_main_add26_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add26_CAST_store
solver.Add( + (1)*main_add26_double + (1)*main_add26_CAST_store_fixp + (-1)*C6_main_add26_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add26_CAST_store
solver.Add( + (1)*main_add26_float + (1)*main_add26_CAST_store_double + (-1)*C7_main_add26_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add26_CAST_store
solver.Add( + (1)*main_add26_double + (1)*main_add26_CAST_store_float + (-1)*C8_main_add26_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add26_CAST_store
solver.Add( + (1)*e_fixp + (-1)*main_add26_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*e_float + (-1)*main_add26_CAST_store_float==0)    #float equality
solver.Add( + (1)*e_double + (-1)*main_add26_CAST_store_double==0)    #double equality
solver.Add( + (1)*e_fixbits + (-1)*main_add26_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
e_enob_storeENOB = solver.IntVar(-10000, 10000, 'e_enob_storeENOB')
solver.Add( + (1)*e_enob_storeENOB + (-1)*e_fixbits + (10000)*e_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*e_enob_storeENOB + (10000)*e_float<=10149)    #Enob constraint for float
solver.Add( + (1)*e_enob_storeENOB + (10000)*e_double<=11074)    #Enob constraint for double
solver.Add( + (1)*e_enob_storeENOB + (-1)*main_add26_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
d_enob_memphi_main_tmp13 = solver.IntVar(-10000, 10000, 'd_enob_memphi_main_tmp13')
solver.Add( + (1)*d_enob_memphi_main_tmp13 + (-1)*d_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp13_enob_0 = solver.IntVar(0, 1, 'main_main_tmp13_enob_0')
solver.Add( + (1)*main_main_tmp13_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*d_enob_memphi_main_tmp13 + (-1)*d_enob_storeENOB + (10000)*main_main_tmp13_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   store double %tmp13, double* @f, align 8, !taffo.info !56, !taffo.initweight !41, !taffo.constinfo !48
d_CAST_store_fixbits = solver.IntVar(0, 23, 'd_CAST_store_fixbits')
d_CAST_store_fixp = solver.IntVar(0, 1, 'd_CAST_store_fixp')
d_CAST_store_float = solver.IntVar(0, 1, 'd_CAST_store_float')
d_CAST_store_double = solver.IntVar(0, 1, 'd_CAST_store_double')
solver.Add( + (1)*d_CAST_store_fixp + (1)*d_CAST_store_float + (1)*d_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*d_CAST_store_fixbits + (-10000)*d_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_d_CAST_store = solver.IntVar(0, 1, 'C1_d_CAST_store')
C2_d_CAST_store = solver.IntVar(0, 1, 'C2_d_CAST_store')
solver.Add( + (1)*d_fixbits + (-1)*d_CAST_store_fixbits + (-10000)*C1_d_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*d_fixbits + (1)*d_CAST_store_fixbits + (-10000)*C2_d_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_d_CAST_store
castCostObj +=  + (1)*C2_d_CAST_store
C3_d_CAST_store = solver.IntVar(0, 1, 'C3_d_CAST_store')
C4_d_CAST_store = solver.IntVar(0, 1, 'C4_d_CAST_store')
C5_d_CAST_store = solver.IntVar(0, 1, 'C5_d_CAST_store')
C6_d_CAST_store = solver.IntVar(0, 1, 'C6_d_CAST_store')
C7_d_CAST_store = solver.IntVar(0, 1, 'C7_d_CAST_store')
C8_d_CAST_store = solver.IntVar(0, 1, 'C8_d_CAST_store')
solver.Add( + (1)*d_fixp + (1)*d_CAST_store_float + (-1)*C3_d_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_d_CAST_store
solver.Add( + (1)*d_float + (1)*d_CAST_store_fixp + (-1)*C4_d_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_d_CAST_store
solver.Add( + (1)*d_fixp + (1)*d_CAST_store_double + (-1)*C5_d_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_d_CAST_store
solver.Add( + (1)*d_double + (1)*d_CAST_store_fixp + (-1)*C6_d_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_d_CAST_store
solver.Add( + (1)*d_float + (1)*d_CAST_store_double + (-1)*C7_d_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_d_CAST_store
solver.Add( + (1)*d_double + (1)*d_CAST_store_float + (-1)*C8_d_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_d_CAST_store
solver.Add( + (1)*f_fixp + (-1)*d_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*f_float + (-1)*d_CAST_store_float==0)    #float equality
solver.Add( + (1)*f_double + (-1)*d_CAST_store_double==0)    #double equality
solver.Add( + (1)*f_fixbits + (-1)*d_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
f_enob_storeENOB = solver.IntVar(-10000, 10000, 'f_enob_storeENOB')
solver.Add( + (1)*f_enob_storeENOB + (-1)*f_fixbits + (10000)*f_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*f_enob_storeENOB + (10000)*f_float<=10149)    #Enob constraint for float
solver.Add( + (1)*f_enob_storeENOB + (10000)*f_double<=11074)    #Enob constraint for double
solver.Add( + (1)*f_enob_storeENOB + (-1)*d_enob_memphi_main_tmp13<=0)    #Enob constraint ENOB propagation in load/store



#Stuff for double 1.000000e+00
ConstantValue__27_fixbits = solver.IntVar(0, 31, 'ConstantValue__27_fixbits')
ConstantValue__27_fixp = solver.IntVar(0, 1, 'ConstantValue__27_fixp')
ConstantValue__27_float = solver.IntVar(0, 1, 'ConstantValue__27_float')
ConstantValue__27_double = solver.IntVar(0, 1, 'ConstantValue__27_double')
ConstantValue__27_enob = solver.IntVar(-10000, 10000, 'ConstantValue__27_enob')
solver.Add( + (1)*ConstantValue__27_enob + (-1)*ConstantValue__27_fixbits + (10000)*ConstantValue__27_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__27_enob + (10000)*ConstantValue__27_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__27_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__27_fixp + (1)*ConstantValue__27_float + (1)*ConstantValue__27_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__27_fixbits + (-10000)*ConstantValue__27_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__28_fixbits = solver.IntVar(0, 31, 'ConstantValue__28_fixbits')
ConstantValue__28_fixp = solver.IntVar(0, 1, 'ConstantValue__28_fixp')
ConstantValue__28_float = solver.IntVar(0, 1, 'ConstantValue__28_float')
ConstantValue__28_double = solver.IntVar(0, 1, 'ConstantValue__28_double')
ConstantValue__28_enob = solver.IntVar(-10000, 10000, 'ConstantValue__28_enob')
solver.Add( + (1)*ConstantValue__28_enob + (-1)*ConstantValue__28_fixbits + (10000)*ConstantValue__28_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__28_enob + (10000)*ConstantValue__28_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__28_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_float + (1)*ConstantValue__28_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__28_fixbits + (-10000)*ConstantValue__28_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx37, align 8, !taffo.info !35, !taffo.initweight !45, !taffo.constinfo !66
ConstantValue__28_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__28_CAST_store_fixbits')
ConstantValue__28_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__28_CAST_store_fixp')
ConstantValue__28_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__28_CAST_store_float')
ConstantValue__28_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__28_CAST_store_double')
solver.Add( + (1)*ConstantValue__28_CAST_store_fixp + (1)*ConstantValue__28_CAST_store_float + (1)*ConstantValue__28_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__28_CAST_store_fixbits + (-10000)*ConstantValue__28_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__28_CAST_store')
C2_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__28_CAST_store')
solver.Add( + (1)*ConstantValue__28_fixbits + (-1)*ConstantValue__28_CAST_store_fixbits + (-10000)*C1_ConstantValue__28_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__28_fixbits + (1)*ConstantValue__28_CAST_store_fixbits + (-10000)*C2_ConstantValue__28_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__28_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__28_CAST_store
C3_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__28_CAST_store')
C4_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__28_CAST_store')
C5_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__28_CAST_store')
C6_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__28_CAST_store')
C7_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__28_CAST_store')
C8_ConstantValue__28_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__28_CAST_store')
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_CAST_store_float + (-1)*C3_ConstantValue__28_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__28_CAST_store
solver.Add( + (1)*ConstantValue__28_float + (1)*ConstantValue__28_CAST_store_fixp + (-1)*C4_ConstantValue__28_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__28_CAST_store
solver.Add( + (1)*ConstantValue__28_fixp + (1)*ConstantValue__28_CAST_store_double + (-1)*C5_ConstantValue__28_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__28_CAST_store
solver.Add( + (1)*ConstantValue__28_double + (1)*ConstantValue__28_CAST_store_fixp + (-1)*C6_ConstantValue__28_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__28_CAST_store
solver.Add( + (1)*ConstantValue__28_float + (1)*ConstantValue__28_CAST_store_double + (-1)*C7_ConstantValue__28_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__28_CAST_store
solver.Add( + (1)*ConstantValue__28_double + (1)*ConstantValue__28_CAST_store_float + (-1)*C8_ConstantValue__28_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__28_CAST_store
solver.Add( + (1)*main_v_fixp + (-1)*ConstantValue__28_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_v_float + (-1)*ConstantValue__28_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_v_double + (-1)*ConstantValue__28_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_v_fixbits + (-1)*ConstantValue__28_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 0.000000e+00
ConstantValue__29_fixbits = solver.IntVar(0, 32, 'ConstantValue__29_fixbits')
ConstantValue__29_fixp = solver.IntVar(0, 1, 'ConstantValue__29_fixp')
ConstantValue__29_float = solver.IntVar(0, 1, 'ConstantValue__29_float')
ConstantValue__29_double = solver.IntVar(0, 1, 'ConstantValue__29_double')
ConstantValue__29_enob = solver.IntVar(-10000, 10000, 'ConstantValue__29_enob')
solver.Add( + (1)*ConstantValue__29_enob + (-1)*ConstantValue__29_fixbits + (10000)*ConstantValue__29_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__29_enob + (10000)*ConstantValue__29_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__29_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__29_fixp + (1)*ConstantValue__29_float + (1)*ConstantValue__29_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__29_fixbits + (-10000)*ConstantValue__29_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 0.000000e+00
ConstantValue__30_fixbits = solver.IntVar(0, 32, 'ConstantValue__30_fixbits')
ConstantValue__30_fixp = solver.IntVar(0, 1, 'ConstantValue__30_fixp')
ConstantValue__30_float = solver.IntVar(0, 1, 'ConstantValue__30_float')
ConstantValue__30_double = solver.IntVar(0, 1, 'ConstantValue__30_double')
ConstantValue__30_enob = solver.IntVar(-10000, 10000, 'ConstantValue__30_enob')
solver.Add( + (1)*ConstantValue__30_enob + (-1)*ConstantValue__30_fixbits + (10000)*ConstantValue__30_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__30_enob + (10000)*ConstantValue__30_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__30_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__30_fixp + (1)*ConstantValue__30_float + (1)*ConstantValue__30_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__30_fixbits + (-10000)*ConstantValue__30_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx40, align 16, !taffo.info !37, !taffo.initweight !45, !taffo.constinfo !88
ConstantValue__30_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__30_CAST_store_fixbits')
ConstantValue__30_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__30_CAST_store_fixp')
ConstantValue__30_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__30_CAST_store_float')
ConstantValue__30_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__30_CAST_store_double')
solver.Add( + (1)*ConstantValue__30_CAST_store_fixp + (1)*ConstantValue__30_CAST_store_float + (1)*ConstantValue__30_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__30_CAST_store_fixbits + (-10000)*ConstantValue__30_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__30_CAST_store')
C2_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__30_CAST_store')
solver.Add( + (1)*ConstantValue__30_fixbits + (-1)*ConstantValue__30_CAST_store_fixbits + (-10000)*C1_ConstantValue__30_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__30_fixbits + (1)*ConstantValue__30_CAST_store_fixbits + (-10000)*C2_ConstantValue__30_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__30_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__30_CAST_store
C3_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__30_CAST_store')
C4_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__30_CAST_store')
C5_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__30_CAST_store')
C6_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__30_CAST_store')
C7_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__30_CAST_store')
C8_ConstantValue__30_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__30_CAST_store')
solver.Add( + (1)*ConstantValue__30_fixp + (1)*ConstantValue__30_CAST_store_float + (-1)*C3_ConstantValue__30_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__30_CAST_store
solver.Add( + (1)*ConstantValue__30_float + (1)*ConstantValue__30_CAST_store_fixp + (-1)*C4_ConstantValue__30_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__30_CAST_store
solver.Add( + (1)*ConstantValue__30_fixp + (1)*ConstantValue__30_CAST_store_double + (-1)*C5_ConstantValue__30_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__30_CAST_store
solver.Add( + (1)*ConstantValue__30_double + (1)*ConstantValue__30_CAST_store_fixp + (-1)*C6_ConstantValue__30_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__30_CAST_store
solver.Add( + (1)*ConstantValue__30_float + (1)*ConstantValue__30_CAST_store_double + (-1)*C7_ConstantValue__30_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__30_CAST_store
solver.Add( + (1)*ConstantValue__30_double + (1)*ConstantValue__30_CAST_store_float + (-1)*C8_ConstantValue__30_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__30_CAST_store
solver.Add( + (1)*main_p_fixp + (-1)*ConstantValue__30_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_p_float + (-1)*ConstantValue__30_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_p_double + (-1)*ConstantValue__30_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_p_fixbits + (-1)*ConstantValue__30_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_v_enob_memphi_main_tmp14 = solver.IntVar(-10000, 10000, 'main_v_enob_memphi_main_tmp14')
solver.Add( + (1)*main_v_enob_memphi_main_tmp14 + (-1)*main_v_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   store double %tmp14, double* %arrayidx46, align 16, !taffo.info !39, !taffo.initweight !45
main_v_CAST_store_fixbits = solver.IntVar(0, 29, 'main_v_CAST_store_fixbits')
main_v_CAST_store_fixp = solver.IntVar(0, 1, 'main_v_CAST_store_fixp')
main_v_CAST_store_float = solver.IntVar(0, 1, 'main_v_CAST_store_float')
main_v_CAST_store_double = solver.IntVar(0, 1, 'main_v_CAST_store_double')
solver.Add( + (1)*main_v_CAST_store_fixp + (1)*main_v_CAST_store_float + (1)*main_v_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_v_CAST_store_fixbits + (-10000)*main_v_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_v_CAST_store = solver.IntVar(0, 1, 'C1_main_v_CAST_store')
C2_main_v_CAST_store = solver.IntVar(0, 1, 'C2_main_v_CAST_store')
solver.Add( + (1)*main_v_fixbits + (-1)*main_v_CAST_store_fixbits + (-10000)*C1_main_v_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_v_fixbits + (1)*main_v_CAST_store_fixbits + (-10000)*C2_main_v_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_v_CAST_store
castCostObj +=  + (1)*C2_main_v_CAST_store
C3_main_v_CAST_store = solver.IntVar(0, 1, 'C3_main_v_CAST_store')
C4_main_v_CAST_store = solver.IntVar(0, 1, 'C4_main_v_CAST_store')
C5_main_v_CAST_store = solver.IntVar(0, 1, 'C5_main_v_CAST_store')
C6_main_v_CAST_store = solver.IntVar(0, 1, 'C6_main_v_CAST_store')
C7_main_v_CAST_store = solver.IntVar(0, 1, 'C7_main_v_CAST_store')
C8_main_v_CAST_store = solver.IntVar(0, 1, 'C8_main_v_CAST_store')
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_store_float + (-1)*C3_main_v_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_v_CAST_store
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_store_fixp + (-1)*C4_main_v_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_v_CAST_store
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_store_double + (-1)*C5_main_v_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_v_CAST_store
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_store_fixp + (-1)*C6_main_v_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_v_CAST_store
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_store_double + (-1)*C7_main_v_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_v_CAST_store
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_store_float + (-1)*C8_main_v_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_v_CAST_store
solver.Add( + (1)*main_q_fixp + (-1)*main_v_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_q_float + (-1)*main_v_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_q_double + (-1)*main_v_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_q_fixbits + (-1)*main_v_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_q_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_q_enob_storeENOB')
solver.Add( + (1)*main_q_enob_storeENOB + (-1)*main_q_fixbits + (10000)*main_q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_q_enob_storeENOB + (10000)*main_q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_q_enob_storeENOB + (10000)*main_q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_q_enob_storeENOB + (-1)*main_v_enob_memphi_main_tmp14<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
c_enob_memphi_main_tmp15 = solver.IntVar(-10000, 10000, 'c_enob_memphi_main_tmp15')
solver.Add( + (1)*c_enob_memphi_main_tmp15 + (-1)*c_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp15_enob_0 = solver.IntVar(0, 1, 'main_main_tmp15_enob_0')
solver.Add( + (1)*main_main_tmp15_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*c_enob_memphi_main_tmp15 + (-1)*c_enob_storeENOB + (10000)*main_main_tmp15_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double -0.000000e+00
ConstantValue__31_fixbits = solver.IntVar(0, 32, 'ConstantValue__31_fixbits')
ConstantValue__31_fixp = solver.IntVar(0, 1, 'ConstantValue__31_fixp')
ConstantValue__31_float = solver.IntVar(0, 1, 'ConstantValue__31_float')
ConstantValue__31_double = solver.IntVar(0, 1, 'ConstantValue__31_double')
ConstantValue__31_enob = solver.IntVar(-10000, 10000, 'ConstantValue__31_enob')
solver.Add( + (1)*ConstantValue__31_enob + (-1)*ConstantValue__31_fixbits + (10000)*ConstantValue__31_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__31_enob + (10000)*ConstantValue__31_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__31_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__31_fixp + (1)*ConstantValue__31_float + (1)*ConstantValue__31_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__31_fixbits + (-10000)*ConstantValue__31_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__32_fixbits = solver.IntVar(0, 32, 'ConstantValue__32_fixbits')
ConstantValue__32_fixp = solver.IntVar(0, 1, 'ConstantValue__32_fixp')
ConstantValue__32_float = solver.IntVar(0, 1, 'ConstantValue__32_float')
ConstantValue__32_double = solver.IntVar(0, 1, 'ConstantValue__32_double')
ConstantValue__32_enob = solver.IntVar(-10000, 10000, 'ConstantValue__32_enob')
solver.Add( + (1)*ConstantValue__32_enob + (-1)*ConstantValue__32_fixbits + (10000)*ConstantValue__32_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__32_enob + (10000)*ConstantValue__32_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__32_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__32_fixp + (1)*ConstantValue__32_float + (1)*ConstantValue__32_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__32_fixbits + (-10000)*ConstantValue__32_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__33_fixbits = solver.IntVar(0, 32, 'ConstantValue__33_fixbits')
ConstantValue__33_fixp = solver.IntVar(0, 1, 'ConstantValue__33_fixp')
ConstantValue__33_float = solver.IntVar(0, 1, 'ConstantValue__33_float')
ConstantValue__33_double = solver.IntVar(0, 1, 'ConstantValue__33_double')
ConstantValue__33_enob = solver.IntVar(-10000, 10000, 'ConstantValue__33_enob')
solver.Add( + (1)*ConstantValue__33_enob + (-1)*ConstantValue__33_fixbits + (10000)*ConstantValue__33_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__33_enob + (10000)*ConstantValue__33_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__33_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_float + (1)*ConstantValue__33_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__33_fixbits + (-10000)*ConstantValue__33_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub51 = fsub double -0.000000e+00, %tmp15, !taffo.info !90, !taffo.initweight !44, !taffo.constinfo !74
ConstantValue__33_CAST_sub51_fixbits = solver.IntVar(0, 32, 'ConstantValue__33_CAST_sub51_fixbits')
ConstantValue__33_CAST_sub51_fixp = solver.IntVar(0, 1, 'ConstantValue__33_CAST_sub51_fixp')
ConstantValue__33_CAST_sub51_float = solver.IntVar(0, 1, 'ConstantValue__33_CAST_sub51_float')
ConstantValue__33_CAST_sub51_double = solver.IntVar(0, 1, 'ConstantValue__33_CAST_sub51_double')
solver.Add( + (1)*ConstantValue__33_CAST_sub51_fixp + (1)*ConstantValue__33_CAST_sub51_float + (1)*ConstantValue__33_CAST_sub51_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__33_CAST_sub51_fixbits + (-10000)*ConstantValue__33_CAST_sub51_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C1_ConstantValue__33_CAST_sub51')
C2_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C2_ConstantValue__33_CAST_sub51')
solver.Add( + (1)*ConstantValue__33_fixbits + (-1)*ConstantValue__33_CAST_sub51_fixbits + (-10000)*C1_ConstantValue__33_CAST_sub51<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__33_fixbits + (1)*ConstantValue__33_CAST_sub51_fixbits + (-10000)*C2_ConstantValue__33_CAST_sub51<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__33_CAST_sub51
castCostObj +=  + (1)*C2_ConstantValue__33_CAST_sub51
C3_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C3_ConstantValue__33_CAST_sub51')
C4_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C4_ConstantValue__33_CAST_sub51')
C5_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C5_ConstantValue__33_CAST_sub51')
C6_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C6_ConstantValue__33_CAST_sub51')
C7_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C7_ConstantValue__33_CAST_sub51')
C8_ConstantValue__33_CAST_sub51 = solver.IntVar(0, 1, 'C8_ConstantValue__33_CAST_sub51')
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_CAST_sub51_float + (-1)*C3_ConstantValue__33_CAST_sub51<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__33_CAST_sub51
solver.Add( + (1)*ConstantValue__33_float + (1)*ConstantValue__33_CAST_sub51_fixp + (-1)*C4_ConstantValue__33_CAST_sub51<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__33_CAST_sub51
solver.Add( + (1)*ConstantValue__33_fixp + (1)*ConstantValue__33_CAST_sub51_double + (-1)*C5_ConstantValue__33_CAST_sub51<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__33_CAST_sub51
solver.Add( + (1)*ConstantValue__33_double + (1)*ConstantValue__33_CAST_sub51_fixp + (-1)*C6_ConstantValue__33_CAST_sub51<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__33_CAST_sub51
solver.Add( + (1)*ConstantValue__33_float + (1)*ConstantValue__33_CAST_sub51_double + (-1)*C7_ConstantValue__33_CAST_sub51<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__33_CAST_sub51
solver.Add( + (1)*ConstantValue__33_double + (1)*ConstantValue__33_CAST_sub51_float + (-1)*C8_ConstantValue__33_CAST_sub51<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__33_CAST_sub51



#Constraint for cast for   %sub51 = fsub double -0.000000e+00, %tmp15, !taffo.info !90, !taffo.initweight !44, !taffo.constinfo !74
c_CAST_sub51_fixbits = solver.IntVar(0, 22, 'c_CAST_sub51_fixbits')
c_CAST_sub51_fixp = solver.IntVar(0, 1, 'c_CAST_sub51_fixp')
c_CAST_sub51_float = solver.IntVar(0, 1, 'c_CAST_sub51_float')
c_CAST_sub51_double = solver.IntVar(0, 1, 'c_CAST_sub51_double')
solver.Add( + (1)*c_CAST_sub51_fixp + (1)*c_CAST_sub51_float + (1)*c_CAST_sub51_double==1)    #exactly 1 type
solver.Add( + (1)*c_CAST_sub51_fixbits + (-10000)*c_CAST_sub51_fixp<=0)    #If no fix, fix frac part = 0
C1_c_CAST_sub51 = solver.IntVar(0, 1, 'C1_c_CAST_sub51')
C2_c_CAST_sub51 = solver.IntVar(0, 1, 'C2_c_CAST_sub51')
solver.Add( + (1)*c_fixbits + (-1)*c_CAST_sub51_fixbits + (-10000)*C1_c_CAST_sub51<=0)    #Shift cost 1
solver.Add( + (-1)*c_fixbits + (1)*c_CAST_sub51_fixbits + (-10000)*C2_c_CAST_sub51<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_c_CAST_sub51
castCostObj +=  + (1)*C2_c_CAST_sub51
C3_c_CAST_sub51 = solver.IntVar(0, 1, 'C3_c_CAST_sub51')
C4_c_CAST_sub51 = solver.IntVar(0, 1, 'C4_c_CAST_sub51')
C5_c_CAST_sub51 = solver.IntVar(0, 1, 'C5_c_CAST_sub51')
C6_c_CAST_sub51 = solver.IntVar(0, 1, 'C6_c_CAST_sub51')
C7_c_CAST_sub51 = solver.IntVar(0, 1, 'C7_c_CAST_sub51')
C8_c_CAST_sub51 = solver.IntVar(0, 1, 'C8_c_CAST_sub51')
solver.Add( + (1)*c_fixp + (1)*c_CAST_sub51_float + (-1)*C3_c_CAST_sub51<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_c_CAST_sub51
solver.Add( + (1)*c_float + (1)*c_CAST_sub51_fixp + (-1)*C4_c_CAST_sub51<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_c_CAST_sub51
solver.Add( + (1)*c_fixp + (1)*c_CAST_sub51_double + (-1)*C5_c_CAST_sub51<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_c_CAST_sub51
solver.Add( + (1)*c_double + (1)*c_CAST_sub51_fixp + (-1)*C6_c_CAST_sub51<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_c_CAST_sub51
solver.Add( + (1)*c_float + (1)*c_CAST_sub51_double + (-1)*C7_c_CAST_sub51<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_c_CAST_sub51
solver.Add( + (1)*c_double + (1)*c_CAST_sub51_float + (-1)*C8_c_CAST_sub51<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_c_CAST_sub51



#Stuff for   %sub51 = fsub double -0.000000e+00, %tmp15, !taffo.info !90, !taffo.initweight !44, !taffo.constinfo !74
main_sub51_fixbits = solver.IntVar(0, 23, 'main_sub51_fixbits')
main_sub51_fixp = solver.IntVar(0, 1, 'main_sub51_fixp')
main_sub51_float = solver.IntVar(0, 1, 'main_sub51_float')
main_sub51_double = solver.IntVar(0, 1, 'main_sub51_double')
main_sub51_enob = solver.IntVar(-10000, 10000, 'main_sub51_enob')
solver.Add( + (1)*main_sub51_enob + (-1)*main_sub51_fixbits + (10000)*main_sub51_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub51_enob + (10000)*main_sub51_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub51_enob + (10000)*main_sub51_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub51_fixbits + (-10000)*main_sub51_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_sub51_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub51_enob
solver.Add( + (1)*main_sub51_fixp + (1)*main_sub51_float + (1)*main_sub51_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub51_fixbits + (-10000)*main_sub51_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__33_CAST_sub51_fixp + (-1)*c_CAST_sub51_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__33_CAST_sub51_float + (-1)*c_CAST_sub51_float==0)    #float equality
solver.Add( + (1)*ConstantValue__33_CAST_sub51_double + (-1)*c_CAST_sub51_double==0)    #double equality
solver.Add( + (1)*ConstantValue__33_CAST_sub51_fixbits + (-1)*c_CAST_sub51_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__33_CAST_sub51_fixp + (-1)*main_sub51_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__33_CAST_sub51_float + (-1)*main_sub51_float==0)    #float equality
solver.Add( + (1)*ConstantValue__33_CAST_sub51_double + (-1)*main_sub51_double==0)    #double equality
solver.Add( + (1)*ConstantValue__33_CAST_sub51_fixbits + (-1)*main_sub51_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub51_fixp
mathCostObj +=  + (3)*main_sub51_float
mathCostObj +=  + (6.64928)*main_sub51_double
solver.Add( + (1)*main_sub51_enob + (-1)*ConstantValue__31_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub51_enob + (-1)*c_enob_memphi_main_tmp15<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp16 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp16')
solver.Add( + (1)*a_enob_memphi_main_tmp16 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp16_enob_0 = solver.IntVar(0, 1, 'main_main_tmp16_enob_0')
solver.Add( + (1)*main_main_tmp16_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp16 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp16_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_p_enob_memphi_main_tmp17 = solver.IntVar(-10000, 10000, 'main_p_enob_memphi_main_tmp17')
solver.Add( + (1)*main_p_enob_memphi_main_tmp17 + (-1)*main_p_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul57 = fmul double %tmp16, %tmp17, !taffo.info !92, !taffo.initweight !44
a_CAST_mul57_fixbits = solver.IntVar(0, 22, 'a_CAST_mul57_fixbits')
a_CAST_mul57_fixp = solver.IntVar(0, 1, 'a_CAST_mul57_fixp')
a_CAST_mul57_float = solver.IntVar(0, 1, 'a_CAST_mul57_float')
a_CAST_mul57_double = solver.IntVar(0, 1, 'a_CAST_mul57_double')
solver.Add( + (1)*a_CAST_mul57_fixp + (1)*a_CAST_mul57_float + (1)*a_CAST_mul57_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_mul57_fixbits + (-10000)*a_CAST_mul57_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_mul57 = solver.IntVar(0, 1, 'C1_a_CAST_mul57')
C2_a_CAST_mul57 = solver.IntVar(0, 1, 'C2_a_CAST_mul57')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_mul57_fixbits + (-10000)*C1_a_CAST_mul57<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_mul57_fixbits + (-10000)*C2_a_CAST_mul57<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_a_CAST_mul57
castCostObj +=  + (1)*C2_a_CAST_mul57
C3_a_CAST_mul57 = solver.IntVar(0, 1, 'C3_a_CAST_mul57')
C4_a_CAST_mul57 = solver.IntVar(0, 1, 'C4_a_CAST_mul57')
C5_a_CAST_mul57 = solver.IntVar(0, 1, 'C5_a_CAST_mul57')
C6_a_CAST_mul57 = solver.IntVar(0, 1, 'C6_a_CAST_mul57')
C7_a_CAST_mul57 = solver.IntVar(0, 1, 'C7_a_CAST_mul57')
C8_a_CAST_mul57 = solver.IntVar(0, 1, 'C8_a_CAST_mul57')
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul57_float + (-1)*C3_a_CAST_mul57<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_a_CAST_mul57
solver.Add( + (1)*a_float + (1)*a_CAST_mul57_fixp + (-1)*C4_a_CAST_mul57<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_a_CAST_mul57
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul57_double + (-1)*C5_a_CAST_mul57<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_a_CAST_mul57
solver.Add( + (1)*a_double + (1)*a_CAST_mul57_fixp + (-1)*C6_a_CAST_mul57<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_a_CAST_mul57
solver.Add( + (1)*a_float + (1)*a_CAST_mul57_double + (-1)*C7_a_CAST_mul57<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_a_CAST_mul57
solver.Add( + (1)*a_double + (1)*a_CAST_mul57_float + (-1)*C8_a_CAST_mul57<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_a_CAST_mul57



#Constraint for cast for   %mul57 = fmul double %tmp16, %tmp17, !taffo.info !92, !taffo.initweight !44
main_p_CAST_mul57_fixbits = solver.IntVar(0, 30, 'main_p_CAST_mul57_fixbits')
main_p_CAST_mul57_fixp = solver.IntVar(0, 1, 'main_p_CAST_mul57_fixp')
main_p_CAST_mul57_float = solver.IntVar(0, 1, 'main_p_CAST_mul57_float')
main_p_CAST_mul57_double = solver.IntVar(0, 1, 'main_p_CAST_mul57_double')
solver.Add( + (1)*main_p_CAST_mul57_fixp + (1)*main_p_CAST_mul57_float + (1)*main_p_CAST_mul57_double==1)    #exactly 1 type
solver.Add( + (1)*main_p_CAST_mul57_fixbits + (-10000)*main_p_CAST_mul57_fixp<=0)    #If no fix, fix frac part = 0
C1_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C1_main_p_CAST_mul57')
C2_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C2_main_p_CAST_mul57')
solver.Add( + (1)*main_p_fixbits + (-1)*main_p_CAST_mul57_fixbits + (-10000)*C1_main_p_CAST_mul57<=0)    #Shift cost 1
solver.Add( + (-1)*main_p_fixbits + (1)*main_p_CAST_mul57_fixbits + (-10000)*C2_main_p_CAST_mul57<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_p_CAST_mul57
castCostObj +=  + (1)*C2_main_p_CAST_mul57
C3_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C3_main_p_CAST_mul57')
C4_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C4_main_p_CAST_mul57')
C5_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C5_main_p_CAST_mul57')
C6_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C6_main_p_CAST_mul57')
C7_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C7_main_p_CAST_mul57')
C8_main_p_CAST_mul57 = solver.IntVar(0, 1, 'C8_main_p_CAST_mul57')
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul57_float + (-1)*C3_main_p_CAST_mul57<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_p_CAST_mul57
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul57_fixp + (-1)*C4_main_p_CAST_mul57<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_p_CAST_mul57
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul57_double + (-1)*C5_main_p_CAST_mul57<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_p_CAST_mul57
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul57_fixp + (-1)*C6_main_p_CAST_mul57<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_p_CAST_mul57
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul57_double + (-1)*C7_main_p_CAST_mul57<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_p_CAST_mul57
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul57_float + (-1)*C8_main_p_CAST_mul57<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_p_CAST_mul57



#Stuff for   %mul57 = fmul double %tmp16, %tmp17, !taffo.info !92, !taffo.initweight !44
main_mul57_fixbits = solver.IntVar(0, 22, 'main_mul57_fixbits')
main_mul57_fixp = solver.IntVar(0, 1, 'main_mul57_fixp')
main_mul57_float = solver.IntVar(0, 1, 'main_mul57_float')
main_mul57_double = solver.IntVar(0, 1, 'main_mul57_double')
main_mul57_enob = solver.IntVar(-10000, 10000, 'main_mul57_enob')
solver.Add( + (1)*main_mul57_enob + (-1)*main_mul57_fixbits + (10000)*main_mul57_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul57_enob + (10000)*main_mul57_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul57_enob + (10000)*main_mul57_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul57_fixbits + (-10000)*main_mul57_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_mul57_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul57_enob
solver.Add( + (1)*main_mul57_fixp + (1)*main_mul57_float + (1)*main_mul57_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul57_fixbits + (-10000)*main_mul57_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*a_CAST_mul57_fixp + (-1)*main_p_CAST_mul57_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_mul57_float + (-1)*main_p_CAST_mul57_float==0)    #float equality
solver.Add( + (1)*a_CAST_mul57_double + (-1)*main_p_CAST_mul57_double==0)    #double equality
solver.Add( + (1)*a_CAST_mul57_fixp + (-1)*main_mul57_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_mul57_float + (-1)*main_mul57_float==0)    #float equality
solver.Add( + (1)*a_CAST_mul57_double + (-1)*main_mul57_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul57_fixp
mathCostObj +=  + (6)*main_mul57_float
mathCostObj +=  + (12.2551)*main_mul57_double
main_main_mul57_enob_1 = solver.IntVar(0, 1, 'main_main_mul57_enob_1')
main_main_mul57_enob_2 = solver.IntVar(0, 1, 'main_main_mul57_enob_2')
solver.Add( + (1)*main_main_mul57_enob_1 + (1)*main_main_mul57_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul57_enob + (-1)*main_p_enob_memphi_main_tmp17 + (-10000)*main_main_mul57_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul57_enob + (-1)*a_enob_memphi_main_tmp16 + (-10000)*main_main_mul57_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
b_enob_memphi_main_tmp18 = solver.IntVar(-10000, 10000, 'b_enob_memphi_main_tmp18')
solver.Add( + (1)*b_enob_memphi_main_tmp18 + (-1)*b_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp18_enob_0 = solver.IntVar(0, 1, 'main_main_tmp18_enob_0')
solver.Add( + (1)*main_main_tmp18_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*b_enob_memphi_main_tmp18 + (-1)*b_enob_storeENOB + (10000)*main_main_tmp18_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add58 = fadd double %mul57, %tmp18, !taffo.info !94, !taffo.initweight !44
main_mul57_CAST_add58_fixbits = solver.IntVar(0, 22, 'main_mul57_CAST_add58_fixbits')
main_mul57_CAST_add58_fixp = solver.IntVar(0, 1, 'main_mul57_CAST_add58_fixp')
main_mul57_CAST_add58_float = solver.IntVar(0, 1, 'main_mul57_CAST_add58_float')
main_mul57_CAST_add58_double = solver.IntVar(0, 1, 'main_mul57_CAST_add58_double')
solver.Add( + (1)*main_mul57_CAST_add58_fixp + (1)*main_mul57_CAST_add58_float + (1)*main_mul57_CAST_add58_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul57_CAST_add58_fixbits + (-10000)*main_mul57_CAST_add58_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C1_main_mul57_CAST_add58')
C2_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C2_main_mul57_CAST_add58')
solver.Add( + (1)*main_mul57_fixbits + (-1)*main_mul57_CAST_add58_fixbits + (-10000)*C1_main_mul57_CAST_add58<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul57_fixbits + (1)*main_mul57_CAST_add58_fixbits + (-10000)*C2_main_mul57_CAST_add58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul57_CAST_add58
castCostObj +=  + (1)*C2_main_mul57_CAST_add58
C3_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C3_main_mul57_CAST_add58')
C4_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C4_main_mul57_CAST_add58')
C5_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C5_main_mul57_CAST_add58')
C6_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C6_main_mul57_CAST_add58')
C7_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C7_main_mul57_CAST_add58')
C8_main_mul57_CAST_add58 = solver.IntVar(0, 1, 'C8_main_mul57_CAST_add58')
solver.Add( + (1)*main_mul57_fixp + (1)*main_mul57_CAST_add58_float + (-1)*C3_main_mul57_CAST_add58<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul57_CAST_add58
solver.Add( + (1)*main_mul57_float + (1)*main_mul57_CAST_add58_fixp + (-1)*C4_main_mul57_CAST_add58<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul57_CAST_add58
solver.Add( + (1)*main_mul57_fixp + (1)*main_mul57_CAST_add58_double + (-1)*C5_main_mul57_CAST_add58<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul57_CAST_add58
solver.Add( + (1)*main_mul57_double + (1)*main_mul57_CAST_add58_fixp + (-1)*C6_main_mul57_CAST_add58<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul57_CAST_add58
solver.Add( + (1)*main_mul57_float + (1)*main_mul57_CAST_add58_double + (-1)*C7_main_mul57_CAST_add58<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul57_CAST_add58
solver.Add( + (1)*main_mul57_double + (1)*main_mul57_CAST_add58_float + (-1)*C8_main_mul57_CAST_add58<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul57_CAST_add58



#Constraint for cast for   %add58 = fadd double %mul57, %tmp18, !taffo.info !94, !taffo.initweight !44
b_CAST_add58_fixbits = solver.IntVar(0, 22, 'b_CAST_add58_fixbits')
b_CAST_add58_fixp = solver.IntVar(0, 1, 'b_CAST_add58_fixp')
b_CAST_add58_float = solver.IntVar(0, 1, 'b_CAST_add58_float')
b_CAST_add58_double = solver.IntVar(0, 1, 'b_CAST_add58_double')
solver.Add( + (1)*b_CAST_add58_fixp + (1)*b_CAST_add58_float + (1)*b_CAST_add58_double==1)    #exactly 1 type
solver.Add( + (1)*b_CAST_add58_fixbits + (-10000)*b_CAST_add58_fixp<=0)    #If no fix, fix frac part = 0
C1_b_CAST_add58 = solver.IntVar(0, 1, 'C1_b_CAST_add58')
C2_b_CAST_add58 = solver.IntVar(0, 1, 'C2_b_CAST_add58')
solver.Add( + (1)*b_fixbits + (-1)*b_CAST_add58_fixbits + (-10000)*C1_b_CAST_add58<=0)    #Shift cost 1
solver.Add( + (-1)*b_fixbits + (1)*b_CAST_add58_fixbits + (-10000)*C2_b_CAST_add58<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_b_CAST_add58
castCostObj +=  + (1)*C2_b_CAST_add58
C3_b_CAST_add58 = solver.IntVar(0, 1, 'C3_b_CAST_add58')
C4_b_CAST_add58 = solver.IntVar(0, 1, 'C4_b_CAST_add58')
C5_b_CAST_add58 = solver.IntVar(0, 1, 'C5_b_CAST_add58')
C6_b_CAST_add58 = solver.IntVar(0, 1, 'C6_b_CAST_add58')
C7_b_CAST_add58 = solver.IntVar(0, 1, 'C7_b_CAST_add58')
C8_b_CAST_add58 = solver.IntVar(0, 1, 'C8_b_CAST_add58')
solver.Add( + (1)*b_fixp + (1)*b_CAST_add58_float + (-1)*C3_b_CAST_add58<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_b_CAST_add58
solver.Add( + (1)*b_float + (1)*b_CAST_add58_fixp + (-1)*C4_b_CAST_add58<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_b_CAST_add58
solver.Add( + (1)*b_fixp + (1)*b_CAST_add58_double + (-1)*C5_b_CAST_add58<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_b_CAST_add58
solver.Add( + (1)*b_double + (1)*b_CAST_add58_fixp + (-1)*C6_b_CAST_add58<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_b_CAST_add58
solver.Add( + (1)*b_float + (1)*b_CAST_add58_double + (-1)*C7_b_CAST_add58<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_b_CAST_add58
solver.Add( + (1)*b_double + (1)*b_CAST_add58_float + (-1)*C8_b_CAST_add58<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_b_CAST_add58



#Stuff for   %add58 = fadd double %mul57, %tmp18, !taffo.info !94, !taffo.initweight !44
main_add58_fixbits = solver.IntVar(0, 20, 'main_add58_fixbits')
main_add58_fixp = solver.IntVar(0, 1, 'main_add58_fixp')
main_add58_float = solver.IntVar(0, 1, 'main_add58_float')
main_add58_double = solver.IntVar(0, 1, 'main_add58_double')
main_add58_enob = solver.IntVar(-10000, 10000, 'main_add58_enob')
solver.Add( + (1)*main_add58_enob + (-1)*main_add58_fixbits + (10000)*main_add58_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add58_enob + (10000)*main_add58_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add58_enob + (10000)*main_add58_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add58_fixbits + (-10000)*main_add58_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_add58_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add58_enob
solver.Add( + (1)*main_add58_fixp + (1)*main_add58_float + (1)*main_add58_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add58_fixbits + (-10000)*main_add58_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul57_CAST_add58_fixp + (-1)*b_CAST_add58_fixp==0)    #fix equality
solver.Add( + (1)*main_mul57_CAST_add58_float + (-1)*b_CAST_add58_float==0)    #float equality
solver.Add( + (1)*main_mul57_CAST_add58_double + (-1)*b_CAST_add58_double==0)    #double equality
solver.Add( + (1)*main_mul57_CAST_add58_fixbits + (-1)*b_CAST_add58_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul57_CAST_add58_fixp + (-1)*main_add58_fixp==0)    #fix equality
solver.Add( + (1)*main_mul57_CAST_add58_float + (-1)*main_add58_float==0)    #float equality
solver.Add( + (1)*main_mul57_CAST_add58_double + (-1)*main_add58_double==0)    #double equality
solver.Add( + (1)*main_mul57_CAST_add58_fixbits + (-1)*main_add58_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add58_fixp
mathCostObj +=  + (3)*main_add58_float
mathCostObj +=  + (6.64928)*main_add58_double
solver.Add( + (1)*main_add58_enob + (-1)*main_mul57_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add58_enob + (-1)*b_enob_memphi_main_tmp18<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %div59 = fdiv double %sub51, %add58, !taffo.info !96, !taffo.initweight !45
main_sub51_CAST_div59_fixbits = solver.IntVar(0, 23, 'main_sub51_CAST_div59_fixbits')
main_sub51_CAST_div59_fixp = solver.IntVar(0, 1, 'main_sub51_CAST_div59_fixp')
main_sub51_CAST_div59_float = solver.IntVar(0, 1, 'main_sub51_CAST_div59_float')
main_sub51_CAST_div59_double = solver.IntVar(0, 1, 'main_sub51_CAST_div59_double')
solver.Add( + (1)*main_sub51_CAST_div59_fixp + (1)*main_sub51_CAST_div59_float + (1)*main_sub51_CAST_div59_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub51_CAST_div59_fixbits + (-10000)*main_sub51_CAST_div59_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C1_main_sub51_CAST_div59')
C2_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C2_main_sub51_CAST_div59')
solver.Add( + (1)*main_sub51_fixbits + (-1)*main_sub51_CAST_div59_fixbits + (-10000)*C1_main_sub51_CAST_div59<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub51_fixbits + (1)*main_sub51_CAST_div59_fixbits + (-10000)*C2_main_sub51_CAST_div59<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub51_CAST_div59
castCostObj +=  + (1)*C2_main_sub51_CAST_div59
C3_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C3_main_sub51_CAST_div59')
C4_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C4_main_sub51_CAST_div59')
C5_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C5_main_sub51_CAST_div59')
C6_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C6_main_sub51_CAST_div59')
C7_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C7_main_sub51_CAST_div59')
C8_main_sub51_CAST_div59 = solver.IntVar(0, 1, 'C8_main_sub51_CAST_div59')
solver.Add( + (1)*main_sub51_fixp + (1)*main_sub51_CAST_div59_float + (-1)*C3_main_sub51_CAST_div59<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub51_CAST_div59
solver.Add( + (1)*main_sub51_float + (1)*main_sub51_CAST_div59_fixp + (-1)*C4_main_sub51_CAST_div59<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub51_CAST_div59
solver.Add( + (1)*main_sub51_fixp + (1)*main_sub51_CAST_div59_double + (-1)*C5_main_sub51_CAST_div59<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub51_CAST_div59
solver.Add( + (1)*main_sub51_double + (1)*main_sub51_CAST_div59_fixp + (-1)*C6_main_sub51_CAST_div59<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub51_CAST_div59
solver.Add( + (1)*main_sub51_float + (1)*main_sub51_CAST_div59_double + (-1)*C7_main_sub51_CAST_div59<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub51_CAST_div59
solver.Add( + (1)*main_sub51_double + (1)*main_sub51_CAST_div59_float + (-1)*C8_main_sub51_CAST_div59<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub51_CAST_div59



#Constraint for cast for   %div59 = fdiv double %sub51, %add58, !taffo.info !96, !taffo.initweight !45
main_add58_CAST_div59_fixbits = solver.IntVar(0, 20, 'main_add58_CAST_div59_fixbits')
main_add58_CAST_div59_fixp = solver.IntVar(0, 1, 'main_add58_CAST_div59_fixp')
main_add58_CAST_div59_float = solver.IntVar(0, 1, 'main_add58_CAST_div59_float')
main_add58_CAST_div59_double = solver.IntVar(0, 1, 'main_add58_CAST_div59_double')
solver.Add( + (1)*main_add58_CAST_div59_fixp + (1)*main_add58_CAST_div59_float + (1)*main_add58_CAST_div59_double==1)    #exactly 1 type
solver.Add( + (1)*main_add58_CAST_div59_fixbits + (-10000)*main_add58_CAST_div59_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C1_main_add58_CAST_div59')
C2_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C2_main_add58_CAST_div59')
solver.Add( + (1)*main_add58_fixbits + (-1)*main_add58_CAST_div59_fixbits + (-10000)*C1_main_add58_CAST_div59<=0)    #Shift cost 1
solver.Add( + (-1)*main_add58_fixbits + (1)*main_add58_CAST_div59_fixbits + (-10000)*C2_main_add58_CAST_div59<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add58_CAST_div59
castCostObj +=  + (1)*C2_main_add58_CAST_div59
C3_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C3_main_add58_CAST_div59')
C4_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C4_main_add58_CAST_div59')
C5_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C5_main_add58_CAST_div59')
C6_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C6_main_add58_CAST_div59')
C7_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C7_main_add58_CAST_div59')
C8_main_add58_CAST_div59 = solver.IntVar(0, 1, 'C8_main_add58_CAST_div59')
solver.Add( + (1)*main_add58_fixp + (1)*main_add58_CAST_div59_float + (-1)*C3_main_add58_CAST_div59<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add58_CAST_div59
solver.Add( + (1)*main_add58_float + (1)*main_add58_CAST_div59_fixp + (-1)*C4_main_add58_CAST_div59<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add58_CAST_div59
solver.Add( + (1)*main_add58_fixp + (1)*main_add58_CAST_div59_double + (-1)*C5_main_add58_CAST_div59<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add58_CAST_div59
solver.Add( + (1)*main_add58_double + (1)*main_add58_CAST_div59_fixp + (-1)*C6_main_add58_CAST_div59<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add58_CAST_div59
solver.Add( + (1)*main_add58_float + (1)*main_add58_CAST_div59_double + (-1)*C7_main_add58_CAST_div59<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add58_CAST_div59
solver.Add( + (1)*main_add58_double + (1)*main_add58_CAST_div59_float + (-1)*C8_main_add58_CAST_div59<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add58_CAST_div59



#Stuff for   %div59 = fdiv double %sub51, %add58, !taffo.info !96, !taffo.initweight !45
main_div59_fixbits = solver.IntVar(0, 30, 'main_div59_fixbits')
main_div59_fixp = solver.IntVar(0, 1, 'main_div59_fixp')
main_div59_float = solver.IntVar(0, 1, 'main_div59_float')
main_div59_double = solver.IntVar(0, 1, 'main_div59_double')
main_div59_enob = solver.IntVar(-10000, 10000, 'main_div59_enob')
solver.Add( + (1)*main_div59_enob + (-1)*main_div59_fixbits + (10000)*main_div59_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div59_enob + (10000)*main_div59_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div59_enob + (10000)*main_div59_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div59_fixbits + (-10000)*main_div59_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_div59_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div59_enob
solver.Add( + (1)*main_div59_fixp + (1)*main_div59_float + (1)*main_div59_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div59_fixbits + (-10000)*main_div59_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub51_CAST_div59_fixp + (-1)*main_add58_CAST_div59_fixp==0)    #fix equality
solver.Add( + (1)*main_sub51_CAST_div59_float + (-1)*main_add58_CAST_div59_float==0)    #float equality
solver.Add( + (1)*main_sub51_CAST_div59_double + (-1)*main_add58_CAST_div59_double==0)    #double equality
solver.Add( + (1)*main_sub51_CAST_div59_fixp + (-1)*main_div59_fixp==0)    #fix equality
solver.Add( + (1)*main_sub51_CAST_div59_float + (-1)*main_div59_float==0)    #float equality
solver.Add( + (1)*main_sub51_CAST_div59_double + (-1)*main_div59_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div59_fixp
mathCostObj +=  + (6)*main_div59_float
mathCostObj +=  + (12)*main_div59_double
main_main_div59_enob_1 = solver.IntVar(0, 1, 'main_main_div59_enob_1')
main_main_div59_enob_2 = solver.IntVar(0, 1, 'main_main_div59_enob_2')
solver.Add( + (1)*main_main_div59_enob_1 + (1)*main_main_div59_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div59_enob + (-1)*main_add58_enob + (-10000)*main_main_div59_enob_1<=1044)    #Enob: propagation in division 1
solver.Add( + (1)*main_div59_enob + (-1)*main_sub51_enob + (-10000)*main_main_div59_enob_2<=1044)    #Enob: propagation in division 2



#Constraint for cast for   store double %div59, double* %arrayidx63, align 8, !taffo.info !37, !taffo.initweight !45
main_div59_CAST_store_fixbits = solver.IntVar(0, 30, 'main_div59_CAST_store_fixbits')
main_div59_CAST_store_fixp = solver.IntVar(0, 1, 'main_div59_CAST_store_fixp')
main_div59_CAST_store_float = solver.IntVar(0, 1, 'main_div59_CAST_store_float')
main_div59_CAST_store_double = solver.IntVar(0, 1, 'main_div59_CAST_store_double')
solver.Add( + (1)*main_div59_CAST_store_fixp + (1)*main_div59_CAST_store_float + (1)*main_div59_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div59_CAST_store_fixbits + (-10000)*main_div59_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div59_CAST_store = solver.IntVar(0, 1, 'C1_main_div59_CAST_store')
C2_main_div59_CAST_store = solver.IntVar(0, 1, 'C2_main_div59_CAST_store')
solver.Add( + (1)*main_div59_fixbits + (-1)*main_div59_CAST_store_fixbits + (-10000)*C1_main_div59_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div59_fixbits + (1)*main_div59_CAST_store_fixbits + (-10000)*C2_main_div59_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div59_CAST_store
castCostObj +=  + (1)*C2_main_div59_CAST_store
C3_main_div59_CAST_store = solver.IntVar(0, 1, 'C3_main_div59_CAST_store')
C4_main_div59_CAST_store = solver.IntVar(0, 1, 'C4_main_div59_CAST_store')
C5_main_div59_CAST_store = solver.IntVar(0, 1, 'C5_main_div59_CAST_store')
C6_main_div59_CAST_store = solver.IntVar(0, 1, 'C6_main_div59_CAST_store')
C7_main_div59_CAST_store = solver.IntVar(0, 1, 'C7_main_div59_CAST_store')
C8_main_div59_CAST_store = solver.IntVar(0, 1, 'C8_main_div59_CAST_store')
solver.Add( + (1)*main_div59_fixp + (1)*main_div59_CAST_store_float + (-1)*C3_main_div59_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div59_CAST_store
solver.Add( + (1)*main_div59_float + (1)*main_div59_CAST_store_fixp + (-1)*C4_main_div59_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div59_CAST_store
solver.Add( + (1)*main_div59_fixp + (1)*main_div59_CAST_store_double + (-1)*C5_main_div59_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div59_CAST_store
solver.Add( + (1)*main_div59_double + (1)*main_div59_CAST_store_fixp + (-1)*C6_main_div59_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div59_CAST_store
solver.Add( + (1)*main_div59_float + (1)*main_div59_CAST_store_double + (-1)*C7_main_div59_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div59_CAST_store
solver.Add( + (1)*main_div59_double + (1)*main_div59_CAST_store_float + (-1)*C8_main_div59_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div59_CAST_store
solver.Add( + (1)*main_p_fixp + (-1)*main_div59_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_p_float + (-1)*main_div59_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_p_double + (-1)*main_div59_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_p_fixbits + (-1)*main_div59_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_p_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_p_enob_storeENOB')
solver.Add( + (1)*main_p_enob_storeENOB + (-1)*main_p_fixbits + (10000)*main_p_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_p_enob_storeENOB + (10000)*main_p_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_p_enob_storeENOB + (10000)*main_p_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_p_enob_storeENOB + (-1)*main_div59_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
d_enob_memphi_main_tmp19 = solver.IntVar(-10000, 10000, 'd_enob_memphi_main_tmp19')
solver.Add( + (1)*d_enob_memphi_main_tmp19 + (-1)*d_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp19_enob_0 = solver.IntVar(0, 1, 'main_main_tmp19_enob_0')
solver.Add( + (1)*main_main_tmp19_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*d_enob_memphi_main_tmp19 + (-1)*d_enob_storeENOB + (10000)*main_main_tmp19_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double -0.000000e+00
ConstantValue__34_fixbits = solver.IntVar(0, 32, 'ConstantValue__34_fixbits')
ConstantValue__34_fixp = solver.IntVar(0, 1, 'ConstantValue__34_fixp')
ConstantValue__34_float = solver.IntVar(0, 1, 'ConstantValue__34_float')
ConstantValue__34_double = solver.IntVar(0, 1, 'ConstantValue__34_double')
ConstantValue__34_enob = solver.IntVar(-10000, 10000, 'ConstantValue__34_enob')
solver.Add( + (1)*ConstantValue__34_enob + (-1)*ConstantValue__34_fixbits + (10000)*ConstantValue__34_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__34_enob + (10000)*ConstantValue__34_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__34_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__34_fixp + (1)*ConstantValue__34_float + (1)*ConstantValue__34_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__34_fixbits + (-10000)*ConstantValue__34_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__35_fixbits = solver.IntVar(0, 32, 'ConstantValue__35_fixbits')
ConstantValue__35_fixp = solver.IntVar(0, 1, 'ConstantValue__35_fixp')
ConstantValue__35_float = solver.IntVar(0, 1, 'ConstantValue__35_float')
ConstantValue__35_double = solver.IntVar(0, 1, 'ConstantValue__35_double')
ConstantValue__35_enob = solver.IntVar(-10000, 10000, 'ConstantValue__35_enob')
solver.Add( + (1)*ConstantValue__35_enob + (-1)*ConstantValue__35_fixbits + (10000)*ConstantValue__35_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__35_enob + (10000)*ConstantValue__35_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__35_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__35_fixp + (1)*ConstantValue__35_float + (1)*ConstantValue__35_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__35_fixbits + (-10000)*ConstantValue__35_fixp<=0)    #If not fix, frac part to zero



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



#Constraint for cast for   %sub64 = fsub double -0.000000e+00, %tmp19, !taffo.info !98, !taffo.initweight !44, !taffo.constinfo !74
ConstantValue__36_CAST_sub64_fixbits = solver.IntVar(0, 32, 'ConstantValue__36_CAST_sub64_fixbits')
ConstantValue__36_CAST_sub64_fixp = solver.IntVar(0, 1, 'ConstantValue__36_CAST_sub64_fixp')
ConstantValue__36_CAST_sub64_float = solver.IntVar(0, 1, 'ConstantValue__36_CAST_sub64_float')
ConstantValue__36_CAST_sub64_double = solver.IntVar(0, 1, 'ConstantValue__36_CAST_sub64_double')
solver.Add( + (1)*ConstantValue__36_CAST_sub64_fixp + (1)*ConstantValue__36_CAST_sub64_float + (1)*ConstantValue__36_CAST_sub64_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__36_CAST_sub64_fixbits + (-10000)*ConstantValue__36_CAST_sub64_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C1_ConstantValue__36_CAST_sub64')
C2_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C2_ConstantValue__36_CAST_sub64')
solver.Add( + (1)*ConstantValue__36_fixbits + (-1)*ConstantValue__36_CAST_sub64_fixbits + (-10000)*C1_ConstantValue__36_CAST_sub64<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__36_fixbits + (1)*ConstantValue__36_CAST_sub64_fixbits + (-10000)*C2_ConstantValue__36_CAST_sub64<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__36_CAST_sub64
castCostObj +=  + (1)*C2_ConstantValue__36_CAST_sub64
C3_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C3_ConstantValue__36_CAST_sub64')
C4_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C4_ConstantValue__36_CAST_sub64')
C5_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C5_ConstantValue__36_CAST_sub64')
C6_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C6_ConstantValue__36_CAST_sub64')
C7_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C7_ConstantValue__36_CAST_sub64')
C8_ConstantValue__36_CAST_sub64 = solver.IntVar(0, 1, 'C8_ConstantValue__36_CAST_sub64')
solver.Add( + (1)*ConstantValue__36_fixp + (1)*ConstantValue__36_CAST_sub64_float + (-1)*C3_ConstantValue__36_CAST_sub64<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__36_CAST_sub64
solver.Add( + (1)*ConstantValue__36_float + (1)*ConstantValue__36_CAST_sub64_fixp + (-1)*C4_ConstantValue__36_CAST_sub64<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__36_CAST_sub64
solver.Add( + (1)*ConstantValue__36_fixp + (1)*ConstantValue__36_CAST_sub64_double + (-1)*C5_ConstantValue__36_CAST_sub64<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__36_CAST_sub64
solver.Add( + (1)*ConstantValue__36_double + (1)*ConstantValue__36_CAST_sub64_fixp + (-1)*C6_ConstantValue__36_CAST_sub64<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__36_CAST_sub64
solver.Add( + (1)*ConstantValue__36_float + (1)*ConstantValue__36_CAST_sub64_double + (-1)*C7_ConstantValue__36_CAST_sub64<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__36_CAST_sub64
solver.Add( + (1)*ConstantValue__36_double + (1)*ConstantValue__36_CAST_sub64_float + (-1)*C8_ConstantValue__36_CAST_sub64<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__36_CAST_sub64



#Constraint for cast for   %sub64 = fsub double -0.000000e+00, %tmp19, !taffo.info !98, !taffo.initweight !44, !taffo.constinfo !74
d_CAST_sub64_fixbits = solver.IntVar(0, 23, 'd_CAST_sub64_fixbits')
d_CAST_sub64_fixp = solver.IntVar(0, 1, 'd_CAST_sub64_fixp')
d_CAST_sub64_float = solver.IntVar(0, 1, 'd_CAST_sub64_float')
d_CAST_sub64_double = solver.IntVar(0, 1, 'd_CAST_sub64_double')
solver.Add( + (1)*d_CAST_sub64_fixp + (1)*d_CAST_sub64_float + (1)*d_CAST_sub64_double==1)    #exactly 1 type
solver.Add( + (1)*d_CAST_sub64_fixbits + (-10000)*d_CAST_sub64_fixp<=0)    #If no fix, fix frac part = 0
C1_d_CAST_sub64 = solver.IntVar(0, 1, 'C1_d_CAST_sub64')
C2_d_CAST_sub64 = solver.IntVar(0, 1, 'C2_d_CAST_sub64')
solver.Add( + (1)*d_fixbits + (-1)*d_CAST_sub64_fixbits + (-10000)*C1_d_CAST_sub64<=0)    #Shift cost 1
solver.Add( + (-1)*d_fixbits + (1)*d_CAST_sub64_fixbits + (-10000)*C2_d_CAST_sub64<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_d_CAST_sub64
castCostObj +=  + (1)*C2_d_CAST_sub64
C3_d_CAST_sub64 = solver.IntVar(0, 1, 'C3_d_CAST_sub64')
C4_d_CAST_sub64 = solver.IntVar(0, 1, 'C4_d_CAST_sub64')
C5_d_CAST_sub64 = solver.IntVar(0, 1, 'C5_d_CAST_sub64')
C6_d_CAST_sub64 = solver.IntVar(0, 1, 'C6_d_CAST_sub64')
C7_d_CAST_sub64 = solver.IntVar(0, 1, 'C7_d_CAST_sub64')
C8_d_CAST_sub64 = solver.IntVar(0, 1, 'C8_d_CAST_sub64')
solver.Add( + (1)*d_fixp + (1)*d_CAST_sub64_float + (-1)*C3_d_CAST_sub64<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_d_CAST_sub64
solver.Add( + (1)*d_float + (1)*d_CAST_sub64_fixp + (-1)*C4_d_CAST_sub64<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_d_CAST_sub64
solver.Add( + (1)*d_fixp + (1)*d_CAST_sub64_double + (-1)*C5_d_CAST_sub64<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_d_CAST_sub64
solver.Add( + (1)*d_double + (1)*d_CAST_sub64_fixp + (-1)*C6_d_CAST_sub64<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_d_CAST_sub64
solver.Add( + (1)*d_float + (1)*d_CAST_sub64_double + (-1)*C7_d_CAST_sub64<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_d_CAST_sub64
solver.Add( + (1)*d_double + (1)*d_CAST_sub64_float + (-1)*C8_d_CAST_sub64<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_d_CAST_sub64



#Stuff for   %sub64 = fsub double -0.000000e+00, %tmp19, !taffo.info !98, !taffo.initweight !44, !taffo.constinfo !74
main_sub64_fixbits = solver.IntVar(0, 24, 'main_sub64_fixbits')
main_sub64_fixp = solver.IntVar(0, 1, 'main_sub64_fixp')
main_sub64_float = solver.IntVar(0, 1, 'main_sub64_float')
main_sub64_double = solver.IntVar(0, 1, 'main_sub64_double')
main_sub64_enob = solver.IntVar(-10000, 10000, 'main_sub64_enob')
solver.Add( + (1)*main_sub64_enob + (-1)*main_sub64_fixbits + (10000)*main_sub64_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub64_enob + (10000)*main_sub64_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub64_enob + (10000)*main_sub64_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub64_fixbits + (-10000)*main_sub64_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*main_sub64_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub64_enob
solver.Add( + (1)*main_sub64_fixp + (1)*main_sub64_float + (1)*main_sub64_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub64_fixbits + (-10000)*main_sub64_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__36_CAST_sub64_fixp + (-1)*d_CAST_sub64_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__36_CAST_sub64_float + (-1)*d_CAST_sub64_float==0)    #float equality
solver.Add( + (1)*ConstantValue__36_CAST_sub64_double + (-1)*d_CAST_sub64_double==0)    #double equality
solver.Add( + (1)*ConstantValue__36_CAST_sub64_fixbits + (-1)*d_CAST_sub64_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__36_CAST_sub64_fixp + (-1)*main_sub64_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__36_CAST_sub64_float + (-1)*main_sub64_float==0)    #float equality
solver.Add( + (1)*ConstantValue__36_CAST_sub64_double + (-1)*main_sub64_double==0)    #double equality
solver.Add( + (1)*ConstantValue__36_CAST_sub64_fixbits + (-1)*main_sub64_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub64_fixp
mathCostObj +=  + (3)*main_sub64_float
mathCostObj +=  + (6.64928)*main_sub64_double
solver.Add( + (1)*main_sub64_enob + (-1)*ConstantValue__34_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub64_enob + (-1)*d_enob_memphi_main_tmp19<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
main_u_enob_memphi_main_tmp20 = solver.IntVar(-10000, 10000, 'main_u_enob_memphi_main_tmp20')
solver.Add( + (1)*main_u_enob_memphi_main_tmp20 + (-1)*main_u_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp20_enob_0 = solver.IntVar(0, 1, 'main_main_tmp20_enob_0')
main_main_tmp20_enob_1 = solver.IntVar(0, 1, 'main_main_tmp20_enob_1')
main_main_tmp20_enob_2 = solver.IntVar(0, 1, 'main_main_tmp20_enob_2')
main_main_tmp20_enob_3 = solver.IntVar(0, 1, 'main_main_tmp20_enob_3')
main_main_tmp20_enob_4 = solver.IntVar(0, 1, 'main_main_tmp20_enob_4')
solver.Add( + (1)*main_main_tmp20_enob_0 + (1)*main_main_tmp20_enob_1 + (1)*main_main_tmp20_enob_2 + (1)*main_main_tmp20_enob_3 + (1)*main_main_tmp20_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp20 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp20_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul70 = fmul double %sub64, %tmp20, !taffo.info !100, !taffo.initweight !45
main_sub64_CAST_mul70_fixbits = solver.IntVar(0, 24, 'main_sub64_CAST_mul70_fixbits')
main_sub64_CAST_mul70_fixp = solver.IntVar(0, 1, 'main_sub64_CAST_mul70_fixp')
main_sub64_CAST_mul70_float = solver.IntVar(0, 1, 'main_sub64_CAST_mul70_float')
main_sub64_CAST_mul70_double = solver.IntVar(0, 1, 'main_sub64_CAST_mul70_double')
solver.Add( + (1)*main_sub64_CAST_mul70_fixp + (1)*main_sub64_CAST_mul70_float + (1)*main_sub64_CAST_mul70_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub64_CAST_mul70_fixbits + (-10000)*main_sub64_CAST_mul70_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C1_main_sub64_CAST_mul70')
C2_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C2_main_sub64_CAST_mul70')
solver.Add( + (1)*main_sub64_fixbits + (-1)*main_sub64_CAST_mul70_fixbits + (-10000)*C1_main_sub64_CAST_mul70<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub64_fixbits + (1)*main_sub64_CAST_mul70_fixbits + (-10000)*C2_main_sub64_CAST_mul70<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub64_CAST_mul70
castCostObj +=  + (1)*C2_main_sub64_CAST_mul70
C3_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C3_main_sub64_CAST_mul70')
C4_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C4_main_sub64_CAST_mul70')
C5_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C5_main_sub64_CAST_mul70')
C6_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C6_main_sub64_CAST_mul70')
C7_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C7_main_sub64_CAST_mul70')
C8_main_sub64_CAST_mul70 = solver.IntVar(0, 1, 'C8_main_sub64_CAST_mul70')
solver.Add( + (1)*main_sub64_fixp + (1)*main_sub64_CAST_mul70_float + (-1)*C3_main_sub64_CAST_mul70<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub64_CAST_mul70
solver.Add( + (1)*main_sub64_float + (1)*main_sub64_CAST_mul70_fixp + (-1)*C4_main_sub64_CAST_mul70<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub64_CAST_mul70
solver.Add( + (1)*main_sub64_fixp + (1)*main_sub64_CAST_mul70_double + (-1)*C5_main_sub64_CAST_mul70<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub64_CAST_mul70
solver.Add( + (1)*main_sub64_double + (1)*main_sub64_CAST_mul70_fixp + (-1)*C6_main_sub64_CAST_mul70<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub64_CAST_mul70
solver.Add( + (1)*main_sub64_float + (1)*main_sub64_CAST_mul70_double + (-1)*C7_main_sub64_CAST_mul70<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub64_CAST_mul70
solver.Add( + (1)*main_sub64_double + (1)*main_sub64_CAST_mul70_float + (-1)*C8_main_sub64_CAST_mul70<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub64_CAST_mul70



#Constraint for cast for   %mul70 = fmul double %sub64, %tmp20, !taffo.info !100, !taffo.initweight !45
main_u_CAST_mul70_fixbits = solver.IntVar(0, 28, 'main_u_CAST_mul70_fixbits')
main_u_CAST_mul70_fixp = solver.IntVar(0, 1, 'main_u_CAST_mul70_fixp')
main_u_CAST_mul70_float = solver.IntVar(0, 1, 'main_u_CAST_mul70_float')
main_u_CAST_mul70_double = solver.IntVar(0, 1, 'main_u_CAST_mul70_double')
solver.Add( + (1)*main_u_CAST_mul70_fixp + (1)*main_u_CAST_mul70_float + (1)*main_u_CAST_mul70_double==1)    #exactly 1 type
solver.Add( + (1)*main_u_CAST_mul70_fixbits + (-10000)*main_u_CAST_mul70_fixp<=0)    #If no fix, fix frac part = 0
C1_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C1_main_u_CAST_mul70')
C2_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C2_main_u_CAST_mul70')
solver.Add( + (1)*main_u_fixbits + (-1)*main_u_CAST_mul70_fixbits + (-10000)*C1_main_u_CAST_mul70<=0)    #Shift cost 1
solver.Add( + (-1)*main_u_fixbits + (1)*main_u_CAST_mul70_fixbits + (-10000)*C2_main_u_CAST_mul70<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_u_CAST_mul70
castCostObj +=  + (1)*C2_main_u_CAST_mul70
C3_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C3_main_u_CAST_mul70')
C4_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C4_main_u_CAST_mul70')
C5_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C5_main_u_CAST_mul70')
C6_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C6_main_u_CAST_mul70')
C7_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C7_main_u_CAST_mul70')
C8_main_u_CAST_mul70 = solver.IntVar(0, 1, 'C8_main_u_CAST_mul70')
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul70_float + (-1)*C3_main_u_CAST_mul70<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_u_CAST_mul70
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul70_fixp + (-1)*C4_main_u_CAST_mul70<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_u_CAST_mul70
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul70_double + (-1)*C5_main_u_CAST_mul70<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_u_CAST_mul70
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul70_fixp + (-1)*C6_main_u_CAST_mul70<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_u_CAST_mul70
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul70_double + (-1)*C7_main_u_CAST_mul70<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_u_CAST_mul70
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul70_float + (-1)*C8_main_u_CAST_mul70<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_u_CAST_mul70



#Stuff for   %mul70 = fmul double %sub64, %tmp20, !taffo.info !100, !taffo.initweight !45
main_mul70_fixbits = solver.IntVar(0, 21, 'main_mul70_fixbits')
main_mul70_fixp = solver.IntVar(0, 1, 'main_mul70_fixp')
main_mul70_float = solver.IntVar(0, 1, 'main_mul70_float')
main_mul70_double = solver.IntVar(0, 1, 'main_mul70_double')
main_mul70_enob = solver.IntVar(-10000, 10000, 'main_mul70_enob')
solver.Add( + (1)*main_mul70_enob + (-1)*main_mul70_fixbits + (10000)*main_mul70_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul70_enob + (10000)*main_mul70_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul70_enob + (10000)*main_mul70_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul70_fixbits + (-10000)*main_mul70_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_mul70_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul70_enob
solver.Add( + (1)*main_mul70_fixp + (1)*main_mul70_float + (1)*main_mul70_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul70_fixbits + (-10000)*main_mul70_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub64_CAST_mul70_fixp + (-1)*main_u_CAST_mul70_fixp==0)    #fix equality
solver.Add( + (1)*main_sub64_CAST_mul70_float + (-1)*main_u_CAST_mul70_float==0)    #float equality
solver.Add( + (1)*main_sub64_CAST_mul70_double + (-1)*main_u_CAST_mul70_double==0)    #double equality
solver.Add( + (1)*main_sub64_CAST_mul70_fixp + (-1)*main_mul70_fixp==0)    #fix equality
solver.Add( + (1)*main_sub64_CAST_mul70_float + (-1)*main_mul70_float==0)    #float equality
solver.Add( + (1)*main_sub64_CAST_mul70_double + (-1)*main_mul70_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul70_fixp
mathCostObj +=  + (6)*main_mul70_float
mathCostObj +=  + (12.2551)*main_mul70_double
main_main_mul70_enob_1 = solver.IntVar(0, 1, 'main_main_mul70_enob_1')
main_main_mul70_enob_2 = solver.IntVar(0, 1, 'main_main_mul70_enob_2')
solver.Add( + (1)*main_main_mul70_enob_1 + (1)*main_main_mul70_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul70_enob + (-1)*main_u_enob_memphi_main_tmp20 + (-10000)*main_main_mul70_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul70_enob + (-1)*main_sub64_enob + (-10000)*main_main_mul70_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
d_enob_memphi_main_tmp21 = solver.IntVar(-10000, 10000, 'd_enob_memphi_main_tmp21')
solver.Add( + (1)*d_enob_memphi_main_tmp21 + (-1)*d_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp21_enob_0 = solver.IntVar(0, 1, 'main_main_tmp21_enob_0')
solver.Add( + (1)*main_main_tmp21_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*d_enob_memphi_main_tmp21 + (-1)*d_enob_storeENOB + (10000)*main_main_tmp21_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__37_fixbits = solver.IntVar(0, 30, 'ConstantValue__37_fixbits')
ConstantValue__37_fixp = solver.IntVar(0, 1, 'ConstantValue__37_fixp')
ConstantValue__37_float = solver.IntVar(0, 1, 'ConstantValue__37_float')
ConstantValue__37_double = solver.IntVar(0, 1, 'ConstantValue__37_double')
ConstantValue__37_enob = solver.IntVar(-10000, 10000, 'ConstantValue__37_enob')
solver.Add( + (1)*ConstantValue__37_enob + (-1)*ConstantValue__37_fixbits + (10000)*ConstantValue__37_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__37_enob + (10000)*ConstantValue__37_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__37_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__37_fixp + (1)*ConstantValue__37_float + (1)*ConstantValue__37_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__37_fixbits + (-10000)*ConstantValue__37_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__38_fixbits = solver.IntVar(0, 30, 'ConstantValue__38_fixbits')
ConstantValue__38_fixp = solver.IntVar(0, 1, 'ConstantValue__38_fixp')
ConstantValue__38_float = solver.IntVar(0, 1, 'ConstantValue__38_float')
ConstantValue__38_double = solver.IntVar(0, 1, 'ConstantValue__38_double')
ConstantValue__38_enob = solver.IntVar(-10000, 10000, 'ConstantValue__38_enob')
solver.Add( + (1)*ConstantValue__38_enob + (-1)*ConstantValue__38_fixbits + (10000)*ConstantValue__38_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__38_enob + (10000)*ConstantValue__38_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__38_enob + (10000)*ConstantValue__38_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__38_fixbits + (-10000)*ConstantValue__38_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__38_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__38_fixp + (1)*ConstantValue__38_float + (1)*ConstantValue__38_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__38_fixbits + (-10000)*ConstantValue__38_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__39_fixbits = solver.IntVar(0, 30, 'ConstantValue__39_fixbits')
ConstantValue__39_fixp = solver.IntVar(0, 1, 'ConstantValue__39_fixp')
ConstantValue__39_float = solver.IntVar(0, 1, 'ConstantValue__39_float')
ConstantValue__39_double = solver.IntVar(0, 1, 'ConstantValue__39_double')
ConstantValue__39_enob = solver.IntVar(-10000, 10000, 'ConstantValue__39_enob')
solver.Add( + (1)*ConstantValue__39_enob + (-1)*ConstantValue__39_fixbits + (10000)*ConstantValue__39_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__39_enob + (10000)*ConstantValue__39_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__39_enob + (10000)*ConstantValue__39_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__39_fixbits + (-10000)*ConstantValue__39_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__39_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__39_fixp + (1)*ConstantValue__39_float + (1)*ConstantValue__39_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__39_fixbits + (-10000)*ConstantValue__39_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul71 = fmul double 2.000000e+00, %tmp21, !taffo.info !17, !taffo.initweight !44, !taffo.constinfo !63
ConstantValue__39_CAST_mul71_fixbits = solver.IntVar(0, 30, 'ConstantValue__39_CAST_mul71_fixbits')
ConstantValue__39_CAST_mul71_fixp = solver.IntVar(0, 1, 'ConstantValue__39_CAST_mul71_fixp')
ConstantValue__39_CAST_mul71_float = solver.IntVar(0, 1, 'ConstantValue__39_CAST_mul71_float')
ConstantValue__39_CAST_mul71_double = solver.IntVar(0, 1, 'ConstantValue__39_CAST_mul71_double')
solver.Add( + (1)*ConstantValue__39_CAST_mul71_fixp + (1)*ConstantValue__39_CAST_mul71_float + (1)*ConstantValue__39_CAST_mul71_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__39_CAST_mul71_fixbits + (-10000)*ConstantValue__39_CAST_mul71_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C1_ConstantValue__39_CAST_mul71')
C2_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C2_ConstantValue__39_CAST_mul71')
solver.Add( + (1)*ConstantValue__39_fixbits + (-1)*ConstantValue__39_CAST_mul71_fixbits + (-10000)*C1_ConstantValue__39_CAST_mul71<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__39_fixbits + (1)*ConstantValue__39_CAST_mul71_fixbits + (-10000)*C2_ConstantValue__39_CAST_mul71<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__39_CAST_mul71
castCostObj +=  + (1)*C2_ConstantValue__39_CAST_mul71
C3_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C3_ConstantValue__39_CAST_mul71')
C4_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C4_ConstantValue__39_CAST_mul71')
C5_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C5_ConstantValue__39_CAST_mul71')
C6_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C6_ConstantValue__39_CAST_mul71')
C7_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C7_ConstantValue__39_CAST_mul71')
C8_ConstantValue__39_CAST_mul71 = solver.IntVar(0, 1, 'C8_ConstantValue__39_CAST_mul71')
solver.Add( + (1)*ConstantValue__39_fixp + (1)*ConstantValue__39_CAST_mul71_float + (-1)*C3_ConstantValue__39_CAST_mul71<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__39_CAST_mul71
solver.Add( + (1)*ConstantValue__39_float + (1)*ConstantValue__39_CAST_mul71_fixp + (-1)*C4_ConstantValue__39_CAST_mul71<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__39_CAST_mul71
solver.Add( + (1)*ConstantValue__39_fixp + (1)*ConstantValue__39_CAST_mul71_double + (-1)*C5_ConstantValue__39_CAST_mul71<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__39_CAST_mul71
solver.Add( + (1)*ConstantValue__39_double + (1)*ConstantValue__39_CAST_mul71_fixp + (-1)*C6_ConstantValue__39_CAST_mul71<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__39_CAST_mul71
solver.Add( + (1)*ConstantValue__39_float + (1)*ConstantValue__39_CAST_mul71_double + (-1)*C7_ConstantValue__39_CAST_mul71<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__39_CAST_mul71
solver.Add( + (1)*ConstantValue__39_double + (1)*ConstantValue__39_CAST_mul71_float + (-1)*C8_ConstantValue__39_CAST_mul71<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__39_CAST_mul71



#Constraint for cast for   %mul71 = fmul double 2.000000e+00, %tmp21, !taffo.info !17, !taffo.initweight !44, !taffo.constinfo !63
d_CAST_mul71_fixbits = solver.IntVar(0, 23, 'd_CAST_mul71_fixbits')
d_CAST_mul71_fixp = solver.IntVar(0, 1, 'd_CAST_mul71_fixp')
d_CAST_mul71_float = solver.IntVar(0, 1, 'd_CAST_mul71_float')
d_CAST_mul71_double = solver.IntVar(0, 1, 'd_CAST_mul71_double')
solver.Add( + (1)*d_CAST_mul71_fixp + (1)*d_CAST_mul71_float + (1)*d_CAST_mul71_double==1)    #exactly 1 type
solver.Add( + (1)*d_CAST_mul71_fixbits + (-10000)*d_CAST_mul71_fixp<=0)    #If no fix, fix frac part = 0
C1_d_CAST_mul71 = solver.IntVar(0, 1, 'C1_d_CAST_mul71')
C2_d_CAST_mul71 = solver.IntVar(0, 1, 'C2_d_CAST_mul71')
solver.Add( + (1)*d_fixbits + (-1)*d_CAST_mul71_fixbits + (-10000)*C1_d_CAST_mul71<=0)    #Shift cost 1
solver.Add( + (-1)*d_fixbits + (1)*d_CAST_mul71_fixbits + (-10000)*C2_d_CAST_mul71<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_d_CAST_mul71
castCostObj +=  + (1)*C2_d_CAST_mul71
C3_d_CAST_mul71 = solver.IntVar(0, 1, 'C3_d_CAST_mul71')
C4_d_CAST_mul71 = solver.IntVar(0, 1, 'C4_d_CAST_mul71')
C5_d_CAST_mul71 = solver.IntVar(0, 1, 'C5_d_CAST_mul71')
C6_d_CAST_mul71 = solver.IntVar(0, 1, 'C6_d_CAST_mul71')
C7_d_CAST_mul71 = solver.IntVar(0, 1, 'C7_d_CAST_mul71')
C8_d_CAST_mul71 = solver.IntVar(0, 1, 'C8_d_CAST_mul71')
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul71_float + (-1)*C3_d_CAST_mul71<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_d_CAST_mul71
solver.Add( + (1)*d_float + (1)*d_CAST_mul71_fixp + (-1)*C4_d_CAST_mul71<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_d_CAST_mul71
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul71_double + (-1)*C5_d_CAST_mul71<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_d_CAST_mul71
solver.Add( + (1)*d_double + (1)*d_CAST_mul71_fixp + (-1)*C6_d_CAST_mul71<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_d_CAST_mul71
solver.Add( + (1)*d_float + (1)*d_CAST_mul71_double + (-1)*C7_d_CAST_mul71<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_d_CAST_mul71
solver.Add( + (1)*d_double + (1)*d_CAST_mul71_float + (-1)*C8_d_CAST_mul71<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_d_CAST_mul71



#Stuff for   %mul71 = fmul double 2.000000e+00, %tmp21, !taffo.info !17, !taffo.initweight !44, !taffo.constinfo !63
main_mul71_fixbits = solver.IntVar(0, 22, 'main_mul71_fixbits')
main_mul71_fixp = solver.IntVar(0, 1, 'main_mul71_fixp')
main_mul71_float = solver.IntVar(0, 1, 'main_mul71_float')
main_mul71_double = solver.IntVar(0, 1, 'main_mul71_double')
main_mul71_enob = solver.IntVar(-10000, 10000, 'main_mul71_enob')
solver.Add( + (1)*main_mul71_enob + (-1)*main_mul71_fixbits + (10000)*main_mul71_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul71_enob + (10000)*main_mul71_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul71_enob + (10000)*main_mul71_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul71_fixbits + (-10000)*main_mul71_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_mul71_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul71_enob
solver.Add( + (1)*main_mul71_fixp + (1)*main_mul71_float + (1)*main_mul71_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul71_fixbits + (-10000)*main_mul71_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__39_CAST_mul71_fixp + (-1)*d_CAST_mul71_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__39_CAST_mul71_float + (-1)*d_CAST_mul71_float==0)    #float equality
solver.Add( + (1)*ConstantValue__39_CAST_mul71_double + (-1)*d_CAST_mul71_double==0)    #double equality
solver.Add( + (1)*ConstantValue__39_CAST_mul71_fixp + (-1)*main_mul71_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__39_CAST_mul71_float + (-1)*main_mul71_float==0)    #float equality
solver.Add( + (1)*ConstantValue__39_CAST_mul71_double + (-1)*main_mul71_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul71_fixp
mathCostObj +=  + (6)*main_mul71_float
mathCostObj +=  + (12.2551)*main_mul71_double
main_main_mul71_enob_1 = solver.IntVar(0, 1, 'main_main_mul71_enob_1')
main_main_mul71_enob_2 = solver.IntVar(0, 1, 'main_main_mul71_enob_2')
solver.Add( + (1)*main_main_mul71_enob_1 + (1)*main_main_mul71_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul71_enob + (-1)*d_enob_memphi_main_tmp21 + (-10000)*main_main_mul71_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul71_enob + (-1)*ConstantValue__37_enob + (-10000)*main_main_mul71_enob_2<=1024)    #Enob: propagation in product 2



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



#Constraint for cast for   %add72 = fadd double 1.000000e+00, %mul71, !taffo.info !102, !taffo.initweight !45, !taffo.constinfo !66
ConstantValue__42_CAST_add72_fixbits = solver.IntVar(0, 31, 'ConstantValue__42_CAST_add72_fixbits')
ConstantValue__42_CAST_add72_fixp = solver.IntVar(0, 1, 'ConstantValue__42_CAST_add72_fixp')
ConstantValue__42_CAST_add72_float = solver.IntVar(0, 1, 'ConstantValue__42_CAST_add72_float')
ConstantValue__42_CAST_add72_double = solver.IntVar(0, 1, 'ConstantValue__42_CAST_add72_double')
solver.Add( + (1)*ConstantValue__42_CAST_add72_fixp + (1)*ConstantValue__42_CAST_add72_float + (1)*ConstantValue__42_CAST_add72_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__42_CAST_add72_fixbits + (-10000)*ConstantValue__42_CAST_add72_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C1_ConstantValue__42_CAST_add72')
C2_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C2_ConstantValue__42_CAST_add72')
solver.Add( + (1)*ConstantValue__42_fixbits + (-1)*ConstantValue__42_CAST_add72_fixbits + (-10000)*C1_ConstantValue__42_CAST_add72<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__42_fixbits + (1)*ConstantValue__42_CAST_add72_fixbits + (-10000)*C2_ConstantValue__42_CAST_add72<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__42_CAST_add72
castCostObj +=  + (1)*C2_ConstantValue__42_CAST_add72
C3_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C3_ConstantValue__42_CAST_add72')
C4_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C4_ConstantValue__42_CAST_add72')
C5_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C5_ConstantValue__42_CAST_add72')
C6_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C6_ConstantValue__42_CAST_add72')
C7_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C7_ConstantValue__42_CAST_add72')
C8_ConstantValue__42_CAST_add72 = solver.IntVar(0, 1, 'C8_ConstantValue__42_CAST_add72')
solver.Add( + (1)*ConstantValue__42_fixp + (1)*ConstantValue__42_CAST_add72_float + (-1)*C3_ConstantValue__42_CAST_add72<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__42_CAST_add72
solver.Add( + (1)*ConstantValue__42_float + (1)*ConstantValue__42_CAST_add72_fixp + (-1)*C4_ConstantValue__42_CAST_add72<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__42_CAST_add72
solver.Add( + (1)*ConstantValue__42_fixp + (1)*ConstantValue__42_CAST_add72_double + (-1)*C5_ConstantValue__42_CAST_add72<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__42_CAST_add72
solver.Add( + (1)*ConstantValue__42_double + (1)*ConstantValue__42_CAST_add72_fixp + (-1)*C6_ConstantValue__42_CAST_add72<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__42_CAST_add72
solver.Add( + (1)*ConstantValue__42_float + (1)*ConstantValue__42_CAST_add72_double + (-1)*C7_ConstantValue__42_CAST_add72<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__42_CAST_add72
solver.Add( + (1)*ConstantValue__42_double + (1)*ConstantValue__42_CAST_add72_float + (-1)*C8_ConstantValue__42_CAST_add72<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__42_CAST_add72



#Constraint for cast for   %add72 = fadd double 1.000000e+00, %mul71, !taffo.info !102, !taffo.initweight !45, !taffo.constinfo !66
main_mul71_CAST_add72_fixbits = solver.IntVar(0, 22, 'main_mul71_CAST_add72_fixbits')
main_mul71_CAST_add72_fixp = solver.IntVar(0, 1, 'main_mul71_CAST_add72_fixp')
main_mul71_CAST_add72_float = solver.IntVar(0, 1, 'main_mul71_CAST_add72_float')
main_mul71_CAST_add72_double = solver.IntVar(0, 1, 'main_mul71_CAST_add72_double')
solver.Add( + (1)*main_mul71_CAST_add72_fixp + (1)*main_mul71_CAST_add72_float + (1)*main_mul71_CAST_add72_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul71_CAST_add72_fixbits + (-10000)*main_mul71_CAST_add72_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C1_main_mul71_CAST_add72')
C2_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C2_main_mul71_CAST_add72')
solver.Add( + (1)*main_mul71_fixbits + (-1)*main_mul71_CAST_add72_fixbits + (-10000)*C1_main_mul71_CAST_add72<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul71_fixbits + (1)*main_mul71_CAST_add72_fixbits + (-10000)*C2_main_mul71_CAST_add72<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul71_CAST_add72
castCostObj +=  + (1)*C2_main_mul71_CAST_add72
C3_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C3_main_mul71_CAST_add72')
C4_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C4_main_mul71_CAST_add72')
C5_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C5_main_mul71_CAST_add72')
C6_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C6_main_mul71_CAST_add72')
C7_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C7_main_mul71_CAST_add72')
C8_main_mul71_CAST_add72 = solver.IntVar(0, 1, 'C8_main_mul71_CAST_add72')
solver.Add( + (1)*main_mul71_fixp + (1)*main_mul71_CAST_add72_float + (-1)*C3_main_mul71_CAST_add72<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul71_CAST_add72
solver.Add( + (1)*main_mul71_float + (1)*main_mul71_CAST_add72_fixp + (-1)*C4_main_mul71_CAST_add72<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul71_CAST_add72
solver.Add( + (1)*main_mul71_fixp + (1)*main_mul71_CAST_add72_double + (-1)*C5_main_mul71_CAST_add72<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul71_CAST_add72
solver.Add( + (1)*main_mul71_double + (1)*main_mul71_CAST_add72_fixp + (-1)*C6_main_mul71_CAST_add72<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul71_CAST_add72
solver.Add( + (1)*main_mul71_float + (1)*main_mul71_CAST_add72_double + (-1)*C7_main_mul71_CAST_add72<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul71_CAST_add72
solver.Add( + (1)*main_mul71_double + (1)*main_mul71_CAST_add72_float + (-1)*C8_main_mul71_CAST_add72<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul71_CAST_add72



#Stuff for   %add72 = fadd double 1.000000e+00, %mul71, !taffo.info !102, !taffo.initweight !45, !taffo.constinfo !66
main_add72_fixbits = solver.IntVar(0, 22, 'main_add72_fixbits')
main_add72_fixp = solver.IntVar(0, 1, 'main_add72_fixp')
main_add72_float = solver.IntVar(0, 1, 'main_add72_float')
main_add72_double = solver.IntVar(0, 1, 'main_add72_double')
main_add72_enob = solver.IntVar(-10000, 10000, 'main_add72_enob')
solver.Add( + (1)*main_add72_enob + (-1)*main_add72_fixbits + (10000)*main_add72_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add72_enob + (10000)*main_add72_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add72_enob + (10000)*main_add72_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add72_fixbits + (-10000)*main_add72_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_add72_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add72_enob
solver.Add( + (1)*main_add72_fixp + (1)*main_add72_float + (1)*main_add72_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add72_fixbits + (-10000)*main_add72_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__42_CAST_add72_fixp + (-1)*main_mul71_CAST_add72_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__42_CAST_add72_float + (-1)*main_mul71_CAST_add72_float==0)    #float equality
solver.Add( + (1)*ConstantValue__42_CAST_add72_double + (-1)*main_mul71_CAST_add72_double==0)    #double equality
solver.Add( + (1)*ConstantValue__42_CAST_add72_fixbits + (-1)*main_mul71_CAST_add72_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__42_CAST_add72_fixp + (-1)*main_add72_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__42_CAST_add72_float + (-1)*main_add72_float==0)    #float equality
solver.Add( + (1)*ConstantValue__42_CAST_add72_double + (-1)*main_add72_double==0)    #double equality
solver.Add( + (1)*ConstantValue__42_CAST_add72_fixbits + (-1)*main_add72_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add72_fixp
mathCostObj +=  + (3)*main_add72_float
mathCostObj +=  + (6.64928)*main_add72_double
solver.Add( + (1)*main_add72_enob + (-1)*ConstantValue__40_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add72_enob + (-1)*main_mul71_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
main_u_enob_memphi_main_tmp22 = solver.IntVar(-10000, 10000, 'main_u_enob_memphi_main_tmp22')
solver.Add( + (1)*main_u_enob_memphi_main_tmp22 + (-1)*main_u_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp22_enob_0 = solver.IntVar(0, 1, 'main_main_tmp22_enob_0')
main_main_tmp22_enob_1 = solver.IntVar(0, 1, 'main_main_tmp22_enob_1')
main_main_tmp22_enob_2 = solver.IntVar(0, 1, 'main_main_tmp22_enob_2')
main_main_tmp22_enob_3 = solver.IntVar(0, 1, 'main_main_tmp22_enob_3')
main_main_tmp22_enob_4 = solver.IntVar(0, 1, 'main_main_tmp22_enob_4')
solver.Add( + (1)*main_main_tmp22_enob_0 + (1)*main_main_tmp22_enob_1 + (1)*main_main_tmp22_enob_2 + (1)*main_main_tmp22_enob_3 + (1)*main_main_tmp22_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp22 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp22_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul77 = fmul double %add72, %tmp22, !taffo.info !104, !taffo.initweight !51
main_add72_CAST_mul77_fixbits = solver.IntVar(0, 22, 'main_add72_CAST_mul77_fixbits')
main_add72_CAST_mul77_fixp = solver.IntVar(0, 1, 'main_add72_CAST_mul77_fixp')
main_add72_CAST_mul77_float = solver.IntVar(0, 1, 'main_add72_CAST_mul77_float')
main_add72_CAST_mul77_double = solver.IntVar(0, 1, 'main_add72_CAST_mul77_double')
solver.Add( + (1)*main_add72_CAST_mul77_fixp + (1)*main_add72_CAST_mul77_float + (1)*main_add72_CAST_mul77_double==1)    #exactly 1 type
solver.Add( + (1)*main_add72_CAST_mul77_fixbits + (-10000)*main_add72_CAST_mul77_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C1_main_add72_CAST_mul77')
C2_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C2_main_add72_CAST_mul77')
solver.Add( + (1)*main_add72_fixbits + (-1)*main_add72_CAST_mul77_fixbits + (-10000)*C1_main_add72_CAST_mul77<=0)    #Shift cost 1
solver.Add( + (-1)*main_add72_fixbits + (1)*main_add72_CAST_mul77_fixbits + (-10000)*C2_main_add72_CAST_mul77<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add72_CAST_mul77
castCostObj +=  + (1)*C2_main_add72_CAST_mul77
C3_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C3_main_add72_CAST_mul77')
C4_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C4_main_add72_CAST_mul77')
C5_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C5_main_add72_CAST_mul77')
C6_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C6_main_add72_CAST_mul77')
C7_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C7_main_add72_CAST_mul77')
C8_main_add72_CAST_mul77 = solver.IntVar(0, 1, 'C8_main_add72_CAST_mul77')
solver.Add( + (1)*main_add72_fixp + (1)*main_add72_CAST_mul77_float + (-1)*C3_main_add72_CAST_mul77<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add72_CAST_mul77
solver.Add( + (1)*main_add72_float + (1)*main_add72_CAST_mul77_fixp + (-1)*C4_main_add72_CAST_mul77<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add72_CAST_mul77
solver.Add( + (1)*main_add72_fixp + (1)*main_add72_CAST_mul77_double + (-1)*C5_main_add72_CAST_mul77<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add72_CAST_mul77
solver.Add( + (1)*main_add72_double + (1)*main_add72_CAST_mul77_fixp + (-1)*C6_main_add72_CAST_mul77<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add72_CAST_mul77
solver.Add( + (1)*main_add72_float + (1)*main_add72_CAST_mul77_double + (-1)*C7_main_add72_CAST_mul77<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add72_CAST_mul77
solver.Add( + (1)*main_add72_double + (1)*main_add72_CAST_mul77_float + (-1)*C8_main_add72_CAST_mul77<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add72_CAST_mul77



#Constraint for cast for   %mul77 = fmul double %add72, %tmp22, !taffo.info !104, !taffo.initweight !51
main_u_CAST_mul77_fixbits = solver.IntVar(0, 28, 'main_u_CAST_mul77_fixbits')
main_u_CAST_mul77_fixp = solver.IntVar(0, 1, 'main_u_CAST_mul77_fixp')
main_u_CAST_mul77_float = solver.IntVar(0, 1, 'main_u_CAST_mul77_float')
main_u_CAST_mul77_double = solver.IntVar(0, 1, 'main_u_CAST_mul77_double')
solver.Add( + (1)*main_u_CAST_mul77_fixp + (1)*main_u_CAST_mul77_float + (1)*main_u_CAST_mul77_double==1)    #exactly 1 type
solver.Add( + (1)*main_u_CAST_mul77_fixbits + (-10000)*main_u_CAST_mul77_fixp<=0)    #If no fix, fix frac part = 0
C1_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C1_main_u_CAST_mul77')
C2_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C2_main_u_CAST_mul77')
solver.Add( + (1)*main_u_fixbits + (-1)*main_u_CAST_mul77_fixbits + (-10000)*C1_main_u_CAST_mul77<=0)    #Shift cost 1
solver.Add( + (-1)*main_u_fixbits + (1)*main_u_CAST_mul77_fixbits + (-10000)*C2_main_u_CAST_mul77<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_u_CAST_mul77
castCostObj +=  + (1)*C2_main_u_CAST_mul77
C3_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C3_main_u_CAST_mul77')
C4_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C4_main_u_CAST_mul77')
C5_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C5_main_u_CAST_mul77')
C6_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C6_main_u_CAST_mul77')
C7_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C7_main_u_CAST_mul77')
C8_main_u_CAST_mul77 = solver.IntVar(0, 1, 'C8_main_u_CAST_mul77')
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul77_float + (-1)*C3_main_u_CAST_mul77<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_u_CAST_mul77
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul77_fixp + (-1)*C4_main_u_CAST_mul77<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_u_CAST_mul77
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul77_double + (-1)*C5_main_u_CAST_mul77<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_u_CAST_mul77
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul77_fixp + (-1)*C6_main_u_CAST_mul77<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_u_CAST_mul77
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul77_double + (-1)*C7_main_u_CAST_mul77<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_u_CAST_mul77
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul77_float + (-1)*C8_main_u_CAST_mul77<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_u_CAST_mul77



#Stuff for   %mul77 = fmul double %add72, %tmp22, !taffo.info !104, !taffo.initweight !51
main_mul77_fixbits = solver.IntVar(0, 20, 'main_mul77_fixbits')
main_mul77_fixp = solver.IntVar(0, 1, 'main_mul77_fixp')
main_mul77_float = solver.IntVar(0, 1, 'main_mul77_float')
main_mul77_double = solver.IntVar(0, 1, 'main_mul77_double')
main_mul77_enob = solver.IntVar(-10000, 10000, 'main_mul77_enob')
solver.Add( + (1)*main_mul77_enob + (-1)*main_mul77_fixbits + (10000)*main_mul77_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul77_enob + (10000)*main_mul77_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul77_enob + (10000)*main_mul77_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul77_fixbits + (-10000)*main_mul77_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_mul77_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul77_enob
solver.Add( + (1)*main_mul77_fixp + (1)*main_mul77_float + (1)*main_mul77_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul77_fixbits + (-10000)*main_mul77_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add72_CAST_mul77_fixp + (-1)*main_u_CAST_mul77_fixp==0)    #fix equality
solver.Add( + (1)*main_add72_CAST_mul77_float + (-1)*main_u_CAST_mul77_float==0)    #float equality
solver.Add( + (1)*main_add72_CAST_mul77_double + (-1)*main_u_CAST_mul77_double==0)    #double equality
solver.Add( + (1)*main_add72_CAST_mul77_fixp + (-1)*main_mul77_fixp==0)    #fix equality
solver.Add( + (1)*main_add72_CAST_mul77_float + (-1)*main_mul77_float==0)    #float equality
solver.Add( + (1)*main_add72_CAST_mul77_double + (-1)*main_mul77_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul77_fixp
mathCostObj +=  + (6)*main_mul77_float
mathCostObj +=  + (12.2551)*main_mul77_double
main_main_mul77_enob_1 = solver.IntVar(0, 1, 'main_main_mul77_enob_1')
main_main_mul77_enob_2 = solver.IntVar(0, 1, 'main_main_mul77_enob_2')
solver.Add( + (1)*main_main_mul77_enob_1 + (1)*main_main_mul77_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul77_enob + (-1)*main_u_enob_memphi_main_tmp22 + (-10000)*main_main_mul77_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul77_enob + (-1)*main_add72_enob + (-10000)*main_main_mul77_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add78 = fadd double %mul70, %mul77, !taffo.info !106, !taffo.initweight !51
main_mul70_CAST_add78_fixbits = solver.IntVar(0, 21, 'main_mul70_CAST_add78_fixbits')
main_mul70_CAST_add78_fixp = solver.IntVar(0, 1, 'main_mul70_CAST_add78_fixp')
main_mul70_CAST_add78_float = solver.IntVar(0, 1, 'main_mul70_CAST_add78_float')
main_mul70_CAST_add78_double = solver.IntVar(0, 1, 'main_mul70_CAST_add78_double')
solver.Add( + (1)*main_mul70_CAST_add78_fixp + (1)*main_mul70_CAST_add78_float + (1)*main_mul70_CAST_add78_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul70_CAST_add78_fixbits + (-10000)*main_mul70_CAST_add78_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C1_main_mul70_CAST_add78')
C2_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C2_main_mul70_CAST_add78')
solver.Add( + (1)*main_mul70_fixbits + (-1)*main_mul70_CAST_add78_fixbits + (-10000)*C1_main_mul70_CAST_add78<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul70_fixbits + (1)*main_mul70_CAST_add78_fixbits + (-10000)*C2_main_mul70_CAST_add78<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul70_CAST_add78
castCostObj +=  + (1)*C2_main_mul70_CAST_add78
C3_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C3_main_mul70_CAST_add78')
C4_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C4_main_mul70_CAST_add78')
C5_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C5_main_mul70_CAST_add78')
C6_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C6_main_mul70_CAST_add78')
C7_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C7_main_mul70_CAST_add78')
C8_main_mul70_CAST_add78 = solver.IntVar(0, 1, 'C8_main_mul70_CAST_add78')
solver.Add( + (1)*main_mul70_fixp + (1)*main_mul70_CAST_add78_float + (-1)*C3_main_mul70_CAST_add78<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul70_CAST_add78
solver.Add( + (1)*main_mul70_float + (1)*main_mul70_CAST_add78_fixp + (-1)*C4_main_mul70_CAST_add78<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul70_CAST_add78
solver.Add( + (1)*main_mul70_fixp + (1)*main_mul70_CAST_add78_double + (-1)*C5_main_mul70_CAST_add78<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul70_CAST_add78
solver.Add( + (1)*main_mul70_double + (1)*main_mul70_CAST_add78_fixp + (-1)*C6_main_mul70_CAST_add78<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul70_CAST_add78
solver.Add( + (1)*main_mul70_float + (1)*main_mul70_CAST_add78_double + (-1)*C7_main_mul70_CAST_add78<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul70_CAST_add78
solver.Add( + (1)*main_mul70_double + (1)*main_mul70_CAST_add78_float + (-1)*C8_main_mul70_CAST_add78<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul70_CAST_add78



#Constraint for cast for   %add78 = fadd double %mul70, %mul77, !taffo.info !106, !taffo.initweight !51
main_mul77_CAST_add78_fixbits = solver.IntVar(0, 20, 'main_mul77_CAST_add78_fixbits')
main_mul77_CAST_add78_fixp = solver.IntVar(0, 1, 'main_mul77_CAST_add78_fixp')
main_mul77_CAST_add78_float = solver.IntVar(0, 1, 'main_mul77_CAST_add78_float')
main_mul77_CAST_add78_double = solver.IntVar(0, 1, 'main_mul77_CAST_add78_double')
solver.Add( + (1)*main_mul77_CAST_add78_fixp + (1)*main_mul77_CAST_add78_float + (1)*main_mul77_CAST_add78_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul77_CAST_add78_fixbits + (-10000)*main_mul77_CAST_add78_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C1_main_mul77_CAST_add78')
C2_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C2_main_mul77_CAST_add78')
solver.Add( + (1)*main_mul77_fixbits + (-1)*main_mul77_CAST_add78_fixbits + (-10000)*C1_main_mul77_CAST_add78<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul77_fixbits + (1)*main_mul77_CAST_add78_fixbits + (-10000)*C2_main_mul77_CAST_add78<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul77_CAST_add78
castCostObj +=  + (1)*C2_main_mul77_CAST_add78
C3_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C3_main_mul77_CAST_add78')
C4_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C4_main_mul77_CAST_add78')
C5_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C5_main_mul77_CAST_add78')
C6_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C6_main_mul77_CAST_add78')
C7_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C7_main_mul77_CAST_add78')
C8_main_mul77_CAST_add78 = solver.IntVar(0, 1, 'C8_main_mul77_CAST_add78')
solver.Add( + (1)*main_mul77_fixp + (1)*main_mul77_CAST_add78_float + (-1)*C3_main_mul77_CAST_add78<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul77_CAST_add78
solver.Add( + (1)*main_mul77_float + (1)*main_mul77_CAST_add78_fixp + (-1)*C4_main_mul77_CAST_add78<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul77_CAST_add78
solver.Add( + (1)*main_mul77_fixp + (1)*main_mul77_CAST_add78_double + (-1)*C5_main_mul77_CAST_add78<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul77_CAST_add78
solver.Add( + (1)*main_mul77_double + (1)*main_mul77_CAST_add78_fixp + (-1)*C6_main_mul77_CAST_add78<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul77_CAST_add78
solver.Add( + (1)*main_mul77_float + (1)*main_mul77_CAST_add78_double + (-1)*C7_main_mul77_CAST_add78<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul77_CAST_add78
solver.Add( + (1)*main_mul77_double + (1)*main_mul77_CAST_add78_float + (-1)*C8_main_mul77_CAST_add78<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul77_CAST_add78



#Stuff for   %add78 = fadd double %mul70, %mul77, !taffo.info !106, !taffo.initweight !51
main_add78_fixbits = solver.IntVar(0, 19, 'main_add78_fixbits')
main_add78_fixp = solver.IntVar(0, 1, 'main_add78_fixp')
main_add78_float = solver.IntVar(0, 1, 'main_add78_float')
main_add78_double = solver.IntVar(0, 1, 'main_add78_double')
main_add78_enob = solver.IntVar(-10000, 10000, 'main_add78_enob')
solver.Add( + (1)*main_add78_enob + (-1)*main_add78_fixbits + (10000)*main_add78_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add78_enob + (10000)*main_add78_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add78_enob + (10000)*main_add78_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add78_fixbits + (-10000)*main_add78_fixp>=-9982)    #Limit the lower number of frac bits19
solver.Add( + (1)*main_add78_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add78_enob
solver.Add( + (1)*main_add78_fixp + (1)*main_add78_float + (1)*main_add78_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add78_fixbits + (-10000)*main_add78_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul70_CAST_add78_fixp + (-1)*main_mul77_CAST_add78_fixp==0)    #fix equality
solver.Add( + (1)*main_mul70_CAST_add78_float + (-1)*main_mul77_CAST_add78_float==0)    #float equality
solver.Add( + (1)*main_mul70_CAST_add78_double + (-1)*main_mul77_CAST_add78_double==0)    #double equality
solver.Add( + (1)*main_mul70_CAST_add78_fixbits + (-1)*main_mul77_CAST_add78_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul70_CAST_add78_fixp + (-1)*main_add78_fixp==0)    #fix equality
solver.Add( + (1)*main_mul70_CAST_add78_float + (-1)*main_add78_float==0)    #float equality
solver.Add( + (1)*main_mul70_CAST_add78_double + (-1)*main_add78_double==0)    #double equality
solver.Add( + (1)*main_mul70_CAST_add78_fixbits + (-1)*main_add78_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add78_fixp
mathCostObj +=  + (3)*main_add78_float
mathCostObj +=  + (6.64928)*main_add78_double
solver.Add( + (1)*main_add78_enob + (-1)*main_mul70_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add78_enob + (-1)*main_mul77_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
f_enob_memphi_main_tmp23 = solver.IntVar(-10000, 10000, 'f_enob_memphi_main_tmp23')
solver.Add( + (1)*f_enob_memphi_main_tmp23 + (-1)*f_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp23_enob_0 = solver.IntVar(0, 1, 'main_main_tmp23_enob_0')
solver.Add( + (1)*main_main_tmp23_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*f_enob_memphi_main_tmp23 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp23_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_u_enob_memphi_main_tmp24 = solver.IntVar(-10000, 10000, 'main_u_enob_memphi_main_tmp24')
solver.Add( + (1)*main_u_enob_memphi_main_tmp24 + (-1)*main_u_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp24_enob_0 = solver.IntVar(0, 1, 'main_main_tmp24_enob_0')
main_main_tmp24_enob_1 = solver.IntVar(0, 1, 'main_main_tmp24_enob_1')
main_main_tmp24_enob_2 = solver.IntVar(0, 1, 'main_main_tmp24_enob_2')
main_main_tmp24_enob_3 = solver.IntVar(0, 1, 'main_main_tmp24_enob_3')
main_main_tmp24_enob_4 = solver.IntVar(0, 1, 'main_main_tmp24_enob_4')
solver.Add( + (1)*main_main_tmp24_enob_0 + (1)*main_main_tmp24_enob_1 + (1)*main_main_tmp24_enob_2 + (1)*main_main_tmp24_enob_3 + (1)*main_main_tmp24_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp24 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp24_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul84 = fmul double %tmp23, %tmp24, !taffo.info !100, !taffo.initweight !44
f_CAST_mul84_fixbits = solver.IntVar(0, 23, 'f_CAST_mul84_fixbits')
f_CAST_mul84_fixp = solver.IntVar(0, 1, 'f_CAST_mul84_fixp')
f_CAST_mul84_float = solver.IntVar(0, 1, 'f_CAST_mul84_float')
f_CAST_mul84_double = solver.IntVar(0, 1, 'f_CAST_mul84_double')
solver.Add( + (1)*f_CAST_mul84_fixp + (1)*f_CAST_mul84_float + (1)*f_CAST_mul84_double==1)    #exactly 1 type
solver.Add( + (1)*f_CAST_mul84_fixbits + (-10000)*f_CAST_mul84_fixp<=0)    #If no fix, fix frac part = 0
C1_f_CAST_mul84 = solver.IntVar(0, 1, 'C1_f_CAST_mul84')
C2_f_CAST_mul84 = solver.IntVar(0, 1, 'C2_f_CAST_mul84')
solver.Add( + (1)*f_fixbits + (-1)*f_CAST_mul84_fixbits + (-10000)*C1_f_CAST_mul84<=0)    #Shift cost 1
solver.Add( + (-1)*f_fixbits + (1)*f_CAST_mul84_fixbits + (-10000)*C2_f_CAST_mul84<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_f_CAST_mul84
castCostObj +=  + (1)*C2_f_CAST_mul84
C3_f_CAST_mul84 = solver.IntVar(0, 1, 'C3_f_CAST_mul84')
C4_f_CAST_mul84 = solver.IntVar(0, 1, 'C4_f_CAST_mul84')
C5_f_CAST_mul84 = solver.IntVar(0, 1, 'C5_f_CAST_mul84')
C6_f_CAST_mul84 = solver.IntVar(0, 1, 'C6_f_CAST_mul84')
C7_f_CAST_mul84 = solver.IntVar(0, 1, 'C7_f_CAST_mul84')
C8_f_CAST_mul84 = solver.IntVar(0, 1, 'C8_f_CAST_mul84')
solver.Add( + (1)*f_fixp + (1)*f_CAST_mul84_float + (-1)*C3_f_CAST_mul84<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_f_CAST_mul84
solver.Add( + (1)*f_float + (1)*f_CAST_mul84_fixp + (-1)*C4_f_CAST_mul84<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_f_CAST_mul84
solver.Add( + (1)*f_fixp + (1)*f_CAST_mul84_double + (-1)*C5_f_CAST_mul84<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_f_CAST_mul84
solver.Add( + (1)*f_double + (1)*f_CAST_mul84_fixp + (-1)*C6_f_CAST_mul84<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_f_CAST_mul84
solver.Add( + (1)*f_float + (1)*f_CAST_mul84_double + (-1)*C7_f_CAST_mul84<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_f_CAST_mul84
solver.Add( + (1)*f_double + (1)*f_CAST_mul84_float + (-1)*C8_f_CAST_mul84<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_f_CAST_mul84



#Constraint for cast for   %mul84 = fmul double %tmp23, %tmp24, !taffo.info !100, !taffo.initweight !44
main_u_CAST_mul84_fixbits = solver.IntVar(0, 28, 'main_u_CAST_mul84_fixbits')
main_u_CAST_mul84_fixp = solver.IntVar(0, 1, 'main_u_CAST_mul84_fixp')
main_u_CAST_mul84_float = solver.IntVar(0, 1, 'main_u_CAST_mul84_float')
main_u_CAST_mul84_double = solver.IntVar(0, 1, 'main_u_CAST_mul84_double')
solver.Add( + (1)*main_u_CAST_mul84_fixp + (1)*main_u_CAST_mul84_float + (1)*main_u_CAST_mul84_double==1)    #exactly 1 type
solver.Add( + (1)*main_u_CAST_mul84_fixbits + (-10000)*main_u_CAST_mul84_fixp<=0)    #If no fix, fix frac part = 0
C1_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C1_main_u_CAST_mul84')
C2_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C2_main_u_CAST_mul84')
solver.Add( + (1)*main_u_fixbits + (-1)*main_u_CAST_mul84_fixbits + (-10000)*C1_main_u_CAST_mul84<=0)    #Shift cost 1
solver.Add( + (-1)*main_u_fixbits + (1)*main_u_CAST_mul84_fixbits + (-10000)*C2_main_u_CAST_mul84<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_u_CAST_mul84
castCostObj +=  + (1)*C2_main_u_CAST_mul84
C3_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C3_main_u_CAST_mul84')
C4_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C4_main_u_CAST_mul84')
C5_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C5_main_u_CAST_mul84')
C6_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C6_main_u_CAST_mul84')
C7_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C7_main_u_CAST_mul84')
C8_main_u_CAST_mul84 = solver.IntVar(0, 1, 'C8_main_u_CAST_mul84')
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul84_float + (-1)*C3_main_u_CAST_mul84<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_u_CAST_mul84
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul84_fixp + (-1)*C4_main_u_CAST_mul84<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_u_CAST_mul84
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul84_double + (-1)*C5_main_u_CAST_mul84<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_u_CAST_mul84
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul84_fixp + (-1)*C6_main_u_CAST_mul84<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_u_CAST_mul84
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul84_double + (-1)*C7_main_u_CAST_mul84<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_u_CAST_mul84
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul84_float + (-1)*C8_main_u_CAST_mul84<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_u_CAST_mul84



#Stuff for   %mul84 = fmul double %tmp23, %tmp24, !taffo.info !100, !taffo.initweight !44
main_mul84_fixbits = solver.IntVar(0, 21, 'main_mul84_fixbits')
main_mul84_fixp = solver.IntVar(0, 1, 'main_mul84_fixp')
main_mul84_float = solver.IntVar(0, 1, 'main_mul84_float')
main_mul84_double = solver.IntVar(0, 1, 'main_mul84_double')
main_mul84_enob = solver.IntVar(-10000, 10000, 'main_mul84_enob')
solver.Add( + (1)*main_mul84_enob + (-1)*main_mul84_fixbits + (10000)*main_mul84_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul84_enob + (10000)*main_mul84_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul84_enob + (10000)*main_mul84_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul84_fixbits + (-10000)*main_mul84_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_mul84_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul84_enob
solver.Add( + (1)*main_mul84_fixp + (1)*main_mul84_float + (1)*main_mul84_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul84_fixbits + (-10000)*main_mul84_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*f_CAST_mul84_fixp + (-1)*main_u_CAST_mul84_fixp==0)    #fix equality
solver.Add( + (1)*f_CAST_mul84_float + (-1)*main_u_CAST_mul84_float==0)    #float equality
solver.Add( + (1)*f_CAST_mul84_double + (-1)*main_u_CAST_mul84_double==0)    #double equality
solver.Add( + (1)*f_CAST_mul84_fixp + (-1)*main_mul84_fixp==0)    #fix equality
solver.Add( + (1)*f_CAST_mul84_float + (-1)*main_mul84_float==0)    #float equality
solver.Add( + (1)*f_CAST_mul84_double + (-1)*main_mul84_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul84_fixp
mathCostObj +=  + (6)*main_mul84_float
mathCostObj +=  + (12.2551)*main_mul84_double
main_main_mul84_enob_1 = solver.IntVar(0, 1, 'main_main_mul84_enob_1')
main_main_mul84_enob_2 = solver.IntVar(0, 1, 'main_main_mul84_enob_2')
solver.Add( + (1)*main_main_mul84_enob_1 + (1)*main_main_mul84_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul84_enob + (-1)*main_u_enob_memphi_main_tmp24 + (-10000)*main_main_mul84_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul84_enob + (-1)*f_enob_memphi_main_tmp23 + (-10000)*main_main_mul84_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub85 = fsub double %add78, %mul84, !taffo.info !109, !taffo.initweight !45
main_add78_CAST_sub85_fixbits = solver.IntVar(0, 19, 'main_add78_CAST_sub85_fixbits')
main_add78_CAST_sub85_fixp = solver.IntVar(0, 1, 'main_add78_CAST_sub85_fixp')
main_add78_CAST_sub85_float = solver.IntVar(0, 1, 'main_add78_CAST_sub85_float')
main_add78_CAST_sub85_double = solver.IntVar(0, 1, 'main_add78_CAST_sub85_double')
solver.Add( + (1)*main_add78_CAST_sub85_fixp + (1)*main_add78_CAST_sub85_float + (1)*main_add78_CAST_sub85_double==1)    #exactly 1 type
solver.Add( + (1)*main_add78_CAST_sub85_fixbits + (-10000)*main_add78_CAST_sub85_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C1_main_add78_CAST_sub85')
C2_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C2_main_add78_CAST_sub85')
solver.Add( + (1)*main_add78_fixbits + (-1)*main_add78_CAST_sub85_fixbits + (-10000)*C1_main_add78_CAST_sub85<=0)    #Shift cost 1
solver.Add( + (-1)*main_add78_fixbits + (1)*main_add78_CAST_sub85_fixbits + (-10000)*C2_main_add78_CAST_sub85<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add78_CAST_sub85
castCostObj +=  + (1)*C2_main_add78_CAST_sub85
C3_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C3_main_add78_CAST_sub85')
C4_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C4_main_add78_CAST_sub85')
C5_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C5_main_add78_CAST_sub85')
C6_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C6_main_add78_CAST_sub85')
C7_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C7_main_add78_CAST_sub85')
C8_main_add78_CAST_sub85 = solver.IntVar(0, 1, 'C8_main_add78_CAST_sub85')
solver.Add( + (1)*main_add78_fixp + (1)*main_add78_CAST_sub85_float + (-1)*C3_main_add78_CAST_sub85<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add78_CAST_sub85
solver.Add( + (1)*main_add78_float + (1)*main_add78_CAST_sub85_fixp + (-1)*C4_main_add78_CAST_sub85<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add78_CAST_sub85
solver.Add( + (1)*main_add78_fixp + (1)*main_add78_CAST_sub85_double + (-1)*C5_main_add78_CAST_sub85<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add78_CAST_sub85
solver.Add( + (1)*main_add78_double + (1)*main_add78_CAST_sub85_fixp + (-1)*C6_main_add78_CAST_sub85<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add78_CAST_sub85
solver.Add( + (1)*main_add78_float + (1)*main_add78_CAST_sub85_double + (-1)*C7_main_add78_CAST_sub85<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add78_CAST_sub85
solver.Add( + (1)*main_add78_double + (1)*main_add78_CAST_sub85_float + (-1)*C8_main_add78_CAST_sub85<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add78_CAST_sub85



#Constraint for cast for   %sub85 = fsub double %add78, %mul84, !taffo.info !109, !taffo.initweight !45
main_mul84_CAST_sub85_fixbits = solver.IntVar(0, 21, 'main_mul84_CAST_sub85_fixbits')
main_mul84_CAST_sub85_fixp = solver.IntVar(0, 1, 'main_mul84_CAST_sub85_fixp')
main_mul84_CAST_sub85_float = solver.IntVar(0, 1, 'main_mul84_CAST_sub85_float')
main_mul84_CAST_sub85_double = solver.IntVar(0, 1, 'main_mul84_CAST_sub85_double')
solver.Add( + (1)*main_mul84_CAST_sub85_fixp + (1)*main_mul84_CAST_sub85_float + (1)*main_mul84_CAST_sub85_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul84_CAST_sub85_fixbits + (-10000)*main_mul84_CAST_sub85_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C1_main_mul84_CAST_sub85')
C2_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C2_main_mul84_CAST_sub85')
solver.Add( + (1)*main_mul84_fixbits + (-1)*main_mul84_CAST_sub85_fixbits + (-10000)*C1_main_mul84_CAST_sub85<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul84_fixbits + (1)*main_mul84_CAST_sub85_fixbits + (-10000)*C2_main_mul84_CAST_sub85<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul84_CAST_sub85
castCostObj +=  + (1)*C2_main_mul84_CAST_sub85
C3_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C3_main_mul84_CAST_sub85')
C4_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C4_main_mul84_CAST_sub85')
C5_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C5_main_mul84_CAST_sub85')
C6_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C6_main_mul84_CAST_sub85')
C7_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C7_main_mul84_CAST_sub85')
C8_main_mul84_CAST_sub85 = solver.IntVar(0, 1, 'C8_main_mul84_CAST_sub85')
solver.Add( + (1)*main_mul84_fixp + (1)*main_mul84_CAST_sub85_float + (-1)*C3_main_mul84_CAST_sub85<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul84_CAST_sub85
solver.Add( + (1)*main_mul84_float + (1)*main_mul84_CAST_sub85_fixp + (-1)*C4_main_mul84_CAST_sub85<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul84_CAST_sub85
solver.Add( + (1)*main_mul84_fixp + (1)*main_mul84_CAST_sub85_double + (-1)*C5_main_mul84_CAST_sub85<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul84_CAST_sub85
solver.Add( + (1)*main_mul84_double + (1)*main_mul84_CAST_sub85_fixp + (-1)*C6_main_mul84_CAST_sub85<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul84_CAST_sub85
solver.Add( + (1)*main_mul84_float + (1)*main_mul84_CAST_sub85_double + (-1)*C7_main_mul84_CAST_sub85<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul84_CAST_sub85
solver.Add( + (1)*main_mul84_double + (1)*main_mul84_CAST_sub85_float + (-1)*C8_main_mul84_CAST_sub85<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul84_CAST_sub85



#Stuff for   %sub85 = fsub double %add78, %mul84, !taffo.info !109, !taffo.initweight !45
main_sub85_fixbits = solver.IntVar(0, 19, 'main_sub85_fixbits')
main_sub85_fixp = solver.IntVar(0, 1, 'main_sub85_fixp')
main_sub85_float = solver.IntVar(0, 1, 'main_sub85_float')
main_sub85_double = solver.IntVar(0, 1, 'main_sub85_double')
main_sub85_enob = solver.IntVar(-10000, 10000, 'main_sub85_enob')
solver.Add( + (1)*main_sub85_enob + (-1)*main_sub85_fixbits + (10000)*main_sub85_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub85_enob + (10000)*main_sub85_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub85_enob + (10000)*main_sub85_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub85_fixbits + (-10000)*main_sub85_fixp>=-9982)    #Limit the lower number of frac bits19
solver.Add( + (1)*main_sub85_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub85_enob
solver.Add( + (1)*main_sub85_fixp + (1)*main_sub85_float + (1)*main_sub85_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub85_fixbits + (-10000)*main_sub85_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add78_CAST_sub85_fixp + (-1)*main_mul84_CAST_sub85_fixp==0)    #fix equality
solver.Add( + (1)*main_add78_CAST_sub85_float + (-1)*main_mul84_CAST_sub85_float==0)    #float equality
solver.Add( + (1)*main_add78_CAST_sub85_double + (-1)*main_mul84_CAST_sub85_double==0)    #double equality
solver.Add( + (1)*main_add78_CAST_sub85_fixbits + (-1)*main_mul84_CAST_sub85_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add78_CAST_sub85_fixp + (-1)*main_sub85_fixp==0)    #fix equality
solver.Add( + (1)*main_add78_CAST_sub85_float + (-1)*main_sub85_float==0)    #float equality
solver.Add( + (1)*main_add78_CAST_sub85_double + (-1)*main_sub85_double==0)    #double equality
solver.Add( + (1)*main_add78_CAST_sub85_fixbits + (-1)*main_sub85_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub85_fixp
mathCostObj +=  + (3)*main_sub85_float
mathCostObj +=  + (6.64928)*main_sub85_double
solver.Add( + (1)*main_sub85_enob + (-1)*main_add78_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub85_enob + (-1)*main_mul84_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp25 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp25')
solver.Add( + (1)*a_enob_memphi_main_tmp25 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp25_enob_0 = solver.IntVar(0, 1, 'main_main_tmp25_enob_0')
solver.Add( + (1)*main_main_tmp25_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp25 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp25_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_q_enob_memphi_main_tmp26 = solver.IntVar(-10000, 10000, 'main_q_enob_memphi_main_tmp26')
solver.Add( + (1)*main_q_enob_memphi_main_tmp26 + (-1)*main_q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp26_enob_0 = solver.IntVar(0, 1, 'main_main_tmp26_enob_0')
solver.Add( + (1)*main_main_tmp26_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp26 + (-1)*main_q_enob_storeENOB + (10000)*main_main_tmp26_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul91 = fmul double %tmp25, %tmp26, !taffo.info !111, !taffo.initweight !44
a_CAST_mul91_fixbits = solver.IntVar(0, 22, 'a_CAST_mul91_fixbits')
a_CAST_mul91_fixp = solver.IntVar(0, 1, 'a_CAST_mul91_fixp')
a_CAST_mul91_float = solver.IntVar(0, 1, 'a_CAST_mul91_float')
a_CAST_mul91_double = solver.IntVar(0, 1, 'a_CAST_mul91_double')
solver.Add( + (1)*a_CAST_mul91_fixp + (1)*a_CAST_mul91_float + (1)*a_CAST_mul91_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_mul91_fixbits + (-10000)*a_CAST_mul91_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_mul91 = solver.IntVar(0, 1, 'C1_a_CAST_mul91')
C2_a_CAST_mul91 = solver.IntVar(0, 1, 'C2_a_CAST_mul91')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_mul91_fixbits + (-10000)*C1_a_CAST_mul91<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_mul91_fixbits + (-10000)*C2_a_CAST_mul91<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_a_CAST_mul91
castCostObj +=  + (1)*C2_a_CAST_mul91
C3_a_CAST_mul91 = solver.IntVar(0, 1, 'C3_a_CAST_mul91')
C4_a_CAST_mul91 = solver.IntVar(0, 1, 'C4_a_CAST_mul91')
C5_a_CAST_mul91 = solver.IntVar(0, 1, 'C5_a_CAST_mul91')
C6_a_CAST_mul91 = solver.IntVar(0, 1, 'C6_a_CAST_mul91')
C7_a_CAST_mul91 = solver.IntVar(0, 1, 'C7_a_CAST_mul91')
C8_a_CAST_mul91 = solver.IntVar(0, 1, 'C8_a_CAST_mul91')
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul91_float + (-1)*C3_a_CAST_mul91<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_a_CAST_mul91
solver.Add( + (1)*a_float + (1)*a_CAST_mul91_fixp + (-1)*C4_a_CAST_mul91<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_a_CAST_mul91
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul91_double + (-1)*C5_a_CAST_mul91<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_a_CAST_mul91
solver.Add( + (1)*a_double + (1)*a_CAST_mul91_fixp + (-1)*C6_a_CAST_mul91<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_a_CAST_mul91
solver.Add( + (1)*a_float + (1)*a_CAST_mul91_double + (-1)*C7_a_CAST_mul91<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_a_CAST_mul91
solver.Add( + (1)*a_double + (1)*a_CAST_mul91_float + (-1)*C8_a_CAST_mul91<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_a_CAST_mul91



#Constraint for cast for   %mul91 = fmul double %tmp25, %tmp26, !taffo.info !111, !taffo.initweight !44
main_q_CAST_mul91_fixbits = solver.IntVar(0, 22, 'main_q_CAST_mul91_fixbits')
main_q_CAST_mul91_fixp = solver.IntVar(0, 1, 'main_q_CAST_mul91_fixp')
main_q_CAST_mul91_float = solver.IntVar(0, 1, 'main_q_CAST_mul91_float')
main_q_CAST_mul91_double = solver.IntVar(0, 1, 'main_q_CAST_mul91_double')
solver.Add( + (1)*main_q_CAST_mul91_fixp + (1)*main_q_CAST_mul91_float + (1)*main_q_CAST_mul91_double==1)    #exactly 1 type
solver.Add( + (1)*main_q_CAST_mul91_fixbits + (-10000)*main_q_CAST_mul91_fixp<=0)    #If no fix, fix frac part = 0
C1_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C1_main_q_CAST_mul91')
C2_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C2_main_q_CAST_mul91')
solver.Add( + (1)*main_q_fixbits + (-1)*main_q_CAST_mul91_fixbits + (-10000)*C1_main_q_CAST_mul91<=0)    #Shift cost 1
solver.Add( + (-1)*main_q_fixbits + (1)*main_q_CAST_mul91_fixbits + (-10000)*C2_main_q_CAST_mul91<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_q_CAST_mul91
castCostObj +=  + (1)*C2_main_q_CAST_mul91
C3_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C3_main_q_CAST_mul91')
C4_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C4_main_q_CAST_mul91')
C5_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C5_main_q_CAST_mul91')
C6_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C6_main_q_CAST_mul91')
C7_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C7_main_q_CAST_mul91')
C8_main_q_CAST_mul91 = solver.IntVar(0, 1, 'C8_main_q_CAST_mul91')
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_mul91_float + (-1)*C3_main_q_CAST_mul91<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_q_CAST_mul91
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_mul91_fixp + (-1)*C4_main_q_CAST_mul91<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_q_CAST_mul91
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_mul91_double + (-1)*C5_main_q_CAST_mul91<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_q_CAST_mul91
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_mul91_fixp + (-1)*C6_main_q_CAST_mul91<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_q_CAST_mul91
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_mul91_double + (-1)*C7_main_q_CAST_mul91<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_q_CAST_mul91
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_mul91_float + (-1)*C8_main_q_CAST_mul91<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_q_CAST_mul91



#Stuff for   %mul91 = fmul double %tmp25, %tmp26, !taffo.info !111, !taffo.initweight !44
main_mul91_fixbits = solver.IntVar(0, 13, 'main_mul91_fixbits')
main_mul91_fixp = solver.IntVar(0, 1, 'main_mul91_fixp')
main_mul91_float = solver.IntVar(0, 1, 'main_mul91_float')
main_mul91_double = solver.IntVar(0, 1, 'main_mul91_double')
main_mul91_enob = solver.IntVar(-10000, 10000, 'main_mul91_enob')
solver.Add( + (1)*main_mul91_enob + (-1)*main_mul91_fixbits + (10000)*main_mul91_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul91_enob + (10000)*main_mul91_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul91_enob + (10000)*main_mul91_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul91_fixbits + (-10000)*main_mul91_fixp>=-9988)    #Limit the lower number of frac bits13
solver.Add( + (1)*main_mul91_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul91_enob
solver.Add( + (1)*main_mul91_fixp + (1)*main_mul91_float + (1)*main_mul91_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul91_fixbits + (-10000)*main_mul91_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*a_CAST_mul91_fixp + (-1)*main_q_CAST_mul91_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_mul91_float + (-1)*main_q_CAST_mul91_float==0)    #float equality
solver.Add( + (1)*a_CAST_mul91_double + (-1)*main_q_CAST_mul91_double==0)    #double equality
solver.Add( + (1)*a_CAST_mul91_fixp + (-1)*main_mul91_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_mul91_float + (-1)*main_mul91_float==0)    #float equality
solver.Add( + (1)*a_CAST_mul91_double + (-1)*main_mul91_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul91_fixp
mathCostObj +=  + (6)*main_mul91_float
mathCostObj +=  + (12.2551)*main_mul91_double
main_main_mul91_enob_1 = solver.IntVar(0, 1, 'main_main_mul91_enob_1')
main_main_mul91_enob_2 = solver.IntVar(0, 1, 'main_main_mul91_enob_2')
solver.Add( + (1)*main_main_mul91_enob_1 + (1)*main_main_mul91_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul91_enob + (-1)*main_q_enob_memphi_main_tmp26 + (-10000)*main_main_mul91_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul91_enob + (-1)*a_enob_memphi_main_tmp25 + (-10000)*main_main_mul91_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub92 = fsub double %sub85, %mul91, !taffo.info !113, !taffo.initweight !45
main_sub85_CAST_sub92_fixbits = solver.IntVar(0, 19, 'main_sub85_CAST_sub92_fixbits')
main_sub85_CAST_sub92_fixp = solver.IntVar(0, 1, 'main_sub85_CAST_sub92_fixp')
main_sub85_CAST_sub92_float = solver.IntVar(0, 1, 'main_sub85_CAST_sub92_float')
main_sub85_CAST_sub92_double = solver.IntVar(0, 1, 'main_sub85_CAST_sub92_double')
solver.Add( + (1)*main_sub85_CAST_sub92_fixp + (1)*main_sub85_CAST_sub92_float + (1)*main_sub85_CAST_sub92_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub85_CAST_sub92_fixbits + (-10000)*main_sub85_CAST_sub92_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C1_main_sub85_CAST_sub92')
C2_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C2_main_sub85_CAST_sub92')
solver.Add( + (1)*main_sub85_fixbits + (-1)*main_sub85_CAST_sub92_fixbits + (-10000)*C1_main_sub85_CAST_sub92<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub85_fixbits + (1)*main_sub85_CAST_sub92_fixbits + (-10000)*C2_main_sub85_CAST_sub92<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub85_CAST_sub92
castCostObj +=  + (1)*C2_main_sub85_CAST_sub92
C3_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C3_main_sub85_CAST_sub92')
C4_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C4_main_sub85_CAST_sub92')
C5_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C5_main_sub85_CAST_sub92')
C6_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C6_main_sub85_CAST_sub92')
C7_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C7_main_sub85_CAST_sub92')
C8_main_sub85_CAST_sub92 = solver.IntVar(0, 1, 'C8_main_sub85_CAST_sub92')
solver.Add( + (1)*main_sub85_fixp + (1)*main_sub85_CAST_sub92_float + (-1)*C3_main_sub85_CAST_sub92<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub85_CAST_sub92
solver.Add( + (1)*main_sub85_float + (1)*main_sub85_CAST_sub92_fixp + (-1)*C4_main_sub85_CAST_sub92<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub85_CAST_sub92
solver.Add( + (1)*main_sub85_fixp + (1)*main_sub85_CAST_sub92_double + (-1)*C5_main_sub85_CAST_sub92<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub85_CAST_sub92
solver.Add( + (1)*main_sub85_double + (1)*main_sub85_CAST_sub92_fixp + (-1)*C6_main_sub85_CAST_sub92<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub85_CAST_sub92
solver.Add( + (1)*main_sub85_float + (1)*main_sub85_CAST_sub92_double + (-1)*C7_main_sub85_CAST_sub92<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub85_CAST_sub92
solver.Add( + (1)*main_sub85_double + (1)*main_sub85_CAST_sub92_float + (-1)*C8_main_sub85_CAST_sub92<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub85_CAST_sub92



#Constraint for cast for   %sub92 = fsub double %sub85, %mul91, !taffo.info !113, !taffo.initweight !45
main_mul91_CAST_sub92_fixbits = solver.IntVar(0, 13, 'main_mul91_CAST_sub92_fixbits')
main_mul91_CAST_sub92_fixp = solver.IntVar(0, 1, 'main_mul91_CAST_sub92_fixp')
main_mul91_CAST_sub92_float = solver.IntVar(0, 1, 'main_mul91_CAST_sub92_float')
main_mul91_CAST_sub92_double = solver.IntVar(0, 1, 'main_mul91_CAST_sub92_double')
solver.Add( + (1)*main_mul91_CAST_sub92_fixp + (1)*main_mul91_CAST_sub92_float + (1)*main_mul91_CAST_sub92_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul91_CAST_sub92_fixbits + (-10000)*main_mul91_CAST_sub92_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C1_main_mul91_CAST_sub92')
C2_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C2_main_mul91_CAST_sub92')
solver.Add( + (1)*main_mul91_fixbits + (-1)*main_mul91_CAST_sub92_fixbits + (-10000)*C1_main_mul91_CAST_sub92<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul91_fixbits + (1)*main_mul91_CAST_sub92_fixbits + (-10000)*C2_main_mul91_CAST_sub92<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul91_CAST_sub92
castCostObj +=  + (1)*C2_main_mul91_CAST_sub92
C3_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C3_main_mul91_CAST_sub92')
C4_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C4_main_mul91_CAST_sub92')
C5_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C5_main_mul91_CAST_sub92')
C6_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C6_main_mul91_CAST_sub92')
C7_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C7_main_mul91_CAST_sub92')
C8_main_mul91_CAST_sub92 = solver.IntVar(0, 1, 'C8_main_mul91_CAST_sub92')
solver.Add( + (1)*main_mul91_fixp + (1)*main_mul91_CAST_sub92_float + (-1)*C3_main_mul91_CAST_sub92<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul91_CAST_sub92
solver.Add( + (1)*main_mul91_float + (1)*main_mul91_CAST_sub92_fixp + (-1)*C4_main_mul91_CAST_sub92<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul91_CAST_sub92
solver.Add( + (1)*main_mul91_fixp + (1)*main_mul91_CAST_sub92_double + (-1)*C5_main_mul91_CAST_sub92<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul91_CAST_sub92
solver.Add( + (1)*main_mul91_double + (1)*main_mul91_CAST_sub92_fixp + (-1)*C6_main_mul91_CAST_sub92<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul91_CAST_sub92
solver.Add( + (1)*main_mul91_float + (1)*main_mul91_CAST_sub92_double + (-1)*C7_main_mul91_CAST_sub92<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul91_CAST_sub92
solver.Add( + (1)*main_mul91_double + (1)*main_mul91_CAST_sub92_float + (-1)*C8_main_mul91_CAST_sub92<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul91_CAST_sub92



#Stuff for   %sub92 = fsub double %sub85, %mul91, !taffo.info !113, !taffo.initweight !45
main_sub92_fixbits = solver.IntVar(0, 13, 'main_sub92_fixbits')
main_sub92_fixp = solver.IntVar(0, 1, 'main_sub92_fixp')
main_sub92_float = solver.IntVar(0, 1, 'main_sub92_float')
main_sub92_double = solver.IntVar(0, 1, 'main_sub92_double')
main_sub92_enob = solver.IntVar(-10000, 10000, 'main_sub92_enob')
solver.Add( + (1)*main_sub92_enob + (-1)*main_sub92_fixbits + (10000)*main_sub92_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub92_enob + (10000)*main_sub92_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub92_enob + (10000)*main_sub92_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub92_fixbits + (-10000)*main_sub92_fixp>=-9988)    #Limit the lower number of frac bits13
solver.Add( + (1)*main_sub92_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub92_enob
solver.Add( + (1)*main_sub92_fixp + (1)*main_sub92_float + (1)*main_sub92_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub92_fixbits + (-10000)*main_sub92_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub85_CAST_sub92_fixp + (-1)*main_mul91_CAST_sub92_fixp==0)    #fix equality
solver.Add( + (1)*main_sub85_CAST_sub92_float + (-1)*main_mul91_CAST_sub92_float==0)    #float equality
solver.Add( + (1)*main_sub85_CAST_sub92_double + (-1)*main_mul91_CAST_sub92_double==0)    #double equality
solver.Add( + (1)*main_sub85_CAST_sub92_fixbits + (-1)*main_mul91_CAST_sub92_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub85_CAST_sub92_fixp + (-1)*main_sub92_fixp==0)    #fix equality
solver.Add( + (1)*main_sub85_CAST_sub92_float + (-1)*main_sub92_float==0)    #float equality
solver.Add( + (1)*main_sub85_CAST_sub92_double + (-1)*main_sub92_double==0)    #double equality
solver.Add( + (1)*main_sub85_CAST_sub92_fixbits + (-1)*main_sub92_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub92_fixp
mathCostObj +=  + (3)*main_sub92_float
mathCostObj +=  + (6.64928)*main_sub92_double
solver.Add( + (1)*main_sub92_enob + (-1)*main_sub85_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub92_enob + (-1)*main_mul91_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub92, double* %arrayidx96, align 8, !taffo.info !39, !taffo.initweight !45
main_sub92_CAST_store_fixbits = solver.IntVar(0, 13, 'main_sub92_CAST_store_fixbits')
main_sub92_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub92_CAST_store_fixp')
main_sub92_CAST_store_float = solver.IntVar(0, 1, 'main_sub92_CAST_store_float')
main_sub92_CAST_store_double = solver.IntVar(0, 1, 'main_sub92_CAST_store_double')
solver.Add( + (1)*main_sub92_CAST_store_fixp + (1)*main_sub92_CAST_store_float + (1)*main_sub92_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub92_CAST_store_fixbits + (-10000)*main_sub92_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub92_CAST_store = solver.IntVar(0, 1, 'C1_main_sub92_CAST_store')
C2_main_sub92_CAST_store = solver.IntVar(0, 1, 'C2_main_sub92_CAST_store')
solver.Add( + (1)*main_sub92_fixbits + (-1)*main_sub92_CAST_store_fixbits + (-10000)*C1_main_sub92_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub92_fixbits + (1)*main_sub92_CAST_store_fixbits + (-10000)*C2_main_sub92_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub92_CAST_store
castCostObj +=  + (1)*C2_main_sub92_CAST_store
C3_main_sub92_CAST_store = solver.IntVar(0, 1, 'C3_main_sub92_CAST_store')
C4_main_sub92_CAST_store = solver.IntVar(0, 1, 'C4_main_sub92_CAST_store')
C5_main_sub92_CAST_store = solver.IntVar(0, 1, 'C5_main_sub92_CAST_store')
C6_main_sub92_CAST_store = solver.IntVar(0, 1, 'C6_main_sub92_CAST_store')
C7_main_sub92_CAST_store = solver.IntVar(0, 1, 'C7_main_sub92_CAST_store')
C8_main_sub92_CAST_store = solver.IntVar(0, 1, 'C8_main_sub92_CAST_store')
solver.Add( + (1)*main_sub92_fixp + (1)*main_sub92_CAST_store_float + (-1)*C3_main_sub92_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub92_CAST_store
solver.Add( + (1)*main_sub92_float + (1)*main_sub92_CAST_store_fixp + (-1)*C4_main_sub92_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub92_CAST_store
solver.Add( + (1)*main_sub92_fixp + (1)*main_sub92_CAST_store_double + (-1)*C5_main_sub92_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub92_CAST_store
solver.Add( + (1)*main_sub92_double + (1)*main_sub92_CAST_store_fixp + (-1)*C6_main_sub92_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub92_CAST_store
solver.Add( + (1)*main_sub92_float + (1)*main_sub92_CAST_store_double + (-1)*C7_main_sub92_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub92_CAST_store
solver.Add( + (1)*main_sub92_double + (1)*main_sub92_CAST_store_float + (-1)*C8_main_sub92_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub92_CAST_store
solver.Add( + (1)*main_q_fixp + (-1)*main_sub92_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_q_float + (-1)*main_sub92_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_q_double + (-1)*main_sub92_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_q_fixbits + (-1)*main_sub92_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_q_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_q_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB + (-1)*main_q_fixbits + (10000)*main_q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB + (10000)*main_q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB + (10000)*main_q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB + (-1)*main_sub92_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp27 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp27')
solver.Add( + (1)*a_enob_memphi_main_tmp27 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp27_enob_0 = solver.IntVar(0, 1, 'main_main_tmp27_enob_0')
solver.Add( + (1)*main_main_tmp27_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp27 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp27_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_p_enob_memphi_main_tmp28 = solver.IntVar(-10000, 10000, 'main_p_enob_memphi_main_tmp28')
solver.Add( + (1)*main_p_enob_memphi_main_tmp28 + (-1)*main_p_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul102 = fmul double %tmp27, %tmp28, !taffo.info !92, !taffo.initweight !44
a_CAST_mul102_fixbits = solver.IntVar(0, 22, 'a_CAST_mul102_fixbits')
a_CAST_mul102_fixp = solver.IntVar(0, 1, 'a_CAST_mul102_fixp')
a_CAST_mul102_float = solver.IntVar(0, 1, 'a_CAST_mul102_float')
a_CAST_mul102_double = solver.IntVar(0, 1, 'a_CAST_mul102_double')
solver.Add( + (1)*a_CAST_mul102_fixp + (1)*a_CAST_mul102_float + (1)*a_CAST_mul102_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_mul102_fixbits + (-10000)*a_CAST_mul102_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_mul102 = solver.IntVar(0, 1, 'C1_a_CAST_mul102')
C2_a_CAST_mul102 = solver.IntVar(0, 1, 'C2_a_CAST_mul102')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_mul102_fixbits + (-10000)*C1_a_CAST_mul102<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_mul102_fixbits + (-10000)*C2_a_CAST_mul102<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_a_CAST_mul102
castCostObj +=  + (1)*C2_a_CAST_mul102
C3_a_CAST_mul102 = solver.IntVar(0, 1, 'C3_a_CAST_mul102')
C4_a_CAST_mul102 = solver.IntVar(0, 1, 'C4_a_CAST_mul102')
C5_a_CAST_mul102 = solver.IntVar(0, 1, 'C5_a_CAST_mul102')
C6_a_CAST_mul102 = solver.IntVar(0, 1, 'C6_a_CAST_mul102')
C7_a_CAST_mul102 = solver.IntVar(0, 1, 'C7_a_CAST_mul102')
C8_a_CAST_mul102 = solver.IntVar(0, 1, 'C8_a_CAST_mul102')
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul102_float + (-1)*C3_a_CAST_mul102<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_a_CAST_mul102
solver.Add( + (1)*a_float + (1)*a_CAST_mul102_fixp + (-1)*C4_a_CAST_mul102<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_a_CAST_mul102
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul102_double + (-1)*C5_a_CAST_mul102<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_a_CAST_mul102
solver.Add( + (1)*a_double + (1)*a_CAST_mul102_fixp + (-1)*C6_a_CAST_mul102<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_a_CAST_mul102
solver.Add( + (1)*a_float + (1)*a_CAST_mul102_double + (-1)*C7_a_CAST_mul102<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_a_CAST_mul102
solver.Add( + (1)*a_double + (1)*a_CAST_mul102_float + (-1)*C8_a_CAST_mul102<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_a_CAST_mul102



#Constraint for cast for   %mul102 = fmul double %tmp27, %tmp28, !taffo.info !92, !taffo.initweight !44
main_p_CAST_mul102_fixbits = solver.IntVar(0, 30, 'main_p_CAST_mul102_fixbits')
main_p_CAST_mul102_fixp = solver.IntVar(0, 1, 'main_p_CAST_mul102_fixp')
main_p_CAST_mul102_float = solver.IntVar(0, 1, 'main_p_CAST_mul102_float')
main_p_CAST_mul102_double = solver.IntVar(0, 1, 'main_p_CAST_mul102_double')
solver.Add( + (1)*main_p_CAST_mul102_fixp + (1)*main_p_CAST_mul102_float + (1)*main_p_CAST_mul102_double==1)    #exactly 1 type
solver.Add( + (1)*main_p_CAST_mul102_fixbits + (-10000)*main_p_CAST_mul102_fixp<=0)    #If no fix, fix frac part = 0
C1_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C1_main_p_CAST_mul102')
C2_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C2_main_p_CAST_mul102')
solver.Add( + (1)*main_p_fixbits + (-1)*main_p_CAST_mul102_fixbits + (-10000)*C1_main_p_CAST_mul102<=0)    #Shift cost 1
solver.Add( + (-1)*main_p_fixbits + (1)*main_p_CAST_mul102_fixbits + (-10000)*C2_main_p_CAST_mul102<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_p_CAST_mul102
castCostObj +=  + (1)*C2_main_p_CAST_mul102
C3_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C3_main_p_CAST_mul102')
C4_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C4_main_p_CAST_mul102')
C5_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C5_main_p_CAST_mul102')
C6_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C6_main_p_CAST_mul102')
C7_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C7_main_p_CAST_mul102')
C8_main_p_CAST_mul102 = solver.IntVar(0, 1, 'C8_main_p_CAST_mul102')
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul102_float + (-1)*C3_main_p_CAST_mul102<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_p_CAST_mul102
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul102_fixp + (-1)*C4_main_p_CAST_mul102<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_p_CAST_mul102
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul102_double + (-1)*C5_main_p_CAST_mul102<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_p_CAST_mul102
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul102_fixp + (-1)*C6_main_p_CAST_mul102<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_p_CAST_mul102
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul102_double + (-1)*C7_main_p_CAST_mul102<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_p_CAST_mul102
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul102_float + (-1)*C8_main_p_CAST_mul102<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_p_CAST_mul102



#Stuff for   %mul102 = fmul double %tmp27, %tmp28, !taffo.info !92, !taffo.initweight !44
main_mul102_fixbits = solver.IntVar(0, 22, 'main_mul102_fixbits')
main_mul102_fixp = solver.IntVar(0, 1, 'main_mul102_fixp')
main_mul102_float = solver.IntVar(0, 1, 'main_mul102_float')
main_mul102_double = solver.IntVar(0, 1, 'main_mul102_double')
main_mul102_enob = solver.IntVar(-10000, 10000, 'main_mul102_enob')
solver.Add( + (1)*main_mul102_enob + (-1)*main_mul102_fixbits + (10000)*main_mul102_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul102_enob + (10000)*main_mul102_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul102_enob + (10000)*main_mul102_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul102_fixbits + (-10000)*main_mul102_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_mul102_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul102_enob
solver.Add( + (1)*main_mul102_fixp + (1)*main_mul102_float + (1)*main_mul102_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul102_fixbits + (-10000)*main_mul102_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*a_CAST_mul102_fixp + (-1)*main_p_CAST_mul102_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_mul102_float + (-1)*main_p_CAST_mul102_float==0)    #float equality
solver.Add( + (1)*a_CAST_mul102_double + (-1)*main_p_CAST_mul102_double==0)    #double equality
solver.Add( + (1)*a_CAST_mul102_fixp + (-1)*main_mul102_fixp==0)    #fix equality
solver.Add( + (1)*a_CAST_mul102_float + (-1)*main_mul102_float==0)    #float equality
solver.Add( + (1)*a_CAST_mul102_double + (-1)*main_mul102_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul102_fixp
mathCostObj +=  + (6)*main_mul102_float
mathCostObj +=  + (12.2551)*main_mul102_double
main_main_mul102_enob_1 = solver.IntVar(0, 1, 'main_main_mul102_enob_1')
main_main_mul102_enob_2 = solver.IntVar(0, 1, 'main_main_mul102_enob_2')
solver.Add( + (1)*main_main_mul102_enob_1 + (1)*main_main_mul102_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul102_enob + (-1)*main_p_enob_memphi_main_tmp28 + (-10000)*main_main_mul102_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul102_enob + (-1)*a_enob_memphi_main_tmp27 + (-10000)*main_main_mul102_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
b_enob_memphi_main_tmp29 = solver.IntVar(-10000, 10000, 'b_enob_memphi_main_tmp29')
solver.Add( + (1)*b_enob_memphi_main_tmp29 + (-1)*b_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp29_enob_0 = solver.IntVar(0, 1, 'main_main_tmp29_enob_0')
solver.Add( + (1)*main_main_tmp29_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*b_enob_memphi_main_tmp29 + (-1)*b_enob_storeENOB + (10000)*main_main_tmp29_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add103 = fadd double %mul102, %tmp29, !taffo.info !94, !taffo.initweight !44
main_mul102_CAST_add103_fixbits = solver.IntVar(0, 22, 'main_mul102_CAST_add103_fixbits')
main_mul102_CAST_add103_fixp = solver.IntVar(0, 1, 'main_mul102_CAST_add103_fixp')
main_mul102_CAST_add103_float = solver.IntVar(0, 1, 'main_mul102_CAST_add103_float')
main_mul102_CAST_add103_double = solver.IntVar(0, 1, 'main_mul102_CAST_add103_double')
solver.Add( + (1)*main_mul102_CAST_add103_fixp + (1)*main_mul102_CAST_add103_float + (1)*main_mul102_CAST_add103_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul102_CAST_add103_fixbits + (-10000)*main_mul102_CAST_add103_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C1_main_mul102_CAST_add103')
C2_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C2_main_mul102_CAST_add103')
solver.Add( + (1)*main_mul102_fixbits + (-1)*main_mul102_CAST_add103_fixbits + (-10000)*C1_main_mul102_CAST_add103<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul102_fixbits + (1)*main_mul102_CAST_add103_fixbits + (-10000)*C2_main_mul102_CAST_add103<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul102_CAST_add103
castCostObj +=  + (1)*C2_main_mul102_CAST_add103
C3_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C3_main_mul102_CAST_add103')
C4_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C4_main_mul102_CAST_add103')
C5_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C5_main_mul102_CAST_add103')
C6_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C6_main_mul102_CAST_add103')
C7_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C7_main_mul102_CAST_add103')
C8_main_mul102_CAST_add103 = solver.IntVar(0, 1, 'C8_main_mul102_CAST_add103')
solver.Add( + (1)*main_mul102_fixp + (1)*main_mul102_CAST_add103_float + (-1)*C3_main_mul102_CAST_add103<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul102_CAST_add103
solver.Add( + (1)*main_mul102_float + (1)*main_mul102_CAST_add103_fixp + (-1)*C4_main_mul102_CAST_add103<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul102_CAST_add103
solver.Add( + (1)*main_mul102_fixp + (1)*main_mul102_CAST_add103_double + (-1)*C5_main_mul102_CAST_add103<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul102_CAST_add103
solver.Add( + (1)*main_mul102_double + (1)*main_mul102_CAST_add103_fixp + (-1)*C6_main_mul102_CAST_add103<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul102_CAST_add103
solver.Add( + (1)*main_mul102_float + (1)*main_mul102_CAST_add103_double + (-1)*C7_main_mul102_CAST_add103<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul102_CAST_add103
solver.Add( + (1)*main_mul102_double + (1)*main_mul102_CAST_add103_float + (-1)*C8_main_mul102_CAST_add103<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul102_CAST_add103



#Constraint for cast for   %add103 = fadd double %mul102, %tmp29, !taffo.info !94, !taffo.initweight !44
b_CAST_add103_fixbits = solver.IntVar(0, 22, 'b_CAST_add103_fixbits')
b_CAST_add103_fixp = solver.IntVar(0, 1, 'b_CAST_add103_fixp')
b_CAST_add103_float = solver.IntVar(0, 1, 'b_CAST_add103_float')
b_CAST_add103_double = solver.IntVar(0, 1, 'b_CAST_add103_double')
solver.Add( + (1)*b_CAST_add103_fixp + (1)*b_CAST_add103_float + (1)*b_CAST_add103_double==1)    #exactly 1 type
solver.Add( + (1)*b_CAST_add103_fixbits + (-10000)*b_CAST_add103_fixp<=0)    #If no fix, fix frac part = 0
C1_b_CAST_add103 = solver.IntVar(0, 1, 'C1_b_CAST_add103')
C2_b_CAST_add103 = solver.IntVar(0, 1, 'C2_b_CAST_add103')
solver.Add( + (1)*b_fixbits + (-1)*b_CAST_add103_fixbits + (-10000)*C1_b_CAST_add103<=0)    #Shift cost 1
solver.Add( + (-1)*b_fixbits + (1)*b_CAST_add103_fixbits + (-10000)*C2_b_CAST_add103<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_b_CAST_add103
castCostObj +=  + (1)*C2_b_CAST_add103
C3_b_CAST_add103 = solver.IntVar(0, 1, 'C3_b_CAST_add103')
C4_b_CAST_add103 = solver.IntVar(0, 1, 'C4_b_CAST_add103')
C5_b_CAST_add103 = solver.IntVar(0, 1, 'C5_b_CAST_add103')
C6_b_CAST_add103 = solver.IntVar(0, 1, 'C6_b_CAST_add103')
C7_b_CAST_add103 = solver.IntVar(0, 1, 'C7_b_CAST_add103')
C8_b_CAST_add103 = solver.IntVar(0, 1, 'C8_b_CAST_add103')
solver.Add( + (1)*b_fixp + (1)*b_CAST_add103_float + (-1)*C3_b_CAST_add103<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_b_CAST_add103
solver.Add( + (1)*b_float + (1)*b_CAST_add103_fixp + (-1)*C4_b_CAST_add103<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_b_CAST_add103
solver.Add( + (1)*b_fixp + (1)*b_CAST_add103_double + (-1)*C5_b_CAST_add103<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_b_CAST_add103
solver.Add( + (1)*b_double + (1)*b_CAST_add103_fixp + (-1)*C6_b_CAST_add103<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_b_CAST_add103
solver.Add( + (1)*b_float + (1)*b_CAST_add103_double + (-1)*C7_b_CAST_add103<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_b_CAST_add103
solver.Add( + (1)*b_double + (1)*b_CAST_add103_float + (-1)*C8_b_CAST_add103<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_b_CAST_add103



#Stuff for   %add103 = fadd double %mul102, %tmp29, !taffo.info !94, !taffo.initweight !44
main_add103_fixbits = solver.IntVar(0, 20, 'main_add103_fixbits')
main_add103_fixp = solver.IntVar(0, 1, 'main_add103_fixp')
main_add103_float = solver.IntVar(0, 1, 'main_add103_float')
main_add103_double = solver.IntVar(0, 1, 'main_add103_double')
main_add103_enob = solver.IntVar(-10000, 10000, 'main_add103_enob')
solver.Add( + (1)*main_add103_enob + (-1)*main_add103_fixbits + (10000)*main_add103_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add103_enob + (10000)*main_add103_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add103_enob + (10000)*main_add103_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add103_fixbits + (-10000)*main_add103_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_add103_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add103_enob
solver.Add( + (1)*main_add103_fixp + (1)*main_add103_float + (1)*main_add103_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add103_fixbits + (-10000)*main_add103_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul102_CAST_add103_fixp + (-1)*b_CAST_add103_fixp==0)    #fix equality
solver.Add( + (1)*main_mul102_CAST_add103_float + (-1)*b_CAST_add103_float==0)    #float equality
solver.Add( + (1)*main_mul102_CAST_add103_double + (-1)*b_CAST_add103_double==0)    #double equality
solver.Add( + (1)*main_mul102_CAST_add103_fixbits + (-1)*b_CAST_add103_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul102_CAST_add103_fixp + (-1)*main_add103_fixp==0)    #fix equality
solver.Add( + (1)*main_mul102_CAST_add103_float + (-1)*main_add103_float==0)    #float equality
solver.Add( + (1)*main_mul102_CAST_add103_double + (-1)*main_add103_double==0)    #double equality
solver.Add( + (1)*main_mul102_CAST_add103_fixbits + (-1)*main_add103_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add103_fixp
mathCostObj +=  + (3)*main_add103_float
mathCostObj +=  + (6.64928)*main_add103_double
solver.Add( + (1)*main_add103_enob + (-1)*main_mul102_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add103_enob + (-1)*b_enob_memphi_main_tmp29<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
main_q_enob_memphi_main_tmp30 = solver.IntVar(-10000, 10000, 'main_q_enob_memphi_main_tmp30')
solver.Add( + (1)*main_q_enob_memphi_main_tmp30 + (-1)*main_q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp30_enob_0 = solver.IntVar(0, 1, 'main_main_tmp30_enob_0')
solver.Add( + (1)*main_main_tmp30_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp30 + (-1)*main_q_enob_storeENOB_storeENOB + (10000)*main_main_tmp30_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div108 = fdiv double %tmp30, %add103, !taffo.info !115, !taffo.initweight !45
main_q_CAST_div108_fixbits = solver.IntVar(0, 22, 'main_q_CAST_div108_fixbits')
main_q_CAST_div108_fixp = solver.IntVar(0, 1, 'main_q_CAST_div108_fixp')
main_q_CAST_div108_float = solver.IntVar(0, 1, 'main_q_CAST_div108_float')
main_q_CAST_div108_double = solver.IntVar(0, 1, 'main_q_CAST_div108_double')
solver.Add( + (1)*main_q_CAST_div108_fixp + (1)*main_q_CAST_div108_float + (1)*main_q_CAST_div108_double==1)    #exactly 1 type
solver.Add( + (1)*main_q_CAST_div108_fixbits + (-10000)*main_q_CAST_div108_fixp<=0)    #If no fix, fix frac part = 0
C1_main_q_CAST_div108 = solver.IntVar(0, 1, 'C1_main_q_CAST_div108')
C2_main_q_CAST_div108 = solver.IntVar(0, 1, 'C2_main_q_CAST_div108')
solver.Add( + (1)*main_q_fixbits + (-1)*main_q_CAST_div108_fixbits + (-10000)*C1_main_q_CAST_div108<=0)    #Shift cost 1
solver.Add( + (-1)*main_q_fixbits + (1)*main_q_CAST_div108_fixbits + (-10000)*C2_main_q_CAST_div108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_q_CAST_div108
castCostObj +=  + (1)*C2_main_q_CAST_div108
C3_main_q_CAST_div108 = solver.IntVar(0, 1, 'C3_main_q_CAST_div108')
C4_main_q_CAST_div108 = solver.IntVar(0, 1, 'C4_main_q_CAST_div108')
C5_main_q_CAST_div108 = solver.IntVar(0, 1, 'C5_main_q_CAST_div108')
C6_main_q_CAST_div108 = solver.IntVar(0, 1, 'C6_main_q_CAST_div108')
C7_main_q_CAST_div108 = solver.IntVar(0, 1, 'C7_main_q_CAST_div108')
C8_main_q_CAST_div108 = solver.IntVar(0, 1, 'C8_main_q_CAST_div108')
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_div108_float + (-1)*C3_main_q_CAST_div108<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_q_CAST_div108
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_div108_fixp + (-1)*C4_main_q_CAST_div108<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_q_CAST_div108
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_div108_double + (-1)*C5_main_q_CAST_div108<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_q_CAST_div108
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_div108_fixp + (-1)*C6_main_q_CAST_div108<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_q_CAST_div108
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_div108_double + (-1)*C7_main_q_CAST_div108<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_q_CAST_div108
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_div108_float + (-1)*C8_main_q_CAST_div108<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_q_CAST_div108



#Constraint for cast for   %div108 = fdiv double %tmp30, %add103, !taffo.info !115, !taffo.initweight !45
main_add103_CAST_div108_fixbits = solver.IntVar(0, 20, 'main_add103_CAST_div108_fixbits')
main_add103_CAST_div108_fixp = solver.IntVar(0, 1, 'main_add103_CAST_div108_fixp')
main_add103_CAST_div108_float = solver.IntVar(0, 1, 'main_add103_CAST_div108_float')
main_add103_CAST_div108_double = solver.IntVar(0, 1, 'main_add103_CAST_div108_double')
solver.Add( + (1)*main_add103_CAST_div108_fixp + (1)*main_add103_CAST_div108_float + (1)*main_add103_CAST_div108_double==1)    #exactly 1 type
solver.Add( + (1)*main_add103_CAST_div108_fixbits + (-10000)*main_add103_CAST_div108_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C1_main_add103_CAST_div108')
C2_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C2_main_add103_CAST_div108')
solver.Add( + (1)*main_add103_fixbits + (-1)*main_add103_CAST_div108_fixbits + (-10000)*C1_main_add103_CAST_div108<=0)    #Shift cost 1
solver.Add( + (-1)*main_add103_fixbits + (1)*main_add103_CAST_div108_fixbits + (-10000)*C2_main_add103_CAST_div108<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add103_CAST_div108
castCostObj +=  + (1)*C2_main_add103_CAST_div108
C3_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C3_main_add103_CAST_div108')
C4_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C4_main_add103_CAST_div108')
C5_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C5_main_add103_CAST_div108')
C6_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C6_main_add103_CAST_div108')
C7_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C7_main_add103_CAST_div108')
C8_main_add103_CAST_div108 = solver.IntVar(0, 1, 'C8_main_add103_CAST_div108')
solver.Add( + (1)*main_add103_fixp + (1)*main_add103_CAST_div108_float + (-1)*C3_main_add103_CAST_div108<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add103_CAST_div108
solver.Add( + (1)*main_add103_float + (1)*main_add103_CAST_div108_fixp + (-1)*C4_main_add103_CAST_div108<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add103_CAST_div108
solver.Add( + (1)*main_add103_fixp + (1)*main_add103_CAST_div108_double + (-1)*C5_main_add103_CAST_div108<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add103_CAST_div108
solver.Add( + (1)*main_add103_double + (1)*main_add103_CAST_div108_fixp + (-1)*C6_main_add103_CAST_div108<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add103_CAST_div108
solver.Add( + (1)*main_add103_float + (1)*main_add103_CAST_div108_double + (-1)*C7_main_add103_CAST_div108<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add103_CAST_div108
solver.Add( + (1)*main_add103_double + (1)*main_add103_CAST_div108_float + (-1)*C8_main_add103_CAST_div108<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add103_CAST_div108



#Stuff for   %div108 = fdiv double %tmp30, %add103, !taffo.info !115, !taffo.initweight !45
main_div108_fixbits = solver.IntVar(0, 29, 'main_div108_fixbits')
main_div108_fixp = solver.IntVar(0, 1, 'main_div108_fixp')
main_div108_float = solver.IntVar(0, 1, 'main_div108_float')
main_div108_double = solver.IntVar(0, 1, 'main_div108_double')
main_div108_enob = solver.IntVar(-10000, 10000, 'main_div108_enob')
solver.Add( + (1)*main_div108_enob + (-1)*main_div108_fixbits + (10000)*main_div108_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div108_enob + (10000)*main_div108_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div108_enob + (10000)*main_div108_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div108_fixbits + (-10000)*main_div108_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_div108_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div108_enob
solver.Add( + (1)*main_div108_fixp + (1)*main_div108_float + (1)*main_div108_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div108_fixbits + (-10000)*main_div108_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_q_CAST_div108_fixp + (-1)*main_add103_CAST_div108_fixp==0)    #fix equality
solver.Add( + (1)*main_q_CAST_div108_float + (-1)*main_add103_CAST_div108_float==0)    #float equality
solver.Add( + (1)*main_q_CAST_div108_double + (-1)*main_add103_CAST_div108_double==0)    #double equality
solver.Add( + (1)*main_q_CAST_div108_fixp + (-1)*main_div108_fixp==0)    #fix equality
solver.Add( + (1)*main_q_CAST_div108_float + (-1)*main_div108_float==0)    #float equality
solver.Add( + (1)*main_q_CAST_div108_double + (-1)*main_div108_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div108_fixp
mathCostObj +=  + (6)*main_div108_float
mathCostObj +=  + (12)*main_div108_double
main_main_div108_enob_1 = solver.IntVar(0, 1, 'main_main_div108_enob_1')
main_main_div108_enob_2 = solver.IntVar(0, 1, 'main_main_div108_enob_2')
solver.Add( + (1)*main_main_div108_enob_1 + (1)*main_main_div108_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div108_enob + (-1)*main_add103_enob + (-10000)*main_main_div108_enob_1<=1044)    #Enob: propagation in division 1
solver.Add( + (1)*main_div108_enob + (-1)*main_q_enob_memphi_main_tmp30 + (-10000)*main_main_div108_enob_2<=1044)    #Enob: propagation in division 2



#Constraint for cast for   store double %div108, double* %arrayidx107, align 8, !taffo.info !39, !taffo.initweight !45
main_div108_CAST_store_fixbits = solver.IntVar(0, 29, 'main_div108_CAST_store_fixbits')
main_div108_CAST_store_fixp = solver.IntVar(0, 1, 'main_div108_CAST_store_fixp')
main_div108_CAST_store_float = solver.IntVar(0, 1, 'main_div108_CAST_store_float')
main_div108_CAST_store_double = solver.IntVar(0, 1, 'main_div108_CAST_store_double')
solver.Add( + (1)*main_div108_CAST_store_fixp + (1)*main_div108_CAST_store_float + (1)*main_div108_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div108_CAST_store_fixbits + (-10000)*main_div108_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div108_CAST_store = solver.IntVar(0, 1, 'C1_main_div108_CAST_store')
C2_main_div108_CAST_store = solver.IntVar(0, 1, 'C2_main_div108_CAST_store')
solver.Add( + (1)*main_div108_fixbits + (-1)*main_div108_CAST_store_fixbits + (-10000)*C1_main_div108_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div108_fixbits + (1)*main_div108_CAST_store_fixbits + (-10000)*C2_main_div108_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div108_CAST_store
castCostObj +=  + (1)*C2_main_div108_CAST_store
C3_main_div108_CAST_store = solver.IntVar(0, 1, 'C3_main_div108_CAST_store')
C4_main_div108_CAST_store = solver.IntVar(0, 1, 'C4_main_div108_CAST_store')
C5_main_div108_CAST_store = solver.IntVar(0, 1, 'C5_main_div108_CAST_store')
C6_main_div108_CAST_store = solver.IntVar(0, 1, 'C6_main_div108_CAST_store')
C7_main_div108_CAST_store = solver.IntVar(0, 1, 'C7_main_div108_CAST_store')
C8_main_div108_CAST_store = solver.IntVar(0, 1, 'C8_main_div108_CAST_store')
solver.Add( + (1)*main_div108_fixp + (1)*main_div108_CAST_store_float + (-1)*C3_main_div108_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div108_CAST_store
solver.Add( + (1)*main_div108_float + (1)*main_div108_CAST_store_fixp + (-1)*C4_main_div108_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div108_CAST_store
solver.Add( + (1)*main_div108_fixp + (1)*main_div108_CAST_store_double + (-1)*C5_main_div108_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div108_CAST_store
solver.Add( + (1)*main_div108_double + (1)*main_div108_CAST_store_fixp + (-1)*C6_main_div108_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div108_CAST_store
solver.Add( + (1)*main_div108_float + (1)*main_div108_CAST_store_double + (-1)*C7_main_div108_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div108_CAST_store
solver.Add( + (1)*main_div108_double + (1)*main_div108_CAST_store_float + (-1)*C8_main_div108_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div108_CAST_store
solver.Add( + (1)*main_q_fixp + (-1)*main_div108_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_q_float + (-1)*main_div108_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_q_double + (-1)*main_div108_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_q_fixbits + (-1)*main_div108_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_q_enob_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_q_enob_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB + (-1)*main_q_fixbits + (10000)*main_q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB + (10000)*main_q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB + (10000)*main_q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB + (-1)*main_div108_enob<=0)    #Enob constraint ENOB propagation in load/store



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
solver.Add( + (1)*ConstantValue__44_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__44_fixp + (1)*ConstantValue__44_float + (1)*ConstantValue__44_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__44_fixbits + (-10000)*ConstantValue__44_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx114, align 8, !taffo.info !35, !taffo.initweight !45, !taffo.constinfo !66
ConstantValue__44_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__44_CAST_store_fixbits')
ConstantValue__44_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__44_CAST_store_fixp')
ConstantValue__44_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__44_CAST_store_float')
ConstantValue__44_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__44_CAST_store_double')
solver.Add( + (1)*ConstantValue__44_CAST_store_fixp + (1)*ConstantValue__44_CAST_store_float + (1)*ConstantValue__44_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__44_CAST_store_fixbits + (-10000)*ConstantValue__44_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__44_CAST_store')
C2_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__44_CAST_store')
solver.Add( + (1)*ConstantValue__44_fixbits + (-1)*ConstantValue__44_CAST_store_fixbits + (-10000)*C1_ConstantValue__44_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__44_fixbits + (1)*ConstantValue__44_CAST_store_fixbits + (-10000)*C2_ConstantValue__44_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__44_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__44_CAST_store
C3_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__44_CAST_store')
C4_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__44_CAST_store')
C5_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__44_CAST_store')
C6_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__44_CAST_store')
C7_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__44_CAST_store')
C8_ConstantValue__44_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__44_CAST_store')
solver.Add( + (1)*ConstantValue__44_fixp + (1)*ConstantValue__44_CAST_store_float + (-1)*C3_ConstantValue__44_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__44_CAST_store
solver.Add( + (1)*ConstantValue__44_float + (1)*ConstantValue__44_CAST_store_fixp + (-1)*C4_ConstantValue__44_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__44_CAST_store
solver.Add( + (1)*ConstantValue__44_fixp + (1)*ConstantValue__44_CAST_store_double + (-1)*C5_ConstantValue__44_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__44_CAST_store
solver.Add( + (1)*ConstantValue__44_double + (1)*ConstantValue__44_CAST_store_fixp + (-1)*C6_ConstantValue__44_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__44_CAST_store
solver.Add( + (1)*ConstantValue__44_float + (1)*ConstantValue__44_CAST_store_double + (-1)*C7_ConstantValue__44_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__44_CAST_store
solver.Add( + (1)*ConstantValue__44_double + (1)*ConstantValue__44_CAST_store_float + (-1)*C8_ConstantValue__44_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__44_CAST_store
solver.Add( + (1)*main_v_fixp + (-1)*ConstantValue__44_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_v_float + (-1)*ConstantValue__44_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_v_double + (-1)*ConstantValue__44_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_v_fixbits + (-1)*ConstantValue__44_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp20 + (-1)*ConstantValue__43_enob + (10000)*main_main_tmp20_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp22 + (-1)*ConstantValue__43_enob + (10000)*main_main_tmp22_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp24 + (-1)*ConstantValue__43_enob + (10000)*main_main_tmp24_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_p_enob_memphi_main_tmp31 = solver.IntVar(-10000, 10000, 'main_p_enob_memphi_main_tmp31')
solver.Add( + (1)*main_p_enob_memphi_main_tmp31 + (-1)*main_p_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp31_enob_0 = solver.IntVar(0, 1, 'main_main_tmp31_enob_0')
main_main_tmp31_enob_1 = solver.IntVar(0, 1, 'main_main_tmp31_enob_1')
solver.Add( + (1)*main_main_tmp31_enob_0 + (1)*main_main_tmp31_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_p_enob_memphi_main_tmp31 + (-1)*main_q_enob_storeENOB + (10000)*main_main_tmp31_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_p_enob_memphi_main_tmp31 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp31_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_v_enob_memphi_main_tmp32 = solver.IntVar(-10000, 10000, 'main_v_enob_memphi_main_tmp32')
solver.Add( + (1)*main_v_enob_memphi_main_tmp32 + (-1)*main_v_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul128 = fmul double %tmp31, %tmp32, !taffo.info !35, !taffo.initweight !51
main_p_CAST_mul128_fixbits = solver.IntVar(0, 30, 'main_p_CAST_mul128_fixbits')
main_p_CAST_mul128_fixp = solver.IntVar(0, 1, 'main_p_CAST_mul128_fixp')
main_p_CAST_mul128_float = solver.IntVar(0, 1, 'main_p_CAST_mul128_float')
main_p_CAST_mul128_double = solver.IntVar(0, 1, 'main_p_CAST_mul128_double')
solver.Add( + (1)*main_p_CAST_mul128_fixp + (1)*main_p_CAST_mul128_float + (1)*main_p_CAST_mul128_double==1)    #exactly 1 type
solver.Add( + (1)*main_p_CAST_mul128_fixbits + (-10000)*main_p_CAST_mul128_fixp<=0)    #If no fix, fix frac part = 0
C1_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C1_main_p_CAST_mul128')
C2_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C2_main_p_CAST_mul128')
solver.Add( + (1)*main_p_fixbits + (-1)*main_p_CAST_mul128_fixbits + (-10000)*C1_main_p_CAST_mul128<=0)    #Shift cost 1
solver.Add( + (-1)*main_p_fixbits + (1)*main_p_CAST_mul128_fixbits + (-10000)*C2_main_p_CAST_mul128<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_p_CAST_mul128
castCostObj +=  + (1)*C2_main_p_CAST_mul128
C3_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C3_main_p_CAST_mul128')
C4_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C4_main_p_CAST_mul128')
C5_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C5_main_p_CAST_mul128')
C6_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C6_main_p_CAST_mul128')
C7_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C7_main_p_CAST_mul128')
C8_main_p_CAST_mul128 = solver.IntVar(0, 1, 'C8_main_p_CAST_mul128')
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul128_float + (-1)*C3_main_p_CAST_mul128<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_p_CAST_mul128
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul128_fixp + (-1)*C4_main_p_CAST_mul128<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_p_CAST_mul128
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul128_double + (-1)*C5_main_p_CAST_mul128<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_p_CAST_mul128
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul128_fixp + (-1)*C6_main_p_CAST_mul128<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_p_CAST_mul128
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul128_double + (-1)*C7_main_p_CAST_mul128<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_p_CAST_mul128
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul128_float + (-1)*C8_main_p_CAST_mul128<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_p_CAST_mul128



#Constraint for cast for   %mul128 = fmul double %tmp31, %tmp32, !taffo.info !35, !taffo.initweight !51
main_v_CAST_mul128_fixbits = solver.IntVar(0, 29, 'main_v_CAST_mul128_fixbits')
main_v_CAST_mul128_fixp = solver.IntVar(0, 1, 'main_v_CAST_mul128_fixp')
main_v_CAST_mul128_float = solver.IntVar(0, 1, 'main_v_CAST_mul128_float')
main_v_CAST_mul128_double = solver.IntVar(0, 1, 'main_v_CAST_mul128_double')
solver.Add( + (1)*main_v_CAST_mul128_fixp + (1)*main_v_CAST_mul128_float + (1)*main_v_CAST_mul128_double==1)    #exactly 1 type
solver.Add( + (1)*main_v_CAST_mul128_fixbits + (-10000)*main_v_CAST_mul128_fixp<=0)    #If no fix, fix frac part = 0
C1_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C1_main_v_CAST_mul128')
C2_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C2_main_v_CAST_mul128')
solver.Add( + (1)*main_v_fixbits + (-1)*main_v_CAST_mul128_fixbits + (-10000)*C1_main_v_CAST_mul128<=0)    #Shift cost 1
solver.Add( + (-1)*main_v_fixbits + (1)*main_v_CAST_mul128_fixbits + (-10000)*C2_main_v_CAST_mul128<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_v_CAST_mul128
castCostObj +=  + (1)*C2_main_v_CAST_mul128
C3_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C3_main_v_CAST_mul128')
C4_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C4_main_v_CAST_mul128')
C5_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C5_main_v_CAST_mul128')
C6_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C6_main_v_CAST_mul128')
C7_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C7_main_v_CAST_mul128')
C8_main_v_CAST_mul128 = solver.IntVar(0, 1, 'C8_main_v_CAST_mul128')
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul128_float + (-1)*C3_main_v_CAST_mul128<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_v_CAST_mul128
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul128_fixp + (-1)*C4_main_v_CAST_mul128<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_v_CAST_mul128
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul128_double + (-1)*C5_main_v_CAST_mul128<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_v_CAST_mul128
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul128_fixp + (-1)*C6_main_v_CAST_mul128<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_v_CAST_mul128
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul128_double + (-1)*C7_main_v_CAST_mul128<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_v_CAST_mul128
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul128_float + (-1)*C8_main_v_CAST_mul128<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_v_CAST_mul128



#Stuff for   %mul128 = fmul double %tmp31, %tmp32, !taffo.info !35, !taffo.initweight !51
main_mul128_fixbits = solver.IntVar(0, 29, 'main_mul128_fixbits')
main_mul128_fixp = solver.IntVar(0, 1, 'main_mul128_fixp')
main_mul128_float = solver.IntVar(0, 1, 'main_mul128_float')
main_mul128_double = solver.IntVar(0, 1, 'main_mul128_double')
main_mul128_enob = solver.IntVar(-10000, 10000, 'main_mul128_enob')
solver.Add( + (1)*main_mul128_enob + (-1)*main_mul128_fixbits + (10000)*main_mul128_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul128_enob + (10000)*main_mul128_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul128_enob + (10000)*main_mul128_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul128_fixbits + (-10000)*main_mul128_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_mul128_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul128_enob
solver.Add( + (1)*main_mul128_fixp + (1)*main_mul128_float + (1)*main_mul128_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul128_fixbits + (-10000)*main_mul128_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_p_CAST_mul128_fixp + (-1)*main_v_CAST_mul128_fixp==0)    #fix equality
solver.Add( + (1)*main_p_CAST_mul128_float + (-1)*main_v_CAST_mul128_float==0)    #float equality
solver.Add( + (1)*main_p_CAST_mul128_double + (-1)*main_v_CAST_mul128_double==0)    #double equality
solver.Add( + (1)*main_p_CAST_mul128_fixp + (-1)*main_mul128_fixp==0)    #fix equality
solver.Add( + (1)*main_p_CAST_mul128_float + (-1)*main_mul128_float==0)    #float equality
solver.Add( + (1)*main_p_CAST_mul128_double + (-1)*main_mul128_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul128_fixp
mathCostObj +=  + (6)*main_mul128_float
mathCostObj +=  + (12.2551)*main_mul128_double
main_main_mul128_enob_1 = solver.IntVar(0, 1, 'main_main_mul128_enob_1')
main_main_mul128_enob_2 = solver.IntVar(0, 1, 'main_main_mul128_enob_2')
solver.Add( + (1)*main_main_mul128_enob_1 + (1)*main_main_mul128_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul128_enob + (-1)*main_v_enob_memphi_main_tmp32 + (-10000)*main_main_mul128_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul128_enob + (-1)*main_p_enob_memphi_main_tmp31 + (-10000)*main_main_mul128_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_q_enob_memphi_main_tmp33 = solver.IntVar(-10000, 10000, 'main_q_enob_memphi_main_tmp33')
solver.Add( + (1)*main_q_enob_memphi_main_tmp33 + (-1)*main_q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp33_enob_0 = solver.IntVar(0, 1, 'main_main_tmp33_enob_0')
main_main_tmp33_enob_1 = solver.IntVar(0, 1, 'main_main_tmp33_enob_1')
solver.Add( + (1)*main_main_tmp33_enob_0 + (1)*main_main_tmp33_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp33 + (-1)*main_q_enob_storeENOB + (10000)*main_main_tmp33_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp33 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp33_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add133 = fadd double %mul128, %tmp33, !taffo.info !121, !taffo.initweight !51
main_mul128_CAST_add133_fixbits = solver.IntVar(0, 29, 'main_mul128_CAST_add133_fixbits')
main_mul128_CAST_add133_fixp = solver.IntVar(0, 1, 'main_mul128_CAST_add133_fixp')
main_mul128_CAST_add133_float = solver.IntVar(0, 1, 'main_mul128_CAST_add133_float')
main_mul128_CAST_add133_double = solver.IntVar(0, 1, 'main_mul128_CAST_add133_double')
solver.Add( + (1)*main_mul128_CAST_add133_fixp + (1)*main_mul128_CAST_add133_float + (1)*main_mul128_CAST_add133_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul128_CAST_add133_fixbits + (-10000)*main_mul128_CAST_add133_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C1_main_mul128_CAST_add133')
C2_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C2_main_mul128_CAST_add133')
solver.Add( + (1)*main_mul128_fixbits + (-1)*main_mul128_CAST_add133_fixbits + (-10000)*C1_main_mul128_CAST_add133<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul128_fixbits + (1)*main_mul128_CAST_add133_fixbits + (-10000)*C2_main_mul128_CAST_add133<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul128_CAST_add133
castCostObj +=  + (1)*C2_main_mul128_CAST_add133
C3_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C3_main_mul128_CAST_add133')
C4_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C4_main_mul128_CAST_add133')
C5_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C5_main_mul128_CAST_add133')
C6_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C6_main_mul128_CAST_add133')
C7_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C7_main_mul128_CAST_add133')
C8_main_mul128_CAST_add133 = solver.IntVar(0, 1, 'C8_main_mul128_CAST_add133')
solver.Add( + (1)*main_mul128_fixp + (1)*main_mul128_CAST_add133_float + (-1)*C3_main_mul128_CAST_add133<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul128_CAST_add133
solver.Add( + (1)*main_mul128_float + (1)*main_mul128_CAST_add133_fixp + (-1)*C4_main_mul128_CAST_add133<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul128_CAST_add133
solver.Add( + (1)*main_mul128_fixp + (1)*main_mul128_CAST_add133_double + (-1)*C5_main_mul128_CAST_add133<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul128_CAST_add133
solver.Add( + (1)*main_mul128_double + (1)*main_mul128_CAST_add133_fixp + (-1)*C6_main_mul128_CAST_add133<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul128_CAST_add133
solver.Add( + (1)*main_mul128_float + (1)*main_mul128_CAST_add133_double + (-1)*C7_main_mul128_CAST_add133<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul128_CAST_add133
solver.Add( + (1)*main_mul128_double + (1)*main_mul128_CAST_add133_float + (-1)*C8_main_mul128_CAST_add133<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul128_CAST_add133



#Constraint for cast for   %add133 = fadd double %mul128, %tmp33, !taffo.info !121, !taffo.initweight !51
main_q_CAST_add133_fixbits = solver.IntVar(0, 22, 'main_q_CAST_add133_fixbits')
main_q_CAST_add133_fixp = solver.IntVar(0, 1, 'main_q_CAST_add133_fixp')
main_q_CAST_add133_float = solver.IntVar(0, 1, 'main_q_CAST_add133_float')
main_q_CAST_add133_double = solver.IntVar(0, 1, 'main_q_CAST_add133_double')
solver.Add( + (1)*main_q_CAST_add133_fixp + (1)*main_q_CAST_add133_float + (1)*main_q_CAST_add133_double==1)    #exactly 1 type
solver.Add( + (1)*main_q_CAST_add133_fixbits + (-10000)*main_q_CAST_add133_fixp<=0)    #If no fix, fix frac part = 0
C1_main_q_CAST_add133 = solver.IntVar(0, 1, 'C1_main_q_CAST_add133')
C2_main_q_CAST_add133 = solver.IntVar(0, 1, 'C2_main_q_CAST_add133')
solver.Add( + (1)*main_q_fixbits + (-1)*main_q_CAST_add133_fixbits + (-10000)*C1_main_q_CAST_add133<=0)    #Shift cost 1
solver.Add( + (-1)*main_q_fixbits + (1)*main_q_CAST_add133_fixbits + (-10000)*C2_main_q_CAST_add133<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_q_CAST_add133
castCostObj +=  + (1)*C2_main_q_CAST_add133
C3_main_q_CAST_add133 = solver.IntVar(0, 1, 'C3_main_q_CAST_add133')
C4_main_q_CAST_add133 = solver.IntVar(0, 1, 'C4_main_q_CAST_add133')
C5_main_q_CAST_add133 = solver.IntVar(0, 1, 'C5_main_q_CAST_add133')
C6_main_q_CAST_add133 = solver.IntVar(0, 1, 'C6_main_q_CAST_add133')
C7_main_q_CAST_add133 = solver.IntVar(0, 1, 'C7_main_q_CAST_add133')
C8_main_q_CAST_add133 = solver.IntVar(0, 1, 'C8_main_q_CAST_add133')
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_add133_float + (-1)*C3_main_q_CAST_add133<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_q_CAST_add133
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_add133_fixp + (-1)*C4_main_q_CAST_add133<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_q_CAST_add133
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_add133_double + (-1)*C5_main_q_CAST_add133<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_q_CAST_add133
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_add133_fixp + (-1)*C6_main_q_CAST_add133<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_q_CAST_add133
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_add133_double + (-1)*C7_main_q_CAST_add133<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_q_CAST_add133
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_add133_float + (-1)*C8_main_q_CAST_add133<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_q_CAST_add133



#Stuff for   %add133 = fadd double %mul128, %tmp33, !taffo.info !121, !taffo.initweight !51
main_add133_fixbits = solver.IntVar(0, 22, 'main_add133_fixbits')
main_add133_fixp = solver.IntVar(0, 1, 'main_add133_fixp')
main_add133_float = solver.IntVar(0, 1, 'main_add133_float')
main_add133_double = solver.IntVar(0, 1, 'main_add133_double')
main_add133_enob = solver.IntVar(-10000, 10000, 'main_add133_enob')
solver.Add( + (1)*main_add133_enob + (-1)*main_add133_fixbits + (10000)*main_add133_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add133_enob + (10000)*main_add133_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add133_enob + (10000)*main_add133_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add133_fixbits + (-10000)*main_add133_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_add133_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add133_enob
solver.Add( + (1)*main_add133_fixp + (1)*main_add133_float + (1)*main_add133_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add133_fixbits + (-10000)*main_add133_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul128_CAST_add133_fixp + (-1)*main_q_CAST_add133_fixp==0)    #fix equality
solver.Add( + (1)*main_mul128_CAST_add133_float + (-1)*main_q_CAST_add133_float==0)    #float equality
solver.Add( + (1)*main_mul128_CAST_add133_double + (-1)*main_q_CAST_add133_double==0)    #double equality
solver.Add( + (1)*main_mul128_CAST_add133_fixbits + (-1)*main_q_CAST_add133_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul128_CAST_add133_fixp + (-1)*main_add133_fixp==0)    #fix equality
solver.Add( + (1)*main_mul128_CAST_add133_float + (-1)*main_add133_float==0)    #float equality
solver.Add( + (1)*main_mul128_CAST_add133_double + (-1)*main_add133_double==0)    #double equality
solver.Add( + (1)*main_mul128_CAST_add133_fixbits + (-1)*main_add133_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add133_fixp
mathCostObj +=  + (3)*main_add133_float
mathCostObj +=  + (6.64928)*main_add133_double
solver.Add( + (1)*main_add133_enob + (-1)*main_mul128_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add133_enob + (-1)*main_q_enob_memphi_main_tmp33<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add133, double* %arrayidx137, align 8, !taffo.info !35, !taffo.initweight !45
main_add133_CAST_store_fixbits = solver.IntVar(0, 22, 'main_add133_CAST_store_fixbits')
main_add133_CAST_store_fixp = solver.IntVar(0, 1, 'main_add133_CAST_store_fixp')
main_add133_CAST_store_float = solver.IntVar(0, 1, 'main_add133_CAST_store_float')
main_add133_CAST_store_double = solver.IntVar(0, 1, 'main_add133_CAST_store_double')
solver.Add( + (1)*main_add133_CAST_store_fixp + (1)*main_add133_CAST_store_float + (1)*main_add133_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add133_CAST_store_fixbits + (-10000)*main_add133_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add133_CAST_store = solver.IntVar(0, 1, 'C1_main_add133_CAST_store')
C2_main_add133_CAST_store = solver.IntVar(0, 1, 'C2_main_add133_CAST_store')
solver.Add( + (1)*main_add133_fixbits + (-1)*main_add133_CAST_store_fixbits + (-10000)*C1_main_add133_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add133_fixbits + (1)*main_add133_CAST_store_fixbits + (-10000)*C2_main_add133_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add133_CAST_store
castCostObj +=  + (1)*C2_main_add133_CAST_store
C3_main_add133_CAST_store = solver.IntVar(0, 1, 'C3_main_add133_CAST_store')
C4_main_add133_CAST_store = solver.IntVar(0, 1, 'C4_main_add133_CAST_store')
C5_main_add133_CAST_store = solver.IntVar(0, 1, 'C5_main_add133_CAST_store')
C6_main_add133_CAST_store = solver.IntVar(0, 1, 'C6_main_add133_CAST_store')
C7_main_add133_CAST_store = solver.IntVar(0, 1, 'C7_main_add133_CAST_store')
C8_main_add133_CAST_store = solver.IntVar(0, 1, 'C8_main_add133_CAST_store')
solver.Add( + (1)*main_add133_fixp + (1)*main_add133_CAST_store_float + (-1)*C3_main_add133_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add133_CAST_store
solver.Add( + (1)*main_add133_float + (1)*main_add133_CAST_store_fixp + (-1)*C4_main_add133_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add133_CAST_store
solver.Add( + (1)*main_add133_fixp + (1)*main_add133_CAST_store_double + (-1)*C5_main_add133_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add133_CAST_store
solver.Add( + (1)*main_add133_double + (1)*main_add133_CAST_store_fixp + (-1)*C6_main_add133_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add133_CAST_store
solver.Add( + (1)*main_add133_float + (1)*main_add133_CAST_store_double + (-1)*C7_main_add133_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add133_CAST_store
solver.Add( + (1)*main_add133_double + (1)*main_add133_CAST_store_float + (-1)*C8_main_add133_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add133_CAST_store
solver.Add( + (1)*main_v_fixp + (-1)*main_add133_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_v_float + (-1)*main_add133_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_v_double + (-1)*main_add133_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_v_fixbits + (-1)*main_add133_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_v_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_v_enob_storeENOB')
solver.Add( + (1)*main_v_enob_storeENOB + (-1)*main_v_fixbits + (10000)*main_v_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_v_enob_storeENOB + (10000)*main_v_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_v_enob_storeENOB + (10000)*main_v_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_v_enob_storeENOB + (-1)*main_add133_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp20 + (-1)*main_v_enob_storeENOB + (10000)*main_main_tmp20_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp22 + (-1)*main_v_enob_storeENOB + (10000)*main_main_tmp22_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp24 + (-1)*main_v_enob_storeENOB + (10000)*main_main_tmp24_enob_2<=10000)    #Enob: forcing MEM phi enob



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
solver.Add( + (1)*ConstantValue__45_double<=0)    #Disable double data type
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
solver.Add( + (1)*ConstantValue__46_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__46_fixp + (1)*ConstantValue__46_float + (1)*ConstantValue__46_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__46_fixbits + (-10000)*ConstantValue__46_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx149, align 16, !taffo.info !33, !taffo.initweight !45, !taffo.constinfo !66
ConstantValue__46_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__46_CAST_store_fixbits')
ConstantValue__46_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__46_CAST_store_fixp')
ConstantValue__46_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__46_CAST_store_float')
ConstantValue__46_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__46_CAST_store_double')
solver.Add( + (1)*ConstantValue__46_CAST_store_fixp + (1)*ConstantValue__46_CAST_store_float + (1)*ConstantValue__46_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__46_CAST_store_fixbits + (-10000)*ConstantValue__46_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__46_CAST_store')
C2_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__46_CAST_store')
solver.Add( + (1)*ConstantValue__46_fixbits + (-1)*ConstantValue__46_CAST_store_fixbits + (-10000)*C1_ConstantValue__46_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__46_fixbits + (1)*ConstantValue__46_CAST_store_fixbits + (-10000)*C2_ConstantValue__46_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__46_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__46_CAST_store
C3_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__46_CAST_store')
C4_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__46_CAST_store')
C5_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__46_CAST_store')
C6_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__46_CAST_store')
C7_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__46_CAST_store')
C8_ConstantValue__46_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__46_CAST_store')
solver.Add( + (1)*ConstantValue__46_fixp + (1)*ConstantValue__46_CAST_store_float + (-1)*C3_ConstantValue__46_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__46_CAST_store
solver.Add( + (1)*ConstantValue__46_float + (1)*ConstantValue__46_CAST_store_fixp + (-1)*C4_ConstantValue__46_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__46_CAST_store
solver.Add( + (1)*ConstantValue__46_fixp + (1)*ConstantValue__46_CAST_store_double + (-1)*C5_ConstantValue__46_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__46_CAST_store
solver.Add( + (1)*ConstantValue__46_double + (1)*ConstantValue__46_CAST_store_fixp + (-1)*C6_ConstantValue__46_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__46_CAST_store
solver.Add( + (1)*ConstantValue__46_float + (1)*ConstantValue__46_CAST_store_double + (-1)*C7_ConstantValue__46_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__46_CAST_store
solver.Add( + (1)*ConstantValue__46_double + (1)*ConstantValue__46_CAST_store_float + (-1)*C8_ConstantValue__46_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__46_CAST_store
solver.Add( + (1)*main_u_fixp + (-1)*ConstantValue__46_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_u_float + (-1)*ConstantValue__46_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_u_double + (-1)*ConstantValue__46_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_u_fixbits + (-1)*ConstantValue__46_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Stuff for double 0.000000e+00
ConstantValue__47_fixbits = solver.IntVar(0, 32, 'ConstantValue__47_fixbits')
ConstantValue__47_fixp = solver.IntVar(0, 1, 'ConstantValue__47_fixp')
ConstantValue__47_float = solver.IntVar(0, 1, 'ConstantValue__47_float')
ConstantValue__47_double = solver.IntVar(0, 1, 'ConstantValue__47_double')
ConstantValue__47_enob = solver.IntVar(-10000, 10000, 'ConstantValue__47_enob')
solver.Add( + (1)*ConstantValue__47_enob + (-1)*ConstantValue__47_fixbits + (10000)*ConstantValue__47_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__47_enob + (10000)*ConstantValue__47_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__47_enob + (10000)*ConstantValue__47_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__47_fixbits + (-10000)*ConstantValue__47_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__47_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__47_fixp + (1)*ConstantValue__47_float + (1)*ConstantValue__47_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__47_fixbits + (-10000)*ConstantValue__47_fixp<=0)    #If not fix, frac part to zero



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
solver.Add( + (1)*ConstantValue__48_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__48_fixp + (1)*ConstantValue__48_float + (1)*ConstantValue__48_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__48_fixbits + (-10000)*ConstantValue__48_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 0.000000e+00, double* %arrayidx152, align 16, !taffo.info !37, !taffo.initweight !45, !taffo.constinfo !88
ConstantValue__48_CAST_store_fixbits = solver.IntVar(0, 32, 'ConstantValue__48_CAST_store_fixbits')
ConstantValue__48_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__48_CAST_store_fixp')
ConstantValue__48_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__48_CAST_store_float')
ConstantValue__48_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__48_CAST_store_double')
solver.Add( + (1)*ConstantValue__48_CAST_store_fixp + (1)*ConstantValue__48_CAST_store_float + (1)*ConstantValue__48_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__48_CAST_store_fixbits + (-10000)*ConstantValue__48_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__48_CAST_store')
C2_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__48_CAST_store')
solver.Add( + (1)*ConstantValue__48_fixbits + (-1)*ConstantValue__48_CAST_store_fixbits + (-10000)*C1_ConstantValue__48_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__48_fixbits + (1)*ConstantValue__48_CAST_store_fixbits + (-10000)*C2_ConstantValue__48_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__48_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__48_CAST_store
C3_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__48_CAST_store')
C4_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__48_CAST_store')
C5_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__48_CAST_store')
C6_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__48_CAST_store')
C7_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__48_CAST_store')
C8_ConstantValue__48_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__48_CAST_store')
solver.Add( + (1)*ConstantValue__48_fixp + (1)*ConstantValue__48_CAST_store_float + (-1)*C3_ConstantValue__48_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__48_CAST_store
solver.Add( + (1)*ConstantValue__48_float + (1)*ConstantValue__48_CAST_store_fixp + (-1)*C4_ConstantValue__48_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__48_CAST_store
solver.Add( + (1)*ConstantValue__48_fixp + (1)*ConstantValue__48_CAST_store_double + (-1)*C5_ConstantValue__48_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__48_CAST_store
solver.Add( + (1)*ConstantValue__48_double + (1)*ConstantValue__48_CAST_store_fixp + (-1)*C6_ConstantValue__48_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__48_CAST_store
solver.Add( + (1)*ConstantValue__48_float + (1)*ConstantValue__48_CAST_store_double + (-1)*C7_ConstantValue__48_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__48_CAST_store
solver.Add( + (1)*ConstantValue__48_double + (1)*ConstantValue__48_CAST_store_float + (-1)*C8_ConstantValue__48_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__48_CAST_store
solver.Add( + (1)*main_p_fixp + (-1)*ConstantValue__48_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_p_float + (-1)*ConstantValue__48_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_p_double + (-1)*ConstantValue__48_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_p_fixbits + (-1)*ConstantValue__48_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.

#Restriction for new enob [LOAD]
main_u_enob_memphi_main_tmp34 = solver.IntVar(-10000, 10000, 'main_u_enob_memphi_main_tmp34')
solver.Add( + (1)*main_u_enob_memphi_main_tmp34 + (-1)*main_u_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   store double %tmp34, double* %arrayidx158, align 16, !taffo.info !39, !taffo.initweight !45
main_u_CAST_store_fixbits = solver.IntVar(0, 28, 'main_u_CAST_store_fixbits')
main_u_CAST_store_fixp = solver.IntVar(0, 1, 'main_u_CAST_store_fixp')
main_u_CAST_store_float = solver.IntVar(0, 1, 'main_u_CAST_store_float')
main_u_CAST_store_double = solver.IntVar(0, 1, 'main_u_CAST_store_double')
solver.Add( + (1)*main_u_CAST_store_fixp + (1)*main_u_CAST_store_float + (1)*main_u_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_u_CAST_store_fixbits + (-10000)*main_u_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_u_CAST_store = solver.IntVar(0, 1, 'C1_main_u_CAST_store')
C2_main_u_CAST_store = solver.IntVar(0, 1, 'C2_main_u_CAST_store')
solver.Add( + (1)*main_u_fixbits + (-1)*main_u_CAST_store_fixbits + (-10000)*C1_main_u_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_u_fixbits + (1)*main_u_CAST_store_fixbits + (-10000)*C2_main_u_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_u_CAST_store
castCostObj +=  + (1)*C2_main_u_CAST_store
C3_main_u_CAST_store = solver.IntVar(0, 1, 'C3_main_u_CAST_store')
C4_main_u_CAST_store = solver.IntVar(0, 1, 'C4_main_u_CAST_store')
C5_main_u_CAST_store = solver.IntVar(0, 1, 'C5_main_u_CAST_store')
C6_main_u_CAST_store = solver.IntVar(0, 1, 'C6_main_u_CAST_store')
C7_main_u_CAST_store = solver.IntVar(0, 1, 'C7_main_u_CAST_store')
C8_main_u_CAST_store = solver.IntVar(0, 1, 'C8_main_u_CAST_store')
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_store_float + (-1)*C3_main_u_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_u_CAST_store
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_store_fixp + (-1)*C4_main_u_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_u_CAST_store
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_store_double + (-1)*C5_main_u_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_u_CAST_store
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_store_fixp + (-1)*C6_main_u_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_u_CAST_store
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_store_double + (-1)*C7_main_u_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_u_CAST_store
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_store_float + (-1)*C8_main_u_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_u_CAST_store
solver.Add( + (1)*main_q_fixp + (-1)*main_u_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_q_float + (-1)*main_u_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_q_double + (-1)*main_u_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_q_fixbits + (-1)*main_u_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_q_fixbits + (10000)*main_q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_u_enob_memphi_main_tmp34<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
f_enob_memphi_main_tmp35 = solver.IntVar(-10000, 10000, 'f_enob_memphi_main_tmp35')
solver.Add( + (1)*f_enob_memphi_main_tmp35 + (-1)*f_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp35_enob_0 = solver.IntVar(0, 1, 'main_main_tmp35_enob_0')
solver.Add( + (1)*main_main_tmp35_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*f_enob_memphi_main_tmp35 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp35_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double -0.000000e+00
ConstantValue__49_fixbits = solver.IntVar(0, 32, 'ConstantValue__49_fixbits')
ConstantValue__49_fixp = solver.IntVar(0, 1, 'ConstantValue__49_fixp')
ConstantValue__49_float = solver.IntVar(0, 1, 'ConstantValue__49_float')
ConstantValue__49_double = solver.IntVar(0, 1, 'ConstantValue__49_double')
ConstantValue__49_enob = solver.IntVar(-10000, 10000, 'ConstantValue__49_enob')
solver.Add( + (1)*ConstantValue__49_enob + (-1)*ConstantValue__49_fixbits + (10000)*ConstantValue__49_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__49_enob + (10000)*ConstantValue__49_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__49_enob + (10000)*ConstantValue__49_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__49_fixbits + (-10000)*ConstantValue__49_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__49_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__49_fixp + (1)*ConstantValue__49_float + (1)*ConstantValue__49_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__49_fixbits + (-10000)*ConstantValue__49_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__50_fixbits = solver.IntVar(0, 32, 'ConstantValue__50_fixbits')
ConstantValue__50_fixp = solver.IntVar(0, 1, 'ConstantValue__50_fixp')
ConstantValue__50_float = solver.IntVar(0, 1, 'ConstantValue__50_float')
ConstantValue__50_double = solver.IntVar(0, 1, 'ConstantValue__50_double')
ConstantValue__50_enob = solver.IntVar(-10000, 10000, 'ConstantValue__50_enob')
solver.Add( + (1)*ConstantValue__50_enob + (-1)*ConstantValue__50_fixbits + (10000)*ConstantValue__50_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__50_enob + (10000)*ConstantValue__50_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__50_enob + (10000)*ConstantValue__50_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__50_fixbits + (-10000)*ConstantValue__50_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__50_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__50_fixp + (1)*ConstantValue__50_float + (1)*ConstantValue__50_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__50_fixbits + (-10000)*ConstantValue__50_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__51_fixbits = solver.IntVar(0, 32, 'ConstantValue__51_fixbits')
ConstantValue__51_fixp = solver.IntVar(0, 1, 'ConstantValue__51_fixp')
ConstantValue__51_float = solver.IntVar(0, 1, 'ConstantValue__51_float')
ConstantValue__51_double = solver.IntVar(0, 1, 'ConstantValue__51_double')
ConstantValue__51_enob = solver.IntVar(-10000, 10000, 'ConstantValue__51_enob')
solver.Add( + (1)*ConstantValue__51_enob + (-1)*ConstantValue__51_fixbits + (10000)*ConstantValue__51_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__51_enob + (10000)*ConstantValue__51_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__51_enob + (10000)*ConstantValue__51_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__51_fixbits + (-10000)*ConstantValue__51_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__51_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__51_fixp + (1)*ConstantValue__51_float + (1)*ConstantValue__51_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__51_fixbits + (-10000)*ConstantValue__51_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub163 = fsub double -0.000000e+00, %tmp35, !taffo.info !98, !taffo.initweight !44, !taffo.constinfo !74
ConstantValue__51_CAST_sub163_fixbits = solver.IntVar(0, 32, 'ConstantValue__51_CAST_sub163_fixbits')
ConstantValue__51_CAST_sub163_fixp = solver.IntVar(0, 1, 'ConstantValue__51_CAST_sub163_fixp')
ConstantValue__51_CAST_sub163_float = solver.IntVar(0, 1, 'ConstantValue__51_CAST_sub163_float')
ConstantValue__51_CAST_sub163_double = solver.IntVar(0, 1, 'ConstantValue__51_CAST_sub163_double')
solver.Add( + (1)*ConstantValue__51_CAST_sub163_fixp + (1)*ConstantValue__51_CAST_sub163_float + (1)*ConstantValue__51_CAST_sub163_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__51_CAST_sub163_fixbits + (-10000)*ConstantValue__51_CAST_sub163_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C1_ConstantValue__51_CAST_sub163')
C2_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C2_ConstantValue__51_CAST_sub163')
solver.Add( + (1)*ConstantValue__51_fixbits + (-1)*ConstantValue__51_CAST_sub163_fixbits + (-10000)*C1_ConstantValue__51_CAST_sub163<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__51_fixbits + (1)*ConstantValue__51_CAST_sub163_fixbits + (-10000)*C2_ConstantValue__51_CAST_sub163<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__51_CAST_sub163
castCostObj +=  + (1)*C2_ConstantValue__51_CAST_sub163
C3_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C3_ConstantValue__51_CAST_sub163')
C4_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C4_ConstantValue__51_CAST_sub163')
C5_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C5_ConstantValue__51_CAST_sub163')
C6_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C6_ConstantValue__51_CAST_sub163')
C7_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C7_ConstantValue__51_CAST_sub163')
C8_ConstantValue__51_CAST_sub163 = solver.IntVar(0, 1, 'C8_ConstantValue__51_CAST_sub163')
solver.Add( + (1)*ConstantValue__51_fixp + (1)*ConstantValue__51_CAST_sub163_float + (-1)*C3_ConstantValue__51_CAST_sub163<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__51_CAST_sub163
solver.Add( + (1)*ConstantValue__51_float + (1)*ConstantValue__51_CAST_sub163_fixp + (-1)*C4_ConstantValue__51_CAST_sub163<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__51_CAST_sub163
solver.Add( + (1)*ConstantValue__51_fixp + (1)*ConstantValue__51_CAST_sub163_double + (-1)*C5_ConstantValue__51_CAST_sub163<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__51_CAST_sub163
solver.Add( + (1)*ConstantValue__51_double + (1)*ConstantValue__51_CAST_sub163_fixp + (-1)*C6_ConstantValue__51_CAST_sub163<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__51_CAST_sub163
solver.Add( + (1)*ConstantValue__51_float + (1)*ConstantValue__51_CAST_sub163_double + (-1)*C7_ConstantValue__51_CAST_sub163<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__51_CAST_sub163
solver.Add( + (1)*ConstantValue__51_double + (1)*ConstantValue__51_CAST_sub163_float + (-1)*C8_ConstantValue__51_CAST_sub163<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__51_CAST_sub163



#Constraint for cast for   %sub163 = fsub double -0.000000e+00, %tmp35, !taffo.info !98, !taffo.initweight !44, !taffo.constinfo !74
f_CAST_sub163_fixbits = solver.IntVar(0, 23, 'f_CAST_sub163_fixbits')
f_CAST_sub163_fixp = solver.IntVar(0, 1, 'f_CAST_sub163_fixp')
f_CAST_sub163_float = solver.IntVar(0, 1, 'f_CAST_sub163_float')
f_CAST_sub163_double = solver.IntVar(0, 1, 'f_CAST_sub163_double')
solver.Add( + (1)*f_CAST_sub163_fixp + (1)*f_CAST_sub163_float + (1)*f_CAST_sub163_double==1)    #exactly 1 type
solver.Add( + (1)*f_CAST_sub163_fixbits + (-10000)*f_CAST_sub163_fixp<=0)    #If no fix, fix frac part = 0
C1_f_CAST_sub163 = solver.IntVar(0, 1, 'C1_f_CAST_sub163')
C2_f_CAST_sub163 = solver.IntVar(0, 1, 'C2_f_CAST_sub163')
solver.Add( + (1)*f_fixbits + (-1)*f_CAST_sub163_fixbits + (-10000)*C1_f_CAST_sub163<=0)    #Shift cost 1
solver.Add( + (-1)*f_fixbits + (1)*f_CAST_sub163_fixbits + (-10000)*C2_f_CAST_sub163<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_f_CAST_sub163
castCostObj +=  + (1)*C2_f_CAST_sub163
C3_f_CAST_sub163 = solver.IntVar(0, 1, 'C3_f_CAST_sub163')
C4_f_CAST_sub163 = solver.IntVar(0, 1, 'C4_f_CAST_sub163')
C5_f_CAST_sub163 = solver.IntVar(0, 1, 'C5_f_CAST_sub163')
C6_f_CAST_sub163 = solver.IntVar(0, 1, 'C6_f_CAST_sub163')
C7_f_CAST_sub163 = solver.IntVar(0, 1, 'C7_f_CAST_sub163')
C8_f_CAST_sub163 = solver.IntVar(0, 1, 'C8_f_CAST_sub163')
solver.Add( + (1)*f_fixp + (1)*f_CAST_sub163_float + (-1)*C3_f_CAST_sub163<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_f_CAST_sub163
solver.Add( + (1)*f_float + (1)*f_CAST_sub163_fixp + (-1)*C4_f_CAST_sub163<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_f_CAST_sub163
solver.Add( + (1)*f_fixp + (1)*f_CAST_sub163_double + (-1)*C5_f_CAST_sub163<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_f_CAST_sub163
solver.Add( + (1)*f_double + (1)*f_CAST_sub163_fixp + (-1)*C6_f_CAST_sub163<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_f_CAST_sub163
solver.Add( + (1)*f_float + (1)*f_CAST_sub163_double + (-1)*C7_f_CAST_sub163<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_f_CAST_sub163
solver.Add( + (1)*f_double + (1)*f_CAST_sub163_float + (-1)*C8_f_CAST_sub163<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_f_CAST_sub163



#Stuff for   %sub163 = fsub double -0.000000e+00, %tmp35, !taffo.info !98, !taffo.initweight !44, !taffo.constinfo !74
main_sub163_fixbits = solver.IntVar(0, 24, 'main_sub163_fixbits')
main_sub163_fixp = solver.IntVar(0, 1, 'main_sub163_fixp')
main_sub163_float = solver.IntVar(0, 1, 'main_sub163_float')
main_sub163_double = solver.IntVar(0, 1, 'main_sub163_double')
main_sub163_enob = solver.IntVar(-10000, 10000, 'main_sub163_enob')
solver.Add( + (1)*main_sub163_enob + (-1)*main_sub163_fixbits + (10000)*main_sub163_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub163_enob + (10000)*main_sub163_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub163_enob + (10000)*main_sub163_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub163_fixbits + (-10000)*main_sub163_fixp>=-9977)    #Limit the lower number of frac bits24
solver.Add( + (1)*main_sub163_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub163_enob
solver.Add( + (1)*main_sub163_fixp + (1)*main_sub163_float + (1)*main_sub163_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub163_fixbits + (-10000)*main_sub163_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__51_CAST_sub163_fixp + (-1)*f_CAST_sub163_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__51_CAST_sub163_float + (-1)*f_CAST_sub163_float==0)    #float equality
solver.Add( + (1)*ConstantValue__51_CAST_sub163_double + (-1)*f_CAST_sub163_double==0)    #double equality
solver.Add( + (1)*ConstantValue__51_CAST_sub163_fixbits + (-1)*f_CAST_sub163_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__51_CAST_sub163_fixp + (-1)*main_sub163_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__51_CAST_sub163_float + (-1)*main_sub163_float==0)    #float equality
solver.Add( + (1)*ConstantValue__51_CAST_sub163_double + (-1)*main_sub163_double==0)    #double equality
solver.Add( + (1)*ConstantValue__51_CAST_sub163_fixbits + (-1)*main_sub163_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub163_fixp
mathCostObj +=  + (3)*main_sub163_float
mathCostObj +=  + (6.64928)*main_sub163_double
solver.Add( + (1)*main_sub163_enob + (-1)*ConstantValue__49_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub163_enob + (-1)*f_enob_memphi_main_tmp35<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
d_enob_memphi_main_tmp36 = solver.IntVar(-10000, 10000, 'd_enob_memphi_main_tmp36')
solver.Add( + (1)*d_enob_memphi_main_tmp36 + (-1)*d_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp36_enob_0 = solver.IntVar(0, 1, 'main_main_tmp36_enob_0')
solver.Add( + (1)*main_main_tmp36_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*d_enob_memphi_main_tmp36 + (-1)*d_enob_storeENOB + (10000)*main_main_tmp36_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_p_enob_memphi_main_tmp37 = solver.IntVar(-10000, 10000, 'main_p_enob_memphi_main_tmp37')
solver.Add( + (1)*main_p_enob_memphi_main_tmp37 + (-1)*main_p_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul169 = fmul double %tmp36, %tmp37, !taffo.info !125, !taffo.initweight !44
d_CAST_mul169_fixbits = solver.IntVar(0, 23, 'd_CAST_mul169_fixbits')
d_CAST_mul169_fixp = solver.IntVar(0, 1, 'd_CAST_mul169_fixp')
d_CAST_mul169_float = solver.IntVar(0, 1, 'd_CAST_mul169_float')
d_CAST_mul169_double = solver.IntVar(0, 1, 'd_CAST_mul169_double')
solver.Add( + (1)*d_CAST_mul169_fixp + (1)*d_CAST_mul169_float + (1)*d_CAST_mul169_double==1)    #exactly 1 type
solver.Add( + (1)*d_CAST_mul169_fixbits + (-10000)*d_CAST_mul169_fixp<=0)    #If no fix, fix frac part = 0
C1_d_CAST_mul169 = solver.IntVar(0, 1, 'C1_d_CAST_mul169')
C2_d_CAST_mul169 = solver.IntVar(0, 1, 'C2_d_CAST_mul169')
solver.Add( + (1)*d_fixbits + (-1)*d_CAST_mul169_fixbits + (-10000)*C1_d_CAST_mul169<=0)    #Shift cost 1
solver.Add( + (-1)*d_fixbits + (1)*d_CAST_mul169_fixbits + (-10000)*C2_d_CAST_mul169<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_d_CAST_mul169
castCostObj +=  + (1)*C2_d_CAST_mul169
C3_d_CAST_mul169 = solver.IntVar(0, 1, 'C3_d_CAST_mul169')
C4_d_CAST_mul169 = solver.IntVar(0, 1, 'C4_d_CAST_mul169')
C5_d_CAST_mul169 = solver.IntVar(0, 1, 'C5_d_CAST_mul169')
C6_d_CAST_mul169 = solver.IntVar(0, 1, 'C6_d_CAST_mul169')
C7_d_CAST_mul169 = solver.IntVar(0, 1, 'C7_d_CAST_mul169')
C8_d_CAST_mul169 = solver.IntVar(0, 1, 'C8_d_CAST_mul169')
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul169_float + (-1)*C3_d_CAST_mul169<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_d_CAST_mul169
solver.Add( + (1)*d_float + (1)*d_CAST_mul169_fixp + (-1)*C4_d_CAST_mul169<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_d_CAST_mul169
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul169_double + (-1)*C5_d_CAST_mul169<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_d_CAST_mul169
solver.Add( + (1)*d_double + (1)*d_CAST_mul169_fixp + (-1)*C6_d_CAST_mul169<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_d_CAST_mul169
solver.Add( + (1)*d_float + (1)*d_CAST_mul169_double + (-1)*C7_d_CAST_mul169<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_d_CAST_mul169
solver.Add( + (1)*d_double + (1)*d_CAST_mul169_float + (-1)*C8_d_CAST_mul169<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_d_CAST_mul169



#Constraint for cast for   %mul169 = fmul double %tmp36, %tmp37, !taffo.info !125, !taffo.initweight !44
main_p_CAST_mul169_fixbits = solver.IntVar(0, 30, 'main_p_CAST_mul169_fixbits')
main_p_CAST_mul169_fixp = solver.IntVar(0, 1, 'main_p_CAST_mul169_fixp')
main_p_CAST_mul169_float = solver.IntVar(0, 1, 'main_p_CAST_mul169_float')
main_p_CAST_mul169_double = solver.IntVar(0, 1, 'main_p_CAST_mul169_double')
solver.Add( + (1)*main_p_CAST_mul169_fixp + (1)*main_p_CAST_mul169_float + (1)*main_p_CAST_mul169_double==1)    #exactly 1 type
solver.Add( + (1)*main_p_CAST_mul169_fixbits + (-10000)*main_p_CAST_mul169_fixp<=0)    #If no fix, fix frac part = 0
C1_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C1_main_p_CAST_mul169')
C2_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C2_main_p_CAST_mul169')
solver.Add( + (1)*main_p_fixbits + (-1)*main_p_CAST_mul169_fixbits + (-10000)*C1_main_p_CAST_mul169<=0)    #Shift cost 1
solver.Add( + (-1)*main_p_fixbits + (1)*main_p_CAST_mul169_fixbits + (-10000)*C2_main_p_CAST_mul169<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_p_CAST_mul169
castCostObj +=  + (1)*C2_main_p_CAST_mul169
C3_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C3_main_p_CAST_mul169')
C4_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C4_main_p_CAST_mul169')
C5_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C5_main_p_CAST_mul169')
C6_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C6_main_p_CAST_mul169')
C7_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C7_main_p_CAST_mul169')
C8_main_p_CAST_mul169 = solver.IntVar(0, 1, 'C8_main_p_CAST_mul169')
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul169_float + (-1)*C3_main_p_CAST_mul169<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_p_CAST_mul169
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul169_fixp + (-1)*C4_main_p_CAST_mul169<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_p_CAST_mul169
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul169_double + (-1)*C5_main_p_CAST_mul169<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_p_CAST_mul169
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul169_fixp + (-1)*C6_main_p_CAST_mul169<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_p_CAST_mul169
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul169_double + (-1)*C7_main_p_CAST_mul169<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_p_CAST_mul169
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul169_float + (-1)*C8_main_p_CAST_mul169<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_p_CAST_mul169



#Stuff for   %mul169 = fmul double %tmp36, %tmp37, !taffo.info !125, !taffo.initweight !44
main_mul169_fixbits = solver.IntVar(0, 23, 'main_mul169_fixbits')
main_mul169_fixp = solver.IntVar(0, 1, 'main_mul169_fixp')
main_mul169_float = solver.IntVar(0, 1, 'main_mul169_float')
main_mul169_double = solver.IntVar(0, 1, 'main_mul169_double')
main_mul169_enob = solver.IntVar(-10000, 10000, 'main_mul169_enob')
solver.Add( + (1)*main_mul169_enob + (-1)*main_mul169_fixbits + (10000)*main_mul169_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul169_enob + (10000)*main_mul169_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul169_enob + (10000)*main_mul169_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul169_fixbits + (-10000)*main_mul169_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_mul169_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul169_enob
solver.Add( + (1)*main_mul169_fixp + (1)*main_mul169_float + (1)*main_mul169_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul169_fixbits + (-10000)*main_mul169_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*d_CAST_mul169_fixp + (-1)*main_p_CAST_mul169_fixp==0)    #fix equality
solver.Add( + (1)*d_CAST_mul169_float + (-1)*main_p_CAST_mul169_float==0)    #float equality
solver.Add( + (1)*d_CAST_mul169_double + (-1)*main_p_CAST_mul169_double==0)    #double equality
solver.Add( + (1)*d_CAST_mul169_fixp + (-1)*main_mul169_fixp==0)    #fix equality
solver.Add( + (1)*d_CAST_mul169_float + (-1)*main_mul169_float==0)    #float equality
solver.Add( + (1)*d_CAST_mul169_double + (-1)*main_mul169_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul169_fixp
mathCostObj +=  + (6)*main_mul169_float
mathCostObj +=  + (12.2551)*main_mul169_double
main_main_mul169_enob_1 = solver.IntVar(0, 1, 'main_main_mul169_enob_1')
main_main_mul169_enob_2 = solver.IntVar(0, 1, 'main_main_mul169_enob_2')
solver.Add( + (1)*main_main_mul169_enob_1 + (1)*main_main_mul169_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul169_enob + (-1)*main_p_enob_memphi_main_tmp37 + (-10000)*main_main_mul169_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul169_enob + (-1)*d_enob_memphi_main_tmp36 + (-10000)*main_main_mul169_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
e_enob_memphi_main_tmp38 = solver.IntVar(-10000, 10000, 'e_enob_memphi_main_tmp38')
solver.Add( + (1)*e_enob_memphi_main_tmp38 + (-1)*e_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp38_enob_0 = solver.IntVar(0, 1, 'main_main_tmp38_enob_0')
solver.Add( + (1)*main_main_tmp38_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*e_enob_memphi_main_tmp38 + (-1)*e_enob_storeENOB + (10000)*main_main_tmp38_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add170 = fadd double %mul169, %tmp38, !taffo.info !127, !taffo.initweight !44
main_mul169_CAST_add170_fixbits = solver.IntVar(0, 23, 'main_mul169_CAST_add170_fixbits')
main_mul169_CAST_add170_fixp = solver.IntVar(0, 1, 'main_mul169_CAST_add170_fixp')
main_mul169_CAST_add170_float = solver.IntVar(0, 1, 'main_mul169_CAST_add170_float')
main_mul169_CAST_add170_double = solver.IntVar(0, 1, 'main_mul169_CAST_add170_double')
solver.Add( + (1)*main_mul169_CAST_add170_fixp + (1)*main_mul169_CAST_add170_float + (1)*main_mul169_CAST_add170_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul169_CAST_add170_fixbits + (-10000)*main_mul169_CAST_add170_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C1_main_mul169_CAST_add170')
C2_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C2_main_mul169_CAST_add170')
solver.Add( + (1)*main_mul169_fixbits + (-1)*main_mul169_CAST_add170_fixbits + (-10000)*C1_main_mul169_CAST_add170<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul169_fixbits + (1)*main_mul169_CAST_add170_fixbits + (-10000)*C2_main_mul169_CAST_add170<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul169_CAST_add170
castCostObj +=  + (1)*C2_main_mul169_CAST_add170
C3_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C3_main_mul169_CAST_add170')
C4_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C4_main_mul169_CAST_add170')
C5_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C5_main_mul169_CAST_add170')
C6_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C6_main_mul169_CAST_add170')
C7_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C7_main_mul169_CAST_add170')
C8_main_mul169_CAST_add170 = solver.IntVar(0, 1, 'C8_main_mul169_CAST_add170')
solver.Add( + (1)*main_mul169_fixp + (1)*main_mul169_CAST_add170_float + (-1)*C3_main_mul169_CAST_add170<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul169_CAST_add170
solver.Add( + (1)*main_mul169_float + (1)*main_mul169_CAST_add170_fixp + (-1)*C4_main_mul169_CAST_add170<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul169_CAST_add170
solver.Add( + (1)*main_mul169_fixp + (1)*main_mul169_CAST_add170_double + (-1)*C5_main_mul169_CAST_add170<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul169_CAST_add170
solver.Add( + (1)*main_mul169_double + (1)*main_mul169_CAST_add170_fixp + (-1)*C6_main_mul169_CAST_add170<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul169_CAST_add170
solver.Add( + (1)*main_mul169_float + (1)*main_mul169_CAST_add170_double + (-1)*C7_main_mul169_CAST_add170<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul169_CAST_add170
solver.Add( + (1)*main_mul169_double + (1)*main_mul169_CAST_add170_float + (-1)*C8_main_mul169_CAST_add170<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul169_CAST_add170



#Constraint for cast for   %add170 = fadd double %mul169, %tmp38, !taffo.info !127, !taffo.initweight !44
e_CAST_add170_fixbits = solver.IntVar(0, 23, 'e_CAST_add170_fixbits')
e_CAST_add170_fixp = solver.IntVar(0, 1, 'e_CAST_add170_fixp')
e_CAST_add170_float = solver.IntVar(0, 1, 'e_CAST_add170_float')
e_CAST_add170_double = solver.IntVar(0, 1, 'e_CAST_add170_double')
solver.Add( + (1)*e_CAST_add170_fixp + (1)*e_CAST_add170_float + (1)*e_CAST_add170_double==1)    #exactly 1 type
solver.Add( + (1)*e_CAST_add170_fixbits + (-10000)*e_CAST_add170_fixp<=0)    #If no fix, fix frac part = 0
C1_e_CAST_add170 = solver.IntVar(0, 1, 'C1_e_CAST_add170')
C2_e_CAST_add170 = solver.IntVar(0, 1, 'C2_e_CAST_add170')
solver.Add( + (1)*e_fixbits + (-1)*e_CAST_add170_fixbits + (-10000)*C1_e_CAST_add170<=0)    #Shift cost 1
solver.Add( + (-1)*e_fixbits + (1)*e_CAST_add170_fixbits + (-10000)*C2_e_CAST_add170<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_e_CAST_add170
castCostObj +=  + (1)*C2_e_CAST_add170
C3_e_CAST_add170 = solver.IntVar(0, 1, 'C3_e_CAST_add170')
C4_e_CAST_add170 = solver.IntVar(0, 1, 'C4_e_CAST_add170')
C5_e_CAST_add170 = solver.IntVar(0, 1, 'C5_e_CAST_add170')
C6_e_CAST_add170 = solver.IntVar(0, 1, 'C6_e_CAST_add170')
C7_e_CAST_add170 = solver.IntVar(0, 1, 'C7_e_CAST_add170')
C8_e_CAST_add170 = solver.IntVar(0, 1, 'C8_e_CAST_add170')
solver.Add( + (1)*e_fixp + (1)*e_CAST_add170_float + (-1)*C3_e_CAST_add170<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_e_CAST_add170
solver.Add( + (1)*e_float + (1)*e_CAST_add170_fixp + (-1)*C4_e_CAST_add170<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_e_CAST_add170
solver.Add( + (1)*e_fixp + (1)*e_CAST_add170_double + (-1)*C5_e_CAST_add170<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_e_CAST_add170
solver.Add( + (1)*e_double + (1)*e_CAST_add170_fixp + (-1)*C6_e_CAST_add170<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_e_CAST_add170
solver.Add( + (1)*e_float + (1)*e_CAST_add170_double + (-1)*C7_e_CAST_add170<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_e_CAST_add170
solver.Add( + (1)*e_double + (1)*e_CAST_add170_float + (-1)*C8_e_CAST_add170<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_e_CAST_add170



#Stuff for   %add170 = fadd double %mul169, %tmp38, !taffo.info !127, !taffo.initweight !44
main_add170_fixbits = solver.IntVar(0, 21, 'main_add170_fixbits')
main_add170_fixp = solver.IntVar(0, 1, 'main_add170_fixp')
main_add170_float = solver.IntVar(0, 1, 'main_add170_float')
main_add170_double = solver.IntVar(0, 1, 'main_add170_double')
main_add170_enob = solver.IntVar(-10000, 10000, 'main_add170_enob')
solver.Add( + (1)*main_add170_enob + (-1)*main_add170_fixbits + (10000)*main_add170_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add170_enob + (10000)*main_add170_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add170_enob + (10000)*main_add170_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add170_fixbits + (-10000)*main_add170_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_add170_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add170_enob
solver.Add( + (1)*main_add170_fixp + (1)*main_add170_float + (1)*main_add170_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add170_fixbits + (-10000)*main_add170_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul169_CAST_add170_fixp + (-1)*e_CAST_add170_fixp==0)    #fix equality
solver.Add( + (1)*main_mul169_CAST_add170_float + (-1)*e_CAST_add170_float==0)    #float equality
solver.Add( + (1)*main_mul169_CAST_add170_double + (-1)*e_CAST_add170_double==0)    #double equality
solver.Add( + (1)*main_mul169_CAST_add170_fixbits + (-1)*e_CAST_add170_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul169_CAST_add170_fixp + (-1)*main_add170_fixp==0)    #fix equality
solver.Add( + (1)*main_mul169_CAST_add170_float + (-1)*main_add170_float==0)    #float equality
solver.Add( + (1)*main_mul169_CAST_add170_double + (-1)*main_add170_double==0)    #double equality
solver.Add( + (1)*main_mul169_CAST_add170_fixbits + (-1)*main_add170_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add170_fixp
mathCostObj +=  + (3)*main_add170_float
mathCostObj +=  + (6.64928)*main_add170_double
solver.Add( + (1)*main_add170_enob + (-1)*main_mul169_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add170_enob + (-1)*e_enob_memphi_main_tmp38<=0)    #Enob propagation in sum second addend



#Constraint for cast for   %div171 = fdiv double %sub163, %add170, !taffo.info !129, !taffo.initweight !45
main_sub163_CAST_div171_fixbits = solver.IntVar(0, 24, 'main_sub163_CAST_div171_fixbits')
main_sub163_CAST_div171_fixp = solver.IntVar(0, 1, 'main_sub163_CAST_div171_fixp')
main_sub163_CAST_div171_float = solver.IntVar(0, 1, 'main_sub163_CAST_div171_float')
main_sub163_CAST_div171_double = solver.IntVar(0, 1, 'main_sub163_CAST_div171_double')
solver.Add( + (1)*main_sub163_CAST_div171_fixp + (1)*main_sub163_CAST_div171_float + (1)*main_sub163_CAST_div171_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub163_CAST_div171_fixbits + (-10000)*main_sub163_CAST_div171_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C1_main_sub163_CAST_div171')
C2_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C2_main_sub163_CAST_div171')
solver.Add( + (1)*main_sub163_fixbits + (-1)*main_sub163_CAST_div171_fixbits + (-10000)*C1_main_sub163_CAST_div171<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub163_fixbits + (1)*main_sub163_CAST_div171_fixbits + (-10000)*C2_main_sub163_CAST_div171<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub163_CAST_div171
castCostObj +=  + (1)*C2_main_sub163_CAST_div171
C3_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C3_main_sub163_CAST_div171')
C4_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C4_main_sub163_CAST_div171')
C5_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C5_main_sub163_CAST_div171')
C6_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C6_main_sub163_CAST_div171')
C7_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C7_main_sub163_CAST_div171')
C8_main_sub163_CAST_div171 = solver.IntVar(0, 1, 'C8_main_sub163_CAST_div171')
solver.Add( + (1)*main_sub163_fixp + (1)*main_sub163_CAST_div171_float + (-1)*C3_main_sub163_CAST_div171<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub163_CAST_div171
solver.Add( + (1)*main_sub163_float + (1)*main_sub163_CAST_div171_fixp + (-1)*C4_main_sub163_CAST_div171<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub163_CAST_div171
solver.Add( + (1)*main_sub163_fixp + (1)*main_sub163_CAST_div171_double + (-1)*C5_main_sub163_CAST_div171<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub163_CAST_div171
solver.Add( + (1)*main_sub163_double + (1)*main_sub163_CAST_div171_fixp + (-1)*C6_main_sub163_CAST_div171<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub163_CAST_div171
solver.Add( + (1)*main_sub163_float + (1)*main_sub163_CAST_div171_double + (-1)*C7_main_sub163_CAST_div171<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub163_CAST_div171
solver.Add( + (1)*main_sub163_double + (1)*main_sub163_CAST_div171_float + (-1)*C8_main_sub163_CAST_div171<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub163_CAST_div171



#Constraint for cast for   %div171 = fdiv double %sub163, %add170, !taffo.info !129, !taffo.initweight !45
main_add170_CAST_div171_fixbits = solver.IntVar(0, 21, 'main_add170_CAST_div171_fixbits')
main_add170_CAST_div171_fixp = solver.IntVar(0, 1, 'main_add170_CAST_div171_fixp')
main_add170_CAST_div171_float = solver.IntVar(0, 1, 'main_add170_CAST_div171_float')
main_add170_CAST_div171_double = solver.IntVar(0, 1, 'main_add170_CAST_div171_double')
solver.Add( + (1)*main_add170_CAST_div171_fixp + (1)*main_add170_CAST_div171_float + (1)*main_add170_CAST_div171_double==1)    #exactly 1 type
solver.Add( + (1)*main_add170_CAST_div171_fixbits + (-10000)*main_add170_CAST_div171_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C1_main_add170_CAST_div171')
C2_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C2_main_add170_CAST_div171')
solver.Add( + (1)*main_add170_fixbits + (-1)*main_add170_CAST_div171_fixbits + (-10000)*C1_main_add170_CAST_div171<=0)    #Shift cost 1
solver.Add( + (-1)*main_add170_fixbits + (1)*main_add170_CAST_div171_fixbits + (-10000)*C2_main_add170_CAST_div171<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add170_CAST_div171
castCostObj +=  + (1)*C2_main_add170_CAST_div171
C3_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C3_main_add170_CAST_div171')
C4_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C4_main_add170_CAST_div171')
C5_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C5_main_add170_CAST_div171')
C6_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C6_main_add170_CAST_div171')
C7_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C7_main_add170_CAST_div171')
C8_main_add170_CAST_div171 = solver.IntVar(0, 1, 'C8_main_add170_CAST_div171')
solver.Add( + (1)*main_add170_fixp + (1)*main_add170_CAST_div171_float + (-1)*C3_main_add170_CAST_div171<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add170_CAST_div171
solver.Add( + (1)*main_add170_float + (1)*main_add170_CAST_div171_fixp + (-1)*C4_main_add170_CAST_div171<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add170_CAST_div171
solver.Add( + (1)*main_add170_fixp + (1)*main_add170_CAST_div171_double + (-1)*C5_main_add170_CAST_div171<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add170_CAST_div171
solver.Add( + (1)*main_add170_double + (1)*main_add170_CAST_div171_fixp + (-1)*C6_main_add170_CAST_div171<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add170_CAST_div171
solver.Add( + (1)*main_add170_float + (1)*main_add170_CAST_div171_double + (-1)*C7_main_add170_CAST_div171<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add170_CAST_div171
solver.Add( + (1)*main_add170_double + (1)*main_add170_CAST_div171_float + (-1)*C8_main_add170_CAST_div171<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add170_CAST_div171



#Stuff for   %div171 = fdiv double %sub163, %add170, !taffo.info !129, !taffo.initweight !45
main_div171_fixbits = solver.IntVar(0, 30, 'main_div171_fixbits')
main_div171_fixp = solver.IntVar(0, 1, 'main_div171_fixp')
main_div171_float = solver.IntVar(0, 1, 'main_div171_float')
main_div171_double = solver.IntVar(0, 1, 'main_div171_double')
main_div171_enob = solver.IntVar(-10000, 10000, 'main_div171_enob')
solver.Add( + (1)*main_div171_enob + (-1)*main_div171_fixbits + (10000)*main_div171_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div171_enob + (10000)*main_div171_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div171_enob + (10000)*main_div171_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div171_fixbits + (-10000)*main_div171_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*main_div171_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div171_enob
solver.Add( + (1)*main_div171_fixp + (1)*main_div171_float + (1)*main_div171_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div171_fixbits + (-10000)*main_div171_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub163_CAST_div171_fixp + (-1)*main_add170_CAST_div171_fixp==0)    #fix equality
solver.Add( + (1)*main_sub163_CAST_div171_float + (-1)*main_add170_CAST_div171_float==0)    #float equality
solver.Add( + (1)*main_sub163_CAST_div171_double + (-1)*main_add170_CAST_div171_double==0)    #double equality
solver.Add( + (1)*main_sub163_CAST_div171_fixp + (-1)*main_div171_fixp==0)    #fix equality
solver.Add( + (1)*main_sub163_CAST_div171_float + (-1)*main_div171_float==0)    #float equality
solver.Add( + (1)*main_sub163_CAST_div171_double + (-1)*main_div171_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div171_fixp
mathCostObj +=  + (6)*main_div171_float
mathCostObj +=  + (12)*main_div171_double
main_main_div171_enob_1 = solver.IntVar(0, 1, 'main_main_div171_enob_1')
main_main_div171_enob_2 = solver.IntVar(0, 1, 'main_main_div171_enob_2')
solver.Add( + (1)*main_main_div171_enob_1 + (1)*main_main_div171_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div171_enob + (-1)*main_add170_enob + (-10000)*main_main_div171_enob_1<=1042)    #Enob: propagation in division 1
solver.Add( + (1)*main_div171_enob + (-1)*main_sub163_enob + (-10000)*main_main_div171_enob_2<=1042)    #Enob: propagation in division 2



#Constraint for cast for   store double %div171, double* %arrayidx175, align 8, !taffo.info !37, !taffo.initweight !45
main_div171_CAST_store_fixbits = solver.IntVar(0, 30, 'main_div171_CAST_store_fixbits')
main_div171_CAST_store_fixp = solver.IntVar(0, 1, 'main_div171_CAST_store_fixp')
main_div171_CAST_store_float = solver.IntVar(0, 1, 'main_div171_CAST_store_float')
main_div171_CAST_store_double = solver.IntVar(0, 1, 'main_div171_CAST_store_double')
solver.Add( + (1)*main_div171_CAST_store_fixp + (1)*main_div171_CAST_store_float + (1)*main_div171_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div171_CAST_store_fixbits + (-10000)*main_div171_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div171_CAST_store = solver.IntVar(0, 1, 'C1_main_div171_CAST_store')
C2_main_div171_CAST_store = solver.IntVar(0, 1, 'C2_main_div171_CAST_store')
solver.Add( + (1)*main_div171_fixbits + (-1)*main_div171_CAST_store_fixbits + (-10000)*C1_main_div171_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div171_fixbits + (1)*main_div171_CAST_store_fixbits + (-10000)*C2_main_div171_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div171_CAST_store
castCostObj +=  + (1)*C2_main_div171_CAST_store
C3_main_div171_CAST_store = solver.IntVar(0, 1, 'C3_main_div171_CAST_store')
C4_main_div171_CAST_store = solver.IntVar(0, 1, 'C4_main_div171_CAST_store')
C5_main_div171_CAST_store = solver.IntVar(0, 1, 'C5_main_div171_CAST_store')
C6_main_div171_CAST_store = solver.IntVar(0, 1, 'C6_main_div171_CAST_store')
C7_main_div171_CAST_store = solver.IntVar(0, 1, 'C7_main_div171_CAST_store')
C8_main_div171_CAST_store = solver.IntVar(0, 1, 'C8_main_div171_CAST_store')
solver.Add( + (1)*main_div171_fixp + (1)*main_div171_CAST_store_float + (-1)*C3_main_div171_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div171_CAST_store
solver.Add( + (1)*main_div171_float + (1)*main_div171_CAST_store_fixp + (-1)*C4_main_div171_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div171_CAST_store
solver.Add( + (1)*main_div171_fixp + (1)*main_div171_CAST_store_double + (-1)*C5_main_div171_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div171_CAST_store
solver.Add( + (1)*main_div171_double + (1)*main_div171_CAST_store_fixp + (-1)*C6_main_div171_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div171_CAST_store
solver.Add( + (1)*main_div171_float + (1)*main_div171_CAST_store_double + (-1)*C7_main_div171_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div171_CAST_store
solver.Add( + (1)*main_div171_double + (1)*main_div171_CAST_store_float + (-1)*C8_main_div171_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div171_CAST_store
solver.Add( + (1)*main_p_fixp + (-1)*main_div171_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_p_float + (-1)*main_div171_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_p_double + (-1)*main_div171_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_p_fixbits + (-1)*main_div171_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_p_enob_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_p_enob_storeENOB_storeENOB')
solver.Add( + (1)*main_p_enob_storeENOB_storeENOB + (-1)*main_p_fixbits + (10000)*main_p_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_p_enob_storeENOB_storeENOB + (10000)*main_p_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_p_enob_storeENOB_storeENOB + (10000)*main_p_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_p_enob_storeENOB_storeENOB + (-1)*main_div171_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp39 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp39')
solver.Add( + (1)*a_enob_memphi_main_tmp39 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp39_enob_0 = solver.IntVar(0, 1, 'main_main_tmp39_enob_0')
solver.Add( + (1)*main_main_tmp39_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp39 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp39_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double -0.000000e+00
ConstantValue__52_fixbits = solver.IntVar(0, 32, 'ConstantValue__52_fixbits')
ConstantValue__52_fixp = solver.IntVar(0, 1, 'ConstantValue__52_fixp')
ConstantValue__52_float = solver.IntVar(0, 1, 'ConstantValue__52_float')
ConstantValue__52_double = solver.IntVar(0, 1, 'ConstantValue__52_double')
ConstantValue__52_enob = solver.IntVar(-10000, 10000, 'ConstantValue__52_enob')
solver.Add( + (1)*ConstantValue__52_enob + (-1)*ConstantValue__52_fixbits + (10000)*ConstantValue__52_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__52_enob + (10000)*ConstantValue__52_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__52_enob + (10000)*ConstantValue__52_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__52_fixbits + (-10000)*ConstantValue__52_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__52_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__52_fixp + (1)*ConstantValue__52_float + (1)*ConstantValue__52_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__52_fixbits + (-10000)*ConstantValue__52_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__53_fixbits = solver.IntVar(0, 32, 'ConstantValue__53_fixbits')
ConstantValue__53_fixp = solver.IntVar(0, 1, 'ConstantValue__53_fixp')
ConstantValue__53_float = solver.IntVar(0, 1, 'ConstantValue__53_float')
ConstantValue__53_double = solver.IntVar(0, 1, 'ConstantValue__53_double')
ConstantValue__53_enob = solver.IntVar(-10000, 10000, 'ConstantValue__53_enob')
solver.Add( + (1)*ConstantValue__53_enob + (-1)*ConstantValue__53_fixbits + (10000)*ConstantValue__53_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__53_enob + (10000)*ConstantValue__53_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__53_enob + (10000)*ConstantValue__53_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__53_fixbits + (-10000)*ConstantValue__53_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__53_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__53_fixp + (1)*ConstantValue__53_float + (1)*ConstantValue__53_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__53_fixbits + (-10000)*ConstantValue__53_fixp<=0)    #If not fix, frac part to zero



#Stuff for double -0.000000e+00
ConstantValue__54_fixbits = solver.IntVar(0, 32, 'ConstantValue__54_fixbits')
ConstantValue__54_fixp = solver.IntVar(0, 1, 'ConstantValue__54_fixp')
ConstantValue__54_float = solver.IntVar(0, 1, 'ConstantValue__54_float')
ConstantValue__54_double = solver.IntVar(0, 1, 'ConstantValue__54_double')
ConstantValue__54_enob = solver.IntVar(-10000, 10000, 'ConstantValue__54_enob')
solver.Add( + (1)*ConstantValue__54_enob + (-1)*ConstantValue__54_fixbits + (10000)*ConstantValue__54_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__54_enob + (10000)*ConstantValue__54_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__54_enob + (10000)*ConstantValue__54_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__54_fixbits + (-10000)*ConstantValue__54_fixp>=-9969)    #Limit the lower number of frac bits32
solver.Add( + (1)*ConstantValue__54_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__54_fixp + (1)*ConstantValue__54_float + (1)*ConstantValue__54_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__54_fixbits + (-10000)*ConstantValue__54_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %sub176 = fsub double -0.000000e+00, %tmp39, !taffo.info !90, !taffo.initweight !44, !taffo.constinfo !74
ConstantValue__54_CAST_sub176_fixbits = solver.IntVar(0, 32, 'ConstantValue__54_CAST_sub176_fixbits')
ConstantValue__54_CAST_sub176_fixp = solver.IntVar(0, 1, 'ConstantValue__54_CAST_sub176_fixp')
ConstantValue__54_CAST_sub176_float = solver.IntVar(0, 1, 'ConstantValue__54_CAST_sub176_float')
ConstantValue__54_CAST_sub176_double = solver.IntVar(0, 1, 'ConstantValue__54_CAST_sub176_double')
solver.Add( + (1)*ConstantValue__54_CAST_sub176_fixp + (1)*ConstantValue__54_CAST_sub176_float + (1)*ConstantValue__54_CAST_sub176_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__54_CAST_sub176_fixbits + (-10000)*ConstantValue__54_CAST_sub176_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C1_ConstantValue__54_CAST_sub176')
C2_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C2_ConstantValue__54_CAST_sub176')
solver.Add( + (1)*ConstantValue__54_fixbits + (-1)*ConstantValue__54_CAST_sub176_fixbits + (-10000)*C1_ConstantValue__54_CAST_sub176<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__54_fixbits + (1)*ConstantValue__54_CAST_sub176_fixbits + (-10000)*C2_ConstantValue__54_CAST_sub176<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__54_CAST_sub176
castCostObj +=  + (1)*C2_ConstantValue__54_CAST_sub176
C3_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C3_ConstantValue__54_CAST_sub176')
C4_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C4_ConstantValue__54_CAST_sub176')
C5_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C5_ConstantValue__54_CAST_sub176')
C6_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C6_ConstantValue__54_CAST_sub176')
C7_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C7_ConstantValue__54_CAST_sub176')
C8_ConstantValue__54_CAST_sub176 = solver.IntVar(0, 1, 'C8_ConstantValue__54_CAST_sub176')
solver.Add( + (1)*ConstantValue__54_fixp + (1)*ConstantValue__54_CAST_sub176_float + (-1)*C3_ConstantValue__54_CAST_sub176<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__54_CAST_sub176
solver.Add( + (1)*ConstantValue__54_float + (1)*ConstantValue__54_CAST_sub176_fixp + (-1)*C4_ConstantValue__54_CAST_sub176<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__54_CAST_sub176
solver.Add( + (1)*ConstantValue__54_fixp + (1)*ConstantValue__54_CAST_sub176_double + (-1)*C5_ConstantValue__54_CAST_sub176<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__54_CAST_sub176
solver.Add( + (1)*ConstantValue__54_double + (1)*ConstantValue__54_CAST_sub176_fixp + (-1)*C6_ConstantValue__54_CAST_sub176<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__54_CAST_sub176
solver.Add( + (1)*ConstantValue__54_float + (1)*ConstantValue__54_CAST_sub176_double + (-1)*C7_ConstantValue__54_CAST_sub176<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__54_CAST_sub176
solver.Add( + (1)*ConstantValue__54_double + (1)*ConstantValue__54_CAST_sub176_float + (-1)*C8_ConstantValue__54_CAST_sub176<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__54_CAST_sub176



#Constraint for cast for   %sub176 = fsub double -0.000000e+00, %tmp39, !taffo.info !90, !taffo.initweight !44, !taffo.constinfo !74
a_CAST_sub176_fixbits = solver.IntVar(0, 22, 'a_CAST_sub176_fixbits')
a_CAST_sub176_fixp = solver.IntVar(0, 1, 'a_CAST_sub176_fixp')
a_CAST_sub176_float = solver.IntVar(0, 1, 'a_CAST_sub176_float')
a_CAST_sub176_double = solver.IntVar(0, 1, 'a_CAST_sub176_double')
solver.Add( + (1)*a_CAST_sub176_fixp + (1)*a_CAST_sub176_float + (1)*a_CAST_sub176_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_sub176_fixbits + (-10000)*a_CAST_sub176_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_sub176 = solver.IntVar(0, 1, 'C1_a_CAST_sub176')
C2_a_CAST_sub176 = solver.IntVar(0, 1, 'C2_a_CAST_sub176')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_sub176_fixbits + (-10000)*C1_a_CAST_sub176<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_sub176_fixbits + (-10000)*C2_a_CAST_sub176<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_a_CAST_sub176
castCostObj +=  + (1)*C2_a_CAST_sub176
C3_a_CAST_sub176 = solver.IntVar(0, 1, 'C3_a_CAST_sub176')
C4_a_CAST_sub176 = solver.IntVar(0, 1, 'C4_a_CAST_sub176')
C5_a_CAST_sub176 = solver.IntVar(0, 1, 'C5_a_CAST_sub176')
C6_a_CAST_sub176 = solver.IntVar(0, 1, 'C6_a_CAST_sub176')
C7_a_CAST_sub176 = solver.IntVar(0, 1, 'C7_a_CAST_sub176')
C8_a_CAST_sub176 = solver.IntVar(0, 1, 'C8_a_CAST_sub176')
solver.Add( + (1)*a_fixp + (1)*a_CAST_sub176_float + (-1)*C3_a_CAST_sub176<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_a_CAST_sub176
solver.Add( + (1)*a_float + (1)*a_CAST_sub176_fixp + (-1)*C4_a_CAST_sub176<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_a_CAST_sub176
solver.Add( + (1)*a_fixp + (1)*a_CAST_sub176_double + (-1)*C5_a_CAST_sub176<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_a_CAST_sub176
solver.Add( + (1)*a_double + (1)*a_CAST_sub176_fixp + (-1)*C6_a_CAST_sub176<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_a_CAST_sub176
solver.Add( + (1)*a_float + (1)*a_CAST_sub176_double + (-1)*C7_a_CAST_sub176<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_a_CAST_sub176
solver.Add( + (1)*a_double + (1)*a_CAST_sub176_float + (-1)*C8_a_CAST_sub176<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_a_CAST_sub176



#Stuff for   %sub176 = fsub double -0.000000e+00, %tmp39, !taffo.info !90, !taffo.initweight !44, !taffo.constinfo !74
main_sub176_fixbits = solver.IntVar(0, 23, 'main_sub176_fixbits')
main_sub176_fixp = solver.IntVar(0, 1, 'main_sub176_fixp')
main_sub176_float = solver.IntVar(0, 1, 'main_sub176_float')
main_sub176_double = solver.IntVar(0, 1, 'main_sub176_double')
main_sub176_enob = solver.IntVar(-10000, 10000, 'main_sub176_enob')
solver.Add( + (1)*main_sub176_enob + (-1)*main_sub176_fixbits + (10000)*main_sub176_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub176_enob + (10000)*main_sub176_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub176_enob + (10000)*main_sub176_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub176_fixbits + (-10000)*main_sub176_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_sub176_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub176_enob
solver.Add( + (1)*main_sub176_fixp + (1)*main_sub176_float + (1)*main_sub176_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub176_fixbits + (-10000)*main_sub176_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__54_CAST_sub176_fixp + (-1)*a_CAST_sub176_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__54_CAST_sub176_float + (-1)*a_CAST_sub176_float==0)    #float equality
solver.Add( + (1)*ConstantValue__54_CAST_sub176_double + (-1)*a_CAST_sub176_double==0)    #double equality
solver.Add( + (1)*ConstantValue__54_CAST_sub176_fixbits + (-1)*a_CAST_sub176_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__54_CAST_sub176_fixp + (-1)*main_sub176_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__54_CAST_sub176_float + (-1)*main_sub176_float==0)    #float equality
solver.Add( + (1)*ConstantValue__54_CAST_sub176_double + (-1)*main_sub176_double==0)    #double equality
solver.Add( + (1)*ConstantValue__54_CAST_sub176_fixbits + (-1)*main_sub176_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub176_fixp
mathCostObj +=  + (3)*main_sub176_float
mathCostObj +=  + (6.64928)*main_sub176_double
solver.Add( + (1)*main_sub176_enob + (-1)*ConstantValue__52_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub176_enob + (-1)*a_enob_memphi_main_tmp39<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
main_v_enob_memphi_main_tmp40 = solver.IntVar(-10000, 10000, 'main_v_enob_memphi_main_tmp40')
solver.Add( + (1)*main_v_enob_memphi_main_tmp40 + (-1)*main_v_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp40_enob_0 = solver.IntVar(0, 1, 'main_main_tmp40_enob_0')
main_main_tmp40_enob_1 = solver.IntVar(0, 1, 'main_main_tmp40_enob_1')
main_main_tmp40_enob_2 = solver.IntVar(0, 1, 'main_main_tmp40_enob_2')
main_main_tmp40_enob_4 = solver.IntVar(0, 1, 'main_main_tmp40_enob_4')
solver.Add( + (1)*main_main_tmp40_enob_0 + (1)*main_main_tmp40_enob_1 + (1)*main_main_tmp40_enob_2 + (1)*main_main_tmp40_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp40 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp40_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp40 + (-1)*main_v_enob_storeENOB + (10000)*main_main_tmp40_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul182 = fmul double %sub176, %tmp40, !taffo.info !100, !taffo.initweight !45
main_sub176_CAST_mul182_fixbits = solver.IntVar(0, 23, 'main_sub176_CAST_mul182_fixbits')
main_sub176_CAST_mul182_fixp = solver.IntVar(0, 1, 'main_sub176_CAST_mul182_fixp')
main_sub176_CAST_mul182_float = solver.IntVar(0, 1, 'main_sub176_CAST_mul182_float')
main_sub176_CAST_mul182_double = solver.IntVar(0, 1, 'main_sub176_CAST_mul182_double')
solver.Add( + (1)*main_sub176_CAST_mul182_fixp + (1)*main_sub176_CAST_mul182_float + (1)*main_sub176_CAST_mul182_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub176_CAST_mul182_fixbits + (-10000)*main_sub176_CAST_mul182_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C1_main_sub176_CAST_mul182')
C2_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C2_main_sub176_CAST_mul182')
solver.Add( + (1)*main_sub176_fixbits + (-1)*main_sub176_CAST_mul182_fixbits + (-10000)*C1_main_sub176_CAST_mul182<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub176_fixbits + (1)*main_sub176_CAST_mul182_fixbits + (-10000)*C2_main_sub176_CAST_mul182<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub176_CAST_mul182
castCostObj +=  + (1)*C2_main_sub176_CAST_mul182
C3_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C3_main_sub176_CAST_mul182')
C4_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C4_main_sub176_CAST_mul182')
C5_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C5_main_sub176_CAST_mul182')
C6_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C6_main_sub176_CAST_mul182')
C7_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C7_main_sub176_CAST_mul182')
C8_main_sub176_CAST_mul182 = solver.IntVar(0, 1, 'C8_main_sub176_CAST_mul182')
solver.Add( + (1)*main_sub176_fixp + (1)*main_sub176_CAST_mul182_float + (-1)*C3_main_sub176_CAST_mul182<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub176_CAST_mul182
solver.Add( + (1)*main_sub176_float + (1)*main_sub176_CAST_mul182_fixp + (-1)*C4_main_sub176_CAST_mul182<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub176_CAST_mul182
solver.Add( + (1)*main_sub176_fixp + (1)*main_sub176_CAST_mul182_double + (-1)*C5_main_sub176_CAST_mul182<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub176_CAST_mul182
solver.Add( + (1)*main_sub176_double + (1)*main_sub176_CAST_mul182_fixp + (-1)*C6_main_sub176_CAST_mul182<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub176_CAST_mul182
solver.Add( + (1)*main_sub176_float + (1)*main_sub176_CAST_mul182_double + (-1)*C7_main_sub176_CAST_mul182<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub176_CAST_mul182
solver.Add( + (1)*main_sub176_double + (1)*main_sub176_CAST_mul182_float + (-1)*C8_main_sub176_CAST_mul182<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub176_CAST_mul182



#Constraint for cast for   %mul182 = fmul double %sub176, %tmp40, !taffo.info !100, !taffo.initweight !45
main_v_CAST_mul182_fixbits = solver.IntVar(0, 29, 'main_v_CAST_mul182_fixbits')
main_v_CAST_mul182_fixp = solver.IntVar(0, 1, 'main_v_CAST_mul182_fixp')
main_v_CAST_mul182_float = solver.IntVar(0, 1, 'main_v_CAST_mul182_float')
main_v_CAST_mul182_double = solver.IntVar(0, 1, 'main_v_CAST_mul182_double')
solver.Add( + (1)*main_v_CAST_mul182_fixp + (1)*main_v_CAST_mul182_float + (1)*main_v_CAST_mul182_double==1)    #exactly 1 type
solver.Add( + (1)*main_v_CAST_mul182_fixbits + (-10000)*main_v_CAST_mul182_fixp<=0)    #If no fix, fix frac part = 0
C1_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C1_main_v_CAST_mul182')
C2_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C2_main_v_CAST_mul182')
solver.Add( + (1)*main_v_fixbits + (-1)*main_v_CAST_mul182_fixbits + (-10000)*C1_main_v_CAST_mul182<=0)    #Shift cost 1
solver.Add( + (-1)*main_v_fixbits + (1)*main_v_CAST_mul182_fixbits + (-10000)*C2_main_v_CAST_mul182<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_v_CAST_mul182
castCostObj +=  + (1)*C2_main_v_CAST_mul182
C3_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C3_main_v_CAST_mul182')
C4_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C4_main_v_CAST_mul182')
C5_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C5_main_v_CAST_mul182')
C6_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C6_main_v_CAST_mul182')
C7_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C7_main_v_CAST_mul182')
C8_main_v_CAST_mul182 = solver.IntVar(0, 1, 'C8_main_v_CAST_mul182')
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul182_float + (-1)*C3_main_v_CAST_mul182<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_v_CAST_mul182
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul182_fixp + (-1)*C4_main_v_CAST_mul182<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_v_CAST_mul182
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul182_double + (-1)*C5_main_v_CAST_mul182<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_v_CAST_mul182
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul182_fixp + (-1)*C6_main_v_CAST_mul182<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_v_CAST_mul182
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul182_double + (-1)*C7_main_v_CAST_mul182<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_v_CAST_mul182
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul182_float + (-1)*C8_main_v_CAST_mul182<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_v_CAST_mul182



#Stuff for   %mul182 = fmul double %sub176, %tmp40, !taffo.info !100, !taffo.initweight !45
main_mul182_fixbits = solver.IntVar(0, 21, 'main_mul182_fixbits')
main_mul182_fixp = solver.IntVar(0, 1, 'main_mul182_fixp')
main_mul182_float = solver.IntVar(0, 1, 'main_mul182_float')
main_mul182_double = solver.IntVar(0, 1, 'main_mul182_double')
main_mul182_enob = solver.IntVar(-10000, 10000, 'main_mul182_enob')
solver.Add( + (1)*main_mul182_enob + (-1)*main_mul182_fixbits + (10000)*main_mul182_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul182_enob + (10000)*main_mul182_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul182_enob + (10000)*main_mul182_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul182_fixbits + (-10000)*main_mul182_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_mul182_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul182_enob
solver.Add( + (1)*main_mul182_fixp + (1)*main_mul182_float + (1)*main_mul182_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul182_fixbits + (-10000)*main_mul182_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub176_CAST_mul182_fixp + (-1)*main_v_CAST_mul182_fixp==0)    #fix equality
solver.Add( + (1)*main_sub176_CAST_mul182_float + (-1)*main_v_CAST_mul182_float==0)    #float equality
solver.Add( + (1)*main_sub176_CAST_mul182_double + (-1)*main_v_CAST_mul182_double==0)    #double equality
solver.Add( + (1)*main_sub176_CAST_mul182_fixp + (-1)*main_mul182_fixp==0)    #fix equality
solver.Add( + (1)*main_sub176_CAST_mul182_float + (-1)*main_mul182_float==0)    #float equality
solver.Add( + (1)*main_sub176_CAST_mul182_double + (-1)*main_mul182_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul182_fixp
mathCostObj +=  + (6)*main_mul182_float
mathCostObj +=  + (12.2551)*main_mul182_double
main_main_mul182_enob_1 = solver.IntVar(0, 1, 'main_main_mul182_enob_1')
main_main_mul182_enob_2 = solver.IntVar(0, 1, 'main_main_mul182_enob_2')
solver.Add( + (1)*main_main_mul182_enob_1 + (1)*main_main_mul182_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul182_enob + (-1)*main_v_enob_memphi_main_tmp40 + (-10000)*main_main_mul182_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul182_enob + (-1)*main_sub176_enob + (-10000)*main_main_mul182_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
a_enob_memphi_main_tmp41 = solver.IntVar(-10000, 10000, 'a_enob_memphi_main_tmp41')
solver.Add( + (1)*a_enob_memphi_main_tmp41 + (-1)*a_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp41_enob_0 = solver.IntVar(0, 1, 'main_main_tmp41_enob_0')
solver.Add( + (1)*main_main_tmp41_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*a_enob_memphi_main_tmp41 + (-1)*a_enob_storeENOB + (10000)*main_main_tmp41_enob_0<=10000)    #Enob: forcing MEM phi enob



#Stuff for double 2.000000e+00
ConstantValue__55_fixbits = solver.IntVar(0, 30, 'ConstantValue__55_fixbits')
ConstantValue__55_fixp = solver.IntVar(0, 1, 'ConstantValue__55_fixp')
ConstantValue__55_float = solver.IntVar(0, 1, 'ConstantValue__55_float')
ConstantValue__55_double = solver.IntVar(0, 1, 'ConstantValue__55_double')
ConstantValue__55_enob = solver.IntVar(-10000, 10000, 'ConstantValue__55_enob')
solver.Add( + (1)*ConstantValue__55_enob + (-1)*ConstantValue__55_fixbits + (10000)*ConstantValue__55_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__55_enob + (10000)*ConstantValue__55_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__55_enob + (10000)*ConstantValue__55_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__55_fixbits + (-10000)*ConstantValue__55_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__55_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__55_fixp + (1)*ConstantValue__55_float + (1)*ConstantValue__55_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__55_fixbits + (-10000)*ConstantValue__55_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__56_fixbits = solver.IntVar(0, 30, 'ConstantValue__56_fixbits')
ConstantValue__56_fixp = solver.IntVar(0, 1, 'ConstantValue__56_fixp')
ConstantValue__56_float = solver.IntVar(0, 1, 'ConstantValue__56_float')
ConstantValue__56_double = solver.IntVar(0, 1, 'ConstantValue__56_double')
ConstantValue__56_enob = solver.IntVar(-10000, 10000, 'ConstantValue__56_enob')
solver.Add( + (1)*ConstantValue__56_enob + (-1)*ConstantValue__56_fixbits + (10000)*ConstantValue__56_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__56_enob + (10000)*ConstantValue__56_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__56_enob + (10000)*ConstantValue__56_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__56_fixbits + (-10000)*ConstantValue__56_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__56_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__56_fixp + (1)*ConstantValue__56_float + (1)*ConstantValue__56_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__56_fixbits + (-10000)*ConstantValue__56_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 2.000000e+00
ConstantValue__57_fixbits = solver.IntVar(0, 30, 'ConstantValue__57_fixbits')
ConstantValue__57_fixp = solver.IntVar(0, 1, 'ConstantValue__57_fixp')
ConstantValue__57_float = solver.IntVar(0, 1, 'ConstantValue__57_float')
ConstantValue__57_double = solver.IntVar(0, 1, 'ConstantValue__57_double')
ConstantValue__57_enob = solver.IntVar(-10000, 10000, 'ConstantValue__57_enob')
solver.Add( + (1)*ConstantValue__57_enob + (-1)*ConstantValue__57_fixbits + (10000)*ConstantValue__57_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__57_enob + (10000)*ConstantValue__57_float<=10022)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__57_enob + (10000)*ConstantValue__57_double<=10051)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__57_fixbits + (-10000)*ConstantValue__57_fixp>=-9971)    #Limit the lower number of frac bits30
solver.Add( + (1)*ConstantValue__57_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__57_fixp + (1)*ConstantValue__57_float + (1)*ConstantValue__57_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__57_fixbits + (-10000)*ConstantValue__57_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %mul183 = fmul double 2.000000e+00, %tmp41, !taffo.info !131, !taffo.initweight !44, !taffo.constinfo !63
ConstantValue__57_CAST_mul183_fixbits = solver.IntVar(0, 30, 'ConstantValue__57_CAST_mul183_fixbits')
ConstantValue__57_CAST_mul183_fixp = solver.IntVar(0, 1, 'ConstantValue__57_CAST_mul183_fixp')
ConstantValue__57_CAST_mul183_float = solver.IntVar(0, 1, 'ConstantValue__57_CAST_mul183_float')
ConstantValue__57_CAST_mul183_double = solver.IntVar(0, 1, 'ConstantValue__57_CAST_mul183_double')
solver.Add( + (1)*ConstantValue__57_CAST_mul183_fixp + (1)*ConstantValue__57_CAST_mul183_float + (1)*ConstantValue__57_CAST_mul183_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__57_CAST_mul183_fixbits + (-10000)*ConstantValue__57_CAST_mul183_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C1_ConstantValue__57_CAST_mul183')
C2_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C2_ConstantValue__57_CAST_mul183')
solver.Add( + (1)*ConstantValue__57_fixbits + (-1)*ConstantValue__57_CAST_mul183_fixbits + (-10000)*C1_ConstantValue__57_CAST_mul183<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__57_fixbits + (1)*ConstantValue__57_CAST_mul183_fixbits + (-10000)*C2_ConstantValue__57_CAST_mul183<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__57_CAST_mul183
castCostObj +=  + (1)*C2_ConstantValue__57_CAST_mul183
C3_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C3_ConstantValue__57_CAST_mul183')
C4_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C4_ConstantValue__57_CAST_mul183')
C5_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C5_ConstantValue__57_CAST_mul183')
C6_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C6_ConstantValue__57_CAST_mul183')
C7_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C7_ConstantValue__57_CAST_mul183')
C8_ConstantValue__57_CAST_mul183 = solver.IntVar(0, 1, 'C8_ConstantValue__57_CAST_mul183')
solver.Add( + (1)*ConstantValue__57_fixp + (1)*ConstantValue__57_CAST_mul183_float + (-1)*C3_ConstantValue__57_CAST_mul183<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__57_CAST_mul183
solver.Add( + (1)*ConstantValue__57_float + (1)*ConstantValue__57_CAST_mul183_fixp + (-1)*C4_ConstantValue__57_CAST_mul183<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__57_CAST_mul183
solver.Add( + (1)*ConstantValue__57_fixp + (1)*ConstantValue__57_CAST_mul183_double + (-1)*C5_ConstantValue__57_CAST_mul183<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__57_CAST_mul183
solver.Add( + (1)*ConstantValue__57_double + (1)*ConstantValue__57_CAST_mul183_fixp + (-1)*C6_ConstantValue__57_CAST_mul183<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__57_CAST_mul183
solver.Add( + (1)*ConstantValue__57_float + (1)*ConstantValue__57_CAST_mul183_double + (-1)*C7_ConstantValue__57_CAST_mul183<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__57_CAST_mul183
solver.Add( + (1)*ConstantValue__57_double + (1)*ConstantValue__57_CAST_mul183_float + (-1)*C8_ConstantValue__57_CAST_mul183<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__57_CAST_mul183



#Constraint for cast for   %mul183 = fmul double 2.000000e+00, %tmp41, !taffo.info !131, !taffo.initweight !44, !taffo.constinfo !63
a_CAST_mul183_fixbits = solver.IntVar(0, 22, 'a_CAST_mul183_fixbits')
a_CAST_mul183_fixp = solver.IntVar(0, 1, 'a_CAST_mul183_fixp')
a_CAST_mul183_float = solver.IntVar(0, 1, 'a_CAST_mul183_float')
a_CAST_mul183_double = solver.IntVar(0, 1, 'a_CAST_mul183_double')
solver.Add( + (1)*a_CAST_mul183_fixp + (1)*a_CAST_mul183_float + (1)*a_CAST_mul183_double==1)    #exactly 1 type
solver.Add( + (1)*a_CAST_mul183_fixbits + (-10000)*a_CAST_mul183_fixp<=0)    #If no fix, fix frac part = 0
C1_a_CAST_mul183 = solver.IntVar(0, 1, 'C1_a_CAST_mul183')
C2_a_CAST_mul183 = solver.IntVar(0, 1, 'C2_a_CAST_mul183')
solver.Add( + (1)*a_fixbits + (-1)*a_CAST_mul183_fixbits + (-10000)*C1_a_CAST_mul183<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_CAST_mul183_fixbits + (-10000)*C2_a_CAST_mul183<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_a_CAST_mul183
castCostObj +=  + (1)*C2_a_CAST_mul183
C3_a_CAST_mul183 = solver.IntVar(0, 1, 'C3_a_CAST_mul183')
C4_a_CAST_mul183 = solver.IntVar(0, 1, 'C4_a_CAST_mul183')
C5_a_CAST_mul183 = solver.IntVar(0, 1, 'C5_a_CAST_mul183')
C6_a_CAST_mul183 = solver.IntVar(0, 1, 'C6_a_CAST_mul183')
C7_a_CAST_mul183 = solver.IntVar(0, 1, 'C7_a_CAST_mul183')
C8_a_CAST_mul183 = solver.IntVar(0, 1, 'C8_a_CAST_mul183')
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul183_float + (-1)*C3_a_CAST_mul183<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_a_CAST_mul183
solver.Add( + (1)*a_float + (1)*a_CAST_mul183_fixp + (-1)*C4_a_CAST_mul183<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_a_CAST_mul183
solver.Add( + (1)*a_fixp + (1)*a_CAST_mul183_double + (-1)*C5_a_CAST_mul183<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_a_CAST_mul183
solver.Add( + (1)*a_double + (1)*a_CAST_mul183_fixp + (-1)*C6_a_CAST_mul183<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_a_CAST_mul183
solver.Add( + (1)*a_float + (1)*a_CAST_mul183_double + (-1)*C7_a_CAST_mul183<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_a_CAST_mul183
solver.Add( + (1)*a_double + (1)*a_CAST_mul183_float + (-1)*C8_a_CAST_mul183<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_a_CAST_mul183



#Stuff for   %mul183 = fmul double 2.000000e+00, %tmp41, !taffo.info !131, !taffo.initweight !44, !taffo.constinfo !63
main_mul183_fixbits = solver.IntVar(0, 21, 'main_mul183_fixbits')
main_mul183_fixp = solver.IntVar(0, 1, 'main_mul183_fixp')
main_mul183_float = solver.IntVar(0, 1, 'main_mul183_float')
main_mul183_double = solver.IntVar(0, 1, 'main_mul183_double')
main_mul183_enob = solver.IntVar(-10000, 10000, 'main_mul183_enob')
solver.Add( + (1)*main_mul183_enob + (-1)*main_mul183_fixbits + (10000)*main_mul183_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul183_enob + (10000)*main_mul183_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul183_enob + (10000)*main_mul183_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul183_fixbits + (-10000)*main_mul183_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_mul183_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul183_enob
solver.Add( + (1)*main_mul183_fixp + (1)*main_mul183_float + (1)*main_mul183_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul183_fixbits + (-10000)*main_mul183_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__57_CAST_mul183_fixp + (-1)*a_CAST_mul183_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__57_CAST_mul183_float + (-1)*a_CAST_mul183_float==0)    #float equality
solver.Add( + (1)*ConstantValue__57_CAST_mul183_double + (-1)*a_CAST_mul183_double==0)    #double equality
solver.Add( + (1)*ConstantValue__57_CAST_mul183_fixp + (-1)*main_mul183_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__57_CAST_mul183_float + (-1)*main_mul183_float==0)    #float equality
solver.Add( + (1)*ConstantValue__57_CAST_mul183_double + (-1)*main_mul183_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul183_fixp
mathCostObj +=  + (6)*main_mul183_float
mathCostObj +=  + (12.2551)*main_mul183_double
main_main_mul183_enob_1 = solver.IntVar(0, 1, 'main_main_mul183_enob_1')
main_main_mul183_enob_2 = solver.IntVar(0, 1, 'main_main_mul183_enob_2')
solver.Add( + (1)*main_main_mul183_enob_1 + (1)*main_main_mul183_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul183_enob + (-1)*a_enob_memphi_main_tmp41 + (-10000)*main_main_mul183_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul183_enob + (-1)*ConstantValue__55_enob + (-10000)*main_main_mul183_enob_2<=1024)    #Enob: propagation in product 2



#Stuff for double 1.000000e+00
ConstantValue__58_fixbits = solver.IntVar(0, 31, 'ConstantValue__58_fixbits')
ConstantValue__58_fixp = solver.IntVar(0, 1, 'ConstantValue__58_fixp')
ConstantValue__58_float = solver.IntVar(0, 1, 'ConstantValue__58_float')
ConstantValue__58_double = solver.IntVar(0, 1, 'ConstantValue__58_double')
ConstantValue__58_enob = solver.IntVar(-10000, 10000, 'ConstantValue__58_enob')
solver.Add( + (1)*ConstantValue__58_enob + (-1)*ConstantValue__58_fixbits + (10000)*ConstantValue__58_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__58_enob + (10000)*ConstantValue__58_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__58_enob + (10000)*ConstantValue__58_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__58_fixbits + (-10000)*ConstantValue__58_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__58_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__58_fixp + (1)*ConstantValue__58_float + (1)*ConstantValue__58_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__58_fixbits + (-10000)*ConstantValue__58_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__59_fixbits = solver.IntVar(0, 31, 'ConstantValue__59_fixbits')
ConstantValue__59_fixp = solver.IntVar(0, 1, 'ConstantValue__59_fixp')
ConstantValue__59_float = solver.IntVar(0, 1, 'ConstantValue__59_float')
ConstantValue__59_double = solver.IntVar(0, 1, 'ConstantValue__59_double')
ConstantValue__59_enob = solver.IntVar(-10000, 10000, 'ConstantValue__59_enob')
solver.Add( + (1)*ConstantValue__59_enob + (-1)*ConstantValue__59_fixbits + (10000)*ConstantValue__59_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__59_enob + (10000)*ConstantValue__59_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__59_enob + (10000)*ConstantValue__59_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__59_fixbits + (-10000)*ConstantValue__59_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__59_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__59_fixp + (1)*ConstantValue__59_float + (1)*ConstantValue__59_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__59_fixbits + (-10000)*ConstantValue__59_fixp<=0)    #If not fix, frac part to zero



#Stuff for double 1.000000e+00
ConstantValue__60_fixbits = solver.IntVar(0, 31, 'ConstantValue__60_fixbits')
ConstantValue__60_fixp = solver.IntVar(0, 1, 'ConstantValue__60_fixp')
ConstantValue__60_float = solver.IntVar(0, 1, 'ConstantValue__60_float')
ConstantValue__60_double = solver.IntVar(0, 1, 'ConstantValue__60_double')
ConstantValue__60_enob = solver.IntVar(-10000, 10000, 'ConstantValue__60_enob')
solver.Add( + (1)*ConstantValue__60_enob + (-1)*ConstantValue__60_fixbits + (10000)*ConstantValue__60_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__60_enob + (10000)*ConstantValue__60_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__60_enob + (10000)*ConstantValue__60_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__60_fixbits + (-10000)*ConstantValue__60_fixp>=-9970)    #Limit the lower number of frac bits31
solver.Add( + (1)*ConstantValue__60_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__60_fixp + (1)*ConstantValue__60_float + (1)*ConstantValue__60_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__60_fixbits + (-10000)*ConstantValue__60_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   %add184 = fadd double 1.000000e+00, %mul183, !taffo.info !133, !taffo.initweight !45, !taffo.constinfo !66
ConstantValue__60_CAST_add184_fixbits = solver.IntVar(0, 31, 'ConstantValue__60_CAST_add184_fixbits')
ConstantValue__60_CAST_add184_fixp = solver.IntVar(0, 1, 'ConstantValue__60_CAST_add184_fixp')
ConstantValue__60_CAST_add184_float = solver.IntVar(0, 1, 'ConstantValue__60_CAST_add184_float')
ConstantValue__60_CAST_add184_double = solver.IntVar(0, 1, 'ConstantValue__60_CAST_add184_double')
solver.Add( + (1)*ConstantValue__60_CAST_add184_fixp + (1)*ConstantValue__60_CAST_add184_float + (1)*ConstantValue__60_CAST_add184_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__60_CAST_add184_fixbits + (-10000)*ConstantValue__60_CAST_add184_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C1_ConstantValue__60_CAST_add184')
C2_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C2_ConstantValue__60_CAST_add184')
solver.Add( + (1)*ConstantValue__60_fixbits + (-1)*ConstantValue__60_CAST_add184_fixbits + (-10000)*C1_ConstantValue__60_CAST_add184<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__60_fixbits + (1)*ConstantValue__60_CAST_add184_fixbits + (-10000)*C2_ConstantValue__60_CAST_add184<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__60_CAST_add184
castCostObj +=  + (1)*C2_ConstantValue__60_CAST_add184
C3_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C3_ConstantValue__60_CAST_add184')
C4_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C4_ConstantValue__60_CAST_add184')
C5_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C5_ConstantValue__60_CAST_add184')
C6_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C6_ConstantValue__60_CAST_add184')
C7_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C7_ConstantValue__60_CAST_add184')
C8_ConstantValue__60_CAST_add184 = solver.IntVar(0, 1, 'C8_ConstantValue__60_CAST_add184')
solver.Add( + (1)*ConstantValue__60_fixp + (1)*ConstantValue__60_CAST_add184_float + (-1)*C3_ConstantValue__60_CAST_add184<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__60_CAST_add184
solver.Add( + (1)*ConstantValue__60_float + (1)*ConstantValue__60_CAST_add184_fixp + (-1)*C4_ConstantValue__60_CAST_add184<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__60_CAST_add184
solver.Add( + (1)*ConstantValue__60_fixp + (1)*ConstantValue__60_CAST_add184_double + (-1)*C5_ConstantValue__60_CAST_add184<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__60_CAST_add184
solver.Add( + (1)*ConstantValue__60_double + (1)*ConstantValue__60_CAST_add184_fixp + (-1)*C6_ConstantValue__60_CAST_add184<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__60_CAST_add184
solver.Add( + (1)*ConstantValue__60_float + (1)*ConstantValue__60_CAST_add184_double + (-1)*C7_ConstantValue__60_CAST_add184<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__60_CAST_add184
solver.Add( + (1)*ConstantValue__60_double + (1)*ConstantValue__60_CAST_add184_float + (-1)*C8_ConstantValue__60_CAST_add184<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__60_CAST_add184



#Constraint for cast for   %add184 = fadd double 1.000000e+00, %mul183, !taffo.info !133, !taffo.initweight !45, !taffo.constinfo !66
main_mul183_CAST_add184_fixbits = solver.IntVar(0, 21, 'main_mul183_CAST_add184_fixbits')
main_mul183_CAST_add184_fixp = solver.IntVar(0, 1, 'main_mul183_CAST_add184_fixp')
main_mul183_CAST_add184_float = solver.IntVar(0, 1, 'main_mul183_CAST_add184_float')
main_mul183_CAST_add184_double = solver.IntVar(0, 1, 'main_mul183_CAST_add184_double')
solver.Add( + (1)*main_mul183_CAST_add184_fixp + (1)*main_mul183_CAST_add184_float + (1)*main_mul183_CAST_add184_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul183_CAST_add184_fixbits + (-10000)*main_mul183_CAST_add184_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C1_main_mul183_CAST_add184')
C2_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C2_main_mul183_CAST_add184')
solver.Add( + (1)*main_mul183_fixbits + (-1)*main_mul183_CAST_add184_fixbits + (-10000)*C1_main_mul183_CAST_add184<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul183_fixbits + (1)*main_mul183_CAST_add184_fixbits + (-10000)*C2_main_mul183_CAST_add184<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul183_CAST_add184
castCostObj +=  + (1)*C2_main_mul183_CAST_add184
C3_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C3_main_mul183_CAST_add184')
C4_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C4_main_mul183_CAST_add184')
C5_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C5_main_mul183_CAST_add184')
C6_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C6_main_mul183_CAST_add184')
C7_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C7_main_mul183_CAST_add184')
C8_main_mul183_CAST_add184 = solver.IntVar(0, 1, 'C8_main_mul183_CAST_add184')
solver.Add( + (1)*main_mul183_fixp + (1)*main_mul183_CAST_add184_float + (-1)*C3_main_mul183_CAST_add184<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul183_CAST_add184
solver.Add( + (1)*main_mul183_float + (1)*main_mul183_CAST_add184_fixp + (-1)*C4_main_mul183_CAST_add184<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul183_CAST_add184
solver.Add( + (1)*main_mul183_fixp + (1)*main_mul183_CAST_add184_double + (-1)*C5_main_mul183_CAST_add184<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul183_CAST_add184
solver.Add( + (1)*main_mul183_double + (1)*main_mul183_CAST_add184_fixp + (-1)*C6_main_mul183_CAST_add184<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul183_CAST_add184
solver.Add( + (1)*main_mul183_float + (1)*main_mul183_CAST_add184_double + (-1)*C7_main_mul183_CAST_add184<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul183_CAST_add184
solver.Add( + (1)*main_mul183_double + (1)*main_mul183_CAST_add184_float + (-1)*C8_main_mul183_CAST_add184<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul183_CAST_add184



#Stuff for   %add184 = fadd double 1.000000e+00, %mul183, !taffo.info !133, !taffo.initweight !45, !taffo.constinfo !66
main_add184_fixbits = solver.IntVar(0, 21, 'main_add184_fixbits')
main_add184_fixp = solver.IntVar(0, 1, 'main_add184_fixp')
main_add184_float = solver.IntVar(0, 1, 'main_add184_float')
main_add184_double = solver.IntVar(0, 1, 'main_add184_double')
main_add184_enob = solver.IntVar(-10000, 10000, 'main_add184_enob')
solver.Add( + (1)*main_add184_enob + (-1)*main_add184_fixbits + (10000)*main_add184_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add184_enob + (10000)*main_add184_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add184_enob + (10000)*main_add184_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add184_fixbits + (-10000)*main_add184_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_add184_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add184_enob
solver.Add( + (1)*main_add184_fixp + (1)*main_add184_float + (1)*main_add184_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add184_fixbits + (-10000)*main_add184_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*ConstantValue__60_CAST_add184_fixp + (-1)*main_mul183_CAST_add184_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__60_CAST_add184_float + (-1)*main_mul183_CAST_add184_float==0)    #float equality
solver.Add( + (1)*ConstantValue__60_CAST_add184_double + (-1)*main_mul183_CAST_add184_double==0)    #double equality
solver.Add( + (1)*ConstantValue__60_CAST_add184_fixbits + (-1)*main_mul183_CAST_add184_fixbits==0)    #same fractional bit
solver.Add( + (1)*ConstantValue__60_CAST_add184_fixp + (-1)*main_add184_fixp==0)    #fix equality
solver.Add( + (1)*ConstantValue__60_CAST_add184_float + (-1)*main_add184_float==0)    #float equality
solver.Add( + (1)*ConstantValue__60_CAST_add184_double + (-1)*main_add184_double==0)    #double equality
solver.Add( + (1)*ConstantValue__60_CAST_add184_fixbits + (-1)*main_add184_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add184_fixp
mathCostObj +=  + (3)*main_add184_float
mathCostObj +=  + (6.64928)*main_add184_double
solver.Add( + (1)*main_add184_enob + (-1)*ConstantValue__58_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add184_enob + (-1)*main_mul183_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
main_v_enob_memphi_main_tmp42 = solver.IntVar(-10000, 10000, 'main_v_enob_memphi_main_tmp42')
solver.Add( + (1)*main_v_enob_memphi_main_tmp42 + (-1)*main_v_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp42_enob_0 = solver.IntVar(0, 1, 'main_main_tmp42_enob_0')
main_main_tmp42_enob_1 = solver.IntVar(0, 1, 'main_main_tmp42_enob_1')
main_main_tmp42_enob_2 = solver.IntVar(0, 1, 'main_main_tmp42_enob_2')
main_main_tmp42_enob_4 = solver.IntVar(0, 1, 'main_main_tmp42_enob_4')
solver.Add( + (1)*main_main_tmp42_enob_0 + (1)*main_main_tmp42_enob_1 + (1)*main_main_tmp42_enob_2 + (1)*main_main_tmp42_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp42 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp42_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp42 + (-1)*main_v_enob_storeENOB + (10000)*main_main_tmp42_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul189 = fmul double %add184, %tmp42, !taffo.info !135, !taffo.initweight !51
main_add184_CAST_mul189_fixbits = solver.IntVar(0, 21, 'main_add184_CAST_mul189_fixbits')
main_add184_CAST_mul189_fixp = solver.IntVar(0, 1, 'main_add184_CAST_mul189_fixp')
main_add184_CAST_mul189_float = solver.IntVar(0, 1, 'main_add184_CAST_mul189_float')
main_add184_CAST_mul189_double = solver.IntVar(0, 1, 'main_add184_CAST_mul189_double')
solver.Add( + (1)*main_add184_CAST_mul189_fixp + (1)*main_add184_CAST_mul189_float + (1)*main_add184_CAST_mul189_double==1)    #exactly 1 type
solver.Add( + (1)*main_add184_CAST_mul189_fixbits + (-10000)*main_add184_CAST_mul189_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C1_main_add184_CAST_mul189')
C2_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C2_main_add184_CAST_mul189')
solver.Add( + (1)*main_add184_fixbits + (-1)*main_add184_CAST_mul189_fixbits + (-10000)*C1_main_add184_CAST_mul189<=0)    #Shift cost 1
solver.Add( + (-1)*main_add184_fixbits + (1)*main_add184_CAST_mul189_fixbits + (-10000)*C2_main_add184_CAST_mul189<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add184_CAST_mul189
castCostObj +=  + (1)*C2_main_add184_CAST_mul189
C3_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C3_main_add184_CAST_mul189')
C4_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C4_main_add184_CAST_mul189')
C5_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C5_main_add184_CAST_mul189')
C6_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C6_main_add184_CAST_mul189')
C7_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C7_main_add184_CAST_mul189')
C8_main_add184_CAST_mul189 = solver.IntVar(0, 1, 'C8_main_add184_CAST_mul189')
solver.Add( + (1)*main_add184_fixp + (1)*main_add184_CAST_mul189_float + (-1)*C3_main_add184_CAST_mul189<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add184_CAST_mul189
solver.Add( + (1)*main_add184_float + (1)*main_add184_CAST_mul189_fixp + (-1)*C4_main_add184_CAST_mul189<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add184_CAST_mul189
solver.Add( + (1)*main_add184_fixp + (1)*main_add184_CAST_mul189_double + (-1)*C5_main_add184_CAST_mul189<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add184_CAST_mul189
solver.Add( + (1)*main_add184_double + (1)*main_add184_CAST_mul189_fixp + (-1)*C6_main_add184_CAST_mul189<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add184_CAST_mul189
solver.Add( + (1)*main_add184_float + (1)*main_add184_CAST_mul189_double + (-1)*C7_main_add184_CAST_mul189<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add184_CAST_mul189
solver.Add( + (1)*main_add184_double + (1)*main_add184_CAST_mul189_float + (-1)*C8_main_add184_CAST_mul189<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add184_CAST_mul189



#Constraint for cast for   %mul189 = fmul double %add184, %tmp42, !taffo.info !135, !taffo.initweight !51
main_v_CAST_mul189_fixbits = solver.IntVar(0, 29, 'main_v_CAST_mul189_fixbits')
main_v_CAST_mul189_fixp = solver.IntVar(0, 1, 'main_v_CAST_mul189_fixp')
main_v_CAST_mul189_float = solver.IntVar(0, 1, 'main_v_CAST_mul189_float')
main_v_CAST_mul189_double = solver.IntVar(0, 1, 'main_v_CAST_mul189_double')
solver.Add( + (1)*main_v_CAST_mul189_fixp + (1)*main_v_CAST_mul189_float + (1)*main_v_CAST_mul189_double==1)    #exactly 1 type
solver.Add( + (1)*main_v_CAST_mul189_fixbits + (-10000)*main_v_CAST_mul189_fixp<=0)    #If no fix, fix frac part = 0
C1_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C1_main_v_CAST_mul189')
C2_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C2_main_v_CAST_mul189')
solver.Add( + (1)*main_v_fixbits + (-1)*main_v_CAST_mul189_fixbits + (-10000)*C1_main_v_CAST_mul189<=0)    #Shift cost 1
solver.Add( + (-1)*main_v_fixbits + (1)*main_v_CAST_mul189_fixbits + (-10000)*C2_main_v_CAST_mul189<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_v_CAST_mul189
castCostObj +=  + (1)*C2_main_v_CAST_mul189
C3_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C3_main_v_CAST_mul189')
C4_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C4_main_v_CAST_mul189')
C5_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C5_main_v_CAST_mul189')
C6_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C6_main_v_CAST_mul189')
C7_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C7_main_v_CAST_mul189')
C8_main_v_CAST_mul189 = solver.IntVar(0, 1, 'C8_main_v_CAST_mul189')
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul189_float + (-1)*C3_main_v_CAST_mul189<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_v_CAST_mul189
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul189_fixp + (-1)*C4_main_v_CAST_mul189<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_v_CAST_mul189
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul189_double + (-1)*C5_main_v_CAST_mul189<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_v_CAST_mul189
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul189_fixp + (-1)*C6_main_v_CAST_mul189<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_v_CAST_mul189
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul189_double + (-1)*C7_main_v_CAST_mul189<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_v_CAST_mul189
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul189_float + (-1)*C8_main_v_CAST_mul189<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_v_CAST_mul189



#Stuff for   %mul189 = fmul double %add184, %tmp42, !taffo.info !135, !taffo.initweight !51
main_mul189_fixbits = solver.IntVar(0, 20, 'main_mul189_fixbits')
main_mul189_fixp = solver.IntVar(0, 1, 'main_mul189_fixp')
main_mul189_float = solver.IntVar(0, 1, 'main_mul189_float')
main_mul189_double = solver.IntVar(0, 1, 'main_mul189_double')
main_mul189_enob = solver.IntVar(-10000, 10000, 'main_mul189_enob')
solver.Add( + (1)*main_mul189_enob + (-1)*main_mul189_fixbits + (10000)*main_mul189_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul189_enob + (10000)*main_mul189_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul189_enob + (10000)*main_mul189_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul189_fixbits + (-10000)*main_mul189_fixp>=-9981)    #Limit the lower number of frac bits20
solver.Add( + (1)*main_mul189_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul189_enob
solver.Add( + (1)*main_mul189_fixp + (1)*main_mul189_float + (1)*main_mul189_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul189_fixbits + (-10000)*main_mul189_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add184_CAST_mul189_fixp + (-1)*main_v_CAST_mul189_fixp==0)    #fix equality
solver.Add( + (1)*main_add184_CAST_mul189_float + (-1)*main_v_CAST_mul189_float==0)    #float equality
solver.Add( + (1)*main_add184_CAST_mul189_double + (-1)*main_v_CAST_mul189_double==0)    #double equality
solver.Add( + (1)*main_add184_CAST_mul189_fixp + (-1)*main_mul189_fixp==0)    #fix equality
solver.Add( + (1)*main_add184_CAST_mul189_float + (-1)*main_mul189_float==0)    #float equality
solver.Add( + (1)*main_add184_CAST_mul189_double + (-1)*main_mul189_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul189_fixp
mathCostObj +=  + (6)*main_mul189_float
mathCostObj +=  + (12.2551)*main_mul189_double
main_main_mul189_enob_1 = solver.IntVar(0, 1, 'main_main_mul189_enob_1')
main_main_mul189_enob_2 = solver.IntVar(0, 1, 'main_main_mul189_enob_2')
solver.Add( + (1)*main_main_mul189_enob_1 + (1)*main_main_mul189_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul189_enob + (-1)*main_v_enob_memphi_main_tmp42 + (-10000)*main_main_mul189_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul189_enob + (-1)*main_add184_enob + (-10000)*main_main_mul189_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %add190 = fadd double %mul182, %mul189, !taffo.info !137, !taffo.initweight !51
main_mul182_CAST_add190_fixbits = solver.IntVar(0, 21, 'main_mul182_CAST_add190_fixbits')
main_mul182_CAST_add190_fixp = solver.IntVar(0, 1, 'main_mul182_CAST_add190_fixp')
main_mul182_CAST_add190_float = solver.IntVar(0, 1, 'main_mul182_CAST_add190_float')
main_mul182_CAST_add190_double = solver.IntVar(0, 1, 'main_mul182_CAST_add190_double')
solver.Add( + (1)*main_mul182_CAST_add190_fixp + (1)*main_mul182_CAST_add190_float + (1)*main_mul182_CAST_add190_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul182_CAST_add190_fixbits + (-10000)*main_mul182_CAST_add190_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C1_main_mul182_CAST_add190')
C2_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C2_main_mul182_CAST_add190')
solver.Add( + (1)*main_mul182_fixbits + (-1)*main_mul182_CAST_add190_fixbits + (-10000)*C1_main_mul182_CAST_add190<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul182_fixbits + (1)*main_mul182_CAST_add190_fixbits + (-10000)*C2_main_mul182_CAST_add190<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul182_CAST_add190
castCostObj +=  + (1)*C2_main_mul182_CAST_add190
C3_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C3_main_mul182_CAST_add190')
C4_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C4_main_mul182_CAST_add190')
C5_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C5_main_mul182_CAST_add190')
C6_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C6_main_mul182_CAST_add190')
C7_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C7_main_mul182_CAST_add190')
C8_main_mul182_CAST_add190 = solver.IntVar(0, 1, 'C8_main_mul182_CAST_add190')
solver.Add( + (1)*main_mul182_fixp + (1)*main_mul182_CAST_add190_float + (-1)*C3_main_mul182_CAST_add190<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul182_CAST_add190
solver.Add( + (1)*main_mul182_float + (1)*main_mul182_CAST_add190_fixp + (-1)*C4_main_mul182_CAST_add190<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul182_CAST_add190
solver.Add( + (1)*main_mul182_fixp + (1)*main_mul182_CAST_add190_double + (-1)*C5_main_mul182_CAST_add190<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul182_CAST_add190
solver.Add( + (1)*main_mul182_double + (1)*main_mul182_CAST_add190_fixp + (-1)*C6_main_mul182_CAST_add190<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul182_CAST_add190
solver.Add( + (1)*main_mul182_float + (1)*main_mul182_CAST_add190_double + (-1)*C7_main_mul182_CAST_add190<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul182_CAST_add190
solver.Add( + (1)*main_mul182_double + (1)*main_mul182_CAST_add190_float + (-1)*C8_main_mul182_CAST_add190<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul182_CAST_add190



#Constraint for cast for   %add190 = fadd double %mul182, %mul189, !taffo.info !137, !taffo.initweight !51
main_mul189_CAST_add190_fixbits = solver.IntVar(0, 20, 'main_mul189_CAST_add190_fixbits')
main_mul189_CAST_add190_fixp = solver.IntVar(0, 1, 'main_mul189_CAST_add190_fixp')
main_mul189_CAST_add190_float = solver.IntVar(0, 1, 'main_mul189_CAST_add190_float')
main_mul189_CAST_add190_double = solver.IntVar(0, 1, 'main_mul189_CAST_add190_double')
solver.Add( + (1)*main_mul189_CAST_add190_fixp + (1)*main_mul189_CAST_add190_float + (1)*main_mul189_CAST_add190_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul189_CAST_add190_fixbits + (-10000)*main_mul189_CAST_add190_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C1_main_mul189_CAST_add190')
C2_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C2_main_mul189_CAST_add190')
solver.Add( + (1)*main_mul189_fixbits + (-1)*main_mul189_CAST_add190_fixbits + (-10000)*C1_main_mul189_CAST_add190<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul189_fixbits + (1)*main_mul189_CAST_add190_fixbits + (-10000)*C2_main_mul189_CAST_add190<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul189_CAST_add190
castCostObj +=  + (1)*C2_main_mul189_CAST_add190
C3_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C3_main_mul189_CAST_add190')
C4_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C4_main_mul189_CAST_add190')
C5_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C5_main_mul189_CAST_add190')
C6_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C6_main_mul189_CAST_add190')
C7_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C7_main_mul189_CAST_add190')
C8_main_mul189_CAST_add190 = solver.IntVar(0, 1, 'C8_main_mul189_CAST_add190')
solver.Add( + (1)*main_mul189_fixp + (1)*main_mul189_CAST_add190_float + (-1)*C3_main_mul189_CAST_add190<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul189_CAST_add190
solver.Add( + (1)*main_mul189_float + (1)*main_mul189_CAST_add190_fixp + (-1)*C4_main_mul189_CAST_add190<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul189_CAST_add190
solver.Add( + (1)*main_mul189_fixp + (1)*main_mul189_CAST_add190_double + (-1)*C5_main_mul189_CAST_add190<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul189_CAST_add190
solver.Add( + (1)*main_mul189_double + (1)*main_mul189_CAST_add190_fixp + (-1)*C6_main_mul189_CAST_add190<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul189_CAST_add190
solver.Add( + (1)*main_mul189_float + (1)*main_mul189_CAST_add190_double + (-1)*C7_main_mul189_CAST_add190<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul189_CAST_add190
solver.Add( + (1)*main_mul189_double + (1)*main_mul189_CAST_add190_float + (-1)*C8_main_mul189_CAST_add190<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul189_CAST_add190



#Stuff for   %add190 = fadd double %mul182, %mul189, !taffo.info !137, !taffo.initweight !51
main_add190_fixbits = solver.IntVar(0, 19, 'main_add190_fixbits')
main_add190_fixp = solver.IntVar(0, 1, 'main_add190_fixp')
main_add190_float = solver.IntVar(0, 1, 'main_add190_float')
main_add190_double = solver.IntVar(0, 1, 'main_add190_double')
main_add190_enob = solver.IntVar(-10000, 10000, 'main_add190_enob')
solver.Add( + (1)*main_add190_enob + (-1)*main_add190_fixbits + (10000)*main_add190_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add190_enob + (10000)*main_add190_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add190_enob + (10000)*main_add190_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add190_fixbits + (-10000)*main_add190_fixp>=-9982)    #Limit the lower number of frac bits19
solver.Add( + (1)*main_add190_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add190_enob
solver.Add( + (1)*main_add190_fixp + (1)*main_add190_float + (1)*main_add190_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add190_fixbits + (-10000)*main_add190_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul182_CAST_add190_fixp + (-1)*main_mul189_CAST_add190_fixp==0)    #fix equality
solver.Add( + (1)*main_mul182_CAST_add190_float + (-1)*main_mul189_CAST_add190_float==0)    #float equality
solver.Add( + (1)*main_mul182_CAST_add190_double + (-1)*main_mul189_CAST_add190_double==0)    #double equality
solver.Add( + (1)*main_mul182_CAST_add190_fixbits + (-1)*main_mul189_CAST_add190_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul182_CAST_add190_fixp + (-1)*main_add190_fixp==0)    #fix equality
solver.Add( + (1)*main_mul182_CAST_add190_float + (-1)*main_add190_float==0)    #float equality
solver.Add( + (1)*main_mul182_CAST_add190_double + (-1)*main_add190_double==0)    #double equality
solver.Add( + (1)*main_mul182_CAST_add190_fixbits + (-1)*main_add190_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add190_fixp
mathCostObj +=  + (3)*main_add190_float
mathCostObj +=  + (6.64928)*main_add190_double
solver.Add( + (1)*main_add190_enob + (-1)*main_mul182_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add190_enob + (-1)*main_mul189_enob<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
c_enob_memphi_main_tmp43 = solver.IntVar(-10000, 10000, 'c_enob_memphi_main_tmp43')
solver.Add( + (1)*c_enob_memphi_main_tmp43 + (-1)*c_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp43_enob_0 = solver.IntVar(0, 1, 'main_main_tmp43_enob_0')
solver.Add( + (1)*main_main_tmp43_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*c_enob_memphi_main_tmp43 + (-1)*c_enob_storeENOB + (10000)*main_main_tmp43_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_v_enob_memphi_main_tmp44 = solver.IntVar(-10000, 10000, 'main_v_enob_memphi_main_tmp44')
solver.Add( + (1)*main_v_enob_memphi_main_tmp44 + (-1)*main_v_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp44_enob_0 = solver.IntVar(0, 1, 'main_main_tmp44_enob_0')
main_main_tmp44_enob_1 = solver.IntVar(0, 1, 'main_main_tmp44_enob_1')
main_main_tmp44_enob_2 = solver.IntVar(0, 1, 'main_main_tmp44_enob_2')
main_main_tmp44_enob_4 = solver.IntVar(0, 1, 'main_main_tmp44_enob_4')
solver.Add( + (1)*main_main_tmp44_enob_0 + (1)*main_main_tmp44_enob_1 + (1)*main_main_tmp44_enob_2 + (1)*main_main_tmp44_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp44 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp44_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp44 + (-1)*main_v_enob_storeENOB + (10000)*main_main_tmp44_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul196 = fmul double %tmp43, %tmp44, !taffo.info !100, !taffo.initweight !44
c_CAST_mul196_fixbits = solver.IntVar(0, 22, 'c_CAST_mul196_fixbits')
c_CAST_mul196_fixp = solver.IntVar(0, 1, 'c_CAST_mul196_fixp')
c_CAST_mul196_float = solver.IntVar(0, 1, 'c_CAST_mul196_float')
c_CAST_mul196_double = solver.IntVar(0, 1, 'c_CAST_mul196_double')
solver.Add( + (1)*c_CAST_mul196_fixp + (1)*c_CAST_mul196_float + (1)*c_CAST_mul196_double==1)    #exactly 1 type
solver.Add( + (1)*c_CAST_mul196_fixbits + (-10000)*c_CAST_mul196_fixp<=0)    #If no fix, fix frac part = 0
C1_c_CAST_mul196 = solver.IntVar(0, 1, 'C1_c_CAST_mul196')
C2_c_CAST_mul196 = solver.IntVar(0, 1, 'C2_c_CAST_mul196')
solver.Add( + (1)*c_fixbits + (-1)*c_CAST_mul196_fixbits + (-10000)*C1_c_CAST_mul196<=0)    #Shift cost 1
solver.Add( + (-1)*c_fixbits + (1)*c_CAST_mul196_fixbits + (-10000)*C2_c_CAST_mul196<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_c_CAST_mul196
castCostObj +=  + (1)*C2_c_CAST_mul196
C3_c_CAST_mul196 = solver.IntVar(0, 1, 'C3_c_CAST_mul196')
C4_c_CAST_mul196 = solver.IntVar(0, 1, 'C4_c_CAST_mul196')
C5_c_CAST_mul196 = solver.IntVar(0, 1, 'C5_c_CAST_mul196')
C6_c_CAST_mul196 = solver.IntVar(0, 1, 'C6_c_CAST_mul196')
C7_c_CAST_mul196 = solver.IntVar(0, 1, 'C7_c_CAST_mul196')
C8_c_CAST_mul196 = solver.IntVar(0, 1, 'C8_c_CAST_mul196')
solver.Add( + (1)*c_fixp + (1)*c_CAST_mul196_float + (-1)*C3_c_CAST_mul196<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_c_CAST_mul196
solver.Add( + (1)*c_float + (1)*c_CAST_mul196_fixp + (-1)*C4_c_CAST_mul196<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_c_CAST_mul196
solver.Add( + (1)*c_fixp + (1)*c_CAST_mul196_double + (-1)*C5_c_CAST_mul196<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_c_CAST_mul196
solver.Add( + (1)*c_double + (1)*c_CAST_mul196_fixp + (-1)*C6_c_CAST_mul196<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_c_CAST_mul196
solver.Add( + (1)*c_float + (1)*c_CAST_mul196_double + (-1)*C7_c_CAST_mul196<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_c_CAST_mul196
solver.Add( + (1)*c_double + (1)*c_CAST_mul196_float + (-1)*C8_c_CAST_mul196<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_c_CAST_mul196



#Constraint for cast for   %mul196 = fmul double %tmp43, %tmp44, !taffo.info !100, !taffo.initweight !44
main_v_CAST_mul196_fixbits = solver.IntVar(0, 29, 'main_v_CAST_mul196_fixbits')
main_v_CAST_mul196_fixp = solver.IntVar(0, 1, 'main_v_CAST_mul196_fixp')
main_v_CAST_mul196_float = solver.IntVar(0, 1, 'main_v_CAST_mul196_float')
main_v_CAST_mul196_double = solver.IntVar(0, 1, 'main_v_CAST_mul196_double')
solver.Add( + (1)*main_v_CAST_mul196_fixp + (1)*main_v_CAST_mul196_float + (1)*main_v_CAST_mul196_double==1)    #exactly 1 type
solver.Add( + (1)*main_v_CAST_mul196_fixbits + (-10000)*main_v_CAST_mul196_fixp<=0)    #If no fix, fix frac part = 0
C1_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C1_main_v_CAST_mul196')
C2_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C2_main_v_CAST_mul196')
solver.Add( + (1)*main_v_fixbits + (-1)*main_v_CAST_mul196_fixbits + (-10000)*C1_main_v_CAST_mul196<=0)    #Shift cost 1
solver.Add( + (-1)*main_v_fixbits + (1)*main_v_CAST_mul196_fixbits + (-10000)*C2_main_v_CAST_mul196<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_v_CAST_mul196
castCostObj +=  + (1)*C2_main_v_CAST_mul196
C3_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C3_main_v_CAST_mul196')
C4_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C4_main_v_CAST_mul196')
C5_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C5_main_v_CAST_mul196')
C6_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C6_main_v_CAST_mul196')
C7_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C7_main_v_CAST_mul196')
C8_main_v_CAST_mul196 = solver.IntVar(0, 1, 'C8_main_v_CAST_mul196')
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul196_float + (-1)*C3_main_v_CAST_mul196<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_v_CAST_mul196
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul196_fixp + (-1)*C4_main_v_CAST_mul196<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_v_CAST_mul196
solver.Add( + (1)*main_v_fixp + (1)*main_v_CAST_mul196_double + (-1)*C5_main_v_CAST_mul196<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_v_CAST_mul196
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul196_fixp + (-1)*C6_main_v_CAST_mul196<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_v_CAST_mul196
solver.Add( + (1)*main_v_float + (1)*main_v_CAST_mul196_double + (-1)*C7_main_v_CAST_mul196<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_v_CAST_mul196
solver.Add( + (1)*main_v_double + (1)*main_v_CAST_mul196_float + (-1)*C8_main_v_CAST_mul196<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_v_CAST_mul196



#Stuff for   %mul196 = fmul double %tmp43, %tmp44, !taffo.info !100, !taffo.initweight !44
main_mul196_fixbits = solver.IntVar(0, 21, 'main_mul196_fixbits')
main_mul196_fixp = solver.IntVar(0, 1, 'main_mul196_fixp')
main_mul196_float = solver.IntVar(0, 1, 'main_mul196_float')
main_mul196_double = solver.IntVar(0, 1, 'main_mul196_double')
main_mul196_enob = solver.IntVar(-10000, 10000, 'main_mul196_enob')
solver.Add( + (1)*main_mul196_enob + (-1)*main_mul196_fixbits + (10000)*main_mul196_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul196_enob + (10000)*main_mul196_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul196_enob + (10000)*main_mul196_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul196_fixbits + (-10000)*main_mul196_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_mul196_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul196_enob
solver.Add( + (1)*main_mul196_fixp + (1)*main_mul196_float + (1)*main_mul196_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul196_fixbits + (-10000)*main_mul196_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*c_CAST_mul196_fixp + (-1)*main_v_CAST_mul196_fixp==0)    #fix equality
solver.Add( + (1)*c_CAST_mul196_float + (-1)*main_v_CAST_mul196_float==0)    #float equality
solver.Add( + (1)*c_CAST_mul196_double + (-1)*main_v_CAST_mul196_double==0)    #double equality
solver.Add( + (1)*c_CAST_mul196_fixp + (-1)*main_mul196_fixp==0)    #fix equality
solver.Add( + (1)*c_CAST_mul196_float + (-1)*main_mul196_float==0)    #float equality
solver.Add( + (1)*c_CAST_mul196_double + (-1)*main_mul196_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul196_fixp
mathCostObj +=  + (6)*main_mul196_float
mathCostObj +=  + (12.2551)*main_mul196_double
main_main_mul196_enob_1 = solver.IntVar(0, 1, 'main_main_mul196_enob_1')
main_main_mul196_enob_2 = solver.IntVar(0, 1, 'main_main_mul196_enob_2')
solver.Add( + (1)*main_main_mul196_enob_1 + (1)*main_main_mul196_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul196_enob + (-1)*main_v_enob_memphi_main_tmp44 + (-10000)*main_main_mul196_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul196_enob + (-1)*c_enob_memphi_main_tmp43 + (-10000)*main_main_mul196_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub197 = fsub double %add190, %mul196, !taffo.info !139, !taffo.initweight !45
main_add190_CAST_sub197_fixbits = solver.IntVar(0, 19, 'main_add190_CAST_sub197_fixbits')
main_add190_CAST_sub197_fixp = solver.IntVar(0, 1, 'main_add190_CAST_sub197_fixp')
main_add190_CAST_sub197_float = solver.IntVar(0, 1, 'main_add190_CAST_sub197_float')
main_add190_CAST_sub197_double = solver.IntVar(0, 1, 'main_add190_CAST_sub197_double')
solver.Add( + (1)*main_add190_CAST_sub197_fixp + (1)*main_add190_CAST_sub197_float + (1)*main_add190_CAST_sub197_double==1)    #exactly 1 type
solver.Add( + (1)*main_add190_CAST_sub197_fixbits + (-10000)*main_add190_CAST_sub197_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C1_main_add190_CAST_sub197')
C2_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C2_main_add190_CAST_sub197')
solver.Add( + (1)*main_add190_fixbits + (-1)*main_add190_CAST_sub197_fixbits + (-10000)*C1_main_add190_CAST_sub197<=0)    #Shift cost 1
solver.Add( + (-1)*main_add190_fixbits + (1)*main_add190_CAST_sub197_fixbits + (-10000)*C2_main_add190_CAST_sub197<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add190_CAST_sub197
castCostObj +=  + (1)*C2_main_add190_CAST_sub197
C3_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C3_main_add190_CAST_sub197')
C4_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C4_main_add190_CAST_sub197')
C5_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C5_main_add190_CAST_sub197')
C6_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C6_main_add190_CAST_sub197')
C7_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C7_main_add190_CAST_sub197')
C8_main_add190_CAST_sub197 = solver.IntVar(0, 1, 'C8_main_add190_CAST_sub197')
solver.Add( + (1)*main_add190_fixp + (1)*main_add190_CAST_sub197_float + (-1)*C3_main_add190_CAST_sub197<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add190_CAST_sub197
solver.Add( + (1)*main_add190_float + (1)*main_add190_CAST_sub197_fixp + (-1)*C4_main_add190_CAST_sub197<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add190_CAST_sub197
solver.Add( + (1)*main_add190_fixp + (1)*main_add190_CAST_sub197_double + (-1)*C5_main_add190_CAST_sub197<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add190_CAST_sub197
solver.Add( + (1)*main_add190_double + (1)*main_add190_CAST_sub197_fixp + (-1)*C6_main_add190_CAST_sub197<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add190_CAST_sub197
solver.Add( + (1)*main_add190_float + (1)*main_add190_CAST_sub197_double + (-1)*C7_main_add190_CAST_sub197<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add190_CAST_sub197
solver.Add( + (1)*main_add190_double + (1)*main_add190_CAST_sub197_float + (-1)*C8_main_add190_CAST_sub197<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add190_CAST_sub197



#Constraint for cast for   %sub197 = fsub double %add190, %mul196, !taffo.info !139, !taffo.initweight !45
main_mul196_CAST_sub197_fixbits = solver.IntVar(0, 21, 'main_mul196_CAST_sub197_fixbits')
main_mul196_CAST_sub197_fixp = solver.IntVar(0, 1, 'main_mul196_CAST_sub197_fixp')
main_mul196_CAST_sub197_float = solver.IntVar(0, 1, 'main_mul196_CAST_sub197_float')
main_mul196_CAST_sub197_double = solver.IntVar(0, 1, 'main_mul196_CAST_sub197_double')
solver.Add( + (1)*main_mul196_CAST_sub197_fixp + (1)*main_mul196_CAST_sub197_float + (1)*main_mul196_CAST_sub197_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul196_CAST_sub197_fixbits + (-10000)*main_mul196_CAST_sub197_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C1_main_mul196_CAST_sub197')
C2_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C2_main_mul196_CAST_sub197')
solver.Add( + (1)*main_mul196_fixbits + (-1)*main_mul196_CAST_sub197_fixbits + (-10000)*C1_main_mul196_CAST_sub197<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul196_fixbits + (1)*main_mul196_CAST_sub197_fixbits + (-10000)*C2_main_mul196_CAST_sub197<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul196_CAST_sub197
castCostObj +=  + (1)*C2_main_mul196_CAST_sub197
C3_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C3_main_mul196_CAST_sub197')
C4_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C4_main_mul196_CAST_sub197')
C5_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C5_main_mul196_CAST_sub197')
C6_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C6_main_mul196_CAST_sub197')
C7_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C7_main_mul196_CAST_sub197')
C8_main_mul196_CAST_sub197 = solver.IntVar(0, 1, 'C8_main_mul196_CAST_sub197')
solver.Add( + (1)*main_mul196_fixp + (1)*main_mul196_CAST_sub197_float + (-1)*C3_main_mul196_CAST_sub197<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul196_CAST_sub197
solver.Add( + (1)*main_mul196_float + (1)*main_mul196_CAST_sub197_fixp + (-1)*C4_main_mul196_CAST_sub197<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul196_CAST_sub197
solver.Add( + (1)*main_mul196_fixp + (1)*main_mul196_CAST_sub197_double + (-1)*C5_main_mul196_CAST_sub197<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul196_CAST_sub197
solver.Add( + (1)*main_mul196_double + (1)*main_mul196_CAST_sub197_fixp + (-1)*C6_main_mul196_CAST_sub197<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul196_CAST_sub197
solver.Add( + (1)*main_mul196_float + (1)*main_mul196_CAST_sub197_double + (-1)*C7_main_mul196_CAST_sub197<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul196_CAST_sub197
solver.Add( + (1)*main_mul196_double + (1)*main_mul196_CAST_sub197_float + (-1)*C8_main_mul196_CAST_sub197<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul196_CAST_sub197



#Stuff for   %sub197 = fsub double %add190, %mul196, !taffo.info !139, !taffo.initweight !45
main_sub197_fixbits = solver.IntVar(0, 19, 'main_sub197_fixbits')
main_sub197_fixp = solver.IntVar(0, 1, 'main_sub197_fixp')
main_sub197_float = solver.IntVar(0, 1, 'main_sub197_float')
main_sub197_double = solver.IntVar(0, 1, 'main_sub197_double')
main_sub197_enob = solver.IntVar(-10000, 10000, 'main_sub197_enob')
solver.Add( + (1)*main_sub197_enob + (-1)*main_sub197_fixbits + (10000)*main_sub197_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub197_enob + (10000)*main_sub197_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub197_enob + (10000)*main_sub197_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub197_fixbits + (-10000)*main_sub197_fixp>=-9982)    #Limit the lower number of frac bits19
solver.Add( + (1)*main_sub197_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub197_enob
solver.Add( + (1)*main_sub197_fixp + (1)*main_sub197_float + (1)*main_sub197_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub197_fixbits + (-10000)*main_sub197_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_add190_CAST_sub197_fixp + (-1)*main_mul196_CAST_sub197_fixp==0)    #fix equality
solver.Add( + (1)*main_add190_CAST_sub197_float + (-1)*main_mul196_CAST_sub197_float==0)    #float equality
solver.Add( + (1)*main_add190_CAST_sub197_double + (-1)*main_mul196_CAST_sub197_double==0)    #double equality
solver.Add( + (1)*main_add190_CAST_sub197_fixbits + (-1)*main_mul196_CAST_sub197_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add190_CAST_sub197_fixp + (-1)*main_sub197_fixp==0)    #fix equality
solver.Add( + (1)*main_add190_CAST_sub197_float + (-1)*main_sub197_float==0)    #float equality
solver.Add( + (1)*main_add190_CAST_sub197_double + (-1)*main_sub197_double==0)    #double equality
solver.Add( + (1)*main_add190_CAST_sub197_fixbits + (-1)*main_sub197_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub197_fixp
mathCostObj +=  + (3)*main_sub197_float
mathCostObj +=  + (6.64928)*main_sub197_double
solver.Add( + (1)*main_sub197_enob + (-1)*main_add190_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub197_enob + (-1)*main_mul196_enob<=0)    #Enob propagation in sub second addend

#Restriction for new enob [LOAD]
d_enob_memphi_main_tmp45 = solver.IntVar(-10000, 10000, 'd_enob_memphi_main_tmp45')
solver.Add( + (1)*d_enob_memphi_main_tmp45 + (-1)*d_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp45_enob_0 = solver.IntVar(0, 1, 'main_main_tmp45_enob_0')
solver.Add( + (1)*main_main_tmp45_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*d_enob_memphi_main_tmp45 + (-1)*d_enob_storeENOB + (10000)*main_main_tmp45_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_q_enob_memphi_main_tmp46 = solver.IntVar(-10000, 10000, 'main_q_enob_memphi_main_tmp46')
solver.Add( + (1)*main_q_enob_memphi_main_tmp46 + (-1)*main_q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp46_enob_0 = solver.IntVar(0, 1, 'main_main_tmp46_enob_0')
solver.Add( + (1)*main_main_tmp46_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp46 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp46_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %mul203 = fmul double %tmp45, %tmp46, !taffo.info !141, !taffo.initweight !44
d_CAST_mul203_fixbits = solver.IntVar(0, 23, 'd_CAST_mul203_fixbits')
d_CAST_mul203_fixp = solver.IntVar(0, 1, 'd_CAST_mul203_fixp')
d_CAST_mul203_float = solver.IntVar(0, 1, 'd_CAST_mul203_float')
d_CAST_mul203_double = solver.IntVar(0, 1, 'd_CAST_mul203_double')
solver.Add( + (1)*d_CAST_mul203_fixp + (1)*d_CAST_mul203_float + (1)*d_CAST_mul203_double==1)    #exactly 1 type
solver.Add( + (1)*d_CAST_mul203_fixbits + (-10000)*d_CAST_mul203_fixp<=0)    #If no fix, fix frac part = 0
C1_d_CAST_mul203 = solver.IntVar(0, 1, 'C1_d_CAST_mul203')
C2_d_CAST_mul203 = solver.IntVar(0, 1, 'C2_d_CAST_mul203')
solver.Add( + (1)*d_fixbits + (-1)*d_CAST_mul203_fixbits + (-10000)*C1_d_CAST_mul203<=0)    #Shift cost 1
solver.Add( + (-1)*d_fixbits + (1)*d_CAST_mul203_fixbits + (-10000)*C2_d_CAST_mul203<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_d_CAST_mul203
castCostObj +=  + (1)*C2_d_CAST_mul203
C3_d_CAST_mul203 = solver.IntVar(0, 1, 'C3_d_CAST_mul203')
C4_d_CAST_mul203 = solver.IntVar(0, 1, 'C4_d_CAST_mul203')
C5_d_CAST_mul203 = solver.IntVar(0, 1, 'C5_d_CAST_mul203')
C6_d_CAST_mul203 = solver.IntVar(0, 1, 'C6_d_CAST_mul203')
C7_d_CAST_mul203 = solver.IntVar(0, 1, 'C7_d_CAST_mul203')
C8_d_CAST_mul203 = solver.IntVar(0, 1, 'C8_d_CAST_mul203')
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul203_float + (-1)*C3_d_CAST_mul203<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_d_CAST_mul203
solver.Add( + (1)*d_float + (1)*d_CAST_mul203_fixp + (-1)*C4_d_CAST_mul203<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_d_CAST_mul203
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul203_double + (-1)*C5_d_CAST_mul203<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_d_CAST_mul203
solver.Add( + (1)*d_double + (1)*d_CAST_mul203_fixp + (-1)*C6_d_CAST_mul203<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_d_CAST_mul203
solver.Add( + (1)*d_float + (1)*d_CAST_mul203_double + (-1)*C7_d_CAST_mul203<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_d_CAST_mul203
solver.Add( + (1)*d_double + (1)*d_CAST_mul203_float + (-1)*C8_d_CAST_mul203<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_d_CAST_mul203



#Constraint for cast for   %mul203 = fmul double %tmp45, %tmp46, !taffo.info !141, !taffo.initweight !44
main_q_CAST_mul203_fixbits = solver.IntVar(0, 22, 'main_q_CAST_mul203_fixbits')
main_q_CAST_mul203_fixp = solver.IntVar(0, 1, 'main_q_CAST_mul203_fixp')
main_q_CAST_mul203_float = solver.IntVar(0, 1, 'main_q_CAST_mul203_float')
main_q_CAST_mul203_double = solver.IntVar(0, 1, 'main_q_CAST_mul203_double')
solver.Add( + (1)*main_q_CAST_mul203_fixp + (1)*main_q_CAST_mul203_float + (1)*main_q_CAST_mul203_double==1)    #exactly 1 type
solver.Add( + (1)*main_q_CAST_mul203_fixbits + (-10000)*main_q_CAST_mul203_fixp<=0)    #If no fix, fix frac part = 0
C1_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C1_main_q_CAST_mul203')
C2_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C2_main_q_CAST_mul203')
solver.Add( + (1)*main_q_fixbits + (-1)*main_q_CAST_mul203_fixbits + (-10000)*C1_main_q_CAST_mul203<=0)    #Shift cost 1
solver.Add( + (-1)*main_q_fixbits + (1)*main_q_CAST_mul203_fixbits + (-10000)*C2_main_q_CAST_mul203<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_q_CAST_mul203
castCostObj +=  + (1)*C2_main_q_CAST_mul203
C3_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C3_main_q_CAST_mul203')
C4_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C4_main_q_CAST_mul203')
C5_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C5_main_q_CAST_mul203')
C6_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C6_main_q_CAST_mul203')
C7_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C7_main_q_CAST_mul203')
C8_main_q_CAST_mul203 = solver.IntVar(0, 1, 'C8_main_q_CAST_mul203')
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_mul203_float + (-1)*C3_main_q_CAST_mul203<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_q_CAST_mul203
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_mul203_fixp + (-1)*C4_main_q_CAST_mul203<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_q_CAST_mul203
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_mul203_double + (-1)*C5_main_q_CAST_mul203<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_q_CAST_mul203
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_mul203_fixp + (-1)*C6_main_q_CAST_mul203<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_q_CAST_mul203
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_mul203_double + (-1)*C7_main_q_CAST_mul203<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_q_CAST_mul203
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_mul203_float + (-1)*C8_main_q_CAST_mul203<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_q_CAST_mul203



#Stuff for   %mul203 = fmul double %tmp45, %tmp46, !taffo.info !141, !taffo.initweight !44
main_mul203_fixbits = solver.IntVar(0, 14, 'main_mul203_fixbits')
main_mul203_fixp = solver.IntVar(0, 1, 'main_mul203_fixp')
main_mul203_float = solver.IntVar(0, 1, 'main_mul203_float')
main_mul203_double = solver.IntVar(0, 1, 'main_mul203_double')
main_mul203_enob = solver.IntVar(-10000, 10000, 'main_mul203_enob')
solver.Add( + (1)*main_mul203_enob + (-1)*main_mul203_fixbits + (10000)*main_mul203_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul203_enob + (10000)*main_mul203_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul203_enob + (10000)*main_mul203_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul203_fixbits + (-10000)*main_mul203_fixp>=-9987)    #Limit the lower number of frac bits14
solver.Add( + (1)*main_mul203_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul203_enob
solver.Add( + (1)*main_mul203_fixp + (1)*main_mul203_float + (1)*main_mul203_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul203_fixbits + (-10000)*main_mul203_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*d_CAST_mul203_fixp + (-1)*main_q_CAST_mul203_fixp==0)    #fix equality
solver.Add( + (1)*d_CAST_mul203_float + (-1)*main_q_CAST_mul203_float==0)    #float equality
solver.Add( + (1)*d_CAST_mul203_double + (-1)*main_q_CAST_mul203_double==0)    #double equality
solver.Add( + (1)*d_CAST_mul203_fixp + (-1)*main_mul203_fixp==0)    #fix equality
solver.Add( + (1)*d_CAST_mul203_float + (-1)*main_mul203_float==0)    #float equality
solver.Add( + (1)*d_CAST_mul203_double + (-1)*main_mul203_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul203_fixp
mathCostObj +=  + (6)*main_mul203_float
mathCostObj +=  + (12.2551)*main_mul203_double
main_main_mul203_enob_1 = solver.IntVar(0, 1, 'main_main_mul203_enob_1')
main_main_mul203_enob_2 = solver.IntVar(0, 1, 'main_main_mul203_enob_2')
solver.Add( + (1)*main_main_mul203_enob_1 + (1)*main_main_mul203_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul203_enob + (-1)*main_q_enob_memphi_main_tmp46 + (-10000)*main_main_mul203_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul203_enob + (-1)*d_enob_memphi_main_tmp45 + (-10000)*main_main_mul203_enob_2<=1024)    #Enob: propagation in product 2



#Constraint for cast for   %sub204 = fsub double %sub197, %mul203, !taffo.info !143, !taffo.initweight !45
main_sub197_CAST_sub204_fixbits = solver.IntVar(0, 19, 'main_sub197_CAST_sub204_fixbits')
main_sub197_CAST_sub204_fixp = solver.IntVar(0, 1, 'main_sub197_CAST_sub204_fixp')
main_sub197_CAST_sub204_float = solver.IntVar(0, 1, 'main_sub197_CAST_sub204_float')
main_sub197_CAST_sub204_double = solver.IntVar(0, 1, 'main_sub197_CAST_sub204_double')
solver.Add( + (1)*main_sub197_CAST_sub204_fixp + (1)*main_sub197_CAST_sub204_float + (1)*main_sub197_CAST_sub204_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub197_CAST_sub204_fixbits + (-10000)*main_sub197_CAST_sub204_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C1_main_sub197_CAST_sub204')
C2_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C2_main_sub197_CAST_sub204')
solver.Add( + (1)*main_sub197_fixbits + (-1)*main_sub197_CAST_sub204_fixbits + (-10000)*C1_main_sub197_CAST_sub204<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub197_fixbits + (1)*main_sub197_CAST_sub204_fixbits + (-10000)*C2_main_sub197_CAST_sub204<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub197_CAST_sub204
castCostObj +=  + (1)*C2_main_sub197_CAST_sub204
C3_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C3_main_sub197_CAST_sub204')
C4_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C4_main_sub197_CAST_sub204')
C5_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C5_main_sub197_CAST_sub204')
C6_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C6_main_sub197_CAST_sub204')
C7_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C7_main_sub197_CAST_sub204')
C8_main_sub197_CAST_sub204 = solver.IntVar(0, 1, 'C8_main_sub197_CAST_sub204')
solver.Add( + (1)*main_sub197_fixp + (1)*main_sub197_CAST_sub204_float + (-1)*C3_main_sub197_CAST_sub204<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub197_CAST_sub204
solver.Add( + (1)*main_sub197_float + (1)*main_sub197_CAST_sub204_fixp + (-1)*C4_main_sub197_CAST_sub204<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub197_CAST_sub204
solver.Add( + (1)*main_sub197_fixp + (1)*main_sub197_CAST_sub204_double + (-1)*C5_main_sub197_CAST_sub204<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub197_CAST_sub204
solver.Add( + (1)*main_sub197_double + (1)*main_sub197_CAST_sub204_fixp + (-1)*C6_main_sub197_CAST_sub204<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub197_CAST_sub204
solver.Add( + (1)*main_sub197_float + (1)*main_sub197_CAST_sub204_double + (-1)*C7_main_sub197_CAST_sub204<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub197_CAST_sub204
solver.Add( + (1)*main_sub197_double + (1)*main_sub197_CAST_sub204_float + (-1)*C8_main_sub197_CAST_sub204<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub197_CAST_sub204



#Constraint for cast for   %sub204 = fsub double %sub197, %mul203, !taffo.info !143, !taffo.initweight !45
main_mul203_CAST_sub204_fixbits = solver.IntVar(0, 14, 'main_mul203_CAST_sub204_fixbits')
main_mul203_CAST_sub204_fixp = solver.IntVar(0, 1, 'main_mul203_CAST_sub204_fixp')
main_mul203_CAST_sub204_float = solver.IntVar(0, 1, 'main_mul203_CAST_sub204_float')
main_mul203_CAST_sub204_double = solver.IntVar(0, 1, 'main_mul203_CAST_sub204_double')
solver.Add( + (1)*main_mul203_CAST_sub204_fixp + (1)*main_mul203_CAST_sub204_float + (1)*main_mul203_CAST_sub204_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul203_CAST_sub204_fixbits + (-10000)*main_mul203_CAST_sub204_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C1_main_mul203_CAST_sub204')
C2_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C2_main_mul203_CAST_sub204')
solver.Add( + (1)*main_mul203_fixbits + (-1)*main_mul203_CAST_sub204_fixbits + (-10000)*C1_main_mul203_CAST_sub204<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul203_fixbits + (1)*main_mul203_CAST_sub204_fixbits + (-10000)*C2_main_mul203_CAST_sub204<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul203_CAST_sub204
castCostObj +=  + (1)*C2_main_mul203_CAST_sub204
C3_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C3_main_mul203_CAST_sub204')
C4_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C4_main_mul203_CAST_sub204')
C5_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C5_main_mul203_CAST_sub204')
C6_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C6_main_mul203_CAST_sub204')
C7_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C7_main_mul203_CAST_sub204')
C8_main_mul203_CAST_sub204 = solver.IntVar(0, 1, 'C8_main_mul203_CAST_sub204')
solver.Add( + (1)*main_mul203_fixp + (1)*main_mul203_CAST_sub204_float + (-1)*C3_main_mul203_CAST_sub204<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul203_CAST_sub204
solver.Add( + (1)*main_mul203_float + (1)*main_mul203_CAST_sub204_fixp + (-1)*C4_main_mul203_CAST_sub204<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul203_CAST_sub204
solver.Add( + (1)*main_mul203_fixp + (1)*main_mul203_CAST_sub204_double + (-1)*C5_main_mul203_CAST_sub204<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul203_CAST_sub204
solver.Add( + (1)*main_mul203_double + (1)*main_mul203_CAST_sub204_fixp + (-1)*C6_main_mul203_CAST_sub204<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul203_CAST_sub204
solver.Add( + (1)*main_mul203_float + (1)*main_mul203_CAST_sub204_double + (-1)*C7_main_mul203_CAST_sub204<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul203_CAST_sub204
solver.Add( + (1)*main_mul203_double + (1)*main_mul203_CAST_sub204_float + (-1)*C8_main_mul203_CAST_sub204<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul203_CAST_sub204



#Stuff for   %sub204 = fsub double %sub197, %mul203, !taffo.info !143, !taffo.initweight !45
main_sub204_fixbits = solver.IntVar(0, 14, 'main_sub204_fixbits')
main_sub204_fixp = solver.IntVar(0, 1, 'main_sub204_fixp')
main_sub204_float = solver.IntVar(0, 1, 'main_sub204_float')
main_sub204_double = solver.IntVar(0, 1, 'main_sub204_double')
main_sub204_enob = solver.IntVar(-10000, 10000, 'main_sub204_enob')
solver.Add( + (1)*main_sub204_enob + (-1)*main_sub204_fixbits + (10000)*main_sub204_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_sub204_enob + (10000)*main_sub204_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_sub204_enob + (10000)*main_sub204_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_sub204_fixbits + (-10000)*main_sub204_fixp>=-9987)    #Limit the lower number of frac bits14
solver.Add( + (1)*main_sub204_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_sub204_enob
solver.Add( + (1)*main_sub204_fixp + (1)*main_sub204_float + (1)*main_sub204_double==1)    #Exactly one selected type
solver.Add( + (1)*main_sub204_fixbits + (-10000)*main_sub204_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_sub197_CAST_sub204_fixp + (-1)*main_mul203_CAST_sub204_fixp==0)    #fix equality
solver.Add( + (1)*main_sub197_CAST_sub204_float + (-1)*main_mul203_CAST_sub204_float==0)    #float equality
solver.Add( + (1)*main_sub197_CAST_sub204_double + (-1)*main_mul203_CAST_sub204_double==0)    #double equality
solver.Add( + (1)*main_sub197_CAST_sub204_fixbits + (-1)*main_mul203_CAST_sub204_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_sub197_CAST_sub204_fixp + (-1)*main_sub204_fixp==0)    #fix equality
solver.Add( + (1)*main_sub197_CAST_sub204_float + (-1)*main_sub204_float==0)    #float equality
solver.Add( + (1)*main_sub197_CAST_sub204_double + (-1)*main_sub204_double==0)    #double equality
solver.Add( + (1)*main_sub197_CAST_sub204_fixbits + (-1)*main_sub204_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_sub204_fixp
mathCostObj +=  + (3)*main_sub204_float
mathCostObj +=  + (6.64928)*main_sub204_double
solver.Add( + (1)*main_sub204_enob + (-1)*main_sub197_enob<=0)    #Enob propagation in sub first addend
solver.Add( + (1)*main_sub204_enob + (-1)*main_mul203_enob<=0)    #Enob propagation in sub second addend



#Constraint for cast for   store double %sub204, double* %arrayidx208, align 8, !taffo.info !39, !taffo.initweight !45
main_sub204_CAST_store_fixbits = solver.IntVar(0, 14, 'main_sub204_CAST_store_fixbits')
main_sub204_CAST_store_fixp = solver.IntVar(0, 1, 'main_sub204_CAST_store_fixp')
main_sub204_CAST_store_float = solver.IntVar(0, 1, 'main_sub204_CAST_store_float')
main_sub204_CAST_store_double = solver.IntVar(0, 1, 'main_sub204_CAST_store_double')
solver.Add( + (1)*main_sub204_CAST_store_fixp + (1)*main_sub204_CAST_store_float + (1)*main_sub204_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_sub204_CAST_store_fixbits + (-10000)*main_sub204_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_sub204_CAST_store = solver.IntVar(0, 1, 'C1_main_sub204_CAST_store')
C2_main_sub204_CAST_store = solver.IntVar(0, 1, 'C2_main_sub204_CAST_store')
solver.Add( + (1)*main_sub204_fixbits + (-1)*main_sub204_CAST_store_fixbits + (-10000)*C1_main_sub204_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_sub204_fixbits + (1)*main_sub204_CAST_store_fixbits + (-10000)*C2_main_sub204_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_sub204_CAST_store
castCostObj +=  + (1)*C2_main_sub204_CAST_store
C3_main_sub204_CAST_store = solver.IntVar(0, 1, 'C3_main_sub204_CAST_store')
C4_main_sub204_CAST_store = solver.IntVar(0, 1, 'C4_main_sub204_CAST_store')
C5_main_sub204_CAST_store = solver.IntVar(0, 1, 'C5_main_sub204_CAST_store')
C6_main_sub204_CAST_store = solver.IntVar(0, 1, 'C6_main_sub204_CAST_store')
C7_main_sub204_CAST_store = solver.IntVar(0, 1, 'C7_main_sub204_CAST_store')
C8_main_sub204_CAST_store = solver.IntVar(0, 1, 'C8_main_sub204_CAST_store')
solver.Add( + (1)*main_sub204_fixp + (1)*main_sub204_CAST_store_float + (-1)*C3_main_sub204_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_sub204_CAST_store
solver.Add( + (1)*main_sub204_float + (1)*main_sub204_CAST_store_fixp + (-1)*C4_main_sub204_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_sub204_CAST_store
solver.Add( + (1)*main_sub204_fixp + (1)*main_sub204_CAST_store_double + (-1)*C5_main_sub204_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_sub204_CAST_store
solver.Add( + (1)*main_sub204_double + (1)*main_sub204_CAST_store_fixp + (-1)*C6_main_sub204_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_sub204_CAST_store
solver.Add( + (1)*main_sub204_float + (1)*main_sub204_CAST_store_double + (-1)*C7_main_sub204_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_sub204_CAST_store
solver.Add( + (1)*main_sub204_double + (1)*main_sub204_CAST_store_float + (-1)*C8_main_sub204_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_sub204_CAST_store
solver.Add( + (1)*main_q_fixp + (-1)*main_sub204_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_q_float + (-1)*main_sub204_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_q_double + (-1)*main_sub204_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_q_fixbits + (-1)*main_sub204_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_q_fixbits + (10000)*main_q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_sub204_enob<=0)    #Enob constraint ENOB propagation in load/store

#Restriction for new enob [LOAD]
d_enob_memphi_main_tmp47 = solver.IntVar(-10000, 10000, 'd_enob_memphi_main_tmp47')
solver.Add( + (1)*d_enob_memphi_main_tmp47 + (-1)*d_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp47_enob_0 = solver.IntVar(0, 1, 'main_main_tmp47_enob_0')
solver.Add( + (1)*main_main_tmp47_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*d_enob_memphi_main_tmp47 + (-1)*d_enob_storeENOB + (10000)*main_main_tmp47_enob_0<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_p_enob_memphi_main_tmp48 = solver.IntVar(-10000, 10000, 'main_p_enob_memphi_main_tmp48')
solver.Add( + (1)*main_p_enob_memphi_main_tmp48 + (-1)*main_p_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul214 = fmul double %tmp47, %tmp48, !taffo.info !125, !taffo.initweight !44
d_CAST_mul214_fixbits = solver.IntVar(0, 23, 'd_CAST_mul214_fixbits')
d_CAST_mul214_fixp = solver.IntVar(0, 1, 'd_CAST_mul214_fixp')
d_CAST_mul214_float = solver.IntVar(0, 1, 'd_CAST_mul214_float')
d_CAST_mul214_double = solver.IntVar(0, 1, 'd_CAST_mul214_double')
solver.Add( + (1)*d_CAST_mul214_fixp + (1)*d_CAST_mul214_float + (1)*d_CAST_mul214_double==1)    #exactly 1 type
solver.Add( + (1)*d_CAST_mul214_fixbits + (-10000)*d_CAST_mul214_fixp<=0)    #If no fix, fix frac part = 0
C1_d_CAST_mul214 = solver.IntVar(0, 1, 'C1_d_CAST_mul214')
C2_d_CAST_mul214 = solver.IntVar(0, 1, 'C2_d_CAST_mul214')
solver.Add( + (1)*d_fixbits + (-1)*d_CAST_mul214_fixbits + (-10000)*C1_d_CAST_mul214<=0)    #Shift cost 1
solver.Add( + (-1)*d_fixbits + (1)*d_CAST_mul214_fixbits + (-10000)*C2_d_CAST_mul214<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_d_CAST_mul214
castCostObj +=  + (1)*C2_d_CAST_mul214
C3_d_CAST_mul214 = solver.IntVar(0, 1, 'C3_d_CAST_mul214')
C4_d_CAST_mul214 = solver.IntVar(0, 1, 'C4_d_CAST_mul214')
C5_d_CAST_mul214 = solver.IntVar(0, 1, 'C5_d_CAST_mul214')
C6_d_CAST_mul214 = solver.IntVar(0, 1, 'C6_d_CAST_mul214')
C7_d_CAST_mul214 = solver.IntVar(0, 1, 'C7_d_CAST_mul214')
C8_d_CAST_mul214 = solver.IntVar(0, 1, 'C8_d_CAST_mul214')
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul214_float + (-1)*C3_d_CAST_mul214<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_d_CAST_mul214
solver.Add( + (1)*d_float + (1)*d_CAST_mul214_fixp + (-1)*C4_d_CAST_mul214<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_d_CAST_mul214
solver.Add( + (1)*d_fixp + (1)*d_CAST_mul214_double + (-1)*C5_d_CAST_mul214<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_d_CAST_mul214
solver.Add( + (1)*d_double + (1)*d_CAST_mul214_fixp + (-1)*C6_d_CAST_mul214<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_d_CAST_mul214
solver.Add( + (1)*d_float + (1)*d_CAST_mul214_double + (-1)*C7_d_CAST_mul214<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_d_CAST_mul214
solver.Add( + (1)*d_double + (1)*d_CAST_mul214_float + (-1)*C8_d_CAST_mul214<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_d_CAST_mul214



#Constraint for cast for   %mul214 = fmul double %tmp47, %tmp48, !taffo.info !125, !taffo.initweight !44
main_p_CAST_mul214_fixbits = solver.IntVar(0, 30, 'main_p_CAST_mul214_fixbits')
main_p_CAST_mul214_fixp = solver.IntVar(0, 1, 'main_p_CAST_mul214_fixp')
main_p_CAST_mul214_float = solver.IntVar(0, 1, 'main_p_CAST_mul214_float')
main_p_CAST_mul214_double = solver.IntVar(0, 1, 'main_p_CAST_mul214_double')
solver.Add( + (1)*main_p_CAST_mul214_fixp + (1)*main_p_CAST_mul214_float + (1)*main_p_CAST_mul214_double==1)    #exactly 1 type
solver.Add( + (1)*main_p_CAST_mul214_fixbits + (-10000)*main_p_CAST_mul214_fixp<=0)    #If no fix, fix frac part = 0
C1_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C1_main_p_CAST_mul214')
C2_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C2_main_p_CAST_mul214')
solver.Add( + (1)*main_p_fixbits + (-1)*main_p_CAST_mul214_fixbits + (-10000)*C1_main_p_CAST_mul214<=0)    #Shift cost 1
solver.Add( + (-1)*main_p_fixbits + (1)*main_p_CAST_mul214_fixbits + (-10000)*C2_main_p_CAST_mul214<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_p_CAST_mul214
castCostObj +=  + (1)*C2_main_p_CAST_mul214
C3_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C3_main_p_CAST_mul214')
C4_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C4_main_p_CAST_mul214')
C5_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C5_main_p_CAST_mul214')
C6_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C6_main_p_CAST_mul214')
C7_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C7_main_p_CAST_mul214')
C8_main_p_CAST_mul214 = solver.IntVar(0, 1, 'C8_main_p_CAST_mul214')
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul214_float + (-1)*C3_main_p_CAST_mul214<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_p_CAST_mul214
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul214_fixp + (-1)*C4_main_p_CAST_mul214<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_p_CAST_mul214
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul214_double + (-1)*C5_main_p_CAST_mul214<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_p_CAST_mul214
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul214_fixp + (-1)*C6_main_p_CAST_mul214<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_p_CAST_mul214
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul214_double + (-1)*C7_main_p_CAST_mul214<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_p_CAST_mul214
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul214_float + (-1)*C8_main_p_CAST_mul214<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_p_CAST_mul214



#Stuff for   %mul214 = fmul double %tmp47, %tmp48, !taffo.info !125, !taffo.initweight !44
main_mul214_fixbits = solver.IntVar(0, 23, 'main_mul214_fixbits')
main_mul214_fixp = solver.IntVar(0, 1, 'main_mul214_fixp')
main_mul214_float = solver.IntVar(0, 1, 'main_mul214_float')
main_mul214_double = solver.IntVar(0, 1, 'main_mul214_double')
main_mul214_enob = solver.IntVar(-10000, 10000, 'main_mul214_enob')
solver.Add( + (1)*main_mul214_enob + (-1)*main_mul214_fixbits + (10000)*main_mul214_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul214_enob + (10000)*main_mul214_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul214_enob + (10000)*main_mul214_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul214_fixbits + (-10000)*main_mul214_fixp>=-9978)    #Limit the lower number of frac bits23
solver.Add( + (1)*main_mul214_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul214_enob
solver.Add( + (1)*main_mul214_fixp + (1)*main_mul214_float + (1)*main_mul214_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul214_fixbits + (-10000)*main_mul214_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*d_CAST_mul214_fixp + (-1)*main_p_CAST_mul214_fixp==0)    #fix equality
solver.Add( + (1)*d_CAST_mul214_float + (-1)*main_p_CAST_mul214_float==0)    #float equality
solver.Add( + (1)*d_CAST_mul214_double + (-1)*main_p_CAST_mul214_double==0)    #double equality
solver.Add( + (1)*d_CAST_mul214_fixp + (-1)*main_mul214_fixp==0)    #fix equality
solver.Add( + (1)*d_CAST_mul214_float + (-1)*main_mul214_float==0)    #float equality
solver.Add( + (1)*d_CAST_mul214_double + (-1)*main_mul214_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul214_fixp
mathCostObj +=  + (6)*main_mul214_float
mathCostObj +=  + (12.2551)*main_mul214_double
main_main_mul214_enob_1 = solver.IntVar(0, 1, 'main_main_mul214_enob_1')
main_main_mul214_enob_2 = solver.IntVar(0, 1, 'main_main_mul214_enob_2')
solver.Add( + (1)*main_main_mul214_enob_1 + (1)*main_main_mul214_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul214_enob + (-1)*main_p_enob_memphi_main_tmp48 + (-10000)*main_main_mul214_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul214_enob + (-1)*d_enob_memphi_main_tmp47 + (-10000)*main_main_mul214_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
e_enob_memphi_main_tmp49 = solver.IntVar(-10000, 10000, 'e_enob_memphi_main_tmp49')
solver.Add( + (1)*e_enob_memphi_main_tmp49 + (-1)*e_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp49_enob_0 = solver.IntVar(0, 1, 'main_main_tmp49_enob_0')
solver.Add( + (1)*main_main_tmp49_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*e_enob_memphi_main_tmp49 + (-1)*e_enob_storeENOB + (10000)*main_main_tmp49_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add215 = fadd double %mul214, %tmp49, !taffo.info !127, !taffo.initweight !44
main_mul214_CAST_add215_fixbits = solver.IntVar(0, 23, 'main_mul214_CAST_add215_fixbits')
main_mul214_CAST_add215_fixp = solver.IntVar(0, 1, 'main_mul214_CAST_add215_fixp')
main_mul214_CAST_add215_float = solver.IntVar(0, 1, 'main_mul214_CAST_add215_float')
main_mul214_CAST_add215_double = solver.IntVar(0, 1, 'main_mul214_CAST_add215_double')
solver.Add( + (1)*main_mul214_CAST_add215_fixp + (1)*main_mul214_CAST_add215_float + (1)*main_mul214_CAST_add215_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul214_CAST_add215_fixbits + (-10000)*main_mul214_CAST_add215_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C1_main_mul214_CAST_add215')
C2_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C2_main_mul214_CAST_add215')
solver.Add( + (1)*main_mul214_fixbits + (-1)*main_mul214_CAST_add215_fixbits + (-10000)*C1_main_mul214_CAST_add215<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul214_fixbits + (1)*main_mul214_CAST_add215_fixbits + (-10000)*C2_main_mul214_CAST_add215<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul214_CAST_add215
castCostObj +=  + (1)*C2_main_mul214_CAST_add215
C3_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C3_main_mul214_CAST_add215')
C4_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C4_main_mul214_CAST_add215')
C5_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C5_main_mul214_CAST_add215')
C6_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C6_main_mul214_CAST_add215')
C7_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C7_main_mul214_CAST_add215')
C8_main_mul214_CAST_add215 = solver.IntVar(0, 1, 'C8_main_mul214_CAST_add215')
solver.Add( + (1)*main_mul214_fixp + (1)*main_mul214_CAST_add215_float + (-1)*C3_main_mul214_CAST_add215<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul214_CAST_add215
solver.Add( + (1)*main_mul214_float + (1)*main_mul214_CAST_add215_fixp + (-1)*C4_main_mul214_CAST_add215<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul214_CAST_add215
solver.Add( + (1)*main_mul214_fixp + (1)*main_mul214_CAST_add215_double + (-1)*C5_main_mul214_CAST_add215<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul214_CAST_add215
solver.Add( + (1)*main_mul214_double + (1)*main_mul214_CAST_add215_fixp + (-1)*C6_main_mul214_CAST_add215<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul214_CAST_add215
solver.Add( + (1)*main_mul214_float + (1)*main_mul214_CAST_add215_double + (-1)*C7_main_mul214_CAST_add215<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul214_CAST_add215
solver.Add( + (1)*main_mul214_double + (1)*main_mul214_CAST_add215_float + (-1)*C8_main_mul214_CAST_add215<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul214_CAST_add215



#Constraint for cast for   %add215 = fadd double %mul214, %tmp49, !taffo.info !127, !taffo.initweight !44
e_CAST_add215_fixbits = solver.IntVar(0, 23, 'e_CAST_add215_fixbits')
e_CAST_add215_fixp = solver.IntVar(0, 1, 'e_CAST_add215_fixp')
e_CAST_add215_float = solver.IntVar(0, 1, 'e_CAST_add215_float')
e_CAST_add215_double = solver.IntVar(0, 1, 'e_CAST_add215_double')
solver.Add( + (1)*e_CAST_add215_fixp + (1)*e_CAST_add215_float + (1)*e_CAST_add215_double==1)    #exactly 1 type
solver.Add( + (1)*e_CAST_add215_fixbits + (-10000)*e_CAST_add215_fixp<=0)    #If no fix, fix frac part = 0
C1_e_CAST_add215 = solver.IntVar(0, 1, 'C1_e_CAST_add215')
C2_e_CAST_add215 = solver.IntVar(0, 1, 'C2_e_CAST_add215')
solver.Add( + (1)*e_fixbits + (-1)*e_CAST_add215_fixbits + (-10000)*C1_e_CAST_add215<=0)    #Shift cost 1
solver.Add( + (-1)*e_fixbits + (1)*e_CAST_add215_fixbits + (-10000)*C2_e_CAST_add215<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_e_CAST_add215
castCostObj +=  + (1)*C2_e_CAST_add215
C3_e_CAST_add215 = solver.IntVar(0, 1, 'C3_e_CAST_add215')
C4_e_CAST_add215 = solver.IntVar(0, 1, 'C4_e_CAST_add215')
C5_e_CAST_add215 = solver.IntVar(0, 1, 'C5_e_CAST_add215')
C6_e_CAST_add215 = solver.IntVar(0, 1, 'C6_e_CAST_add215')
C7_e_CAST_add215 = solver.IntVar(0, 1, 'C7_e_CAST_add215')
C8_e_CAST_add215 = solver.IntVar(0, 1, 'C8_e_CAST_add215')
solver.Add( + (1)*e_fixp + (1)*e_CAST_add215_float + (-1)*C3_e_CAST_add215<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_e_CAST_add215
solver.Add( + (1)*e_float + (1)*e_CAST_add215_fixp + (-1)*C4_e_CAST_add215<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_e_CAST_add215
solver.Add( + (1)*e_fixp + (1)*e_CAST_add215_double + (-1)*C5_e_CAST_add215<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_e_CAST_add215
solver.Add( + (1)*e_double + (1)*e_CAST_add215_fixp + (-1)*C6_e_CAST_add215<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_e_CAST_add215
solver.Add( + (1)*e_float + (1)*e_CAST_add215_double + (-1)*C7_e_CAST_add215<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_e_CAST_add215
solver.Add( + (1)*e_double + (1)*e_CAST_add215_float + (-1)*C8_e_CAST_add215<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_e_CAST_add215



#Stuff for   %add215 = fadd double %mul214, %tmp49, !taffo.info !127, !taffo.initweight !44
main_add215_fixbits = solver.IntVar(0, 21, 'main_add215_fixbits')
main_add215_fixp = solver.IntVar(0, 1, 'main_add215_fixp')
main_add215_float = solver.IntVar(0, 1, 'main_add215_float')
main_add215_double = solver.IntVar(0, 1, 'main_add215_double')
main_add215_enob = solver.IntVar(-10000, 10000, 'main_add215_enob')
solver.Add( + (1)*main_add215_enob + (-1)*main_add215_fixbits + (10000)*main_add215_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add215_enob + (10000)*main_add215_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add215_enob + (10000)*main_add215_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add215_fixbits + (-10000)*main_add215_fixp>=-9980)    #Limit the lower number of frac bits21
solver.Add( + (1)*main_add215_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add215_enob
solver.Add( + (1)*main_add215_fixp + (1)*main_add215_float + (1)*main_add215_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add215_fixbits + (-10000)*main_add215_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul214_CAST_add215_fixp + (-1)*e_CAST_add215_fixp==0)    #fix equality
solver.Add( + (1)*main_mul214_CAST_add215_float + (-1)*e_CAST_add215_float==0)    #float equality
solver.Add( + (1)*main_mul214_CAST_add215_double + (-1)*e_CAST_add215_double==0)    #double equality
solver.Add( + (1)*main_mul214_CAST_add215_fixbits + (-1)*e_CAST_add215_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul214_CAST_add215_fixp + (-1)*main_add215_fixp==0)    #fix equality
solver.Add( + (1)*main_mul214_CAST_add215_float + (-1)*main_add215_float==0)    #float equality
solver.Add( + (1)*main_mul214_CAST_add215_double + (-1)*main_add215_double==0)    #double equality
solver.Add( + (1)*main_mul214_CAST_add215_fixbits + (-1)*main_add215_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add215_fixp
mathCostObj +=  + (3)*main_add215_float
mathCostObj +=  + (6.64928)*main_add215_double
solver.Add( + (1)*main_add215_enob + (-1)*main_mul214_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add215_enob + (-1)*e_enob_memphi_main_tmp49<=0)    #Enob propagation in sum second addend

#Restriction for new enob [LOAD]
main_q_enob_memphi_main_tmp50 = solver.IntVar(-10000, 10000, 'main_q_enob_memphi_main_tmp50')
solver.Add( + (1)*main_q_enob_memphi_main_tmp50 + (-1)*main_q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp50_enob_0 = solver.IntVar(0, 1, 'main_main_tmp50_enob_0')
solver.Add( + (1)*main_main_tmp50_enob_0==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp50 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp50_enob_0<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %div220 = fdiv double %tmp50, %add215, !taffo.info !145, !taffo.initweight !45
main_q_CAST_div220_fixbits = solver.IntVar(0, 22, 'main_q_CAST_div220_fixbits')
main_q_CAST_div220_fixp = solver.IntVar(0, 1, 'main_q_CAST_div220_fixp')
main_q_CAST_div220_float = solver.IntVar(0, 1, 'main_q_CAST_div220_float')
main_q_CAST_div220_double = solver.IntVar(0, 1, 'main_q_CAST_div220_double')
solver.Add( + (1)*main_q_CAST_div220_fixp + (1)*main_q_CAST_div220_float + (1)*main_q_CAST_div220_double==1)    #exactly 1 type
solver.Add( + (1)*main_q_CAST_div220_fixbits + (-10000)*main_q_CAST_div220_fixp<=0)    #If no fix, fix frac part = 0
C1_main_q_CAST_div220 = solver.IntVar(0, 1, 'C1_main_q_CAST_div220')
C2_main_q_CAST_div220 = solver.IntVar(0, 1, 'C2_main_q_CAST_div220')
solver.Add( + (1)*main_q_fixbits + (-1)*main_q_CAST_div220_fixbits + (-10000)*C1_main_q_CAST_div220<=0)    #Shift cost 1
solver.Add( + (-1)*main_q_fixbits + (1)*main_q_CAST_div220_fixbits + (-10000)*C2_main_q_CAST_div220<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_q_CAST_div220
castCostObj +=  + (1)*C2_main_q_CAST_div220
C3_main_q_CAST_div220 = solver.IntVar(0, 1, 'C3_main_q_CAST_div220')
C4_main_q_CAST_div220 = solver.IntVar(0, 1, 'C4_main_q_CAST_div220')
C5_main_q_CAST_div220 = solver.IntVar(0, 1, 'C5_main_q_CAST_div220')
C6_main_q_CAST_div220 = solver.IntVar(0, 1, 'C6_main_q_CAST_div220')
C7_main_q_CAST_div220 = solver.IntVar(0, 1, 'C7_main_q_CAST_div220')
C8_main_q_CAST_div220 = solver.IntVar(0, 1, 'C8_main_q_CAST_div220')
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_div220_float + (-1)*C3_main_q_CAST_div220<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_q_CAST_div220
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_div220_fixp + (-1)*C4_main_q_CAST_div220<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_q_CAST_div220
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_div220_double + (-1)*C5_main_q_CAST_div220<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_q_CAST_div220
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_div220_fixp + (-1)*C6_main_q_CAST_div220<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_q_CAST_div220
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_div220_double + (-1)*C7_main_q_CAST_div220<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_q_CAST_div220
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_div220_float + (-1)*C8_main_q_CAST_div220<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_q_CAST_div220



#Constraint for cast for   %div220 = fdiv double %tmp50, %add215, !taffo.info !145, !taffo.initweight !45
main_add215_CAST_div220_fixbits = solver.IntVar(0, 21, 'main_add215_CAST_div220_fixbits')
main_add215_CAST_div220_fixp = solver.IntVar(0, 1, 'main_add215_CAST_div220_fixp')
main_add215_CAST_div220_float = solver.IntVar(0, 1, 'main_add215_CAST_div220_float')
main_add215_CAST_div220_double = solver.IntVar(0, 1, 'main_add215_CAST_div220_double')
solver.Add( + (1)*main_add215_CAST_div220_fixp + (1)*main_add215_CAST_div220_float + (1)*main_add215_CAST_div220_double==1)    #exactly 1 type
solver.Add( + (1)*main_add215_CAST_div220_fixbits + (-10000)*main_add215_CAST_div220_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C1_main_add215_CAST_div220')
C2_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C2_main_add215_CAST_div220')
solver.Add( + (1)*main_add215_fixbits + (-1)*main_add215_CAST_div220_fixbits + (-10000)*C1_main_add215_CAST_div220<=0)    #Shift cost 1
solver.Add( + (-1)*main_add215_fixbits + (1)*main_add215_CAST_div220_fixbits + (-10000)*C2_main_add215_CAST_div220<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add215_CAST_div220
castCostObj +=  + (1)*C2_main_add215_CAST_div220
C3_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C3_main_add215_CAST_div220')
C4_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C4_main_add215_CAST_div220')
C5_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C5_main_add215_CAST_div220')
C6_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C6_main_add215_CAST_div220')
C7_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C7_main_add215_CAST_div220')
C8_main_add215_CAST_div220 = solver.IntVar(0, 1, 'C8_main_add215_CAST_div220')
solver.Add( + (1)*main_add215_fixp + (1)*main_add215_CAST_div220_float + (-1)*C3_main_add215_CAST_div220<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add215_CAST_div220
solver.Add( + (1)*main_add215_float + (1)*main_add215_CAST_div220_fixp + (-1)*C4_main_add215_CAST_div220<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add215_CAST_div220
solver.Add( + (1)*main_add215_fixp + (1)*main_add215_CAST_div220_double + (-1)*C5_main_add215_CAST_div220<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add215_CAST_div220
solver.Add( + (1)*main_add215_double + (1)*main_add215_CAST_div220_fixp + (-1)*C6_main_add215_CAST_div220<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add215_CAST_div220
solver.Add( + (1)*main_add215_float + (1)*main_add215_CAST_div220_double + (-1)*C7_main_add215_CAST_div220<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add215_CAST_div220
solver.Add( + (1)*main_add215_double + (1)*main_add215_CAST_div220_float + (-1)*C8_main_add215_CAST_div220<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add215_CAST_div220



#Stuff for   %div220 = fdiv double %tmp50, %add215, !taffo.info !145, !taffo.initweight !45
main_div220_fixbits = solver.IntVar(0, 29, 'main_div220_fixbits')
main_div220_fixp = solver.IntVar(0, 1, 'main_div220_fixp')
main_div220_float = solver.IntVar(0, 1, 'main_div220_float')
main_div220_double = solver.IntVar(0, 1, 'main_div220_double')
main_div220_enob = solver.IntVar(-10000, 10000, 'main_div220_enob')
solver.Add( + (1)*main_div220_enob + (-1)*main_div220_fixbits + (10000)*main_div220_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_div220_enob + (10000)*main_div220_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_div220_enob + (10000)*main_div220_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_div220_fixbits + (-10000)*main_div220_fixp>=-9972)    #Limit the lower number of frac bits29
solver.Add( + (1)*main_div220_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_div220_enob
solver.Add( + (1)*main_div220_fixp + (1)*main_div220_float + (1)*main_div220_double==1)    #Exactly one selected type
solver.Add( + (1)*main_div220_fixbits + (-10000)*main_div220_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_q_CAST_div220_fixp + (-1)*main_add215_CAST_div220_fixp==0)    #fix equality
solver.Add( + (1)*main_q_CAST_div220_float + (-1)*main_add215_CAST_div220_float==0)    #float equality
solver.Add( + (1)*main_q_CAST_div220_double + (-1)*main_add215_CAST_div220_double==0)    #double equality
solver.Add( + (1)*main_q_CAST_div220_fixp + (-1)*main_div220_fixp==0)    #fix equality
solver.Add( + (1)*main_q_CAST_div220_float + (-1)*main_div220_float==0)    #float equality
solver.Add( + (1)*main_q_CAST_div220_double + (-1)*main_div220_double==0)    #double equality
mathCostObj +=  + (1.61159)*main_div220_fixp
mathCostObj +=  + (6)*main_div220_float
mathCostObj +=  + (12)*main_div220_double
main_main_div220_enob_1 = solver.IntVar(0, 1, 'main_main_div220_enob_1')
main_main_div220_enob_2 = solver.IntVar(0, 1, 'main_main_div220_enob_2')
solver.Add( + (1)*main_main_div220_enob_1 + (1)*main_main_div220_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_div220_enob + (-1)*main_add215_enob + (-10000)*main_main_div220_enob_1<=1042)    #Enob: propagation in division 1
solver.Add( + (1)*main_div220_enob + (-1)*main_q_enob_memphi_main_tmp50 + (-10000)*main_main_div220_enob_2<=1042)    #Enob: propagation in division 2



#Constraint for cast for   store double %div220, double* %arrayidx219, align 8, !taffo.info !39, !taffo.initweight !45
main_div220_CAST_store_fixbits = solver.IntVar(0, 29, 'main_div220_CAST_store_fixbits')
main_div220_CAST_store_fixp = solver.IntVar(0, 1, 'main_div220_CAST_store_fixp')
main_div220_CAST_store_float = solver.IntVar(0, 1, 'main_div220_CAST_store_float')
main_div220_CAST_store_double = solver.IntVar(0, 1, 'main_div220_CAST_store_double')
solver.Add( + (1)*main_div220_CAST_store_fixp + (1)*main_div220_CAST_store_float + (1)*main_div220_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_div220_CAST_store_fixbits + (-10000)*main_div220_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_div220_CAST_store = solver.IntVar(0, 1, 'C1_main_div220_CAST_store')
C2_main_div220_CAST_store = solver.IntVar(0, 1, 'C2_main_div220_CAST_store')
solver.Add( + (1)*main_div220_fixbits + (-1)*main_div220_CAST_store_fixbits + (-10000)*C1_main_div220_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_div220_fixbits + (1)*main_div220_CAST_store_fixbits + (-10000)*C2_main_div220_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_div220_CAST_store
castCostObj +=  + (1)*C2_main_div220_CAST_store
C3_main_div220_CAST_store = solver.IntVar(0, 1, 'C3_main_div220_CAST_store')
C4_main_div220_CAST_store = solver.IntVar(0, 1, 'C4_main_div220_CAST_store')
C5_main_div220_CAST_store = solver.IntVar(0, 1, 'C5_main_div220_CAST_store')
C6_main_div220_CAST_store = solver.IntVar(0, 1, 'C6_main_div220_CAST_store')
C7_main_div220_CAST_store = solver.IntVar(0, 1, 'C7_main_div220_CAST_store')
C8_main_div220_CAST_store = solver.IntVar(0, 1, 'C8_main_div220_CAST_store')
solver.Add( + (1)*main_div220_fixp + (1)*main_div220_CAST_store_float + (-1)*C3_main_div220_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_div220_CAST_store
solver.Add( + (1)*main_div220_float + (1)*main_div220_CAST_store_fixp + (-1)*C4_main_div220_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_div220_CAST_store
solver.Add( + (1)*main_div220_fixp + (1)*main_div220_CAST_store_double + (-1)*C5_main_div220_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_div220_CAST_store
solver.Add( + (1)*main_div220_double + (1)*main_div220_CAST_store_fixp + (-1)*C6_main_div220_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_div220_CAST_store
solver.Add( + (1)*main_div220_float + (1)*main_div220_CAST_store_double + (-1)*C7_main_div220_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_div220_CAST_store
solver.Add( + (1)*main_div220_double + (1)*main_div220_CAST_store_float + (-1)*C8_main_div220_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_div220_CAST_store
solver.Add( + (1)*main_q_fixp + (-1)*main_div220_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_q_float + (-1)*main_div220_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_q_double + (-1)*main_div220_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_q_fixbits + (-1)*main_div220_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB = solver.IntVar(-10000, 10000, 'main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB')
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_q_fixbits + (10000)*main_q_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_q_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_q_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (-1)*main_div220_enob<=0)    #Enob constraint ENOB propagation in load/store



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
solver.Add( + (1)*ConstantValue__61_double<=0)    #Disable double data type
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
solver.Add( + (1)*ConstantValue__62_double<=0)    #Disable double data type
solver.Add( + (1)*ConstantValue__62_fixp + (1)*ConstantValue__62_float + (1)*ConstantValue__62_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__62_fixbits + (-10000)*ConstantValue__62_fixp<=0)    #If not fix, frac part to zero



#Constraint for cast for   store double 1.000000e+00, double* %arrayidx226, align 8, !taffo.info !33, !taffo.initweight !45, !taffo.constinfo !66
ConstantValue__62_CAST_store_fixbits = solver.IntVar(0, 31, 'ConstantValue__62_CAST_store_fixbits')
ConstantValue__62_CAST_store_fixp = solver.IntVar(0, 1, 'ConstantValue__62_CAST_store_fixp')
ConstantValue__62_CAST_store_float = solver.IntVar(0, 1, 'ConstantValue__62_CAST_store_float')
ConstantValue__62_CAST_store_double = solver.IntVar(0, 1, 'ConstantValue__62_CAST_store_double')
solver.Add( + (1)*ConstantValue__62_CAST_store_fixp + (1)*ConstantValue__62_CAST_store_float + (1)*ConstantValue__62_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*ConstantValue__62_CAST_store_fixbits + (-10000)*ConstantValue__62_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C1_ConstantValue__62_CAST_store')
C2_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C2_ConstantValue__62_CAST_store')
solver.Add( + (1)*ConstantValue__62_fixbits + (-1)*ConstantValue__62_CAST_store_fixbits + (-10000)*C1_ConstantValue__62_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__62_fixbits + (1)*ConstantValue__62_CAST_store_fixbits + (-10000)*C2_ConstantValue__62_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_ConstantValue__62_CAST_store
castCostObj +=  + (1)*C2_ConstantValue__62_CAST_store
C3_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C3_ConstantValue__62_CAST_store')
C4_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C4_ConstantValue__62_CAST_store')
C5_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C5_ConstantValue__62_CAST_store')
C6_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C6_ConstantValue__62_CAST_store')
C7_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C7_ConstantValue__62_CAST_store')
C8_ConstantValue__62_CAST_store = solver.IntVar(0, 1, 'C8_ConstantValue__62_CAST_store')
solver.Add( + (1)*ConstantValue__62_fixp + (1)*ConstantValue__62_CAST_store_float + (-1)*C3_ConstantValue__62_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_ConstantValue__62_CAST_store
solver.Add( + (1)*ConstantValue__62_float + (1)*ConstantValue__62_CAST_store_fixp + (-1)*C4_ConstantValue__62_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_ConstantValue__62_CAST_store
solver.Add( + (1)*ConstantValue__62_fixp + (1)*ConstantValue__62_CAST_store_double + (-1)*C5_ConstantValue__62_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_ConstantValue__62_CAST_store
solver.Add( + (1)*ConstantValue__62_double + (1)*ConstantValue__62_CAST_store_fixp + (-1)*C6_ConstantValue__62_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_ConstantValue__62_CAST_store
solver.Add( + (1)*ConstantValue__62_float + (1)*ConstantValue__62_CAST_store_double + (-1)*C7_ConstantValue__62_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_ConstantValue__62_CAST_store
solver.Add( + (1)*ConstantValue__62_double + (1)*ConstantValue__62_CAST_store_float + (-1)*C8_ConstantValue__62_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_ConstantValue__62_CAST_store
solver.Add( + (1)*main_u_fixp + (-1)*ConstantValue__62_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_u_float + (-1)*ConstantValue__62_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_u_double + (-1)*ConstantValue__62_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_u_fixbits + (-1)*ConstantValue__62_CAST_store_fixbits==0)    #same fractional bit

#Storing constant, no new enob.



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp20 + (-1)*ConstantValue__61_enob + (10000)*main_main_tmp20_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp22 + (-1)*ConstantValue__61_enob + (10000)*main_main_tmp22_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp24 + (-1)*ConstantValue__61_enob + (10000)*main_main_tmp24_enob_3<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp40 + (-1)*ConstantValue__61_enob + (10000)*main_main_tmp40_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp42 + (-1)*ConstantValue__61_enob + (10000)*main_main_tmp42_enob_1<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp44 + (-1)*ConstantValue__61_enob + (10000)*main_main_tmp44_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_p_enob_memphi_main_tmp51 = solver.IntVar(-10000, 10000, 'main_p_enob_memphi_main_tmp51')
solver.Add( + (1)*main_p_enob_memphi_main_tmp51 + (-1)*main_p_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp51_enob_0 = solver.IntVar(0, 1, 'main_main_tmp51_enob_0')
main_main_tmp51_enob_1 = solver.IntVar(0, 1, 'main_main_tmp51_enob_1')
solver.Add( + (1)*main_main_tmp51_enob_0 + (1)*main_main_tmp51_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_p_enob_memphi_main_tmp51 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp51_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_p_enob_memphi_main_tmp51 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp51_enob_1<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_u_enob_memphi_main_tmp52 = solver.IntVar(-10000, 10000, 'main_u_enob_memphi_main_tmp52')
solver.Add( + (1)*main_u_enob_memphi_main_tmp52 + (-1)*main_u_enob<=0)    #Enob constraint, new enob at most original variable enob



#Constraint for cast for   %mul240 = fmul double %tmp51, %tmp52, !taffo.info !33, !taffo.initweight !51
main_p_CAST_mul240_fixbits = solver.IntVar(0, 30, 'main_p_CAST_mul240_fixbits')
main_p_CAST_mul240_fixp = solver.IntVar(0, 1, 'main_p_CAST_mul240_fixp')
main_p_CAST_mul240_float = solver.IntVar(0, 1, 'main_p_CAST_mul240_float')
main_p_CAST_mul240_double = solver.IntVar(0, 1, 'main_p_CAST_mul240_double')
solver.Add( + (1)*main_p_CAST_mul240_fixp + (1)*main_p_CAST_mul240_float + (1)*main_p_CAST_mul240_double==1)    #exactly 1 type
solver.Add( + (1)*main_p_CAST_mul240_fixbits + (-10000)*main_p_CAST_mul240_fixp<=0)    #If no fix, fix frac part = 0
C1_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C1_main_p_CAST_mul240')
C2_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C2_main_p_CAST_mul240')
solver.Add( + (1)*main_p_fixbits + (-1)*main_p_CAST_mul240_fixbits + (-10000)*C1_main_p_CAST_mul240<=0)    #Shift cost 1
solver.Add( + (-1)*main_p_fixbits + (1)*main_p_CAST_mul240_fixbits + (-10000)*C2_main_p_CAST_mul240<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_p_CAST_mul240
castCostObj +=  + (1)*C2_main_p_CAST_mul240
C3_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C3_main_p_CAST_mul240')
C4_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C4_main_p_CAST_mul240')
C5_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C5_main_p_CAST_mul240')
C6_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C6_main_p_CAST_mul240')
C7_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C7_main_p_CAST_mul240')
C8_main_p_CAST_mul240 = solver.IntVar(0, 1, 'C8_main_p_CAST_mul240')
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul240_float + (-1)*C3_main_p_CAST_mul240<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_p_CAST_mul240
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul240_fixp + (-1)*C4_main_p_CAST_mul240<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_p_CAST_mul240
solver.Add( + (1)*main_p_fixp + (1)*main_p_CAST_mul240_double + (-1)*C5_main_p_CAST_mul240<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_p_CAST_mul240
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul240_fixp + (-1)*C6_main_p_CAST_mul240<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_p_CAST_mul240
solver.Add( + (1)*main_p_float + (1)*main_p_CAST_mul240_double + (-1)*C7_main_p_CAST_mul240<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_p_CAST_mul240
solver.Add( + (1)*main_p_double + (1)*main_p_CAST_mul240_float + (-1)*C8_main_p_CAST_mul240<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_p_CAST_mul240



#Constraint for cast for   %mul240 = fmul double %tmp51, %tmp52, !taffo.info !33, !taffo.initweight !51
main_u_CAST_mul240_fixbits = solver.IntVar(0, 28, 'main_u_CAST_mul240_fixbits')
main_u_CAST_mul240_fixp = solver.IntVar(0, 1, 'main_u_CAST_mul240_fixp')
main_u_CAST_mul240_float = solver.IntVar(0, 1, 'main_u_CAST_mul240_float')
main_u_CAST_mul240_double = solver.IntVar(0, 1, 'main_u_CAST_mul240_double')
solver.Add( + (1)*main_u_CAST_mul240_fixp + (1)*main_u_CAST_mul240_float + (1)*main_u_CAST_mul240_double==1)    #exactly 1 type
solver.Add( + (1)*main_u_CAST_mul240_fixbits + (-10000)*main_u_CAST_mul240_fixp<=0)    #If no fix, fix frac part = 0
C1_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C1_main_u_CAST_mul240')
C2_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C2_main_u_CAST_mul240')
solver.Add( + (1)*main_u_fixbits + (-1)*main_u_CAST_mul240_fixbits + (-10000)*C1_main_u_CAST_mul240<=0)    #Shift cost 1
solver.Add( + (-1)*main_u_fixbits + (1)*main_u_CAST_mul240_fixbits + (-10000)*C2_main_u_CAST_mul240<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_u_CAST_mul240
castCostObj +=  + (1)*C2_main_u_CAST_mul240
C3_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C3_main_u_CAST_mul240')
C4_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C4_main_u_CAST_mul240')
C5_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C5_main_u_CAST_mul240')
C6_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C6_main_u_CAST_mul240')
C7_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C7_main_u_CAST_mul240')
C8_main_u_CAST_mul240 = solver.IntVar(0, 1, 'C8_main_u_CAST_mul240')
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul240_float + (-1)*C3_main_u_CAST_mul240<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_u_CAST_mul240
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul240_fixp + (-1)*C4_main_u_CAST_mul240<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_u_CAST_mul240
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_mul240_double + (-1)*C5_main_u_CAST_mul240<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_u_CAST_mul240
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul240_fixp + (-1)*C6_main_u_CAST_mul240<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_u_CAST_mul240
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_mul240_double + (-1)*C7_main_u_CAST_mul240<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_u_CAST_mul240
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_mul240_float + (-1)*C8_main_u_CAST_mul240<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_u_CAST_mul240



#Stuff for   %mul240 = fmul double %tmp51, %tmp52, !taffo.info !33, !taffo.initweight !51
main_mul240_fixbits = solver.IntVar(0, 28, 'main_mul240_fixbits')
main_mul240_fixp = solver.IntVar(0, 1, 'main_mul240_fixp')
main_mul240_float = solver.IntVar(0, 1, 'main_mul240_float')
main_mul240_double = solver.IntVar(0, 1, 'main_mul240_double')
main_mul240_enob = solver.IntVar(-10000, 10000, 'main_mul240_enob')
solver.Add( + (1)*main_mul240_enob + (-1)*main_mul240_fixbits + (10000)*main_mul240_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul240_enob + (10000)*main_mul240_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_mul240_enob + (10000)*main_mul240_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_mul240_fixbits + (-10000)*main_mul240_fixp>=-9973)    #Limit the lower number of frac bits28
solver.Add( + (1)*main_mul240_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_mul240_enob
solver.Add( + (1)*main_mul240_fixp + (1)*main_mul240_float + (1)*main_mul240_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul240_fixbits + (-10000)*main_mul240_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_p_CAST_mul240_fixp + (-1)*main_u_CAST_mul240_fixp==0)    #fix equality
solver.Add( + (1)*main_p_CAST_mul240_float + (-1)*main_u_CAST_mul240_float==0)    #float equality
solver.Add( + (1)*main_p_CAST_mul240_double + (-1)*main_u_CAST_mul240_double==0)    #double equality
solver.Add( + (1)*main_p_CAST_mul240_fixp + (-1)*main_mul240_fixp==0)    #fix equality
solver.Add( + (1)*main_p_CAST_mul240_float + (-1)*main_mul240_float==0)    #float equality
solver.Add( + (1)*main_p_CAST_mul240_double + (-1)*main_mul240_double==0)    #double equality
mathCostObj +=  + (1.65217)*main_mul240_fixp
mathCostObj +=  + (6)*main_mul240_float
mathCostObj +=  + (12.2551)*main_mul240_double
main_main_mul240_enob_1 = solver.IntVar(0, 1, 'main_main_mul240_enob_1')
main_main_mul240_enob_2 = solver.IntVar(0, 1, 'main_main_mul240_enob_2')
solver.Add( + (1)*main_main_mul240_enob_1 + (1)*main_main_mul240_enob_2==1)    #Enob: one selected constraint
solver.Add( + (1)*main_mul240_enob + (-1)*main_u_enob_memphi_main_tmp52 + (-10000)*main_main_mul240_enob_1<=1024)    #Enob: propagation in product 1
solver.Add( + (1)*main_mul240_enob + (-1)*main_p_enob_memphi_main_tmp51 + (-10000)*main_main_mul240_enob_2<=1024)    #Enob: propagation in product 2

#Restriction for new enob [LOAD]
main_q_enob_memphi_main_tmp53 = solver.IntVar(-10000, 10000, 'main_q_enob_memphi_main_tmp53')
solver.Add( + (1)*main_q_enob_memphi_main_tmp53 + (-1)*main_q_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp53_enob_0 = solver.IntVar(0, 1, 'main_main_tmp53_enob_0')
main_main_tmp53_enob_1 = solver.IntVar(0, 1, 'main_main_tmp53_enob_1')
solver.Add( + (1)*main_main_tmp53_enob_0 + (1)*main_main_tmp53_enob_1==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp53 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp53_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_q_enob_memphi_main_tmp53 + (-1)*main_q_enob_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB_storeENOB + (10000)*main_main_tmp53_enob_1<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %add245 = fadd double %mul240, %tmp53, !taffo.info !147, !taffo.initweight !51
main_mul240_CAST_add245_fixbits = solver.IntVar(0, 28, 'main_mul240_CAST_add245_fixbits')
main_mul240_CAST_add245_fixp = solver.IntVar(0, 1, 'main_mul240_CAST_add245_fixp')
main_mul240_CAST_add245_float = solver.IntVar(0, 1, 'main_mul240_CAST_add245_float')
main_mul240_CAST_add245_double = solver.IntVar(0, 1, 'main_mul240_CAST_add245_double')
solver.Add( + (1)*main_mul240_CAST_add245_fixp + (1)*main_mul240_CAST_add245_float + (1)*main_mul240_CAST_add245_double==1)    #exactly 1 type
solver.Add( + (1)*main_mul240_CAST_add245_fixbits + (-10000)*main_mul240_CAST_add245_fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C1_main_mul240_CAST_add245')
C2_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C2_main_mul240_CAST_add245')
solver.Add( + (1)*main_mul240_fixbits + (-1)*main_mul240_CAST_add245_fixbits + (-10000)*C1_main_mul240_CAST_add245<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul240_fixbits + (1)*main_mul240_CAST_add245_fixbits + (-10000)*C2_main_mul240_CAST_add245<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_mul240_CAST_add245
castCostObj +=  + (1)*C2_main_mul240_CAST_add245
C3_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C3_main_mul240_CAST_add245')
C4_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C4_main_mul240_CAST_add245')
C5_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C5_main_mul240_CAST_add245')
C6_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C6_main_mul240_CAST_add245')
C7_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C7_main_mul240_CAST_add245')
C8_main_mul240_CAST_add245 = solver.IntVar(0, 1, 'C8_main_mul240_CAST_add245')
solver.Add( + (1)*main_mul240_fixp + (1)*main_mul240_CAST_add245_float + (-1)*C3_main_mul240_CAST_add245<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_mul240_CAST_add245
solver.Add( + (1)*main_mul240_float + (1)*main_mul240_CAST_add245_fixp + (-1)*C4_main_mul240_CAST_add245<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_mul240_CAST_add245
solver.Add( + (1)*main_mul240_fixp + (1)*main_mul240_CAST_add245_double + (-1)*C5_main_mul240_CAST_add245<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_mul240_CAST_add245
solver.Add( + (1)*main_mul240_double + (1)*main_mul240_CAST_add245_fixp + (-1)*C6_main_mul240_CAST_add245<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_mul240_CAST_add245
solver.Add( + (1)*main_mul240_float + (1)*main_mul240_CAST_add245_double + (-1)*C7_main_mul240_CAST_add245<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_mul240_CAST_add245
solver.Add( + (1)*main_mul240_double + (1)*main_mul240_CAST_add245_float + (-1)*C8_main_mul240_CAST_add245<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_mul240_CAST_add245



#Constraint for cast for   %add245 = fadd double %mul240, %tmp53, !taffo.info !147, !taffo.initweight !51
main_q_CAST_add245_fixbits = solver.IntVar(0, 22, 'main_q_CAST_add245_fixbits')
main_q_CAST_add245_fixp = solver.IntVar(0, 1, 'main_q_CAST_add245_fixp')
main_q_CAST_add245_float = solver.IntVar(0, 1, 'main_q_CAST_add245_float')
main_q_CAST_add245_double = solver.IntVar(0, 1, 'main_q_CAST_add245_double')
solver.Add( + (1)*main_q_CAST_add245_fixp + (1)*main_q_CAST_add245_float + (1)*main_q_CAST_add245_double==1)    #exactly 1 type
solver.Add( + (1)*main_q_CAST_add245_fixbits + (-10000)*main_q_CAST_add245_fixp<=0)    #If no fix, fix frac part = 0
C1_main_q_CAST_add245 = solver.IntVar(0, 1, 'C1_main_q_CAST_add245')
C2_main_q_CAST_add245 = solver.IntVar(0, 1, 'C2_main_q_CAST_add245')
solver.Add( + (1)*main_q_fixbits + (-1)*main_q_CAST_add245_fixbits + (-10000)*C1_main_q_CAST_add245<=0)    #Shift cost 1
solver.Add( + (-1)*main_q_fixbits + (1)*main_q_CAST_add245_fixbits + (-10000)*C2_main_q_CAST_add245<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_q_CAST_add245
castCostObj +=  + (1)*C2_main_q_CAST_add245
C3_main_q_CAST_add245 = solver.IntVar(0, 1, 'C3_main_q_CAST_add245')
C4_main_q_CAST_add245 = solver.IntVar(0, 1, 'C4_main_q_CAST_add245')
C5_main_q_CAST_add245 = solver.IntVar(0, 1, 'C5_main_q_CAST_add245')
C6_main_q_CAST_add245 = solver.IntVar(0, 1, 'C6_main_q_CAST_add245')
C7_main_q_CAST_add245 = solver.IntVar(0, 1, 'C7_main_q_CAST_add245')
C8_main_q_CAST_add245 = solver.IntVar(0, 1, 'C8_main_q_CAST_add245')
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_add245_float + (-1)*C3_main_q_CAST_add245<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_q_CAST_add245
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_add245_fixp + (-1)*C4_main_q_CAST_add245<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_q_CAST_add245
solver.Add( + (1)*main_q_fixp + (1)*main_q_CAST_add245_double + (-1)*C5_main_q_CAST_add245<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_q_CAST_add245
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_add245_fixp + (-1)*C6_main_q_CAST_add245<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_q_CAST_add245
solver.Add( + (1)*main_q_float + (1)*main_q_CAST_add245_double + (-1)*C7_main_q_CAST_add245<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_q_CAST_add245
solver.Add( + (1)*main_q_double + (1)*main_q_CAST_add245_float + (-1)*C8_main_q_CAST_add245<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_q_CAST_add245



#Stuff for   %add245 = fadd double %mul240, %tmp53, !taffo.info !147, !taffo.initweight !51
main_add245_fixbits = solver.IntVar(0, 22, 'main_add245_fixbits')
main_add245_fixp = solver.IntVar(0, 1, 'main_add245_fixp')
main_add245_float = solver.IntVar(0, 1, 'main_add245_float')
main_add245_double = solver.IntVar(0, 1, 'main_add245_double')
main_add245_enob = solver.IntVar(-10000, 10000, 'main_add245_enob')
solver.Add( + (1)*main_add245_enob + (-1)*main_add245_fixbits + (10000)*main_add245_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add245_enob + (10000)*main_add245_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_add245_enob + (10000)*main_add245_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_add245_fixbits + (-10000)*main_add245_fixp>=-9979)    #Limit the lower number of frac bits22
solver.Add( + (1)*main_add245_double<=0)    #Disable double data type
enobCostObj +=  + (-1)*main_add245_enob
solver.Add( + (1)*main_add245_fixp + (1)*main_add245_float + (1)*main_add245_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add245_fixbits + (-10000)*main_add245_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*main_mul240_CAST_add245_fixp + (-1)*main_q_CAST_add245_fixp==0)    #fix equality
solver.Add( + (1)*main_mul240_CAST_add245_float + (-1)*main_q_CAST_add245_float==0)    #float equality
solver.Add( + (1)*main_mul240_CAST_add245_double + (-1)*main_q_CAST_add245_double==0)    #double equality
solver.Add( + (1)*main_mul240_CAST_add245_fixbits + (-1)*main_q_CAST_add245_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_mul240_CAST_add245_fixp + (-1)*main_add245_fixp==0)    #fix equality
solver.Add( + (1)*main_mul240_CAST_add245_float + (-1)*main_add245_float==0)    #float equality
solver.Add( + (1)*main_mul240_CAST_add245_double + (-1)*main_add245_double==0)    #double equality
solver.Add( + (1)*main_mul240_CAST_add245_fixbits + (-1)*main_add245_fixbits==0)    #same fractional bit
mathCostObj +=  + (1.27246)*main_add245_fixp
mathCostObj +=  + (3)*main_add245_float
mathCostObj +=  + (6.64928)*main_add245_double
solver.Add( + (1)*main_add245_enob + (-1)*main_mul240_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add245_enob + (-1)*main_q_enob_memphi_main_tmp53<=0)    #Enob propagation in sum second addend



#Constraint for cast for   store double %add245, double* %arrayidx249, align 8, !taffo.info !33, !taffo.initweight !45
main_add245_CAST_store_fixbits = solver.IntVar(0, 22, 'main_add245_CAST_store_fixbits')
main_add245_CAST_store_fixp = solver.IntVar(0, 1, 'main_add245_CAST_store_fixp')
main_add245_CAST_store_float = solver.IntVar(0, 1, 'main_add245_CAST_store_float')
main_add245_CAST_store_double = solver.IntVar(0, 1, 'main_add245_CAST_store_double')
solver.Add( + (1)*main_add245_CAST_store_fixp + (1)*main_add245_CAST_store_float + (1)*main_add245_CAST_store_double==1)    #exactly 1 type
solver.Add( + (1)*main_add245_CAST_store_fixbits + (-10000)*main_add245_CAST_store_fixp<=0)    #If no fix, fix frac part = 0
C1_main_add245_CAST_store = solver.IntVar(0, 1, 'C1_main_add245_CAST_store')
C2_main_add245_CAST_store = solver.IntVar(0, 1, 'C2_main_add245_CAST_store')
solver.Add( + (1)*main_add245_fixbits + (-1)*main_add245_CAST_store_fixbits + (-10000)*C1_main_add245_CAST_store<=0)    #Shift cost 1
solver.Add( + (-1)*main_add245_fixbits + (1)*main_add245_CAST_store_fixbits + (-10000)*C2_main_add245_CAST_store<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_add245_CAST_store
castCostObj +=  + (1)*C2_main_add245_CAST_store
C3_main_add245_CAST_store = solver.IntVar(0, 1, 'C3_main_add245_CAST_store')
C4_main_add245_CAST_store = solver.IntVar(0, 1, 'C4_main_add245_CAST_store')
C5_main_add245_CAST_store = solver.IntVar(0, 1, 'C5_main_add245_CAST_store')
C6_main_add245_CAST_store = solver.IntVar(0, 1, 'C6_main_add245_CAST_store')
C7_main_add245_CAST_store = solver.IntVar(0, 1, 'C7_main_add245_CAST_store')
C8_main_add245_CAST_store = solver.IntVar(0, 1, 'C8_main_add245_CAST_store')
solver.Add( + (1)*main_add245_fixp + (1)*main_add245_CAST_store_float + (-1)*C3_main_add245_CAST_store<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_add245_CAST_store
solver.Add( + (1)*main_add245_float + (1)*main_add245_CAST_store_fixp + (-1)*C4_main_add245_CAST_store<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_add245_CAST_store
solver.Add( + (1)*main_add245_fixp + (1)*main_add245_CAST_store_double + (-1)*C5_main_add245_CAST_store<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_add245_CAST_store
solver.Add( + (1)*main_add245_double + (1)*main_add245_CAST_store_fixp + (-1)*C6_main_add245_CAST_store<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_add245_CAST_store
solver.Add( + (1)*main_add245_float + (1)*main_add245_CAST_store_double + (-1)*C7_main_add245_CAST_store<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_add245_CAST_store
solver.Add( + (1)*main_add245_double + (1)*main_add245_CAST_store_float + (-1)*C8_main_add245_CAST_store<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_add245_CAST_store
solver.Add( + (1)*main_u_fixp + (-1)*main_add245_CAST_store_fixp==0)    #fix equality
solver.Add( + (1)*main_u_float + (-1)*main_add245_CAST_store_float==0)    #float equality
solver.Add( + (1)*main_u_double + (-1)*main_add245_CAST_store_double==0)    #double equality
solver.Add( + (1)*main_u_fixbits + (-1)*main_add245_CAST_store_fixbits==0)    #same fractional bit


#Restriction for new enob [STORE]
main_u_enob_storeENOB = solver.IntVar(-10000, 10000, 'main_u_enob_storeENOB')
solver.Add( + (1)*main_u_enob_storeENOB + (-1)*main_u_fixbits + (10000)*main_u_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_u_enob_storeENOB + (10000)*main_u_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_u_enob_storeENOB + (10000)*main_u_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_u_enob_storeENOB + (-1)*main_add245_enob<=0)    #Enob constraint ENOB propagation in load/store



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp20 + (-1)*main_u_enob_storeENOB + (10000)*main_main_tmp20_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp22 + (-1)*main_u_enob_storeENOB + (10000)*main_main_tmp22_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp24 + (-1)*main_u_enob_storeENOB + (10000)*main_main_tmp24_enob_4<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp40 + (-1)*main_u_enob_storeENOB + (10000)*main_main_tmp40_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp42 + (-1)*main_u_enob_storeENOB + (10000)*main_main_tmp42_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_v_enob_memphi_main_tmp44 + (-1)*main_u_enob_storeENOB + (10000)*main_main_tmp44_enob_2<=10000)    #Enob: forcing MEM phi enob

#Restriction for new enob [LOAD]
main_u_enob_memphi_main_tmp56 = solver.IntVar(-10000, 10000, 'main_u_enob_memphi_main_tmp56')
solver.Add( + (1)*main_u_enob_memphi_main_tmp56 + (-1)*main_u_enob<=0)    #Enob constraint, new enob at most original variable enob
main_main_tmp56_enob_0 = solver.IntVar(0, 1, 'main_main_tmp56_enob_0')
main_main_tmp56_enob_2 = solver.IntVar(0, 1, 'main_main_tmp56_enob_2')
main_main_tmp56_enob_4 = solver.IntVar(0, 1, 'main_main_tmp56_enob_4')
solver.Add( + (1)*main_main_tmp56_enob_0 + (1)*main_main_tmp56_enob_2 + (1)*main_main_tmp56_enob_4==1)    #Enob: one selected constraint



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp56 + (-1)*f_enob_storeENOB + (10000)*main_main_tmp56_enob_0<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp56 + (-1)*main_v_enob_storeENOB + (10000)*main_main_tmp56_enob_2<=10000)    #Enob: forcing MEM phi enob



#Closing MEM phi loop...
solver.Add( + (1)*main_u_enob_memphi_main_tmp56 + (-1)*main_u_enob_storeENOB + (10000)*main_main_tmp56_enob_4<=10000)    #Enob: forcing MEM phi enob



#Constraint for cast for   %call275 = call i32 (%struct._IO_FILE*, i8*, ...) @fprintf(%struct._IO_FILE* %tmp55, i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.7, i32 0, i32 0), double %tmp56), !taffo.info !33, !taffo.initweight !51, !taffo.constinfo !154
main_u_CAST_call275_fixbits = solver.IntVar(0, 28, 'main_u_CAST_call275_fixbits')
main_u_CAST_call275_fixp = solver.IntVar(0, 1, 'main_u_CAST_call275_fixp')
main_u_CAST_call275_float = solver.IntVar(0, 1, 'main_u_CAST_call275_float')
main_u_CAST_call275_double = solver.IntVar(0, 1, 'main_u_CAST_call275_double')
solver.Add( + (1)*main_u_CAST_call275_fixp + (1)*main_u_CAST_call275_float + (1)*main_u_CAST_call275_double==1)    #exactly 1 type
solver.Add( + (1)*main_u_CAST_call275_fixbits + (-10000)*main_u_CAST_call275_fixp<=0)    #If no fix, fix frac part = 0
C1_main_u_CAST_call275 = solver.IntVar(0, 1, 'C1_main_u_CAST_call275')
C2_main_u_CAST_call275 = solver.IntVar(0, 1, 'C2_main_u_CAST_call275')
solver.Add( + (1)*main_u_fixbits + (-1)*main_u_CAST_call275_fixbits + (-10000)*C1_main_u_CAST_call275<=0)    #Shift cost 1
solver.Add( + (-1)*main_u_fixbits + (1)*main_u_CAST_call275_fixbits + (-10000)*C2_main_u_CAST_call275<=0)    #Shift cost 2
castCostObj +=  + (1)*C1_main_u_CAST_call275
castCostObj +=  + (1)*C2_main_u_CAST_call275
C3_main_u_CAST_call275 = solver.IntVar(0, 1, 'C3_main_u_CAST_call275')
C4_main_u_CAST_call275 = solver.IntVar(0, 1, 'C4_main_u_CAST_call275')
C5_main_u_CAST_call275 = solver.IntVar(0, 1, 'C5_main_u_CAST_call275')
C6_main_u_CAST_call275 = solver.IntVar(0, 1, 'C6_main_u_CAST_call275')
C7_main_u_CAST_call275 = solver.IntVar(0, 1, 'C7_main_u_CAST_call275')
C8_main_u_CAST_call275 = solver.IntVar(0, 1, 'C8_main_u_CAST_call275')
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_call275_float + (-1)*C3_main_u_CAST_call275<=1)    #Fix to float
castCostObj +=  + (6.25227)*C3_main_u_CAST_call275
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_call275_fixp + (-1)*C4_main_u_CAST_call275<=1)    #Float to fix
castCostObj +=  + (1.47246)*C4_main_u_CAST_call275
solver.Add( + (1)*main_u_fixp + (1)*main_u_CAST_call275_double + (-1)*C5_main_u_CAST_call275<=1)    #Fix to double
castCostObj +=  + (11.6207)*C5_main_u_CAST_call275
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_call275_fixp + (-1)*C6_main_u_CAST_call275<=1)    #Double to fix
castCostObj +=  + (15.9217)*C6_main_u_CAST_call275
solver.Add( + (1)*main_u_float + (1)*main_u_CAST_call275_double + (-1)*C7_main_u_CAST_call275<=1)    #Float to double
castCostObj +=  + (4.48696)*C7_main_u_CAST_call275
solver.Add( + (1)*main_u_double + (1)*main_u_CAST_call275_float + (-1)*C8_main_u_CAST_call275<=1)    #Double to float
castCostObj +=  + (5.30435)*C8_main_u_CAST_call275
solver.Add( + (1)*main_u_CAST_call275_double==1)    #Type constraint for argument value





#All the model has been generated, lets solve it!
solver.Minimize(10000 * castCostObj / 2069.83+ 1 * enobCostObj / 70988+ 10000 * mathCostObj / 487.386)

# Model declaration end.