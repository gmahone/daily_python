def max_rot(n):
    n = str(n)
    rot_list = [int(n)]
    for i in range(0,len(n)):
        after_index = n[i+1:]
        index_value = n[i:i+1]
        before_index = ""
        if i is not 0:
            before_index = n[:i]
        n = before_index + after_index + index_value
        rot_list.append(int(n))
    return max(rot_list)
