from Deck import Deck
from Hand import Hand

GOAL = 21


class Game:
    @staticmethod
    def simulate():
        """
        Simulates a single game, distributing one 52-card deck across
        4 possible hands
        """
        blackjacks = 0
        discards = 0
        hands = []
        for _ in range(0, 4):
            hands.append(Hand())
        deck = Deck()
        this_card = deck.draw_card()
        used_card = False
        while this_card is not None:
            for x in range(0, 4):
                if hands[x].can_make_value(this_card, GOAL):
                    hands[x].add_card(this_card)
                    used_card = True
                    break
            if used_card is False:
                card_counts = deck.get_card_counts()
                for i in range(16, 0, -1):
                    for key, val in card_counts.items():
                        if val == i:
                            for x in range(0, 4):
                                if hands[x].can_make_value(this_card, GOAL - key):
                                    hands[x].add_card(this_card)
                                    used_card = True
                                    break
                            if used_card is True:
                                break
                    if used_card is True:
                        break
            if used_card is False:
                for x in range(0, 4):
                    if hands[x].can_add_card(this_card):
                        hands[x].add_card(this_card)
                        used_card = True
                        break
            if used_card is False:
                discards += 1
            this_card = deck.draw_card()
            used_card = False
        for x in range(0, 4):
            blackjacks += hands[x].get_blackjacks()
        return blackjacks, discards

    @staticmethod
    def print_results(num_runs, blackjacks, discards):
        """
        Pretty print Monte Carlo run results
        """
        avg_blackjacks = blackjacks / num_runs
        avg_discards = discards / num_runs
        print("Simulated games: " + str(num_runs))
        print("Total blackjacks: " + str(blackjacks))
        print("Total discards: " + str(discards))
        print("---------------------------------")
        print("Blackjacks / game = " + str(avg_blackjacks))
        print("Discards / game = " + str(avg_discards))

    def run(self, num_runs=100000):
        """
        Conduct given number of simulations then print results
        """
        run_counter = 1
        total_blackjacks = 0
        total_discards = 0
        while run_counter <= num_runs:
            blackjacks, discards = self.simulate()
            total_blackjacks += blackjacks
            total_discards += discards
            run_counter += 1
        self.print_results(num_runs, total_blackjacks, total_discards)

if __name__ == "__main__":
    game = Game()
    game.run()
