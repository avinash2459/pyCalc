from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance


def standard_deviation(data):
    variance_value = variance(data)
    return round(squarerooting(variance_value), 1)

