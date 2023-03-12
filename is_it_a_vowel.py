def is_vowel(s): 
    if len(s) != 1:
        return False
    else:
        return s in 'aeiouAEIOU'

# solution using set
def is_vowel(s):
    return s.lower() in set("aeiou")


#using regexp
import re
def is_vowel(s): 
    regex = r'^[aeiou]{1}$'
    return bool(re.match(regex, re.escape(s), re.IGNORECASE))

# another regex solution
import re

def is_vowel(stg): 
    return bool(re.fullmatch(r"[aeiou]", stg, re.I))
