from rich import print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def riddle12(riddle_input: str, k: int) -> int | str:
    answer = 0
    for line in riddle_input.splitlines():
        for start in range(0, len(line) - k):
            if len(set(line[start : start + k])) == k:
                answer += start + k
                break

    return answer


def riddle1(riddle_input: str) -> int | str:
    return riddle12(riddle_input, 4)


def riddle2(riddle_input: str) -> int | str:
    return riddle12(riddle_input, 14)


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    print(riddle1(riddle_input))
    print(riddle2(get_riddle_input(day)))
