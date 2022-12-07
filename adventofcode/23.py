from rich import print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def riddle1(riddle_input: str) -> int | str:
    print(riddle_input)
    answer = 0
    return answer


def riddle2(riddle_input: str) -> int | str:
    # print(riddle_input)
    answer = 0
    return answer


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    answer1 = riddle1(riddle_input)
    print(answer1)

    answer2 = riddle2(riddle_input)
    print(answer2)
