from common.input_data import parse_input

START = 50


def _main() -> None:
    input = parse_input(__file__)
    parsed_input = [_parse_line(l) for l in input]

    position = START
    result = 0

    for amount in parsed_input:
        prior_position = position

        position += amount

        turns = abs(position // 100 - prior_position // 100)

        if position % 100 == 0 and amount < 0:
            turns += 1

        if prior_position % 100 == 0 and amount < 0:
            turns -= 1

        if turns > 0:
            print(f"State {prior_position=}, {amount=}, {position=}, {turns=}, {result=}")
            print(f"Adding {turns} to result")
            result += turns

        position %= 100

    print(result)


def _parse_line(value: str) -> int:
    amount = int(value[1:])

    if value[0] == "L":
        return -amount

    return amount


if __name__ == "__main__":
    _main()
