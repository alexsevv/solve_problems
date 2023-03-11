# https://contest.yandex.ru/contest/23389/problems/D/
"""
D. Хаотичность погоды
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.2 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод
или output.txt
C# (MS .Net 5.0)+ASP	0.5 секунд	64Mb
Oracle Java 8	0.5 секунд	64Mb
OpenJDK Java 11	0.5 секунд	64Mb
Kotlin 1.8.0 (JRE 11)	0.6 секунд	64Mb
Метеорологическая служба вашего города решила исследовать погоду новым
способом.

Под температурой воздуха в конкретный день будем понимать максимальную
температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые
температура строго больше, чем в день до (если такой существует) и в день
после текущего (если такой существует). Например, если за 5 дней максимальная
температура воздуха составляла [1, 2, 5, 4, 8] градусов, то хаотичность за
этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот
период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.

Формат ввода
В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105. Во
второй строке даны n целых чисел –— значения температуры в каждый из n дней.
Значения температуры не превосходят 273 по модулю.

Формат вывода
Выведите единственное число — хаотичность за данный период.
"""

from typing import List, Tuple


def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            count += 1
    try:
        if temperatures[1]:
            if temperatures[0] > temperatures[1]:
                count += 1
            if temperatures[-2] < temperatures[-1]:
                count += 1
    except Exception:
        count = 1
    return count


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures


def main():
    n, temperatures = read_input()
    print(get_weather_randomness(temperatures))


if __name__ == '__main__':
    main()
