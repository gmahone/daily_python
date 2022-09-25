def get_real_floor(n):
    return n-2 if n > 13 else n-1 if n > 0 else n

# standard if case solution
def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2
