from math import log


def populate_dict(count):
    for i in range(1, count + 1):
        d[i] = 1


def loop(count):
    populate_dict(count)
    index = 1

    while True:
        new_index = find_next_index(index, count)

        if new_index == index:
            break

        d[index] += d[new_index]
        d[new_index] = 0
        index = find_next_index(index, count)

    return index


def increment(index, count):
    if index == len(d):
        return 1
    else:
        return index + 1


def find_next_index(index, count):
    next_index = increment(index, count)

    while not d[next_index]:
        next_index = increment(next_index, count)

    return next_index


def calculate(n):
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

print(loop(data))
print(calculate(data))
