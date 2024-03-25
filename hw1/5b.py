import numpy 

def f(x):
    return numpy.exp(x) - 2 * x**2

def g_pos(x):
    return numpy.sqrt(numpy.exp(x) / 2)

def g_neg(x):
    return -numpy.sqrt(numpy.exp(x) / 2)

def fixed_point_iteration(x0, g, tolerance):
    iter = 0
    while iter < 50:
        iter += 1
        if x0 > 1e10:
            break   
        x1 = g(x0)
        if abs(x1 - x0) < tolerance:
            print(x1, iter)
            return
        x0 = x1
    print("No convergence")


fixed_point_iteration(2.5, g_pos, 1e-5)
fixed_point_iteration(2.7, g_pos, 1e-5)