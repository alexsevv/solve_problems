# n = list(map(int, input().strip().split()))    # n = [int(i) for i in input().split()]
# numbers = [int(input()) for _ in range(int(input()))]
# numbers = [i + j for i in ['a', 'b'] for j in ['z', 'h', 'q']]
# объявление функции
# объявление функции

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
#     print()
#  Результатом работы такого кода будет:

# 1 4 7 
# 2 5 8 
# 3 6 9




# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()
#  Результатом работы такого кода будет:

# 1 2 3 
# 4 5 6 
# 7 8 9





# # Ввод пользователя
# n = int(input())
# # Создание матрицы
# matrix = [input().split() for i in range(n)]
# # Вывод суммы главной диагонали
# print(sum([int(matrix[i][i]) for i in range(n)]))

# res = 0
# n = int(input())
# for i in range(n):
#     res += int(input().split()[i])
# print(res)


# Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# or
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)



# import re

# text = re.sub(r'[.,;:-?-!]', '', input().lower())


# sequence1 = [set(input()) for _ in range(int(input()))]

# student1 = set(int(i) for i in input().split())
# student2 = set(int(i) for i in input().split())
# student3 = set(int(i) for i in input().split())
# print(*sorted((student1 & student2) - student3, reverse=True))



nk = [int(i) for i in input().split()]
coun_v = 0
coun_p = 0
seq = [int(i) for i in input().split()]

for i in seq:
    if i % 5 == 0 and i % 3 != 0:
        coun_v += 1
        if coun_v >= nk[0]:
            break
    if i % 3 == 0 and i % 5 != 0:
        coun_p += 1
        if coun_p >= nk[0]:
            break
if coun_p < coun_v:
    print("Vasya")
else:
    print("Petya")