##Write a program to check if user has entered correct userid and password.##
userid = input("Enter UserID: ")
password = input("Enter Password: ")
if userid == "admin" and password == "admin123":
    print("Login successful!")
else:
    print("Invalid UserID or Password.")