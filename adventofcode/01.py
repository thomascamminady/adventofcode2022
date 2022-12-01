from rich import print

from adventofcode.helper.io import get_riddle_input


def main(riddle_input: str) -> int:
    calories = []
    elfs_calories = []
    for x in riddle_input.splitlines():
        if x == "":
            calories.append(sum(elfs_calories))
            elfs_calories = []
        else:
            elfs_calories.append(int(x))

    answer = max(calories)
    return answer


if __name__ == "__main__":
    print(main(get_riddle_input(__file__)))
