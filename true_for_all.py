def _all(seq, fun): 
    return all(map(fun, seq))


## solution using loop
def all(seq, fun): 
    for item in seq: 
        if not fun(item): 
            return False
    return True


## using list comprehension
def _all(seq, fun):
    return all([fun(x) for x in seq])
