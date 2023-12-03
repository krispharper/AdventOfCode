from .common import Parser, Character


class Parser1(Parser):
    def parse(self) -> None:
        for row_index in range(len(self.rows)):
            self._parse_row(row_index)

        valid_numbers = [
            parsed_number.number
            for parsed_number in self.parsed_numbers
            if any(Parser1._is_symbol(c) for c in parsed_number.surrounding_characters)
        ]

        print(sum(valid_numbers))

    @staticmethod
    def _is_symbol(character: Character) -> bool:
        return character.value != "." and not character.value.isdigit()


if __name__ == "__main__":
    Parser1().parse()
