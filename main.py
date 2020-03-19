from Deck import *
from card import *

ans = input("Hey Player, Do you want to begin the game? yes or no ")
if ans!='yes':
    print('Come back later')
while(ans=='yes'):
    deck = Deck()
    deckinlist = deck.createdeck()
    shuffleddeck = deck.shuffle_deck()
    ###################################################################
    while True:
        try:
            player1money = int(input("Hey Player, How much do you want to bet? "))
            break;
        except:
            print("Type error")

    print("Player 1 has bet " + str(player1money) + " dollar bill")
    player1first = deck.hitme()
    print("The player card is " + str(player1first.getrank()) + " of suit " + player1first.getsuit())
    player1second = deck.hitme()
    print("The player card is " + str(player1second.getrank()) + " of suit " + player1second.getsuit())
    countplay1 = card.countingnum(player1first.getrank()) + card.countingnum(player1second.getrank())
    print("The sum is " + str(countplay1))
    #ans = input("hit or stay : ")
    while True:
            ans = input("hit or stay : ")
            if ans=='hit' or ans=='stay':
                break;
    while ans == 'hit':
        player1draw = deck.hitme()
        print("The player card is " + str(player1draw.getrank()) + " of suit " + player1draw.getsuit())
        countplay1 = countplay1 + card.countingnum(player1draw.getrank())
        print("The sum is " + str(countplay1))
        if countplay1 > 21:
            print("Greater than 21.Busted.Computer Wins")
            print("Sorry player. Your " + str(player1money) + " dollar bill is gone.Better luck next time.")
            exit()
        #ans = input("hit or stay : ")
        while True:
            ans = input("hit or stay : ")
            if ans == 'hit' or ans == 'stay':
                break;
        if (ans == 'stay'):
            break


    ##############################################
    def countforcom(countcom):
        if countcom > 21:
            print("Player 1 won the game")
            print("Congo player. You won the game. Your new money after doubling is " + str(
                int(player1money) * 2) + " dollars")
            exit()
        if countcom <= 21 and countcom > countplay1:
            print("Computer won the game")
            print("Sorry player. Your " + str(player1money) + " dollar bill is gone.Better luck next time.")
            exit()
        if countcom==countplay1==21:
            print("No one won the game")
            exit()


    computer1first = deck.hitme()
    print("The computer card is " + str(computer1first.getrank()) + " of suit " + computer1first.getsuit())
    computer1second = deck.hitme()
    print("The computer card is " + str(computer1second.getrank()) + " of suit " + computer1second.getsuit())
    countcom = card.countingnum(computer1first.getrank()) + card.countingnum(computer1second.getrank())
    print("The sum is " + str(countcom))
    countforcom(countcom)
    while (True):
        computer1draw = deck.hitme()
        print("The computer card is " + str(computer1draw.getrank()) + " of suit " + computer1draw.getsuit())
        countcom = countcom + card.countingnum(computer1draw.getrank())
        print("The sum is " + str(countcom))
        countforcom(countcom)

