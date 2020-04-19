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

player_1 = Player("Kostia")
player_2 = Player("Ilia")
# Этап 1, раздача карт, определение козыря
deck_1 = Deck()
deck_1.shuffle()

player_1.draw_card(deck_1)
player_1.draw_card(deck_1)
player_1.show_hand()

player_2.draw_card(deck_1)
player_2.show_hand()