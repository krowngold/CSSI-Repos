numChoice = raw_input("Please enter a number: ")
wordChoice = raw_input("Please enter a word: ")

print numChoice

while (wordChoice != "quit"):
    if (numChoice == str(1)):
        print str(numChoice) + " " + wordChoice
    else:
        print str(numChoice) + " " + wordChoice +"s"

    numChoice = raw_input("Please enter a number: ")
    wordChoice = raw_input("Please enter a word (\"quit\" to stop):")
