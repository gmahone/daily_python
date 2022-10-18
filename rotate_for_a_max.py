def max_rot(n):
    n = str(n)
    rot_list = []
    print(n)
    for i in range(0,len(n)):
        print(n[i+1:])
        print(n[i:i+1])
        tmp = n[i+1:] + n[i:i+1]
        if i is not 0:
            tmp = n[:i-1] + tmp
        print(tmp)
        n = tmp
    pass
