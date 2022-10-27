def solution(value):
    result = f"Value is {value:05}"
    return result


# alternative solution
def solution(value):
    return "Value is %05d" % value


# add another alternative
def solution(value):
    return "Value is {:05}".format(value)
