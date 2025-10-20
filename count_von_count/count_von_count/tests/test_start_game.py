import unittest
from ..start_game import process_init_input


class TestProcessInitInput(unittest.TestCase):

    def test_input_lower(self):
        game_state, response = process_init_input("Bina", "YES")
        self.assertEqual(game_state, "break")

    def test_input_strip(self):
        game_state, response = process_init_input("Bina", "   no ")
        self.assertEqual(game_state, "exit")

    def test_input_yes(self):
        game_state, response = process_init_input("Bina", "yes")
        self.assertEqual(game_state, "break")
        self.assertIn("Alright! It's a", response)

    def test_input_no(self):
        game_state, response = process_init_input("Bina", "no")
        self.assertEqual(game_state, "exit")
        self.assertIn("I'm sorry that", response)

    def test_empty_input(self):
        game_state, response = process_init_input("Bina", "")
        self.assertEqual(game_state, "")
        self.assertIn("Sorry, I didn't", response)


if __name__ == "__main__":
    unittest.main()
