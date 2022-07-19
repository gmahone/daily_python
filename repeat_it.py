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


def repeat_it(string,n):
    if type(string) is not str:
        return 'Not a string'
    return string * n

# lambda func version
repeat_it = lambda string, n: string*n if isinstance(string, str) else "Not a string"
