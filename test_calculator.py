import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    # Test add() 
    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(-1, 2), 1)

    # Test subtract() 
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # Test multiply() 
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # Test divide() 
    def test_divide1(self):
        self.assertEqual(self.calc.divide(14, 3), 4)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(17, 5), 3)

    # Test modulo() 
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(14, 3), 2)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(15, 5), 0)

if __name__ == '__main__':
    unittest.main()