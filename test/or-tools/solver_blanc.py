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


result_fixbits = solver.IntVar(0, 26, 'result_fixbits')
result_fixp = solver.IntVar(0, 1, 'result_fixp')
result_float = solver.IntVar(0, 1, 'result_float')
result_double = solver.IntVar(0, 1, 'result_double')
solver.Add( + (1)*result_fixp + (1)*result_float + (1)*result_double==1)
solver.Add( + (1)*result_fixbits + (-10000)*result_fixp<=0)
main_x_fixbits = solver.IntVar(0, 27, 'main_x_fixbits')
main_x_fixp = solver.IntVar(0, 1, 'main_x_fixp')
main_x_float = solver.IntVar(0, 1, 'main_x_float')
main_x_double = solver.IntVar(0, 1, 'main_x_double')
solver.Add( + (1)*main_x_fixp + (1)*main_x_float + (1)*main_x_double==1)
solver.Add( + (1)*main_x_fixbits + (-10000)*main_x_fixp<=0)
main_y_fixbits = solver.IntVar(0, 28, 'main_y_fixbits')
main_y_fixp = solver.IntVar(0, 1, 'main_y_fixp')
main_y_float = solver.IntVar(0, 1, 'main_y_float')
main_y_double = solver.IntVar(0, 1, 'main_y_double')
solver.Add( + (1)*main_y_fixp + (1)*main_y_float + (1)*main_y_double==1)
solver.Add( + (1)*main_y_fixbits + (-10000)*main_y_fixp<=0)
main_x_add_fixbits = solver.IntVar(0, 27, 'main_x_add_fixbits')
main_x_add_fixp = solver.IntVar(0, 1, 'main_x_add_fixp')
main_x_add_float = solver.IntVar(0, 1, 'main_x_add_float')
main_x_add_double = solver.IntVar(0, 1, 'main_x_add_double')
solver.Add( + (1)*main_x_add_fixp + (1)*main_x_add_float + (1)*main_x_add_double==1)
solver.Add( + (1)*main_x_add_fixbits + (-10000)*main_x_add_fixp<=0)
C1_main_x_add = solver.IntVar(0, 1, 'C1_main_x_add')
C2_main_x_add = solver.IntVar(0, 1, 'C2_main_x_add')
solver.Add( + (1)*main_x_fixbits + (-1)*main_x_add_fixbits + (-10000)*C1_main_x_add<=0)
solver.Add( + (-1)*main_x_fixbits + (1)*main_x_add_fixbits + (-10000)*C2_main_x_add<=0)
C3_main_x_add = solver.IntVar(0, 1, 'C3_main_x_add')
C4_main_x_add = solver.IntVar(0, 1, 'C4_main_x_add')
C5_main_x_add = solver.IntVar(0, 1, 'C5_main_x_add')
C6_main_x_add = solver.IntVar(0, 1, 'C6_main_x_add')
C7_main_x_add = solver.IntVar(0, 1, 'C7_main_x_add')
C8_main_x_add = solver.IntVar(0, 1, 'C8_main_x_add')
solver.Add( + (1)*main_x_fixp + (1)*main_x_add_float + (-1)*C3_main_x_add<=1)
solver.Add( + (1)*main_x_float + (1)*main_x_add_fixp + (-1)*C4_main_x_add<=1)
solver.Add( + (1)*main_x_fixp + (1)*main_x_add_double + (-1)*C5_main_x_add<=1)
solver.Add( + (1)*main_x_double + (1)*main_x_add_fixp + (-1)*C6_main_x_add<=1)
solver.Add( + (1)*main_x_float + (1)*main_x_add_double + (-1)*C7_main_x_add<=1)
solver.Add( + (1)*main_x_double + (1)*main_x_add_float + (-1)*C8_main_x_add<=1)
main_y_add_fixbits = solver.IntVar(0, 28, 'main_y_add_fixbits')
main_y_add_fixp = solver.IntVar(0, 1, 'main_y_add_fixp')
main_y_add_float = solver.IntVar(0, 1, 'main_y_add_float')
main_y_add_double = solver.IntVar(0, 1, 'main_y_add_double')
solver.Add( + (1)*main_y_add_fixp + (1)*main_y_add_float + (1)*main_y_add_double==1)
solver.Add( + (1)*main_y_add_fixbits + (-10000)*main_y_add_fixp<=0)
C1_main_y_add = solver.IntVar(0, 1, 'C1_main_y_add')
C2_main_y_add = solver.IntVar(0, 1, 'C2_main_y_add')
solver.Add( + (1)*main_y_fixbits + (-1)*main_y_add_fixbits + (-10000)*C1_main_y_add<=0)
solver.Add( + (-1)*main_y_fixbits + (1)*main_y_add_fixbits + (-10000)*C2_main_y_add<=0)
C3_main_y_add = solver.IntVar(0, 1, 'C3_main_y_add')
C4_main_y_add = solver.IntVar(0, 1, 'C4_main_y_add')
C5_main_y_add = solver.IntVar(0, 1, 'C5_main_y_add')
C6_main_y_add = solver.IntVar(0, 1, 'C6_main_y_add')
C7_main_y_add = solver.IntVar(0, 1, 'C7_main_y_add')
C8_main_y_add = solver.IntVar(0, 1, 'C8_main_y_add')
solver.Add( + (1)*main_y_fixp + (1)*main_y_add_float + (-1)*C3_main_y_add<=1)
solver.Add( + (1)*main_y_float + (1)*main_y_add_fixp + (-1)*C4_main_y_add<=1)
solver.Add( + (1)*main_y_fixp + (1)*main_y_add_double + (-1)*C5_main_y_add<=1)
solver.Add( + (1)*main_y_double + (1)*main_y_add_fixp + (-1)*C6_main_y_add<=1)
solver.Add( + (1)*main_y_float + (1)*main_y_add_double + (-1)*C7_main_y_add<=1)
solver.Add( + (1)*main_y_double + (1)*main_y_add_float + (-1)*C8_main_y_add<=1)
main_add_fixbits = solver.IntVar(0, 26, 'main_add_fixbits')
main_add_fixp = solver.IntVar(0, 1, 'main_add_fixp')
main_add_float = solver.IntVar(0, 1, 'main_add_float')
main_add_double = solver.IntVar(0, 1, 'main_add_double')
solver.Add( + (1)*main_add_fixp + (1)*main_add_float + (1)*main_add_double==1)
solver.Add( + (1)*main_add_fixbits + (-10000)*main_add_fixp<=0)
solver.Add( + (1)*main_x_add_fixp + (-1)*main_y_add_fixp==0)
solver.Add( + (1)*main_x_add_float + (-1)*main_y_add_float==0)
solver.Add( + (1)*main_x_add_double + (-1)*main_y_add_double==0)
solver.Add( + (1)*main_x_add_fixbits + (-1)*main_y_add_fixbits==0)
solver.Add( + (1)*main_x_add_fixp + (-1)*main_add_fixp==0)
solver.Add( + (1)*main_x_add_float + (-1)*main_add_float==0)
solver.Add( + (1)*main_x_add_double + (-1)*main_add_double==0)
solver.Add( + (1)*main_x_add_fixbits + (-1)*main_add_fixbits==0)
main_add__fixbits = solver.IntVar(0, 26, 'main_add__fixbits')
main_add__fixp = solver.IntVar(0, 1, 'main_add__fixp')
main_add__float = solver.IntVar(0, 1, 'main_add__float')
main_add__double = solver.IntVar(0, 1, 'main_add__double')
solver.Add( + (1)*main_add__fixp + (1)*main_add__float + (1)*main_add__double==1)
solver.Add( + (1)*main_add__fixbits + (-10000)*main_add__fixp<=0)
C1_main_add_ = solver.IntVar(0, 1, 'C1_main_add_')
C2_main_add_ = solver.IntVar(0, 1, 'C2_main_add_')
solver.Add( + (1)*main_add_fixbits + (-1)*main_add__fixbits + (-10000)*C1_main_add_<=0)
solver.Add( + (-1)*main_add_fixbits + (1)*main_add__fixbits + (-10000)*C2_main_add_<=0)
C3_main_add_ = solver.IntVar(0, 1, 'C3_main_add_')
C4_main_add_ = solver.IntVar(0, 1, 'C4_main_add_')
C5_main_add_ = solver.IntVar(0, 1, 'C5_main_add_')
C6_main_add_ = solver.IntVar(0, 1, 'C6_main_add_')
C7_main_add_ = solver.IntVar(0, 1, 'C7_main_add_')
C8_main_add_ = solver.IntVar(0, 1, 'C8_main_add_')
solver.Add( + (1)*main_add_fixp + (1)*main_add__float + (-1)*C3_main_add_<=1)
solver.Add( + (1)*main_add_float + (1)*main_add__fixp + (-1)*C4_main_add_<=1)
solver.Add( + (1)*main_add_fixp + (1)*main_add__double + (-1)*C5_main_add_<=1)
solver.Add( + (1)*main_add_double + (1)*main_add__fixp + (-1)*C6_main_add_<=1)
solver.Add( + (1)*main_add_float + (1)*main_add__double + (-1)*C7_main_add_<=1)
solver.Add( + (1)*main_add_double + (1)*main_add__float + (-1)*C8_main_add_<=1)
solver.Add( + (1)*result_fixp + (-1)*main_add__fixp==0)
solver.Add( + (1)*result_float + (-1)*main_add__float==0)
solver.Add( + (1)*result_double + (-1)*main_add__double==0)
solver.Add( + (1)*result_fixbits + (-1)*main_add__fixbits==0)
solver.Minimize( + (-1)*result_fixbits + (-20)*result_float + (-49)*result_double + (-1)*main_x_fixbits + (-23)*main_x_float + (-52)*main_x_double + (-1)*main_y_fixbits + (-21)*main_y_float + (-50)*main_y_double + (1)*C1_main_x_add + (1)*C2_main_x_add + (1)*C3_main_x_add + (1)*C4_main_x_add + (1)*C5_main_x_add + (1)*C6_main_x_add + (1)*C7_main_x_add + (1)*C8_main_x_add + (1)*C1_main_y_add + (1)*C2_main_y_add + (1)*C3_main_y_add + (1)*C4_main_y_add + (1)*C5_main_y_add + (1)*C6_main_y_add + (1)*C7_main_y_add + (1)*C8_main_y_add + (-1)*main_add_fixbits + (-20)*main_add_float + (-49)*main_add_double + (1)*C1_main_add_ + (1)*C2_main_add_ + (1)*C3_main_add_ + (1)*C4_main_add_ + (1)*C5_main_add_ + (1)*C6_main_add_ + (1)*C7_main_add_ + (1)*C8_main_add_)

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






















