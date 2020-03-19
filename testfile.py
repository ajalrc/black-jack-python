import unittest
import Deck
from Deck import *


class new_test_class(unittest.TestCase):
#this is to check if the correct rank is output
    def test_output_rank(self):
        mycard=card('H',1)
        myrank=mycard.getrank()
        self.assertEqual(myrank,1)

#this is to check the counting value of the face cards is 10
    def test_facecardvalues(self):
        mycard=card('C',12)
        myrank=card.countingnum(mycard.getrank())
        self.assertEqual(myrank,10)

#this is to test if the value of ace would be what we want in our input
    def test_acevalue(self):
        mycard=card('C',1)
        myrank=card.countingnum(mycard.getrank())
        self.assertTrue(myrank==11 or myrank==1)

#after creating the deck making sure that it has 52 cards
    def test_decksize(self):
        deck=Deck()
        deckinlist=deck.createdeck()
        self.assertEqual(len(deckinlist),52)


#here we will test if after suffling the decklist, its inner items are still cards
    def test_shuffledeck(self):
        deck=Deck()
        shuffledlist=deck.shuffle_deck()
        self.assertIsInstance(shuffledlist[0],card)

#here we will be testing that after hitting the card is returned
    def test_hitme(self):
        deck=Deck()
        shouldbecard=deck.hitme()
        self.assertIsInstance(shouldbecard,card)


if __name__=='__main__':
    unittest.main()
