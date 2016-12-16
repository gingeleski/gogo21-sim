from Deck import Deck
from Hand import Hand
from random import shuffle


GOAL = 21

class Game:

    def simulate(self):
        """
        Simulates a single game, distributing one 52-card deck across
        4 possible hands
        """
        total_throwaways = 0
        total_blackjacks = 0

        deck = Deck()

        hands = []
        for _ in range(1, 5):
            hands.append(Hand())

        this_card = deck.draw_card()

        while this_card is not None:
            used_card = False
            for hand in hands:
                if hand.can_make(this_card, GOAL):
                    hand.add(this_card)
                    used_card = True
                    break
            if used_card is False:
                card_counts = deck.get_card_counts()
                for c in range(16,0,-1):
                    for key, value in card_counts.items():
                        if value == c:
                            for hand in hands:
                                if hand.can_make(this_card, GOAL - key):
                                    hand.add(this_card)
                                    used_card = True
                                    break
                        if used_card is True:
                            break
                    if used_card is True:
                        break
            if used_card is False:
                for hand in hands:
                    if hand.can_add(this_card):
                        hand.add(this_card)
                        used_card = True
                        break
            if used_card is False:
                total_throwaways += 1
            this_card = deck.draw_card()

        for hand in hands:
            total_blackjacks += hand.get_blackjacks()

        return total_blackjacks, total_throwaways

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
