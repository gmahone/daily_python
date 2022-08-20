def shortcut(s):
    for i in list("aeiou"):
        s = "".join(s.split(i))
    return s


# solution using .translate()
def shortcut(s):
    return s.translate(None, 'aeiou')

# using "normal" python structure
def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')
