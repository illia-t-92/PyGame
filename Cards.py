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

    def get_card(self, position):
        return self._cards[position]
