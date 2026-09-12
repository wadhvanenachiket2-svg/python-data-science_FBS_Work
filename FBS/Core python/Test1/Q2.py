## Write a program to calculate simple interest based on Principal, Rate and Time
##(SI = P*R*T/100)
P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time in years: "))
SI = (P * R * T) / 100
print("Simple Interest:", SI)
