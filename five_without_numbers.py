def unusual_five():
    return ["", "", "", "", "", "a"].index("a")


# via len()
def unusual_five():
    return len("aaaaa")

# add solution using ord()
def unusual_five():
    return ord("")

# lambda solution using len
unusual_five = lambda: len("aaaaa")
