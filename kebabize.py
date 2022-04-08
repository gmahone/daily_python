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
