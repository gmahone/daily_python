def sum_str(a, b):
    int_a = 0
    int_b = 0
    if a is not "":
        int_a = int(a)
    if b is not "":
        int_b = int(b)
    return str(int_a+int_b)

# other solutions

# simple or solution
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

# different "" handling solution
def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))
