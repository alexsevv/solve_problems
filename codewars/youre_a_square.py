"""
https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
"""


# my solutin
import math


def is_square(n):
    if n < 0:
        return False
    elif math.sqrt(n)**2 == n or n == 0:
        return True
    else:
        return False


# best practices
# import math


# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;


def test_is_squar():
    assert is_square(-1) is False
    assert is_square(0) is True
    assert is_square(3) is False
    assert is_square(4) is True
    assert is_square(25) is True

#dfsff