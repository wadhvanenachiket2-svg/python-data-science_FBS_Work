#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

id = "admin"
password = "admin123"
for i in range(3):
    user_id = input("Enter User ID: ")
    user_password = input("Enter Password: ")

    if user_id == id and user_password == password:
        print("Login successful!")
        break
    else:
        print("Incorrect User ID or Password. Please try again.")
else:
    print("Maximum attempts exceeded. Program terminated.")
