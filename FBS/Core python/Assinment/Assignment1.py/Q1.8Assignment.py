## Write a program to convert days into years, weeks and days.

days=int(input("Enter number of days:"))

year=days//365
weeks=days//7
remaining_days=days%7

print("Years:",year)
print("Weeks:",weeks)
print("Days:",remaining_days)
