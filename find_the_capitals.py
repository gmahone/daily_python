def define_capital(char):
    return 64 < ord(char) < 91

def capitals(word):
    word_list = list(word)
    result = []
    for i in range(0, len(word_list)):
        if define_capital(word_list[i]):
            result.append(i)
    return result
