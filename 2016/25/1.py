import re
from copy import deepcopy


class Process:
    def __init__(self, registers, data):
        self.registers = registers
        self.data = data
        self.instruction_pointer = 0
        self.output_list = []
        self.output_is_valid = True

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
        if (x.isalpha() and self.registers[ord(x) - 97]) or (x.isdigit() and int(x)):
            if y.isalpha():
                self.instruction_pointer += self.registers[ord(y) - 97]
            else:
                self.instruction_pointer += int(y)
        else:
            self.instruction_pointer += 1

    def toggle(self, x):
        index = self.registers[ord(x) - 97] + self.instruction_pointer
        self.instruction_pointer += 1

        if index > len(self.data) - 1:
            return

        if self.data[index].startswith('inc'):
            self.data[index] = self.data[index].replace('inc', 'dec')
        elif self.data[index].startswith('dec'):
            self.data[index] = self.data[index].replace('dec', 'inc')
        elif self.data[index].startswith('tgl'):
            self.data[index] = self.data[index].replace('tgl', 'inc')
        elif self.data[index].startswith('cpy'):
            self.data[index] = self.data[index].replace('cpy', 'jnz')
        elif self.data[index].startswith('jnz'):
            self.data[index] = self.data[index].replace('jnz', 'cpy')
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

    def output(self, x):
        if x.isalpha():
            self.output_list.append(self.registers[ord(x) - 97])
        else:
            self.output_list.append(x)

        print(self.output_list[-1], end='')
        self.set_output_is_valid()
        self.instruction_pointer += 1

    def set_output_is_valid(self):
        if len(self.output_list) == 1 and self.output_list[0] not in [0, 1]:
            self.output_is_valid = False
        elif len(self.output_list) > 1:
            if self.output_list[-1] != (1 - self.output_list[-2]):
                self.output_is_valid = False

    def parse_instruction(self, s):
        if s.startswith('cpy'):
            m = re.search('cpy (.+) (.)', s)
            self.copy(*m.groups())
        elif s.startswith('inc'):
            m = re.search('inc (.+)', s)

            if (self.data[self.instruction_pointer + 1].startswith('dec') and
                    self.data[self.instruction_pointer + 2].startswith('jnz') and
                    self.data[self.instruction_pointer + 1][4] == self.data[self.instruction_pointer + 2][4]):
                m2 = re.search('dec (.+)', self.data[self.instruction_pointer + 1])

                if (self.data[self.instruction_pointer + 3].startswith('dec') and
                        self.data[self.instruction_pointer + 4].startswith('jnz') and
                        self.data[self.instruction_pointer + 3][4] == self.data[self.instruction_pointer + 4][4]):
                    m3 = re.search('dec (.+)', self.data[self.instruction_pointer + 3])
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
            self.toggle(m.groups()[0])
        elif s.startswith('out'):
            m = re.search('out (.*)', s)
            self.output(m.groups()[0])
        else:
            raise Exception

    def process(self):
        while self.instruction_pointer < len(self.data) and self.output_is_valid:
            self.parse_instruction(self.data[self.instruction_pointer])


def try_output():
    for i in range(1, 1000):
        copy = deepcopy(data)
        print(i)
        p = Process([i, 0, 0, 0], copy)
        p.process()
        print()


with open('input.txt') as f:
    data = [line.strip() for line in f]

try_output()
