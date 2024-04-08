import numpy as np

A = np.array([[7, -3, 4], [2, 5, 3], [-3, 2, 6]])
B = np.array([6, -5, 2])
x0 = np.array([0.0, 0.0, 0.0])

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
    
    return x, iter

print(jacobi(A, B, x0, 1e-5))