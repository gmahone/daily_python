def define_capital(char):
    return 64 < ord(char) < 91

def capitals(word):
    word_list = filter(define_capital, list(word))
    return list(word_list)
    
