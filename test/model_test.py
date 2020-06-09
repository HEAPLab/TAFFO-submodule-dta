a_fixbits = solver.IntVar(0, 31, 'a_fixbits')
a_fixp = solver.IntVar(0, 1, 'a_fixp')
a_float = solver.IntVar(0, 1, 'a_float')
a_double = solver.IntVar(0, 1, 'a_double')
a_enob = solver.IntVar(-10000, 10000, 'a_enob')
solver.Add( + (1)*a_enob + (-1)*a_fixbits + (10000)*a_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*a_enob + (10000)*a_float<=10027)    #Enob constraint for float
solver.Add( + (1)*a_enob + (10000)*a_double<=10056)    #Enob constraint for double
solver.Add( + (1)*a_fixp + (1)*a_float + (1)*a_double==1)    #Exactly one selected type
solver.Add( + (1)*a_fixbits + (-10000)*a_fixp<=0)    #If not fix, frac part to zero
b_fixbits = solver.IntVar(0, 31, 'b_fixbits')
b_fixp = solver.IntVar(0, 1, 'b_fixp')
b_float = solver.IntVar(0, 1, 'b_float')
b_double = solver.IntVar(0, 1, 'b_double')
b_enob = solver.IntVar(-10000, 10000, 'b_enob')
solver.Add( + (1)*b_enob + (-1)*b_fixbits + (10000)*b_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*b_enob + (10000)*b_float<=10027)    #Enob constraint for float
solver.Add( + (1)*b_enob + (10000)*b_double<=10056)    #Enob constraint for double
solver.Add( + (1)*b_fixp + (1)*b_float + (1)*b_double==1)    #Exactly one selected type
solver.Add( + (1)*b_fixbits + (-10000)*b_fixp<=0)    #If not fix, frac part to zero
e_fixbits = solver.IntVar(0, 30, 'e_fixbits')
e_fixp = solver.IntVar(0, 1, 'e_fixp')
e_float = solver.IntVar(0, 1, 'e_float')
e_double = solver.IntVar(0, 1, 'e_double')
e_enob = solver.IntVar(-10000, 10000, 'e_enob')
solver.Add( + (1)*e_enob + (-1)*e_fixbits + (10000)*e_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*e_enob + (10000)*e_float<=10027)    #Enob constraint for float
solver.Add( + (1)*e_enob + (10000)*e_double<=10056)    #Enob constraint for double
solver.Add( + (1)*e_fixp + (1)*e_float + (1)*e_double==1)    #Exactly one selected type
solver.Add( + (1)*e_fixbits + (-10000)*e_fixp<=0)    #If not fix, frac part to zero
c_fixbits = solver.IntVar(0, 18, 'c_fixbits')
c_fixp = solver.IntVar(0, 1, 'c_fixp')
c_float = solver.IntVar(0, 1, 'c_float')
c_double = solver.IntVar(0, 1, 'c_double')
c_enob = solver.IntVar(-10000, 10000, 'c_enob')
solver.Add( + (1)*c_enob + (-1)*c_fixbits + (10000)*c_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*c_enob + (10000)*c_float<=10027)    #Enob constraint for float
solver.Add( + (1)*c_enob + (10000)*c_double<=10056)    #Enob constraint for double
solver.Add( + (1)*c_fixp + (1)*c_float + (1)*c_double==1)    #Exactly one selected type
solver.Add( + (1)*c_fixbits + (-10000)*c_fixp<=0)    #If not fix, frac part to zero
d_fixbits = solver.IntVar(0, 18, 'd_fixbits')
d_fixp = solver.IntVar(0, 1, 'd_fixp')
d_float = solver.IntVar(0, 1, 'd_float')
d_double = solver.IntVar(0, 1, 'd_double')
d_enob = solver.IntVar(-10000, 10000, 'd_enob')
solver.Add( + (1)*d_enob + (-1)*d_fixbits + (10000)*d_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*d_enob + (10000)*d_float<=10027)    #Enob constraint for float
solver.Add( + (1)*d_enob + (10000)*d_double<=10056)    #Enob constraint for double
solver.Add( + (1)*d_fixp + (1)*d_float + (1)*d_double==1)    #Exactly one selected type
solver.Add( + (1)*d_fixbits + (-10000)*d_fixp<=0)    #If not fix, frac part to zero
f_fixbits = solver.IntVar(0, 17, 'f_fixbits')
f_fixp = solver.IntVar(0, 1, 'f_fixp')
f_float = solver.IntVar(0, 1, 'f_float')
f_double = solver.IntVar(0, 1, 'f_double')
f_enob = solver.IntVar(-10000, 10000, 'f_enob')
solver.Add( + (1)*f_enob + (-1)*f_fixbits + (10000)*f_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*f_enob + (10000)*f_float<=10027)    #Enob constraint for float
solver.Add( + (1)*f_enob + (10000)*f_double<=10056)    #Enob constraint for double
solver.Add( + (1)*f_fixp + (1)*f_float + (1)*f_double==1)    #Exactly one selected type
solver.Add( + (1)*f_fixbits + (-10000)*f_fixp<=0)    #If not fix, frac part to zero
g_fixbits = solver.IntVar(0, 17, 'g_fixbits')
g_fixp = solver.IntVar(0, 1, 'g_fixp')
g_float = solver.IntVar(0, 1, 'g_float')
g_double = solver.IntVar(0, 1, 'g_double')
g_enob = solver.IntVar(-10000, 10000, 'g_enob')
solver.Add( + (1)*g_enob + (-1)*g_fixbits + (10000)*g_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*g_enob + (10000)*g_float<=10027)    #Enob constraint for float
solver.Add( + (1)*g_enob + (10000)*g_double<=10056)    #Enob constraint for double
solver.Add( + (1)*g_fixp + (1)*g_float + (1)*g_double==1)    #Exactly one selected type
solver.Add( + (1)*g_fixbits + (-10000)*g_fixp<=0)    #If not fix, frac part to zero
a_add_fixbits = solver.IntVar(0, 31, 'a_add_fixbits')
a_add_fixp = solver.IntVar(0, 1, 'a_add_fixp')
a_add_float = solver.IntVar(0, 1, 'a_add_float')
a_add_double = solver.IntVar(0, 1, 'a_add_double')
a_add_enob = solver.IntVar(-10000, 10000, 'a_add_enob')
solver.Add( + (1)*a_add_fixp + (1)*a_add_float + (1)*a_add_double==1)    #exactly 1 type
solver.Add( + (-1)*a_enob + (1)*a_add_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*a_add_fixbits + (-10000)*a_add_fixp<=0)    #If no fix, fix frac part = 0
C1_a_add = solver.IntVar(0, 1, 'C1_a_add')
C2_a_add = solver.IntVar(0, 1, 'C2_a_add')
solver.Add( + (1)*a_fixbits + (-1)*a_add_fixbits + (-10000)*C1_a_add<=0)    #Shift cost 1
solver.Add( + (-1)*a_fixbits + (1)*a_add_fixbits + (-10000)*C2_a_add<=0)    #Shift cost 2
C3_a_add = solver.IntVar(0, 1, 'C3_a_add')
C4_a_add = solver.IntVar(0, 1, 'C4_a_add')
C5_a_add = solver.IntVar(0, 1, 'C5_a_add')
C6_a_add = solver.IntVar(0, 1, 'C6_a_add')
C7_a_add = solver.IntVar(0, 1, 'C7_a_add')
C8_a_add = solver.IntVar(0, 1, 'C8_a_add')
solver.Add( + (1)*a_fixp + (1)*a_add_float + (-1)*C3_a_add<=1)    #Fix to float
solver.Add( + (1)*a_float + (1)*a_add_fixp + (-1)*C4_a_add<=1)    #Float to fix
solver.Add( + (1)*a_fixp + (1)*a_add_double + (-1)*C5_a_add<=1)    #Fix to double
solver.Add( + (1)*a_double + (1)*a_add_fixp + (-1)*C6_a_add<=1)    #Double to fix
solver.Add( + (1)*a_float + (1)*a_add_double + (-1)*C7_a_add<=1)    #Float to double
solver.Add( + (1)*a_double + (1)*a_add_float + (-1)*C8_a_add<=1)    #Double to float
b_add_fixbits = solver.IntVar(0, 31, 'b_add_fixbits')
b_add_fixp = solver.IntVar(0, 1, 'b_add_fixp')
b_add_float = solver.IntVar(0, 1, 'b_add_float')
b_add_double = solver.IntVar(0, 1, 'b_add_double')
b_add_enob = solver.IntVar(-10000, 10000, 'b_add_enob')
solver.Add( + (1)*b_add_fixp + (1)*b_add_float + (1)*b_add_double==1)    #exactly 1 type
solver.Add( + (-1)*b_enob + (1)*b_add_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*b_add_fixbits + (-10000)*b_add_fixp<=0)    #If no fix, fix frac part = 0
C1_b_add = solver.IntVar(0, 1, 'C1_b_add')
C2_b_add = solver.IntVar(0, 1, 'C2_b_add')
solver.Add( + (1)*b_fixbits + (-1)*b_add_fixbits + (-10000)*C1_b_add<=0)    #Shift cost 1
solver.Add( + (-1)*b_fixbits + (1)*b_add_fixbits + (-10000)*C2_b_add<=0)    #Shift cost 2
C3_b_add = solver.IntVar(0, 1, 'C3_b_add')
C4_b_add = solver.IntVar(0, 1, 'C4_b_add')
C5_b_add = solver.IntVar(0, 1, 'C5_b_add')
C6_b_add = solver.IntVar(0, 1, 'C6_b_add')
C7_b_add = solver.IntVar(0, 1, 'C7_b_add')
C8_b_add = solver.IntVar(0, 1, 'C8_b_add')
solver.Add( + (1)*b_fixp + (1)*b_add_float + (-1)*C3_b_add<=1)    #Fix to float
solver.Add( + (1)*b_float + (1)*b_add_fixp + (-1)*C4_b_add<=1)    #Float to fix
solver.Add( + (1)*b_fixp + (1)*b_add_double + (-1)*C5_b_add<=1)    #Fix to double
solver.Add( + (1)*b_double + (1)*b_add_fixp + (-1)*C6_b_add<=1)    #Double to fix
solver.Add( + (1)*b_float + (1)*b_add_double + (-1)*C7_b_add<=1)    #Float to double
solver.Add( + (1)*b_double + (1)*b_add_float + (-1)*C8_b_add<=1)    #Double to float
main_add_fixbits = solver.IntVar(0, 31, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
main_add_enob = solver.IntVar(-10000, 10000, 'main_add_enob')
solver.Add( + (1)*main_add_enob + (-1)*main_add_fixbits + (10000)*main_add_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add_enob + (10000)*main_add_float<=10027)    #Enob constraint for float
solver.Add( + (1)*main_add_enob + (10000)*main_add_double<=10056)    #Enob constraint for double
solver.Add( + (1)*main_add_fixp + (1)*main_add_float + (1)*main_add_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*a_add_fixp + (-1)*b_add_fixp==0)    #fix equality
solver.Add( + (1)*a_add_float + (-1)*b_add_float==0)    #float equality
solver.Add( + (1)*a_add_double + (-1)*b_add_double==0)    #double equality
solver.Add( + (1)*a_add_fixbits + (-1)*b_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*a_add_fixp + (-1)*main_add_fixp==0)    #fix equality
solver.Add( + (1)*a_add_float + (-1)*main_add_float==0)    #float equality
solver.Add( + (1)*a_add_double + (-1)*main_add_double==0)    #double equality
solver.Add( + (1)*a_add_fixbits + (-1)*main_add_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add_enob + (-1)*a_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add_enob + (-1)*b_enob<=0)    #Enob propagation in sum second addend
main_add__fixbits = solver.IntVar(0, 31, 'main_add__fixbits')
main_add__fixp = solver.IntVar(0, 1, 'main_add__fixp')
main_add__float = solver.IntVar(0, 1, 'main_add__float')
main_add__double = solver.IntVar(0, 1, 'main_add__double')
main_add__enob = solver.IntVar(-10000, 10000, 'main_add__enob')
solver.Add( + (1)*main_add__fixp + (1)*main_add__float + (1)*main_add__double==1)    #exactly 1 type
solver.Add( + (-1)*main_add_enob + (1)*main_add__enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*main_add__fixbits + (-10000)*main_add__fixp<=0)    #If no fix, fix frac part = 0
C1_main_add_ = solver.IntVar(0, 1, 'C1_main_add_')
C2_main_add_ = solver.IntVar(0, 1, 'C2_main_add_')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add__fixbits + (-10000)*C1_main_add_<=0)    #Shift cost 1
solver.Add( + (-1)*main_add_fixbits + (1)*main_add__fixbits + (-10000)*C2_main_add_<=0)    #Shift cost 2
C3_main_add_ = solver.IntVar(0, 1, 'C3_main_add_')
C4_main_add_ = solver.IntVar(0, 1, 'C4_main_add_')
C5_main_add_ = solver.IntVar(0, 1, 'C5_main_add_')
C6_main_add_ = solver.IntVar(0, 1, 'C6_main_add_')
C7_main_add_ = solver.IntVar(0, 1, 'C7_main_add_')
C8_main_add_ = solver.IntVar(0, 1, 'C8_main_add_')
solver.Add( + (1)*main_add_fixp + (1)*main_add__float + (-1)*C3_main_add_<=1)    #Fix to float
solver.Add( + (1)*main_add_float + (1)*main_add__fixp + (-1)*C4_main_add_<=1)    #Float to fix
solver.Add( + (1)*main_add_fixp + (1)*main_add__double + (-1)*C5_main_add_<=1)    #Fix to double
solver.Add( + (1)*main_add_double + (1)*main_add__fixp + (-1)*C6_main_add_<=1)    #Double to fix
solver.Add( + (1)*main_add_float + (1)*main_add__double + (-1)*C7_main_add_<=1)    #Float to double
solver.Add( + (1)*main_add_double + (1)*main_add__float + (-1)*C8_main_add_<=1)    #Double to float
solver.Add( + (1)*e_fixp + (-1)*main_add__fixp==0)    #fix equality
solver.Add( + (1)*e_float + (-1)*main_add__float==0)    #float equality
solver.Add( + (1)*e_double + (-1)*main_add__double==0)    #double equality
solver.Add( + (1)*e_fixbits + (-1)*main_add__fixbits==0)    #same fractional bit
c_add1_fixbits = solver.IntVar(0, 18, 'c_add1_fixbits')
c_add1_fixp = solver.IntVar(0, 1, 'c_add1_fixp')
c_add1_float = solver.IntVar(0, 1, 'c_add1_float')
c_add1_double = solver.IntVar(0, 1, 'c_add1_double')
c_add1_enob = solver.IntVar(-10000, 10000, 'c_add1_enob')
solver.Add( + (1)*c_add1_fixp + (1)*c_add1_float + (1)*c_add1_double==1)    #exactly 1 type
solver.Add( + (-1)*c_enob + (1)*c_add1_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*c_add1_fixbits + (-10000)*c_add1_fixp<=0)    #If no fix, fix frac part = 0
C1_c_add1 = solver.IntVar(0, 1, 'C1_c_add1')
C2_c_add1 = solver.IntVar(0, 1, 'C2_c_add1')
solver.Add( + (1)*c_fixbits + (-1)*c_add1_fixbits + (-10000)*C1_c_add1<=0)    #Shift cost 1
solver.Add( + (-1)*c_fixbits + (1)*c_add1_fixbits + (-10000)*C2_c_add1<=0)    #Shift cost 2
C3_c_add1 = solver.IntVar(0, 1, 'C3_c_add1')
C4_c_add1 = solver.IntVar(0, 1, 'C4_c_add1')
C5_c_add1 = solver.IntVar(0, 1, 'C5_c_add1')
C6_c_add1 = solver.IntVar(0, 1, 'C6_c_add1')
C7_c_add1 = solver.IntVar(0, 1, 'C7_c_add1')
C8_c_add1 = solver.IntVar(0, 1, 'C8_c_add1')
solver.Add( + (1)*c_fixp + (1)*c_add1_float + (-1)*C3_c_add1<=1)    #Fix to float
solver.Add( + (1)*c_float + (1)*c_add1_fixp + (-1)*C4_c_add1<=1)    #Float to fix
solver.Add( + (1)*c_fixp + (1)*c_add1_double + (-1)*C5_c_add1<=1)    #Fix to double
solver.Add( + (1)*c_double + (1)*c_add1_fixp + (-1)*C6_c_add1<=1)    #Double to fix
solver.Add( + (1)*c_float + (1)*c_add1_double + (-1)*C7_c_add1<=1)    #Float to double
solver.Add( + (1)*c_double + (1)*c_add1_float + (-1)*C8_c_add1<=1)    #Double to float
d_add1_fixbits = solver.IntVar(0, 18, 'd_add1_fixbits')
d_add1_fixp = solver.IntVar(0, 1, 'd_add1_fixp')
d_add1_float = solver.IntVar(0, 1, 'd_add1_float')
d_add1_double = solver.IntVar(0, 1, 'd_add1_double')
d_add1_enob = solver.IntVar(-10000, 10000, 'd_add1_enob')
solver.Add( + (1)*d_add1_fixp + (1)*d_add1_float + (1)*d_add1_double==1)    #exactly 1 type
solver.Add( + (-1)*d_enob + (1)*d_add1_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*d_add1_fixbits + (-10000)*d_add1_fixp<=0)    #If no fix, fix frac part = 0
C1_d_add1 = solver.IntVar(0, 1, 'C1_d_add1')
C2_d_add1 = solver.IntVar(0, 1, 'C2_d_add1')
solver.Add( + (1)*d_fixbits + (-1)*d_add1_fixbits + (-10000)*C1_d_add1<=0)    #Shift cost 1
solver.Add( + (-1)*d_fixbits + (1)*d_add1_fixbits + (-10000)*C2_d_add1<=0)    #Shift cost 2
C3_d_add1 = solver.IntVar(0, 1, 'C3_d_add1')
C4_d_add1 = solver.IntVar(0, 1, 'C4_d_add1')
C5_d_add1 = solver.IntVar(0, 1, 'C5_d_add1')
C6_d_add1 = solver.IntVar(0, 1, 'C6_d_add1')
C7_d_add1 = solver.IntVar(0, 1, 'C7_d_add1')
C8_d_add1 = solver.IntVar(0, 1, 'C8_d_add1')
solver.Add( + (1)*d_fixp + (1)*d_add1_float + (-1)*C3_d_add1<=1)    #Fix to float
solver.Add( + (1)*d_float + (1)*d_add1_fixp + (-1)*C4_d_add1<=1)    #Float to fix
solver.Add( + (1)*d_fixp + (1)*d_add1_double + (-1)*C5_d_add1<=1)    #Fix to double
solver.Add( + (1)*d_double + (1)*d_add1_fixp + (-1)*C6_d_add1<=1)    #Double to fix
solver.Add( + (1)*d_float + (1)*d_add1_double + (-1)*C7_d_add1<=1)    #Float to double
solver.Add( + (1)*d_double + (1)*d_add1_float + (-1)*C8_d_add1<=1)    #Double to float
main_add1_fixbits = solver.IntVar(0, 18, 'main_add1_fixbits')
main_add1_fixp = solver.IntVar(0, 1, 'main_add1_fixp')
main_add1_float = solver.IntVar(0, 1, 'main_add1_float')
main_add1_double = solver.IntVar(0, 1, 'main_add1_double')
main_add1_enob = solver.IntVar(-10000, 10000, 'main_add1_enob')
solver.Add( + (1)*main_add1_enob + (-1)*main_add1_fixbits + (10000)*main_add1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_add1_enob + (10000)*main_add1_float<=10027)    #Enob constraint for float
solver.Add( + (1)*main_add1_enob + (10000)*main_add1_double<=10056)    #Enob constraint for double
solver.Add( + (1)*main_add1_fixp + (1)*main_add1_float + (1)*main_add1_double==1)    #Exactly one selected type
solver.Add( + (1)*main_add1_fixbits + (-10000)*main_add1_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*c_add1_fixp + (-1)*d_add1_fixp==0)    #fix equality
solver.Add( + (1)*c_add1_float + (-1)*d_add1_float==0)    #float equality
solver.Add( + (1)*c_add1_double + (-1)*d_add1_double==0)    #double equality
solver.Add( + (1)*c_add1_fixbits + (-1)*d_add1_fixbits==0)    #same fractional bit
solver.Add( + (1)*c_add1_fixp + (-1)*main_add1_fixp==0)    #fix equality
solver.Add( + (1)*c_add1_float + (-1)*main_add1_float==0)    #float equality
solver.Add( + (1)*c_add1_double + (-1)*main_add1_double==0)    #double equality
solver.Add( + (1)*c_add1_fixbits + (-1)*main_add1_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_add1_enob + (-1)*c_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_add1_enob + (-1)*d_enob<=0)    #Enob propagation in sum second addend
main_add1__fixbits = solver.IntVar(0, 18, 'main_add1__fixbits')
main_add1__fixp = solver.IntVar(0, 1, 'main_add1__fixp')
main_add1__float = solver.IntVar(0, 1, 'main_add1__float')
main_add1__double = solver.IntVar(0, 1, 'main_add1__double')
main_add1__enob = solver.IntVar(-10000, 10000, 'main_add1__enob')
solver.Add( + (1)*main_add1__fixp + (1)*main_add1__float + (1)*main_add1__double==1)    #exactly 1 type
solver.Add( + (-1)*main_add1_enob + (1)*main_add1__enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*main_add1__fixbits + (-10000)*main_add1__fixp<=0)    #If no fix, fix frac part = 0
C1_main_add1_ = solver.IntVar(0, 1, 'C1_main_add1_')
C2_main_add1_ = solver.IntVar(0, 1, 'C2_main_add1_')
solver.Add( + (1)*main_add1_fixbits + (-1)*main_add1__fixbits + (-10000)*C1_main_add1_<=0)    #Shift cost 1
solver.Add( + (-1)*main_add1_fixbits + (1)*main_add1__fixbits + (-10000)*C2_main_add1_<=0)    #Shift cost 2
C3_main_add1_ = solver.IntVar(0, 1, 'C3_main_add1_')
C4_main_add1_ = solver.IntVar(0, 1, 'C4_main_add1_')
C5_main_add1_ = solver.IntVar(0, 1, 'C5_main_add1_')
C6_main_add1_ = solver.IntVar(0, 1, 'C6_main_add1_')
C7_main_add1_ = solver.IntVar(0, 1, 'C7_main_add1_')
C8_main_add1_ = solver.IntVar(0, 1, 'C8_main_add1_')
solver.Add( + (1)*main_add1_fixp + (1)*main_add1__float + (-1)*C3_main_add1_<=1)    #Fix to float
solver.Add( + (1)*main_add1_float + (1)*main_add1__fixp + (-1)*C4_main_add1_<=1)    #Float to fix
solver.Add( + (1)*main_add1_fixp + (1)*main_add1__double + (-1)*C5_main_add1_<=1)    #Fix to double
solver.Add( + (1)*main_add1_double + (1)*main_add1__fixp + (-1)*C6_main_add1_<=1)    #Double to fix
solver.Add( + (1)*main_add1_float + (1)*main_add1__double + (-1)*C7_main_add1_<=1)    #Float to double
solver.Add( + (1)*main_add1_double + (1)*main_add1__float + (-1)*C8_main_add1_<=1)    #Double to float
solver.Add( + (1)*f_fixp + (-1)*main_add1__fixp==0)    #fix equality
solver.Add( + (1)*f_float + (-1)*main_add1__float==0)    #float equality
solver.Add( + (1)*f_double + (-1)*main_add1__double==0)    #double equality
solver.Add( + (1)*f_fixbits + (-1)*main_add1__fixbits==0)    #same fractional bit
f_mul_fixbits = solver.IntVar(0, 17, 'f_mul_fixbits')
f_mul_fixp = solver.IntVar(0, 1, 'f_mul_fixp')
f_mul_float = solver.IntVar(0, 1, 'f_mul_float')
f_mul_double = solver.IntVar(0, 1, 'f_mul_double')
f_mul_enob = solver.IntVar(-10000, 10000, 'f_mul_enob')
solver.Add( + (1)*f_mul_fixp + (1)*f_mul_float + (1)*f_mul_double==1)    #exactly 1 type
solver.Add( + (-1)*f_enob + (1)*f_mul_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*f_mul_fixbits + (-10000)*f_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_f_mul = solver.IntVar(0, 1, 'C1_f_mul')
C2_f_mul = solver.IntVar(0, 1, 'C2_f_mul')
solver.Add( + (1)*f_fixbits + (-1)*f_mul_fixbits + (-10000)*C1_f_mul<=0)    #Shift cost 1
solver.Add( + (-1)*f_fixbits + (1)*f_mul_fixbits + (-10000)*C2_f_mul<=0)    #Shift cost 2
C3_f_mul = solver.IntVar(0, 1, 'C3_f_mul')
C4_f_mul = solver.IntVar(0, 1, 'C4_f_mul')
C5_f_mul = solver.IntVar(0, 1, 'C5_f_mul')
C6_f_mul = solver.IntVar(0, 1, 'C6_f_mul')
C7_f_mul = solver.IntVar(0, 1, 'C7_f_mul')
C8_f_mul = solver.IntVar(0, 1, 'C8_f_mul')
solver.Add( + (1)*f_fixp + (1)*f_mul_float + (-1)*C3_f_mul<=1)    #Fix to float
solver.Add( + (1)*f_float + (1)*f_mul_fixp + (-1)*C4_f_mul<=1)    #Float to fix
solver.Add( + (1)*f_fixp + (1)*f_mul_double + (-1)*C5_f_mul<=1)    #Fix to double
solver.Add( + (1)*f_double + (1)*f_mul_fixp + (-1)*C6_f_mul<=1)    #Double to fix
solver.Add( + (1)*f_float + (1)*f_mul_double + (-1)*C7_f_mul<=1)    #Float to double
solver.Add( + (1)*f_double + (1)*f_mul_float + (-1)*C8_f_mul<=1)    #Double to float
e_mul_fixbits = solver.IntVar(0, 30, 'e_mul_fixbits')
e_mul_fixp = solver.IntVar(0, 1, 'e_mul_fixp')
e_mul_float = solver.IntVar(0, 1, 'e_mul_float')
e_mul_double = solver.IntVar(0, 1, 'e_mul_double')
e_mul_enob = solver.IntVar(-10000, 10000, 'e_mul_enob')
solver.Add( + (1)*e_mul_fixp + (1)*e_mul_float + (1)*e_mul_double==1)    #exactly 1 type
solver.Add( + (-1)*e_enob + (1)*e_mul_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*e_mul_fixbits + (-10000)*e_mul_fixp<=0)    #If no fix, fix frac part = 0
C1_e_mul = solver.IntVar(0, 1, 'C1_e_mul')
C2_e_mul = solver.IntVar(0, 1, 'C2_e_mul')
solver.Add( + (1)*e_fixbits + (-1)*e_mul_fixbits + (-10000)*C1_e_mul<=0)    #Shift cost 1
solver.Add( + (-1)*e_fixbits + (1)*e_mul_fixbits + (-10000)*C2_e_mul<=0)    #Shift cost 2
C3_e_mul = solver.IntVar(0, 1, 'C3_e_mul')
C4_e_mul = solver.IntVar(0, 1, 'C4_e_mul')
C5_e_mul = solver.IntVar(0, 1, 'C5_e_mul')
C6_e_mul = solver.IntVar(0, 1, 'C6_e_mul')
C7_e_mul = solver.IntVar(0, 1, 'C7_e_mul')
C8_e_mul = solver.IntVar(0, 1, 'C8_e_mul')
solver.Add( + (1)*e_fixp + (1)*e_mul_float + (-1)*C3_e_mul<=1)    #Fix to float
solver.Add( + (1)*e_float + (1)*e_mul_fixp + (-1)*C4_e_mul<=1)    #Float to fix
solver.Add( + (1)*e_fixp + (1)*e_mul_double + (-1)*C5_e_mul<=1)    #Fix to double
solver.Add( + (1)*e_double + (1)*e_mul_fixp + (-1)*C6_e_mul<=1)    #Double to fix
solver.Add( + (1)*e_float + (1)*e_mul_double + (-1)*C7_e_mul<=1)    #Float to double
solver.Add( + (1)*e_double + (1)*e_mul_float + (-1)*C8_e_mul<=1)    #Double to float
main_mul_fixbits = solver.IntVar(0, 30, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
main_mul_enob = solver.IntVar(-10000, 10000, 'main_mul_enob')
solver.Add( + (1)*main_mul_enob + (-1)*main_mul_fixbits + (10000)*main_mul_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_float<=10027)    #Enob constraint for float
solver.Add( + (1)*main_mul_enob + (10000)*main_mul_double<=10056)    #Enob constraint for double
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)    #Exactly one selected type
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)    #If not fix, frac part to zero
solver.Add( + (1)*f_mul_fixp + (-1)*e_mul_fixp==0)    #fix equality
solver.Add( + (1)*f_mul_float + (-1)*e_mul_float==0)    #float equality
solver.Add( + (1)*f_mul_double + (-1)*e_mul_double==0)    #double equality
solver.Add( + (1)*f_mul_fixp + (-1)*main_mul_fixp==0)    #fix equality
solver.Add( + (1)*f_mul_float + (-1)*main_mul_float==0)    #float equality
solver.Add( + (1)*f_mul_double + (-1)*main_mul_double==0)    #double equality
solver.Add( + (1)*main_mul_enob + (-1)*f_enob + (-1)*e_enob<=0)    #Enob propagation in product
main_mul__fixbits = solver.IntVar(0, 30, 'main_mul__fixbits')
main_mul__fixp = solver.IntVar(0, 1, 'main_mul__fixp')
main_mul__float = solver.IntVar(0, 1, 'main_mul__float')
main_mul__double = solver.IntVar(0, 1, 'main_mul__double')
main_mul__enob = solver.IntVar(-10000, 10000, 'main_mul__enob')
solver.Add( + (1)*main_mul__fixp + (1)*main_mul__float + (1)*main_mul__double==1)    #exactly 1 type
solver.Add( + (-1)*main_mul_enob + (1)*main_mul__enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*main_mul__fixbits + (-10000)*main_mul__fixp<=0)    #If no fix, fix frac part = 0
C1_main_mul_ = solver.IntVar(0, 1, 'C1_main_mul_')
C2_main_mul_ = solver.IntVar(0, 1, 'C2_main_mul_')
solver.Add( + (1)*main_mul_fixbits + (-1)*main_mul__fixbits + (-10000)*C1_main_mul_<=0)    #Shift cost 1
solver.Add( + (-1)*main_mul_fixbits + (1)*main_mul__fixbits + (-10000)*C2_main_mul_<=0)    #Shift cost 2
C3_main_mul_ = solver.IntVar(0, 1, 'C3_main_mul_')
C4_main_mul_ = solver.IntVar(0, 1, 'C4_main_mul_')
C5_main_mul_ = solver.IntVar(0, 1, 'C5_main_mul_')
C6_main_mul_ = solver.IntVar(0, 1, 'C6_main_mul_')
C7_main_mul_ = solver.IntVar(0, 1, 'C7_main_mul_')
C8_main_mul_ = solver.IntVar(0, 1, 'C8_main_mul_')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul__float + (-1)*C3_main_mul_<=1)    #Fix to float
solver.Add( + (1)*main_mul_float + (1)*main_mul__fixp + (-1)*C4_main_mul_<=1)    #Float to fix
solver.Add( + (1)*main_mul_fixp + (1)*main_mul__double + (-1)*C5_main_mul_<=1)    #Fix to double
solver.Add( + (1)*main_mul_double + (1)*main_mul__fixp + (-1)*C6_main_mul_<=1)    #Double to fix
solver.Add( + (1)*main_mul_float + (1)*main_mul__double + (-1)*C7_main_mul_<=1)    #Float to double
solver.Add( + (1)*main_mul_double + (1)*main_mul__float + (-1)*C8_main_mul_<=1)    #Double to float
solver.Add( + (1)*g_fixp + (-1)*main_mul__fixp==0)    #fix equality
solver.Add( + (1)*g_float + (-1)*main_mul__float==0)    #float equality
solver.Add( + (1)*g_double + (-1)*main_mul__double==0)    #double equality
solver.Add( + (1)*g_fixbits + (-1)*main_mul__fixbits==0)    #same fractional bit
solver.Minimize( + (-0.5)*a_enob + (-0.5)*b_enob + (-0.5)*e_enob + (-0.5)*c_enob + (-0.5)*d_enob + (-0.5)*f_enob + (-0.5)*g_enob + (5)*C1_a_add + (5)*C2_a_add + (10)*C3_a_add + (10)*C4_a_add + (10)*C5_a_add + (10)*C6_a_add + (10)*C7_a_add + (10)*C8_a_add + (5)*C1_b_add + (5)*C2_b_add + (10)*C3_b_add + (10)*C4_b_add + (10)*C5_b_add + (10)*C6_b_add + (10)*C7_b_add + (10)*C8_b_add + (-0.5)*main_add_enob + (10)*main_add_fixp + (40)*main_add_float + (60)*main_add_double + (5)*C1_main_add_ + (5)*C2_main_add_ + (10)*C3_main_add_ + (10)*C4_main_add_ + (10)*C5_main_add_ + (10)*C6_main_add_ + (10)*C7_main_add_ + (10)*C8_main_add_ + (5)*C1_c_add1 + (5)*C2_c_add1 + (10)*C3_c_add1 + (10)*C4_c_add1 + (10)*C5_c_add1 + (10)*C6_c_add1 + (10)*C7_c_add1 + (10)*C8_c_add1 + (5)*C1_d_add1 + (5)*C2_d_add1 + (10)*C3_d_add1 + (10)*C4_d_add1 + (10)*C5_d_add1 + (10)*C6_d_add1 + (10)*C7_d_add1 + (10)*C8_d_add1 + (-0.5)*main_add1_enob + (10)*main_add1_fixp + (40)*main_add1_float + (60)*main_add1_double + (5)*C1_main_add1_ + (5)*C2_main_add1_ + (10)*C3_main_add1_ + (10)*C4_main_add1_ + (10)*C5_main_add1_ + (10)*C6_main_add1_ + (10)*C7_main_add1_ + (10)*C8_main_add1_ + (5)*C1_f_mul + (5)*C2_f_mul + (10)*C3_f_mul + (10)*C4_f_mul + (10)*C5_f_mul + (10)*C6_f_mul + (10)*C7_f_mul + (10)*C8_f_mul + (5)*C1_e_mul + (5)*C2_e_mul + (10)*C3_e_mul + (10)*C4_e_mul + (10)*C5_e_mul + (10)*C6_e_mul + (10)*C7_e_mul + (10)*C8_e_mul + (-0.5)*main_mul_enob + (10)*main_mul_fixp + (60)*main_mul_float + (80)*main_mul_double + (5)*C1_main_mul_ + (5)*C2_main_mul_ + (10)*C3_main_mul_ + (10)*C4_main_mul_ + (10)*C5_main_mul_ + (10)*C6_main_mul_ + (10)*C7_main_mul_ + (10)*C8_main_mul_)

# Model declaration end.