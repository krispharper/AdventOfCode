from collections import Counter

with open('input.txt') as f:
    raw_data = [line.strip() for line in f]

columns = []

for i in range(len(raw_data[0])):
    columns.append([])

for d in raw_data:
    for i in range(len(raw_data[0])):
        columns[i].append(d[i])

for c in columns:
    print(Counter(c).most_common()[-1:][0][0], end='')

print()
