from rich import print
from adventofcode.helper.io.get_input_from_url import get_input_from_url


def main(day: int) -> int:
    riddle_input = get_input_from_url(f"https://adventofcode.com/2022/day/{day}/input")
    print(riddle_input)

    return answer


if __name__ == "__main__":
    answer = main(day=)
    print(answer)
