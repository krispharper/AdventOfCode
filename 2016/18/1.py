test1 = '..^^.'
test2 = '.^^.^.^^^^'
data = '.^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^'


def get_next_row(row):
    result = ''

    for i in range(len(row)):
        if i == 0:
            result += get_type('.', row[i], row[i + 1])
        elif i == len(row) - 1:
            result += get_type(row[i - 1], row[i], '.')
        else:
            result += get_type(row[i - 1], row[i], row[i + 1])

    return result


def get_type(l, c, r):
    if (l == c == '^' and r == '.') or (c == r == '^' and l == '.') or (c == r == '.' and l == '^') or (l == c == '.' and r == '^'):
        return '^'
    else:
        return '.'


def get_map(start, rows):
    result = [start]

    for _ in range(rows - 1):
        start = get_next_row(start)
        result.append(start)

    return result


def print_map(start, rows):
    for row in get_map(start, rows):
        print(row)


def count_safe(start, rows):
    return len([t for r in get_map(start, rows) for t in r if t == '.'])


#print_map(test2, 10)
#print(count_safe(test2, 10))

print(count_safe(data, 40))
print(count_safe(data, 400000))
