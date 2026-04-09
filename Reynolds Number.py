rho = float(input("Density (kg/m3): "))
V = float(input("Velocity (m/s): "))
D = float(input(" Diameter (m): "))
mu = float(input("Viscosity (Pa . s): "))
Re = (rho *  V * D) / mu
print("Reynolds number =", Re)