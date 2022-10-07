def first(seq, n):
    print(n)
    return seq[slice(0,n)] if n else seq[slice(0,1)]
