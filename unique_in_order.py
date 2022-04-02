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
