F = float(input("friction factor: "))
L = float(input("lenght (m): "))
D= float(input("Diameter (m): "))
rho = float(input("Density (kg/m3): "))
V = float(input("Velocity (m/s):"))
dp = F * (L/D) * 0.5 * rho * V ** 2
print("pressure drop Darcy - Weisbach =", dp, "Pa")