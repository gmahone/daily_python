def string_clean(s):
    removeString = "0123456789"
    for i in removeString:
        s = "".join(s.split(i))
    return s
