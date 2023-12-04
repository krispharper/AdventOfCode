import re


def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    one, two, three, four = re.split(r"[,-]", line)

    return (int(one), int(two)), (int(three), int(four))
