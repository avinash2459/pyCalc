import random
from random import seed


def randomlist_with_seed(a, b, val, length):
    seed(val)
    result = []
    for i in range(0, length):
        item = random.randint(a, b)
        result.append(item)
    return result
