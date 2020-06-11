main_a_0_fixbits = solver.IntVar(0, 29, 'main_a_0_fixbits')
main_a_0_fixp = solver.IntVar(0, 1, 'main_a_0_fixp')
main_a_0_float = solver.IntVar(0, 1, 'main_a_0_float')
main_a_0_double = solver.IntVar(0, 1, 'main_a_0_double')
main_a_0_enob = solver.IntVar(-10000, 10000, 'main_a_0_enob')
solver.Add( + (1)*main_a_0_enob + (-1)*main_a_0_fixbits + (10000)*main_a_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_a_0_enob + (10000)*main_a_0_float<=10021)    #Enob constraint for float
solver.Add( + (1)*main_a_0_enob + (10000)*main_a_0_double<=10050)    #Enob constraint for double
solver.Add( + (1)*main_a_0_fixp + (1)*main_a_0_float + (1)*main_a_0_double==1)    #Exactly one selected type
solver.Add( + (1)*main_a_0_fixbits + (-10000)*main_a_0_fixp<=0)    #If not fix, frac part to zero
a_0_enob_0 = solver.IntVar(0, 1, 'a_0_enob_0')
a_0_enob_1 = solver.IntVar(0, 1, 'a_0_enob_1')
solver.Add( + (1)*a_0_enob_0 + (1)*a_0_enob_1==1)    #Enob: one selected constraint
ConstantValue__fixbits = solver.IntVar(0, 29, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
ConstantValue__enob = solver.IntVar(-10000, 10000, 'ConstantValue__enob')
solver.Add( + (1)*ConstantValue__enob + (-1)*ConstantValue__fixbits + (10000)*ConstantValue__fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__float<=10021)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__enob + (10000)*ConstantValue__double<=10050)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)    #If not fix, frac part to zero
ConstantValue__a_0_fixbits = solver.IntVar(0, 29, 'ConstantValue__a_0_fixbits')
ConstantValue__a_0_fixp = solver.IntVar(0, 1, 'ConstantValue__a_0_fixp')
ConstantValue__a_0_float = solver.IntVar(0, 1, 'ConstantValue__a_0_float')
ConstantValue__a_0_double = solver.IntVar(0, 1, 'ConstantValue__a_0_double')
ConstantValue__a_0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__a_0_enob')
solver.Add( + (1)*ConstantValue__a_0_fixp + (1)*ConstantValue__a_0_float + (1)*ConstantValue__a_0_double==1)    #exactly 1 type
solver.Add( + (-1)*ConstantValue__enob + (1)*ConstantValue__a_0_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*ConstantValue__a_0_fixbits + (-10000)*ConstantValue__a_0_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__a_0 = solver.IntVar(0, 1, 'C1_ConstantValue__a_0')
C2_ConstantValue__a_0 = solver.IntVar(0, 1, 'C2_ConstantValue__a_0')
solver.Add( + (1)*ConstantValue__fixbits + (-1)*ConstantValue__a_0_fixbits + (-10000)*C1_ConstantValue__a_0<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__fixbits + (1)*ConstantValue__a_0_fixbits + (-10000)*C2_ConstantValue__a_0<=0)    #Shift cost 2
C3_ConstantValue__a_0 = solver.IntVar(0, 1, 'C3_ConstantValue__a_0')
C4_ConstantValue__a_0 = solver.IntVar(0, 1, 'C4_ConstantValue__a_0')
C5_ConstantValue__a_0 = solver.IntVar(0, 1, 'C5_ConstantValue__a_0')
C6_ConstantValue__a_0 = solver.IntVar(0, 1, 'C6_ConstantValue__a_0')
C7_ConstantValue__a_0 = solver.IntVar(0, 1, 'C7_ConstantValue__a_0')
C8_ConstantValue__a_0 = solver.IntVar(0, 1, 'C8_ConstantValue__a_0')
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__a_0_float + (-1)*C3_ConstantValue__a_0<=1)    #Fix to float
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__a_0_fixp + (-1)*C4_ConstantValue__a_0<=1)    #Float to fix
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__a_0_double + (-1)*C5_ConstantValue__a_0<=1)    #Fix to double
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__a_0_fixp + (-1)*C6_ConstantValue__a_0<=1)    #Double to fix
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__a_0_double + (-1)*C7_ConstantValue__a_0<=1)    #Float to double
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__a_0_float + (-1)*C8_ConstantValue__a_0<=1)    #Double to float
solver.Add( + (1)*main_a_0_fixp + (-1)*ConstantValue__a_0_fixp==0)    #fix equality
solver.Add( + (1)*main_a_0_float + (-1)*ConstantValue__a_0_float==0)    #float equality
solver.Add( + (1)*main_a_0_double + (-1)*ConstantValue__a_0_double==0)    #double equality
solver.Add( + (1)*main_a_0_fixbits + (-1)*ConstantValue__a_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_a_0_enob + (-1)*ConstantValue__enob + (-10000)*a_0_enob_0<=0)    #Enob: forcing phi enob
ConstantValue__0_fixbits = solver.IntVar(0, 29, 'ConstantValue__0_fixbits')
ConstantValue__0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_fixp')
ConstantValue__0_float = solver.IntVar(0, 1, 'ConstantValue__0_float')
ConstantValue__0_double = solver.IntVar(0, 1, 'ConstantValue__0_double')
ConstantValue__0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_enob')
solver.Add( + (1)*ConstantValue__0_enob + (-1)*ConstantValue__0_fixbits + (10000)*ConstantValue__0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_float<=10021)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_enob + (10000)*ConstantValue__0_double<=10050)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_float + (1)*ConstantValue__0_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_fixbits + (-10000)*ConstantValue__0_fixp<=0)    #If not fix, frac part to zero
ConstantValue__0_a_0_fixbits = solver.IntVar(0, 29, 'ConstantValue__0_a_0_fixbits')
ConstantValue__0_a_0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_a_0_fixp')
ConstantValue__0_a_0_float = solver.IntVar(0, 1, 'ConstantValue__0_a_0_float')
ConstantValue__0_a_0_double = solver.IntVar(0, 1, 'ConstantValue__0_a_0_double')
ConstantValue__0_a_0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_a_0_enob')
solver.Add( + (1)*ConstantValue__0_a_0_fixp + (1)*ConstantValue__0_a_0_float + (1)*ConstantValue__0_a_0_double==1)    #exactly 1 type
solver.Add( + (-1)*ConstantValue__0_enob + (1)*ConstantValue__0_a_0_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*ConstantValue__0_a_0_fixbits + (-10000)*ConstantValue__0_a_0_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C1_ConstantValue__0_a_0')
C2_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C2_ConstantValue__0_a_0')
solver.Add( + (1)*ConstantValue__0_fixbits + (-1)*ConstantValue__0_a_0_fixbits + (-10000)*C1_ConstantValue__0_a_0<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__0_fixbits + (1)*ConstantValue__0_a_0_fixbits + (-10000)*C2_ConstantValue__0_a_0<=0)    #Shift cost 2
C3_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C3_ConstantValue__0_a_0')
C4_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C4_ConstantValue__0_a_0')
C5_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C5_ConstantValue__0_a_0')
C6_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C6_ConstantValue__0_a_0')
C7_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C7_ConstantValue__0_a_0')
C8_ConstantValue__0_a_0 = solver.IntVar(0, 1, 'C8_ConstantValue__0_a_0')
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_a_0_float + (-1)*C3_ConstantValue__0_a_0<=1)    #Fix to float
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_a_0_fixp + (-1)*C4_ConstantValue__0_a_0<=1)    #Float to fix
solver.Add( + (1)*ConstantValue__0_fixp + (1)*ConstantValue__0_a_0_double + (-1)*C5_ConstantValue__0_a_0<=1)    #Fix to double
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_a_0_fixp + (-1)*C6_ConstantValue__0_a_0<=1)    #Double to fix
solver.Add( + (1)*ConstantValue__0_float + (1)*ConstantValue__0_a_0_double + (-1)*C7_ConstantValue__0_a_0<=1)    #Float to double
solver.Add( + (1)*ConstantValue__0_double + (1)*ConstantValue__0_a_0_float + (-1)*C8_ConstantValue__0_a_0<=1)    #Double to float
solver.Add( + (1)*main_a_0_fixp + (-1)*ConstantValue__0_a_0_fixp==0)    #fix equality
solver.Add( + (1)*main_a_0_float + (-1)*ConstantValue__0_a_0_float==0)    #float equality
solver.Add( + (1)*main_a_0_double + (-1)*ConstantValue__0_a_0_double==0)    #double equality
solver.Add( + (1)*main_a_0_fixbits + (-1)*ConstantValue__0_a_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_a_0_enob + (-1)*ConstantValue__0_enob + (-10000)*a_0_enob_1<=0)    #Enob: forcing phi enob
main_b_0_fixbits = solver.IntVar(0, 26, 'main_b_0_fixbits')
main_b_0_fixp = solver.IntVar(0, 1, 'main_b_0_fixp')
main_b_0_float = solver.IntVar(0, 1, 'main_b_0_float')
main_b_0_double = solver.IntVar(0, 1, 'main_b_0_double')
main_b_0_enob = solver.IntVar(-10000, 10000, 'main_b_0_enob')
solver.Add( + (1)*main_b_0_enob + (-1)*main_b_0_fixbits + (10000)*main_b_0_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_b_0_enob + (10000)*main_b_0_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_b_0_enob + (10000)*main_b_0_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_b_0_fixp + (1)*main_b_0_float + (1)*main_b_0_double==1)    #Exactly one selected type
solver.Add( + (1)*main_b_0_fixbits + (-10000)*main_b_0_fixp<=0)    #If not fix, frac part to zero
b_0_enob_0 = solver.IntVar(0, 1, 'b_0_enob_0')
b_0_enob_1 = solver.IntVar(0, 1, 'b_0_enob_1')
solver.Add( + (1)*b_0_enob_0 + (1)*b_0_enob_1==1)    #Enob: one selected constraint
ConstantValue__0_1_fixbits = solver.IntVar(0, 26, 'ConstantValue__0_1_fixbits')
ConstantValue__0_1_fixp = solver.IntVar(0, 1, 'ConstantValue__0_1_fixp')
ConstantValue__0_1_float = solver.IntVar(0, 1, 'ConstantValue__0_1_float')
ConstantValue__0_1_double = solver.IntVar(0, 1, 'ConstantValue__0_1_double')
ConstantValue__0_1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_1_enob')
solver.Add( + (1)*ConstantValue__0_1_enob + (-1)*ConstantValue__0_1_fixbits + (10000)*ConstantValue__0_1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_1_enob + (10000)*ConstantValue__0_1_float<=10018)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_1_enob + (10000)*ConstantValue__0_1_double<=10047)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_1_fixp + (1)*ConstantValue__0_1_float + (1)*ConstantValue__0_1_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_1_fixbits + (-10000)*ConstantValue__0_1_fixp<=0)    #If not fix, frac part to zero
ConstantValue__0_1_b_0_fixbits = solver.IntVar(0, 26, 'ConstantValue__0_1_b_0_fixbits')
ConstantValue__0_1_b_0_fixp = solver.IntVar(0, 1, 'ConstantValue__0_1_b_0_fixp')
ConstantValue__0_1_b_0_float = solver.IntVar(0, 1, 'ConstantValue__0_1_b_0_float')
ConstantValue__0_1_b_0_double = solver.IntVar(0, 1, 'ConstantValue__0_1_b_0_double')
ConstantValue__0_1_b_0_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_1_b_0_enob')
solver.Add( + (1)*ConstantValue__0_1_b_0_fixp + (1)*ConstantValue__0_1_b_0_float + (1)*ConstantValue__0_1_b_0_double==1)    #exactly 1 type
solver.Add( + (-1)*ConstantValue__0_1_enob + (1)*ConstantValue__0_1_b_0_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*ConstantValue__0_1_b_0_fixbits + (-10000)*ConstantValue__0_1_b_0_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C1_ConstantValue__0_1_b_0')
C2_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C2_ConstantValue__0_1_b_0')
solver.Add( + (1)*ConstantValue__0_1_fixbits + (-1)*ConstantValue__0_1_b_0_fixbits + (-10000)*C1_ConstantValue__0_1_b_0<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__0_1_fixbits + (1)*ConstantValue__0_1_b_0_fixbits + (-10000)*C2_ConstantValue__0_1_b_0<=0)    #Shift cost 2
C3_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C3_ConstantValue__0_1_b_0')
C4_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C4_ConstantValue__0_1_b_0')
C5_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C5_ConstantValue__0_1_b_0')
C6_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C6_ConstantValue__0_1_b_0')
C7_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C7_ConstantValue__0_1_b_0')
C8_ConstantValue__0_1_b_0 = solver.IntVar(0, 1, 'C8_ConstantValue__0_1_b_0')
solver.Add( + (1)*ConstantValue__0_1_fixp + (1)*ConstantValue__0_1_b_0_float + (-1)*C3_ConstantValue__0_1_b_0<=1)    #Fix to float
solver.Add( + (1)*ConstantValue__0_1_float + (1)*ConstantValue__0_1_b_0_fixp + (-1)*C4_ConstantValue__0_1_b_0<=1)    #Float to fix
solver.Add( + (1)*ConstantValue__0_1_fixp + (1)*ConstantValue__0_1_b_0_double + (-1)*C5_ConstantValue__0_1_b_0<=1)    #Fix to double
solver.Add( + (1)*ConstantValue__0_1_double + (1)*ConstantValue__0_1_b_0_fixp + (-1)*C6_ConstantValue__0_1_b_0<=1)    #Double to fix
solver.Add( + (1)*ConstantValue__0_1_float + (1)*ConstantValue__0_1_b_0_double + (-1)*C7_ConstantValue__0_1_b_0<=1)    #Float to double
solver.Add( + (1)*ConstantValue__0_1_double + (1)*ConstantValue__0_1_b_0_float + (-1)*C8_ConstantValue__0_1_b_0<=1)    #Double to float
solver.Add( + (1)*main_b_0_fixp + (-1)*ConstantValue__0_1_b_0_fixp==0)    #fix equality
solver.Add( + (1)*main_b_0_float + (-1)*ConstantValue__0_1_b_0_float==0)    #float equality
solver.Add( + (1)*main_b_0_double + (-1)*ConstantValue__0_1_b_0_double==0)    #double equality
solver.Add( + (1)*main_b_0_fixbits + (-1)*ConstantValue__0_1_b_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_b_0_enob + (-1)*ConstantValue__0_1_enob + (-10000)*b_0_enob_0<=0)    #Enob: forcing phi enob
main_b_1_fixbits = solver.IntVar(0, 26, 'main_b_1_fixbits')
main_b_1_fixp = solver.IntVar(0, 1, 'main_b_1_fixp')
main_b_1_float = solver.IntVar(0, 1, 'main_b_1_float')
main_b_1_double = solver.IntVar(0, 1, 'main_b_1_double')
main_b_1_enob = solver.IntVar(-10000, 10000, 'main_b_1_enob')
solver.Add( + (1)*main_b_1_enob + (-1)*main_b_1_fixbits + (10000)*main_b_1_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_b_1_enob + (10000)*main_b_1_float<=10149)    #Enob constraint for float
solver.Add( + (1)*main_b_1_enob + (10000)*main_b_1_double<=11074)    #Enob constraint for double
solver.Add( + (1)*main_b_1_fixp + (1)*main_b_1_float + (1)*main_b_1_double==1)    #Exactly one selected type
solver.Add( + (1)*main_b_1_fixbits + (-10000)*main_b_1_fixp<=0)    #If not fix, frac part to zero
b_1_enob_0 = solver.IntVar(0, 1, 'b_1_enob_0')
b_1_enob_1 = solver.IntVar(0, 1, 'b_1_enob_1')
solver.Add( + (1)*b_1_enob_0 + (1)*b_1_enob_1==1)    #Enob: one selected constraint
ConstantValue__0_1_2_fixbits = solver.IntVar(0, 32, 'ConstantValue__0_1_2_fixbits')
ConstantValue__0_1_2_fixp = solver.IntVar(0, 1, 'ConstantValue__0_1_2_fixp')
ConstantValue__0_1_2_float = solver.IntVar(0, 1, 'ConstantValue__0_1_2_float')
ConstantValue__0_1_2_double = solver.IntVar(0, 1, 'ConstantValue__0_1_2_double')
ConstantValue__0_1_2_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_1_2_enob')
solver.Add( + (1)*ConstantValue__0_1_2_enob + (-1)*ConstantValue__0_1_2_fixbits + (10000)*ConstantValue__0_1_2_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_1_2_enob + (10000)*ConstantValue__0_1_2_float<=10149)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_1_2_enob + (10000)*ConstantValue__0_1_2_double<=11074)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_1_2_fixp + (1)*ConstantValue__0_1_2_float + (1)*ConstantValue__0_1_2_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_1_2_fixbits + (-10000)*ConstantValue__0_1_2_fixp<=0)    #If not fix, frac part to zero
ConstantValue__0_1_2_b_1_fixbits = solver.IntVar(0, 32, 'ConstantValue__0_1_2_b_1_fixbits')
ConstantValue__0_1_2_b_1_fixp = solver.IntVar(0, 1, 'ConstantValue__0_1_2_b_1_fixp')
ConstantValue__0_1_2_b_1_float = solver.IntVar(0, 1, 'ConstantValue__0_1_2_b_1_float')
ConstantValue__0_1_2_b_1_double = solver.IntVar(0, 1, 'ConstantValue__0_1_2_b_1_double')
ConstantValue__0_1_2_b_1_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_1_2_b_1_enob')
solver.Add( + (1)*ConstantValue__0_1_2_b_1_fixp + (1)*ConstantValue__0_1_2_b_1_float + (1)*ConstantValue__0_1_2_b_1_double==1)    #exactly 1 type
solver.Add( + (-1)*ConstantValue__0_1_2_enob + (1)*ConstantValue__0_1_2_b_1_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*ConstantValue__0_1_2_b_1_fixbits + (-10000)*ConstantValue__0_1_2_b_1_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C1_ConstantValue__0_1_2_b_1')
C2_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C2_ConstantValue__0_1_2_b_1')
solver.Add( + (1)*ConstantValue__0_1_2_fixbits + (-1)*ConstantValue__0_1_2_b_1_fixbits + (-10000)*C1_ConstantValue__0_1_2_b_1<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__0_1_2_fixbits + (1)*ConstantValue__0_1_2_b_1_fixbits + (-10000)*C2_ConstantValue__0_1_2_b_1<=0)    #Shift cost 2
C3_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C3_ConstantValue__0_1_2_b_1')
C4_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C4_ConstantValue__0_1_2_b_1')
C5_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C5_ConstantValue__0_1_2_b_1')
C6_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C6_ConstantValue__0_1_2_b_1')
C7_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C7_ConstantValue__0_1_2_b_1')
C8_ConstantValue__0_1_2_b_1 = solver.IntVar(0, 1, 'C8_ConstantValue__0_1_2_b_1')
solver.Add( + (1)*ConstantValue__0_1_2_fixp + (1)*ConstantValue__0_1_2_b_1_float + (-1)*C3_ConstantValue__0_1_2_b_1<=1)    #Fix to float
solver.Add( + (1)*ConstantValue__0_1_2_float + (1)*ConstantValue__0_1_2_b_1_fixp + (-1)*C4_ConstantValue__0_1_2_b_1<=1)    #Float to fix
solver.Add( + (1)*ConstantValue__0_1_2_fixp + (1)*ConstantValue__0_1_2_b_1_double + (-1)*C5_ConstantValue__0_1_2_b_1<=1)    #Fix to double
solver.Add( + (1)*ConstantValue__0_1_2_double + (1)*ConstantValue__0_1_2_b_1_fixp + (-1)*C6_ConstantValue__0_1_2_b_1<=1)    #Double to fix
solver.Add( + (1)*ConstantValue__0_1_2_float + (1)*ConstantValue__0_1_2_b_1_double + (-1)*C7_ConstantValue__0_1_2_b_1<=1)    #Float to double
solver.Add( + (1)*ConstantValue__0_1_2_double + (1)*ConstantValue__0_1_2_b_1_float + (-1)*C8_ConstantValue__0_1_2_b_1<=1)    #Double to float
solver.Add( + (1)*main_b_1_fixp + (-1)*ConstantValue__0_1_2_b_1_fixp==0)    #fix equality
solver.Add( + (1)*main_b_1_float + (-1)*ConstantValue__0_1_2_b_1_float==0)    #float equality
solver.Add( + (1)*main_b_1_double + (-1)*ConstantValue__0_1_2_b_1_double==0)    #double equality
solver.Add( + (1)*main_b_1_fixbits + (-1)*ConstantValue__0_1_2_b_1_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_b_1_enob + (-1)*ConstantValue__0_1_2_enob + (-10000)*b_1_enob_0<=0)    #Enob: forcing phi enob
main_b_0_b_1_fixbits = solver.IntVar(0, 26, 'main_b_0_b_1_fixbits')
main_b_0_b_1_fixp = solver.IntVar(0, 1, 'main_b_0_b_1_fixp')
main_b_0_b_1_float = solver.IntVar(0, 1, 'main_b_0_b_1_float')
main_b_0_b_1_double = solver.IntVar(0, 1, 'main_b_0_b_1_double')
main_b_0_b_1_enob = solver.IntVar(-10000, 10000, 'main_b_0_b_1_enob')
solver.Add( + (1)*main_b_0_b_1_fixp + (1)*main_b_0_b_1_float + (1)*main_b_0_b_1_double==1)    #exactly 1 type
solver.Add( + (-1)*main_b_0_enob + (1)*main_b_0_b_1_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*main_b_0_b_1_fixbits + (-10000)*main_b_0_b_1_fixp<=0)    #If no fix, fix frac part = 0
C1_main_b_0_b_1 = solver.IntVar(0, 1, 'C1_main_b_0_b_1')
C2_main_b_0_b_1 = solver.IntVar(0, 1, 'C2_main_b_0_b_1')
solver.Add( + (1)*main_b_0_fixbits + (-1)*main_b_0_b_1_fixbits + (-10000)*C1_main_b_0_b_1<=0)    #Shift cost 1
solver.Add( + (-1)*main_b_0_fixbits + (1)*main_b_0_b_1_fixbits + (-10000)*C2_main_b_0_b_1<=0)    #Shift cost 2
C3_main_b_0_b_1 = solver.IntVar(0, 1, 'C3_main_b_0_b_1')
C4_main_b_0_b_1 = solver.IntVar(0, 1, 'C4_main_b_0_b_1')
C5_main_b_0_b_1 = solver.IntVar(0, 1, 'C5_main_b_0_b_1')
C6_main_b_0_b_1 = solver.IntVar(0, 1, 'C6_main_b_0_b_1')
C7_main_b_0_b_1 = solver.IntVar(0, 1, 'C7_main_b_0_b_1')
C8_main_b_0_b_1 = solver.IntVar(0, 1, 'C8_main_b_0_b_1')
solver.Add( + (1)*main_b_0_fixp + (1)*main_b_0_b_1_float + (-1)*C3_main_b_0_b_1<=1)    #Fix to float
solver.Add( + (1)*main_b_0_float + (1)*main_b_0_b_1_fixp + (-1)*C4_main_b_0_b_1<=1)    #Float to fix
solver.Add( + (1)*main_b_0_fixp + (1)*main_b_0_b_1_double + (-1)*C5_main_b_0_b_1<=1)    #Fix to double
solver.Add( + (1)*main_b_0_double + (1)*main_b_0_b_1_fixp + (-1)*C6_main_b_0_b_1<=1)    #Double to fix
solver.Add( + (1)*main_b_0_float + (1)*main_b_0_b_1_double + (-1)*C7_main_b_0_b_1<=1)    #Float to double
solver.Add( + (1)*main_b_0_double + (1)*main_b_0_b_1_float + (-1)*C8_main_b_0_b_1<=1)    #Double to float
solver.Add( + (1)*main_b_1_fixp + (-1)*main_b_0_b_1_fixp==0)    #fix equality
solver.Add( + (1)*main_b_1_float + (-1)*main_b_0_b_1_float==0)    #float equality
solver.Add( + (1)*main_b_1_double + (-1)*main_b_0_b_1_double==0)    #double equality
solver.Add( + (1)*main_b_1_fixbits + (-1)*main_b_0_b_1_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_b_1_enob + (-1)*main_b_0_enob + (-10000)*b_1_enob_1<=0)    #Enob: forcing phi enob
ConstantValue__0_1_2_3_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_1_2_3_fixbits')
ConstantValue__0_1_2_3_fixp = solver.IntVar(0, 1, 'ConstantValue__0_1_2_3_fixp')
ConstantValue__0_1_2_3_float = solver.IntVar(0, 1, 'ConstantValue__0_1_2_3_float')
ConstantValue__0_1_2_3_double = solver.IntVar(0, 1, 'ConstantValue__0_1_2_3_double')
ConstantValue__0_1_2_3_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_1_2_3_enob')
solver.Add( + (1)*ConstantValue__0_1_2_3_enob + (-1)*ConstantValue__0_1_2_3_fixbits + (10000)*ConstantValue__0_1_2_3_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*ConstantValue__0_1_2_3_enob + (10000)*ConstantValue__0_1_2_3_float<=10023)    #Enob constraint for float
solver.Add( + (1)*ConstantValue__0_1_2_3_enob + (10000)*ConstantValue__0_1_2_3_double<=10052)    #Enob constraint for double
solver.Add( + (1)*ConstantValue__0_1_2_3_fixp + (1)*ConstantValue__0_1_2_3_float + (1)*ConstantValue__0_1_2_3_double==1)    #Exactly one selected type
solver.Add( + (1)*ConstantValue__0_1_2_3_fixbits + (-10000)*ConstantValue__0_1_2_3_fixp<=0)    #If not fix, frac part to zero
main_b_1_inc12_fixbits = solver.IntVar(0, 26, 'main_b_1_inc12_fixbits')
main_b_1_inc12_fixp = solver.IntVar(0, 1, 'main_b_1_inc12_fixp')
main_b_1_inc12_float = solver.IntVar(0, 1, 'main_b_1_inc12_float')
main_b_1_inc12_double = solver.IntVar(0, 1, 'main_b_1_inc12_double')
main_b_1_inc12_enob = solver.IntVar(-10000, 10000, 'main_b_1_inc12_enob')
solver.Add( + (1)*main_b_1_inc12_fixp + (1)*main_b_1_inc12_float + (1)*main_b_1_inc12_double==1)    #exactly 1 type
solver.Add( + (-1)*main_b_1_enob + (1)*main_b_1_inc12_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*main_b_1_inc12_fixbits + (-10000)*main_b_1_inc12_fixp<=0)    #If no fix, fix frac part = 0
C1_main_b_1_inc12 = solver.IntVar(0, 1, 'C1_main_b_1_inc12')
C2_main_b_1_inc12 = solver.IntVar(0, 1, 'C2_main_b_1_inc12')
solver.Add( + (1)*main_b_1_fixbits + (-1)*main_b_1_inc12_fixbits + (-10000)*C1_main_b_1_inc12<=0)    #Shift cost 1
solver.Add( + (-1)*main_b_1_fixbits + (1)*main_b_1_inc12_fixbits + (-10000)*C2_main_b_1_inc12<=0)    #Shift cost 2
C3_main_b_1_inc12 = solver.IntVar(0, 1, 'C3_main_b_1_inc12')
C4_main_b_1_inc12 = solver.IntVar(0, 1, 'C4_main_b_1_inc12')
C5_main_b_1_inc12 = solver.IntVar(0, 1, 'C5_main_b_1_inc12')
C6_main_b_1_inc12 = solver.IntVar(0, 1, 'C6_main_b_1_inc12')
C7_main_b_1_inc12 = solver.IntVar(0, 1, 'C7_main_b_1_inc12')
C8_main_b_1_inc12 = solver.IntVar(0, 1, 'C8_main_b_1_inc12')
solver.Add( + (1)*main_b_1_fixp + (1)*main_b_1_inc12_float + (-1)*C3_main_b_1_inc12<=1)    #Fix to float
solver.Add( + (1)*main_b_1_float + (1)*main_b_1_inc12_fixp + (-1)*C4_main_b_1_inc12<=1)    #Float to fix
solver.Add( + (1)*main_b_1_fixp + (1)*main_b_1_inc12_double + (-1)*C5_main_b_1_inc12<=1)    #Fix to double
solver.Add( + (1)*main_b_1_double + (1)*main_b_1_inc12_fixp + (-1)*C6_main_b_1_inc12<=1)    #Double to fix
solver.Add( + (1)*main_b_1_float + (1)*main_b_1_inc12_double + (-1)*C7_main_b_1_inc12<=1)    #Float to double
solver.Add( + (1)*main_b_1_double + (1)*main_b_1_inc12_float + (-1)*C8_main_b_1_inc12<=1)    #Double to float
ConstantValue__0_1_2_3_inc12_fixbits = solver.IntVar(0, 31, 'ConstantValue__0_1_2_3_inc12_fixbits')
ConstantValue__0_1_2_3_inc12_fixp = solver.IntVar(0, 1, 'ConstantValue__0_1_2_3_inc12_fixp')
ConstantValue__0_1_2_3_inc12_float = solver.IntVar(0, 1, 'ConstantValue__0_1_2_3_inc12_float')
ConstantValue__0_1_2_3_inc12_double = solver.IntVar(0, 1, 'ConstantValue__0_1_2_3_inc12_double')
ConstantValue__0_1_2_3_inc12_enob = solver.IntVar(-10000, 10000, 'ConstantValue__0_1_2_3_inc12_enob')
solver.Add( + (1)*ConstantValue__0_1_2_3_inc12_fixp + (1)*ConstantValue__0_1_2_3_inc12_float + (1)*ConstantValue__0_1_2_3_inc12_double==1)    #exactly 1 type
solver.Add( + (-1)*ConstantValue__0_1_2_3_enob + (1)*ConstantValue__0_1_2_3_inc12_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*ConstantValue__0_1_2_3_inc12_fixbits + (-10000)*ConstantValue__0_1_2_3_inc12_fixp<=0)    #If no fix, fix frac part = 0
C1_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C1_ConstantValue__0_1_2_3_inc12')
C2_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C2_ConstantValue__0_1_2_3_inc12')
solver.Add( + (1)*ConstantValue__0_1_2_3_fixbits + (-1)*ConstantValue__0_1_2_3_inc12_fixbits + (-10000)*C1_ConstantValue__0_1_2_3_inc12<=0)    #Shift cost 1
solver.Add( + (-1)*ConstantValue__0_1_2_3_fixbits + (1)*ConstantValue__0_1_2_3_inc12_fixbits + (-10000)*C2_ConstantValue__0_1_2_3_inc12<=0)    #Shift cost 2
C3_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C3_ConstantValue__0_1_2_3_inc12')
C4_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C4_ConstantValue__0_1_2_3_inc12')
C5_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C5_ConstantValue__0_1_2_3_inc12')
C6_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C6_ConstantValue__0_1_2_3_inc12')
C7_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C7_ConstantValue__0_1_2_3_inc12')
C8_ConstantValue__0_1_2_3_inc12 = solver.IntVar(0, 1, 'C8_ConstantValue__0_1_2_3_inc12')
solver.Add( + (1)*ConstantValue__0_1_2_3_fixp + (1)*ConstantValue__0_1_2_3_inc12_float + (-1)*C3_ConstantValue__0_1_2_3_inc12<=1)    #Fix to float
solver.Add( + (1)*ConstantValue__0_1_2_3_float + (1)*ConstantValue__0_1_2_3_inc12_fixp + (-1)*C4_ConstantValue__0_1_2_3_inc12<=1)    #Float to fix
solver.Add( + (1)*ConstantValue__0_1_2_3_fixp + (1)*ConstantValue__0_1_2_3_inc12_double + (-1)*C5_ConstantValue__0_1_2_3_inc12<=1)    #Fix to double
solver.Add( + (1)*ConstantValue__0_1_2_3_double + (1)*ConstantValue__0_1_2_3_inc12_fixp + (-1)*C6_ConstantValue__0_1_2_3_inc12<=1)    #Double to fix
solver.Add( + (1)*ConstantValue__0_1_2_3_float + (1)*ConstantValue__0_1_2_3_inc12_double + (-1)*C7_ConstantValue__0_1_2_3_inc12<=1)    #Float to double
solver.Add( + (1)*ConstantValue__0_1_2_3_double + (1)*ConstantValue__0_1_2_3_inc12_float + (-1)*C8_ConstantValue__0_1_2_3_inc12<=1)    #Double to float
main_inc12_fixbits = solver.IntVar(0, 26, 'main_inc12_fixbits')
main_inc12_fixp = solver.IntVar(0, 1, 'main_inc12_fixp')
main_inc12_float = solver.IntVar(0, 1, 'main_inc12_float')
main_inc12_double = solver.IntVar(0, 1, 'main_inc12_double')
main_inc12_enob = solver.IntVar(-10000, 10000, 'main_inc12_enob')
solver.Add( + (1)*main_inc12_enob + (-1)*main_inc12_fixbits + (10000)*main_inc12_fixp<=10000)    #Enob constraint for fix
solver.Add( + (1)*main_inc12_enob + (10000)*main_inc12_float<=10023)    #Enob constraint for float
solver.Add( + (1)*main_inc12_enob + (10000)*main_inc12_double<=10052)    #Enob constraint for double
solver.Add( + (1)*main_inc12_fixp + (1)*main_inc12_float + (1)*main_inc12_double==1)    #Exactly one selected type
solver.Add( + (1)*main_inc12_fixbits + (-10000)*main_inc12_fixp<=0)    #If not fix, frac part to zero
main_inc12_b_0_fixbits = solver.IntVar(0, 26, 'main_inc12_b_0_fixbits')
main_inc12_b_0_fixp = solver.IntVar(0, 1, 'main_inc12_b_0_fixp')
main_inc12_b_0_float = solver.IntVar(0, 1, 'main_inc12_b_0_float')
main_inc12_b_0_double = solver.IntVar(0, 1, 'main_inc12_b_0_double')
main_inc12_b_0_enob = solver.IntVar(-10000, 10000, 'main_inc12_b_0_enob')
solver.Add( + (1)*main_inc12_b_0_fixp + (1)*main_inc12_b_0_float + (1)*main_inc12_b_0_double==1)    #exactly 1 type
solver.Add( + (-1)*main_inc12_enob + (1)*main_inc12_b_0_enob<=0)    #The ENOB is less or equal!
solver.Add( + (1)*main_inc12_b_0_fixbits + (-10000)*main_inc12_b_0_fixp<=0)    #If no fix, fix frac part = 0
C1_main_inc12_b_0 = solver.IntVar(0, 1, 'C1_main_inc12_b_0')
C2_main_inc12_b_0 = solver.IntVar(0, 1, 'C2_main_inc12_b_0')
solver.Add( + (1)*main_inc12_fixbits + (-1)*main_inc12_b_0_fixbits + (-10000)*C1_main_inc12_b_0<=0)    #Shift cost 1
solver.Add( + (-1)*main_inc12_fixbits + (1)*main_inc12_b_0_fixbits + (-10000)*C2_main_inc12_b_0<=0)    #Shift cost 2
C3_main_inc12_b_0 = solver.IntVar(0, 1, 'C3_main_inc12_b_0')
C4_main_inc12_b_0 = solver.IntVar(0, 1, 'C4_main_inc12_b_0')
C5_main_inc12_b_0 = solver.IntVar(0, 1, 'C5_main_inc12_b_0')
C6_main_inc12_b_0 = solver.IntVar(0, 1, 'C6_main_inc12_b_0')
C7_main_inc12_b_0 = solver.IntVar(0, 1, 'C7_main_inc12_b_0')
C8_main_inc12_b_0 = solver.IntVar(0, 1, 'C8_main_inc12_b_0')
solver.Add( + (1)*main_inc12_fixp + (1)*main_inc12_b_0_float + (-1)*C3_main_inc12_b_0<=1)    #Fix to float
solver.Add( + (1)*main_inc12_float + (1)*main_inc12_b_0_fixp + (-1)*C4_main_inc12_b_0<=1)    #Float to fix
solver.Add( + (1)*main_inc12_fixp + (1)*main_inc12_b_0_double + (-1)*C5_main_inc12_b_0<=1)    #Fix to double
solver.Add( + (1)*main_inc12_double + (1)*main_inc12_b_0_fixp + (-1)*C6_main_inc12_b_0<=1)    #Double to fix
solver.Add( + (1)*main_inc12_float + (1)*main_inc12_b_0_double + (-1)*C7_main_inc12_b_0<=1)    #Float to double
solver.Add( + (1)*main_inc12_double + (1)*main_inc12_b_0_float + (-1)*C8_main_inc12_b_0<=1)    #Double to float
solver.Add( + (1)*main_b_0_fixp + (-1)*main_inc12_b_0_fixp==0)    #fix equality
solver.Add( + (1)*main_b_0_float + (-1)*main_inc12_b_0_float==0)    #float equality
solver.Add( + (1)*main_b_0_double + (-1)*main_inc12_b_0_double==0)    #double equality
solver.Add( + (1)*main_b_0_fixbits + (-1)*main_inc12_b_0_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_b_0_enob + (-1)*main_inc12_enob + (-10000)*b_0_enob_1<=0)    #Enob: forcing phi enob
solver.Add( + (1)*main_b_1_inc12_fixp + (-1)*ConstantValue__0_1_2_3_inc12_fixp==0)    #fix equality
solver.Add( + (1)*main_b_1_inc12_float + (-1)*ConstantValue__0_1_2_3_inc12_float==0)    #float equality
solver.Add( + (1)*main_b_1_inc12_double + (-1)*ConstantValue__0_1_2_3_inc12_double==0)    #double equality
solver.Add( + (1)*main_b_1_inc12_fixbits + (-1)*ConstantValue__0_1_2_3_inc12_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_b_1_inc12_fixp + (-1)*main_inc12_fixp==0)    #fix equality
solver.Add( + (1)*main_b_1_inc12_float + (-1)*main_inc12_float==0)    #float equality
solver.Add( + (1)*main_b_1_inc12_double + (-1)*main_inc12_double==0)    #double equality
solver.Add( + (1)*main_b_1_inc12_fixbits + (-1)*main_inc12_fixbits==0)    #same fractional bit
solver.Add( + (1)*main_inc12_enob + (-1)*main_b_1_enob<=0)    #Enob propagation in sum first addend
solver.Add( + (1)*main_inc12_enob + (-1)*ConstantValue__0_1_2_3_enob<=0)    #Enob propagation in sum second addend
solver.Minimize( + (-0.5)*main_a_0_enob + (-0.5)*ConstantValue__enob + (5)*C1_ConstantValue__a_0 + (5)*C2_ConstantValue__a_0 + (10)*C3_ConstantValue__a_0 + (10)*C4_ConstantValue__a_0 + (10)*C5_ConstantValue__a_0 + (10)*C6_ConstantValue__a_0 + (10)*C7_ConstantValue__a_0 + (10)*C8_ConstantValue__a_0 + (-0.5)*ConstantValue__0_enob + (5)*C1_ConstantValue__0_a_0 + (5)*C2_ConstantValue__0_a_0 + (10)*C3_ConstantValue__0_a_0 + (10)*C4_ConstantValue__0_a_0 + (10)*C5_ConstantValue__0_a_0 + (10)*C6_ConstantValue__0_a_0 + (10)*C7_ConstantValue__0_a_0 + (10)*C8_ConstantValue__0_a_0 + (-0.5)*main_b_0_enob + (-0.5)*ConstantValue__0_1_enob + (5)*C1_ConstantValue__0_1_b_0 + (5)*C2_ConstantValue__0_1_b_0 + (10)*C3_ConstantValue__0_1_b_0 + (10)*C4_ConstantValue__0_1_b_0 + (10)*C5_ConstantValue__0_1_b_0 + (10)*C6_ConstantValue__0_1_b_0 + (10)*C7_ConstantValue__0_1_b_0 + (10)*C8_ConstantValue__0_1_b_0 + (-0.5)*main_b_1_enob + (-0.5)*ConstantValue__0_1_2_enob + (5)*C1_ConstantValue__0_1_2_b_1 + (5)*C2_ConstantValue__0_1_2_b_1 + (10)*C3_ConstantValue__0_1_2_b_1 + (10)*C4_ConstantValue__0_1_2_b_1 + (10)*C5_ConstantValue__0_1_2_b_1 + (10)*C6_ConstantValue__0_1_2_b_1 + (10)*C7_ConstantValue__0_1_2_b_1 + (10)*C8_ConstantValue__0_1_2_b_1 + (5)*C1_main_b_0_b_1 + (5)*C2_main_b_0_b_1 + (10)*C3_main_b_0_b_1 + (10)*C4_main_b_0_b_1 + (10)*C5_main_b_0_b_1 + (10)*C6_main_b_0_b_1 + (10)*C7_main_b_0_b_1 + (10)*C8_main_b_0_b_1 + (-0.5)*ConstantValue__0_1_2_3_enob + (5)*C1_main_b_1_inc12 + (5)*C2_main_b_1_inc12 + (10)*C3_main_b_1_inc12 + (10)*C4_main_b_1_inc12 + (10)*C5_main_b_1_inc12 + (10)*C6_main_b_1_inc12 + (10)*C7_main_b_1_inc12 + (10)*C8_main_b_1_inc12 + (5)*C1_ConstantValue__0_1_2_3_inc12 + (5)*C2_ConstantValue__0_1_2_3_inc12 + (10)*C3_ConstantValue__0_1_2_3_inc12 + (10)*C4_ConstantValue__0_1_2_3_inc12 + (10)*C5_ConstantValue__0_1_2_3_inc12 + (10)*C6_ConstantValue__0_1_2_3_inc12 + (10)*C7_ConstantValue__0_1_2_3_inc12 + (10)*C8_ConstantValue__0_1_2_3_inc12 + (-0.5)*main_inc12_enob + (5)*C1_main_inc12_b_0 + (5)*C2_main_inc12_b_0 + (10)*C3_main_inc12_b_0 + (10)*C4_main_inc12_b_0 + (10)*C5_main_inc12_b_0 + (10)*C6_main_inc12_b_0 + (10)*C7_main_inc12_b_0 + (10)*C8_main_inc12_b_0 + (10)*main_inc12_fixp + (40)*main_inc12_float + (60)*main_inc12_double)

# Model declaration end.