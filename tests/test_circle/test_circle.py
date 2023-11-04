import math
import unittest

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_integer_radius_area(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)
    def test_integer_radius_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_float_radius_area(self):
        res = area(2.5)
        self.assertEqual(res, 19.634954084936208)
    def test_float_radius_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 15.707963267948966)

    def test_zero_radius_area(self):
        res = area(0)
        self.assertEqual(res, "IllegalArgumentException")
    def test_zero_radius_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, "IllegalArgumentException")

    def test_negative_radius_area(self):
        res = area(-10)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_radius_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, "IllegalArgumentException")

    def test_big_radius_area(self):
        res = area(10000000000000000000000000000000000000000000000000000000000000000)
        self.assertEqual(res, 3.1415926535897935e+128)

    def test_big_radius_perimeter(self):
        res = perimeter(10000000000000000000000000000000000000000000000000000000000000000)
        self.assertEqual(res, 6.283185307179586e+64)

    def test_char_radius_area(self):
        res = area('h')
        self.assertEqual(res, "IllegalArgumentException")

    def test_char_radius_perimeter(self):
        res = perimeter('h')
        self.assertEqual(res, "IllegalArgumentException")


