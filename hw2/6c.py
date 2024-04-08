import numpy as np

A = np.array([[2, -1.99], [-1.99, 2]])
B = np.array([0, 0])

def jacobi(A, b, x0, tol):
    x = x0.copy()
    n = len(x)
    iter = 0
    
    while True:
        iter += 1
        x_old = x.copy()
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i, j] * x_old[j]
            x[i] = s / A[i, i]
        if np.linalg.norm(x - x_old) < tol:
            break
        if iter > 10000:
            break
    
    return x, iter

def gauss_seidel(A, b, x0, tol):
    x = x0.copy()
    n = len(x)
    iter = 0
    
    while True:
        iter += 1
        x_old = x.copy()
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i != j:
                    s -= A[i, j] * x[j]
            x[i] = s / A[i, i]
        if np.linalg.norm(x - x_old) < tol:
            break
    
    return x, iter

print("Jacobi:")
print(jacobi(A, B, np.array([1.0, 1.0]), 1e-5))
print(jacobi(A, B, np.array([1.0, -1.0]), 1e-5))
print(jacobi(A, B, np.array([-1.0, 1.0]), 1e-5))
print(jacobi(A, B, np.array([2.0, 5.0]), 1e-5))
print(jacobi(A, B, np.array([5.0, 2.0]), 1e-5))
print("Gauss-Seidel:")
print(gauss_seidel(A, B, np.array([1.0, 1.0]), 1e-5))
print(gauss_seidel(A, B, np.array([1.0, -1.0]), 1e-5))
print(gauss_seidel(A, B, np.array([-1.0, 1.0]), 1e-5))
print(gauss_seidel(A, B, np.array([2.0, 5.0]), 1e-5))
print(gauss_seidel(A, B, np.array([5.0, 2.0]), 1e-5))