from Statistics.Mean import mean
from Calculator.Square import squaring


def variance(data):
    mean_value = mean(data)
    data1 = []
    for item in data:
        item1 = squaring(item-mean_value)
        data1.append(item1)

    return mean(data1)

