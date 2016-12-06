from hashlib import md5

def get_next_character(data, starting_number):
    while True:
        h = md5(data+str(starting_number).encode('ascii')).hexdigest()

        if h.startswith('00000'):
            return h[5], h[6], starting_number + 1

        starting_number += 1

data = b'cxdnnyjw'

password = ['_'] * 8
starting_number = 0

while '_' in password:
    pos, c, starting_number = get_next_character(data, starting_number)
    if pos.isdigit() and int(pos) < 8 and password[int(pos)] == '_':
        password[int(pos)] = c
        print("".join(password))

print("".join(password))
