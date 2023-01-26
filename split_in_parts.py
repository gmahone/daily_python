def split_in_parts(s, part_length):
    result = [s[n:n+part_length] for n in range(0,len(s),part_length)]
    print(result)
    pass
