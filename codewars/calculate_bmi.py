"""
https://www.codewars.com/kata/57a429e253ba3381850000fb
"""


# my solutin
def bmi(weight, height):
    result = weight / height ** 2
    if result <= 18.5:
        return "Underweight"
    elif result <= 25.0:
        return "Normal"
    elif result <= 30.0:
        return "Overweight"
    else:
        return "Obese"


# # best practices
# def bmi(weight, height):
#     bmi = weight / height ** 2
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi <= 25:
#         return "Normal"
#     elif bmi <= 30:
#         return "Overweight"
#     else:
#         return "Obese"

def test_solution():
    assert bmi(50, 1.80) == "Underweight"
    assert bmi(80, 1.80) == "Normal"
    assert bmi(90, 1.80) == "Overweight"
    assert bmi(110, 1.80) == "Obese"
    assert bmi(50, 1.50) == "Normal"
