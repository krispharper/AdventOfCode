from common.input_data import parse_input
from .common import follow_instructions, make_map


def _main():
    lines = parse_input(__file__)
    instructions, map_lines = lines[0], lines[2:]
    map = make_map(map_lines)
    result = follow_instructions("AAA", "ZZZ", instructions, map)
    print(result)


if __name__ == "__main__":
    _main()
