def unique_in_order(string):
    out = string[0] + "".join("" if string[x] == string[x-1] else string[x] for x in range(1, len(string)))
    return list(out)
