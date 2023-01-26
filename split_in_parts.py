def split_in_parts(s, part_length):
    result = [s[n:n+part_length] for n in range(0,len(s),part_length)]
    return " ".join(result)


# single line
def split_in_parts(s, n): 
    return ' '.join([s[i:i+n] for i in range(0, len(s), n)])
