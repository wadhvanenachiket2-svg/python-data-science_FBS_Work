#Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))
if num < 100 or num > 999:
    print("Please enter a valid 3-digit number.")
else:
    str_num = str(num)
    if str_num == str_num[::-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
        