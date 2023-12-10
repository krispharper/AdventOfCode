from math import ceil

from .common import Parser


class Parser1(Parser):
    def parse(self) -> None:
        result = ceil(len(self.path.keys()) / 2)
        print(result)


if __name__ == "__main__":
    Parser1().parse()
