from .common import Parser


class Parser1(Parser):
    @property
    def expansion_factor(self) -> int:
        return 1


if __name__ == "__main__":
    Parser1().parse()
