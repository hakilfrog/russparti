class Suit:  # AAAAAAAAAAA
    name: str
    symbol: str

    def to_text(self):
        return self.symbol


# Создание объекта

class Suits:
    def diamond(self):
        d = Suit()
        d.name = 'diamond'
        d.symbol = '♢'
        return d

    def spades(self):
        d = Suit()
        d.name = 'spades'
        d.symbol = '♤'
        return d

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


# пользовательский код
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

class Card:
    name: str
    suit: Suit

    def to_text(self):
        return self.name + self.suit.symbol


class Deck:
    cards: list[Card]

    def __init__(self):
        self.cards = list()

    def give_one_card(self):
        return self.cards.pop()

    def to_text(self):
        text = ''
        for c in self.cards:
            text += c.to_text() + ' '
        return text

    # def shuffle(self):
    #     pass


class DeckBuilder:
    cards: list[Card]

    def create_card_names_set(self):
        list1 = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return list1

    def create_suits_set(self):
        suits = Suits()
        list2 = list()
        list2.append(suits.clubs())
        list2.append(suits.diamond())
        list2.append(suits.spades())
        list2.append(suits.hearts())
        return list2

    def create_deck(self):
        self.cards = list()

        # для каждой масти s
        suits = self.create_suits_set()
        names = self.create_card_names_set()
        for su in suits:
            # для каждого имени карты n
            for na in names:
                # создать объект карты c
                c = Card()
                c.name = na
                c.suit = su
                # print(na,su.symbol)
                self.cards.append(c)

        d = Deck()
        d.cards = self.cards
        return d


db = DeckBuilder()
deck = db.create_deck()
print(deck.to_text())
print(len(deck.to_text())/2)
# deck.shuffle()
# print(deck.to_text())
# abobus xd