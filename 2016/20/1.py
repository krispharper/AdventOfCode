def find_first():
    max_bound = data[0][1]

    for d in data:
        if d[0] > max_bound + 1:
            result = max_bound + 1
            break
        else:
            max_bound = max(max_bound, d[1])

    print(result)


def find_all():
    count = 0
    max_bound = data[0][1]

    for d in data:
        if d[0] > max_bound + 1:
            count += (d[0] - max_bound - 1)

        max_bound = max(max_bound, d[1])

    print(count)


with open('input.txt') as f:
    raw_data = [line.strip() for line in f]

data = []

for d in raw_data:
    t = d.split('-')
    data.append((int(t[0]), int(t[1])))

data = sorted(data)
find_first()
find_all()
