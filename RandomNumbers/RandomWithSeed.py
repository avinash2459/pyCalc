import random
from random import seed


def random_with_seed(a, b, val):
    seed(val)
    result = random.randint(a, b)
    return result
