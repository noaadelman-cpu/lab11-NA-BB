import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

     def test_add(self): # 3 assertions
         self.assertEqual(add(1, 2), 3)
         self.assertEqual(add(3, 7), 10)
         self.assertEqual(add(14, -2), 12)

     def test_subtract(self): # 3 assertions
         self.assertEqual(subtract(5, 2), 3)
         self.assertEqual(subtract(10, 15), -5)
         self.assertEqual(subtract(-5, -3), -2)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 7), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(calculator.div(2, 10), 5.0)
        self.assertAlmostEqual(calculator.div(4, 20), 5.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)
    # ##########################

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 81), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 8)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)



    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5.0)

    def test_sqrt(self): # 3 assertions
         with self.assertRaises(ValueError):
            calculator.square_root(4)
         with self.assertRaises(ValueError):
            calculator.square_root(0)
         with self.assertRaises(ValueError):
            calculator.square_root(-1)


# Do not touch this
if __name__ == "__main__":
    unittest.main()