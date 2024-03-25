import numpy

def get_mid(a, b):
	return a + (b - a) / 2

def f(x):
    return x * numpy.sin((x-2)/(x-1))

def bisection(a, b, f, tol):
	iter = 0
	while (b-a) > tol:
		iter += 1
		mid = get_mid(a, b)
		if f(mid) == 0:
			break
		elif f(a) * f(mid) < 0:
			b = mid
		else:
			a = mid
	return get_mid(a, b), iter

print(bisection(0.94, 0.945, f, 1e-5))
print(bisection(0.95, 0.955, f, 1e-5))
print(bisection(0.955, 0.96, f, 1e-5))
print(bisection(0.96, 0.965, f, 1e-5))