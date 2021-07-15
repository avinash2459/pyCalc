from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance


def standard_deviation(data):
    variance_val = variance(data)
    return round(squarerooting(variance_val), 1)

