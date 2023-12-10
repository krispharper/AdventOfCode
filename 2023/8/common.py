import re
from itertools import repeat


def make_map(map_lines: list[str]) -> dict[str, tuple[str, str]]:
    return {x: (l, r) for x, l, r in [_parse_map_line(line) for line in map_lines]}


def follow_instructions(
    start_position: str, end_pattern: str, instructions: str, map: dict[str, tuple[str, str]]
) -> int:
    current_position = start_position
    steps = 0

    for instruction_iter in repeat(instructions):
        for instruction in instruction_iter:
            if instruction == "L":
                current_position = map[current_position][0]
            elif instruction == "R":
                current_position = map[current_position][1]
            else:
                raise ValueError(f"Unknown instruction {instruction}")

            steps += 1

            if re.match(end_pattern, current_position):
                return steps


def _parse_map_line(map_line: str) -> tuple[str, str, str]:
    if matches := re.search(r"(.{3}) = \((.{3}), (.{3})\)", map_line):
        return matches.groups()

    raise ValueError(f"Could not parse map line {map_line}")
