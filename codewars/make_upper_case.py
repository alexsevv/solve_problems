"""
https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7
"""


# my solutin
def make_upper_case(s):
    return s.upper()


# best practices
# def make_upper_case(s):
#     return s.upper()


def test_solution():
    assert make_upper_case("hello") == "HELLO"
    assert make_upper_case("trolololo") == "TROLOLOLO"
