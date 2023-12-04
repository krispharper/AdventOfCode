from common.input_data import parse_input
from .common import parse_line


def _main() -> None:
    result = sum(_parse_line(line) for line in parse_input(__file__))

    print(result)


def _parse_line(line: str):
    _, matches = parse_line(line)

    if matches == 0:
        return 0
    return 2 ** (matches - 1)


if __name__ == "__main__":
    _main()
