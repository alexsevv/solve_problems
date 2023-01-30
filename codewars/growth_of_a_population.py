"""
https://www.codewars.com/kata/563b662a59afc2b5120000c6
"""


# my solutin
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += (int(p0 * (percent/100)) + aug)
        years += 1
    return years


# best practices
# def nb_year(p0, percent, aug, p, years = 0):
#     if p0 < p:
#         return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#     return years


def test_solution():
    assert nb_year(1500, 5, 100, 5000) == 15
    assert nb_year(1500000, 2.5, 10000, 2000000) == 10
    assert nb_year(1500000, 0.25, 1000, 2000000) == 94

