gender=input('enter gender(M/F):')
age=int(input('enter age:'))

if(gender=='F'):
    if(age>=18):
       print('Girl is eligible for marrige')
    else:
        print('Girl is not eligible for marrige')
else:
    if(age>=21):
         print('Boy is eligible for marrige')

    else:
        print('Boy is not eligible for marrige')