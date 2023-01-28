def explode(s):
    result = ""
    for i in s:
        result += i * int(i)
    return result
