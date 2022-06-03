def find_difference(a, b):
    vol_a = 1
    vol_b = 1
    for i in range(0, len(a)):
        vol_a *= a[i]
        vol_b *= b[i]
    return abs(vol_a - vol_b)


# other solutions

# solution using zip()
def find_difference(a, b):
    A = B = 1
    for i, j in zip(a, b):
        A *= i
        B *= j
    return abs(A - B)
