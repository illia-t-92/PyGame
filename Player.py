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

    def trumps(self, trump_suit):
        return [card for card in self.hand if card.trump==True]

    def lowest_trump(self):
        trumps=sorted(self.trumps(),key=lambda card: card.value)
        if not trumps:
            return None
        return trumps[0]
    
    @property
    def hand_size(self):
        return len(self.hand)

    def play_card(self, suit, letter):
        selected_card=next((Card for Card in self.hand if Card.suit==suit and Card.letter==str(letter), None)
        return selected_card
    
