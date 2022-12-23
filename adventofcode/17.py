from __future__ import annotations

import numpy as np
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def get_shapes() -> list[np.ndarray]:
    shape0 = np.array([[0, 0], [0, 1], [0, 2], [0, 3]])
    shape1 = np.array([[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]])
    shape2 = np.array([[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]])
    shape3 = np.array([[0, 0], [1, 0], [2, 0], [3, 0]])
    shape4 = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    return [shape0, shape1, shape2, shape3, shape4]


def initial_stack() -> np.ndarray:
    return np.array([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]])


def get_initial_height(shape: np.ndarray, stack: np.ndarray) -> int:
    # get lowest y value of shape
    min_y = np.min(shape[:, 1])

    # get highest y value of stack
    max_y = np.max(stack[:, 1])

    # gap should be 3
    return max_y - min_y + 3


def get_initial_width(shape: np.ndarray, stack: np.ndarray) -> int:
    # get lowest x value of shape
    min_x = np.min(shape[:, 0])

    # get highest x value of stack
    max_x = np.max(stack[:, 0])

    # gap should be 3
    return max_x - min_x + 2


def get_initial_delta(shape: np.ndarray, stack: np.ndarray) -> np.ndarray:
    dx = get_initial_width(shape, stack)
    dy = get_initial_height(shape, stack)

    return np.array([dx, dy])


def check_if_overlap(shape: np.ndarray, stack: np.ndarray) -> bool:
    for i in range(shape.shape[0]):
        for j in range(stack.shape[0]):
            if np.array_equal(shape[i], stack[j]):
                return True
    return False


def riddle1(riddle_input: str) -> int | str:
    shapes = get_shapes()
    stack = initial_stack()
    print(shapes)
    movements = riddle_input
    current_movement = 0
    i = 0
    while i < 3:
        print(i)
        shape = shapes[i % 5].copy()
        delta = get_initial_delta(shape, stack)
        shape += delta
        print("###")
        print(delta)
        print(shape)
        # print(shapes)
        print(stack)
        for _ in range(5):
            print(shape)
            if movements[current_movement % len(movements)] == "<":
                shape -= np.array([1, 0])
            else:
                shape += np.array([1, 0])
            current_movement += 1

            if not check_if_overlap(shape - np.array([0, 1]), stack):
                shape -= np.array([0, 1])
            else:
                stack = np.concatenate((stack, shape))
                i += 1
                
                break
            
    return 0


def riddle2(riddle_input: str) -> int | str:
    answer = 0

    for i, line in enumerate(riddle_input.splitlines()):
        pass

    return answer


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    # placeholder for example
    # riddle_input = """"""

    # print(riddle_input)
    answer1 = riddle1(riddle_input)
    print(answer1)

    if answer1 != 0:
        answer2 = riddle2(riddle_input)
        print(answer2)
