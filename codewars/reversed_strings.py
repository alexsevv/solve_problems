"""
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
"""


# my solutin
def solution(string):
    return string[::-1]


# # best practices
# def solution(str):
#     return str[::-1]

def test_solution():
    assert solution('world') == 'dlrow'
    assert solution('hello') == 'olleh'
    assert solution('') == ''
    assert solution('h') == 'h'
