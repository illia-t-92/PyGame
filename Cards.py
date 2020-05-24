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
    
    def __init__(self,suit, letter):
        self.suit=suit
        self.letter=str(letter)
        self.trump=False
        values={'A':14, 'K':13, 'Q':12, 'J':11}
        self.value=values.get(self.letter, int(self.letter))

    def show(self):
        print ('{} of {}'.format(self.letter, self.suit))

    def __eq__(self, other):
        if self.suit==other.suit:
            return self.value==other.value and self.suit==other.suit
        else:
            NotImplemented

    def __gt__(self, other):
        if self.suit==other.suit:
            return self.value>other.value
        else:
            NotImplemented
    
    def __lt__(self, other):
        if self.suit==other.suit:
            return self.value<other.value
        else:
            NotImplemented

    def __ge__(self, other):
        if self.suit==other.suit:
            return self.value>=other.value
        else:
            raise NotImplementedError('Comparison of different suits is not implemented')

    def __le__(self, other):
        if self.suit==other.suit:
            return self.value<=self.value
        else:
            raise NotImplementedError('Comparison of different suits is not implemented')
