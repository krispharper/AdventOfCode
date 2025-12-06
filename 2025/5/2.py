from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)

    ranges = _parse_input_lines(input)
    ranges = _merge_all_ranges(ranges)
    total = 0

    for range_item1 in ranges:
        total += range_item1[1] - range_item1[0] + 1

    print(total)


def _merge_all_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    for range1 in ranges:
        ranges = _merge_range_with_others(range1, ranges)

    return ranges


def _merge_range_with_others(range1: tuple[int, int], ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    results = []

    for range2 in ranges:
        merged = _merge_ranges(range1, range2)

        if not merged:
            results.append(range2)
        else:
            range1 = merged

    results.append(range1)

    return results


def _merge_ranges(range1: tuple[int, int], range2: tuple[int, int]) -> tuple[int, int] | None:
    a, b = range1
    c, d = range2

    if a < c:
        if b < c:
            return None

        if b <= d:
            return a, d

        if b > d:
            return a, b

    if a >= c:
        if b <= d:
            return c, d

        if a > d:
            return None

        if b > d:
            return c, b

    raise ValueError("Unnknown range overlap")


def _parse_input_lines(value: list[str]) -> list[tuple[int, int]]:
    linebreak = value.index("")
    ranges = []

    for line in value[:linebreak]:
        range_item = list(map(int, line.split("-")))
        ranges.append((range_item[0], range_item[1]))

    return ranges


if __name__ == "__main__":
    _main()
