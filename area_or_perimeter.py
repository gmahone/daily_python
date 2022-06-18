def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)

# one line if else
def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2
