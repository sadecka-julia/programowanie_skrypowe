import sys
print(sys.path)
from term import Term
from class_day import Day
from lesson_class import Lesson
import unittest

# lesson1 = Lesson(Term(Day.TUE, 9, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
# lesson2 = Lesson(Term(Day.MON, 18, 40), "Analiza", "Jan Nowak", 3)
# lesson3 = Lesson(Term(Day.THU, 18, 00), "WOW", "Witold Gombrowicz", 1)
# lesson4 = Lesson(Term(Day.SUN, 9, 40), "Algebra", "Marcin Wąs", 3, False)
# lesson5 = Lesson(Term(Day.FRI, 17, 40), "Systemy Operacyjne", "Joanna Agata", 5, False)
# lesson6 = Lesson(Term(Day.SAT, 11, 30), "Ochrona", "Anna Bratek", 1, False)

class Test_TestDay(unittest.TestCase):

    def test_laterDay(self):
        lesson1 = Lesson(Term(Day.TUE, 9, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.MON, 18, 40), "Analiza", "Jan Nowak", 3)
        lesson3 = Lesson(Term(Day.THU, 18, 00), "WOW", "Witold Gombrowicz", 1)
        lesson4 = Lesson(Term(Day.SUN, 9, 40), "Algebra", "Marcin Wąs", 3, False)
        lesson5 = Lesson(Term(Day.FRI, 17, 40), "Systemy Operacyjne", "Joanna Agata", 5, False)
        lesson6 = Lesson(Term(Day.SAT, 11, 30), "Ochrona", "Anna Bratek", 1, False)

        self.assertFalse(Lesson.laterDay(lesson3))
        self.assertFalse(Lesson.laterDay(lesson2))
        self.assertFalse(Lesson.laterDay(lesson6))
        self.assertTrue(Lesson.laterDay(lesson4))

    def test_earlier_day(self):
        lesson1 = Lesson(Term(Day.TUE, 9, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.MON, 18, 40), "Analiza", "Jan Nowak", 3)
        lesson3 = Lesson(Term(Day.THU, 18, 00), "WOW", "Witold Gombrowicz", 1)
        lesson4 = Lesson(Term(Day.SUN, 9, 40), "Algebra", "Marcin Wąs", 3, False)
        lesson5 = Lesson(Term(Day.FRI, 17, 40), "Systemy Operacyjne", "Joanna Agata", 5, False)
        lesson6 = Lesson(Term(Day.SAT, 11, 30), "Ochrona", "Anna Bratek", 1, False)

        self.assertTrue(Lesson.earlierDay(lesson1))
        self.assertFalse(Lesson.earlierDay(lesson3))
        self.assertTrue(Lesson.earlierDay(lesson6))
        self.assertFalse(Lesson.earlierDay(lesson4))

    def test_earlier_time(self):
        lesson1 = Lesson(Term(Day.TUE, 9, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.MON, 18, 40), "Analiza", "Jan Nowak", 3)
        lesson3 = Lesson(Term(Day.THU, 18, 00), "WOW", "Witold Gombrowicz", 1)
        lesson4 = Lesson(Term(Day.SUN, 9, 40), "Algebra", "Marcin Wąs", 3, False)
        lesson5 = Lesson(Term(Day.FRI, 17, 40), "Systemy Operacyjne", "Joanna Agata", 5, False)
        lesson6 = Lesson(Term(Day.SAT, 11, 30), "Ochrona", "Anna Bratek", 1, False)

        self.assertTrue(Lesson.earlierTime(lesson1))
        self.assertFalse(Lesson.earlierTime(lesson3))
        self.assertTrue(Lesson.earlierTime(lesson6))
        self.assertFalse(Lesson.earlierTime(lesson4))

    def test_later_time(self):
        lesson1 = Lesson(Term(Day.TUE, 8, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.MON, 18, 40), "Analiza", "Jan Nowak", 3)
        lesson3 = Lesson(Term(Day.FRI, 19, 10), "WOW", "Witold Gombrowicz", 1)
        lesson4 = Lesson(Term(Day.SUN, 9, 40), "Algebra", "Marcin Wąs", 3, False)
        lesson5 = Lesson(Term(Day.FRI, 17, 40), "Systemy Operacyjne", "Joanna Agata", 5, False)
        lesson6 = Lesson(Term(Day.SAT, 11, 30), "Ochrona", "Anna Bratek", 1, False)

        self.assertTrue(Lesson.laterTime(lesson1))
        self.assertFalse(Lesson.laterTime(lesson3))
        self.assertTrue(Lesson.laterTime(lesson5))
        self.assertTrue(Lesson.laterTime(lesson4))

unittest.main