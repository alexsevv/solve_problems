a = (i for i in range(10))
b = [i for i in range(10)]
c = {i for i in range(10)}
d = {x: x**2 for x in range(10)}
r = range(10)

print(type(a))  # <class 'generator'>
print(type(b))  # <class 'list'>
print(type(c))  # <class 'set'>
print(type(d))  # <class 'dict'>
print(type(r))  # <class 'range'>

print("-"*50)
print(a)  # <generator object <genexpr> at 0x7f930768aa50>
print(b)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(c)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(d)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(r)  # range(0, 10)
print("-"*50)
print(*a)  # 0 1 2 3 4 5 6 7 8 9
print(*r)  # 0 1 2 3 4 5 6 7 8 9