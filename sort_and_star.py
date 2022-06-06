def get_char_code(element):
    result = []
    for i in list(element):
        result.append(ord(i))
    return result

def two_sort(array):
    first_item = sorted(array, key = get_char_code)[0]
    return "***".join(list(first_item))


# other solutions
def two_sort(array):
    return '***'.join(min(array))

# apparently sorted works directly with no key here
def two_sort(array):
    return '***'.join(sorted(array)[0])
