import unittest

from simple_calculator import SimpleCalculator
class TestSimpleCalculor (unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1, 3), 4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 10), 30)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(6, 0), None)                        
