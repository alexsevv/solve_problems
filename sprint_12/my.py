

# Стек - работа с первый элементом
# push(item) — добавляет элемент на вершину стека;
# pop() — возвращает элемент с вершины стека и удаляет его;
# size() — возвращает размер стека (количество лежащих в нём элементов).
# Иногда стек реализует дополнительные операции: 
# peek() или top() — возвращает элемент с вершины стека, не удаляя его;
# isEmpty() — определяет, пуст ли стек.


# # Дек - работает с первым и послденим элементом. (англ. deque — double ended queue, «очередь с двумя концами»)
# push_back(item) — вставка нового элемента в конец;
# pop_back() — удаление последнего элемента;
# push_front(item) — вставка нового элемента в начало;
# pop_front() — удаление первого элемента;
# size() — количество элементов в очереди.


# Очередь - работа с первым элементом
# push(item) — добавляет элемент в конец очереди;
# pop() — берёт элемент из начала очереди и удаляет его;
# peek() — берёт элемент из начала очереди без удаления;
# size() — возвращает количество элементов в очереди.
class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
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
    
    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


q = Queue(8) 
q.push(1)
print(q.queue)  # [1, None, None, None, None, None, None, None]
print(q.size)   # 1
q.push(-1)
q.push(0)
q.push(11)
q.push("11")
q.push("12")
q.push("13")
q.push("14")
q.pop()
print(q.queue)  # [1, -1, 0, 11, None, None, None, None]
print(q.size)