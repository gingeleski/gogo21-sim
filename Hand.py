class Hand:
    def __init__(self):
        self.cards = []
        self.possible_values = [0]
        self.blackjacks = 0

    def can_add(self, card):
        if (min(self.possible_values) + card.get_value()) <= 21:
            return True
        else:
            return False

    def add(self, card):
        self.possible_values = [i + card.get_value() for i in self.possible_values]
        if card.has_alt_value():
            temp = []
            for i in self.possible_values:
                temp.append(i + card.get_alt_value() - card.get_value())
            for x in temp:
                self.possible_values.append(x)
        if 21 in self.possible_values:
            self.blackjack()

    def blackjack(self):
        self.blackjacks += 1
        self.possible_values = [0]
        self.cards = []

    def get_possible_values(self):
        return self.possible_values

    def get_blackjacks(self):
        return self.blackjacks
