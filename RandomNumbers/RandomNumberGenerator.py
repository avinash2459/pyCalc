from RandomNumbers.RandomWithSeed import random_with_seed
from RandomNumbers.RandomWithoutSeed import random_without_seed
from RandomNumbers.RandomList_With_Seed import randomlist_with_seed

class RandomNumberGenerator:
    result = 0

    def __init__(self):
        pass

    def random_with_seed(self, a, b, seed):
        self.result = random_with_seed(a, b, seed)
        return self.result

    def random_without_seed(self, a, b):
        self.result = random_without_seed(a, b)
        return self.result

    def randomlist_with_seed(self, a, b, seed, length):
        self.result = randomlist_with_seed(a, b, seed, length)
        return self.result
