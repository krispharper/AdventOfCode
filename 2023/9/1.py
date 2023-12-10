from .common import process_lines, process_sequence


def _main():
    sequences = process_lines()
    result = sum(process_sequence(sequence) for sequence in sequences)
    print(result)


if __name__ == "__main__":
    _main()
