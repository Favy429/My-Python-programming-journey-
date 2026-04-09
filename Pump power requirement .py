rho = float(input("Density (kg/m3): "))
Q = float(input("flow rate (m3/s): "))
H = float(input("Head (m): "))
eta = float(input("Efficiency (0-1): "))
g = 9.81
P = (rho * g * Q * H) / eta
print("pump power =", P, "W")