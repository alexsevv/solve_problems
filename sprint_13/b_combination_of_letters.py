# https://contest.yandex.ru/contest/24734/problems/B/
"""
B. Комбинации
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.

Пример 1
Ввод	
23
Вывод
ad ae af bd be bf cd ce cf
"""

LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def keyboard(buttons, path, result):
    if buttons == '':
        result.append(path)
        return
    for letter in LETTERS[buttons[0]]:
        path += letter
        keyboard(buttons[1:], path, result)
        path = path[:-1]


def read_input() -> str:
    buttons = input()
    return buttons


def main():
    buttons = read_input()
    result = []
    keyboard(buttons, '', result)
    for x in result:
        print(x, end=' ')


if __name__ == '__main__':
    main()