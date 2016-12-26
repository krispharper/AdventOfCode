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

for y in range(28):
    for x in range(32):
        d = data[x * 28 + y]
        if d[0] == 31 and d[1] == 0:
            print(' G ', end='')
        elif int(d[2]) > 100:
            print(' # ', end='')
        elif int(d[2]) == 0:
            print(' _ ', end='')
        else:
            print(" . ", end='')

    print()
