"""
https://www.codewars.com/kata/5583090cbe83f4fd8c000051
"""


# my solutin
def digitize(n):
    x = [int(a) for a in str(n)]
    return x[::-1]


# # best practices
# def digitize(n):
#     return map(int, str(n)[::-1])

def test_solution():
    assert digitize(35231) == [1, 3, 2, 5, 3]
    assert digitize(0) == [0]
    assert digitize(23582357) == [7, 5, 3, 2, 8, 5, 3, 2]
    assert digitize(984764738) == [8, 3, 7, 4, 6, 7, 4, 8, 9]
