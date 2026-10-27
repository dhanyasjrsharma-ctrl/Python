import random

number=random.randint(1,100)
while True:
 counts+=1
 user  =int(input("enter your no."))
 if user < number:
    print(f"too low, guess high")

 elif user>number:
    print("too high , guess lower value")
 elif user==number:
    print("you won mann...")
    print(f"you took {counts} to win!")
    break
 
 #what if user have only 5 chances to guess the number

import random

number=random.randint(1,100)
counts=0
while counts<5:
 user = int(input("enter your no."))
 counts+=1
 if user < number:
    print(f"too low, guess high")

 elif user>number:
    print("too high , guess lower value")
 elif user==number:
    print("you won mann...")
 if counts==5:
    print("you lost the game, chances expired")
    break