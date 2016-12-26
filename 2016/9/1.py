with open('input.txt') as f:
    data = [line.strip() for line in f][0]


def process(data):
    output = ""
    i = 0

    while i < len(data):
        c = data[i]

        if c != '(':
            output += c
            i += 1
            continue

        number_of_characters = ''
        repeat = ''
        temp_index = i + 1

        while data[temp_index] != 'x':
            number_of_characters += data[temp_index]
            temp_index += 1

        temp_index += 1

        while data[temp_index] != ')':
            repeat += data[temp_index]
            temp_index += 1

        number_of_characters = int(number_of_characters)
        repeat = int(repeat)
        temp_index += 1
        output += data[temp_index:temp_index + number_of_characters] * repeat
        i = temp_index + number_of_characters

    return output


test1 = 'ADVENT'
test2 = 'A(1x5)BC'
test3 = '(3x3)XYZ'
test4 = 'A(2x2)BCD(2x2)EFG'
test5 = '(6x1)(1x3)A'
test6 = 'X(8x2)(3x3)ABCY'

for t in [test1, test2, test3, test4, test5, test6, data]:
    print(len(process(t)))
