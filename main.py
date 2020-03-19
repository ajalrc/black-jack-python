'''
This is the actual game file that is runnning and importing the deck and card module and using all their methods
'''
from Deck import *
from card import *

ans = input("Hey Player, Do you want to begin the game? yes or no ")
if ans!='yes':
    print('Come back later')
if(ans=='yes'):
    '''
    The game begins by creating a deck and then shuffling the deck and # signs is seperating the code for the player which is you
    and the computer.
    '''
    deck = Deck()
    deckinlist = deck.createdeck()
    shuffleddeck = deck.shuffle_deck()
    
    ###################################################################
    #this small test to make sure that the input bet is of type integer
    while True:
        try:
            player1money = int(input("Hey Player, How much do you want to bet? "))
            break;
        except:
            print("Type error")

    print("Player 1 has bet " + str(player1money) + " dollar bill")
    player1first = deck.hitme()#this is the first card of the player
    print("The player card is " + str(player1first.getrank()) + " of suit " + player1first.getsuit())
    player1second = deck.hitme()#this is the second card of the player
    print("The player card is " + str(player1second.getrank()) + " of suit " + player1second.getsuit())
    #below countplay1 is created to make sure that the face card would be counted as 10 and for ace it would depend on the choice of player
    countplay1 = card.countingnum(player1first.getrank()) + card.countingnum(player1second.getrank())
    print("The sum is " + str(countplay1))
    
    #the below code is to make sure that the user have the correct input
    while True:
            ans = input("hit or stay : ")
            if ans=='hit' or ans=='stay':
                break;
    #this is the other cards that the player draw incase he/she is not busted        
    while ans == 'hit':
        player1draw = deck.hitme()
        print("The player card is " + str(player1draw.getrank()) + " of suit " + player1draw.getsuit())
        countplay1 = countplay1 + card.countingnum(player1draw.getrank())
        print("The sum is " + str(countplay1))
        if countplay1 > 21:
            print("Greater than 21.Busted.Computer Wins")
            print("Sorry player. Your " + str(player1money) + " dollar bill is gone.Better luck next time.")
            exit()
        #the below code is to make sure that the user have the correct input
        while True:
            ans = input("hit or stay : ")
            if ans == 'hit' or ans == 'stay':
                break;
        if (ans == 'stay'):
            break


    ##############################################
    '''
    Most of the code here are automatic to ensure that the computer has the best possible change of winning
    as the casino always looks for profit. The computer would keep on drawing until the player one gets busted or the computer wins the game
    '''
    #this countforcom is the function created for easy tracking of the score
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
    '''
    Below code make sure that the computer keep on drawing the card until won or got busted. Here the user has to make the choice for the 
    computer. The best choice that would enable them to win.
    '''
    while (True):
        computer1draw = deck.hitme()
        print("The computer card is " + str(computer1draw.getrank()) + " of suit " + computer1draw.getsuit())
        countcom = countcom + card.countingnum(computer1draw.getrank())
        print("The sum is " + str(countcom))
        countforcom(countcom)

