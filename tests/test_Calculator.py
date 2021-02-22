import unittest

from src.calculator.calculator import Calculator
from src.CsvReader.CsvReader import CsvReader

class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("../tests/Data/Unit Test Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CsvReader("../tests/Data/Unit Test Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("../tests/Data/Unit Test Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.mult(row['Value 1'], row['Value 2']), result)

    def test_division(self):
        test_data = CsvReader("../tests/Data/Unit Test Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divi(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader("../tests/Data/Unit Test Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squ(row['Value 1']), result)

    def test_square_root(self):
        test_data = CsvReader("../tests/Data/Unit Test Square Root.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.root(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)



