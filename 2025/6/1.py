import math

from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)
    lines = _parse_input_lines(input)

    operations = lines[-1]
    total = 0

    for index, operation in enumerate(operations):
        if operation == "+":
            total += sum(int(l[index]) for l in lines[:-1])
        elif operation == "*":
            total += math.prod(int(l[index]) for l in lines[:-1])

    print(total)


def _parse_input_lines(value: list[str]) -> list[list[str]]:
    result = []

    for line in value:
        result.append(line.split())

    return result


if __name__ == "__main__":
    _main()
