def filter_string(string):
    string_list = list(string)
    result = filter(isdigit, string_list)
    print(result)
    return 0
