import pytest

from simple_function import divide_numbers


def test_divide_numbers_positive():

    assert divide_numbers(10, 2) == 5

    assert divide_numbers(9, 3) == 3


def test_divide_numbers_negative():

    assert divide_numbers(-10, 2) == -5

    assert divide_numbers(10, -2) == -5


def test_divide_numbers_zero_divisor():

    with pytest.raises(ZeroDivisionError, match="The divisor cannot be zero"):

        divide_numbers(10, 0)

    with pytest.raises(ZeroDivisionError, match="The divisor cannot be zero"):

        divide_numbers(0, 0)

        

# Define a fixture that provides a list of numbers

@pytest.fixture

def generate_number_pairs():

    return [(i, j) for i in range(-10, 10) for j in range(-10, 10)]


def test_generated_numbers(generate_number_pairs):

    for pair in generate_number_pairs:

        if pair[1] == 0:

            with pytest.raises(ZeroDivisionError, match="The divisor cannot be zero"):

                divide_numbers(pair[0], pair[1])

        else:

            result = divide_numbers(pair[0], pair[1])

            assert result == pair[0] / pair[1]