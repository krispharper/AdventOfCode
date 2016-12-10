with open('input.txt') as f:
    data = [line.strip() for line in f][0]


def parse_instructions(s):
    number_of_characters = ''
    repeat = ''
    index = 1

    while s[index] != 'x':
        number_of_characters += s[index]
        index += 1

    index += 1

    while s[index] != ')':
        repeat += s[index]
        index += 1

    number_of_characters = int(number_of_characters)
    repeat = int(repeat)
    index += 1

    return index, number_of_characters, repeat


def count_substring(s):
    if '(' not in s:
        return len(s)

    if not s.startswith('('):
        index = s.index('(')
        return count_substring(s[:index]) + count_substring(s[index:])

    index, number_of_characters, repeat = parse_instructions(s)
    return repeat * count_substring(s[index:index + number_of_characters]) + count_substring(s[index + number_of_characters:])


test1 = '(3x3)XYZ'
test2 = 'X(8x2)(3x3)ABCY'

test3 = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
test4 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

for t in [test1, test2, test3, test4, data]:
    print(count_substring(t))
