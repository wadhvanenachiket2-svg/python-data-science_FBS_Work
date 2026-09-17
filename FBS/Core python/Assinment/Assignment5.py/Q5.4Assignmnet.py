#WAP to print Armstrong number within a given range

num = int(input("Enter the upper limit: "))
print(f"Armstrong numbers between 1 and {num} are:")

for i in range(1, num + 1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if i == sum:
        print(i, end=" ")
     