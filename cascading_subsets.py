def each_cons(lst, n):
    for i in range(0, len(lst) - n + 1):
        print(lst[i:i+n])
    pass
