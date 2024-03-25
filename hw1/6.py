import numpy

def f(x, y):
    return numpy.array([y - numpy.cos(x) ** 2, x ** 2 + y ** 2 - x - 2])


def newton(x, y, f, tol):
    iter = 0
    while numpy.linalg.norm(f(x, y)) > tol:
        iter += 1
        jacobian = numpy.array([[2 * numpy.cos(x) * numpy.sin(x), 1], 
                                [2 * x - 1, 2 * y]])
        delta = numpy.linalg.solve(jacobian, -f(x, y))
        x += delta[0]
        y += delta[1]
    return x, y, iter

print(newton(2, 1, f, 1e-5))