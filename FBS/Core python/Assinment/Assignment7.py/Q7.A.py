# Number of rows for the top half of the diamond
n = 5

# Top half including the middle row
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Bottom half
for i in range(n - 1, 0, -1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()