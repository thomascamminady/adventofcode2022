from rich import print

from adventofcode.helper.io import get_riddle_input, save_riddle_input


def outcome(me: str, opponent: str) -> int:
    # you : A B C, ROCK PAPER SCISSORS
    # me: X Y Z, ROCK PAPER SCISSORS
    # 3 points for draw
    # 6 points for win
    # 0 points for loss
    # return points

    if me == "X" and opponent == "A":
        return 3
    elif me == "Y" and opponent == "B":
        return 3
    elif me == "Z" and opponent == "C":
        return 3
    elif me == "X" and opponent == "C":
        return 6
    elif me == "Y" and opponent == "A":
        return 6
    elif me == "Z" and opponent == "B":
        return 6
    else:
        return 0


def scoreforchoice(me: str) -> int:
    if me == "X":
        return 1
    elif me == "Y":
        return 2
    elif me == "Z":
        return 3
    else:
        print(me)
        raise ValueError("Invalid input")


def riddle1(riddle_input: str) -> int:
    p = 0
    for line in riddle_input.splitlines():
        opponent, me = line.split(" ")
        score1 = outcome(me, opponent)
        score2 = scoreforchoice(me)
        # print(me, opponent, score1, score2)
        p += score1 + score2
    return p


def outcome_to_action(opponent: str, outcome: str) -> str:
    if outcome == "X":  # loss
        if opponent == "A":
            return "Z"
        elif opponent == "B":
            return "X"
        elif opponent == "C":
            return "Y"
    elif outcome == "Y":  # draw
        if opponent == "A":
            return "X"
        elif opponent == "B":
            return "Y"
        elif opponent == "C":
            return "Z"
    elif outcome == "Z":
        if opponent == "A":
            return "Y"
        elif opponent == "B":
            return "Z"
        elif opponent == "C":
            return "X"
    else:
        raise ValueError("Invalid input")


def riddle2(riddle_input: str) -> int:
    p = 0
    for line in riddle_input.splitlines():
        opponent, expected_result = line.split(" ")
        me = outcome_to_action(opponent, expected_result)
        score1 = outcome(me, opponent)
        score2 = scoreforchoice(me)
        # print(me, opponent, score1, score2)
        p += score1 + score2
    return p


if __name__ == "__main__":

    riddle_input = get_riddle_input(__file__)
    save_riddle_input(__file__, riddle_input)

    print(riddle1(riddle_input))
    print(riddle2(get_riddle_input(__file__)))
