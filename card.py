'''
Playing Cards¶
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, 
then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10
. Aces have a rank of either 11 or 1 as needed to reach 21 without busting. As a starting point in your program, you may want to 
assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values.
'''
'''
This is the card file where each individual card has its rank and the suits. Both of them has been initialised here and would be very useful
later on in the deck and main class.
'''
class card():
    def __init__(self,suits,rank):
        self.suits=suits
        self.rank=rank

    def getsuit(self):
        return self.suits

    def getrank(self):
        return self.rank
'''
Since we know that in this particular game we can choose ace to be 1 or 11 so, it is given as an option to the player.
Also, as for the face cards each has the value of 10.
'''
    def countingnum(self):
        if(self==1):
            askvalueofa=int(input("What do you want the value of Ace to be: 1 or 11"))
            return askvalueofa
        elif(self==11 or self==12 or self==13):
            return 10
        else:
            return self

'''
Below are some of the smaller test codes for the card class.
cars= card('H',1)
print(cars.getrank())
countingnum= cars.countingnum(cars.getrank())
print(countingnum)
#print("The two things are "+ cars.getsuit()+ str(cars.getrank()))
'''
