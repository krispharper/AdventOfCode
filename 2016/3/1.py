def test_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


with open('input.txt') as f:
    raw_data = [line.strip().split() for line in f]

data = []

for d in raw_data:
    data.append(list(map(int, d)))

print(sum(test_triangle(*d) for d in data))
