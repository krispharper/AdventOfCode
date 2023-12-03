from common.input_data import parse_input

from common.iterables import batch
from .common import rank


def _main() -> None:
    result = sum(parse_line_group(line_group) for line_group in batch(parse_input(__file__), 3))

    print(result)


def parse_line_group(line_group: list[str]) -> int:
    intersection = (set(line_group[0]) & set(line_group[1]) & set(line_group[2])).pop()

    return rank(intersection)


if __name__ == "__main__":
    _main()
