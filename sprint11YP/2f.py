# https://contest.yandex.ru/contest/23389/problems/F/
"""
F. Палиндром
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Помогите Васе понять, будет ли фраза палиндромом‎. Учитываются только буквы и
цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только
латинские. Длина текста не превосходит 20000 символов.

Фраза может состоять из строчных и прописных латинских букв, цифр, знаков
препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.
"""


def is_palindrome(line: str) -> bool:
    new_line = ''.join(e for e in line if e.isalnum()).lower()
    return new_line == new_line[::-1]


def main():
    print(is_palindrome(input().strip()))


if __name__ == '__main__':
    main()
