"""
https://www.codewars.com/kata/50654ddff44f800200000004/train/python
"""


# my solutin
def multiply(a, b):
    return a * b

# best practices
# def multiply(a, b):
#     return a * b


def test_multiply():
    assert multiply(2, 1) == 2
    assert multiply(-1, 1) == -1
    assert multiply(0, 1) == 0
