def no_boring_zeros(n):
    if not n:
        return n
    elif n % 10:
        return n
    else:
        n = int(n/10)
        return no_boring_zeros(n)
