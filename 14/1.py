from hashlib import md5


def get_repeated_character(s, length):
    for i in range(len(s) - length + 1):
        if len(set(s[i:i + length])) == 1:
            return s[i]

    return None


def set_hashes(hashes, number_of_hashings):
    for i in range(100000):
        s = salt + str(i).encode('ascii')

        for _ in range(number_of_hashings):
            s = md5(s).hexdigest().encode('ascii')

        hashes[i] = s.decode('ascii')


def find_index(salt, number_of_hashings):
    hashes = {}
    keys = set([])
    set_hashes(hashes, number_of_hashings)
    index = 0

    while(len(keys) < 64):
        c = get_repeated_character(hashes[index], 3)

        if c:
            for i in range(1000):
                if c * 5 in hashes[index + i + 1]:
                    keys.add(hashes[index])
        index += 1

    print(index - 1)


salt = b'ngcjuoqr'
#salt = b'abc'
find_index(salt, 1)
find_index(salt, 2017)
