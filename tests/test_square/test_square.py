import unittest

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

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
        self.assertEqual(res, "IllegalArgumentException")
    def test_zero_side_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, "IllegalArgumentException")

    def test_negative_side_area(self):
        res = area(-10)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_side_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, "IllegalArgumentException")

    def test_big_side_area(self):
        res = area(10000000000000000000000000000000000000000000000000000000000000000)
        self.assertEqual(res, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    def test_big_side_perimeter(self):
        res = perimeter(10000000000000000000000000000000000000000000000000000000000000000)
        self.assertEqual(res, 40000000000000000000000000000000000000000000000000000000000000000)

    def test_char_side_area(self):
        res = area('h')
        self.assertEqual(res, "IllegalArgumentException")

    def test_char_side_perimeter(self):
        res = perimeter('h')
        self.assertEqual(res, "IllegalArgumentException")
