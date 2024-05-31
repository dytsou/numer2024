from scipy.integrate import solve_ivp

Y0 = [0, 1, 0]
t_span = (0, 0.6)
t_eval = [0.2, 0.4, 0.6]

def rkf_system(t, Y):
    y0, y1, y2 = Y
    y3 = t - t * y1 + 2 * y0
    return [y1, y2, y3]
    
sol = solve_ivp(rkf_system, t_span, Y0, method='RK45', t_eval=t_eval)
print(sol.y[0])