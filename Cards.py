import random

class Card:
    
    def __init__(self,suit, value):
        self.suit=suit
        self.value=value

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    
    suits=["Spades", "Clubs", "Hearts", "Diamonds"] 
    values=[str(n) for n in range(2,11)]+list('JQKA')

    def __init__(self):
        self._cards=[Card(suit, value) for suit in self.suits for value in self.values]

    def size(self):
        return len(self._cards)

    def shuffle(self):
        for i in range(len(self._cards)-1, 0, -1):
            r=random.randint(0,i)
            self._cards[i], self._cards[r] = self._cards[r], self._cards[i]

    def draw_card(self):
        return self._cards.pop()


konec

jojo