# pump_power_plot.py

import numpy as np
import matplotlib.pyplot as plt

rho = 998    #kg/m3
H = 120     #m
eta = 40
g = 9.81

Q = np.linspace(0, 0.2, 100)
P = (rho * g * Q * H) / eta

plt.plot(Q, P)
plt.xlabel("Flow Rate (m3/s)")
plt.ylabel("Pump Power (W)")
plt.title("Pump Power vs Flow Rate")
plt.grid(True)
plt.show()