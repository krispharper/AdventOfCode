from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)

    print(sum([_parse_line(l) for l in input]))


def _parse_line(value: str) -> int:
    indexed_digits = list(enumerate(value))

    results = []
    index = -1

    for i in range(11, -1, -1):
        if i > 0:
            index, digit = max(indexed_digits[index + 1 : -i], key=lambda indexed_digit: indexed_digit[1])
        else:
            index, digit = max(indexed_digits[index + 1 :], key=lambda indexed_digit: indexed_digit[1])

        results.append(digit)

    return int("".join(results))


if __name__ == "__main__":
    _main()
