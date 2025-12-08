from pathlib import Path


def parse_input(file: str, strip_input: bool = True) -> list[str]:
    with open(Path(file).parent / "input.txt") as f:
        if strip_input:
            return [l.strip() for l in f.readlines()]

        return [l for l in f.readlines()]


def parse_int_str(int_str: str) -> list[int]:
    return [int(n.strip()) for n in int_str.strip().split(" ") if n and not n.isspace()]
