def find_children(dancing_brigade):
    list_input = list(dancing_brigade.lower())
    list_input = sorted(list_input)
    iter_list = zip(list_input, list_input[1 : ] + list_input[ : 1])
    iter_list = list(iter_list)
    iter_list.pop()
    print(iter_list)
    for thiselem,nextelem in zip(list_input, list_input[1 : ] + list_input[ : 1]):
        print(thiselem)
        print(nextelem)
        print("   ")
    return []
