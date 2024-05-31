import numpy as np

x0 = 0
y0 = 2
h = 0.01

def f(x, y):
    return np.sin(x) + y

def modified_euler(xn):
    steps = int((xn - x0) / h)
    x = x0
    y = y0
    for _ in range(steps):
        z1 = f(x, y)
        z2 = f(x + h, y + h * z1)
        y += h * (z1 + z2)/2.0
        x += h
    return y

print(modified_euler(0.1).round(5))
print(modified_euler(0.5).round(5))