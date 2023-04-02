# https://contest.yandex.ru/contest/24734/problems/K/
"""
Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше обязательно надо реализовать отдельно функцию merge и функцию merge_sort.
Функция merge принимает два отсортированных массива, сливает их в один отсортированный массив и возвращает его. Если требуемая сигнатура имеет вид merge(array, left, mid, right), то первый массив задаётся полуинтервалом 
[
l
e
f
t
,
m
i
d
)
 массива array, а второй – полуинтервалом 
[
m
i
d
,
r
i
g
h
t
)
 массива array.
Функция merge_sort принимает некоторый подмассив, который нужно отсортировать. Подмассив задаётся полуинтервалом — его началом и концом. Функция должна отсортировать передаваемый в неё подмассив, она ничего не возвращает.
Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно вызывает сортировку отдельно для каждой. Затем два отсортированных массива сливаются в один с помощью merge.
Заметьте, что в функции передаются именно полуинтервалы 
[
b
e
g
i
n
,
e
n
d
)
, то есть правый конец не включается. Например, если вызвать merge_sort(arr, 0, 4), где 
a
r
r
=
[
4
,
5
,
3
,
0
,
1
,
2
]
, то будут отсортированы только первые четыре элемента, изменённый массив будет выглядеть как 
a
r
r
=
[
0
,
3
,
4
,
5
,
1
,
2
]
.
Реализуйте эти две функции.
Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по ссылке.

Формат ввода
Передаваемый в функции массив состоит из целых чисел, не превосходящих по модулю 
1
0
9
. Длина сортируемого диапазона не превосходит 
1
0
5
.
Формат вывода
При написании и отправке решений соблюдайте следующие правила:
Отправляйте решение в виде файла. Если текст решения будет вставлен в форму, то будет возвращена ошибка.
В качестве компилятора выберите  Make.
На Java назовите файл с решением Solution.java и реализуйте внутри класса указанные функции, для C# – Solution.cs
Для остальных решений не используйте в качестве имени файла слово solution
Укажите правильное разрешение для файла (.cpp, .java, .go. .js, .py). Для решений на C++ разрешение .h не поддерживается.
Ниже приведены сигнатуры функций, которые необходимо реализовать, для различных языков программирования.
C++
using Iterator = std::vector<int>::iterator; 
using CIterator = std::vector<int>::const_iterator; 
std::vector<int> merge(CIterator left_begin, CIterator left_end, 
                       CIterator right_begin, CIterator right_end); 
void merge_sort(Iterator begin, Iterator end);
Java

public class Solution { 
        public static int[] merge(int[] arr, int left, int mid, int right); 
        public static void merge_sort(int[] arr, int left, int right); 
}
Python

merge(arr: list, left: int, mid: int, right: int) -> array 
merge_sort(arr: list, left: int, right: int) -> None
Go

package main 
func merge(arr []int, lf int, mid int, rg int) []int 
func merge_sort(arr []int, lf int, rg int)
JavaScript

merge :: (Array arr, Number lf, Number mid, Number rg) -> Array 
merge_sort :: (Array arr, Number lf, Number rg) -> void
"""


def merge_sorting(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sorting(lefthalf)
        merge_sorting(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


n = int(input())
alist = list(map(int, input().split()))[:n]
merge_sorting(alist)
print(*alist)
