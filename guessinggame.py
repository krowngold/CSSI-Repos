import random

randomNumber = random.randint(1,10)
userGuess = 0
win = False
turns = 0

print "Get ready to guess a number between 1 and 10!"

while (win == False and turns < 3):
    userGuess = int(raw_input("Guess a number:"))
    if (userGuess > randomNumber):
        print "... a little bit too high..."
    elif(userGuess < randomNumber):
        print"... a little bit too low..."
    if (userGuess == randomNumber):
        print "You guessed the number!"
        win = True

    turns += 1

if(win):
    print "You win!"
else:
    print "You lose. The hidden number was " + str(randomNumber)

# while (True):
#     print "the end is never ",
