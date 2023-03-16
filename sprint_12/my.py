from math import sqrt


a, b, c = float(input()), float(input()), float(input())

d = (b ** 2) - (4 * a * c)

sol1 = (-b-sqrt(d))/(2*a)
sol2 = (-b+sqrt(d))/(2*a)
if abs(sol2) == abs(sol1):
    print(sol2)
else:
    print(sol1)
    print(sol2)
