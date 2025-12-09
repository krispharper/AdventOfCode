from common.input_data import parse_input


def _main() -> None:
    input = parse_input(__file__)

    ray_indices = [0] * len(input[0])
    splits = 0

    for row in input:
        for index, value in enumerate(row):
            if value == "S":
                ray_indices[index] = 1

            if value == "^" and ray_indices[index] == 1:
                ray_indices[index - 1] = 1
                ray_indices[index] = 0
                ray_indices[index + 1] = 1
                splits += 1

    print(splits)


if __name__ == "__main__":
    _main()
