from collections import Counter


def mode(data):
    try:
        data_length = len(data)
        data.sort()
        data = Counter(data)
        get_mode = dict(data)
        mode1 = [k for k, v in get_mode.items() if v == max(list(data.values()))]

        if len(mode1) == data_length:
            get_mode = "No mode found"
        else:
            get_mode = mode1

        return get_mode
    except ZeroDivisionError:
        print("Error: Cannot divide a number by Zero")
    except ValueError:
        print("Error: Check input values")
