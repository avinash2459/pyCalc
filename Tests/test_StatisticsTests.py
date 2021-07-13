import unittest

from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader


class StatisticsTests(unittest.TestCase):
    sample_data = CsvReader('Tests/Data/statistics_data.csv').data

    column1 = [int(row["value1"]) for row in sample_data]
    mean = float(sample_data[0]["mean"])
    # column1 = []

    # for row in sample_data:
    #     column1.append(row)

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean_statistics(self):
        self.assertEqual(self.statistics.mean(self.column1), self.mean)
        self.assertEqual(self.statistics.result, self.mean)


if __name__ == '__main__':
    unittest.main()
