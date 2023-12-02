from collections.abc import Callable

from common.input_data import parse_input

NUMBERS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def _main() -> None:
    input = parse_input(__file__)
    result = sum(_parse_line(l) for l in input)
    print(result)


def _parse_line(line: str) -> int:
    min_value = _parse_number(line, min, lambda d: line.find(d))
    max_value = _parse_number(line, max, lambda d: line.rfind(d))

    return int(f"{min_value}{max_value}")


def _parse_number(line: str, min_max: Callable, find: Callable) -> str:
    text_indices = {find(n): n for n in NUMBERS}
    digit_indices = {i: d for i, d in enumerate(line) if d.isdigit()}

    _, value = min_max((i, n) for i, n in (text_indices | digit_indices).items() if i >= 0)

    if value.isdigit():
        return value

    return str(NUMBERS.index(value) + 1)


if __name__ == "__main__":
    _main()
