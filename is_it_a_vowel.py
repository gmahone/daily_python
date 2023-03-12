def is_vowel(s): 
    if len(s) != 1:
        return False
    else:
        return s in 'aeiouAEIOU'

# solution using set
def is_vowel(s):
    return s.lower() in set("aeiou")
