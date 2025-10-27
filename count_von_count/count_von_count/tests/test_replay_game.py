import unittest
from ..replay_game import process_replay_input


class TestProcessReplayInput(unittest.TestCase):

    def test_input_yes(self):
        game_state, response = process_replay_input("bina", "yes")
        self.assertEqual(game_state, "break")
        self.assertEqual(response, "")

    def test_input_no(self):
        game_state, response = process_replay_input("bina", "no")
        self.assertEqual(game_state, "exit")
        self.assertIn("Thank you for", response)

    def test_wrong_input(self):
        game_state, response = process_replay_input("bina", "tes")
        self.assertEqual(game_state, None)
        self.assertIn("Sorry, I didn't", response)

    def test_input_with_spaces(self):
        game_state, response = process_replay_input("bina", "  yes  ")
        self.assertEqual(game_state, "break")
        self.assertEqual(response, "")

    def test_input_case_insensitiv(self):
        game_state, response = process_replay_input("bina", "yEs")
        self.assertEqual(game_state, "break")
        self.assertEqual(response, "")


if __name__ == "__main__":
    unittest.main()
