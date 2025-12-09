from functools import lru_cache

from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)

    @lru_cache
    def _recurse(row_index: int, col_index: int) -> int:
        if row_index >= len(input):
            return 1

        row = input[row_index]
        col = row[col_index]

        if col == "S" or col == ".":
            result = _recurse(row_index + 1, col_index)
        elif col == "^":
            result = _recurse(row_index + 1, col_index - 1) + _recurse(row_index + 1, col_index + 1)
        else:
            result = 0

        return result

    result = _recurse(0, input[0].index("S"))

    print(result)


if __name__ == "__main__":
    _main()
