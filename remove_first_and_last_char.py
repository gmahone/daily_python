def remove_first_and_last_char(x):
    return x[1:(len(x)-1)]

test = "title"
print(remove_first_and_last_char(test))


# other solutions
def remove_char(s):
    return s[1 : -1]

remove_char=lambda s: s[1:-1]

def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)
