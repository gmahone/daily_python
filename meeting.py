def meeting(s):
    s_split = s.split(";")
    s_split = [i.split(':')[::-1] for i in s_split]
    s_split = list(map(lambda x: x[0] + "," + x[1], s_split))
    return sorted(s_split)
