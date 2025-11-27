import random

random_number = random.randint(1, 2)

guessing = True

players_number = int(input("Guess the Number from 1-10:"))

while guessing:
    if players_number == random_number:
        print("LUCKY, HUH !?!?")
        guessing = False
    
    else:
        print("HAH, YOU FAILED")
        guessing = False
