def kebabize(string):
    result = ""
    for i in string:
        if not i.isalpha():
            next
        elif i.isupper():
            if result == "":
                result += (i.lower())
            else:
                result += ("-" + i.lower())
        else:
            result += i
    return result


# other solutions

def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

def kebabize(string):
    result = ""
    for c in string:
        if c.isupper():
            if result is not "":
                result += "-{}".format(c.lower())
            else:
                result += c.lower()
        if c.islower():
            result += c
    return result


def kebabize(string):
    a = ''
    for i in string:
        if i.isupper():
            a += '-' + i.lower()
        if i.islower():
            a += i
    return a.strip('-')
