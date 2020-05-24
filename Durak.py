from Cards import Deck, Card
from Player import Player
import time


class Fool:

    def __init__(self):
        self.deck=Deck()
        self.status='play'
        self.fool=''
        self.HAND_SIZE=6
        self.moves_count=0
        self.endmove='no'

    def get_players(self): #getting list of players
        self.player_no=0
        while self.player_no==0:
            input_string=input(f'Please, list names of players separted by ",": ') 
            self.player_list=input_string.split(',')
            if 2<=len(self.player_list)<=6:
                self.player_no=len(self.player_list)
                self.players=[Player(name) for name in self.player_list]
            else:
                print('Invalid number of players. Must be between 2 and 6')
                
    def get_trump(self):
        self.deck.shuffle()
        self.trump_suit=self.deck._cards[-1].suit #getting the suit of the last card in the deck
        self.deck.set_trump(self.trump_suit)

    def deal_cards(self, hand_size):
        loop_count=0
        while loop_count < len(self.players)*self.HAND_SIZE:
            for player in self.players:
                player.draw_card(self.deck)
                loop_count+=1
        print(f'Trump suit is {self.trump_suit}')
        time.sleep(2)
    
    def get_first_player(self):
        trumps={}
        for player in self.players: #indentify who moves first based on the lowest trump card value
            if not player.lowest_trump is None: #add to the dict only players with trumps
                trumps.update({player.lowest_trump.value: player})
        sorted_trumps=sorted(trumps.keys())
        lowest_key=sorted_trumps[0]
        self.first_player=trumps[lowest_key]
        self.players.remove(self.first_player)
        self.players.insert(0, self.first_player) #move player to the first position in the list of players        
        print(f'{self.first_player.name} has {self.first_player.lowest_trump.value} of {self.first_player.lowest_trump.suit}. He moves first.')
        time.sleep(2)
    
    @property
    def table_is_not_full(self):
        if self.moves_count==0:
            if not len(self.table.offender_cards)<=5:
                return False
            else:
                return True
        else:
            if not len(self.table.offender_cards)<=6:
                return False
            else:
                return True
        
    
    def next_move(self):
        self.offender=self.players.pop(0)
        self.defender=self.players.pop(0)
        self.players.append(self.offender)
        print(f'{self.offender.name}, you have following cards...')
        time.sleep(2)
        self.offender.show_hand()
        selection =input(f'{self.offender.name}, enter letter and suit of the card to play: ')
        selection=selection.split(' ')        
        letter=selection[0]
        suit=selection[2]
        self.offender_card=self.offender.play_card(suit=suit, letter=str(letter))
        self.table.offender_cards.append(self.offender_card)
        time.sleep(2)
        print(f'{self.defender.name}, {self.offender.name} has moved with {self.offender_card.letter} of {self.offender_card.suit}')
        time.sleep(2)
        print('Select your card to beat or enter "take" to take the card')
        time.sleep(2)
        print('You have the following cards on hand:')
        time.sleep(2)
        self.defender.show_hand()
        selection=input()
        if selection=="take":
            self.defender.hand.append(self.offender_card) #append taken card to defender's hand
            self.offender.hand.remove(self.offender_card) #remove the card from offender's hand
            #self.table.offender_cards.pop() #remove card from table
            self.players.append=self.defender #move defender to the end of the players list
            self.endmove='yes'
            self.moves_count+=1
            self.check_status()
        else:
            selection=selection.split(' ')
            letter=selection[0]
            suit=selection[2]
            self.defender_card=self.defender.play_card(suit=suit, letter=letter)
            self.table.defender_cards.append(self.defender_card)
            if self.table.beat(offender_card=self.offender_card, defender_card=self.defender_card):
                self.players.insert(0,self.defender) #defender moves next
                self.offender.hand.remove(self.offender_card) #remove played cards from hand
                self.defender.hand.remove(self.defender_card) #remove played cards from hand
                self.check_status()
                print(f'{self.offender.name}, whant to throw in one more card? (y/n)')
                time.sleep(2)
                answer=input()
                if answer=='y':
                    self.next_move()
                else:
                    self.endmove='yes'
                    self.moves_count+=1
                    self.check_status()
                
            
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
                print(f'{defender_card.show()}beats {offender_card.show()}')
                self.discard_pile.append(offender_card)
                self.discard_pile.append(defender_card)                
                return True
            elif not offender_card.suit==defender_card.suit:
                raise ValueError("Defender's card has invalid suit")
            elif defender_card > offender_card:
                print(f'{defender_card.show()} beats {offender_card.show()}')
                return True
            elif not defender_card.value>offender_card.value:
                raise ValueError("Defender card's value is too low")

