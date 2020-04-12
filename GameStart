if input ("Do you want to start the game?") == "Yes" or 'yes':
    play = True

class Player:
    def __init__ (self, active, name, number, level):
        self.active = active
        self.name = name
        self.number = number
        self.level = level

List_of_inactive_players = []
player_1 = Player(False, "no",1, 0)
player_2 = Player(False, "no",2, 0)
player_3 = Player(False, "no",3, 0)
player_4 = Player(False, "no",4, 0)
player_5 = Player(False, "no",5, 0)
player_6 = Player(False, "no",6, 0)

List_of_inactive_players.append(player_1)
List_of_inactive_players.append(player_2)
List_of_inactive_players.append(player_3)
List_of_inactive_players.append(player_4)
List_of_inactive_players.append(player_5)
List_of_inactive_players.append(player_6)

class Card:
    def __init__ (self, name, owner):
        self.name = name
        self.owner = owner

List_of_active_players = []
player_1 = Player(True, input("Enter your name"),1, 1)
List_of_active_players.append(player_1)
List_of_inactive_players.pop(0)

Number_of_players = int(input("How many other players will be in the game?"))

while Number_of_players > 0:
    a = List_of_inactive_players[0]
    a.name = input(f"Enter {a.number} player's name")
    List_of_active_players.append(a)
    List_of_inactive_players.pop(0)
    Number_of_players -= 1

List_of_active_players_names = []
for i in List_of_active_players:
    List_of_active_players_names.append(i.name)

print("List of active players names ",List_of_active_players_names)

for i in List_of_active_players_names:
    print (i)

def Words_in_list(a):
    for i in a:
        print (i)
        return i

print (f"Players {Words_in_list(List_of_active_players_names)} get ready")



while play:
    break
