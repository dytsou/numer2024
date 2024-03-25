import numpy

def f(x):
    return x ** 2 + numpy.exp(x) - 5

def muller(x1, x2, x3, f, tol):
    iter = 0
    while abs(f(x3)) > tol: 
        iter += 1
        q = (x3 - x2) / (x2 - x1)
        a = q * f(x3) - q * (1 + q) * f(x2) + q**2 * f(x1)
        b = (2 * q + 1) * f(x3) - (1 + q)**2 * f(x2) + q**2 * f(x1)
        c = (1 + q) * f(x3)
        m = x3 - (x3 - x2) * (2 * c / (b + numpy.sqrt(b**2 - 4 * a * c)))
        n = x3 - (x3 - x2) * (2 * c / (b - numpy.sqrt(b**2 - 4 * a * c)))
        if abs(f(m)) < abs(f(n)):
            x4 = m
        else:
            x4 = n
        x1, x2, x3 = x2, x3, x4
    return x3, iter

print(muller(0.5, 1, 1.5, f, 1e-5))
print(muller(-2.5, -2, -1.5, f, 1e-5))