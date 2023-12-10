from common.grids import Character
from .common import Parser


class Parser2(Parser):
    def parse(self) -> None:
        print(self._count_inner_cells())

    def _count_inner_cells(self) -> int:
        inner_cells = 0

        for row_index, row in enumerate(self.rows[:-1]):
            crossing_count = 0

            for column_index, column in enumerate(row):
                character = Character(row_index, column_index, column)

                if character not in self.path.keys() and crossing_count != 0:
                    inner_cells += 1

                if character in self.path.keys():
                    character_below = Character(row_index + 1, column_index, self.rows[row_index + 1][column_index])

                    if character_below not in self.path.keys():
                        continue

                    difference = self.path[character] - self.path[character_below]

                    if difference > 0:
                        difference %= len(self.path.keys())

                    if abs(difference) != 1:
                        continue

                    crossing_count += difference

        return inner_cells


if __name__ == "__main__":
    Parser2().parse()
