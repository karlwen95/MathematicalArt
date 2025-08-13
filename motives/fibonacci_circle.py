"""
Motive
    Creating a circle with lines from points determined by fibonacci numbers.
    Take the 3 first digits of each number in the sequence, until the nth position.
    Observe the circle as a line from 0-10 and place the number on the line.
    So, the first number which is 0 would be translated to 0.00.
    Number 2 would be 0.01. Number 8 which is 13 would be 0.13.
    Connecting the adjacent numbers in the sequence will make the pattern emerge.

13/8 2025
@karlwennerstrom
"""

# Imports
import numpy as np
from tqdm import tqdm


# The fibonacci series as a generator
def fibonacci_sequence(n: int):
    """
    Call next() on this function to yield the next value in the sequence
    :param n: int | The lenght of the sequence
    :return:
    """
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b

def leading_three_digits(num: int):
    """
    Convert the 3 first digits in the number to a number between 0-10.
    Numbers < 100 will get leading zeros.
    :param num: int | A number in the fibonacci series
    :return: float
    """
    s_num = str(num)  # strings can be treated as a list
    s_num = s_num[:3].zfill(3)
    f_num = float(s_num) / 100  # Should be between 0-10
    return f_num


if __name__ == '__main__':
    fib_generator = fibonacci_sequence(100)
    for n in fib_generator:
        print(leading_three_digits(n))
