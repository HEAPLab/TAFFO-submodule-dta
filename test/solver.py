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

with open('model_test.py', 'r') as content_file:
    content = content_file.read()

exec(content)

# Model declaration end.


print('Number of variables =', solver.NumVariables())
print('Number of constraints =', solver.NumConstraints())
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())

    with open('model_results.txt', 'w') as model_result:
        print("__ERROR__, 0", file=model_result)
        for v in solver.variables():
            print(v, ", ", v.solution_value(), file=model_result, sep='')
else:
    print('The problem does not have an optimal solution.')
    with open('model_results.txt', 'w') as model_result:
        print("__ERROR__, 1", file=model_result)

print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())






















