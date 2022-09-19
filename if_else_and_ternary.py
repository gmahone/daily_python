def sale_hotdogs(n):
    if n >= 10:
        return 90*n
    elif n < 5:
        return 100*n
    else:
        return 95*n

# using ternary
def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)
