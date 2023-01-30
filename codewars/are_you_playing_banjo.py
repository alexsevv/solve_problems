"""
https://www.codewars.com/kata/53af2b8861023f1d88000832
"""


# my solutin
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# # best practices
# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'


def test_solution():
    assert are_you_playing_banjo("martin") == "martin does not play banjo"
    assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
    assert are_you_playing_banjo("bravo") == "bravo does not play banjo"
    assert are_you_playing_banjo("rolf") == "rolf plays banjo"
