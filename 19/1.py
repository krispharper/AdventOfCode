from math import log


def calculate1(n):
    p = int(log(n, 2))
    r = n - 2 ** p
    return 2 * r + 1


def calculate2(n):
    p = int(log(n, 3))
    low = 3 ** p
    high = 3 ** (p + 1)

    if n > low * 2:
        return 2 * n - high
    else:
        return n - low


test_data = 5
data = 3017957
d = {}

print(calculate1(data))
print(calculate2(data))
