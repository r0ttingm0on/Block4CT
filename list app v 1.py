"""
Program Goals:
1. Get input from the user( at multiple stages)
2.Convert some, but not all, inputs to INTs from STRs
3. we need to provide the user with choices
    a. add more values to a list
    b. return a value at a specific index position
"""

def mainProgram():
    myList = []
    print("Hi mortal, lets work with lists!")
    print("Choose from the following options. Type a number")
    choice = input("1. Add to a list or 2. Retrn a value at an index")
    if choice == 1:
        addToList()
    elif choice == "2":
        indexValues()

def addToList():
     print(" Adding to list:)")
     newItem = input("type an integer here!     "
     myList.append(int(newItem))                
def indexValues():
    
#dunder main--> double underscore--- dunder
if_name_ == "_main_":
    mainProgram()
