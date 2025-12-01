from common.input_data import parse_input

START = 50


def _main() -> None:
    input = parse_input(__file__)
    parsed_input = [_parse_line(l) for l in input]

    position = START
    result = 0

    for direction, amount in parsed_input:
        if direction == "L":
            position -= amount
        elif direction == "R":
            position += amount
        else:
            raise ValueError("Invalid direction")

        position %= 100

        if position == 0:
            result += 1

    print(result)


def _parse_line(value: str) -> tuple[str, int]:
    return value[0], int(value[1:])


if __name__ == "__main__":
    _main()
