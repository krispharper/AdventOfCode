from collections import defaultdict

from common.input_data import parse_input
from .common import parse_line


class Parser:
    def __init__(self):
        self.lines = parse_input(__file__)
        self.card_counts = defaultdict(lambda: 1)

    def parse(self) -> None:
        for line in self.lines:
            self._parse_line(line)

        result = sum(self.card_counts.values())

        print(result)

    def _parse_line(self, line: str) -> int:
        card, matches = parse_line(line)

        for i in range(self.card_counts[card]):
            for i in range(card + 1, card + matches + 1):
                self.card_counts[i] += 1


if __name__ == "__main__":
    Parser().parse()
