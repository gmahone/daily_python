def get_number_from_string(string):
    return int(''.join(c for c in string if c in '0123456789'))

# using isdigit
def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))


# using regex
import re

def get_number_from_string(s):
    return int(re.sub(r'\D', '', s))
