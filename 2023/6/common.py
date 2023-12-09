from collections.abc import Callable
from dataclasses import dataclass
from functools import reduce

from common.input_data import parse_input


@dataclass
class Race:
    time: int
    record: int


def main(parse_input: Callable[[], list[Race]]):
    outcomes = [_process_race(r) for r in parse_input()]
    result = reduce(lambda x, y: x * y, outcomes)

    print(result)


def _process_race(race: Race) -> int:
    winning_times = 0

    for speed in range(race.time + 1):
        distance = speed * (race.time - speed)

        if distance > race.record:
            winning_times += 1

    return winning_times
