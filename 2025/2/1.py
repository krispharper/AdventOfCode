from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)
    parsed_input = _parse_line(input[0])

    results = []

    for lower, upper in parsed_input:
        for value in range(lower, upper + 1):
            string_value = str(value)

            if (
                len(string_value) % 2 == 0
                and string_value[: len(string_value) // 2] == string_value[len(string_value) // 2 :]
            ):
                results.append(value)

    print(sum(results))


def _parse_line(value: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, v.split("-"))) for v in value.split(",")]


if __name__ == "__main__":
    _main()
