import unittest
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator


class CalculatorTests(unittest.TestCase):
    test_data = CsvReader('Tests/Data/UnitTestAll.csv').data

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        for row in self.test_data:
            self.assertEqual(self.calculator.add(row["avalue1"], row['avalue2']), int(row['aresult']))
            self.assertEqual(self.calculator.result, int(row['aresult']))

    def test_subtract_method_calculator(self):
        for row in self.test_data:
            self.assertEqual(self.calculator.subtract(row['svalue1'], row['svalue2']), int(row['subresult']))
            self.assertEqual(self.calculator.result, int(row['subresult']))

    def test_multiply_method_calculator(self):
        for row in self.test_data:
            self.assertEqual(self.calculator.multiply(row['mvalue1'], row['mvalue2']), int(row['mresult']))
            self.assertEqual(self.calculator.result, int(row['mresult']))

    def test_divide_method_calculator(self):
        for row in self.test_data:
            self.assertEqual(self.calculator.divide(row['dvalue2'], row['dvalue1']), float(row['divideresult']))
            self.assertEqual(self.calculator.result, float(row['divideresult']))

    def test_square_method_calculator(self):
        for row in self.test_data:
            self.assertEqual(self.calculator.square(row['sqvalue1']), int(row['sqresult']))
            self.assertEqual(self.calculator.result, int(row['sqresult']))

    def test_square_root_method_calculator(self):
        for row in self.test_data:
            self.assertEqual(self.calculator.square_root(row['sqrootvalue1']), float(row['sqrootresult']))
            self.assertEqual(self.calculator.result, float(row['sqrootresult']))


if __name__ == '__main__':
    unittest.main()
