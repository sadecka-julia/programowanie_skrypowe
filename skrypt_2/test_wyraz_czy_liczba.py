import wyraz_czy_liczba
import unittest


class Test_TestZ2(unittest.TestCase):
    def test_only_word(self):
        self.assertEqual(wyraz_czy_liczba.wyraz_czy_liczba('WyrAz'), ('WyrAz', ''))

    def test_only_numbers(self):
        self.assertEqual(wyraz_czy_liczba.wyraz_czy_liczba('187301'), ('', '187301'))

    def test_numbers_and_letters(self):
        self.assertEqual(wyraz_czy_liczba.wyraz_czy_liczba('kj231kuwb'), ('kjkuwb', '231'))

    def test_polish_letters(self):
        self.assertEqual(wyraz_czy_liczba.wyraz_czy_liczba('ąĘćłń'), ('ąĘćłń', ''))

    def test_letter_and_numbers(self):
        self.assertEqual(wyraz_czy_liczba.wyraz_czy_liczba('qwerty123456'), ('qwerty', '123456'))


if __name__ == '__main__':
    unittest.z2()
