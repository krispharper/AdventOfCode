from pathlib import Path


def parse_input(file: str) -> list[str]:
    with open(Path(file).parent / "input.txt") as f:
        return [l.strip() for l in f.readlines()]


def parse_int_str(int_str: str) -> list[int]:
    return [int(n.strip()) for n in int_str.strip().split(" ") if n and not n.isspace()]
