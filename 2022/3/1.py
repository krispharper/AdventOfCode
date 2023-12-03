from common.input_data import parse_input
from .common import rank


def _main() -> None:
    result = sum(parse_line(line) for line in parse_input(__file__))

    print(result)


def parse_line(line: str) -> int:
    index = int(len(line) / 2)
    intersection = (set(line[:index]) & set(line[index:])).pop()

    return rank(intersection)


if __name__ == "__main__":
    _main()
