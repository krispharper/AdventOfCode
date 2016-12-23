with open('input.txt') as f:
    data = [tuple(map(int, line.strip().split(' '))) for line in f]

count = 0

for d1 in data:
    for d2 in data:
        if d1 == d2:
            continue

        if d1[2] and d1[2] <= d2[3]:
            count += 1

print(count)
