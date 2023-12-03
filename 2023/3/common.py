from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import auto, Enum

from more_itertools import flatten

from common.input_data import parse_input


class Direction(Enum):
    NORTHWEST = auto()
    NORTH = auto()
    NORTHEAST = auto()
    EAST = auto()
    SOUTHEAST = auto()
    SOUTH = auto()
    SOUTHWEST = auto()
    WEST = auto()


@dataclass(frozen=True)
class Character:
    row_index: int
    column_index: int
    value: str


@dataclass(frozen=True)
class ParsedNumber:
    number: int
    surrounding_characters: set[Character]


class Parser(ABC):
    def __init__(self):
        self.rows: list[str] = parse_input(__file__)
        self.max_row_index = len(self.rows) - 1
        self.max_column_index = len(self.rows[0]) - 1
        self.current_number: list[tuple[str, list[Character]]] = []
        self.parsed_numbers: list[ParsedNumber] = []

    @abstractmethod
    def parse(self) -> None:
        pass

    def _parse_row(self, row_index: int) -> None:
        row = self.rows[row_index]

        for column_index, character in enumerate(row):
            if not character.isdigit():
                self._parse_current_number()
                continue

            surrounding_characters = list(self._get_surrounding_characters(row_index, column_index).values())
            self.current_number.append((character, surrounding_characters))

        self._parse_current_number()

    def _parse_current_number(self):
        if not self.current_number:
            return

        number = int("".join(n for n, _ in self.current_number))
        characters = flatten(c for _, c in self.current_number)
        self.parsed_numbers.append(ParsedNumber(number, set(characters)))
        self.current_number = []

    def _get_surrounding_characters(self, row_index: int, column_index: int) -> dict[Direction, Character]:
        """
        Returns a dictionary of all characters surrounding a given character.
        """

        result = {}

        if row_index > 0 and column_index > 0:
            result[Direction.NORTHWEST] = Character(
                row_index - 1, column_index - 1, self.rows[row_index - 1][column_index - 1]
            )

        if row_index > 0:
            result[Direction.NORTH] = Character(row_index - 1, column_index, self.rows[row_index - 1][column_index])

        if row_index > 0 and column_index < self.max_column_index:
            result[Direction.NORTHEAST] = Character(
                row_index - 1, column_index + 1, self.rows[row_index - 1][column_index + 1]
            )

        if column_index < self.max_column_index:
            result[Direction.EAST] = Character(row_index, column_index + 1, self.rows[row_index][column_index + 1])

        if row_index < self.max_row_index and column_index < self.max_column_index:
            result[Direction.SOUTHEAST] = Character(
                row_index + 1, column_index + 1, self.rows[row_index + 1][column_index + 1]
            )

        if row_index < self.max_row_index:
            result[Direction.SOUTH] = Character(row_index + 1, column_index, self.rows[row_index + 1][column_index])

        if row_index < self.max_row_index and column_index > 0:
            result[Direction.SOUTHWEST] = Character(
                row_index + 1, column_index - 1, self.rows[row_index + 1][column_index - 1]
            )

        if column_index > 0:
            result[Direction.WEST] = Character(row_index, column_index - 1, self.rows[row_index][column_index - 1])

        return result
