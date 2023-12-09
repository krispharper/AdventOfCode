from common.input_data import parse_int_str
from common.iterables import batch
from .common import Parser


class Parser2(Parser):
    def _parse_seeds(self) -> list[tuple[int, int]]:
        seed_ints = parse_int_str(self.data[0].split(":")[1])

        result = []

        for seed, length in batch(seed_ints, 2):
            result.append((seed, length))

        return result


if __name__ == "__main__":
    Parser2().parse()
