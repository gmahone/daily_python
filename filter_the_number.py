def digit_test(s):
    return s.isdigit()

def filter_string(string):
    string_list = list(string)
    filter_string = filter(digit_test, string_list)
    result = int("".join(list(filter_string)))
    return result


## simple solution
def filter_string(string):
    return int(filter(str.isdigit, string))


## classic formulation
def filter_string(string):
    return int(''.join(a for a in string if a.isdigit()))
