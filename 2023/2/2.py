from common.input_data import parse_input
from .common import parse_line, Game, Round


def _main() -> None:
    games = [parse_line(i) for i in parse_input(__file__)]
    result = sum(_find_minimum_round(g).power for g in games)

    print(result)


def _find_minimum_round(game: Game) -> Round:
    return Round(
        blue=max(r.blue for r in game.rounds),
        green=max(r.green for r in game.rounds),
        red=max(r.red for r in game.rounds),
    )


if __name__ == "__main__":
    _main()
