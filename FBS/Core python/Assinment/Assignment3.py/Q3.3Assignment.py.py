#Write a program to input angles of a triangle and check whether triangle is valid or not.
a1 = int(input("Enter first angle: "))
a2 = int(input("Enter second angle: "))
a3 = int(input("Enter third angle: "))
if a1 + a2 + a3 == 180:
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")