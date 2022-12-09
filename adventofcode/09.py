from __future__ import annotations

import webbrowser
from typing import Literal

from rich import print

from adventofcode.helper.io import (
    get_day,
    get_riddle_input,
    save_riddle_input,
    submit_answer,
)


class Thing:
    def __init__(self):
        self.i: int = 0
        self.j: int = 0
        self.history: list[tuple[int, int]] = [(0, 0)]

    def up(self):
        self.i += 1
        # self.update_history()

    def down(self):
        self.i -= 1
        # self.update_history()

    def left(self):
        self.j -= 1
        # self.update_history()

    def right(self):
        self.j += 1
        # self.update_history()

    def update_history(self):
        # add current position to history if not already there
        if (self.i, self.j) not in self.history:
            self.history.append((self.i, self.j))

    def move(self, c: str):
        if c == "U":
            self.up()
        elif c == "D":
            self.down()
        elif c == "L":
            self.left()
        elif c == "R":
            self.right()
        else:
            raise ValueError("Invalid literal")

    def distance(self, other: Thing):
        return max(abs(self.i - other.i), abs(self.j - other.j))

    def plot(self):
        print("")
        n = 6
        for i, j in self.history:
            n = max(n, i, j)
        for i in range(n - 2, -1, -1):
            for j in range(n):
                if (i, j) in self.history:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def follow(self, other: Thing):
        if self.distance(other) <= 1:
            return
        else:
            if self.i < other.i:
                self.up()
            if self.i > other.i:
                self.down()
            if self.j < other.j:
                self.right()
            if self.j > other.j:
                self.left()
            self.update_history()


def print_board(head: Thing, tail: Thing):
    n = 6
    for i, j in head.history:
        n = max(n, i, j)
    for i, j in tail.history:
        n = max(n, i, j)

    print("")
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if (i, j) == (head.i, head.j):
                print("H", end="")
            elif (i, j) == (tail.i, tail.j):
                print("T", end="")
            else:
                print(".", end="")
        print()


def riddle1(riddle_input: str) -> int | str:
    head = Thing()
    tail = Thing()
    # print_board(head, tail)

    for row in riddle_input.splitlines():
        direction = row.split(" ")[0]
        repetitions = int(row.split(" ")[1])
        for _ in range(repetitions):
            head.move(direction)
            tail.follow(head)
            # print_board(head, tail)
    # tail.plot()
    # head.plot()
    # print(tail.history)
    answer = len(tail.history)
    return answer


def riddle2(riddle_input: str) -> int | str:

    knots = [Thing() for _ in range(10)]
    for row in riddle_input.splitlines():
        direction = row.split(" ")[0]
        repetitions = int(row.split(" ")[1])
        for _ in range(repetitions):
            knots[0].move(direction)
            for i in range(1, len(knots)):
                knots[i].follow(knots[i - 1])
    answer = len(knots[-1].history)
    return answer


if __name__ == "__main__":
    day = get_day(__file__)
    # webbrowser.open_new_tab(f"https://adventofcode.com/2022/day/{day}")

    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    #     riddle_input = """R 4
    # U 4
    # L 3
    # D 1
    # R 4
    # D 1
    # L 5
    # R 2"""
    answer1 = riddle1(riddle_input)
    print(answer1)
    # submit_answer(day, 1, answer1)

    answer2 = riddle2(riddle_input)
    print(answer2)
    # submit_answer(day, 2, answer2)
