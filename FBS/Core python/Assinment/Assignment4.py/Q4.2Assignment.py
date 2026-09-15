#WAP to print all odd numbers until n.
n = int(input("Enter a number: "))
i = 1
while(i <= n):
    if(i % 2 != 0):
        print(i)
    i += 1