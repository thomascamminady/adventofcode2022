from rich import print

from adventofcode.helper.io import get_riddle_input, save_riddle_input


def riddle1(riddle_input: str) -> int:
    answer = 0
    current_count = 0
    for x in riddle_input.splitlines():
        if x == "":
            answer = max(answer, current_count)
            current_count = 0
        else:
            current_count += int(x)
    return answer


def riddle2(riddle_input: str) -> int:
    calories = []
    current_count = 0
    for x in riddle_input.splitlines():
        if x == "":
            calories.append(current_count)
            current_count = 0
        else:
            current_count += int(x)

    top = sorted(calories, reverse=True)[:3]
    return sum(top)


if __name__ == "__main__":
    riddle_input = get_riddle_input(__file__)
    save_riddle_input(__file__, riddle_input)

    print(riddle1(riddle_input))
    print(riddle2(get_riddle_input(__file__)))
