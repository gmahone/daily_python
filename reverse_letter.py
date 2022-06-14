def alpha_test(char):
    return char.isalpha()

def reverse_letter(string):
    alpha_only = filter(alpha_test, list(string))
    return "".join(alpha_only[::-1])
