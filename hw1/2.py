import numpy

def f(x):
	return x * numpy.sin((x-2)/(x-1))

def secant(a, b, f, tol):
	iter = 0
	while abs(f(b)) > tol:
		iter += 1
		a, b = b, b - f(b) * (b - a) / (f(b) - f(a))
	return b, iter

print(secant(0.945, 0.95, f, 1e-5))
print(secant(0.95, 0.955, f, 1e-5))
print(secant(0.955, 0.96, f, 1e-5))
print(secant(0.96, 0.965, f, 1e-5))