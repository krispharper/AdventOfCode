from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)

    grid = parse_input_lines(input)
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != "@":
                continue

            if len([n for n in _get_all_neighbors(row, col, grid) if n == "@"]) < 4:
                total += 1

    print(total)


def parse_input_lines(value: list[str]) -> list[list[str]]:
    return [list(line) for line in value]


def _get_all_neighbors(row: int, col: int, grid: list[list[str]]) -> list[str]:
    neighbors = []

    for r in [row - 1, row, row + 1]:
        for c in [col - 1, col, col + 1]:
            if r == row and c == col:
                continue

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue

            try:
                neighbors.append(grid[r][c])
            except IndexError:
                pass

    return neighbors


if __name__ == "__main__":
    _main()
