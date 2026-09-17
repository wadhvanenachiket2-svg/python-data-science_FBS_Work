#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

student_count = int(input("Enter the number of students: "))

for i in range(student_count):
    print(f"Enter marks for student {i + 1}:")
    total_marks = 0
    for j in range(5):
        marks = float(input(f"Enter marks for subject {j + 1}: "))
        total_marks += marks
    percentage = (total_marks / 500) * 100
    print(f"Percentage for student {i + 1}: {percentage:.2f}%")

average_percentage = sum((sum(float(input(f"Enter marks for subject {j + 1}: ")) for j in range(5)) / 500) * 100 for i in range(student_count)) / student_count
print(f"Average percentage of students: {average_percentage:.2f}%")