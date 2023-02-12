# создаём класс Suit, к которому будем обращаться далее
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
        d.name = 'spades' # имя масти
        d.symbol = '♤' # значок
        return d # возвращаем self.symbol

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
        return self.name + self.suit.symbol # вывод имени и масти карты вместе


# класс Deck в котором прописываем колоду карт?
class Deck:
    cards: list[Card] # объект cards в котором список из объектов Card
    def __init__(self):    # я не знаю что такое инит, сорри)
        self.cards = list() # э а о э

    # функция чтобы взять карту из колоды
    def give_one_card(self):
        return self.cards.pop()

    # я хз, но похоже что эта функция вывод нам карту + "пробел"
    def to_text(self):
        text = ''
        for c in self.cards:
            text += c.to_text() + ' '
        return text

#класс, который составляет колоду карт
class DeckBuilder:
    cards: list[Card]

    # функция с списком "имени" карт
    def create_card_names_set(self):
        list1 = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return list1

    # функция с списком мастей карт
    def create_suits_set(self):
        suits = Suits()
        # из объекта делаем лист
        list2 = list()
        # добавляем в лист все масти suits
        list2.append(suits.clubs())
        list2.append(suits.diamond())
        list2.append(suits.spades())
        list2.append(suits.hearts())
        return list2

    def create_deck(self): #функция создания колоды
        self.cards = list() #делаем лист

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
                self.cards.append(c) #добавляем в список карту/ы

        d = Deck()
        d.cards = self.cards
        return d


db = DeckBuilder()
deck = db.create_deck()
print(deck.to_text())
print(len(deck.to_text())/2)

#на будущее:

# deck.shuffle()
# print(deck.to_text())

# def shuffle(self):
    #     pass