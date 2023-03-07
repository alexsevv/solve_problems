from typing import List, Tuple
from collections import Counter


def get_max_points(matrix: List[str], k: int) -> int:
    c = Counter(int(x) for x in matrix if x != ".")
    result = sum(x <= 2 * k for x in c.values())
    return result


def read_input() -> Tuple[List[str], int]:
    k = int(input())
    matrix = [i for i in range(4) for i in input().strip()]
    return matrix, k


def main():
    matrix, k = read_input()
    print(get_max_points(matrix, k))


if __name__ == '__main__':
    main()
