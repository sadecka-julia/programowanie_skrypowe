import main
import unittest
import cmath
from fractions import Fraction


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)

    def test_sum_with_assertRaise(self):
        with self.assertRaises(TypeError):
            main.sum(2, 'Ala ma kota123')
            main.sum(2, [1, 2])

    def test_sum_fraction(self):
        self.assertEqual(main.sum(Fraction(2, 3), Fraction(2, 3)), Fraction(4, 3))

    def test_sum_complex_numbers(self):
        self.assertEqual(main.sum(complex(2, 5), complex(2, 3)), complex(4, 8))


if __name__ == '__main__':
    unittest.main()