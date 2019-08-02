start = raw_input("Do you want to play Mad Libs? (y/n)")
while (start.lower() == "y"):
    firstAdj = raw_input("Enter the first adjective: ")
    secondAdj = raw_input("Enter another adjective: ")
    thirdAdj = raw_input("Enter another adjective: ")
    name = raw_input("Enter a name: ")
    animal = raw_input("Enter an animal: ")

    madlib = """
    The %s man entered the %s building to visit a very %s man.
    \"Sit down, Mr. %s, can I interest you in any good... %s food?\"
    """ % (firstAdj, secondAdj, thirdAdj, name, animal)

    print madlib

    start = raw_input("Do you want to redo this madlib? (y/n)")

print "Exiting MadLibs."
