from math import lcm

from common.input_data import parse_input
from .common import follow_instructions, make_map


def _main():
    lines = parse_input(__file__)
    instructions, map_lines = lines[0], lines[2:]
    map = make_map(map_lines)
    result = _follow_instructions(instructions, map)
    print(result)


def _follow_instructions(instructions: str, map: dict[str, tuple[str, str]]) -> int:
    start_positions = [k for k in map if k.endswith("A")]
    steps = [follow_instructions(p, r"..Z", instructions, map) for p in start_positions]
    return lcm(*steps)


if __name__ == "__main__":
    _main()
