##Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#e. x - x2/3 + x3/5 - x4/7 + .... to n terms

for i in range(1, n + 1):
    # a. 1! + 2! + 3! + 4! + .....n!
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum_factorial += factorial

    # b. N + N^2 + N^3+N^4 .....+N^N
    sum_exponent += n ** i

    # c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
    sum_geometric += 2 ** (i - 1)

    # d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
    sum_series_d += (a ** i) / i

    # e. x - x2/3 + x3/5 - x4/7 + .... to n terms
    if i % 2 == 0:
        sum_series_e -= (x ** i) / (2 * i - 1)
    else:
        sum_series_e += (x ** i) / (2 * i - 1)
