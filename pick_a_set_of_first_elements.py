def first(seq, n=None):
    if n is None:
        return seq[slice(0,1)]
    else:
        return seq[slice(0,n)]

# simple solution
def first(seq, n=1): 
    return seq[:n]
# more explicit
def first(seq, n=1): 
    return seq[0:n]
