#program to Find the Roots of a Quadratic Equation.

ax=int(input("Enter value of a :"))
bx=int(input("Enter valuen of b :"))
cx=int (input ("Enter value of c :"))

d=(bx**2)-(4*ax*cx)  ##Discriminant is calculate by using formula b^2-4ac.

x1=(-bx+(d**0.5))/(2*ax)  ##Root1 is calculate by using formula (-b+√d)/2a.
x2=(-bx-(d**0.5))/(2*ax)  ##Root2


print("Root1 of quadratic equation is:",x1)
print("Root2 of quadratic equation is:",x2)

