import unittest
from dekoratroy import Operacje


class Test_Dekoratory(unittest.TestCase):

    def test_decoratory(self):

        op = Operacje()

        x = op.suma(1, 2, 3)
        self.assertEqual(x[0], "1+2+3=6")
        self.assertEqual(x[1], 4)

        x = op.suma(1, 2)
        self.assertEqual(x[0], "1+2+4=7")
        self.assertEqual(x[1], 5)

        x = op.suma(1)
        self.assertEqual(x[0], "1+4+5=10")
        self.assertEqual(x[1], 5)
        self.assertTrue(x)

        x = op.roznica(2, 1)
        self.assertEqual(x[0], "2-1=1")
        self.assertEqual(x[1], 4)

        x = op.roznica(2)
        self.assertEqual(x[0], "2-4=-2")
        self.assertEqual(x[1], 5)

        x = op.roznica()
        self.assertEqual(x[0], "4-5=-1")
        self.assertEqual(x[1], 6)

        op['suma'] = [1, 2]
        op['roznica'] = [1, 2, 3]
        self.assertEqual(op.argumentySuma, [1, 2])
        self.assertEqual(op.argumentyRoznica, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()