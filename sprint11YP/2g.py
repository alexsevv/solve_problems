# https://contest.yandex.ru/contest/23389/problems/G/
"""
G. Работа из дома
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вася реализовал функцию, которая переводит целое число из десятичной системы в
двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу чисел в бинарное
представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.
"""


def to_binary(number: int) -> str:
    numberbinary = ''
    if number == 0:
        return number
    else:
        while number > 0:
            numberbinary = str(number % 2) + numberbinary
            number = number // 2

        return numberbinary


def read_input() -> int:
    return int(input().strip())


def main():
    print(to_binary(read_input()))


if __name__ == '__main__':
    main()
