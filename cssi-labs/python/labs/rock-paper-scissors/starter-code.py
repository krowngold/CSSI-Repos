import math
import random

numRounds = raw_input("How many rounds do you want to play?")
playerWins = 0;
compWins = 0;
choices = ["rock", "paper", "scissors"]
compObject = ""

def compTurn():
    compObject = choices[math.floor(0.1 * random.randint(0,10)*len(choices))]
    return compObject

def chooseWinner(playerInput, compInput):

    if (playerInput.lower() == "rock" and compInput.lower() == "scissors"):
        print "Rock beats scissors!"
        print "You won this round."
        # playerWins+=1
        return True
    elif (playerInput.lower() == "scissors" and compInput.lower() == "paper"):
        print "Scissors beats paper!"
        print "You won this round."
        # playerWins+=1
        return True
    elif (playerInput.lower() == "paper" and compInput.lower() == "rock"):
        print "Paper beats rock!"
        print "You won this round."
        # playerWins+=1
        return True
    elif(playerInput.lower() == compInput.lower()):
        return None
    else:
        print "The computer wins this round."
        # compWins+=1
        return False

for i in range(int(numRounds)):
    playerObject = raw_input("Rock, paper, or scissors?")
    listSelection = math.floor(random.randint(0,10)*0.1*len(choices))
    compObject = choices[int(listSelection)]
    print "You played " + playerObject + ", and the computer played " +compObject + "."
    if(chooseWinner(playerObject, compObject)):
        playerWins += 1
    elif(chooseWinner(playerObject, compObject) == None):
        print "It's a draw. Nobody wins this round."
    else:
        compWins +=1
    print "You have " + str(playerWins) + " wins. The computer has " + str(compWins) + " wins."

if (playerWins > compWins):
    print "Congratulations! You beat the computer!"
elif (playerWins == compWins):
    print "It's a tie. How boring."
else:
    print "You couldn't beat a computer. Disappointing."
