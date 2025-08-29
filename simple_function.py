# lets define some functions that might be used for data transformation
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("The divisor cannot be zero")
    result = a / b
    return result