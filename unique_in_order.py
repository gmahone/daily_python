# def unique_in_order(string):
#     out = string[0] + "".join("" if string[x] == string[x-1] else string[x] for x in range(1, len(string)))
#     return list(out)

def unique_in_order(iterable):
    if not len(iterable):
        return []
    out = [iterable[0]]
    for x in range(1, len(iterable)):
        if iterable[x] != iterable[x-1]:
            out.append(iterable[x])
    return out

# other solutions

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]


def unique_in_order(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r


