import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_car(self):
        result = rpn.calculate("1 1 ^")
        self.assertEqual(1, result)
    def test_car2(self):
        result = rpn.calculate("5 3 ^")
        self.assertEqual(125, result)
    def test_car3(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)
    def test_car4(self):
        result = rpn.calculate("6 2 ^")
        self.assertEqual(36, result)
    def test_mod(self):
        result = rpn.calculate("6 2 %")
        self.assertEqual(0, result)
    def test_mod2(self):
        result = rpn.calculate("5 2 %")
        self.assertEqual(1, result)
    def test_mod3(self):
        result = rpn.calculate("1 5 %")
        self.assertEqual(5, result)
