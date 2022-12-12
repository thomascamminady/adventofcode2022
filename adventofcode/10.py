import numpy as np
from rich import print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def riddle1(riddle_input: str) -> int | str:
    answer = 0
    x = 1
    checkpoints = np.arange(20, 221, 40)
    cycle = 0
    for line in riddle_input.splitlines():

        if line == "noop":
            n_cycle = 1
            op = 0
        else:
            _, op = line.split(" ")
            op = int(op)
            n_cycle = 2

        for _ in range(n_cycle):
            cycle += 1
            if cycle in checkpoints:
                # print(cycle, x, x * cycle)
                answer += cycle * x

        x += op

    return answer


def riddle2(riddle_input: str, show_output=True) -> int | str:
    x = 1
    checkpoints = np.arange(40, 241, 40)
    cycle = 0
    current_row = ""
    row = 0
    matrix = []
    for line in riddle_input.splitlines():

        if line == "noop":
            n_cycle = 1
            op = 0
        else:
            _, op = line.split(" ")
            op = int(op)
            n_cycle = 2

        for _ in range(n_cycle):
            if _ == 1:
                x += op
            if abs(len(current_row) + 1 - row * 40 - x) <= 1:
                current_row += "#"
            else:
                current_row += " "

            cycle += 1
            if cycle in checkpoints:
                if show_output:
                    y = "#" + current_row[row * 40 : row * 40 + 40]
                    print(y)
                    matrix.append([1 if xi == "#" else 0 for xi in y])
                row += 1

    # Save the matrix as an image
    return "RGLRBZAU"


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    answer1 = riddle1(riddle_input)
    print(answer1)

    answer2 = riddle2(riddle_input)
    print(answer2)
