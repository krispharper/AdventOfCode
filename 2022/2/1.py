from common.input_data import parse_input
from .common import score


def _main() -> None:
    result = sum(score(*parse_line(line)) for line in parse_input(__file__))

    print(result)


def parse_line(line: str) -> tuple[int, int]:
    left, right = line.split(" ")

    return "ABC".index(left), "XYZ".index(right)


if __name__ == "__main__":
    _main()
