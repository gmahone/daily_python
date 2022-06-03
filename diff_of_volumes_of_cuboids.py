def find_difference(a, b):
    vol_a = reduce((lambda x, y: x * y), a)
    vol_b = reduce((lambda x, y: x * y), b)
    return abs(vol_a - vol_b)
