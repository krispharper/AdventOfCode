from abc import ABC, abstractmethod
from math import ceil

from common.grids import Character, Direction, get_surrounding_characters
from common.input_data import parse_input


class Parser(ABC):
    def __init__(self):
        self.rows = parse_input(__file__)
        self.start_position = self._find_start_position()
        self.path = self._walk_maze()

    @abstractmethod
    def parse(self) -> None:
        result = ceil(len(self.path.keys()) / 2)
        print(result)

    def _walk_maze(self) -> dict[Character, int]:
        count = 1

        next_direction, next_character = self._find_next_pipe(self.start_position, None)
        path = {next_character: count}

        while next_character != self.start_position:
            incoming_direction = next_direction.find_opposite()
            next_direction, next_character = self._find_next_pipe(next_character, incoming_direction)
            count += 1
            path[next_character] = count

        return path

    def _find_next_pipe(
        self, character: Character, incoming_direction: Direction | None
    ) -> tuple[Direction, Character]:
        surrounding_characters = get_surrounding_characters(self.rows, character.row_index, character.column_index)

        if incoming_direction:
            surrounding_characters.pop(incoming_direction)

        for next_direction, next_character in surrounding_characters.items():
            if _is_valid_direction(character, next_character, next_direction):
                return next_direction, next_character

        raise ValueError(f"Cound not find next pipe for {character} with incoming direction {incoming_direction}")

    def _find_start_position(self) -> Character:
        for row_index, row in enumerate(self.rows):
            for column_index, column in enumerate(row):
                if column == "S":
                    return Character(row_index, column_index, "S")

        raise ValueError("Could not find start position")


def _is_valid_direction(current_character: Character, next_character: Character, direction: Direction) -> bool:
    if direction in {Direction.NORTHEAST, direction.SOUTHEAST, direction.SOUTHWEST, direction.NORTHWEST}:
        return False

    if next_character.value == ".":
        return False

    if direction == Direction.NORTH:
        if current_character.value in {"-", "F", "7"}:
            return False

        if next_character.value in {"-", "L", "J"}:
            return False

        return True

    if direction == Direction.EAST:
        if current_character.value in {"|", "J", "7"}:
            return False

        if next_character.value in {"|", "F", "L"}:
            return False

        return True

    if direction == Direction.SOUTH:
        if current_character.value in {"-", "L", "J"}:
            return False

        if next_character.value in {"-", "F", "7"}:
            return False

        return True

    if direction == Direction.WEST:
        if current_character.value in {"|", "F", "L"}:
            return False

        if next_character.value in {"|", "7", "J"}:
            return False

        return True


if __name__ == "__main__":
    Parser().parse()
