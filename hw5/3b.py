import numpy as np
from scipy.integrate import solve_ivp

Y0 = [0, 1, 0]
t_span = (0, 0.6)
t_eval = [0.2, 0.4, 0.6]

def rkf_system(t, Y):
    y0, y1, y2 = Y
    y3 = t - t * y1 + 2 * y0
    return [y1, y2, y3]
    
sol = solve_ivp(rkf_system, t_span, Y0, method='RK45', t_eval=t_eval)

h = 0.2
t = 0.6
y0_vals = np.append(Y0[0], sol.y[0, :])
y1_vals = np.append(Y0[1], sol.y[1, :])
y2_vals = np.append(Y0[2], sol.y[2, :])
y3_vals = [t - t * y1 + 2 * y0 for y0, y1 in zip(y0_vals, y1_vals)]
    
def adams_moulton(h, t, y0, y1, y2, y3):
    y0_pred = y0[-1] + (h / 24.0) * (55 * y1[-1] - 59 * y1[-2] + 37 * y1[-3] - 9 * y1[-4])
    y1_pred = y1[-1] + (h / 24.0) * (55 * y2[-1] - 59 * y2[-2] + 37 * y2[-3] - 9 * y2[-4])
    y2_pred = y2[-1] + (h / 24.0) * (55 * y3[-1] - 59 * y3[-2] + 37 * y3[-3] - 9 * y3[-4])
    
    y0_corr = y0[-1] + (h / 24.0) * (9 * y1_pred + 19 * y1[-1] - 5 * y1[-2] + y1[-3])
    y1_corr = y1[-1] + (h / 24.0) * (9 * y2_pred + 19 * y2[-1] - 5 * y2[-2] + y2[-3])
    y3_corr = t - t * y1_corr + 2 * y0_corr
    y2_corr = y2[-1] + (h / 24.0) * (9 * y3_corr + 19 * y3[-1] - 5 * y3[-2] + y3[-3])
    
    return y0_corr, y1_corr, y2_corr, y3_corr

while t < 1.0:
    y0_corr, y1_corr, y2_corr, y3_corr = adams_moulton(h, t, y0_vals, y1_vals, y2_vals, y3_vals)
    y0_vals = np.append(y0_vals, y0_corr)
    y1_vals = np.append(y1_vals, y1_corr)
    y2_vals = np.append(y2_vals, y2_corr)
    t += h
    
print(y0_vals[-1])
