from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)

    ranges, items = _parse_input_lines(input)
    total = 0

    for item in items:
        for range in ranges:
            if range[0] <= item <= range[1]:
                total += 1
                break

    print(total)


def _parse_input_lines(value: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    linebreak = value.index("")
    ranges = []

    items = [int(v) for v in value[linebreak + 1 :]]

    for line in value[:linebreak]:
        range = list(map(int, line.split("-")))
        ranges.append((range[0], range[1]))

    return ranges, items


if __name__ == "__main__":
    _main()
