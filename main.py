import random


# создаём класс Suit (масть), к которому будем обращаться далее
class Suit:
    name: str
    symbol: str

    def to_text(self):
        return self.symbol


# Создание объекта
# Класс суитс, где мы обозначаем каждую масть
class Suits:
    # создаём функцию на каждую масть, где прописываем нужные параметры, обращаясь к классу Suit
    def diamond(self):
        d = Suit()
        d.name = 'diamond'
        d.symbol = '♢'
        return d

    def spades(self):
        d = Suit()
        d.name = 'spades'  # имя масти
        d.symbol = '♤'  # значок
        return d  # возвращаем объект Suit (пики)

    def clubs(self):
        d = Suit()
        d.name = 'clubs'
        d.symbol = '♧'
        return d

    def hearts(self):
        d = Suit()
        d.name = 'hearts'
        d.symbol = '♡'
        return d


# пользовательский код чтобы чисто затестить вывод мастей (уже не нужен(вроде))
# def tests():
#     s = Suits()
#     diamond = s.diamond()
#     print(diamond.to_text())
#     spades = s.spades()
#     print(spades.to_text())
#     clubs = s.clubs()
#     print(clubs.to_text())
#     hearts = s.hearts()
#     print(hearts.to_text())
#
# tests()

# класс Card, прописываем параметры, имя и масть, обращаясь к классу Suit
class Card:
    name: str
    suit: Suit

    def to_text(self):
        return self.name + self.suit.symbol  # вывод имени и масти карты вместе


# класс Deck в котором прописываем колоду карт?
class Deck:
    cards: list[Card]  # объект cards в котором список из объектов Card

    def __init__(self):  # я не знаю что такое инит, сорри)
        self.cards = list()  # э а о э

    def shuffle(self):
        random.shuffle(self.cards)

    # функция чтобы взять карту из колоды
    def give_one_card(self):
        return self.cards.pop()

    # я хз, но похоже что эта функция вывод нам карту + "пробел"
    def to_text(self):
        text = ''
        for c in self.cards:
            text += c.to_text() + ' '
        return text


# класс, который составляет колоду карт

class DeckBuilder:
    cards: list[Card]

    def __init__(self):
        self.cards = list()

    def create_card_names_set(self):
        raise NotImplementedError()

    # функция со списком мастей карт
    def create_suits_set(self):
        suits = Suits()
        # из объекта делаем лист
        list_values_suits = list()
        # добавляем в лист все масти suits
        list_values_suits.append(suits.clubs())
        list_values_suits.append(suits.diamond())
        list_values_suits.append(suits.spades())
        list_values_suits.append(suits.hearts())
        return list_values_suits

    def create_deck(self):  # функция создания колоды
        self.cards = list()  # делаем лист

        suits = self.create_suits_set()
        names = self.create_card_names_set()
        # для каждой масти su
        for su in suits:
            # для каждого имени карты na
            for na in names:
                # создаем объект карты c
                c = Card()
                c.name = na
                c.suit = su
                # print(na,su.symbol)  # по идее эта строчка нужна, но с ней работает не так лол
                self.cards.append(c)  # добавляем в список карту/ы

        d = Deck()
        d.cards = self.cards
        return d


class SmallDeckBuilder(DeckBuilder):

    # функция с списком "имени" карт
    def create_card_names_set(self):
        list_36_values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return list_36_values


class FullDeckBuilder(DeckBuilder):

    def create_card_names_set(self):
        list_52_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return list_52_values


db36 = SmallDeckBuilder()
deck36 = db36.create_deck()
# print(deck36.to_text())  # изначальная колода

deck36.shuffle()  # рандомим колоду
print(deck36.to_text())  # вывод рандомизированной колоды

db52 = FullDeckBuilder()
deck52 = db52.create_deck()
deck52.shuffle()  # рандомим колоду
print(deck52.to_text())  # изначальная колода
c = deck52.give_one_card()
print(c.to_text())  # вывод карты из колоды
print(deck52.to_text())  # вывод рандомизи
