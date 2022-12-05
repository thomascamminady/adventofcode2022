import re

from rich import print

from adventofcode.helper.io import get_riddle_input, save_riddle_input


def riddle1(riddle_input: str) -> str:
    lines = riddle_input.splitlines()[:8]
    contents = [[] for _ in range(9)]
    for li in lines:
        c = li[1:-1:4]
        for i, ci in enumerate(c):
            if ci != " ":
                contents[i].insert(0, ci)

    for line in riddle_input.splitlines()[10:]:
        if m := re.match(r"move (\d+) from (\w+) to (\w+)", line):
            n, x, y = m.groups()
            x, y, n = int(x) - 1, int(y) - 1, int(n)
            for i in range(min(n, len(contents[x]))):
                value = contents[x].pop()
                contents[y].append(value)

    answer = "".join([c[-1] for c in contents if c])
    return answer


def riddle2(riddle_input: str) -> str:
    lines = riddle_input.splitlines()[:8]
    contents = [[] for _ in range(9)]
    for li in lines:
        c = li[1:-1:4]
        for i, ci in enumerate(c):
            if ci != " ":
                contents[i].insert(0, ci)

    for line in riddle_input.splitlines()[10:]:
        if m := re.match(r"move (\d+) from (\w+) to (\w+)", line):
            n, x, y = m.groups()
            x, y, n = int(x) - 1, int(y) - 1, int(n)

            values = contents[x][-n:]
            contents[x] = contents[x][:-n]
            contents[y].extend(values)

    answer = "".join([c[-1] for c in contents if c])
    return answer


if __name__ == "__main__":
    riddle_input = get_riddle_input(__file__)
    save_riddle_input(__file__, riddle_input)

    print(riddle1(riddle_input))
    print(riddle2(get_riddle_input(__file__)))
