from common.input_data import parse_input
from .common import parse_line


def _main() -> None:
    result = len([line for line in parse_input(__file__) if overlaps(*parse_line(line))])
    print(result)


def overlaps(one: tuple[int, int], two: tuple[int, int]) -> bool:
    if one[0] <= two[0] and two[1] <= one[1]:
        return True

    if two[0] <= one[0] and one[1] <= two[1]:
        return True

    return False


if __name__ == "__main__":
    _main()
