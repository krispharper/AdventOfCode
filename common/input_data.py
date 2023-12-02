from pathlib import Path


def parse_input(file: str) -> list[str]:
    with open(Path(file).parent / 'input.txt') as f:
        return [l.strip() for l in f.readlines()]
