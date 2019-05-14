from random import randint
secretnum = randint(1,100)
print (secretnum)
usernum=int(input('Set a number in range 1-100:'))
while usernum == secretnum:
    print('You guessed the number!')
    
else: 
    print("Try again!")
    usernum=int(input('Set a number in range 1-100:'))