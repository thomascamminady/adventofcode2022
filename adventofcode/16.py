from __future__ import annotations

from typing import Any, Optional

import matplotlib.pyplot as plt
import numpy as np
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


# #############################################################################
# ################################ RIDDLE 1 ###################################
# #############################################################################
def riddle1(riddle_input: str) -> int | str:
    # parsed_input = parse_input(riddle_input)

    answer = 0
    return answer


# #############################################################################
# ################################ RIDDLE 2 ###################################
# #############################################################################
def riddle2(riddle_input: str) -> int | str:
    # parsed_input = parse_input(riddle_input)

    answer = 0
    return answer


# #############################################################################
# ################################ HELPER #####################################
# #############################################################################
def parse_input(riddle_input: str) -> Optional[Any]:
    for i, line in enumerate(riddle_input.splitlines()):
        pass


def print_input() -> bool:
    return True
    return False


def get_example() -> str:
    return """"""


def load() -> str:
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)
    if (example := get_example()) != "":
        riddle_input = example
    if print_input():
        print(riddle_input)
    return riddle_input


if __name__ == "__main__":
    riddle_input = load()
    answer1 = riddle1(riddle_input)
    print(answer1)
    answer2 = riddle2(riddle_input)
    print(answer2)
