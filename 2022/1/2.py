from .common import get_top_groups


def _main() -> None:
    result = get_top_groups(3)

    print(result)


if __name__ == "__main__":
    _main()
