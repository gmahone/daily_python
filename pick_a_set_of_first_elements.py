def first(seq, n):
    return seq[slice(0,n)] if n is not None else seq[slice(0,1)]
