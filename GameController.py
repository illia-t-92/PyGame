from Durak import Fool

game=Fool()
   
 #dealing cards and setting trump card 
game.get_players()
game.get_trump()
game.deal_cards(game.HAND_SIZE)
game.get_first_player()

 #run game until win condition is met and status of the game is changed to 'fin'
while not game.status=='fin':
    if game.moves_count==0:
        while game.table_is_not_full or not game.endmove=='yes':
            game.next_move()
            game.check_status

print("The fool is {}".format(game.fool.name))


