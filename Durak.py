from Cards import Deck, Card
from Player import Player


class Fool:

    def __init__(self):
        self.deck=Deck()

    def get_players(self): #getting list of players
        player_no=0
        while player_no==0:
            input_string=input(f'Please, list names of players separted by ",": ') 
            player_list=input_string.split(',')
            if 2<len(player_list)<6:
                player_no=len(player_list)
                self._players=[Player(name) for name in player_list]
            else:
                print('Invalid number of players. Must be between 2 and 6')
                

    def get_trump(self):
        self.deck.shuffle()
        trump_suit=self.deck._cards[-1].suit #getting the suit of the last card in the deck
        self.deck.set_trump(trump_suit)
        print(f'Trump suit is {trump_suit}')

    def deal_cards(self):
        loop_count=0
        while loop_count < len(self._players)*6: #TODO: move hand size to setting for general method
            for player in self._players:
                player.draw_card(self.deck)
                loop_count+=1

    def first_player(self): #indentify who moves first based on the lowest trump card value
        trumps={}
        for player in self._players:
            if not player.lowest_trump is None: #add to the dict only players with trumps
                trumps.update({player.lowest_trump.value: player})
        sorted_trumps=sorted(trumps.keys())
        lowest_key=sorted_trumps[0]
        first_player=trumps[lowest_key]
 
        self._players.insert(0, first_player)#move player to the first position in the list of players
        print(f'{first_player.name} has {player.lowest_trump.show()}. He moves first.')
        return first_player #returns Player object

"""
    def next_move(self):
        offender=_players.pop(0)
        defender=_players[0]
        _players.append(offender)
        print(f'----{offender.name} goes to {defender.name}----')
       
       offender_endmove=False
       while offender_endmove==False: #continue until offender ends the move
           if offender.hand_size==0:
               offender_endmove=True
"""
