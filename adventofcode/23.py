from __future__ import annotations

import numpy as np
from rich import inspect, print
from collections import Counter

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def still(A, i, j):
    if np.sum(A[i - 1 : i + 2, j - 1 : j + 2]) - A[i, j] == 0:
        return (0, 0)
    else:
        return None


def north(A, i, j):
    # print("north")
    if np.sum(A[i - 1, j - 1 : j + 2]) == 0:
        return (-1, 0)
    else:
        return None


def south(A, i, j):
    # print("south")
    if np.sum(A[i + 1, j - 1 : j + 2]) == 0:
        return (1, 0)
    else:
        return None


def west(A, i, j):
    # print("west")
    if np.sum(A[i - 1 : i + 2, j - 1]) == 0:
        return (0, -1)
    else:
        return None


def east(A, i, j):
    # print("east")
    if np.sum(A[i - 1 : i + 2, j + 1]) == 0:
        return (0, +1)
    else:
        return None


def find_direction(A, i, j, niteration):
    if direction := still(A, i, j):
        return direction

    operations = [north, south, west, east]
    # print("for ", i, j)
    # print(A[i - 1 : i + 2, j - 1 : j + 2])
    for _ in range(4):
        operation = operations[(_ + niteration) % 4]

        if direction := operation(A, i, j):
            return direction

    return (0, 0)


def parse(riddle_input: str) -> np.ndarray:
    listoflists = []
    for i, line in enumerate(riddle_input.splitlines()):
        listoflists.append([1 if c == "#" else 0 for c in line])

    return np.array(listoflists, dtype=int)


def check_if_unique(x: list[tuple[int, int]]) -> list[bool]:
    c = Counter(x)
    return [c[xi] == 1 for xi in x]


def printmatrix(A):
    print("")
    for i in range(1, A.shape[0] - 1):
        for j in range(1, A.shape[1] - 1):
            if A[i, j] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")


def riddle1(riddle_input: str) -> int | str:
    smallA = parse(riddle_input)
    width = 10
    A = np.zeros((2 * width + smallA.shape[0], 2 * width + smallA.shape[1]), dtype=int)
    A[width:-width, width:-width] = smallA
    n = A.shape[0]
    # printmatrix(A)
    for turn in range(10):
        pairs = []
        nextpairs = []
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if A[i, j] == 1:
                    direction = find_direction(A, i, j, turn)
                    ii = i + direction[0]
                    jj = j + direction[1]
                    pairs.append((i, j))

                    nextpairs.append((ii, jj))
                    # print(f"({i},{j}) ->({ii},{jj})")
        # B = A.copy()
        A *= 0
        # get non unique positions
        is_unique = check_if_unique(nextpairs)
        for i in range(len(is_unique)):
            if is_unique[i]:
                A[nextpairs[i][0], nextpairs[i][1]] = 1
            else:
                A[pairs[i][0], pairs[i][1]] = 1
        # if A == B:
        # print(turn)
        # break
        # print(turn + 1)
        # printmatrix(A)

    mini = 10000
    maxi = 0
    minj = 10000
    maxj = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if A[i, j] == 1:
                mini = min(mini, i)
                maxi = max(maxi, i)
                minj = min(minj, j)
                maxj = max(maxj, j)
    # print((1 + maxi - mini) * (1 + maxj - minj))
    # print(np.sum(A))
    return (1 + maxi - mini) * (1 + maxj - minj) - np.sum(A)


def riddle2(riddle_input: str) -> int | str:
    smallA = parse(riddle_input)
    width = 1000
    A = np.zeros((2 * width + smallA.shape[0], 2 * width + smallA.shape[1]), dtype=int)
    A[width:-width, width:-width] = smallA
    n = A.shape[0]
    # printmatrix(A)
    pairs = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if A[i, j] == 1:
                pairs.append((i, j))

    for turn in range(10000000):
        print(turn)
        nextpairs = []
        for pair in pairs:
            i, j = pair
            direction = find_direction(A, i, j, turn)
            ii = i + direction[0]
            jj = j + direction[1]

            nextpairs.append((ii, jj))
            # print(f"({i},{j}) ->({ii},{jj})")
        B = A.copy()
        A *= 0
        # get non unique positions
        is_unique = check_if_unique(nextpairs)
        updatedpairs = []
        for i in range(len(is_unique)):
            if is_unique[i]:
                ii, jj = nextpairs[i][0], nextpairs[i][1]
            else:
                ii, jj = pairs[i][0], pairs[i][1]
            A[ii, jj] = 1
            updatedpairs.append((ii, jj))
        pairs = updatedpairs

        if np.linalg.norm(A - B) < 1e-5:
            return turn + 1


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    # placeholder for example
    riddle_input = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
.............."""

    answer1 = riddle1(riddle_input)
    print(answer1)

    if answer1 != 0:
        answer2 = riddle2(riddle_input)
        print(answer2)
