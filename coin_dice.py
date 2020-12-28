#                                                LAB_5
#Task#1: Write a python class to flip a coin 1000 times and display the number of heads and tails.
import random
class Cointoss:

    def __init__(self):
        self.upperside = 'Tails'

    def tossing(self):
        if random.randint(0, 1) == 0:
            self.upperside = 'Tails'
        else:
            self.upperside = 'Heads'

    def get_upperside(self):
        return self.upperside

def main():
    start_toss = Cointoss()

    print("This is upper side Before Toss :[", start_toss.get_upperside(), "]")

    print("........tossing the coin........")
    start_toss.tossing()

    print("Got the up side After Toss :[", start_toss.get_upperside(), "]")

main()
#Task#2: Perform the same task in Task#1, but this time use dice instead of a coin.
import random
class Die(object):
    def roll( self ):
        self.value= random.randint(1, 6)
        return self.value
    def getValue( self ):
        return self.value
d = Die()
d.roll()
d.getValue()
