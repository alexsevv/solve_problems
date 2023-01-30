"""
https://www.codewars.com/kata/576bb71bbbcf0951d5000044
"""


# my solutin
def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]),
            sum([i for i in arr if i < 0])] if len(arr) != 0 else []


# best practices
# def count_positives_sum_negatives(arr):
#     if not arr: return []
#     pos = 0
#     neg = 0
#     for x in arr:
#       if x > 0:
#           pos += 1
#       if x < 0:
#           neg += x
#     return [pos, neg]


def test_solution():
    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
    assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
    assert count_positives_sum_negatives([1]) == [1, 0]
    assert count_positives_sum_negatives([-1]) == [0, -1]
    assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
    assert count_positives_sum_negatives([]) == []
