from ortools.linear_solver import pywraplp


def main():
    # Create the mip solver with the CBC backend.
    solver = pywraplp.Solver('simple_mip_program',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    infinity = solver.infinity()
    M = 10000
    #x = solver.IntVar(0.0, infinity, 'x')
    #y = solver.IntVar(0.0, infinity, 'y')
    #solver.Add(x + 7 * y <= 17.5)
    #solver.Add(x <= 3.5)
    #solver.Minimize(x + 10 * y)
    
    
    #variavles definitions (loads does not have actual variable definitions)
    x_a = solver.IntVar(0.0, 24, 'x_a')
    x_b = solver.IntVar(0.0, 24, 'x_b')
    x_c = solver.IntVar(0.0, 22, 'x_c')
    
   
    
    
    
    
    #HANDLING SUM
    #clone for use in sum
    x_a_sum = solver.IntVar(0.0, 24, 'x_a_sum')
    x_b_sum = solver.IntVar(0.0, 24, 'x_b_sum')
    x_res_sum = solver.IntVar(0.0, infinity, 'x_res_sum')
    
    #sum properties
    solver.Add(x_a_sum == x_b_sum)
    solver.Add(x_a_sum == x_res_sum)
    
     #casting cost handling
    c1_a_to_a_sum = solver.IntVar(0.0, 1.01, 'c1_a_to_a_sum')
    c2_a_to_a_sum = solver.IntVar(0.0, 1.01, 'c2_a_to_a_sum')
    solver.Add((x_a-x_a_sum) <= M * c1_a_to_a_sum)
    solver.Add((x_a_sum -x_a) <= M * c2_a_to_a_sum)
    
    
    
    
    c1_b_to_b_sum = solver.IntVar(0.0, 1.01, 'c1_b_to_b_sum')
    c2_b_to_b_sum = solver.IntVar(0.0, 1.01, 'c2_b_to_b_sum')
    solver.Add((x_b-x_b_sum) <= M * c1_b_to_b_sum)
    solver.Add((x_b_sum -x_b) <= M * c2_b_to_b_sum)
    
    
    
    
    
    #HANDLING STORE
    #doesn't need additional variables where to store results
    x_res_sum_store = solver.IntVar(0.0, infinity, 'x_res_sum_store')
    solver.Add(x_res_sum_store == x_c)
    
    c1_res_to_res_store = solver.IntVar(0.0, 1.01, 'c1_res_to_res_store')
    c2_res_to_res_store = solver.IntVar(0.0, 1.01, 'c2_res_to_res_store')
    solver.Add((x_res_sum-x_res_sum_store) <= M * c1_res_to_res_store)
    solver.Add((x_res_sum_store -x_res_sum) <= M * c2_res_to_res_store)
    
    
    
    #COST FUNCTION!
    W = 0.09
    B_a = 24
    B_b = 24
    B_c = 22
    solver.Minimize(W*(c1_a_to_a_sum + c2_a_to_a_sum + c1_b_to_b_sum + c2_b_to_b_sum + c1_res_to_res_store + c2_res_to_res_store)+
                    (1-W) * ((B_a - x_a) + (B_b - x_b) + (B_c - x_c)))
    
    



    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        
        for v in solver.variables():
            print(v, v.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())


if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
