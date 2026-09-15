#WAP to print sum of series upto n.
sum = 0
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    sum += i
print("The sum of the series is:", sum)
