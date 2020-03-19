#import input
class card():
    def __init__(self,suits,rank):
        self.suits=suits
        self.rank=rank

    def getsuit(self):
        return self.suits

    def getrank(self):
        return self.rank

    def countingnum(self):
        if(self==1):
            askvalueofa=int(input("What do you want the value of Ace to be: 1 or 11"))
            return askvalueofa
        elif(self==11 or self==12 or self==13):
            return 10
        else:
            return self


'''
cars= card('H',1)
print(cars.getrank())
countingnum= cars.countingnum(cars.getrank())
print(countingnum)
#print("The two things are "+ cars.getsuit()+ str(cars.getrank()))
'''