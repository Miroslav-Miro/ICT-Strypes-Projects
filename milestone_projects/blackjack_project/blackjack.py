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


def calculate_hand_value(cards: List[str]) -> int:
    """Calculate the total value of the hand, handling Ace as 11 or 1."""
    total_value = 0
    ace_count = 0

    for card in cards:
        if card in ["Jack", "Queen", "King"]:
            total_value += 10
        elif card == "Ace":
            total_value += 11
            ace_count += 1
        else:
            total_value += int(values[card])  # Use existing mapping

    # Adjust Aces from 11 to 1 if total is over 21
    while total_value > 21 and ace_count:
        total_value -= 10
        ace_count -= 1

    return total_value


def gameplay(
    player_cards,
    bet_amount,
    choice: str,
    player: Player,
    input_func=input,
    output_func=print,
) -> str:
    total_player_cards_value: int = sum(values[card] for card in player_cards)

    if choice == "BET":
        while choice == "BET":
            new_card = random.choice(ranks)
            player_cards.append(new_card)
            total_player_cards_value += values[new_card]
            output_func(f"Total cards value: {total_player_cards_value}")

            if total_player_cards_value > 21:
                output_func("You are BUSTED")
                return "busted"
            else:
                choice = input_func("--BET-- / --STAY--")
        return "STAY"
    elif choice == "STAY":
        dealer_cards_value: int = 0

        while True:
            dealer_card: str = random.choice(ranks)
            dealer_cards_value += values[dealer_card]
            output_func(
                f"Dealer draws: {dealer_card} ({values[dealer_card]}) -> Total: {dealer_cards_value}"
            )

            if dealer_cards_value == total_player_cards_value:
                player.add_money(bet_amount)
                output_func("It's a draw! Your money is returned.")
                return "draw"
            elif (
                dealer_cards_value > total_player_cards_value
                and dealer_cards_value <= 21
            ):
                output_func("Dealer wins. You lose your bet.")
                return "lose"
            elif dealer_cards_value > 21:
                player.add_money(bet_amount * 2)
                output_func("Dealer is busted! You win double your bet.")
                return "win"


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
    "Ace": 11,  # Ace is considered 11, but will be adjusted in calculate_hand_value
}

# Create a player with an initial bank of 1000
player: Player = Player(1000)


# Main game loop
def main_game():
    while player.bank > 0:
        print(f"\n--- Your bank: {player.bank} ---")
        print("You are on the table:")

        while True:
            try:
                bet_amount = int(input("Place your bet: "))
                if bet_amount <= 0:
                    print("Bet must be greater than 0.")
                elif bet_amount > player.bank:
                    print("You can't bet more than you have.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        print(f"You are betting: {bet_amount}")
        player.bet_money(bet_amount)

        player_cards: List[str] = []

        for _ in range(2):
            player_cards.append(random.choice(ranks))

        total_player_cards_value = sum(values[card] for card in player_cards)

        print(", ".join(player_cards))
        print(f"Your cards value: {total_player_cards_value}")

        # Initial choice
        while True:
            choice = input("--BET-- / --STAY--").strip().upper()
            if choice in {"BET", "STAY"}:
                break
            else:
                print("Invalid input. Type 'BET' or 'STAY'.")

        result = gameplay(player_cards, bet_amount, choice, player)

        if result == "busted":
            print("You busted and lost your bet.")
        elif result == "draw":
            print("Round ended in a draw.")
        elif result == "win":
            print("You won the round!")
        elif result == "lose":
            print("Dealer won. You lost your bet.")
    print("\nGame over! You're out of money.")


if __name__ == "__main__":
    main_game()
