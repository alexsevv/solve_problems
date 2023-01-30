"""
https://www.codewars.com/kata/55f2b110f61eb01779000053
"""


# my solutin
def get_sum(a, b):
    if a == b:
        return a
    else:
        collection = [a, b]
        return sum([n for n in range(min(collection), max(collection)+1)])


# best practices
# def get_sum(a,b):
#     return sum(range(min(a, b), max(a, b) + 1))


def test_solution():
    assert get_sum(0, 1) == 1
    assert get_sum(0, -1) == -1
