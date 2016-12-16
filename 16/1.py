from itertools import zip_longest


test_data = '10000'
test_length = 20

data = '10001110011110000'
length1 = 272
length2 = 35651584


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def fill_data(data, length):
    if len(data) >= length:
        return data[:length]
    else:
        data = data + "0" + "".join(str(1 - int(d)) for d in reversed(data))
        return fill_data(data, length)


def checksum(data):
    if len(data) % 2:
        return data
    else:
        data = "".join(str(1 - ((int(d[0]) + int(d[1])) % 2)) for d in grouper(2, data))
        return checksum(data)


print(checksum(fill_data(data, length1)))
print(checksum(fill_data(data, length2)))
