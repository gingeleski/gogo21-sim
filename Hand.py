MAX_VALUE = 21

class Hand:
    def __init__(self):
        self.blackjacks = 0
        self.possible_values = [0]

    def blackjack(self):
        self.blackjacks += 1
        self.possible_values = [0]

    def can_add_card(self, card):
        """
        Tests if possible to add the given card to the hand

        :param card:
        :return:
        """
        if min(self.possible_values) + card.get_value() <= MAX_VALUE:
            return True
        return False

    def can_make_value(self, card, value):
        """
        Tests if possible to make the target value with the given card

        :param card:
        :param value:
        :return:
        """
        for pv in self.possible_values:
            if pv + card.get_value() == value:
                return True
            if card.has_alt_value() and pv + card.get_alt_value() == value:
                return True
        return False

    def add_card(self, card):
        self.possible_values = [i + card.get_value()
                                for i in self.possible_values]
        if card.has_alt_value():
            temp = []
            for i in self.possible_values:
                temp.append(i + card.get_alt_value() - card.get_value())
            for x in temp:
                self.possible_values.append(x)
            if MAX_VALUE in self.possible_values:
                self.blackjack()
