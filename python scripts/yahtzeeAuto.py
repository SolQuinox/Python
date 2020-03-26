import random

yahtzee = True

tries = 0

while yahtzee == True:
    die1 = random.randint(0, 6)
    die2 = random.randint(0, 6)
    die3 = random.randint(0, 6)
    die4 = random.randint(0, 6)
    die5 = random.randint(0, 6)
    if die1 == die2 and die2 == die3 and die3 == die4 and die4 == die5:
        print("You win! It took you" , tries , "tries to get a Yahtzee.")
        print("Your lucky number was" , die1)
        yahtzee = False
    else:
        print("Try again! Your numbers were" , die1 , die2 , die3 , die4 , die5)
        tries = tries + 1
