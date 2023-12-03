from collections import defaultdict
from functools import reduce

from .common import Parser


class Parser2(Parser):
    def parse(self) -> None:
        for row_index in range(len(self.rows)):
            self._parse_row(row_index)

        gears = self._create_gear_map()
        result = sum(reduce(lambda x, y: x * y, numbers) for numbers in gears.values() if len(numbers) == 2)

        print(result)

    def _create_gear_map(self) -> dict[tuple[int, int], list[int]]:
        gears = defaultdict(list)

        for parsed_number in self.parsed_numbers:
            for surrounding_character in parsed_number.surrounding_characters:
                if surrounding_character.value != "*":
                    continue

                gears[(surrounding_character.row_index, surrounding_character.column_index)].append(
                    parsed_number.number
                )

        return gears


if __name__ == "__main__":
    Parser2().parse()
