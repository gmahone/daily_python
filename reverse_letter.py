def alpha_test(char):
    return char.isalpha()

def reverse_letter(string):
    alpha_only = list(filter(alpha_test, list(string)))
    return "".join(alpha_only[::-1])

# other solutions

# classic python formulaic method
def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]

# different filter formulation
def reverse_letter(string):
    return ''.join(filter(str.isalpha, reversed(string)))
