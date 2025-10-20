import unittest
from ..username import validate_name_input


class TestProcessNameInput(unittest.TestCase):

    def test_empty_input(self):
        name, response = validate_name_input("")
        self.assertEqual(name, "")
        self.assertIn("Don't be shy!", response)

    def test_noalpha_input(self):
        name, response = validate_name_input("foo123")
        self.assertEqual(name, "")
        self.assertIn("I love numbers", response)

    def test_name_input(self):
        name, response = validate_name_input("bina")
        self.assertEqual(name, "bina")
        self.assertIn("Would you like", response)
        self.assertIn("Bina", response)

    def test_input_with_spaces(self):
        name, response = validate_name_input("  bina   ")
        self.assertEqual(name, "bina")
        self.assertIn("Would you like", response)
        self.assertIn("Bina", response)

    def test_input_case_insensitiv(self):
        name, response = validate_name_input("biNa")
        self.assertEqual(name, "biNa")
        self.assertIn("Would you like", response)
        self.assertIn("Bina", response)


if __name__ == "__main__":
    unittest.main()
