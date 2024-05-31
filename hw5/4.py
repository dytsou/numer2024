import numpy as np

PI = np.pi
N = 4
h = (0.5*PI - 0) / N # 1/8 * pi
x = np.linspace(0, 0.5*PI, N+1)

A = np.zeros((N+1, N+1))
b = np.zeros(N+1)

for i in range(1, N):
    A[i][i-1] = 1
    A[i][i] = -2 - h**2
    A[i][i+1] = 1

A[0][0] = h**2
A[0][1] = 2
b[0] = 4*h

A[N][N-1] = 2
A[N][N] = -4 + h**2
b[N] = 2*h

y = np.linalg.solve(A, b)

print(y)