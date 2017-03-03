import unittest

from my_app import first_letter_is_uppercase

class AppTest(unittest.TestCase):

    def test_first_letter_of_word_is_uppercase(self):
        self.assertTrue(first_letter_is_uppercase("Word"))

if __name__ == '__main__':
    unittest.main()

