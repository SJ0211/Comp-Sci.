# Welcome to the Unit 3 Test
# Replace the Below Comment with your name and the date
# SJ Hwang, 3/31/2022
#
#
# There are x Errors in the code, When you find one  fix it, and leave a comment saying your found it and what you
# did to fix it EG. This loop was broken due to I not being defined, This print was broken, needed to add str()

import random     # Random was not imported


# Variables Here
ColorList = ["green", "blue", "red"]     #extra comma was here, had random numbers, too
Counter = 0          #This was set to -45, had double equals, which doesn't work for declaring 'Counter'
Name_Len = " "

# Function that does things
def list_fun(usercolor):
    global ColorList
    for i in ColorList:
        if usercolor == i:
            y = str(usercolor) + " is already in the list of colors, you are not imaginative -_- "   #it was int(usercolor), which doesn't work since usercolor is a str
            return y
    ColorList.append(usercolor)
    y = str(usercolor) + " is not yet on the list of colors! You are imaginative :) "    #this was not defined as y
    return y


# Git some inputs
UserName = input("Please enter your name:")     # quotation marks
FavoriteColor = input("Enter your favorite color :")  # Brackets

# Some calculations before the print
FunctionOutput = list_fun(FavoriteColor)
x = random.randint(0, len(ColorList) - 1)
RandomColor = ColorList[x]

# Do some cool math
while Counter == 0:
    if len(UserName) <= 5:         # added equal sign, so it works when UserName is 5 letters long
        Name_Len = "You have a short name"
    elif len(UserName) > 5:
        Name_Len = "You have a long name"
# deleted the steve thing here. wasnt making problems but I dont think it was needed
    else:
        Name_Len = "Broken Code You Turkey"
    Counter = Counter + 1 # changed adding 1 to Counter



# Printing some outputs NOTHING BROKEN BELOW HERE
print("Your name is " + UserName)
print(Name_Len)
print("Your favorite color is " + RandomColor)
print(FunctionOutput)
