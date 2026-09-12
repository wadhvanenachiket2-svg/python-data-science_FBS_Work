##Write a program to check if person is eligible to marry or not (male age >=21 and
##female age>=18)#

person_gender = input("Enter your gender (male/female): ").strip().lower()
person_age = int(input("Enter your age: "))

if person_gender == "male":
    if person_age >= 21:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
elif person_gender == "female":
    if person_age >= 18:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
else:
    print("Invalid gender entered.")