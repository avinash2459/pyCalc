def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(b) - int(a)


def multiplication(a, b):
    return int(a) * int(b)


def division(a, b):
    return round((int(b) / int(a)), 9)


def square2(a):
    return int(a) ** 2


def squareroot2(a):
    return round((int(a) ** 0.5), 8)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square2(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot2(a)
        return self.result
