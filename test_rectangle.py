import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_integer_sides_area(self):
        res = area(5, 10)
        self.assertEqual(res, 50)
    def test_integer_sides_perimeter(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_float_sides_area(self):
        res = area(2.5, 7.5)
        self.assertEqual(res, 18.75)
    def test_float_sides_perimeter(self):
        res = perimeter(2.5, 7.5)
        self.assertEqual(res, 20)

    def test_zero_sides_area(self):
        res = area(0, 10)
        self.assertEqual(res, ValueError)
    def test_zero_sides_perimeter(self):
        res = perimeter(0, 10)
        self.assertEqual(res, ValueError)

    def test_negative_sides_area(self):
        res = area(-10, - 5)
        self.assertEqual(res, ValueError)
    def test_negative_sides_perimeter(self):
        res = perimeter(-10, -5)
        self.assertEqual(res, ValueError)

    def test_big_sides_area(self):
        res = area(1.0e+100, 2.0e+100)
        self.assertEqual(res, 2.0e+200)
    def test_big_sides_perimeter(self):
        res = perimeter(1.0e+100, 2.0e+100)
        self.assertEqual(res, 6.0e+100)

    def test_char_sides_area(self):
        res = area('h', 5)
        self.assertEqual(res, TypeError)
    def test_char_sides_perimeter(self):
        res = perimeter('h', 5)
        self.assertEqual(res, TypeError)
