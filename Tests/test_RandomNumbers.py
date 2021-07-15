import unittest

from RandomNumbers.RandomNumberGenerator import RandomNumberGenerator


class RandomNumberTests(unittest.TestCase):

    def setUp(self) -> None:
        self.randomgenerator = RandomNumberGenerator()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.randomgenerator, RandomNumberGenerator)

    def test_decorator_statistics(self):
        self.assertIsInstance(self.randomgenerator, RandomNumberGenerator)

    def test_random_with_seed(self):
        result = self.randomgenerator.random_with_seed(1, 300, 4)
        print(result)

    def test_random_without_seed(self):
        result = self.randomgenerator.random_without_seed(1, 300)
        print(result)

    def test_randomlist_with_seed(self):
        result = self.randomgenerator.randomlist_with_seed(1, 300, 4, 10)
        print(result)


if __name__ == '__main__':
    unittest.main()
