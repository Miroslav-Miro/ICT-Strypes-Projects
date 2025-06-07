import unittest
from blackjack import (
    Player,
    calculate_hand_value,
    gameplay,
)


class TestPlayer(unittest.TestCase):
    def test_bet_money(self):
        player = Player(1000)
        player.bet_money(200)
        self.assertEqual(player.bank, 800)

    def test_add_money(self):
        player = Player(500)
        player.add_money(300)
        self.assertEqual(player.bank, 800)


class TestHandValue(unittest.TestCase):
    def test_hand_value_with_number_and_face_card(self):
        self.assertEqual(calculate_hand_value(["Two", "King"]), 12)

    def test_hand_value_with_ace_under_21(self):
        self.assertEqual(calculate_hand_value(["Ace", "Nine"]), 20)

    def test_hand_value_with_ace_over_21(self):
        self.assertEqual(
            calculate_hand_value(["Ace", "King", "Queen"]), 31 - 10
        )  # Ace -> 1


class TestGameplay(unittest.TestCase):
    def test_gameplay_busted(self):
        player = Player(1000)
        player_cards = ["King", "Queen", "Three"]  # 10 + 10 + 3 = 23
        outputs = []

        def fake_input(_):
            return "BET"

        def fake_output(msg):
            outputs.append(msg)

        result = gameplay(
            player_cards,
            100,
            "BET",
            player,
            input_func=fake_input,
            output_func=fake_output,
        )
        self.assertEqual(result, "busted")
        self.assertTrue(any("BUSTED" in msg for msg in outputs))

    def test_gameplay_draw(self):
        player = Player(1000)
        player.bet_money(100)
        outputs = []

        def fake_input(_):
            return "STAY"

        def fake_output(msg):
            outputs.append(msg)

        # Monkey-patch random.choice to force dealer's cards
        import random

        original_choice = random.choice
        random.choice = lambda x: "Ten"  # dealer: Ten + Ten = 20

        try:
            result = gameplay(
                ["Ten", "Ten"],
                100,
                "STAY",
                player,
                input_func=fake_input,
                output_func=fake_output,
            )
            self.assertEqual(result, "draw")
            self.assertTrue(any("draw" in msg.lower() for msg in outputs))
        finally:
            random.choice = original_choice


if __name__ == "__main__":
    unittest.main()
