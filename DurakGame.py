from Durak import Fool

game=Fool()
   
 #dealing cards and setting trump card
 game.deal_cards()
 game.get_trump()
 print(f'-- Trump suit is {game.trump_suit} --')

 #run game until win condition is met and status of the game is changed to 'fin'
 while game.status<>'fin':
     game.next_move()      

