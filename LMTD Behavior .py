# heat_exchanger_LMTD_plot.py

import numpy as np
import matplotlib.pyplot as plt

dT1 = 50 #ΔT1
dT2_min = 1
dT2_values = np.linspace(1, dT1 - 0.1, 100)

DTlm = (dT1 - dT2_values) / np.log(dT1 / dT2_values)

plt.plot(dT2_values, DTlm)
plt.xlabel("ΔT2 (°C)")
plt.ylabel("LMTD (°C)")
plt.title("LMTD Variation")
plt.grid(True)
plt.show()