from Cards import Deck, Card
from Player import Player


class Fool:

    def __init__(self):
        self.deck=Deck()
        self.status='play'
        self.fool=''
        HAND_SIZE=6

    def getplayers(self): #getting list of players
        player_no=0
        while player_no==0:
            input_string=input(f'Please, list names of players separted by ",": ') 
            player_list=input_string.split(',')
            if 2<len(player_list)<6:
                player_no=len(player_list)
                self.players=[Player(name) for name in player_list]
            else:
                print('Invalid number of players. Must be between 2 and 6')
                
    def get_trump(self):
        self.deck.shuffle()
        self.trump_suit=self.deck._cards[-1].suit #getting the suit of the last card in the deck
        self.deck.set_trump(self.trump_suit)

    def deal_cards(self, hand_size):
        loop_count=0
        while loop_count < len(self.players)*HAND_SIZE:
            for player in self.players:
                player.draw_card(self.deck)
                loop_count+=1
        print(f'Trump suit is {self.trump_suit}')
    
    def first_player(self):
        trumps={}
        for player in self.players: #indentify who moves first based on the lowest trump card value
            if not player.lowest_trump is None: #add to the dict only players with trumps
                trumps.update({player.lowest_trump.value: player})
        sorted_trumps=sorted(trumps.keys())
        lowest_key=sorted_trumps[0]
        self.first_player=trumps[lowest_key]
        self.players.insert(0, self.first_player) #move player to the first position in the list of players
        print(f'{self.first_player.name} has {self.first_player.lowest_trump.value} of {self.first_player.lowest_trump.suit}. He moves first.')
    
    @property
    def table(self): #initialize table object for the game
        return self.Table()

    def check_status(self):
        if self.deck.size==0: #when the deck is empty...
            for player in self.players: #...check each player's hand...
                if player.hand_size==0: #...when player has no cards on hand...
                    self.players.remove(player) #...remove him from the game...
        if len(self.players)==1: #when only one player left in the game...
            self.status='fin' #...the game ends...
            self.fool=self.players[0] #...and the fool is the last player with cards on hand.

                
    class Table():
        
        def __init__(self):
            self.offender_cards=[]
            self.defender_cards=[]
            #self.other_cards=[]
            self.discard_pile=[]

        def beat(self, offender_card, defender_card): #method to resolve played cards on table
            if defender_card.trump and not offender_card.trump:
                print(f'{defender_card.value} of {defender_card.suit} beats {offender_card.value} of {ofender_card.suit}')
                self.discard_pile.append(offender_card)
                self.discard_pile.append(offender_card)                
                return True
            elif not offender_card.suit==defender_card.suit:
                raise ValueError("Defender's card has invalid suit")
            elif defender_card.value > offender_card.value:
                print(f'{defender_card.value} of {defender_card.suit} beats {offender_card.value} of {ofender_card.suit}')
                return True

        def throw_in(self, card): #method to check if card of the same value is on table (for throw-ins)
            return any(table_card.value==card.value for table_card in offender_cards) or \
                   any(table_card.value==card.value for table_card in defernder_cards) or \
                   #any(table_card.value==card.value for table_card in other_cards)
            

