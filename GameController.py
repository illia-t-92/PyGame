from Durak import Fool

game=Fool()
   
 #dealing cards and setting trump card 
game.get_trump()
game.deal_cards()
game.first_player()

 #run game until win condition is met and status of the game is changed to 'fin'
while game.status<>'fin':
    for player in game.players:
        

