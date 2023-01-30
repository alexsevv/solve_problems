"""
https://www.codewars.com/kata/554b4ac871d6813a03000035
"""


# my solutin
def high_and_low(numbers):
    mynumbers = []
    allnumbers = numbers.split(" ")
    allnumbersint = list(map(int, allnumbers))
    mynumbers.append(max(allnumbersint))
    mynumbers.append(min(allnumbersint))
    return " ".join(map(str, mynumbers))


# best practices
# def high_and_low(numbers): #z.
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))


def test_solution():
    assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
    assert high_and_low("1 2 3") == "3 1"
