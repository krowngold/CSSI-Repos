def sum_to_n(n):


    sum = 0
    for i in range(n):
        sum = sum + i+1
    return sum

def isTriangle(s1, s2, s3):


    check = 0
    if (s1 + s2 > s3):
        check += 1
    if (s2 + s3 > s1):
        check += 1
    if (s3 + s1 > s2):
        check+=1
    if (check == 3):
        return True
    else: return False


def isPrime(n):
    check = 2
    for i in range(2,n/2):
        if (n%i == 0):
            return False
    return True

def snakeCase(camel):
    list = []
    for char in camel:
        if char.islower():
            list.append(char)
        else:
            list.append("_")
            list.append(char.lower())
    return ''.join(list)

def splicedSnakeCase(camel):
    splicedString = ""
    for char in camel:
        if (char.isupper()):
            splicedString = splicedString + "_" + camel[camel.find(char)].lower()
        else:
            splicedString += char
    return splicedString

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getNumberInput(string):
    print "The prompt is: " + string
    userInput = raw_input("Enter something: ")
    while (not isNumber(userInput)):
        userInput = input("Try again. The prompt was " + string + " Enter something: ")

    return userInput

print getNumberInput("How many apples have you had today?")
