def two_decimal_places(n):
    return round(n, 2)

## another way with full round
def two_decimal_places(n):
   return round(n * 100) / 100

# another solution with format
def two_decimal_places(n):
    return float("{0:.2f}".format(n))

