import random

name = input("What's your name?")
print("Hello, " + name)

compName = input("What is the computer's name?")
print("Your challenger is " + compName)

compList = ["Rock", "Paper", "Scissors"]

def rockPaperScissors(fname, fCompName):
    playagain = True
    while playagain == True:
        computerChoice = random.choice(compList)
        playagain = False
        humanInput = input("Rock, Paper, or Scissors? Please remember that you can only respond with 'Rock', 'Paper' or 'Scissors'.")
        if computerChoice == compList[0]:
            if humanInput == " Rock":
                print("Tie! Try again! You and your opponent both chose rock!")
                playagain = True
            elif humanInput == "Paper":
                print(fname + " wins! Paper covers rock!")
                computerWin = False
            elif humanInput == "Scissors":
                print(fCompName + " wins! Rock smashes scissors!")
                computerWin = True
            else:
                print("Please only use the terms 'Rock', 'Paper' or 'Scissors as said exactly in this sentence.")
                playagain = True
        elif computerChoice == compList[1]:
            if humanInput == "Rock":
                print(fCompName + " wins! Paper covers rock!")
                computerWin = True
            elif humanInput == "Paper":
                print("Tie! Try again! You and your opponent both chose paper!")
                playagain = True
            elif humanInput == "Scissors":
                print(fname + " wins! Scissors cuts paper!")
                computerWin = False
            else:
                print("Please only use the terms 'Rock', 'Paper' or 'Scissors as said exactly in this sentence.")
                playagain = True
        elif computerChoice == compList[2]:
            if humanInput == "Rock":
                print(fname + " wins! Rock smashes scissors!")
                computerWin = False
            elif humanInput == "Paper":
                print(fCompName + " wins! Scissors cuts paper!")
                computerWin = True
            elif humanInput == "Scissors":
                print("Tie! Try again! You and your opponent both chose scissors!")
                playagain = True
            else:
                print("Please only use the terms 'Rock', 'Paper' or 'Scissors as said exactly in this sentence.")
                playagain = True
    return computerWin
rockPaperScissors(name, compName)