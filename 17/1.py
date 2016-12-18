from hashlib import md5


test1 = b'hijkl'
test2 = (b'ihgpwlah', 'DDRRRD')
test3 = (b'kglvqrro', 'DDUDRLRRUDRD')
test4 = (b'ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')
code = b'dmypynyp'


def get_neighbors(x, y, s):
    neighbors = []
    h = get_hash(s)

    if is_open_position(h[0]) and y - 1 >= 0:
        neighbors.append((x, y - 1, b'U'))
    if is_open_position(h[1]) and y + 1 <= 3:
        neighbors.append((x, y + 1, b'D'))
    if is_open_position(h[2]) and x - 1 >= 0:
        neighbors.append((x - 1, y, b'L'))
    if is_open_position(h[3]) and x + 1 <= 3:
        neighbors.append((x + 1, y, b'R'))

    return set(neighbors)


def get_hash(s):
    return md5(s).hexdigest()[:4]


def is_open_position(c):
    return c in "bcdef"


def find_path(start, goal, code):
    distances = {}
    unvisted = set([])
    previous_nodes = {}
    distances[start] = 0
    unvisted.add(start)

    while unvisted:
        current = sorted([(k, v) for k, v in distances.items() if k in unvisted], key=lambda x: x[1])[0][0]

        if (current[0], current[1]) == goal:
            return current[2].decode('ascii')

        unvisted.remove(current)
        hash_string = code + current[2]

        for neighbor in get_neighbors(current[0], current[1], hash_string):
            neighbor = (neighbor[0], neighbor[1], current[2] + neighbor[2])
            unvisted.add(neighbor)
            temp_distance = distances[current] + 1

            if neighbor in distances:
                neighbor_distance = distances[neighbor]
            else:
                neighbor_distance = 1e6

            if temp_distance < neighbor_distance:
                distances[neighbor] = temp_distance
                previous_nodes[neighbor] = current


def dfs(start, goal, code):
    visited = set([])
    paths = []

    def dfs_helper(current, goal, code):
        visited.add(current)
        hash_string = code + current[2]

        if (current[0], current[1]) == goal:
            paths.append(current[2].decode('ascii'))
            return

        for neighbor in get_neighbors(current[0], current[1], hash_string):
            neighbor = (neighbor[0], neighbor[1], current[2] + neighbor[2])

            if neighbor not in visited:
                dfs_helper(neighbor, goal, code)

    dfs_helper(start, goal, code)
    return len(sorted(paths, key=lambda x: -len(x))[0])


#for t in [test2, test3, test4]:
    #print(t[1] == find_path((0, 0, b''), (3, 3), t[0]))

print(find_path((0, 0, b''), (3, 3), code))

#for t in [test2, test3, test4]:
    #print(dfs((0, 0, b''), (3, 3), t[0]))

print(dfs((0, 0, b''), (3, 3), code))
