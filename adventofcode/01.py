from rich import print
from adventofcode.helper.io.get_input_from_url import get_input_from_url


def main(day: int) -> int:
    riddle_input = get_input_from_url(f"https://adventofcode.com/2022/day/{day}/input")
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
    answer = main(day=1)
    print(answer)
