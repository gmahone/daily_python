def vowel_2_index(string):
    result = string
    for vowel in "aeiouAEIOU":
        while vowel in string:
            tmp_index = string.index(vowel) + 1
            string = string.replace(vowel, "x", 1)
            result = result.replace(vowel, str(tmp_index), 1)
    return result


# short solution with enumerate
def vowel_2_index(string):
    vowels = 'aeiouAEIOU'
    return ''.join(x if x not in vowels else str(n + 1) for n,x in enumerate(string))
