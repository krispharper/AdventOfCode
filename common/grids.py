from dataclasses import dataclass
from enum import auto, Enum


class Direction(Enum):
    NORTHWEST = auto()
    NORTH = auto()
    NORTHEAST = auto()
    EAST = auto()
    SOUTHEAST = auto()
    SOUTH = auto()
    SOUTHWEST = auto()
    WEST = auto()

    def find_opposite(self) -> "Direction":
        if self == Direction.NORTHWEST:
            return Direction.SOUTHEAST

        if self == Direction.NORTH:
            return Direction.SOUTH

        if self == Direction.NORTHEAST:
            return Direction.SOUTHWEST

        if self == Direction.EAST:
            return Direction.WEST

        if self == Direction.SOUTHEAST:
            return Direction.NORTHWEST

        if self == Direction.SOUTH:
            return Direction.NORTH

        if self == Direction.SOUTHWEST:
            return Direction.NORTHEAST

        if self == Direction.WEST:
            return Direction.EAST


@dataclass(frozen=True)
class Character:
    row_index: int
    column_index: int
    value: str


def get_surrounding_characters(rows: list[str], row_index: int, column_index: int) -> dict[Direction, Character]:
    """
    Returns a dictionary of all characters surrounding a given character.
    """

    max_row_index = len(rows) - 1
    max_column_index = len(rows[0]) - 1
    result = {}

    if row_index > 0 and column_index > 0:
        result[Direction.NORTHWEST] = Character(row_index - 1, column_index - 1, rows[row_index - 1][column_index - 1])

    if row_index > 0:
        result[Direction.NORTH] = Character(row_index - 1, column_index, rows[row_index - 1][column_index])

    if row_index > 0 and column_index < max_column_index:
        result[Direction.NORTHEAST] = Character(row_index - 1, column_index + 1, rows[row_index - 1][column_index + 1])

    if column_index < max_column_index:
        result[Direction.EAST] = Character(row_index, column_index + 1, rows[row_index][column_index + 1])

    if row_index < max_row_index and column_index < max_column_index:
        result[Direction.SOUTHEAST] = Character(row_index + 1, column_index + 1, rows[row_index + 1][column_index + 1])

    if row_index < max_row_index:
        result[Direction.SOUTH] = Character(row_index + 1, column_index, rows[row_index + 1][column_index])

    if row_index < max_row_index and column_index > 0:
        result[Direction.SOUTHWEST] = Character(row_index + 1, column_index - 1, rows[row_index + 1][column_index - 1])

    if column_index > 0:
        result[Direction.WEST] = Character(row_index, column_index - 1, rows[row_index][column_index - 1])

    return result
