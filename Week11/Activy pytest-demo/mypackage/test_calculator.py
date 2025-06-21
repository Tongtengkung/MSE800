import unittest  
from calculator import add, subtract, multiply, divide, root, power, trigonometric_sine

# Test cases for the calculator functions
# Each function tests a specific operation of the calculator

class TestMathOperations(unittest.TestCase):            # Test class inheriting from unittest.TestCase
    def test_add(self):                                 # Test "add"
        self.assertEqual(add(2, 3), 5)                  # Test  2 + 3 = 5
        self.assertEqual(add(-1, 1), 0)                 # Test -1 + 1 = 0 (negative number)

    def test_subtract(self):                            # Test "subtract"
        self.assertEqual(subtract(10, 5), 5)            # Test 10 - 5 = 5
        self.assertEqual(subtract(5, 10), -5)           # Test 5 - 10 = -5 (negative result)
        self.assertEqual(subtract(0, 0), 0)             # Test 0 - 0 = 0 (zero result)

    def test_multiply(self):                            # Test "multiply"
        self.assertEqual(multiply(3, 4), 12)            # Test 3 * 4 = 12
        self.assertEqual(multiply(0, 5), 0)             # Test 0 * 5 = 0 (multiplication by zero)      
        self.assertEqual(multiply(-1, 5), -5)           # Test -1 * 5 = -5 (negative number)

    def test_divide(self):                              # Test "divide"
        self.assertEqual(divide(10, 2), 5)              # Test 10 / 2 = 5
        self.assertEqual(divide(9, 3), 3)               # Test 9 / 3 = 3    
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):             # Test division by zero raises ValueError
            divide(10, 0)                               # Expecting ValueError when dividing by zero

    def test_root(self):
        with self.assertRaises(ValueError):                 # Test square root of negative number raises ValueError
            root(-1)                                        # Expecting ValueError when computing square root of negative number
        self.assertEqual(root(4), 2)                        # Test square root of 4 is 2
        self.assertEqual(root(0), 0)                        # Test square root of 0 is 0

    def test_power(self):
        self.assertEqual(power(2, 3), 8)                    # Test 2 raised to the power of 3 is 8
        self.assertEqual(power(5, 0), 1)                    # Test any number raised to the power of 0 is 1
        self.assertEqual(power(3, -1), 1/3)                 # Test negative exponent (3^-1 = 1/3)

    def test_trigonometric_sine(self):
        self.assertAlmostEqual(trigonometric_sine(0), 0)         # Test sine of 0 degrees is 0
        self.assertAlmostEqual(trigonometric_sine(30), 0.5)      # Test sine of 30 degrees is 0.5
        self.assertAlmostEqual(trigonometric_sine(90), 1)        # Test sine of 90 degrees is 1
        self.assertAlmostEqual(trigonometric_sine(180), 0)       # Test sine of 180 degrees is 0
        self.assertAlmostEqual(trigonometric_sine(270), -1)      # Test sine of 270 degrees is -1
        self.assertAlmostEqual(trigonometric_sine(360), 0)       # Test sine of 360 degrees is 0

if __name__ == '__main__':                              # Main block to run the tests                            
    unittest.main()
