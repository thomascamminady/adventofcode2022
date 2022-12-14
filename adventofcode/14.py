from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def get_matrix(riddle_input: str) -> tuple[np.ndarray, int]:
    n = 1000
    A = np.zeros((n, n), dtype=int)
    A[0, 499] = 1
    maxi, maxj = 0, 0
    mini, minj = 0, n
    for i, line in enumerate(riddle_input.splitlines()):
        # print(line)
        elements = line.split(" -> ")
        # print(elements)
        for k in range(1, len(elements)):

            start = elements[k - 1]
            stop = elements[k]

            x0 = int(start.split(",")[0])
            y0 = int(start.split(",")[1])
            x1 = int(stop.split(",")[0])
            y1 = int(stop.split(",")[1])

            if x0 < x1:
                xstart = x0
                xstop = x1
            else:
                xstart = x1
                xstop = x0
            if y0 < y1:
                ystart = y0
                ystop = y1
            else:
                ystart = y1
                ystop = y0

            mini = min(mini, ystart)
            minj = min(minj, xstart)
            maxi = max(maxi, ystop)
            maxj = max(maxj, xstop)
            for x in range(xstart, xstop + 1):
                for y in range(ystart, ystop + 1):
                    A[y, x] = 1

    A = A[mini : maxi + 1, minj : maxj + 1]
    startj = 0
    for j in range(A.shape[1]):
        if A[0, j] == 1:
            startj = j
            A[0, :] = 0
            break
    return A, startj


def riddle1(riddle_input: str) -> int | str:
    # print(riddle_input)
    A, start = get_matrix(riddle_input)

    # print(A.shape)
    # print(start)
    # fig, ax = plt.subplots()
    # ax.imshow(A)
    # plt.show()
    answer = 0
    while True:
        i = 0
        j = start + 1
        fixed = False
        while i < A.shape[0] - 1:
            if A[i + 1, j] == 0:
                i += 1
            elif A[i + 1, j - 1] == 0:
                i += 1
                j -= 1
            elif A[i + 1, j + 1] == 0:
                i += 1
                j += 1
            else:
                fixed = True
                answer += 1
                break
        A[i, j] = 2
        # fig, ax = plt.subplots()
        # ax.imshow(A)
        # plt.show()
        if not fixed:
            break

    return answer


def riddle2(riddle_input: str) -> int | str:
    answer = 0
    B, start = get_matrix(riddle_input)
    width = 1000
    A = np.zeros((B.shape[0] + 2, B.shape[1] + 2 * width), dtype=int)
    # place A in the middle
    A[: B.shape[0], width : width + B.shape[1]] = B
    A[-1, :] = 1
    start += width

    answer = 0
    while True:
        i = 0
        j = start + 1
        while i < A.shape[0] - 1:
            if A[i + 1, j] == 0:
                i += 1
            elif A[i + 1, j - 1] == 0:
                i += 1
                j -= 1
            elif A[i + 1, j + 1] == 0:
                i += 1
                j += 1
            else:
                answer += 1
                break
        # print(i, j)
        A[i, j] = 2

        if i == 0 and j == start + 1:
            break
    # fig, ax = plt.subplots()
    # ax.imshow(A)
    # plt.show()
    return answer


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    # placeholder for example
    # riddle_input = """498,4 -> 498,6 -> 496,6
    #  503,4 -> 502,4 -> 502,9 -> 494,9"""

    answer1 = riddle1(riddle_input)
    print(answer1)

    if answer1 != 0:
        answer2 = riddle2(riddle_input)
        print(answer2)
