import numpy

def f(x):
	return (x-2)**3 * (x-4)**2

def get_mid(a, b):
	return a + (b - a) / 2

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

def secant(a, b, f, tol):
	iter = 0
	while abs(f(b)) > tol:
		iter += 1
		a, b = b, b - f(b) * (b - a) / (f(b) - f(a))
	return b, iter

print(bisection(2.1, 5, f, 1e-5))
print(secant(4.6, 5, f, 1e-5))