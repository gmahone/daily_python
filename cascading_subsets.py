def each_cons(lst, n):
    result = []
    for i in range(0, len(lst) - n + 1):
        result.append(lst[i:i+n])
    pass
