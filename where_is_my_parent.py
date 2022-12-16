def find_children(dancing_brigade):
    list_input = list(dancing_brigade.lower())
    list_input = sorted(list_input)
    tmp_list = list_input[1:2][0]
    print(tmp_list)
    print("  ")
    for i in range(len(list_input)-1):
        tmp_current = list_input[i]
        print(tmp_current)
        tmp_next = list_input[i+1]
        print(tmp_next)
        print("  ")
    pass
