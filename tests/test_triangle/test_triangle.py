import unittest

def area(a, h):
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_integer_sides_area(self):
        res = area(5, 10)
        self.assertEqual(res, 25)
    def test_integer_sides_perimeter(self):
        res = perimeter(5, 10, 10)
        self.assertEqual(res, 25)

    def test_float_sides_area(self):
        res = area(2.5, 7.5)
        self.assertEqual(res, 9.375)
    def test_float_sides_perimeter(self):
        res = perimeter(2.5, 5.5, 4.5)
        self.assertEqual(res, 12.5)

    def test_zero_sides_area(self):
        res = area(0, 10)
        self.assertEqual(res, "IllegalArgumentException")
    def test_zero_sides_perimeter(self):
        res = perimeter(0, 10, 10)
        self.assertEqual(res, "IllegalArgumentException")

    def test_negative_sides_area(self):
        res = area(-10, -10)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_sides_perimeter(self):
        res = perimeter(-10, -10, -10)
        self.assertEqual(res, "IllegalArgumentException")

    def test_big_sides_area(self):
        res = area(10000000000000000000000000000000000000000, 10000000000000000000000000000000000000000)
        self.assertEqual(res, 5e+79)
    def test_big_sides_perimeter(self):
        res = perimeter(10000000000000000000000000000000000000000, 10000000000000000000000000000000000000000, 10000000000000000000000000000000000000000)
        self.assertEqual(res, 30000000000000000000000000000000000000000)

    def test_char_sides_area(self):
        res = area('h', 10)
        self.assertEqual(res, "IllegalArgumentException")
    def test_char_sides_perimeter(self):
        res = perimeter('h', 10, 10)
        self.assertEqual(res, "IllegalArgumentException")

    def test_impossible_triangle_perimeter(self):
        res = perimeter(5, 10, 15)
        self.assertEqual(res, "IllegalArgumentException")