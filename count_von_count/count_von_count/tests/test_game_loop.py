import unittest
from ..game_loop import validate_guess_input, right_guess, out_of_guesses


class TestValidateGuessInput(unittest.TestCase):

    def test_input_isdigit(self):
        guess, error = validate_guess_input("fifty")
        self.assertEqual(guess, None)
        self.assertIn("Sorry, but your", error)

    def test_input_not_in_range(self):
        guess, error = validate_guess_input("101")
        self.assertEqual(guess, None)
        self.assertIn("Please enter a", error)

        guess, error = validate_guess_input("0")
        self.assertEqual(guess, None)
        self.assertIn("Please enter a", error)

    def test_correct_input(self):
        guess, error = validate_guess_input("50")
        self.assertEqual(guess, 50)
        self.assertEqual(error, None)

    def test_input_with_spaces(self):
        guess, error = validate_guess_input("  50  ")
        self.assertEqual(guess, 50)
        self.assertEqual(error, None)


class TestRightGuess(unittest.TestCase):

    def test_win_in_1_guess(self):
        response = right_guess(50, 50, 1)
        self.assertIn("in 1 guess", response)

    def test_win_in_mulitple_guesses(self):
        response = right_guess(50, 50, 2)
        self.assertIn("in 2 guesses", response)

    def test_no_win(self):
        response = right_guess(51, 50, 1)
        self.assertEqual(None, response)


if __name__ == "__main__":
    unittest.main()
