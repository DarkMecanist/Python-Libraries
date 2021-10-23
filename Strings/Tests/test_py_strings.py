import unittest
from ..py_strings import Strings


class TestsIsValidEmail(unittest.TestCase):
    """is_valid_email unit tests"""

    def setUp(self):
        self.strings = Strings()

    def test_case_1(self):
        """Testing with a valid email"""

        email = "jmoutinho94@gmail.com"
        result = self.strings.is_valid_email(email)

        self.assertEqual(result, True)

    def test_case_2(self):
        """Testing with an invalid email"""

        email = "jmoutinhail.com"
        result = self.strings.is_valid_email(email)

        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()