def find_children(dancing_brigade):
    if not len(dancing_brigade):
        return ""
    list_input = list(dancing_brigade.lower())
    list_input = sorted(list_input)
    tmp_list = []
    curr_item = list_input[0:1][0]
    for i in range(len(list_input)-1):
        print(curr_item)
        tmp_current = list_input[i]
        tmp_next = list_input[i+1]
        if(tmp_current == tmp_next):
            curr_item += tmp_next
        else:
            tmp_list.append(curr_item)
            curr_item = tmp_next
    tmp_list.append(curr_item)
    tmp_title = " ".join(tmp_list).title()
    result = "".join(tmp_title.split(" "))
    return result
