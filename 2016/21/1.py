import re


def swap(x, y):
    if x < y:
        return x, y
    else:
        return y, x


def swap_position(s, x, y):
    x, y = swap(x, y)
    return s[:x] + s[y] + s[x + 1:y] + s[x] + s[y + 1:]


def swap_letters(s, x, y):
    return swap_position(s, s.index(x), s.index(y))


def rotate_position(s, r, d):
    r = r % len(s)

    if d == 'left':
        return s[r:] + s[:r]
    else:
        return s[-r:] + s[:-r]


def rotate_letter(s, x):
    x_pos = s.index(x)

    if x_pos < 4:
        return rotate_position(s, x_pos + 1, "right")
    else:
        return rotate_position(s, x_pos + 2, "right")


def rotate_letter_backwards(s, x):
    temp = s

    while rotate_letter(temp, x) != s:
        temp = rotate_position(temp, 1, "left")

    return temp


def reverse(s, x, y):
    x, y = swap(x, y)
    return s[:x] + s[x:y + 1][::-1] + s[y + 1:]


def move_letter(s, x, y):
    if x < y:
        return s[:x] + s[x + 1:y + 1] + s[x] + s[y + 1:]
    else:
        return s[:y] + s[x] + s[y:x] + s[x + 1:]


def parse_instruction(s, instruction, undo=False):
    m1 = re.search("swap position (\d+) with position (\d+)", instruction)
    m2 = re.search("swap letter (.) with letter (.)", instruction)
    m3 = re.search("rotate (left|right) (\d+) step", instruction)
    m4 = re.search("rotate based on position of letter (.)", instruction)
    m5 = re.search("reverse positions (\d+) through (\d+)", instruction)
    m6 = re.search("move position (\d+) to position (\d+)", instruction)

    if m1:
        args = list(map(int, m1.groups()))
        return swap_position(s, *args)
    elif m2:
        return swap_letters(s, *m2.groups())
    elif m3:
        if undo:
            d = "left" if m3.groups()[0] == "right" else "right"
            return rotate_position(s, int(m3.groups()[1]), d)
        else:
            return rotate_position(s, int(m3.groups()[1]), m3.groups()[0])
    elif m4:
        if undo:
            return rotate_letter_backwards(s, m4.groups()[0])
        else:
            return rotate_letter(s, m4.groups()[0])
    elif m5:
        args = list(map(int, m5.groups()))

        if undo:
            return reverse(s, *reversed(args))
        else:
            return reverse(s, *args)
    elif m6:
        args = list(map(int, m6.groups()))
        if undo:
            return move_letter(s, *reversed(args))
        else:
            return move_letter(s, *args)
    else:
        print(instruction)
        raise Exception


def process(s, data):
    for d in data:
        s = parse_instruction(s, d)

    return s


def process_backwards(s, data):
    for d in reversed(data):
        s = parse_instruction(s, d, undo=True)

    return s


test_data = [
    "swap position 4 with position 0",
    "swap letter d with letter b",
    "reverse positions 0 through 4",
    "rotate left 1 step",
    "move position 1 to position 4",
    "move position 3 to position 0",
    "rotate based on position of letter b",
    "rotate based on position of letter d"
]

test_s = "abcde"

with open('input.txt') as f:
    data = [line.strip() for line in f]

s = "abcdefgh"
s2 = "fbgdceah"

print(process(s, data))
print(process_backwards(s2, data))
