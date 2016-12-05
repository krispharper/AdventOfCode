def test_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


with open('input.txt') as f:
    data = [int(x) for line in f for x in line.strip().split()]

count = 0

for i in range(0, len(data), 9):
    for j in range(3):
        if test_triangle(data[i + j], data[i + j + 3], data[i + j + 6]):
            count += 1

print(count)
