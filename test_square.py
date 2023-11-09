import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_integer_side_area(self):
        res = area(5)
        self.assertEqual(res, 25)
    def test_integer_side_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_float_side_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)
    def test_float_side_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10)

    def test_zero_side_area(self):
        res = area(0)
        self.assertEqual(res, ValueError)
    def test_zero_side_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, ValueError)

    def test_negative_side_area(self):
        res = area(-10)
        self.assertEqual(res, ValueError)
    def test_negative_side_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, ValueError)

    def test_big_side_area(self):
        res = area(1.0e+100)
        self.assertEqual(res, 1.0e+200)
    def test_big_side_perimeter(self):
        res = perimeter(1.0e+100)
        self.assertEqual(res, 4.0e+100)

    def test_char_side_area(self):
        res = area('h')
        self.assertEqual(res, TypeError)
    def test_char_side_perimeter(self):
        res = perimeter('h')
        self.assertEqual(res, TypeError)
