def first(seq, n=None):
    if n is None:
        return seq[slice(0,1)]
    else:
        return seq[slice(0,n)]
