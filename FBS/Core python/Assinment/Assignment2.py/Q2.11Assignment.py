##Write a program to accept an integer amount from user and tell minimum 
#number of notes needed for representing that amount
amount=int(input("Enter amount:"))
notes_2000=amount//2000
amount=amount%2000
notes_500=amount//500
amount=amount%500
notes_100=amount//100
amount=amount%100
notes_50=amount//50
amount=amount%50
notes_20=amount//20
amount=amount%20
notes_10=amount//10
amount=amount%10
notes_5=amount//5
amount=amount%5
notes_2=amount//2
amount=amount%2
notes_1=amount//1
print("Number of 2000 notes:",notes_2000)
print("Number of 500 notes:",notes_500)
print("Number of 100 notes:",notes_100)
print("Number of 50 notes:",notes_50)
print("Number of 20 notes:",notes_20)
print("Number of 10 notes:",notes_10)
print("Number of 5 notes:",notes_5)
print("Number of 2 notes:",notes_2)
print("Number of 1 notes:",notes_1)