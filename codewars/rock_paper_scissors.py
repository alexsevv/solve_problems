"""
https://www.codewars.com/kata/5672a98bdbdd995fad00000f
"""


# my solutin
def rps(p1, p2):
    sc = "scissors"
    pa = "paper"
    ro = "rock"
    if p1 == sc and p2 == pa or p1 == pa and p2 == ro or p1 == ro and p2 == sc:
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    else:
        return "Player 2 won!"


# # best practices
# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"


def test_solution():
    assert rps('rock', 'scissors') == "Player 1 won!"
    assert rps('scissors', 'rock') == "Player 2 won!"
    assert rps('rock', 'rock') == 'Draw!'
