def reverse(lst):
    result = list()
    while len(lst) > 0:
        result.append(lst.pop(len(lst)-1))
        print(result)
    return result
