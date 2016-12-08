with open('input.txt') as f:
    raw_data = [line.strip() for line in f]


def parse_data(raw_data):
    data = []

    for d in raw_data:
        good = []
        bad = []
        current = ""

        for c in d:
            if c == "[":
                good.append(current)
                current = ""
            elif c == "]":
                bad.append(current)
                current = ""
            else:
                current += c

        good.append(current)
        data.append((good, bad))

    return data


def is_valid(s):
    if len(s) < 4:
        return False

    for i in range(len(s)):
        if len(s[i:]) < 4:
            return False

        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
            return True


print(sum(any(map(is_valid, d[0])) and not any(map(is_valid, d[1])) for d in parse_data(raw_data)))
