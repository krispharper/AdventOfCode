test1 = 'R2, L3'
test2 = 'R2, R2, R2'
test3 = 'R5, L5, R5, R3'
raw_data = 'L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2'


def distance(raw_data):
    data = raw_data.split(', ')

    distances = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    face = 'N'

    for d in data:
        if face == 'N':
            if d[0] == 'L':
                face = 'W'
            else:
                face = 'E'
        elif face == 'S':
            if d[0] == 'L':
                face = 'E'
            else:
                face = 'W'
        elif face == 'E':
            if d[0] == 'L':
                face = 'N'
            else:
                face = 'S'
        elif face == 'W':
            if d[0] == 'L':
                face = 'S'
            else:
                face = 'N'

        distances[face] += int(d[1:])

    location = calculate_location(distances)
    print(location)
    print(abs(location[0]) + abs(location[1]))


def calculate_location(distances):
    return distances['E'] - distances['W'], distances['N'] - distances['S']


for d in [test1, test2, test3, raw_data]:
    distance(d)
