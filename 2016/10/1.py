import re


def parse_input(s, remaining_instructions):
    if s.startswith('value'):
        value_match = re.match("value (\d+) goes to bot (\d+)", s)
        add_value(int(value_match.groups()[1]), int(value_match.groups()[0]))
        return

    bot_match = re.match("bot (\d+)", s)
    bot = int(bot_match.groups()[0])

    if not is_full(bot):
        remaining_instructions.append(s)
        return

    m1 = re.search("gives low to output (\d+) and high to output (\d+)", s)
    m2 = re.search("gives low to output (\d+) and high to bot (\d+)", s)
    m3 = re.search("gives low to bot (\d+) and high to output (\d+)", s)
    m4 = re.search("gives low to bot (\d+) and high to bot (\d+)", s)

    if m1:
        args = list(map(int, m1.groups()))
        remove_low_value(bot, args[0])
        remove_high_value(bot, args[1])
    elif m2:
        args = list(map(int, m2.groups()))
        remove_low_value(bot, args[0])
        transfer_high(bot, args[1])
    elif m3:
        args = list(map(int, m3.groups()))
        remove_high_value(bot, args[1])
        transfer_low(bot, args[0])
    elif m4:
        args = list(map(int, m4.groups()))
        transfer_low(bot, args[0])
        transfer_high(bot, args[1])


def add_value(bot, value):
    if bot in state:
        if state[bot][0] != 0:
            test_for_success(bot, state[bot][0], value)

            if state[bot][0] > value:
                state[bot] = (value, state[bot][0])
            else:
                state[bot] = (state[bot][0], value)
        else:
            test_for_success(bot, state[bot][1], value)

            if state[bot][1] > value:
                state[bot] = (value, state[bot][0])
            else:
                state[bot] = (state[bot][0], value)
    else:
        state[bot] = (value, 0)


def clear_low_value(bot):
    state[bot] = (0, state[bot][1])


def clear_high_value(bot):
    state[bot] = (state[bot][0], 0)


def remove_low_value(bot, output):
    if output in outputs:
        outputs[output].append(state[bot][0])
    else:
        outputs[output] = state[bot][0]

    clear_low_value(bot)


def remove_high_value(bot, output):
    if output in outputs:
        outputs[output].append(state[bot][1])
    else:
        outputs[output] = state[bot][1]

    clear_high_value(bot)


def transfer_low(from_bot, to_bot):
    add_value(to_bot, state[from_bot][0])
    clear_low_value(from_bot)


def transfer_high(from_bot, to_bot):
    add_value(to_bot, state[from_bot][1])
    clear_high_value(from_bot)


def is_full(bot):
    return bot in state and state[bot][0] != 0 and state[bot][1] != 0


def test_for_success(bot, v1, v2):
    if min(v1, v2) == 17 and max(v1, v2) == 61:
        print("Bot {0} is the answer".format(bot))


def process_list(l):
    remaining_instructions = []

    for i in l:
        parse_input(i, remaining_instructions)

    return remaining_instructions


def process(data):
    while data:
        data = process_list(data)


with open('input.txt') as f:
    data = [line.strip() for line in f]

state = {}
outputs = {}

test_data = [
    'value 5 goes to bot 2',
    'bot 2 gives low to bot 1 and high to bot 0',
    'value 3 goes to bot 1',
    'bot 1 gives low to output 1 and high to bot 0',
    'bot 0 gives low to output 2 and high to output 0',
    'value 2 goes to bot 2'
]

process(data)
print(outputs[0] * outputs[1] * outputs[2])
