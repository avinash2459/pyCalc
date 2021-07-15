from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance


def standard_deviation(data):
    try:
        variance_val = variance(data)
        return round(squarerooting(variance_val), 1)
    except ZeroDivisionError:
        print("Error: Cannot divide a number by Zero")
    except ValueError:
        print("Error: Check input values")
