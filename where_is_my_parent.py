def find_children(dancing_brigade):
    list_input = list(dancing_brigade.lower())
    list_input = sorted(list_input)
    tmp_list = []
    curr_item = list_input[1:2][0]
    for i in range(len(list_input)-1):
        tmp_current = list_input[i]
        tmp_next = list_input[i+1]
        if(tmp_current == tmp_next):
            curr_item += tmp_next
        else:
            tmp_list.append(curr_item)
            curr_item = tmp_next
    tmp_list.append(curr_item)
    print(tmp_list)
