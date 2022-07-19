def repeat_it(string,n):
    result = string
    for i in range(1,n):
        result += string
    return result if isinstance(string, str) else "Not a string"
