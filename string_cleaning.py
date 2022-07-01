def string_clean(s):
    removeString = "0123456789"
    for i in removeString:
        s = "".join(s.split(i))
    return s


# using isdigit()
def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())
