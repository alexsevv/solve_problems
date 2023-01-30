"""
https://www.codewars.com/kata/55d24f55d7dd296eb9000030
"""


# my solutin
def summation(num):
    nums = [n for n in range(0, num+1)]
    return sum(nums)


# best practices
# def summation(num):
#     return sum(xrange(num + 1))


def test_solution():
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791
