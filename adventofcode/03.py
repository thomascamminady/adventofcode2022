from rich import print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def count(char: str):
    # map a through z to 1 through 26
    # and A through Z to 27 through 52
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def riddle1(riddle_input: str) -> int:
    answer = 0
    for line in riddle_input.splitlines():
        n = len(line)
        firsthalf = set(line[: n // 2])  # noqa: E203
        secondhalf = set(line[n // 2 :])  # noqa: E203
        commonchar = firsthalf.intersection(secondhalf)
        assert len(commonchar) == 1
        c = commonchar.pop()
        answer += count(c)

    return answer


def riddle2(riddle_input: str) -> int:
    answer = 0
    all_lines = riddle_input.splitlines()
    # iterate in steps of 3
    for i in range(0, len(all_lines), 3):
        f, s, t = all_lines[i : i + 3]  # noqa: E203
        intersection = set(f).intersection(set(s)).intersection(set(t))
        assert len(intersection) == 1
        c = intersection.pop()
        answer += count(c)

    return answer


if __name__ == "__main__":
    day = get_day(__file__)

    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)

    print(riddle1(riddle_input))
    print(riddle2(get_riddle_input(day)))
