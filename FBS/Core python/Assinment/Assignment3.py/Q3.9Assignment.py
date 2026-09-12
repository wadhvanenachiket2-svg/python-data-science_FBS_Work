##Input 5 subject marks from user and display grade(eg.First class,Second class,Third class,Fail) based on average marks.

int_marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    int_marks.append(mark)

average = sum(int_marks) / len(int_marks)

if average >= 75:
    grade = "First Class"
elif average >= 60:
    grade = "Second Class"
elif average >= 40:
    grade = "Third Class"
else:
    grade = "Fail"

print(f"Average Marks: {average}")
print(f"Grade: {grade}")