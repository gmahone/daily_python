def switcheroo(s):
    s = "_".join(s.split("a"))
    s = "a".join(s.split("b"))
    s = "b".join(s.split("_"))
    return s

# using translate
def switcheroo(s):
    return s.translate(str.maketrans('ab','ba'))
