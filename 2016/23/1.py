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
            if y.isalpha():
                self.instruction_pointer += self.registers[ord(y) - 97]
            else:
                self.instruction_pointer += int(y)
        else:
            self.instruction_pointer += 1

    def toggle(self, x, data):
        index = self.registers[ord(x) - 97] + self.instruction_pointer
        self.instruction_pointer += 1

        if index > len(data) - 1:
            return

        if data[index].startswith('inc'):
            data[index] = data[index].replace('inc', 'dec')
        elif data[index].startswith('dec'):
            data[index] = data[index].replace('dec', 'inc')
        elif data[index].startswith('tgl'):
            data[index] = data[index].replace('tgl', 'inc')
        elif data[index].startswith('cpy'):
            data[index] = data[index].replace('cpy', 'jnz')
        elif data[index].startswith('jnz'):
            data[index] = data[index].replace('jnz', 'cpy')
        else:
            raise Exception

    def add(self, x, y):
        if y.isalpha():
            amount = self.registers[ord(y) - 97]
        else:
            amount = int(y)

        self.registers[ord(x) - 97] += amount
        self.instruction_pointer += 3

    def multiply(self, x, y, z):
        if y.isalpha():
            p1 = self.registers[ord(y) - 97]
        else:
            p1 = int(y)

        if z.isalpha():
            p2 = self.registers[ord(z) - 97]
        else:
            p2 = int(z)

        self.registers[ord(x) - 97] += p1 * p2
        self.instruction_pointer += 5

    def parse_instruction(self, s, data):
        if s.startswith('cpy'):
            m = re.search('cpy (.+) (.)', s)
            self.copy(*m.groups())
        elif s.startswith('inc'):
            m = re.search('inc (.+)', s)

            if (data[self.instruction_pointer + 1].startswith('dec') and
                    data[self.instruction_pointer + 2].startswith('jnz') and
                    data[self.instruction_pointer + 1][4] == data[self.instruction_pointer + 2][4]):
                m2 = re.search('dec (.+)', data[self.instruction_pointer + 1])

                if (data[self.instruction_pointer + 3].startswith('dec') and
                        data[self.instruction_pointer + 4].startswith('jnz') and
                        data[self.instruction_pointer + 3][4] == data[self.instruction_pointer + 4][4]):
                    m3 = re.search('dec (.+)', data[self.instruction_pointer + 3])
                    self.multiply(m.groups()[0], m2.groups()[0], m3.groups()[0])
                else:
                    self.add(m.groups()[0], m2.groups()[0])
            else:
                self.increment(m.groups()[0])
        elif s.startswith('dec'):
            m = re.search('dec (.+)', s)
            self.decrement(m.groups()[0])
        elif s.startswith('jnz'):
            m = re.search('jnz (.+) (.+)', s)
            self.jump(*m.groups())
        elif s.startswith('tgl'):
            m = re.search('tgl (.*)', s)
            self.toggle(m.groups()[0], data)
        else:
            raise Exception

    def process(self, data):
        while self.instruction_pointer < len(data):
            self.parse_instruction(data[self.instruction_pointer], data)
            self.count += 1

        print(self.count, self.instruction_pointer, self.registers)


test_data = [
    'cpy 2 a',
    'tgl a',
    'tgl a',
    'tgl a',
    'cpy 1 a',
    'dec a',
    'dec a'
]

#test_p = Process([0, 0, 0, 0])
#test_p.process(test_data)

with open('input.txt') as f:
    data = [line.strip() for line in f]

p = Process([7, 0, 0, 0])
p.process(data)

with open('input.txt') as f:
    data = [line.strip() for line in f]

p = Process([12, 0, 0, 0])
p.process(data)
