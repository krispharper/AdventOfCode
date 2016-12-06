from collections import Counter
from string import ascii_lowercase

def split_data(data):
    index1 = data.rfind('-')
    index2 = data.find('[')
    return data[:index1].replace('-', ''), int(data[index1 + 1:index2]), data[index2 + 1:-1]


def is_real(data):
    freq = Counter(data[0]).most_common()
    s = sorted(freq, reverse=True, key=lambda x: (x[1], 25 - ascii_lowercase.index(x[0])))
    return data[2] == "".join(x[0] for x in s[:5])


def sum_real(data):
    print(sum(d[1] for d in [split_data(x) for x in data] if is_real(d)))


with open('input.txt') as f:
    raw_data = [line.strip() for line in f]

test_data = [
    'aaaaa-bbb-z-y-x-123[abxyz]',
    'a-b-c-d-e-f-g-h-987[abcde]',
    'not-a-real-room-404[oarel]',
    'totally-real-room-200[decoy]'
]

sum_real(raw_data)
