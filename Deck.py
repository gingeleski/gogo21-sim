from Card import Card
from random import shuffle


class Deck:
    def __init__(self):
        """
        Builds a new, shuffled deck of 52 playing cards, with their counts
        """
        self.cards = []
        for _ in range(1,5):
            self.cards.append(Card(1,11))
            for i in range(2,10):
                self.cards.append(Card(i))
            for _ in range(1,5):
                self.cards.append(Card(10))
        shuffle(self.cards)
        self.card_counts = dict()
        for i in range(1, 10):
            self.card_counts[i] = 4
        self.card_counts[10] = 16
        self.card_counts[11] = 4
        self.possible_values = [0]

    def get_card_counts(self):
        """
        :return: card_counts
        """
        return self.card_counts

    def draw_card(self):
        if len(self.cards) > 0:
            this_card = self.cards[-1]
            del self.cards[-1]
            value = this_card.get_value()
            self.card_counts[value] -= 1
            if this_card.has_alt_value():
                value = this_card.get_alt_value()
                self.card_counts[value] -= 1
            return this_card
        return None
