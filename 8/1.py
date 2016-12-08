with open('input.txt') as f:
    raw_data = [line.strip() for line in f]

screen_width = 50
screen_height = 6
screen = [[0] * screen_height for _ in range(screen_width)]


def print_screen():
    for y in range(screen_height):
        for x in range(screen_width):
            if screen[x][y] == 0:
                print('.', end='')
            else:
                print('#', end='')

        print()

    print()


def create_rectangle(x, y):
    for i in range(x):
        for j in range(y):
            screen[i][j] = 1


def rotate_row(row, amount):
    copy_row = list(screen[_][row] for _ in range(screen_width))

    for i in range(screen_width):
        screen[(i + amount) % screen_width][row] = copy_row[i]


def rotate_column(column, amount):
    copy_column = list(screen[column])

    for i in range(screen_height):
        screen[column][(i + amount) % screen_height] = copy_column[i]

def parse_instruction(instruction):
    if instruction.startswith("rect"):
        index = instruction.index('x')
        width = int(instruction[5:index])
        height = int(instruction[index + 1:])
        create_rectangle(width, height)
    elif instruction.startswith("rotate row"):
        index = instruction.index(" by ")
        row = int(instruction[13:index])
        amount = int(instruction[index + 4:])
        rotate_row(row, amount)
    elif instruction.startswith("rotate column"):
        index = instruction.index(" by ")
        column = int(instruction[16:index])
        amount = int(instruction[index + 4:])
        rotate_column(column, amount)
    else:
        raise Exception


for line in raw_data:
    parse_instruction(line)

print(sum(x for y in screen for x in y))
print_screen()
