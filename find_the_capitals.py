def define_capital(char):
    return 64 < ord(char) < 91

def capitals(word):
    word_list = list(word)
    result = []
    for i in range(0, len(word_list)):
        if define_capital(word_list[i]):
            result.append(i)
    return result


## other solutions

# using enumerate
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]

# similar solution using isupper
def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers
