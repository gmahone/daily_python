def each_cons(lst, n):
    result = []
    for i in range(0, len(lst) - n + 1):
        result.append(lst[i:i+n])
    return result


# single line func
def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]
