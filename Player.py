from Cards import Card, Deck

class Player:
        
    def __init__(self, name):
        self.name=name
        self.hand=[]

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        

    def show_hand(self):
         for card in self.hand:
            card.show()

    def trumps(self):
        return [card for card in self.hand if card.trump==True]
    
    @property
    def lowest_trump(self):
        trumps=sorted(self.trumps(),key=lambda card: card.value)
        if not trumps:
            return None
        return trumps[0]
    
    @property
    def hand_size(self):
        return len(self.hand)

    def play_card(self, suit, letter):
        for card in self.hand:
            if card.suit==suit and card.letter==str(letter):
                return card
            else:
                return None            
    
