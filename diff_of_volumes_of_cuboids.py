def find_difference(a, b):
    vol_a = 1
    vol_b = 1
    for i in range(0, len(a)):
        vol_a *= vol_a * a[i]
        vol_b *= vol_b * b[i]
    return abs(vol_a - vol_b)
