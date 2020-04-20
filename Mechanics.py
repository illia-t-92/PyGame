import random
import time

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        letters = {"A": 14, 'K': 13, 'Q': 12, 'J': 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
        self.weight = letters.get(self.value)

    def show(self):
        return ('{} of {}'.format(self.value, self.suit)) # Поменял print на return


class Deck:
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = [str(n) for n in range(7, 11)] + list('JQKA')

    def __init__(self):
        self._cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def size(self):
        return len(self._cards)

    def shuffle(self):
        for i in range(len(self._cards) - 1, 0, -1):
            r = random.randint(0, i)
            self._cards[i], self._cards[r] = self._cards[r], self._cards[i]

    def draw_card(self):
        return self._cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            print ('{} of {}'.format(card.value, card.suit))


    # def show_hand(self):
    #     for card in self.hand:
    #         # card.show()
    #         print(f"{card.value} of {card.suit}")

deck1 = Deck()
deck1.shuffle()
game = "on"

player_1 = Player("Kostia")
player_2 = Player("Ilia")
player_3 = Player("Vova")
player_4 = Player("Valera")



Players_list = []
Players_list.append(player_1)
Players_list.append(player_2)
Players_list.append(player_3)
Players_list.append(player_4)

# Первый этап, раздаем карты, определяем козырь
print (f"Deck has {deck1.size()} cards.")
for Pl in Players_list:
    print(f"----- {Pl.name} takes cards -----")
    while len(Pl.hand) < 6:
        a = deck1.draw_card()
        print(f"{Pl.name} you draw card {a.value} of {a.suit}")
        Pl.hand.append(a)
        a=0
        # time.sleep(1)

    time.sleep(1)


Kozyr=deck1._cards[-1].suit
print (f"-- Kozyr is {Kozyr}. Deck has {deck1.size()} cards. --")

cycle = 1
otboy = 0
while game == "on":
    for Pl in Players_list:
        Offender = Players_list.pop(0)
        Defender = Players_list[0]
        Others_list = []
        if len(Players_list) > 1:
            Others_list = Players_list[1:]
        Players_list.append(Offender)
        print(f"----- {Offender.name} goes to {Defender.name} -----")
        time.sleep(1)

        print (f"-- {Offender.name} what card would you like to use? --")
        c = 1
        for i in Offender.hand:
            print(f"press {c} to use {i.show()}")
            c += 1

        d = int(input())
        if d <= len(Offender.hand):
            Offender_card_index = d-1
        else:
            print ("My fucking god, you are retarded, stop the game, code #4")
            game = "off"
            break

        Offender_card = Offender.hand[Offender_card_index]
        print (f"{Offender.name} you picked {Offender_card.show()}")
        Offender.hand.pop(Offender_card_index)

        Offence_card_list = []
        Offence_card_list.append(Offender_card)
        time.sleep(1)

        # докидывает атакующий
        Dokidyvanie = "no"
        Perebor = "no"
        for i in Offender.hand:
            if i.weight == Offender_card.weight:
                Dokidyvanie = "yes"

        while Dokidyvanie == "yes":
            print(f"{Offender.name}, do you want dokinut' cards?")
            print(f"you have these cards:")
            for crd in Offender.hand:
                print(f"{crd.value} of {crd.suit}")
            print(f"- Kozyr is {Kozyr} -")
            print("Press --1-- if yes, press --2-- if no")
            answ = int(input())
            if answ == 2:
                Dokidyvanie = "no"
            elif answ == 1:
                print(f"-- {Offender.name} what card would you like to use? --")
                c = 1
                for i in Offender.hand:
                    print(f"press {c} to use {i.show()}")
                    c += 1
                d = int(input())
                if d <= len(Offender.hand):
                    Offender_card_index = d - 1
                else:
                    print("My fucking god, you are retarded, stop the game, code #6")
                    game = "off"
                    break

                Offender_chosen_card = Offender.hand[Offender_card_index]
                if Offender_chosen_card.weight == Offender_card.weight:
                    Offender_card = Offender_chosen_card
                    print(f"{Offender.name} you picked {Offender_card.show()}")
                    Offender.hand.pop(Offender_card_index)
                    Offence_card_list.append(Offender_card)

                else:
                    print("My fucking god, you are retarded, stop the game, code #7")
                    game = "off"
                    break

            else:
                print("My fucking god, you are retarded, stop the game, code #5")
                game = "off"
                break

            Dokidyvanie = "fin-1"

            for i in Offender.hand:
                if i.weight == Offender_card.weight and answ == 1:
                    Dokidyvanie = "yes"

            if otboy == 0 and len(Offence_card_list) >= 5 or otboy == 1 and len(Offence_card_list) >= len(Defender.hand): # Не работает
                Dokidyvanie = "fin-1"
                Perebor = "yes"


        # дальше докидывают остальные
        for Pl in Others_list:
            if Perebor == "no":
                for i in Pl.hand:
                    if i.weight == Offender_card.weight:
                        Dokidyvanie = "yes-1"
                    while Dokidyvanie == "yes-1":
                        print(f"{Pl.name}, do you want dokinut' cards?")
                        print("You have these cards:")
                        for crd in Pl.hand:
                            print(f"{crd.value} of {crd.suit}")
                        print(f"- Kozyr is {Kozyr} -")
                        print("Press --1-- if yes, press --2-- if no")
                        answ = int(input())
                        if answ == 2:
                            Dokidyvanie = "no"

                        elif answ == 1:
                            Dokidyvanie = "fin-2"
                            print(f"-- {Pl.name} what card would you like to use? --")
                            c = 1
                            for i in Pl.hand:
                                print(f"press {c} to use {i.show()}")
                                c += 1
                            d = int(input())
                            if d <= len(Pl.hand):
                                Offender_card_index = d - 1
                            else:
                                print("My fucking god, you are retarded, stop the game, code #8")
                                game = "off"
                                break

                            Offender_chosen_card = Pl.hand[Offender_card_index]
                            if Offender_chosen_card.weight == Offender_card.weight:
                                Offender_card = Offender_chosen_card
                                print(f"{Pl.name} you picked {Offender_card.show()}")
                                Pl.hand.pop(Offender_card_index)
                                Offence_card_list.append(Offender_card)

                            else:
                                print("My fucking god, you are retarded, stop the game, code #9")
                                game = "off"
                                break

                        else:
                            print("My fucking god, you are retarded, stop the game, code #10")
                            game = "off"
                            break


                        for crd in Pl.hand:
                            if crd.weight == Offender_card.weight and answ == 1:
                                Dokidyvanie = "yes-2"

                        if otboy == 0 and + len(Offence_card_list) >= 5 or otboy == 1 and len(Offence_card_list) >= len(Defender.hand): # Не работает
                            Dokidyvanie = "fin-2"
                            Perebor = "yes"

        # отбивающийся отбивается
        print(f"-- {Defender.name}, you have to battle these cards:")
        for i in Offence_card_list:
            print (f"{i.value} of {i.suit}")
        print("You have these cards in your hand:")
        Defender.show_hand()
        print(f"- Kozyr is {Kozyr} -")
        print("Press --1-- to beat it or --2-- take")
        e = int(input())
        if e == 1:
            for Offender_card in Offence_card_list:
                print(f"-- {Defender.name} what card would you like to use to beat {Offender_card.value} of {Offender_card.suit}? --")
                c = 1
                for i in Defender.hand:
                    print(f"press {c} to use {i.show()}")
                    c += 1

                d = int(input())
                if d <= len(Defender.hand):
                    Defender_card_index = d-1
                else:
                    print("My fucking god, you are retarded, stop the game, code #1")
                    game = "off"
                    break

                Defender_card = Defender.hand[Defender_card_index]
                print(f"{Defender.name} you picked {Defender_card.show()}")

                game_result = 0

                if Defender_card.suit == Offender_card.suit and Defender_card.weight > Offender_card.weight:
                    print("Defended successfully")
                    game_result = "Defended successfully"
                elif Defender_card.suit == Kozyr and not Offender_card.suit == Kozyr:
                    print("Defended Kozyrem successfully")
                    game_result = "Defended successfully"
                else:
                    print("Defender retarded")
                    game_result = "Defender retarded"

                if game_result == "Defended successfully":
                    print(f"{Defender.name} successfully used {Defender_card.show()} against {Offender_card.show()}")
                    Defender.hand.pop(Defender_card_index)
                if game_result == "Defender retarded":
                    print("My fucking god, you are retarded, stop the game, code #2")
                    game = "off"
                    break

        elif e == 2:
            print(f"{Defender.name} you took these cards:")
            for i in Offence_card_list:
                print(f"{i.value} of {i.suit}")
                Defender.hand.append(i)
            a = Players_list.pop(0)
            b = Players_list.pop(-1)
            Players_list.insert(0, b)
            Players_list.append(a)
        else:
            print("My fucking god, you are retarded, stop the game, code #3")
            game = "off"
            break

        # ниже игроки берут карты, если нужно и если они есть
        if len(Offender.hand) < 6:
            if deck1.size() > 0:
                print(f"----- {Offender.name} takes cards -----")
                while len(Offender.hand) < 6 and deck1.size() > 0:
                    a = deck1.draw_card()
                    print(f"{Offender.name} you draw card {a.value} of {a.suit}")
                    Offender.hand.append(a)
                    a = 0
                    # time.sleep(1)

                time.sleep(1)

        if len(Defender.hand) < 6:
            if deck1.size() > 0:
                print(f"----- {Defender.name} takes cards -----")
                while len(Defender.hand) < 6 and deck1.size() > 0:
                    a = deck1.draw_card()
                    print(f"{Defender.name} you draw card {a.value} of {a.suit}")
                    Defender.hand.append(a)
                    a = 0
                    # time.sleep(1)

                time.sleep(1)
        for Pl in Others_list:
            if len(Pl.hand) < 6:
                if deck1.size() > 0:
                    print(f"----- {Pl.name} takes cards -----")
                    while len(Pl.hand) < 6 and deck1.size() > 0:
                        a = deck1.draw_card()
                        print(f"{Pl.name} you draw card {a.value} of {a.suit}")
                        Pl.hand.append(a)
                        a = 0

        for Oth in Others_list:  # Не работает
            if len(Oth.hand) == 0:
                print (f"{Oth.name} wins and leaves the match")
                Others_list.remove(Oth)

        if len(Offender.hand) == 0 and len(Defender.hand) == 0:
            print("-----------------------------")
            print("------------DRAW-------------")
            print("-----------------------------")
            print("----Thank you for playing----")
            game = "fin"
            break

        if len(Offender.hand) == 0 and len(Others_list) == 0 and not len(Defender.hand) == 0:
            print("----------------------------------")
            print(f"-----{Defender.name} IS FOOL-----")
            print("----------------------------------")
            print("------Thank you for playing-------")
            game = "fin"
            break

        if len(Offender.hand) == 0 and len(Defender.hand) == 0 and len(Others_list) == 1:
            h = Others_list[0]
            print("---------------------------------")
            print(f"--------{h.name} IS FOOL--------")
            print("---------------------------------")
            print("------Thank you for playing------")
            game = "fin"
            break

    if game == "on":
        print("--- Next cycle ---")
        print(f"--- Deck has {deck1.size()} cards ---")
        print(f"--- Kozyr is {Kozyr} ---")
        cycle += 1