import numpy as np
from scipy.integrate import nquad

bounds = [[-0.2, 1.4], [0.4, 2.6]]
h = 0.1

def f(x, y):
    return np.exp(x) * np.sin(2*y)

def trapezoidal(f, bounds, h):
    a, b = bounds[0]
    c, d = bounds[1]
    Nx = int((b - a) / h)
    Ny = int((d - c) / h)
    x = np.linspace(a, b, Nx + 1)
    y = np.linspace(c, d, Ny + 1)
    result = 0.0
    for i in range(Nx + 1):
        for j in range(Ny + 1):
            is_x_edge = (i == 0 or i == Nx)
            is_y_edge = (j == 0 or j == Ny)
            x_coeff = 1.0 if is_x_edge else 2.0
            y_coeff = 1.0 if is_y_edge else 2.0
            result += x_coeff * y_coeff * f(x[i], y[j])
    return result * (( h / 2.0 ) ** 2)

def simpsons(f, bounds, h):
    a, b = bounds[0]
    c, d = bounds[1]
    Nx = int((b - a) / h)
    Ny = int((d - c) / h)
    x = np.linspace(a, b, Nx + 1)
    y = np.linspace(c, d, Ny + 1)
    result = 0.0
    for i in range(Nx + 1):
        for j in range(Ny + 1):
            is_x_edge = (i == 0 or i == Nx)
            is_y_edge = (j == 0 or j == Ny)
            x_coeff = 1.0 if is_x_edge else 2.0 if (i % 2 == 0) else 4.0
            y_coeff = 1.0 if is_y_edge else 2.0 if (j % 2 == 0) else 4.0
            result += x_coeff * y_coeff * f(x[i], y[j])
    return result * ((h/3.0)**2)

def gaussian(f, bounds):
    a, b = bounds[0]
    c, d = bounds[1]
    
    # Gauss quadrature points and weights for 3 points, which is hardcoded
    points = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
    weights = [5/9, 8/9, 5/9]
    
    def map_to_interval(x, a, b): # maps [-1, 1] to [a, b]
        return 0.5 * (b - a) * x + 0.5 * (b + a)
    
    result = 0.0
    for i in range(3):
        for j in range(3):
            x = map_to_interval(points[i], a, b)
            y = map_to_interval(points[j], c, d)
            result += weights[i] * weights[j] * f(x, y)
    return result * ((b - a) / 2.0) * ((d - c) / 2.0)

def integral(f, bounds):
    a, b = bounds[0]
    c, d = bounds[1]
    result, _ = nquad(f, [[a, b], [c, d]])
    return result

if __name__ == "__main__":
    trapezoidal_result = trapezoidal(f, bounds, h)
    simpsons_result = simpsons(f, bounds, h)
    gaussian_result = gaussian(f, bounds)
    true_value = integral(f, bounds)
    print("Trapezoidal: ", trapezoidal_result)
    print("Simpsons: ", simpsons_result)
    print("Gaussian: ", gaussian_result)
    print("True value: ", true_value)
    print("Trapezoidal error: ", np.abs(trapezoidal_result - true_value))
    print("Simpsons error: ", np.abs(simpsons_result - true_value))
    print("Gaussian error: ", np.abs(gaussian_result - true_value))
    