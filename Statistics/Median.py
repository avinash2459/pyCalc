from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Addition import addition
from pprint import pprint


def median(data):
    try:
        data_length = len(data)
        data.sort()
        if data_length % 2 == 0:
            index1 = subtraction(division(data_length, 2), 1)
            index2 = subtraction(division(data_length, 2), 2)

            total = addition(data[index1], data[index2])

            median_result = float(division(total, 2))

            return median_result
        else:
            index = int(division(data_length, 2))
            median_result = data[index]

        return median_result
    except ZeroDivisionError:
        print("Error: Cannot divide a number by Zero")
    except ValueError:
        print("Error: Check input values")
