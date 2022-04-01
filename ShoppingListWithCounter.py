from time import time

import time

def PrintFunction():
    global PrintList
    global location
    global PrintAdd
    location = 1
    PrintThis = ""
    PrintList = list.copy(ShoppingList)                             #makes list just for print
    for i in PrintList:
        CountX = PrintList.count(i)
        if CountX == 1:
            PrintAdd = (str(location) + ". " + str(i) + "\n")
            PrintThis = PrintThis + PrintAdd
            location = location + 1
        elif CountX > 1:
            PrintAdd = (str(location) + ". " + str(i) + " x " + str(CountX) + "\n")
            PrintThis = PrintThis + PrintAdd
            location = location + 1
            print("for loop")
            while CountX > 0:                           #deletes item in printlist till its all gone
                X = PrintList.index(i)
                PrintList.pop(X)
                CountX = PrintList.count(i)
                print("while loop")                             
        else:
            return
    print("\nYour current list is: \n" + str(PrintThis))
    print(ShoppingList)






def AddFunction(a):                             #Fuction for adding item
    global ItemAdd
    global ShoppingList
    ShoppingList.append(a)                      #add item to the list
    PrintFunction()

def RemoveFunction (r):                         #Function for removing item
    global ItemRemove
    global ShoppingList
    ShoppingList.remove(r)                      #remove item from the list
    PrintFunction()


Run = True                                      #For While loop
ShoppingList = []                               #List

while Run == True:                              #Start while loop

    Command = input('''
(add/remove) to choose to add or remove an item
(exit) to leave
(clear) to clear items in the list
(check) to see the list
enter here: ''')
    if Command == ("add"):
        ItemAdd = input("enter an item you want to add: ")          #Get input of what item will user add

        if ShoppingList.count(ItemAdd) < 1:                         #Check if the same item already exists
            print("adding " + ItemAdd)                              #if not, run AddFuction
            AddFunction(ItemAdd)

        else:
            print("you entered an existing item, updating the list")                   #if same item exists, print this

            AddFunction(ItemAdd)


    #if input = remove
    elif Command == ("remove"):

        ItemRemove = input("enter an item you want to remove: ")    #get userinput for what item to remove

        if len(ShoppingList) == 0:                      #if there is no item in list, print this
            print("No item in the list yet!")

        elif ShoppingList.count(ItemRemove) > 0:        #if item exists, run RemoveFunction
            print("removing " + ItemRemove)
            RemoveFunction(ItemRemove)

        else:
            print("please enter an existing item")      #if item not exists, print this
            PrintFunction()
#   #if exit, run this
    elif Command == ("exit"):
        print("Shutting down...")
        time.sleep(0.5)
        print("final shopping list: " + str(ShoppingList)) #print final shopping list
        #adding time gap to shut down.. u can ignore times (just to look cool)
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        exit()

    elif Command == ("clear"):              #Clear
        ShoppingList.clear()
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        print("complete")


    #show list
    elif Command == ("check"):
        PrintFunction()

    # if user put a wrong input
    else:
        print("please enter 'add', 'remove', or 'exit'")
