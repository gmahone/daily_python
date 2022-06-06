def get_char_code(element):
    return ord(element[0])

def two_sort(array):
    first_item = sorted(array, key = get_char_code)[0]
    return "***".join(list(first_item))
