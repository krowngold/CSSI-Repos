#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = raw_input("Enter your choice [a|b|c|d|e]:")

    if(choice.lower() == "a"):
        newItem = raw_input("What are you adding to the list?")
        shopping_list.append(newItem);

    elif(choice.lower() == "b"):
        print shopping_list
        loseItem = raw_input("What are you removing from the list?")
        if (loseItem in shopping_list):
            shopping_list.remove(loseItem)
        else:
            loseItem = raw_input("That item isn't in the list. What did you want to remove?")
    elif(choice.lower() =="c"):
        searchItem = raw_input("What item are you looking for?")
        if (searchItem in shopping_list):
            print str(searchItem) + " is in the shopping list!"
        else:
            print str(searchItem) + " is not in the shopping list."

    elif(choice.lower() == "d"):
        print shopping_list


    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
