# https://contest.yandex.ru/contest/24734/problems/G/
"""
Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового. После того как вещи других расцветок были убраны, Рита захотела отсортировать свой новый гардероб по цветам. Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового. Помогите Рите справиться с этой задачей.

Примечание: попробуйте решить задачу за один проход по массиву!

Формат ввода
В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000. Во второй строке даётся массив, в котором указан цвет для каждого предмета. Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.

Формат вывода
Нужно вывести в строку через пробел цвета предметов в правильном порядке.

Пример 1
Ввод	
7
Вывод
0 2 1 2 0 0 1
0 0 0 1 1 2 2
"""
from typing import List


# def counting_sort(color, n=3):
#     if len(color) == 0:
#         print(*color)
#     counted_values = [0] * n
#     counted_values[0] = color.count(0)
#     counted_values[1] = color.count(1)
#     counted_values[2] = color.count(2)
#     i = 0
#     for value in range(n):
#         for _ in range(0, counted_values[value]):
#             color[i] = value
#             i += 1
#     print(*color)


def read_input() -> List:
    n = int(input())
    color = list(map(int, input().split()))
    return color


def main():
    color = read_input()
    # counting_sort(color)
    print(*sorted(color))


if __name__ == '__main__':
    main()

