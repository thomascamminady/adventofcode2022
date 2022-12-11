from abc import ABC, abstractmethod

from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


class Operation(ABC):
    def __init__(self, value, use_old=False):
        self.value = value
        self.use_old = use_old

    @abstractmethod
    def execute(self, old):
        pass


class Add(Operation):
    def __init__(self, value, use_old=False):
        super().__init__(value, use_old)

    def execute(self, old):
        return old + (self.value if not self.use_old else old)


class Subtract(Operation):
    def __init__(self, value, use_old=False):
        super().__init__(value, use_old)

    def execute(self, old):
        return old - (self.value if not self.use_old else old)


class Multiply(Operation):
    def __init__(self, value, use_old=False):
        super().__init__(value, use_old)

    def execute(self, old):
        return old * (self.value if not self.use_old else old)


class Divide(Operation):
    def __init__(self, value, use_old=False):
        super().__init__(value, use_old)

    def execute(self, old):
        return old / (self.value if not self.use_old else old)


def operation_dispatcher(line: str) -> Operation:
    operation = line.split("=")[-1]
    use_old = "old" in operation[4:]
    value = int(operation.split(" ")[-1]) if not use_old else 0

    if "+" in operation:
        return Add(value, use_old)
    elif "-" in operation:
        return Subtract(value, use_old)
    elif "*" in operation:
        return Multiply(value, use_old)
    elif "/" in operation:
        return Divide(value, use_old)
    else:
        raise Exception("Unknown operation")


class Monkey:
    def __init__(self, starting_items, operation, divisible_by, if_true, if_false):
        self.starting_items = starting_items
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false
        self.inspection_count = 0

    def __repr__(self):
        return f"Monkey({self.starting_items}, {self.operation}, {self.divisible_by}, {self.if_true}, {self.if_false})"


def loop(monkeys: list[Monkey]) -> None:
    n_monkeys = len(monkeys)
    for i in range(n_monkeys):
        n_items = len(monkeys[i].starting_items)
        # inspect(monkeys[i])
        # inspect(monkeys[i].operation)
        for j in range(n_items):

            worry_level = monkeys[i].starting_items[j]
            # print(worry_level)
            worry_level = monkeys[i].operation.execute(worry_level)
            # print(worry_level)
            worry_level = worry_level // 3
            # print(worry_level)

            if worry_level % monkeys[i].divisible_by == 0:
                to_monkey = monkeys[i].if_true
            else:
                to_monkey = monkeys[i].if_false

            # print(
            # f"throw item {j} with final worry level {worry_level} to monkey {to_monkey}"
            # )
            monkeys[to_monkey].starting_items.append(worry_level)
        monkeys[i].inspection_count += n_items
        monkeys[i].starting_items = []


def loop2(monkeys: list[Monkey], gcd) -> None:
    n_monkeys = len(monkeys)
    for i in range(n_monkeys):
        n_items = len(monkeys[i].starting_items)
        # inspect(monkeys[i])
        # inspect(monkeys[i].operation)
        for j in range(n_items):

            worry_level = monkeys[i].starting_items[j]
            # print(worry_level)
            worry_level = monkeys[i].operation.execute(worry_level)
            # print(worry_level)
            worry_level = worry_level % gcd
            # print(worry_level)

            if worry_level % monkeys[i].divisible_by == 0:
                to_monkey = monkeys[i].if_true
            else:
                to_monkey = monkeys[i].if_false

            # print(
            # f"throw item {j} with final worry level {worry_level} to monkey {to_monkey}"
            # )
            monkeys[to_monkey].starting_items.append(worry_level)
        monkeys[i].inspection_count += n_items
        monkeys[i].starting_items = []


def get_monkeys(riddle_input: str) -> list[Monkey]:
    splitlines = riddle_input.splitlines()
    # print(splitlines)
    monkeys = []
    for i in range(0, len(splitlines), 7):
        items = splitlines[i + 1].split(":")[-1]
        items = [int(x) for x in items.split(",")]

        operation = operation_dispatcher(splitlines[i + 2])
        divisible_by = int(splitlines[i + 3].split("by")[-1])
        if_true = int(splitlines[i + 4].split("throw to monkey")[-1])
        if_false = int(splitlines[i + 5].split("throw to monkey")[-1])

        monkey = Monkey(items, operation, divisible_by, if_true, if_false)
        monkeys.append(monkey)
    return monkeys


def riddle1(riddle_input: str) -> int | str:
    monkeys = get_monkeys(riddle_input)

    for _ in range(20):
        loop(monkeys)

    counts = [monkey.inspection_count for monkey in monkeys]
    # sort
    counts.sort(reverse=True)
    # get two highest
    a, b = counts[:2]
    return a * b


def riddle2(riddle_input: str) -> int | str:
    monkeys = get_monkeys(riddle_input)
    divisors = [monkey.divisible_by for monkey in monkeys]
    # multiply together the entries in divisors
    prod = 1
    for d in divisors:
        prod *= d

    for _ in range(10000):
        loop2(monkeys, prod)

    counts = [monkey.inspection_count for monkey in monkeys]
    # sort
    counts.sort(reverse=True)
    # get two highest
    a, b = counts[:2]
    return a * b


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)

    save_riddle_input(day, riddle_input)

    answer1 = riddle1(riddle_input)
    print(answer1)

    answer2 = riddle2(riddle_input)
    print(answer2)
