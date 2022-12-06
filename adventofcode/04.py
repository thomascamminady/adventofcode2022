from rich import print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def contains(start0, end0, start1, end1):
    return start0 <= start1 and end0 >= end1


def riddle1(riddle_input: str) -> int:
    answer = 0
    for line in riddle_input.splitlines():
        first, second = line.split(",")
        start0, end0 = first.split("-")
        start1, end1 = second.split("-")
        start0, start1 = int(start0), int(start1)
        end0, end1 = int(end0), int(end1)

        if contains(start0, end0, start1, end1):
            answer += 1
        elif contains(start1, end1, start0, end0):
            answer += 1

    return answer


def riddle2(riddle_input: str) -> int:
    answer = 0
    for line in riddle_input.splitlines():
        first, second = line.split(",")
        start0, end0 = first.split("-")
        start1, end1 = second.split("-")
        start0, start1 = int(start0), int(start1)
        end0, end1 = int(end0), int(end1)

        numbers0 = set(range(start0, end0 + 1))
        numbers1 = set(range(start1, end1 + 1))
        common = numbers0.intersection(numbers1)
        ncommon = len(common)
        if ncommon > 0:
            answer += 1
    return answer


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    print(riddle1(riddle_input))
    print(riddle2(get_riddle_input(day)))
