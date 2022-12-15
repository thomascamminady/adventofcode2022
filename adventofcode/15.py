from __future__ import annotations

import re
from typing import Any, Optional

import matplotlib.pyplot as plt
import numpy as np
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def distance(self, other: Point) -> int:
        return self.manhatten_distance(other)

    def manhatten_distance(self, other: Point) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return self.__str__()


def unique(seq: list[Any]) -> list[Any]:
    output = []
    for x in seq:
        if x not in output:
            output.append(x)
    return output


class Interval:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def contains(self, point: Point) -> bool:
        return self.start <= point.x <= self.stop

    def elements(self) -> int:
        return self.stop - self.start + 1

    def elements_between(self, lower, upper) -> int:
        return min(self.stop, upper) - max(self.start, lower) + 1

    def __repr__(self) -> str:
        return f"[{self.start}, {self.stop}]"

    def __str__(self) -> str:
        return self.__repr__()


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    intervals = sorted(intervals, key=lambda x: x.start)
    merged = []
    for higher in intervals:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            if higher.start <= lower.stop:
                upper_bound = max(lower.stop, higher.stop)
                merged[-1] = Interval(
                    lower.start, upper_bound
                )  # replace by merged interval
            else:
                merged.append(higher)
    return merged


# #############################################################################
# ################################ RIDDLE 1 ###################################
# #############################################################################
def riddle1(riddle_input: str) -> int | str:
    y = 2000000
    sensors, beacons = parse_input(riddle_input)

    intervals = []
    for sensor, beacon in zip(sensors, beacons):
        distance = sensor.distance(beacon)
        if (dx := distance - abs(sensor.y - y)) < 0:
            continue
        else:
            intervals.append(Interval(sensor.x - dx, sensor.x + dx))

    intervals = merge_intervals(intervals)
    beacon_count = 0
    for beacon in unique(beacons):
        if beacon.y == y:
            for interval in intervals:
                if interval.contains(beacon):
                    beacon_count += 1
                    break

    nelements = 0
    for interval in intervals:
        nelements += interval.elements()

    return nelements - beacon_count


def get_elements_in_row_between_0_and_4000000(
    y, sensors, beacons, lower=0, upper=4000000
):
    intervals = []
    for sensor, beacon in zip(sensors, beacons):
        distance = sensor.distance(beacon)
        if (dx := distance - abs(sensor.y - y)) < 0:
            continue
        else:
            intervals.append(Interval(sensor.x - dx, sensor.x + dx))

    intervals = merge_intervals(intervals)

    nelements = 0
    for interval in intervals:
        nelements += interval.elements_between(lower, upper)

    return nelements


# #############################################################################
# ################################# RIDDLE 2 ##################################
# #############################################################################
def riddle2(riddle_input: str) -> int | str:
    sensors, beacons = parse_input(riddle_input)
    lower = 0
    upper = 20
    upper = 4000000
    finaly = 0
    for y in range(upper + 1):
        x = get_elements_in_row_between_0_and_4000000(
            y, sensors, beacons, lower=lower, upper=upper
        )
        # print(y, x, upper + 1)
        if x < (upper + 1):
            finaly = y
            break
    intervals = []
    for sensor, beacon in zip(sensors, beacons):
        distance = sensor.distance(beacon)
        if (dx := distance - abs(sensor.y - finaly)) < 0:
            continue
        else:
            intervals.append(Interval(sensor.x - dx, sensor.x + dx))
    x = merge_intervals(intervals)[0].stop + 1
    return finaly + x * 4000000


# #############################################################################
# ################################ HELPER #####################################
# #############################################################################
def parse_input(riddle_input: str) -> tuple[list[Point], list[Point]]:
    beacons = []
    sensors = []
    for i, line in enumerate(riddle_input.splitlines()):
        sensor, beacon = line.split(":")
        matches = re.findall(r"x=(-?\d+), y=(-?\d+)", sensor)
        sx, sy = matches[0]
        ps = Point(sx, sy)
        sensors.append(ps)
        matches = re.findall(r"x=(-?\d+), y=(-?\d+)", beacon)
        bx, by = matches[0]
        pb = Point(bx, by)
        # print(ps, pb)
        beacons.append(pb)

    return sensors, beacons


def print_input() -> bool:
    # return True
    return False


def get_example() -> str:
    return ""
    return """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def load() -> str:
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)
    if (example := get_example()) != "":
        riddle_input = example
    if print_input():
        print(riddle_input)
    return riddle_input


if __name__ == "__main__":
    riddle_input = load()
    answer1 = riddle1(riddle_input)
    print(answer1)
    answer2 = riddle2(riddle_input)
    print(answer2)
