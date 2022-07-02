def meeting(s):
    s_split = s.split(";")
    s_split = [i.upper().split(':')[::-1] for i in s_split]
    s_split = list(map(lambda x: "(" + x[0] + ", " + x[1] + ")", s_split))
    return "".join(sorted(s_split))


# beatiful one-liner
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
