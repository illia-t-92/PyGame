from Cards import Deck, Card
from Player import Player


class Fool:

    def get_players(self): #getting list of players
        player_no=0
        while player_no==0:
            input_string=input(f'Please, list names of players separted by ","') 
            player_list=input_sting.split(',')
            if not 2<len(player_list)>6:
                print('Invalid number of players. Must be between 2 and 6')
            elif:
                player_no=len(player_list)
                self._players=[Player(name) for player in player_list]

    def get_trump(self):
        deck=Deck()
        deck.shuffle
        trump_suit=deck._cards[-1].suit #getting the suit of the last card in the deck
        deck.set_trump(trump_suit)
        print(f'Trump suit is {trump_suit}')

    def deal_cards(self):
        loop_count=0
        while loop_count < player_no*6: #TODO: move hand-size to setting for general method
            for player in _players:
                player.draw_card()

    def first_player(self): #indentify who moves first based on the lowest trump card value
        trumps={}
        for player in _players:
            trumps.update({player.lowest_trump.value: player})
        sorted_trumps=sorted(trumps.keys())
        lowest_key=sorted_trumps[0]
        first_player=trumps[lowest_key]
        _players.insert(0, first_player)#move player to the first position in the list of players
        print(f'{first_player.name} has {player.lowest_trump.show()}. He moves first.'
        return first_player #returns Player object

    def next_move(self):
        offender=_players.pop(0)
        defender=_players[0]
        _players.append(offender)
        print(f'----{offender.name} goes to {defender.name}----')
       
       offender_endmove=False
       while offender_endmove==False: #continue until offender ends the move
           if offender.hand_size==0:
               offender_endmove=True

