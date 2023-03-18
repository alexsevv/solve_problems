# https://contest.yandex.ru/contest/23758/problems/I/
"""
Астрологи объявили день очередей ограниченного размера. Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size, означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.

Пример 1
Ввод	
8
2
peek
push 5
push 2
peek
size
size
push 1
size

Вывод
None
5
2
2
error
2
"""


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


def main():
    n = int(input())
    max_size = int(input())

    stack = MyQueueSized(max_size)
    result = []

    for i in range(n):
        item = input().split()
        if item[0] == 'push':
            if stack.push(int(item[1])) == 'error':
                result.append('error')
        elif item[0] == 'pop':
            result.append(stack.pop())
        elif item[0] == 'peek':
            result.append(stack.peek())
        elif item[0] == 'size':
            result.append(stack.size)

    for i in result:
        print(i)


if __name__ == '__main__':
    main()
