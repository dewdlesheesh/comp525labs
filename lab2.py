import math
import random

"""
***************************************************
Code collaborated from s-gomezriv/comp525 homework
NOT originally written by me
From 2/14/18
"""


def circle_area(radius):
    """
    Calculates the area of a circle with given radius.
    radius: non-negative float
    Returns: float

    >>> circle_area(1)
    3.141592653589793
    >>> circle_area(10*10)
    31415.926535897932
    """
    area = math.pi*(radius**2)
    return area
def is_even(number):
    """
    Checks if number is even
    number: integer
    Returns: True if number is even, False otherwise

    >>> is_even(2)
    True
    >>> is_even(5)
    False
    """
    remander = number%2
    if remander == 0:
        return True
    else:
        return False


def sum_of_odd_to(n):
    """
    Calculates the sum of all odd numbers
    from 1 to given n
    n: positive integer
    Returns: integer
    """
    odd_sum = 0
    for odd in range(1,n+1,2):

        odd_sum += odd
    return odd_sum
def miles_per_gallon(miles, gallons):
    """
    Calculates miles per gallons
    miles: positive float
    gallons: positive float
    """
    if (gallons > 0):
        mpg = miles/gallons
        return mpg
def ten_random_numbers(start, stop):
    """
    Prints ten random integers between start and stop
    """
    if start <= stop:
        for i in range(10):

            random_int = random.randint(start,stop)
            print(random_int)
def average_random_1_to_10(n):
    """
    Calculates the average of random numbers
    between 1 and 10  generated n times
    n: positive integer - how many times random numbers
         are generated
    Returns: integer
    """

    sum_randint = 0

    if (n > 0) and type(n) == int:
        for i in range(n):
            random_int = random.randint(1,10)
            sum_randint += random_int
        sum_randint /= n
    return sum_randint


if __name__ == '__main__':
    import doctest
    doctest.testmod( )
