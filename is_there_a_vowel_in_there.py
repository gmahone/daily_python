def is_vow(inp):
    vowel_dict = {"a":97,
                  "e":101,
                  "i":105,
                  "o":111,
                  "u":117}
    
    for vowel, charcode in vowel_dict.items():
        while charcode in inp:
            inp[inp.index(charcode)] = vowel
    return inp


# solution using chr()
def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]
