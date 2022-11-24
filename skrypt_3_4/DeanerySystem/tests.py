import unittest
from class_day import Day
from term import Term


class Test_TestDay(unittest.TestCase):
    examp_1 = Term(Day.MON, 7, 10)
    examp_2 = Term(Day.FRI, 10, 25)
    examp_3 = Term(Day.WED, 11, 20)
    examp_4 = Term(Day.WED, 11, 40)
    examp_5 = Term(Day.MON, 7, 10)

    def test_print(self):
        examp_1 = Term(Day.MON, 7, 10)
        examp_2 = Term(Day.FRI, 10, 25)
        self.assertEqual(str(examp_1), '"7:10 [90]"')
        self.assertEqual(str(examp_2), '"10:25 [90]"')

    def test_earlierThan(self):
        self.assertTrue(self.examp_1.earlierThan(self.examp_2))
        self.assertTrue(self.examp_3.earlierThan(self.examp_4))

    def test_laterThan(self):
        self.assertFalse(self.examp_1.laterThan(self.examp_2))
        self.assertFalse(self.examp_3.laterThan(self.examp_4))
        self.assertTrue(self.examp_4.laterThan(self.examp_3))

    def test_equals(self):
        self.assertFalse(self.examp_1.equals(self.examp_2))
        self.assertFalse(self.examp_3.equals(self.examp_4))
        self.assertTrue(self.examp_5.equals(self.examp_1))


if __name__ == '__main__':
    unittest.main()
