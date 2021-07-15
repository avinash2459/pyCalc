import unittest

from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class StatisticsTests(unittest.TestCase):
    sample_data = CsvReader('Tests/Data/statistics_data.csv').data

    column1 = [int(row["value1"]) for row in sample_data]
    mean = float(sample_data[0]["mean"])
    median = int(sample_data[0]["median"])
    mode = int(sample_data[0]["mode"])
    variance = float(sample_data[0]["variance"])
    sd = float(sample_data[0]["sd"])

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        self.assertEqual(self.statistics.mean(self.column1), self.mean)
        self.assertEqual(self.statistics.result, self.mean)

    def test_median_statistics(self):
        self.assertEqual(self.statistics.median(self.column1), self.median)
        self.assertEqual(self.statistics.result, self.median)

    def test_mode_statistics(self):
        self.assertEqual(self.statistics.mode(self.column1)[0], self.mode)
        self.assertEqual(self.statistics.result[0], self.mode)

    def test_variance_statistics(self):
        self.assertEqual(self.statistics.variance(self.column1), self.variance)
        self.assertEqual(self.statistics.result, self.variance)

    def test_variance_statistics(self):
        self.assertEqual(self.statistics.standard_deviation(self.column1), self.sd)
        self.assertEqual(self.statistics.result, self.sd)


if __name__ == '__main__':
    unittest.main()
