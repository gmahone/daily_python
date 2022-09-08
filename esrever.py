def reverse(lst):
    result = list()
    while len(lst) > 0:
        result.append(lst.pop(len(lst)-1))
    return result

## no need to specify pop index
def reverse(lst):
    result = list()
    while lst:
        result.append(lst.pop())
    return result
