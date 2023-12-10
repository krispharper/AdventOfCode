from collections.abc import Sized


def batch(iterable: Sized, size: int):
    for i in range(0, len(iterable), size):
        yield iterable[i : i + size]
