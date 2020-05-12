from ortools.linear_solver import pywraplp


# Create the mip solver with the CBC backend.
solver = pywraplp.Solver('simple_mip_program',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

infinity = solver.infinity()
M = 10000

##############################################
##############################################
#APPEND CODE HERE
##############################################
##############################################

array_fixbits = solver.IntVar(0, 21, 'array_fixbits')
array_fixp = solver.IntVar(0, 1, 'array_fixp')
array_float = solver.IntVar(0, 1, 'array_float')
array_double = solver.IntVar(0, 1, 'array_double')
solver.Add( + (1)*array_fixp + (1)*array_float + (1)*array_double==1)
solver.Add( + (1)*array_fixbits + (-10000)*array_fixp<=0)
ConstantValue__fixbits = solver.IntVar(0, 31, 'ConstantValue__fixbits')
ConstantValue__fixp = solver.IntVar(0, 1, 'ConstantValue__fixp')
ConstantValue__float = solver.IntVar(0, 1, 'ConstantValue__float')
ConstantValue__double = solver.IntVar(0, 1, 'ConstantValue__double')
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__float + (1)*ConstantValue__double==1)
solver.Add( + (1)*ConstantValue__fixbits + (-10000)*ConstantValue__fixp<=0)
array_inc7_fixbits = solver.IntVar(0, 21, 'array_inc7_fixbits')
array_inc7_fixp = solver.IntVar(0, 1, 'array_inc7_fixp')
array_inc7_float = solver.IntVar(0, 1, 'array_inc7_float')
array_inc7_double = solver.IntVar(0, 1, 'array_inc7_double')
solver.Add( + (1)*array_inc7_fixp + (1)*array_inc7_float + (1)*array_inc7_double==1)
solver.Add( + (1)*array_inc7_fixbits + (-10000)*array_inc7_fixp<=0)
C1_array_inc7 = solver.IntVar(0, 1, 'C1_array_inc7')
C2_array_inc7 = solver.IntVar(0, 1, 'C2_array_inc7')
solver.Add( + (1)*array_fixbits + (-1)*array_inc7_fixbits + (-10000)*C1_array_inc7<=0)
solver.Add( + (-1)*array_fixbits + (1)*array_inc7_fixbits + (-10000)*C2_array_inc7<=0)
C3_array_inc7 = solver.IntVar(0, 1, 'C3_array_inc7')
C4_array_inc7 = solver.IntVar(0, 1, 'C4_array_inc7')
C5_array_inc7 = solver.IntVar(0, 1, 'C5_array_inc7')
C6_array_inc7 = solver.IntVar(0, 1, 'C6_array_inc7')
C7_array_inc7 = solver.IntVar(0, 1, 'C7_array_inc7')
C8_array_inc7 = solver.IntVar(0, 1, 'C8_array_inc7')
solver.Add( + (1)*array_fixp + (1)*array_inc7_float + (-1)*C3_array_inc7<=1)
solver.Add( + (1)*array_float + (1)*array_inc7_fixp + (-1)*C4_array_inc7<=1)
solver.Add( + (1)*array_fixp + (1)*array_inc7_double + (-1)*C5_array_inc7<=1)
solver.Add( + (1)*array_double + (1)*array_inc7_fixp + (-1)*C6_array_inc7<=1)
solver.Add( + (1)*array_float + (1)*array_inc7_double + (-1)*C7_array_inc7<=1)
solver.Add( + (1)*array_double + (1)*array_inc7_float + (-1)*C8_array_inc7<=1)
ConstantValue__inc7_fixbits = solver.IntVar(0, 31, 'ConstantValue__inc7_fixbits')
ConstantValue__inc7_fixp = solver.IntVar(0, 1, 'ConstantValue__inc7_fixp')
ConstantValue__inc7_float = solver.IntVar(0, 1, 'ConstantValue__inc7_float')
ConstantValue__inc7_double = solver.IntVar(0, 1, 'ConstantValue__inc7_double')
solver.Add( + (1)*ConstantValue__inc7_fixp + (1)*ConstantValue__inc7_float + (1)*ConstantValue__inc7_double==1)
solver.Add( + (1)*ConstantValue__inc7_fixbits + (-10000)*ConstantValue__inc7_fixp<=0)
C1_ConstantValue__inc7 = solver.IntVar(0, 1, 'C1_ConstantValue__inc7')
C2_ConstantValue__inc7 = solver.IntVar(0, 1, 'C2_ConstantValue__inc7')
solver.Add( + (1)*ConstantValue__fixbits + (-1)*ConstantValue__inc7_fixbits + (-10000)*C1_ConstantValue__inc7<=0)
solver.Add( + (-1)*ConstantValue__fixbits + (1)*ConstantValue__inc7_fixbits + (-10000)*C2_ConstantValue__inc7<=0)
C3_ConstantValue__inc7 = solver.IntVar(0, 1, 'C3_ConstantValue__inc7')
C4_ConstantValue__inc7 = solver.IntVar(0, 1, 'C4_ConstantValue__inc7')
C5_ConstantValue__inc7 = solver.IntVar(0, 1, 'C5_ConstantValue__inc7')
C6_ConstantValue__inc7 = solver.IntVar(0, 1, 'C6_ConstantValue__inc7')
C7_ConstantValue__inc7 = solver.IntVar(0, 1, 'C7_ConstantValue__inc7')
C8_ConstantValue__inc7 = solver.IntVar(0, 1, 'C8_ConstantValue__inc7')
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__inc7_float + (-1)*C3_ConstantValue__inc7<=1)
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__inc7_fixp + (-1)*C4_ConstantValue__inc7<=1)
solver.Add( + (1)*ConstantValue__fixp + (1)*ConstantValue__inc7_double + (-1)*C5_ConstantValue__inc7<=1)
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__inc7_fixp + (-1)*C6_ConstantValue__inc7<=1)
solver.Add( + (1)*ConstantValue__float + (1)*ConstantValue__inc7_double + (-1)*C7_ConstantValue__inc7<=1)
solver.Add( + (1)*ConstantValue__double + (1)*ConstantValue__inc7_float + (-1)*C8_ConstantValue__inc7<=1)
main_inc7_fixbits = solver.IntVar(0, 21, 'main_inc7_fixbits')
main_inc7_fixp = solver.IntVar(0, 1, 'main_inc7_fixp')
main_inc7_float = solver.IntVar(0, 1, 'main_inc7_float')
main_inc7_double = solver.IntVar(0, 1, 'main_inc7_double')
solver.Add( + (1)*main_inc7_fixp + (1)*main_inc7_float + (1)*main_inc7_double==1)
solver.Add( + (1)*main_inc7_fixbits + (-10000)*main_inc7_fixp<=0)
solver.Add( + (1)*array_inc7_fixp + (-1)*ConstantValue__inc7_fixp==0)
solver.Add( + (1)*array_inc7_float + (-1)*ConstantValue__inc7_float==0)
solver.Add( + (1)*array_inc7_double + (-1)*ConstantValue__inc7_double==0)
solver.Add( + (1)*array_inc7_fixbits + (-1)*ConstantValue__inc7_fixbits==0)
solver.Add( + (1)*array_inc7_fixp + (-1)*main_inc7_fixp==0)
solver.Add( + (1)*array_inc7_float + (-1)*main_inc7_float==0)
solver.Add( + (1)*array_inc7_double + (-1)*main_inc7_double==0)
solver.Add( + (1)*array_inc7_fixbits + (-1)*main_inc7_fixbits==0)
main_inc7__fixbits = solver.IntVar(0, 21, 'main_inc7__fixbits')
main_inc7__fixp = solver.IntVar(0, 1, 'main_inc7__fixp')
main_inc7__float = solver.IntVar(0, 1, 'main_inc7__float')
main_inc7__double = solver.IntVar(0, 1, 'main_inc7__double')
solver.Add( + (1)*main_inc7__fixp + (1)*main_inc7__float + (1)*main_inc7__double==1)
solver.Add( + (1)*main_inc7__fixbits + (-10000)*main_inc7__fixp<=0)
C1_main_inc7_ = solver.IntVar(0, 1, 'C1_main_inc7_')
C2_main_inc7_ = solver.IntVar(0, 1, 'C2_main_inc7_')
solver.Add( + (1)*main_inc7_fixbits + (-1)*main_inc7__fixbits + (-10000)*C1_main_inc7_<=0)
solver.Add( + (-1)*main_inc7_fixbits + (1)*main_inc7__fixbits + (-10000)*C2_main_inc7_<=0)
C3_main_inc7_ = solver.IntVar(0, 1, 'C3_main_inc7_')
C4_main_inc7_ = solver.IntVar(0, 1, 'C4_main_inc7_')
C5_main_inc7_ = solver.IntVar(0, 1, 'C5_main_inc7_')
C6_main_inc7_ = solver.IntVar(0, 1, 'C6_main_inc7_')
C7_main_inc7_ = solver.IntVar(0, 1, 'C7_main_inc7_')
C8_main_inc7_ = solver.IntVar(0, 1, 'C8_main_inc7_')
solver.Add( + (1)*main_inc7_fixp + (1)*main_inc7__float + (-1)*C3_main_inc7_<=1)
solver.Add( + (1)*main_inc7_float + (1)*main_inc7__fixp + (-1)*C4_main_inc7_<=1)
solver.Add( + (1)*main_inc7_fixp + (1)*main_inc7__double + (-1)*C5_main_inc7_<=1)
solver.Add( + (1)*main_inc7_double + (1)*main_inc7__fixp + (-1)*C6_main_inc7_<=1)
solver.Add( + (1)*main_inc7_float + (1)*main_inc7__double + (-1)*C7_main_inc7_<=1)
solver.Add( + (1)*main_inc7_double + (1)*main_inc7__float + (-1)*C8_main_inc7_<=1)
solver.Add( + (1)*array_fixp + (-1)*main_inc7__fixp==0)
solver.Add( + (1)*array_float + (-1)*main_inc7__float==0)
solver.Add( + (1)*array_double + (-1)*main_inc7__double==0)
solver.Add( + (1)*array_fixbits + (-1)*main_inc7__fixbits==0)
solver.Minimize( + (-1)*array_fixbits + (-21)*array_float + (-50)*array_double + (-1)*ConstantValue__fixbits + (-23)*ConstantValue__float + (-52)*ConstantValue__double + (1)*C1_array_inc7 + (1)*C2_array_inc7 + (1)*C3_array_inc7 + (1)*C4_array_inc7 + (1)*C5_array_inc7 + (1)*C6_array_inc7 + (1)*C7_array_inc7 + (1)*C8_array_inc7 + (1)*C1_ConstantValue__inc7 + (1)*C2_ConstantValue__inc7 + (1)*C3_ConstantValue__inc7 + (1)*C4_ConstantValue__inc7 + (1)*C5_ConstantValue__inc7 + (1)*C6_ConstantValue__inc7 + (1)*C7_ConstantValue__inc7 + (1)*C8_ConstantValue__inc7 + (-1)*main_inc7_fixbits + (-21)*main_inc7_float + (-50)*main_inc7_double + (1)*C1_main_inc7_ + (1)*C2_main_inc7_ + (1)*C3_main_inc7_ + (1)*C4_main_inc7_ + (1)*C5_main_inc7_ + (1)*C6_main_inc7_ + (1)*C7_main_inc7_ + (1)*C8_main_inc7_)

# Model declaration end.


print('Number of variables =', solver.NumVariables())
print('Number of constraints =', solver.NumConstraints())
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())

    for v in solver.variables():
        print(v, "=", v.solution_value())
else:
    print('The problem does not have an optimal solution.')

print('\nAdvanced usage:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())






















