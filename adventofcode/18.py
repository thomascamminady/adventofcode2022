from __future__ import annotations

import numpy as np
from numba import stencil
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def parse(riddle_input: str) -> np.ndarray:
    maxi, maxj, maxk = 0, 0, 0
    for _, line in enumerate(riddle_input.splitlines()):
        i, j, k = line.split(",")
        i = int(i)
        j = int(j)
        k = int(k)
        maxi = max(maxi, i)
        maxj = max(maxj, j)
        maxk = max(maxk, k)

    A = np.zeros((maxi + 3, maxj + 3, maxk + 3), dtype=bool)
    for _, line in enumerate(riddle_input.splitlines()):
        i, j, k = line.split(",")
        i = int(i)
        j = int(j)
        k = int(k)
        A[i + 1, j + 1, k + 1] = True
    return A


def riddle1(riddle_input: str) -> int | str:
    answer = 0
    A = parse(riddle_input)
    n = 0
    for _, line in enumerate(riddle_input.splitlines()):
        i, j, k = line.split(",")
        i = int(i) + 1
        j = int(j) + 1
        k = int(k) + 1
        if A[i, j, k]:
            # check how many of the six neighbors are active
            sum = 0
            sum += A[i - 1, j, k]
            sum += A[i + 1, j, k]
            sum += A[i, j - 1, k]
            sum += A[i, j + 1, k]
            sum += A[i, j, k - 1]
            sum += A[i, j, k + 1]
            n += 6 - sum

    return n


@stencil
def kernel1(a):
    if a[0, 0, 0] == 1:
        return 1
    if (
        a[0, 0, 1] == -1
        or a[0, 0, -1] == -1
        or a[0, 1, 0] == -1
        or a[0, -1, 0] == -1
        or a[1, 0, 0] == -1
        or a[-1, 0, 0] == -1
    ):
        return -1
    return 0


def riddle2(riddle_input: str) -> int | str:
    A = parse(riddle_input)
    A = np.asarray(A, dtype=int)
    # place a -1 in all eight corners of the cube
    A[0, :, :] = -1
    A[-1, :, :] = -1
    A[:, 0, :] = -1
    A[:, -1, :] = -1
    A[:, :, 0] = -1
    A[:, :, -1] = -1

    for _ in range(1000):
        for i in range(1, A.shape[0] - 1):
            for j in range(1, A.shape[1] - 1):
                for k in range(1, A.shape[2] - 1):
                    if A[i, j, k] == 1:
                        continue
                    else:
                        if (
                            A[i - 1, j, k] == -1
                            or A[i + 1, j, k] == -1
                            or A[i, j - 1, k] == -1
                            or A[i, j + 1, k] == -1
                            or A[i, j, k - 1] == -1
                            or A[i, j, k + 1] == -1
                        ):
                            A[i, j, k] = -1
    n = 0
    for _, line in enumerate(riddle_input.splitlines()):
        i, j, k = line.split(",")
        i = int(i) + 1
        j = int(j) + 1
        k = int(k) + 1
        if A[i, j, k]:
            # check how many of the six neighbors are active
            sum = 0
            if A[i - 1, j, k] == -1:
                sum += 1
            if A[i + 1, j, k] == -1:
                sum += 1
            if A[i, j - 1, k] == -1:
                sum += 1
            if A[i, j + 1, k] == -1:
                sum += 1
            if A[i, j, k - 1] == -1:
                sum += 1
            if A[i, j, k + 1] == -1:
                sum += 1

            n += sum
    return n


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    # placeholder for example
    # riddle_input = """2,2,2
    # 1,2,2
    # 3,2,2
    # 2,1,2
    # 2,3,2
    # 2,2,1
    # 2,2,3
    # 2,2,4
    # 2,2,6
    # 1,2,5
    # 3,2,5
    # 2,1,5
    # 2,3,5"""

    # print(riddle_input)
    answer1 = riddle1(riddle_input)
    print(answer1)

    if answer1 != 0:
        answer2 = riddle2(riddle_input)
        print(answer2)
