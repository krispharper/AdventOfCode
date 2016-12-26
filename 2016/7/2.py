def parse_data(raw_data):
    data = []

    for d in raw_data:
        good = []
        bad = []
        current = ""

        for c in d:
            if c == "[":
                good += find_strings(current)
                current = ""
            elif c == "]":
                bad += find_strings(current)
                current = ""
            else:
                current += c

        good += find_strings(current)
        data.append((good, bad))

    return data


def find_strings(s):
    result = []

    for i in range(len(s)):
        if len(s[i:]) < 3:
            return result

        if s[i] != s[i + 1] and s[i] == s[i + 2]:
            result.append(s[i:i + 3])

    return result


def invert_string(s):
    return s[1] + s[0] + s[1]

with open('input.txt') as f:
    raw_data = [line.strip() for line in f]

print(sum(any(set.intersection(set(invert_string(s) for s in d[0]), set(d[1]))) for d in parse_data(raw_data)))
