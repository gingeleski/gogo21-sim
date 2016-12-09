from Deck import Deck
from Hand import Hand


class Game:
    @staticmethod
    def simulate():
        """
        Simulates a single game, distributing one 52-card deck
        across 4 possible hands
        """
        blackjacks = 0
        discards = 0
        hands = []
        for _ in range(1,5):
            hands.append(Hand())
        deck = Deck()
        this_card = deck.draw_card()
        while this_card != None:
            # TODO card-to-hand distribution logic
            this_card = deck.draw_card()
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

    def run(self, num_runs=1):
        """
        Conduct given number of simulations then
        print results
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
