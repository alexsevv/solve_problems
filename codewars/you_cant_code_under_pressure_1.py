"""
https://www.codewars.com/kata/53ee5429ba190077850011d4
"""


# my solutin
def double_integer(i):
    return i*2


# # best practices
# def doubleInteger(i):
#     return i * 2


def test_solution():
    assert double_integer(2) == 4
    assert double_integer(4) == 8
    assert double_integer(-10) == -20
    assert double_integer(0) == 0
    assert double_integer(100) == 200
