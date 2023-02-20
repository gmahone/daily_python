def switcheroo(s):
    s = "_".join(s.split("a"))
    s = "a".join(s.split("b"))
    s = "b".join(s.split("_"))
    return s

# using translate
def switcheroo(s):
    return s.translate(str.maketrans('ab','ba'))

# using replace
def switcheroo(string):
    return ((string.replace('a','x')).replace('b','a')).replace('x','b')

# using a loop
def switcheroo(string):
    result = ''
    for letter in string:
        if letter == 'a':
            letter = 'b'
        elif letter == 'b':
            letter = 'a'
        result += letter
    return result
