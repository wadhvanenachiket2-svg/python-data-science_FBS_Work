## WAP to calculate total salary of employee based on basic, da=10% of basic, 
#ta=12% of basic, hra=15% of basic.

bsic=int(input("Enter basic salary of employee:"))
da=bsic*10/100
ta=bsic*12/100
hra=bsic*15/100
total_salary=bsic+da+ta+hra
print("Total salary of employee is:",total_salary)