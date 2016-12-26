from collections import deque


number = 1352
#number = 10


def is_open(x, y):
    temp = x * x + 3 * x + 2 * x * y + y + y * y + number
    return sum(int(d) for d in bin(temp)[2:]) % 2 == 0


def get_neighbor_nodes(x, y, max_size):
    neighbors = [
        (min(max_size, x + 1), y),
        (max(0, x - 1), y),
        (x, min(max_size, y + 1)),
        (x, max(0, y - 1))
    ]

    return set([n for n in neighbors if is_open(*n)])


def draw_map(x, y, path=[]):
    print('  ', end='')

    for i in range(x):
        print(str(i).zfill(2), end='')

    print()

    for i in range(y):
        print(str(i).zfill(2) + ' ', end='')

        for j in range(x):
            if is_open(j, i):
                if (j, i) in path:
                    print('O ', end='')
                else:
                    print('. ', end='')
            else:
                print('# ', end='')

        print()


def find_path(x, y, start, goal):
    distances = {}
    unvisted = set([])
    previous_nodes = {}

    for i in range(x):
        for j in range(y):
            distances[(i,j)] = int(1e6)
            unvisted.add((i, j))

    distances[start] = 0

    while unvisted:
        current = sorted([(k, v) for k, v in distances.items() if k in unvisted], key=lambda x: x[1])[0][0]

        if current == goal:
            return construct_path(previous_nodes, current)

        unvisted.remove(current)

        neighbors = get_neighbor_nodes(*current, y - 1)
        for neighbor in neighbors:
            temp_distance = distances[current] + 1

            if temp_distance < distances[neighbor]:
                distances[neighbor] = temp_distance
                previous_nodes[neighbor] = current


def construct_path(previous_nodes, current):
    path = [current]

    while current in previous_nodes:
        current = previous_nodes[current]
        path.append(current)

    return path

def valid_point(start, end, map_size):
    if not is_open(*end):
        return False

    path = find_path(map_size, map_size, start, end)

    if len(path) == 1 or len(path) > 51:
        return False

    return True


map_size = 52
start = (1, 1)
end = (31, 39)

path = find_path(map_size, map_size, start, end)
print(len(path) - 1)
draw_map(map_size, map_size, path)
print(sum([1 for x in range(map_size) for y in range(map_size) if valid_point(start, (x, y), map_size)]) + 1)
