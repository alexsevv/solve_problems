"""
https://www.codewars.com/kata/56269eb78ad2e4ced1000013
"""


# my solutin
def find_next_square(sq):
    if (sq**0.5) % 1:
        return -1
    else:
        return int(((sq**0.5)+1)**2)


# best practices
# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer():
#         return (root + 1)**2
#     return -1


def test_solution():
    assert find_next_square(121) == 144
    assert find_next_square(625) == 676
    assert find_next_square(319225) == 320356
    assert find_next_square(15241383936) == 15241630849
    assert find_next_square(155) == -1
    assert find_next_square(342786627) == -1
