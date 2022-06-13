def double_char(s):
    output = []
    for x in list(s):
        output.append(x)
        output.append(x)
    return "".join(output)

# other solutions

# string multiplication solution
def double_char(s):
    return ''.join(c * 2 for c in s)

# another formulation of string multiplication
def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res
