def reverse_array(n):
    out = [None] * len(str(n))
    for i in range(1, len(str(n))+1):
        out[i-1] = int(str(n)[-i])
    return print(out)


reverse_array(12345)


#best solution
def digitize(n):
    return map(int, str(n)[::-1])

#second best
def digitize(n):
    return [int(x) for x in str(n)[::-1]]
