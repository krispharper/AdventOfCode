from hashlib import md5

def get_next_character(data, starting_number):
    while True:
        h = md5(data+str(starting_number).encode('ascii')).hexdigest()

        if h.startswith('00000'):
            return h[5], starting_number + 1

        starting_number += 1

data = b'cxdnnyjw'

password = ''
starting_number = 0

while len(password) < 8:
    c, starting_number = get_next_character(data, starting_number)
    password += c

print(password)
