from common.input_data import parse_int_str
from .common import Parser


class Parser1(Parser):
    def _parse_seeds(self) -> list[tuple[int, int]]:
        return [(s, 1) for s in parse_int_str(self.data[0].split(":")[1])]


if __name__ == "__main__":
    Parser1().parse()
