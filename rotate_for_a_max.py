def max_rot(n):
    n = str(n)
    print(n)
    print([(n[slice(i+1, len(n))] + n[i]) for i in range(0,len(n))])
    pass
