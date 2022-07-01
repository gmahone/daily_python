def string_clean(s):
    removeString = "123456789"
    for i in removeString:
        s = "".join(s.split(i))
    return s
