# https://contest.yandex.ru/contest/26207/problems/E/
"""
E. Дерево поиска
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гоша понял, что такое дерево поиска, и захотел написать функцию, которая определяет, является ли заданное дерево деревом поиска. Значения в левом поддереве должны быть строго меньше, в правом —- строго больше значения в узле.
Помогите Гоше с реализацией этого алгоритма.
PIC

Формат ввода
На вход функции подается корень бинарного дерева.
Замечания про отправку решений
По умолчанию выбран компилятор make. Решение нужно отправлять в виде файла с расширением, которое соответствует вашему языку программирования. Если вы пишете на Java, имя файла должно быть Solution.java, для C# – Solution.cs. Для остальных языков назовите файл my_solution.ext, заменив ext на необходимое расширение.
Используйте заготовки кода для данной задачи, расположенные по ссылкам:

c++
Java
js
Python
C#
go
Формат вывода
Функция должна вернуть True, если дерево является деревом поиска, иначе - False.

"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.value > max_l) and
                   (min_r is None or node.value < min_r))

    min_value = min([x for x in [min_l, node.value, min_r] if x is not None])
    max_value = max([x for x in [max_l, node.value, max_r] if x is not None])

    return is_bst_node, min_value, max_value


def solution(root) -> bool:
    return is_bst(root)[0]


def test():
    root1 = Node(1, None, None)
    root2 = Node(4, None, None)
    root3 = Node(3, root1, root2)
    root4 = Node(8, None, None)
    root5 = Node(5, root3, root4)

    assert solution(root5)
    root2.value = 5
    assert not solution(root5)


if __name__ == "__main__":
    test()