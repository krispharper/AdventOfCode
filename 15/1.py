test_data = [
    (5, 4),
    (2, 1)
]

data = [
    (5, 2),
    (13, 7),
    (17, 10),
    (3, 2),
    (19, 9),
    (7, 0)
]


def find_solution(data):
    index = 0

    while True:
        if not any((data[d][1] + index + d + 1) % data[d][0] for d in range(len(data))):
            return index

        index += 1

#print(find_solution(test_data))
print(find_solution(data))
data.append((11, 0))
print(find_solution(data))
