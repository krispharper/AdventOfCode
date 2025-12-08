import math

from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__, strip_input=False)
    row_groups = _parse_input_lines(input)

    total = 0

    for row_group in row_groups:
        operation = row_group[0][-1]

        values = []

        for row in row_group:
            if "".join(row).strip() == "":
                continue

            values.append(int("".join(row[:-1])))

        if operation == "+":
            total += sum(values)
        elif operation == "*":
            total += math.prod(values)

    print(total)


def _parse_input_lines(value: list[str]) -> list[list[list[str]]]:
    transposed = [[] for _ in range(len(value[0]))]

    for i in range(len(value[0])):
        for j in range(len(value)):
            transposed[i].append(value[j][i])

    result = []
    row_group = []

    for row in transposed:
        if set(row) == set(" "):
            result.append(row_group)
            row_group = []
        else:
            row_group.append(row)

    result.append(row_group)

    return result


if __name__ == "__main__":
    _main()
