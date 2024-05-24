import numpy as np
import scipy.integrate as integrate

R = np.array([[-2, 3],[-1 , 2]])

def f(x, y):
    return (x-1)**2 + (y**2)/16

def monte_carlo(f, R):
    a, b = R[0]
    c, d = R[1]
    n = 100000
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(c, d, n)
    return (b-a)*(d-c)*np.sum(f(x, y))/n

print(monte_carlo(f, R))