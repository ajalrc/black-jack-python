'''
Here some of the modules are imported first cause the deck is comprised of cards and other import would be 
used later on as you would read the code below
'''
import card
import random
from card import *
from random import shuffle
deck_in_list = []
class Deck():
 
    def createdeck(self):
        for j in ['H','S','D','C']:
            for i in range(1,14):
                new_deck = card(j,i)
                deck_in_list.append(new_deck)
        return deck_in_list#will return all the card in the deck in the form of the list so can be shuffled


    def shuffle_deck(self):
        random.shuffle(deck_in_list)
        return deck_in_list

    def printallcards(self):
        #print(all(isinstance(n,card) for n in deck)): small test to ensure that the type matches
        for individual_card in deck_in_list:
            print("The card is "+ str(individual_card.getrank())+ " of "+ individual_card.getsuit())

    ''' 
    Here hit me is calling the top card in the deck unless it is empty
    '''

    def hitme(self):
        if(len(deck_in_list)==0):
            print("Sorry, the deck is empty")
            return None
        else:
            return deck_in_list.pop(0)

'''
Below are some smaller codes to double check that the codes are running correctly
'''
#deck=Deck()
#deckinlist= deck.createdeck()
#shuffleddeck = deck.shuffle_deck(deckinlist)
#print(type(shuffleddeck[0]))
#deck.printallcards(shuffleddeck)
#deck.hitme(shuffleddeck)
