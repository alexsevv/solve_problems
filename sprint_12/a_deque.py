# номер успешной посылки 84186973, После рефакторинга: 84333195. P.s: почемуто я не проходил по времени из-за вывода ошибки в raize. 
# https://contest.yandex.ru/contest/23759/problems/A/
"""
Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x),
pop_back(), pop_front() работали корректно. Но, если в деке было
много элементов, программа работала очень долго. Дело в том, что
не все операции выполнялись за O(1). Помогите Гоше! Напишите
эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
100000. Во второй строке записано число m — максимальный размер дека. Он не
превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится
максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится
максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то
вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст,
то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных
запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1

Ввод
4
4
push_front
push_front
pop_back
pop_back

Вывод
861
-819
"""


class NoItemsException(Exception):
    def __init__(self):
        pass


class MaxItemsException(Exception):
    def __init__(self):
        pass


class Deque:
    def __init__(self, max_size):
        self._array = [None] * max_size
        self._max_size = max_size
        self._size = 0
        self._head = 0
        self._tail = -1

    @property
    def is_full(self):
        return self._size == self._max_size

    @property
    def is_empty(self):
        return self._size == 0

    def push_back(self, value):
        if self.is_full:
            raise MaxItemsException("Дек переполнен")

        self._tail = (self._tail + 1) % self._max_size
        self._array[self._tail] = value
        self._size += 1

    def push_front(self, value):
        if self.is_full:
            raise MaxItemsException("Дек переполнен")

        self._head = (self._head - 1) % self._max_size
        self._array[self._head] = value
        self._size += 1

    def pop_back(self):
        if self.is_empty:
            raise NoItemsException("Дек пуст")

        value = self._array[self._tail]
        self._tail = (self._tail - 1) % self._max_size
        self._size -= 1
        return value

    def pop_front(self):
        if self.is_empty:
            raise NoItemsException("Дек пуст")

        value = self._array[self._head]
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return value


def main():
    commands_count, max_size = int(input()), int(input())
    deque = Deque(max_size)

    for _ in range(commands_count):
        try:
            item = input().split(' ')
            if len(item) == 1:
                print(getattr(deque, item[0])())
            else:
                getattr(deque, item[0])(item[1])
        except (NoItemsException, MaxItemsException):
            print('error')


if __name__ == '__main__':
    main()
