import time
import random # to pic cards
import sys
from collections import Counter
global Player1
global Player2
global Player3
global Dealer
global Player1Ace
global Player2Ace
global Player3Ace


global WinCounter
global Bet
#This cool LoadingFunction is the only thing I copied from internet.
def LoadingFunction():

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


def DealerDealingFunction():
    #globall stuff
    global DealerAce
    global DealerSum
    global Player1Money
    global Player2Money
    global Player3Money
    global Player1Bet
    global Player2Bet
    global Player3Bet
    #find total value in dealer's hand
    Dealerint = [int(x) for x in Dealer]
    DealerSum = sum(Dealerint)
#if less than 17, get more card
    if DealerSum < 17:
        #pick a card from card deck, then remove it from the deck
        Card = random.choice(CardValue)
        CardValue.remove(Card)
        #record number of aces he has
        if Card == ('Ace'):
            DealerAce = DealerAce + 1
            # If its q,j,k, add 10 to his hand value
        elif Card == 'Q':
            Dealer.append(10)
        elif Card == 'J':
            Dealer.append(10)
        elif Card == 'K':
            Dealer.append(10)
        else:
            Dealer.append(Card)
    else:
        print("Dealer stays.")

#if dealer has Ace, he decides to pic 1 or 11 according to his value
    while DealerAce > 0:
        if DealerSum < 11:
            Dealer.append(11)
            DealerAce = DealerAce - 1
        elif DealerSum >= 11:
            Dealer.append(1)
            DealerAce = DealerAce - 1
#calculate his hand value again
    Dealerint = [int(x) for x in Dealer]
    DealerSum = sum(Dealerint)
    #if dealer has 21, he wins
    if DealerSum == 21:
        print("The dealer got a black jack, dealer wins.")
        WinCounter.append("Dealer")
        return "GameOver"
    #if dealer busts, every player gets x2 of their bet
    elif DealerSum > 21:
        print("The Dealer busts with a value of " + str(DealerSum) +".")
        WinCounter.append(PlayerName[0])
        if len(PlayerValue) > 1:
            WinCounter.append(PlayerName[1])
            pass
        else:
            pass
        if len(PlayerValue) >2:
            WinCounter.append(PlayerName[2])
            pass
        else:
            pass
        Player1Money = Player1Money + 2 * Player1Bet
        Player2Money = Player2Money + 2 * Player2Bet
        Player3Money = Player3Money + 2 * Player3Bet

        return 'GameOver' # tells that the round is over



    print("The dealer has: " + str(len(Dealer)) + " cards") # Tells the number of cards the dealer has

    if len(Dealer) > 1:
# Shows dealer's cards other than his 1st one
        if len(Dealer) ==2:
            print("[ ? , " + str(Dealer[1]) + "]\n")
        elif len(Dealer) ==3:
            print("[ ? , " + str(Dealer[1]) + " , " + str(Dealer[2]) + "]\n")
        elif len(Dealer) ==4:
            print("[ ? , " + str(Dealer[1]) + " , " + str(Dealer[2]) + " , " + str(Dealer[3]) + "]\n")
        elif len(Dealer) ==5:
            print("[ ? , " + str(Dealer[1]) + " , " + str(Dealer[2]) + " , " + str(Dealer[3]) + " , " + str(Dealer[4]) + "]\n")
        elif len(Dealer) ==6:
            print("[ x ," + str(Dealer[1]) + "," + str(Dealer[2]) + "," + str(Dealer[3]) + "," + str(Dealer[4]) + "," + str(Dealer[5]) +  "]\n")
        else:
            pass

    else:
        pass
    Dealerint = [int(x) for x in Dealer]
    DealerSum = sum(Dealerint)
# calculate total value again



def PlayerDealingFunction():
    # Global stuff
    global PlayerValue
    global Player1Sum
    global Player2Sum
    global Player3Sum
    global DealerSum
    global Player1Money
    global Player1Bet
    global Player2Money
    global Player2Bet
    global Player3Money
    global Player3Bet
    global BustedPlayers
#PlayerDecision =  0 for hit, +1 for stay
    PlayerDecision = 0
    for i in PlayerValue:

# mention their name when its their turn, and let them know what cards they have
        if i == 'Player1':
            print("\n" + PlayerName[0] + "'s Turn.")
            print("You have " + str(Player1) + " and " + str(Player1Ace) + " Ace(s).")
        elif i == 'Player2':
            print("\n" + PlayerName[1] + "'s Turn.")
            print("You have " + str(Player2) + " and " + str(Player2Ace) + " Ace(s).")
        elif i == 'Player3':
            print("\n" + PlayerName[2] + "'s Turn.")
            print("You have " + str(Player3) + " and " + str(Player3Ace) + " Ace(s).")
        else:
            pass
        D = True
#loop till correct answer, preventing crash
        while D == True:
            HitOrStay = input("Hit or Stay?:")
            if HitOrStay == 'Hit':
                break
            elif HitOrStay == 'Stay':
                break
            else:
                print("Please enter 'Hit' or 'Stay'.")
                continue

#If the player chose hit, run this
        if HitOrStay == ("Hit"):
            #run dealingfunction for the player
            DealingFunction(i)
            #calculate values of player hand.
            Player1int = [int(x) for x in Player1]
            Player1Sum = sum(Player1int)
            if PlayerValue.count('Player2') > 0:
                Player2int = [int(x) for x in Player2]
                Player2Sum = sum(Player2int)
                pass
            else:
                pass
            if PlayerValue.count('Player3') > 0:
                Player3int = [int(x) for x in Player3]
                Player3Sum = sum(Player3int)
                pass
            else:
                pass

            # for each players, determine if they busts or get a blackjack.
            if i == ('Player1'):
                print("You have " + str(Player1) + " and " + str(Player1Ace) + " Ace(s).")
                if Player1Sum > 21:
                    print("You bust...")
                    PlayerValue.remove('Player1')   # if they bust, they are out of the game.
                    BustedPlayers.append('Player1')  # add them to busted list
                elif Player1Sum == 21:
                    print(PlayerName[0] + " got a blackjack!")
                    WinCounter.append(PlayerName[0])               #if they get blackjack, add them to winners list
                    Player1Money = Player1Money + 1.5 * Player1Bet    #and give them x1.5 of money they bet

                    return "GameOver"
                else:
                    pass

            elif i == ('Player2'):   #same thing for player2

                print("You have " + str(Player2) + " and " + str(Player2Ace) + " Ace(s).")
                if Player2Sum > 21:
                    print("You bust...")
                    PlayerValue.remove('Player2')
                    BustedPlayers.append('Player2')
                elif Player2Sum == 21:
                    print(PlayerName[1]+" got a blackjack!")
                    WinCounter.append(PlayerName[1])
                    Player2Money = Player2Money + 1.5 * Player2Bet
                    return "GameOver"
                else:
                    pass
            else:

                print("You have " + str(Player3) + " and " + str(Player3Ace) + " Ace(s).")
                if Player3Sum > 21:
                    print("You bust...")
                    PlayerValue.remove('Player3')
                    BustedPlayers.append('Player3')
                elif Player3Sum == 21:
                    print(PlayerName[2]+" got a blackjack!")
                    WinCounter.append(PlayerName[2])
                    Player3Money = Player3Money + 1.5 * Player3Bet
                    return "GameOver"
                else:
                    pass
        #if user choose to stay, do this
        elif HitOrStay == ("Stay"):

            if i == ('Player1'):
                PlayerDecision = PlayerDecision + 1   # add 1 player choosed stay
                print("You have " + str(Player1) + " and " + str(Player1Ace) + " Ace(s).")
                AceFunction(1)
                Player1int = [int(x) for x in Player1]
                Player1Sum = sum(Player1int)
                if Player1Sum > 21:
                    print("You bust...")
                    PlayerValue.remove('Player1')
                    BustedPlayers.append('Player1')
                elif Player1Sum == 21:
                    print(PlayerName[0] + " got a blackjack!")
                    WinCounter.append(PlayerName[0])
                    Player1Money = Player1Money + 1.5 * Player1Bet
                    return "GameOver"
                else:
                    pass


            elif i == ('Player2'):
                PlayerDecision = PlayerDecision + 1
                print("You have " + str(Player2) + " and " + str(Player2Ace) + " Ace(s).")
                AceFunction(2)
                Player2int = [int(x) for x in Player2]
                Player2Sum = sum(Player2int)
                if Player2Sum > 21:
                    print("You bust...")
                    PlayerValue.remove('Player2')
                    BustedPlayers.append('Player2')
                elif Player2Sum == 21:
                    print(PlayerName[1] + " got a blackjack!")
                    WinCounter.append(PlayerName[1])
                    Player2Money = Player2Money + 1.5 * Player2Bet
                    return "GameOver"
            else:
                PlayerDecision = PlayerDecision + 1
                print("You have " + str(Player3) + " and " + str(Player3Ace) + " Ace(s).")
                AceFunction(3)
                Player3int = [int(x) for x in Player3]
                Player3Sum = sum(Player3int)
                if Player3Sum > 21:
                    print("You bust...")
                    PlayerValue.remove('Player3')
                    BustedPlayers.append('Player3')
                elif Player3Sum == 21:
                    print(PlayerName[2] + " got a blackjack!")
                    WinCounter.append(PlayerName[2])
                    Player3Money = Player3Money + 1.5 * Player3Bet
                    return "GameOver"
#calculate everyone's hand again
    Player1int = [int(x) for x in Player1]
    Player1Sum = sum(Player1int)
    if PlayerValue.count('Player2') > 0:
        Player2int = [int(x) for x in Player2]
        Player2Sum = sum(Player2int)
        pass
    else:
        pass
    if PlayerValue.count('Player3') > 0:
        Player3int = [int(x) for x in Player3]
        Player3Sum = sum(Player3int)
        pass
    else:
        pass


    if PlayerDecision == len(PlayerValue): #if everyone choosed to stay, compare their values.
        return CompareFunction()
    else:
        pass

    return
#this is the function that lets the player decide 1 or 11 for their aces
def AceFunction(i):
    global Player1Ace, Player2Ace, Player3Ace
    if i == 1:  #if its player1
        while Player1Ace > 0:
            AceDecide = input('''
            You have Ace(s), want to determine its value now?
            (1)1
            (2)11
            (3)Later
            :''')     # ask user what value will they choose
            if AceDecide == '1':
                Player1Ace = Player1Ace - 1
                Player1.append(1) # if user chose 1, add 1 to their hand
            elif AceDecide == '2':
                Player1Ace = Player1Ace - 1
                Player1.append(11)  # if they chose 2, add 11
            elif AceDecide == '3':  # decide later, will ask it again in next turn
                pass
            else:
                print("please enter a correct number")
    elif i == 2:
        while Player2Ace > 0:
            AceDecide = input('''
            You have Ace(s), want to determine its value now?
            (1)1
            (2)11
            (3)Later
            :''')
            if AceDecide == '1':
                Player2Ace = Player2Ace - 1
                Player2.append(1)
            elif AceDecide == '2':
                Player2Ace = Player2Ace - 1
                Player2.append(11)
            elif AceDecide == '3':
                pass
            else:
                print("please enter a correct number")
    elif i == 3:
        while Player3Ace > 0:
            AceDecide = input('''
            You have Ace(s), want to determine its value now?
            (1)1
            (2)11
            (3)Later
            :''')
            if AceDecide == '1':
                Player3Ace = Player3Ace - 1
                Player3.append(1)
            elif AceDecide == '2':
                Player3Ace = Player3Ace - 1
                Player3.append(11)
            elif AceDecide == '3':
                pass
            else:
                print("please enter a correct number")
    else:
        pass

    return
# this is the function for betting
def BettingFunction():
    global Player1Bet
    global Player2Bet
    global Player3Bet
    global Player1Money
    global Player2Money
    global Player3Money
    global Bet
    Betting = True
    Player2Bet = 0   #set player 2 and 3's bet to zero so it doesn't glitch when they are out of game
    Player3Bet = 0
    while Betting == True:
        Player1Bet = int(input(PlayerName[0] + ", please place your bet\n: $"))
        if Player1Bet == str:
            print("please put numbers in")
            continue
        elif Player1Bet == '':
            print("please put numbers in")
        else:
            pass
        if Player1Money < Player1Bet:
            print("you don't have enough money!")   #ask them to try again with other value if they tried to bet more than they have
            continue
        else:
            pass
        Player1Money = Player1Money - Player1Bet
        break
    while Betting == True:
        if PlayerValue.count('Player2') > 0: #check if player2 is in game
            Player2Bet = int(input(PlayerName[1] + ", please place your bet\n: $"))
            if Player2Bet == str or '':
                print("please put numbers in")
                continue
            elif Player2Bet == '':
                print("please put numbers in")
            else:
                pass
            if Player2Money < Player2Bet:
                print("you don't have enough money!")
                continue
            else:
                pass
            Player2Money = Player2Money - Player2Bet
            break
        else:
            break
    while Betting == True:
        if PlayerValue.count('Player3') > 0:
            Player3Bet = int(input(PlayerName[2] + ", please place your bet\n: $"))
            if Player3Bet == str or "":
                print("please put numbers in")
                continue
            elif Player3Bet == '':
                print("please put numbers in")
            else:
                pass
            if Player3Money < Player3Bet:
                print("you don't have enough money!")
                continue
            else:
                pass
            Player3Money = Player3Money - Player3Bet
            break
        else:
            break
    # calculate total bet
    Bet = Player1Bet + Player2Bet + Player3Bet
    print("Total Bet: $" + str(Bet))
    return

#function for compareing once everyone stays.
def CompareFunction():
    global Player1Sum
    global Player2Sum
    global Player3Sum
    global DealerSum
    global PlayerValue
    global WinValue1
    global WinValue2
    global WinValue3
    global WinValueD
    global Player1Money
    global Player1Bet
    global Player2Money
    global Player2Bet
    global Player3Money
    global Player3Bet

    Player1int = [int(x) for x in Player1]
    Player1Sum = sum(Player1int)
    if PlayerValue.count('Player2') > 0:
        Player2int = [int(x) for x in Player2]
        Player2Sum = sum(Player2int)
        pass
    else:
        pass
    if PlayerValue.count('Player3') > 0:
        Player3int = [int(x) for x in Player3]
        Player3Sum = sum(Player3int)
        pass
    else:
        pass
    # prevent glitch
    WinValue1 = 99
    WinValue2 = 99
    WinValue3 = 99
    WinValueD = 21 - DealerSum
    # determine how close to 21 each player is
    for i in PlayerValue:

        if i == 'Player1':

            WinValue1 = 21-Player1Sum

        elif i == 'Player2':

            WinValue2 = 21-Player2Sum

        elif i == 'Player3':

            WinValue3 = 21-Player3Sum

        else:
            pass

#if everyone busts, dealer wins

        if len(PlayerValue) == 0:
            print("Dealer Won.")
            WinCounter.append("Dealer")
            return "GameOver"
        else:
            pass


        Winners = 0

        #from here, determines who win

        if WinValue1 < WinValueD:
            print(PlayerName[0] + " Won!")
            WinCounter.append(PlayerName[0])
            #give twice of money
            Player1Money = Player1Money + 2 * Player1Bet
            Winners = Winners + 1
            pass
        else:
            pass

        if WinValue1 == WinValueD:
            print(PlayerName[0] + " Draw.")
            Player1Money = Player1Money + Player1Bet
            pass
        else:
            pass

        if WinValue2 < WinValueD:
            print(PlayerName[1] + " Won!")
            WinCounter.append(PlayerName[1])
            Player2Money = Player2Money + 2 * Player2Bet
            Winners = Winners + 1
            pass
        else:
            pass
        if WinValue2 == WinValue2:
            print(PlayerName[1] + " Draw.")
            Player2Money = Player2Money + Player2Bet
            pass
        else:
            pass



        if WinValue3 < WinValueD:
            print(PlayerName[2] + " Won!")
            WinCounter.append(PlayerName[2])
            Player3Money = Player3Money + 2 * Player3Bet
            Winners = Winners + 1
            pass
        else:
            pass
        if WinValue3 == WinValueD:
            print(PlayerName[2] + " Draw.")
            Player3Money = Player3Money + Player3Bet
            pass
        else:
            pass

        if WinValueD < (WinValue1 and WinValue3 and WinValue2):
            print("Dealer Won.")
            WinCounter.append("Dealer")
            Winners = Winners + 1
            pass
        else:
            pass

# if there is a winner or winners, end the round
        if Winners > 0:
            return 'GameOver'
        else:
            pass





#this is picking cards from the card deck

def DealingFunction(d):
    global Player1Ace
    global Player2Ace
    global Player3Ace
    if d == 'Player1':
        Card = random.choice(CardValue)
        CardValue.remove(Card)
        print(PlayerName[0] + " got:" + Card)
        if Card == ('Ace'):
            Player1Ace = Player1Ace + 1
        elif Card == 'Q':
            Player1.append(10)
        elif Card == 'J':
            Player1.append(10)
        elif Card == 'K':
            Player1.append(10)
        else:
            Player1.append(Card)

    elif d == 'Player2':
        Card = random.choice(CardValue)
        CardValue.remove(Card)
        print(PlayerName[1] + " got:" + Card)
        if Card == ('Ace'):
            Player2Ace = Player2Ace + 1
            # if cards are q,j, or k, add 10 to player hand value
        elif Card == 'Q':
            Player2.append(10)
        elif Card == 'J':
            Player2.append(10)
        elif Card == 'K':
            Player2.append(10)
        else:
            Player2.append(Card)

    elif d == 'Player3':
        Card = random.choice(CardValue)
        CardValue.remove(Card)
        print(PlayerName[2] + " got:" + Card)
        if Card == ('Ace'):
            Player3Ace = Player3Ace + 1
        elif Card == 'Q':
            Player3.append(10)
        elif Card == 'J':
            Player3.append(10)
        elif Card == 'K':
            Player3.append(10)
        else:
            Player3.append(Card)

    else:
        pass



Round = 1

#players start with $100

Player1Money = 100
Player2Money = 100
Player3Money = 100
BustedPlayers = []
WinCounter = []
Menu = True
while Menu == True:
    Game = True

    #card in hand
    Player1 = []
    Dealer = []
    Player2 = []
    Player3 = []
    #how many players
    PlayerValue = []
    #their name
    PlayerName = []
    #this is the card deck
    CardValue = ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q','Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q','Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q','Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q']
    #Ask user if they want to look over rules
    Userinput = str(input("Press (P) to play the game\nPress (R) to check rules\nEnter here:"))
    if Userinput == "P":
        Menu = False
    elif Userinput == "R":
        #print rules
        print('''
Basic Blackjack Rules:

The goal of blackjack is to beat the dealer's hand without going over 21.
Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
Each player starts with two cards, one of the dealer's cards is hidden until the end.
To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
If you are dealt 21 from the start (Ace & 10), you got a blackjack.
Dealer will hit until his/her cards total 17 or higher.
        ''')
        Userinput2 = str(input("Enter (B) to return:"))
        if Userinput2 == "B":
            continue
    else:
        print("Please Enter P/R")
        continue
    PlayerNumber = True
    #define how many players
    while PlayerNumber == True:
        HowManyPlayers = input("Select how many players you will play with\n(1):1P\n(2):2P\n(3):3P\n:")
        if HowManyPlayers == '1':
            PlayerValue.append('Player1')
            break
        elif HowManyPlayers == '2':
            PlayerValue.append('Player1')
            PlayerValue.append('Player2')
            break
        elif HowManyPlayers == '3':
            PlayerValue.append('Player1')
            PlayerValue.append('Player2')
            PlayerValue.append('Player3')
            break
        else:
            print("Please enter 1, 2, or 3.")
            continue
#get names of players
    for x in PlayerValue:
        PlayerName.append(input("Enter " + x + "'s name here:"))

    print("Players are:" + str(PlayerName))
#the round starts here
    while Game == True:
        # reset number of ace and Bet
        DealerAce = 0
        Player1Ace = 0
        Player2Ace = 0
        Player3Ace = 0
        Player1Bet = 0
        Player2Bet = 0
        Player3Bet = 0
        Bet = 0
        #reset busted players
        for i in BustedPlayers:
            PlayerValue.append(i)
            #now reset bustedplayers list
        BustedPlayers = []
        #delete Players who have no money
        for x in PlayerValue:
            if x == 'Player1':
                if Player1Money == 0:
                    print(PlayerName[0] + " broke...")
                    PlayerValue.remove('Player1')
            elif x == 'Player2':
                if Player2Money == 0:
                    print(PlayerName[1] + " broke...")
                    PlayerValue.remove('Player2')
            elif x == 'Player3':
                if Player3Money == 0:
                    print(PlayerName[2] + " broke...")
                    PlayerValue.remove('Player3')
    # give info of game history
        print("Round " + str(Round) )
        print("History: " + str(Counter(WinCounter)) + "\n")
        print(PlayerName[0] + " has: $" + str(Player1Money))
        if PlayerValue.count('Player2') > 0:
            print(PlayerName[1] + " has: $" + str(Player2Money))
            pass
        else:
            pass
        if PlayerValue.count('Player3') > 0:
            print(PlayerName[2] + " has: $" + str(Player3Money))
            pass
        else:
            pass
        BettingFunction()
        print("Dealing Cards...")
        LoadingFunction()
        DealerDealingFunction()
        DealingFunction('Player1')
        if PlayerValue.count('Player2') > 0:
            DealingFunction('Player2')
            pass
        else:
            pass
        if PlayerValue.count('Player3') > 0:
            DealingFunction('Player3')
            pass
        else:
            pass
        if DealerDealingFunction() == "GameOver":
            break
        else:
            pass
        DealingFunction('Player1')
        if PlayerValue.count('Player2') > 0:
            DealingFunction('Player2')
            pass
        else:
            pass
        if PlayerValue.count('Player3') > 0:
            DealingFunction('Player3')
            pass
        else:
            pass
        while len(PlayerValue) > 0:
            print("Dealer's turn...")
            LoadingFunction()
            #checks if the game is over after every function, if get return 'GameOver', end the program
            if DealerDealingFunction() == 'GameOver':
                break
            else:
                pass
            if PlayerDealingFunction() == 'GameOver':
                break

            else:
                continue
        #ask for another round
        if input("another round? (Y/N):") == "Y":
            Round = Round + 1
            continue
        # if not, stop the program
        else:
            break


# Random comment to make the code exactly 800 lines long