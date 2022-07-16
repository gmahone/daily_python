import re

def is_digit(n):
    return len(n) & n.isdigit() & bool(re.search(n, "0123456789"))


def is_digit(n):
    print(n)
    return n.isdigit() & bool(len(n.strip()))

import re
def is_digit(n):
    return bool(re.search("[0-9]"))
                
                
import re
def is_digit(n):
    print(n);
    return bool(re.search(n, "^[0123456789]$")) & bool(len(n.strip()))

import re
def is_digit(n):
    print(n);
    return bool(re.search(n, "^[\W_][0123456789]*$")) & bool(len(n.strip()))


def is_digit(n):
    return n.isdigit() & len(n) == 1


import re

def is_digit(n):
    return bool(re.match("\d\Z", n))
