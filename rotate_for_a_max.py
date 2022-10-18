def max_rot(n):
    n = str(n)
    rot_list = []
    print(n)
    for i in range(0,len(n)):
        after_index = n[i+1:]
        index_value = n[i:i+1]
        before_index = n[:i-1]
        print(after_index)
        print(index_value)
        print(before_index)
        if i is not 0:
            tmp = n[:i-1] + tmp
    pass
