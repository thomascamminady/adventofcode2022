from adventofcode.helper.io import get_riddle_input


def main(riddle_input: str) -> int:
    answer = 0
    current_count = 0
    for x in riddle_input.splitlines():
        if x == "":
            answer = max(answer, current_count)
            current_count = 0
        else:
            current_count += int(x)
    return answer


if __name__ == "__main__":
    print(main(get_riddle_input(__file__)))
