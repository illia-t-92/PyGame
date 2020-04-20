import random

class Deck:
    
    suits=["Spades", "Clubs", "Hearts", "Diamonds"] 
    values=[int(n) for n in range(2,15)]

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

    def set_trump(self, suit):
        for Card in self._cards:
            if Card.suit==suit:
               Card.trump=True

    @property
    def is_empty(self):
        return self.size==0


class Card:
    
    def __init__(self,suit, value):
        self.suit=suit
        self.value=value
        self.trump=False
        letters={14:'A', 13:'K', 12:'Q', 11:'J'}
        self.letter=letters.get(self.value, str(self.value))

    def show(self):
        print ('{} of {}'.format(self.letter, self.suit))

