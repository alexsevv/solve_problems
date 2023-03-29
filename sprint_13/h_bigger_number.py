# https://contest.yandex.ru/contest/24734/problems/H/
"""
H. Большое число
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.055 секунд	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	0.5 секунд	64Mb
Python 3.7.3	0.5 секунд	64Mb
C# (MS .Net 5.0)+ASP	0.5 секунд	64Mb
Oracle Java 8	0.5 секунд	64Mb
OpenJDK Java 11	0.5 секунд	64Mb
Node JS 8.16	0.3 секунды	64Mb
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.

Пример 1
Ввод	
3
15 56 2
Вывод
56215
"""

from typing import List


def comparator(number_1, number_2):
    if len(number_1) == len(number_2):
        return number_1 > number_2
    else:
        sum_1 = number_1 + number_2
        sum_2 = number_2 + number_1
        return sum_1 > sum_2


def bigger_number(numbers, comparator):
    for i in range(len(numbers)):
        item = numbers[i]
        while i > 0 and comparator(item, numbers[i - 1]):
            numbers[i] = numbers[i - 1]
            i -= 1
        numbers[i] = item
    return numbers


def read_input() -> List:
    _ = int(input())
    numbers = [x for x in input().split()]
    return numbers


def main():
    numbers = read_input()
    print(''.join(bigger_number(numbers, comparator)))


if __name__ == '__main__':
    main()