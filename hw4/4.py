import numpy as np

def f(x):
    return np.where(x != 0, np.sin(x)/x, 1)

def simpsons(f, a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = y[0] + y[-1]
    for i in range(1, n, 2):
        S += 4 * y[i]
    for i in range(2, n-1, 2):
        S += 2 * y[i]
    return S * h / 3

result_h0_5 = simpsons(f, 0, 1, 0.5)
result_h0_25 = simpsons(f, 0, 1, 0.25)

print(f"result of h=0.5: {result_h0_5}")
print(f"result of h=0.25: {result_h0_25}")

from scipy.integrate import quad
true_value, _ = quad(f, 0, 1)
print(f"true value: {true_value}")

error_h0_5 = abs(true_value - result_h0_5)
error_h0_25 = abs(true_value - result_h0_25)
print(f"error of h=0.5: {error_h0_5}")
print(f"error of h=0.25: {error_h0_25}")

for i in range(1000):
    p = 2 ** (i+2)
    result_extrapolated = (p * result_h0_25 - result_h0_5) / (p - 1)
    error_extrapolated = abs(true_value - result_extrapolated)
    if error_extrapolated < error_h0_25:
        print(f"result after extrapolated: {result_extrapolated}")
        print(f"error after extrapolated: {error_extrapolated}")
        print(f"order of error: O(h^{i+1})")
        break