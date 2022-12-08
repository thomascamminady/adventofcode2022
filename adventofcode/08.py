import numpy as np
from rich import print

from adventofcode.helper.io import (
    get_day,
    get_riddle_input,
    save_riddle_input,
    submit_answer,
)


def to_matrix(riddle_input: str) -> np.ndarray:
    return np.array(
        [[int(_) for _ in line] for line in riddle_input.splitlines()], dtype=int
    )


def riddle1(riddle_input: str) -> int | str:

    A = to_matrix(riddle_input)
    possibly_invisible = np.ones(A.shape, dtype=bool)

    n = A.shape[0]
    for i in range(n):
        current_max = -1
        for j in range(n):
            if A[i, j] > current_max:
                current_max = A[i, j]
                possibly_invisible[i, j] = False

        current_max = -1
        for j in range(n):
            if A[i, n - 1 - j] > current_max:
                current_max = A[i, n - 1 - j]
                possibly_invisible[i, n - 1 - j] = False

    for j in range(n):
        current_max = -1
        for i in range(n):
            if A[i, j] > current_max:
                current_max = A[i, j]
                possibly_invisible[i, j] = False

        current_max = -1
        for i in range(n):
            if A[n - 1 - i, j] > current_max:
                current_max = A[n - 1 - i, j]
                possibly_invisible[n - 1 - i, j] = False
    hidden = np.sum(possibly_invisible[1:-1, 1:-1])

    return n**2 - hidden


def riddle2(riddle_input: str) -> int | str:
    A = to_matrix(riddle_input)
    score = np.zeros_like(A)
    for i in range(1, A.shape[0] - 1):
        for j in range(1, A.shape[1] - 1):
            h = A[i, j]
            north, south, east, west = 0, 0, 0, 0
            # go north until we find a tree of the same hight
            for k in range(i - 1, -1, -1):
                north += 1
                if A[k, j] >= h:
                    break
            # go south until we find a tree of the same hight
            for k in range(i + 1, A.shape[0]):
                south += 1
                if A[k, j] >= h:
                    break
            # go west until we find a tree of the same hight
            for k in range(j - 1, -1, -1):
                west += 1
                if A[i, k] >= h:
                    break
            # go east until we find a tree of the same hight
            for k in range(j + 1, A.shape[1]):
                east += 1
                if A[i, k] >= h:
                    break
            score[i, j] = south * north * east * west
    return np.max(score)


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    answer1 = riddle1(riddle_input)
    submit_answer(day, 1, answer1)

    if answer1 != 0:
        answer2 = riddle2(riddle_input)
        submit_answer(day, 2, answer2)
