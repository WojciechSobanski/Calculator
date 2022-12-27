###Simple calculator with tests. ###

import unittest

#Calculator function
class Calculator:


    def add(self, a, b):
        return a + b


    def sub(self, a, b):
        return a - b


    def multiplication (self, a, b):
       return a * b


    def division (self, a, b):
       return a / b

#Calculator function tests
class CalculatorTest(unittest.TestCase):


    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(1, 3), 4)


    def test_sub(self):
        calc = Calculator()
        self.assertTrue(calc.sub(5, 3) == 2)


    def test_multiplication(self):
        calc = Calculator()
        self.assertTrue(calc.multiplication(2, 2) == 4)


    def test_division(self):
        calc = Calculator()
        self.assertEqual(calc.division(4, 2), 2)


unittest.main()
