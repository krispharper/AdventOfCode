def compare(left: int, right: int) -> int:
    match (right - left):
        case -1 | 2:
            return 0
        case 0:
            return 3
        case 1 | -2:
            return 6


def score(left: int, right: int) -> int:
    return compare(left, right) + right + 1
