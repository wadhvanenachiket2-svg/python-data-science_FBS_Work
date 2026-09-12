##Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

entered_userid = input("Enter UserID: ")
entered_password = input("Enter Password: ")
if entered_userid == "admin" and entered_password == "admin123":
    import random
    random_number = random.randint(1000, 9999)
    print(f"Your captcha is: {random_number}")
    user_captcha = int(input("Please enter the captcha number: "))
    if user_captcha == random_number:
        print("Success! You have entered the correct captcha.")
    else:
        print("Failed! The captcha you entered is incorrect.")
        