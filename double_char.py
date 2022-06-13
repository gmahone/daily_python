def double_char(s):
    output = []
    for x in list(s):
        if x not in output:
            output.append(x)
    return "".join(output)
