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
import matplotlib.pyplot as plt


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


def get_circle_position(num: float):
    """
    Find the coordinates for a number between 0-10 on the circle with radius 1.
    Starting from the positive x-axis going counterclockwise.
    :param num: float | Three digit number between 0 and 10.
    :return: x- and y-coordinates on the circle
    """
    # Convert the number to radians
    max_num = 10.0
    num = num * (2 * np.pi) / max_num
    x, y = np.cos(num), np.sin(num)
    return x, y


if __name__ == '__main__':
    n = 1000
    fib_generator = fibonacci_sequence(n)

    xs, ys = [], []
    for num in fib_generator:
        scaled_num = leading_three_digits(num)
        x,y = get_circle_position(scaled_num)
        xs.append(x)
        ys.append(y)
        #print(f'Number: {num}')
        #print(f'Coords: {x, y}')

    plt.figure()
    # Create circle
    x = np.linspace(0, 2*np.pi, 1000)
    plt.plot(np.cos(x), np.sin(x), linewidth=0.1, c='k')
    plt.plot(xs, ys, linewidth=0.05, c='y')
    plt.title(f'Fibonacci circle with n={n}')
    plt.axis('scaled')  # Equally scaled axes
    plt.show()
