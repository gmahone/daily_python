def max_rot(n):
    n = str(n)
    rot_list = [int(n)]
    for i in range(0,len(n)):
        after_index = n[i+1:]
        index_value = n[i:i+1]
        if i is not 0:
            before_index = n[:i]
        else:
            before_index = ""
        print("full n: {}".format(n))
        print("after_index: {}".format(after_index))
        print("index_value: {}".format(index_value))
        print("before_index: {}".format(before_index))
        n = before_index + after_index + index_value
        rot_list.append(int(n))
    return max(rot_list)
