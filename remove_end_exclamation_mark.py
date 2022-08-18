def remove(s):
    while s[-1] == "!":
        s = s[0:-1]
    return s


# using rstrip
def remove(s):
    return s.rstrip("!")
