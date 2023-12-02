from pathlib import Path

from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)
    result = sum(_parse_number(i) for i in input)

    print(result)


def _parse_number(value: str) -> int:
    first = [x for x in value if x.isdigit()][0]
    last = [x for x in value if x.isdigit()][-1]

    return int(f"{first}{last}")


if __name__ == "__main__":
    _main()
