F_in = float(input("input flow (kg/s): "))
F_out = float(input("output flow (kg/s): "))
acc = float(input("accumulation (kg/s): "))
gen = F_out + acc - F_in
print("Generation term =", gen, "kg/s")