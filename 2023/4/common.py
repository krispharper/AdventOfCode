def parse_line(line: str) -> tuple[int, int]:
    card_str, numbers = line.split(":")
    card = int(card_str[5:])

    winners_str, cadidates_str = numbers.split("|")
    winners, candidates = _parse_set(winners_str), _parse_set(cadidates_str)

    matches = len(winners & candidates)

    return card, matches


def _parse_set(input_str: str) -> set[int]:
    values = input_str.replace("  ", " ").strip().split(" ")
    return set(int(value) for value in values)
