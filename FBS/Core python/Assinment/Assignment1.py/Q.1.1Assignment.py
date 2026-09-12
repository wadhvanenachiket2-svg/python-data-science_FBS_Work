1. ##Write a program to calculate the percentage of student based on marks of any 5 
#subjects.

student1=int(input("Enter marks of subject 1:"))
student2=int(input("Enter marks of subject 2:"))
student3=int(input("Enter marks of subject 3:"))
student4=int(input("Enter marks of subject 4:"))
student5=int(input("Enter marks of subject 5:"))


total=student1+student2+student3+student4+student5
percentage=(total/500)*100
print("Percentage of student:",percentage)
