def explode(s):
    result = ""
    for i in s:
        result += i * int(i)
    return result


# add join solution
def explode(s):
    return ''.join(c * int(c) for c in s)
