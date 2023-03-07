from typing import List, Tuple


def zero_dists(start, sequence):
    d = start
    for n in sequence:
        if n == '0':
            d = 0
        else:
            d += 1
        yield d


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    numbers = input().split()
    return numbers, n


def main():
    numbers, n = read_input()
    to_left = zero_dists(n, numbers)
    to_right = reversed(tuple(zero_dists(n, reversed(numbers))))
    result = map(min, zip(to_left, to_right))
    print(*result)


if __name__ == '__main__':
    main()