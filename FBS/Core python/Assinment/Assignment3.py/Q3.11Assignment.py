#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

AMOUNT = 0
for i in range(5):
    age = int(input("Enter the age of person {}: ".format(i + 1)))
    ticket_amount = float(input("Enter the ticket amount for person {}: ".format(i + 1)))

    if age < 12:
        discount = 0.30 * ticket_amount
    elif age > 59:
        discount = 0.50 * ticket_amount
    else:
        discount = 0

    total_amount = ticket_amount - discount
    AMOUNT += total_amount

print("The total amount for all tickets is: ${:.2f}".format(AMOUNT))
