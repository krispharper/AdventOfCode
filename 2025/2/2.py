from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)
    parsed_input = _parse_line(input[0])

    results = []

    for lower, upper in parsed_input:
        for value in range(lower, upper + 1):
            string_value = str(value)

            for chunk_size in range(1, len(string_value) // 2 + 1):
                if len(string_value) % chunk_size != 0:
                    continue

                if len(set(string_value[0 + i : chunk_size + i] for i in range(0, len(string_value), chunk_size))) == 1:
                    results.append(value)
                    break

    print(sum(results))


def _parse_line(value: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, v.split("-"))) for v in value.split(",")]


if __name__ == "__main__":
    _main()
