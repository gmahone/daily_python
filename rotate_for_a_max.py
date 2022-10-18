def max_rot(n):
    n = str(n)
    rot_list <- []
    print(n)
    for i in range(0,len(n)):
        rot_list.append(n[slice(i+1, len(n))] + n[i]))
        print(rot_list)
    pass
