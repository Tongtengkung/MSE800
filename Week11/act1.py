import unittest                                         # importing the unittest module

def add(x, y):                                          # Function to add two numbers and combine them
    return x + y

class TestMathOperations(unittest.TestCase):            # Test class inheriting from unittest.TestCase
    def test_add(self):                                 # Test method to check the add function
        self.assertEqual(add(2, 3), 5)                  # Check if 2 + 3 equals 5
        self.assertEqual(add(-1, 1), 0)                 # Check if -1 + 1 equals 0

if __name__ == '__main__':                              # Main block to run the tests                            
    unittest.main()