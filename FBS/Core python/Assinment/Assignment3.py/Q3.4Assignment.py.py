#Write a program to check if the given number is positive or negative.
num = int(input('Enter number'))
if(num>0):
    if(num%2==0):
        print('positive and even')
    else:
        print('positive and odd')
else:
    if(num%2==0):
        print('negative and even')
    else:
        print('negative and odd')

   