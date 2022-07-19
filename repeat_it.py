def repeat_it(string,n):
    if not isinstance(string, str):
        return "Not a string"
    result = ""
    for i in range(0,n):
        result += string
    return result

# * works on strings
def repeat_it(string,n):
    return string * n if isinstance(string,str) else 'Not a string'
