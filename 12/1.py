import re


class Process:
    def __init__(self, registers):
        self.registers = registers
        self.instruction_pointer = 0
        self.count = 0

    def copy(self, x, y):
        if x.isalpha():
            self.registers[ord(y) - 97] = self.registers[ord(x) - 97]
        else:
            self.registers[ord(y) - 97] = int(x)

        self.instruction_pointer += 1

    def increment(self, x):
        self.registers[ord(x) - 97] += 1
        self.instruction_pointer += 1

    def decrement(self, x):
        self.registers[ord(x) - 97] -= 1
        self.instruction_pointer += 1

    def jump(self, x, y):
        if (x.isdigit() and int(x)) or self.registers[ord(x) - 97]:
            self.instruction_pointer += int(y)
        else:
            self.instruction_pointer += 1

    def parse_instruction(self, s):
        if s.startswith('cpy'):
            m = re.search('cpy (.+) (.)', s)
            self.copy(*m.groups())
        elif s.startswith('inc'):
            m = re.search('inc (.+)', s)
            self.increment(m.groups()[0])
        elif s.startswith('dec'):
            m = re.search('dec (.+)', s)
            self.decrement(m.groups()[0])
        elif s.startswith('jnz'):
            m = re.search('jnz (.+) (.+)', s)
            self.jump(*m.groups())
        else:
            raise Exception

    def process(self, data):
        while self.instruction_pointer < len(data):
            self.parse_instruction(data[self.instruction_pointer])
            self.count += 1

        print(self.count, self.instruction_pointer, self.registers)


with open('input.txt') as f:
    data = [line.strip() for line in f]

test_data = [
    'cpy 41 a',
    'inc a',
    'inc a',
    'dec a',
    'jnz a 2',
    'dec a'
]

p = Process([0, 0, 0, 0])
p.process(data)

p = Process([0, 0, 1, 0])
p.process(data)
