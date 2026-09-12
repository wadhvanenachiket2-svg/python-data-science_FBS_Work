## Write a program to enter P, T, R and calculate Compound Interest.

principle_amount=int(input("Enter principle amount:"))
time_period=int(input("Enter time period:"))
rate_of_interest=int(input("Enter rate of interest:"))
compound_interest=principle_amount*(1+(rate_of_interest/100))**time_period
print("Compound Interest is:",compound_interest)



