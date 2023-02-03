def solve(s):
    score_dict = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26
    }
    
    for vowel in "aeiou":
        s = s.replace(vowel, "_")
    
    s_list = s.split("_")
    
    result_list = []
    for consonant_group in s_list:
        score = [score_dict.get(consonant) for consonant in consonant_group]
        result_list.append(sum(score))
    return max(result_list)


# solution with ord
def solve(s):
    count = 0
    max = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in s:
        if letter in vowels:
            if count > max:
                max = count
            count = 0
        else:
            count+=int(ord(letter)) - 96
    return max
