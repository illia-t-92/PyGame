import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = [str(n) for n in range(2, 11)] + list('JQKA')

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


deck1 = Deck()
deck1.shuffle()


class Player:
    def __init__(self, name, carrds=[]):
        self.name = name
        self.carrds = carrds

    def show_carrds(self):
        if len(self.carrds) > 0:
            print(self.name, "you have these cards in your hand:")
            for i in self.carrds:
                print(i.value, "of", i.suit)
        else:
            print(self.name, "you have no cards in your hand")


player_1 = Player("Kostia")
player_2 = Player("Ilia")

player_1.show_carrds()  # тут видим что у игрока Кастя нет карт

player_1.carrds.append(deck1.draw_card())  # даем Косте 1 карту
player_2.carrds.append(deck1.draw_card())  # даем Илье 1 карту

player_1.show_carrds()  # В итоге обе карты у обоих игроков, вообще набор карт у всех игроков всегда синхронизирован
player_2.show_carrds()

