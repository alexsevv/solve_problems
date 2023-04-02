# https://contest.yandex.ru/contest/24734/problems/N/
"""
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме земельного участка клумбы обозначаются просто горизонтальными отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято n садовников. Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был организован не очень хорошо, иногда один и тот же отрезок или его часть могли быть обработаны сразу несколькими садовниками. Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один. Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб.
Рассмотрим примеры.
Пример 1:
Даны 4 отрезка: 
[
7
,
8
]
, 
[
7
,
8
]
 ,
[
2
,
3
]
, 
[
6
,
1
0
]
. Два одинаковых отрезка 
[
7
,
8
]
 и 
[
7
,
8
]
 сливаются в один, но потом их накрывает отрезок 
[
6
,
1
0
]
. Таким образом, имеем две клумбы с координатами 
[
2
,
3
]
 и 
[
6
,
1
0
]
.
Пример 2
Во втором сэмпле опять 4 отрезка: 
[
2
,
3
]
, 
[
3
,
4
]
, 
[
3
,
4
]
, 
[
5
,
6
]
. Отрезки 
[
2
,
3
]
, 
[
3
,
4
]
 и 
[
3
,
4
]
 сольются в один отрезок 
[
2
,
4
]
. Отрезок 
[
5
,
6
]
 ни с кем не объединяется, добавляем его в ответ.

Формат ввода
В первой строке задано количество садовников 
n
. Число садовников не превосходит 
1
0
0
0
0
0
.
В следующих 
n
 строках через пробел записаны координаты клумб в формате: start end, где start —– координата начала, end —– координата конца. Оба числа целые, неотрицательные и не превосходят 
1
0
7
. start строго меньше, чем end.

Формат вывода
Нужно вывести координаты каждой из получившихся клумб в отдельных строках. Данные должны выводиться в отсортированном порядке —– сначала клумбы с меньшими координатами, затем —– с бОльшими.
Пример 1
Ввод	
4
7 8
7 8
2 3
6 10
Вывод
2 3
6 10
"""

from typing import Tuple, List


def flowerbed(gardeners, coordinates):
    coordinates.sort()
    result = []
    i = 0
    start, end = coordinates[i]
    while i < gardeners:
        if start <= coordinates[i][0] <= end:
            _, curr_end = coordinates[i]
            i += 1
            if curr_end > end:
                end = curr_end
        else:
            result.append([start, end])
            start, end = coordinates[i]
            i += 1
    result.append([start, end])

    for res in result:
        print(*res)


def read_input() -> Tuple[int, List[List[int]]]:
    gardeners = int(input())
    coordinates = [list(map(int, input().split())) for _ in range(gardeners)]
    return gardeners, coordinates


def main():
    gardeners, coordinates = read_input()
    flowerbed(gardeners, coordinates)


if __name__ == '__main__':
    main()