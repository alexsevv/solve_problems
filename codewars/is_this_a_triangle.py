"""
https://www.codewars.com/kata/56606694ec01347ce800001b/solutions/python
"""


# my solutin
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# best practices
# def is_triangle(a, b, c):
#     return (a<b+c) and (b<a+c) and (c<a+b)


def test_solution():
    assert is_triangle(1, 2, 5) is False
    assert is_triangle(2, 5, 1) is False
    assert is_triangle(4, 2, 3) is True
    assert is_triangle(5, 1, 5) is True
    assert is_triangle(2, 2, 2) is True
    assert is_triangle(-1, 2, 3) is False
    assert is_triangle(1, -2, 3) is False
