##Write a program to reverse three-digit number.
num=int(input("Enter three digit number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reversed number is:",rev)