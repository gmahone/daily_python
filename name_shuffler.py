def name_shuffler(str_):
    return " ".join(str_.split()[::-1])

# using reversed
def name_shuffler(s):
    return " ".join(reversed(s.split()))


# using explicit list
def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first
