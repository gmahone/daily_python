def alternate_case(s):
    return s.swapcase()

# loop solution
def alternateCase(s):
    return ''.join(c.upper() if c.islower() else c.lower() for c in s)
