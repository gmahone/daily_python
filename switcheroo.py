def vowel_2_index(string):
    for vowel in "aeiou":
        while vowel in string:
            tmp_index = string.index(vowel) + 1
            print(tmp_index)
            string = string.replace(vowel, str(tmp_index), 1)
    pass
