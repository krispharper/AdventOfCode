from abc import ABC, abstractmethod
from itertools import combinations

from common.grids import Character
from common.input_data import parse_input


class Parser(ABC):
    def __init__(self):
        self.rows = parse_input(__file__)
        self.empty_rows, self.empty_columns = self._find_empty_indices()

    @property
    @abstractmethod
    def expansion_factor(self) -> int:
        pass

    def parse(self) -> None:
        galaxies = self._find_all_galaxies()
        distances = self._find_all_distances(galaxies)
        result = sum(distances)

        print(result)

    def _find_empty_indices(self) -> tuple[set[int], set[int]]:
        empty_rows = set()
        empty_columns = set()

        for row_index, row in enumerate(self.rows):
            if "#" not in row:
                empty_rows.add(row_index)

        for column_index in range(len(self.rows[0])):
            column = [r[column_index] for r in self.rows]

            if "#" not in column:
                empty_columns.add(column_index)

        return empty_rows, empty_columns

    def _find_distance(self, galaxy1: Character, galaxy2: Character) -> int:
        start_row = min(galaxy1.row_index, galaxy2.row_index)
        end_row = max(galaxy1.row_index, galaxy2.row_index)
        start_column = min(galaxy1.column_index, galaxy2.column_index)
        end_column = max(galaxy1.column_index, galaxy2.column_index)
        rows = 0
        columns = 0

        for row_index in range(start_row, end_row):
            if row_index in self.empty_rows:
                rows += self.expansion_factor
            else:
                rows += 1

        for column_index in range(start_column, end_column):
            if column_index in self.empty_columns:
                columns += self.expansion_factor
            else:
                columns += 1

        return rows + columns

    def _find_all_distances(self, galaxies: list[Character]) -> list[int]:
        return [self._find_distance(g1, g2) for g1, g2 in combinations(galaxies, 2)]

    def _find_all_galaxies(self) -> list[Character]:
        result = []

        for row_index, row in enumerate(self.rows):
            for column_index, column in enumerate(row):
                if column != "#":
                    continue

                result.append(Character(row_index, column_index, column))

        return result
