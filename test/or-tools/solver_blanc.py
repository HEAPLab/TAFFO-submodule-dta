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

main_a_fixbits = solver.IntVar(0, 27, 'main_a_fixbits')
main_a_fixp = solver.IntVar(0, 1, 'main_a_fixp')
main_a_float = solver.IntVar(0, 1, 'main_a_float')
main_a_double = solver.IntVar(0, 1, 'main_a_double')
solver.Add( + (1)*main_a_fixp + (1)*main_a_float + (1)*main_a_double==1)
solver.Add( + (1)*main_a_fixbits + (-10000)*main_a_fixp<=0)
main_b_fixbits = solver.IntVar(0, 30, 'main_b_fixbits')
main_b_fixp = solver.IntVar(0, 1, 'main_b_fixp')
main_b_float = solver.IntVar(0, 1, 'main_b_float')
main_b_double = solver.IntVar(0, 1, 'main_b_double')
solver.Add( + (1)*main_b_fixp + (1)*main_b_float + (1)*main_b_double==1)
solver.Add( + (1)*main_b_fixbits + (-10000)*main_b_fixp<=0)
main_a_mul_fixbits = solver.IntVar(0, 27, 'main_a_mul_fixbits')
main_a_mul_fixp = solver.IntVar(0, 1, 'main_a_mul_fixp')
main_a_mul_float = solver.IntVar(0, 1, 'main_a_mul_float')
main_a_mul_double = solver.IntVar(0, 1, 'main_a_mul_double')
solver.Add( + (1)*main_a_mul_fixp + (1)*main_a_mul_float + (1)*main_a_mul_double==1)
solver.Add( + (1)*main_a_mul_fixbits + (-10000)*main_a_mul_fixp<=0)
C1_main_a_mul = solver.IntVar(0, 1, 'C1_main_a_mul')
C2_main_a_mul = solver.IntVar(0, 1, 'C2_main_a_mul')
solver.Add( + (1)*main_a_fixbits + (-1)*main_a_mul_fixbits + (-10000)*C1_main_a_mul<=0)
solver.Add( + (-1)*main_a_fixbits + (1)*main_a_mul_fixbits + (-10000)*C2_main_a_mul<=0)
C3_main_a_mul = solver.IntVar(0, 1, 'C3_main_a_mul')
C4_main_a_mul = solver.IntVar(0, 1, 'C4_main_a_mul')
C5_main_a_mul = solver.IntVar(0, 1, 'C5_main_a_mul')
C6_main_a_mul = solver.IntVar(0, 1, 'C6_main_a_mul')
C7_main_a_mul = solver.IntVar(0, 1, 'C7_main_a_mul')
C8_main_a_mul = solver.IntVar(0, 1, 'C8_main_a_mul')
solver.Add( + (1)*main_a_fixp + (1)*main_a_mul_float + (-1)*C3_main_a_mul<=1)
solver.Add( + (1)*main_a_float + (1)*main_a_mul_fixp + (-1)*C4_main_a_mul<=1)
solver.Add( + (1)*main_a_fixp + (1)*main_a_mul_double + (-1)*C5_main_a_mul<=1)
solver.Add( + (1)*main_a_double + (1)*main_a_mul_fixp + (-1)*C6_main_a_mul<=1)
solver.Add( + (1)*main_a_float + (1)*main_a_mul_double + (-1)*C7_main_a_mul<=1)
solver.Add( + (1)*main_a_double + (1)*main_a_mul_float + (-1)*C8_main_a_mul<=1)
main_b_mul_fixbits = solver.IntVar(0, 30, 'main_b_mul_fixbits')
main_b_mul_fixp = solver.IntVar(0, 1, 'main_b_mul_fixp')
main_b_mul_float = solver.IntVar(0, 1, 'main_b_mul_float')
main_b_mul_double = solver.IntVar(0, 1, 'main_b_mul_double')
solver.Add( + (1)*main_b_mul_fixp + (1)*main_b_mul_float + (1)*main_b_mul_double==1)
solver.Add( + (1)*main_b_mul_fixbits + (-10000)*main_b_mul_fixp<=0)
C1_main_b_mul = solver.IntVar(0, 1, 'C1_main_b_mul')
C2_main_b_mul = solver.IntVar(0, 1, 'C2_main_b_mul')
solver.Add( + (1)*main_b_fixbits + (-1)*main_b_mul_fixbits + (-10000)*C1_main_b_mul<=0)
solver.Add( + (-1)*main_b_fixbits + (1)*main_b_mul_fixbits + (-10000)*C2_main_b_mul<=0)
C3_main_b_mul = solver.IntVar(0, 1, 'C3_main_b_mul')
C4_main_b_mul = solver.IntVar(0, 1, 'C4_main_b_mul')
C5_main_b_mul = solver.IntVar(0, 1, 'C5_main_b_mul')
C6_main_b_mul = solver.IntVar(0, 1, 'C6_main_b_mul')
C7_main_b_mul = solver.IntVar(0, 1, 'C7_main_b_mul')
C8_main_b_mul = solver.IntVar(0, 1, 'C8_main_b_mul')
solver.Add( + (1)*main_b_fixp + (1)*main_b_mul_float + (-1)*C3_main_b_mul<=1)
solver.Add( + (1)*main_b_float + (1)*main_b_mul_fixp + (-1)*C4_main_b_mul<=1)
solver.Add( + (1)*main_b_fixp + (1)*main_b_mul_double + (-1)*C5_main_b_mul<=1)
solver.Add( + (1)*main_b_double + (1)*main_b_mul_fixp + (-1)*C6_main_b_mul<=1)
solver.Add( + (1)*main_b_float + (1)*main_b_mul_double + (-1)*C7_main_b_mul<=1)
solver.Add( + (1)*main_b_double + (1)*main_b_mul_float + (-1)*C8_main_b_mul<=1)
main_mul_fixbits = solver.IntVar(0, 26, 'main_mul_fixbits')
main_mul_fixp = solver.IntVar(0, 1, 'main_mul_fixp')
main_mul_float = solver.IntVar(0, 1, 'main_mul_float')
main_mul_double = solver.IntVar(0, 1, 'main_mul_double')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_float + (1)*main_mul_double==1)
solver.Add( + (1)*main_mul_fixbits + (-10000)*main_mul_fixp<=0)
solver.Add( + (1)*main_a_mul_float + (-1)*main_b_mul_float==0)
solver.Add( + (1)*main_a_mul_double + (-1)*main_b_mul_double==0)
solver.Add( + (1)*main_a_mul_fixbits + (-1)*main_b_mul_fixbits==0)
solver.Add( + (1)*main_a_mul_float + (-1)*main_mul_float==0)
solver.Add( + (1)*main_a_mul_double + (-1)*main_mul_double==0)
solver.Add( + (1)*main_a_mul_fixbits + (-1)*main_mul_fixbits==0)
main_mul_div_fixbits = solver.IntVar(0, 26, 'main_mul_div_fixbits')
main_mul_div_fixp = solver.IntVar(0, 1, 'main_mul_div_fixp')
main_mul_div_float = solver.IntVar(0, 1, 'main_mul_div_float')
main_mul_div_double = solver.IntVar(0, 1, 'main_mul_div_double')
solver.Add( + (1)*main_mul_div_fixp + (1)*main_mul_div_float + (1)*main_mul_div_double==1)
solver.Add( + (1)*main_mul_div_fixbits + (-10000)*main_mul_div_fixp<=0)
C1_main_mul_div = solver.IntVar(0, 1, 'C1_main_mul_div')
C2_main_mul_div = solver.IntVar(0, 1, 'C2_main_mul_div')
solver.Add( + (1)*main_mul_fixbits + (-1)*main_mul_div_fixbits + (-10000)*C1_main_mul_div<=0)
solver.Add( + (-1)*main_mul_fixbits + (1)*main_mul_div_fixbits + (-10000)*C2_main_mul_div<=0)
C3_main_mul_div = solver.IntVar(0, 1, 'C3_main_mul_div')
C4_main_mul_div = solver.IntVar(0, 1, 'C4_main_mul_div')
C5_main_mul_div = solver.IntVar(0, 1, 'C5_main_mul_div')
C6_main_mul_div = solver.IntVar(0, 1, 'C6_main_mul_div')
C7_main_mul_div = solver.IntVar(0, 1, 'C7_main_mul_div')
C8_main_mul_div = solver.IntVar(0, 1, 'C8_main_mul_div')
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_div_float + (-1)*C3_main_mul_div<=1)
solver.Add( + (1)*main_mul_float + (1)*main_mul_div_fixp + (-1)*C4_main_mul_div<=1)
solver.Add( + (1)*main_mul_fixp + (1)*main_mul_div_double + (-1)*C5_main_mul_div<=1)
solver.Add( + (1)*main_mul_double + (1)*main_mul_div_fixp + (-1)*C6_main_mul_div<=1)
solver.Add( + (1)*main_mul_float + (1)*main_mul_div_double + (-1)*C7_main_mul_div<=1)
solver.Add( + (1)*main_mul_double + (1)*main_mul_div_float + (-1)*C8_main_mul_div<=1)
main_a_div_fixbits = solver.IntVar(0, 27, 'main_a_div_fixbits')
main_a_div_fixp = solver.IntVar(0, 1, 'main_a_div_fixp')
main_a_div_float = solver.IntVar(0, 1, 'main_a_div_float')
main_a_div_double = solver.IntVar(0, 1, 'main_a_div_double')
solver.Add( + (1)*main_a_div_fixp + (1)*main_a_div_float + (1)*main_a_div_double==1)
solver.Add( + (1)*main_a_div_fixbits + (-10000)*main_a_div_fixp<=0)
C1_main_a_div = solver.IntVar(0, 1, 'C1_main_a_div')
C2_main_a_div = solver.IntVar(0, 1, 'C2_main_a_div')
solver.Add( + (1)*main_a_fixbits + (-1)*main_a_div_fixbits + (-10000)*C1_main_a_div<=0)
solver.Add( + (-1)*main_a_fixbits + (1)*main_a_div_fixbits + (-10000)*C2_main_a_div<=0)
C3_main_a_div = solver.IntVar(0, 1, 'C3_main_a_div')
C4_main_a_div = solver.IntVar(0, 1, 'C4_main_a_div')
C5_main_a_div = solver.IntVar(0, 1, 'C5_main_a_div')
C6_main_a_div = solver.IntVar(0, 1, 'C6_main_a_div')
C7_main_a_div = solver.IntVar(0, 1, 'C7_main_a_div')
C8_main_a_div = solver.IntVar(0, 1, 'C8_main_a_div')
solver.Add( + (1)*main_a_fixp + (1)*main_a_div_float + (-1)*C3_main_a_div<=1)
solver.Add( + (1)*main_a_float + (1)*main_a_div_fixp + (-1)*C4_main_a_div<=1)
solver.Add( + (1)*main_a_fixp + (1)*main_a_div_double + (-1)*C5_main_a_div<=1)
solver.Add( + (1)*main_a_double + (1)*main_a_div_fixp + (-1)*C6_main_a_div<=1)
solver.Add( + (1)*main_a_float + (1)*main_a_div_double + (-1)*C7_main_a_div<=1)
solver.Add( + (1)*main_a_double + (1)*main_a_div_float + (-1)*C8_main_a_div<=1)
main_div_fixbits = solver.IntVar(0, 26, 'main_div_fixbits')
main_div_fixp = solver.IntVar(0, 1, 'main_div_fixp')
main_div_float = solver.IntVar(0, 1, 'main_div_float')
main_div_double = solver.IntVar(0, 1, 'main_div_double')
solver.Add( + (1)*main_div_fixp + (1)*main_div_float + (1)*main_div_double==1)
solver.Add( + (1)*main_div_fixbits + (-10000)*main_div_fixp<=0)
solver.Add( + (1)*main_mul_div_float + (-1)*main_a_div_float==0)
solver.Add( + (1)*main_mul_div_double + (-1)*main_a_div_double==0)
solver.Add( + (1)*main_mul_div_fixbits + (-1)*main_a_div_fixbits==0)
solver.Add( + (1)*main_mul_div_float + (-1)*main_div_float==0)
solver.Add( + (1)*main_mul_div_double + (-1)*main_div_double==0)
solver.Add( + (1)*main_mul_div_fixbits + (-1)*main_div_fixbits==0)
main_a_cmp_fixbits = solver.IntVar(0, 27, 'main_a_cmp_fixbits')
main_a_cmp_fixp = solver.IntVar(0, 1, 'main_a_cmp_fixp')
main_a_cmp_float = solver.IntVar(0, 1, 'main_a_cmp_float')
main_a_cmp_double = solver.IntVar(0, 1, 'main_a_cmp_double')
solver.Add( + (1)*main_a_cmp_fixp + (1)*main_a_cmp_float + (1)*main_a_cmp_double==1)
solver.Add( + (1)*main_a_cmp_fixbits + (-10000)*main_a_cmp_fixp<=0)
C1_main_a_cmp = solver.IntVar(0, 1, 'C1_main_a_cmp')
C2_main_a_cmp = solver.IntVar(0, 1, 'C2_main_a_cmp')
solver.Add( + (1)*main_a_fixbits + (-1)*main_a_cmp_fixbits + (-10000)*C1_main_a_cmp<=0)
solver.Add( + (-1)*main_a_fixbits + (1)*main_a_cmp_fixbits + (-10000)*C2_main_a_cmp<=0)
C3_main_a_cmp = solver.IntVar(0, 1, 'C3_main_a_cmp')
C4_main_a_cmp = solver.IntVar(0, 1, 'C4_main_a_cmp')
C5_main_a_cmp = solver.IntVar(0, 1, 'C5_main_a_cmp')
C6_main_a_cmp = solver.IntVar(0, 1, 'C6_main_a_cmp')
C7_main_a_cmp = solver.IntVar(0, 1, 'C7_main_a_cmp')
C8_main_a_cmp = solver.IntVar(0, 1, 'C8_main_a_cmp')
solver.Add( + (1)*main_a_fixp + (1)*main_a_cmp_float + (-1)*C3_main_a_cmp<=1)
solver.Add( + (1)*main_a_float + (1)*main_a_cmp_fixp + (-1)*C4_main_a_cmp<=1)
solver.Add( + (1)*main_a_fixp + (1)*main_a_cmp_double + (-1)*C5_main_a_cmp<=1)
solver.Add( + (1)*main_a_double + (1)*main_a_cmp_fixp + (-1)*C6_main_a_cmp<=1)
solver.Add( + (1)*main_a_float + (1)*main_a_cmp_double + (-1)*C7_main_a_cmp<=1)
solver.Add( + (1)*main_a_double + (1)*main_a_cmp_float + (-1)*C8_main_a_cmp<=1)
main_b_cmp_fixbits = solver.IntVar(0, 30, 'main_b_cmp_fixbits')
main_b_cmp_fixp = solver.IntVar(0, 1, 'main_b_cmp_fixp')
main_b_cmp_float = solver.IntVar(0, 1, 'main_b_cmp_float')
main_b_cmp_double = solver.IntVar(0, 1, 'main_b_cmp_double')
solver.Add( + (1)*main_b_cmp_fixp + (1)*main_b_cmp_float + (1)*main_b_cmp_double==1)
solver.Add( + (1)*main_b_cmp_fixbits + (-10000)*main_b_cmp_fixp<=0)
C1_main_b_cmp = solver.IntVar(0, 1, 'C1_main_b_cmp')
C2_main_b_cmp = solver.IntVar(0, 1, 'C2_main_b_cmp')
solver.Add( + (1)*main_b_fixbits + (-1)*main_b_cmp_fixbits + (-10000)*C1_main_b_cmp<=0)
solver.Add( + (-1)*main_b_fixbits + (1)*main_b_cmp_fixbits + (-10000)*C2_main_b_cmp<=0)
C3_main_b_cmp = solver.IntVar(0, 1, 'C3_main_b_cmp')
C4_main_b_cmp = solver.IntVar(0, 1, 'C4_main_b_cmp')
C5_main_b_cmp = solver.IntVar(0, 1, 'C5_main_b_cmp')
C6_main_b_cmp = solver.IntVar(0, 1, 'C6_main_b_cmp')
C7_main_b_cmp = solver.IntVar(0, 1, 'C7_main_b_cmp')
C8_main_b_cmp = solver.IntVar(0, 1, 'C8_main_b_cmp')
solver.Add( + (1)*main_b_fixp + (1)*main_b_cmp_float + (-1)*C3_main_b_cmp<=1)
solver.Add( + (1)*main_b_float + (1)*main_b_cmp_fixp + (-1)*C4_main_b_cmp<=1)
solver.Add( + (1)*main_b_fixp + (1)*main_b_cmp_double + (-1)*C5_main_b_cmp<=1)
solver.Add( + (1)*main_b_double + (1)*main_b_cmp_fixp + (-1)*C6_main_b_cmp<=1)
solver.Add( + (1)*main_b_float + (1)*main_b_cmp_double + (-1)*C7_main_b_cmp<=1)
solver.Add( + (1)*main_b_double + (1)*main_b_cmp_float + (-1)*C8_main_b_cmp<=1)
solver.Add( + (1)*main_a_cmp_fixp + (-1)*main_b_cmp_fixp==0)
solver.Add( + (1)*main_a_cmp_float + (-1)*main_b_cmp_float==0)
solver.Add( + (1)*main_a_cmp_double + (-1)*main_b_cmp_double==0)
solver.Add( + (1)*main_a_cmp_fixbits + (-1)*main_b_cmp_fixbits==0)
main_call16_fixbits = solver.IntVar(0, 27, 'main_call16_fixbits')
main_call16_fixp = solver.IntVar(0, 1, 'main_call16_fixp')
main_call16_float = solver.IntVar(0, 1, 'main_call16_float')
main_call16_double = solver.IntVar(0, 1, 'main_call16_double')
solver.Add( + (1)*main_call16_fixp + (1)*main_call16_float + (1)*main_call16_double==1)
solver.Add( + (1)*main_call16_fixbits + (-10000)*main_call16_fixp<=0)
solver.Minimize( + (-1)*main_a_fixbits + (-23)*main_a_float + (-52)*main_a_double + (-1)*main_b_fixbits + (-23)*main_b_float + (-52)*main_b_double + (6.7)*C1_main_a_mul + (6.7)*C2_main_a_mul + (6.1)*C3_main_a_mul + (6.3)*C4_main_a_mul + (6.2)*C5_main_a_mul + (6.5)*C6_main_a_mul + (6.4)*C7_main_a_mul + (6.6)*C8_main_a_mul + (6.7)*C1_main_b_mul + (6.7)*C2_main_b_mul + (6.1)*C3_main_b_mul + (6.3)*C4_main_b_mul + (6.2)*C5_main_b_mul + (6.5)*C6_main_b_mul + (6.4)*C7_main_b_mul + (6.6)*C8_main_b_mul + (-1)*main_mul_fixbits + (-23)*main_mul_float + (-52)*main_mul_double + (3.1)*main_mul_fixp + (3.2)*main_mul_float + (3.3)*main_mul_double + (6.7)*C1_main_mul_div + (6.7)*C2_main_mul_div + (6.1)*C3_main_mul_div + (6.3)*C4_main_mul_div + (6.2)*C5_main_mul_div + (6.5)*C6_main_mul_div + (6.4)*C7_main_mul_div + (6.6)*C8_main_mul_div + (6.7)*C1_main_a_div + (6.7)*C2_main_a_div + (6.1)*C3_main_a_div + (6.3)*C4_main_a_div + (6.2)*C5_main_a_div + (6.5)*C6_main_a_div + (6.4)*C7_main_a_div + (6.6)*C8_main_a_div + (-1)*main_div_fixbits + (-28)*main_div_float + (-57)*main_div_double + (4.1)*main_div_fixp + (4.2)*main_div_float + (4.3)*main_div_double + (6.7)*C1_main_a_cmp + (6.7)*C2_main_a_cmp + (6.1)*C3_main_a_cmp + (6.3)*C4_main_a_cmp + (6.2)*C5_main_a_cmp + (6.5)*C6_main_a_cmp + (6.4)*C7_main_a_cmp + (6.6)*C8_main_a_cmp + (6.7)*C1_main_b_cmp + (6.7)*C2_main_b_cmp + (6.1)*C3_main_b_cmp + (6.3)*C4_main_b_cmp + (6.2)*C5_main_b_cmp + (6.5)*C6_main_b_cmp + (6.4)*C7_main_b_cmp + (6.6)*C8_main_b_cmp + (-1)*main_call16_fixbits + (-22)*main_call16_float + (-51)*main_call16_double)

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






















