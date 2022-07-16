import re

def is_digit(n):
    return len(n) & bool(re.search(n, "0123456789"))
