def digit_test(s):
    return s.isdigit()

def filter_string(string):
    string_list = list(string)
    result = filter(digit_test, string_list)
    print(result)
    return 0
