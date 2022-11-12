def ensure_question(s):
    return s if s[-1:] == "?" else "{}?".format(s)
