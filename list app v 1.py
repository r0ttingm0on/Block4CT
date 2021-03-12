"""
Program Goals:
1. Get input from the user( at multiple stages)
2.Convert some, but not all, inputs to INTs from STRs
3. we need to provide the user with choices
    a. add more values to a list
    b. return a value at a specific index position
"""
import random
myList = []

def mainProgram():
    while true:
    myList = []
    print("Hi mortal, lets work with lists!")
    print("Choose from the following options. Type a number")
    choice = input(""" 1. add to a list or
2.Return a value at index
3.Random search
4. Quit program""")
    choice = input("1. Add to a list or 2. Retrn a value at an index")
    if choice == 1:
        addToList()
    elif choice == "2":
        indexValues()
    elif choice == "3":
        randomSearch()
    else:
        break

def addToList():
     print(" Adding to list:)")
     newItem = input("type an integer here!     "
     myList.append(int(newItem))
                     
def indexValues():
    print("curious about and index position? me too!")
    indexPos = input("What index position would you like to check out?"
    print(myList[int(indexPos)])                

def randomSearch();
    print("RaNDoM SeArCH?!?")
    print(myList[random.randint(0, len(myList)-1])
#dunder main--> double underscore--- dunder
if_name_ == "_main_":
    mainProgram()
