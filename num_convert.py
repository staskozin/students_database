def to_int(value):
    try:
        return int(value)
    except ValueError:
        return 0


def to_float(value):
    try:
        return float(value)
    except ValueError:
        return 0
