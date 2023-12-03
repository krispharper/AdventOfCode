from string import ascii_lowercase, ascii_uppercase


def rank(value: str) -> int:
    if value in ascii_lowercase:
        return ascii_lowercase.index(value) + 1

    return ascii_uppercase.index(value) + 27
