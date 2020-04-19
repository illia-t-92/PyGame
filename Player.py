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

    def play_card(self, suit, letter):
        selected_card=next((Card for Card in self.hand if Card.suit=suit and Card.letter=str(letter), None)
        return selected_card
    
