def split_and_merge(string_, separator):
    words = string_.split(" ")
    result = " ".join([separator.join(list(c)) for c in words])        
    return result

# shorter solution
def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())
