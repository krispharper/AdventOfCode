from common.input_data import parse_input
from .common import compare, score


def _main() -> None:
    result = sum(score(*parse_line(line)) for line in parse_input(__file__))

    print(result)


def parse_line(line: str) -> tuple[int, int]:
    left, right = line.split(" ")
    left_value, target_score = "ABC".index(left), [0, 3, 6]["XYZ".index(right)]
    right_value = next(rv for rv in range(3) if compare(left_value, rv) == target_score)

    return left_value, right_value


if __name__ == "__main__":
    _main()
