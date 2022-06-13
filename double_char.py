def double_char(s):
    output = []
    for x in list(s):
        output.append(x)
        output.append(x)
    return "".join(output)
