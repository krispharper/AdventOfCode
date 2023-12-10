from common.input_data import parse_input, parse_int_str


def process_lines() -> list[list[int]]:
    lines = parse_input(__file__)
    return [parse_int_str(line) for line in lines]


def process_sequence(sequence: list[int]) -> int:
    sequences = [sequence]

    while not all(i == 0 for i in sequence):
        sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        sequences.append(sequence)

    next_number = 0

    for sequence in sequences[::-1][1:]:
        next_number = sequence[-1] + next_number

    return next_number
