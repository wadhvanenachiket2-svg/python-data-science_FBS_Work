##Write a program to check whether the triangle is equilateral, isosceles or scalene
##triangle.
int1 = int(input("Enter the first side of the triangle: "))
int2 = int(input("Enter the second side of the triangle: "))
int3 = int(input("Enter the third side of the triangle: "))
if int1 == int2 == int3:
        print("The triangle is equilateral.")
elif (int1 == int2 or int1 == int3 or int2 == int3):
        print("The triangle is isosceles.")
else:
        print("The triangle is scalene.")