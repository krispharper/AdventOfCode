from itertools import permutations


def populate_data():
    for i in range(len(raw_data[0])):
        for j in range(len(raw_data)):
            if raw_data[j][i] == '.':
                data.append((i, j))
            elif raw_data[j][i] == '0':
                temp_start = (i, j)
                points.append((i, j))
                data.append((i, j))
            elif raw_data[j][i].isdigit():
                points.append((i, j))
                data.append((i, j))

    return temp_start


def get_neighbor_nodes(x, y):
    neighbors = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    return set([n for n in neighbors if n in data])


def find_path(start, goal):
    distances = {}
    unvisted = set([])
    previous_nodes = {}
    distances[start] = 0
    unvisted.add(start)

    while unvisted:
        current = sorted([(k, v) for k, v in distances.items() if k in unvisted], key=lambda x: x[1])[0][0]

        if current == goal:
            return construct_path(previous_nodes, current)[:-1]

        unvisted.remove(current)
        neighbors = get_neighbor_nodes(*current)

        for neighbor in neighbors:
            temp_distance = distances[current] + 1

            if neighbor not in distances:
                unvisted.add(neighbor)

            if neighbor in distances:
                neighbor_distance = distances[neighbor]
            else:
                neighbor_distance = 1e6

            if temp_distance < neighbor_distance:
                distances[neighbor] = temp_distance
                previous_nodes[neighbor] = current


def construct_path(previous_nodes, current):
    path = [current]

    while current in previous_nodes:
        current = previous_nodes[current]
        path.append(current)

    return path


def find_min_path(go_back=False):
    min_distance = int(1e6)

    for p in permutations([x for x in points if x != start]):
        path = [start]
        path = path + list(p)

        if go_back:
            path.append(start)

        distance = 0

        for i in range(len(path) - 1):
            pair = (path[i], path[i + 1])
            distance += point_distances[pair]

        min_distance = min(min_distance, distance)

    print(min_distance)


with open('input.txt') as f:
    raw_data = [line.strip() for line in f]

data = []
points = []
start = populate_data()
end = [p for p in points if p != start][0]

point_distances = {}

for p1 in points:
    for p2 in points:
        point_distances[(p1, p2)] = len(find_path(p1, p2))

find_min_path()
find_min_path(True)
