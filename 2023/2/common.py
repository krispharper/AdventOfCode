from dataclasses import dataclass

from common.input_data import parse_input


class Colors:
    BLUE = "blue"
    GREEN = "green"
    RED = "red"


@dataclass
class Round:
    blue: int = 0
    green: int = 0
    red: int = 0

    @property
    def power(self):
        return self.blue * self.green * self.red


@dataclass
class Game:
    number: int
    rounds: list[Round]


def parse_line(line: str) -> Game:
    game_str, rounds_str = line.split(":")
    rounds = []

    for round_str in rounds_str.split(";"):
        round = Round()

        for draw_str in round_str.split(","):
            if Colors.BLUE in draw_str:
                round.blue = int(draw_str.replace(Colors.BLUE, ""))
            elif Colors.GREEN in draw_str:
                round.green = int(draw_str.replace(Colors.GREEN, ""))
            elif Colors.RED in draw_str:
                round.red = int(draw_str.replace(Colors.RED, ""))

        rounds.append(round)

    return Game(number=int(game_str[5:]), rounds=rounds)
