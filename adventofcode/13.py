from __future__ import annotations

import copy
from typing import Any

import numpy as np
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def is_ordered(left: list[Any], right: list[Any]) -> int:
    # -1, 0, +1, no,maybe,yes
    result = 0

    # check situation where one or more lists are empty
    if len(left) == 0 and len(right) == 0:
        return 0
    elif len(left) == 0:
        return -1
    elif len(right) == 0:
        return 1

    left_head = left.pop(0)
    right_head = right.pop(0)

    if isinstance(left_head, int) and isinstance(right_head, int):
        if left_head < right_head:
            return -1
        elif left_head > right_head:
            return 1
        else:
            result = is_ordered(left, right)

    if isinstance(left_head, list) and isinstance(right_head, int):
        result = is_ordered(left_head, [right_head])
    if isinstance(left_head, int) and isinstance(right_head, list):
        result = is_ordered([left_head], right_head)
    if isinstance(left_head, list) and isinstance(right_head, list):
        result = is_ordered(left_head, right_head)

    if result == 0:
        return is_ordered(left, right)
    else:
        return result


def riddle1(riddle_input: str) -> int | str:
    answer = 0
    lines = riddle_input.splitlines()
    n = len(lines)
    count = 0
    for i in range(0, n - 1, 3):
        count += 1
        left = list(eval(lines[i]))
        right = list(eval(lines[i + 1]))
        # print(left, right)
        order = is_ordered(left, right)
        if order == -1:
            answer += count
            # print("Is ordered")
        # else:
        # print("Is not ordered")

    return answer


def sort(lines: list[list[Any]]) -> list[list[Any]]:
    n = len(lines)
    for i in range(n):
        for j in range(0, n - i - 1):
            originalj = copy.deepcopy(lines[j])
            originaljplus1 = copy.deepcopy(lines[j + 1])
            if is_ordered(lines[j], lines[j + 1]) == 1:
                lines[j] = copy.deepcopy(originaljplus1)
                lines[j + 1] = copy.deepcopy(originalj)
            else:
                lines[j] = copy.deepcopy(originalj)
                lines[j + 1] = copy.deepcopy(originaljplus1)
    return lines


def riddle2(riddle_input: str) -> int | str:

    lines = riddle_input.splitlines()

    lines = [line for line in lines if line != ""]
    lines.append("[[2]]")
    lines.append("[[6]]")

    lines = [list(eval(line)) for line in lines]

    idx2 = 0
    idx6 = 0
    for i, line in enumerate(sort(lines)):
        if line == [[2]]:
            idx2 = i + 1
        if line == [[6]]:
            idx6 = i + 1
    return idx2 * idx6


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    # placeholder for example
    # riddle_input = """[1,1,3,1,1]
    # [1,1,5,1,1]

    # [[1],[2,3,4]]
    # [[1],4]

    # [9]
    # [[8,7,6]]

    # [[4,4],4,4]
    # [[4,4],4,4,4]

    # [7,7,7,7]
    # [7,7,7]

    # []
    # [3]

    # [[[]]]
    # [[]]

    # [1,[2,[3,[4,[5,6,7]]]],8,9]
    # [1,[2,[3,[4,[5,6,0]]]],8,9]"""

    # print(riddle_input)
    answer1 = riddle1(riddle_input)
    print(answer1)

    if answer1 != 0:
        answer2 = riddle2(riddle_input)
        print(answer2)
