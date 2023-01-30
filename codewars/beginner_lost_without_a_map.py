"""
https://www.codewars.com/kata/57f781872e3d8ca2a000007e/solutions/python
"""


# my solutin
def maps(a):
    result = [i + i for i in a]
    return result


# # best practices
# def maps(a):
#     return [2 * x for x in a]

def test_solution():
    assert maps([1, 2, 3]) == [2, 4, 6]
    assert maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert maps([]) == []
