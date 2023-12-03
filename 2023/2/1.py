from common.input_data import parse_input
from .common import parse_line, Game, Round


def _main() -> None:
    games = [parse_line(i) for i in parse_input(__file__)]
    result = sum(g.number for g in games if _is_valid_game(g))

    print(result)


def _is_valid_game(game: Game) -> bool:
    return all(_is_valid_round(r) for r in game.rounds)


def _is_valid_round(round: Round) -> bool:
    return round.red <= 12 and round.green <= 13 and round.blue <= 14


if __name__ == "__main__":
    _main()
