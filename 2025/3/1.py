from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)

    print(sum([_parse_line(l) for l in input]))


def _parse_line(value: str) -> int:
    indexed_digits = list(enumerate(value))

    index, first_digit = max(indexed_digits[:-1], key=lambda indexed_digit: indexed_digit[1])
    _, second_digit = max(indexed_digits[index + 1 :], key=lambda indexed_digit: indexed_digit[1])

    return int(f"{first_digit}{second_digit}")


if __name__ == "__main__":
    _main()
