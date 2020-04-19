from Cards import Card, Deck
from Player import Player


class DurakGame:

    def __init__(self, players):

        if not 2<=players<=6:
            raise ValueError('Invalid number of players: must be between 2 and 15 players')
        deck=Deck()
        deck.shuffle()
        trump_card=deck_draw_card()
        trump_suit=trump_card.suite
        trump_card.show()
        deck.append(trump_card)

    def play(attacker, defendant):
        
        successful_defense=[]
        discard_pile=[]
        
        attacker=attacker
        defendant=defendant

        while True
            attacker_move=input('{} select a card from your hand for move'.format(attacker.name))
            attacker.show_hand()
            attack=attacker.play_card(attacker_move)

            defendant_move=input(' {} select a card from your hand to defend'.format(defendant.name))
            defendant.show_hand()
            defense=defendant.play_card(defendant_move)

            if defense.suit!=attack.suite and defense.suite!=trump_suit:
                defendant_move=input('Wrong suit selected! Please, choose another')
                defense=defendant.play_card(defendant_move)
                if defense.suit=trump_suit and attack.suit=trump.suit:
                    if

