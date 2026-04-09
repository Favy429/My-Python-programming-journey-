import matplotlib.pyplot as plt
import numpy as np

# Enter your values here
rho = 998       # kg/m³
D = 0.05        # m
mu = 0.001      # Pa·s

velocities = np.linspace(0.1, 10, 100)
Re = (rho * velocities * D) / mu

plt.plot(velocities, Re)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Reynolds Number")
plt.title("Reynolds Number vs Velocity")
plt.grid(True)
plt.show()