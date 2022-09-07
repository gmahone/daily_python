def uni_total(s):
    return sum([ord(i) for i in s])


# solution using map
def uni_total(string):
    return sum(map(ord, string))
