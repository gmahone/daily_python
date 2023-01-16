def vaporcode(s):
    word_list = s.split()
    letter_list = []
    for word in word_list:
        letter_list += list(word.upper())
    return "  ".join(letter_list)


# solution that replaces spaces
def vaporcode(s):
    return "  ".join(s.replace(" ", "").upper())


# loop over non-spaces
def vaporcode(s):
    return '  '.join(i.upper() for i in s if i!=' ')
