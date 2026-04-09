R = 0.082057 #L . atm/mol . K
P = float(input("pressure (atm): "))
V = float(input("Volume (L): "))
T = float(input("Temperature (K): "))
n = (P * V) / (R * T)
print("Moles of gas =", n, "mol")