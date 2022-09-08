def reverse(lst):
    result = list()
    while len(lst) > 0:
        result.append(lst.pop(len(lst)-1))
    return result
