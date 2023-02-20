def switcheroo(s):
    s = "_".join(s.split("a"))
    s = "a".join(s.split("b"))
    s = "b".join(s.split("_"))
    print(s)
    return s
