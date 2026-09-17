#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

cases = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))

total_amount = 0

for i in range(cases):
    age = int(input(f"Enter age of passenger {i+1}: "))
    if age < 12:
        amount = ticket_cost * 0.7  # Apply 30% discount
    elif age > 59:
        amount = ticket_cost * 0.5  # Apply 50% discount
    else:
        amount = ticket_cost  # No discount
    total_amount += amount

print(f"Total amount to be paid: {total_amount}")