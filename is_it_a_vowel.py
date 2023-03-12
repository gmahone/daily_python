def is_vowel(s): 
    if len(s) != 1:
        return False
    else:
        return s in 'aeiouAEIOU'
