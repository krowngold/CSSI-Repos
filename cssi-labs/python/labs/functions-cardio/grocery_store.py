# class Item(object):
#     def __init__(self, name, price, inventory, isTaxable):
#         self.price=price
#         self.inventory=inventory
#         self.isTaxable=isTaxable
#         self.name=name
#
# banana = Item("banana", 8, 10, False)
# bread = Item("bread", 3, 10, False)
# eggs = Item("eggs", 10, 1, False)

# def parseList(userList):
#     userList = userList + ","
#     start = 0
#     finalList = []
#     for i in range(len(userList)):
#         if(userList[i] == ","):
#             finalList.append(userList[start:i])
#             start = i + 2
#     return finalList
# THIS IS OLD NOW JUST USE .split(<STRING>)!!!!!!!!
#
# def isNum(s):
#     if (float(s) == s):
#         return s
#     else:
#         newNum = raw_input("Enter a new number: ")
#         return isNum(s)

store = {
    "banana": Item("banana", 8, 10, False),
    "bread": Item("bread", 3, 10, False),
    "eggs": Item("eggs", 10, 1, True)
}


prices = {
    'banana': 8,
    'watermelon': 1,
    'chocolate milk': 5,
    'nutritional yeast': 8,
    'bread': 3,
    'eggs':10
}

inventory = {
    'banana': 10,
    'watermelon': 10,
    'chocolate milk': 20,
    'nutritonal yeast': 50,
    'bread': 4,
    'eggs': 1
}

taxable = ['chocolate milk', 'eggs']
#
# def taxTotal(sum):
#     return (sum + (sum*0.1))

def sum(shopping_list):
    total = 0
    for item in shopping_list:
        if item in store and store[item].inventory > 0:
            if store[item].is_taxable:
                total += (store[item].price * 1.1)
            else:
                total += store[item].price
            store[item].inventory -= 1

sum(raw_input("Add items to your shopping list: ").split())

def subtract(item, num):
    """
        We don't accept non-numeric values for the second parameter
    """
    if(item in inventory):
        while((inventory[item] - num)<0):
            print "That's too much of " + item + "! Please enter a new amount of " + item + " to not outbuy us :)"
            num = raw_input("New amount of " + item + ": ")
        inventory[item]-=num
        print item + ": " + str(inventory[item])
    else:
        print "We don't carry that item."

def add(item, num):
    while(not item in inventory):
        item = raw_input("We don't carry that item. Please enter another: ")
    inventory[item]+=num
    print item + ": " + str(inventory[item])

def buyMore(item, num):
    while (not item in inventory):
        item = raw_input("We don't carry that item. Please enter another")


def reportInventory():
    print "The inventory is as follows: " + inventory

def reportCommands():
    print """
        type 'help' to receive assistance on your commands
        type 'add' to add an item to your shopping list
        type 'purchase' to receive your total
    """

userInput = raw_input("Would you like to start your shopping list? (y/n; enter \"quit\" to stop): ")
print userInput.split(", ")
while (not userInput.lower() == "quit"):
    reportCommands()
    addNum = 0
    addItem = ""
    subtractNum = 0
    subtractItem = ""
