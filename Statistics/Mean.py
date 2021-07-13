from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    try:
        data_length = len(data)
        total = 0
        for val in data:
            total = addition(total, val)
        return round(division(data_length, total), 3)
    except ZeroDivisionError:
        print("Error: Cannot divide a number by Zero")
    except ValueError:
        print("Error: Check input values")
