from rich import print

from adventofcode.helper.io import get_riddle_input, save_riddle_input


def riddle1(riddle_input: str) -> int:
    print(riddle_input)
    answer = 0
    return answer


def riddle2(riddle_input: str) -> int:
    print(riddle_input)
    answer = 0
    return answer


if __name__ == "__main__":
    riddle_input = get_riddle_input(__file__)
    save_riddle_input(__file__, riddle_input)

    print(riddle1(riddle_input))
    # print(riddle2(get_riddle_input(__file__)))
