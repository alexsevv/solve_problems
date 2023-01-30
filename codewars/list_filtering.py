"""
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
"""


# my solutin
def filter_list(l):
    return [i for i in l if type(i) == int]


# best practices
# def filter_list(l):
#   return [i for i in l if not isinstance(i, str)]


def test_solution():
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]
