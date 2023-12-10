from abc import ABC, abstractmethod
from dataclasses import dataclass

from more_itertools import flatten

from common.grids import Character, Direction, get_surrounding_characters
from common.input_data import parse_input


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

        return get_surrounding_characters(self.rows, row_index, column_index)
