import random
from typing import List

# Global variable to store total value of player's cards


class Player:
    """
    Represents a player in the game with a bank balance.

    Attributes:
        bank (int): The player's current bank balance.
    """

    def __init__(self, bank: int) -> None:
        """
        Initialize the player with a starting bank amount.

        Args:
            bank (int): Initial amount of money the player has.
        """
        self.bank: int = bank

    def bet_money(self, amount: int) -> None:
        """
        Deducts a specified amount from the player's bank when a bet is placed.

        Args:
            amount (int): The amount to bet (subtract from bank).
        """
        self.bank -= amount

    def add_money(self, amount: int) -> None:
        """
        Adds a specified amount to the player's bank.

        Args:
            amount (int): The amount to add to the bank.
        """
        self.bank += amount


def gameplay(player_cards, bet_amount, choice: str) -> None:
    """
    Handles the gameplay loop based on the player's decision to BET or STAY.

    Args:
        choice (str): The initial player choice, either 'BET' or 'STAY'.
    """
    total_player_cards_value: int = 0

    if choice == "BET":
        while choice == "BET":
            player_cards.append(random.choice(ranks))
            total_player_cards_value += values[player_cards[-1]]

            print(f"Total cards value: {total_player_cards_value}")

            if total_player_cards_value > 21:
                print("You are BUSTED")
                break
            else:
                choice = input("--BET-- / --STAY--")
    else:
        dealer_cards_value: int = 0

        while True:
            # Draw a random card and add its value
            dealer_card: str = random.choice(ranks)
            dealer_cards_value += values[dealer_card]
            print(
                f"Dealer draws: {dealer_card} ({values[dealer_card]}) -> Total: {dealer_cards_value}"
            )

            if dealer_cards_value == total_player_cards_value:
                player.add_money(bet_amount)
                print("It's a draw! Your money is returned.")
                break

            elif dealer_cards_value > 21:
                player.add_money(bet_amount * 2)
                print("Dealer is busted! You win double your bet.")
                break


# Card ranks and their corresponding values
ranks: tuple[str, ...] = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values: dict[str, int] = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 10,
}

# Create a player with an initial bank of 1000
player: Player = Player(1000)


# Main game loop
def main_game():
    while player.bank > 0:
        print(f"\n--- Your bank: {player.bank} ---")
        print("You are on the table:")

        bet_amount: int = int(input("Place your bet: "))

        print(f"You betting: {bet_amount}")
        player.bet_money(bet_amount)

        total_player_cards_value = 0
        player_cards: List[str] = []

        for _ in range(2):
            player_cards.append(random.choice(ranks))

        total_player_cards_value = sum(values[card] for card in player_cards)

        print(", ".join(player_cards))
        print(f"Your cards value: {total_player_cards_value}")

        choice: str = input("--BET-- / --STAY--")

        gameplay(player_cards, bet_amount, choice)


main_game()
