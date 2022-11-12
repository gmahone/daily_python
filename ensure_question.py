def ensure_question(s):
    return s if s[-1:] == "?" else "{}?".format(s)


# solution using rstrip
def ensure_question(s):
    return s.rstrip('?') + '?'

# using endswith
def ensure_question(s):
    return s if s.endswith('?') else s + '?'
