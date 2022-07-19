def repeat_it(string,n):
    if not isinstance(string, str):
        return "Not a string"
    result = string
    for i in range(1,n):
        result += string
    return result
