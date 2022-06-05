from random import  randint

guessNumber=int(input("Enter your guess between 1 to 5:"))
randomNumber=randint(1,5)
if guessNumber==randomNumber:
    print("you are won")
else:
    print("you have lost")
    print("Random number was:",randomNumber)
"""
##
from random import  randint

for x in range(1,11):
    guessNumber=int(input("Enter your guess between 1 to 10:"))
    randomNumber=randint(1,10)
    if guessNumber==randomNumber:
       print("you are won")
    else:
       print("you have lost")
       print("Random number was:",randomNumber)
    """