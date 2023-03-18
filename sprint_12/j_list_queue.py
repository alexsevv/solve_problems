# https://contest.yandex.ru/contest/23758/problems/J/
"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка. Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.

Пример 1
Ввод	
10
put -34
put -23
get
size
get
size
get
get
put 80
size
Вывод
-34
1
-23
0
error
error
1
"""


class ListQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.size() == 0

    def get(self):
        if self.is_empty():
            return 'error'
        else:
            return self.queue.pop(0)

    def put(self, item):
        self.queue.append(item)
        return self.queue[-1]

    def size(self):
        return len(self.queue)


def main():
    n = int(input())

    stack = ListQueue()
    result = []

    for i in range(n):
        item = input().split()
        if item[0] == 'get':
            result.append(stack.get())
        elif item[0] == 'size':
            result.append(stack.size())
        elif item[0] == 'put':
            stack.put(int(item[1]))

    for i in result:
        print(i)


if __name__ == '__main__':
    main()