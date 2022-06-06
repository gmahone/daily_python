def get_char_code(element):
    return ord(element[0])

def two_sort(array):
    print(array.sort(key = get_char_code))
