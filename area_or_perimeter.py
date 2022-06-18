def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)

# one line if else
def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2


# lambda function version
area_or_perimeter = lambda a, b : a * b if a == b else 2 * (a + b)
