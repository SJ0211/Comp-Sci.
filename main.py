
import time

def GuessFunction():
    global Counter
    global UsedWords
    global Wordlist

    Input = True
    while Input == True:
        guess = input("What letter? : ")
        Guess = guess.upper()
        if UsedWords.count(Guess) > 0:
            print("You used this word!")
            continue
        elif len(Guess) > 1:
            print("please enter 1 letter")
            continue
        elif Guess == ' ':
            print("Do not enter space!")
            continue
        else:
            Input = False



        UsedWords.append(Guess)
        if Wordlist.count(Guess) > 0:
            print("You got it!\n\n\n")

            for p in [p for p, x in enumerate(Wordlist) if x == Guess]:
                Displaylist.pop(p)
                Displaylist.insert(p, Guess)

            if Wordlist == Displaylist:
                print(HangmanWord)
                print("Yay you won")
                Functions.EndingFunction()
                exit()

            else:
                pass
        else:
            print("Hangman is getting closer to death....\n\n\n")
            Counter = Counter + 1
            if Counter == 6:
                Functions.HangmanGraphic(Counter)
                print("You killed him...")
                exit()
            else:
                pass



    if Wordlist == Displaylist:
        print("Yay you won")
        exit()
    else:
        pass
def DisplayFunction():
    global Display
    Display = ""
    for i in Displaylist:
        if i == " ":
            Display = Display + (" ")
        else:
            Display = Display + (i)


# import stuff
import Functions
global Displaylist
Counter = 0
f = open("Hangman.txt", "r")
HangmanWord = (f.read()).upper()
f.close()
# make the letter into a list
Wordlist = list(HangmanWord)
UsedWords = []
#print underlines
Display = ""

for i in Wordlist:
    if i == " ":
        Display = Display + (" ")
    else:
        Display = Display + ("_")

Display = Display + ""
Displaylist = list(Display)

Functions.Menu()

Game = True
while Game == True:
    Functions.HangmanGraphic(Counter)
    print("    [    " + Display + "    ]")
    print("You've used: " + str(UsedWords))
    GuessFunction()
    DisplayFunction()







