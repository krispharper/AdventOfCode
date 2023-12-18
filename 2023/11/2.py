from .common import Parser


class Parser2(Parser):
    @property
    def expansion_factor(self) -> int:
        return 1_000_000


if __name__ == "__main__":
    Parser2().parse()
