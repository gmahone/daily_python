def meeting(s):
    s_split = s.split(";")
    s_split = [i.split(":") for i in s_split]
    print(s_split)
